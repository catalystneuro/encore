# elie-2019 · author · run 43501306087

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper | head -50
```

```
<persisted-output>
Output too large (40.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ea682754-10b6-48b5-b540-fcbb89022792/tool-results/b1ag3nuns.txt

Preview (first 2KB):
Fri Nov 13 20:27:54 UTC 2026
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ea682754-10b6-48b5-b540-fcbb89022792/tool-results/b1ag3nuns.txt"
}
```

```
1	Fri Nov 13 20:27:54 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 739 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/elie-2019.yaml; ls paper; cat papers/datasets/elie-2019.yaml; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat README.md | head -80; cat docs/archives.md | sed -n '/CRCNS/,/^## [A-Z]/p' | head -120
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 88 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ea682754-10b6-48b5-b540-fcbb89022792/tool-results/biorim1ym.txt"
}
```

```
1	# Claims for Elie & Theunissen (2019), PLoS Computational Biology 15(9):e1006698, "Invariant neural
2	# responses for sensory categories revealed by the time-varying information for communication calls",
3	# doi:10.1371/journal.pcbi.1006698, on CRCNS data set aa-4 (doi:10.6080/K00C4T06).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC6762074, open access), as JATS XML flattened to text under
8	# paper/: main text, Methods, Table 1, and the legends of Figures 1 to 10 and of S1 to S7 Fig. The
9	# supplement is the seven figures whose legends are in the text; it has no other file. No PDF was
10	# supplied. The extraction drops every displayed equation: the information formulas, the
11	# coherence-based information (Methods, Time-varying spike rate estimation), the exponential model
12	# of the cumulative information (Results, Time-varying Information for 3 example neurons), the
13	# definition of the CII (Methods, Calculation of the expected value of categorical information) and
14	# the confusion-matrix information. Where the words around an equation or the code fix it, the
15	# criteria say so; where not, the equation is named as open and the reading the text allows is given.
16	# The author may read those equations in the published article (they are not figures). The data
17	# set's description (paper/aa-4.data-description.txt) was read only to know what it holds; no claim
18	# comes from it.
19	#
20	# Code read: https://github.com/julieelie/PoissonTimeVaryingInfo, commit 97802032 (2019-04-01), the
[... 784 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/aa-4.data-description.txt; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=aa-4/" | python -c "import sys,re; d=sys.stdin.read(); [print(k,s) for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',d)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; cd $TMPDIR && curl -s $B/data/CRCNSCode.tar.gz | tar tzv | head -60
```

```
ee387cc051e5fa5ee66a5f4db5d8bae6  data/BlaBro09xxF.tar.gz
baabaf8aa449c1b6e7138a37a1267920  data/CRCNSCode.tar.gz
16f1bb223946288f8b426d6382f06510  data/GreBlu9508M.tar.gz
80c181eb8bd70ddbbd9b3aa46587dfb5  data/LblBlu2028M.tar.gz
2ba7776cd4130d0090b13e5f5c0359fd  data/WhiBlu5396M.tar.gz
c47d6660019a2a0d1e3375ce7da68bf1  data/WhiWhi4522M.tar.gz
6027933cdf765dd0b67f811b1a133095  data/YelBlu6903F.tar.gz
d68011366738da82c7cce800fbbb2022  docs/crcns_aa-4_data_description.docx
eaa1bf674eb92a954d7bab61de3a5f0e  docs/crcns_aa-4_data_description.pdf
ca6a647eebe3ad68924029f872c95645  filelist.txt
# CRCNS.org 'aa-4' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data/BlaBro09xxF.tar.gz	1306705539 (1.2 GB)
 data/CRCNSCode.tar.gz	398459 (389.1 KB)
 data/GreBlu9508M.tar.gz	1779075074 (1.6 GB)
 data/LblBlu2028M.tar.gz	281649302 (268.6 MB)
 data/WhiBlu5396M.tar.gz	195086134 (186.0 MB)
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && time (curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/WhiBlu5396M.tar.gz | tar tzv > wb.txt); wc -l wb.txt; head -30 wb.txt; awk '{print $6}' wb.txt | sed 's/.*\.//' | sort | uniq -c
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && for b in BlaBro09xxF GreBlu9508M LblBlu2028M WhiWhi4522M YelBlu6903F; do (curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/$b.tar.gz | tar tzv > $b.txt) & done; wait; cp wb.txt WhiBlu5396M.txt; for f in *M.txt *F.txt; do echo $f $(grep -c '\.h5$' $f) ss=$(grep -c '_ss[0-9]*\.h5$' $f) wav=$(grep -c wav$ $f) other=$(grep -v -e '\.h5$' -e 'wav$' -e '/$' $f | wc -l); done; grep -v -e '\.h5$' -e 'wav$' *.txt | grep -v f32 | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p code && curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/CRCNSCode.tar.gz | tar xz -C code && cat code/CRCNSCode/read_unit_h5file.m; python -c "import h5py,fsspec,numpy; print(h5py.__version__)"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls entries/fouke-2025/*; head -c 3000 attempts/fouke-2025-01.yaml
```

```
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
  runtime_minutes: 6
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.12 venv && . venv/bin/activate && uv pip install -q h5py fsspec aiohttp requests numpy scipy pandas statsmodels matplotlib jupyter nbconvert ipykernel diptest numba 2>&1 | tail -2; python -c "
import tarfile,fsspec,h5py,io
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/WhiBlu5396M.tar.gz',block_size=2**22).open()
t=tarfile.open(fileobj=f,mode='r|gz')
n=0
for m in t:
    if m.name.endswith('_ss1.h5'):
        b=t.extractfile(m).read(); h=h5py.File(io.BytesIO(b),'r')
        print(m.name, dict(h.attrs))
        def show(name,obj):
            if name.count('/')<=3: print(name, obj, dict(obj.attrs) if len(obj.attrs)<30 else list(obj.attrs)[:30])
        h.visititems(show)
        break
"
```

```
<persisted-output>
Output too large (320.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ea682754-10b6-48b5-b540-fcbb89022792/tool-results/bdba9qw6h.txt

Preview (first 2KB):
WhiBlu5396M/Site6_L5200_e3_s0_ss1.h5 {'electrode': np.float64(3.0), 'ldepth': np.float64(5200.0), 'site': np.bytes_(b'Site6'), 'sortType': np.bytes_(b'single'), 'sortid': np.float64(1.0), 'source_directory': np.bytes_(b'/auto/fdata/julie/Exported_data_tank/WhiBlu5396M')}
Call <HDF5 group "/Call" (34 members)> {}
Call/100 <HDF5 group "/Call/100" (10 members)> {'callerAge': np.bytes_(b'A'), 'callid': np.bytes_(b'Th'), 'original_wavfile': np.bytes_(b'/auto/fdata/julie/Stims/WhiBlu5396M/Call/wavfiles_Familiar_calls/WhiBlu5698_Th_4-2-5.wav'), 'pvalue': np.float64(0.37370947309497815), 'stim_class': np.bytes_(b'Con'), 'stim_duration': np.float64(2.5), 'stim_md5': np.bytes_(b'ea20a0331b2b94d61145f20148edc0b4'), 'stim_source': np.bytes_(b'familiar'), 'stim_source_sex': np.bytes_(b'm'), 'stim_type': np.bytes_(b'call'), 'tdt_wavfile': np.bytes_(b'/auto/fdata/julie/Stims/WhiBlu5396M/wavfiles/stim100.wav'), 'tstat': np.float64(0.935994977396633), 'zscore': np.float64(0.2959876007051179)}
Call/100/1 <HDF5 group "/Call/100/1" (2 members)> {'bg_rate': np.float64(0.9888037993006136), 'peri_rate': np.float64(1.6), 'post_time': np.float64(1.0075545300000002), 'pre_time': np.float64(1.0113229750000006)}
Call/100/1/spike_ids <HDF5 dataset "spike_ids": shape (6, 1), type "<f8"> {}
Call/100/1/spike_times <HDF5 dataset "spike_times": shape (6, 1), type "<f8"> {}
Call/100/10 <HDF5 group "/Call/100/10" (2 members)> {'bg_rate': np.float64(0.9866859946612841), 'peri_rate': np.float64(1.6), 'post_time': np.float64(1.0116300600000159), 'pre_time': np.float64(1.0134936599999946)}
Call/100/10/spike_ids <HDF5 dataset "spike_ids": shape (5, 1), type "<f8"> {}
Call/100/10/spike_times <HDF5 dataset "spike_times": shape (5, 1), type "<f8"> {}
Call/100/2 <HDF5 group "/Call/100/2" (2 member
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v -E '^Call/[0-9]+/' /home/runner/.claude/projects/-home-runner-work-encore-encore/ea682754-10b6-48b5-b540-fcbb89022792/tool-results/bdba9qw6h.txt | grep -v -E '^Call/[0-9]+ ' | head -60; grep -E '^Call/[0-9]+ ' /home/runner/.claude/projects/-home-runner-work-encore-encore/ea682754-10b6-48b5-b540-fcbb89022792/tool-results/bdba9qw6h.txt | grep -o "callid': np.bytes_(b'[A-Za-z]*'" | sort | uniq -c
```

```
WhiBlu5396M/Site6_L5200_e3_s0_ss1.h5 {'electrode': np.float64(3.0), 'ldepth': np.float64(5200.0), 'site': np.bytes_(b'Site6'), 'sortType': np.bytes_(b'single'), 'sortid': np.float64(1.0), 'source_directory': np.bytes_(b'/auto/fdata/julie/Exported_data_tank/WhiBlu5396M')}
Call <HDF5 group "/Call" (34 members)> {}
Mask1 <HDF5 group "/Mask1" (30 members)> {}
Mask1/10 <HDF5 group "/Mask1/10" (10 members)> {'original_wavfile': np.bytes_(b'/auto/fdata/julie/Stims/WhiBlu5396M/Mask/1/stim/rip5.wav'), 'pvalue': np.float64(0.41381694979334727), 'stim_class': np.bytes_(b'Syn'), 'stim_duration': np.float64(2.0000409601048577), 'stim_md5': np.bytes_(b'e162bbdac4b35bd3808fda7c9589beef'), 'stim_source': np.bytes_(b'None'), 'stim_source_sex': np.bytes_(b'c'), 'stim_type': np.bytes_(b'mlnoise'), 'tdt_wavfile': np.bytes_(b'/auto/fdata/julie/Stims/WhiBlu5396M/wavfiles/stim10.wav'), 'tstat': np.float64(0.8567421928147781), 'zscore': np.float64(0.2709256696861843)}
Mask1/10/1 <HDF5 group "/Mask1/10/1" (2 members)> {'bg_rate': np.float64(1.6629699491407801), 'peri_rate': np.float64(1.4999692805504927), 'post_time': np.float64(1.6195583350000007), 'pre_time': np.float64(1.8040013300000002)}
Mask1/10/1/spike_ids <HDF5 dataset "spike_ids": shape (8, 1), type "<f8"> {}
Mask1/10/1/spike_times <HDF5 dataset "spike_times": shape (8, 1), type "<f8"> {}
Mask1/10/10 <HDF5 group "/Mask1/10/10" (2 members)> {'bg_rate': np.float64(2.683394893185088), 'peri_rate': np.float64(2.4999488009174877), 'post_time': np.float64(2.476195930000017), 'pre_time': np.float64(1.863311289999956)}
Mask1/10/10/spike_ids <HDF5 dataset "spike_ids": shape (15, 1), type "<f8"> {}
Mask1/10/10/spike_times <HDF5 dataset "spike_times": shape (15, 1), type "<f8"> {}
Mask1/10/2 <HDF5 group "/Mask1/10/2" (2 members)> {'bg_rate': np.float64(2.110993572161772), 'peri_rate': np.float64(1.4999692805504927), 'post_time': np.float64(1.9605914349999694), 'pre_time': np.float64(2.3685529250000172)}
Mask1/10/2/spike_ids <HDF5 dataset "spi
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; mkdir -p entries/elie-2019; grep -n -i -E "404|2015|reference 40|\[40\]|decod" paper/10.1371-journal.pcbi.1006698.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/elie-2019/elie.py",
 "content": "\"\"\"Loading and measures for Elie & Theunissen (2019) on CRCNS aa-4.\n\nData. CRCNS aa-4 is unversioned; the files are read from the public S3 bucket\ncrcnsarchive under aa-4/live/data/, one tar.gz per bird. Each tar.gz is read as\na stream (tarfile mode \"r|gz\" over fsspec), each h5 member is opened in memory\nwith h5py, reduced to what the analysis needs, and dropped. Nothing is written\nto disk.\n\nParameters and where they come from (claims file header, Methods R, B, P):\n- Window 0 to 600 ms after stimulus onset, 60 bins of 10 ms (Methods B; paper,\n  Methods, \"Here, we analyzed the neural response in the first 600ms\").\n- Call stimuli: the h5 group \"Call\" with stim_type \"call\"; call types Ag (Wsst,\n  Ws), Be, DC, Di, LT, Ne, Te, Th and song (So). Whines (Wh) and noise are\n  dropped (claims header, selVoc.m).\n\"\"\"\nfrom __future__ import annotations\n\nimport io\nimport tarfile\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport fsspec\nimport h5py\nimport numpy as np\n\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/\"\nBIRDS = [\"BlaBro09xxF\", \"GreBlu9508M\", \"LblBlu2028M\", \"WhiBlu5396M\", \"WhiWhi4522M\", \"YelBlu6903F\"]\n# md5 sums from aa-4/live/checksums.md5, read on 2026-11-13\nMD5 = {\n    \"BlaBro09xxF\": \"ee387cc051e5fa5ee66a5f4db5d8bae6\",\n    \"GreBlu9508M\": \"16f1bb223946288f8b426d6382f06510\",\n    \"LblBlu2028M\": \"80c181eb8bd70ddbbd9b3aa46587dfb5\",\n    \"WhiBlu5396M\": \"2ba7776cd4130d0090b13e5f5c0359fd\",\n    \"WhiWhi4522M\": \"c47d6660019a2a0d1e3375ce7da68bf1\",\n    \"YelBlu6903F\": \"6027933cdf765dd0b67f811b1a133095\",\n}\nCALL_TYPES = [\"Ag\", \"Be\", \"DC\", \"Di\", \"LT\", \"Ne\", \"Te\", \"Th\", \"So\"]\nT_MAX = 0.6  # s, analysis window (Methods B)\n\n\ndef _s(x):\n    return x.decode() if isinstance(x, bytes) else (x.item() if hasattr(x, \"item\") else x)\n\n\ndef read_unit(h: h5py.File, name: str, bird: str) -> dict:\n    \"\"\"Reduce one unit's h5 file to attributes and its call responses in 0-600 ms.\n\n    Spike times are kept in seconds relative to stimulus onset, as stored, for\n    spikes in [0, T_MAX), plus the count of spikes in the whole response window\n    stored (pre_time / post_time of each trial are kept).\n    \"\"\"\n    u = {\"bird\": bird, \"file\": name.split(\"/\")[-1]}\n    for k, v in h.attrs.items():\n        u[k] = _s(v)\n    u[\"groups\"] = list(h.keys())\n    stims = []\n    for g in h.keys():\n        if g in (\"class_info\", \"extra_info\"):\n            continue\n        for sn, sg in h[g].items():\n            a = {k: _s(v) for k, v in sg.attrs.items()}\n            st = {\"group\": g, \"number\": sn, **{k: a.get(k) for k in (\n                \"callid\", \"callerAge\", \"stim_type\", \"stim_class\", \"stim_source\", \"stim_source_sex\",\n                \"stim_duration\", \"original_wavfile\", \"stim_md5\")}}\n            if a.get(\"stim_type\") != \"call\" and a.get(\"stim_type\") != \"song\":\n                # keep only metadata of non-call stimuli\n                st[\"trials\"] = None\n                st[\"ntrials\"] = len(sg)\n                stims.append(st)\n                continue\n            trials = []\n            for tn in sorted(sg.keys(), key=lambda x: int(x) if x.isdigit() else x):\n                tg = sg[tn]\n                t = np.asarray(tg[\"spike_times\"][()], dtype=float).ravel()\n                ids = np.asarray(tg[\"spike_ids\"][()], dtype=float).ravel()\n                if ids.size == 1 and ids[0] == -999:\n                    t = np.empty(0)\n                trials.append(t[(t >= 0) & (t < T_MAX)].astype(np.float32))\n            st[\"trials\"] = trials\n            st[\"ntrials\"] = len(trials)\n            stims.append(st)\n    u[\"stims\"] = stims\n    u[\"has_class_info\"] = \"class_info\" in h\n    u[\"has_extra_info\"] = \"extra_info\" in h\n    return u\n\n\ndef stream_bird(bird: str, block_size: int = 2**23) -> list[dict]:\n    \"\"\"Stream one bird's tar.gz and return the reduced units of all its h5 files.\"\"\"\n    units = []\n    with fsspec.open(BASE + bird + \".tar.gz\", block_size=block_size).open() as f:\n        with tarfile.open(fileobj=f, mode=\"r|gz\") as tar:\n            for m in tar:\n                if not (m.isfile() and m.name.endswith(\".h5\")):\n                    continue\n                b = tar.extractfile(m).read()\n                with h5py.File(io.BytesIO(b), \"r\") as h:\n                    units.append(read_unit(h, m.name, bird))\n    return units\n\n\ndef load_all(birds=BIRDS, workers: int = 3) -> list[dict]:\n    with ThreadPoolExecutor(workers) as ex:\n        res = list(ex.map(stream_bird, birds))\n    return [u for r in res for u in r]\n\n\ndef call_stims(u: dict) -> list[dict]:\n    \"\"\"The call stimuli of a unit (stim_type call, call types of CALL_TYPES).\"\"\"\n    return [s for s in u[\"stims\"] if s[\"trials\"] is not None and s[\"callid\"] in CALL_TYPES]\n"
}
```

```
File created successfully at: entries/elie-2019/elie.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/elie-2019 && . $TMPDIR/venv/bin/activate && /usr/bin/time -v python -c "
import elie,pickle,time
t=time.time(); U=elie.load_all(); print(len(U), time.time()-t)
pickle.dump(U,open('$TMPDIR/units.pkl','wb'))
" 2>&1 | grep -E "^[0-9]|Maximum resident|Elapsed"
```

```
2298 1102.8610277175903
	Elapsed (wall clock) time (h:mm:ss or m:ss): 18:38.26
	Maximum resident set size (kbytes): 2642728
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . venv/bin/activate && python -c "
import pickle,collections,numpy as np
U=pickle.load(open('units.pkl','rb'))
print(collections.Counter(u.get('sortType') for u in U))
print(collections.Counter((u['bird'],u.get('sortType')) for u in U))
print(collections.Counter(tuple(u['groups']) for u in U).most_common(20))
print(collections.Counter((u['has_class_info'],u['has_extra_info']) for u in U))
print(collections.Counter('_ss' in u['file'] for u in U if u.get('sortType')=='single'))
st=collections.Counter((s['group'][:4],s['stim_type'],s['callid']) for u in U for s in u['stims'])
print(st)
print(set(u.keys()) )
"
```

```
Exit code 1
Fri Nov 13 20:49:07 UTC 2026
Traceback (most recent call last):
  File "<string>", line 11, in <module>
NameError: name 'u' is not defined. Did you mean: 'U'?
Counter({'single': 1278, 'tdt': 845, 'noise': 109, 'multi': 63, b'singl': 3})
Counter({('GreBlu9508M', 'single'): 343, ('WhiWhi4522M', 'single'): 290, ('YelBlu6903F', 'single'): 264, ('BlaBro09xxF', 'tdt'): 213, ('WhiBlu5396M', 'single'): 190, ('GreBlu9508M', 'tdt'): 165, ('WhiWhi4522M', 'tdt'): 160, ('BlaBro09xxF', 'single'): 144, ('WhiBlu5396M', 'tdt'): 143, ('YelBlu6903F', 'tdt'): 129, ('LblBlu2028M', 'single'): 47, ('GreBlu9508M', 'noise'): 39, ('LblBlu2028M', 'tdt'): 35, ('BlaBro09xxF', 'noise'): 22, ('YelBlu6903F', 'noise'): 21, ('WhiWhi4522M', 'noise'): 20, ('YelBlu6903F', 'multi'): 18, ('WhiWhi4522M', 'multi'): 14, ('GreBlu9508M', 'multi'): 13, ('BlaBro09xxF', 'multi'): 7, ('WhiBlu5396M', 'multi'): 7, ('LblBlu2028M', 'multi'): 4, ('WhiBlu5396M', 'noise'): 4, ('LblBlu2028M', 'noise'): 3, ('LblBlu2028M', b'singl'): 2, ('WhiBlu5396M', b'singl'): 1})
[(('Call2', 'class_info', 'extra_info'), 664), (('Call1', 'class_info', 'extra_info'), 661), (('Call3', 'class_info', 'extra_info'), 456), (('Call1', 'STRF1', 'class_info', 'extra_info'), 91), (('Call1c', 'class_info', 'extra_info'), 73), (('Call1', 'Mask1', 'Sel4', 'class_info', 'extra_info'), 63), (('Call', 'Mask1', 'Sel5', 'class_info', 'extra_info'), 57), (('Call', 'Mask1', 'Sel6', 'class_info', 'extra_info'), 48), (('Call', 'Mask1', 'Sel1', 'class_info', 'extra_info'), 45), (('Call', 'Mask1', 'Sel3', 'class_info', 'extra_info'), 44), (('Call', 'Mask1', 'Sel2', 'class_info', 'extra_info'), 43), (('Call', 'Mask1', 'Sel7', 'class_info', 'extra_info'), 37), (('Call1b', 'Call1c', 'class_info', 'extra_info'), 8), (('Mask1', 'class_info'), 7), (('Call', 'Mask1', 'class_info', 'extra_info'), 1)]
Counter({(True, True): 2291, (True, False): 7})
Counter({True: 1278})
Counter({('Call', 'song', None): 52537, ('Call', 'call', 'Te'): 37187, ('Call', 'call', 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python -c "
import pickle,collections,numpy as np, re
U=pickle.load(open('units.pkl','rb'))
c=collections.Counter()
for u in U[:50]:
  for s in u['stims']:
    if s['stim_type']=='song': c[(s['stim_source'],s['stim_class'],re.sub(r'\d','#',s['original_wavfile'].split('/')[-2]+'/'+s['original_wavfile'].split('/')[-1])[:50])]+=1
for k,v in c.most_common(30): print(v,k)
c=collections.Counter()
for u in U[:50]:
  for s in u['stims']:
    if s['stim_type']=='call': c[(s['stim_source'],s['stim_class'],s['callid'],s['original_wavfile'].split('/')[-2])]+=1
for k,v in c.most_common(30): print(v,k)
"
```

```
550 ('unfamiliar', 'Con', 'wavfiles_calls_Always/STRFxx####__So_##.wav')
450 ('unfamiliar', 'Con', 'wavfiles_calls_Always/STRFxx####__So_#.wav')
150 ('unfamiliar', 'Con', 'wavfiles_calls_Once/WhiLbl####_MAS_So_#.wav')
150 ('familiar', 'Con', 'wavfiles_calls_Always/BlaBla####_MAF_So_#.wav')
50 ('familiar', 'Con', 'wavfiles_calls_Once/YelGre####_MAF_So_#.wav')
300 ('familiar', 'Con', 'Ne', 'wavfiles_calls_Always')
300 ('familiar', 'Con', 'Te', 'wavfiles_calls_Always')
300 ('unfamiliar', 'Con', 'Ag', 'wavfiles_calls_Once')
300 ('unfamiliar', 'Con', 'DC', 'wavfiles_calls_Once')
300 ('unfamiliar', 'Con', 'Ne', 'wavfiles_calls_Once')
300 ('unfamiliar', 'Con', 'Te', 'wavfiles_calls_Once')
300 ('unfamiliar', 'Con', 'Be', 'wavfiles_calls_Once')
300 ('familiar', 'Con', 'DC', 'wavfiles_calls_Once')
300 ('familiar', 'Con', 'Te', 'wavfiles_calls_Once')
300 ('unfamiliar', 'Con', 'Be', 'wavfiles_calls_Always')
300 ('unfamiliar', 'Con', 'LT', 'wavfiles_calls_Always')
250 ('familiar', 'Con', 'Th', 'wavfiles_calls_Always')
250 ('familiar', 'Con', 'DC', 'wavfiles_calls_Always')
200 ('familiar', 'Con', 'Ag', 'wavfiles_calls_Always')
150 ('familiar', 'Con', 'Ne', 'wavfiles_calls_Once')
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1111/ejn.12812&format=json&resultType=core" | python -c "import sys,json; d=json.load(sys.stdin); r=d['resultList']['result']; print([(x.get('pmcid'),x.get('isOpenAccess'),x.get('title')) for x in r])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4347984/fullTextXML" -o ejn.xml; ls -la ejn.xml; python - <<'E'
import re
t=open('ejn.xml').read()
t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
open('ejn.txt','w').write(t)
for k in ['404','914','above chance','PCC','discriminant','random forest','selectiv']:
    for m in re.finditer(k,t):
        print(k,'::',t[max(0,m.start()-300):m.start()+400]); print('---'); break
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -A "Mozilla/5.0" "https://pmc.ncbi.nlm.nih.gov/articles/PMC4347984/" -o ejn.html; ls -la ejn.html; python - <<'E'
import re
t=open('ejn.html',errors='ignore').read()
t=re.sub(r'<script.*?</script>',' ',t,flags=re.S); t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
open('ejn.txt','w').write(t)
print(len(t))
for k in ['404','914','above chance','discriminant','Random Forest','PCC']:
    for m in list(re.finditer(k,t))[:2]:
        print(k,'::',t[max(0,m.start()-400):m.start()+400]); print('---')
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
import re
t=open('ejn.txt').read()
i=t.find('Neural data analysis Sorting multi-units')
j=t.find('Discrimination or classification performance of Semantic Informative')
print(t[i:j+200])
E
```

```
Neural data analysis Sorting multi-units to select auditory single units 688 multi-units (2 × 16 × 18 + 16 × 7= 688) were recorded using the protocol described above. These units were sorted into single units based on spike shape (spike sorting) and twice sorted for the quality of their neural responses to sounds: before and after spike sorting. This process yielded 914 single auditory units. To identify units responsive to sounds, we quantified the reliability and strength of the neural activity in response to auditory stimuli by estimating the coherence between a single spike train (R) and the actual time-varying mean response (A). This value of coherence γ A R 2 can be derived from the coherence between the peristimulus time histogram (PSTH) obtained from half of the trials and the PSTH obtained from the other half ( Hsu et al. , 2004b ): γ A R 2 = [ 1 - M 2 × ( 1 - 1 γ R ¯ 1 , M / 2 R ¯ 2 , M / 2 2 ) ] - 1 with M the total number of trials (presentations of the stimuli) and γ R ¯ 1 , M / 2 R ¯ 2 , M / 2 2 the coherence between the two PSTHs calculated on half of the trials. The coherence between two responses is a function of frequency (ω). An overall quantifier of the reliability and strength of the neural response was obtained by integrating over all frequencies ( Hsu et al. , 2004a ): I A R = - ∫ 0 ∞ log 2 [ 1 - γ A R 2 ( ω ) ] d ω . Here I AR is expressed in information units (bits per second) and is an estimate of the mutual information between R and A responses ( Borst &amp; Theunissen, 1999 ). The thresholds used on I AR to consider a unit as responsive to sounds was 3 bits/s for multi-units, yielding 658/688 auditory units before spike sorting, and 2.3 bits/s for spike-sorted units. These thresholds were chosen so that none of the units below that threshold had a spiking rate significantly increased by any stimulus. Spike sorting of multi-units was performed using a semi-automatic custom program written in Matlab that used both un-supervised (k-means) an
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
import re
t=open('ejn.txt').read()
i=t.find('Nine values were tested')
print(t[i:i+7000])
E
```

```
Nine values were tested (2, 5, 10, 20, 30, 50, 100 and 600ms) and the quartiles of the windows selected for the 914 single units were 30/50/100 ms with an average value of 145.5±185.2ms (mean ± sd). This convolution gave two time-varying mean firing rate responses or “smoothed words” of exact same length. Then every possible delay between the two “smoothed words” was tested to find the shortest Euclidian distance between them. Non-overlapping regions of responses were padded with the time average mean firing rate for each response. This process yielded the shortest distance between each of the NR spike patterns or “words” and each of the NS (NV+20) templates of response to stimuli (vocalizations and silences). Then, for each neural response, the algorithm predicted the most probable stimulus that had elicited the spike pattern by choosing the stimulus template that had the shortest distance to that spike pattern. The confusion matrix (see an example on Figure 2A ) represents for each stimulus i (rows: actual stimuli), the joint probability that the T neural responses to that stimulus i were classified as belonging to the same stimulus (diagonal) or the other stimuli (other columns in that row; columns: predicted stimuli j). A unit that would give robust but different spike patterns to every single stimulus would yield a diagonal matrix of value 1/NS while a unit that would give random spike patterns to every single stimulus would yield a uniform matrix of value 1/NS 2 . Figure 2. Confusion Matrices and calculations of Inclusive and Exclusive Categorical Information. Open in a new tab (A) Confusion matrix obtained at the end of the decoding procedure of the spike pattern responses of an example unit. The color in each bin of the matrix represents the joint probability that the neural responses to the stimulus i (rows: actual stimuli) were classified as belonging to the same stimulus (j predicted stimulus and here on the diagonal j=i) or the other stimuli (other colum
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
t=open('ejn.txt').read()
i=t.find('The Inclusive-Cate')
print(t[i:i+5000])
E
```

```
The Inclusive-Categorical-uniform matrix ( Figure 2B ) was obtained by keeping intact the probabilities p(i,j) only if i and j belong to the same semantic category and by substituting the probabilities p(i,j) by the average probability of misclassification within each row if i and j did not belong to the same category. Making uniform the distribution of probabilities of misclassification (i.e. classification outside of the same semantic category) was equivalent to maximizing the randomness of predictions outside semantic categories and removed any systematic classification reflecting other types of information content in the neural responses. The Inclusive-Categorical-uniform matrix ( Figure 2B ) is therefore the matrix with the smallest MI that still preserves all the predictions within categories. In this sense, the MI measure computed this way captures only the information regarding correct semantic classification and correct classification of calls within categories. We call this measure the Inclusive Categorical Information (ICI). Note that the upper bound for estimates of ICI, ICI max , is the same than the upper bound for estimates of MI in the original confusion matrix and equals MI max . For each unit, the value of ICI was normalized by this upper bound for ICI. The Exclusive-Categorical-uniform matrix ( Fig 2C ) was obtained from the Inclusive-Categorical-uniform matrix by making uniform the probabilities of correct categorical classification (i.e. classification within categories): if i and j belong to the same semantic category then the probability p(i,j) was substituted by the average probability of correct classification within each row. This process maximized the randomness of predictions inside semantic categories and further removed any systematic classification reflecting information about individual calls within categories in the neural responses. The Exclusive-Categorical-uniform matrix ( Fig 2C ) is therefore the matrix with the smallest MI that
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep wav$ WhiBlu5396M.txt | head -3; grep wav$ GreBlu9508M.txt | head -3; grep -c . GreBlu9508M.txt
```

```
-rw-r----- jteeters/m2043   124020 2011-05-24 00:31 WhiBlu5396M/wavfiles/stim28.wav
-rw-r----- jteeters/m2043   122114 2011-05-24 00:31 WhiBlu5396M/wavfiles/stim81.wav
-rw-r----- jteeters/m2043   115132 2011-05-24 00:31 WhiBlu5396M/wavfiles/stim16.wav
-rw-r----- jteeters/m2043   122114 2012-03-12 17:19 GreBlu9508M/wavfiles/stim143.wav
-rw-r----- jteeters/m2043     9944 2012-03-12 17:19 GreBlu9508M/wavfiles/stim125.wav
-rw-r----- jteeters/m2043   123948 2012-03-12 17:19 GreBlu9508M/wavfiles/stim156.wav
856
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'E'
import tarfile,fsspec,h5py,io,hashlib
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/LblBlu2028M.tar.gz',block_size=2**23).open()
t=tarfile.open(fileobj=f,mode='r|gz')
md5={}
n=0
for m in t:
    if m.name.endswith('.wav'):
        b=t.extractfile(m).read(); md5[hashlib.md5(b).hexdigest()]=m.name
    elif m.name.endswith('.h5') and n<1:
        h=h5py.File(io.BytesIO(t.extractfile(m).read()),'r'); n+=1
        def show(name,obj): print(name,obj)
        h['class_info'].visititems(show); h['extra_info'].visititems(show)
        g=[k for k in h.keys() if k.startswith('Call')][0]
        print(g, h['class_info'][g]['coherence']['info']['mean'][()], h['class_info'][g]['mean_rate'][()])
        S=[(h[g][s].attrs['stim_md5'].decode(), h[g][s].attrs['tdt_wavfile'].decode().split('/')[-1]) for s in h[g]]
print(len(md5), sum(a in md5 for a,b in S), len(S), [ (md5.get(a),b) for a,b in S[:3]])
E
```

```
Call1 <HDF5 group "/class_info/Call1" (2 members)>
Call1/coherence <HDF5 group "/class_info/Call1/coherence" (6 members)>
Call1/coherence/cutoff_frequency <HDF5 dataset "cutoff_frequency": shape (1, 1), type "<f8">
Call1/coherence/frequencies <HDF5 dataset "frequencies": shape (124, 1), type "<f8">
Call1/coherence/info <HDF5 group "/class_info/Call1/coherence/info" (3 members)>
Call1/coherence/info/lower <HDF5 dataset "lower": shape (1, 1), type "<f8">
Call1/coherence/info/mean <HDF5 dataset "mean": shape (1, 1), type "<f8">
Call1/coherence/info/upper <HDF5 dataset "upper": shape (1, 1), type "<f8">
Call1/coherence/lower <HDF5 dataset "lower": shape (124, 1), type "<f8">
Call1/coherence/mean <HDF5 dataset "mean": shape (124, 1), type "<f8">
Call1/coherence/upper <HDF5 dataset "upper": shape (124, 1), type "<f8">
Call1/mean_rate <HDF5 dataset "mean_rate": shape (1, 1), type "<f8">
STRF1 <HDF5 group "/class_info/STRF1" (2 members)>
STRF1/coherence <HDF5 group "/class_info/STRF1/coherence" (6 members)>
STRF1/coherence/cutoff_frequency <HDF5 dataset "cutoff_frequency": shape (1, 1), type "<f8">
STRF1/coherence/frequencies <HDF5 dataset "frequencies": shape (124, 1), type "<f8">
STRF1/coherence/info <HDF5 group "/class_info/STRF1/coherence/info" (3 members)>
STRF1/coherence/info/lower <HDF5 dataset "lower": shape (1, 1), type "<f8">
STRF1/coherence/info/mean <HDF5 dataset "mean": shape (1, 1), type "<f8">
STRF1/coherence/info/upper <HDF5 dataset "upper": shape (1, 1), type "<f8">
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/elie-2019 && python - <<'E'
s=open('elie.py').read()
s=s.replace('''import fsspec
import h5py
import numpy as np
''','''import hashlib
from concurrent.futures import ProcessPoolExecutor

import fsspec
import h5py
import numpy as np
from scipy.io import wavfile
''')
s=s.replace('from concurrent.futures import ThreadPoolExecutor\n','')
s=s.replace('''T_MAX = 0.6  # s, analysis window (Methods B)
''','''T_MAX = 0.6  # s, analysis window (Methods B)
# Spikes are kept from KEEP[0] to KEEP[1] s around onset: the 2015 decoding of
# units-404 places its 600 ms window around the first sound element and takes
# silence sections from the 600 ms before onset (Elie & Theunissen 2015, Methods,
# Decoding the responses of auditory single units).
KEEP = (-0.7, 1.3)
''')
s=s.replace('''            for tn in sorted(sg.keys(), key=lambda x: int(x) if x.isdigit() else x):
                tg = sg[tn]
                t = np.asarray(tg["spike_times"][()], dtype=float).ravel()
                ids = np.asarray(tg["spike_ids"][()], dtype=float).ravel()
                if ids.size == 1 and ids[0] == -999:
                    t = np.empty(0)
                trials.append(t[(t >= 0) & (t < T_MAX)].astype(np.float32))''','''            for tn in sorted(sg.keys(), key=lambda x: int(x) if x.isdigit() else x):
                tg = sg[tn]
                t = np.asarray(tg["spike_times"][()], dtype=float).ravel()
                ids = np.asarray(tg["spike_ids"][()], dtype=float).ravel()
                if ids.size == 1 and ids[0] == -999:
                    t = np.empty(0)
                trials.append(np.sort(t[(t >= KEEP[0]) & (t < KEEP[1])]))''')
s=s.replace('''    u["stims"] = stims
    u["has_class_info"] = "class_info" in h''','''    u["stims"] = stims
    ci = {}
    if "class_info" in h:
        for g, cg in h["class_info"].items():
            c = cg["coherence"]
            ci[g] = {"mean_rate": float(cg["mean_rate"][()].ravel()[0]),
                     "info": float(c["info"]["mean"][()].ravel()[0]),
                     "info_lower": float(c["info"]["lower"][()].ravel()[0]),
                     "cutoff": float(c["cutoff_frequency"][()].ravel()[0]),
                     "f": c["frequencies"][()].ravel(), "c": c["mean"][()].ravel()}
    u["class_info"] = ci
    u["has_class_info"] = "class_info" in h''')
s=s.replace('''def stream_bird(bird: str, block_size: int = 2**23) -> list[dict]:
    """Stream one bird's tar.gz and return the reduced units of all its h5 files."""
    units = []
    with fsspec.open(BASE + bird + ".tar.gz", block_size=block_size).open() as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tar:
            for m in tar:
                if not (m.isfile() and m.name.endswith(".h5")):
                    continue
                b = tar.extractfile(m).read()
                with h5py.File(io.BytesIO(b), "r") as h:
                    units.append(read_unit(h, m.name, bird))
    return units


def load_all(birds=BIRDS, workers: int = 3) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(stream_bird, birds))
    return [u for r in res for u in r]
''','''def sound_elements(x: np.ndarray, fs: float) -> dict:
    """First sound element of a stimulus (Elie & Theunissen 2015, Methods, Decoding).

    The 2015 paper: "The first sound element was defined as any sound longer than
    30ms and followed by minimum 10ms of silence before the next sound element.
    Silences were defined as periods where the absolute value of the waveform was
    below 35% of the RMS intensity." Assumption: the absolute value is taken as
    an envelope, the maximum of |x| in a sliding 2 ms window, since the raw
    waveform crosses zero within every period; the RMS is that of the whole file.
    """
    x = x.astype(float)
    if x.ndim > 1:
        x = x[:, 0]
    w = max(1, int(round(0.002 * fs)))
    from scipy.ndimage import maximum_filter1d
    env = maximum_filter1d(np.abs(x), w)
    loud = env >= 0.35 * np.sqrt(np.mean(x ** 2))
    d = np.diff(np.r_[0, loud.astype(int), 0])
    on, off = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    # merge elements separated by less than 10 ms of silence
    els = []
    for a, b in zip(on, off):
        if els and (a - els[-1][1]) < 0.010 * fs:
            els[-1][1] = b
        else:
            els.append([a, b])
    els = [(a / fs, b / fs) for a, b in els]
    long_ = [i for i, (a, b) in enumerate(els) if b - a > 0.030]
    i0 = long_[0] if long_ else 0
    first = els[i0] if els else (0.0, len(x) / fs)
    nxt = els[i0 + 1][0] if i0 + 1 < len(els) else np.inf
    return {"on1": first[0], "off1": first[1], "on2": nxt, "dur": len(x) / fs}


def stream_bird(bird: str, block_size: int = 2**23) -> list[dict]:
    """Stream one bird's tar.gz and return the reduced units of all its h5 files.

    The wav files of the bird are matched to the stimuli by their md5 sum, which
    the h5 files store for each stimulus (stim_md5).
    """
    units, wav = [], {}
    with fsspec.open(BASE + bird + ".tar.gz", block_size=block_size).open() as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tar:
            for m in tar:
                if not m.isfile():
                    continue
                if m.name.endswith(".wav"):
                    b = tar.extractfile(m).read()
                    fs, x = wavfile.read(io.BytesIO(b))
                    wav[hashlib.md5(b).hexdigest()] = {"wav": m.name, **sound_elements(x, fs)}
                elif m.name.endswith(".h5"):
                    b = tar.extractfile(m).read()
                    with h5py.File(io.BytesIO(b), "r") as h:
                        units.append(read_unit(h, m.name, bird))
    for u in units:
        for s in u["stims"]:
            s["sound"] = wav.get(s["stim_md5"])
    return units


def load_all(birds=BIRDS, workers: int = 4) -> list[dict]:
    """All units of all birds, the birds streamed in parallel processes."""
    order = sorted(birds, key=lambda b: -["LblBlu2028M", "WhiBlu5396M"].count(b))
    with ProcessPoolExecutor(workers) as ex:
        res = dict(zip(order, ex.map(stream_bird, order)))
    return [u for b in birds for u in res[b]]
''')
s=s.replace('''def call_stims(u: dict) -> list[dict]:
    """The call stimuli of a unit (stim_type call, call types of CALL_TYPES)."""
    return [s for s in u["stims"] if s["trials"] is not None and s["callid"] in CALL_TYPES]''','''def call_type(s: dict) -> str | None:
    """Call type of a stimulus. Songs of the vocalization bank (named after their
    caller) are So; the songs of the search set (files STRFxx..._So_*.wav) and the
    noises are not call stimuli (paper, S4 Fig legend; claims header)."""
    if s["stim_type"] == "call":
        return s["callid"] if s["callid"] in CALL_TYPES else None
    if s["stim_type"] == "song":
        w = (s.get("original_wavfile") or "").split("/")[-1]
        return None if w.startswith("STRF") else "So"
    return None


def call_stims(u: dict) -> list[dict]:
    """The call stimuli of a unit, with their call type in "ct"."""
    out = []
    for s in u["stims"]:
        ct = call_type(s)
        if ct is not None and s["trials"] is not None:
            out.append({**s, "ct": ct})
    return out''')
open('elie.py','w').write(s)
E
grep -n "ThreadPool\|order = " elie.py
```

```
168:    order = sorted(birds, key=lambda b: -["LblBlu2028M", "WhiBlu5396M"].count(b))
```

**Agent calls Bash**

```bash
cd entries/elie-2019 && python - <<'E'
s=open('elie.py').read()
s=s.replace('key=lambda b: -["LblBlu2028M", "WhiBlu5396M"].count(b))','key=lambda b: ["LblBlu2028M", "WhiBlu5396M"].count(b))')
s=s.replace('''            if a.get("stim_type") != "call" and a.get("stim_type") != "song":''','''            if not single or a.get("stim_type") not in ("call", "song"):''')
s=s.replace('''    u["groups"] = list(h.keys())''','''    u["groups"] = list(h.keys())
    # spikes are kept for single units only; other files keep their metadata
    single = str(u.get("sortType", "")).startswith("singl")''')
s=s.replace('''trials.append(np.sort(t[(t >= KEEP[0]) & (t < KEEP[1])]))''','''trials.append(np.sort(t[(t >= KEEP[0]) & (t < KEEP[1])]).astype(np.float32))''')
open('elie.py','w').write(s)
E
. $TMPDIR/venv/bin/activate && /usr/bin/time -v python -c "
import elie,pickle,time
t=time.time(); U=elie.load_all(); print(len(U), time.time()-t)
pickle.dump(U,open('$TMPDIR/units2.pkl','wb'))
" 2>&1 | grep -E "^[0-9]|Maximum resident|Elapsed|Error|error"; date -u
```

```
/bin/bash: line 1: cd: entries/elie-2019: No such file or directory
2298 542.0788931846619
	Elapsed (wall clock) time (h:mm:ss or m:ss): 9:19.62
	Maximum resident set size (kbytes): 3188116
Fri Nov 13 21:01:32 UTC 2026
```

**Agent calls Bash**

```bash
pwd; python - <<'E'
s=open('elie.py').read()
s=s.replace('key=lambda b: -["LblBlu2028M", "WhiBlu5396M"].count(b))','key=lambda b: ["LblBlu2028M", "WhiBlu5396M"].count(b))')
s=s.replace('''            if a.get("stim_type") != "call" and a.get("stim_type") != "song":''','''            if not single or a.get("stim_type") not in ("call", "song"):''')
s=s.replace('''    u["groups"] = list(h.keys())''','''    u["groups"] = list(h.keys())
    # spikes are kept for single units only; other files keep their metadata
    single = str(u.get("sortType", "")).startswith("singl")''')
s=s.replace('''trials.append(np.sort(t[(t >= KEEP[0]) & (t < KEEP[1])]))''','''trials.append(np.sort(t[(t >= KEEP[0]) & (t < KEEP[1])]).astype(np.float32))''')
open('elie.py','w').write(s)
E
grep -n "single\|float32\|order =" elie.py
```

```
entries/elie-2019
45:# Decoding the responses of auditory single units).
64:    # spikes are kept for single units only; other files keep their metadata
65:    single = str(u.get("sortType", "")).startswith("singl")
75:            if not single or a.get("stim_type") not in ("call", "song"):
88:                trials.append(np.sort(t[(t >= KEEP[0]) & (t < KEEP[1])]).astype(np.float32))
170:    order = sorted(birds, key=lambda b: ["LblBlu2028M", "WhiBlu5396M"].count(b))
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && PYTHONPATH=entries/elie-2019 python - <<'E'
import pickle,collections,numpy as np, elie
U=pickle.load(open('units2.pkl','rb'))
S=[u for u in U if str(u.get('sortType')).startswith('singl')]
print('single',len(S))
def calls(u): return elie.call_stims(u)
ns=np.array([len(calls(u)) for u in S]); print('call stims per single unit', ns.mean(), ns.std(), ns.min(), ns.max(), (ns==0).sum())
callg=[ [g for g in u['class_info'] if g.startswith('Call')] for u in S]
print(collections.Counter(len(c) for c in callg))
iar=np.array([max([u['class_info'][g]['info'] for g in c] or [np.nan]) for u,c in zip(S,callg)])
print('IAR', np.nanpercentile(iar,[0,5,25,50,75,100]))
for th in [2.3,3]: print(th,(iar>=th).sum(), (iar>th).sum())
# per bird
print(collections.Counter(u['bird'] for u,i in zip(S,iar) if i>=2.3))
# all stims count including non-call
nall=np.array([len(u['stims']) for u in S]); print('all stims',nall.mean(), nall.min(), nall.max())
nt=[len(s['trials']) for u in S for s in calls(u)]; print('trials',collections.Counter(nt))
snd=[s['sound'] is None for u in S for s in calls(u)]; print('no wav match', sum(snd), len(snd))
ct=collections.Counter(s['ct'] for u in S for s in calls(u)); print(ct)
# duplicate check: hash of all spike times of first 3 stims
import hashlib
h=collections.defaultdict(list)
for u in S:
    st=calls(u)
    if not st: continue
    key=hashlib.md5(b''.join(np.concatenate(s['trials']).tobytes() for s in sorted(st,key=lambda s:s['stim_md5']))).hexdigest()
    h[key].append(u['bird']+'/'+u['file'])
d=[v for v in h.values() if len(v)>1]; print('dups',len(d), d[:5])
E
```

```
single 1278
call stims per single unit 95.35680751173709 14.05420135488003 63 120 0
Counter({1: 1278})
IAR [ 0.          2.76909846  4.70357981  7.46713704 14.31151637 96.84851178]
2.3 1243 1243
3 1185 1185
Counter({'GreBlu9508M': 333, 'WhiWhi4522M': 278, 'YelBlu6903F': 259, 'WhiBlu5396M': 187, 'BlaBro09xxF': 139, 'LblBlu2028M': 47})
all stims 121.90532081377152 73 137
trials Counter({10: 97533, 11: 14346, 9: 8113, 12: 1874})
no wav match 0 121866
Counter({'Te': 20724, 'DC': 19068, 'Ne': 16769, 'So': 14520, 'Ag': 13201, 'Be': 13046, 'Th': 8986, 'LT': 8442, 'Di': 7110})
dups 0 []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 1,200p code/CRCNSCode/h5_plot_one_spike.m | head -120
```

```
function h5_plot_one_spike(Response,Path2Sound, fsnip)
% plots the spectrogram, spike arrival times and average firing rate for
% response structure in our tdt hdf5 files. 
% fsnip is the pointer to the snipet file or -1 if no snipets should be
% plotted.

Before_stim = 2000;                     % Time before stimulus in ms
Total_duration = 6000;                  % Total duration in ms- will give variable after stimulus time
Nsnip = 18;                             % Length of a snippet - the length is set in RPVDs macro used for TDT.
% This value of 20 was taken from 32Channel2EC.rcx in
% Masker_Multielectrode_FJN.  THe snipped length is set in the
% Spike_Store_MC macro.


% Read the stim wave file.
Stim_name = strsplit(Response.tdt_wavfile, '/');
Stim_name = fullfile(Path2Sound,Stim_name{end});
[Sound_in, Samprate] = audioread(Stim_name);

% Get sound, number of trials, etc
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s "https://api.github.com/repos/julieelie/PoissonTimeVaryingInfo/commits?per_page=5" | python -c "import sys,json; [print(c['sha'],c['commit']['author']['date'],c['commit']['message'][:60]) for c in json.load(sys.stdin)]"; curl -s "https://api.github.com/repos/julieelie/PoissonTimeVaryingInfo/git/trees/97802032?recursive=1" | python -c "import sys,json; d=json.load(sys.stdin); print(d.get('sha')); [print(t['path'],t.get('size')) for t in d.get('tree',[])]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && R=https://raw.githubusercontent.com/julieelie/PoissonTimeVaryingInfo/978020328321c7ed83be12c0152bed85ec77e218; mkdir -p repo && cd repo && for f in README.md info_poisson_model_calculus.m cumulative_info_poisson_model_calculus_MCJK.m cumulative_info_poisson_model_MCJK_wrapper.m info_model_Calculus_wrapper2.m; do curl -s $R/$f -o $f; done; cat README.md; . ../venv/bin/activate; python -c "
import fsspec,scipy.io as sio,io
b=fsspec.open('$R/ModelCell_InfoCumInfo_Tutorial.mat').open().read()
try:
  d=sio.loadmat(io.BytesIO(b)); print({k:(type(v),getattr(v,'shape',None),getattr(v,'dtype',None)) for k,v in d.items()})
except Exception as e:
  print(e); import h5py; h=h5py.File(io.BytesIO(b)); h.visititems(lambda n,o: print(n,o))
"
```

```
# PoissonTimeVaryingInfo
Matlab code for calculating time varying information of single units spike patterns about stimulus ID and stimulus category
This code was developped for analysing electrophysioloical recordings of single auditory cortical neurons responding to playback
of vocalizations. This code can be applicable to any system where one wants to measure how much information a neuron convey in
its time-varying spike pattern about the identity of input stimuli or about classes or categories of stimuli.

The core functions of this repository are:

-> *info_poisson_model_calculus.m* which calculates the mutual information between n events (stimuli, categories of stimuli, motor output...)
and a poisson response defined by its n means.

-> *cumulative_info_poisson_model_calculus_MCJK.m* which calculates the cumulative information in a neural response given
conditional probability distributions of responses given stims at each time point. Although it is assumed that this stimulus
conditional probability is time independent (i.e know that stim identity and the rate at a previous time does not tell you 
about the rate at the current time - as in a poisson distribution), the joint probability distribution is not, making the
cumulative information calculation difficult. This algorithm uses a Monte Carlo approximation to estimate this joint probability
distribution. The error on the calculation of cumulative information is estimated by a Jack-knife procedure.

-> *info_cumulative_model_Calculus.m* which calulates the cumulative information in a neural response given
conditional probability distributions of responses given stims at each time point. Although it is assumed that this stimulus
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate; python -c "
import fsspec,scipy.io as sio,io,numpy as np
np.set_printoptions(precision=3,linewidth=200)
R='https://raw.githubusercontent.com/julieelie/PoissonTimeVaryingInfo/978020328321c7ed83be12c0152bed85ec77e218/'
d=sio.loadmat(io.BytesIO(fsspec.open(R+'ModelCell_InfoCumInfo_Tutorial.mat').open().read()))
open('model.pkl','wb').write(__import__('pickle').dumps(d))
print(d['Input_Spike_count']); print(d['Win'],d['Step'],d['Response_samprate'],d['NR_Duration'],d['NTrials'])
sa=d['Spike_array'][0,0]['stim1']; print(type(sa), sa.shape, sa.dtype, sa.sum())
sf=d['Spike_filtered'][0,0]['stim1']; print(sf.shape, sf[:5])
print(d['tin'][0,:5], d['tin'][0,-3:]); print('MSE',d['MSE_KDE_SpikeRate'].ravel(), d['Average_MSE_KDE_SpikeRate'])
print('Info',d['Info_bcorr'].ravel()); print('Icum',d['Icum_EstMonteCarloOpt_bcorr'].ravel())
print(d['Bin_Trials'][0])
"
```

```
[[0.1 0.1 0.1 1.5 2.5 2.5 1.5 0.5 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1]
 [0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1.5 2.5 1.5 1.5 0.5 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1]
 [0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1.  1.5 1.5 1.  0.5 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1]
 [0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 1.  1.5 2.5 1.5 0.5 0.1 0.1 0.1 0.1]]
[[ 10  20  30  40  50  60  70  80  90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300 310 320 330 340 350 360 370 380 390 400]] [[10]] [[1000]] [[400]] [[10]]
<class 'numpy.ndarray'> (10, 400) uint8 121
(1, 400) [[0.005 0.005 0.005 0.006 0.006 0.006 0.007 0.007 0.008 0.009 0.01  0.011 0.012 0.014 0.016 0.018 0.02  0.023 0.027 0.03  0.034 0.039 0.044 0.049 0.055 0.062 0.068 0.075 0.083 0.091 0.099 0.107
  0.115 0.123 0.131 0.14  0.148 0.156 0.163 0.17  0.177 0.184 0.19  0.195 0.2   0.205 0.209 0.212 0.215 0.217 0.219 0.22  0.221 0.221 0.221 0.219 0.218 0.215 0.212 0.209 0.205 0.2   0.195 0.189
  0.183 0.176 0.169 0.161 0.154 0.146 0.138 0.13  0.122 0.114 0.106 0.098 0.091 0.084 0.077 0.07  0.064 0.058 0.053 0.048 0.043 0.039 0.035 0.032 0.028 0.026 0.023 0.021 0.019 0.017 0.015 0.014
  0.013 0.012 0.011 0.01  0.01  0.009 0.009 0.008 0.008 0.007 0.007 0.007 0.006 0.006 0.006 0.005 0.005 0.005 0.004 0.004 0.004 0.004 0.003 0.003 0.003 0.003 0.003 0.003 0.003 0.003 0.003 0.003
  0.003 0.003 0.003 0.004 0.004 0.004 0.004 0.004 0.004 0.005 0.005 0.005 0.005 0.005 0.005 0.006 0.006 0.006 0.006 0.007 0.007 0.008 0.008 0.008 0.009 0.01  0.01  0.011 0.012 0.012 0.013 0.014
  0.014 0.015 0.015 0.015 0.016 0.016 0.016 0.016 0.016 0.016 0.016 0.015 0.015 0.015 0.014 0.014 0.013 0.012 0.012 0.011 0.01  0
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && uv pip install -q adaptivekde 2>&1 | tail -2; python -c "
import adaptivekde, inspect; print(adaptivekde.__file__); from adaptivekde import ssvkernel; print(inspect.signature(ssvkernel.ssvkernel)); print(ssvkernel.ssvkernel.__doc__[:1500])"; pip index versions adaptivekde 2>/dev/null | head -2
```

```
/tmp/claude-1001/venv/lib/python3.12/site-packages/adaptivekde/sskernel.py:9: SyntaxWarning: invalid escape sequence '\i'
  \int k(x - x_i) k(x - x_j) dx  -  2 sum_{i~=j} k(x_i - x_j), where k(x) is
Traceback (most recent call last):
  File "<string>", line 2, in <module>
AttributeError: 'function' object has no attribute 'ssvkernel'
/tmp/claude-1001/venv/lib/python3.12/site-packages/adaptivekde/__init__.py
adaptivekde (1.2.0)
Available versions: 1.2.0, 1.1.1, 1.1.0, 1.0.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python -W ignore -c "
from adaptivekde import ssvkernel; import inspect; print(inspect.signature(ssvkernel)); print(ssvkernel.__doc__[:2500])"; grep -n "ssvkernel\|Spike_filtered\|KDE\|tin" repo/*.m | head;
```

```
(x, tin=None, M=80, nbs=100, WinFunc='Boxcar')

    Generates a locally adaptive kernel-density estimate for one-dimensional
    data.

    The user provides a one-dimensional vector of samples drawn from some
    underlying unknown distribution, and optionally the values where they want
    to estimate the probability density of that distribution. The algorithm
    solves an optimization problem to identify variable bandwidths across the
    domain where the data is provided.

    The optimization is based on a principle of minimizing expected L2 loss
    function between the kernel estimate and an unknown underlying density
    function. An assumption is merely that samples are drawn from the density
    independently of each other.

    The locally adaptive bandwidth is obtained by iteratively computing optimal
    fixed-size bandwidths wihtihn local intervals. The optimal bandwidths are
    selected such that they are selected in the intervals that are gamma times
    larger than the optimal bandwidths themselves. The paramter gamma is
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s https://raw.githubusercontent.com/julieelie/PoissonTimeVaryingInfo/978020328321c7ed83be12c0152bed85ec77e218/Tutorial_TimeVarying_Information.mlx -o tut.mlx && python -c "
import zipfile,re
z=zipfile.ZipFile('tut.mlx'); d=z.read('matlab/document.xml').decode()
t=re.sub(r'<w:p[ >]','\n<',d); t=re.sub(r'<[^>]+>','',t)
open('tut.txt','w').write(t)
" && grep -n -i "kde\|ssvkernel\|sskernel\|Spike_filtered\|MSE\|lambda\|Input_Spike\|poissrnd\|MuLim\|Info_bcorr\|MCJK\|Icum" tut.txt | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 1,400p tut.txt | grep -v "^\s*$" | head -300
```

```
Tutorial on the calculations of time-varying instantaneous  and cumulative Information about stimulus in spike patterns
In this tutorial, we are generating a model neuron responses to hypothetical stimuli in order to demonstrate how to calculate time varying information using the code described in Elie and Theunissen 2018.
The first step consists in obtaining spike pattern responses modeled as inhomogenous Poisson processes. The time varying rates of the artificial neuron in response to 4 hypothetical stimuli is arbitrary fixed. Then these rates are used as the lambdas of inhomogenous Poisson distributions to generate 10 realizations per stimulus.
The second step corresponds to the estimation of the time varying rates by applying the kernel density estimation algorithm written by Hideaki Shimazaki and Shigeru Shinomoto on the realizations generated at step 1. A Jackknife procedure is used to estimate the error on the rate calculation.
The third step consists in binning the obtained time varying rates at 100Hz and calculate the instantaneous information in the neural response about the stimulus at each time bin. The error on the calculation due to the uncertainty of the exact time varying spike rates is estimated by a bootstrap and a Jackknife procedure.
The fourth and final step uses the probability distribution of conditional responses generated at step 3 to calculate the cumulative information about the stimulus at each time bin using a Monte Carlo with importance sampling approach. The error on the calculation due to the uncertainty of the exact time varying spike rates and to the stochastic aspect of the sampling approach is estimated by a bootstrap and a Jackknife procedure.
This tutorial requires the code for calculating kernel density estimates of the spike patterns, ssvkernel, written by Hideaki Shimazaki and Shigeru Shinomoto  and available here:
https://github.com/shimazaki/density_estimation
Several plots call the function shaddedErrorBar written by Rob C
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A6 "^Bias correction\|^The cumulative information\|^Time-varying spike rate estimation" paper/10.1371-journal.pcbi.1006698.txt | cut -c1-2500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "jackknife\|jack-knife\|model neuron\|less than 0.02\|Fig 1" paper/10.1371-journal.pcbi.1006698.txt | cut -c1-900 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 425,441p paper/10.1371-journal.pcbi.1006698.txt | cut -c1-2000; sed -n 87p paper/10.1371-journal.pcbi.1006698.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat >> entries/elie-2019/elie.py <<'E'


# ---------------------------------------------------------------------------
# Time-varying rate and information (claims header, Methods R, B and I)
# ---------------------------------------------------------------------------
from scipy.stats import poisson  # noqa: E402

R_MAX = 20      # spike counts summed from 0 to 20 (paper, Methods, The instantaneous information)
MU_MIN = 1 / 20  # lower bound on the Poisson mean of a bin (same paragraph; code, MuLims)


def kde_rate(spike_times_ms: np.ndarray, n_trials: int, duration_ms: int) -> np.ndarray:
    """Locally adaptive KDE rate (spikes/ms) at 1 kHz, by ssvkernel (Shimazaki and
    Shinomoto; paper reference 42; Methods, Time-varying spike rate estimation),
    from the Python port in the adaptivekde package. The density is scaled by the
    number of spikes over the number of trials. A set with no spike gets
    1/(2*Ntrials*duration) per ms and one with a single spike 1/(Ntrials*duration)
    per ms (same paragraph)."""
    import warnings
    from adaptivekde import ssvkernel
    tin = np.arange(duration_ms) + 0.5
    x = np.asarray(spike_times_ms, dtype=float)
    if x.size == 0:
        return np.full(duration_ms, 1 / (2 * n_trials * duration_ms))
    if x.size == 1 or np.unique(x).size == 1:
        return np.full(duration_ms, x.size / (n_trials * duration_ms))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        y = ssvkernel(x, tin, nbs=0)[0]
    return y * x.size / n_trials


def bin_means(rate_1khz: np.ndarray, bin_ms: int = 10) -> np.ndarray:
    """Poisson mean of each bin: the rate summed over the bin, bounded below by
    1/20 (claims header, Methods B)."""
    r = rate_1khz[: (rate_1khz.size // bin_ms) * bin_ms].reshape(-1, bin_ms).sum(1)
    return np.maximum(r, MU_MIN)


def _pyx(mu: np.ndarray) -> np.ndarray:
    """p(y|s) for y = 0..R_MAX; mu has shape (..., ) -> (..., R_MAX+1)."""
    y = np.arange(R_MAX + 1)
    return poisson.pmf(y, mu[..., None])


def inst_info(mu: np.ndarray, groups: np.ndarray | None = None) -> np.ndarray:
    """Instantaneous information (bits) per bin, mu of shape (n_stim, n_bins).

    With groups (a category per stimulus), p(y|c) is the mean of p(y|s) over the
    stimuli of the category and categories are weighted equally (claims header,
    code info_callsemantic.m)."""
    p = _pyx(mu)  # stim x bins x y
    if groups is not None:
        cats = np.unique(groups)
        p = np.stack([p[groups == c].mean(0) for c in cats])
    py = p.mean(0)
    with np.errstate(divide="ignore", invalid="ignore"):
        hy = -np.nansum(np.where(py > 0, py * np.log2(py), 0), -1)
        hys = -np.nansum(np.where(p > 0, p * np.log2(p), 0), -1).mean(0)
    return hy - hys


def cum_info_mc(mu: np.ndarray, n_samples: int, rng: np.random.Generator,
                groups: np.ndarray | None = None) -> np.ndarray:
    """Cumulative information (bits) from bin 1 to each bin, by Monte Carlo with
    importance sampling (paper, Methods, The cumulative information): samples
    are drawn from the proposal q, the product over bins of the marginal p(y_t),
    and the entropy of the response is the mean of -log2 p(y) weighted by p/q.
    The conditional entropy is exact, as bins are independent given the stimulus
    (or given the category, whose p(y|c) is then the mixture over its stimuli,
    computed by summing over stimuli)."""
    n_stim, T = mu.shape
    p = _pyx(mu)  # s, t, y
    if groups is None:
        groups = np.arange(n_stim)
    cats = np.unique(groups)
    pm = p.mean(0)  # marginal per bin (t, y)
    cdf = np.cumsum(pm, -1)
    u = rng.random((n_samples, T))
    ys = np.minimum((u[..., None] > cdf[None]).sum(-1), R_MAX)  # n x T
    logq = np.cumsum(np.log(pm[np.arange(T), ys]), 1)  # n x T
    lps = np.log(np.maximum(p[:, np.arange(T), ys], 1e-300))  # s x n x T
    cl = np.cumsum(lps, -1)  # s x n x T
    lp = np.logaddexp.reduce(cl, 0) - np.log(n_stim)  # log p(y_1..t)
    w = np.exp(lp - logq)
    hy = -(w * lp).mean(0) / np.log(2)
    # conditional entropy H(Y_1..t | C), with C the category (stimulus by default)
    hyc = np.zeros(T)
    for c in cats:
        idx = np.flatnonzero(groups == c)
        lc = np.logaddexp.reduce(cl[idx], 0) - np.log(idx.size)  # log p(y|c)
        hyc += -(w * np.exp(lc - lp) * lc).mean(0) / np.log(2) / cats.size
    return hy - hyc
E
cd $TMPDIR && . venv/bin/activate && PYTHONPATH=entries/elie-2019 python -W ignore - <<'E'
import pickle,numpy as np,time,elie
d=pickle.loads(open('model.pkl','rb').read())
t=time.time()
for s in range(4):
    a=d['Spike_array'][0,0][f'stim{s+1}']
    tr,ix=np.nonzero(a); st=np.repeat(ix,a[tr,ix].astype(int))+1.0
    r=elie.kde_rate(st,10,400)
print('one kde',(time.time()-t)/4)
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "entries/elie-2019/elie.py", line 224, in kde_rate
    y = ssvkernel(x, tin, nbs=0)[0]
        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/adaptivekde/ssvkernel.py", line 180, in ssvkernel
    y95b = ybsort[int(np.floor(0.05 * nbs)), :]
           ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: index 0 is out of bounds for axis 0 with size 0
```

**Agent calls Bash**

```bash
cd entries/elie-2019 && sed -i 's/y = ssvkernel(x, tin, nbs=0)\[0\]/y = ssvkernel(x, tin, nbs=1)[0]  # nbs: bootstrap CI, unused/' elie.py && cd $TMPDIR && . venv/bin/activate && PYTHONPATH=entries/elie-2019 python -W ignore - <<'E'
import pickle,numpy as np,time,elie
d=pickle.loads(open('model.pkl','rb').read())
t=time.time()
R=[]
for s in range(4):
    a=d['Spike_array'][0,0][f'stim{s+1}']
    tr,ix=np.nonzero(a); st=np.repeat(ix,a[tr,ix].astype(int))+1.0
    r=elie.kde_rate(st,10,400); R.append(r)
print('one kde',(time.time()-t)/4)
R=np.array(R); ref=np.array([d['Spike_filtered'][0,0][f'stim{s+1}'].ravel() for s in range(4)])
print('vs saved KDE max abs diff', np.abs(R-ref).max(), np.abs(R-ref).mean())
model=np.repeat(d['Input_Spike_count']/10,10,1)
print('MAE', np.abs(R-model).mean(1), np.abs(R-model).mean(), 'RMSE',np.sqrt(((R-model)**2).mean()))
mu=np.array([elie.bin_means(r) for r in R]); print(np.round(elie.inst_info(mu),3))
t=time.time(); ci=elie.cum_info_mc(mu,100000,np.random.default_rng(0)); print(time.time()-t); print(np.round(ci,3))
print(np.round(elie.cum_info_mc(np.maximum(d['Input_Spike_count'],1/20),100000,np.random.default_rng(0)),3))
E
```

```
one kde 0.8511805534362793
vs saved KDE max abs diff 0.003302623858234738 0.00039100204758168636
MAE [0.01033952 0.01003396 0.00754843 0.00816622] 0.009022030096610028 RMSE 0.016139804485637954
[0.005 0.013 0.116 0.341 0.477 0.5   0.428 0.206 0.067 0.01  0.004 0.01
 0.244 0.463 0.365 0.228 0.089 0.007 0.008 0.016 0.069 0.204 0.303 0.298
 0.183 0.082 0.038 0.023 0.008 0.018 0.109 0.259 0.424 0.479 0.419 0.223
 0.042 0.007 0.019 0.007]
1.1694631576538086
[0.005 0.018 0.134 0.424 0.653 0.777 0.829 0.851 0.862 0.867 0.868 0.873
 1.051 1.295 1.39  1.417 1.42  1.418 1.421 1.427 1.473 1.595 1.732 1.794
 1.816 1.809 1.812 1.821 1.824 1.825 1.851 1.826 1.887 1.884 1.916 1.911
 1.911 1.945 1.933 1.929]
[0.    0.    0.    0.355 0.64  0.741 0.754 0.764 0.764 0.764 0.764 0.764
 1.076 1.314 1.371 1.38  1.371 1.371 1.371 1.371 1.371 1.53  1.681 1.779
 1.798 1.799 1.799 1.799 1.799 1.799 1.799 1.823 1.882 1.906 1.946 1.959
 1.959 1.959 1.959 1.959]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . venv/bin/activate && python - <<'E'
import pickle,numpy as np
U=pickle.load(open('units2.pkl','rb'))
S=[u for u in U if 'singl' in str(u.get('sortType'))][:200]
for u in S[:5]:
    g=[k for k in u['class_info'] if k.startswith('Call')][0]; c=u['class_info'][g]
    f=c['f']; co=c['c']; df=np.diff(f).mean()
    I=-np.sum(np.log2(1-np.clip(co,0,0.9999)))*df
    print(g, c['info'], I, f[:3], f[-1], c['cutoff'], co.min(), co.max(), len(f))
E
```

```
Fri Nov 13 21:04:30 UTC 2026
Call3 5.596967971779364 5.596967971779364 [ 4.  8. 12.] 496.0 24.0 6.881780500072702e-05 0.29570950244527117 124
Call3 5.124294148166161 5.1242941481661575 [ 4.  8. 12.] 496.0 72.0 1.7891348159639907e-05 0.18715054865061875 124
Call3 9.802747233988264 9.802747233988269 [ 4.  8. 12.] 496.0 52.0 4.3567879427099144e-06 0.43806465932590755 124
Call1 4.584553421783336 4.584553421783336 [ 4.  8. 12.] 496.0 28.0 5.497962662666926e-06 0.18055140503767544 124
Call3 4.145059965497352 4.145059965497353 [ 4.  8. 12.] 496.0 40.0 2.4325433162214093e-05 0.19752938644373688 124
Shell cwd was reset to
```

**Agent**

Coherence check: the stored coherence curves integrate exactly to the stored I_AR, so S1's coherence fraction can be computed from the files. Now writing the notebook.

**Agent calls Bash**

```bash
cd entries/elie-2019 && python - <<'E'
s=open('elie.py').read()
s=s.replace('''def _s(x):
    return x.decode() if isinstance(x, bytes) else (x.item() if hasattr(x, "item") else x)''','''def _s(x):
    if hasattr(x, "item"):
        x = x.item()
    return x.decode() if isinstance(x, bytes) else x''')
s=s.replace('''def call_type(s: dict)''','''def is_single(u: dict) -> bool:
    """A unit whose file is labelled a single unit (sortType "single"; three
    files store it truncated as "singl")."""
    return str(u.get("sortType", "")).startswith("singl")


def iar(u: dict) -> float:
    """I_AR (bits/s) of the unit's call protocol, as stored in class_info."""
    v = [c["info"] for g, c in u["class_info"].items() if g.startswith("Call")]
    return max(v) if v else np.nan


def call_type(s: dict)''')
s=s.replace('''    single = str(u.get("sortType", "")).startswith("singl")''','''    single = is_single(u)''')
open('elie.py','w').write(s)
E
grep -n "def " elie.py
```

```
49:def _s(x):
55:def read_unit(h: h5py.File, name: str, bird: str) -> dict:
110:def sound_elements(x: np.ndarray, fs: float) -> dict:
144:def stream_bird(bird: str, block_size: int = 2**23) -> list[dict]:
170:def load_all(birds=BIRDS, workers: int = 4) -> list[dict]:
178:def is_single(u: dict) -> bool:
184:def iar(u: dict) -> float:
190:def call_type(s: dict) -> str | None:
202:def call_stims(u: dict) -> list[dict]:
221:def kde_rate(spike_times_ms: np.ndarray, n_trials: int, duration_ms: int) -> np.ndarray:
242:def bin_means(rate_1khz: np.ndarray, bin_ms: int = 10) -> np.ndarray:
249:def _pyx(mu: np.ndarray) -> np.ndarray:
255:def inst_info(mu: np.ndarray, groups: np.ndarray | None = None) -> np.ndarray:
272:def cum_info_mc(mu: np.ndarray, n_samples: int, rng: np.random.Generator,
```

**Agent calls Bash**

```bash
python - <<'E'
import re
s=open('elie.py').read()
a=s.index('def sound_elements'); b=s.index('def stream_bird')
s=s[:a]+s[b:]
s=s.replace('''    """Stream one bird's tar.gz and return the reduced units of all its h5 files.

    The wav files of the bird are matched to the stimuli by their md5 sum, which
    the h5 files store for each stimulus (stim_md5).
    """
    units, wav = [], {}''','''    """Stream one bird's tar.gz and return the reduced units of all its h5 files."""
    units = []''')
s=s.replace('''                if m.name.endswith(".wav"):
                    b = tar.extractfile(m).read()
                    fs, x = wavfile.read(io.BytesIO(b))
                    wav[hashlib.md5(b).hexdigest()] = {"wav": m.name, **sound_elements(x, fs)}
                elif m.name.endswith(".h5"):''','''                if m.name.endswith(".h5"):''')
s=s.replace('''    for u in units:
        for s in u["stims"]:
            s["sound"] = wav.get(s["stim_md5"])
    return units''','''    return units''')
s=s.replace('import hashlib\n','').replace('from scipy.io import wavfile\n','')
s=s.replace('''# Spikes are kept from KEEP[0] to KEEP[1] s around onset: the 2015 decoding of
# units-404 places its 600 ms window around the first sound element and takes
# silence sections from the 600 ms before onset (Elie & Theunissen 2015, Methods,
# Decoding the responses of auditory single units).
KEEP = (-0.7, 1.3)''','''# Spikes are kept from KEEP[0] to KEEP[1] s around onset; the 600 ms before onset
# serve the check of the clock (protocol, author step 2). A standard choice.
KEEP = (-0.6, 0.6)''')
open('elie.py','w').write(s)
E
sed -n 1,60p elie.py; sed -n 100,140p elie.py
```

```
"""Loading and measures for Elie & Theunissen (2019) on CRCNS aa-4.

Data. CRCNS aa-4 is unversioned; the files are read from the public S3 bucket
crcnsarchive under aa-4/live/data/, one tar.gz per bird. Each tar.gz is read as
a stream (tarfile mode "r|gz" over fsspec), each h5 member is opened in memory
with h5py, reduced to what the analysis needs, and dropped. Nothing is written
to disk.

Parameters and where they come from (claims file header, Methods R, B, P):
- Window 0 to 600 ms after stimulus onset, 60 bins of 10 ms (Methods B; paper,
  Methods, "Here, we analyzed the neural response in the first 600ms").
- Call stimuli: the h5 group "Call" with stim_type "call"; call types Ag (Wsst,
  Ws), Be, DC, Di, LT, Ne, Te, Th and song (So). Whines (Wh) and noise are
  dropped (claims header, selVoc.m).
"""
from __future__ import annotations

import io
import tarfile

[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
s=open('elie.py').read()
s=s.replace('''    """Reduce one unit's h5 file to attributes and its call responses in 0-600 ms.

    Spike times are kept in seconds relative to stimulus onset, as stored, for
    spikes in [0, T_MAX), plus the count of spikes in the whole response window
    stored (pre_time / post_time of each trial are kept).
    """''','''    """Reduce one unit's h5 file to its attributes, its stored coherence
    (class_info) and, for single units, the spike times of each trial of its call
    and song stimuli in KEEP, in seconds from stimulus onset, as stored."""''')
s=s.replace('''- Call stimuli: the h5 group "Call" with stim_type "call"; call types Ag (Wsst,
  Ws), Be, DC, Di, LT, Ne, Te, Th and song (So). Whines (Wh) and noise are
  dropped (claims header, selVoc.m).''','''- Call stimuli: in the unit's Call group, stim_type "call" with call types Ag
  (Wsst, Ws), Be, DC, Di, LT, Ne, Te, Th, and the songs of the vocalization bank
  (So). Whines (Wh), noise and the search songs are dropped (claims header,
  selVoc.m; paper, S4 Fig legend).''')
s+='''

# ---------------------------------------------------------------------------
# Spike-count measures (claims s2-spike-counts, fig2cd-fano-factor,
# fig2b-noise-correlations, s1-temporal-resolution); shown in the notebook as
# variants only, as the claims rest on the 404 units of units-404.
# ---------------------------------------------------------------------------
N_BINS = 60
BIN_S = 0.010


def counts(u: dict) -> list[np.ndarray]:
    """Per call stimulus, the trial x bin spike counts in the 60 bins of Methods B."""
    edges = np.arange(N_BINS + 1) * BIN_S
    return [np.stack([np.histogram(t, edges)[0] for t in s["trials"]]) for s in call_stims(u)]


def fano(cs: list[np.ndarray], zero_as_one: bool = True) -> float:
    """Time-averaged Fano factor: per bin and stimulus the variance (ddof 1, as
    MATLAB var) over the mean of the trial counts, averaged over stimuli, then
    over the 60 bins (claims, fig2cd-fano-factor). With zero_as_one the ratio is
    1 where variance equals mean, which covers bins with no spike (code,
    PoissonGaussianNeuralResponses.m, reading a); otherwise such stimuli are
    left out of the bin's average (reading b)."""
    m = np.stack([c.mean(0) for c in cs])
    v = np.stack([c.var(0, ddof=1) for c in cs])
    with np.errstate(divide="ignore", invalid="ignore"):
        ff = v / m
    if zero_as_one:
        ff[v == m] = 1.0
    return float(np.nanmean(np.nanmean(ff, 0)))


def noise_corr(cs: list[np.ndarray]) -> float:
    """Pearson correlation over trials of the counts in successive bins for the
    same stimulus, averaged across pairs of bins and stimuli (claims,
    fig2b-noise-correlations; paper, Methods, Testing the poisson assumptions).
    Pairs where a bin has no variance are left out (a standard choice)."""
    vals = []
    for c in cs:
        a, b = c[:, :-1], c[:, 1:]
        a = a - a.mean(0)
        b = b - b.mean(0)
        den = np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
        with np.errstate(divide="ignore", invalid="ignore"):
            r = (a * b).sum(0) / den
        vals.append(r[den > 0])
    v = np.concatenate(vals)
    return float(v.mean()) if v.size else np.nan


def stim_corr(cs: list[np.ndarray]) -> tuple[float, float]:
    """Stimulus correlation of consecutive bins: (i) over stimuli, the Pearson
    correlation of the mean counts at bins t and t+1, averaged over bin pairs;
    (ii) within each stimulus, the correlation over bins of the mean count at t
    and t+1, averaged over stimuli (claims, fig2b-noise-correlations, both
    readings)."""
    m = np.stack([c.mean(0) for c in cs])  # stim x bins
    a, b = m[:, :-1] - m[:, :-1].mean(0), m[:, 1:] - m[:, 1:].mean(0)
    den = np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
    with np.errstate(divide="ignore", invalid="ignore"):
        r1 = (a * b).sum(0) / den
    r2 = []
    for row in m:
        if row[:-1].std() > 0 and row[1:].std() > 0:
            r2.append(np.corrcoef(row[:-1], row[1:])[0, 1])
    return float(np.nanmean(r1[den > 0])), float(np.mean(r2)) if r2 else np.nan


def coherence_fraction(u: dict, f_max: float = 50.0) -> float:
    """Fraction of I_AR below f_max from the coherence stored in class_info:
    I_AR = -integral of log2(1 - coherence) over frequency (claims,
    s1-temporal-resolution; paper, S1 Fig legend). The stored curve integrates
    to the stored I_AR (checked in the notebook)."""
    g = [k for k in u["class_info"] if k.startswith("Call")][0]
    f, c = u["class_info"][g]["f"], u["class_info"][g]["c"]
    d = -np.log2(1 - np.clip(c, 0, 1 - 1e-12))
    return float(d[f <= f_max].sum() / d.sum())
'''
open('elie.py','w').write(s)
E
cd $TMPDIR && . venv/bin/activate && PYTHONPATH=entries/elie-2019 python - <<'E'
import pickle,numpy as np,elie,time
U=pickle.load(open('units2.pkl','rb'))
S=[u for u in U if elie.is_single(u)]
print(len(S))
t=time.time()
for u in S[:50]:
    cs=elie.counts(u)
print('counts per unit',(time.time()-t)/50)
u=S[0]; cs=elie.counts(u); print(elie.fano(cs),elie.fano(cs,False),elie.noise_corr(cs),elie.stim_corr(cs),elie.coherence_fraction(u))
E
```

```
1278
counts per unit 0.011466240882873536
0.9959575957992622 0.9935243422218735 0.014935872586663883 (0.027955060692771427, 0.0025307151455406128) 0.7844300210522719
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/elie-2019 && python - <<'E'
s=open('elie.py').read()
s=s.replace('''                if ids.size == 1 and ids[0] == -999:
                    t = np.empty(0)
                trials.append''','''                if ids.size == 1 and ids[0] == -999:
                    t = np.empty(0)
                n_unsorted += int(np.any(np.diff(t) < 0))
                trials.append''')
s=s.replace('''    stims = []
    for g in h.keys():''','''    stims = []
    n_unsorted = 0  # trials whose stored spike times are not in increasing order
    for g in h.keys():''')
s=s.replace('''    u["stims"] = stims
''','''    u["stims"] = stims
    u["n_unsorted_trials"] = n_unsorted
''')
open('elie.py','w').write(s)
E
grep -n "n_unsorted" elie.py
```

```
63:    n_unsorted = 0  # trials whose stored spike times are not in increasing order
85:                n_unsorted += int(np.any(np.diff(t) < 0))
91:    u["n_unsorted_trials"] = n_unsorted
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb && cat > $TMPDIR/nb/cells.py <<'E'
# %% load
import time, resource, collections
import numpy as np, pandas as pd
from scipy import stats
import elie

t0 = time.time()
U = elie.load_all()
print(f"loaded {len(U)} h5 files in {time.time() - t0:.0f} s; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB (this process)")

# %% sanity
pd.set_option("display.width", 200)
df = pd.DataFrame([{
    "bird": u["bird"], "file": u["file"], "site": u.get("site"), "electrode": u.get("electrode"),
    "sortType": u.get("sortType"), "ldepth": u.get("ldepth"), "rdepth": u.get("rdepth"),
    "spike_sorted_name": "_ss" in u["file"], "groups": "+".join(u["groups"]),
    "iar": elie.iar(u), "n_call_stims": len(elie.call_stims(u)) if elie.is_single(u) else np.nan,
    "n_stims_all": len(u["stims"]), "n_unsorted_trials": u["n_unsorted_trials"],
} for u in U])
df["single"] = [elie.is_single(u) for u in U]
print("h5 files by bird and sortType:")
print(pd.crosstab(df.bird, df.sortType.astype(str), margins=True))
print("\nfiles named as spike sorted (_ss) by sortType:")
print(pd.crosstab(df.spike_sorted_name, df.sortType.astype(str)))
print("\nsites per bird:", df.groupby("bird").site.nunique().to_dict())
print("depths (um), left:", np.nanmin(df.ldepth.astype(float)), "to", np.nanmax(df.ldepth.astype(float)),
      "; right:", np.nanmin(df.rdepth.astype(float)), "to", np.nanmax(df.rdepth.astype(float)))
S = [u for u in U if elie.is_single(u)]
sd = df[df.single]
print(f"\nsingle units: {len(S)}; with I_AR >= 2.3 bits/s: {(sd.iar >= 2.3).sum()}; I_AR range "
      f"{sd.iar.min():.2f} to {sd.iar.max():.2f} bits/s")
print(f"call stimuli per single unit: mean {sd.n_call_stims.mean():.1f}, sd {sd.n_call_stims.std():.1f}, "
      f"min {sd.n_call_stims.min():.0f}, max {sd.n_call_stims.max():.0f}")
print(f"all stimuli per single unit (any type): mean {sd.n_stims_all.mean():.1f}, sd {sd.n_stims_all.std():.1f}, "
      f"min {sd.n_stims_all.min()}, max {sd.n_stims_all.max()}")
ntr = collections.Counter(len(s["trials"]) for u in S for s in elie.call_stims(u))
print("trials per call stimulus:", dict(sorted(ntr.items())))
print("call stimuli by call type (unit x stimulus):",
      dict(collections.Counter(s["ct"] for u in S for s in elie.call_stims(u))))
allsp = np.concatenate([np.concatenate(s["trials"]) for u in S for s in elie.call_stims(u) if sum(map(len, s["trials"]))])
print(f"spike times kept: {allsp.size} spikes, from {allsp.min():.4f} to {allsp.max():.4f} s around onset (unit s)")
dur = np.array([s["stim_duration"] for u in S for s in elie.call_stims(u)], float)
print(f"stim_duration of call stimuli: {dur.min():.3f} to {dur.max():.3f} s, median {np.median(dur):.3f}")
print("trials with stored spike times out of order:", int(df.n_unsorted_trials.sum()))

# %% duplicates
import hashlib
keys = collections.defaultdict(list)
for u in S:
    st = sorted(elie.call_stims(u), key=lambda s: s["stim_md5"])
    h = hashlib.md5()
    for s in st:
        for t in s["trials"]:
            h.update(np.asarray(t, np.float32).tobytes()); h.update(b"|")
    keys[h.hexdigest()].append(u["bird"] + "/" + u["file"])
dups = [v for v in keys.values() if len(v) > 1]
print(f"single units with identical spike trains to all call stimuli: {len(dups)} groups")
for v in dups[:10]:
    print("  ", v)

# %% clock
# Contrast between conditions around the trial start: in 50 ms windows from -300 to
# 600 ms, a Kruskal-Wallis test of the trial spike counts across the nine call types,
# per unit. Before onset the counts cannot depend on the call type.
wins = np.arange(-0.3, 0.6, 0.05)
frac = []
rate = []
for w0 in wins:
    sig, r = 0, []
    for u in S:
        st = elie.call_stims(u)
        grp = collections.defaultdict(list)
        for s in st:
            for t in s["trials"]:
                n = int(((t >= w0) & (t < w0 + 0.05)).sum())
                grp[s["ct"]].append(n); r.append(n)
        vals = list(grp.values())
        try:
            p = stats.kruskal(*vals).pvalue
        except ValueError:
            p = 1.0
        sig += p < 0.01
    frac.append(sig / len(S)); rate.append(np.mean(r) / 0.05)
clock = pd.DataFrame({"window_start_ms": (wins * 1000).round().astype(int), "fraction_units_p<0.01": np.round(frac, 3),
                      "mean_rate_spikes_per_s": np.round(rate, 2)})
print(clock.to_string(index=False))
E
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python -c "
import elie,pickle,time,resource
t=time.time(); U=elie.load_all(); print(len(U), time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
pickle.dump(U,open('$TMPDIR/units3.pkl','wb'))
"; date -u
```

```
2298 388.92889404296875 938496
Fri Nov 13 21:12:45 UTC 2026
```

**Agent**

Full reload with the process-based loader now takes 6.5 minutes and under 1 GB in the parent process. Running the data-check cells on it.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && . ../venv/bin/activate && sed 's/^U = elie.load_all()/import pickle; U = pickle.load(open("..\/units3.pkl","rb"))/' cells.py > dev.py && PYTHONPATH=entries/elie-2019 timeout 1200 python -W ignore dev.py
```

```
loaded 2298 h5 files in 2 s; peak memory 1.33 GB (this process)
h5 files by bird and sortType:
sortType     multi  noise  singl  single  tdt   All
bird                                               
BlaBro09xxF      7     22      0     144  213   386
GreBlu9508M     13     39      0     343  165   560
LblBlu2028M      4      3      2      47   35    91
WhiBlu5396M      7      4      1     190  143   345
WhiWhi4522M     14     20      0     290  160   484
YelBlu6903F     18     21      0     264  129   432
All             63    109      3    1278  845  2298

files named as spike sorted (_ss) by sortType:
sortType           multi  noise  singl  single  tdt
spike_sorted_name                                  
False                  0      0      0       0  845
True                  63    109      3    1278    0

sites per bird: {'BlaBro09xxF': 4, 'GreBlu9508M': 5, 'LblBlu2028M': 1, 'WhiBlu5396M': 7, 'WhiWhi4522M': 5, 'YelBlu6903F': 4}
depths (um), left: 500.0 to 5400.0 ; right: 400.0 to 2400.0
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/cells2.py <<'E'
# %% units404
n_single = len(S)
n_aud = int((sd.iar >= 2.3).sum())
print(f"files labelled single units (sortType single or singl): {n_single}")
print(f"  of which I_AR >= 2.3 bits/s (the 2015 threshold for auditory spike-sorted units): {n_aud}")
print(f"spike-sorted files (_ss) of any sortType: {int(df.spike_sorted_name.sum())}")
print("expected: 914 single auditory units, of which 404 selected by the 2015 decoding")
print("per bird, single / single with I_AR >= 2.3:")
print(sd.assign(aud=sd.iar >= 2.3).groupby("bird").agg(single=("file", "size"), auditory=("aud", "sum")).to_string())
attrs = sorted({k for u in U for k in u if k not in ("stims", "class_info", "groups")})
print("unit-level fields read from every file:", attrs)
print("groups found in files:", sorted({g for u in U for g in u["groups"]}))

# %% cost
# Cost of the paper's rate estimate (Methods R) on the data: time the locally
# adaptive KDE on the call stimuli of a few auditory single units, for the full
# set of trials and one jackknife set, and scale to 404 units x 11 estimates per stimulus.
rng_cost = np.random.default_rng(404)
aud = [u for u in S if elie.iar(u) >= 2.3]
sample = [aud[i] for i in rng_cost.choice(len(aud), 3, replace=False)]
n_kde, t_kde = 0, 0.0
for u in sample:
    for s in elie.call_stims(u)[:10]:
        tr = [t[(t >= 0) & (t < 0.6)] * 1000 for t in s["trials"]]
        for drop in (None, 0):
            use = [t for i, t in enumerate(tr) if i != drop]
            t1 = time.time()
            elie.kde_rate(np.concatenate(use), len(use), 600)
            t_kde += time.time() - t1; n_kde += 1
per = t_kde / n_kde
mean_stims = sd[sd.iar >= 2.3].n_call_stims.mean()
est_h = per * 404 * mean_stims * 11 / 3600
print(f"{n_kde} KDE estimates on 3 units: {per:.2f} s each")
print(f"estimate for the rates alone (404 units x {mean_stims:.0f} stimuli x 11 estimates): {est_h:.0f} h on one core, "
      f"{est_h / 4:.0f} h on 4 cores")

# %% variants
# Not deciding any outcome: the spike-count measures of s2-spike-counts,
# fig2cd-fano-factor, fig2b-noise-correlations and the coherence part of
# s1-temporal-resolution, on all auditory single units (I_AR >= 2.3 bits/s),
# since the 404 units cannot be identified.
rows = []
for u in aud:
    cs = elie.counts(u)
    allc = np.concatenate([c.ravel() for c in cs])
    sc1, sc2 = elie.stim_corr(cs)
    rows.append({"bird": u["bird"], "max_count": int(allc.max()), "n8": int((allc == 8).sum()),
                 "n_bins": allc.size, "sum": int(allc.sum()),
                 "mean_trialavg": float(np.mean([c.mean(0).mean() for c in cs])),
                 "fano_a": elie.fano(cs, True), "fano_b": elie.fano(cs, False),
                 "noise_corr": elie.noise_corr(cs), "stim_corr_over_stims": sc1, "stim_corr_within_stim": sc2,
                 "coh_frac_50": elie.coherence_fraction(u)})
V = pd.DataFrame(rows)
print(f"units: {len(V)}")
print(f"s2: largest count in a 10 ms bin {V.max_count.max()}; bins with 8 spikes {V.n8.sum()}; "
      f"bins with more than 8: {(V.max_count > 8).sum()} units have one; mean count per bin over trials "
      f"{V['sum'].sum() / V.n_bins.sum():.3f}, over trial-averaged counts {V.mean_trialavg.mean():.3f} "
      f"(paper, 404 units: 8, 1, 0.108)")
print("  distribution of the largest count per unit:", dict(sorted(collections.Counter(V.max_count).items())))
for col in ["fano_a", "fano_b"]:
    x = V[col].dropna()
    print(f"Fano ({col}): mean {x.mean():.3f}, SEM {x.std() / np.sqrt(len(x)):.3f}, range {x.min():.2f} to {x.max():.2f}; "
          f"t-test vs 1 p = {stats.ttest_1samp(x, 1).pvalue:.2g}; Wilcoxon vs 1 p = {stats.wilcoxon(x - 1).pvalue:.2g} "
          f"(paper: 1.04, SEM 0.04)")
x = V.noise_corr.dropna()
print(f"noise correlation: median {x.median():.3f}, mean {x.mean():.3f}, skewness {stats.skew(x):.2f}, range {x.min():.2f} to {x.max():.2f}")
for col in ["stim_corr_over_stims", "stim_corr_within_stim"]:
    x = V[col].dropna()
    print(f"stimulus correlation ({col}): median {x.median():.3f}, mean {x.mean():.3f}, range {x.min():.2f} to {x.max():.2f} (paper: around 0.4)")
x = V.coh_frac_50 * 100
print(f"coherence information below 50 Hz: {x.mean():.1f}% +- {x.std():.1f}% (mean +- SD); units losing more than 5%: "
      f"{(x < 95).sum()} of {len(x)} (paper, 404 units: 96.7 +- 6.9%, 88 of 404)")
print("\nby bird (medians):")
print(V.groupby("bird")[["fano_a", "noise_corr", "stim_corr_over_stims", "coh_frac_50"]].median().round(3).to_string())
E
cd $TMPDIR/nb && cat dev.py cells2.py > dev2.py && . ../venv/bin/activate && PYTHONPATH=entries/elie-2019 timeout 1800 python -W ignore dev2.py 2>&1 | sed -n '/files labelled/,$p'
```

```
files labelled single units (sortType single or singl): 1281
  of which I_AR >= 2.3 bits/s (the 2015 threshold for auditory spike-sorted units): 1246
spike-sorted files (_ss) of any sortType: 1453
expected: 914 single auditory units, of which 404 selected by the 2015 decoding
per bird, single / single with I_AR >= 2.3:
             single  auditory
bird                         
BlaBro09xxF     144       139
GreBlu9508M     343       333
LblBlu2028M      49        49
WhiBlu5396M     191       188
WhiWhi4522M     290       278
YelBlu6903F     264       259
unit-level fields read from every file: ['bird', 'electrode', 'file', 'has_class_info', 'has_extra_info', 'ldepth', 'n_unsorted_trials', 'rdepth', 'site', 'sortType', 'sortid', 'source_directory', 'tank_name']
groups found in files: ['Call', 'Call1', 'Call1b', 'Call1c', 'Call2', 'Call3', 'Mask1', 'STRF1', 'Sel1', 'Sel2', 'Sel3', 'Sel4', 'Sel5', 'Sel6', 'Sel7', 'class_info', 'extra_info']
60 KDE estimates on 3 units: 1.09 s each
estimate for the rates alone (404 units x 95 stimuli x 11 estimates): 128 h on one core, 32 h on 4 cores
units: 1246
s2: largest count in a 10 ms bin 9; bins with 8 spikes 442; bins with more than 8: 4 units have one; mean count per bin over trials 0.132, over trial-averaged counts 0.127 (paper, 404 units: 8, 1, 0.108)
  distribution of the largest count per unit: {1: 20, 2: 195, 3: 340, 4: 259, 5: 229, 6: 120, 7: 63, 8: 16, 9: 4}
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/cells3.py <<'E'
# %% fig1
import io, fsspec, scipy.io as sio
REPO = "https://raw.githubusercontent.com/julieelie/PoissonTimeVaryingInfo/978020328321c7ed83be12c0152bed85ec77e218/"
with fsspec.open(REPO + "ModelCell_InfoCumInfo_Tutorial.mat", block_size=2**24).open() as f:
    M = sio.loadmat(io.BytesIO(f.read()))
n_stim, n_tr, dur = int(M["NStims"][0, 0]), int(M["NTrials"][0, 0]), int(M["NR_Duration"][0, 0])
model_bins = M["Input_Spike_count"]            # model mean count per 10 ms bin, stimulus x bin
print(f"tutorial model cell: {n_stim} stimuli, {n_tr} trials, {dur} ms at {int(M['Response_samprate'][0, 0])} Hz, "
      f"{model_bins.shape[1]} bins of {int(M['Step'][0, 0])} ms")
print("model mean count per 10 ms bin, range", model_bins.min(), "to", model_bins.max())
print("bins where each stimulus has its response (model count > 0.1):",
      [list(np.flatnonzero(r > 0.1) * 10) for r in model_bins])
arr = [M["Spike_array"][0, 0][f"stim{s + 1}"] for s in range(n_stim)]   # trial x 1 ms
spk = [[np.repeat(np.flatnonzero(a[t]), a[t][a[t] > 0].astype(int)) + 1.0 for t in range(n_tr)] for a in arr]
print("spikes per stimulus (all trials):", [int(a.sum()) for a in arr])

rate = np.array([elie.kde_rate(np.concatenate(sp), n_tr, dur) for sp in spk])           # spikes/ms
jk = np.array([[elie.kde_rate(np.concatenate([x for i, x in enumerate(sp) if i != k]), n_tr - 1, dur)
                for sp in spk] for k in range(n_tr)])                                     # set x stim x ms
saved = np.array([M["Spike_filtered"][0, 0][f"stim{s + 1}"].ravel() for s in range(n_stim)])
print(f"KDE here against the KDE saved by the MATLAB tutorial: mean |diff| {np.abs(rate - saved).mean():.5f}, "
      f"max {np.abs(rate - saved).max():.5f} spikes/ms")
model = np.repeat(model_bins / 10.0, 10, axis=1)                                          # spikes/ms at 1 kHz
mae = np.abs(rate - model).mean(1)
print("mean |KDE - model rate| per stimulus (spikes/ms):", np.round(mae, 4), "; all:", round(float(mae.mean()), 4),
      "; RMS:", round(float(np.sqrt(((rate - model) ** 2).mean())), 4))

mu = np.array([elie.bin_means(r) for r in rate])
mu_jk = np.array([[elie.bin_means(r) for r in s] for s in jk])
mu_model = np.maximum(model_bins, elie.MU_MIN)
N = n_tr

def jackknife(full, reps):
    """Bias-corrected value N*I - (N-1)*mean(I_k) and its jackknife standard error."""
    reps = np.asarray(reps)
    bc = N * full - (N - 1) * reps.mean(0)
    se = np.sqrt((N - 1) / N * ((reps - reps.mean(0)) ** 2).sum(0))
    return bc, se

ii, ii_se = jackknife(elie.inst_info(mu), [elie.inst_info(m) for m in mu_jk])
ii_model = elie.inst_info(mu_model)
rng_f1 = np.random.default_rng(1)
NS = 200_000
ci_full = elie.cum_info_mc(mu, NS, rng_f1)
ci, ci_se = jackknife(ci_full, [elie.cum_info_mc(m, NS, rng_f1) for m in mu_jk])
ci_model = elie.cum_info_mc(mu_model, NS, rng_f1)
tab = pd.DataFrame({"bin_end_ms": np.arange(1, mu.shape[1] + 1) * 10, "inst_bc": ii.round(3), "inst_se": ii_se.round(3),
                    "inst_model": ii_model.round(3), "cum_bc": ci.round(3), "cum_se": ci_se.round(3),
                    "cum_model": ci_model.round(3)})
print(tab.to_string(index=False))
print(f"peak bias-corrected instantaneous information {ii.max():.3f} bits at bin ending {10 * (ii.argmax() + 1)} ms "
      f"(model rate: {ii_model.max():.3f}); uncorrected peak {elie.inst_info(mu).max():.3f}")
print(f"cumulative information: largest {ci.max():.3f} bits, last bin {ci[-1]:.3f} bits (model rate: {ci_model[-1]:.3f}); "
      f"largest jackknife SE {ci_se.max():.3f} bits; maximum log2(4) = 2 bits")
print("same with the MATLAB tutorial's saved results: peak instantaneous",
      round(float(M["Info_bcorr"].max()), 3), "; last cumulative", round(float(M["Icum_EstMonteCarloOpt_bcorr"][0, -1]), 3))
E
cd $TMPDIR/nb && printf 'import time, collections\nimport numpy as np, pandas as pd\nfrom scipy import stats\nimport elie\n' > dev3.py && cat cells3.py >> dev3.py && . ../venv/bin/activate && PYTHONPATH=entries/elie-2019 timeout 1800 python -W ignore dev3.py 2>&1 | tail -60
```

```
tutorial model cell: 4 stimuli, 10 trials, 400 ms at 1000 Hz, 40 bins of 10 ms
model mean count per 10 ms bin, range 0.1 to 2.5
bins where each stimulus has its response (model count > 0.1): [[np.int64(30), np.int64(40), np.int64(50), np.int64(60), np.int64(70)], [np.int64(120), np.int64(130), np.int64(140), np.int64(150), np.int64(160)], [np.int64(210), np.int64(220), np.int64(230), np.int64(240), np.int64(250)], [np.int64(310), np.int64(320), np.int64(330), np.int64(340), np.int64(350)]]
spikes per stimulus (all trials): [121, 83, 85, 114]
KDE here against the KDE saved by the MATLAB tutorial: mean |diff| 0.00039, max 0.00330 spikes/ms
mean |KDE - model rate| per stimulus (spikes/ms): [0.0103 0.01   0.0075 0.0082] ; all: 0.009 ; RMS: 0.0161
 bin_end_ms  inst_bc  inst_se  inst_model  cum_bc  cum_se  cum_model
         10    0.004    0.006       0.000   0.004   0.006      0.000
         20   -0.006    0.004       0.000  -0.002   0.006      0.000
         30    0.112    0.021       0.000   0.110   0.019      0.000
         40    0.413    0.033       0.356   0.464   0.035      0.356
         50    0.482    0.041       0.540   0.641   0.026      0.650
         60    0.466    0.039       0.540   0.864   0.024      0.749
         70    0.408    0.053       0.356   0.989   0.050      0.766
         80    0.162    0.074       0.084   1.039   0.063      0.768
         90    0.081    0.036       0.000   1.152   0.066      0.768
        100    0.014    0.013       0.000   1.173   0.062      0.768
        110   -0.007    0.006       0.000   1.180   0.061      0.768
        120   -0.019    0.010       0.000   1.198   0.062      0.768
        130    0.254    0.060       0.356   1.310   0.081      1.072
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/elie-2019 && python - <<'E'
s=open('elie.py').read()
s=s.replace('''def cum_info_mc(mu: np.ndarray, n_samples: int, rng: np.random.Generator,
                groups: np.ndarray | None = None) -> np.ndarray:''','''def cum_info_mc(mu: np.ndarray, n_samples: int, seed: int,
                groups: np.ndarray | None = None) -> np.ndarray:''')
s=s.replace('''    computed by summing over stimuli)."""''','''    computed by summing over stimuli).

    The uniform draws come from a generator seeded with `seed`, so that the
    jackknife replicates, called with the same seed, use common random numbers
    (an assumption: the paper does not say how the replicates are sampled, and
    independent draws multiply the Monte Carlo noise by about Ntrials in the
    bias-corrected value)."""
    rng = np.random.default_rng(seed)''')
open('elie.py','w').write(s)
E
cd $TMPDIR/nb && sed -i 's/rng_f1 = np.random.default_rng(1)/SEED_F1 = 1/; s/, rng_f1)/, SEED_F1)/g' cells3.py && grep -n "SEED_F1\|rng_f1" cells3.py && printf 'import time, collections\nimport numpy as np, pandas as pd\nfrom scipy import stats\nimport elie\n' > dev3.py && cat cells3.py >> dev3.py && sed -i 's/print(tab.to_string(index=False))/print(tab.to_string(index=False)); print(np.round(ci_full,3))/' dev3.py && . ../venv/bin/activate && PYTHONPATH=entries/elie-2019 timeout 1800 python -W ignore dev3.py 2>&1 | tail -48
```

```
42:SEED_F1 = 1
44:ci_full = elie.cum_info_mc(mu, NS, SEED_F1)
45:ci, ci_se = jackknife(ci_full, [elie.cum_info_mc(m, NS, SEED_F1) for m in mu_jk])
46:ci_model = elie.cum_info_mc(mu_model, NS, SEED_F1)
 bin_end_ms  inst_bc  inst_se  inst_model  cum_bc  cum_se  cum_model
         10    0.004    0.006       0.000   0.004   0.006      0.000
         20   -0.006    0.004       0.000  -0.002   0.006      0.000
         30    0.112    0.021       0.000   0.110   0.019      0.000
         40    0.413    0.033       0.356   0.454   0.036      0.357
         50    0.482    0.041       0.540   0.650   0.033      0.647
         60    0.466    0.039       0.540   0.759   0.032      0.752
         70    0.408    0.053       0.356   0.852   0.042      0.774
         80    0.162    0.074       0.084   0.862   0.043      0.778
         90    0.081    0.036       0.000   0.861   0.044      0.778
        100    0.014    0.013       0.000   0.880   0.044      0.778
        110   -0.007    0.006       0.000   0.877   0.045      0.778
        120   -0.019    0.010       0.000   0.862   0.051      0.778
        130    0.254    0.060       0.356   1.041   0.070      1.086
        140    0.519    0.073       0.540   1.313   0.056      1.341
        150    0.361    0.081       0.356   1.444   0.040      1.397
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> $TMPDIR/nb/cells3.py <<'E'
# Variant: jackknife replicates with independent Monte Carlo draws (seeds 2 to 11).
ci_ind, _ = jackknife(ci_full, [elie.cum_info_mc(m, NS, 2 + k) for k, m in enumerate(mu_jk)])
print(f"variant, independent draws per replicate: largest {ci_ind.max():.3f} bits, last bin {ci_ind[-1]:.3f} bits")
E
```

```
Fri Nov 13 21:21:29 UTC 2026
```

**Agent**

Analysis is done. The model-neuron claim passes all three of its tests on the one model neuron the tutorial file holds. Now assembling the notebook.

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/build.py <<'PYEOF'
import nbformat as nbf, re
src = open('cells.py').read() + "\n" + open('cells2.py').read() + "\n" + open('cells3.py').read()
parts = re.split(r'^# %% (\w+)\n', src, flags=re.M)
code = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
nb = nbf.v4.new_notebook()
C = []
def md(s): C.append(nbf.v4.new_markdown_cell(s.strip()))
def cc(name, tags=()):
    c = nbf.v4.new_code_cell(code[name]); c.metadata["tags"] = list(tags); C.append(c)

md(r"""
# Elie & Theunissen (2019) on CRCNS aa-4

Paper: Elie JE, Theunissen FE (2019). Invariant neural responses for sensory categories revealed by the
time-varying information for communication calls. PLoS Comput Biol 15(9):e1006698,
doi:10.1371/journal.pcbi.1006698.

Dataset: CRCNS aa-4, "Simultaneous extracellular recordings of avian auditory neurons in zebra finches presented
with all the repertoire of vocalizations used by this species for vocal communication", doi:10.6080/K00C4T06,
data description version 0.6 (July 15, 2019). CRCNS data sets are not versioned, so the version is recorded as
`unversioned`; the only published state is the one in `aa-4/live/`, and it is the one read here. The files are
streamed from the public S3 bucket `crcnsarchive`; their MD5 sums in `aa-4/live/checksums.md5`, read on
2026-11-13, are:

| file | md5 |
|---|---|
| data/BlaBro09xxF.tar.gz | ee387cc051e5fa5ee66a5f4db5d8bae6 |
| data/GreBlu9508M.tar.gz | 16f1bb223946288f8b426d6382f06510 |
| data/LblBlu2028M.tar.gz | 80c181eb8bd70ddbbd9b3aa46587dfb5 |
| data/WhiBlu5396M.tar.gz | 2ba7776cd4130d0090b13e5f5c0359fd |
| data/WhiWhi4522M.tar.gz | c47d6660019a2a0d1e3375ce7da68bf1 |
| data/YelBlu6903F.tar.gz | 6027933cdf765dd0b67f811b1a133095 |

Outside input: the tutorial model cell `ModelCell_InfoCumInfo_Tutorial.mat` of the paper's code repository,
github.com/julieelie/PoissonTimeVaryingInfo at commit 978020328321c7ed83be12c0152bed85ec77e218 (claim
fig1-model-neurons, `data: elsewhere`).

Claims file: `claims/elie-2019.yaml`, written from the version of record (PMC6762074) with its S1 to S7 Fig
legends.

| claim | status here |
|---|---|
| units-404 | blocked: the 914 single auditory units and the 404 selected ones cannot be identified in the files |
| units-337, s1-temporal-resolution, fig2a-poisson-test, fig2cd-fano-factor, fig2b-noise-correlations, s2-spike-counts | blocked: rest on the 404 units (variants on all auditory single units shown, not deciding) |
| fig6a-onset-sustained-information, fig6c-new-information, fig6b-fixed-rate-fraction, fig7a-time-constants, fig7b-k300, k300-rate-regression, fig9a-mean-cii, fig9a-top-quartile, s7-invariant-information, fig9b-cii-tau-ratio, fig9c-cii-k300, cii-unimodal | blocked: rest on the 337 units of units-337 |
| fig3-5-example-neurons | blocked: the paper does not name the three units |
| table1-anatomy-counts, fig10-cii-distance, fig10-cii-area-anova, fig10-tau-k300-distance, fig10-no-anatomy-categorical | blocked: no anatomical location in the data set |
| fig1-model-neurons | tested, on the one model neuron the paper's code repository holds |
""")
md("## Loading\n\nEach bird's tar.gz is streamed and its h5 files are read in memory (`elie.load_all`); only spike times from -600 to 600 ms around stimulus onset, the stimulus attributes and the stored coherence are kept.")
cc("load")
md("## Data check\n\nCounts of files, units, stimuli and trials, and the ranges of the variables used, against the data description and the paper.")
cc("sanity", ["sanity"])
md(r"""
Checks against the description and the paper, from the output above:

- The data description says 688 multi-units were recorded and 914 single auditory units were saved, one h5 file
  each. The files hold 845 unsorted (`tdt`) multi-unit files and 1453 spike-sorted (`_ss`) files, of which 1281
  are labelled single units (`sortType` "single", or "singl" in three files), 63 multi and 109 noise. The 914
  are not marked. This is recorded as a finding.
- Six birds, as described; WhiBlu5396M is the bird missing from the paper's Table 1. The description's file
  organisation section names it WhiBlu5896M once.
- Call stimuli per single unit: mean 95.4 (63 to 120), against the paper's 114 on average (sd 22, 34 to 123).
  All stimuli of any kind: mean 121.9 (73 to 137), against the description's 144 (64 to 153). The counts do not
  match either source.
- Trials per stimulus: 9 to 12, with 1874 unit-stimulus pairs at 12, against "min=9, max=11".
- Spike times are in seconds from stimulus onset (range -0.6 to 0.6 s as kept); no trial holds spike times out of
  order. `stim_duration` (0.08 to 2.9 s, median 2.5 s) is longer than most calls; it is not used.
""")
md("No recording is deposited twice: the spike trains of every single unit to its call stimuli are compared.")
cc("duplicates")
md(r"""
Clock. In 50 ms windows around onset, a Kruskal-Wallis test of the spike counts across the nine call types, per
single unit. Before onset the counts cannot depend on the call that follows; after onset they can.
""")
cc("clock")
md(r"""
Before onset 0.9% to 1.9% of units differ across call types at p < 0.01, near the 1% false-positive rate, and
the mean rate is flat at about 6.1 spikes/s; from the 0 to 50 ms window on, 44% to 66% do and the rate rises to
22 spikes/s. The spike times share the clock of the stimulus onsets, for the population; a check per unit was not
made.
""")
md(r"""
## units-404

> The analysis uses 404 of the 914 isolated single units, those from which call type could be decoded above
> chance in the authors' earlier study.

Criterion: reading (a), a list of the 404 units from the data set's documentation or the 2015 paper; reading (b),
the 2015 decoding selection redone as that paper describes it. Blocked as methods_underspecified when neither
can be carried out.
""")
cc("units404", ["claim:units-404"])
md(r"""
The files hold no list or flag of the 404 units, and the data description and the 2015 paper (Elie &
Theunissen 2015, Eur J Neurosci 41:546-567, read at PMC4347984) give none, so reading (a) cannot be carried out.
Reading (b) starts from the 914 single auditory units, which the 2015 paper defines by an SNR of the spike
snippets above 5 among the spike-sorted units with I_AR of at least 2.3 bits/s. The SNR is not stored in the h5
files, and the snippet files (`.f32`) are undocumented and exist for only some sites. The I_AR threshold alone
leaves 1246 units, not 914. The 2015 decoding would also have to be run on a set that is not the paper's.

**Result: blocked.** The data set holds 1281 files labelled single units, 1246 of them with I_AR of at least 2.3
bits/s; neither the 914 nor the 404 can be identified.
""")
md(r"""
## Cost of the paper's pipeline

Every claim from units-337 on needs the locally adaptive KDE rate of each unit and stimulus, and its 10
jackknife estimates (Methods R), before the Monte Carlo cumulative information. The time of the KDE alone, on a
sample of call stimuli of three auditory single units:
""")
cc("cost")
md(r"""
The rate estimates alone would take about 128 hours on one core, or 32 hours on the runner's 4 cores, before any
Monte Carlo estimate of cumulative information; this is beyond the limit of a notebook even if the 404 units
could be identified.
""")
md(r"""
## Variants on all auditory single units (not deciding any outcome)

The spike-count measures of s2-spike-counts, fig2cd-fano-factor and fig2b-noise-correlations, and the coherence
part of s1-temporal-resolution, on all 1246 single units with I_AR of at least 2.3 bits/s. The claims rest on the
404 units; these numbers describe the data set's units and decide nothing.
""")
cc("variants")
md(r"""
On the 1246 auditory single units: the largest count in a 10 ms bin is 9 (4 units) with 442 bins at 8, and the
mean count per bin is 0.132, against 8, 1 and 0.108 for the paper's 404. The time-averaged Fano factor is 1.027
(SEM 0.002) under the code's reading and 1.054 (SEM 0.003) leaving out empty bins, both significantly above 1 at
this n. The noise correlation has median 0.152 and positive skew (1.09); the stimulus correlation has median 0.291
over stimuli and 0.239 within stimuli. The stored coherence puts 65.8% +- 19.0% of I_AR below 50 Hz, far from the
paper's 96.7% +- 6.9%; the stored curve, from 4 to 496 Hz, may not be the one the paper's S1 Fig used.
""")
md(r"""
## fig1-model-neurons

> For simulated Poisson neurons (rate, onset and temporal codes, 4 stimuli, 10 trials), the KDE recovers the
> model rates with an average error below 0.02 spikes/ms, the cumulative information approaches the 2-bit
> maximum, and the temporal neuron's peak instantaneous information is 0.5 bits.

Criterion: with the tutorial's model cells, mean absolute difference between KDE and model rates below 0.02
spikes/ms, the cumulative information of each model neuron reaching at least 1.8 bits before it ends, and the
temporal neuron's peak instantaneous information within 0.5 +- 0.05 bits.

The repository holds one model cell, a temporal neuron (each stimulus drives a response at a different time).
The rate and onset neurons are not there. The KDE is the Python port of ssvkernel (`adaptivekde`); the bias
correction is the jackknife, N I - (N-1) mean(I_k), with the jackknife set k used for every stimulus (Methods,
Bias correction; the equation is not in the text read, and this is the standard form). The cumulative
information uses 200,000 Monte Carlo samples with the paper's proposal, the product of the per-bin marginals
(Methods, The cumulative information).
""")
cc("fig1", ["claim:fig1-model-neurons"])
md(r"""
**Result: partially reproduced.** On the tutorial's temporal neuron the KDE differs from the model rate by 0.009
spikes/ms on average (below 0.02), the bias-corrected cumulative information reaches 1.928 bits (at least 1.8;
1.828 at 400 ms, 1.956 from the model rates), and the peak bias-corrected instantaneous information is 0.519
bits (within 0.5 +- 0.05; 0.540 from the model rates). The KDE matches the MATLAB tutorial's saved KDE to 0.0004
spikes/ms on average. With independent Monte Carlo draws per jackknife replicate the cumulative information still
peaks above 1.8 bits. The rate and onset neurons of Fig 1 are not in the repository, so the claim holds for one of
its three model neurons.
""")
md(r"""
## Summary

| claim | outcome |
|---|---|
| units-404 | blocked (methods_underspecified): 914 and 404 units not identifiable; 1281 files labelled single |
| units-337, fig2a-poisson-test, fig2cd-fano-factor, fig2b-noise-correlations, s1-temporal-resolution, s2-spike-counts | blocked (methods_underspecified, from units-404) |
| fig6a-onset-sustained-information, fig6c-new-information, fig6b-fixed-rate-fraction, fig7a-time-constants, fig7b-k300, k300-rate-regression, fig9a-mean-cii, fig9a-top-quartile, s7-invariant-information, fig9b-cii-tau-ratio, fig9c-cii-k300, cii-unimodal | blocked (methods_underspecified, from units-337) |
| fig3-5-example-neurons | blocked (methods_underspecified): the three units are not named |
| table1-anatomy-counts, fig10-cii-distance, fig10-cii-area-anova, fig10-tau-k300-distance, fig10-no-anatomy-categorical | blocked (data_missing): no anatomical location in the data set |
| fig1-model-neurons | partially reproduced, on the one model neuron in the paper's repository |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

Differences from the paper's method: the KDE is a Python port of ssvkernel; the jackknife replicates of the Monte
Carlo estimate share their random draws (an assumption, with the independent variant shown); the bootstrap of the
jackknife (20 replicates) and the adaptive sample size of the Monte Carlo are not run, as the claim tested does not
use the error.

What was found about the data set: the files do not mark the 914 single auditory units or the 404 analysed units
(1281 files are labelled single units, 1246 pass the 2.3 bits/s auditory threshold); the anatomical locations and
coordinates of the recording sites are not in the data set (depths are in the file names); the numbers of stimuli
per unit match neither the paper nor the description; up to 12 trials per stimulus, against a stated maximum of 11;
three files store `sortType` as "singl"; the description names one bird WhiBlu5896M where the files say
WhiBlu5396M.
""")
nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, 'entries/elie-2019/reproduce_elie_2019.ipynb')
print(len(C))
PYEOF
cd $TMPDIR/nb && . ../venv/bin/activate && python build.py
```

```
24
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat entries/fouke-2025/README.md | head -30; ls schemas; python tools/entry.py --help 2>&1 | head -20
```

```
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/elie-2019 && cat > entry.yaml <<'E'
schema_version: 1
name: elie-2019
type: reproduction
title: Time-varying information of avian auditory neurons for communication calls (Elie and Theunissen 2019)
description: Tests the findings of Elie and Theunissen (2019) on CRCNS data set aa-4, which holds the spike
  times of zebra finch auditory units to the vocal repertoire. The files do not mark the 914 single units or
  the 404 units the paper analyses, and hold no anatomical locations, so the population claims are blocked;
  the simulated model neuron of Figure 1 is tested on the paper's code repository.
license: Apache-2.0
notebooks:
- path: reproduce_elie_2019.ipynb
  title: Reproducing Elie and Theunissen (2019) from CRCNS aa-4
  runtime_minutes: 12
helpers:
- elie.py
related:
- id: crcns:aa-4/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pcbi.1006698
  relation: reproduces
E
printf 'adaptivekde\naiohttp\nfsspec\nh5py\nnumpy\npandas\nrequests\nscipy\n' > requirements.in
cat > README.md <<'E'
# Elie & Theunissen (2019) from CRCNS aa-4

Tests the findings of [Elie and Theunissen (2019)](https://doi.org/10.1371/journal.pcbi.1006698) on
[CRCNS aa-4](https://doi.org/10.6080/K00C4T06), the spike times of auditory units of six zebra finches
to the calls of their vocal repertoire.

| Claim | Outcome |
|---|---|
| 404 of 914 single units selected by the 2015 decoding | Blocked: methods underspecified |
| Claims on the 404 and 337 units (Poisson checks, information, time constants, CII; 19 claims) | Blocked: methods underspecified |
| Three example neurons (Figures 3 to 5) | Blocked: methods underspecified |
| Anatomy (Table 1, Figure 10; 5 claims) | Blocked: data missing |
| Model neurons of Figure 1 | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold 1281 units labelled single units, of which 1246 pass the 2015 auditory threshold, and
mark neither the 914 single auditory units nor the 404 the paper analyses. The anatomical locations
of the recording sites are not in the data set. The attempt record, with the reasons and the
differences from the paper's method, is [`attempts/elie-2019-01.yaml`](../../attempts/elie-2019-01.yaml).
E
cd  && date -u && python tools/entry.py lock entries/elie-2019 2>&1 | tail -5
```

```
Fri Nov 13 21:22:48 UTC 2026
wrote elie-2019/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/elie-2019 2>&1 | tail -30
```

```
Installed kernelspec registry-elie-2019 in executed/elie-2019/.venv/share/jupyter/kernels/registry-elie-2019
0 error(s)
pass  reproduce_elie_2019.ipynb  (772 s)

real	13m7.745s
user	24m8.337s
sys	0m32.042s
```

**Agent calls Bash**

```bash
date -u; ls executed/elie-2019/; python - <<'E'
import json
nb=json.load(open('executed/elie-2019/reproduce_elie_2019.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or ''.join(o.get('data',{}).get('text/plain',''))
            print(''.join(t)[:3500]); print('=====')
E
```

```
Fri Nov 13 21:36:02 UTC 2026
reproduce_elie_2019.ipynb
result.json
loaded 2298 h5 files in 435 s; peak memory 1.01 GB (this process)

=====
h5 files by bird and sortType:

=====
sortType     multi  noise  singl  single  tdt   All
bird                                               
BlaBro09xxF      7     22      0     144  213   386
GreBlu9508M     13     39      0     343  165   560
LblBlu2028M      4      3      2      47   35    91
WhiBlu5396M      7      4      1     190  143   345
WhiWhi4522M     14     20      0     290  160   484
YelBlu6903F     18     21      0     264  129   432
All             63    109      3    1278  845  2298

files named as spike sorted (_ss) by sortType:
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^outcomes:/,$p' attempts/fouke-2025-01.yaml | grep -n -B2 -A12 "outcome: blocked" | head -50; sed -n '/^findings:/,/^[a-z_]*:$/p' attempts/fouke-2025-01.yaml | head -40; python -c "
import json; s=json.load(open('schemas/attempt.schema.json')); print(list(s['properties'].keys())); print(json.dumps(s['properties']['datasets'],indent=0)[:1500])"
```

```
163-    in the dandiset; the measure was chosen here before the analysis.
164-- claim: fig1cef-representative-values
165:  outcome: blocked
166-  blocked_by: metadata_insufficient
167-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
168-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
169-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
170-- claim: fig2d-shared-architecture
171:  outcome: blocked
172-  blocked_by: data_missing
173-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
174-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
175-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
176-- claim: fig2g-dsi-similar
177:  outcome: blocked
178-  blocked_by: data_missing
179-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
180-- claim: fig2h-fewer-motion-responsive
181:  outcome: blocked
182-  blocked_by: data_missing
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']; print(json.dumps({k:v.get('description','')[:150] for k,v in o['properties'].items()},indent=0)); print(o.get('required')); print(json.dumps(o.get('allOf',o.get('if','')))[:1500])
f=s['properties']['findings']['items']; print(list(f['properties'].keys()), f.get('required'))
i=s['properties']['inputs']['items']; print(list(i['properties'].keys()), i.get('required'))
p=s['properties']['provenance']; print(json.dumps(p)[:1500])
"
```

```
{
"claim": "Claim id from the target's claims file.",
"outcome": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`.",
"blocked_by": "Required when outcome is blocked.",
"notes": "What differs, or what was missing, stated factually.",
"notebook": "Path of the notebook within the entry.",
"output": "Which output shows the result, e.g. a cell tag.",
"measured": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.",
"deviations": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.",
"assumed": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says w",
"proposed": "A change of outcome found after the last verification round, held until a further round agrees with it."
}
['claim', 'outcome']
[{"if": {"properties": {"outcome": {"const": "blocked"}}}, "then": {"required": ["blocked_by", "notes"]}}, {"if": {"properties": {"assumed": {"const": true}}, "required": ["assumed"]}, "then": {"required": ["deviations"], "properties": {"deviations": {"minItems": 1}, "outcome": {"not": {"const": "blocked"}}}}}]
['kind', 'statement', 'found', 'about', 'datasets'] ['kind', 'statement']
['what', 'source'] ['what', 'source']
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required":
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/\[list(np.flatnonzero(r > 0.1) \* 10) for r in model_bins\]/[[int(b) for b in np.flatnonzero(r > 0.1) * 10] for r in model_bins]/' cells3.py && grep -n "flatnonzero(r > 0.1)" cells3.py && python - <<'E'
s=open('build.py').read()
old='''The rate estimates alone would take about 128 hours on one core, or 32 hours on the runner's 4 cores, before any
Monte Carlo estimate of cumulative information; this is beyond the limit of a notebook even if the 404 units
could be identified.'''
new='''The rate estimates alone would take more than 100 hours on one core, and more than 25 hours on the runner's 4
cores, before any Monte Carlo estimate of cumulative information; this is beyond the limit of a notebook even if
the 404 units could be identified. The time per estimate varies between runs; the printed estimate is the one
for this run.'''
assert old in s; s=s.replace(old,new); open('build.py','w').write(s)
E
. ../venv/bin/activate && python build.py
```

```
12:      [[int(b) for b in np.flatnonzero(r > 0.1) * 10] for r in model_bins])
24
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/print("bins where each stimulus has its response (model count > 0.1):",/print("start (ms) of the bins where each stimulus drives a response (model count > 0.1):",/' cells3.py && grep -c "start (ms)" cells3.py && . ../venv/bin/activate && python build.py
```

```
1
24
Shell cwd was reset to
```

**Agent**

Now writing the attempt record.

**Agent calls Bash**

```bash
python - <<'PYEOF'
import yaml
claims = yaml.safe_load(open('claims/elie-2019.yaml'))['claims']
ids = [c['id'] for c in claims]
NB = 'reproduce_elie_2019.ipynb'
dep404 = "Rests on the 404 units of units-404, which cannot be identified in the files (see units-404); blocked for the same reason."
dep337 = ("Rests on the 337 units of units-337, which rests on the 404 units of units-404; neither can be identified, so the "
          "claim is blocked for the same reason. Even with the units, the locally adaptive KDE rates and their jackknife "
          "estimates alone were estimated in the notebook at more than 100 hours on one core (cell 'cost'), before the Monte Carlo "
          "cumulative information, so the claim would also be too_large here.")
out = []
for c in claims:
    i = c['id']
    o = {'claim': i}
    if i == 'units-404':
        o.update(outcome='blocked', blocked_by='methods_underspecified', notebook=NB, output='claim:units-404',
                 notes=("Neither reading of the criterion can be carried out. Reading (a): the files hold no list or flag of the 404 "
                        "units, and the data description and the 2015 paper (Elie and Theunissen 2015, read at PMC4347984) give none. "
                        "Reading (b): the 2015 decoding starts from the 914 single auditory units, defined in the 2015 Methods by I_AR of "
                        "at least 2.3 bits/s among spike-sorted units and a spike-snippet SNR above 5. The files hold 1281 units labelled "
                        "single (sortType single, or singl in three files), 1246 of them with stored I_AR of at least 2.3 bits/s; the SNR "
                        "is not stored, and the snippet files (.f32) are undocumented and present for only some sites. So the data set does "
                        "not hold 914 identifiable single units (expected 914, tolerance 0), and a selection of 404 could only be redone on "
                        "a different base set. The main reason is the missing unit labels (metadata_insufficient); methods_underspecified "
                        "is the block the criterion names."),
                 measured=[1281])
    elif i == 'fig1-model-neurons':
        o.update(outcome='partially_reproduced', notebook=NB, output='claim:fig1-model-neurons',
                 measured=[0.009, 0.519],
                 notes=("The paper's code repository holds one model cell (ModelCell_InfoCumInfo_Tutorial.mat), a temporal neuron: 4 "
                        "stimuli, 10 trials, 400 ms, each stimulus driving a response at a different time. The rate and onset neurons of Fig 1 "
                        "are not there, so the criterion's 'each model neuron' can be checked for one of three. On it all three conditions "
                        "hold. The mean absolute difference between the KDE and the model rate is 0.009 spikes/ms (per stimulus 0.0075 to "
                        "0.0103; RMS 0.016), below 0.02. The bias-corrected cumulative information reaches 1.928 bits (1.828 at 400 ms; 1.956 "
                        "from the model rates), at least 1.8. The peak bias-corrected instantaneous information is 0.519 bits at 140 ms "
                        "(uncorrected 0.500; 0.540 from the model rates), within 0.5 +- 0.05. The Python KDE matches the KDE saved by the "
                        "MATLAB tutorial to 0.0004 spikes/ms on average (largest 0.0033)."),
                 deviations=[
                     "Data, the paper's tutorial model cell only (data elsewhere, GitHub julieelie/PoissonTimeVaryingInfo at commit 978020328321c7ed83be12c0152bed85ec77e218); the rate and onset model neurons of Fig 1 are not published.",
                     "KDE, the Python port of ssvkernel in the adaptivekde package (1.2.0), in place of the MATLAB ssvkernel the paper cites (reference 42); its output matches the MATLAB KDE saved with the tutorial (mean difference 0.0004 spikes/ms).",
                     "Model rate, the tutorial's Input_Spike_count read as the mean count per 10 ms bin and divided by 10 for spikes/ms; its rows sum to the observed spikes per trial (11.8 against 12.1 for stimulus 1).",
                     "Bias correction, N I - (N-1) mean(I_k) over the 10 jackknife sets, set k used for every stimulus (Methods, Bias correction, which names the jackknife; the equation is not in the text read, and this is its standard form).",
                     "Cumulative information, 200,000 Monte Carlo samples from the paper's proposal, the product of the per-bin marginals (Methods, The cumulative information). The jackknife replicates use common random numbers; with independent draws the cumulative information peaks at 2.206 bits and ends at 0.803 bits, so the 1.8-bit condition holds under both. The adaptive sample size (chunks of 100,000 up to 5,000,000) and the bootstrap of the jackknife (NB = 20) are not run, as the criterion does not use the error.",
                 ])
    elif i == 'fig3-5-example-neurons':
        o.update(outcome='blocked', blocked_by='methods_underspecified',
                 notes=("The paper does not name the three example units, and no PDF of the figures was supplied, so the rasters of S4 to S6 "
                        "Fig could not be compared with the data; the criterion blocks the claim when the units cannot be identified. The "
                        "units would also have to be among the 404 of units-404, which cannot be identified."))
    elif i in ('table1-anatomy-counts', 'fig10-cii-distance', 'fig10-cii-area-anova', 'fig10-tau-k300-distance', 'fig10-no-anatomy-categorical'):
        o.update(outcome='blocked', blocked_by='data_missing',
                 notes=("The data set holds no anatomical area or x, y, z coordinate for any unit or site: the h5 files store the electrode, "
                        "the site and the depth of each array (also in the file names), and the data description mentions no histology. "
                        "The claim also rests on units-337 and units-404, which are blocked as methods_underspecified."
                        + ("" if i == 'table1-anatomy-counts' else " It also needs the CII or the exponential fits, which are too large to run here (see units-337).")))
    elif i in ('units-337', 'fig6a-onset-sustained-information', 'fig6c-new-information', 'fig6b-fixed-rate-fraction', 'fig7a-time-constants',
               'fig7b-k300', 'k300-rate-regression', 'fig9a-mean-cii', 'fig9a-top-quartile', 's7-invariant-information',
               'fig9b-cii-tau-ratio', 'fig9c-cii-k300', 'cii-unimodal'):
        o.update(outcome='blocked', blocked_by='methods_underspecified',
                 notes=(dep404 + " Even with the units, the locally adaptive KDE rates and their jackknife estimates alone were estimated in "
                        "the notebook at more than 100 hours on one core (cell 'cost'), before the Monte Carlo cumulative information, so the "
                        "claim would also be too_large here.") if i == 'units-337' else dep337)
    else:
        notes = dep404
        if i == 's2-spike-counts':
            notes += (" As a variant that decides nothing, on all 1246 single units with I_AR of at least 2.3 bits/s: largest count 9 "
                      "(4 units), 442 bins with 8 spikes, mean count per bin 0.132 (0.127 over trial-averaged counts).")
        if i == 'fig2cd-fano-factor':
            notes += (" Variant on the 1246 auditory single units, deciding nothing: time-averaged Fano factor 1.027 (SEM 0.002) as the "
                      "code, 1.054 (SEM 0.003) leaving out empty bins; both differ from 1 at this n (t-test p 7.4e-38 and 1.2e-69).")
        if i == 'fig2b-noise-correlations':
            notes += (" Variant on the 1246 auditory single units, deciding nothing: noise correlation median 0.152, skewness 1.09; "
                      "stimulus correlation median 0.291 over stimuli and 0.239 within stimuli.")
        if i == 's1-temporal-resolution':
            notes += (" Variant on the 1246 auditory single units, deciding nothing: the coherence stored in the files (4 to 496 Hz, "
                      "integrating to the stored I_AR) puts 65.8% +- 19.0% of I_AR below 50 Hz. The KDE power part needs the KDE "
                      "rates, which are too large to compute here (see units-337).")
        if i == 'fig2a-poisson-test':
            notes += " The test also needs the KDE and jackknife KDE rates of every unit and stimulus, too large to compute here (see units-337)."
        o.update(outcome='blocked', blocked_by='methods_underspecified', notes=notes)
    out.append(o)
assert [o['claim'] for o in out] == ids

rec = {
 'schema_version': 3, 'id': 'elie-2019-01',
 'datasets': [{'archive': 'crcns', 'id': 'aa-4', 'version': 'unversioned', 'doi': '10.6080/K00C4T06', 'relation': 'primary'}],
 'paper': 'doi:10.1371/journal.pcbi.1006698', 'date': '2026-11-13', 'entry': 'elie-2019',
 'provenance': {'kind': 'agent', 'accountable': {'name': 'CatalystNeuro'},
                'agent': {'harness': 'Claude Code', 'model': 'claude-opus-5-5', 'protocol': 'pilot-15'},
                'runner': {'platform': 'GitHub Actions', 'url': 'https://github.com/catalystneuro/encore/actions/runs/43501306087'}},
 'inputs': [{'what': 'The tutorial model cell ModelCell_InfoCumInfo_Tutorial.mat (spike rasters, model rates and the MATLAB results of the tutorial), for fig1-model-neurons.',
             'source': 'https://github.com/julieelie/PoissonTimeVaryingInfo at commit 978020328321c7ed83be12c0152bed85ec77e218'}],
 'outcomes': out,
 'findings': [
  {'kind': 'metadata_insufficient', 'statement': ("The files do not mark the 914 single auditory units the data description and the paper report, "
     "nor the 404 units the paper analyses. 1281 h5 files are labelled single units (sortType), 1246 of them with stored I_AR of at least "
     "2.3 bits/s, the 2015 auditory threshold; the spike-snippet SNR that defines a single unit is not stored. Without a list of units, "
     "none of the paper's population results can be repeated on its units.")},
  {'kind': 'metadata_error', 'statement': ("The data description says the data set holds 688 multi-units and 914 single auditory units, one h5 "
     "file each. The files are 845 unsorted multi-unit files (sortType tdt) and 1453 spike-sorted files (named _ss): 1281 labelled single, "
     "63 multi and 109 noise.")},
  {'kind': 'data_missing', 'statement': ("The anatomical area and the x, y, z coordinates of the recording sites, used in the paper's Table 1 and "
     "Figure 10, are not in the data set; only the electrode, site and array depths are stored.")},
  {'kind': 'metadata_error', 'statement': ("The numbers of stimuli and trials differ from the stated ones. Single units have 95.4 call stimuli on "
     "average (63 to 120) against the paper's 114 (34 to 123), and 121.9 stimuli of any kind (73 to 137) against the description's 144 (64 to 153). "
     "1874 unit-stimulus pairs have 12 trials, against a stated maximum of 11.")},
  {'kind': 'metadata_error', 'statement': ("Three h5 files store sortType as 'singl'; and the description's section on file organisation names a "
     "bird WhiBlu5896M, where the files and the summary say WhiBlu5396M.")},
  {'kind': 'metadata_insufficient', 'statement': ("The per-site .f32 files of spike waveforms are described only as the waveform of the action "
     "potentials; their layout (18-sample snippets, per the tutorial code) and their link to the spike_ids of the h5 files are not documented, "
     "and they exist for only some sites.")},
  {'kind': 'methods_unavailable', 'statement': ("The paper selects its 404 units by a decoding analysis it does not describe, citing Elie and "
     "Theunissen 2015, and its code repository holds neither that selection nor the selection of the 337 units, the locally adaptive KDE "
     "step, the exponential fits or the CII. Question for the authors: can the lists of the 914, 404 and 337 units be published, with the "
     "file names of the data set? For the jackknife bias correction of the Monte Carlo cumulative information, do the jackknife replicates "
     "share their Monte Carlo samples (assumed here for the model neuron, with the independent variant shown)?")},
 ],
}
class D(yaml.SafeDumper): pass
yaml.dump(rec, open('attempts/elie-2019-01.yaml', 'w'), Dumper=D, sort_keys=False, width=110, allow_unicode=True)
PYEOF
grep -n ": .*: " attempts/elie-2019-01.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: '" | head; python tools/entry.py check entries/elie-2019 2>&1 | tail -15
```

```
0 error(s)
```

**Agent calls Bash**

```bash
date -u; time python tools/entry.py all entries/elie-2019 2>&1 | tail -4
```

```
Fri Nov 13 21:37:12 UTC 2026
Installed kernelspec registry-elie-2019 in executed/elie-2019/.venv/share/jupyter/kernels/registry-elie-2019
0 error(s)
pass  reproduce_elie_2019.ipynb  (797 s)

real	13m27.348s
user	24m9.617s
sys	0m31.308s
```

**Agent calls Bash**

```bash
python - <<'E'
import json
nb=json.load(open('executed/elie-2019/reproduce_elie_2019.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=''.join(o.get('text') or '')
            for l in t.splitlines():
                if any(k in l for k in ['KDE estimates','estimate for','loaded','start (ms)','peak bias','cumulative information:','variant,','mean |KDE','Fano','coherence information','s2:']): print(l[:250])
E
date -u; python tools/entry.py handover entries/elie-2019 2>&1 | tail -5; ls executed/elie-2019/handover; git status --short
```

```
loaded 2298 h5 files in 456 s; peak memory 1.01 GB (this process)
60 KDE estimates on 3 units: 1.24 s each
estimate for the rates alone (404 units x 95 stimuli x 11 estimates): 146 h on one core, 37 h on 4 cores
s2: largest count in a 10 ms bin 9; bins with 8 spikes 442; bins with more than 8: 4 units have one; mean count per bin over trials 0.132, over trial-averaged counts 0.127 (paper, 404 units: 8, 1, 0.108)
Fano (fano_a): mean 1.027, SEM 0.002, range 0.86 to 1.98; t-test vs 1 p = 7.4e-38; Wilcoxon vs 1 p = 4.3e-59 (paper: 1.04, SEM 0.04)
Fano (fano_b): mean 1.054, SEM 0.003, range 0.79 to 1.99; t-test vs 1 p = 1.2e-69; Wilcoxon vs 1 p = 9.5e-83 (paper: 1.04, SEM 0.04)
coherence information below 50 Hz: 65.8% +- 19.0% (mean +- SD); units losing more than 5%: 1245 of 1246 (paper, 404 units: 96.7 +- 6.9%, 88 of 404)
start (ms) of the bins where each stimulus drives a response (model count > 0.1): [[30, 40, 50, 60, 70], [120, 130, 140, 150, 160], [210, 220, 230, 240, 250], [310, 320, 330, 340, 350]]
mean |KDE - model rate| per stimulus (spikes/ms): [0.0103 0.01   0.0075 0.0082] ; all: 0.009 ; RMS: 0.0161
peak bias-corrected instantaneous information 0.519 bits at bin ending 140 ms (model rate: 0.540); uncorrected peak 0.500
cumulative information: largest 1.928 bits, last bin 1.828 bits (model rate: 1.956); largest jackknife SE 0.085 bits; maximum log2(4) = 2 bits
variant, independent draws per replicate: largest 2.206 bits, last bin 0.803 bits
Fri Nov 13 21:50:42 UTC 2026
wrote executed/elie-2019/handover
elie-2019.yaml
elie.py
reproduce_elie_2019.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
ls -a entries/elie-2019; git status --short --ignored entries/elie-2019 | head
```

```
.
..
.claude
README.md
__pycache__
elie.py
entry.yaml
reproduce_elie_2019.ipynb
requirements.in
requirements.lock.txt
?? entries/elie-2019/
!! entries/elie-2019/__pycache__/
```

**Agent calls Bash**

```bash
ls -la entries/elie-2019/.claude; rm -rf entries/elie-2019/__pycache__
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Nov 13 20:49 .
drwxr-xr-x 4 runner runner 4096 Nov 13 21:22 ..
drwx------ 2 runner runner 4096 Nov 13 20:49 .cc-writes
```

**Agent**

The entry is written, locked and checked (0 errors), and the notebook ran from a clean environment in 13.3 minutes. `tools/entry.py handover` built the verifier's package in `executed/elie-2019/handover/`. Only one of the 25 claims could be tested: almost all the others rest on the paper's 404 units, which the files do not identify.

**1. Outcomes**

| claim | outcome |
|---|---|
| fig1-model-neurons (data: elsewhere) | partially reproduced |
| units-404 | blocked, methods_underspecified (the reason the criterion names) |
| units-337, s1, fig2a, fig2cd, fig2b, s2, fig6a, fig6c, fig6b, fig7a, fig7b, k300-rate-regression, fig9a-mean-cii, fig9a-top-quartile, s7, fig9b, fig9c, cii-unimodal | blocked, methods_underspecified (they rest on units-404); also too large to run, see section 4 |
| fig3-5-example-neurons | blocked, methods_underspecified (the paper does not name the three units) |
| table1-anatomy-counts and the four fig10 claims | blocked, data_missing |

- **Why fig1 is only partial:** the code repository holds one of the three model neurons in Fig 1, the temporal one. On that neuron all three conditions pass:
  - KDE error 0.009 spikes/ms, against a limit of 0.02.
  - Cumulative information reaches 1.928 bits, against a threshold of 1.8.
  - Peak instantaneous information 0.519 bits, within 0.5 ± 0.05.
- **KDE port:** the Python port matches the KDE saved by the paper's MATLAB tutorial to 0.0004 spikes/ms on average.

**2. Dataset, assumptions, questions**
- **Unit labels missing:** there are 1281 files labelled single units, and 1246 pass the 2.3 bits/s auditory threshold. The files do not mark the 914 single units or the 404 the paper analyses. The spike-shape quality score (SNR) that defines a single unit is not stored.
- **File counts:** the description says 688 multi-units and 914 single units. The files are 845 unsorted multi-unit files and 1453 spike-sorted files.
- **No anatomy:** there are no brain areas or coordinates for the recording sites, only electrode depths.
- **Stimulus and trial counts:**
  - Call stimuli per unit average 95.4, against the paper's 114.
  - Stimuli of any kind average 121.9, against the description's 144.
  - Some stimuli have 12 trials, against a stated maximum of 11.
- **Labelling errors:**
  - Three files store `sortType` as "singl".
  - The description spells one bird's name two ways (WhiBlu5896M and WhiBlu5396M).
  - The `.f32` spike-waveform files are undocumented.
- **Data checks that passed:** no recording is deposited twice, and spike times share the stimulus-onset clock. Before onset, about 1% of units respond differently by call type; after onset, 44% to 66% do.
- **Assumption (fig1):** the jackknife replicates of the Monte Carlo estimate share their random draws. With independent draws the result still passes, so the outcome does not rest on this.
- **Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
  - Can the lists of the 914, 404 and 337 units be published?
  - Do the jackknife replicates share Monte Carlo samples?
- **Questions to a reader:** none.
- **Variants that decide nothing:** I ran the cheap measures on all 1246 auditory single units instead of the 404, so they describe the units the files hold. Fano factor 1.027 (paper 1.04); stimulus correlation 0.29 (paper about 0.4). Coherence below 50 Hz is 65.8% against the paper's 96.7%. The coherence curve stored in the files may not be the one S1 Fig used.

**3. Protocol points**
1. **Missing base set:** the units-404 criterion assumes the 914 units can be found; it does not say what to do when the starting set itself cannot be identified. I blocked the claim with the reason it names (methods_underspecified) and said in the notes that the main cause is missing labels.
2. **Two block reasons:** "A claim that depends on a blocked claim is blocked for the same reason" conflicts with a claim that has its own, stronger reason. For the anatomy claims I used data_missing as the main reason and noted the inherited one.
3. **Variants:** the protocol does not say whether analyses on a stand-in population may appear when the dependency is blocked. I showed them, marked as deciding nothing.
4. **CRCNS layout:** `archives.md` describes zip files, but aa-4 is tar.gz archives. Those can only be read front to back, so the notebook reads all 7 GB on every run.
5. **One file instead of three:** the claim names three model neurons and the code repository holds one. I recorded partially reproduced.

**4. Runtime and failures**
- The session used about 1 h 26 min (20:25 to 21:51 UTC). The notebook runs in about 13 minutes, 7.5 of them reading the data from S3.
- The first loader took 18 minutes on one core; switching to separate processes fixed that.
- Nothing failed. Independent random draws in the jackknife made the cumulative information unstable, which led to the shared-draws assumption above.
- The paper's KDE pipeline was estimated at 146 hours on one core, or 37 hours on 4, for the rates alone.
- Untracked files I did not create are in the checkout: dotfiles at the repo root and `entries/elie-2019/.claude/`. I left them in place.

Nothing was committed.

## End of run

70 turns, 84 minutes, $5.01 at API prices, result: success.
