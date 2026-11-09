# crcns-ssc-8 · author · run 42461891472

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims/crcns-ssc-8 entries | head -50
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/291e1e12-7e91-4526-b28a-ede8193304d1/tool-results/bpsc5f50k.txt

Preview (first 2KB):
Sun Nov  8 08:19:12 UTC 2026
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/291e1e12-7e91-4526-b28a-ede8193304d1/tool-results/bpsc5f50k.txt"
}
```

```
1	Sun Nov  8 08:19:12 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 683 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/crcns-ssc-8/10.1038-nn.3415.yaml; ls paper; cat paper/ssc-8.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/291e1e12-7e91-4526-b28a-ede8193304d1/tool-results/b6fwi28x7.txt"
}
```

```
1	# Claims for Goncalves, Anstey, Golshani & Portera-Cailliau (2013), Nature Neuroscience 16:903-909,
2	# on CRCNS data set ssc-8 (doi:10.6080/K0X63K3X).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
4	# protocol as stated in docs/protocol.md (Reader, version pilot-13).
5	#
6	# Text read: the version of record, PMC3695061 (open access), Europe PMC full-text XML flattened
7	# to text: abstract, Introduction, Results, Discussion and Online Methods. The text holds no
8	# figure legends and no supplement (Supplementary Figures 1 to 4 are cited but not supplied), and
9	# no PDF was supplied. Every claim below rests on numbers printed in the Results text; details
10	# that the legends or the supplement may have given (the correlation measure of Fig. 1, how
11	# Fig. 1d was binned, the panels of Suppl. Figs. 1 to 4) are treated as open. The paper links no
12	# analysis code. It names outside software only (ScanImage, the iPeak package, Chronux); none
13	# was read, and none of it settles a detail used here.
14	#
15	# Data the paper used. Male and female C57Bl/6 wild-type (WT) and Fmr1 -/- (KO) mice, P9 to P40,
16	# head-fixed and unanesthetized unless stated. Layer 2/3 barrel cortex, right hemisphere, bulk
17	# loaded with Oregon Green BAPTA-1 AM; two-photon imaging at 3.9 Hz (512 x 128 pixels), or
18	# 15.6 Hz in one control experiment. Several 3-min movies concatenated per mouse; contours of
19	# cells drawn on the mean image, astrocytes (sulforhodamine-101) excluded; dF/F per cell, low-pass
20	# filtered and deconvolved; firing rates extrapolated from the deconvolved traces. Ages P9-11,
[... 921 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -l docs/design.md; grep -n -A60 "^## CRCNS" docs/archives.md
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
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ssc-8/" | python3 -c "import sys,re; t=sys.stdin.read(); [print(k,s) for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t)]"; ls entries/001453-fouke-2025/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -150; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/checksums.md5 https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/filelist.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 150,400p attempts/001453-fouke-2025-01.yaml; cat entries/001453-fouke-2025/README.md | head -30
```

```
notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
    stimuli (medians 143 to 191 against 55.4 to 66.4 deg/s2, Kruskal-Wallis p below 0.05/9 for
    each), the reverse of the claim. Per-fish medians, and the files at 128 to 171 Hz alone
    (ZF 84.9, DC 178.6 deg/s2, p = 6.3e-05), give the same. The quantity Fig1-S1.ipynb computes
    gives ZF higher with p below 0.05/9 for 7 of 9 stimuli; it divides the heading change per
    frame by the file's mean frame interval, which in DC files is a median 8.73 times the frame
    interval (ZF 1.37), as DC files hold only trial frames. Part of the DC values may be tracking
    noise. In the 3 s stationary phase the DC median is 205 deg/s2, higher than the 171 during
    motion (per fish median ratio 1.24, p = 0.016), but ZF are also higher at rest (66.9 and 60.8,
    ratio 1.07, p = 0.00012), so this does not separate the species. In frames where the fish is
    still (below 1 mm/s) DC are higher than ZF (per-fish medians 72.4 and 34.9 deg/s2, Mann-Whitney
    p = 0.00014), and DC are higher in every speed band (at 5 mm/s or more, 207 and 85.8). The
    outputs cannot say whether the higher values in moving DC are noise or turning during
    continuous swimming. With the heading from the unwrapped `f0_theta` DC are higher still (218
    to 278 against ZF 61.8 to 77.3 deg/s2, 0 of 9). The reversal should not be read as evidence
    against the paper.
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/10.1038-nn.3415.txt; grep -n -i "deconvol\|correlat\|shuffl\|peaks of synchrony\|firing rate\|Statistical\|ANOVA\|frame\|reference 15\|ref" paper/10.1038-nn.3415.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper is 44 KB; I'll read it whole.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.3415.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; python3 -c "import fsspec, scipy, h5py, numpy, statsmodels; print('ok')"; python3 tools/entry.py --help 2>&1 | head -30
```

```
Sun Nov  8 08:19:45 UTC 2026
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec, scipy, h5py, numpy, statsmodels; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'fsspec'
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/crcns-ssc-8-goncalves-2013 && cd entries/crcns-ssc-8-goncalves-2013 && printf "fsspec\naiohttp\nrequests\nh5py\nscipy\nnumpy\npandas\nmatplotlib\nstatsmodels\n" > requirements.in && cd ../.. && python tools/entry.py lock entries/crcns-ssc-8-goncalves-2013 2>&1 | tail -3 && uv venv -q $TMPDIR/venv && VIRTUAL_ENV=$TMPDIR/venv uv pip install -q -r entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt ipykernel nbconvert 2>&1 | tail -2
```

```
[--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]
entry.py: error: [PosixPath('entries/crcns-ssc-8-goncalves-2013')] has no entry.yaml
error: File not found: entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt
```

**Agent calls Bash**

```bash
cat > entries/crcns-ssc-8-goncalves-2013/entry.yaml <<'EOF'
schema_version: 1
name: crcns-ssc-8-goncalves-2013
type: reproduction
title: Network synchrony in the developing barrel cortex of Fmr1 knockout mice (Goncalves et al. 2013)
description: Tests the calcium imaging findings of Goncalves, Anstey, Golshani and Portera-Cailliau
  (2013) on CRCNS data set ssc-8, which holds the estimated firing rates and cell-to-cell distances
  of L2/3 barrel cortex neurons in unanesthetized WT and Fmr1 knockout mice at three ages. It
  compares pairwise correlation between genotypes and ages, peaks of synchrony and firing rates.
  The whole-cell, EEG, isoflurane and 15.6 Hz data of the paper are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_goncalves_2013.ipynb
  title: Reproducing Goncalves et al. (2013) from CRCNS ssc-8
  runtime_minutes: 5
helpers:
- ssc8.py
related:
- id: crcns:ssc-8/unversioned
  relation: uses_data
- id: doi:10.1038/nn.3415
  relation: reproduces
EOF
python tools/entry.py lock entries/crcns-ssc-8-goncalves-2013 2>&1 | tail -3 && uv venv -q $TMPDIR/venv && VIRTUAL_ENV=$TMPDIR/venv uv pip install -q -r entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt ipykernel nbconvert 2>&1 | tail -2
```

```
Exit code 2
wrote entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt
error: Failed to create virtual environment
  cause: A virtual environment already exists at: /tmp/claude-1001/venv

hint: Use the `--clear` flag or set `UV_VENV_CLEAR=1` to replace the existing virtual environment
```

**Agent calls Bash**

```bash
VIRTUAL_ENV=$TMPDIR/venv uv pip install -q -r entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt ipykernel nbconvert 2>&1 | tail -2; $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, io, scipy.io, time
t=time.time()
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/firingrates_and_distances.mat"
with fsspec.open(url,"rb") as f: b=f.read()
print(len(b), time.time()-t, b[:120])
import hashlib; print(hashlib.md5(b).hexdigest())
m=scipy.io.loadmat(io.BytesIO(b))
for k,v in m.items():
    if k.startswith('__'): continue
    print(k, type(v), getattr(v,'shape',None), v.dtype)
    for i,x in enumerate(v.ravel()[:20]): print('   ',i, x.shape, x.dtype)
EOF
```

```
14673677 0.7155261039733887 b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Thu Oct  5 21:27:47 2017                                         \x00\x00\x00\x00'
ae1b48123540ecfd1bc9675c1eaa9a3d
WT_P9P11_movies <class 'numpy.ndarray'> (13, 1) object
    0 (2160, 98) float64
    1 (2870, 49) float64
    2 (3600, 164) float64
    3 (2880, 198) float64
    4 (2160, 79) float64
    5 (1873, 90) float64
    6 (1598, 107) float64
    7 (2011, 108) float64
    8 (2160, 112) float64
    9 (2160, 123) float64
    10 (2160, 128) float64
    11 (2160, 103) float64
    12 (2160, 120) float64
KO_P9P11_movies <class 'numpy.ndarray'> (9, 1) object
    0 (1851, 142) float64
    1 (2160, 97) float64
    2 (2079, 84) float64
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, io, scipy.io, numpy as np, hashlib
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/firingrates_and_distances.mat"
with fsspec.open(url,"rb") as f: b=f.read()
open('ssc8.mat','wb').write(b)  # local scratch copy for exploration only
m=scipy.io.loadmat(io.BytesIO(b))
hs={}
for g in ['WT_P9P11','WT_P14P16','WT_P30P40','KO_P9P11','KO_P14P16','KO_P30P40']:
    for i,(x,d) in enumerate(zip(m[g+'_movies'].ravel(), m[g+'_distances'].ravel())):
        nz=(x>0).mean(); u=np.unique(x)
        print(g,i,x.shape,'min %.3g max %.3g mean %.4g nzfrac %.3f nuniq %d'%(x.min(),x.max(),x.mean(),nz,len(u)), 'u:',np.round(u[:5],4), 'nan',np.isnan(x).sum(),
              'D: sym',np.allclose(d,d.T),'diag',np.abs(np.diag(d)).max(),'max %.0f'%np.nanmax(d), 'frac<100 %.3f'%((d[np.triu_indices_from(d,1)]<100).mean()), 'zeros-cols', (x.sum(0)==0).sum())
        h=hashlib.md5(x.tobytes()).hexdigest(); hs.setdefault(h,[]).append((g,i))
print([v for v in hs.values() if len(v)>1])
EOF
```

```
WT_P9P11 0 (2160, 98) min 0 max 27.4 mean 0.2451 nzfrac 0.090 nuniq 18982 u: [0.     0.6663 0.667  0.671  0.6722] nan 0 D: sym True diag 0.0 max 229 frac<100 0.578 zeros-cols 0
WT_P9P11 1 (2870, 49) min 0 max 41.9 mean 0.292 nzfrac 0.108 nuniq 15147 u: [0.     0.6109 0.6132 0.6155 0.6156] nan 0 D: sym True diag 0.0 max 253 frac<100 0.609 zeros-cols 0
WT_P9P11 2 (3600, 164) min 0 max 49.9 mean 0.5438 nzfrac 0.119 nuniq 70002 u: [0.     0.9504 0.9528 0.9532 0.9565] nan 0 D: sym True diag 0.0 max 405 frac<100 0.387 zeros-cols 0
WT_P9P11 3 (2880, 198) min 0 max 26.9 mean 0.4076 nzfrac 0.124 nuniq 70452 u: [0.     0.6488 0.6493 0.6494 0.6507] nan 0 D: sym True diag 0.0 max 341 frac<100 0.491 zeros-cols 0
WT_P9P11 4 (2160, 79) min 0 max 23.7 mean 0.3458 nzfrac 0.103 nuniq 17587 u: [0.     0.7631 0.7641 0.7694 0.7697] nan 0 D: sym True diag 0.0 max 189 frac<100 0.885 zeros-cols 0
WT_P9P11 5 (1873, 90) min 0 max 37.8 mean 0.4367 nzfrac 0.091 nuniq 15315 u: [0.     1.0554 1.0561 1.0593 1.0595] nan 0 D: sym True diag 0.0 max 242 frac<100 0.709 zeros-cols 0
WT_P9P11 6 (1598, 107) min 0 max 30.9 mean 0.4188 nzfrac 0.106 nuniq 18169 u: [0.     0.9204 0.921  0.9225 0.9229] nan 0 D: sym True diag 0.0 max 245 frac<100 0.704 zeros-cols 0
WT_P9P11 7 (2011, 108) min 0 max 16.7 mean 0.3737 nzfrac 0.119 nuniq 25834 u: [0.     0.7033 0.7053 0.7053 0.706 ] nan 0 D: sym True diag 0.0 max 241 frac<100 0.760 zeros-cols 0
WT_P9P11 8 (2160, 112) min 0 max 46 mean 0.5291 nzfrac 0.099 nuniq 24029 u: [0.     0.9405 0.9628 0.9642 0.9658] nan 0 D: sym True diag 0.0 max 239 frac<100 0.685 zeros-cols 0
WT_P9P11 9 (2160, 123) min 0 max 45.8 mean 0.3805 nzfrac 0.067 nuniq 17811 u: [0.     1.2266 1.2346 1.2367 1.2523] nan 0 D: sym True diag 0.0 max 240 frac<100 0.683 zeros-cols 0
WT_P9P11 10 (2160, 128) min 0 max 41.2 mean 0.4956 nzfrac 0.105 nuniq 29087 u: [0.     1.0369 1.0378 1.0414 1.0439] nan 0 D: sym True diag 0.0 max 249 frac<100 0.599 zeros-cols 0
WT_P9P11 11 (2160, 103) min 0 max 33.4 mean 0.37
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
rm -f $TMPDIR/ssc8.mat; $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, tarfile, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/Ca2+_imaging_TIFFs.tar.gz"
t=time.time()
f=fsspec.open(url,"rb",block_size=2**24).open()
tf=tarfile.open(fileobj=f,mode="r|gz")
n=0
for mem in tf:
    print(mem.name, mem.size, round(time.time()-t,1))
    if mem.isfile():
        x=tf.extractfile(mem); 
        hdr=x.read(4096); print(hdr[:8])
        n+=1
    if n>=2: break
print(f.loc if hasattr(f,'loc') else '', time.time()-t)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/fsspec/implementations/http.py", line 447, in _info
    await _file_info(
    ...<5 lines>...
    )
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/fsspec/implementations/http.py", line 865, in _file_info
    r.raise_for_status()
    ~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/aiohttp/client_reqrep.py", line 842, in raise_for_status
    raise ClientResponseError(
    ...<5 lines>...
    )
aiohttp.client_exceptions.ClientResponseError: 404, message='Not Found', url='https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/Ca2+_imaging_TIFFs.tar.gz'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/fsspec/core.py", line 147, in open
[... 23 more lines not kept]
```

**Agent**

The `+` must be URL-encoded as `%2B`.

**Agent calls Bash**

```bash
timeout 300 $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, tarfile, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/Ca2%2B_imaging_TIFFs.tar.gz"
t=time.time()
f=fsspec.open(url,"rb",block_size=2**24).open()
tf=tarfile.open(fileobj=f,mode="r|gz")
n=0
for mem in tf:
    print(mem.name, mem.size, round(time.time()-t,1))
    if mem.isfile():
        x=tf.extractfile(mem); hdr=x.read(); print(hdr[:16], len(hdr))
        n+=1
    if n>=3: break
print(f.tell(), time.time()-t)
EOF
```

```
Ca2+_imaging_TIFFs 0 0.5
Ca2+_imaging_TIFFs/Fmr1_KO_P9-P11_4Hz 0 0.5
Ca2+_imaging_TIFFs/Fmr1_KO_P9-P11_4Hz/Movie_8.tif 128631934 0.5
b'MM\x00*\x00\x00\x00\x08\x00\n\x00\xfe\x00\x04\x00\x00' 128631934
Ca2+_imaging_TIFFs/Fmr1_KO_P9-P11_4Hz/Movie_2.tif 142037288 3.7
b'II*\x00\x08\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00' 142037288
Ca2+_imaging_TIFFs/Fmr1_KO_P9-P11_4Hz/Movie_9.tif 141764334 6.6
b'MM\x00*\x00\x00\x00\x08\x00\n\x00\xfe\x00\x04\x00\x00' 141764334
243517440 9.946989297866821
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-8-goncalves-2013 && echo tifffile >> requirements.in && cd ../.. && python tools/entry.py lock entries/crcns-ssc-8-goncalves-2013 2>&1|tail -1 && VIRTUAL_ENV=$TMPDIR/venv uv pip install -q -r entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt && date -u && timeout 900 $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, tarfile, time, io, tifffile, numpy as np, resource
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/Ca2%2B_imaging_TIFFs.tar.gz"
t=time.time()
f=fsspec.open(url,"rb",block_size=2**24).open()
tf=tarfile.open(fileobj=f,mode="r|gz")
for mem in tf:
    if not mem.isfile(): print('DIR',mem.name); continue
    b=tf.extractfile(mem).read()
    try:
        with tifffile.TiffFile(io.BytesIO(b)) as tif:
            p=tif.pages; n=len(p); p0=p[0]
            sw=(p0.software if hasattr(p0,'software') else '')
            desc=(p0.description or '')[:0]
            print(mem.name.split('/',1)[1], mem.size, n, p0.shape, p0.dtype, round(time.time()-t))
    except Exception as e: print(mem.name, 'ERR', e)
print('rss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, time.time()-t)
EOF
```

```
wrote entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt
Sun Nov  8 08:21:05 UTC 2026
DIR Ca2+_imaging_TIFFs
DIR Ca2+_imaging_TIFFs/Fmr1_KO_P9-P11_4Hz
Fmr1_KO_P9-P11_4Hz/Movie_8.tif 128631934 1959 (128, 256) uint16 3
Fmr1_KO_P9-P11_4Hz/Movie_2.tif 142037288 2160 (128, 256) uint16 6
Fmr1_KO_P9-P11_4Hz/Movie_9.tif 141764334 2159 (128, 256) uint16 9
Fmr1_KO_P9-P11_4Hz/Movie_3.tif 136511940 2079 (128, 256) uint16 13
Fmr1_KO_P9-P11_4Hz/Movie_7.tif 142037288 2160 (128, 256) uint16 17
Fmr1_KO_P9-P11_4Hz/Movie_5.tif 142037288 2160 (128, 256) uint16 20
Fmr1_KO_P9-P11_4Hz/Movie_1.tif 121541004 1851 (128, 256) uint16 23
Fmr1_KO_P9-P11_4Hz/Movie_6.tif 134672838 2051 (128, 256) uint16 26
Fmr1_KO_P9-P11_4Hz/Movie_4.tif 134936052 2055 (128, 256) uint16 29
Ca2+_imaging_TIFFs/._.DS_Store ERR not a TIFF file: header=b'\x00\x05\x16\x07'
DIR Ca2+_imaging_TIFFs/WT_P30-P40_4Hz
Ca2+_imaging_TIFFs/WT_P30-P40_4Hz/._.DS_Store ERR not a TIFF file: header=b'\x00\x05\x16\x07'
WT_P30-P40_4Hz/Movie_2.tif 142037288 2160 (128, 256) uint16 32
WT_P30-P40_4Hz/Movie_3.tif 142037288 2160 (128, 256) uint16 36
WT_P30-P40_4Hz/Movie_7.tif 142037288 2160 (128, 256) uint16 39
WT_P30-P40_4Hz/Movie_5.tif 142037288 2160 (128, 256) uint16 43
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
timeout 300 $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, tarfile, time, io, numpy as np, resource, struct
def rss(): return int(open('/proc/self/status').read().split('VmRSS:')[1].split()[0])//1024
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/Ca2%2B_imaging_TIFFs.tar.gz"
f=fsspec.open(url,"rb",block_size=2**22, cache_type="none").open()
tf=tarfile.open(fileobj=f,mode="r|gz")
k=0
for mem in tf:
    if not mem.isfile(): continue
    b=tf.extractfile(mem).read()
    print(mem.name[-30:], rss(), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1024)
    del b; k+=1
    if k>6: break
EOF
```

```
Exit code 124
```

**Agent calls Bash**

```bash
timeout 300 $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, tarfile, time, io, numpy as np, resource
def rss(): return int(open('/proc/self/status').read().split('VmRSS:')[1].split()[0])//1024
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-8/live/Ca2%2B_imaging_TIFFs.tar.gz"
f=fsspec.open(url,"rb",block_size=2**24).open()
tf=tarfile.open(fileobj=f,mode="r|gz")
k=0;t=time.time()
for mem in tf:
    if not mem.isfile(): continue
    b=tf.extractfile(mem).read()
    print(mem.name[-30:], rss(), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1024, round(time.time()-t))
    del b; k+=1
    if k>6: break
EOF
```

```
Fmr1_KO_P9-P11_4Hz/Movie_8.tif 362 484 3
Fmr1_KO_P9-P11_4Hz/Movie_2.tif 380 515 6
Fmr1_KO_P9-P11_4Hz/Movie_9.tif 376 515 9
Fmr1_KO_P9-P11_4Hz/Movie_3.tif 377 515 13
Fmr1_KO_P9-P11_4Hz/Movie_7.tif 374 515 17
Fmr1_KO_P9-P11_4Hz/Movie_5.tif 374 515 21
Fmr1_KO_P9-P11_4Hz/Movie_1.tif 335 515 24
```

**Agent calls Bash**

```bash
date -u; sed -n 1,80p entries/001453-fouke-2025/omr.py; $TMPDIR/venv/bin/python -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:8]: print(c['cell_type'], c['metadata'], ''.join(c['source'])[:1500]); print('-----')
"
```

```
Sun Nov  8 08:30:11 UTC 2026
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative
  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or
  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;
  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median
  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.
[... 199 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-ssc-8-goncalves-2013/ssc8.py",
 "content": "\"\"\"Loading and measures for CRCNS data set ssc-8 (doi:10.6080/K0X63K3X).\n\nGoncalves, Anstey, Golshani & Portera-Cailliau (2013), Nature Neuroscience 16:903-909,\ndoi:10.1038/nn.3415. Two-photon calcium imaging of L2/3 barrel cortex in unanesthetized WT and\nFmr1 -/- (KO) mice at P9-11, P14-16 and P30-40.\n\nThe data set (unversioned on CRCNS; files under ssc-8/live/ in the bucket crcnsarchive) holds\n`firingrates_and_distances.mat`, with per mouse a frames x neurons matrix of estimated firing\nrates and a neurons x neurons matrix of cell-to-cell distances in microns, and\n`Ca2+_imaging_TIFFs.tar.gz`, the raw movies, one per mouse. Both are streamed from the bucket;\nnothing is written to disk.\n\nWhere the parameters come from:\n\n- `FRAME_HZ` = 3.9 Hz, the Methods (\"an acquisition speed of 3.9 Hz\") and the data descriptor.\n  The movie folders are named \"4Hz\"; `FRAME_HZ_ALT` = 4.0 is shown as a variant where a rate in\n  time units is computed.\n- Correlation measures (claims file, shared method): `xcorr0`, the zero-lag normalised\n  cross-correlation without mean subtraction (reading C-b, the claims file's main reading);\n  `pearson`, the paper's own variant; `spearman`, reading C-a, a variant only. Trace reading T-a,\n  the deposited estimated firing rates; T-b (low-pass filtered dF/F) cannot be run, as the data\n  set holds no cell contours.\n- Distance bins under 100, 100 to 200 and over 200 um (claims file, fig1d; Results, paragraph 1).\n  A pair at exactly 100 or 200 um goes to the upper bin, a standard choice that cannot change a\n  result at this precision.\n- Per mouse, the mean over its pairs (claims file, shared method; the n in the paper are mice).\n- The unequal-variance 2 x 3 fixed-effects ANOVA with Satterthwaite error degrees of freedom\n  (Online Methods, Statistical Analyses) is fitted on the six cell means with each cell's\n  variance of the mean (s^2/n); a contrast of k rows is tested with the Welch-James statistic\n  (Johansen 1980), which for one row is the Welch t with Satterthwaite degrees of freedom. The\n  claims file names weighted least squares with inverse-variance weights and Satterthwaite\n  degrees of freedom as its standard choice; this is that model.\n- Peaks of synchrony (Online Methods, \"To calculate frequency...\"): per frame the percent of\n  cells active; 100 shuffles of each cell's trace keeping its mean; the 95th percentile of the\n  100 shuffled peaks is the threshold; an event runs while the percent active is above it. The\n  readings of \"active\" (R-a, rate above 0; R-b, at least one estimated spike in the frame, rate\n  / FRAME_HZ >= 1) and of the shuffle (S-a, permutation of frames; S-b, circular shift) are the\n  claims file's. The seed is a standard choice.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport struct\nimport tarfile\n\nimport fsspec\nimport numpy as np\nimport scipy.io\nfrom scipy import stats\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com\"\nDATASET_ID = \"ssc-8\"\nDATASET_VERSION = \"unversioned\"   # CRCNS data sets are not versioned (docs/archives.md)\nDATASET_DOI = \"10.6080/K0X63K3X\"\nMAT_URL = f\"{BUCKET}/ssc-8/live/firingrates_and_distances.mat\"\nTIFF_URL = f\"{BUCKET}/ssc-8/live/Ca2%2B_imaging_TIFFs.tar.gz\"\nCHECKSUMS_URL = f\"{BUCKET}/ssc-8/live/checksums.md5\"\n\nGENOTYPES = [\"WT\", \"KO\"]\nAGES = [\"P9P11\", \"P14P16\", \"P30P40\"]\nAGE_LABEL = {\"P9P11\": \"P9-11\", \"P14P16\": \"P14-16\", \"P30P40\": \"P30-40\"}\nGROUPS = [(g, a) for g in GENOTYPES for a in AGES]\n# Folder names in the TIFF archive for each group.\nTIFF_FOLDER = {(\"WT\", \"P9P11\"): \"WT_P9-P11_4Hz\", (\"WT\", \"P14P16\"): \"WT_P14-P16_4Hz\",\n               (\"WT\", \"P30P40\"): \"WT_P30-P40_4Hz\", (\"KO\", \"P9P11\"): \"Fmr1_KO_P9-P11_4Hz\",\n               (\"KO\", \"P14P16\"): \"Fmr1_KO_P14-P16_4Hz\", (\"KO\", \"P30P40\"): \"Fmr1_KO_P30-P40_4Hz\"}\n\nFRAME_HZ = 3.9\nFRAME_HZ_ALT = 4.0\nBINS = [(0.0, 100.0, \"<100\"), (100.0, 200.0, \"100-200\"), (200.0, np.inf, \">200\")]\nN_SHUFFLES = 100\nSHUFFLE_PERCENTILE = 95\n\n\ndef checksums() -> dict[str, str]:\n    \"\"\"The data set's published MD5 sums, by file name.\"\"\"\n    with fsspec.open(CHECKSUMS_URL, \"rt\") as f:\n        return {line.split()[1]: line.split()[0] for line in f if line.strip()}\n\n\ndef load_mat() -> tuple[dict, str]:\n    \"\"\"Return {(genotype, age): [{'rates': T x N, 'dist': N x N}, ...]} and the file's MD5.\n\n    The 14.7 MB file is read into memory from the bucket.\"\"\"\n    with fsspec.open(MAT_URL, \"rb\") as f:\n        raw = f.read()\n    md5 = hashlib.md5(raw).hexdigest()\n    m = scipy.io.loadmat(io.BytesIO(raw))\n    data = {}\n    for g, a in GROUPS:\n        movies = m[f\"{g}_{a}_movies\"].ravel()\n        dists = m[f\"{g}_{a}_distances\"].ravel()\n        data[(g, a)] = [{\"rates\": np.asarray(r, float), \"dist\": np.asarray(d, float)}\n                        for r, d in zip(movies, dists)]\n    keys = sorted(k for k in m if not k.startswith(\"__\"))\n    return data, md5, keys\n\n\n# ---------------------------------------------------------------- TIFF movies\n\ndef _tiff_frames(buf: bytes):\n    \"\"\"Walk the IFD chain of a classic TIFF; return (n_frames, height, width, bits, frame means).\n\n    Each frame's mean pixel value is computed from its strips, assuming uncompressed data, which\n    the Compression tag is checked for.\"\"\"\n    endian = \"<\" if buf[:2] == b\"II\" else \">\"\n    (magic,) = struct.unpack(endian + \"H\", buf[2:4])\n    if magic != 42:\n        raise ValueError(\"not a classic TIFF\")\n    (off,) = struct.unpack(endian + \"I\", buf[4:8])\n    means, shape, bits = [], None, None\n    tsize = {1: 1, 3: 2, 4: 4}\n    while off:\n        (n,) = struct.unpack(endian + \"H\", buf[off:off + 2])\n        tags = {}\n        for i in range(n):\n            e = off + 2 + 12 * i\n            tag, typ, cnt = struct.unpack(endian + \"HHI\", buf[e:e + 8])\n            if typ not in tsize:\n                continue\n            size = tsize[typ] * cnt\n            code = {1: \"B\", 3: \"H\", 4: \"I\"}[typ]\n            if size <= 4:\n                vals = struct.unpack(endian + code * cnt, buf[e + 8:e + 8 + size])\n            else:\n                (p,) = struct.unpack(endian + \"I\", buf[e + 8:e + 12])\n                vals = struct.unpack(endian + code * cnt, buf[p:p + size])\n            tags[tag] = vals\n        w, h = tags[256][0], tags[257][0]\n        bits = tags.get(258, (1,))[0]\n        if tags.get(259, (1,))[0] != 1:\n            raise ValueError(\"compressed TIFF\")\n        shape = (h, w)\n        dt = np.dtype(endian + {8: \"u1\", 16: \"u2\"}[bits])\n        tot, cnt_px = 0.0, 0\n        for so, sb in zip(tags[273], tags[279]):\n            px = np.frombuffer(buf, dtype=dt, count=sb // dt.itemsize, offset=so)\n            tot += float(px.sum(dtype=np.float64))\n            cnt_px += px.size\n        means.append(tot / cnt_px)\n        (off,) = struct.unpack(endian + \"I\", buf[off + 2 + 12 * n:off + 6 + 12 * n])\n    return len(means), shape, bits, np.array(means)\n\n\ndef survey_movies() -> list[dict]:\n    \"\"\"Stream the TIFF archive once; per member, its folder, name, size, MD5, frame count, frame\n    shape and per-frame mean intensity. One movie is held in memory at a time (up to 373 MB).\"\"\"\n    out = []\n    with fsspec.open(TIFF_URL, \"rb\", block_size=2**24) as f:\n        with tarfile.open(fileobj=f, mode=\"r|gz\") as tf:\n            for mem in tf:\n                if not mem.isfile():\n                    continue\n                buf = tf.extractfile(mem).read()\n                parts = mem.name.split(\"/\")\n                rec = {\"path\": mem.name, \"folder\": parts[-2] if len(parts) > 2 else \"\",\n                       \"name\": parts[-1], \"bytes\": mem.size,\n                       \"md5\": hashlib.md5(buf).hexdigest()}\n                try:\n                    n, shape, bits, means = _tiff_frames(buf)\n                    rec.update(tiff=True, frames=n, height=shape[0], width=shape[1], bits=bits,\n                               frame_mean=means)\n                except Exception as e:  # macOS resource forks and the like\n                    rec.update(tiff=False, error=str(e)[:60])\n                del buf\n                out.append(rec)\n    return out\n\n\n# ---------------------------------------------------------------- correlation\n\ndef pair_corr(x: np.ndarray, measure: str) -> np.ndarray:\n    \"\"\"N x N matrix of zero-lag correlations between the columns of x (T x N).\"\"\"\n    x = np.asarray(x, float)\n    if measure == \"spearman\":\n        x = np.apply_along_axis(stats.rankdata, 0, x)\n        measure = \"pearson\"\n    if measure == \"pearson\":\n        x = x - x.mean(0)\n    elif measure != \"xcorr0\":\n        raise ValueError(measure)\n    norm = np.sqrt((x * x).sum(0))\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        c = (x.T @ x) / np.outer(norm, norm)\n    return c\n\n\ndef mouse_pair_means(rec: dict, measure: str) -> dict:\n    \"\"\"Per mouse, the mean correlation of its pairs in each distance bin and over all pairs;\n    pairs with an undefined correlation (a silent cell) are left out and counted.\"\"\"\n    c = pair_corr(rec[\"rates\"], measure)\n    d = rec[\"dist\"]\n    iu = np.triu_indices_from(d, 1)\n    cv, dv = c[iu], d[iu]\n    ok = np.isfinite(cv)\n    res = {\"n_pairs\": int(ok.sum()), \"n_undefined\": int((~ok).sum()), \"all\": float(cv[ok].mean())}\n    for lo, hi, name in BINS:\n        sel = ok & (dv >= lo) & (dv < hi)\n        res[name] = float(cv[sel].mean()) if sel.any() else np.nan\n        res[\"n_\" + name] = int(sel.sum())\n    return res\n\n\n# ---------------------------------------------------------------- statistics\n\ndef welch_james(means, variances, ns, L) -> dict:\n    \"\"\"Welch-James test of L @ mu = 0 for independent groups with unequal variances.\n\n    means, variances (sample variances) and ns are per group; L is k x G. Returns F, df1, df2, p.\n    For k = 1 this is the Welch t-test squared with Satterthwaite degrees of freedom.\"\"\"\n    m = np.asarray(means, float)\n    v = np.asarray(variances, float) / np.asarray(ns, float)\n    n = np.asarray(ns, float)\n    L = np.atleast_2d(np.asarray(L, float))\n    k = L.shape[0]\n    V = np.diag(v)\n    LVL = L @ V @ L.T\n    inv = np.linalg.inv(LVL)\n    est = L @ m\n    T = float(est @ inv @ est)\n    P = V @ L.T @ inv @ L\n    A = 0.0\n    for j in range(len(m)):\n        Q = np.zeros((len(m), len(m)))\n        Q[j, j] = 1.0\n        PQ = P @ Q\n        A += (np.trace(PQ @ PQ) + np.trace(PQ) ** 2) / (2 * (n[j] - 1))\n    c = k + 2 * A - 6 * A / (k + 2)\n    df2 = k * (k + 2) / (3 * A)\n    F = T / c\n    return {\"F\": F, \"df1\": k, \"df2\": df2, \"p\": float(stats.f.sf(F, k, df2)), \"estimate\": est}\n\n\ndef welch_anova(groups) -> dict:\n    \"\"\"Welch's one-way ANOVA for unequal variances.\"\"\"\n    g = [np.asarray(x, float) for x in groups]\n    n = np.array([len(x) for x in g], float)\n    m = np.array([x.mean() for x in g])\n    w = n / np.array([x.var(ddof=1) for x in g])\n    mw = (w * m).sum() / w.sum()\n    k = len(g)\n    num = (w * (m - mw) ** 2).sum() / (k - 1)\n    lam = 3 * (((1 - w / w.sum()) ** 2) / (n - 1)).sum() / (k ** 2 - 1)\n    F = num / (1 + 2 * (k - 2) * lam / 3)\n    df2 = 1 / lam\n    return {\"F\": F, \"df1\": k - 1, \"df2\": df2, \"p\": float(stats.f.sf(F, k - 1, df2))}\n\n\ndef two_by_three(values: dict) -> dict:\n    \"\"\"The unequal-variance 2 x 3 model on per-mouse values {(genotype, age): array}.\n\n    Returns the genotype main effect (KO minus WT, equal weight on the three ages), the age\n    effect within each genotype (2 df) and the interaction.\"\"\"\n    order = GROUPS\n    means = [np.mean(values[k]) for k in order]\n    var = [np.var(values[k], ddof=1) for k in order]\n    ns = [len(values[k]) for k in order]\n    geno = np.array([[-1, -1, -1, 1, 1, 1]]) / 3.0\n    age_wt = np.array([[1, -1, 0, 0, 0, 0], [0, 1, -1, 0, 0, 0]])\n    age_ko = np.array([[0, 0, 0, 1, -1, 0], [0, 0, 0, 0, 1, -1]])\n    inter = np.array([[1, -1, 0, -1, 1, 0], [0, 1, -1, 0, -1, 1]])\n    age_main = np.array([[1, -1, 0, 1, -1, 0], [0, 1, -1, 0, 1, -1]]) / 2.0\n    return {\"genotype\": welch_james(means, var, ns, geno),\n            \"age_main\": welch_james(means, var, ns, age_main),\n            \"age_within_WT\": welch_james(means, var, ns, age_wt),\n            \"age_within_KO\": welch_james(means, var, ns, age_ko),\n            \"interaction\": welch_james(means, var, ns, inter)}\n\n\ndef sem(x) -> float:\n    x = np.asarray(x, float)\n    return float(x.std(ddof=1) / np.sqrt(len(x)))\n\n\n# ---------------------------------------------------------------- peaks of synchrony\n\ndef _active(rates: np.ndarray, rule: str) -> np.ndarray:\n    if rule == \"R-a\":\n        return rates > 0\n    if rule == \"R-b\":\n        return rates / FRAME_HZ >= 1.0\n    raise ValueError(rule)\n\n\ndef _shuffle(rates: np.ndarray, how: str, rng: np.random.Generator) -> np.ndarray:\n    T, N = rates.shape\n    if how == \"S-a\":\n        idx = np.argsort(rng.random((T, N)), axis=0)\n        return np.take_along_axis(rates, idx, axis=0)\n    if how == \"S-b\":\n        shifts = rng.integers(0, T, N)\n        rows = (np.arange(T)[:, None] - shifts[None, :]) % T\n        return np.take_along_axis(rates, rows, axis=0)\n    raise ValueError(how)\n\n\ndef synchrony_events(rates: np.ndarray, rule: str, how: str, rng: np.random.Generator) -> dict:\n    \"\"\"Peaks of synchrony of one recording (Online Methods), under an active rule and a shuffle.\n\n    Both shuffles keep each cell's mean rate, as the Methods require. Returns the threshold\n    (percent of cells), the events as (start, end) frame indices (end exclusive), and the\n    participation measures Q-a (per event, fraction of cells active in any frame of the event,\n    averaged over events) and Q-b (fraction of cells active in at least one event).\"\"\"\n    T, N = rates.shape\n    act = _active(rates, rule)\n    pct = 100.0 * act.mean(1)\n    peaks = np.empty(N_SHUFFLES)\n    for s in range(N_SHUFFLES):\n        peaks[s] = 100.0 * _active(_shuffle(rates, how, rng), rule).mean(1).max()\n    thr = float(np.percentile(peaks, SHUFFLE_PERCENTILE))\n    above = pct > thr\n    edges = np.diff(np.concatenate([[0], above.astype(int), [0]]))\n    starts, ends = np.flatnonzero(edges == 1), np.flatnonzero(edges == -1)\n    in_any = np.zeros(N, bool)\n    frac = []\n    for a, b in zip(starts, ends):\n        part = act[a:b].any(0)\n        in_any |= part\n        frac.append(part.mean())\n    return {\"threshold\": thr, \"n_events\": len(starts), \"frames\": T,\n            \"rate_per_s\": len(starts) / (T / FRAME_HZ),\n            \"rate_per_s_4hz\": len(starts) / (T / FRAME_HZ_ALT),\n            \"Q-a\": float(np.mean(frac)) if frac else np.nan,\n            \"Q-b\": float(in_any.mean()),\n            \"mean_pct_active\": float(pct.mean())}\n"
}
```

```
File created successfully at: entries/crcns-ssc-8-goncalves-2013/ssc8.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-8-goncalves-2013 && time $TMPDIR/venv/bin/python - <<'EOF'
import ssc8, numpy as np, time
from scipy import stats
rng=np.random.default_rng(0)
a=rng.normal(0,1,8);b=rng.normal(1,2,10)
r=ssc8.welch_james([a.mean(),b.mean()],[a.var(ddof=1),b.var(ddof=1)],[8,10],[[1,-1]])
print(r['p'], stats.ttest_ind(a,b,equal_var=False).pvalue)
g=[rng.normal(0,s,n) for s,n in [(1,8),(2,10),(3,9)]]
L=[[1,-1,0],[0,1,-1]]
print(ssc8.welch_james([x.mean() for x in g],[x.var(ddof=1) for x in g],[len(x) for x in g],L)['p'], ssc8.welch_anova(g)['p'])
t=time.time(); data,md5,keys=ssc8.load_mat(); print(md5, time.time()-t)
res={}
for meas in ['xcorr0','pearson','spearman']:
    t=time.time()
    vals={k:[ssc8.mouse_pair_means(r,meas) for r in v] for k,v in data.items()}
    res[meas]=vals
    print(meas, round(time.time()-t,1))
    for k,v in vals.items():
        x=np.array([d['<100'] for d in v]); y=np.array([d['all'] for d in v])
        print('  ',k, 'n',len(x),'<100 %.3f±%.3f'%(x.mean(),ssc8.sem(x)),'all %.3f±%.3f'%(y.mean(),ssc8.sem(y)), 'undef',sum(d['n_undefined'] for d in v))
import pickle; pickle.dump(res,open('/tmp/claude-1001/res.pkl','wb'))
EOF
```

```
0.07112257492165433 0.07112257492165437
0.10222905467722104 0.10222905467722104
ae1b48123540ecfd1bc9675c1eaa9a3d 0.7281954288482666
xcorr0 0.1
   ('WT', 'P9P11') n 13 <100 0.360±0.024 all 0.318±0.024 undef 0
   ('WT', 'P14P16') n 8 <100 0.169±0.010 all 0.163±0.011 undef 0
   ('WT', 'P30P40') n 7 <100 0.119±0.005 all 0.114±0.005 undef 59
   ('KO', 'P9P11') n 9 <100 0.421±0.022 all 0.395±0.022 undef 0
   ('KO', 'P14P16') n 10 <100 0.204±0.013 all 0.194±0.013 undef 0
   ('KO', 'P30P40') n 6 <100 0.134±0.011 all 0.131±0.010 undef 0
pearson 0.1
   ('WT', 'P9P11') n 13 <100 0.310±0.025 all 0.266±0.026 undef 0
   ('WT', 'P14P16') n 8 <100 0.078±0.010 all 0.073±0.010 undef 0
   ('WT', 'P30P40') n 7 <100 0.049±0.005 all 0.044±0.005 undef 59
   ('KO', 'P9P11') n 9 <100 0.374±0.027 all 0.346±0.027 undef 0
   ('KO', 'P14P16') n 10 <100 0.118±0.014 all 0.108±0.014 undef 0
   ('KO', 'P30P40') n 6 <100 0.047±0.011 all 0.044±0.011 undef 0
spearman 0.5
   ('WT', 'P9P11') n 13 <100 0.246±0.020 all 0.211±0.020 undef 0
   ('WT', 'P14P16') n 8 <100 0.071±0.009 all 0.066±0.010 undef 0
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; time $TMPDIR/venv/bin/python - <<'EOF'
import ssc8, numpy as np, time
data,md5,keys=ssc8.load_mat()
for rule in ['R-a','R-b']:
  for how in ['S-a','S-b']:
    rng=np.random.default_rng(1)
    t=time.time()
    for g in [('WT','P14P16'),('KO','P14P16')]:
        ev=[ssc8.synchrony_events(r['rates'],rule,how,rng) for r in data[g]]
        f=np.array([e['rate_per_s'] for e in ev]); qa=np.array([e['Q-a'] for e in ev]); qb=np.array([e['Q-b'] for e in ev])
        print(rule,how,g,'freq %.3f±%.3f'%(f.mean(),ssc8.sem(f)),'Qa %.3f±%.3f'%(np.nanmean(qa),ssc8.sem(qa)),'Qb %.3f'%qb.mean(),'thr',np.round([e['threshold'] for e in ev],1), [e['n_events'] for e in ev])
    print(time.time()-t)
EOF
```

```
Sun Nov  8 08:31:26 UTC 2026
R-a S-a ('WT', 'P14P16') freq 0.055±0.008 Qa 0.408±0.018 Qb 1.000 thr [26.2 23.5 25.5 26.5 31.2 25.  30.8 28.6] [15, 18, 26, 25, 33, 34, 49, 11]
R-a S-a ('KO', 'P14P16') freq 0.060±0.006 Qa 0.443±0.018 Qb 0.998 thr [24.6 24.2 24.5 24.  28.6 28.1 31.2 27.7 26.6 37.5] [34, 31, 23, 13, 29, 37, 29, 51, 15, 24]
10.208626508712769
R-a S-b ('WT', 'P14P16') freq 0.056±0.007 Qa 0.408±0.019 Qb 1.000 thr [26.2 23.5 24.6 25.6 30.1 25.  32.3 28.6] [15, 18, 30, 28, 35, 34, 44, 11]
R-a S-b ('KO', 'P14P16') freq 0.063±0.006 Qa 0.438±0.019 Qb 0.998 thr [23.8 24.2 23.5 23.  28.6 28.  31.2 27.7 26.6 37.5] [36, 31, 27, 16, 29, 37, 29, 51, 15, 24]
1.9180054664611816
R-b S-a ('WT', 'P14P16') freq 0.016±0.004 Qa 0.150±nan Qb 0.471 thr [13.1 11.8  8.5 10.2  7.5  6.   6.2  7.8] [11, 7, 7, 10, 3, 6, 14, 0]
R-b S-a ('KO', 'P14P16') freq 0.025±0.005 Qa 0.172±0.017 Qb 0.649 thr [12.3  4.7 11.2 10.  14.3  9.8  9.4  7.4  6.3  7.5] [25, 4, 13, 8, 16, 20, 8, 17, 3, 2]
10.23696517944336
R-b S-b ('WT', 'P14P16') freq 0.017±0.004 Qa 0.139±0.016 Qb 0.502 thr [12.1 11.   8.5 10.2  7.5  6.   6.2  6.6] [14, 8, 7, 10, 3, 6, 14, 1]
R-b S-b ('KO', 'P14P16') freq 0.027±0.006 Qa 0.171±0.017 Qb 0.656 thr [11.5  4.7 10.2 10.  13.2  9.8  9.4  6.4  6.3  5.1] [27, 4, 13, 8, 21, 20, 8, 18, 3, 2]
2.0147194862365723

real	0m25.934s
user	0m26.053s
sys	0m0.154s
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-8-goncalves-2013 && python3 - <<'EOF'
import re
s=open('ssc8.py').read()
s=s.replace('''def sem(x) -> float:
    x = np.asarray(x, float)
    return''','''def sem(x) -> float:
    """Standard error of the mean, NaN values left out."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    return''')
open('ssc8.py','w').write(s)
EOF
timeout 600 $TMPDIR/venv/bin/python - <<'EOF'
import ssc8, numpy as np, fsspec, tarfile, hashlib, time
data,md5,keys=ssc8.load_mat()
t=time.time()
recs=[]
with fsspec.open(ssc8.TIFF_URL,"rb",block_size=2**24) as f:
    with tarfile.open(fileobj=f,mode="r|gz") as tf:
        for mem in tf:
            if not mem.isfile() or not mem.name.endswith('.tif') or '/._' in mem.name: continue
            buf=tf.extractfile(mem).read()
            n,shape,bits,means=ssc8._tiff_frames(buf)
            recs.append((mem.name,n,shape,means))
            if len(recs)>=9: break
print(time.time()-t)
ko=data[('KO','P9P11')]
for name,n,shape,means in recs:
    i=int(name.split('Movie_')[1].split('.')[0])-1
    pop=ko[i]['rates'].mean(1)
    dm=np.diff(means, prepend=means[0])
    out=[]
    for j,r in enumerate(ko):
        p=r['rates'].mean(1); L=min(len(p),len(means))
        out.append(np.corrcoef(p[:L],means[:L])[0,1])
    lags=range(-5,6)
    lc=[np.corrcoef(np.roll(pop,l),means)[0,1] for l in lags]
    print(name[-12:], n, len(pop), 'own %.2f others max %.2f'%(out[i], max(o for j,o in enumerate(out) if j!=i)), 'lag corr', np.round(lc,2))
EOF
```

```
/bin/bash: line 1: cd: entries/crcns-ssc-8-goncalves-2013: No such file or directory
27.36770510673523
/Movie_8.tif 1959 1959 own 0.84 others max 0.13 lag corr [0.45 0.52 0.61 0.69 0.77 0.84 0.88 0.9  0.9  0.88 0.84]
/Movie_2.tif 2160 2160 own 0.69 others max 0.13 lag corr [0.29 0.36 0.44 0.53 0.62 0.69 0.74 0.75 0.73 0.69 0.63]
/Movie_9.tif 2159 2159 own 0.70 others max 0.13 lag corr [0.31 0.37 0.45 0.54 0.63 0.7  0.76 0.78 0.78 0.75 0.72]
/Movie_3.tif 2079 2079 own 0.68 others max 0.12 lag corr [0.3  0.37 0.45 0.54 0.62 0.68 0.72 0.73 0.71 0.67 0.62]
/Movie_7.tif 2160 2160 own 0.79 others max 0.16 lag corr [0.31 0.41 0.51 0.62 0.71 0.79 0.83 0.85 0.83 0.78 0.73]
/Movie_5.tif 2160 2160 own 0.80 others max 0.18 lag corr [0.39 0.47 0.56 0.65 0.73 0.8  0.85 0.86 0.85 0.82 0.77]
/Movie_1.tif 1851 1851 own 0.56 others max 0.09 lag corr [0.33 0.38 0.43 0.48 0.53 0.56 0.58 0.59 0.58 0.56 0.54]
/Movie_6.tif 2051 2051 own 0.72 others max 0.07 lag corr [0.32 0.4  0.48 0.56 0.65 0.72 0.77 0.79 0.79 0.77 0.74]
/Movie_4.tif 2055 2055 own 0.77 others max 0.10 lag corr [0.52 0.57 0.62 0.68 0.73 0.77 0.8  0.82 0.81 0.8  0.77]
```

**Agent calls Bash**

```bash
pwd; date -u; $TMPDIR/venv/bin/python -c "import nbformat; print(nbformat.__version__)"; grep -n "sanity\|tag\|claim:" tools/entry.py | head -40
```

```
entries/crcns-ssc-8-goncalves-2013
Sun Nov  8 08:33:02 UTC 2026
5.11.1
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
196:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
305:            tag = outcome.get("output")
306:            if notebook in present and tag:
308:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
309:                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Goncalves et al. (2013) from CRCNS ssc-8\n\n**Paper.** Goncalves JT, Anstey JE, Golshani P, Portera-Cailliau C (2013). Circuit level defects in\nthe developing neocortex of Fragile X mice. *Nature Neuroscience* 16:903-909,\n[doi:10.1038/nn.3415](https://doi.org/10.1038/nn.3415). The claims file\n(`claims/crcns-ssc-8/10.1038-nn.3415.yaml`) was written from the version of record in PubMed Central\n(PMC3695061): main text and Online Methods, without the figure legends or the supplement.\n\n**Data set.** CRCNS ssc-8, [doi:10.6080/K0X63K3X](https://doi.org/10.6080/K0X63K3X), read from the\npublic bucket `crcnsarchive` under `ssc-8/live/`. CRCNS data sets are not versioned, and the paper\ncites no version (it predates the deposit of 2017); the only published state is the one in\n`ssc-8/live/`, data descriptor version 0.7 (13 October 2017), so that is the state used. It is\nrecorded as `unversioned` and pinned by the MD5 sums of the data set's `checksums.md5`, which the\nnext cell checks against the bytes read:\n`firingrates_and_distances.mat` ae1b48123540ecfd1bc9675c1eaa9a3d and\n`Ca2+_imaging_TIFFs.tar.gz` 75bf460dbe90c625637d1a1af3a25ca3 (the archive is streamed once, and\nits members are hashed one by one, as the archive's own MD5 needs the whole compressed stream).\n\n**What the data set holds.** For each of 53 unanesthetized mice (WT and Fmr1 -/-, three ages), the\nestimated firing rate of each neuron in each frame, the cell-to-cell distances in microns, and the\nraw movie. The whole-cell recordings, the EEG, the isoflurane imaging and the 15.6 Hz imaging of\nthe paper are not in it.\n\n| Claim | Tested here |\n|---|---|\n| group-sizes | tested |\n| fig1d-distance-dependent-decorrelation | tested |\n| fig1e-age-decrease | tested |\n| genotype-pooled-ages | tested |\n| pearson-genotype | tested |\n| fig1ef-p14-16-difference | tested |\n| p30-40-no-difference | tested |\n| fig2b-peak-frequency | tested |\n| fig2c-participation | tested |\n| imaging-firing-rate-no-genotype-difference | tested |\n| unanesthetized-p14-16-values | tested |\n| wholecell-updown-firing, wholecell-state-modulation, fig3f-foa-time, ap-kinetics-similar, fig4-updown-properties-similar, fig4f-spikes-per-up-state, fig4g-up-state-firing-probability | blocked: no whole-cell data |\n| fig5c-firing-vs-lh-p14-16, p30-40-firing-vs-lh, fig5d-correlation-vs-lh, fig5ef-slow-wave-epochs, suppl4a-firing-vs-correlation, fig5g-lh-power-similar | blocked: no EEG, and the EEG subset of recordings is not identified (suppl4a is shown as a variant on 3-min segments) |\n| fast-imaging-control | blocked: no 15.6 Hz imaging |\n| fig6-isoflurane-wt-correlation, fig6-isoflurane-ko-correlation, fig6-isoflurane-firing | blocked: no isoflurane imaging |\n\n**Readings shared by the claims** (claims file, header). The trace is the deposited estimated firing\nrate (reading T-a); reading T-b, the low-pass filtered dF/F, needs the cells to be segmented anew\nfrom the raw movies, and the data set holds no contours, so it cannot be run here. The correlation\nis the zero-lag normalised cross-correlation without mean subtraction (C-b); Spearman (C-a) is a\nvariant only, and Pearson is the paper's own variant (claim pearson-genotype). Each mouse's value\nis the mean over its pairs.\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport statsmodels.api as sm\nfrom scipy import stats\nfrom statsmodels.formula.api import ols\n\nimport ssc8\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\npublished = ssc8.checksums()\ndata, mat_md5, mat_keys = ssc8.load_mat()\nprint(f\"data set {ssc8.DATASET_ID} ({ssc8.DATASET_VERSION}, doi:{ssc8.DATASET_DOI})\")\nprint(\"firingrates_and_distances.mat MD5\", mat_md5, \"matches checksums.md5:\",\n      mat_md5 == published[\"firingrates_and_distances.mat\"])\nprint(\"published MD5 of the TIFF archive:\", published[\"Ca2+_imaging_TIFFs.tar.gz\"])\nt0 = time.time()\nmovies = ssc8.survey_movies()\nprint(f\"streamed the TIFF archive ({len(movies)} members) in {time.time() - t0:.0f} s\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEvery check of the descriptor against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Variables in the MAT file:\", mat_keys)\nrows = []\nfor (g, a), recs in data.items():\n    for i, r in enumerate(recs):\n        x, d = r[\"rates\"], r[\"dist\"]\n        iu = np.triu_indices_from(d, 1)\n        rows.append({\"genotype\": g, \"age\": ssc8.AGE_LABEL[a], \"index\": i, \"movie\": f\"Movie_{i + 1}.tif\",\n                     \"frames\": x.shape[0], \"neurons\": x.shape[1], \"dist_shape_ok\": d.shape == (x.shape[1],) * 2,\n                     \"minutes_at_3.9Hz\": x.shape[0] / ssc8.FRAME_HZ / 60,\n                     \"rate_min\": x.min(), \"rate_max\": x.max(), \"mean_rate\": x.mean(),\n                     \"frac_frames_nonzero\": (x > 0).mean(), \"min_nonzero\": x[x > 0].min(),\n                     \"silent_cells\": int((x.sum(0) == 0).sum()), \"nan\": int(np.isnan(x).sum()),\n                     \"dist_symmetric\": bool(np.allclose(d, d.T)), \"dist_diag_max\": np.abs(np.diag(d)).max(),\n                     \"dist_min_offdiag\": d[iu].min(), \"dist_max\": d[iu].max(), \"pairs\": len(iu[0]),\n                     \"pairs_lt100\": int((d[iu] < 100).sum())})\ninfo = pd.DataFrame(rows)\nprint(\"\\nMice per group (recordings in the MAT file):\")\nprint(info.groupby([\"genotype\", \"age\"], sort=False).size().to_string())\nprint(\"\\nNeurons per recording: %d to %d; frames %d to %d (%.1f to %.1f min at 3.9 Hz; median %.1f)\"\n      % (info.neurons.min(), info.neurons.max(), info.frames.min(), info.frames.max(),\n         info[\"minutes_at_3.9Hz\"].min(), info[\"minutes_at_3.9Hz\"].max(), info[\"minutes_at_3.9Hz\"].median()))\nprint(\"Recordings of exactly 2160 frames:\", int((info.frames == 2160).sum()), \"of\", len(info))\nprint(\"Rates: min %.3g, max %.3g; mean over recordings of the mean rate %.3f; smallest non-zero value %.3f to %.3f\"\n      % (info.rate_min.min(), info.rate_max.max(), info.mean_rate.mean(), info.min_nonzero.min(), info.min_nonzero.max()))\nprint(\"Fraction of non-zero frames per recording: %.3f to %.3f\" % (info.frac_frames_nonzero.min(), info.frac_frames_nonzero.max()))\nprint(\"Silent cells (all zero):\", info.silent_cells.sum(), \"; NaN values:\", info.nan.sum())\nprint(\"Distance matrices square and matching N:\", bool(info.dist_shape_ok.all()), \"; symmetric:\", bool(info.dist_symmetric.all()),\n      \"; zero diagonal:\", bool((info.dist_diag_max == 0).all()))\nprint(\"Off-diagonal distances: %.1f to %.1f um\" % (info.dist_min_offdiag.min(), info.dist_max.max()))\nprint(info.round(3).to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe descriptor says 6 to 13 animals per group, 40 to 149 neurons per animal, 3.9 Hz and about 7 to\n8 min per recording. The counts per group (6 to 13) agree. The neuron counts run to 198 (two WT\nP9-11 recordings have 164 and 198), so the stated range is wrong. Most recordings have 2160 frames,\nwhich is 9.2 min at 3.9 Hz, longer than the stated 7 to 8 min; the range is printed above. The\ndescriptor gives no unit for the estimated rates. They are 0 in about 90% of frames, with\nnon-zero values from about 0.5 upwards, and the mean per recording is 0.19 to 0.74, close to the\nHz the paper reports (0.30 Hz in WT at P14-16, Fig. 6); per frame they would be 3.9 times that\n(about 1.2 Hz). They are read as Hz below (reading U-a), and the claims on rates also show U-b.\nThe distance matrices are symmetric with zero diagonals, and match the neuron counts.\n\"\"\")\n\ncode(r\"\"\"\nmv = pd.DataFrame([{k: v for k, v in m.items() if k != \"frame_mean\"} for m in movies])\ntifs = mv[mv.tiff].copy()\nprint(\"Archive members:\", len(mv), \"; TIFF movies:\", len(tifs), \"; other members (not TIFF):\")\nprint(mv[~mv.tiff][[\"path\", \"bytes\", \"error\"]].to_string(index=False))\nfolder_group = {v: k for k, v in ssc8.TIFF_FOLDER.items()}\ntifs[\"genotype\"] = [folder_group[f][0] for f in tifs.folder]\ntifs[\"age\"] = [ssc8.AGE_LABEL[folder_group[f][1]] for f in tifs.folder]\ntifs[\"index\"] = [int(n.split(\"_\")[1].split(\".\")[0]) - 1 for n in tifs.name]\nprint(\"\\nMovies per folder:\")\nprint(tifs.groupby(\"folder\").size().to_string())\nmerged = tifs.merge(info[[\"genotype\", \"age\", \"index\", \"frames\", \"neurons\"]], on=[\"genotype\", \"age\", \"index\"],\n                    how=\"outer\", suffixes=(\"_tiff\", \"_mat\"), indicator=True)\nprint(\"\\nMovies matched to a MAT recording by group and number (Movie_k is entry k):\",\n      merged._merge.value_counts().to_dict())\nprint(\"Frame count of the movie equals the rows of the rate matrix:\",\n      int((merged.frames_tiff == merged.frames_mat).sum()), \"of\", len(merged))\nprint(\"Frame shapes (height x width):\", tifs.groupby([\"height\", \"width\"]).size().to_dict(), \"; bits:\", tifs.bits.unique().tolist())\ndup = tifs[tifs.duplicated(\"md5\", keep=False)]\nprint(\"Movies with identical bytes:\", len(dup))\n\n# Recordings deposited twice in the MAT file: identical matrices or identical cell traces.\ncol_hash = {}\nfor (g, a), recs in data.items():\n    for i, r in enumerate(recs):\n        for j in range(r[\"rates\"].shape[1]):\n            col = r[\"rates\"][:, j]\n            if col.any():\n                col_hash.setdefault(col.tobytes(), set()).add((g, a, i))\nshared = [v for v in col_hash.values() if len(v) > 1]\nprint(\"Non-silent cell traces found in more than one recording:\", len(shared))\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# Do the rates share the movies' clock? Per recording, the correlation of the population rate (mean\n# over cells) with the movie's mean frame brightness, at lags of -5 to +5 frames, and at lag 0 with\n# the other recordings of the same group (the wrong movie).\nlags = np.arange(-5, 6)\nclock = []\nby_key = {(r.genotype, r.age, r[\"index\"]): m for (_, r), m in zip(tifs.iterrows(), [movies[i] for i in tifs.index])}\nfor (g, a), recs in data.items():\n    for i, r in enumerate(recs):\n        fm = by_key[(g, ssc8.AGE_LABEL[a], i)][\"frame_mean\"]\n        pop = r[\"rates\"].mean(1)\n        lc = [np.corrcoef(np.roll(pop, l)[5:-5], fm[5:-5])[0, 1] for l in lags]\n        others = []\n        for j, r2 in enumerate(recs):\n            if j != i:\n                p2 = r2[\"rates\"].mean(1)\n                n = min(len(p2), len(fm))\n                others.append(np.corrcoef(p2[:n], fm[:n])[0, 1])\n        # concatenation boundaries every 720 frames: brightness step there against elsewhere\n        step = np.abs(np.diff(fm))\n        bnd = [k - 1 for k in range(720, len(fm), 720)]\n        clock.append({\"genotype\": g, \"age\": ssc8.AGE_LABEL[a], \"index\": i, \"r_lag0\": lc[5],\n                      \"best_lag\": int(lags[np.argmax(lc)]), \"r_best\": max(lc),\n                      \"max_r_other_movie\": max(others) if others else np.nan,\n                      \"step_at_720k_over_median\": np.median(step[bnd]) / np.median(step) if bnd else np.nan})\nclock = pd.DataFrame(clock)\nprint(clock.round(2).to_string(index=False))\nprint(\"\\nOwn movie, lag 0: r = %.2f to %.2f (median %.2f); best other movie: up to %.2f\"\n      % (clock.r_lag0.min(), clock.r_lag0.max(), clock.r_lag0.median(), clock.max_r_other_movie.max()))\nprint(\"Recordings whose own movie beats every other movie of the group at lag 0:\",\n      int((clock.r_lag0 > clock.max_r_other_movie).sum()), \"of\", len(clock))\nprint(\"Lag (frames, + = brightness after the rate) of the best correlation:\", clock.best_lag.value_counts().sort_index().to_dict())\nprint(\"Median ratio of the brightness step at frames 720k to the median step: %.1f\" % clock.step_at_720k_over_median.median())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe movies are named for the groups, one folder each (the folders are named \"4Hz\", where the\nMethods and the descriptor give 3.9 Hz). Each movie `Movie_k.tif` has exactly as many frames as\nthe k-th rate matrix of its group, and the population rate follows the movie's brightness, with\nthe best correlation when the brightness lags the rate by a few frames, as a calcium signal lags\nthe spikes it is deconvolved from. Each matrix correlates far better with its own movie than with\nany other of its group. So the rate matrices and the movies share one frame clock, and the k-th\nentry of each group is `Movie_k.tif`. Frames are 128 x 256 pixels in most movies, where the\nMethods give 512 x 128 at 3.9 Hz. Most recordings are 2160 frames, three times 720, which at\n4 Hz is three 3-min movies, consistent with the Methods' \"several 3-min calcium movies were\nconcatenated\"; the brightness step at multiples of 720 frames is printed above. No movie or\ncell trace is deposited twice. The absolute frame rate cannot be checked from the files, as\nthe TIFFs carry no time stamps; 3.9 Hz is used, with 4 Hz as a variant where a rate per second is\ncomputed.\n\"\"\")\n\n# ------------------------------------------------------------ correlations for all mice\ncode(r\"\"\"\nMEASURES = [\"xcorr0\", \"spearman\", \"pearson\"]\nrows = []\nfor meas in MEASURES:\n    for (g, a), recs in data.items():\n        for i, r in enumerate(recs):\n            rows.append({\"measure\": meas, \"genotype\": g, \"age\": a, \"index\": i, **ssc8.mouse_pair_means(r, meas)})\ncorr = pd.DataFrame(rows)\nprint(\"Pairs left out because a cell is silent (correlation undefined):\",\n      corr[corr.measure == \"xcorr0\"].n_undefined.sum(), \"in\",\n      int((corr[corr.measure == \"xcorr0\"].n_undefined > 0).sum()), \"recording(s)\")\nsummary = (corr.groupby([\"measure\", \"genotype\", \"age\"], sort=False)\n           .agg(n=(\"all\", \"size\"), lt100=(\"<100\", \"mean\"), lt100_sem=(\"<100\", ssc8.sem),\n                b100_200=(\"100-200\", \"mean\"), gt200=(\">200\", \"mean\"), all_pairs=(\"all\", \"mean\"),\n                all_sem=(\"all\", ssc8.sem), pairs_lt100=(\"n_<100\", \"sum\")))\nprint(summary.round(4).to_string())\nprint(\"Range of mouse values, pairs under 100 um, xcorr0: %.3f to %.3f\"\n      % (corr[corr.measure == \"xcorr0\"][\"<100\"].min(), corr[corr.measure == \"xcorr0\"][\"<100\"].max()))\n\n\ndef values(meas, col=\"<100\"):\n    d = corr[corr.measure == meas]\n    return {(g, a): d[(d.genotype == g) & (d.age == a)][col].to_numpy() for g, a in ssc8.GROUPS}\n\n\ndef within(x, value, tol):\n    return abs(x - value) <= tol + 1e-12\n\"\"\")\n\n# ------------------------------------------------------------ group sizes\nmd(r\"\"\"\n## group-sizes\n\n> The calcium imaging of unanesthetized mice comprises 12, 9 and 8 WT mice and 9, 10 and 8 Fmr1 -/-\n> mice at P9-11, P14-16 and P30-40.\n\"\"\")\ncode(r\"\"\"\nexpected = {(\"WT\", \"P9P11\"): 12, (\"WT\", \"P14P16\"): 9, (\"WT\", \"P30P40\"): 8,\n            (\"KO\", \"P9P11\"): 9, (\"KO\", \"P14P16\"): 10, (\"KO\", \"P30P40\"): 8}\ngs = pd.DataFrame([{\"genotype\": g, \"age\": ssc8.AGE_LABEL[a], \"mat_recordings\": len(data[(g, a)]),\n                    \"tiff_movies\": int(((tifs.genotype == g) & (tifs.age == ssc8.AGE_LABEL[a])).sum()),\n                    \"paper_fig1e\": expected[(g, a)]} for g, a in ssc8.GROUPS])\ngs[\"match\"] = gs.mat_recordings == gs.paper_fig1e\nprint(gs.to_string(index=False))\nprint(\"Totals: WT %d (paper 29), KO %d (paper 27)\" % (gs[gs.genotype == \"WT\"].mat_recordings.sum(), gs[gs.genotype == \"KO\"].mat_recordings.sum()))\nprint(\"P14-16 against the n of the peaks of synchrony sentence (9 KO, 10 WT): KO %d, WT %d\"\n      % (len(data[(\"KO\", \"P14P16\")]), len(data[(\"WT\", \"P14P16\")])))\nprint(\"Groups matching Fig. 1e:\", int(gs.match.sum()), \"of 6\")\n\"\"\", [\"claim:group-sizes\"])\nmd(r\"\"\"\n**Result: not reproduced.** Two of the six groups match Fig. 1e (KO P9-11, 9, and KO P14-16, 10). The\ndata set holds 13, 8 and 7 WT mice and 9, 10 and 6 KO mice, 28 WT and 25 KO in all, against 29 and\n27 in the paper. The P14-16 counts (8 WT, 10 KO) match neither the Fig. 1e counts (9 WT, 10 KO) nor\nthose of the peaks of synchrony sentence (10 WT, 9 KO). The MAT file and the movies agree on every\ncount.\n\"\"\")\n\n# ------------------------------------------------------------ fig1d\nmd(r\"\"\"\n## fig1d-distance-dependent-decorrelation\n\n> In WT mice, the drop in pairwise correlation from P9-11 (12 mice) to P14-16 (9 mice) is largest for\n> cells less than 100 um apart (mean difference 0.223) and smaller for cells 100-200 um (0.159) and\n> more than 200 um apart (0.067, not significant).\n\nWT mice at P9-11 and P14-16 (13 and 8 in the data set). Readings of the ANOVA, from the criterion:\nA-a, ordinary two-way ANOVA (age by bin, both between); post hoc per bin, the age difference\nagainst the ANOVA's pooled residual mean square, Bonferroni over three bins. A-b, mouse as a\nrepeated measure over bins (split-plot ANOVA); post hoc per bin as an unpaired t-test within the\nbin, Bonferroni over three bins. Six mice (P9-11) have no pairs over 200 um, or few; they are\ncounted below.\n\"\"\")\ncode(r\"\"\"\nEXP_1D = [0.223, 0.159, 0.067]\nTOL_1D = [0.0223, 0.0159, 0.0067]\nBIN_NAMES = [\"<100\", \"100-200\", \">200\"]\n\n\ndef fig1d(meas):\n    d = corr[(corr.measure == meas) & (corr.genotype == \"WT\") & corr.age.isin([\"P9P11\", \"P14P16\"])]\n    long = d.melt(id_vars=[\"age\", \"index\"], value_vars=BIN_NAMES, var_name=\"bin\", value_name=\"r\").dropna()\n    long[\"mouse\"] = long.age + \"_\" + long[\"index\"].astype(str)\n    # A-a: ordinary two-way ANOVA\n    fit = ols(\"r ~ C(age) * C(bin)\", data=long).fit()\n    aov = sm.stats.anova_lm(fit, typ=2)\n    mse, dfr = fit.mse_resid, fit.df_resid\n    out = []\n    for b in BIN_NAMES:\n        x = long[(long.bin == b) & (long.age == \"P9P11\")].r.to_numpy()\n        y = long[(long.bin == b) & (long.age == \"P14P16\")].r.to_numpy()\n        diff = x.mean() - y.mean()\n        t_a = diff / np.sqrt(mse * (1 / len(x) + 1 / len(y)))\n        p_a = min(1.0, 3 * 2 * stats.t.sf(abs(t_a), dfr))\n        p_b = min(1.0, 3 * stats.ttest_ind(x, y).pvalue)\n        out.append({\"bin\": b, \"n_P9-11\": len(x), \"n_P14-16\": len(y), \"mean_P9-11\": x.mean(), \"mean_P14-16\": y.mean(),\n                    \"difference\": diff, \"p_bonf_A-a\": p_a, \"p_bonf_A-b\": p_b})\n    out = pd.DataFrame(out)\n    # A-b: split-plot ANOVA on mice with all three bins\n    full = long.groupby(\"mouse\").filter(lambda g: len(g) == 3)\n    return out, aov, full\n\n\ndef split_plot(full):\n    # between factor age, within factor bin, subject mouse\n    gm = full.r.mean()\n    a_levels, b_levels = full.age.unique(), BIN_NAMES\n    ss_age = sum(len(g) * (g.r.mean() - gm) ** 2 for _, g in full.groupby(\"age\"))\n    ss_subj = sum(3 * (g.r.mean() - gm) ** 2 for _, g in full.groupby(\"mouse\"))\n    ss_bin = sum(len(g) * (g.r.mean() - gm) ** 2 for _, g in full.groupby(\"bin\"))\n    ss_cells = sum(len(g) * (g.r.mean() - gm) ** 2 for _, g in full.groupby([\"age\", \"bin\"]))\n    ss_ab = ss_cells - ss_age - ss_bin\n    ss_tot = ((full.r - gm) ** 2).sum()\n    n_subj = full.mouse.nunique()\n    df_age, df_sw = len(a_levels) - 1, n_subj - len(a_levels)\n    ss_sw = ss_subj - ss_age\n    ss_err = ss_tot - ss_subj - ss_bin - ss_ab\n    df_bin, df_ab, df_err = 2, 2 * df_age, 2 * df_sw\n    f_age = (ss_age / df_age) / (ss_sw / df_sw)\n    f_bin = (ss_bin / df_bin) / (ss_err / df_err)\n    f_ab = (ss_ab / df_ab) / (ss_err / df_err)\n    return pd.DataFrame({\"F\": [f_age, f_bin, f_ab], \"df1\": [df_age, df_bin, df_ab], \"df2\": [df_sw, df_err, df_err],\n                         \"p\": [stats.f.sf(f_age, df_age, df_sw), stats.f.sf(f_bin, df_bin, df_err), stats.f.sf(f_ab, df_ab, df_err)]},\n                        index=[\"age\", \"bin\", \"age x bin\"])\n\n\ndef judge_1d(out, col):\n    within_tol = all(within(d, e, t) for d, e, t in zip(out.difference, EXP_1D, TOL_1D))\n    p_ok = out[col].iloc[0] < 0.05 and out[col].iloc[1] < 0.05 and out[col].iloc[2] >= 0.05\n    falls = out.difference.iloc[0] > out.difference.iloc[1] > out.difference.iloc[2]\n    return within_tol, p_ok, falls\n\n\nfor meas in [\"xcorr0\", \"spearman\"]:\n    out, aov, full = fig1d(meas)\n    print(f\"=== measure {meas}\" + (\" (variant only)\" if meas == \"spearman\" else \" (reading C-b)\"))\n    print(out.round(4).to_string(index=False))\n    print(\"expected differences\", EXP_1D, \"+/-\", TOL_1D)\n    print(\"A-a two-way ANOVA:\\n\", aov.round(4).to_string())\n    print(f\"A-b split-plot ANOVA on {full.mouse.nunique()} mice with pairs in all three bins:\\n\", split_plot(full).round(4).to_string())\n    for col in [\"p_bonf_A-a\", \"p_bonf_A-b\"]:\n        w, p, f = judge_1d(out, col)\n        print(f\"{col}: differences within tolerance {w}; first two p < 0.05 and third not {p}; falls with distance {f}\")\n\"\"\", [\"claim:fig1d-distance-dependent-decorrelation\"])\ncode(r\"\"\"\n# Bin edges are fixed by the text; the share of mice without pairs over 200 um, and how the per-bin\n# difference moves when the mice lacking a bin are dropped from every bin.\nd = corr[(corr.measure == \"xcorr0\") & (corr.genotype == \"WT\") & corr.age.isin([\"P9P11\", \"P14P16\"])]\nprint(d[[\"age\", \"index\", \"n_<100\", \"n_100-200\", \"n_>200\", \"<100\", \"100-200\", \">200\"]].round(3).to_string(index=False))\nfull = d.dropna(subset=BIN_NAMES)\nprint(\"Mice with pairs in all bins: P9-11 %d of %d, P14-16 %d of %d\" % (\n    (full.age == \"P9P11\").sum(), (d.age == \"P9P11\").sum(), (full.age == \"P14P16\").sum(), (d.age == \"P14P16\").sum()))\nfor b in BIN_NAMES:\n    print(b, \"difference on those mice: %.4f\" % (full[full.age == \"P9P11\"][b].mean() - full[full.age == \"P14P16\"][b].mean()))\n\"\"\", [\"claim:fig1d-distance-dependent-decorrelation\"])\n\n# ------------------------------------------------------------ fig1e age decrease\nmd(r\"\"\"\n## fig1e-age-decrease\n\n> For cell pairs within 100 um, correlation decreases significantly with age in both WT and Fmr1 -/-\n> mice.\n\nReadings from the criterion: E-a, the 2-df age contrast within each genotype of the unequal-variance\n2 x 3 model; E-b, Welch's one-way ANOVA of age per genotype.\n\"\"\")\ncode(r\"\"\"\ndef age_tests(meas):\n    v = values(meas)\n    m = ssc8.two_by_three(v)\n    rows = []\n    for g in ssc8.GENOTYPES:\n        wa = ssc8.welch_anova([v[(g, a)] for a in ssc8.AGES])\n        rows.append({\"genotype\": g, **{f\"mean_{ssc8.AGE_LABEL[a]}\": v[(g, a)].mean() for a in ssc8.AGES},\n                     \"E-a F\": m[f\"age_within_{g}\"][\"F\"], \"E-a df2\": m[f\"age_within_{g}\"][\"df2\"], \"E-a p\": m[f\"age_within_{g}\"][\"p\"],\n                     \"E-b F\": wa[\"F\"], \"E-b df2\": wa[\"df2\"], \"E-b p\": wa[\"p\"],\n                     \"P9-11 > P30-40\": v[(g, \"P9P11\")].mean() > v[(g, \"P30P40\")].mean()})\n    return pd.DataFrame(rows)\n\n\nfor meas in [\"xcorr0\", \"spearman\"]:\n    print(f\"=== measure {meas}\" + (\" (variant only)\" if meas == \"spearman\" else \" (reading C-b)\"))\n    print(age_tests(meas).round(5).to_string(index=False))\n\"\"\", [\"claim:fig1e-age-decrease\"])\n\n# ------------------------------------------------------------ genotype pooled\nmd(r\"\"\"\n## genotype-pooled-ages\n\n> Pooling all ages, correlation coefficients are higher in Fmr1 -/- than WT mice (0.265 +/- 0.009\n> against 0.230 +/- 0.008, p = 0.0057).\n\nReadings from the criterion: pairs P-a (under 100 um) and P-b (all pairs); pooled average M-a (mean\nover all mice of a genotype, s.e.m. over mice) and M-b (mean of the three age means, s.e.m. from the\nthree age s.e.m.s). The test is the genotype main effect of the unequal-variance 2 x 3 model,\nwhich is the same under M-a and M-b.\n\"\"\")\ncode(r\"\"\"\ndef pooled(meas, exp, tol):\n    rows = []\n    for pairs, col in [(\"P-a (<100 um)\", \"<100\"), (\"P-b (all pairs)\", \"all\")]:\n        v = values(meas, col)\n        test = ssc8.two_by_three(v)[\"genotype\"]\n        for avg in [\"M-a\", \"M-b\"]:\n            r = {\"pairs\": pairs, \"average\": avg}\n            for g in ssc8.GENOTYPES:\n                if avg == \"M-a\":\n                    x = np.concatenate([v[(g, a)] for a in ssc8.AGES])\n                    r[f\"{g}_mean\"], r[f\"{g}_sem\"] = x.mean(), ssc8.sem(x)\n                else:\n                    r[f\"{g}_mean\"] = np.mean([v[(g, a)].mean() for a in ssc8.AGES])\n                    r[f\"{g}_sem\"] = np.sqrt(sum(ssc8.sem(v[(g, a)]) ** 2 for a in ssc8.AGES)) / 3\n            r[\"F\"], r[\"df2\"], r[\"p\"] = test[\"F\"], test[\"df2\"], test[\"p\"]\n            r[\"KO higher\"] = r[\"KO_mean\"] > r[\"WT_mean\"]\n            r[\"WT within\"] = within(r[\"WT_mean\"], exp[\"WT\"], tol[\"WT\"])\n            r[\"KO within\"] = within(r[\"KO_mean\"], exp[\"KO\"], tol[\"KO\"])\n            rows.append(r)\n    return pd.DataFrame(rows)\n\n\nEXP_POOL, TOL_POOL = {\"WT\": 0.230, \"KO\": 0.265}, {\"WT\": 0.008, \"KO\": 0.009}\nfor meas in [\"xcorr0\", \"spearman\"]:\n    print(f\"=== measure {meas}\" + (\" (variant only)\" if meas == \"spearman\" else \" (reading C-b)\"))\n    print(pooled(meas, EXP_POOL, TOL_POOL).round(4).to_string(index=False))\nprint(\"expected WT 0.230 +/- 0.008, KO 0.265 +/- 0.009\")\n\"\"\", [\"claim:genotype-pooled-ages\"])\n\nmd(r\"\"\"\n## pearson-genotype\n\n> With Pearson correlation, pooled over ages, coefficients are again higher in Fmr1 -/- than WT mice\n> (0.196 +/- 0.010 against 0.164 +/- 0.009, p = 0.026).\n\nAs genotype-pooled-ages, with the zero-lag Pearson correlation.\n\"\"\")\ncode(r\"\"\"\nEXP_PEAR, TOL_PEAR = {\"WT\": 0.164, \"KO\": 0.196}, {\"WT\": 0.009, \"KO\": 0.010}\nprint(pooled(\"pearson\", EXP_PEAR, TOL_PEAR).round(4).to_string(index=False))\nprint(\"expected WT 0.164 +/- 0.009, KO 0.196 +/- 0.010\")\nv = values(\"pearson\")\nprint(\"Pearson, pairs under 100 um, per group:\", {f\"{g} {ssc8.AGE_LABEL[a]}\": round(v[(g, a)].mean(), 3) for g, a in ssc8.GROUPS})\n\"\"\", [\"claim:pearson-genotype\"])\n\n# ------------------------------------------------------------ P14-16 difference\nmd(r\"\"\"\n## fig1ef-p14-16-difference\n\n> The genotype difference is largest at P14-16, where correlation is 0.210 +/- 0.011 in Fmr1 -/-\n> against 0.172 +/- 0.012 in WT mice (p = 0.032).\n\nPairs under 100 um, mouse means, unpaired two-tailed Student's t-test (Online Methods, Statistical\nAnalyses). The KO minus WT difference is printed for every age.\n\"\"\")\ncode(r\"\"\"\ndef per_age(meas, col=\"<100\"):\n    v = values(meas, col)\n    rows = []\n    for a in ssc8.AGES:\n        w, k = v[(\"WT\", a)], v[(\"KO\", a)]\n        rows.append({\"age\": ssc8.AGE_LABEL[a], \"n_WT\": len(w), \"WT\": w.mean(), \"WT_sem\": ssc8.sem(w),\n                     \"n_KO\": len(k), \"KO\": k.mean(), \"KO_sem\": ssc8.sem(k), \"KO-WT\": k.mean() - w.mean(),\n                     \"t\": stats.ttest_ind(k, w).statistic, \"p_student\": stats.ttest_ind(k, w).pvalue,\n                     \"p_welch\": stats.ttest_ind(k, w, equal_var=False).pvalue})\n    return pd.DataFrame(rows)\n\n\nfor meas in [\"xcorr0\", \"spearman\"]:\n    print(f\"=== measure {meas}\" + (\" (variant only)\" if meas == \"spearman\" else \" (reading C-b)\"))\n    t = per_age(meas)\n    print(t.round(4).to_string(index=False))\n    p14 = t[t.age == \"P14-16\"].iloc[0]\n    print(\"P14-16 WT within 0.172 +/- 0.012:\", within(p14.WT, 0.172, 0.012), \"; KO within 0.210 +/- 0.011:\", within(p14.KO, 0.210, 0.011),\n          \"; p < 0.05:\", p14.p_student < 0.05, \"; KO higher:\", p14.KO > p14.WT,\n          \"; P14-16 difference largest:\", bool(p14[\"KO-WT\"] > t[t.age != \"P14-16\"][\"KO-WT\"].max()))\n\"\"\", [\"claim:fig1ef-p14-16-difference\"])\n\nmd(r\"\"\"\n## p30-40-no-difference\n\n> By P30-40 the genotype difference in correlation has decreased and is not significant (0.144 +/-\n> 0.008 in Fmr1 -/- against 0.123 +/- 0.008 in WT, p = 0.075).\n\nA claim of absence, judged on the unpaired two-tailed t-test at alpha 0.05, under reading C-b (the\nreading of fig1ef-p14-16-difference, the only one here that can decide).\n\"\"\")\ncode(r\"\"\"\nfor meas in [\"xcorr0\", \"spearman\"]:\n    t = per_age(meas)\n    p30 = t[t.age == \"P30-40\"].iloc[0]\n    print(f\"{meas}: WT {p30.WT:.4f} +/- {p30.WT_sem:.4f} (n {p30.n_WT}), KO {p30.KO:.4f} +/- {p30.KO_sem:.4f} (n {p30.n_KO}), \"\n          f\"KO-WT {p30['KO-WT']:.4f}, Student p = {p30.p_student:.4f}, Welch p = {p30.p_welch:.4f}; \"\n          f\"WT within 0.123 +/- 0.008: {within(p30.WT, 0.123, 0.008)}, KO within 0.144 +/- 0.008: {within(p30.KO, 0.144, 0.008)}\")\nd = corr[(corr.measure == \"xcorr0\") & (corr.age == \"P30P40\")]\nprint(\"\\nP30-40 mouse values, xcorr0, pairs under 100 um:\")\nprint(d[[\"genotype\", \"index\", \"<100\", \"n_<100\"]].round(4).to_string(index=False))\n\"\"\", [\"claim:p30-40-no-difference\"])\n\n# ------------------------------------------------------------ peaks of synchrony\nmd(r\"\"\"\n## fig2b-peak-frequency\n\n> The frequency of peaks of synchrony at P14-16 is slightly but not significantly higher in Fmr1 -/-\n> mice (0.060 +/- 0.007 against 0.053 +/- 0.006 peaks per s, p = 0.45).\n\nPeaks of synchrony as the Online Methods define them, under the readings of the criterion: active\nR-a (rate above 0) or R-b (at least one estimated spike in the frame, rate / 3.9 >= 1); shuffle S-a\n(permutation of a trace's frames) or S-b (circular shift). Both shuffles keep each cell's mean\nrate. Frequency is events over the recording's duration at 3.9 Hz (4 Hz as a variant). A claim of\nabsence: unpaired two-tailed t-test at alpha 0.05 on the data set's P14-16 mice (8 WT, 10 KO).\nEach reading has its own seeded generator.\n\"\"\")\ncode(r\"\"\"\nREADINGS = [(r, s) for r in [\"R-a\", \"R-b\"] for s in [\"S-a\", \"S-b\"]]\nev_rows = []\nfor k, (rule, how) in enumerate(READINGS):\n    rng = np.random.default_rng(2013 + k)\n    for g in ssc8.GENOTYPES:\n        for i, r in enumerate(data[(g, \"P14P16\")]):\n            e = ssc8.synchrony_events(r[\"rates\"], rule, how, rng)\n            ev_rows.append({\"rule\": rule, \"shuffle\": how, \"genotype\": g, \"index\": i, **e})\nev = pd.DataFrame(ev_rows)\nprint(ev[(ev[\"rule\"] == \"R-a\") & (ev.shuffle == \"S-a\")][[\"genotype\", \"index\", \"frames\", \"threshold\", \"n_events\", \"rate_per_s\", \"Q-a\", \"Q-b\"]].round(4).to_string(index=False))\nrows = []\nfor (rule, how), d in ev.groupby([\"rule\", \"shuffle\"]):\n    w, k = d[d.genotype == \"WT\"], d[d.genotype == \"KO\"]\n    for col in [\"rate_per_s\", \"rate_per_s_4hz\"]:\n        rows.append({\"rule\": rule, \"shuffle\": how, \"measure\": col, \"WT\": w[col].mean(), \"WT_sem\": ssc8.sem(w[col]),\n                     \"KO\": k[col].mean(), \"KO_sem\": ssc8.sem(k[col]), \"p_student\": stats.ttest_ind(k[col], w[col]).pvalue,\n                     \"WT within\": within(w[col].mean(), 0.053, 0.006), \"KO within\": within(k[col].mean(), 0.060, 0.007),\n                     \"threshold_range\": f\"{d.threshold.min():.1f}-{d.threshold.max():.1f}%\", \"mice_without_events\": int((d.n_events == 0).sum())})\nfb = pd.DataFrame(rows)\nprint(\"\\nexpected KO 0.060 +/- 0.007, WT 0.053 +/- 0.006 peaks per s\")\nprint(fb.round(4).to_string(index=False))\nprint(\"Range of per-mouse frequencies, all readings: %.4f to %.4f per s\" % (ev.rate_per_s.min(), ev.rate_per_s.max()))\n\"\"\", [\"claim:fig2b-peak-frequency\"])\n\nmd(r\"\"\"\n## fig2c-participation\n\n> At P14-16 a higher proportion of neurons participates in peaks of synchrony in Fmr1 -/- than in WT\n> mice (0.380 +/- 0.023 against 0.300 +/- 0.017, p = 0.023).\n\nEvents as in fig2b-peak-frequency, under its readings R and S; proportion Q-a (per event, the fraction\nof the mouse's cells active in any frame of the event, averaged over events) or Q-b (the fraction of\nthe mouse's cells active in at least one event). Unpaired two-tailed t-test. Mice without events\nhave no Q-a and are dropped, and counted.\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor (rule, how), d in ev.groupby([\"rule\", \"shuffle\"]):\n    for q in [\"Q-a\", \"Q-b\"]:\n        w, k = d[d.genotype == \"WT\"][q].dropna(), d[d.genotype == \"KO\"][q].dropna()\n        rows.append({\"rule\": rule, \"shuffle\": how, \"measure\": q, \"n_WT\": len(w), \"WT\": w.mean(), \"WT_sem\": ssc8.sem(w),\n                     \"n_KO\": len(k), \"KO\": k.mean(), \"KO_sem\": ssc8.sem(k), \"p_student\": stats.ttest_ind(k, w).pvalue,\n                     \"KO higher\": k.mean() > w.mean(), \"WT within\": within(w.mean(), 0.300, 0.017),\n                     \"KO within\": within(k.mean(), 0.380, 0.023)})\nfc = pd.DataFrame(rows)\nprint(\"expected KO 0.380 +/- 0.023, WT 0.300 +/- 0.017\")\nprint(fc.round(4).to_string(index=False))\n# How the per-event participation depends on the event size: the mean percent active in all frames.\nprint(\"\\nMean percent of cells active per frame, R-a: WT %.1f%%, KO %.1f%%\" % (\n    ev[(ev[\"rule\"] == \"R-a\") & (ev.genotype == \"WT\")].mean_pct_active.mean(), ev[(ev[\"rule\"] == \"R-a\") & (ev.genotype == \"KO\")].mean_pct_active.mean()))\n\"\"\", [\"claim:fig2c-participation\"])\n\n# ------------------------------------------------------------ firing rates\nmd(r\"\"\"\n## imaging-firing-rate-no-genotype-difference\n\n> Firing rates extrapolated from the calcium imaging by deconvolution do not differ between genotypes\n> at any age.\n\nPer mouse, the mean over cells of each cell's mean estimated rate; unpaired two-tailed t-test per age\nat alpha 0.05 (criterion). Reading U-a takes the rates as Hz; U-b as per frame (times 3.9), which\nscales both groups alike and leaves the tests unchanged.\n\"\"\")\ncode(r\"\"\"\nfr = pd.DataFrame([{\"genotype\": g, \"age\": a, \"index\": i, \"rate_Hz\": r[\"rates\"].mean(1).mean() if False else r[\"rates\"].mean(0).mean()}\n                   for g, a in ssc8.GROUPS for i, r in enumerate(data[(g, a)])])\nrows = []\nfor a in ssc8.AGES:\n    w, k = fr[(fr.genotype == \"WT\") & (fr.age == a)].rate_Hz, fr[(fr.genotype == \"KO\") & (fr.age == a)].rate_Hz\n    rows.append({\"age\": ssc8.AGE_LABEL[a], \"n_WT\": len(w), \"WT_U-a\": w.mean(), \"WT_sem\": ssc8.sem(w), \"n_KO\": len(k),\n                 \"KO_U-a\": k.mean(), \"KO_sem\": ssc8.sem(k), \"KO-WT\": k.mean() - w.mean(),\n                 \"WT_U-b\": 3.9 * w.mean(), \"KO_U-b\": 3.9 * k.mean(),\n                 \"p_student\": stats.ttest_ind(k, w).pvalue, \"p_welch\": stats.ttest_ind(k, w, equal_var=False).pvalue})\nrates_by_age = pd.DataFrame(rows)\nprint(rates_by_age.round(4).to_string(index=False))\nprint(\"Range of mouse rates: %.3f to %.3f Hz (U-a)\" % (fr.rate_Hz.min(), fr.rate_Hz.max()))\nprint(\"Ages with p < 0.05:\", rates_by_age[rates_by_age.p_student < 0.05].age.tolist())\n\"\"\", [\"claim:imaging-firing-rate-no-genotype-difference\"])\n\nmd(r\"\"\"\n## unanesthetized-p14-16-values\n\n> In unanesthetized P14-16 mice the extrapolated firing rate is 0.30 +/- 0.03 Hz in WT and 0.29 +/-\n> 0.03 Hz in Fmr1 -/- mice, and the correlation of pairs within 100 um is 0.17 +/- 0.01 in WT mice.\n\nThe unanesthetized groups of Fig. 6 are read as the P14-16 mice (criterion).\n\"\"\")\ncode(r\"\"\"\np14 = rates_by_age[rates_by_age.age == \"P14-16\"].iloc[0]\nc14 = per_age(\"xcorr0\")\nc14 = c14[c14.age == \"P14-16\"].iloc[0]\ns14 = per_age(\"spearman\")\ns14 = s14[s14.age == \"P14-16\"].iloc[0]\nfor unit, wt, ko in [(\"U-a (Hz)\", p14[\"WT_U-a\"], p14[\"KO_U-a\"]), (\"U-b (per frame x 3.9)\", p14[\"WT_U-b\"], p14[\"KO_U-b\"])]:\n    print(f\"{unit}: WT {wt:.3f} (0.30 +/- 0.03: {within(wt, 0.30, 0.03)}), KO {ko:.3f} (0.29 +/- 0.03: {within(ko, 0.29, 0.03)})\")\nprint(f\"s.e.m. of rates (U-a): WT {p14.WT_sem:.3f}, KO {p14.KO_sem:.3f}; n WT {p14.n_WT}, KO {p14.n_KO}\")\nprint(f\"WT correlation, pairs under 100 um, xcorr0: {c14.WT:.4f} +/- {c14.WT_sem:.4f} (0.17 +/- 0.01: {within(c14.WT, 0.17, 0.01)}); \"\n      f\"Spearman variant {s14.WT:.4f}\")\n\"\"\", [\"claim:unanesthetized-p14-16-values\"])\n\n# ------------------------------------------------------------ suppl4a variant\nmd(r\"\"\"\n## Variant for suppl4a-firing-vs-correlation (blocked)\n\nThe claim uses the 3-min recordings of the EEG subset (13 WT and 10 KO recordings), which the data set\ndoes not identify, and it holds no EEG. The outcome is blocked. As a variant only, the P14-16\nrecordings of 2160 frames are cut at multiples of 720 frames (one 3-min movie each, as the data\ncheck suggests), and each segment's mean rate is regressed on its mean correlation of pairs under\n100 um (xcorr0). Segments of one mouse are not independent, so the F-test p is optimistic.\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor g in ssc8.GENOTYPES:\n    for i, r in enumerate(data[(g, \"P14P16\")]):\n        x = r[\"rates\"]\n        for s in range(x.shape[0] // 720):\n            seg = {\"rates\": x[720 * s:720 * (s + 1)], \"dist\": r[\"dist\"]}\n            m = ssc8.mouse_pair_means(seg, \"xcorr0\")\n            rows.append({\"genotype\": g, \"mouse\": i, \"segment\": s, \"rate\": seg[\"rates\"].mean(), \"corr\": m[\"<100\"]})\nseg = pd.DataFrame(rows).dropna()\nfor g in ssc8.GENOTYPES:\n    d = seg[seg.genotype == g]\n    lr = stats.linregress(d.rate, d[\"corr\"])\n    print(f\"{g}: {len(d)} segments from {d.mouse.nunique()} mice, r2 = {lr.rvalue ** 2:.3f}, slope {lr.slope:.3f}, p = {lr.pvalue:.4f}\")\n\"\"\", [\"variant:suppl4a-firing-vs-correlation\"])\n\nmd(r\"\"\"\n## Summary\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Notebook run time: {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/crcns-ssc-8-goncalves-2013/reproduce_goncalves_2013.ipynb\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/"rate_Hz": r\["rates"\].mean(1).mean() if False else r\["rates"\].mean(0).mean()}/"rate_Hz": r["rates"].mean(0).mean()}/' $TMPDIR/build_nb.py && grep -n '"rate_Hz": r' $TMPDIR/build_nb.py && $TMPDIR/venv/bin/python $TMPDIR/build_nb.py && $TMPDIR/venv/bin/python -m ipykernel install --user --name ssc8dev >/dev/null 2>&1; date -u; time $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1800 --ExecutePreprocessor.kernel_name=ssc8dev reproduce_goncalves_2013.ipynb --output $TMPDIR/dev.ipynb 2>&1 | tail -5
```

```
608:fr = pd.DataFrame([{"genotype": g, "age": a, "index": i, "rate_Hz": r["rates"].mean(0).mean()}
Sun Nov  8 08:35:22 UTC 2026
[NbConvertApp] Converting notebook reproduce_goncalves_2013.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 93532 bytes to /tmp/claude-1001/dev.ipynb

real	4m51.857s
user	1m34.968s
sys	0m19.186s
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
nb=json.load(open('/tmp/claude-1001/dev.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[])) or ''.join(o.get('traceback',[]))
        print(f'--- cell {i}', c['metadata'].get('tags'))
        print(t[:6000])
EOF
```

```
--- cell 1 None
data set ssc-8 (unversioned, doi:10.6080/K0X63K3X)
firingrates_and_distances.mat MD5 ae1b48123540ecfd1bc9675c1eaa9a3d matches checksums.md5: True
published MD5 of the TIFF archive: 75bf460dbe90c625637d1a1af3a25ca3

--- cell 1 None
streamed the TIFF archive (58 members) in 258 s

--- cell 3 ['sanity']
Variables in the MAT file: ['KO_P14P16_distances', 'KO_P14P16_movies', 'KO_P30P40_distances', 'KO_P30P40_movies', 'KO_P9P11_distances', 'KO_P9P11_movies', 'WT_P14P16_distances', 'WT_P14P16_movies', 'WT_P30P40_distances', 'WT_P30P40_movies', 'WT_P9P11_distances', 'WT_P9P11_movies']

Mice per group (recordings in the MAT file):
genotype  age   
WT        P9-11     13
          P14-16     8
          P30-40     7
KO        P9-11      9
          P14-16    10
          P30-40     6

[... 355 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 900 $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,'entries/crcns-ssc-8-goncalves-2013')
import ssc8, pickle, numpy as np
mv=ssc8.survey_movies()
pickle.dump([{k:v for k,v in m.items()} for m in mv], open('movies.pkl','wb'))
EOF
ls -la $TMPDIR/movies.pkl; date -u
```

```
-rw-r--r-- 1 runner runner 870606 Nov  8 08:43 /tmp/claude-1001/movies.pkl
Sun Nov  8 08:43:50 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ssc-8-goncalves-2013 && $TMPDIR/venv/bin/python - <<'EOF'
import ssc8, pickle, numpy as np
from scipy.ndimage import median_filter
mv=pickle.load(open('/tmp/claude-1001/movies.pkl','rb'))
data,_,_=ssc8.load_mat()
inv={v:k for k,v in ssc8.TIFF_FOLDER.items()}
fm={}
for m in mv:
    if m['tiff']: fm[(inv[m['folder']], int(m['name'].split('_')[1].split('.')[0])-1)]=m['frame_mean']
def hp(x): return x-median_filter(x,41,mode='nearest')
bad=0
for g,recs in data.items():
    for i,r in enumerate(recs):
        pop=r['rates'].mean(1); f=hp(fm[(g,i)])
        own=np.corrcoef(pop,f)[0,1]
        oth=[]
        for (g2,j),f2 in fm.items():
            if (g2,j)==(g,i): continue
            n=min(len(pop),len(f2)); oth.append(np.corrcoef(pop[:n],hp(f2)[:n])[0,1])
        lc=[np.corrcoef(np.roll(pop,l)[5:-5],f[5:-5])[0,1] for l in range(-5,6)]
        if own<=max(oth) or i in (3,0): print(g,i,'own %.2f max other (all 53) %.2f'%(own,max(oth)), 'bestlag',np.argmax(lc)-5)
        bad+= own<=max(oth)
print('bad',bad)
EOF
```

```
('WT', 'P9P11') 0 own 0.63 max other (all 53) 0.13 bestlag 2
('WT', 'P9P11') 3 own 0.62 max other (all 53) 0.18 bestlag 2
('WT', 'P14P16') 0 own 0.29 max other (all 53) 0.12 bestlag 1
('WT', 'P14P16') 3 own 0.37 max other (all 53) 0.13 bestlag 2
('WT', 'P30P40') 0 own 0.34 max other (all 53) 0.23 bestlag 1
('WT', 'P30P40') 3 own 0.15 max other (all 53) 0.10 bestlag 2
('KO', 'P9P11') 0 own 0.80 max other (all 53) 0.10 bestlag 2
('KO', 'P9P11') 3 own 0.59 max other (all 53) 0.16 bestlag 2
('KO', 'P14P16') 0 own 0.52 max other (all 53) 0.16 bestlag 2
('KO', 'P14P16') 3 own 0.52 max other (all 53) 0.30 bestlag 2
('KO', 'P30P40') 0 own 0.15 max other (all 53) 0.15 bestlag 1
('KO', 'P30P40') 3 own 0.35 max other (all 53) 0.10 bestlag 2
bad 0
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb.py').read()
s=s.replace('pd.set_option("display.max_rows", 200)\n','pd.set_option("display.max_rows", 200)\npd.set_option("display.float_format", "{:.4g}".format)\n')
import re
s=re.sub(r'\.round\(\d\)\.to_string', '.to_string', s)
old_start=s.index('# Do the rates share the movies\' clock?')
old_end=s.index('""", ["sanity"])', old_start)
new='''# Do the rates share the movies' clock? Per recording, the correlation of the population rate (mean
# over cells) with the movie's mean frame brightness, high-passed by subtracting a 41-frame running
# median (a standard choice, to remove bleaching and drift), at lags of -5 to +5 frames; against
# every other movie of the data set at lag 0 (the wrong movie); and against its own movie with the
# rate shifted by 50 to 400 frames (shifted labels).
from scipy.ndimage import median_filter


def highpass(x):
    return x - median_filter(x, 41, mode="nearest")


folder_group = {v: k for k, v in ssc8.TIFF_FOLDER.items()}
bright = {(folder_group[m["folder"]], int(m["name"].split("_")[1].split(".")[0]) - 1): highpass(m["frame_mean"])
          for m in movies if m["tiff"]}
lags = np.arange(-5, 6)
clock = []
for (g, a), recs in data.items():
    for i, r in enumerate(recs):
        fm = bright[((g, a), i)]
        pop = r["rates"].mean(1)
        lc = [np.corrcoef(np.roll(pop, l)[5:-5], fm[5:-5])[0, 1] for l in lags]
        others = []
        for key, f2 in bright.items():
            if key != ((g, a), i):
                n = min(len(pop), len(f2))
                others.append(np.corrcoef(pop[:n], f2[:n])[0, 1])
        shifted = [np.corrcoef(np.roll(pop, s), fm)[0, 1] for s in range(50, 401, 50)]
        # concatenation boundaries every 720 frames: brightness step there against elsewhere
        step = np.abs(np.diff(r_fm := next(m["frame_mean"] for m in movies if m["tiff"] and folder_group[m["folder"]] == (g, a)
                                          and m["name"] == f"Movie_{i + 1}.tif")))
        bnd = [k - 1 for k in range(720, len(r_fm), 720)]
        clock.append({"genotype": g, "age": ssc8.AGE_LABEL[a], "index": i, "r_lag0": lc[5],
                      "best_lag": int(lags[np.argmax(lc)]), "r_best": max(lc),
                      "max_r_other_movie": max(others), "max_abs_r_shifted": max(np.abs(shifted)),
                      "step_at_720k_over_median": np.median(step[bnd]) / np.median(step) if bnd else np.nan})
clock = pd.DataFrame(clock)
print(clock.to_string(index=False))
print("\\nOwn movie, lag 0: r = %.2f to %.2f (median %.2f); other movies: up to %.2f; own movie with shifted rates: up to %.2f"
      % (clock.r_lag0.min(), clock.r_lag0.max(), clock.r_lag0.median(), clock.max_r_other_movie.max(), clock.max_abs_r_shifted.max()))
print("Recordings whose own movie beats every one of the 52 other movies at lag 0:",
      int((clock.r_lag0 > clock.max_r_other_movie).sum()), "of", len(clock))
print("Recordings whose lag-0 correlation beats every shifted one:", int((clock.r_lag0 > clock.max_abs_r_shifted).sum()), "of", len(clock))
print("Lag (frames, + = brightness after the rate) of the best correlation:", clock.best_lag.value_counts().sort_index().to_dict())
print("Median ratio of the brightness step at frames 720k to the median step: %.1f" % clock.step_at_720k_over_median.median())
'''
s=s[:old_start]+new+s[old_end:]
s=s.replace('folder_group = {v: k for k, v in ssc8.TIFF_FOLDER.items()}\ntifs["genotype"]','tifs["genotype"]')
s=s.replace('mv = pd.DataFrame(','folder_group = {v: k for k, v in ssc8.TIFF_FOLDER.items()}\nmv = pd.DataFrame(')
open('build_nb.py','w').write(s)
EOF
grep -n "Each matrix correlates far better" build_nb.py
```

```
235:the spikes it is deconvolved from. Each matrix correlates far better with its own movie than with
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb.py').read()
s=s.replace('''bright = {(folder_group[m["folder"]], int(m["name"].split("_")[1].split(".")[0]) - 1): highpass(m["frame_mean"])
          for m in movies if m["tiff"]}''','''raw = {(folder_group[m["folder"]], int(m["name"].split("_")[1].split(".")[0]) - 1): m["frame_mean"]
       for m in movies if m["tiff"]}
bright = {k: highpass(v) for k, v in raw.items()}''')
s=s.replace('''        step = np.abs(np.diff(r_fm := next(m["frame_mean"] for m in movies if m["tiff"] and folder_group[m["folder"]] == (g, a)
                                          and m["name"] == f"Movie_{i + 1}.tif")))
        bnd = [k - 1 for k in range(720, len(r_fm), 720)]''','''        step = np.abs(np.diff(raw[((g, a), i)]))
        bnd = [k - 1 for k in range(720, len(step) + 1, 720)]''')
open('build_nb.py','w').write(s)
EOF
sed -n 225,245p build_nb.py
```

```
print("Recordings whose lag-0 correlation beats every shifted one:", int((clock.r_lag0 > clock.max_abs_r_shifted).sum()), "of", len(clock))
print("Lag (frames, + = brightness after the rate) of the best correlation:", clock.best_lag.value_counts().sort_index().to_dict())
print("Median ratio of the brightness step at frames 720k to the median step: %.1f" % clock.step_at_720k_over_median.median())
""", ["sanity"])

md(r"""
The movies are named for the groups, one folder each (the folders are named "4Hz", where the
Methods and the descriptor give 3.9 Hz). Each movie `Movie_k.tif` has exactly as many frames as
the k-th rate matrix of its group, and the population rate follows the movie's brightness, with
the best correlation when the brightness lags the rate by a few frames, as a calcium signal lags
the spikes it is deconvolved from. Each matrix correlates far better with its own movie than with
any other of its group. So the rate matrices and the movies share one frame clock, and the k-th
entry of each group is `Movie_k.tif`. Frames are 128 x 256 pixels in most movies, where the
Methods give 512 x 128 at 3.9 Hz. Most recordings are 2160 frames, three times 720, which at
4 Hz is three 3-min movies, consistent with the Methods' "several 3-min calcium movies were
concatenated"; the brightness step at multiples of 720 frames is printed above. No movie or
cell trace is deposited twice. The absolute frame rate cannot be checked from the files, as
the TIFFs carry no time stamps; 3.9 Hz is used, with 4 Hz as a variant where a rate per second is
computed.
""")
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results.py <<'PYEOF'
R = {
"fig1d-distance-dependent-decorrelation": r"""
**Result: partially reproduced.** In WT mice the drop in correlation from P9-11 (13 mice) to P14-16
(8 mice) is largest for pairs under 100 um and falls with distance: 0.191, 0.105 and 0.025 under
the main reading (C-b), with Bonferroni p below 0.05 for the first two bins and 1.0 for the third,
under both ANOVA readings. The pattern and the significance of the paper hold, but all three
differences are below the paper's (0.223, 0.159, 0.067) and outside the 10% tolerance; the
Spearman variant gives 0.175, 0.108 and 0.051, also outside. Only 4 of the 8 P14-16 mice have pairs
over 200 um, and one P9-11 mouse has none.
""",
"fig1e-age-decrease": r"""
**Result: reproduced.** For pairs under 100 um correlation falls with age in both genotypes, from
0.360 to 0.169 to 0.119 in WT and from 0.421 to 0.204 to 0.134 in KO (C-b). The age contrast of the
unequal-variance model gives F = 52.5 (WT) and 64.3 (KO), p far below 0.01 in both; Welch's one-way
ANOVA gives the same values, as the two tests coincide for a one-way design. The Spearman variant
agrees.
""",
"genotype-pooled-ages": r"""
**Result: partially reproduced.** The genotype main effect of the unequal-variance 2 x 3 model is
significant with KO higher: p = 0.0064 for pairs under 100 um (paper 0.0057) and 0.0028 for all
pairs. No reading puts both pooled means within the paper's s.e.m.: pairs under 100 um averaged
over mice give WT 0.245 and KO 0.265 (KO within, WT not); all pairs over mice give WT 0.223 and KO
0.251 (WT within, KO not); the mean of the age means gives WT 0.216 and KO 0.253 (under 100 um),
whose s.e.m.s (0.0088 and 0.0093) are close to the paper's (0.008 and 0.009).
""",
"pearson-genotype": r"""
**Result: partially reproduced.** With Pearson correlation the genotype effect is significant with
KO higher: p = 0.023 for pairs under 100 um (paper 0.026) and 0.012 for all pairs. No reading puts
both means within the paper's s.e.m.: under 100 um over mice WT 0.179 and KO 0.193 (KO within);
all pairs over mice WT 0.155 and KO 0.178 (WT within); the means of the age means are 0.146 and
0.180 (under 100 um), with s.e.m.s 0.0092 and 0.0107, close to the paper's 0.009 and 0.010.
""",
"fig1ef-p14-16-difference": r"""
**Result: not reproduced.** At P14-16 the means match the paper (WT 0.169 +/- 0.010, 8 mice; KO 0.204
+/- 0.013, 10 mice; tolerances 0.172 +/- 0.012 and 0.210 +/- 0.011), and KO is higher, but the
unpaired Student's t-test gives p = 0.057, above 0.05 (Welch's test, not the Methods' test, gives
0.049). The KO minus WT difference is 0.062 at P9-11, 0.035 at P14-16 and 0.015 at P30-40, so it is
not largest at P14-16. The Spearman variant gives p = 0.058 at P14-16.
""",
"p30-40-no-difference": r"""
**Result: reproduced.** At P30-40 the t-test finds no genotype difference: KO 0.134 +/- 0.011 (6 mice)
against WT 0.119 +/- 0.005 (7 mice), difference 0.015, p = 0.22. WT is within the paper's s.e.m.
(0.123 +/- 0.008); KO is below it (0.144 +/- 0.008).
""",
"fig2b-peak-frequency": r"""
**Result: reproduced.** At P14-16 the frequency of peaks of synchrony does not differ between
genotypes under any of the four readings (p = 0.13 to 0.64). Under R-a, the reading of "active" that
gives the paper's values, both means are within the paper's s.e.m. with either shuffle: S-a gives
KO 0.060 +/- 0.006 and WT 0.054 +/- 0.007 per s (p = 0.52), S-b KO 0.061 and WT 0.057 (p = 0.64).
Under R-b events are rarer (0.016 to 0.027 per s) and outside the tolerances. A 4 Hz frame rate
changes the frequencies by 2.6% and not the tests.
""",
"fig2c-participation": r"""
**Result: not reproduced.** No reading gives a significant genotype difference in the proportion of
neurons in peaks of synchrony (p = 0.15 to 0.37). Under R-a and Q-a KO is higher (0.444 against
0.411 with S-a, p = 0.25), but both are above the paper's 0.380 and 0.300 and outside their s.e.m.
Under Q-b with R-a nearly every cell takes part in some event (0.998 to 1.0).
""",
"imaging-firing-rate-no-genotype-difference": r"""
**Result: reproduced.** Firing rates do not differ between genotypes at any age: KO minus WT is 0.017
Hz at P9-11 (p = 0.73), 0.0002 Hz at P14-16 (p = 0.997) and 0.014 Hz at P30-40 (p = 0.76).
""",
"unanesthetized-p14-16-values": r"""
**Result: reproduced.** With the rates read as Hz (U-a), the P14-16 firing rate is 0.304 +/- 0.027 Hz
in WT (8 mice) and 0.304 +/- 0.027 Hz in KO (10 mice), within 0.30 +/- 0.03 and 0.29 +/- 0.03, and
the WT correlation of pairs under 100 um is 0.169 +/- 0.010, within 0.17 +/- 0.01. Read as per frame
(U-b) the rates would be 1.19 Hz, far outside.
""",
}
PYEOF
python3 - <<'EOF'
import sys; sys.path.insert(0,'.')
from results import R
s=open('build_nb.py').read()
for cid,txt in R.items():
    anchor=f'""", ["claim:{cid}"])\n'
    k=s.rindex(anchor)+len(anchor)
    s=s[:k]+f'md(r"""{txt}""")\n'+s[k:]
open('build_nb.py','w').write(s)
EOF
grep -c 'Result:' build_nb.py
```

```
11
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb.py').read()
# ratio variant in fig1ef
s=s.replace('''          "; P14-16 difference largest:", bool(p14["KO-WT"] > t[t.age != "P14-16"]["KO-WT"].max()))''','''          "; P14-16 difference largest:", bool(p14["KO-WT"] > t[t.age != "P14-16"]["KO-WT"].max()))
    print("Variant, KO / WT ratio per age:", dict(zip(t.age, (t.KO / t.WT).round(3))))''')
old=s[s.index('The movies are named for the groups, one folder each'):s.index('computed.\n""")', s.index('The movies are named for the groups'))+len('computed.\n')]
new='''The movies are in one folder per group (the folders are named "4Hz", where the Methods and the
descriptor give 3.9 Hz). Each movie `Movie_k.tif` has exactly as many frames as the k-th rate
matrix of its group. The population rate follows the movie's high-passed brightness, best when the
brightness lags the rate by one to three frames, as a calcium signal lags the spikes it is
deconvolved from. Every rate matrix correlates better with its own movie at lag 0 than with any
of the 52 other movies, and than with its own movie when the rates are shifted by 50 to 400 frames
(counts above). So the rate matrices and the movies share one frame clock, and the k-th entry of
each group is `Movie_k.tif`; this is shown for every recording, though the margin is small for
some (KO P30-40 entry 0). Frames are 128 x 256 pixels in 50 movies (one each of 357, 404 and 512
wide), where the Methods give 512 x 128 at 3.9 Hz. Most recordings are 2160 frames, three times
720, which at 4 Hz is three 3-min movies, consistent with the Methods' "several 3-min calcium
movies were concatenated" and with the folder names; the brightness steps at multiples of 720
frames, larger than elsewhere, fit this. The TIFFs carry no time stamps, so the absolute frame rate
cannot be checked; 3.9 Hz (Methods) is used, with 4 Hz as a variant where a rate per second is
computed. No movie or cell trace is deposited twice.
'''
s=s.replace(old,new)
s=s.replace('''md(r"""
## Summary
""")''','''md(r"""
The variant is not the paper's sample and decides nothing: across 3-min segments the KO
regression is positive (r2 = 0.157, p = 0.050) and the WT one flat (r2 = 0.006).

## Summary

| Claim | Outcome |
|---|---|
| group-sizes | not reproduced (13, 8, 7 WT and 9, 10, 6 KO mice against 12, 9, 8 and 9, 10, 8) |
| fig1d-distance-dependent-decorrelation | partially reproduced (pattern and tests hold, differences smaller) |
| fig1e-age-decrease | reproduced |
| genotype-pooled-ages | partially reproduced (p = 0.0064, means not both within s.e.m.) |
| pearson-genotype | partially reproduced (p = 0.023, means not both within s.e.m.) |
| fig1ef-p14-16-difference | not reproduced (means match, Student p = 0.057) |
| p30-40-no-difference | reproduced |
| fig2b-peak-frequency | reproduced |
| fig2c-participation | not reproduced |
| imaging-firing-rate-no-genotype-difference | reproduced |
| unanesthetized-p14-16-values | reproduced |
| seven whole-cell claims | blocked: data missing |
| six EEG claims | blocked: data missing |
| fast-imaging-control | blocked: data missing |
| three isoflurane claims | blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

**How the analysis differs from the paper's.** The data set holds 53 mice, not the paper's 56, in
groups of different sizes (two of six match), so every group statistic is on a different sample.
The trace is the deposited estimated rate; the paper's correlation may have used the filtered dF/F
(reading T-b), which cannot be rebuilt as no cell contours are deposited. The correlation measure
of the paper (its ref. 15) is not given; the zero-lag normalised cross-correlation is the claims
file's reading, and it matches the paper's P14-16 and P30-40 WT values. The way the 2 x 3
unequal-variance ANOVA was fitted is not given; the Welch-James form used here reduces to the
Welch test for one-df contrasts. For peaks of synchrony, what counts as an active cell and how the
traces were shuffled are not given; all four readings were run, and the outcomes do not depend on
them.

**What was found about the data set.** The group sizes differ from the paper's. The descriptor
gives 40 to 149 neurons per animal (the data run to 198) and 7 to 8 min per recording (most are
9.2 min at 3.9 Hz; the range is 3.8 to 15.4 min), and no unit for the estimated rates (they fit
Hz). The movie folders say 4 Hz where the paper and descriptor say 3.9 Hz, and frames are 128 x
256 pixels where the Methods say 512 x 128. The archive carries five macOS resource-fork files.
Movies and rate matrices share their frame clock, and the k-th matrix of each group is
`Movie_k.tif`, which the descriptor does not say. One WT P30-40 cell is silent throughout. No
cell contours or dF/F traces are deposited, nor the EEG, whole-cell, isoflurane or 15.6 Hz data.
""")''')
open('build_nb.py','w').write(s)
EOF
$TMPDIR/venv/bin/python build_nb.py && cd entries/crcns-ssc-8-goncalves-2013 && date -u && $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1800 --ExecutePreprocessor.kernel_name=ssc8dev reproduce_goncalves_2013.ipynb --output $TMPDIR/dev.ipynb 2>&1 | tail -2
```

```
Sun Nov  8 08:45:11 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 104952 bytes to /tmp/claude-1001/dev.ipynb
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
nb=json.load(open('/tmp/claude-1001/dev.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    if i<5: continue
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[])) or ''.join(o.get('traceback',[]))
        print(f'--- cell {i}', c['metadata'].get('tags'))
        print(t[-2500:] if i==6 else t[:3500])
EOF
```

```
--- cell 5 ['sanity']
Archive members: 58 ; TIFF movies: 53 ; other members (not TIFF):
                                              path  bytes              error
                    Ca2+_imaging_TIFFs/._.DS_Store    120 not a classic TIFF
     Ca2+_imaging_TIFFs/WT_P30-P40_4Hz/._.DS_Store    120 not a classic TIFF
   Ca2+_imaging_TIFFs/WT_P30-P40_4Hz/._Movie_1.tif    177 not a classic TIFF
Ca2+_imaging_TIFFs/Fmr1_KO_P30-P40_4Hz/._.DS_Store    120 not a classic TIFF
     Ca2+_imaging_TIFFs/WT_P14-P16_4Hz/._.DS_Store    120 not a classic TIFF

Movies per folder:
folder
Fmr1_KO_P14-P16_4Hz    10
Fmr1_KO_P30-P40_4Hz     6
Fmr1_KO_P9-P11_4Hz      9
WT_P14-P16_4Hz          8
WT_P30-P40_4Hz          7
WT_P9-P11_4Hz          13

Movies matched to a MAT recording by group and number (Movie_k is entry k): {'both': 53, 'left_only': 0, 'right_only': 0}
Frame count of the movie equals the rows of the rate matrix: 53 of 53
[... 272 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" claims/crcns-ssc-8/10.1038-nn.3415.yaml; ls schemas; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:5000])" 2>/dev/null || ls schemas
```

```
28
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "One attempt at reproducing the claims of a target",
"description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
"type": "object",
"additionalProperties": false,
"required": [
"schema_version",
"id",
"dataset",
"paper",
"date",
"provenance",
"outcomes"
],
[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));o=s['properties']['outcomes']['items']['properties']
print(json.dumps({k:v for k,v in o.items() if k not in ('claim','outcome','blocked_by','notes','notebook','output')},indent=0)[:2500]); print(json.dumps(s['properties']['findings'],indent=0)[:1500]); print(list(s['properties']))"
```

```
{
"measured": {
"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.",
"oneOf": [
{
"type": "number"
},
{
"type": "array",
"minItems": 1,
"items": {
"type": "number"
}
}
]
},
"deviations": {
"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.",
"type": "array",
"items": {
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb.py').read()
s=s.replace("brightness lags the rate by one to three frames","brightness lags the rate by one or two frames")
s=s.replace("""0.049). The KO minus WT difference is 0.062 at P9-11, 0.035 at P14-16 and 0.015 at P30-40, so it is
not largest at P14-16.""","""0.049). The KO minus WT difference is 0.062 at P9-11, 0.035 at P14-16 and 0.015 at P30-40, so it is
not largest at P14-16; as a ratio (a variant the criterion does not use) it is largest there (1.21,
against 1.17 and 1.13).""")
open('build_nb.py','w').write(s)
EOF
$TMPDIR/venv/bin/python build_nb.py && echo ok; date -u
```

```
ok
Sun Nov  8 08:49:16 UTC 2026
Shell cwd was reset to
```

**Agent**

Now the README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-ssc-8-goncalves-2013/README.md",
 "content": "# Goncalves, Anstey, Golshani & Portera-Cailliau (2013) from CRCNS ssc-8\n\nTests the findings of [Goncalves et al. (2013)](https://doi.org/10.1038/nn.3415) that can be tested\non CRCNS data set [ssc-8](https://doi.org/10.6080/K0X63K3X), which holds the estimated firing rates,\ncell-to-cell distances and raw movies of two-photon calcium imaging in L2/3 barrel cortex of 53\nunanesthetized WT and Fmr1 -/- mice at P9-11, P14-16 and P30-40. The whole-cell recordings, EEG,\nisoflurane imaging and 15.6 Hz imaging of the paper are not in it.\n\n| Claim | Outcome |\n|---|---|\n| Group sizes of Fig. 1e (12, 9, 8 WT and 9, 10, 8 KO mice) | Not reproduced |\n| In WT mice the drop in correlation from P9-11 to P14-16 is largest for nearby cells | Partially reproduced |\n| Correlation decreases with age in both genotypes | Reproduced |\n| Correlation is higher in KO mice, pooled over ages | Partially reproduced |\n| The same with Pearson correlation | Partially reproduced |\n| The genotype difference is largest, and significant, at P14-16 | Not reproduced |\n| No significant genotype difference at P30-40 | Reproduced |\n| Frequency of peaks of synchrony does not differ at P14-16 | Reproduced |\n| More neurons take part in peaks of synchrony in KO mice at P14-16 | Not reproduced |\n| Firing rates do not differ between genotypes at any age | Reproduced |\n| Firing rates and WT correlation at P14-16 (Fig. 6, unanesthetized) | Reproduced |\n| Whole-cell recordings (seven claims) | Blocked: data missing |\n| EEG with imaging (six claims) | Blocked: data missing |\n| Imaging at 15.6 Hz | Blocked: data missing |\n| Isoflurane imaging (three claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe data set's groups differ from the paper's (53 mice against 56), and it deposits estimated firing\nrates, not the dF/F traces the paper may have correlated. The attempt record, with the reasons and\nthe differences from the paper's method, is\n[`attempts/crcns-ssc-8-goncalves-2013-01.yaml`](../../attempts/crcns-ssc-8-goncalves-2013-01.yaml).\n"
}
```

```
File created successfully at: entries/crcns-ssc-8-goncalves-2013/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
ls questions | head; ls questions | grep -i crcns
```

```
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
000013.yaml
000015.yaml
000019.yaml
000023.yaml
crcns-ac-2.yaml
crcns-alm-3.yaml
crcns-bf-1.yaml
crcns-bf-3.yaml
crcns-ear-1.yaml
crcns-fcx-1.yaml
crcns-hc-16.yaml
crcns-hc-24.yaml
crcns-hc-7.yaml
crcns-nac-1.yaml
[... 7 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-ssc-8-goncalves-2013-01.yaml",
 "content": "schema_version: 2\nid: crcns-ssc-8-goncalves-2013-01\ndataset:\n  archive: crcns\n  id: ssc-8\n  version: unversioned\n  doi: 10.6080/K0X63K3X\npaper: doi:10.1038/nn.3415\ndate: 2026-11-08\nentry: crcns-ssc-8-goncalves-2013\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42461891472\noutcomes:\n- claim: group-sizes\n  outcome: not_reproduced\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:group-sizes\n  measured: [13, 8, 7, 9, 10, 6]\n  notes: The MAT file and the TIFF archive agree on 13, 8 and 7 WT and 9, 10 and 6 KO mice at P9-11,\n    P14-16 and P30-40 (28 WT and 25 KO), against 12, 9, 8 and 9, 10, 8 in Fig. 1e (29 and 27). Two of\n    six groups match (KO P9-11 and KO P14-16). The P14-16 counts (8 WT, 10 KO) match neither the Fig. 1e\n    counts nor the reversed n of the peaks of synchrony sentence (10 WT, 9 KO). No recording is\n    deposited twice (no identical movie or cell trace).\n- claim: fig1d-distance-dependent-decorrelation\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:fig1d-distance-dependent-decorrelation\n  measured: [0.191, 0.105, 0.025]\n  notes: WT mice, 13 at P9-11 and 8 at P14-16. Under the main reading (C-b, zero-lag normalised\n    cross-correlation of the estimated rates) the P9-11 minus P14-16 difference is 0.191 under 100 um,\n    0.105 at 100 to 200 um and 0.025 over 200 um, against 0.223, 0.159 and 0.067. The Bonferroni\n    corrected p are 6.6e-08, 0.0019 and 1.0 under A-a and 2.4e-05, 0.0066 and 1.0 under A-b, so the\n    significance pattern holds, and the difference falls with distance; none of the three\n    differences is within the 10% tolerance. The Spearman variant gives 0.175, 0.108 and 0.051. Only\n    4 of 8 P14-16 mice and 12 of 13 P9-11 mice have pairs over 200 um; on the mice with all three\n    bins the differences are 0.188, 0.102 and 0.025.\n  deviations:\n  - The data set holds 13 and 8 WT mice at these ages, not 12 and 9.\n  - The trace is the deposited estimated firing rate (reading T-a). Reading T-b, the low-pass filtered\n    dF/F, cannot be run, as the data set holds no cell contours or dF/F traces; the outcome is\n    assumed to hold for the trace the paper used. The Methods say only \"pair-wise continuous-trace\n    cross-correlations as previously described 15\".\n  - The post hoc test of A-a uses the two-way ANOVA's pooled residual mean square; that of A-b is a\n    t-test within each bin, both with Bonferroni over three bins. The text does not give the form.\n- claim: fig1e-age-decrease\n  outcome: reproduced\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:fig1e-age-decrease\n  notes: Pairs under 100 um, reading C-b. WT 0.360, 0.169 and 0.119 at the three ages (13, 8, 7 mice),\n    KO 0.421, 0.204 and 0.134 (9, 10, 6 mice). The 2-df age contrast within genotype of the\n    unequal-variance model gives F = 52.5 (df2 14.9, p = 1.8e-07) for WT and F = 64.3 (df2 14.1,\n    p = 8.1e-08) for KO. Welch's one-way ANOVA gives the same numbers, as the Welch-James test reduces\n    to it for a one-way design, so readings E-a and E-b agree. The Spearman variant agrees.\n  deviations:\n  - Group sizes differ from the paper's (see group-sizes).\n- claim: genotype-pooled-ages\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:genotype-pooled-ages\n  measured: [0.245, 0.265]\n  notes: The genotype main effect of the unequal-variance 2 x 3 model is significant with KO higher,\n    p = 0.0064 (F = 8.48, df2 33.5) for pairs under 100 um and p = 0.0028 for all pairs (paper\n    0.0057). No reading puts both means within the paper's s.e.m. Under 100 um over all mice (P-a,\n    M-a, given as measured) WT 0.245 and KO 0.265, KO within and WT not; all pairs over mice (P-b,\n    M-a) WT 0.223 and KO 0.251, WT within and KO not; mean of the age means (M-b) WT 0.216 and KO\n    0.253 under 100 um, 0.198 and 0.240 for all pairs. The s.e.m. under M-b (0.0088 and 0.0093) is\n    close to the paper's (0.008 and 0.009), while that over mice is 0.024 and 0.026, which suggests\n    the paper's pooled values are averages of age means, or model estimates, on a different sample.\n  deviations:\n  - Group sizes differ from the paper's (see group-sizes), which moves the pooled means.\n  - The trace is the estimated firing rate (T-a); T-b cannot be run (see\n    fig1d-distance-dependent-decorrelation). The outcome is assumed to hold for the paper's trace.\n  - The unequal-variance ANOVA is fitted on the six cell means with their variances of the mean,\n    and the genotype contrast tested with the Welch-James statistic and Satterthwaite degrees of\n    freedom; the claims file names this standard choice.\n- claim: pearson-genotype\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:pearson-genotype\n  measured: [0.179, 0.193]\n  notes: Pearson correlation. The genotype effect is significant with KO higher, p = 0.023 for pairs\n    under 100 um (paper 0.026) and 0.012 for all pairs. No reading puts both means within the paper's\n    s.e.m. Under 100 um over mice (given as measured) WT 0.179 and KO 0.193, KO within; all pairs over\n    mice WT 0.155 and KO 0.178, WT within; means of the age means WT 0.146 and KO 0.180, with s.e.m.\n    0.0092 and 0.0107 against the paper's 0.009 and 0.010.\n  deviations:\n  - Group sizes differ from the paper's; the trace is the estimated firing rate (T-a), and T-b cannot\n    be run; the outcome is assumed to hold for the paper's trace.\n- claim: fig1ef-p14-16-difference\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:fig1ef-p14-16-difference\n  measured: [0.169, 0.204]\n  notes: At P14-16 the means are within the paper's s.e.m. (WT 0.169 +/- 0.010, 8 mice; KO 0.204 +/-\n    0.013, 10 mice) and KO is higher, but the unpaired Student's t-test gives t = 2.05, p = 0.057\n    (Welch's test, not the Methods' test, gives p = 0.049). The KO minus WT difference is 0.062 at\n    P9-11, 0.035 at P14-16 and 0.015 at P30-40, so it is not largest at P14-16; as a ratio it is (1.21\n    against 1.17 and 1.13). The Spearman variant gives p = 0.058. The data set has one WT mouse fewer\n    at P14-16 than the paper.\n  deviations:\n  - 8 WT mice at P14-16, not 9.\n  - The trace is the estimated firing rate (T-a); T-b cannot be run; the outcome is assumed to hold\n    for the paper's trace.\n- claim: p30-40-no-difference\n  outcome: reproduced\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:p30-40-no-difference\n  measured: [0.134, 0.119]\n  notes: KO 0.134 +/- 0.011 (6 mice) against WT 0.119 +/- 0.005 (7 mice), difference 0.015, Student\n    p = 0.22 (Welch 0.25), reading C-b. WT is within the paper's s.e.m. (0.123 +/- 0.008); KO is below\n    it (0.144 +/- 0.008). The Spearman variant gives p = 0.62.\n  deviations:\n  - 6 KO and 7 WT mice, not 8 and 8.\n- claim: fig2b-peak-frequency\n  outcome: reproduced\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:fig2b-peak-frequency\n  measured: [0.060, 0.054]\n  notes: P14-16, 10 KO and 8 WT mice. No reading finds a difference (p = 0.13 to 0.64). Under R-a\n    (active when the rate is above 0) both means are within the paper's s.e.m. with either shuffle;\n    with S-a (given as measured) KO 0.060 +/- 0.006 and WT 0.054 +/- 0.007 peaks per s, p = 0.52; with\n    S-b 0.061 and 0.057, p = 0.64. Under R-b (at least one estimated spike in the frame) events are\n    rarer, 0.016 to 0.027 per s, outside the tolerances. Thresholds under R-a are 23 to 37.5% of\n    cells active. At 4 Hz the frequencies rise by 2.6% and the tests do not change.\n  deviations:\n  - 8 WT mice, against 10 in the text (and 9 in Fig. 1e).\n  - The definition of an active cell and the shuffle are not given in the paper; all four readings of\n    the claims file were run and give the same outcome. The shuffle seeds are a standard choice.\n- claim: fig2c-participation\n  outcome: not_reproduced\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:fig2c-participation\n  measured: [0.444, 0.411]\n  notes: No reading gives a significant genotype difference (p = 0.15 to 0.37). Under R-a, S-a and Q-a\n    (given as measured) KO 0.444 +/- 0.020 and WT 0.411 +/- 0.019, p = 0.25; both are above the paper's\n    0.380 and 0.300. Under R-a nearly every cell joins at least one event (Q-b 0.998 to 1.0). Under R-b\n    Q-a is 0.17 against 0.13 to 0.14 and Q-b 0.66 against 0.49 to 0.54, KO higher, p = 0.15 to 0.37.\n    No mouse lacks events.\n  deviations:\n  - 8 WT mice at P14-16, not 9 or 10.\n  - The definition of the proportion, of an active cell and of the shuffle are not given in the paper;\n    all eight readings of the claims file were run and give the same outcome.\n- claim: imaging-firing-rate-no-genotype-difference\n  outcome: reproduced\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:imaging-firing-rate-no-genotype-difference\n  notes: KO minus WT is 0.017 Hz at P9-11 (0.446 against 0.429, p = 0.73), 0.0002 Hz at P14-16 (0.304\n    against 0.304, p = 0.997) and 0.014 Hz at P30-40 (0.371 against 0.356, p = 0.76). Reading the rates\n    as per frame scales both groups by 3.9 and does not change the tests.\n  deviations:\n  - Group sizes differ from the paper's (see group-sizes).\n- claim: unanesthetized-p14-16-values\n  outcome: reproduced\n  notebook: reproduce_goncalves_2013.ipynb\n  output: claim:unanesthetized-p14-16-values\n  measured: [0.304, 0.304, 0.169]\n  notes: With the rates read as Hz (U-a), WT 0.304 +/- 0.027 Hz (8 mice) and KO 0.304 +/- 0.027 Hz (10\n    mice), within 0.30 +/- 0.03 and 0.29 +/- 0.03; the WT correlation of pairs under 100 um is 0.169 +/-\n    0.010 (C-b), within 0.17 +/- 0.01. Read as per frame (U-b) the rates would be 1.19 Hz. The data\n    descriptor gives no unit; the values, which are 0 in about 90% of frames and average 0.19 to 0.74\n    per recording, fit Hz.\n  deviations:\n  - The unanesthetized groups of Fig. 6 are taken to be the P14-16 mice of Fig. 1e, as the claims file\n    reads them; the data set has 8 WT, not 9.\n- claim: wholecell-updown-firing\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The data set holds only calcium imaging (the bucket's ssc-8/live/ lists the TIFF archive, the\n    MAT file of rates and distances, and the descriptor). The descriptor and the paper name no\n    deposit of the whole-cell recordings.\n- claim: wholecell-state-modulation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Whole-cell recordings are not in the data set (see wholecell-updown-firing).\n- claim: fig3f-foa-time\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Whole-cell recordings are not in the data set (see wholecell-updown-firing).\n- claim: ap-kinetics-similar\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Whole-cell recordings are not in the data set (see wholecell-updown-firing).\n- claim: fig4-updown-properties-similar\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Whole-cell recordings are not in the data set (see wholecell-updown-firing).\n- claim: fig4f-spikes-per-up-state\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Whole-cell recordings are not in the data set (see wholecell-updown-firing).\n- claim: fig4g-up-state-firing-probability\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Whole-cell recordings are not in the data set (see wholecell-updown-firing).\n- claim: fig5c-firing-vs-lh-p14-16\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The EEG is not in the data set, nor named as deposited anywhere by the paper or the\n    descriptor, and the data set does not say which recordings had EEG.\n- claim: p30-40-firing-vs-lh\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No EEG in the data set (see fig5c-firing-vs-lh-p14-16).\n- claim: fig5d-correlation-vs-lh\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No EEG in the data set (see fig5c-firing-vs-lh-p14-16).\n- claim: fig5ef-slow-wave-epochs\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No EEG in the data set (see fig5c-firing-vs-lh-p14-16).\n- claim: suppl4a-firing-vs-correlation\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: reproduce_goncalves_2013.ipynb\n  output: variant:suppl4a-firing-vs-correlation\n  notes: The claim's sample is the 3-min recordings of the EEG subset (13 WT and 10 KO), which the data\n    set does not identify; it holds one concatenated recording per mouse and no EEG. As a variant that\n    decides nothing, the P14-16 recordings cut into 720-frame segments give KO r2 = 0.157 (slope\n    positive, p = 0.050, 25 segments from 10 mice) and WT r2 = 0.006 (p = 0.76, 18 segments from 8 mice);\n    segments of one mouse are not independent.\n- claim: fig5g-lh-power-similar\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No EEG in the data set (see fig5c-firing-vs-lh-p14-16).\n- claim: fast-imaging-control\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The 15.6 Hz recordings are not in the data set; all its movies are in folders named 4Hz, and\n    the descriptor lists 3.9 Hz recordings only.\n- claim: fig6-isoflurane-wt-correlation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The data set holds unanesthetized mice only (descriptor, Summary); no isoflurane imaging is\n    deposited, here or elsewhere as far as the paper and descriptor say.\n- claim: fig6-isoflurane-ko-correlation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No isoflurane imaging in the data set (see fig6-isoflurane-wt-correlation).\n- claim: fig6-isoflurane-firing\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No isoflurane imaging in the data set (see fig6-isoflurane-wt-correlation).\nfindings:\n- kind: selection_undocumented\n  statement: The data set holds 13, 8 and 7 WT mice and 9, 10 and 6 Fmr1 -/- mice at P9-11, P14-16 and\n    P30-40 (53), while the paper analysed 12, 9 and 8 and 9, 10 and 8 (56). Neither the descriptor nor\n    the files say which mice differ from the paper's sample or why.\n- kind: metadata_error\n  statement: The descriptor gives 40 to 149 neurons per animal; two WT P9-11 recordings have 164 and 198.\n    It gives about 7 to 8 min per recording; at the stated 3.9 Hz the recordings last 3.8 to 15.4 min,\n    and 27 of 53 are 2160 frames (9.2 min).\n- kind: metadata_insufficient\n  statement: The descriptor gives no unit for the estimated firing rates; their values fit Hz. It does\n    not say that the k-th matrix of each group belongs to Movie_k.tif, which the frame counts and the\n    correlation of the population rate with each movie's brightness show.\n- kind: other\n  statement: The movie folders are named \"4Hz\" where the paper and the descriptor give 3.9 Hz, and most\n    recordings are 2160 frames, three 3-min movies at 4 Hz. Frames are 128 x 256 pixels in 50 movies\n    (and 357, 404 and 512 wide in one each), where the Methods give 512 x 128. The TIFFs carry no time\n    stamps, so the frame rate cannot be checked.\n- kind: data_missing\n  statement: No cell contours or dF/F traces are deposited, so the paper's correlations cannot be\n    computed from the filtered dF/F if that is what the paper used; only the estimated firing rates\n    are given. The whole-cell recordings, the EEG, the isoflurane imaging and the 15.6 Hz imaging are\n    not deposited, and 17 of the paper's 28 claims cannot be tested.\n- kind: format_error\n  statement: The TIFF archive holds five macOS resource-fork files (._.DS_Store and ._Movie_1.tif) beside\n    the 53 movies.\n- kind: methods_unavailable\n  statement: Question for the authors. Which trace and which measure give the pairwise correlation of\n    Fig. 1 (the Methods refer to ref. 15 for \"continuous-trace cross-correlations\")? Was it the\n    deconvolved trace deposited here or the filtered dF/F, was the mean subtracted, and at which lag?\n    The zero-lag normalised cross-correlation of the deposited rates gives the paper's P14-16 values\n    (WT 0.169, KO 0.204) but pooled means that differ from the paper's.\n- kind: methods_unavailable\n  statement: Question for the authors. For peaks of synchrony, when is a cell active in a frame, how was\n    each trace shuffled, and how is the proportion of neurons participating in an event formed? With\n    an active cell as any non-zero rate the frequencies match the paper's, but every reading gives\n    proportions above the paper's 0.300 and 0.380.\n- kind: methods_unavailable\n  statement: Question for the authors. How was the pooled average correlation (0.230 and 0.265) formed,\n    and how was the unequal-variance 2 x 3 ANOVA fitted? The paper's s.e.m. fit an average of the\n    three age means, not the mean over mice.\n"
}
```

```
File created successfully at: attempts/crcns-ssc-8-goncalves-2013-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n ': .*: ' attempts/crcns-ssc-8-goncalves-2013-01.yaml entries/crcns-ssc-8-goncalves-2013/entry.yaml | grep -v '^\S*:\s*- ' | head; grep -n "—\|rather\|\*\*" attempts/crcns-ssc-8-goncalves-2013-01.yaml entries/crcns-ssc-8-goncalves-2013/README.md entries/crcns-ssc-8-goncalves-2013/ssc8.py | head; python tools/entry.py lock entries/crcns-ssc-8-goncalves-2013 2>&1 | tail -2; date -u; time python tools/entry.py all entries/crcns-ssc-8-goncalves-2013 2>&1 | tail -20
```

```
entries/crcns-ssc-8-goncalves-2013/ssc8.py:151:    with fsspec.open(TIFF_URL, "rb", block_size=2**24) as f:
entries/crcns-ssc-8-goncalves-2013/ssc8.py:229:        A += (np.trace(PQ @ PQ) + np.trace(PQ) ** 2) / (2 * (n[j] - 1))
entries/crcns-ssc-8-goncalves-2013/ssc8.py:244:    num = (w * (m - mw) ** 2).sum() / (k - 1)
entries/crcns-ssc-8-goncalves-2013/ssc8.py:245:    lam = 3 * (((1 - w / w.sum()) ** 2) / (n - 1)).sum() / (k ** 2 - 1)
wrote entries/crcns-ssc-8-goncalves-2013/requirements.lock.txt
Sun Nov  8 08:50:31 UTC 2026
Installed kernelspec registry-crcns-ssc-8-goncalves-2013 in executed/crcns-ssc-8-goncalves-2013/.venv/share/jupyter/kernels/registry-crcns-ssc-8-goncalves-2013
0 error(s)
pass  reproduce_goncalves_2013.ipynb  (203 s)

real	3m31.570s
user	1m37.029s
sys	0m21.023s
```

**Agent calls Bash**

```bash
ls executed/crcns-ssc-8-goncalves-2013/; $TMPDIR/venv/bin/python - <<'EOF'
import json,glob
def outs(p):
    nb=json.load(open(p)); r=[]
    for c in nb['cells']:
        if c['cell_type']=='code':
            r.append(''.join(''.join(o.get('text',[])) for o in c.get('outputs',[])))
    return r
a=outs('/tmp/claude-1001/dev.ipynb'); b=outs(glob.glob('executed/crcns-ssc-8-goncalves-2013/*.ipynb')[0])
import re
for i,(x,y) in enumerate(zip(a,b)):
    x=re.sub(r'in \d+ s|\d+\.\d min','',x); y=re.sub(r'in \d+ s|\d+\.\d min','',y)
    if x!=y: print('differs cell',i)
print(len(a),len(b))
EOF
```

```
reproduce_goncalves_2013.ipynb
result.json
19 19
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/crcns-ssc-8-goncalves-2013 2>&1 | tail -5; ls executed/crcns-ssc-8-goncalves-2013/handover/; git status --short; date -u
```

```
wrote executed/crcns-ssc-8-goncalves-2013/handover
10.1038-nn.3415.yaml
reproduce_goncalves_2013.ipynb
ssc8.py
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
?? attempts/crcns-ssc-8-goncalves-2013-01.yaml
?? entries/crcns-ssc-8-goncalves-2013/
?? scripts
Sun Nov  8 08:54:22 UTC 2026
```

**Agent calls Bash**

```bash
ls -a entries/crcns-ssc-8-goncalves-2013/; git check-ignore -v entries/crcns-ssc-8-goncalves-2013/__pycache__ 2>&1; ls -la scripts | head -5
```

```
.
..
.claude
README.md
__pycache__
entry.yaml
reproduce_goncalves_2013.ipynb
requirements.in
requirements.lock.txt
ssc8.py
.gitignore:1:__pycache__/	entries/crcns-ssc-8-goncalves-2013/__pycache__
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 08:11 scripts
```

**Agent calls Bash**

```bash
ls -la entries/crcns-ssc-8-goncalves-2013/.claude; git check-ignore -v entries/crcns-ssc-8-goncalves-2013/.claude
```

```
Exit code 1
total 12
drwxr-xr-x 3 runner runner 4096 Nov  8 08:31 .
drwxr-xr-x 4 runner runner 4096 Nov  8 08:50 ..
drwx------ 2 runner runner 4096 Nov  8 08:31 .cc-writes
```

**Agent**

I tested 11 of the 28 claims: 5 reproduced, 3 partially reproduced and 3 not reproduced. The other 17 are blocked because their data are not in ssc-8. The entry passed `tools/entry.py all` with 0 errors, and the notebook runs in 203 s. The handover package is in `executed/crcns-ssc-8-goncalves-2013/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome | Key numbers |
|---|---|---|
| group-sizes | not reproduced | 13/8/7 WT and 9/10/6 KO mice, against 12/9/8 and 9/10/8 in the paper |
| fig1d-distance-dependent-decorrelation | partially reproduced (assumed) | drops of 0.191, 0.105, 0.025 against 0.223, 0.159, 0.067; the significance pattern holds |
| fig1e-age-decrease | reproduced | p of 1.8e-07 (WT) and 8.1e-08 (KO) |
| genotype-pooled-ages | partially reproduced (assumed) | p = 0.0064 (paper 0.0057); no reading puts both means within the s.e.m. |
| pearson-genotype | partially reproduced (assumed) | p = 0.023 (paper 0.026); means not both within the s.e.m. |
| fig1ef-p14-16-difference | not reproduced (assumed) | means match (0.169, 0.204), but Student's p = 0.057; the difference is not largest at P14-16 |
| p30-40-no-difference | reproduced | p = 0.22 |
| fig2b-peak-frequency | reproduced | 0.060 and 0.054 per s, p = 0.52; the same under all four readings |
| fig2c-participation | not reproduced | p = 0.15 to 0.37 under all eight readings |
| imaging-firing-rate-no-genotype-difference | reproduced | p ≥ 0.73 at every age |
| unanesthetized-p14-16-values | reproduced | 0.304 and 0.304 Hz; WT correlation 0.169 |
| 7 whole-cell, 6 EEG, 1 at 15.6 Hz, 3 isoflurane claims | blocked (`data_missing`) | none of these data are deposited |

For the blocked suppl4a claim I ran a variant on 3-min segments of the recordings. It does not decide the outcome.

**2. The dataset, assumptions and questions**
- **Group sizes:** the dataset has 53 mice where the paper has 56, and the groups differ in size. Nothing says why.
- **Descriptor errors:** neuron counts go up to 198 (the descriptor says 40 to 149). Recordings last 3.8 to 15.4 min (it says 7 to 8). It gives no unit for the firing rates; the values fit Hz.
- **Frame rate and size:** the movie folders are named "4Hz", but the paper says 3.9 Hz. Most recordings are 2160 frames, which is three 3-minute movies at 4 Hz. Frames are 128 x 256 pixels, while the Methods say 512 x 128.
- **Clock check:** each rate matrix k belongs to `Movie_k.tif`, and they share one frame clock. This holds for all 53 recordings, but the descriptor does not say it.
- **Duplicates and stray files:** no recording is deposited twice. The TIFF archive also holds 5 macOS `._` resource-fork files.
- **Not deposited:** cell contours, dF/F traces, and the whole-cell, EEG, isoflurane and 15.6 Hz data.
- **Assumption:** correlations use the deposited deconvolved rates (reading T-a). Reading T-b, the filtered dF/F traces, cannot be rebuilt without cell contours. So the four correlation outcomes that are not plain matches carry `assumed: true`.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which trace and measure the correlation uses, including mean subtraction and lag.
  - For peaks of synchrony: when a cell counts as active, how traces were shuffled, and how participation is formed.
  - How the pooled average was formed and how the ANOVA was fitted. The paper's s.e.m. match a mean of the three age means.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. Step 2 (clock check) assumes trial tables or annotations, and this dataset has neither. I compared the population rate against each movie's frame brightness, against the other movies and against time-shifted rates instead.
2. archives.md does not say that `+` in a CRCNS file name must be URL-encoded as `%2B`. Without it the bucket returns 404. I encoded it.
3. "Run every reading" does not cover a reading that cannot be run at all (T-b). I ran T-a only and marked the outcomes that rest on it as assumed.
4. A `.tar.gz` cannot be opened in place the way a zip can. I streamed it once in order, holding one movie in memory at a time, and hashed each member, since the archive's own MD5 needs the whole compressed stream.
5. The protocol does not say whether a variant for a blocked claim may have its own tagged cell. I tagged it `variant:suppl4a-...` and stated that it decides nothing.

**4. Runtime and failures**
- The run took about 42 minutes (08:13 to 08:55 UTC).
- The first attempt to read the TIFF archive failed with a 404 until I encoded `+` as `%2B`.
- In one exploratory pass, parsing the TIFFs with the `tifffile` library peaked at 7.3 GB of memory. I replaced it with a small parser in the helper module, and streaming a member then peaks at about 0.5 GB.

## End of run

48 turns, 36 minutes, $4.28 at API prices, result: success.
