# hazon-2022 · author · run 43082448402

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (39.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/32d67ad6-7c84-45d8-af3f-b809b1f0fb01/tool-results/b90casu6b.txt

Preview (first 2KB):
Wed Nov 11 19:00:49 UTC 2026
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/32d67ad6-7c84-45d8-af3f-b809b1f0fb01/tool-results/b90casu6b.txt"
}
```

```
1	Wed Nov 11 19:00:49 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-14`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 678 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/hazon-2022.yaml; ls paper; cat papers/datasets/hazon-2022.yaml
```

```
<persisted-output>
Output too large (56.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/32d67ad6-7c84-45d8-af3f-b809b1f0fb01/tool-results/bw8b29le2.txt

Preview (first 2KB):
# Claims for Hazon, Minces, Tomàs, Ganguli, Schnitzer & Jercog (2022), Nature Communications 13,
# 4276, doi:10.1038/s41467-022-31254-y, tested on CRCNS hc-30.
#
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
# protocol as stated in docs/protocol.md (version pilot-14), reader role. The dataset's data were
# not looked at; only its title and its data descriptor (paper/hc-30.data-description.txt) were read.
#
# Text read: the version of record, open access in PMC (PMC9314334), full text from Europe PMC
# (JATS XML flattened): main text, figure legends and Methods; and the Supplementary Information
# (41467_2022_31254_MOESM1_ESM.pdf, Supplementary Figures 1 to 19 and Supplementary Tables 1 and 2),
# as text, with the PDF for the tables. The Source Data file and the Reporting Summary were not
# read; no claim rests on them.
#
# Code read: github.com/approbatory/ML-project, commit 2057af9facfd3035c573e1254bdc32ed4781ba60
# (2022-06-07), linked from Code availability. MATLAB. It holds the event detection
# (utils/hyperdetect.m, supfigs_code/events_converter.mlx), the trial selection, activity tensor,
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/32d67ad6-7c84-45d8-af3f-b809b1f0fb01/tool-results/bw8b29le2.txt"
}
```

```
1	# Claims for Hazon, Minces, Tomàs, Ganguli, Schnitzer & Jercog (2022), Nature Communications 13,
2	# 4276, doi:10.1038/s41467-022-31254-y, tested on CRCNS hc-30.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol as stated in docs/protocol.md (version pilot-14), reader role. The dataset's data were
6	# not looked at; only its title and its data descriptor (paper/hc-30.data-description.txt) were read.
7	#
8	# Text read: the version of record, open access in PMC (PMC9314334), full text from Europe PMC
9	# (JATS XML flattened): main text, figure legends and Methods; and the Supplementary Information
10	# (41467_2022_31254_MOESM1_ESM.pdf, Supplementary Figures 1 to 19 and Supplementary Tables 1 and 2),
11	# as text, with the PDF for the tables. The Source Data file and the Reporting Summary were not
12	# read; no claim rests on them.
13	#
14	# Code read: github.com/approbatory/ML-project, commit 2057af9facfd3035c573e1254bdc32ed4781ba60
15	# (2022-06-07), linked from Code availability. MATLAB. It holds the event detection
16	# (utils/hyperdetect.m, supfigs_code/events_converter.mlx), the trial selection, activity tensor,
17	# trial shuffle, two-fold decoding and signal and noise measures (DecodeTensor.m), the SVM decoders
18	# (decoding/my_algs.m), the IMSE fit (createFit_infoSaturation.m, PanelGenerator.m), the noise
19	# eigenvector analyses (@Cloud), the per-session and per-animal quantities and correlations (@Org),
20	# the session lists (SessManager.m), and live scripts behind most published numbers
[... 902 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/hc-30.data-description.txt; sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls -R entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150
```

```
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^findings/,$p' attempts/fouke-2025-01.yaml | head -60; cat entries/fouke-2025/README.md | head -30; python -c "import json;nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'));print([ (c['cell_type'],c['metadata'].get('tags'),''.join(c['source'])[:80]) for c in nb['cells'][:12]])"
```

```
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
    file of its stimulus software.
- kind: code_mismatch
  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
    while its conversion of the stimulus software's names gives the reverse (it carries a remap
    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
    only if the fish turn with lateral motion.
- kind: metadata_error
  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
    only Danio rerio; the files hold 37 fish of two species.
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l README.md docs/design.md; head -60 docs/design.md; ls schemas tools; date -u
```

```
139 README.md
  271 docs/design.md
  410 total
# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.

## Goal

Agents work through the dandisets on the DANDI Archive that have an associated
paper. For each one, an agent tries to reproduce the paper's key findings and
figures from the open data, writes the analysis as a notebook, and registers it
here. People can deposit too, but most deposits are expected to come from
agents.

This serves two purposes:

1. **Check the data.** A finding that can be reproduced shows the dandiset is
   complete and accurate enough to support it. A finding that cannot be
   reproduced, with the reason, tells the data owner and the archive what is
[... 86 more lines not kept]
```

**Agent**

Now list the dataset files on S3.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=hc-30/" | python -c "import sys,re;t=sys.stdin.read();print(re.findall(r'<Key>(.*?)</Key><LastModified>(.*?)</LastModified><ETag>(.*?)</ETag><Size>(.*?)</Size>',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=hc-30/" | head -c 3000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-30/live; curl -s $B/checksums.md5; echo; curl -s $B/filelist.txt; which python; python -c "import scipy,fsspec,h5py,numpy,sklearn;print(scipy.__version__,numpy.__version__,sklearn.__version__)"; nproc; free -g
```

```
3c3e0d67784a84430b62e2a2c65922eb  docs/crcns_hc-30_data_description.docx
320d157fbcc43be385485cc186842636  docs/crcns_hc-30_data_description.pdf
fe0f5dd2fca6d64dbf0cd3f35e31e1f0  event_traces.mat
2c89f46e4851b4c4d60beb7950362fb5  filelist.txt

# CRCNS.org 'hc-30' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 docs/crcns_hc-30_data_description.docx	21098 (20.6 KB)
 docs/crcns_hc-30_data_description.pdf	48537 (47.3 KB)
 event_traces.mat	142350100 (135.7 MB)
 checksums.md5	243
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import scipy,fsspec,h5py,numpy,sklearn;print(scipy.__version__,numpy.__version__,sklearn.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'scipy'
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q numpy scipy fsspec aiohttp requests h5py scikit-learn pandas matplotlib statsmodels jupyter nbconvert ipykernel 2>&1 | tail -3; python -c "import scipy,sklearn;print(scipy.__version__,sklearn.__version__)"
```

```
1.18.1 1.9.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > peek.py <<'EOF'
import fsspec, io, time, scipy.io, h5py
t=time.time()
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-30/live/event_traces.mat"
with fsspec.open(url, block_size=2**22) as f:
    head=f.read(128); print(head[:116])
    f.seek(0); b=f.read()
print(len(b), time.time()-t)
import hashlib; print(hashlib.md5(b).hexdigest())
import pickle; open('raw.mat','wb').write(b)  # dev cache only
EOF
python peek.py
```

```
b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Thu Jun 30 13:47:55 2022                                        '
142350100 4.15219521522522
fe0f5dd2fca6d64dbf0cd3f35e31e1f0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > peek2.py <<'EOF'
import scipy.io, numpy as np, time
t=time.time()
m=scipy.io.loadmat('raw.mat', squeeze_me=True, struct_as_record=False)
print(time.time()-t, [k for k in m if not k.startswith('__')])
E=m['event_traces']; print(type(E), E.shape)
e=E[0]; print(e._fieldnames)
for e in E[:3]:
    print(e.mouse_name, e.session_ID, type(e.traces), e.traces.shape, e.traces.nnz, e.position.shape, e.position.dtype, np.nanmin(e.position), np.nanmax(e.position), np.isnan(e.position).sum())
    tr=e.traces.tocsc(); d=tr.data; print(' vals', d.min(), d.max(), np.percentile(d,[5,50,95]))
    col=tr[:,0].toarray().ravel(); nz=np.nonzero(col)[0]; print(' col0 first nz', nz[:20], col[nz[:20]])
import collections
print(collections.Counter(str(e.mouse_name) for e in E))
ns=[e.traces.shape[1] for e in E]; print(len(ns), sum(ns), np.median(ns), min(ns), max(ns))
print([str(e.session_ID) for e in E][:20])
EOF
python peek2.py
```

```
0.6402115821838379 ['event_traces']
<class 'numpy.ndarray'> (110,)
['mouse_name', 'session_ID', 'traces', 'position']
Mouse2023 124240 <class 'scipy.sparse._csc.csc_array'> (36078, 188) 52036 (36078,) float64 45.51285067363833 724.7909574486926 0
 vals 0.06442713017605253 11.411425170793715 [0.20351438 0.3943514  1.2174646 ]
 col0 first nz [ 229  316  670 2286 2990 3424 3592 3795 3807 4521 4585 5003 5708 6627
 6677 6845 6891 7014 7178 7985] [0.29968411 0.24316269 0.25805817 0.32680524 0.32225337 0.50494142
 0.28595581 0.33129916 0.77693164 0.34314807 0.25831829 0.45916154
 0.40609775 0.31018636 0.23444984 0.35396139 1.21089411 0.39797373
 0.28223883 0.22755587]
Mouse2023 091246 <class 'scipy.sparse._csc.csc_array'> (36098, 193) 63420 (36098,) float64 48.336076775513874 719.7096211332844 0
 vals 0.0669399261508815 9.431010352474027 [0.18719516 0.37561354 1.15853434]
 col0 first nz [ 1987  5600  6303  6737  7200  7360  7657  7986  8453  8789  8929  9117
  9228 10112 10172 10292 10429 10783 10906 11358] [0.27710446 0.40187073 0.3902613  0.22340074 0.21747631 0.42991518
 0.23881181 0.73332673 0.56114251 0.42740502 0.3566361  0.3148165
 0.28690223 0.31918407 0.24955276 0.2955437  0.33698057 0.33973008
 0.29864134 0.33421195]
Mouse2023 114832 <class 'scipy.sparse._csc.csc_array'> (36005, 178) 53129 (36005,) float64 48.2312881334352 718.6020658562229 0
 vals 0.05894908782608331 11.382034254631852 [0.18647868 0.36595057 1.16429908]
 col0 first nz [ 264  589 1079 1447 1570 1855 2695 2990 3312 4087 4358 4578 5036 5688
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "methods\|preprocessing\|alpha\|convol" paper/10.1038-s41467-022-31254-y.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-022-31254-y.txt",
 "offset": 103,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && git clone -q https://github.com/approbatory/ML-project.git mlp 2>&1 | tail -2; cd mlp && git checkout -q 2057af9facfd3035c573e1254bdc32ed4781ba60 && git log -1 --format='%H %cd' && ls
```

```
Wed Nov 11 19:02:07 UTC 2026
2057af9facfd3035c573e1254bdc32ed4781ba60 Tue Jun 7 19:24:56 2022 -0700
15pix_separation_decoding.db
2s_pad_decoding.db
@Calc
@Cloud
@Org
Analyzer.m
Asymp_ratio_new.xlsx
Asymp_snr.xlsx
Asymp_snr_per_single_snr.xlsx
Asymp_snr_shuf.xlsx
DS_README.md
DecodeTensor.m
DecodingPlotGenerator.m
EvalSettings.m
Fitted_N.xlsx
I0N_ratio.xlsx
IMSE_ratio_at_150.xlsx
MultiSessionVisualizer.m
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; grep -n "function\b" DecodeTensor.m | head -80; sed -n 85,105p SessManager.m
```

```
3:        function dispatch(dispatch_index, padded, distance_cutoff)
4:            %Dispatching decoding as a function of number of cells using
21:        function dispatch_filt(dispatch_index, data_type)
31:        function dispatch_datasize_filt(dispatch_index, data_type)
41:        function decode_series(source_path, mouse_id, opt)
42:            %%Decoding performance as a function of number of neurons
61:            % they are not entered in this function to allow this function
160:        function opt = default_opt
170:            %       function of size of ensemble (30)
200:        function [source_path, mouse_name, session_id] = default_datasets(index, pref)
225:        function id = qid(indices)
232:        function [source_path, mouse_name] = default_datasets_OLD(index)
257:        function [T, d, cell_coords] = tensor_loader(source_path, mouse_id, opt)
390:        function results_table = adjacent_metrics(data_tensor, tr_dir, num_neurons, num_trials, no_decoding)
488:        function [noise_var, noise_var_s, noise_var_d, m2, m2_s, m2_d, mean_dist2]...
580:        function err_res = decode_all(data_tensor, tr_dir, binsize, alg, num_neurons, num_trials, no_dir_shuf)
634:        function [mean_err, MSE, ps, ks, model, stats] = decode_tensor(data_tensor, tr_dir,...
744:        function [cpp, vel, trial_start, trial_end,...
790:        function [cpp, vel, trial_start, trial_end,...
932:            %function for converting pixel valued position to place bin index
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 257,390p DecodeTensor.m; sed -n 744,1060p DecodeTensor.m
```

```
function [T, d, cell_coords] = tensor_loader(source_path, mouse_id, opt)
            %%Load data tensor from file, from path and name of the mouse
            % uses opt struct for options
            % opt.neural_data_type = 'rawTraces' OR 'rawProbs' OR
            %   'spikeDeconv'
            % opt.n_bins = number of bins to use, e.g. 20
            
            
            load(source_path);
            
            [~,w_] = fileparts(source_path);
            if strcmp(w_, 'Mouse-2026-20150329_115639-linear-track-TracesAndEvents')
                % special_74_cut_350 = true;
%                 tracesEvents.position = tracesEvents.position(351:end,:);
%                 tracesEvents.velocity = tracesEvents.velocity(351:end,:);
%                 tracesEvents.rawProb = tracesEvents.rawProb(351:end,:);
%                 tracesEvents.rawTraces = tracesEvents.rawTraces(351:end,:);
%                 tracesEvents.zTraces = tracesEvents.zTraces(351:end,:);
%                 tracesEvents.zProb = tracesEvents.zProb(351:end,:);
%                 tracesEvents.tresholdEvents = tracesEvents.tresholdEvents(351:end,:);
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 41,200p DecodeTensor.m; sed -n 580,744p DecodeTensor.m; sed -n 1053,1200p DecodeTensor.m
```

```
function decode_series(source_path, mouse_id, opt)
            %%Decoding performance as a function of number of neurons
            % in three settings: unshuffled, shuffled, and diagonal
            % The shuffled setting is when the training and testing sets
            % are both shuffled.
            % The diagonal setting is when the learning model is
            % insensitive to correlations (e.g. naive Bayes models, or any
            % model where the training data is trial shuffled prior to
            % learning)
            % saves records into a file containing the following fields:
            % Mouse (representing mouse ID)
            % Setting (representing either 'unshuffled', 'shuffled', or
            %       'diagonal')
            % NumNeurons (number of neurons used for decoding)
            % DataSize (number of trials [of each direction] used for
            %       decoding)
            % MeanErrors (absolute mean error of decoding)
            % MSE (Mean squared error of decoding)
            %
            % These records are later entered into a SQLite database
[... 454 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; grep -n -A12 "ecoclin" decoding/my_algs.m | head -40; sed -n 390,500p DecodeTensor.m
```

```
64:ecoclin = struct('name', 'pairwise ECOC SVM', 'pre', ecoc_pre, 'train', ecoc_trainlin, 'test', ecoc_test, 'short', 'pSVM');
65:ecoclin_onevsall = struct('name', '1 vs. others ECOC SVM', 'pre', ecoc_pre, 'train', ecoc_trainlin_onevsall, 'test', ecoc_test, 'short', '1SVM');
66-ecoc_binarized = struct('name', 'ECOC SVM binarized\_input', 'pre', ecoc_pre_binarized, 'train', ecoc_train, 'test', ecoc_test, 'short', 'bin pSVM');
67:ecoclin_binarized = struct('name', 'ECOC SVM lin binarized\_input', 'pre', ecoc_pre_binarized, 'train', ecoc_trainlin, 'test', ecoc_test, 'short', 'bin pSVM');
68-
69-linsvm = struct('name', 'lin SVM', 'pre', @(x)x, 'train', linsvm_train, 'test', linsvm_test, 'short', 'SVM');
70-
71-if ~exist('settings', 'var')
72-    settings = 'original';
73-end
74-if ~exist('all2all', 'var')
75-    all2all = true;
76-end
77-
78-if ~iscell(names)
79-    names = {names};
--
120:            case 'ecoclin'
121:                alg = ecoclin;
122:            case 'ecoclin_onevsall'
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 1,63p decoding/my_algs.m | grep -n "ecoc\|linsvm\|template" ; cat signal_and_noise_analysis.m | head -80
```

```
22:ecoc_pre = @(X) X;
23:ecoc_pre_binarized = @(X) double(X ~= 0);
24:t = templateSVM('Standardize',1,'KernelFunction','linear');
25:t2 = templateSVM('Standardize',1,'KernelFunction','polynomial', 'PolynomialOrder', 2);
31:tlin = templateLinear('Learner', 'svm',...
40:linsvm_train = @(X_train, ks_train) fitclinear(X_train, ks_train, 'Learner', 'svm',...
43:linsvm_test = @(model, X_test) predict(model, X_test);
45:ecoc_train = @(X_train, ks_train) fitcecoc(X_train, ks_train, 'Learners', t);
46:ecoc_train2 = @(X_train, ks_train) fitcecoc(X_train, ks_train, 'Learners', t2);
47:ecoc_trainlin = @(X_train, ks_train) fitcecoc(X_train, ks_train, 'Learners', tlin);
48:ecoc_trainlin_onevsall = @(X_train, ks_train) fitcecoc(X_train, ks_train, 'Coding', 'onevsall', 'Learners', tlin);
49:ecoc_test = @(model, X_test) predict(model, X_test);
62:ecoc = struct('name', 'ECOC SVM', 'pre', ecoc_pre, 'train', ecoc_train, 'test', ecoc_test, 'short', 'pSVM');
63:ecoc2 = struct('name', 'ECOC SVM quadratic', 'pre', ecoc_pre, 'train', ecoc_train2, 'test', ecoc_test, 'short', 'QSVM');
recompute = false;

%load adjacent_metrics_agg_191202-163306_0.mat
%load adjacent_metrics_agg_200801-184941_0.mat
%load adjacent_metrics_HD_gamma_agg_210622-180228_0.mat
load adjacent_metrics_events_transients_agg_210707-152508_0.mat
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 24,44p decoding/my_algs.m; cat error_trial_counter.m; cat estimate_position_jitter.m | head -80
```

```
t = templateSVM('Standardize',1,'KernelFunction','linear');
t2 = templateSVM('Standardize',1,'KernelFunction','polynomial', 'PolynomialOrder', 2);
if ~exist('Lambda', 'var')
    L = 0;
else
    L = Lambda;
end
tlin = templateLinear('Learner', 'svm',...
    'Regularization', 'lasso', 'Lambda', L,...
    'Solver', 'sparsa');

%if ~exist('Lambda', 'var')
%    L = 0.02;
%else
%    L = Lambda;
%end
linsvm_train = @(X_train, ks_train) fitclinear(X_train, ks_train, 'Learner', 'svm',...
    'Regularization', 'lasso', 'Lambda', L,...
    'Solver', 'sparsa');
linsvm_test = @(model, X_test) predict(model, X_test);
[... 207 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/hazon-2022; date -u
```

```
Wed Nov 11 19:02:50 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/hazon-2022/hc30.py",
 "content": "\"\"\"Loading and measures for CRCNS hc-30 (Hazon et al. 2022, Nat Commun 13:4276).\n\nSources of each parameter are given as:\n  [claims]  the claims file claims/hazon-2022.yaml (its \"common method\" header or a criterion),\n            which cites the paper's Methods or its code (github.com/approbatory/ML-project at\n            commit 2057af9facfd3035c573e1254bdc32ed4781ba60);\n  [paper]   a passage of the paper taken by the author (protocol, author step 1.6);\n  [code]    the paper's code at that commit, cited by file, where the paper is silent;\n  [assumed] an assumption, with the reason;\n  [standard] a standard choice for a detail that cannot change a result.\n\"\"\"\nimport io\nimport time\n\nimport fsspec\nimport numpy as np\nimport scipy.io\nimport scipy.sparse\nfrom scipy.signal import lfilter\n\nURL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-30/live/event_traces.mat\"\nMD5 = \"fe0f5dd2fca6d64dbf0cd3f35e31e1f0\"  # from hc-30/live/checksums.md5\n\nFS = 20.0  # Hz [paper] Methods, Analysis of behavioral data, \"20 frames per second\"\nTRACK_CM = 118.0  # [claims] common method, code DecodeTensor.default_opt total_length\nCUTOFF_P = 5  # percentile [claims] common method\nV_THRESH = 4.0  # cm/s [claims] common method; Methods, Data preprocessing\nLEEWAY = 1 / 20  # [claims] common method, code default_opt leeway_frac\nN_BINS = 20  # [claims] common method\nBIN_CM = TRACK_CM / N_BINS  # 5.9 cm, [claims] common method (code bin_width)\n\n\ndef load_sessions(url=URL):\n    \"\"\"Stream event_traces.mat from the bucket into memory and return a list of sessions.\n\n    Each session is a dict with mouse, session_id, events (frames x neurons, CSC sparse, the\n    event onsets with their amplitudes, as the data descriptor says) and position (pixels).\n    \"\"\"\n    t0 = time.time()\n    with fsspec.open(url, block_size=2**22) as f:\n        raw = f.read()\n    import hashlib\n    md5 = hashlib.md5(raw).hexdigest()\n    m = scipy.io.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)\n    del raw\n    out = []\n    for e in m[\"event_traces\"]:\n        out.append(dict(mouse=str(e.mouse_name), session_id=str(e.session_ID),\n                        events=scipy.sparse.csc_matrix(e.traces),\n                        position=np.asarray(e.position, dtype=float)))\n    return out, md5, time.time() - t0\n\n\ndef alpha_kernel():\n    \"\"\"alpha(t) = (t/tau) exp(1 - t/tau), tau = 0.2 s, sampled at 20 Hz from 0.05 to 1.5 s.\n\n    [paper] Methods, Event detection algorithm, last two steps; [code] DecodeTensor.tensor_loader\n    ('HD_gamma': linspace(0, 7.5, 31)(2:end) in units of tau, causal 'full' convolution).\n    \"\"\"\n    t = np.arange(1, 31) * 0.05 / 0.2\n    return t * np.exp(1 - t)\n\n\ndef event_trace(events):\n    \"\"\"Convolve the event onsets with the alpha kernel (causal) and divide each trace by its\n    standard deviation. [paper] Methods, Event detection algorithm (\"Finally, we divided each\n    event trace by its own standard deviation\"); [code] tensor_loader, X ./ (std(X) + eps).\"\"\"\n    X = events.toarray()\n    Y = lfilter(alpha_kernel(), [1.0], X, axis=0)\n    sd = Y.std(axis=0, ddof=1)\n    return Y / (sd + np.finfo(float).eps)\n\n\ndef select_trials(position, n_bins=N_BINS):\n    \"\"\"Trials as in [claims] common method (code DecodeTensor.new_sel).\n\n    Returns dict with cpp (cm per pixel), vel (cm/s), starts and ends (inclusive frame indices,\n    0-based, as MATLAB's find(diff(...)) gives them), direction (+1 rightward, -1 leftward),\n    bins (0..n_bins-1 per frame, clamped), and the counts before the bin filter.\n    \"\"\"\n    x = position\n    lo, hi = np.percentile(x, CUTOFF_P), np.percentile(x, 100 - CUTOFF_P)\n    rng = hi - lo\n    cpp = TRACK_CM / rng\n    vel = np.concatenate([[0.0], np.diff(x)]) * cpp * FS\n    fast = (np.abs(vel) > V_THRESH).astype(int)\n    d = np.diff(fast)\n    starts = np.where(d == 1)[0]\n    ends = np.where(d == -1)[0]\n    starts = starts[:len(ends)]\n    n_runs = len(starts)\n    b = lo + rng * LEEWAY\n    t = hi - rng * LEEWAY\n    sc, ec = x[starts], x[ends]\n    regular = ((sc < b) & (ec > t)) | ((ec < b) & (sc > t))\n    starts, ends = starts[regular], ends[regular]\n    direction = np.where(x[starts] < b, 1, -1)\n    bins = np.ceil(n_bins * (x - lo) / rng).astype(int)\n    bins = np.clip(bins, 1, n_bins) - 1\n    keep = np.array([len(np.unique(bins[s:e + 1])) == n_bins for s, e in zip(starts, ends)],\n                    dtype=bool)\n    return dict(cpp=cpp, vel=vel, lo=lo, hi=hi, n_fast_runs=n_runs, n_regular=int(regular.sum()),\n                starts=starts[keep], ends=ends[keep], direction=direction[keep], bins=bins)\n\n\ndef build_tensor(X, tr, n_bins=N_BINS):\n    \"\"\"Tensor (neurons, bins, trials) of the mean event trace over each trial's frames in each\n    bin. [paper] Methods, Data preprocessing (\"mean event trace value for neuron n, during trial\n    t, from all the frames where the mouse was in spatial bin k\"); [code] construct_tensor.\"\"\"\n    starts, ends, bins = tr[\"starts\"], tr[\"ends\"], tr[\"bins\"]\n    T = np.zeros((X.shape[1], n_bins, len(starts)))\n    for i, (s, e) in enumerate(zip(starts, ends)):\n        bb = bins[s:e + 1]\n        seg = X[s:e + 1]\n        cnt = np.bincount(bb, minlength=n_bins)\n        sums = np.zeros((n_bins, X.shape[1]))\n        np.add.at(sums, bb, seg)\n        T[:, :, i] = (sums / cnt[:, None]).T\n    return T\n\n\ndef session_tensor(sess, n_bins=N_BINS):\n    tr = select_trials(sess[\"position\"], n_bins)\n    X = event_trace(sess[\"events\"])\n    return build_tensor(X, tr, n_bins), tr[\"direction\"], tr\n\n\ndef shuffle_tensor(T, d, rng):\n    \"\"\"Permute each neuron's values across trials, independently within each bin and direction.\n    [claims] common method (code shuffle_tensor).\"\"\"\n    S = T.copy()\n    for dirn in (1, -1):\n        idx = np.where(d == dirn)[0]\n        n = len(idx)\n        if n == 0:\n            continue\n        sub = T[:, :, idx]\n        perm = np.argsort(rng.random((T.shape[0], T.shape[1], n)), axis=2)\n        S[:, :, idx] = np.take_along_axis(sub, perm, axis=2)\n    return S\n\n\ndef equalize_trials(d, rng, n_per_dir=None):\n    \"\"\"Random equal numbers of rightward and leftward trials (the smaller count); [claims]\n    common method (code cut_tensor). Returns sorted trial indices.\"\"\"\n    r, l = np.where(d == 1)[0], np.where(d == -1)[0]\n    n = min(len(r), len(l)) if n_per_dir is None else n_per_dir\n    return np.sort(np.concatenate([rng.permutation(r)[:n], rng.permutation(l)[:n]]))\n\n\ndef half_split(d, rng):\n    \"\"\"Random half of each direction's trials (code holdout_half: randperm <= n/2).\"\"\"\n    first = np.zeros(len(d), dtype=bool)\n    for dirn in (1, -1):\n        idx = np.where(d == dirn)[0]\n        first[rng.permutation(idx)[:len(idx) // 2]] = True\n    return first\n\n\ndef to_dataset(T, d):\n    \"\"\"Samples (bin x trial) by neurons with class labels 0..39; class 2*b for rightward and\n    2*b+1 for leftward (code tensor2dataset: 2b - (dir == 1), 1-based); position = class // 2.\"\"\"\n    N, K, Tn = T.shape\n    X = T.transpose(2, 1, 0).reshape(Tn * K, N)\n    y = (2 * np.tile(np.arange(K), Tn) + np.repeat(d != 1, K).astype(int))\n    return X, y\n\n\nclass OvOLinearSVM:\n    \"\"\"One-vs-one linear SVMs with voting over the 40 classes.\n\n    [claims] common method: fitcecoc one-vs-one of linear SVMs (templateLinear, lasso, Lambda\n    0, SpaRSA). [assumed] Implemented with libsvm (scikit-learn SVC, linear kernel on a\n    precomputed Gram matrix), L2-regularized hinge loss with a large C (default 100) to\n    approximate the code's unregularized fit, and majority voting (MATLAB's default is\n    loss-weighted decoding). The MATLAB solver is not available here; the decoder's C is shown\n    as a variant in the notebook.\n    \"\"\"\n\n    def __init__(self, C=100.0):\n        self.C = C\n\n    def fit(self, X, y):\n        from sklearn.svm import SVC\n        self.Xtr = X\n        self.m = SVC(kernel=\"precomputed\", C=self.C, decision_function_shape=\"ovo\",\n                     cache_size=50, tol=1e-3)\n        self.m.fit(X @ X.T, y)\n        return self\n\n    def predict(self, X):\n        return self.m.predict(X @ self.Xtr.T)\n\n\ndef decode_once(T, d, rng, shuffled, C=100.0, return_pred=False):\n    \"\"\"Two-fold decoding of one random trial split ([claims] common method, code decode_all).\n\n    Returns the two-fold MSE in cm^2 (bin error times 5.9 cm, squared, averaged over the two\n    folds) and optionally the true and predicted classes of all test samples.\"\"\"\n    first = half_split(d, rng)\n    halves = []\n    for sel in (first, ~first):\n        Th, dh = T[:, :, sel], d[sel]\n        if shuffled:\n            Th = shuffle_tensor(Th, dh, rng)\n        halves.append(to_dataset(Th, dh))\n    mses, ys, ps = [], [], []\n    for a, b in ((0, 1), (1, 0)):\n        Xa, ya = halves[a]\n        Xb, yb = halves[b]\n        p = OvOLinearSVM(C).fit(Xa, ya).predict(Xb)\n        err = (yb // 2 - p // 2) * BIN_CM\n        mses.append(np.mean(err ** 2))\n        ys.append(yb)\n        ps.append(p)\n    if return_pred:\n        return float(np.mean(mses)), np.concatenate(ys), np.concatenate(ps)\n    return float(np.mean(mses))\n\n\n# ---- signal and noise ----\n\ndef _unit(v):\n    return v / (np.linalg.norm(v) + np.finfo(float).eps)\n\n\ndef adjacent_signal_noise(T, d, rng):\n    \"\"\"One random half split; per direction and adjacent bin pair (38), the signal and noise\n    along the training half's signal direction measured on the test half, unshuffled and\n    shuffled ([claims] common method; Methods, Analyzing signal and noise, paragraphs 2 and 3;\n    code DecodeTensor.adjacent_metrics rows 'm', columns 'se', 'ce', 'ue').\n\n    Returns arrays (38,) signal, noise, noise_shuffled ordered [dir -1 pairs 0..18, dir +1\n    pairs 0..18]; pair k joins bin k and k+1 in track coordinates.\"\"\"\n    first = half_split(d, rng)\n    T1, d1, T2, d2 = T[:, :, first], d[first], T[:, :, ~first], d[~first]\n    T2s = shuffle_tensor(T2, d2, rng)\n    K = T.shape[1]\n    sig, noi, nois = [], [], []\n    for dirn in (-1, 1):\n        A1 = T1[:, :, d1 == dirn]\n        A2 = T2[:, :, d2 == dirn]\n        A2s = T2s[:, :, d2 == dirn]\n        m1 = A1.mean(axis=2)\n        m2 = A2.mean(axis=2)\n        for k in range(K - 1):\n            w = _unit(m1[:, k + 1] - m1[:, k])\n            sig.append(np.dot(w, m2[:, k + 1] - m2[:, k]) ** 2)\n            p0, p1 = w @ A2[:, k, :], w @ A2[:, k + 1, :]\n            noi.append((p0.var(ddof=1) + p1.var(ddof=1)) / 2)\n            q0, q1 = w @ A2s[:, k, :], w @ A2s[:, k + 1, :]\n            nois.append((q0.var(ddof=1) + q1.var(ddof=1)) / 2)\n    return np.array(sig), np.array(noi), np.array(nois)\n\n\ndef ensemble_sizes(n_total, step=10):\n    \"\"\"Sizes 1 (or 2), step, 2*step, ..., and all neurons (code decode_series).\"\"\"\n    s = list(range(step, n_total + 1, step))\n    if not s or s[-1] != n_total:\n        s.append(n_total)\n    return s\n\n\ndef fit_line(n, y, cutoff=100):\n    \"\"\"Unweighted least-squares line through (n, y) for n >= cutoff ([claims] common method,\n    code Utils.fitaline). Returns slope, intercept, R squared.\"\"\"\n    n, y = np.asarray(n, float), np.asarray(y, float)\n    s = n >= cutoff\n    A = np.vstack([n[s], np.ones(s.sum())]).T\n    coef, *_ = np.linalg.lstsq(A, y[s], rcond=None)\n    pred = A @ coef\n    ss = ((y[s] - y[s].mean()) ** 2).sum()\n    r2 = 1 - ((y[s] - pred) ** 2).sum() / ss if ss > 0 else np.nan\n    return coef[0], coef[1], r2\n\n\ndef fit_imse(n, imse):\n    \"\"\"IMSE(n) = I0 n / (1 + n/N), unweighted nonlinear least squares from I0 = 1, N = 100, no\n    bounds ([claims] fig2ef criterion, code createFit_infoSaturation.m). Returns I0, N, and\n    the 95% half-intervals from the Jacobian (nan when the fit fails).\"\"\"\n    from scipy.optimize import curve_fit\n    f = lambda x, I0, N: I0 * x / (1 + x / N)\n    try:\n        p, cov = curve_fit(f, np.asarray(n, float), np.asarray(imse, float), p0=[1.0, 100.0],\n                           maxfev=20000)\n        ci = 1.96 * np.sqrt(np.diag(cov))\n        return p[0], p[1], ci[0], ci[1]\n    except Exception:\n        return np.nan, np.nan, np.nan, np.nan\n\n\ndef nsv(T, d):\n    \"\"\"Normalized signal variance per session: per direction and adjacent bin pair, the\n    variance over neurons of the squared elements of the unit vector of the difference of the\n    two bins' trial-mean responses; mean over the 38 pairs. [claims] fig5f criterion (Methods,\n    Definition of the NSV; code load_definitions.m line 43).\"\"\"\n    vals = []\n    for dirn in (-1, 1):\n        m = T[:, :, d == dirn].mean(axis=2)\n        for k in range(T.shape[1] - 1):\n            u = _unit(m[:, k + 1] - m[:, k])\n            vals.append(np.var(u ** 2))\n    return float(np.mean(vals))\n"
}
```

```
File created successfully at: entries/hazon-2022/hc30.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t1.py <<'EOF'
import sys, time, numpy as np, scipy.io, scipy.sparse
sys.path.insert(0,'entries/hazon-2022')
import hc30
m=scipy.io.loadmat('raw.mat', squeeze_me=True, struct_as_record=False)
S=[dict(mouse=str(e.mouse_name), session_id=str(e.session_ID), events=scipy.sparse.csc_matrix(e.traces), position=np.asarray(e.position,float)) for e in m['event_traces']]
import pickle; pickle.dump(S, open('S.pkl','wb'))
for s in S[:5]:
    t=time.time(); T,d,tr=hc30.session_tensor(s); print(s['mouse'], T.shape, (d==1).sum(), (d==-1).sum(), tr['n_fast_runs'], tr['n_regular'], round(tr['cpp'],3), round(time.time()-t,2))
s=S[0]; T,d,tr=hc30.session_tensor(s)
rng=np.random.default_rng(0)
idx=hc30.equalize_trials(d,rng); T=T[:,:,idx]; d=d[idx]
for C in [1,100]:
  for sh in [False, True]:
    t=time.time(); mse=hc30.decode_once(T,d,rng,sh,C=C); print(C, sh, np.sqrt(mse), round(time.time()-t,2))
EOF
python t1.py
```

```
Mouse2023 (188, 20, 146) 74 72 261 146 0.185 0.13
Mouse2023 (193, 20, 204) 102 102 305 204 0.185 0.11
Mouse2023 (178, 20, 182) 92 90 299 182 0.186 0.09
Mouse2023 (239, 20, 123) 50 73 328 123 0.185 0.12
Mouse2023 (161, 20, 168) 90 78 301 168 0.185 0.09
1 False 10.490489244231336 0.53
1 True 6.010612431820534 0.18
100 False 9.856046684649987 0.16
100 True 5.790405738038666 0.18
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/hazon-2022 && python - <<'EOF'
import re
s=open('hc30.py').read()
s=s.replace("""        sub = T[:, :, idx]
        perm = np.argsort(rng.random((T.shape[0], T.shape[1], n)), axis=2)
        S[:, :, idx] = np.take_along_axis(sub, perm, axis=2)""","""        S[:, :, idx] = rng.permuted(T[:, :, idx], axis=2)""")
open('hc30.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t2.py <<'EOF'
import sys, time, numpy as np, pickle
sys.path.insert(0,'entries/hazon-2022')
import hc30
S=pickle.load(open('S.pkl','rb'))
s=max(S, key=lambda s:s['events'].shape[1]); print(s['mouse'], s['events'].shape)
T,d,tr=hc30.session_tensor(s)
rng=np.random.default_rng(1)
idx=hc30.equalize_trials(d,rng); T=T[:,:,idx]; d=d[idx]; print(T.shape)
t=time.time()
for _ in range(10): hc30.adjacent_signal_noise(T,d,rng)
print('sn full', (time.time()-t)/10)
t=time.time()
for _ in range(5): print(np.sqrt(hc30.decode_once(T,d,rng,False)), np.sqrt(hc30.decode_once(T,d,rng,True)))
print('dec full x2', (time.time()-t)/5)
for n in [10,50,100,200]:
    sub=rng.choice(T.shape[0],n,replace=False)
    t=time.time(); m=hc30.decode_once(T[sub],d,rng,False); print(n, 1/m, time.time()-t)
EOF
python t2.py
```

```
Mouse2022 (36374, 497)
(497, 20, 370)
sn full 0.036278605461120605
6.266341096578044 3.052483526609833
6.422352013029651 3.0915442308118317
5.906065138744654 3.0757777587620008
5.8879762211999935 3.126028654915974
6.062111420772757 3.0662723281751996
dec full x2 2.0400827407836912
10 0.0009174704676261145 13.02253532409668
50 0.005784164984853037 49.79057312011719
100 0.009497809563506631 5.722923517227173
200 0.017555590896316073 0.8813912868499756
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t3.py <<'EOF'
import sys, time, numpy as np, pickle
sys.path.insert(0,'entries/hazon-2022')
import hc30
S=pickle.load(open('S.pkl','rb'))
s=max(S, key=lambda s:s['events'].shape[1])
T,d,tr=hc30.session_tensor(s)
rng=np.random.default_rng(1)
idx=hc30.equalize_trials(d,rng); T=T[:,:,idx]; d=d[idx]
for C in [0.1, 1, 10]:
  for n in [1,10,50,100,200,497]:
    sub=rng.choice(T.shape[0],n,replace=False)
    t=time.time(); m=hc30.decode_once(T[sub],d,rng,False,C=C); m2=hc30.decode_once(T[sub],d,rng,True,C=C); print(C, n, round(np.sqrt(m),2), round(np.sqrt(m2),2), round(time.time()-t,2))
EOF
python t3.py
```

```
0.1 1 49.16 49.53 1.99
0.1 10 29.25 30.7 1.61
0.1 50 13.83 11.26 1.71
0.1 100 9.73 6.63 1.75
0.1 200 7.65 4.51 1.79
0.1 497 6.39 3.07 2.03
1 1 60.15 59.67 1.96
1 10 38.16 36.93 2.18
1 50 12.75 9.59 2.35
1 100 9.87 6.71 2.53
1 200 7.72 4.65 1.9
1 497 6.77 3.04 2.0
10 1 51.24 51.77 2.24
10 10 34.0 34.4 4.57
10 50 12.51 12.0 12.68
10 100 8.86 6.41 7.38
10 200 7.72 4.49 1.82
10 497 5.89 3.22 1.98
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t4.py <<'EOF'
import sys, time, numpy as np, pickle, collections
sys.path.insert(0,'entries/hazon-2022')
import hc30
S=pickle.load(open('S.pkl','rb'))
rows=[]
for s in S:
    tr=hc30.select_trials(s['position'])
    p=s['position']
    rows.append((s['mouse'], s['session_id'], s['events'].shape[0], s['events'].shape[1], (tr['direction']==1).sum(), (tr['direction']==-1).sum(), tr['cpp'], p.min(), p.max(), s['events'].nnz))
import pandas as pd
df=pd.DataFrame(rows, columns=['mouse','sid','frames','neurons','R','L','cpp','pmin','pmax','nnz'])
print(df.describe().T)
print(df.sort_values('frames').head(5)); print(df[df.sid.str.contains('&')])
print('min(R,L)>30', ((df[['R','L']].min(1))>30).sum(), 'neur>150', (df.neurons>150).sum(), '>200', (df.neurons>200).sum(), '>=200', (df.neurons>=200).sum())
for thr in [200]:
  for op in ['>','>=']:
    sel = (df.neurons>thr) if op=='>' else (df.neurons>=thr)
    sel &= df[['R','L']].min(1)>30
    print(op, sel.sum(), df[sel].mouse.nunique())
# duplicates
key=collections.defaultdict(list)
for i,s in enumerate(S): key[s['events'].shape[0]].append(i)
print({k:v for k,v in key.items() if len(v)>1})
pos=[s['position'][:1000] for s in S]
for i in range(len(S)):
    for j in range(i+1,len(S)):
        if np.allclose(pos[i][:500], pos[j][:500]): print('same pos start', i,j)
print(df.groupby('mouse').agg(n=('sid','size'), big=('neurons', lambda x:(x>200).sum())))
EOF
python t4.py
```

```
Wed Nov 11 19:06:58 UTC 2026
/tmp/claude-1001/t4.py:14: Pandas4Warning: Starting with pandas version 4.0 all arguments of min will be keyword-only.
  print('min(R,L)>30', ((df[['R','L']].min(1))>30).sum(), 'neur>150', (df.neurons>150).sum(), '>200', (df.neurons>200).sum(), '>=200', (df.neurons>=200).sum())
/tmp/claude-1001/t4.py:18: Pandas4Warning: Starting with pandas version 4.0 all arguments of min will be keyword-only.
  sel &= df[['R','L']].min(1)>30
         count           mean  ...            75%           max
frames   110.0   35943.381818  ...   36133.250000  5.524700e+04
neurons  110.0     253.618182  ...     295.250000  4.970000e+02
R        110.0     100.145455  ...     130.000000  1.910000e+02
L        110.0      99.690909  ...     129.500000  1.950000e+02
cpp      110.0       0.187382  ...       0.188593  1.991509e-01
pmin     110.0 -333770.103003  ...      52.451513  6.300119e+01
pmax     110.0     721.972194  ...     726.091943  9.361886e+02
nnz      110.0  109186.227273  ...  126407.250000  1.318158e+06

[8 rows x 8 columns]
        mouse     sid  frames  ...       pmin        pmax    nnz
35  Mouse2010  111415   24075  ...  13.494348  713.861318  25756
34  Mouse2010  000156   24109  ...  24.542792  710.433242  24139
36  Mouse2010  151543   24758  ...  54.979595  687.626151  26245
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t5.py <<'EOF'
import sys, numpy as np, pickle
sys.path.insert(0,'entries/hazon-2022')
import hc30
S=pickle.load(open('S.pkl','rb'))
for i,s in enumerate(S):
    p=s['position']
    bad=(p<0).sum()
    if bad or p.max()>800: print(i, s['mouse'], s['session_id'], len(p), bad, np.percentile(p,[0,0.1,1,5,50,95,99,99.9,100]).round(1))
s=S[7]; p=s['position']; neg=np.where(p<0)[0]; print(neg[:20], neg[-5:], p[neg[:10]])
ev=s['events']; print(ev.shape, ev.nnz, (ev.data<0).sum())
# per neuron event rate
r=np.diff(ev.indptr); print(np.percentile(r,[0,50,100]))
others=[np.median(np.diff(x['events'].indptr)) for x in S]; print(np.percentile(others,[0,50,100]))
# frames where p<0 relative to rows with many events
rows=np.asarray((ev!=0).sum(1)).ravel(); print('events per frame', np.percentile(rows,[50,99,100]))
EOF
python t5.py
```

```
7 Mouse2024 090858&091446 55247 503 [-12628.1  -9568.4     55.      64.9    318.6    705.3    712.1    723.6
    728. ]
12 Mouse2024 082641 36106 0 [ 57.   57.5  58.4  62.  434.1 696.7 703.4 705.7 936.2]
28 Mouse2028 105610 36074 6 [-23.   53.6  58.8  66.5 423.2 697.8 704.8 712.5 714.6]
51 Mouse2012 141832 35771 795 [-3.65523015e+07 -3.19515293e+07 -6.46276170e+06  2.65000000e+01
  4.59700000e+02  6.93800000e+02  7.08300000e+02  7.15700000e+02
  7.18200000e+02]
68 Mouse2022 093722 36374 79 [-1.542819e+05 -2.732810e+04  5.620000e+01  5.980000e+01  4.218000e+02
  7.070000e+02  7.152000e+02  7.233000e+02  7.251000e+02]
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19] [498 499 500 501 502] [-12628.09896118 -12568.18221257 -12508.30162844 -12448.48953448
 -12388.77441756 -12329.18092574 -12269.72986829 -12210.43821564
 -12151.31909944 -12092.38181253]
(55247, 369) 1318158 0
[2667. 3548. 4597.]
[ 121.    345.25 3548.  ]
events per frame [24. 51. 75.]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t6.py <<'EOF'
import sys, numpy as np, pickle
sys.path.insert(0,'entries/hazon-2022')
import hc30
S=pickle.load(open('S.pkl','rb'))
for i in [7, 0]:
    ev=S[i]['events']; c=ev[:,0].toarray().ravel(); nz=np.nonzero(c)[0]
    print(i, nz[:30], c[nz[:12]].round(3))
    # run lengths of consecutive nonzero
    runs=np.diff(np.where(np.diff(np.r_[0,(c!=0).astype(int),0])!=0)[0])[::2]; print(' run lengths', np.bincount(runs)[:10])
for i in [7,51,68,28]:
    tr=hc30.select_trials(S[i]['position']); p=S[i]['position']
    bad=[k for k,(s,e) in enumerate(zip(tr['starts'],tr['ends'])) if (p[s:e+1]<tr['lo']-50).any()]
    print(i, len(tr['starts']), 'trials with junk positions', bad, tr['lo'], tr['hi'])
# events at session 7: frames 0..36000 vs after
ev=S[7]['events']; rows=np.asarray((ev!=0).sum(1)).ravel()
print([rows[a:a+5000].mean().round(2) for a in range(0,55247,5000)])
EOF
python t6.py
```

```
7 [ 295  317  341  373  429  441  464  480  490  513  525  539  552  928
  973 1033 1084 1096 1121 1135 1139 1145 1165 1454 1473 1636 1843 1851
 1858 1888] [0.295 0.155 0.113 0.166 0.248 0.121 0.188 0.232 0.275 0.128 0.174 0.12 ]
 run lengths [   0 4115]
0 [  229   316   670  2286  2990  3424  3592  3795  3807  4521  4585  5003
  5708  6627  6677  6845  6891  7014  7178  7985  8338  9912 10240 10449
 10795 11163 11570 11597 11796 11829] [0.3   0.243 0.258 0.327 0.322 0.505 0.286 0.331 0.777 0.343 0.258 0.459]
 run lengths [  0 116]
7 145 trials with junk positions [] 64.90415088953455 705.2781945394134
51 100 trials with junk positions [] 26.543271468554863 693.8016115002295
68 371 trials with junk positions [0] 59.83212970699589 707.0437181295217
28 264 trials with junk positions [] 66.4791331306899 697.8243484084991
[np.float64(11.74), np.float64(12.03), np.float64(12.01), np.float64(15.08), np.float64(27.77), np.float64(28.65), np.float64(29.33), np.float64(30.69), np.float64(31.31), np.float64(32.06), np.float64(31.48), np.float64(30.29)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "Supplementary Table\|Suppl. Table\|Table 1\|Table 2\|^##" paper/10.1038-s41467-022-31254-y.txt | sed -n 1,80p
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 223,232p paper/10.1038-s41467-022-31254-y.txt; sed -n 300,420p paper/10.1038-s41467-022-31254-y.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 420,520p paper/10.1038-s41467-022-31254-y.txt; sed -n 640,760p paper/10.1038-s41467-022-31254-y.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 760,830p paper/10.1038-s41467-022-31254-y.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 1,100p @Org/load_definitions.m
```

```
function load_definitions(org)

org.make_derived('lambda_normed', {'lambda'},...
    @(l)l./sum(l));

org.make_derived('corr_lambda_normed', {'corr_lambda'},...
    @(l)l./sum(l));

org.make_derived('signal_variance', {'lambda', 'loadings'},...
    @(lambda, loadings) lambda .* loadings'.^2);

org.make_derived('corr_signal_variance', {'corr_lambda', 'corr_loadings'},...
    @(lambda, loadings) lambda .* loadings'.^2);

org.make_derived('dmu_ipr', {'dmus'},...
    @(dmu) (sum(dmu.^2).^2 ./ sum(dmu.^4)));

org.make_derived('signal_density', {'dmus'},...
    @(dmu) (sum(dmu.^2).^2 ./ sum(dmu.^4)) ./ length(dmu));

[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; cat @Cloud/eigen_snr_crossval.m | head -70; grep -n "loadings\|lambda\|use_corr" @Cloud/Cloud.m | head -40
```

```
function [dp2_train, dp2_test, signal_train, signal_test, noise_train, noise_test] = eigen_snr_crossval(o)

N_REPS = 100;
%N_DIMS = 91;

X = o.dt.data_tensor;
half_trials = min(sum(o.dt.tr_dir==1), sum(o.dt.tr_dir==-1));
cut = @(x) x(:,:,1:half_trials);
X = cat(2, cut(X(:,:,o.dt.tr_dir==1)), cut(X(:,:,o.dt.tr_dir==-1)));

[N,K,T] = size(X);


T_by_2 = floor(T / 2);
remainder = mod(T, 2);
%partition = [ones(1,T_by_3), 2*ones(1,T_by_3), 3*ones(1,T_by_3) zeros(1,remainder)];

N_DIMS = T_by_2 - 1;

[dp2_train, dp2_test, signal_train, signal_test, noise_train, noise_test] = deal(nan(N_REPS, 38, N_DIMS)); 
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 26,82p @Cloud/Cloud.m; grep -n "function.*area_between" -A12 -r @Org/ | head -20
```

```
function o = Cloud(i, use_corr, use_events, use_binary_spikes)
            if ~exist('use_corr', 'var')
                use_corr = false;
            end
            
            if ~exist('use_events', 'var')
                use_events = false;
            end
            
            if ~exist('use_binary_spikes', 'var')
                use_binary_spikes = false;
            end
            
            if isa(i, 'DecodeTensor')
                o.dt = i;
            else
                sm = SessManager;
                if use_events
                    o.dt = DecodeTensor(sm.cons_usable(i,true), 'events_transients');
                elseif use_binary_spikes
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate; uv pip install -q jupytext 2>&1|tail -1; cd $TMPDIR/mlp; sed -n 2298,2330p DecodeTensor.m; sed -n 2190,2215p DecodeTensor.m
```

```
Wed Nov 11 19:07:51 UTC 2026
        function [mean_cell_snr, sem_cell_snr] = single_cell_d_primes2(o)
            %[N, K, T] = size(o.data_tensor);
            signal_leftward = diff(mean(o.data_tensor(:,:,o.tr_dir==-1), 3, 'omitnan'), 1, 2).^2;
            signal_rightward = diff(mean(o.data_tensor(:,:,o.tr_dir==1), 3, 'omitnan'), 1, 2).^2;
            
            
            noise_leftward = var(o.data_tensor(:,:,o.tr_dir==-1), [], 3, 'omitnan');
            noise_leftward = (noise_leftward(:, 1:end-1) + noise_leftward(:, 2:end))/2;
            
            noise_rightward = var(o.data_tensor(:,:,o.tr_dir==1), [], 3, 'omitnan');
            noise_rightward = (noise_rightward(:, 1:end-1) + noise_rightward(:, 2:end))/2;
            
            dp2_leftward = signal_leftward ./ noise_leftward;
            dp2_rightward = signal_rightward ./ noise_rightward;
            
            mean_over_bins = mean([dp2_leftward dp2_rightward], 2, 'omitnan'); %used to be median
            mean_cell_snr = mean(mean_over_bins, 'omitnan');
            sem_cell_snr = sem(mean_over_bins);
        end
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 250,260p @Org/load_definitions.m; sed -n 555,615p @Org/load_definitions.m
```

```
@(a,b)find(a<b,1));

org.make_var_per_sess('overlap_metric', {'mus'},...
    @overlap_metric);

org.make_var_per_sess('var_fwhm_cm', {'mus'},...
    @(mus) calc_var_hwhm(mus) .* (2*5.9).^2);

org.make_var_per_sess('place_field_mode_right', {'mus'},...
    @(mus) argmax(cell2mat(mus(1:20)),[],2));

n = size(C,1);
r = (sum(C, 'all') - n)./(n^2-n);
end

function var_hwhm = calc_var_hwhm(mus)
mus = cell2mat(mus);
[n_cells, n_bins] = size(mus);
assert(n_bins == 40);
[hwhm_r, hwhm_l] = deal(zeros(1, n_cells));
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/hazon-2022/hc30.py <<'EOF'


# ---- per-session measures used by several claims ----

def signal_noise_series(T, d, seed, n_subsets=20, step=10):
    """Signal and noise against ensemble size for one session ([claims] common method: sizes 2,
    10, 20, ... all; 80 subsets in the paper, n_subsets here; each subset a new trial split;
    equal numbers of trials per direction, code cut_tensor).

    Returns sizes, and arrays (sizes, 38) of the subset-averaged per-pair signal, noise and
    shuffled noise, and arrays (sizes,) of the subset-averaged median over pairs (code
    res_lookup: median over pairs per subset, then mean over subsets)."""
    rng = np.random.default_rng(seed)
    N = T.shape[0]
    sizes = [2] + ensemble_sizes(N, step)
    P = np.zeros((3, len(sizes), 38))
    M = np.zeros((3, len(sizes)))
    for i, n in enumerate(sizes):
        for _ in range(n_subsets):
            idx = equalize_trials(d, rng)
            sub = rng.choice(N, n, replace=False)
            s, c, u = adjacent_signal_noise(T[sub][:, :, idx], d[idx], rng)
            for j, v in enumerate((s, c, u)):
                P[j, i] += v / n_subsets
                M[j, i] += np.median(v) / n_subsets
    return np.array(sizes), P, M


def slope_with_se(n, y, cutoff=100):
    """Slope of an unweighted line fit at n >= cutoff, with its standard error."""
    n, y = np.asarray(n, float), np.asarray(y, float)
    s = n >= cutoff
    x, yy = n[s], y[s]
    if len(x) < 3:
        return np.nan, np.nan
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, yy, rcond=None)
    resid = yy - A @ coef
    s2 = (resid ** 2).sum() / (len(x) - 2)
    se = np.sqrt(s2 / ((x - x.mean()) ** 2).sum())
    return coef[0], se


def noise_pairs_by_peak_distance(T, d, rng):
    """Mean noise correlation per place-field peak distance (bins 0..19) for one session, per
    direction, unshuffled and shuffled ([claims] fig1d criterion; code DecodeTensor.corr_values:
    residuals from the class mean over all trials of that direction, Pearson correlation per
    bin; averaged over the 20 bins). Returns dict direction -> (sum_u, sum_s, count) over
    distance (pairs i < j), and the pooled pair values for the pooled reading."""
    S = shuffle_tensor(T, d, rng)
    out = {}
    for dirn in (1, -1):
        A, B = T[:, :, d == dirn], S[:, :, d == dirn]
        N, K, _ = A.shape
        Cu = np.zeros((N, N))
        Cs = np.zeros((N, N))
        nb = np.zeros((N, N))
        for k in range(K):
            for X, C in ((A[:, k, :], Cu), (B[:, k, :], Cs)):
                with np.errstate(invalid="ignore", divide="ignore"):
                    c = np.corrcoef(X)
                C += np.nan_to_num(c)
            ok = (A[:, k, :].std(axis=1) > 0) & (B[:, k, :].std(axis=1) > 0)
            nb += np.outer(ok, ok)
        with np.errstate(invalid="ignore", divide="ignore"):
            Cu, Cs = Cu / nb, Cs / nb
        peak = A.mean(axis=2).argmax(axis=1)
        iu = np.triu_indices(N, 1)
        dist = np.abs(peak[:, None] - peak[None, :])[iu]
        cu, cs = Cu[iu], Cs[iu]
        good = np.isfinite(cu) & np.isfinite(cs)
        out[dirn] = (dist[good], cu[good], cs[good])
    return out


def jitter(position, tr):
    """Position measurement noise of one session ([claims] position-measurement-noise; code
    estimate_position_jitter.m): frames from the first in bin 7 to the last in bin 13 of each
    trial, in the run's direction; even frames (1-based) fit a line, residuals of odd frames;
    robust scale IQR / 1.349 of all residuals."""
    devs = []
    cpp, bins = tr["cpp"], tr["bins"] + 1  # 1-based bins
    for s, e, dirn in zip(tr["starts"], tr["ends"], tr["direction"]):
        b = bins[s:e + 1]
        pos = cpp * position[s:e + 1]
        first, last = (7, 13) if dirn == 1 else (13, 7)
        i0 = np.where(b == first)[0]
        i1 = np.where(b == last)[0]
        if len(i0) == 0 or len(i1) == 0 or i1[-1] < i0[0]:
            continue
        fr = np.arange(i0[0], i1[-1] + 1) + 1  # 1-based frame index within trial
        rp = pos[fr - 1]
        trn = fr % 2 == 0
        if trn.sum() < 4:
            continue
        a, c = np.polyfit(fr[trn], rp[trn], 1)
        devs.append((rp - (a * fr + c))[~trn])
    devs = np.concatenate(devs)
    q75, q25 = np.percentile(devs, [75, 25])
    return (q75 - q25) / (2 * np.sqrt(2) * 0.4769362762044699)  # erfinv(1/2)


def hwhm_bins(x):
    """Half-width at half maximum of a tuning curve in bins (code load_definitions.m
    one_hwhm)."""
    x = x - x.min()
    ix = int(np.argmax(x))
    h = x[ix] / 2
    pre, post = x[:ix + 1], x[ix:]
    lb = np.where(pre < h)[0]
    left = ix - lb[-1] if len(lb) else -np.inf
    rb = np.where(post < h)[0]
    right = rb[0] if len(rb) else -np.inf
    hw = max(left, right)
    if hw < 0:
        hw = round(len(x) / 2)
    return hw


def var_fwhm_cm(T, d):
    """Variance over neurons (both directions pooled) of the half-width at half maximum of each
    direction's mean tuning curve, times (2 x 5.9 cm)^2 ([claims] fig5f criterion; code
    load_definitions.m var_fwhm_cm, calc_var_hwhm)."""
    hw = []
    for dirn in (1, -1):
        mu = T[:, :, d == dirn].mean(axis=2)
        for row in mu:
            hw.append(np.nan if np.all(row == row[0]) else hwhm_bins(row))
    return np.nanvar(hw, ddof=1) * (2 * BIN_CM) ** 2


def class_clouds(T, d):
    """The 40 clouds (neurons x trials) in the code's order (Cloud.m: bins 1..20 of rightward
    trials, then 1..20 of leftward)."""
    out = []
    for dirn in (1, -1):
        A = T[:, :, d == dirn]
        for k in range(T.shape[1]):
            out.append(A[:, k, :])
    return out


def pca_dirs(X):
    """Principal directions (neurons x components) and eigenvalues of the covariance of the
    samples in the columns of X (MATLAB pca: centred, min(N, T-1) components)."""
    Xc = X - X.mean(axis=1, keepdims=True)
    U, s, _ = np.linalg.svd(Xc, full_matrices=False)
    k = min(X.shape[0], X.shape[1] - 1)
    return U[:, :k], (s[:k] ** 2) / (X.shape[1] - 1)


def overlap_measures(T, d, rng):
    """Per adjacent bin pair (38, code Cloud.m order): cos^2 of the unit signal direction with
    each noise eigenvector of the first bin's cloud, unshuffled and shuffled, for covariance and
    correlation (z-scored) clouds; and the per-pair quantities of Supplementary Table 2.
    [claims] fig4b criterion (code Cloud.m, load_definitions.m area_between)."""
    clouds = class_clouds(T, d)
    S = shuffle_tensor(T, d, rng)
    clouds_s = class_clouds(S, d)
    K = T.shape[1]
    rows = []
    for j in list(range(K - 1)) + list(range(K, 2 * K - 1)):
        mu0, mu1 = clouds[j].mean(axis=1), clouds[j + 1].mean(axis=1)
        dmu = mu1 - mu0
        u = _unit(dmu)
        r = {}
        for kind in ("cov", "corr"):
            for tag, C in (("u", clouds[j]), ("s", clouds_s[j])):
                X = C
                if kind == "corr":
                    sd = X.std(axis=1, ddof=1, keepdims=True)
                    X = (X - X.mean(axis=1, keepdims=True)) / np.where(sd > 0, sd, 1)
                V, lam = pca_dirs(X)
                c2 = (u @ V) ** 2
                r[f"{kind}_{tag}_cos2"] = c2
                r[f"{kind}_{tag}_lam"] = lam
        r["dmu2"] = dmu ** 2
        r["u2"] = u ** 2
        rows.append(r)
    return rows
EOF
date -u
```

```
Wed Nov 11 19:08:51 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t7.py <<'EOF'
import sys, time, numpy as np, pickle
sys.path.insert(0,'entries/hazon-2022')
import hc30
S=pickle.load(open('S.pkl','rb'))
s=max(S, key=lambda s:s['events'].shape[1])
T,d,tr=hc30.session_tensor(s)
t=time.time(); sizes,P,M=hc30.signal_noise_series(T,d,0,n_subsets=5); print('sn5', time.time()-t)
ss=hc30.slope_with_se(sizes,M[0]); sn=hc30.slope_with_se(sizes,M[1]); su=hc30.slope_with_se(sizes,M[2]); print(ss,sn,su, ss[0]/sn[0], ss[0]/su[0])
t=time.time(); o=hc30.noise_pairs_by_peak_distance(T,d,np.random.default_rng(0)); print('corr', time.time()-t)
dist,cu,cs=o[1]; print([ (k, cu[dist==k].mean().round(4), cs[dist==k].mean().round(4)) for k in [0,1,2,5,10,15]])
t=time.time(); rows=hc30.overlap_measures(T,d,np.random.default_rng(0)); print('ovl', time.time()-t)
print(np.mean([r['cov_u_cos2'].sum()-r['cov_s_cos2'].sum() for r in rows]), np.mean([r['cov_u_cos2'][:6].sum()-r['cov_s_cos2'][:6].sum() for r in rows]))
print('jit', hc30.jitter(s['position'],tr), 'nsv', hc30.nsv(T,d), 'vfw', hc30.var_fwhm_cm(T,d))
EOF
python t7.py
```

```
sn5 6.1805100440979
(np.float64(0.023265119491010247), np.float64(0.000334430958835694)) (np.float64(0.009936346519570663), np.float64(0.0001577802783702483)) (np.float64(0.0002548168728575985), np.float64(6.461080830010559e-05)) 2.341415876065432 91.3013303636753
corr 0.20385313034057617
[(0, np.float64(0.0327), np.float64(-0.0002)), (1, np.float64(0.0184), np.float64(-0.0001)), (2, np.float64(0.0094), np.float64(0.0)), (5, np.float64(0.0074), np.float64(-0.0004)), (10, np.float64(0.0021), np.float64(0.0)), (15, np.float64(0.0012), np.float64(0.0))]
ovl 0.9501123428344727
0.2036916531083836 0.13009669442425253
jit 0.15803599273940913 nsv 4.469533134399879e-05 vfw 922.5242132756255
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/hazon-2022/src_nb1.py",
 "content": "# %% [markdown]\n# # Reproducing Hazon et al. (2022) from CRCNS hc-30: tensor, noise and signal analyses\n#\n# HEADER_PLACEHOLDER\n\n# %%\nimport collections\nimport multiprocessing as mp\nimport resource\nimport time\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport hc30\n\nT0 = time.time()\nsessions, md5, load_s = hc30.load_sessions()\nprint(f\"streamed and parsed event_traces.mat in {load_s:.0f} s; md5 {md5} \"\n      f\"({'matches' if md5 == hc30.MD5 else 'DIFFERS FROM'} checksums.md5)\")\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nrows = []\nTENS = []\nfor i, s in enumerate(sessions):\n    T, d, tr = hc30.session_tensor(s)\n    TENS.append((T, d))\n    p = s[\"position\"]\n    ev = s[\"events\"]\n    rows.append(dict(i=i, mouse=s[\"mouse\"], session=s[\"session_id\"], frames=ev.shape[0],\n                     minutes=ev.shape[0] / hc30.FS / 60, neurons=ev.shape[1],\n                     right=int((d == 1).sum()), left=int((d == -1).sum()),\n                     fast_runs=tr[\"n_fast_runs\"], regular=tr[\"n_regular\"],\n                     cm_per_px=tr[\"cpp\"], p5=tr[\"lo\"], p95=tr[\"hi\"], pmin=p.min(), pmax=p.max(),\n                     n_neg=int((p < 0).sum()), events=ev.nnz,\n                     ev_min=ev.data.min(), ev_max=ev.data.max(),\n                     jitter=hc30.jitter(p, tr)))\ninfo = pd.DataFrame(rows)\ninfo[\"min_trials\"] = info[[\"right\", \"left\"]].min(axis=1)\ninfo[\"large\"] = (info.neurons > 200) & (info.min_trials > 30)\npd.set_option(\"display.width\", 200)\nprint(\"sessions\", len(info), \"mice\", info.mouse.nunique())\nprint(info.groupby(\"mouse\").agg(sessions=(\"session\", \"size\"), neurons=(\"neurons\", \"sum\"),\n                                large=(\"large\", \"sum\"), trials_med=(\"min_trials\", \"median\")))\nprint(info[[\"frames\", \"minutes\", \"neurons\", \"right\", \"left\", \"cm_per_px\", \"p5\", \"p95\", \"events\",\n            \"ev_min\", \"ev_max\"]].describe().round(3).T)\n\n# %% [markdown]\n# Checks of the description against the data:\n#\n# - The data descriptor says 110 sessions, each with a frames by neurons sparse array that holds\n#   \"a positive value if neuron n had a calcium event in time frame t\". The cell below checks that\n#   the values are single frames (event onsets with their amplitude) and not the convolved trace\n#   the paper decodes from; the alpha convolution and normalisation of the Methods are therefore\n#   applied here (hc30.event_trace).\n# - Frame rate: no sampling rate is stored; 20 Hz is from the Methods. Session lengths in minutes\n#   below are at 20 Hz; the paper and the descriptor say about 20 min.\n# - Position is in camera pixels, with no unit in the file. The scale is the code's: 118 cm over\n#   the 5th to 95th percentile span.\n\n# %% tags=[\"sanity\"]\nruns = []\nfor s in sessions:\n    ev = s[\"events\"]\n    for j in range(0, ev.shape[1], 25):\n        c = ev[:, j].toarray().ravel() != 0\n        e = np.diff(np.r_[0, c.astype(int), 0])\n        runs.extend(np.where(e == -1)[0] - np.where(e == 1)[0])\nruns = np.array(runs)\nprint(f\"runs of consecutive nonzero frames, sample of neurons: {len(runs)} runs, \"\n      f\"{np.mean(runs == 1):.3f} of length 1, max {runs.max()}\")\nprint(\"events per neuron per minute, by session: median %.2f, range %.2f to %.2f\" % tuple(\n    np.percentile(info.events / info.neurons / info.minutes, [50, 0, 100])))\nprint(\"session with the most events per neuron per minute:\",\n      info.loc[(info.events / info.neurons / info.minutes).idxmax(), [\"mouse\", \"session\"]].tolist(),\n      round((info.events / info.neurons / info.minutes).max(), 2))\nprint(\"minutes at 20 Hz: median %.1f, range %.1f to %.1f\" % tuple(\n    np.percentile(info.minutes, [50, 0, 100])))\nprint(\"sessions with negative positions:\")\nprint(info.loc[info.n_neg > 0, [\"mouse\", \"session\", \"frames\", \"n_neg\", \"pmin\", \"pmax\"]])\nprint(\"sessions whose ID joins two recordings:\",\n      info.loc[info.session.str.contains(\"&\"), [\"mouse\", \"session\", \"frames\"]].values.tolist())\n\n# %% tags=[\"sanity\"]\n# Recordings deposited more than once: compare positions of sessions with the same frame count,\n# and the first 2000 frames of every pair.\ndups = []\nheads = [s[\"position\"][:2000] for s in sessions]\nfor a in range(len(sessions)):\n    for b in range(a + 1, len(sessions)):\n        if np.allclose(heads[a], heads[b]) or (\n                sessions[a][\"events\"].shape == sessions[b][\"events\"].shape\n                and np.allclose(sessions[a][\"position\"], sessions[b][\"position\"])):\n            dups.append((a, b))\nprint(\"pairs with identical positions:\", dups)\nsame_n = collections.Counter((r.mouse, r.neurons) for r in info.itertuples())\nprint(\"sessions of one mouse with the same neuron count:\",\n      {k: v for k, v in same_n.items() if v > 1})\nprint(\"neurons are not matched across sessions in the file (no cell identifiers), so every \"\n      \"analysis is per session\")\n\n# %% tags=[\"sanity\"]\n# Clock check: position and event traces share the frame axis (same length, by construction).\n# A contrast that a lag would destroy: decode position bin from the event trace with the\n# position labels shifted in time, on one session per mouse (nearest-centroid on held-out\n# trials, a quick check, not the paper's decoder).\ndef shift_check(s, shift):\n    tr = hc30.select_trials(s[\"position\"])\n    X = hc30.event_trace(s[\"events\"])\n    if shift:\n        X = np.roll(X, shift, axis=0)\n    T = hc30.build_tensor(X, tr)\n    d = tr[\"direction\"]\n    first = hc30.half_split(d, np.random.default_rng(0))\n    errs = []\n    for dirn in (1, -1):\n        A = T[:, :, first & (d == dirn)].mean(axis=2)\n        B = T[:, :, ~first & (d == dirn)]\n        for t in range(B.shape[2]):\n            dist = ((B[:, :, t][:, :, None] - A[:, None, :]) ** 2).sum(axis=0)\n            errs.append(np.abs(dist.argmin(axis=1) - np.arange(20)).mean())\n    return np.mean(errs) * hc30.BIN_CM\n\nfirst_of_mouse = info.groupby(\"mouse\").i.first().values\nfor lag_s in (0, 2, 10):\n    e = [shift_check(sessions[i], int(lag_s * hc30.FS)) for i in first_of_mouse]\n    print(f\"event trace shifted by {lag_s:>2} s: mean absolute position error \"\n          f\"{np.mean(e):.1f} cm (range {min(e):.1f} to {max(e):.1f}) over {len(e)} sessions\")\n\n# %% tags=[\"sanity\"]\nWORK = info.index.values\nLARGE = info.index[info.large].values\nANIMALS_L = sorted(info.loc[LARGE, \"mouse\"].unique())\nprint(f\"working sessions {len(WORK)}, large-data sessions {len(LARGE)} from {len(ANIMALS_L)} mice\")\nprint(\"tensor values: min %.3f, max %.2f (event trace in units of its SD)\" % (\n    min(T.min() for T, _ in TENS), max(T.max() for T, _ in TENS)))\nprint(f\"peak memory so far {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB, \"\n      f\"{time.time() - T0:.0f} s\")\n\n# %% [markdown]\n# ## data-sessions-and-neurons\n#\n# > The analysed data are 110 sessions from 12 mice with 27,898 neurons (151 to 497 per\n# > session, median 235), selected from 239 sessions for more than 150 neurons and 30 running\n# > trials in each direction; a subset of 73 sessions from 10 mice with at least 200 neurons is\n# > the large-data set.\n\n# %% tags=[\"claim:data-sessions-and-neurons\"]\nok = (info.neurons > 150) & (info.min_trials > 30)\nprint(\"sessions meeting the working rule (>150 neurons, >30 valid trials each way):\",\n      int(ok.sum()), \"of\", len(info))\nprint(\"mice\", info.mouse.nunique(), \"| neurons\", info.neurons.sum(), \"| median\",\n      info.neurons.median(), \"| min\", info.neurons.min(), \"| max\", info.neurons.max())\nfor label, sel in ((\"> 200 neurons (code)\", info.neurons > 200),\n                   (\">= 200 neurons (Methods)\", info.neurons >= 200)):\n    sel = sel & ok\n    print(f\"large-data, {label}: {int(sel.sum())} sessions from \"\n          f\"{info.loc[sel, 'mouse'].nunique()} mice\")\nprint(\"valid trials per direction (smaller of the two): median %d, range %d to %d\" % (\n    info.min_trials.median(), info.min_trials.min(), info.min_trials.max()))\n\n# %% [markdown]\n# RESULT_data-sessions-and-neurons\n\n# %% [markdown]\n# ## single-cell-variability\n#\n# > Single-neuron responses vary strongly between visits to the same bin (response variance\n# > 0.7263 +/- 0.6117), and the single-cell signal-to-noise ratio, variance between bins over\n# > variance within bins, is 0.41 +/- 0.34, pooled over 27,898 neurons.\n\n# %% tags=[\"claim:single-cell-variability\"]\nsd_vals, var_vals, snr40, snr_dir = [], [], [], []\nfor T, d in TENS:\n    per_class_sd, per_class_var, means = [], [], []\n    for dirn in (1, -1):\n        A = T[:, :, d == dirn]\n        per_class_sd.append(A.std(axis=2, ddof=1))\n        per_class_var.append(A.var(axis=2, ddof=1))\n        means.append(A.mean(axis=2))\n    sd = np.concatenate(per_class_sd, axis=1)\n    va = np.concatenate(per_class_var, axis=1)\n    mu = np.concatenate(means, axis=1)\n    sd_vals.append(sd.ravel())\n    var_vals.append(va.ravel())\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        snr40.append(mu.var(axis=1, ddof=1) / va.mean(axis=1))\n        snr_dir.append(np.nanmean([means[k].var(axis=1, ddof=1) / per_class_var[k].mean(axis=1)\n                                   for k in (0, 1)], axis=0))\nsd_vals, var_vals = np.concatenate(sd_vals), np.concatenate(var_vals)\nsnr40, snr_dir = np.concatenate(snr40), np.concatenate(snr_dir)\nprint(\"response variability over (session, class, neuron), n =\", len(sd_vals))\nprint(f\"  SD reading (code):        mean {np.nanmean(sd_vals):.4f} +/- {np.nanstd(sd_vals):.4f}\"\n      \"   (paper 0.7263 +/- 0.6117)\")\nprint(f\"  variance reading (text):  mean {np.nanmean(var_vals):.4f} +/- {np.nanstd(var_vals):.4f}\")\nprint(\"single-cell SNR per neuron, n =\", len(snr40), \"(neurons with no response:\",\n      int(np.isnan(snr40).sum()), \")\")\nprint(f\"  40 classes together:          {np.nanmean(snr40):.3f} +/- {np.nanstd(snr40):.3f}\"\n      \"   (paper 0.41 +/- 0.34)\")\nprint(f\"  per direction, averaged:      {np.nanmean(snr_dir):.3f} +/- {np.nanstd(snr_dir):.3f}\")\nprint(\"  median, 40 classes: %.3f\" % np.nanmedian(snr40))\nby_mouse = pd.DataFrame({\"mouse\": np.repeat(info.mouse.values, info.neurons.values),\n                         \"snr40\": snr40}).groupby(\"mouse\").snr40.mean().round(3)\nprint(\"SNR (40 classes) by mouse:\", by_mouse.to_dict())\n\n# %% [markdown]\n# RESULT_single-cell-variability\n\n# %% [markdown]\n# ## suppl-table1-place-field-properties\n#\n# > In these data the mean event rate is 0.33 +/- 0.24 Hz, the in-field and out-of-field rates\n# > 0.88 +/- 0.72 and 0.034 +/- 0.07 Hz, the maximum rate 1.4 +/- 0.72 Hz, the place-field width\n# > at half amplitude 37.8 +/- 48.5 cm, the trial-by-trial variability 1.2 +/- 0.66 and the\n# > spatial information 0.24 +/- 0.051 bits per event, similar to electrophysiological reports.\n#\n# Rates use the detected events (nonzero onsets of the dataset's array). The Gaussian fit is to\n# each direction's binned event rate (Supplementary Figure 3 legend); the readings of the\n# criterion are computed side by side.\n\n# %% tags=[\"claim:suppl-table1-place-field-properties\"]\nfrom scipy.optimize import curve_fit\n\ndef gauss(x, a, m, s, b):\n    return b + a * np.exp(-0.5 * ((x - m) / s) ** 2)\n\nxb = np.arange(20)\npf_rows = []\nfor si, s in enumerate(sessions):\n    tr = hc30.select_trials(s[\"position\"])\n    ev = s[\"events\"].tocsr()\n    onsets = (ev != 0).astype(float)\n    n_frames = ev.shape[0]\n    in_trial = np.zeros(n_frames, bool)\n    for a, b in zip(tr[\"starts\"], tr[\"ends\"]):\n        in_trial[a:b + 1] = True\n    total_events = np.asarray(onsets.sum(axis=0)).ravel()\n    run_events = np.asarray(onsets[in_trial].sum(axis=0)).ravel()\n    per_dir = {}\n    for dirn in (1, -1):\n        cnt = np.zeros((20, ev.shape[1]))\n        occ = np.zeros(20)\n        visit_counts = []\n        for a, b, dd in zip(tr[\"starts\"], tr[\"ends\"], tr[\"direction\"]):\n            if dd != dirn:\n                continue\n            bb = tr[\"bins\"][a:b + 1]\n            c = np.zeros((20, ev.shape[1]))\n            np.add.at(c, bb, onsets[a:b + 1].toarray())\n            cnt += c\n            occ += np.bincount(bb, minlength=20)\n            visit_counts.append(c)\n        rate = cnt / (occ[:, None] / hc30.FS)  # events per second, bins x neurons\n        V = np.stack(visit_counts, axis=2)  # bins x neurons x visits\n        per_dir[dirn] = (rate, V.var(axis=2, ddof=1).mean(axis=0))\n    minutes = n_frames / hc30.FS / 60\n    for n in range(ev.shape[1]):\n        r = dict(session=si, mouse=s[\"mouse\"],\n                 rate_run=run_events[n] / (in_trial.sum() / hc30.FS),\n                 rate_all=total_events[n] / (n_frames / hc30.FS),\n                 active=total_events[n] / minutes * 10 > 100)\n        for dirn, tag in ((1, \"R\"), (-1, \"L\")):\n            rate, tbt = per_dir[dirn]\n            y = rate[:, n]\n            r[f\"max_{tag}\"] = y.max()\n            r[f\"tbt_{tag}\"] = tbt[n]\n            p = y / y.sum() if y.sum() > 0 else np.full(20, np.nan)\n            with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n                plogp = np.where(p > 0, p * np.log2(p), 0.0)\n            r[f\"si_skaggs_{tag}\"] = np.log2(20) + plogp.sum()\n            r[f\"si_literal_{tag}\"] = -plogp.sum() / 20\n            half = y > y.max() / 2\n            r[f\"in_b_{tag}\"] = y[half].mean() if y.max() > 0 else np.nan\n            r[f\"out_b_{tag}\"] = y[~half].mean() if (~half).any() else np.nan\n            r[f\"sd_{tag}\"] = y.std()\n            fit = (np.nan,) * 4\n            if y.max() > 0:\n                try:\n                    fit, _ = curve_fit(gauss, xb, y, p0=[y.max() - y.min(), y.argmax(), 2.0, y.min()],\n                                       maxfev=2000)\n                except Exception:\n                    pass\n            a_, m_, s_, b_ = fit\n            r[f\"fit_ok_{tag}\"] = np.isfinite(s_)\n            width = 2 * np.sqrt(2 * np.log(2)) * abs(s_) * hc30.BIN_CM\n            r[f\"width_{tag}\"] = width\n            if np.isfinite(s_):\n                inside = np.abs(xb - m_) <= np.sqrt(2 * np.log(2)) * abs(s_)\n                r[f\"in_a_{tag}\"] = y[inside].mean() if inside.any() else np.nan\n                r[f\"out_a_{tag}\"] = y[~inside].mean() if (~inside).any() else np.nan\n            else:\n                r[f\"in_a_{tag}\"] = r[f\"out_a_{tag}\"] = np.nan\n        pf_rows.append(r)\npf = pd.DataFrame(pf_rows)\nprint(\"neurons\", len(pf), \"| Gaussian fits failed: R\", int((~pf.fit_ok_R).sum()), \"L\",\n      int((~pf.fit_ok_L).sum()))\nfor tag in (\"R\", \"L\"):\n    pf[f\"modulated_{tag}\"] = pf[f\"max_{tag}\"] > 0.2 * pf[f\"sd_{tag}\"]\n\ndef both(col):\n    return np.concatenate([pf[f\"{col}_R\"].values, pf[f\"{col}_L\"].values])\n\ndef mstd(x):\n    x = np.asarray(x, float)\n    x = x[np.isfinite(x)]\n    return f\"{x.mean():.3f} +/- {x.std():.3f} (n {len(x)})\"\n\nactive2 = np.concatenate([pf.active.values, pf.active.values])\nmodul = np.concatenate([pf.modulated_R.values, pf.modulated_L.values])\nw = both(\"width\")\nw_ok = np.isfinite(w) & (w < 20 * hc30.BIN_CM * 10)\nprint(\"cells with > 100 events per 10 min:\", int(pf.active.sum()), \"of\", len(pf))\ntable = []\nfor cells, sel1, sel2 in ((\"all\", np.ones(len(pf), bool), np.ones(2 * len(pf), bool)),\n                          (\">100 ev/10 min\", pf.active.values, active2)):\n    table += [\n        (\"mean rate (a) running\", cells, mstd(pf.rate_run[sel1]), 0.33),\n        (\"mean rate (b) session\", cells, mstd(pf.rate_all[sel1]), 0.33),\n        (\"in-field (a) fitted width\", cells, mstd(both(\"in_a\")[sel2]), 0.88),\n        (\"in-field (b) above half peak\", cells, mstd(both(\"in_b\")[sel2]), 0.88),\n        (\"out-of-field (a)\", cells, mstd(both(\"out_a\")[sel2]), 0.034),\n        (\"out-of-field (b)\", cells, mstd(both(\"out_b\")[sel2]), 0.034),\n        (\"max rate\", cells, mstd(both(\"max\")[sel2]), 1.4),\n        (\"PF width, fitted FWHM, cm\", cells, mstd(w[sel2 & w_ok]), 37.8),\n        (\"PF width, modulated cells\", cells, mstd(w[sel2 & w_ok & modul]), 37.8),\n        (\"trial-by-trial variability\", cells, mstd(both(\"tbt\")[sel2]), 1.2),\n        (\"spatial info, log2(20) - H(p)\", cells, mstd(both(\"si_skaggs\")[sel2]), 0.24),\n        (\"spatial info, footnote literal\", cells, mstd(both(\"si_literal\")[sel2]), 0.24),\n    ]\ntab = pd.DataFrame(table, columns=[\"quantity\", \"cells\", \"mean +/- SD (n)\", \"paper\"])\ntab[\"mean\"] = tab[\"mean +/- SD (n)\"].str.split(\" \").str[0].astype(float)\ntab[\"within 10%\"] = (np.abs(tab[\"mean\"] - tab[\"paper\"]) <= 0.1 * tab[\"paper\"])\nprint(tab.to_string())\nprint(\"widths above the cap of 200 bins (fit runaway), dropped:\", int((np.isfinite(w) & ~w_ok).sum()))\nprint(\"width per direction: R\", mstd(pf.width_R[np.isfinite(pf.width_R) & (pf.width_R < 1180)]),\n      \"| L\", mstd(pf.width_L[np.isfinite(pf.width_L) & (pf.width_L < 1180)]))\nprint(\"mean running rate by mouse:\", pf.groupby(\"mouse\").rate_run.mean().round(3).to_dict())\n\n# %% [markdown]\n# RESULT_suppl-table1-place-field-properties\n\n# %% [markdown]\n# ## fig1d-noise-correlation-by-field-distance\n#\n# > Noise correlations between neuron pairs depend on the distance between their place-field\n# > peaks, highest for nearby fields, and trial shuffling drastically reduces them.\n\n# %% tags=[\"claim:fig1d-noise-correlation-by-field-distance\"]\nrng_1d = np.random.default_rng(101)\nper_sess = {1: [], -1: []}\npooled = {1: [np.zeros(20), np.zeros(20), np.zeros(20), np.zeros(20), np.zeros(20)],\n          -1: [np.zeros(20), np.zeros(20), np.zeros(20), np.zeros(20), np.zeros(20)]}\nn_pairs = 0\nfor T, d in TENS:\n    o = hc30.noise_pairs_by_peak_distance(T, d, rng_1d)\n    for dirn in (1, -1):\n        dist, cu, cs = o[dirn]\n        n_pairs += len(dist)\n        mu_u = np.array([cu[dist == k].mean() if (dist == k).any() else np.nan for k in range(20)])\n        mu_s = np.array([cs[dist == k].mean() if (dist == k).any() else np.nan for k in range(20)])\n        per_sess[dirn].append((mu_u, mu_s))\n        cnt = np.bincount(dist, minlength=20)\n        P = pooled[dirn]\n        P[0] += cnt\n        P[1] += np.bincount(dist, cu, minlength=20)\n        P[2] += np.bincount(dist, cu ** 2, minlength=20)\n        P[3] += np.bincount(dist, cs, minlength=20)\n        P[4] += np.bincount(dist, cs ** 2, minlength=20)\nprint(\"pairs counted (both directions):\", n_pairs, \"(legend 3,941,140)\")\nres1d = {}\nfor dirn, name in ((1, \"rightward\"), (-1, \"leftward\")):\n    U = np.array([a for a, _ in per_sess[dirn]])\n    Sh = np.array([b for _, b in per_sess[dirn]])\n    mu_u, mu_s = np.nanmean(U, 0), np.nanmean(Sh, 0)\n    ci_u = 1.96 * np.nanstd(U, 0, ddof=1) / np.sqrt(np.isfinite(U).sum(0))\n    ci_s = 1.96 * np.nanstd(Sh, 0, ddof=1) / np.sqrt(np.isfinite(Sh).sum(0))\n    far = np.nanmean(U[:, 10:], axis=1)\n    print(f\"\\n{name}: mean over sessions (95% interval)\")\n    for k in (0, 1, 2, 3, 5, 10, 15, 19):\n        print(f\"  distance {k:>2}: unshuffled {mu_u[k]:.4f} +/- {ci_u[k]:.4f}   \"\n              f\"shuffled {mu_s[k]:.5f} +/- {ci_s[k]:.5f}\")\n    sep = all(mu_u[k] - ci_u[k] > mu_s[k] + ci_s[k] for k in range(11))\n    print(f\"  distance 0 vs mean of distances >= 10: {mu_u[0]:.4f} vs {np.nanmean(mu_u[10:]):.4f}\")\n    print(f\"  shuffled below unshuffled with non-overlapping intervals at every distance 0..10: {sep}\")\n    # pooled over pairs\n    P = pooled[dirn]\n    pm_u = P[1] / P[0]\n    pm_s = P[3] / P[0]\n    pse_u = np.sqrt(P[2] / P[0] - pm_u ** 2) / np.sqrt(P[0])\n    pse_s = np.sqrt(P[4] / P[0] - pm_s ** 2) / np.sqrt(P[0])\n    sep_p = all(pm_u[k] - 1.96 * pse_u[k] > pm_s[k] + 1.96 * pse_s[k] for k in range(11))\n    print(f\"  pooled pairs: distance 0 {pm_u[0]:.4f}, >= 10 {np.average(pm_u[10:], weights=P[0][10:]):.4f};\"\n          f\" separated 0..10: {sep_p}\")\n    # code's joined bins (d and d+1)\n    joined = [(np.nanmean(U[:, k:k + 2])) for k in range(0, 19)]\n    print(\"  joined distances (code variant), first values:\", np.round(joined[:4], 4))\n    res1d[name] = (mu_u, mu_s, ci_u, ci_s)\nfig, axs = plt.subplots(1, 2, figsize=(9, 3))\nfor ax, (name, (mu_u, mu_s, ci_u, ci_s)) in zip(axs, res1d.items()):\n    x = np.arange(20)\n    ax.plot(x, mu_u, label=\"unshuffled\")\n    ax.fill_between(x, mu_u - ci_u, mu_u + ci_u, alpha=0.3)\n    ax.plot(x, mu_s, label=\"shuffled\")\n    ax.fill_between(x, mu_s - ci_s, mu_s + ci_s, alpha=0.3)\n    ax.set_title(name)\n    ax.set_xlabel(\"PF peak distance (bins)\")\naxs[0].set_ylabel(\"noise correlation\")\naxs[0].legend()\nplt.show()\nprint(\"all plotted values within the axes; y range %.4f to %.4f\" % (\n    min(np.nanmin(v[1] - v[3]) for v in res1d.values()), max(np.nanmax(v[0] + v[2]) for v in res1d.values())))\n\n# %% [markdown]\n# RESULT_fig1d-noise-correlation-by-field-distance\n\n# %% [markdown]\n# ## position-measurement-noise\n#\n# > Position tracking noise is small, 0.28 cm on average (0.12 to 1.0 cm across 110 sessions),\n# > far below the decoding errors.\n\n# %% tags=[\"claim:position-measurement-noise\"]\nj = info.jitter\nprint(f\"jitter over {len(j)} sessions: mean {j.mean():.3f} cm, min {j.min():.3f}, max {j.max():.3f},\"\n      f\" median {j.median():.3f}\")\nprint(\"sessions above 1.1 cm:\", int((j > 1.1).sum()))\nprint(\"by mouse:\", info.groupby(\"mouse\").jitter.mean().round(3).to_dict())\n\n# %% [markdown]\n# RESULT_position-measurement-noise\n\n# %% [markdown]\n# ## Signal and noise against ensemble size (shared by Figures 3 to 5)\n#\n# Per session, 20 random neuron subsets per ensemble size (the paper uses 80; reduced to fit the\n# time limit), sizes 2, 10, 20, ... all neurons, each subset with its own equalised trials and\n# half split. Run in 3 worker processes, each session with its own seed.\n\n# %%\ndef _sn(i):\n    T, d = TENS[i]\n    return hc30.signal_noise_series(T, d, seed=1000 + i, n_subsets=20)\n\nt = time.time()\nwith mp.get_context(\"fork\").Pool(3) as pool:\n    SN = pool.map(_sn, range(len(TENS)))\nprint(f\"signal and noise series: {time.time() - t:.0f} s\")\n\nsn_rows = []\nfor i, (sizes, P, M) in enumerate(SN):\n    sig, sse = hc30.slope_with_se(sizes, M[0])\n    noi, nse = hc30.slope_with_se(sizes, M[1])\n    nos, sse_s = hc30.slope_with_se(sizes, M[2])\n    sig_s = sig  # trial shuffling leaves the bin means, hence the signal, unchanged (code 'se')\n    a, b, r2u = hc30.fit_line(sizes, M[1])\n    _, _, r2s = hc30.fit_line(sizes, M[2])\n    asn = sig / noi\n    asn_s = sig / nos\n    # delta-method 95% half-intervals of the two asymptotic SNRs\n    ci = 1.96 * abs(asn) * np.sqrt((sse / sig) ** 2 + (nse / noi) ** 2)\n    ci_s = 1.96 * abs(asn_s) * np.sqrt((sse / sig) ** 2 + (sse_s / nos) ** 2)\n    ratio = asn / asn_s\n    ci_r = 1.96 * abs(ratio) * np.sqrt((nse / noi) ** 2 + (sse_s / nos) ** 2)\n    # per bin pair slopes\n    pair_sig = np.array([hc30.slope_with_se(sizes, P[0][:, k])[0] for k in range(38)])\n    pair_noi = np.array([hc30.slope_with_se(sizes, P[1][:, k])[0] for k in range(38)])\n    sn_rows.append(dict(i=i, mouse=info.mouse[i], sig_slope=sig, noise_slope=noi,\n                        noise_slope_shuf=nos, noise_r2=r2u, noise_shuf_r2=r2s,\n                        asnr=asn, asnr_shuf=asn_s, asnr_ci=ci, asnr_shuf_ci=ci_s,\n                        ratio=ratio, ratio_ci=ci_r, pair_sig=pair_sig, pair_noi=pair_noi))\nSNR = pd.DataFrame(sn_rows)\nprint(SNR[[\"sig_slope\", \"noise_slope\", \"noise_slope_shuf\", \"asnr\", \"asnr_shuf\", \"ratio\"]]\n      .describe().round(5).T)\n\n# %% [markdown]\n# ## fig3cd-signal-and-noise-growth\n#\n# > The spatial signal grows linearly with ensemble size and does not change with trial\n# > shuffling, while the noise along the signal direction keeps growing linearly in the\n# > unmodified data but saturates within about 100 neurons in the shuffled data.\n\n# %% tags=[\"claim:fig3cd-signal-and-noise-growth\"]\nmed = SNR[[\"sig_slope\", \"noise_slope\", \"noise_slope_shuf\", \"noise_r2\"]].median()\n# the signal measured on the shuffled test half: means are unchanged by the shuffle, check it\nT, d = TENS[0]\nrr = np.random.default_rng(5)\nS_ = hc30.shuffle_tensor(T, d, rr)\nprint(\"largest change of a bin mean under the shuffle (session 0):\",\n      float(np.abs(S_.mean(axis=2) - T.mean(axis=2)).max()))\nprint(f\"median session: signal slope {med.sig_slope:.5f}, unshuffled noise slope \"\n      f\"{med.noise_slope:.5f} (R^2 of the line {med.noise_r2:.3f}), shuffled noise slope \"\n      f\"{med.noise_slope_shuf:.6f}\")\nprint(\"(1) shuffled signal slope / unshuffled: 1.000 (identical bin means)\")\nprint(f\"(2) unshuffled noise slope > 0 in {int((SNR.noise_slope > 0).sum())} of {len(SNR)} sessions;\"\n      f\" R^2 >= 0.9 in {int((SNR.noise_r2 >= 0.9).sum())}; median R^2 {SNR.noise_r2.median():.3f}\")\nrel = SNR.noise_slope_shuf / SNR.noise_slope\nprint(f\"(3) shuffled / unshuffled noise slope: median {rel.median():.3f}, \"\n      f\"below 0.1 in {int((rel < 0.1).sum())} of {len(SNR)} sessions\")\n# example curves, median session by noise slope\nk = int(SNR.noise_slope.sub(med.noise_slope).abs().idxmin())\nsizes, P, M = SN[k]\nfig, axs = plt.subplots(1, 2, figsize=(9, 3))\naxs[0].plot(sizes, M[0]); axs[0].set_title(\"signal |dmu|^2\"); axs[0].set_xlabel(\"neurons\")\naxs[1].plot(sizes, M[1], label=\"unshuffled\"); axs[1].plot(sizes, M[2], label=\"shuffled\")\naxs[1].set_title(\"noise sigma^2\"); axs[1].legend(); axs[1].set_xlabel(\"neurons\")\nplt.show()\nprint(f\"example session {k} ({info.mouse[k]}): signal {M[0].min():.3f} to {M[0].max():.3f}, \"\n      f\"noise {M[1].min():.3f} to {M[1].max():.3f}, shuffled noise {M[2].min():.3f} to {M[2].max():.3f}\")\n\n# %% [markdown]\n# RESULT_fig3cd-signal-and-noise-growth\n\n# %% [markdown]\n# ## suppl10-asymptotic-snr-lower-with-correlations\n#\n# > Across all mice the asymptotic SNR (signal slope over noise slope) is lower in the\n# > unmodified data than in the shuffled data.\n\n# %% tags=[\"claim:suppl10-asymptotic-snr-lower-with-correlations\"]\nw_ = stats.wilcoxon(SNR.asnr, SNR.asnr_shuf)\nprint(f\"asymptotic SNR, median unshuffled {SNR.asnr.median():.3f}, shuffled \"\n      f\"{SNR.asnr_shuf.median():.2f}; shuffled higher in {int((SNR.asnr_shuf > SNR.asnr).sum())} \"\n      f\"of {len(SNR)} sessions; Wilcoxon signed-rank p = {w_.pvalue:.2e}\")\nprint(\"negative shuffled noise slopes (asymptotic SNR undefined or negative):\",\n      int((SNR.noise_slope_shuf <= 0).sum()))\npm = SNR.groupby(\"mouse\")[[\"asnr\", \"asnr_shuf\"]].median()\npm[\"shuf_higher\"] = pm.asnr_shuf > pm.asnr\nprint(pm.round(3))\nprint(\"mice with higher median for shuffled:\", int(pm.shuf_higher.sum()), \"of\", len(pm))\n\n# %% [markdown]\n# RESULT_suppl10-asymptotic-snr-lower-with-correlations\n\n# %% [markdown]\n# ## Run position (Figures 3f to 3h)\n#\n# Beginning of a run: the first bin pair of rightward runs and the last of leftward runs; end:\n# the opposite pairs (the code's choice). Pairs are ordered leftward 0..18 then rightward 0..18,\n# pair k joining bins k and k+1 in track coordinates, rightward runs going from bin 0 to 19.\n\n# %%\ndef begin_end(arr):\n    a = np.stack(arr.values)\n    begin_pooled = np.concatenate([a[:, 19 + 0], a[:, 18]])  # rightward pair 0, leftward pair 18\n    end_pooled = np.concatenate([a[:, 19 + 18], a[:, 0]])\n    return begin_pooled, end_pooled, a[:, 19], a[:, 37]\n\ndef one_sided(x, y, alt):\n    return stats.wilcoxon(x, y, alternative=alt).pvalue\n\nsubsets = {\"110 working\": SNR.index.values, \"73 large-data\": LARGE}\n\n# %% [markdown]\n# ## fig3f-signal-slope-beginning-vs-end\n#\n# > The asymptotic signal slope differs between the beginning and the end of runs, decreasing\n# > over the run as the legend states.\n\n# %% tags=[\"claim:fig3f-signal-slope-beginning-vs-end\"]\nfor name, idx in subsets.items():\n    sub = SNR.loc[idx]\n    b, e, br, er = begin_end(sub.pair_sig)\n    print(f\"{name}: pooled n = {len(b)}: median begin {np.median(b):.4f}, end {np.median(e):.4f}; \"\n          f\"begin > end (legend) p = {one_sided(b, e, 'greater'):.2e}; begin < end (code) p = \"\n          f\"{one_sided(b, e, 'less'):.2e}\")\n    print(f\"   rightward only n = {len(br)}: begin {np.median(br):.4f}, end {np.median(er):.4f}; \"\n          f\"greater p = {one_sided(br, er, 'greater'):.2e}; less p = {one_sided(br, er, 'less'):.2e}\")\na = np.stack(SNR.pair_sig.values)\nalong = np.concatenate([np.median(a[:, 19:], 0), np.median(a[:, :19], 0)[::-1]])\nprint(\"median signal slope along the run, rightward pairs 0..18:\", np.round(along[:19], 4))\nprint(\"                      leftward pairs, run order:\", np.round(along[19:], 4))\n\n# %% [markdown]\n# RESULT_fig3f-signal-slope-beginning-vs-end\n\n# %% [markdown]\n# ## fig3g-noise-slope-decreases-over-run\n#\n# > The asymptotic noise slope decreases monotonically and significantly from the beginning to\n# > the end of runs.\n\n# %% tags=[\"claim:fig3g-noise-slope-decreases-over-run\"]\nfor name, idx in subsets.items():\n    sub = SNR.loc[idx]\n    b, e, br, er = begin_end(sub.pair_noi)\n    print(f\"{name}: pooled n = {len(b)}: median begin {np.median(b):.5f}, end {np.median(e):.5f}; \"\n          f\"begin > end p = {one_sided(b, e, 'greater'):.2e} (other direction \"\n          f\"{one_sided(b, e, 'less'):.2e})\")\na = np.stack(SNR.pair_noi.values)\nprint(\"median noise slope along the run, rightward:\", np.round(np.median(a[:, 19:], 0), 5))\nprint(\"median noise slope along the run, leftward (run order):\", np.round(np.median(a[:, :19], 0)[::-1], 5))\n\n# %% [markdown]\n# RESULT_fig3g-noise-slope-decreases-over-run\n\n# %% [markdown]\n# ## fig3h-snr-higher-at-run-end\n#\n# > The asymptotic SNR (signal slope over noise slope) is significantly higher at the end of\n# > runs than at their start.\n\n# %% tags=[\"claim:fig3h-snr-higher-at-run-end\"]\nfor name, idx in subsets.items():\n    sub = SNR.loc[idx]\n    ratio_pairs = pd.Series([s / n for s, n in zip(sub.pair_sig, sub.pair_noi)], index=sub.index)\n    b, e, br, er = begin_end(ratio_pairs)\n    print(f\"{name}: pooled n = {len(b)}: median begin {np.median(b):.3f}, end {np.median(e):.3f}; \"\n          f\"begin < end p = {one_sided(b, e, 'less'):.2e}\")\n    print(f\"   rightward only: begin {np.median(br):.3f}, end {np.median(er):.3f}; \"\n          f\"begin < end p = {one_sided(br, er, 'less'):.2e}\")\n\n# %% [markdown]\n# RESULT_fig3h-snr-higher-at-run-end\n\n# %% [markdown]\n# ## fig4a-snr-along-noise-pcs-peaks-at-6\n#\n# > Along the eigenvectors of the noise covariance, each component's SNR contribution rises to a\n# > maximum at the sixth component, and the first six carry only a small part of the total, so\n# > spatial information is spread over many dimensions.\n#\n# 20 random half splits per bin pair (the code uses 100; reduced for time).\n\n# %% tags=[\"claim:fig4a-snr-along-noise-pcs-peaks-at-6\"]\nN_SPLITS_4A = 20\n\ndef eigen_snr(i):\n    rng = np.random.default_rng(4000 + i)\n    T, d = TENS[i]\n    h = min((d == 1).sum(), (d == -1).sum())\n    X = np.concatenate([T[:, :, d == 1][:, :, :h], T[:, :, d == -1][:, :, :h]], axis=1)\n    N, K, Tn = X.shape\n    t2 = Tn // 2\n    nd = t2 - 1\n    out = np.zeros((38, nd))\n    for pi, b in enumerate(list(range(19)) + list(range(20, 39))):\n        Xa, Xb = X[:, b, :], X[:, b + 1, :]\n        acc = np.zeros(nd)\n        for _ in range(N_SPLITS_4A):\n            perm = rng.permutation(Tn)\n            p1, p2 = perm[:t2], perm[t2:2 * t2]\n            V, _ = hc30.pca_dirs(Xa[:, p1])\n            V = V[:, :nd]\n            pa, pb = Xa[:, p2].T @ V, Xb[:, p2].T @ V\n            acc += (pa.mean(0) - pb.mean(0)) ** 2 / ((pa.var(0, ddof=1) + pb.var(0, ddof=1)) / 2)\n        out[pi] = acc / N_SPLITS_4A\n    return np.median(out, axis=0)\n\nt = time.time()\nwith mp.get_context(\"fork\").Pool(3) as pool:\n    EIG = pool.map(eigen_snr, list(LARGE))\nprint(f\"eigen-SNR: {time.time() - t:.0f} s, components per session {min(map(len, EIG))} to \"\n      f\"{max(map(len, EIG))}\")\nL = min(map(len, EIG))\nE = np.array([e[:L] for e in EIG])\ncurve = E.mean(axis=0)\npeak = int(np.argmax(curve)) + 1\nshare6 = curve[:6].sum() / curve.sum()\nprint(f\"peak of the session-mean curve at component {peak}; first 10 values:\", np.round(curve[:10], 4))\nprint(f\"share of the first six in the sum over the {L} components common to all sessions: {share6:.3f}\")\nfull_share = [e[:6].sum() / e.sum() for e in EIG]\nprint(f\"share of the first six per session over all its components: median {np.median(full_share):.3f}\")\nper_sess_peak = np.array([int(np.argmax(e)) + 1 for e in EIG])\nprint(\"per-session peak component: median\", np.median(per_sess_peak), \"counts\",\n      dict(collections.Counter(per_sess_peak)))\nmice_curves = pd.DataFrame(E, index=info.mouse[LARGE].values).groupby(level=0).mean()\nprint(\"per-mouse peak:\", {m: int(np.argmax(r.values)) + 1 for m, r in mice_curves.iterrows()})\n\n# %% [markdown]\n# RESULT_fig4a-snr-along-noise-pcs-peaks-at-6\n\n# %% [markdown]\n# ## fig4b-correlations-increase-noise-signal-overlap\n#\n# > Noise correlations increase the overlap (squared cosine) between the noise principal\n# > directions and the signal direction compared with shuffled data.\n\n# %% tags=[\"claim:fig4b-correlations-increase-noise-signal-overlap\"]\ndef _ovl(i):\n    T, d = TENS[i]\n    rows = hc30.overlap_measures(T, d, np.random.default_rng(5000 + i))\n    r = {}\n    for kind in (\"cov\", \"corr\"):\n        r[f\"area_all_{kind}\"] = np.mean([x[f\"{kind}_u_cos2\"].sum() - x[f\"{kind}_s_cos2\"].sum() for x in rows])\n        r[f\"area_6_{kind}\"] = np.mean([x[f\"{kind}_u_cos2\"][:6].sum() - x[f\"{kind}_s_cos2\"][:6].sum() for x in rows])\n        r[f\"ipr_cos2_{kind}\"] = np.mean([x[f\"{kind}_u_cos2\"].sum() ** 2 / (x[f\"{kind}_u_cos2\"] ** 2).sum() for x in rows])\n    r[\"pr_lambda\"] = np.mean([x[\"cov_u_lam\"].sum() ** 2 / (x[\"cov_u_lam\"] ** 2).sum() for x in rows])\n    r[\"nsv\"] = np.mean([np.var(x[\"u2\"]) for x in rows])\n    r[\"var_dmu2\"] = np.mean([np.var(x[\"dmu2\"]) for x in rows])\n    r[\"mean_dmu2\"] = np.mean([np.mean(x[\"dmu2\"]) for x in rows])\n    return r\n\nt = time.time()\nwith mp.get_context(\"fork\").Pool(3) as pool:\n    OV = pool.map(_ovl, list(LARGE))\nOV = pd.DataFrame(OV, index=LARGE)\nOV[\"mouse\"] = info.mouse[LARGE].values\nprint(f\"overlap measures: {time.time() - t:.0f} s\")\nfor col in (\"area_all_cov\", \"area_6_cov\", \"area_all_corr\", \"area_6_corr\"):\n    pm = OV.groupby(\"mouse\")[col].mean()\n    print(f\"{col}: median session {OV[col].median():.4f}, positive in \"\n          f\"{int((OV[col] > 0).sum())} of {len(OV)} sessions; animal means positive in \"\n          f\"{int((pm > 0).sum())} of {len(pm)}; min animal mean {pm.min():.4f}\")\n\n# %% [markdown]\n# RESULT_fig4b-correlations-increase-noise-signal-overlap\n\n# %% [markdown]\n# ## fig4c-overlap-predicts-asymptotic-snr\n#\n# > Across animals, the increase in noise and signal overlap caused by noise correlations is\n# > inversely correlated with the asymptotic SNR (r squared 0.50, p = 0.014), so the geometry of\n# > the noise predicts where information saturates.\n\n# %% tags=[\"claim:fig4c-overlap-predicts-asymptotic-snr\"]\ndef adj_r2(r, n):\n    return 1 - (1 - r ** 2) * (n - 1) / (n - 2)\n\nLS = SNR.loc[LARGE].copy()\nfor col in OV.columns:\n    if col != \"mouse\":\n        LS[col] = OV[col].values\nagg = LS.groupby(\"mouse\").mean(numeric_only=True)\nfor x in (\"area_all_cov\", \"area_6_cov\"):\n    for y in (\"asnr\", \"ratio\"):\n        r, p = stats.pearsonr(agg[x], agg[y])\n        print(f\"{x} vs {y} across {len(agg)} mice: r = {r:.3f}, r^2 = {r * r:.3f}, adjusted \"\n              f\"{adj_r2(r, len(agg)):.3f}, p = {p:.4f}\")\nr, p = stats.pearsonr(LS.area_all_cov, LS.asnr)\nprint(f\"across {len(LS)} sessions, area_all_cov vs asnr: r = {r:.3f}, p = {p:.2e}\")\n\n# %% [markdown]\n# RESULT_fig4c-overlap-predicts-asymptotic-snr\n\n# %% [markdown]\n# ## fig5f-pf-width-variance-vs-nsv\n#\n# > Across animals, the broader the distribution of place-field widths, the smaller the\n# > normalized signal variance (NSV) (Pearson r = -0.65, r squared 0.36, p = 0.039).\n\n# %% tags=[\"claim:fig5f-pf-width-variance-vs-nsv\"]\nLS[\"nsv\"] = [hc30.nsv(*TENS[i]) for i in LARGE]\nLS[\"var_fwhm_cm\"] = [hc30.var_fwhm_cm(*TENS[i]) for i in LARGE]\nagg = LS.groupby(\"mouse\").mean(numeric_only=True)\nr, p = stats.pearsonr(agg.var_fwhm_cm, agg.nsv)\nprint(f\"across {len(agg)} mice: Pearson r = {r:.3f}, r^2 = {r * r:.3f}, p = {p:.4f}\")\nr2_, p2_ = stats.pearsonr(LS.var_fwhm_cm, LS.nsv)\nprint(f\"across {len(LS)} sessions: r = {r2_:.3f}, p = {p2_:.2e}\")\nprint(agg[[\"var_fwhm_cm\", \"nsv\"]].round(6))\nprint(\"NSV range over sessions: %.2e to %.2e; var FWHM %.0f to %.0f cm^2\" % (\n    LS.nsv.min(), LS.nsv.max(), LS.var_fwhm_cm.min(), LS.var_fwhm_cm.max()))\n\n# %% [markdown]\n# RESULT_fig5f-pf-width-variance-vs-nsv\n\n# %% [markdown]\n# ## fig5hi-nsv-predicts-noise-correlation-effect\n#\n# > Across animals, the NSV correlates with the ratio of asymptotic SNR with and without noise\n# > correlations (Pearson 0.83, r squared 0.65, p = 0.003); animals with a small NSV lose more\n# > information to noise correlations.\n\n# %% tags=[\"claim:fig5hi-nsv-predicts-noise-correlation-effect\"]\nfilt = (LS.asnr.abs() > LS.asnr_ci) & (LS.asnr_shuf.abs() > LS.asnr_shuf_ci) & (LS.ratio < 7) & (LS.noise_slope_shuf > 0)\nprint(\"sessions kept by the code's filters (values larger than their interval, ratio < 7):\",\n      int(filt.sum()), \"of\", len(LS))\nfor name, sub in ((\"no filter\", LS), (\"code filters\", LS[filt])):\n    for yname, y in ((\"unshuffled/shuffled\", sub.ratio), (\"shuffled/unshuffled\", 1 / sub.ratio)):\n        rs, ps = stats.pearsonr(sub.nsv, y)\n        ag = pd.DataFrame({\"nsv\": sub.nsv, \"y\": y, \"mouse\": sub.mouse}).groupby(\"mouse\").mean()\n        ra, pa = stats.pearsonr(ag.nsv, ag.y)\n        print(f\"{name:12s} {yname}: sessions r = {rs:.3f} (p {ps:.2e}, n {len(sub)}); \"\n              f\"animals r = {ra:.3f}, r^2 {ra * ra:.3f} (p {pa:.4f}, n {len(ag)})\")\n\n# %% [markdown]\n# RESULT_fig5hi-nsv-predicts-noise-correlation-effect\n\n# %% [markdown]\n# ## suppl-table2-nsv-best-predictor\n#\n# > Of the variables tested, the NSV explains the effect of noise correlations on the\n# > asymptotic SNR best (highest adjusted R squared), and the result does not depend on the\n# > number of neurons or trials in a session.\n\n# %% tags=[\"claim:suppl-table2-nsv-best-predictor\"]\nLS[\"n_neurons\"] = info.neurons[LARGE].values\nLS[\"n_trials\"] = (info.right + info.left)[LARGE].values\nrng_t2 = np.random.default_rng(202)\n\ndef fixed_nsv(i, n=200, reps=100):\n    T, d = TENS[i]\n    return np.mean([hc30.nsv(T[rng_t2.choice(T.shape[0], n, replace=False)], d) for _ in range(reps)])\n\nLS[\"fixed_nsv_200\"] = [fixed_nsv(i) for i in LARGE]\nvariables = {\"NSV\": \"nsv\", \"cos2 area, corr PCs\": \"area_all_corr\", \"Var((dmu_i)^2)\": \"var_dmu2\",\n             \"# neurons\": \"n_neurons\", \"(sum lambda)^2 / sum lambda^2\": \"pr_lambda\",\n             \"Mean((dmu_i)^2)\": \"mean_dmu2\", \"cos2 area, cov PCs\": \"area_all_cov\",\n             \"Var(PF halfwidths)\": \"var_fwhm_cm\", \"IPR cos2, cov PCs\": \"ipr_cos2_cov\",\n             \"# trials\": \"n_trials\", \"IPR cos2, corr PCs\": \"ipr_cos2_corr\"}\nfor name, sub in ((\"all 73\", LS), (\"code filters\", LS[filt])):\n    out = []\n    for lab, col in variables.items():\n        r, p = stats.pearsonr(sub[col], sub.ratio)\n        ag = sub.groupby(\"mouse\")[[col, \"ratio\"]].mean()\n        ra, pa = stats.pearsonr(ag[col], ag.ratio)\n        out.append((lab, r, p, adj_r2(r, len(sub)), ra, pa, adj_r2(ra, len(ag))))\n    tab2 = pd.DataFrame(out, columns=[\"variable\", \"r\", \"p\", \"adjR2\", \"r_agg\", \"p_agg\", \"adjR2_agg\"])\n    print(f\"\\n{name} (n = {len(sub)}), y = asymptotic SNR ratio unshuffled/shuffled\")\n    print(tab2.sort_values(\"adjR2\", ascending=False).round(4).to_string(index=False))\nr, p = stats.pearsonr(LS.fixed_nsv_200, LS.ratio)\nag = LS.groupby(\"mouse\")[[\"fixed_nsv_200\", \"ratio\"]].mean()\nra, pa = stats.pearsonr(ag.fixed_nsv_200, ag.ratio)\nprint(f\"\\nNSV at a fixed 200 neurons (100 subsets) vs ratio: sessions r = {r:.3f}, p = {p:.2e}; \"\n      f\"animals r = {ra:.3f}, p = {pa:.4f}\")\n\n# %% [markdown]\n# RESULT_suppl-table2-nsv-best-predictor\n\n# %% [markdown]\n# ## pf-width-variance-not-predictive\n#\n# > The variance of place-field widths or amplitudes does not directly correlate with the effect\n# > of noise correlations on information saturation.\n\n# %% tags=[\"claim:pf-width-variance-not-predictive\"]\ndef var_amp(i):\n    T, d = TENS[i]\n    return np.var(np.concatenate([T[:, :, d == s].mean(axis=2).max(axis=1) for s in (1, -1)]), ddof=1)\n\nLS[\"var_amp\"] = [var_amp(i) for i in LARGE]\nfor col in (\"var_fwhm_cm\", \"var_amp\"):\n    for name, sub in ((\"all 73\", LS), (\"code filters\", LS[filt])):\n        r, p = stats.pearsonr(sub[col], sub.ratio)\n        ag = sub.groupby(\"mouse\")[[col, \"ratio\"]].mean()\n        ra, pa = stats.pearsonr(ag[col], ag.ratio)\n        print(f\"{col:12s} {name:12s}: sessions r = {r:.3f}, p = {p:.3f} (n {len(sub)}); \"\n              f\"animals r = {ra:.3f}, p = {pa:.3f} (n {len(ag)})\")\n\n# %% [markdown]\n# RESULT_pf-width-variance-not-predictive\n\n# %% [markdown]\n# ## fig5cd-synthetic-narrow-widths-broader-nsv\n#\n# > In synthetic Gaussian place-field populations, a narrow distribution of field widths gives a\n# > broader distribution of PF slopes, a higher NSV, than a broad width distribution, up to ten\n# > thousand neurons.\n#\n# A simulation of the paper's model (data: elsewhere); no dataset values are used. Centres\n# uniform over the 20-bin track (continuous), amplitude 1, tuning evaluated at the 20 bin centres.\n\n# %% tags=[\"claim:fig5cd-synthetic-narrow-widths-broader-nsv\"]\nrng_5 = np.random.default_rng(55)\ncenters_x = np.arange(20) + 0.5\n\ndef sim_nsv(n_cells, halfwidths):\n    c = rng_5.uniform(0, 20, n_cells)\n    sigma = halfwidths / np.sqrt(2 * np.log(2))  # half-width at half maximum to SD\n    F = np.exp(-0.5 * ((centers_x[None, :] - c[:, None]) / sigma[:, None]) ** 2)\n    D = np.diff(F, axis=1)\n    U = D / np.linalg.norm(D, axis=0, keepdims=True)\n    return np.var(U ** 2, axis=0)  # per bin pair\n\nreadings = {\n    \"legend, uniform half-widths\": (lambda n: rng_5.uniform(0.2, 1.42, n), lambda n: rng_5.uniform(0.8, 2.0, n)),\n    \"Methods, log-normal half-widths\": (lambda n: np.exp(rng_5.normal(0, np.sqrt(0.3), n)),\n                                        lambda n: np.exp(rng_5.normal(0, np.sqrt(2.0), n))),\n}\nfor name, (narrow, broad) in readings.items():\n    a = np.array([sim_nsv(50, narrow(50)) for _ in range(1000)])\n    b = np.array([sim_nsv(50, broad(50)) for _ in range(1000)])\n    print(f\"{name}, 50 cells, 1000 simulations: median NSV narrow {np.nanmedian(a):.4f}, broad \"\n          f\"{np.nanmedian(b):.4f}; narrow higher: {np.nanmedian(a) > np.nanmedian(b)}\")\n    line = []\n    for n in (100, 1000, 10000):\n        reps = 50 if n == 10000 else 200\n        a = np.nanmean([sim_nsv(n, narrow(n)).mean() for _ in range(reps)])\n        b = np.nanmean([sim_nsv(n, broad(n)).mean() for _ in range(reps)])\n        line.append(f\"{n}: {a:.2e} vs {b:.2e}\")\n    print(\"   mean NSV narrow vs broad by ensemble size ->\", \"; \".join(line))\n\n# %% [markdown]\n# RESULT_fig5cd-synthetic-narrow-widths-broader-nsv\n\n# %% [markdown]\n# ## Summary\n#\n# SUMMARY_PLACEHOLDER\n\n# %%\nprint(f\"total run time {(time.time() - T0) / 60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n"
}
```

```
File created successfully at: entries/hazon-2022/src_nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate; cd entries/hazon-2022; sed 's/^sessions, md5, load_s = hc30.load_sessions()$/sessions, md5, load_s = hc30.load_sessions(); sessions = sessions[::8]/' src_nb1.py | sed 's/^plt.show()/plt.close("all")/' > $TMPDIR/dev_nb1.py; MPLBACKEND=Agg timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | tail -150
```

```
Wed Nov 11 19:11:55 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_nb1.py", line 17, in <module>
    import hc30
ModuleNotFoundError: No module named 'hc30'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; time MPLBACKEND=Agg PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | tail -150
```

```
distance  1: unshuffled 0.0265 +/- 0.0044   shuffled -0.00018 +/- 0.00030
  distance  2: unshuffled 0.0198 +/- 0.0055   shuffled -0.00005 +/- 0.00038
  distance  3: unshuffled 0.0138 +/- 0.0040   shuffled -0.00008 +/- 0.00018
  distance  5: unshuffled 0.0095 +/- 0.0039   shuffled 0.00015 +/- 0.00040
  distance 10: unshuffled 0.0043 +/- 0.0036   shuffled -0.00038 +/- 0.00050
  distance 15: unshuffled 0.0016 +/- 0.0025   shuffled -0.00042 +/- 0.00046
  distance 19: unshuffled 0.0128 +/- 0.0045   shuffled -0.00001 +/- 0.00041
  distance 0 vs mean of distances >= 10: 0.0340 vs 0.0055
  shuffled below unshuffled with non-overlapping intervals at every distance 0..10: True
  pooled pairs: distance 0 0.0321, >= 10 0.0050; separated 0..10: True
  joined distances (code variant), first values: [0.0302 0.0231 0.0168 0.0123]

leftward: mean over sessions (95% interval)
  distance  0: unshuffled 0.0391 +/- 0.0082   shuffled 0.00011 +/- 0.00029
  distance  1: unshuffled 0.0254 +/- 0.0047   shuffled -0.00014 +/- 0.00038
  distance  2: unshuffled 0.0205 +/- 0.0048   shuffled 0.00012 +/- 0.00020
  distance  3: unshuffled 0.0173 +/- 0.0052   shuffled -0.00051 +/- 0.00033
  distance  5: unshuffled 0.0075 +/- 0.0024   shuffled -0.00007 +/- 0.00038
  distance 10: unshuffled 0.0034 +/- 0.0026   shuffled -0.00011 +/- 0.00046
  distance 15: unshuffled 0.0068 +/- 0.0059   shuffled -0.00022 +/- 0.00034
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; sed -i 's/^import collections$/import os\nfor _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):\n    os.environ[_v] = "1"  # one thread per process; the analyses run in 3 processes\nimport collections/' src_nb1.py; head -20 src_nb1.py | tail -8; sed 's/^sessions, md5, load_s = hc30.load_sessions()$/sessions, md5, load_s = hc30.load_sessions(); sessions = sessions[::8]/' src_nb1.py | sed 's/^plt.show()/plt.close("all")/' > $TMPDIR/dev_nb1.py; time MPLBACKEND=Agg PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | head -120
```

```
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import hc30
/tmp/claude-1001/dev_nb1.py:287: OptimizeWarning: Covariance of the parameters could not be estimated
  fit, _ = curve_fit(gauss, xb, y, p0=[y.max() - y.min(), y.argmax(), 2.0, y.min()],
streamed and parsed event_traces.mat in 4 s; md5 fe0f5dd2fca6d64dbf0cd3f35e31e1f0 (matches checksums.md5)
sessions 14 mice 9
           sessions  neurons  large  trials_med
mouse                                          
Mouse2011         1      249      1        67.0
Mouse2012         3      522      0        72.0
Mouse2021         1      441      1       187.0
Mouse2022         1      224      1       144.0
Mouse2023         1      188      0        72.0
Mouse2024         2      711      2        98.0
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; cat > $TMPDIR/t8.py <<'EOF'
import os
for v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS"): os.environ[v]="1"
import time, numpy as np, pickle, hc30
S=pickle.load(open(os.environ['TMPDIR']+'/S.pkl','rb'))[::8]
tot=0
for s in S:
    T,d,tr=hc30.session_tensor(s); rng=np.random.default_rng(0)
    idx=hc30.equalize_trials(d,rng); T=T[:,:,idx]; d=d[idx]
    t=time.time(); a=hc30.decode_once(T,d,rng,False,C=1); b=hc30.decode_once(T,d,rng,True,C=1); dt=time.time()-t; tot+=dt
    t=time.time(); sub=rng.choice(T.shape[0],10,replace=False); c=hc30.decode_once(T[sub],d,rng,False,C=1); dt2=time.time()-t
    print(T.shape, round(np.sqrt(a),2), round(np.sqrt(b),2), round(dt,2), 'n10', round(dt2,2))
print('mean per session both conds', tot/len(S))
EOF
PYTHONPATH=. python $TMPDIR/t8.py
```

```
(188, 20, 144) 10.49 6.02 0.51 n10 0.12
(422, 20, 168) 7.22 3.27 0.41 n10 0.16
(289, 20, 224) 8.34 4.2 0.7 n10 0.33
(240, 20, 326) 7.99 4.34 1.48 n10 0.8
(257, 20, 356) 5.89 3.71 1.68 n10 0.83
(200, 20, 94) 14.73 5.67 0.14 n10 0.07
(162, 20, 144) 9.69 6.12 0.28 n10 0.13
(160, 20, 200) 9.74 5.92 0.61 n10 0.25
(224, 20, 288) 8.06 4.37 1.22 n10 0.61
(187, 20, 210) 11.84 6.26 0.63 n10 0.34
(237, 20, 192) 10.72 4.92 0.51 n10 0.24
(249, 20, 134) 7.64 3.95 0.24 n10 0.13
(441, 20, 374) 17.55 6.86 2.91 n10 1.2
(190, 20, 266) 10.67 6.33 1.09 n10 0.46
mean per session both conds 0.887128472328186
```

**Agent calls Bash**

```bash
grep -n "Supplementary Figure 9\|Supplementary Figure 8\|Supplementary Figure 7\|Supplementary Figure 11\|Supplementary Figure 10" paper/10.1038-s41467-022-31254-y.txt | head; sed -n '/^Supplementary Figure 7: /,/^Supplementary Figure 12/p' paper/10.1038-s41467-022-31254-y.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^Supplementary Figure 7: /,/^Supplementary Figure 12/' paper/10.1038-s41467-022-31254-y.txt | head -90
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat >> entries/hazon-2022/hc30.py <<'EOF'


# ---- decoding jobs ----

def decode_full(T, d, seed, reps, C=1.0):
    """All neurons, all equalised trials ([claims] fig2d criterion; code mean_rms_all_sess.mlx
    reads the 'max' neurons and 'max' trials rows): per repetition a new random trial split,
    unshuffled and shuffled two-fold decoding. Returns per-repetition MSE (cm^2) of each, the
    40 x 40 confusion counts of each over all test samples, and the sum and count of squared
    errors per true class."""
    rng = np.random.default_rng(seed)
    out = dict(mse_u=[], mse_s=[], conf_u=np.zeros((40, 40)), conf_s=np.zeros((40, 40)))
    for _ in range(reps):
        idx = equalize_trials(d, rng)
        for tag, sh in (("u", False), ("s", True)):
            mse, y, p = decode_once(T[:, :, idx], d[idx], rng, sh, C=C, return_pred=True)
            out[f"mse_{tag}"].append(mse)
            np.add.at(out[f"conf_{tag}"], (y, p), 1)
    return out


def decode_series(T, d, seed, sizes, reps, C=1.0):
    """IMSE against ensemble size ([claims] common method, code decode_series): for each size,
    `reps` random neuron subsets, each with new equalised trials and split; IMSE = 1/MSE per
    subset (MSE in cm^2), averaged over subsets. Returns arrays (sizes,) for unshuffled and
    shuffled."""
    rng = np.random.default_rng(seed)
    N = T.shape[0]
    iu, is_ = [], []
    for n in sizes:
        a, b = [], []
        for _ in range(reps):
            idx = equalize_trials(d, rng)
            sub = rng.choice(N, n, replace=False)
            Tc = T[sub][:, :, idx]
            a.append(1 / decode_once(Tc, d[idx], rng, False, C=C))
            b.append(1 / decode_once(Tc, d[idx], rng, True, C=C))
        iu.append(np.mean(a))
        is_.append(np.mean(b))
    return np.array(iu), np.array(is_)


def decode_bins(sess, n_bins, seed, reps, C=1.0):
    """Unshuffled decoding with all neurons and `n_bins` bins per direction; RMS error (cm)
    relative to the continuous position ([claims] suppl6 criterion): the true position of a
    sample is the mean position (cm, from the 5th percentile) over the trial's frames in the
    bin; the prediction is (a) the predicted bin's centre or (b) the mean true position of the
    training samples of the predicted class. Returns per-repetition RMS of (a) and (b)."""
    tr = select_trials(sess["position"], n_bins)
    X = event_trace(sess["events"])
    T = build_tensor(X, tr, n_bins)
    pos_cm = (sess["position"] - tr["lo"]) * tr["cpp"]
    Pt = build_tensor(pos_cm[:, None], tr, n_bins)[0]  # bins x trials
    d = tr["direction"]
    width = TRACK_CM / n_bins
    rng = np.random.default_rng(seed)
    ra, rb = [], []
    for _ in range(reps):
        idx = equalize_trials(d, rng)
        Tc, dc, Pc = T[:, :, idx], d[idx], Pt[:, idx]
        first = half_split(dc, rng)
        sq_a, sq_b = [], []
        for tr_sel, te_sel in ((first, ~first), (~first, first)):
            Xa, ya = to_dataset(Tc[:, :, tr_sel], dc[tr_sel])
            Xb, yb = to_dataset(Tc[:, :, te_sel], dc[te_sel])
            pa = Pc[:, tr_sel].T.reshape(-1)  # same order as to_dataset (trial-major)
            pb = Pc[:, te_sel].T.reshape(-1)
            p = OvOLinearSVM(C).fit(Xa, ya).predict(Xb)
            centre = (p // 2 + 0.5) * width
            cls_mean = np.array([pa[ya == c].mean() if (ya == c).any() else np.nan
                                 for c in range(2 * n_bins)])
            sq_a.append((centre - pb) ** 2)
            sq_b.append((cls_mean[p] - pb) ** 2)
        ra.append(np.sqrt(np.mean(np.concatenate(sq_a))))
        rb.append(np.sqrt(np.nanmean(np.concatenate(sq_b))))
    return np.array(ra), np.array(rb)


def performance(position, tr, cutoff_cm=5.9):
    """Task performance, correct over total runs ([claims] suppl8 criterion; code
    error_trial_counter.m): slow runs (speed below 4 cm/s) and turn-arounds between the two
    5.9 cm milestones count as errors; correct runs are the valid trials."""
    cpp, vel = tr["cpp"], tr["vel"]
    cm = (position - tr["lo"]) * cpp
    cm[cm < 0] = 0
    right_m = cutoff_cm
    left_m = (tr["hi"] - tr["lo"]) * cpp - cutoff_cm
    slow = np.abs(vel) < V_THRESH
    states = (cm > left_m) * 10 + (cm < right_m) * 1 + slow * 100
    n_slow = n_turn = 0
    state, was_slow = "none", False
    for s in states:
        if s == 101:
            if state == "leftward" and was_slow:
                n_slow += 1
            elif state == "rightward" and was_slow:
                n_turn += 1
            state, was_slow = "rightward", False
        elif s == 110:
            if state == "rightward" and was_slow:
                n_slow += 1
            elif state == "leftward" and was_slow:
                n_turn += 1
            state, was_slow = "leftward", False
        elif s == 100:
            was_slow = True
    n_correct = len(tr["starts"])
    return n_correct / (n_correct + n_slow + n_turn), n_slow, n_turn


def single_cell_snr(T, d):
    """Mean over neurons of the single-cell SNR ([claims] suppl11b criterion). Per neuron,
    per direction and adjacent bin pair: signal (difference of trial means)^2 and noise (mean of
    the two bins' trial variances). Main reading (Methods): median over pairs of signal over
    median over pairs of noise. Variants (code single_cell_d_primes2): mean, and median, of the
    per-pair ratio."""
    sig, noi = [], []
    for dirn in (-1, 1):
        A = T[:, :, d == dirn]
        sig.append(np.diff(A.mean(axis=2), axis=1) ** 2)
        v = A.var(axis=2, ddof=1)
        noi.append((v[:, :-1] + v[:, 1:]) / 2)
    sig, noi = np.concatenate(sig, axis=1), np.concatenate(noi, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        main = np.median(sig, axis=1) / np.median(noi, axis=1)
        ratio = sig / noi
    return (np.nanmean(np.where(np.isfinite(main), main, np.nan)),
            np.nanmean(np.nanmean(np.where(np.isfinite(ratio), ratio, np.nan), axis=1)),
            np.nanmean(np.nanmedian(np.where(np.isfinite(ratio), ratio, np.nan), axis=1)))
EOF
date -u
```

```
Wed Nov 11 19:21:10 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/hazon-2022/src_nb2.py",
 "content": "# %% [markdown]\n# # Reproducing Hazon et al. (2022) from CRCNS hc-30: position decoding\n#\n# HEADER_PLACEHOLDER\n\n# %%\nimport os\nfor _v in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ[_v] = \"1\"  # one thread per process; the decoders run in 3 processes\nimport multiprocessing as mp\nimport resource\nimport time\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport hc30\n\nT0 = time.time()\nsessions, md5, load_s = hc30.load_sessions()\nprint(f\"streamed and parsed event_traces.mat in {load_s:.0f} s; md5 {md5} \"\n      f\"({'matches' if md5 == hc30.MD5 else 'DIFFERS FROM'} checksums.md5)\")\n\n# Settings of this notebook (the paper's values in brackets)\nREPS_FULL = 12   # repetitions with all neurons [80]\nREPS_SUB = 4     # neuron subsets per ensemble size [80]\nSIZES = [1, 10, 20, 30, 50, 75, 100, 150, 200, 250, 300, 400]  # plus all neurons [1, 10, 20, ...]\nBIN_COUNTS = [10, 15, 20, 25, 30, 40]  # Supplementary Figure 6 [not stated]\nREPS_BINS = 2    # [80]\nC_SVM = 1.0      # assumed; see hc30.OvOLinearSVM\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nrows, TENS = [], []\nfor i, s in enumerate(sessions):\n    T, d, tr = hc30.session_tensor(s)\n    TENS.append((T, d))\n    perf, n_slow, n_turn = hc30.performance(s[\"position\"], tr)\n    rows.append(dict(i=i, mouse=s[\"mouse\"], session=s[\"session_id\"], neurons=T.shape[0],\n                     right=int((d == 1).sum()), left=int((d == -1).sum()), performance=perf,\n                     slow_errors=n_slow, turn_errors=n_turn))\ninfo = pd.DataFrame(rows)\ninfo[\"min_trials\"] = info[[\"right\", \"left\"]].min(axis=1)\ninfo[\"large\"] = (info.neurons > 200) & (info.min_trials > 30)\nLARGE = info.index[info.large].values\nprint(f\"sessions {len(info)}, mice {info.mouse.nunique()}, neurons {info.neurons.sum()}, \"\n      f\"large-data sessions {len(LARGE)} from {info.loc[LARGE, 'mouse'].nunique()} mice\")\nprint(\"trials per direction used by the decoder (smaller of the two): median %d, range %d to %d\"\n      % (info.min_trials.median(), info.min_trials.min(), info.min_trials.max()))\nprint(\"performance: median %.3f, range %.3f to %.3f; slow errors median %d, turn-around errors \"\n      \"median %d\" % (info.performance.median(), info.performance.min(), info.performance.max(),\n                     info.slow_errors.median(), info.turn_errors.median()))\n\n# %% tags=[\"sanity\"]\n# Cost estimate before the full run: one repetition on the first session of each mouse.\nt = time.time()\nprobe = info.groupby(\"mouse\").i.first().values\nfor i in probe:\n    T, d = TENS[i]\n    hc30.decode_full(T, d, seed=0, reps=1, C=C_SVM)\nper_rep = (time.time() - t) / len(probe)\nn_sizes = sum(sum(1 for s in SIZES if s < n) for n in info.neurons)\nest = per_rep * (len(info) * REPS_FULL + 0.6 * n_sizes * REPS_SUB) / 3 / 60\nprint(f\"{per_rep:.2f} s per repetition (both conditions, all neurons); estimated decoding time \"\n      f\"{est:.0f} min on 3 processes, before the bin-count variant\")\n\n# %% [markdown]\n# ## Decoding runs\n#\n# Every session: REPS_FULL repetitions with all neurons, and REPS_SUB subsets at each ensemble\n# size below the session's neuron count. Each session has its own seed.\n\n# %%\ndef job(i):\n    T, d = TENS[i]\n    full = hc30.decode_full(T, d, seed=20000 + i, reps=REPS_FULL, C=C_SVM)\n    sizes = [s for s in SIZES if s < T.shape[0]]\n    iu, is_ = hc30.decode_series(T, d, seed=30000 + i, sizes=sizes, reps=REPS_SUB, C=C_SVM)\n    full[\"sizes\"] = np.array(sizes + [T.shape[0]])\n    full[\"imse_u\"] = np.r_[iu, np.mean(1 / np.array(full[\"mse_u\"]))]\n    full[\"imse_s\"] = np.r_[is_, np.mean(1 / np.array(full[\"mse_s\"]))]\n    return full\n\nt = time.time()\nwith mp.get_context(\"fork\").Pool(3) as pool:\n    DEC = pool.map(job, range(len(TENS)), chunksize=1)\nprint(f\"decoding: {(time.time() - t) / 60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n\n# %% [markdown]\n# ## fig2d-rms-error-ensemble-vs-shuffled\n#\n# > The RMS decoding error with all neurons is 9.38 +/- 4.06 cm with noise correlations and\n# > 5.15 +/- 2.40 cm after trial shuffling (median +/- IQR over 110 sessions), so noise\n# > correlations impair position estimates.\n\n# %% tags=[\"claim:fig2d-rms-error-ensemble-vs-shuffled\"]\ninfo[\"rms_u\"] = [np.mean(np.sqrt(r[\"mse_u\"])) for r in DEC]\ninfo[\"rms_s\"] = [np.mean(np.sqrt(r[\"mse_s\"])) for r in DEC]\nfor col, name in ((\"rms_u\", \"ensemble\"), (\"rms_s\", \"shuffled\")):\n    q1, q3 = np.percentile(info[col], [25, 75])\n    print(f\"{name}: median {info[col].median():.2f} cm, IQR {q3 - q1:.2f} cm \"\n          f\"(quartiles {q1:.2f} to {q3:.2f}), range {info[col].min():.2f} to {info[col].max():.2f}\")\nprint(\"ensemble error larger than shuffled in\", int((info.rms_u > info.rms_s).sum()), \"of\",\n      len(info), \"sessions; Wilcoxon p = %.1e\" % stats.wilcoxon(info.rms_u, info.rms_s).pvalue)\nprint(\"spread over repetitions within a session (SD of RMS), median: ensemble %.2f, shuffled %.2f cm\"\n      % (np.median([np.std(np.sqrt(r[\"mse_u\"])) for r in DEC]),\n         np.median([np.std(np.sqrt(r[\"mse_s\"])) for r in DEC])))\nprint(info.groupby(\"mouse\")[[\"rms_u\", \"rms_s\"]].median().round(2))\n\n# %% [markdown]\n# Variant: the decoder's regularisation. On the first session of each mouse, 2 repetitions with\n# C = 0.1 and C = 10 against the main C = 1.\n\n# %% tags=[\"claim:fig2d-rms-error-ensemble-vs-shuffled\"]\ndef c_variant(args):\n    i, C = args\n    T, d = TENS[i]\n    r = hc30.decode_full(T, d, seed=40000 + i, reps=2, C=C)\n    return i, C, np.mean(np.sqrt(r[\"mse_u\"])), np.mean(np.sqrt(r[\"mse_s\"]))\n\nwith mp.get_context(\"fork\").Pool(3) as pool:\n    CV = pool.map(c_variant, [(i, C) for i in probe for C in (0.1, 10.0)], chunksize=1)\ncv = pd.DataFrame(CV, columns=[\"i\", \"C\", \"rms_u\", \"rms_s\"])\ncv = pd.concat([cv, pd.DataFrame({\"i\": probe, \"C\": 1.0, \"rms_u\": info.rms_u[probe].values,\n                                  \"rms_s\": info.rms_s[probe].values})])\nprint(cv.groupby(\"C\")[[\"rms_u\", \"rms_s\"]].median().round(2))\n\n# %% [markdown]\n# RESULT_fig2d-rms-error-ensemble-vs-shuffled\n\n# %% [markdown]\n# ## fig2cd-shuffle-better-in-all-bins\n#\n# > Decoding is less accurate with noise correlations than without in every spatial bin;\n# > misclassifications are typically one bin and reach up to three bins.\n\n# %% tags=[\"claim:fig2cd-shuffle-better-in-all-bins\"]\ndef per_bin_rms(conf):\n    pos = np.arange(40) // 2\n    err2 = (pos[:, None] - pos[None, :]) ** 2 * hc30.BIN_CM ** 2\n    by_class = np.sqrt((conf * err2).sum(1) / conf.sum(1))\n    by_pos = np.sqrt(np.array([(conf[2 * b:2 * b + 2] * err2[2 * b:2 * b + 2]).sum()\n                               / conf[2 * b:2 * b + 2].sum() for b in range(20)]))\n    return by_pos, by_class\n\nBu, Bs, Cu, Cs, accu, accs = [], [], [], [], [], []\nfor r in DEC:\n    a, b = per_bin_rms(r[\"conf_u\"])\n    c, e = per_bin_rms(r[\"conf_s\"])\n    Bu.append(a); Cu.append(b); Bs.append(c); Cs.append(e)\n    accu.append(np.diag(r[\"conf_u\"]) / r[\"conf_u\"].sum(1))\n    accs.append(np.diag(r[\"conf_s\"]) / r[\"conf_s\"].sum(1))\nBu, Bs, Cu, Cs = map(np.array, (Bu, Bs, Cu, Cs))\naccu, accs = np.array(accu), np.array(accs)\nprint(\"(a) 20 positions: session-mean RMS larger for the ensemble in\",\n      int((Bu.mean(0) > Bs.mean(0)).sum()), \"of 20 bins\")\nprint(\"    ensemble\", np.round(Bu.mean(0), 1))\nprint(\"    shuffled\", np.round(Bs.mean(0), 1))\nprint(\"(b) 40 classes: larger for the ensemble in\", int((Cu.mean(0) > Cs.mean(0)).sum()), \"of 40\")\nprint(\"correct-class fraction, session average: higher for shuffled in\",\n      int((accs.mean(0) > accu.mean(0)).sum()), \"of 40 classes\")\nex = info.index[(info.mouse == \"Mouse2022\")].values\nprint(\"sessions of animal 2022:\", list(ex))\nfor i in ex:\n    print(f\"  session {i} ({info.session[i]}): correct fraction higher for shuffled in \"\n          f\"{int((accs[i] > accu[i]).sum())} of 40 classes; ties {int((accs[i] == accu[i]).sum())}\")\n# size of errors\nfor tag in (\"u\", \"s\"):\n    conf = sum(r[f\"conf_{tag}\"] for r in DEC)\n    pos = np.arange(40) // 2\n    dist = np.abs(pos[:, None] - pos[None, :])\n    mis = conf * (dist > 0)\n    hist = np.bincount(dist.ravel(), weights=mis.ravel(), minlength=20)\n    frac = hist / hist.sum()\n    cum = np.cumsum(frac[1:] * 1.0)\n    med = int(np.searchsorted(cum, 0.5) + 1)\n    largest = int(np.max(np.where(frac >= 0.01)[0]))\n    print(f\"{'ensemble' if tag == 'u' else 'shuffled'}: misclassified samples {int(hist.sum())}; \"\n          f\"median error {med} bin(s); largest error with >= 1% of them {largest} bins; \"\n          f\"fractions at 1..4 bins {np.round(frac[1:5], 3)}\")\nfig, ax = plt.subplots(figsize=(5, 3))\nx = np.arange(20) + 1\nfor B, lab in ((Bu, \"ensemble\"), (Bs, \"shuffled\")):\n    m = B.mean(0)\n    ci = 1.96 * B.std(0, ddof=1) / np.sqrt(len(B))\n    ax.plot(x, m, label=lab)\n    ax.fill_between(x, m - ci, m + ci, alpha=0.3)\nax.set_xlabel(\"spatial bin\"); ax.set_ylabel(\"RMS error (cm)\"); ax.legend()\nplt.show()\nprint(\"plotted range %.1f to %.1f cm\" % (min(Bu.mean(0).min(), Bs.mean(0).min()),\n                                       max(Bu.mean(0).max(), Bs.mean(0).max())))\n\n# %% [markdown]\n# RESULT_fig2cd-shuffle-better-in-all-bins\n\n# %% [markdown]\n# ## fig2ef-imse-saturates-with-correlations\n#\n# > With noise correlations the decoding accuracy (IMSE) approaches a bound as ensembles grow,\n# > while without them it keeps increasing; the asymptotic IMSE (I0 N) and the saturation size\n# > N are larger for the shuffled data.\n\n# %% tags=[\"claim:fig2ef-imse-saturates-with-correlations\"]\nfits = []\nfor i, r in enumerate(DEC):\n    I0, N, I0c, Nc = hc30.fit_imse(r[\"sizes\"], r[\"imse_u\"])\n    I0s, Ns, I0sc, Nsc = hc30.fit_imse(r[\"sizes\"], r[\"imse_s\"])\n    fits.append(dict(I0=I0, N=N, I0N=I0 * N, I0_ci=I0c, N_ci=Nc, I0s=I0s, Ns=Ns, I0Ns=I0s * Ns,\n                     I0s_ci=I0sc, Ns_ci=Nsc))\nF = pd.DataFrame(fits)\ninfo = pd.concat([info, F], axis=1)\nprint(\"fits failed: unshuffled\", int(F.N.isna().sum()), \"shuffled\", int(F.Ns.isna().sum()))\nprint(\"negative or absurd fits (N < 0 or N > 1e6): unshuffled\", int(((F.N < 0) | (F.N > 1e6)).sum()),\n      \"shuffled\", int(((F.Ns < 0) | (F.Ns > 1e6)).sum()))\nprint(F[[\"I0\", \"N\", \"I0N\", \"I0s\", \"Ns\", \"I0Ns\"]].describe().round(5).T)\n\ndef two_tests(df, label):\n    a = stats.wilcoxon(df.I0N, df.I0Ns)\n    b = stats.wilcoxon(df.N, df.Ns)\n    print(f\"{label}: I0 N shuffled higher in {int((df.I0Ns > df.I0N).sum())} of {len(df)}, \"\n          f\"p = {a.pvalue:.2e}; N shuffled higher in {int((df.Ns > df.N).sum())} of {len(df)}, \"\n          f\"p = {b.pvalue:.2e}\")\n\nok = F.notna().all(axis=1)\ntwo_tests(info[ok], \"110 sessions\")\npm = info[ok].groupby(\"mouse\")[[\"I0N\", \"I0Ns\", \"N\", \"Ns\"]].mean()\ntwo_tests(pm, \"12 per-animal means\")\nprint(\"animals with higher mean I0 N for shuffled:\", int((pm.I0Ns > pm.I0N).sum()), \"of\", len(pm))\nprint(pm.round(4))\n# saturation: does unshuffled IMSE at the largest size fall short of the fitted asymptote?\nfrac_u = [r[\"imse_u\"][-1] / (f[\"I0N\"]) for r, f in zip(DEC, fits)]\nfrac_s = [r[\"imse_s\"][-1] / (f[\"I0Ns\"]) for r, f in zip(DEC, fits)]\nprint(f\"IMSE at all neurons as a fraction of the fitted asymptote: median unshuffled \"\n      f\"{np.nanmedian(frac_u):.2f}, shuffled {np.nanmedian(frac_s):.2f}\")\nfig, ax = plt.subplots(figsize=(5, 3))\nk = int(info.neurons.idxmax())\nax.plot(DEC[k][\"sizes\"], DEC[k][\"imse_u\"], \"o-\", label=\"ensemble\")\nax.plot(DEC[k][\"sizes\"], DEC[k][\"imse_s\"], \"o-\", label=\"shuffled\")\nax.set_xlabel(\"neurons\"); ax.set_ylabel(\"IMSE (1/cm^2)\"); ax.legend(); ax.set_title(f\"session {k}\")\nplt.show()\nprint(\"plotted IMSE range %.4f to %.4f\" % (min(DEC[k][\"imse_u\"].min(), DEC[k][\"imse_s\"].min()),\n                                          max(DEC[k][\"imse_u\"].max(), DEC[k][\"imse_s\"].max())))\n\n# %% [markdown]\n# RESULT_fig2ef-imse-saturates-with-correlations\n\n# %% [markdown]\n# ## suppl7b-initial-slope-lower-with-correlations\n#\n# > The initial slope I0 of the IMSE curve differs significantly between unshuffled and shuffled\n# > data across all sessions, which the paper attributes to an artifactual sublinear growth of\n# > accuracy at small ensemble sizes.\n\n# %% tags=[\"claim:suppl7b-initial-slope-lower-with-correlations\"]\nw = stats.wilcoxon(info.I0[ok], info.I0s[ok])\nprint(f\"I0 median unshuffled {info.I0[ok].median():.5f}, shuffled {info.I0s[ok].median():.5f}; \"\n      f\"shuffled higher in {int((info.I0s[ok] > info.I0[ok]).sum())} of {int(ok.sum())}; \"\n      f\"Wilcoxon p = {w.pvalue:.2e}\")\n\n# %% [markdown]\n# RESULT_suppl7b-initial-slope-lower-with-correlations\n\n# %% [markdown]\n# ## saturation-ensemble-size\n#\n# > Spatial accuracy approaches saturation (fitted slope 5% of I0) at 346 to 1402 neurons\n# > across animals, and reaches 95% of the asymptotic IMSE at 1894 to 7671 neurons.\n\n# %% tags=[\"claim:saturation-ensemble-size\"]\ndef gmean(x):\n    x = np.asarray(x, float)\n    x = x[np.isfinite(x) & (x > 0)]\n    return np.exp(np.log(x).mean())\n\nfor name, sel in ((\"(a) 73 large-data sessions\", info.large & ok), (\"(b) 110 working sessions\", ok)):\n    g = info[sel].groupby(\"mouse\").N.apply(gmean)\n    lo, hi = g.min(), g.max()\n    print(f\"{name}: {len(g)} mice; geometric-mean N {lo:.0f} to {hi:.0f}; 5% slope at \"\n          f\"{lo * (np.sqrt(20) - 1):.0f} to {hi * (np.sqrt(20) - 1):.0f} neurons; 95% of asymptote \"\n          f\"at {19 * lo:.0f} to {19 * hi:.0f}\")\n    print(\"   per mouse N:\", g.round(0).to_dict())\nprint(\"sessions with N <= 0 left out of the geometric means:\", int((info.N[ok] <= 0).sum()))\n\n# %% [markdown]\n# RESULT_saturation-ensemble-size\n\n# %% [markdown]\n# ## Asymptotic SNR of the large-data sessions (as in the first notebook)\n#\n# The same function, seeds and settings as the first notebook (20 subsets per size), so the\n# values are the same.\n\n# %%\ndef _sn(i):\n    T, d = TENS[i]\n    sizes, P, M = hc30.signal_noise_series(T, d, seed=1000 + i, n_subsets=20)\n    sig, _ = hc30.slope_with_se(sizes, M[0])\n    noi, _ = hc30.slope_with_se(sizes, M[1])\n    return sig / noi\n\nt = time.time()\nwith mp.get_context(\"fork\").Pool(3) as pool:\n    asnr = pool.map(_sn, list(LARGE), chunksize=1)\ninfo.loc[LARGE, \"asnr\"] = asnr\nprint(f\"asymptotic SNR of {len(LARGE)} sessions in {time.time() - t:.0f} s; median {np.median(asnr):.3f}\")\n\n# %% [markdown]\n# ## suppl11b-i0-vs-single-cell-snr\n#\n# > Across mice, the initial slope I0 of the IMSE curve correlates with the average single-cell\n# > SNR (r squared 0.73, p < 0.01).\n\n# %% tags=[\"claim:suppl11b-i0-vs-single-cell-snr\"]\nscs = np.array([hc30.single_cell_snr(*TENS[i]) for i in LARGE])\nL = info.loc[LARGE].copy()\nL[\"scs_main\"], L[\"scs_mean\"], L[\"scs_median\"] = scs[:, 0], scs[:, 1], scs[:, 2]\nag = L.groupby(\"mouse\").mean(numeric_only=True)\nfor col in (\"scs_main\", \"scs_mean\", \"scs_median\"):\n    r, p = stats.pearsonr(ag[col], ag.I0)\n    print(f\"{col}: across {len(ag)} mice r = {r:.3f}, r^2 = {r * r:.3f}, p = {p:.4f}\")\nprint(ag[[\"I0\", \"scs_main\", \"scs_mean\"]].round(5))\n\n# %% [markdown]\n# RESULT_suppl11b-i0-vs-single-cell-snr\n\n# %% [markdown]\n# ## suppl11c-asymptotic-imse-vs-asymptotic-snr\n#\n# > Across mice, the fitted asymptotic IMSE (I0 N) correlates with the asymptotic SNR (r squared\n# > 0.88).\n\n# %% tags=[\"claim:suppl11c-asymptotic-imse-vs-asymptotic-snr\"]\nLok = L[np.isfinite(L.I0N)]\nag = Lok.groupby(\"mouse\")[[\"I0N\", \"asnr\"]].mean()\nr, p = stats.pearsonr(ag.I0N, ag.asnr)\nprint(f\"linear: across {len(ag)} mice r = {r:.3f}, r^2 = {r * r:.3f}, p = {p:.2e}\")\nagl = Lok.assign(lI=np.log10(Lok.I0N.where(Lok.I0N > 0)), la=np.log10(Lok.asnr)).groupby(\"mouse\")[[\"lI\", \"la\"]].mean()\nr, p = stats.pearsonr(agl.lI, agl.la)\nprint(f\"log10:  across {len(agl)} mice r = {r:.3f}, r^2 = {r * r:.3f}, p = {p:.2e}\")\nr, p = stats.pearsonr(Lok.I0N, Lok.asnr)\nprint(f\"across {len(Lok)} sessions, linear r = {r:.3f}, p = {p:.2e}\")\n\n# %% [markdown]\n# RESULT_suppl11c-asymptotic-imse-vs-asymptotic-snr\n\n# %% [markdown]\n# ## suppl8-task-performance-and-accuracy\n#\n# > Task performance correlates with the number of trials (r 0.85) and with asymptotic decoding\n# > accuracy (r 0.52); the number of trials correlates weakly with accuracy (r 0.34), and a path\n# > analysis shows performance predicts accuracy while trial number does not.\n\n# %% tags=[\"claim:suppl8-task-performance-and-accuracy\"]\nimport statsmodels.api as sm\n\nL[\"n_trials\"] = L.right + L.left\nLp = L[np.isfinite(L.I0N) & (L.I0N > 0)].copy()\nLp[\"log_I0N\"] = np.log10(Lp.I0N)\nprint(f\"{len(Lp)} sessions (of {len(L)}) with a positive I0 N\")\nr, p = stats.pearsonr(Lp.performance, Lp.n_trials)\nprint(f\"performance vs trials: r = {r:.3f}, p = {p:.1e}\")\nfor acc in (\"log_I0N\", \"I0N\"):\n    r1, p1 = stats.pearsonr(Lp[acc], Lp.n_trials)\n    r2, p2 = stats.pearsonr(Lp[acc], Lp.performance)\n    print(f\"{acc}: vs trials r = {r1:.3f} (p {p1:.1e}); vs performance r = {r2:.3f} (p {p2:.1e})\")\nX = sm.add_constant(Lp[[\"n_trials\", \"performance\"]])\nmod = sm.OLS(Lp.log_I0N, X).fit()\nprint(\"path model, log10 I0 N ~ trials + performance:\")\nprint(mod.summary2().tables[1][[\"Coef.\", \"Std.Err.\", \"P>|t|\"]].round(5))\nprint(\"performance range %.3f to %.3f; trials %d to %d\" % (Lp.performance.min(), Lp.performance.max(),\n                                                           Lp.n_trials.min(), Lp.n_trials.max()))\n\n# %% [markdown]\n# RESULT_suppl8-task-performance-and-accuracy\n\n# %% [markdown]\n# ## suppl6-twenty-bins-near-optimal\n#\n# > Twenty spatial bins give close to the smallest decoding error relative to the continuous\n# > position (11.75 cm, 95% CI 10.33 to 13.18 cm), similar to 30 bins (11.53 cm).\n\n# %% tags=[\"claim:suppl6-twenty-bins-near-optimal\"]\ndef bins_job(args):\n    i, nb = args\n    try:\n        a, b = hc30.decode_bins(sessions[i], nb, seed=50000 + 100 * i + nb, reps=REPS_BINS, C=C_SVM)\n        return i, nb, a.mean(), b.mean()\n    except Exception as e:  # a session with too few trials visiting every bin\n        return i, nb, np.nan, np.nan\n\nt = time.time()\nwith mp.get_context(\"fork\").Pool(3) as pool:\n    BR = pool.map(bins_job, [(i, nb) for i in range(len(sessions)) for nb in BIN_COUNTS], chunksize=1)\nprint(f\"bin-count variant: {(time.time() - t) / 60:.1f} min\")\nbr = pd.DataFrame(BR, columns=[\"i\", \"bins\", \"centre\", \"class_mean\"])\nprint(\"failed (session, bins):\", br[br.centre.isna()][[\"i\", \"bins\"]].values.tolist())\nsumm = br.groupby(\"bins\").agg(n=(\"centre\", \"count\"), centre=(\"centre\", \"mean\"),\n                              sem_c=(\"centre\", lambda x: x.std(ddof=1) / np.sqrt(x.count())),\n                              class_mean=(\"class_mean\", \"mean\"),\n                              sem_m=(\"class_mean\", lambda x: x.std(ddof=1) / np.sqrt(x.count())))\nsumm[\"ci_c\"] = 1.96 * summ.sem_c\nprint(summ.round(3))\nfor col, sem in ((\"centre\", \"sem_c\"), (\"class_mean\", \"sem_m\")):\n    m20, s20 = summ.loc[20, col], summ.loc[20, sem]\n    below = summ.index[summ[col] < m20 - s20].tolist()\n    print(f\"{col}: 20 bins {m20:.2f} cm, 30 bins {summ.loc[30, col]:.2f}; bin counts more than one \"\n          f\"SEM below 20: {below}\")\n\n# %% [markdown]\n# RESULT_suppl6-twenty-bins-near-optimal\n\n# %% [markdown]\n# ## suppl9-fit-recovers-saturation\n#\n# > On simulated place cells with information-limiting input noise, the IMSE fit gives\n# > consistent saturation estimates N from ensembles of 500 and 2000 neurons.\n#\n# A simulation of the model of the Supplementary Figure 9 legend (data: elsewhere); no dataset\n# values are used. Choices the legend leaves open (standard choices named by the criterion):\n# back-and-forth runs at a constant 30 cm/s over 118 cm, frames at 20 Hz, input noise drawn\n# independently per frame, 20 bins, decoding of single frames.\n\n# %% tags=[\"claim:suppl9-fit-recovers-saturation\"]\nrng9 = np.random.default_rng(909)\nL9, FS9, SPEED = hc30.TRACK_CM, 20.0, 30.0\nn_frames = int(30 * 60 * FS9)\nphase = (np.arange(n_frames) * SPEED / FS9) % (2 * L9)\ntrue_pos = np.where(phase < L9, phase, 2 * L9 - phase)\nnoisy_pos = true_pos + rng9.normal(0, 10, n_frames)\ntrue_bin = np.clip((true_pos / L9 * 20).astype(int), 0, 19)\nsigma9 = 30 / (2 * np.sqrt(2 * np.log(2)))\n\ndef simulate(n_cells):\n    c = rng9.uniform(0, L9, n_cells)\n    rate = 0.05 * np.exp(-0.5 * ((noisy_pos[:, None] - c[None, :]) / sigma9) ** 2)\n    return rng9.poisson(rate).astype(np.int8)\n\ndef nb_imse(Y, sizes, reps):\n    \"\"\"Poisson naive Bayes on single frames, two halves of the session (first and second\n    half of the runs), errors in bins times 5.9 cm; IMSE per subset averaged over subsets.\"\"\"\n    half = np.arange(n_frames) < n_frames // 2\n    out = []\n    for n in sizes:\n        v = []\n        for _ in range(reps):\n            sub = rng9.choice(Y.shape[1], n, replace=False)\n            mses = []\n            for a, b in ((half, ~half), (~half, half)):\n                Ya, Yb = Y[a][:, sub].astype(float), Y[b][:, sub].astype(float)\n                lam = np.array([Ya[true_bin[a] == k].mean(0) for k in range(20)]) + 1e-4\n                ll = Yb @ np.log(lam).T - lam.sum(1)[None, :]\n                p = ll.argmax(1)\n                mses.append(np.mean(((p - true_bin[b]) * hc30.BIN_CM) ** 2))\n            v.append(1 / np.mean(mses))\n        out.append(np.mean(v))\n    return np.array(out)\n\nres9 = {}\nfor n_total, sizes in ((500, [1, 10, 25, 50, 100, 200, 300, 400, 500]),\n                       (2000, [1, 10, 25, 50, 100, 200, 300, 400, 500, 1000, 1500, 2000])):\n    Y = simulate(n_total)\n    im = nb_imse(Y, sizes, reps=16)\n    I0, N, I0c, Nc = hc30.fit_imse(sizes, im)\n    res9[n_total] = (N, Nc)\n    print(f\"{n_total} neurons: IMSE {np.round(im, 5)}; fit I0 = {I0:.5f}, N = {N:.0f} +/- {Nc:.0f} (95%)\")\n(N1, c1), (N2, c2) = res9[500], res9[2000]\nprint(f\"intervals overlap: {(N1 - c1) <= (N2 + c2) and (N2 - c2) <= (N1 + c1)}\")\n\n# %% [markdown]\n# RESULT_suppl9-fit-recovers-saturation\n\n# %% [markdown]\n# ## Summary\n#\n# SUMMARY_PLACEHOLDER\n\n# %%\nprint(f\"total run time {(time.time() - T0) / 60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n"
}
```

```
File created successfully at: entries/hazon-2022/src_nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; sed -e 's/^sessions, md5, load_s = hc30.load_sessions()$/sessions, md5, load_s = hc30.load_sessions(); sessions = sessions[::8]/' -e 's/^plt.show()/plt.close("all")/' -e 's/^REPS_FULL = 12/REPS_FULL = 2/' -e 's/^REPS_SUB = 4 /REPS_SUB = 1 /' -e 's/^REPS_BINS = 2 /REPS_BINS = 1 /' src_nb2.py > $TMPDIR/dev_nb2.py; time MPLBACKEND=Agg PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb2.py 2>&1 | grep -v Warning | tail -120
```

```
streamed and parsed event_traces.mat in 4 s; md5 fe0f5dd2fca6d64dbf0cd3f35e31e1f0 (matches checksums.md5)
sessions 14, mice 9, neurons 3446, large-data sessions 8 from 6 mice
trials per direction used by the decoder (smaller of the two): median 102, range 47 to 187
performance: median 0.847, range 0.623 to 0.981; slow errors median 25, turn-around errors median 12
0.95 s per repetition (both conditions, all neurons); estimated decoding time 1 min on 3 processes, before the bin-count variant
decoding: 1.5 min; peak memory 0.9 GB
ensemble: median 9.74 cm, IQR 3.29 cm (quartiles 8.33 to 11.62), range 5.67 to 17.19
shuffled: median 5.35 cm, IQR 1.65 cm (quartiles 4.45 to 6.10), range 3.41 to 6.54
ensemble error larger than shuffled in 14 of 14 sessions; Wilcoxon p = 1.2e-04
spread over repetitions within a session (SD of RMS), median: ensemble 0.29, shuffled 0.08 cm
           rms_u  rms_s
mouse                  
Mouse2011   7.26   3.94
Mouse2012   9.88   5.96
Mouse2021  17.19   6.54
Mouse2022   7.97   4.52
Mouse2023  10.05   6.08
Mouse2024   8.45   3.96
Mouse2025  11.92   6.20
Mouse2026  11.38   5.50
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; head -60 nbins_validation.m
```

```
load nbins_agg_200930-174641_0.mat

%%

nbins = res(1).nbins;
N_usable = numel(res);

for i = 1:N_usable
   mean_cerr(i,:) = squeeze(mean(res(i).c_err , 3));
end

%%
figure;

grand_mean_cerr = mean(mean_cerr);
mean_cerr_conf = sem(mean_cerr).*1.96;
serrorbar(nbins, grand_mean_cerr, mean_cerr_conf);
xlabel '# of bins'
ylabel 'RMS decoding error'
title(sprintf('Decoding error by # of bins, 80 samples per session,\nn = %d sessions (95%% CI over sessions)', N_usable));
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; grep -rln "c_err" --include=*.m . | head;
```

```
./OpenField.m
./int_time_runner.m
./bin_integration_time_checker.m
./plotting/bsep.m
./plotting/berr.m
./nbins_validation.m
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; grep -n "c_err\|nbins\|discard\|function" bin_integration_time_checker.m | head -40
```

```
1:function res = bin_integration_time_checker(i_usable, n_divs_array, integration_frames_array, reps, alg)
163:res.c_err = coordwise_error;
165:res.nbins = n_divs_array;
201:function [x, f] = denan_rows(x)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mlp; sed -n 1,165p bin_integration_time_checker.m
```

```
function res = bin_integration_time_checker(i_usable, n_divs_array, integration_frames_array, reps, alg)
if ~exist('alg', 'var')
    alg = my_algs('ecoclin');
end

ntype = 'events_transients';

t_ = tic;

[coordwise_error, binwise_error] = deal(zeros(numel(n_divs_array), numel(integration_frames_array), reps));


%i_usable = 69;
if isstruct(i_usable)
    tracesEvents = i_usable;
else
    sm = SessManager;
    data_file = sm.data_path(i_usable, 'Usable');
    load(data_file, 'tracesEvents');
end
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hazon-2022 && python3 - <<'EOF'
s=open('hc30.py').read()
old_doc='''    training samples of the predicted class. Returns per-repetition RMS of (a) and (b)."""
    tr = select_trials(sess["position"], n_bins)
    X = event_trace(sess["events"])
    T = build_tensor(X, tr, n_bins)
    pos_cm = (sess["position"] - tr["lo"]) * tr["cpp"]
    Pt = build_tensor(pos_cm[:, None], tr, n_bins)[0]  # bins x trials'''
new_doc='''    training samples of the predicted class. Returns per-repetition RMS of (a) and (b).

    Trials are those of the 20-bin selection for every bin count, and a (trial, bin) sample with
    no frame is left out ([code] bin_integration_time_checker.m, which feeds Supplementary
    Figure 6: new_sel with the default 20 bins, then NaN samples dropped by tensor2dataset)."""
    tr = select_trials(sess["position"], N_BINS)
    rng_cm = tr["hi"] - tr["lo"]
    tr = dict(tr, bins=np.clip(np.ceil(n_bins * (sess["position"] - tr["lo"]) / rng_cm)
                               .astype(int), 1, n_bins) - 1)
    X = event_trace(sess["events"])
    with np.errstate(invalid="ignore", divide="ignore"):
        T = build_tensor(X, tr, n_bins)
        pos_cm = (sess["position"] - tr["lo"]) * tr["cpp"]
        Pt = build_tensor(pos_cm[:, None], tr, n_bins)[0]  # bins x trials'''
assert old_doc in s
s=s.replace(old_doc,new_doc)
old='''            Xa, ya = to_dataset(Tc[:, :, tr_sel], dc[tr_sel])
            Xb, yb = to_dataset(Tc[:, :, te_sel], dc[te_sel])
            pa = Pc[:, tr_sel].T.reshape(-1)  # same order as to_dataset (trial-major)
            pb = Pc[:, te_sel].T.reshape(-1)'''
new='''            Xa, ya = to_dataset(Tc[:, :, tr_sel], dc[tr_sel])
            Xb, yb = to_dataset(Tc[:, :, te_sel], dc[te_sel])
            pa = Pc[:, tr_sel].T.reshape(-1)  # same order as to_dataset (trial-major)
            pb = Pc[:, te_sel].T.reshape(-1)
            ka, kb = np.isfinite(pa), np.isfinite(pb)
            Xa, ya, pa, Xb, yb, pb = Xa[ka], ya[ka], pa[ka], Xb[kb], yb[kb], pb[kb]'''
assert old in s
s=s.replace(old,new)
open('hc30.py','w').write(s)
EOF
grep -n "n_samples_dropped\|def decode_bins" hc30.py
```

```
524:def decode_bins(sess, n_bins, seed, reps, C=1.0):
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('hc30.py').read()
s=s.replace('''        ra.append(np.sqrt(np.mean(np.concatenate(sq_a))))
        rb.append(np.sqrt(np.nanmean(np.concatenate(sq_b))))
    return np.array(ra), np.array(rb)''','''        ra.append(np.sqrt(np.mean(np.concatenate(sq_a))))
        rb.append(np.sqrt(np.nanmean(np.concatenate(sq_b))))
    return np.array(ra), np.array(rb), float(np.mean(~np.isfinite(Pt)))''')
s=s.replace("training samples of the predicted class. Returns per-repetition RMS of (a) and (b).","training samples of the predicted class. Returns per-repetition RMS of (a) and (b), and the\n    fraction of (trial, bin) samples with no frame.")
open('hc30.py','w').write(s)
s=open('src_nb2.py').read()
s=s.replace('''        a, b = hc30.decode_bins(sessions[i], nb, seed=50000 + 100 * i + nb, reps=REPS_BINS, C=C_SVM)
        return i, nb, a.mean(), b.mean()
    except Exception as e:  # a session with too few trials visiting every bin
        return i, nb, np.nan, np.nan''','''        a, b, drop = hc30.decode_bins(sessions[i], nb, seed=50000 + 100 * i + nb, reps=REPS_BINS,
                                      C=C_SVM)
        return i, nb, a.mean(), b.mean(), drop
    except Exception as e:
        print("failed", i, nb, repr(e))
        return i, nb, np.nan, np.nan, np.nan''')
s=s.replace('''br = pd.DataFrame(BR, columns=["i", "bins", "centre", "class_mean"])''','''br = pd.DataFrame(BR, columns=["i", "bins", "centre", "class_mean", "dropped"])
print("fraction of (trial, bin) samples with no frame, mean over sessions:",
      br.groupby("bins").dropped.mean().round(4).to_dict())''')
# simulation rewrite
a=s.index('# A simulation of the model of the Supplementary Figure 9 legend')
b=s.index('# RESULT_suppl9-fit-recovers-saturation')
new_sim='''# A simulation of the model of the Supplementary Figure 9 legend (data: elsewhere); no dataset
# values are used. The legend says the decoding follows the paper's methods except for the
# Poisson naive Bayes model, so the simulated events are arranged as the paper's tensor: summed
# per run and spatial bin, 40 bin and direction classes, two halves of the runs. Choices the
# legend leaves open (standard choices named by the criterion): back-and-forth runs at a
# constant 30 cm/s over 118 cm, frames at 20 Hz, input noise drawn independently per frame,
# peak rate 0.05 events per frame, 20 bins.

# %% tags=["claim:suppl9-fit-recovers-saturation"]
rng9 = np.random.default_rng(909)
L9, FS9, SPEED = hc30.TRACK_CM, 20.0, 30.0
n_frames = int(30 * 60 * FS9)
step = SPEED / FS9
phase = (np.arange(n_frames) * step) % (2 * L9)
true_pos = np.where(phase < L9, phase, 2 * L9 - phase)
direction = np.where(phase < L9, 1, -1)
run_id = (np.arange(n_frames) * step // L9).astype(int)
noisy_pos = true_pos + rng9.normal(0, 10, n_frames)
true_bin = np.clip((true_pos / L9 * 20).astype(int), 0, 19)
cls = 2 * true_bin + (direction == -1)
sigma9 = 30 / (2 * np.sqrt(2 * np.log(2)))
key = run_id * 40 + cls
uk, inv = np.unique(key, return_inverse=True)
s_run, s_cls = uk // 40, uk % 40
s_frames = np.bincount(inv).astype(float)
n_runs = run_id.max() + 1
print(f"{n_runs} runs, {len(uk)} run-bin samples, {s_frames.mean():.1f} frames per sample")

def simulate(n_cells):
    c = rng9.uniform(0, L9, n_cells)
    Y = np.zeros((len(uk), n_cells))
    for a in range(0, n_frames, 6000):
        rate = 0.05 * np.exp(-0.5 * ((noisy_pos[a:a + 6000, None] - c[None, :]) / sigma9) ** 2)
        np.add.at(Y, inv[a:a + 6000], rng9.poisson(rate))
    return Y

def nb_imse(Y, sizes, reps):
    out = []
    for n in sizes:
        v = []
        for _ in range(reps):
            sub = rng9.choice(Y.shape[1], n, replace=False)
            first_runs = rng9.permutation(n_runs)[: n_runs // 2]
            half = np.isin(s_run, first_runs)
            mses = []
            for a, b in ((half, ~half), (~half, half)):
                Ya, Yb = Y[a][:, sub], Y[b][:, sub]
                lam = np.array([Ya[s_cls[a] == k].sum(0) / s_frames[a][s_cls[a] == k].sum()
                                for k in range(40)]) + 1e-6
                ll = Yb @ np.log(lam).T - s_frames[b][:, None] * lam.sum(1)[None, :]
                p = ll.argmax(1)
                mses.append(np.mean(((p // 2 - s_cls[b] // 2) * hc30.BIN_CM) ** 2))
            v.append(1 / np.mean(mses))
        out.append(np.mean(v))
    return np.array(out)

res9 = {}
for n_total, sizes in ((500, [1, 10, 20, 50, 100, 200, 300, 400, 500]),
                       (2000, [1, 10, 20, 50, 100, 200, 300, 400, 500, 1000, 1500, 2000])):
    Y = simulate(n_total)
    im = nb_imse(Y, sizes, reps=16)
    I0, N, I0c, Nc = hc30.fit_imse(sizes, im)
    res9[n_total] = (N, Nc)
    print(f"{n_total} neurons: IMSE {np.round(im, 4)}; fit I0 = {I0:.5f}, N = {N:.0f} +/- {Nc:.0f} (95%)")
(N1, c1), (N2, c2) = res9[500], res9[2000]
print(f"intervals overlap: {(N1 - c1) <= (N2 + c2) and (N2 - c2) <= (N1 + c1)}")

# %% [markdown]
'''
s=s[:a]+new_sim+s[b:]
open('src_nb2.py','w').write(s)
EOF
grep -n "RESULT_suppl9" src_nb2.py
```

```
495:# RESULT_suppl9-fit-recovers-saturation
```

**Agent calls Bash**

```bash
sed -n 480,500p entries/hazon-2022/src_nb2.py; . $TMPDIR/dev/bin/activate; cd entries/hazon-2022; python - <<'EOF' 2>&1 | grep -v Warn
# run only the bins part and the simulation from the dev script
src=open('src_nb2.py').read()
import re
pre=src[:src.index('# %% [markdown]\n# ## Data check')]
pre=pre.replace("sessions, md5, load_s = hc30.load_sessions()","sessions, md5, load_s = hc30.load_sessions(); sessions = sessions[::8]").replace("REPS_BINS = 2 ","REPS_BINS = 1 ")
b0=src.index('# %% tags=["claim:suppl6-twenty-bins-near-optimal"]'); b1=src.index('# %% [markdown]\n# RESULT_suppl6')
s0=src.index('# %% tags=["claim:suppl9-fit-recovers-saturation"]'); s1=src.index('# %% [markdown]\n# RESULT_suppl9')
code=pre+src[b0:b1]+src[s0:s1]
import os; os.environ['MPLBACKEND']='Agg'
import sys; sys.path.insert(0,'.')
import time; t=time.time()
exec(compile(code,'x','exec'))
print('elapsed', time.time()-t)
EOF
```

```
out.append(np.mean(v))
    return np.array(out)

res9 = {}
for n_total, sizes in ((500, [1, 10, 20, 50, 100, 200, 300, 400, 500]),
                       (2000, [1, 10, 20, 50, 100, 200, 300, 400, 500, 1000, 1500, 2000])):
    Y = simulate(n_total)
    im = nb_imse(Y, sizes, reps=16)
    I0, N, I0c, Nc = hc30.fit_imse(sizes, im)
    res9[n_total] = (N, Nc)
    print(f"{n_total} neurons: IMSE {np.round(im, 4)}; fit I0 = {I0:.5f}, N = {N:.0f} +/- {Nc:.0f} (95%)")
(N1, c1), (N2, c2) = res9[500], res9[2000]
print(f"intervals overlap: {(N1 - c1) <= (N2 + c2) and (N2 - c2) <= (N1 + c1)}")

# %% [markdown]
# RESULT_suppl9-fit-recovers-saturation

# %% [markdown]
# ## Summary
#
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; grep -n "def cmd_\|nbconvert\|papermill\|timeout\|def run\|python_version\|PYTHON" tools/entry.py | head -40
```

```
Wed Nov 11 19:27:58 UTC 2026
63:PYTHON_VERSION = "3.13"
64:HARNESS = ["ipykernel", "nbconvert"]      # needed to execute, not part of the entry
391:    (entries from before the field), else the registry's default for new entries, PYTHON_VERSION."""
400:    return PYTHON_VERSION
443:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
450:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
515:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
530:    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
545:            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
546:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
621:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
663:                              args.timeout, args.max_minutes)
673:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; sed -e 's/^plt.show()/plt.close("all")/' src_nb1.py > $TMPDIR/full_nb1.py; time MPLBACKEND=Agg PYTHONPATH=. timeout 3500 python $TMPDIR/full_nb1.py > $TMPDIR/nb1.out 2>&1; tail -5 $TMPDIR/nb1.out
```

```
real	5m11.360s
user	10m49.341s
sys	0m12.747s
legend, uniform half-widths, 50 cells, 1000 simulations: median NSV narrow 0.0033, broad 0.0020; narrow higher: True
   mean NSV narrow vs broad by ensemble size -> 100: 9.33e-04 vs 5.44e-04; 1000: 9.16e-06 vs 5.39e-06; 10000: 9.14e-08 vs 5.40e-08
Methods, log-normal half-widths, 50 cells, 1000 simulations: median NSV narrow 0.0030, broad 0.0044; narrow higher: False
   mean NSV narrow vs broad by ensemble size -> 100: 8.53e-04 vs 1.38e-03; 1000: 8.59e-06 vs 1.42e-05; 10000: 8.58e-08 vs 1.42e-07
total run time 5.2 min; peak memory 1.8 GB
```

**Agent calls Bash**

```bash
grep -v "Warning\|curve_fit(" $TMPDIR/nb1.out | head -150
```

```
snr_dir.append(np.nanmean([means[k].var(axis=1, ddof=1) / per_class_var[k].mean(axis=1)
streamed and parsed event_traces.mat in 4 s; md5 fe0f5dd2fca6d64dbf0cd3f35e31e1f0 (matches checksums.md5)
sessions 110 mice 12
           sessions  neurons  large  trials_med
mouse                                          
Mouse2010         4      667      0        46.5
Mouse2011        11     3340     11        48.0
Mouse2012        19     3521      4        60.0
Mouse2019         7     2062      7       130.0
Mouse2021         4     1700      4       154.5
Mouse2022         6     2030      5       146.0
Mouse2023         5      959      1        78.0
Mouse2024        14     5048     14        89.5
Mouse2025         8     1421      1       126.5
Mouse2026        13     2971     11        99.0
Mouse2028        15     3510     15       143.0
Mouse2029         4      669      0        93.0
           count        mean  ...         75%          max
frames     110.0   35943.382  ...   36133.250    55247.000
minutes    110.0      29.953  ...      30.111       46.039
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "Warning\|curve_fit(" $TMPDIR/nb1.out | sed -n 150,400p
```

```
Mouse2012  1.472     13.684         True
Mouse2019  4.543     54.476         True
Mouse2021  0.916     29.673         True
Mouse2022  1.543     49.634         True
Mouse2023  2.201     15.057         True
Mouse2024  1.956     27.195         True
Mouse2025  1.072     11.706         True
Mouse2026  2.156     16.399         True
Mouse2028  2.447     33.599         True
Mouse2029  2.558     28.243         True
mice with higher median for shuffled: 12 of 12
110 working: pooled n = 220: median begin 0.2082, end 0.3126; begin > end (legend) p = 1.00e+00; begin < end (code) p = 1.12e-18
   rightward only n = 110: begin 0.2026, end 0.2995; greater p = 1.00e+00; less p = 1.75e-09
73 large-data: pooled n = 146: median begin 0.2150, end 0.3135; begin > end (legend) p = 1.00e+00; begin < end (code) p = 3.85e-15
   rightward only n = 73: begin 0.2229, end 0.2954; greater p = 1.00e+00; less p = 1.72e-05
median signal slope along the run, rightward pairs 0..18: [0.2026 0.1033 0.0551 0.0352 0.0275 0.0225 0.0211 0.019  0.018  0.0197
 0.0184 0.0186 0.0184 0.0218 0.0238 0.0302 0.0494 0.1073 0.2995]
                      leftward pairs, run order: [0.2105 0.0972 0.0472 0.0363 0.0286 0.0251 0.0218 0.0195 0.0163 0.0159
 0.0155 0.0165 0.0197 0.0231 0.0273 0.0355 0.0504 0.121  0.3193]
110 working: pooled n = 220: median begin 0.01752, end 0.01163; begin > end p = 1.91e-09 (other direction 1.00e+00)
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; cat > $TMPDIR/t9.py <<'EOF'
import pickle, numpy as np, os, hc30, pandas as pd
S=pickle.load(open(os.environ['TMPDIR']+'/S.pkl','rb'))
def shift_err(s, shift):
    tr = hc30.select_trials(s["position"]); X = hc30.event_trace(s["events"])
    if shift: X = np.roll(X, shift, axis=0)
    T = hc30.build_tensor(X, tr); d = tr["direction"]
    first = hc30.half_split(d, np.random.default_rng(0)); errs=[]
    for dirn in (1,-1):
        A = T[:, :, first & (d == dirn)].mean(axis=2); B = T[:, :, ~first & (d == dirn)]
        for t in range(B.shape[2]):
            dist = ((B[:, :, t][:, :, None] - A[:, None, :]) ** 2).sum(axis=0)
            errs.append(np.abs(dist.argmin(axis=1) - np.arange(20)).mean())
    return np.mean(errs)*5.9
out=[]
for i,s in enumerate(S):
    out.append((i,s['mouse'],s['session_id'], round(shift_err(s,0),1)))
df=pd.DataFrame(out,columns=['i','mouse','sid','err0'])
print(df.sort_values('err0').tail(6)); print(df.err0.describe())
EOF
PYTHONPATH=. python $TMPDIR/t9.py
```

```
i      mouse     sid  err0
73  73  Mouse2026  115639  14.7
97  97  Mouse2021  132808  15.3
51  51  Mouse2012  141832  29.3
92  92  Mouse2011  142436  29.4
84  84  Mouse2011  104511  43.9
83  83  Mouse2011  105556  44.0
count    110.000000
mean       6.827273
std        6.297224
min        2.300000
25%        4.600000
50%        5.550000
75%        6.700000
max       44.000000
Name: err0, dtype: float64
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; cat >> $TMPDIR/t9.py <<'EOF'
print('lag scan')
for i in [83,84,51,92,73,97,0]:
    s=S[i]; res=[]
    for lag in [-2000,-1000,-600,-350,-200,-100,-40,-20,0,20,40,100,200,350,600,1000,2000]:
        res.append((lag, round(shift_err(s,lag),1)))
    best=min(res,key=lambda x:x[1]); print(i, s['mouse'], s['session_id'], s['events'].shape, 'best', best, res)
EOF
sed -i 's/^for i,s in enumerate(S):$/for i,s in []:/' $TMPDIR/t9.py; sed -i 's/^df=pd.DataFrame.*$//; s/^print(df.*$//' $TMPDIR/t9.py; PYTHONPATH=. python $TMPDIR/t9.py
```

```
lag scan
83 Mouse2011 105556 (36038, 230) best (-600, np.float64(38.5)) [(-2000, np.float64(39.8)), (-1000, np.float64(41.1)), (-600, np.float64(38.5)), (-350, np.float64(42.5)), (-200, np.float64(42.0)), (-100, np.float64(46.1)), (-40, np.float64(43.7)), (-20, np.float64(45.0)), (0, np.float64(44.0)), (20, np.float64(45.6)), (40, np.float64(42.7)), (100, np.float64(43.6)), (200, np.float64(39.5)), (350, np.float64(40.8)), (600, np.float64(43.5)), (1000, np.float64(45.4)), (2000, np.float64(39.6))]
84 Mouse2011 104511 (36025, 204) best (-600, np.float64(38.4)) [(-2000, np.float64(45.3)), (-1000, np.float64(44.4)), (-600, np.float64(38.4)), (-350, np.float64(43.4)), (-200, np.float64(44.4)), (-100, np.float64(44.5)), (-40, np.float64(44.1)), (-20, np.float64(43.2)), (0, np.float64(43.9)), (20, np.float64(44.1)), (40, np.float64(43.6)), (100, np.float64(40.6)), (200, np.float64(44.7)), (350, np.float64(43.6)), (600, np.float64(47.5)), (1000, np.float64(44.8)), (2000, np.float64(42.5))]
51 Mouse2012 141832 (35771, 216) best (-100, np.float64(7.8)) [(-2000, np.float64(46.0)), (-1000, np.float64(47.8)), (-600, np.float64(42.9)), (-350, np.float64(42.1)), (-200, np.float64(36.0)), (-100, np.float64(7.8)), (-40, np.float64(21.3)), (-20, np.float64(26.8)), (0, np.float64(29.3)), (20, np.float64(33.0)), (40, np.float64(33.0)), (100, np.float64(42.4)), (200, np.float64(41.1)), (350, np.float64(43.3)), (600, np.float64(43.3)), (1000, np.float64(43.9)), (2000, np.float64(39.4))]
92 Mouse2011 142436 (35900, 436) best (-100, np.float64(6.7)) [(-2000, np.float64(43.2)), (-1000, np.float64(47.8)), (-600, np.float64(46.8)), (-350, np.float64(42.5)), (-200, np.float64(34.2)), (-100, np.float64(6.7)), (-40, np.float64(16.1)), (-20, np.float64(25.7)), (0, np.float64(29.4)), (20, np.float64(35.1)), (40, np.float64(38.6)), (100, np.float64(36.9)), (200, np.float64(45.9)), (350, np.float64(48.2)), (600, np.float64(41.8)), (1000, np.float64(44.4)), (2000, np.float64(43.3))]
73 Mouse2026 11
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/hazon-2022; cat > $TMPDIR/t10.py <<'EOF'
import pickle, numpy as np, os, hc30
exec(open(os.environ['TMPDIR']+'/t9.py').read().split("out=[]")[0])
for i in [51,92]:
    print(i, [(l, round(shift_err(S[i],l),1)) for l in range(-130,-70,10)])
for i in [83,84]:
    ev=S[i]['events']; res=[]
    for j,s2 in enumerate(S):
        n=min(len(s2['position']), ev.shape[0])
        s3=dict(events=ev[:n], position=s2['position'][:n])
        try: res.append((round(shift_err(s3,0),1), j, s2['mouse'], s2['session_id']))
        except Exception as e: pass
    print(i, sorted(res)[:4])
EOF
PYTHONPATH=. python $TMPDIR/t10.py 2>&1 | grep -v Warn
```

```
51 [(-130, np.float64(15.8)), (-120, np.float64(12.7)), (-110, np.float64(10.1)), (-100, np.float64(7.8)), (-90, np.float64(5.4)), (-80, np.float64(6.5))]
92 [(-130, np.float64(24.7)), (-120, np.float64(16.2)), (-110, np.float64(10.3)), (-100, np.float64(6.7)), (-90, np.float64(4.6)), (-80, np.float64(2.8))]
83 [(np.float64(38.3), 3, 'Mouse2023', '101329'), (np.float64(39.9), 93, 'Mouse2011', '092502'), (np.float64(40.6), 26, 'Mouse2028', '105814'), (np.float64(40.7), 61, 'Mouse2019', '095525')]
84 [(np.float64(38.7), 39, 'Mouse2012', '100639'), (np.float64(40.4), 100, 'Mouse2025', '104428'), (np.float64(40.5), 2, 'Mouse2023', '114832'), (np.float64(40.9), 19, 'Mouse2028', '192709')]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('src_nb1.py').read()
a=s.index('first_of_mouse = info.groupby("mouse").i.first().values')
b=s.index('# %% tags=["sanity"]\nWORK = info.index.values')
new='''lag0 = np.array([shift_check(s, 0) for s in sessions])
info["clock_err_cm"] = lag0
print("lag 0, per session: mean absolute position error median %.1f cm, range %.1f to %.1f" % (
    np.median(lag0), lag0.min(), lag0.max()))
first_of_mouse = info.groupby("mouse").i.first().values
for lag_s in (2, 10):
    e = [shift_check(sessions[i], int(lag_s * hc30.FS)) for i in first_of_mouse]
    print(f"labels shifted by {lag_s:>2} s (first session of each mouse): error {np.mean(e):.1f} cm "
          f"(range {min(e):.1f} to {max(e):.1f}); the same sessions at lag 0: "
          f"{np.mean(lag0[first_of_mouse]):.1f} cm")
bad = np.where(lag0 > 12)[0]
print(f"sessions with error above 12 cm at lag 0: {len(bad)}; scanning lags of -200 to +200 frames")
lag_rows = []
for i in bad:
    errs = {lag: shift_check(sessions[i], lag) for lag in range(-200, 201, 10)}
    best = min(errs, key=errs.get)
    lag_rows.append((i, info.mouse[i], info.session[i], round(lag0[i], 1), best, round(errs[best], 1)))
print(pd.DataFrame(lag_rows, columns=["i", "mouse", "session", "error_lag0_cm", "best_lag_frames",
                                      "error_best_cm"]).to_string(index=False))

'''
s=s[:a]+new+s[b:]
s=s.replace("N_SPLITS_4A = 20","N_SPLITS_4A = 100")
s=s.replace("# 20 random half splits per bin pair (the code uses 100; reduced for time).","# 100 random half splits per bin pair, as in the code.")
open('src_nb1.py','w').write(s)
EOF
grep -n "shift_check\|lag" src_nb1.py | head
```

```
112:# A contrast that a lag would destroy: decode position bin from the event trace with the
115:def shift_check(s, shift):
132:lag0 = np.array([shift_check(s, 0) for s in sessions])
133:info["clock_err_cm"] = lag0
134:print("lag 0, per session: mean absolute position error median %.1f cm, range %.1f to %.1f" % (
135:    np.median(lag0), lag0.min(), lag0.max()))
137:for lag_s in (2, 10):
138:    e = [shift_check(sessions[i], int(lag_s * hc30.FS)) for i in first_of_mouse]
139:    print(f"labels shifted by {lag_s:>2} s (first session of each mouse): error {np.mean(e):.1f} cm "
140:          f"(range {min(e):.1f} to {max(e):.1f}); the same sessions at lag 0: "
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('src_nb1.py').read()
a=s.index('def shift_check(s, shift):')
b=s.index('lag0 = np.array(')
s=s[:a]+"shift_check = hc30.clock_check\n\n"+s[b:]
s=s.replace('print(f"labels shifted by {lag_s:>2} s','print(f"event trace shifted by {lag_s:>2} s')
open('src_nb1.py','w').write(s)
h=open('hc30.py').read()
h+='''

def clock_check(sess, shift):
    """Mean absolute position error (cm) of a quick nearest-centroid decoder (class means of one
    random half of the trials, per direction; the bin of the nearest mean for each bin of each
    held-out trial), with the event trace shifted by `shift` frames (np.roll). A check that the
    event trace and the position share a clock (protocol, author step 2), not the paper's
    decoder."""
    tr = select_trials(sess["position"])
    X = event_trace(sess["events"])
    if shift:
        X = np.roll(X, shift, axis=0)
    T = build_tensor(X, tr)
    d = tr["direction"]
    first = half_split(d, np.random.default_rng(0))
    errs = []
    for dirn in (1, -1):
        A = T[:, :, first & (d == dirn)].mean(axis=2)
        B = T[:, :, ~first & (d == dirn)]
        for t in range(B.shape[2]):
            dist = ((B[:, :, t][:, :, None] - A[:, None, :]) ** 2).sum(axis=0)
            errs.append(np.abs(dist.argmin(axis=1) - np.arange(N_BINS)).mean())
    return float(np.mean(errs) * BIN_CM)
'''
open('hc30.py','w').write(h)
s=open('src_nb2.py').read()
s=s.replace('''print("performance: median''','''info["clock_err_cm"] = [hc30.clock_check(s, 0) for s in sessions]
MISALIGNED = info.index[info.clock_err_cm > 12].values
print("sessions whose event trace does not track position at lag 0 (quick decoder error > 12 cm,"
      " first notebook):", info.loc[MISALIGNED, ["mouse", "session", "clock_err_cm"]].round(1)
      .values.tolist())
print("performance: median''')
s=s.replace('''print("spread over repetitions within a session (SD of RMS)''','''ok_clock = ~info.index.isin(MISALIGNED)
for col, name in (("rms_u", "ensemble"), ("rms_s", "shuffled")):
    q1, q3 = np.percentile(info.loc[ok_clock, col], [25, 75])
    print(f"variant without the {len(MISALIGNED)} misaligned sessions, {name}: median "
          f"{info.loc[ok_clock, col].median():.2f} cm, IQR {q3 - q1:.2f} cm")
print("spread over repetitions within a session (SD of RMS)''')
open('src_nb2.py','w').write(s)
EOF
grep -n "MISALIGNED" src_nb2.py | head
```

```
55:MISALIGNED = info.index[info.clock_err_cm > 12].values
57:      " first notebook):", info.loc[MISALIGNED, ["mouse", "session", "clock_err_cm"]].round(1)
115:ok_clock = ~info.index.isin(MISALIGNED)
118:    print(f"variant without the {len(MISALIGNED)} misaligned sessions, {name}: median "
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate; cd entries/hazon-2022; sed -e 's/^plt.show()/plt.close("all")/' src_nb2.py > $TMPDIR/full_nb2.py; time MPLBACKEND=Agg PYTHONPATH=. timeout 4000 python $TMPDIR/full_nb2.py > $TMPDIR/nb2.out 2>&1; grep -v "Warn\|curve_fit(\|check_class" $TMPDIR/nb2.out | head -250
```

```
Wed Nov 11 19:35:21 UTC 2026

real	38m29.773s
user	111m8.218s
sys	1m34.079s
streamed and parsed event_traces.mat in 4 s; md5 fe0f5dd2fca6d64dbf0cd3f35e31e1f0 (matches checksums.md5)
sessions 110, mice 12, neurons 27898, large-data sessions 73 from 10 mice
trials per direction used by the decoder (smaller of the two): median 92, range 31 to 187
sessions whose event trace does not track position at lag 0 (quick decoder error > 12 cm, first notebook): [['Mouse2012', '141832', 29.3], ['Mouse2026', '115639', 14.7], ['Mouse2011', '105556', 44.0], ['Mouse2011', '104511', 43.9], ['Mouse2011', '142436', 29.4], ['Mouse2021', '132808', 15.3]]
performance: median 0.830, range 0.404 to 0.989; slow errors median 24, turn-around errors median 12
0.45 s per repetition (both conditions, all neurons); estimated decoding time 9 min on 3 processes, before the bin-count variant
decoding: 28.5 min; peak memory 1.9 GB
ensemble: median 9.35 cm, IQR 3.97 cm (quartiles 7.75 to 11.72), range 4.05 to 51.85
shuffled: median 4.80 cm, IQR 1.71 cm (quartiles 4.19 to 5.90), range 2.78 to 51.69
ensemble error larger than shuffled in 109 of 110 sessions; Wilcoxon p = 9.0e-20
variant without the 6 misaligned sessions, ensemble: median 9.17 cm, IQR 3.39 cm
variant without the 6 misaligned sessions, shuffled: median 4.77 cm, IQR 1.68 cm
spread over repetitions within a session (SD of RMS), median: ensemble 0.48, shuffled 0.13 cm
           rms_u  rms_s
mouse                  
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hazon-2022; python3 - <<'EOF'
s=open('src_nb2.py').read()
s=s.replace("REPS_FULL = 12   # repetitions with all neurons [80]","REPS_FULL = 10   # repetitions with all neurons [80]")
s=s.replace("SIZES = [1, 10, 20, 30, 50, 75, 100, 150, 200, 250, 300, 400]  # plus all neurons [1, 10, 20, ...]","SIZES = [1] + list(range(25, 500, 25))  # below the session's count, plus all neurons [1, 10, 20, ...]")
open('src_nb2.py','w').write(s)
EOF
grep -n "^SIZES\|^REPS" src_nb2.py; date -u
```

```
27:REPS_FULL = 10   # repetitions with all neurons [80]
28:REPS_SUB = 4     # neuron subsets per ensemble size [80]
29:SIZES = [1] + list(range(25, 500, 25))  # below the session's count, plus all neurons [1, 10, 20, ...]
31:REPS_BINS = 2    # [80]
Wed Nov 11 20:14:16 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hazon-2022; python3 - <<'EOF'
s=open('src_nb2.py').read()
s=s.replace('''print(f"{per_rep:.2f} s per repetition (both conditions, all neurons); estimated decoding time "
      f"{est:.0f} min on 3 processes, before the bin-count variant")''','''print(f"{per_rep:.2f} s per repetition (both conditions, all neurons); {len(info) * REPS_FULL} "
      f"full-ensemble repetitions and {n_sizes * REPS_SUB} subset repetitions; a rough lower "
      f"bound of {est:.0f} min on 3 processes (the preparatory run took about three times this)")''')
open('src_nb2.py','w').write(s)

common = '''**Paper.** Hazon O, Minces VH, Tomàs DP, Ganguli S, Schnitzer MJ, Jercog PE (2022). Noise
correlations in neural ensemble activity limit the accuracy of hippocampal spatial
representations. *Nature Communications* 13, 4276.
[doi:10.1038/s41467-022-31254-y](https://doi.org/10.1038/s41467-022-31254-y)

**Dataset.** CRCNS hc-30, Jercog P and Schnitzer M (2022), "Functional calcium imaging
recordings of hippocampal area CA1 from mice performing a linear track task",
[doi:10.6080/K0GH9G5X](https://doi.org/10.6080/K0GH9G5X). One file, `hc-30/live/event_traces.mat`
(142,350,100 bytes), streamed from the public S3 bucket `crcnsarchive` into memory.

**Version.** CRCNS data sets are not versioned, so the version is recorded as `unversioned`
(docs/archives.md). The paper cites no version; the only one published is the one in the bucket
(data descriptor version 0.6, July 8, 2022, the initial version), which matches the claims file's
description (110 sessions with mouse name, session ID, sparse event array and position). The
MD5 sum from the data set's `checksums.md5`, which the next cell checks against the streamed
bytes, is `fe0f5dd2fca6d64dbf0cd3f35e31e1f0` (event_traces.mat); the descriptor PDF is
`320d157fbcc43be385485cc186842636`.

**Text the claims were written from.** The version of record (PMC9314334) with its Methods and
Supplementary Information; the paper's code, github.com/approbatory/ML-project at commit
2057af9facfd3035c573e1254bdc32ed4781ba60, was read for method details (claims/hazon-2022.yaml).
Method details taken by this attempt cite the passage or code file in `hc30.py`.

**Data.** 110 sessions of 12 mice with an event-onset array (frames x neurons) and the position
in camera pixels. There are no cell positions, no frame times and no trial table; trials,
bins and the event trace are built here from the Methods and the code (`hc30.py`).
'''
nb1_table = '''
| Claim | Notebook | Status |
|---|---|---|
| data-sessions-and-neurons | this one | tested |
| single-cell-variability | this one | tested |
| suppl-table1-place-field-properties | this one | tested |
| fig1d-noise-correlation-by-field-distance | this one | tested |
| noise-correlation-not-physical-distance | none | blocked, data_missing: no cell positions in the file |
| position-measurement-noise | this one | tested |
| fig3cd-signal-and-noise-growth | this one | tested |
| suppl10-asymptotic-snr-lower-with-correlations | this one | tested |
| fig3f-signal-slope-beginning-vs-end | this one | tested |
| fig3g-noise-slope-decreases-over-run | this one | tested |
| fig3h-snr-higher-at-run-end | this one | tested |
| fig4a-snr-along-noise-pcs-peaks-at-6 | this one | tested |
| fig4b-correlations-increase-noise-signal-overlap | this one | tested |
| fig4c-overlap-predicts-asymptotic-snr | this one | tested |
| fig5f-pf-width-variance-vs-nsv | this one | tested |
| fig5hi-nsv-predicts-noise-correlation-effect | this one | tested |
| suppl-table2-nsv-best-predictor | this one | tested |
| pf-width-variance-not-predictive | this one | tested |
| fig5cd-synthetic-narrow-widths-broader-nsv | this one | tested (simulation, data elsewhere) |
| fig2d, fig2cd, fig2ef, suppl7b, saturation, suppl11b, suppl11c, suppl8, suppl6, suppl9 | decoding notebook | tested there |

Run time about 6 minutes on 4 CPUs (3 worker processes).
'''
nb2_table = '''
| Claim | Status |
|---|---|
| fig2d-rms-error-ensemble-vs-shuffled | tested |
| fig2cd-shuffle-better-in-all-bins | tested |
| fig2ef-imse-saturates-with-correlations | tested |
| suppl7b-initial-slope-lower-with-correlations | tested |
| saturation-ensemble-size | tested |
| suppl11b-i0-vs-single-cell-snr | tested |
| suppl11c-asymptotic-imse-vs-asymptotic-snr | tested |
| suppl8-task-performance-and-accuracy | tested |
| suppl6-twenty-bins-near-optimal | tested |
| suppl9-fit-recovers-saturation | tested (simulation, data elsewhere) |

The other claims are in `reproduce_hazon_2022.ipynb`. The decoders are the heavy part: this
notebook takes about 40 minutes on 4 CPUs (3 worker processes), with fewer repetitions than the
paper's 80 (stated at each claim).
'''
for fn, tab in (('src_nb1.py', nb1_table), ('src_nb2.py', nb2_table)):
    s=open(fn).read()
    txt = '\n'.join('# '+l if l else '#' for l in (common+tab).strip().split('\n'))
    s=s.replace('# HEADER_PLACEHOLDER', txt)
    open(fn,'w').write(s)
EOF
head -30 src_nb2.py
```

```
# %% [markdown]
# # Reproducing Hazon et al. (2022) from CRCNS hc-30: position decoding
#
# **Paper.** Hazon O, Minces VH, Tomàs DP, Ganguli S, Schnitzer MJ, Jercog PE (2022). Noise
# correlations in neural ensemble activity limit the accuracy of hippocampal spatial
# representations. *Nature Communications* 13, 4276.
# [doi:10.1038/s41467-022-31254-y](https://doi.org/10.1038/s41467-022-31254-y)
#
# **Dataset.** CRCNS hc-30, Jercog P and Schnitzer M (2022), "Functional calcium imaging
# recordings of hippocampal area CA1 from mice performing a linear track task",
# [doi:10.6080/K0GH9G5X](https://doi.org/10.6080/K0GH9G5X). One file, `hc-30/live/event_traces.mat`
# (142,350,100 bytes), streamed from the public S3 bucket `crcnsarchive` into memory.
#
# **Version.** CRCNS data sets are not versioned, so the version is recorded as `unversioned`
# (docs/archives.md). The paper cites no version; the only one published is the one in the bucket
# (data descriptor version 0.6, July 8, 2022, the initial version), which matches the claims file's
# description (110 sessions with mouse name, session ID, sparse event array and position). The
# MD5 sum from the data set's `checksums.md5`, which the next cell checks against the streamed
# bytes, is `fe0f5dd2fca6d64dbf0cd3f35e31e1f0` (event_traces.mat); the descriptor PDF is
# `320d157fbcc43be385485cc186842636`.
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hazon-2022; python3 - <<'EOF'
s=open('src_nb1.py').read()
old='''    per_dir = {}
    for dirn in (1, -1):'''
new='''    per_dir = {}
    cnt_both, occ_both = 0, 0
    for dirn in (1, -1):'''
assert old in s; s=s.replace(old,new)
old='''        rate = cnt / (occ[:, None] / hc30.FS)  # events per second, bins x neurons
        V = np.stack(visit_counts, axis=2)  # bins x neurons x visits
        per_dir[dirn] = (rate, V.var(axis=2, ddof=1).mean(axis=0))'''
new='''        rate = cnt / (occ[:, None] / hc30.FS)  # events per second, bins x neurons
        V = np.stack(visit_counts, axis=2)  # bins x neurons x visits
        per_dir[dirn] = (rate, V.var(axis=2, ddof=1).mean(axis=0))
        cnt_both, occ_both = cnt_both + cnt, occ_both + occ
    rate_both = cnt_both / (occ_both[:, None] / hc30.FS)
    T_, d_ = TENS[si]
    tbt_trace = np.mean([T_[:, :, d_ == s_].var(axis=2, ddof=1).mean(axis=1) for s_ in (1, -1)], axis=0)'''
assert old in s; s=s.replace(old,new)
old='''                 active=total_events[n] / minutes * 10 > 100)'''
new='''                 active=total_events[n] / minutes * 10 > 100, tbt_trace=tbt_trace[n])
        y = rate_both[:, n]
        r["width_both"] = np.nan
        if y.max() > 0:
            try:
                fit, _ = curve_fit(gauss, xb, y, p0=[y.max() - y.min(), y.argmax(), 2.0, y.min()],
                                   maxfev=2000)
                r["width_both"] = 2 * np.sqrt(2 * np.log(2)) * abs(fit[2]) * hc30.BIN_CM
            except Exception:
                pass'''
assert old in s; s=s.replace(old,new)
old='''        ("trial-by-trial variability", cells, mstd(both("tbt")[sel2]), 1.2),'''
new='''        ("PF width, both directions pooled", cells,
         mstd(pf.width_both[sel1 & (pf.width_both < 1180).values]), 37.8),
        ("trial-by-trial variability, counts", cells, mstd(both("tbt")[sel2]), 1.2),
        ("trial-by-trial variability, event trace", cells, mstd(pf.tbt_trace[sel1]), 1.2),'''
assert old in s; s=s.replace(old,new)
open('src_nb1.py','w').write(s)
EOF
cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scikit-learn
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: hazon-2022
type: reproduction
title: Noise correlations limit hippocampal spatial accuracy (Hazon et al. 2022)
description: Tests the findings of Hazon, Minces, Tomàs, Ganguli, Schnitzer and Jercog (2022) on
  CRCNS hc-30, which holds the event onsets and track positions of 110 CA1 calcium imaging sessions
  from 12 mice on a linear track. It rebuilds the paper's activity tensor, trial shuffle, linear SVM
  position decoders and signal and noise measures, and tests the effect of noise correlations on
  decoding accuracy, its saturation with ensemble size, the geometry of noise and signal, and the
  normalized signal variance.
license: Apache-2.0
notebooks:
- path: reproduce_hazon_2022.ipynb
  title: Tensor, noise correlation and signal and noise analyses
  runtime_minutes: 6
- path: reproduce_hazon_2022_decoding.ipynb
  title: Position decoding, IMSE saturation and bin count
  runtime_minutes: 40
helpers:
- hc30.py
related:
- id: crcns:hc-30/unversioned
  relation: uses_data
- id: doi:10.1038/s41467-022-31254-y
  relation: reproduces
EOF
. $TMPDIR/dev/bin/activate; jupytext --to notebook src_nb1.py -o reproduce_hazon_2022.ipynb -q 2>&1|tail -2; jupytext --to notebook src_nb2.py -o reproduce_hazon_2022_decoding.ipynb -q 2>&1 | tail -2; python -c "
import json
for f in ['reproduce_hazon_2022.ipynb','reproduce_hazon_2022_decoding.ipynb']:
    nb=json.load(open(f)); print(f, len(nb['cells']), nb['metadata'].keys(), [c['metadata'].get('tags') for c in nb['cells'] if c['metadata'].get('tags')][:4])
"; cd ../..; python tools/entry.py lock entries/hazon-2022 2>&1 | tail -5; date -u
```

```
reproduce_hazon_2022.ipynb 69 dict_keys(['jupytext']) [['sanity'], ['sanity'], ['sanity'], ['sanity']]
reproduce_hazon_2022_decoding.ipynb 43 dict_keys(['jupytext']) [['sanity'], ['sanity'], ['claim:fig2d-rms-error-ensemble-vs-shuffled'], ['claim:fig2d-rms-error-ensemble-vs-shuffled']]
wrote hazon-2022/requirements.lock.txt (Python 3.13, with hashes)
Wed Nov 11 20:15:03 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;print(json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'))['metadata'])"; python tools/entry.py check entries/hazon-2022 2>&1 | tail -20
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
error: entries/hazon-2022/reproduce_hazon_2022.ipynb: neither the notebook nor a helper names version unversioned of dataset hc-30, which entry.yaml pins
error: entries/hazon-2022/reproduce_hazon_2022_decoding.ipynb: neither the notebook nor a helper names version unversioned of dataset hc-30, which entry.yaml pins
2 error(s)
```

**Agent calls Bash**

```bash
cd  grep -n "names version" -B25 tools/entry.py | grep -n "def \|re\.\|in text\|crcns\|version" | head -30
```

```
4:222-    versions = {d: v for d, _, v in used}
8:226-        for d, v in versions.items():
10:228-                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
15:233-        nb = nbformat.read(path, as_version=4)
24:242-            version = versions[dandiset]
25:243-            if version and version not in code and version not in helper_code:
26:244:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
```

**Agent calls Bash**

```bash
cd  sed -n 230,246p tools/entry.py
```

```
for name in [n for n in listed if n in present]:
        path = entry_dir / name
        nb = nbformat.read(path, as_version=4)
        if any(c.cell_type == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.cells):
            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
        code = code_of(path)
        for dandiset in dandisets:
            if dandiset not in code and dandiset not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
            version = versions[dandiset]
            if version and version not in code and version not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
                                         f"of dataset {dandiset}, which entry.yaml pins")
        _derivation_checks(report, rel / name, code)
```

**Agent**

Add a version constant to the helper, and set kernelspec metadata.

**Agent calls Bash**

```bash
cd entries/hazon-2022; python3 - <<'EOF'
s=open('hc30.py').read()
s=s.replace('''URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-30/live/event_traces.mat"''','''DATASET = "hc-30"
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); the MD5 pins the file
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-30/live/event_traces.mat"''')
open('hc30.py','w').write(s)
import json
for f in ['reproduce_hazon_2022.ipynb','reproduce_hazon_2022_decoding.ipynb']:
    nb=json.load(open(f)); nb['metadata']={'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
    json.dump(nb, open(f,'w'), indent=1, ensure_ascii=False); open(f,'a').write('\n')
EOF
cd ../..; python tools/entry.py check entries/hazon-2022 2>&1 | tail -5; date -u
```

```
0 error(s)
Wed Nov 11 20:15:21 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hazon-2022; mv src_nb1.py src_nb2.py $TMPDIR/; cat > $TMPDIR/build.sh <<'EOF'
. $TMPDIR/dev/bin/activate
cd entries/hazon-2022
jupytext --to notebook $TMPDIR/src_nb1.py -o reproduce_hazon_2022.ipynb -q
jupytext --to notebook $TMPDIR/src_nb2.py -o reproduce_hazon_2022_decoding.ipynb -q
python3 - <<'PY'
import json
for f in ['reproduce_hazon_2022.ipynb','reproduce_hazon_2022_decoding.ipynb']:
    nb=json.load(open(f)); nb['metadata']={'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
    json.dump(nb, open(f,'w'), indent=1, ensure_ascii=False); open(f,'a').write('\n')
PY
EOF
bash $TMPDIR/build.sh; ls; cd ../..; python tools/entry.py check entries/hazon-2022 | tail -1
```

```
__pycache__
entry.yaml
hc30.py
reproduce_hazon_2022.ipynb
reproduce_hazon_2022_decoding.ipynb
requirements.in
requirements.lock.txt
0 error(s)
```

**Agent**

Now the first real run in the clean environment (about 45 minutes).

**Agent calls Bash**

```bash
cd  rm -rf entries/hazon-2022/__pycache__; date -u; time python tools/entry.py run entries/hazon-2022 2>&1 | tail -15; date -u
```

```
Wed Nov 11 20:15:34 UTC 2026
Installed kernelspec registry-hazon-2022 in executed/hazon-2022/.venv/share/jupyter/kernels/registry-hazon-2022
pass  reproduce_hazon_2022.ipynb  (453 s)
pass  reproduce_hazon_2022_decoding.ipynb  (2442 s)

real	48m19.800s
user	132m25.110s
sys	1m55.830s
Wed Nov 11 21:03:54 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/hazon-2022; ls; python3 - <<'EOF' > $TMPDIR/ex1.txt
import json
for f in ['reproduce_hazon_2022.ipynb','reproduce_hazon_2022_decoding.ipynb']:
    nb=json.load(open(f))
    print('=====',f)
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream' and o.get('name')=='stdout': print(''.join(o['text']))
EOF
wc -l $TMPDIR/ex1.txt; diff <(grep -v "s;\| s$\|min;\|time\|memory" $TMPDIR/ex1.txt | sed -n '/=====.*decoding/,$p' | head -0) /dev/null; sed -n '/=====.*decoding/,$p' $TMPDIR/ex1.txt | head -150
```

```
reproduce_hazon_2022.ipynb
reproduce_hazon_2022_decoding.ipynb
result.json
459 /tmp/claude-1001/ex1.txt
===== reproduce_hazon_2022_decoding.ipynb
streamed and parsed event_traces.mat in 4 s; md5 fe0f5dd2fca6d64dbf0cd3f35e31e1f0 (matches checksums.md5)

sessions 110, mice 12, neurons 27898, large-data sessions 73 from 10 mice
trials per direction used by the decoder (smaller of the two): median 92, range 31 to 187

sessions whose event trace does not track position at lag 0 (quick decoder error > 12 cm, first notebook): [['Mouse2012', '141832', 29.3], ['Mouse2026', '115639', 14.7], ['Mouse2011', '105556', 44.0], ['Mouse2011', '104511', 43.9], ['Mouse2011', '142436', 29.4], ['Mouse2021', '132808', 15.3]]
performance: median 0.830, range 0.404 to 0.989; slow errors median 24, turn-around errors median 12

0.46 s per repetition (both conditions, all neurons); 1100 full-ensemble repetitions and 4668 subset repetitions; a rough lower bound of 10 min on 3 processes (the preparatory run took about three times this)

decoding: 30.5 min; peak memory 1.9 GB

ensemble: median 9.36 cm, IQR 3.92 cm (quartiles 7.76 to 11.67), range 4.05 to 51.88
shuffled: median 4.80 cm, IQR 1.73 cm (quartiles 4.19 to 5.92), range 2.78 to 51.69
ensemble error larger than shuffled in 109 of 110 sessions; Wilcoxon p = 9.0e-20
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/=====.*decoding/,$p' $TMPDIR/ex1.txt | sed -n 150,175p; sed -n '/===== reproduce_hazon_2022.ipynb/,/=====.*decoding/p' $TMPDIR/ex1.txt | sed -n '/runs of consecutive/,/single-cell SNR per neuron/p'; grep -n "PF width\|trial-by-trial\|eigen\|peak of the\|share of" $TMPDIR/ex1.txt
```

```
centre: 20 bins 11.84 cm, 30 bins 11.94; bin counts more than one SEM below 20: []
class_mean: 20 bins 11.85 cm, 30 bins 11.94; bin counts more than one SEM below 20: []

458 runs, 9153 run-bin samples, 3.9 frames per sample

500 neurons: IMSE [0.0003 0.0004 0.0007 0.0017 0.0051 0.0128 0.0166 0.0188 0.0207]; fit I0 = 0.00007, N = 704 +/- 554 (95%)

2000 neurons: IMSE [0.0005 0.0005 0.0007 0.0018 0.0055 0.013  0.0166 0.0188 0.0205 0.0246
 0.0264 0.0277]; fit I0 = 0.00010, N = 338 +/- 87 (95%)
intervals overlap: True

total run time 40.7 min; peak memory 2.0 GB

runs of consecutive nonzero frames, sample of neurons: 494491 runs, 1.000 of length 1, max 1
events per neuron per minute, by session: median 12.04, range 6.60 to 77.59
session with the most events per neuron per minute: ['Mouse2024', '090858&091446'] 77.59
minutes at 20 Hz: median 30.1, range 20.1 to 46.0
sessions with negative positions:
        mouse        session  frames  n_neg          pmin        pmax
7   Mouse2024  090858&091446   55247    503 -1.262810e+04  728.026879
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/src_nb2.py'
s=open(p).read()
old='''print("sessions with N <= 0 left out of the geometric means:", int((info.N[ok] <= 0).sum()))'''
new=old+'''
good_fit = ok & (info.N > 0) & (info.N < 1e6) & ~info.index.isin(MISALIGNED)
g = info[good_fit & info.large].groupby("mouse").N.apply(gmean)
print(f"variant, large-data sessions without the misaligned sessions and without fits with N "
      f"outside 0 to 1e6 ({int((good_fit & info.large).sum())} sessions): geometric-mean N "
      f"{g.min():.0f} to {g.max():.0f}; 5% slope at {g.min() * (np.sqrt(20) - 1):.0f} to "
      f"{g.max() * (np.sqrt(20) - 1):.0f}; 19 N {19 * g.min():.0f} to {19 * g.max():.0f}")'''
assert old in s; s=s.replace(old,new)
old='''print(ag[["I0", "scs_main", "scs_mean"]].round(5))'''
new=old+'''
Lg = L[good_fit[LARGE].values]
agg_ = Lg.groupby("mouse").mean(numeric_only=True)
r, p = stats.pearsonr(agg_.scs_main, agg_.I0)
print(f"variant without misaligned sessions and fits with N outside 0 to 1e6 ({len(Lg)} sessions):"
      f" r = {r:.3f}, r^2 = {r * r:.3f}, p = {p:.4f}")'''
assert old in s; s=s.replace(old,new)
old='''r, p = stats.pearsonr(Lok.I0N, Lok.asnr)
print(f"across {len(Lok)} sessions, linear r = {r:.3f}, p = {p:.2e}")'''
new=old+'''
Lg = L[good_fit[LARGE].values]
agg_ = Lg.groupby("mouse")[["I0N", "asnr"]].mean()
r, p = stats.pearsonr(agg_.I0N, agg_.asnr)
print(f"variant, linear, without misaligned sessions and fits with N outside 0 to 1e6 "
      f"({len(Lg)} sessions): r = {r:.3f}, r^2 = {r * r:.3f}, p = {p:.2e}")'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
```

```
Wed Nov 11 21:04:56 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import os
T=os.environ['TMPDIR']
R1={
"data-sessions-and-neurons":"""**Result: reproduced.** All 110 sessions in the file meet the working rule (more than 150 neurons and more than 30 valid trials in each direction), from 12 mice, with 27,898 neurons (median 235, 151 to 497). Under the code's rule of more than 200 neurons, 73 sessions from 10 mice are large-data sessions, as the paper says; the Methods' "at least 200" gives 74. The file holds only the 110 working sessions, so the selection from 239 sessions cannot be checked.""",
"single-cell-variability":"""**Result: reproduced.** Under the code's reading (the standard deviation over trials per neuron and class, pooled over sessions, classes and neurons) the response variability is 0.7263 +/- 0.6117, the paper's numbers to four decimals; the variance reading gives 0.9016 +/- 1.5301. The single-cell SNR with the 40 classes together is 0.437 +/- 0.464, so the mean is within 10% of 0.41 and the spread is larger than the paper's 0.34; per direction it is 0.295.""",
"suppl-table1-place-field-properties":"""**Result: not reproduced.** Two of the seven values are within 10% under some reading: the mean event rate over running frames in cells with more than 100 events per 10 min (0.362 Hz against 0.33) and the maximum rate in the same cells (1.461 Hz against 1.4). In-field rates (1.04 to 1.34 Hz) and out-of-field rates (0.15 to 0.25 Hz) are outside, the fitted place-field width is 16 to 18 cm against 37.8 cm, the trial-by-trial variability is 0.04 in event counts and 0.88 to 0.90 in the event trace against 1.2, and the spatial information is 0.15 to 0.16 (footnote formula) or 1.06 to 1.30 bits (log2(20) minus the entropy) against 0.24. The readings left open by the paper (rates, in-field definition, fit, cell selection) are many, and none brings five values within tolerance.""",
"fig1d-noise-correlation-by-field-distance":"""**Result: reproduced.** In both directions the mean noise correlation is highest for pairs with the same place-field peak (rightward 0.0386, leftward 0.0374) and lower at distances of 10 bins or more (0.0064 and 0.0058), and the shuffled correlations (within 0.0002 of zero) are below the unshuffled ones with non-overlapping 95% intervals at every distance from 0 to 10 bins. Pooling all pairs gives the same. 7,859,771 pairs are counted over both directions, against the legend's 3,941,140, which is about half and may count each pair once.""",
"position-measurement-noise":"""**Result: reproduced.** The jitter is 0.277 cm on average over the 110 sessions, from 0.118 to 1.001 cm, all three within tolerance of 0.28, 0.12 and 1.0 cm.""",
"fig3cd-signal-and-noise-growth":"""**Result: reproduced.** Trial shuffling leaves the bin means, and so the signal, unchanged (largest change 7e-16), so the shuffled and unshuffled signal slopes are equal. In the median session the unshuffled noise slope is 0.0154 with a line explaining 98.3% of the variance at 100 neurons or more (positive in 110 of 110 sessions), and the shuffled noise slope is 0.0012, 8.4% of the unshuffled one in the median session; it is below 10% in 72 of 110 sessions.""",
"suppl10-asymptotic-snr-lower-with-correlations":"""**Result: reproduced.** The asymptotic SNR is higher for the shuffled data in 110 of 110 sessions (medians 1.94 and 23.4; Wilcoxon p = 8.8e-20) and the per-animal median is higher for the shuffled data in 12 of 12 mice.""",
"fig3f-signal-slope-beginning-vs-end":"""**Result: partially reproduced, resting on the code's direction of the test.** The signal slope differs strongly between the beginning and the end of runs, but it is larger at the end (pooled medians 0.208 at the beginning and 0.313 at the end), so the legend's test (beginning greater) gives p = 1.00 under every reading, and the code's test (beginning lower) gives p = 1.1e-18 for 110 sessions, as the code printed (2.19e-18). The legend's "decreases" does not hold; the difference the code tested does.""",
"fig3g-noise-slope-decreases-over-run":"""**Result: reproduced.** The noise slope is larger at the beginning than at the end of runs (pooled medians 0.0175 and 0.0116), one-tailed p = 1.9e-09 over 110 sessions (code printed 7.7e-10) and 1.2e-10 over the 73 large-data sessions. The medians along the run fall from 0.0174 to 0.0107 (rightward) with ups and downs; monotonic decrease is not tested.""",
"fig3h-snr-higher-at-run-end":"""**Result: reproduced.** The asymptotic SNR per bin pair is lower at the beginning than at the end of runs (pooled medians 11.7 and 25.1), one-tailed p = 2.8e-26 over 110 sessions (code printed 2.4e-29), and p = 9.4e-17 for rightward runs alone.""",
"fig4a-snr-along-noise-pcs-peaks-at-6":"""**Result: partially reproduced.** The session-mean SNR along the noise components rises to its maximum at the seventh component (0.0730), with the sixth close (0.0719), against the paper's sixth; per-mouse peaks range from the 4th to the 14th. The first six carry 0.358 of the sum over the 14 components that all sessions have and a median 0.103 of each session's own sum, less than half under both.""",
"fig4b-correlations-increase-noise-signal-overlap":"""**Result: reproduced.** With all components (legend and code), the unshuffled minus shuffled sum of squared cosines is positive in 73 of 73 sessions (median 0.119) and in the means of 10 of 10 animals; up to the sixth component (Methods) and with correlation-matrix components it is also positive in every session and animal.""",
"fig4c-overlap-predicts-asymptotic-snr":"""**Result: reproduced.** Across the 10 mice the overlap change (all components) and the unshuffled asymptotic SNR give r = -0.743, r squared 0.552 (adjusted 0.496) and p = 0.0139, as the code printed (r = -0.744, adjusted 0.498, p = 0.0136). With the first six components (r = -0.441) or with the SNR ratio (r = -0.30) the correlation is not significant.""",
"fig5f-pf-width-variance-vs-nsv":"""**Result: reproduced.** Across the 10 mice the variance of place-field widths and the NSV give r = -0.658, r squared 0.433 and p = 0.0385, within tolerance of -0.65, as the code printed (r = -0.657, p = 0.0389). Across the 73 sessions the correlation is weak (r = -0.140, p = 0.24).""",
"fig5hi-nsv-predicts-noise-correlation-effect":"""**Result: reproduced.** With the ratio unshuffled over shuffled, the NSV correlates across the 10 mice with r = 0.869 (p = 0.0011) and across the 73 sessions with r = 0.716 (p = 1.1e-12), both within tolerance of 0.83 and 0.76; with the code's filters (69 sessions) r = 0.872 and 0.708. The inverse ratio gives negative correlations, as expected.""",
"suppl-table2-nsv-best-predictor":"""**Result: reproduced.** Of the eleven variables the NSV has the highest adjusted R squared across sessions (0.505, next the number of neurons at 0.191), with and without the filters, and across animals (0.724). At a fixed 200 neurons the NSV still correlates with the ratio across sessions (r = 0.475, p = 2.2e-05) and animals (r = 0.730, p = 0.017). As in the paper's table, the number of neurons correlates with the ratio (r = -0.450, p = 1e-04) and the number of trials less (r = -0.205, p = 0.08).""",
"pf-width-variance-not-predictive":"""**Result: not reproduced.** On the 73 sessions the variance of place-field widths correlates with the asymptotic SNR ratio at r = -0.240, p = 0.041, which reaches the paper's 0.05; across animals r = -0.571, p = 0.085. The effect is the size the paper reports (r = -0.21, p = 0.082), and with the code's filters (69 sessions) p = 0.102. The variance of place-field amplitudes, which the text also names, correlates with the ratio across sessions (r = 0.327, p = 0.005) and animals (r = 0.746, p = 0.013).""",
"fig5cd-synthetic-narrow-widths-broader-nsv":"""**Result: reproduced, resting on the legend's width distributions.** With the legend's uniform half-widths the median NSV is higher for the narrow distribution (0.0033 against 0.0020), and the mean NSV stays higher for it at 100, 1,000 and 10,000 neurons. With the Methods' log-normal half-widths the broad distribution has the higher NSV (0.0044 against 0.0030), at every size.""",
}
R2={
"fig2d-rms-error-ensemble-vs-shuffled":"""**Result: reproduced, resting on the decoder's regularisation.** The median RMS error with all neurons is 9.36 cm (IQR 3.92) with noise correlations and 4.80 cm (IQR 1.73) after shuffling, against 9.38 +/- 4.06 and 5.15 +/- 2.40 cm; both medians and the ensemble IQR are within tolerance, the shuffled IQR is not, and the ensemble error is larger in 109 of 110 sessions. Without the six sessions whose events do not track position the medians are 9.14 and 4.78 cm. With C = 0.1 or 10 in place of 1 the medians on 12 sessions change by less than 0.4 cm.""",
"fig2cd-shuffle-better-in-all-bins":"""**Result: reproduced.** The session-mean RMS error is larger for the ensemble than for the shuffled data in 20 of 20 positions and 40 of 40 classes, and the correct-class fraction averaged over sessions is higher for the shuffled data in 40 of 40 classes (38 to 40 of 40 in each session of animal 2022). Misclassifications are most often one bin (median 1 bin, 70.6% of errors); errors of up to 5 bins each hold at least 1% of the misclassified samples with correlations, and up to 3 bins without.""",
"fig2ef-imse-saturates-with-correlations":"""**Result: reproduced.** Over 110 sessions the fitted asymptotic IMSE (I0 N) is higher for the shuffled data in 97 sessions (Wilcoxon p = 3.5e-17) and N in 94 (p = 5.2e-15); over the 12 per-animal means p = 4.9e-04 and 1.5e-03, and the mean I0 N is higher for the shuffled data in 12 of 12 animals. At all neurons the unshuffled IMSE reaches a median 0.49 of its fitted asymptote, the shuffled IMSE a negligible fraction: the shuffled curves are close to straight lines, and 78 of their fits give N above 1e6, while 7 unshuffled fits are degenerate too.""",
"suppl7b-initial-slope-lower-with-correlations":"""**Result: reproduced.** I0 differs between unshuffled and shuffled data (Wilcoxon p = 9.8e-16 over 110 sessions); it is lower with correlations (median 0.00010 against 0.00019, shuffled higher in 102 sessions).""",
"saturation-ensemble-size":"""**Result: not reproduced.** Under reading (a), 73 large-data sessions, the geometric mean of N per animal spans 30 to 886, so the 5% slope is reached at 105 to 3,076 neurons and 95% of the asymptote at 575 to 16,830, against 346 to 1,402 and 1,894 to 7,671; both bounds are outside tolerance. The lowest animal (2011, N = 30) includes the sessions whose events do not track position. Reading (b), 110 sessions, gives a far wider range, from degenerate fits in animals 2010 and 2029.""",
"suppl11b-i0-vs-single-cell-snr":"""**Result: not reproduced.** Across the 10 mice I0 does not correlate with the single-cell SNR under any reading (r = -0.071, -0.114 and -0.016). The per-mouse mean I0 of animal 2011 is 23.7, from degenerate fits; the other animals are between 0.00005 and 0.00031.""",
"suppl11c-asymptotic-imse-vs-asymptotic-snr":"""**Result: reproduced, on the log scale.** On the log scale the per-mouse I0 N and asymptotic SNR give r = 0.894, r squared 0.800 and p = 4.8e-04, within tolerance of 0.88 and below 0.001. On the linear scale r = 0.039, because a few degenerate fits with very large I0 N dominate the per-mouse means.""",
"suppl8-task-performance-and-accuracy":"""**Result: not reproduced.** Performance correlates with the number of trials (r = 0.847, p = 3.8e-21), as the paper reports, but the asymptotic accuracy does not correlate with the number of trials (log10 I0 N, r = -0.054) or with performance (r = 0.189, p = 0.11), against 0.34 and 0.52. In the path model both predictors are significant (performance p = 1.0e-04, trials p = 3.5e-04, with a negative coefficient).""",
"suppl6-twenty-bins-near-optimal":"""**Result: reproduced.** Relative to the continuous position the mean RMS error is 11.84 cm with 20 bins and 11.94 cm with 30 bins, within tolerance of 11.75 and 11.53 cm. 10 and 15 bins give lower means (11.20 and 11.26 cm), but none is more than one SEM (0.96 cm) below 20 bins. The prediction at the class mean position gives the same values within 0.06 cm.""",
"suppl9-fit-recovers-saturation":"""**Result: reproduced.** On the simulated ensembles the fitted N is 704 +/- 554 from 500 neurons and 338 +/- 87 from 2,000 neurons (95% intervals), and the intervals overlap. The estimate from 500 neurons is imprecise: its interval is six times wider.""",
}
SUM1="""| Claim | Outcome |
|---|---|
| data-sessions-and-neurons | reproduced |
| single-cell-variability | reproduced |
| suppl-table1-place-field-properties | not reproduced |
| fig1d-noise-correlation-by-field-distance | reproduced |
| noise-correlation-not-physical-distance | blocked: data missing (no cell positions) |
| position-measurement-noise | reproduced |
| fig3cd-signal-and-noise-growth | reproduced |
| suppl10-asymptotic-snr-lower-with-correlations | reproduced |
| fig3f-signal-slope-beginning-vs-end | partially reproduced (assumed: the code's direction) |
| fig3g-noise-slope-decreases-over-run | reproduced |
| fig3h-snr-higher-at-run-end | reproduced |
| fig4a-snr-along-noise-pcs-peaks-at-6 | partially reproduced |
| fig4b-correlations-increase-noise-signal-overlap | reproduced |
| fig4c-overlap-predicts-asymptotic-snr | reproduced |
| fig5f-pf-width-variance-vs-nsv | reproduced |
| fig5hi-nsv-predicts-noise-correlation-effect | reproduced |
| suppl-table2-nsv-best-predictor | reproduced |
| pf-width-variance-not-predictive | not reproduced |
| fig5cd-synthetic-narrow-widths-broader-nsv | reproduced (assumed: the legend's widths; simulation) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Differences from the paper's method: signal and noise use 20 neuron subsets per ensemble size in
place of 80; the event trace is rebuilt from the deposited onsets with the Methods' alpha kernel;
the place-field table rests on readings the paper leaves open. The decoding claims are in the
second notebook.

What was found about the dataset: the file holds the 110 working sessions only, as event onsets
(single frames with amplitudes), not the convolved trace the paper analyses. Sessions last about
30 min at 20 Hz (20 to 46), not about 20 min. Four sessions have position values far below the
track (down to -3.7e7 pixels). Two session IDs join two recordings, one of them with 6 times the
usual event rate. In six sessions the event trace does not track the position at lag 0: in two
(Mouse2012 141832, Mouse2011 142436) it does at a lag of 80 to 90 frames, and in two (Mouse2011
105556 and 104511) at no lag within 200 frames. There are no cell positions."""
SUM2="""| Claim | Outcome |
|---|---|
| fig2d-rms-error-ensemble-vs-shuffled | reproduced (assumed: SVM regularisation) |
| fig2cd-shuffle-better-in-all-bins | reproduced |
| fig2ef-imse-saturates-with-correlations | reproduced |
| suppl7b-initial-slope-lower-with-correlations | reproduced |
| saturation-ensemble-size | not reproduced |
| suppl11b-i0-vs-single-cell-snr | not reproduced |
| suppl11c-asymptotic-imse-vs-asymptotic-snr | reproduced |
| suppl8-task-performance-and-accuracy | not reproduced |
| suppl6-twenty-bins-near-optimal | reproduced |
| suppl9-fit-recovers-saturation | reproduced (simulation) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Differences from the paper's method: the decoder is libsvm's one-vs-one linear SVM with C = 1 and
voting, not MATLAB's fitcecoc with an unregularised SpaRSA fit and loss-weighted decoding; 10
repetitions with all neurons, 4 subsets per ensemble size and sizes in steps of 25, against 80
and steps of 10; 2 repetitions per bin count. The IMSE fits that rest on these fewer, noisier
points are often degenerate, which is the likeliest reason the claims built on I0 and N (the
saturation range, I0 against single-cell SNR, the performance correlations) are not reproduced.

What was found about the dataset: see the first notebook; the sessions whose events do not track
position inflate the decoding error (up to 51.9 cm) and give degenerate fits."""
for fn,R,S in (('src_nb1.py',R1,SUM1),('src_nb2.py',R2,SUM2)):
    p=os.path.join(T,fn); s=open(p).read()
    for k,v in R.items():
        tag='# RESULT_'+k
        assert tag in s, k
        import textwrap
        s=s.replace(tag, '\n'.join('# '+l for l in textwrap.wrap(v, 96)))
    s=s.replace('# SUMMARY_PLACEHOLDER','\n'.join('# '+l if l else '#' for l in S.split('\n')))
    assert 'RESULT_' not in s and 'PLACEHOLDER' not in s
    open(p,'w').write(s)
print('ok')
EOF
bash $TMPDIR/build.sh; cd  python tools/entry.py check entries/hazon-2022 | tail -2; date -u
```

```
ok
0 error(s)
Wed Nov 11 21:05:59 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "per-mouse peak\|per-session peak\|pooled pairs\|distance  [0-9]*: unshuffled" $TMPDIR/ex1.txt | head -30
```

```
120:  distance  0: unshuffled 0.0386 +/- 0.0040   shuffled 0.00002 +/- 0.00011
121:  distance  1: unshuffled 0.0296 +/- 0.0028   shuffled 0.00002 +/- 0.00011
122:  distance  2: unshuffled 0.0220 +/- 0.0022   shuffled -0.00006 +/- 0.00012
123:  distance  3: unshuffled 0.0177 +/- 0.0021   shuffled -0.00009 +/- 0.00015
124:  distance  5: unshuffled 0.0130 +/- 0.0029   shuffled 0.00005 +/- 0.00016
130:  pooled pairs: distance 0 0.0372, >= 10 0.0054; separated 0..10: True
134:  distance  0: unshuffled 0.0374 +/- 0.0024   shuffled 0.00011 +/- 0.00014
135:  distance  1: unshuffled 0.0284 +/- 0.0020   shuffled 0.00002 +/- 0.00011
136:  distance  2: unshuffled 0.0208 +/- 0.0018   shuffled -0.00016 +/- 0.00011
137:  distance  3: unshuffled 0.0154 +/- 0.0015   shuffled -0.00005 +/- 0.00014
138:  distance  5: unshuffled 0.0098 +/- 0.0013   shuffled -0.00009 +/- 0.00018
144:  pooled pairs: distance 0 0.0369, >= 10 0.0053; separated 0..10: True
215:per-session peak component: median 8.0 counts {np.int64(5): 8, np.int64(7): 11, np.int64(6): 9, np.int64(13): 3, np.int64(8): 6, np.int64(10): 2, np.int64(15): 2, np.int64(18): 2, np.int64(9): 6, np.int64(3): 1, np.int64(12): 4, np.int64(11): 1, np.int64(4): 6, np.int64(23): 2, np.int64(19): 1, np.int64(16): 2, np.int64(14): 3, np.int64(17): 1, np.int64(2): 1, np.int64(24): 1, np.int64(30): 1}
216:per-mouse peak: {'Mouse2011': 5, 'Mouse2012': 4, 'Mouse2019': 7, 'Mouse2021': 8, 'Mouse2022': 13, 'Mouse2023': 5, 'Mouse2024': 6, 'Mouse2025': 5, 'Mouse2026': 9, 'Mouse2028': 8}
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import os
T=os.environ['TMPDIR']
p=T+'/src_nb1.py'; s=open(p).read()
s=s.replace("per-mouse peaks range from the 4th to the\n# 14th.","per-mouse peaks range from the 4th to the\n# 13th.")
s=s.replace("the 4th to the 14th","the 4th to the 13th")
s=s.replace("the shuffled correlations (within 0.0002 of zero)","the shuffled means at the printed distances (within 0.0002 of zero)")
open(p,'w').write(s)
print('14th' in s, '13th' in s)
p=T+'/src_nb2.py'; s=open(p).read()
s=s.replace("(38 to 40 of 40 in each session","(39 to 40 of 40 in each session")
s=s.replace("(38 to 40 of 40 in\n# each session","(39 to 40 of 40 in\n# each session")
print('38 to 40' in s)
open(p,'w').write(s)
EOF
grep -n "13th\|0.0002 of zero" $TMPDIR/src_nb1.py | head; grep -n "to 40 of 40" $TMPDIR/src_nb2.py
```

```
False True
False
506:# or more (0.0064 and 0.0058), and the shuffled means at the printed distances (within 0.0002 of zero) are below the
784:# sixth; per-mouse peaks range from the 4th to the 13th. The first six carry 0.358 of the sum over
259:# averaged over sessions is higher for the shuffled data in 40 of 40 classes (39 to 40 of 40 in
```

**Agent calls Bash**

```bash
bash $TMPDIR/build.sh; cd  rm -rf entries/hazon-2022/__pycache__; date -u; python tools/entry.py all entries/hazon-2022 2>&1 | tail -8; date -u
```

```
Wed Nov 11 21:06:20 UTC 2026
Installed kernelspec registry-hazon-2022 in executed/hazon-2022/.venv/share/jupyter/kernels/registry-hazon-2022
0 error(s)
pass  reproduce_hazon_2022.ipynb  (474 s)
pass  reproduce_hazon_2022_decoding.ipynb  (2523 s)
Wed Nov 11 21:56:25 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/hazon-2022; python3 - <<'EOF' > $TMPDIR/ex2.txt
import json
for f in ['reproduce_hazon_2022.ipynb','reproduce_hazon_2022_decoding.ipynb']:
    nb=json.load(open(f))
    print('=====',f)
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream' and o.get('name')=='stdout': print(''.join(o['text']))
EOF
diff <(grep -v " s$\| s;\|min;\| s,\|run time\|memory\|decoding:\|bin-count variant:\|s per repetition" $TMPDIR/ex1.txt) <(grep -v " s$\| s;\|min;\| s,\|run time\|memory\|decoding:\|bin-count variant:\|s per repetition" $TMPDIR/ex2.txt)
```

```
392a393
> variant, large-data sessions without the misaligned sessions and without fits with N outside 0 to 1e6 (65 sessions): geometric-mean N 207 to 716; 5% slope at 717 to 2487; 19 N 3925 to 13610
409a411
> variant without misaligned sessions and fits with N outside 0 to 1e6 (65 sessions): r = 0.750, r^2 = 0.562, p = 0.0125
413a416
> variant, linear, without misaligned sessions and fits with N outside 0 to 1e6 (65 sessions): r = 0.919, r^2 = 0.845, p = 1.69e-04
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(s.get('required'));
o=s['properties']['outcomes']['items'];print('outcome req',o.get('required'));print(list(o['properties'].keys()))
print(list(s['properties'].keys()))
print(s['properties']['provenance'])
" | head -40; ls attempts | grep hazon
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
outcome req ['claim', 'outcome']
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
{'type': 'object', 'additionalProperties': False, 'required': ['kind', 'accountable'], 'properties': {'kind': {'enum': ['agent', 'person']}, 'accountable': {'description': 'The person or organisation responsible for this attempt.', 'type': 'object', 'additionalProperties': False, 'required': ['name'], 'properties': {'name': {'type': 'string'}, 'orcid': {'type': 'string', 'pattern': '^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$'}, 'ror': {'type': 'string'}}}, 'agent': {'description': 'Required when kind is agent.', 'type': 'object', 'additionalProperties': False, 'required': ['harness', 'model', 'protocol'], 'properties': {'harness': {'type': 'string'}, 'model': {'type': 'string'}, 'protocol': {'description': 'Version of the reproduction protocol the agent followed.', 'type': 'string'}}}, 'runner': {'description': 'Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.', 'type': 'object', 'additionalProperties': False, 'required': ['platform'], 'properties': {'platform': {'description': "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", 'type': 'string', 'minLength': 1}, 'url': {'description': 'The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.', 'type': 'string', 'pattern': '^https://'}}}}}
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python -c "import yaml" 2>&1 || uv pip install -q pyyaml; python -c "import yaml;print(yaml.__version__)"; date -u
```

```
6.0.3
Wed Nov 11 21:56:49 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/mkattempt.py <<'EOF'
import yaml
NB1 = "reproduce_hazon_2022.ipynb"
NB2 = "reproduce_hazon_2022_decoding.ipynb"
def o(claim, outcome, nb, notes, measured=None, deviations=None, assumed=None, blocked_by=None):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if nb:
        d["notebook"] = nb
        d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed: d["assumed"] = True
    return d

SN_DEV = ("Signal and noise use 20 random neuron subsets per ensemble size, each with its own trial "
          "split, where the paper uses 80 (Methods, Analyzing signal and noise, paragraph 3), to fit "
          "the time limit.")
TRACE_DEV = ("The file holds event onsets only; the event trace is rebuilt from them with the Methods' "
             "alpha kernel (tau 0.2 s, sampled at 20 Hz from 0.05 to 1.5 s, causal) and divided by "
             "its standard deviation (Methods, Event detection algorithm, last two steps; code "
             "DecodeTensor.tensor_loader, 'HD_gamma').")
SVM_DEV = ("The decoder is libsvm's one-vs-one linear SVM (scikit-learn SVC on a linear kernel) with "
           "C = 1 and majority voting, in place of MATLAB fitcecoc of templateLinear learners with "
           "lasso, Lambda 0, SpaRSA and loss-weighted decoding (code decoding/my_algs.m). The paper's "
           "unregularised fit has no exact equivalent here; C = 1 is assumed as the standard choice, "
           "and C = 0.1 and 10 are shown on 12 sessions as variants.")
REPS_DEV = ("10 repetitions with all neurons, and 4 neuron subsets at ensemble sizes 1, 25, 50, ... "
            "(steps of 25) plus all neurons, where the paper uses 80 and steps of 10 (code "
            "decode_series, default_opt d_neurons 10), to fit the time limit.")
MIS_NOTE = ("Six sessions whose event trace does not track position at lag 0 (data check) are kept, "
            "as the paper's selection includes them.")

outcomes = [
o("data-sessions-and-neurons", "reproduced", NB1,
  "All 110 sessions in the file meet the working rule (more than 150 neurons, more than 30 valid "
  "trials each way), from 12 mice, 27,898 neurons, median 235, 151 to 497. More than 200 neurons "
  "(code) gives 73 large-data sessions from 10 mice; 200 or more (Methods) gives 74 from 10. The "
  "file holds only the 110 working sessions, so the selection from 239 cannot be checked.",
  measured=[12, 110, 27898, 235, 151, 497, 73, 10],
  deviations=["The 239 recorded sessions are not in the dataset; the 110 count is checked as the "
              "number of sessions meeting the rule, as the criterion allows."]),
o("single-cell-variability", "reproduced", NB1,
  "Code reading (SD over trials per neuron and class, pooled over 1,115,920 session, class and "
  "neuron values) 0.7263 +/- 0.6117, equal to the paper to four decimals; variance reading 0.9016 "
  "+/- 1.5301. Single-cell SNR with the 40 classes together 0.437 +/- 0.464 over 27,898 neurons "
  "(5 with no response); per direction 0.295 +/- 0.294. Both means match under the first reading; "
  "the SNR spread (0.464) is larger than the paper's 0.34.",
  measured=[0.7263, 0.6117, 0.437, 0.464],
  deviations=[TRACE_DEV, "All valid trials of each direction are used (code variance_per_neuron.mlx "
              "works on the session tensor), not the equalised trials of the decoder."]),
o("suppl-table1-place-field-properties", "not_reproduced", NB1,
  "Two of seven values are within 10% under some reading, the mean event rate over running frames "
  "in cells with more than 100 events per 10 min (0.362 Hz) and the maximum binned rate in those "
  "cells (1.461 Hz). Out of tolerance under every reading run are the in-field rate (1.04 to 1.34 "
  "Hz against 0.88), the out-of-field rate (0.15 to 0.25 against 0.034), the fitted FWHM (16.4 to "
  "18.5 cm against 37.8), the trial-by-trial variability (0.036 to 0.043 in event counts, 0.88 to "
  "0.90 in the event trace, against 1.2) and the spatial information (0.15 to 0.16 by the "
  "footnote's formula read literally, 1.06 to 1.30 bits as log2(20) minus the entropy, against "
  "0.24). The 'minimal spatial modulation' selection (maximum rate above 20% of the SD over the "
  "track) keeps every fitted cell, so it equals all cells. Gaussian fits failed for 1536 "
  "rightward and 1422 leftward tuning curves, and 195 widths above 1180 cm were dropped.",
  measured=[0.362, 1.042, 0.153, 1.461, 18.464, 0.902, 0.163],
  deviations=["Readings run for the open details (criterion) are rates over running frames or "
              "the whole session; in-field within the fitted half-amplitude width or above half "
              "the peak; per-direction fits and fits pooled over both directions; all cells and "
              "cells with more than 100 events per 10 min (Supplementary Figure 3 legend). The "
              "measured values listed are, per quantity, the reading closest to the paper.",
              "Trial-by-trial variability was computed both on event counts per visit, as the "
              "footnote says (spike count), and on the event trace tensor, a reading added because "
              "the counts are far from the paper's scale.",
              "The footnote formula for spatial information is garbled in the text; it was read "
              "literally ((1/N) sum p log2 p, sign dropped) and as log2(N) minus the entropy of the "
              "binned rate distribution."]),
o("fig1d-noise-correlation-by-field-distance", "reproduced", NB1,
  "Mean over 110 sessions, rightward, distance 0 0.0386 against 0.0064 at 10 or more bins; "
  "leftward 0.0374 against 0.0058. Shuffled means at the printed distances are within 0.0002 of "
  "zero, and the 95% intervals separate from the unshuffled ones at every distance 0 to 10, in both "
  "directions; pooling all pairs gives the same. 7,859,771 pairs over both directions against the "
  "legend's 3,941,140, about half, which fits counting each pair once over the two directions.",
  deviations=["Pairs whose correlation is undefined in a bin (a neuron silent over all trials of "
              "that bin) are averaged over the remaining bins; a pair with no defined bin is "
              "dropped."]),
o("noise-correlation-not-physical-distance", "blocked", None,
  "The test needs the positions of the cells in the field of view (code "
  "neuropil_contamination_argument.m uses cell centroids, cellAnatomicLocat). event_traces.mat "
  "holds only mouse_name, session_ID, traces and position, and the data set has no other file.",
  blocked_by="data_missing"),
o("position-measurement-noise", "reproduced", NB1,
  "Robust jitter over 110 sessions, mean 0.277 cm, range 0.118 to 1.001 cm, median 0.235; none "
  "above 1.1 cm.",
  measured=[0.277, 0.118, 1.001],
  deviations=["Position is converted to cm with the code's 118 cm over the 5th to 95th percentile "
              "span (the file gives pixels without a scale)."]),
o("fig3cd-signal-and-noise-growth", "reproduced", NB1,
  "Shuffling leaves the bin means unchanged (largest change 7e-16), so the signal and its slope "
  "are identical with and without shuffling. Median session, unshuffled noise slope 0.0154 with "
  "R squared 0.983 at 100 neurons or more (slope positive in 110 of 110 sessions, R squared at "
  "least 0.9 in 109); shuffled noise slope 0.0012, a median 0.084 of the unshuffled slope (below "
  "0.1 in 72 of 110 sessions).",
  deviations=[SN_DEV, TRACE_DEV]),
o("suppl10-asymptotic-snr-lower-with-correlations", "reproduced", NB1,
  "Asymptotic SNR medians 1.94 unshuffled and 23.4 shuffled; shuffled higher in 110 of 110 "
  "sessions, Wilcoxon p = 8.8e-20; per-animal median higher for shuffled in 12 of 12 mice.",
  deviations=[SN_DEV]),
o("fig3f-signal-slope-beginning-vs-end", "partially_reproduced", NB1,
  "The signal slope is larger at the end of runs than at the beginning (pooled medians 0.208 and "
  "0.313, 220 values). The legend's one-tailed test (beginning greater) gives p = 1.00 under both "
  "readings (pooled and rightward only) and for 110 or 73 sessions. The code's test (beginning "
  "lower) gives p = 1.1e-18 pooled over 110 sessions, as the code printed (2.19e-18), and p = "
  "1.8e-09 for rightward runs. Medians along the run are U-shaped, highest in the end bins. The "
  "significant difference holds only in the code's direction, so the outcome rests on that "
  "reading; the legend's 'decreases' is contradicted. The question is recorded for the authors.",
  deviations=[SN_DEV, "Assumed, the direction of the test is the code's (signrank(begin, end, "
              "'tail', 'left')), as the criterion allows; the legend states the opposite."],
  assumed=True),
o("fig3g-noise-slope-decreases-over-run", "reproduced", NB1,
  "Pooled medians 0.0175 at the beginning and 0.0116 at the end; one-tailed (beginning greater) p = "
  "1.9e-09 over 110 sessions (code printed 7.7e-10), p = 1.2e-10 over the 73 large-data "
  "sessions. Medians along rightward runs fall from 0.0174 to 0.0107, not strictly monotonic; "
  "monotonicity is not tested.",
  deviations=[SN_DEV]),
o("fig3h-snr-higher-at-run-end", "reproduced", NB1,
  "Pooled medians 11.7 at the beginning and 25.1 at the end; one-tailed (beginning lower) p = "
  "2.8e-26 over 110 sessions (code printed 2.4e-29), 5.7e-21 over 73; rightward only p = 9.4e-17.",
  deviations=[SN_DEV]),
o("fig4a-snr-along-noise-pcs-peaks-at-6", "partially_reproduced", NB1,
  "With 100 splits per bin pair as in the code, the mean over 73 sessions of the per-session median "
  "over bin pairs peaks at the 7th component (0.0730), the 6th close (0.0719). Per-session peaks "
  "have median 8; per-mouse peaks 4 to 13. The first six carry 0.358 of the sum over the 14 "
  "components that all sessions have, and a median 0.103 of each session's own sum; below one "
  "half either way. A preparatory run with 20 splits peaked at the 6th, so the peak index is "
  "sensitive to sampling between 6 and 7 (that run is not part of the record).",
  measured=7),
o("fig4b-correlations-increase-noise-signal-overlap", "reproduced", NB1,
  "All components, covariance eigenvectors, the unshuffled minus shuffled sum of cos squared is "
  "positive in 73 of 73 sessions (median 0.119) and in all 10 animal means (smallest 0.066). Up to "
  "the sixth component, median 0.137, and with correlation-matrix eigenvectors 0.200 (all) and "
  "0.089 (six), positive in every session and animal under each reading.",
  deviations=["The shuffle and the eigenvectors use all trials of each direction (code Cloud.m), not "
              "equalised trials."]),
o("fig4c-overlap-predicts-asymptotic-snr", "reproduced", NB1,
  "Across 10 mice, overlap change (all components) against unshuffled asymptotic SNR, r = -0.743, r "
  "squared 0.552, adjusted 0.496, p = 0.0139 (code printed r = -0.744, adjusted 0.498, p = 0.0136). "
  "Other readings are not significant, six components r = -0.441 (p = 0.20), SNR ratio r = -0.304 "
  "(p = 0.39). Across 73 sessions r = -0.356, p = 0.002.",
  measured=0.496, deviations=[SN_DEV]),
o("fig5f-pf-width-variance-vs-nsv", "reproduced", NB1,
  "Across 10 mice r = -0.658, r squared 0.433, p = 0.0385 (code printed r = -0.657, p = 0.0389). "
  "Across 73 sessions r = -0.140, p = 0.24.",
  measured=-0.658),
o("fig5hi-nsv-predicts-noise-correlation-effect", "reproduced", NB1,
  "Ratio unshuffled over shuffled. No filter, across 10 mice r = 0.869 (r squared 0.755, p = "
  "0.0011), across 73 sessions r = 0.716 (p = 1.1e-12). With the code's filters as approximated "
  "here (69 sessions) r = 0.872 and 0.708. The inverse ratio gives r = -0.620 and -0.354.",
  measured=[0.869, 0.716],
  deviations=[SN_DEV, "The confidence intervals for the code's filter (values larger than their "
              "interval) are delta-method 95% intervals from the standard errors of the two line "
              "slopes; the code's intervals over subsets were not reproduced."]),
o("suppl-table2-nsv-best-predictor", "reproduced", NB1,
  "NSV has the highest adjusted R squared across 73 sessions (0.505; next the number of neurons, "
  "0.191) and across animals (0.724); with the filters (69 sessions) 0.494, next 0.233. At a fixed "
  "200 neurons (100 subsets) the NSV correlates with the ratio across sessions r = 0.475, p = "
  "2.2e-05, and animals r = 0.730, p = 0.017. Number of neurons against the ratio r = -0.450, p = "
  "1e-04 (paper -0.54); number of trials r = -0.205, p = 0.08 (paper -0.18, p = 0.12).",
  deviations=[SN_DEV, "The eleven variables were computed from the definitions in the table's notes, "
              "per bin pair and averaged over the 38 pairs; the effective number of modes is read "
              "as (sum lambda)^2 / sum lambda^2 of the noise covariance of the first bin, and the "
              "two inverse sums of fourth powers as (sum cos^2)^2 / sum cos^4."]),
o("pf-width-variance-not-predictive", "not_reproduced", NB1,
  "Paper's test on 73 sessions, variance of place-field widths against the asymptotic SNR ratio, r "
  "= -0.240, p = 0.041, which reaches 0.05; across animals r = -0.571, p = 0.085. The effect has "
  "the paper's size (r = -0.21, p = 0.082), and with the code's filters (69 sessions) p = 0.102 "
  "and across animals p = 0.077. The variance of PF amplitudes correlates with the ratio across "
  "sessions (r = 0.327, p = 0.005) and animals (r = 0.746, p = 0.013).",
  deviations=[SN_DEV]),
o("fig5cd-synthetic-narrow-widths-broader-nsv", "reproduced", NB1,
  "Legend reading (uniform half-widths 0.2 to 1.42 and 0.8 to 2.0 bins), median NSV over 1000 "
  "simulations of 50 cells 0.0033 narrow against 0.0020 broad; mean NSV still higher for narrow at "
  "100, 1,000 and 10,000 cells. Methods reading (log-normal half-widths, log variance 0.3 and 2), "
  "0.0030 narrow against 0.0044 broad, and broad higher at every size. The two readings give "
  "opposite results; the legend's, also shown in Supplementary Figure 16, is adopted. The question "
  "is recorded for the authors.",
  deviations=["Assumed, the width distributions of the legend and Supplementary Figure 16; the "
              "Methods' log-normal distributions give the opposite result.",
              "Standard choices, centres uniform over the continuous 20-bin track, amplitude 1, "
              "tuning evaluated at the bin centres, half-width at half maximum converted to the "
              "Gaussian SD; 200 simulations at 100 and 1,000 cells and 50 at 10,000."],
  assumed=True),
o("fig2d-rms-error-ensemble-vs-shuffled", "reproduced", NB2,
  "Median RMS error over 110 sessions 9.36 cm (IQR 3.92) with correlations and 4.80 cm (IQR 1.73) "
  "shuffled; both medians and the ensemble IQR within tolerance, the shuffled IQR not. Ensemble "
  "larger in 109 of 110 sessions (Wilcoxon p = 9.0e-20). Without the six misaligned sessions 9.14 "
  "and 4.78 cm. With C = 0.1, 1 and 10 on 12 sessions the medians are 8.52, 8.86 and 8.56 cm "
  "(ensemble) and 4.98, 5.03 and 4.99 cm (shuffled). " + MIS_NOTE,
  measured=[9.36, 3.92, 4.80, 1.73],
  deviations=[SVM_DEV, REPS_DEV, TRACE_DEV], assumed=True),
o("fig2cd-shuffle-better-in-all-bins", "reproduced", NB2,
  "Session-mean RMS larger with correlations in 20 of 20 positions and 40 of 40 classes. Correct-"
  "class fraction averaged over sessions higher for shuffled in 40 of 40 classes; in the six "
  "sessions of animal 2022, 39 to 40 of 40 (the Fig. 2c session is not identified in the file). "
  "Misclassified samples are a median 1 bin off (70.6% one bin, 16.7% two); errors up to 5 bins "
  "hold at least 1% of them with correlations, up to 3 bins shuffled.",
  deviations=[SVM_DEV, REPS_DEV]),
o("fig2ef-imse-saturates-with-correlations", "reproduced", NB2,
  "110 sessions, I0 N higher for shuffled in 97 (Wilcoxon p = 3.5e-17), N in 94 (p = 5.2e-15); 12 "
  "per-animal means p = 4.9e-04 and 1.5e-03, I0 N higher for shuffled in 12 of 12 animals. Median "
  "unshuffled IMSE at all neurons is 0.49 of its fitted asymptote. 78 shuffled fits give N above "
  "1e6 or below 0 (near-linear curves) and 7 unshuffled fits are degenerate.",
  deviations=[SVM_DEV, REPS_DEV, "The fit uses scipy curve_fit (Levenberg-Marquardt) from I0 = 1, "
              "N = 100, unbounded, as the code's fit options; MATLAB's fit was not run."]),
o("suppl7b-initial-slope-lower-with-correlations", "reproduced", NB2,
  "Wilcoxon p = 9.8e-16 over 110 sessions; median I0 0.00010 unshuffled and 0.00019 shuffled, "
  "shuffled higher in 102 sessions.",
  deviations=[SVM_DEV, REPS_DEV]),
o("saturation-ensemble-size", "not_reproduced", NB2,
  "Reading (a), 73 sessions, geometric-mean N per animal 30 to 886, 5% slope at 105 to 3,076 "
  "neurons, 19 N at 575 to 16,830; both bounds outside tolerance. Reading (b), 110 sessions, 105 "
  "to 4,918,374 from degenerate fits (animals 2010 and 2029). A variant without the misaligned "
  "sessions and without fits with N outside 0 to 1e6 (65 sessions) gives 717 to 2,487 neurons, "
  "still outside tolerance. The lowest animal (2011, N = 30) holds the misaligned sessions.",
  measured=[105, 3076, 575, 16830],
  deviations=[SVM_DEV, REPS_DEV]),
o("suppl11b-i0-vs-single-cell-snr", "not_reproduced", NB2,
  "Across 10 mice r = -0.071 (Methods reading), -0.114 (mean of per-pair ratios), -0.016 (median). "
  "Animal 2011's mean I0 is 23.7 from degenerate fits; the others are 0.00005 to 0.00031. A "
  "variant without the misaligned sessions and degenerate fits (65 sessions) gives r = 0.750, r "
  "squared 0.562, p = 0.0125, positive but outside the r squared tolerance.",
  measured=0.005, deviations=[SVM_DEV, REPS_DEV, SN_DEV]),
o("suppl11c-asymptotic-imse-vs-asymptotic-snr", "reproduced", NB2,
  "Log scale reading, across 10 mice r = 0.894, r squared 0.800, p = 4.8e-04. Linear reading r = "
  "0.039, dominated by degenerate fits with very large I0 N; without the misaligned sessions and "
  "degenerate fits (65 sessions) the linear r = 0.919, r squared 0.845, p = 1.7e-04.",
  measured=0.800, deviations=[SVM_DEV, REPS_DEV, SN_DEV]),
o("suppl8-task-performance-and-accuracy", "not_reproduced", NB2,
  "73 sessions. Performance against trials r = 0.847, p = 3.8e-21 (within tolerance). Asymptotic "
  "accuracy (log10 I0 N) against trials r = -0.054 and against performance r = 0.189 (p = 0.11); "
  "linear I0 N r = -0.127 and -0.012. Path model, performance p = 1.0e-04, trials p = 3.5e-04 with "
  "a negative coefficient. Performance ranges 0.40 to 0.99.",
  measured=[0.847, -0.054, 0.189],
  deviations=[SVM_DEV, REPS_DEV, "Performance is computed with the code's error_trial_counter.m "
              "logic from the position alone; the session's own reward record is not in the "
              "dataset."]),
o("suppl6-twenty-bins-near-optimal", "reproduced", NB2,
  "Mean RMS relative to continuous position over 110 sessions, 20 bins 11.84 cm (SEM 0.96), 30 "
  "bins 11.94 cm; 10, 15, 25 and 40 bins give 11.20, 11.26, 11.81 and 12.22 cm; none is more than "
  "one SEM below 20 bins. Class-mean prediction gives values within 0.06 cm.",
  measured=[11.84, 11.94],
  deviations=[SVM_DEV, "2 repetitions per session and bin count, where the paper uses 80.",
              "Bin counts 10, 15, 20, 25, 30 and 40 were tested; the paper does not list its own.",
              "Trials are those of the 20-bin selection for every bin count, and (trial, bin) "
              "samples with no frame are dropped (code bin_integration_time_checker.m); the "
              "code's single random frame per bin with an integration window is replaced by the "
              "mean over the bin's frames (the common method of the criterion)."]),
o("suppl9-fit-recovers-saturation", "reproduced", NB2,
  "Simulation of the legend's model. Fitted N 704 +/- 554 (500 neurons) and 338 +/- 87 (2,000 "
  "neurons), 95% intervals overlap. The 500-neuron estimate is imprecise.",
  deviations=["Standard choices for what the legend leaves open, runs at a constant 30 cm/s over "
              "118 cm, 20 Hz frames, independent Gaussian input noise per frame, peak rate 0.05 "
              "events per frame, events summed per run and bin as in the paper's tensor, 40 "
              "classes, half the runs for training."]),
]

findings = [
 {"kind": "data_missing", "statement": "The data set holds only the 110 working sessions of the 239 "
  "recorded, and no positions of the cells in the field of view, so the paper's test that noise "
  "correlations do not depend on the distance between cells cannot be run. There is no reward or "
  "trial record; trials and task performance are rebuilt from the position."},
 {"kind": "other", "statement": "The traces array holds event onsets (single frames with the event "
  "amplitude), as the descriptor says, not the alpha-convolved and normalised event trace the paper "
  "decodes from; the trace must be rebuilt with the Methods' kernel. Rebuilt this way, the response "
  "variability matches the paper's 0.7263 +/- 0.6117 exactly."},
 {"kind": "metadata_insufficient", "statement": "No sampling rate, frame times or spatial scale are "
  "stored; position is in camera pixels. 20 Hz and 118 cm over the 5th to 95th percentile of "
  "position are taken from the paper and its code."},
 {"kind": "metadata_error", "statement": "The descriptor and the paper describe sessions of about 20 "
  "min; at 20 Hz the sessions last a median 30.1 min (20.1 to 46.0)."},
 {"kind": "other", "statement": "In six sessions the event trace does not track the position at lag "
  "0 (a quick decoder gives 14.7 to 44.0 cm mean error, against a median 5.6 cm). In Mouse2012 "
  "141832 and Mouse2011 142436 the events lead by 80 to 90 frames (best lag error 5.4 and 2.8 cm); "
  "Mouse2011 105556 and 104511 show no position information at any lag within 200 frames; "
  "Mouse2026 115639 and Mouse2021 132808 are weaker at lag 0 (14.7 and 15.3 cm). The paper's code "
  "trims the first 350 frames of Mouse2026 115639, which suggests a known offset there."},
 {"kind": "format_error", "statement": "Four sessions have position values far outside the track "
  "(Mouse2012 141832 down to -3.7e7 pixels over 795 frames, Mouse2022 093722 down to -1.5e5, "
  "Mouse2024 090858&091446 a ramp from -12,628 over the first 503 frames, Mouse2028 105610 down to "
  "-23); the first valid trial of Mouse2022 093722 includes such frames."},
 {"kind": "metadata_insufficient", "statement": "Two session IDs join two recordings "
  "(Mouse2024 090858&091446 with 55,247 frames, and 130536&130559) without saying how; the first "
  "has 77.6 events per neuron per minute against a median 12.0, with the rate rising about 2.5 "
  "times in its second part."},
 {"kind": "paper_inconsistency", "statement": "The Figure 3f legend says the signal slope decreases "
  "over the run, while the code's test (signrank(begin, end, tail left)) and its printed p = "
  "2.19e-18 test an increase; the data show an increase (medians 0.208 at the start and 0.313 at "
  "the end of runs)."},
 {"kind": "paper_inconsistency", "statement": "The synthetic place-field model has uniform half-width "
  "distributions in the Figure 5 legend and Supplementary Figure 16, and log-normal ones in the "
  "Methods; simulated, they give opposite results for which distribution has the higher NSV."},
 {"kind": "methods_unavailable", "statement": "Questions for the paper's authors. (1) Which direction "
  "does the Figure 3f signal-slope test take, the legend's decrease or the code's increase? This "
  "attempt follows the code. (2) Which half-width distributions produced Figure 5a to 5d, the "
  "legend's uniform ones or the Methods' log-normal ones? This attempt follows the legend. (3) The "
  "decoder is fitted with Lambda 0 (no regularisation); was this the setting for all published "
  "results? This attempt uses an L2 SVM with C = 1, and C = 0.1 and 10 change the median error by "
  "less than 0.4 cm. (4) How were the Supplementary Table 1 values computed (rates over running or "
  "all frames, the in-field definition, the cells averaged, the spatial information formula, and "
  "whether trial-by-trial variability uses counts or the event trace)? None of the readings "
  "tried gives more than two of the seven values."},
]

rec = {
 "schema_version": 3,
 "id": "hazon-2022-01",
 "datasets": [{"archive": "crcns", "id": "hc-30", "version": "unversioned", "doi": "10.6080/K0GH9G5X",
               "relation": "primary"}],
 "paper": "doi:10.1038/s41467-022-31254-y",
 "date": "2026-11-11",
 "entry": "hazon-2022",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-14"},
                "runner": {"platform": "GitHub Actions",
                           "url": "https://github.com/catalystneuro/encore/actions/runs/43082448402"}},
 "inputs": [{"what": "Method details where the paper is silent (trial selection, tensor, shuffle, "
             "decoder settings, signal and noise, overlap, NSV, PF half-width, jitter, performance "
             "and bin-count procedures), cited by file in hc30.py. No data are taken from it.",
             "source": "https://github.com/approbatory/ML-project at commit "
             "2057af9facfd3035c573e1254bdc32ed4781ba60"}],
 "outcomes": outcomes,
 "findings": findings,
}
yaml.safe_dump(rec, open("attempts/hazon-2022-01.yaml", "w"),
               sort_keys=False, allow_unicode=True, width=100)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/mkattempt.py && cd  && python tools/entry.py check entries/hazon-2022 | tail -3; grep -c "claim:" attempts/hazon-2022-01.yaml; date -u
```

```
0 error(s)
57
Wed Nov 11 21:58:22 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -rln "attempt.schema" tools tests scripts 2>/dev/null | head; python tools/entry.py --help 2>&1 | head -20
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
```

**Agent calls Write**

```json
{
 "file_path": "entries/hazon-2022/README.md",
 "content": "# Hazon et al. (2022) from CRCNS hc-30\n\nTests the findings of [Hazon et al. (2022)](https://doi.org/10.1038/s41467-022-31254-y) on\n[CRCNS hc-30](https://doi.org/10.6080/K0GH9G5X), which holds the event onsets and track positions\nof the paper's 110 working sessions (12 mice, 27,898 CA1 neurons). The helper `hc30.py` streams\nthe one data file and rebuilds the paper's event trace, trials, activity tensor, trial shuffle,\ndecoders and signal and noise measures, citing the paper or its code for each choice.\n\n| Claim | Outcome |\n|---|---|\n| Sessions, mice and neuron counts | Reproduced |\n| Single-cell response variability and SNR | Reproduced |\n| Place-field properties (Supplementary Table 1) | Not reproduced |\n| Noise correlations fall with place-field distance and vanish with shuffling | Reproduced |\n| Correlations do not depend on the cells' physical distance | Blocked: no cell positions |\n| Position measurement noise 0.28 cm | Reproduced |\n| Signal and noise growth with ensemble size | Reproduced |\n| Asymptotic SNR lower with correlations | Reproduced |\n| Signal slope changes over the run (Fig. 3f) | Partially reproduced (larger at the end, as the code tests) |\n| Noise slope falls over the run | Reproduced |\n| SNR higher at the end of runs | Reproduced |\n| SNR along noise components peaks at the sixth | Partially reproduced (peak at the seventh) |\n| Correlations increase noise and signal overlap | Reproduced |\n| Overlap predicts asymptotic SNR across animals | Reproduced |\n| PF width variance against NSV across animals | Reproduced |\n| NSV predicts the effect of correlations | Reproduced |\n| NSV is the best predictor (Supplementary Table 2) | Reproduced |\n| PF width variance does not predict the effect | Not reproduced |\n| Synthetic narrow width distributions have higher NSV | Reproduced (legend's widths) |\n| RMS error 9.38 against 5.15 cm | Reproduced |\n| Shuffled decoding better in every bin | Reproduced |\n| IMSE saturates with correlations, not without | Reproduced |\n| Initial slope I0 differs | Reproduced |\n| Saturation at 346 to 1402 neurons | Not reproduced |\n| I0 against single-cell SNR | Not reproduced |\n| Asymptotic IMSE against asymptotic SNR | Reproduced (log scale) |\n| Task performance and decoding accuracy | Not reproduced |\n| Twenty bins near the smallest error | Reproduced |\n| Fit recovers saturation on simulated data | Reproduced (simulation) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nIn six sessions the event trace does not track the position at lag 0; two are offset by about 4\ns and two show no alignment. The attempt record, with the reasons and the differences from the\npaper's method, is [`attempts/hazon-2022-01.yaml`](../../attempts/hazon-2022-01.yaml).\n"
}
```

```
File created successfully at: entries/hazon-2022/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/hazon-2022 | tail -2; python tools/entry.py handover entries/hazon-2022 2>&1 | tail -5; ls executed/hazon-2022/handover; git status --short | head; date -u
```

```
0 error(s)
wrote executed/hazon-2022/handover
hazon-2022.yaml
hc30.py
reproduce_hazon_2022.ipynb
reproduce_hazon_2022_decoding.ipynb
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
Wed Nov 11 21:58:51 UTC 2026
```

**Agent calls Bash**

```bash
cd  git status --short | grep -v "^?? \.\(bash\|git\|idea\|mcp\|profile\|ripgrep\|vscode\|z\)"; python3 -c "
import json
nb=json.load(open('executed/hazon-2022/handover/reproduce_hazon_2022.ipynb'))
print(sum('Result:' in ''.join(c['source']) for c in nb['cells']))"
```

```
?? attempts/hazon-2022-01.yaml
?? entries/hazon-2022/
?? scripts
0
```

**Agent calls Bash**

```bash
cd  ls -la scripts | head; git log --oneline -1 -- scripts 2>&1 | head -2
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 11 18:56 scripts
```

**Agent**

I've finished steps 1 to 5 and the handover (step 6). The entry is `entries/hazon-2022/` (two notebooks plus the helper `hc30.py`) and the record is `attempts/hazon-2022-01.yaml`. `entry.py check` and `all` passed, `handover` built `executed/hazon-2022/handover/`, and nothing was committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| data-sessions-and-neurons | reproduced |
| single-cell-variability | reproduced (0.7263 +/- 0.6117, exactly the paper's numbers) |
| suppl-table1-place-field-properties | not reproduced (2 of 7 values match) |
| fig1d-noise-correlation-by-field-distance | reproduced |
| noise-correlation-not-physical-distance | blocked, data_missing (no cell positions) |
| position-measurement-noise | reproduced (mean 0.277 cm, range 0.118 to 1.001) |
| fig3cd-signal-and-noise-growth | reproduced |
| suppl10-asymptotic-snr-lower-with-correlations | reproduced |
| fig3f-signal-slope-beginning-vs-end | partially reproduced, assumed (the effect runs the way the code tests, opposite to the legend) |
| fig3g-noise-slope-decreases-over-run | reproduced |
| fig3h-snr-higher-at-run-end | reproduced |
| fig4a-snr-along-noise-pcs-peaks-at-6 | partially reproduced (peak at the 7th component) |
| fig4b-correlations-increase-noise-signal-overlap | reproduced |
| fig4c-overlap-predicts-asymptotic-snr | reproduced (r = -0.743, p = 0.0139) |
| fig5f-pf-width-variance-vs-nsv | reproduced (r = -0.658, p = 0.0385) |
| fig5hi-nsv-predicts-noise-correlation-effect | reproduced |
| suppl-table2-nsv-best-predictor | reproduced |
| pf-width-variance-not-predictive | not reproduced (p = 0.041 on 73 sessions) |
| fig5cd-synthetic-narrow-widths-broader-nsv | reproduced, assumed (legend's width distributions) |
| fig2d-rms-error-ensemble-vs-shuffled | reproduced, assumed (SVM C = 1); 9.36 vs 4.80 cm |
| fig2cd-shuffle-better-in-all-bins | reproduced |
| fig2ef-imse-saturates-with-correlations | reproduced |
| suppl7b-initial-slope-lower-with-correlations | reproduced |
| saturation-ensemble-size | not reproduced |
| suppl11b-i0-vs-single-cell-snr | not reproduced |
| suppl11c-asymptotic-imse-vs-asymptotic-snr | reproduced (log-scale reading) |
| suppl8-task-performance-and-accuracy | not reproduced |
| suppl6-twenty-bins-near-optimal | reproduced |
| suppl9-fit-recovers-saturation | reproduced (simulation) |

**(2) What was found about the dataset**
- **Contents and version:** one MATLAB file (142 MB, MD5 matches `checksums.md5`) holding only the 110 working sessions. It holds event onsets, not the convolved trace the paper decodes, and has no cell positions, frame times, spatial scale or reward record. The version is pinned as `unversioned` because CRCNS has only one published version, and the notebook header records the MD5.
- **Misaligned sessions:** in six sessions the event trace does not track position at lag 0.
  - Two (Mouse2012 141832, Mouse2011 142436) line up at a lag of 80 to 90 frames.
  - Two (Mouse2011 105556 and 104511) line up at no lag within 200 frames.
- **Positions off the track:** four sessions have position values far off the track, down to -3.7e7 pixels.
- **Joined sessions:** two session IDs join two recordings; one of them has 6 times the usual event rate.
- **Session length:** sessions last about 30 min at 20 Hz, where the paper and the descriptor say about 20.
- **Paper inconsistencies:**
  - The Fig. 3f legend says the signal slope decreases over the run, but the code tests (and the data show) an increase.
  - The width distributions in the Fig. 5 legend and in the Methods give opposite simulation results.
- **Assumptions:** SVM C = 1 with voting (C = 0.1 and 10 change the median error by less than 0.4 cm), the code's test direction for Fig. 3f, and the legend's widths for Fig. 5a to 5d.
- **Questions for the paper's authors** (recorded as a `methods_unavailable` finding): the Fig. 3f direction, the width distributions, the decoder regularisation, and how the Supplementary Table 1 values were computed.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or missing something**
1. archives.md covers zip files; hc-30 is a plain `.mat`. I streamed it whole into memory with fsspec.
2. The protocol does not say what to do with sessions that fail the clock check when the paper's own selection includes them. I kept them and showed variants without them.
3. It is unclear whether a variant the author adds (dropping degenerate fits or misaligned sessions) may decide an outcome when the criterion does not list it. I let only the criterion's readings decide and reported the variants in the notes.
4. For the absence claim, "the paper's test as written" was ambiguous: the table header says 73 sessions, but its notes add a filter. I followed the criterion's 73 sessions.
5. The fig3f criterion says an outcome that holds only in the code's direction "rests on that reading" but names no outcome label. I chose partially_reproduced with `assumed: true`.
6. The protocol describes a single notebook. I split the work into two for time, each with its own header and summary.
7. Conclusions can only be written after seeing the outputs, but any edit forces a full re-run. For a 50-minute entry that doubled the compute. Three variant numbers that appeared only in the second run are in the record's notes but not in the notebook's conclusions.
8. There is no rule for using fewer repetitions than the paper instead of blocking as `too_large`. I used fewer and recorded each as a deviation:
   - signal and noise: 20 subsets instead of 80;
   - decoding: 10 full-ensemble repetitions and 4 subsets per size, in steps of 25, instead of 80 in steps of 10;
   - bin-count variant: 2 repetitions per bin count.
9. `check` requires the version string to appear in the code, so I added `VERSION = "unversioned"` to the helper.
10. It is unclear whether the paper's code, read only for method details, is an `input`. I listed it.

**(4) Runtime and failures**
- About 3 h 05 min wall time.
- The notebooks take 8 min and 42 min in the clean environment. Each was run twice; the results matched apart from the added variant cells.
- The IMSE fits are often degenerate: 7 unshuffled and 78 shuffled fits give N below 0 or above 1e6. This is the likeliest cause of the three failed claims built on I0 and N (saturation range, I0 against single-cell SNR, performance and accuracy).
- Nothing failed to run.
- Untracked `.bashrc`/dotfiles and a `scripts` device node at the repo root are sandbox artefacts I did not create or touch.

## End of run

95 turns, 179 minutes, $8.71 at API prices, result: success.
