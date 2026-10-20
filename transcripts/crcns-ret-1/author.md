# crcns-ret-1 · author · run 39490975405

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls claims/crcns-ret-1 paper entries | head -50
```

**Agent calls Bash**

```bash
cat README.md; cat docs/design.md
```

```
<persisted-output>
Output too large (29.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/679a0e33-a61b-431a-ac52-8f9b495398df/tool-results/b84l1ejmm.txt

Preview (first 2KB):
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes
[... 24 more lines not kept]
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

[... 539 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/archives.md; cat claims/crcns-ret-1/*.yaml; ls paper
```

```
<persisted-output>
Output too large (37.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/679a0e33-a61b-431a-ac52-8f9b495398df/tool-results/bh6o8qn7v.txt

Preview (first 2KB):
# Archives

The registry tests papers against data in public archives. So far it reads one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. `tools/datasets.py` holds the table of
archives and turns one form of a dataset's name into another. The workflows
take a dataset in any of these forms.

## DANDI
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## CRCNS/,/^## [A-Z]/p' docs/archives.md; ls paper
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-ret-1/10.1242-dev.027912.yaml"
}
```

```
## CRCNS

- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
  `hc-3`), with a DOI of its own (`10.6080/...`). The registry's list is
  `targets/crcns.json`, written by hand; for now it holds one data set, to test
  the pipeline beyond DANDI.
- **Versions.** CRCNS data sets are not versioned. Record the version as
  `unversioned`, with the data set's DOI under `dataset: doi`, and give in the
  notebook header the MD5 sums from the data set's `checksums.md5` for the
  files read, so a later change is detectable.
- **Reading.** The files are in the public S3 bucket `crcnsarchive` (region
  us-west-2), under `<id>/`, readable without an account at
  `https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/<file>`; list a data
  set with `?list-type=2&prefix=<id>/` on the bucket's address. The site
  crcns.org asks for a login to download; the bucket does not. Most data sets
  are zip files of MATLAB or other files: open the zip in place with
  `fsspec.open(url, block_size=2**20).open()` and Python's `zipfile`, which
  read only the parts needed over range requests (`remfile` lacks what
  `zipfile` needs to read a member), and load members in memory
  (`scipy.io.loadmat`, or `h5py` for MATLAB 7.3 files). Do not download whole
[... 6 more lines not kept]
```

```
1	# Claims for Lefebvre, Zhang, Meister, Wang & Sanes (2008), Development 135:4141-4151, on CRCNS
2	# data set ret-1 (doi:10.6080/K0RF5RZT).
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
4	# protocol pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read: the NIH author manuscript in PubMed Central (PMC2644426), as supplied under paper/,
7	# with its Methods, Results, Discussion and the legends of Figures 1 to 9; the version of
8	# record's abstract is appended to it. No PDF was supplied. The supplement (Supplementary
9	# Figures 1 to 3, which PMC lists as present) is not in the text and was not read. Its
10	# contents are known only from the main text's citations: the Chx10-Cre recombination pattern
11	# (S1), synapse density in Bax mutants and example spike-triggered averages (S2; the
12	# manuscript cites S2 for both), and receptive field surrounds (S3). Its legends were not seen
13	# and may hold method details (the test of S2, the measure of S3). The claims that cite it are
14	# quoted from the main text and take no number from it. The paper links no analysis code, so none was read.
15	#
16	# Data the paper used. Mice on a C57/B6J background. Conditional Pcdh-gamma alleles (fdel, the
17	# whole cluster floxed; fcon3, the last constant exon floxed), excised in retina by Chx10-Cre
18	# or Pax6alpha-Cre (Pax6alpha-Cre spares a central sector except for Pax6alpha amacrines); some
19	# crossed onto Bax-/-. Histology (Figures 1 to 8): sections and dissociated cells, layer
20	# thickness and cell counts at E17.5 to P150, 3 to 8 animals per genotype; none of it is in
[... 485 more lines not kept]
```

**Agent**

Now the example entry for formats.

**Agent calls Bash**

```bash
ls -la entries/001453-fouke-2025/ claims/001453/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml; ls questions | head;
```

```
<persisted-output>
Output too large (36.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/679a0e33-a61b-431a-ac52-8f9b495398df/tool-results/b26df282z.txt

Preview (first 2KB):
claims/001453/:
total 28
drwxr-xr-x  2 runner runner  4096 Oct 20 20:19 .
drwxr-xr-x 59 runner runner  4096 Oct 20 20:19 ..
-rw-r--r--  1 runner runner 17825 Oct 20 20:19 10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025/:
total 124
drwxr-xr-x  2 runner runner  4096 Oct 20 20:19 .
drwxr-xr-x 58 runner runner  4096 Oct 20 20:19 ..
-rw-r--r--  1 runner runner  2158 Oct 20 20:19 README.md
-rw-r--r--  1 runner runner   914 Oct 20 20:19 entry.yaml
-rw-r--r--  1 runner runner 16218 Oct 20 20:19 omr.py
-rw-r--r--  1 runner runner 79403 Oct 20 20:19 reproduce_fouke_2025.ipynb
-rw-r--r--  1 runner runner    61 Oct 20 20:19 requirements.in
-rw-r--r--  1 runner runner  5989 Oct 20 20:19 requirements.lock.txt
[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001453-fouke-2025-01.yaml"
}
```

```
1	schema_version: 2
2	id: 001453-fouke-2025-01
3	dataset:
4	  archive: dandi
5	  id: "001453"
6	  version: 0.250518.1950
7	  doi: 10.48324/dandi.001453/0.250518.1950
8	paper: doi:10.1016/j.cub.2025.04.027
9	date: 2026-10-14
10	entry: 001453-fouke-2025
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-5
19	inputs:
20	- what: Names of the stimulus codes (the conversion of stimulus names to codes, its printed list of
[... 598 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ret-1/" | python -c "import sys,re; d=sys.stdin.read(); [print(k,s) for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',d)]"; ls questions; cat targets/crcns.json
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1; curl -s $B/checksums.md5; echo; curl -s $B/filelist.txt; echo; cat questions/README.md; python -c "import fsspec,pdfplumber" ; pip list 2>/dev/null | grep -i -E "pdf|fsspec|scipy|aiohttp|requests"
```

```
4b9390ddc51c72d6f66563cb02e48fe8  crcns_ret-1.zip
1b66fe25386b4d1cc14e66b6f719a985  docs/crcns_ret-1_data_description.docx
eca35a17912488ad1ddf1e5231005aa5  docs/crcns_ret-1_data_description.pdf
f7edda46d58d4b57d71f40b8bffc1a0c  filelist.txt

# CRCNS.org 'ret-1' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 crcns_ret-1.zip	71871914 (68.5 MB)
 docs/crcns_ret-1_data_description.docx	105456 (102.9 KB)
 docs/crcns_ret-1_data_description.pdf	87274 (85.2 KB)
 checksums.md5	242

# Questions

`<dandiset>.yaml` holds an attempt's questions about its paper: what the author needed and the
claims file did not give (docs/protocol.md, "Author", step 1.6), and the reader's answers
("Reader", step 6). Each question has `claim`, `question`, `why` (how the answer could change the
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q ex && . ex/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy h5py pypdf matplotlib pandas 2>&1 | tail -2; python - <<'EOF'
import io, requests, pypdf
r=requests.get("https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/docs/crcns_ret-1_data_description.pdf")
p=pypdf.PdfReader(io.BytesIO(r.content))
for pg in p.pages: print(pg.extract_text())
EOF
```

```
CRCNS.org ret-1 data description 
Version 0.8 (September 2, 2014) 
 
 
The CRCNS.org ret-1 dataset contains neuronal responses of retinal ganglion 
cells to various visual stimuli recorded in the isolated retina from lab mice (Mus 
Musculus) using a 61-electrode array.  Data was recorded by Yifeng Zhang in 
Markus Meister's lab at Harvard University in 2008.  For details, please see the 
following paper: 
 
Lefebvre, J.L., Zhang, Y., Meister, M., Wang, X., and Sanes, J.R. (2008) 
Gamma-Protocadherins regulate neuronal survival but are dispensable for 
circuit formation in retina. Development 135:4141-4151. 
 
Hiroki Asari standardized the data format in MATLAB (2013b: Mathworks).  
Please contact him ([removed: an e-mail address]) if you have any questions on the 
format. Otherwise, address correspondence to: 
 
 
Markus Meister, PhD 
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && python - <<'EOF'
import fsspec, zipfile
f=fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/crcns_ret-1.zip", block_size=2**20).open()
z=zipfile.ZipFile(f)
for i in z.infolist(): print(i.filename, i.file_size, i.compress_size, i.date_time)
EOF
```

```
crcns_ret-1/ 0 0 (2014, 9, 2, 12, 34, 52)
crcns_ret-1/Analysis_example.m 2729 1298 (2014, 7, 16, 13, 9, 54)
__MACOSX/ 0 0 (2014, 9, 2, 12, 39, 6)
__MACOSX/crcns_ret-1/ 0 0 (2014, 9, 2, 12, 39, 6)
__MACOSX/crcns_ret-1/._Analysis_example.m 170 88 (2014, 7, 16, 13, 9, 54)
crcns_ret-1/Data/ 0 0 (2014, 8, 14, 17, 52, 58)
crcns_ret-1/Data/20080516_R1.mat 1515345 1515628 (2014, 8, 14, 17, 42, 14)
__MACOSX/crcns_ret-1/Data/ 0 0 (2014, 9, 2, 12, 39, 6)
__MACOSX/crcns_ret-1/Data/._20080516_R1.mat 170 88 (2014, 8, 14, 17, 42, 14)
crcns_ret-1/Data/20080516_R2.mat 4462406 4462793 (2014, 8, 14, 17, 43, 58)
__MACOSX/crcns_ret-1/Data/._20080516_R2.mat 170 88 (2014, 8, 14, 17, 43, 58)
crcns_ret-1/Data/20080606_R1.mat 217459 217518 (2014, 8, 14, 17, 52, 26)
__MACOSX/crcns_ret-1/Data/._20080606_R1.mat 170 88 (2014, 8, 14, 17, 52, 26)
crcns_ret-1/Data/20080606_R2.mat 425996 426111 (2014, 8, 14, 17, 52, 28)
__MACOSX/crcns_ret-1/Data/._20080606_R2.mat 170 88 (2014, 8, 14, 17, 52, 28)
crcns_ret-1/Data/20080606_R3.mat 112553 112575 (2014, 8, 14, 17, 52, 32)
__MACOSX/crcns_ret-1/Data/._20080606_R3.mat 170 88 (2014, 8, 14, 17, 52, 32)
crcns_ret-1/Data/20080624_R1.mat 6263599 6264113 (2014, 8, 14, 17, 44, 8)
__MACOSX/crcns_ret-1/Data/._20080624_R1.mat 170 88 (2014, 8, 14, 17, 44, 8)
crcns_ret-1/Data/20080624_R2.mat 1950808 1951281 (2014, 8, 14, 17, 44, 8)
[... 25 more lines not kept]
```

**Agent**

I've listed the archive: one 69 MB zip holding 16 MATLAB files (one per retina), a RAN1 generator and its precomputed bit stream. Next, the example code and the contents of the files.

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && python - <<'EOF'
import fsspec, zipfile
f=fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/crcns_ret-1.zip", block_size=2**20).open()
z=zipfile.ZipFile(f)
for n in ["crcns_ret-1/README.txt","crcns_ret-1/Analysis_example.m","crcns_ret-1/ran1.m"]:
    print("=====",n); print(z.read(n).decode('latin1'))
EOF
```

```
===== crcns_ret-1/README.txt
See file:
crcns_ret-1_data_description.pdf
available at 
http://dx.doi.org/10.6080/K0RF5RZT
for information about this data set.

===== crcns_ret-1/Analysis_example.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  
% ANALYSIS SAMPLE COMMANDS
%
%   Here we load the example data 20080516_R1.mat and recover the
%   spatio-temporal receptive field of the mouse retinal ganglion cells.
%   In the example data set (recording no.1), randomly flickering bar 
%   stimulus was presented.
%
%   NOTE: Generating random numbers is quite slow. It takes about 1 hour to 
%   generate 1e8 random numbers on Intel(R) Core(TM) i7-3612QM CPU @ 2.1 GHz.
%
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && python - <<'EOF'
import fsspec, zipfile, io, scipy.io as sio, numpy as np
f=fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/crcns_ret-1.zip", block_size=2**20).open()
z=zipfile.ZipFile(f)
names=[n for n in z.namelist() if n.startswith("crcns_ret-1/Data/") and n.endswith(".mat")]
for n in names:
    m=sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)
    di=m['datainfo']
    print("=====",n.split('/')[-1], [k for k in m if not k.startswith('__')])
    for k in di._fieldnames: print("  ",k,repr(getattr(di,k)))
    st=np.atleast_1d(m['stimulus']); sp=m['spikes']
    print("  spikes shape",np.shape(sp))
    for i,s in enumerate(st):
        d={k:getattr(s,k) for k in s._fieldnames if k!='param'}
        p=s.param; pd={k:getattr(p,k) for k in p._fieldnames} if hasattr(p,'_fieldnames') else p
        col = sp[:,i] if sp.ndim==2 else [sp[i]]
        ns=[np.size(c) for c in col]
        mx=[np.max(c) if np.size(c) else np.nan for c in col]
        print("   stim",i,d,pd,"nspk",sum(ns),"spk range",np.nanmin([np.min(c) for c in col if np.size(c)]) if sum(ns) else None, np.nanmax(mx))
EOF
```

```
===== 20080516_R1.mat ['datainfo', 'stimulus', 'spikes']
   date '20080516'
   SmplNo 1
   RecNo array([4, 5, 6], dtype=uint8)
   RecStartTime array([[2008,    5,   16,   20,   23,   32],
       [2008,    5,   16,   20,   51,   18],
       [2008,    5,   16,   21,   17,   12]], dtype=uint16)
   Ncell 7
   experimenter 'Yifeng Zhang, Markus Meister lab, Harvard University'
   description 'multi-electrode recordings from mouse retinal ganglion cells'
   animal 'KO (pax6)'
  spikes shape (7, 3)
   stim 0 {'type': 'binarywhitenoise', 'onset': 1.2375, 'frame': 0.016671788281371697, 'Nframes': 89899, 'pixelsize': 8.3} {'x': 640, 'y': 480, 'dx': 1, 'dy': 480, 'seed': -10000} nspk 134963 spk range 0.0224 1499.9887
   stim 1 {'type': 'binarywhitenoise', 'onset': 1.2488, 'frame': 0.01667177721587574, 'Nframes': 89898, 'pixelsize': 8.3} {'x': 640, 'y': 480, 'dx': 10, 'dy': 10, 'seed': -10000} nspk 109580 spk range 0.0292 1499.9209
   stim 2 {'type': 'binarywhitenoise', 'onset': 1.2599, 'frame': 0.01667180611835953, 'Nframes': 89897, 'pixelsize': 8.3} {'x': 640, 'y': 480, 'dx': 640, 'dy': 1, 'seed': -10000} nspk 62006 spk range 0.0315 1499.9807
===== 20080516_R2.mat ['datainfo', 'stimulus', 'spikes']
   date '20080516'
   SmplNo 2
   RecNo array([4, 6, 7], dtype=uint8)
   RecStartTime array([[2008,    5,   16,   23,    2,    8],
[... 201 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i -E "electrophysiolog|flicker|Fig(ure)? 9|multielectrode|electrode|spike|LN|Linear-Nonlinear|threshold|gain" paper/10.1242-dev.027912.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
t=open("paper/10.1242-dev.027912.txt").read()
import re
for kw in ["Electrophysiology","Functional visual circuits","Figure 9 ","FIGURE 9","Fig. 9"]:
    for m in re.finditer(kw,t):
        print("=== ",kw,m.start())
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
t=open("paper/10.1242-dev.027912.txt").read()
print(t[10400:12600]); print("--------"); print(t[31300:35500]); print("--------"); print(t[60500:63500])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && python - <<'EOF'
import fsspec, zipfile, numpy as np
def ran1_seq(seed, n):
    IA=16807; IM=2147483647; AM=1.0/IM; IQ=127773; IR=2836; NTAB=32; NDIV=1+(IM-1)//NTAB; RNMX=1-1.2e-7
    iv=[0]*NTAB; s=-seed if seed<-1 else 1
    for j in range(NTAB+8,0,-1):
        k=s//IQ; s=IA*(s-k*IQ)-IR*k
        if s<0: s+=IM
        if j<=NTAB: iv[j-1]=s
    iy=iv[0]; out=[]
    for _ in range(n):
        k=s//IQ; s=IA*(s-k*IQ)-IR*k
        if s<0: s+=IM
        j=iy//NDIV; iy=iv[j]; iv[j]=s
        r=AM*iy; out.append(min(r,RNMX))
    return np.array(out)
r=ran1_seq(-10000,20000)>=0.5
f=fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/crcns_ret-1.zip", block_size=2**20).open()
z=zipfile.ZipFile(f)
with z.open("crcns_ret-1/ran1.bin") as g: b=np.frombuffer(g.read(4000),dtype=np.uint8)
for order in ["little","big"]:
    bits=np.unpackbits(b,bitorder=order)[:20000].astype(bool)
    print(order,(bits==r).mean())
EOF
```

```
little 1.0
big 0.4981
Shell cwd was reset to
```

**Agent**

`ran1.bin` matches RAN1 with seed -10000, read least significant bit first. I'll now write the helper module in the entry directory and use it to explore.

**Agent calls Bash**

```bash
cat entries/001453-fouke-2025/README.md; head -c 3000 entries/001453-fouke-2025/omr.py; python - <<'EOF'
import json
nb=json.load(open("entries/001453-fouke-2025/reproduce_fouke_2025.ipynb"))
print(nb["metadata"])
for c in nb["cells"][:6]: print(c["cell_type"], c.get("metadata"), "".join(c["source"])[:1500]); print('---')
EOF
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
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/entry.py; grep -n "def \|tag\|forbid\|runtime" tools/entry.py | head -80; ls schemas
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 121,290p tools/entry.py; cat schemas/attempt.schema.json | head -c 9000
```

```
def check(entry_dir: Path) -> Report:
    report = Report()
    rel = entry_dir.relative_to(ROOT)
    entry = validate(report, entry_dir / "entry.yaml", "entry")
    if entry is None:
        return report
    if entry.get("name") != entry_dir.name:
        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")

    listed = [n["path"] for n in entry.get("notebooks", [])]
    present = sorted(p.name for p in entry_dir.glob("*.ipynb"))
    for name in sorted(set(present) - set(listed)):
        report.error(rel / name, "notebook is not listed in entry.yaml")
    for name in sorted(set(listed) - set(present)):
        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
    helpers = entry.get("helpers", [])
    for name in helpers:
        if not (entry_dir / name).is_file():
            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")

[... 462 more lines not kept]
```

**Agent**

Now the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-ret-1-lefebvre-2008/ret1.py",
 "content": "\"\"\"Loading and measures for CRCNS data set ret-1 (doi:10.6080/K0RF5RZT).\n\nLefebvre, Zhang, Meister, Wang & Sanes (2008), Development 135:4141-4151,\ndoi:10.1242/dev.027912, Figure 9.\n\nThe data set is one zip file in the public S3 bucket `crcnsarchive`. It holds one MATLAB file per\nretina (16), each with `datainfo` (date, genotype label in `animal`, number of cells), `spikes`\n(cells by stimuli, spike times in s) and `stimulus` (one entry per recording: binary white noise\nwith its onset, frame length, number of frames, pixel size of 8.3 um and the size of its tiles),\nand `ran1.bin`, the bits of the RAN1 generator with seed -10000 from which every stimulus is drawn\n(the seed every recording states). The zip is opened in place over range requests and members are\nread into memory; nothing is written to disk. CRCNS data sets are not versioned; `VERSION` is\n\"unversioned\" and `ZIP_MD5` is the sum the data set's `checksums.md5` gives for the zip.\n\nWhere the parameters come from:\n\n- Stimulus reconstruction follows the data set's own `Analysis_example.m`: frame k of a recording\n  spans [onset + k frame, onset + (k+1) frame), Nframes - 1 frames are used, the first\n  `m = (x/dx)(y/dy)` bits of `ran1.bin` are the tiles of frame 1, the next m those of frame 2, and\n  so on, bit 1 is light (+1) and 0 dark (-1). Bits are read least significant first, as MATLAB's\n  `fread(..., '*ubit1')` does; the notebook checks this against RAN1 itself.\n- The spike-triggered average (Eqn 1 of the paper) subtracts each bar's time average and averages\n  over all spikes of the cell. Its length in time, 0.5 s (30 frames), is the claim's standard\n  choice (fig9d-rf-size-similar); the data set's example script uses the same window. Spikes in the\n  first 29 frames, which lack a full stimulus history, are left out, as the example script does\n  (a standard choice that cannot change a result).\n- The separation h(x, t) = b(x) a(t) (Eqn 2) has the two readings of fig9d-rf-size-similar:\n  \"svd\", the leading singular vectors, and \"peak\", h at the time and at the bar of its largest\n  absolute value.\n- Centre size is the full width at half maximum of |b(x)| around its peak, with linear\n  interpolation between bars (fig9d-rf-size-similar; the interpolation is its standard choice).\n- Time to peak is the time of the extremum of a(t) of largest absolute value (fig9e), at frame\n  resolution or with parabolic interpolation. Lag j (stimulus j frames before the frame of the\n  spike) is placed at (j + 0.5) frames, the convention of the example script; a constant offset\n  that is the same for every cell and cannot change a comparison.\n- The Linear-Nonlinear model (Eqn 3) and its fits follow fig9g-threshold-unaltered: generator\n  y = stimulus filtered by h, scaled to unit variance; N(y) = B below theta and B + G y\n  (\"printed\") or B + G (y - theta) (\"continuous\") above; least squares against the rate in bins of\n  one frame (\"frame\") or against the mean rate in 20 bins of y of equal count (\"binned\"). Theta is\n  searched on a grid of quantiles of y (a standard choice of resolution).\n- The 95% bands of the cumulative histograms have the three readings of the claims file's header:\n  \"binomial\" (pointwise, normal approximation), \"dkw\" (Dvoretzky-Kiefer-Wolfowitz) and\n  \"bootstrap\" (pointwise percentile bootstrap over cells, 1000 resamples, a standard number).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport zipfile\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\n\nARCHIVE = \"crcns\"\nDATASET_ID = \"ret-1\"\nDATASET_DOI = \"10.6080/K0RF5RZT\"\nVERSION = \"unversioned\"\nBASE_URL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/\"\nZIP_NAME = \"crcns_ret-1.zip\"\nZIP_MD5 = \"4b9390ddc51c72d6f66563cb02e48fe8\"   # from the data set's checksums.md5\nZIP_SIZE = 71871914\nPREFIX = \"crcns_ret-1/\"\n\nSTA_FRAMES = 30          # 0.5 s window, fig9d-rf-size-similar (standard choice)\nLN_BINS = 20             # fig9g-threshold-unaltered, reading (b)\nTHETA_GRID = 101         # quantiles of y searched for theta (standard choice of resolution)\nBOOTSTRAP = 1000         # resamples for the bootstrap band (standard choice)\n\n\n# --- loading -------------------------------------------------------------------\n\ndef open_zip() -> zipfile.ZipFile:\n    \"\"\"The data set's zip, opened in place over HTTP range requests.\"\"\"\n    f = fsspec.open(BASE_URL + ZIP_NAME, block_size=2**20).open()\n    return zipfile.ZipFile(f)\n\n\ndef read_text(name: str) -> str:\n    \"\"\"A small text file at the top of the data set (checksums.md5, filelist.txt).\"\"\"\n    with fsspec.open(BASE_URL + name, \"rt\") as f:\n        return f.read()\n\n\ndef ran1_bits(z: zipfile.ZipFile, nbits: int) -> np.ndarray:\n    \"\"\"The first nbits of ran1.bin as booleans, least significant bit of each byte first.\"\"\"\n    nbytes = (nbits + 7) // 8\n    with z.open(PREFIX + \"ran1.bin\") as f:\n        raw = np.frombuffer(f.read(nbytes), dtype=np.uint8)\n    return np.unpackbits(raw, bitorder=\"little\")[:nbits].astype(bool)\n\n\ndef ran1(seed: int, n: int) -> np.ndarray:\n    \"\"\"n uniform numbers from RAN1 (Numerical Recipes 2nd ed.), as the data set's ran1.m.\"\"\"\n    IA, IM, IQ, IR, NTAB = 16807, 2147483647, 127773, 2836, 32\n    NDIV = 1 + (IM - 1) // NTAB\n    iv = [0] * NTAB\n    s = -seed if seed < -1 else 1\n    for j in range(NTAB + 8, 0, -1):\n        k = s // IQ\n        s = IA * (s - k * IQ) - IR * k\n        if s < 0:\n            s += IM\n        if j <= NTAB:\n            iv[j - 1] = s\n    iy = iv[0]\n    out = np.empty(n)\n    for i in range(n):\n        k = s // IQ\n        s = IA * (s - k * IQ) - IR * k\n        if s < 0:\n            s += IM\n        j = iy // NDIV\n        iy = iv[j]\n        iv[j] = s\n        out[i] = min(iy / IM, 1.0 - 1.2e-7)\n    return out\n\n\ndef _cellstr(x):\n    return [np.atleast_1d(np.asarray(v, dtype=float)).ravel() for v in np.atleast_1d(x)]\n\n\ndef load_retinas(z: zipfile.ZipFile) -> list[dict]:\n    \"\"\"Every retina file: its info, its recordings and the spike times of each cell in each.\"\"\"\n    names = sorted(n for n in z.namelist() if n.startswith(PREFIX + \"Data/\") and n.endswith(\".mat\"))\n    out = []\n    for name in names:\n        m = sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True, struct_as_record=False)\n        di = m[\"datainfo\"]\n        stims = list(np.atleast_1d(m[\"stimulus\"]))\n        sp = m[\"spikes\"]\n        ncell = int(di.Ncell)\n        sp = np.asarray(sp, dtype=object).reshape(ncell, len(stims)) if len(stims) > 1 or ncell > 1 else None\n        if sp is None:\n            sp = np.empty((1, 1), dtype=object)\n            sp[0, 0] = m[\"spikes\"]\n        recs = []\n        for i, s in enumerate(stims):\n            p = s.param\n            recs.append({\n                \"index\": i, \"type\": str(s.type), \"onset\": float(s.onset), \"frame\": float(s.frame),\n                \"nframes\": int(s.Nframes), \"pixelsize\": float(s.pixelsize),\n                \"x\": int(p.x), \"y\": int(p.y), \"dx\": int(p.dx), \"dy\": int(p.dy), \"seed\": int(p.seed),\n                \"rec_no\": int(np.atleast_1d(di.RecNo)[i]),\n                \"start\": tuple(int(v) for v in np.atleast_2d(di.RecStartTime)[i]),\n                \"spikes\": [np.atleast_1d(np.asarray(sp[c, i], dtype=float)).ravel() for c in range(ncell)],\n            })\n        out.append({\n            \"file\": name.rsplit(\"/\", 1)[-1], \"retina\": name.rsplit(\"/\", 1)[-1][:-4],\n            \"date\": str(di.date), \"sample\": int(di.SmplNo), \"ncell\": ncell, \"animal\": str(di.animal),\n            \"experimenter\": str(di.experimenter), \"description\": str(di.description), \"recordings\": recs,\n        })\n    return out\n\n\ndef kind(rec: dict) -> str:\n    \"\"\"'vbars' (vertical bars, full height), 'hbars' (horizontal bars, full width) or 'checker'.\"\"\"\n    if rec[\"dy\"] == rec[\"y\"] and rec[\"dx\"] < rec[\"x\"]:\n        return \"vbars\"\n    if rec[\"dx\"] == rec[\"x\"] and rec[\"dy\"] < rec[\"y\"]:\n        return \"hbars\"\n    return \"checker\"\n\n\ndef bar_width_um(rec: dict) -> float:\n    return (rec[\"dx\"] if kind(rec) == \"vbars\" else rec[\"dy\"]) * rec[\"pixelsize\"]\n\n\ndef group(animal: str) -> str:\n    \"\"\"'mutant' for the KO labels without Bax, 'control' for WT, 'bax' for the KO on Bax -/-.\"\"\"\n    if animal.startswith(\"KO\") and \"bax\" in animal:\n        return \"bax\"\n    if animal.startswith(\"KO\"):\n        return \"mutant\"\n    if animal.startswith(\"WT\"):\n        return \"control\"\n    return \"unknown\"\n\n\n# --- stimulus and spikes ---------------------------------------------------------\n\ndef stimulus(rec: dict, bits: np.ndarray) -> np.ndarray:\n    \"\"\"The tiles by frames matrix (+1 light, -1 dark), float32, for frames 0 .. Nframes-2.\"\"\"\n    m = (rec[\"x\"] // rec[\"dx\"]) * (rec[\"y\"] // rec[\"dy\"])\n    n = rec[\"nframes\"] - 1\n    s = bits[: m * n].reshape(n, m).T\n    return np.where(s, np.float32(1), np.float32(-1))\n\n\ndef frame_edges(rec: dict) -> np.ndarray:\n    return rec[\"onset\"] + np.arange(rec[\"nframes\"]) * rec[\"frame\"]\n\n\ndef counts(rec: dict) -> np.ndarray:\n    \"\"\"Spike counts per frame (frames by cells), frames 0 .. Nframes-2, as the example script.\"\"\"\n    edges = frame_edges(rec)\n    return np.stack([np.histogram(t, edges)[0] for t in rec[\"spikes\"]], axis=1).astype(np.float32)\n\n\ndef sta(S: np.ndarray, C: np.ndarray, nlag: int = STA_FRAMES) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Spike-triggered averages, cells by tiles by lags, and the spikes used per cell.\n\n    Lag j is the stimulus j frames before the frame of the spike. Spikes in the first nlag - 1\n    frames are left out. Each tile's time average is subtracted from the stimulus.\n    \"\"\"\n    S = S - S.mean(axis=1, keepdims=True)\n    C = C.copy()\n    C[: nlag - 1] = 0\n    n = C.sum(axis=0)\n    N = S.shape[1]\n    h = np.empty((C.shape[1], S.shape[0], nlag), dtype=np.float64)\n    for j in range(nlag):\n        h[:, :, j] = (S[:, : N - j] @ C[j:]).T\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        h /= n[:, None, None]\n    return h, n\n\n\ndef separate(h: np.ndarray, reading: str) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"b(x) and a(t) from h (tiles by lags), reading 'svd' or 'peak'.\"\"\"\n    if not np.all(np.isfinite(h)) or not np.any(h):\n        return np.full(h.shape[0], np.nan), np.full(h.shape[1], np.nan)\n    if reading == \"svd\":\n        u, s, vt = np.linalg.svd(h, full_matrices=False)\n        b, a = u[:, 0] * s[0], vt[0]\n        # orient so that the extremum of a is positive; b then carries the sign of the centre\n        if a[np.argmax(np.abs(a))] < 0:\n            a, b = -a, -b\n        return b, a\n    if reading == \"peak\":\n        x0, t0 = np.unravel_index(np.argmax(np.abs(h)), h.shape)\n        return h[:, t0].copy(), h[x0, :].copy()\n    raise ValueError(reading)\n\n\ndef fwhm(b: np.ndarray, width_um: float) -> float:\n    \"\"\"Full width at half maximum of |b| around its peak, in um, linear interpolation between bars.\"\"\"\n    if not np.all(np.isfinite(b)):\n        return np.nan\n    v = np.abs(b)\n    i0 = int(np.argmax(v))\n    half = v[i0] / 2\n    left = i0\n    while left > 0 and v[left - 1] >= half:\n        left -= 1\n    right = i0\n    while right < len(v) - 1 and v[right + 1] >= half:\n        right += 1\n    # interpolate the crossings; at an edge of the stimulus the width stops there\n    xl = left - (v[left] - half) / (v[left] - v[left - 1]) if left > 0 else float(left)\n    xr = right + (v[right] - half) / (v[right] - v[right + 1]) if right < len(v) - 1 else float(right)\n    return (xr - xl) * width_um\n\n\ndef time_to_peak(a: np.ndarray, frame: float, reading: str) -> float:\n    \"\"\"Time (s) of the extremum of a(t) of largest absolute value; 'frame' or 'parabolic'.\"\"\"\n    if not np.all(np.isfinite(a)):\n        return np.nan\n    j = int(np.argmax(np.abs(a)))\n    off = 0.0\n    if reading == \"parabolic\" and 0 < j < len(a) - 1:\n        y0, y1, y2 = np.sign(a[j]) * a[j - 1 : j + 2]\n        den = y0 - 2 * y1 + y2\n        if den != 0:\n            off = 0.5 * (y0 - y2) / den\n    elif reading not in (\"frame\", \"parabolic\"):\n        raise ValueError(reading)\n    return (j + off + 0.5) * frame\n\n\ndef surround(b: np.ndarray, frac: float) -> bool:\n    \"\"\"A lobe of sign opposite to the centre peak on both flanks, deeper than frac of the peak.\"\"\"\n    if not np.all(np.isfinite(b)):\n        return False\n    i0 = int(np.argmax(np.abs(b)))\n    c = np.sign(b[i0]) * b / np.abs(b[i0])\n    if i0 == 0 or i0 == len(b) - 1:\n        return False\n    return bool(c[:i0].min() < -frac and c[i0 + 1 :].min() < -frac)\n\n\ndef generator(S: np.ndarray, h: np.ndarray) -> np.ndarray:\n    \"\"\"y(t) = sum over tiles and lags of h(x, j) s(x, t - j), cells by frames; NaN for t < nlag - 1.\"\"\"\n    S = S - S.mean(axis=1, keepdims=True)\n    ncell, m, nlag = h.shape\n    N = S.shape[1]\n    y = np.zeros((ncell, N), dtype=np.float64)\n    for j in range(nlag):\n        y[:, j:] += h[:, :, j].astype(np.float32) @ S[:, : N - j]\n    y[:, : nlag - 1] = np.nan\n    return y\n\n\ndef fit_ln(y: np.ndarray, rate: np.ndarray, fit: str, form: str) -> dict:\n    \"\"\"Fit N(y) to the rate (Hz); y is scaled here to unit variance (Z of Eqn 3).\"\"\"\n    ok = np.isfinite(y)\n    y, r = y[ok], rate[ok]\n    sd = y.std()\n    if not np.isfinite(sd) or sd == 0:\n        return {\"B\": np.nan, \"G\": np.nan, \"theta\": np.nan, \"sse\": np.nan}\n    y = (y - 0.0) / sd\n    if fit == \"binned\":\n        order = np.argsort(y, kind=\"stable\")\n        chunks = np.array_split(order, LN_BINS)\n        y = np.array([y[c].mean() for c in chunks])\n        r = np.array([r[c].mean() for c in chunks])\n    elif fit != \"frame\":\n        raise ValueError(fit)\n    grid = np.quantile(y, np.linspace(0.0, 1.0, THETA_GRID)[1:-1]) if fit == \"frame\" else \\\n        np.unique(np.concatenate([y, (y[1:] + y[:-1]) / 2]))[:-1]\n    best = None\n    for th in grid:\n        above = y >= th\n        g = np.where(above, y if form == \"printed\" else y - th, 0.0)\n        X = np.stack([np.ones_like(y), g], axis=1)\n        coef, *_ = np.linalg.lstsq(X, r, rcond=None)\n        sse = float(np.sum((X @ coef - r) ** 2))\n        if best is None or sse < best[\"sse\"]:\n            best = {\"B\": float(coef[0]), \"G\": float(coef[1]), \"theta\": float(th), \"sse\": sse}\n    return best\n\n\n# --- cumulative histograms and their bands ---------------------------------------\n\ndef ecdf(values: np.ndarray, grid: np.ndarray) -> np.ndarray:\n    v = np.sort(values)\n    return np.searchsorted(v, grid, side=\"right\") / len(v)\n\n\ndef band(values: np.ndarray, grid: np.ndarray, reading: str, rng=None) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Lower and upper 95% band of the cumulative histogram of values, evaluated on grid.\"\"\"\n    v = np.asarray(values, dtype=float)\n    v = v[np.isfinite(v)]\n    n = len(v)\n    F = ecdf(v, grid)\n    if reading == \"binomial\":\n        e = 1.96 * np.sqrt(F * (1 - F) / n)\n        lo, hi = F - e, F + e\n    elif reading == \"dkw\":\n        e = np.sqrt(np.log(2 / 0.05) / (2 * n))\n        lo, hi = F - e, F + e\n    elif reading == \"bootstrap\":\n        rng = rng if rng is not None else np.random.default_rng(0)\n        boots = np.empty((BOOTSTRAP, len(grid)))\n        for i in range(BOOTSTRAP):\n            boots[i] = ecdf(rng.choice(v, n, replace=True), grid)\n        lo, hi = np.percentile(boots, [2.5, 97.5], axis=0)\n    else:\n        raise ValueError(reading)\n    return np.clip(lo, 0, 1), np.clip(hi, 0, 1)\n\n\ndef compare_bands(mutant: np.ndarray, control: np.ndarray, reading: str, rng=None) -> dict:\n    \"\"\"Whether the two 95% bands separate anywhere, where, and which curve lies to the right.\n\n    The grid is every observed value of either group. 'mutant_right' counts grid points where the\n    mutant band lies wholly below the control band (mutant values larger); 'mutant_left' the\n    reverse.\n    \"\"\"\n    mutant = np.asarray(mutant, float)\n    control = np.asarray(control, float)\n    mutant, control = mutant[np.isfinite(mutant)], control[np.isfinite(control)]\n    grid = np.unique(np.concatenate([mutant, control]))\n    lm, hm = band(mutant, grid, reading, rng)\n    lc, hc = band(control, grid, reading, rng)\n    right = hm < lc\n    left = hc < lm\n    sep = right | left\n    return {\n        \"reading\": reading, \"n_mutant\": len(mutant), \"n_control\": len(control),\n        \"separate\": bool(sep.any()), \"points_separate\": int(sep.sum()), \"points\": len(grid),\n        \"mutant_right\": int(right.sum()), \"mutant_left\": int(left.sum()),\n        \"range\": (float(grid[sep].min()), float(grid[sep].max())) if sep.any() else None,\n    }\n"
}
```

```
File created successfully at: entries/crcns-ret-1-lefebvre-2008/ret1.py (file state is current in your context — no need to Read it back)
```

**Agent**

Making the LN fit closed-form and vectorised over theta, since it will run thousands of times.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-ret-1-lefebvre-2008/ret1.py",
 "old_string": "    y = (y - 0.0) / sd\n    if fit == \"binned\":\n        order = np.argsort(y, kind=\"stable\")\n        chunks = np.array_split(order, LN_BINS)\n        y = np.array([y[c].mean() for c in chunks])\n        r = np.array([r[c].mean() for c in chunks])\n    elif fit != \"frame\":\n        raise ValueError(fit)\n    grid = np.quantile(y, np.linspace(0.0, 1.0, THETA_GRID)[1:-1]) if fit == \"frame\" else \\\n        np.unique(np.concatenate([y, (y[1:] + y[:-1]) / 2]))[:-1]\n    best = None\n    for th in grid:\n        above = y >= th\n        g = np.where(above, y if form == \"printed\" else y - th, 0.0)\n        X = np.stack([np.ones_like(y), g], axis=1)\n        coef, *_ = np.linalg.lstsq(X, r, rcond=None)\n        sse = float(np.sum((X @ coef - r) ** 2))\n        if best is None or sse < best[\"sse\"]:\n            best = {\"B\": float(coef[0]), \"G\": float(coef[1]), \"theta\": float(th), \"sse\": sse}\n    return best",
 "new_string": "    y = y / sd\n    order = np.argsort(y, kind=\"stable\")\n    y, r = y[order], r[order].astype(float)\n    if fit == \"binned\":\n        chunks = np.array_split(np.arange(len(y)), LN_BINS)\n        y = np.array([y[c].mean() for c in chunks])\n        r = np.array([r[c].mean() for c in chunks])\n        grid = (y[1:] + y[:-1]) / 2      # every split between the 20 bin centres\n    elif fit == \"frame\":\n        grid = np.quantile(y, np.linspace(0.0, 1.0, THETA_GRID)[1:-1])\n    else:\n        raise ValueError(fit)\n    n = len(y)\n    # sums over the points at or above each theta, from cumulative sums of the sorted values\n    k0 = np.searchsorted(y, grid, side=\"left\")\n    def tail(v):\n        c = np.concatenate([[0.0], np.cumsum(v[::-1])])[::-1]\n        return c[k0]\n    k = n - k0\n    Sy, Syy, Sr_a, Syr = tail(y), tail(y * y), tail(r), tail(y * r)\n    Sr, Srr = r.sum(), (r * r).sum()\n    if form == \"printed\":\n        Sg, Sgg, Sgr = Sy, Syy, Syr\n    elif form == \"continuous\":\n        Sg = Sy - grid * k\n        Sgg = Syy - 2 * grid * Sy + grid ** 2 * k\n        Sgr = Syr - grid * Sr_a\n    else:\n        raise ValueError(form)\n    det = n * Sgg - Sg ** 2\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        B = (Sgg * Sr - Sg * Sgr) / det\n        G = (n * Sgr - Sg * Sr) / det\n    sse = Srr - B * Sr - G * Sgr\n    sse = np.where(np.abs(det) > 1e-12 * max(1.0, n * n), sse, np.inf)\n    i = int(np.argmin(sse))\n    return {\"B\": float(B[i]), \"G\": float(G[i]), \"theta\": float(grid[i]), \"sse\": float(sse[i])}"
}
```

```
The file entries/crcns-ret-1-lefebvre-2008/ret1.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1
rng=np.random.default_rng(1)
# synthetic LN check
y=rng.normal(size=50000); rate=np.where(y>0.5, 2+10*(y-0.5), 2)+rng.normal(0,0.5,50000)
for fit in ["frame","binned"]:
    for form in ["printed","continuous"]:
        print(fit,form,ret1.fit_ln(y,rate,fit,form))
# compare with lstsq brute
yy=y/y.std()
th=0.5/y.std()
print(ret1.fwhm(np.array([0,0,1,2,4,2,1,0,0.]),10), ret1.time_to_peak(np.array([0,1,3,2,0.]),1,"parabolic"))
EOF
```

```
frame printed {'B': 1.965130522774196, 'G': 6.686378253049226, 'theta': 0.7580163997306101, 'sse': 53834.50729693775}
frame continuous {'B': 2.0172846932042234, 'G': 10.068454595224255, 'theta': 0.5152750465028022, 'sse': 12526.767338937847}
binned printed {'B': 2.0869211310776232, 'G': 6.629803785891414, 'theta': 0.8325434288658855, 'sse': 15.155461936210543}
binned continuous {'B': 2.0163147532679386, 'G': 10.080536423495884, 'theta': 0.5157142966416699, 'sse': 0.03582509286383129}
20.0 2.6666666666666665
```

**Agent**

Synthetic checks pass: the continuous-form fit recovers the true parameters, and FWHM and parabolic interpolation give the expected values. Now an exploratory pass over the real data, with timing.

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1, time, pickle, os
t0=time.time()
z=ret1.open_zip(); rets=ret1.load_retinas(z)
print("loaded",time.time()-t0)
nmax=max((r["x"]//r["dx"])*(r["y"]//r["dy"])*r["nframes"] for R in rets for r in R["recordings"] if ret1.kind(r)!="checker")
bits=ret1.ran1_bits(z,nmax); print("bits",time.time()-t0, nmax)
res={}
for R in rets:
    for rec in R["recordings"]:
        if ret1.kind(rec)=="checker": continue
        t1=time.time()
        S=ret1.stimulus(rec,bits); C=ret1.counts(rec)
        h,n=ret1.sta(S,C)
        Cs=np.roll(C,C.shape[0]//2,axis=0); hn,_=ret1.sta(S,Cs)
        res[(R["retina"],rec["index"])]=dict(h=h,n=n,hn=hn)
        pk=np.abs(h).reshape(len(n),-1).max(1); pn=np.abs(hn).reshape(len(n),-1).max(1)
        print(R["retina"],rec["index"],ret1.kind(rec),ret1.bar_width_um(rec),R["animal"],"cells",len(n),"ratio med %.2f"%np.median(pk/pn), "n>2:",(pk/pn>2).sum(), "t %.1f"%(time.time()-t1))
pickle.dump(res,open(os.environ["TMPDIR"]+"/sta.pkl","wb"))
print("total",time.time()-t0)
EOF
```

```
loaded 4.828265190124512
bits 5.497635126113892 61476480
20080516_R1 0 vbars 8.3 KO (pax6) cells 7 ratio med 2.15 n>2: 4 t 1.6
20080516_R1 2 hbars 8.3 KO (pax6) cells 7 ratio med 1.21 n>2: 1 t 1.3
20080516_R2 0 vbars 8.3 KO (pax6) cells 34 ratio med 1.94 n>2: 16 t 2.6
20080516_R2 1 hbars 8.3 KO (pax6) cells 34 ratio med 1.73 n>2: 14 t 1.9
20080606_R1 0 vbars 8.3 KO (chx10) cells 4 ratio med 1.46 n>2: 0 t 1.0
20080606_R1 1 hbars 8.3 KO (chx10) cells 4 ratio med 1.20 n>2: 0 t 0.8
20080606_R2 0 vbars 8.3 KO (chx10) cells 6 ratio med 1.27 n>2: 0 t 1.2
20080606_R2 2 hbars 8.3 KO (chx10) cells 6 ratio med 1.14 n>2: 0 t 0.9
20080606_R3 0 vbars 8.3 KO (chx10) cells 1 ratio med 1.31 n>2: 0 t 0.8
20080606_R3 1 hbars 8.3 KO (chx10) cells 1 ratio med 1.18 n>2: 0 t 0.6
20080624_R1 0 vbars 16.6 WT (chx10 het) cells 37 ratio med 3.63 n>2: 30 t 0.9
20080624_R1 1 hbars 16.6 WT (chx10 het) cells 37 ratio med 2.83 n>2: 26 t 0.7
20080624_R2 0 vbars 16.6 KO (chx10) cells 26 ratio med 1.19 n>2: 4 t 0.7
20080624_R2 1 vbars 16.6 KO (chx10) cells 26 ratio med 1.92 n>2: 12 t 0.7
20080624_R3 0 vbars 16.6 KO (chx10) cells 38 ratio med 1.83 n>2: 18 t 0.9
20080624_R3 2 vbars 41.5 KO (chx10) cells 38 ratio med 2.40 n>2: 24 t 0.3
20080628_R2 0 vbars 16.6 KO (pax6) cells 40 ratio med 5.13 n>2: 38 t 1.2
20080628_R3 0 vbars 16.6 KO (pax6) cells 32 ratio med 1.75 n>2: 13 t 1.0
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1, pickle, os, collections
from scipy import stats
res=pickle.load(open(os.environ["TMPDIR"]+"/sta.pkl","rb"))
z=ret1.open_zip(); rets=ret1.load_retinas(z)
rows=[]
for R in rets:
    g=ret1.group(R["animal"])
    rec=[r for r in R["recordings"] if ret1.kind(r)=="vbars"][0]
    d=res[(R["retina"],rec["index"])]
    for c in range(R["ncell"]):
        h=d["h"][c]
        for sep in ["svd","peak"]:
            b,a=ret1.separate(h,sep)
            rows.append(dict(ret=R["retina"],g=g,c=c,sep=sep,fw=ret1.fwhm(b,ret1.bar_width_um(rec)),ttp=ret1.time_to_peak(a,rec["frame"],"frame"),
              rate=np.sum((rec["spikes"][c]>=rec["onset"])&(rec["spikes"][c]<rec["onset"]+rec["nframes"]*rec["frame"]))/(rec["nframes"]*rec["frame"]),
              snr=np.abs(h).max()/np.abs(d["hn"][c]).max()))
import pandas as pd
df=pd.DataFrame(rows)
print(df[df.sep=="svd"].groupby("g")[["fw","ttp","rate","snr"]].median())
print(df[df.sep=="svd"].groupby(["g","ret"])[["fw","ttp","rate","snr"]].median())
for sep in ["svd","peak"]:
  d=df[df.sep==sep]
  for q in ["fw","ttp","rate"]:
    m=d[d.g=="mutant"][q]; c=d[d.g=="control"][q]
    print(sep,q,m.median(),c.median(),stats.ks_2samp(m.dropna(),c.dropna()).pvalue,[ret1.compare_bands(m,c,r)["separate"] for r in ["binomial","dkw","bootstrap"]])
EOF
```

```
fw       ttp      rate       snr
g                                                
bax      195.820164  0.241702  9.725188  2.265676
control  156.197586  0.108367  9.017525  4.104671
mutant   116.411762  0.125039  3.818510  1.882628
                             fw       ttp       rate       snr
g       ret                                                   
bax     20080702_R1  195.820164  0.241702   9.725188  2.265676
control 20080624_R1  162.106234  0.108367  11.898996  3.629797
        20080628_R4  140.100211  0.108367   3.783579  4.762866
        20080628_R5  143.378750  0.125039   7.578652  4.048792
        20080628_R6  151.227954  0.091695  23.573240  6.799557
        20080628_R7  165.750302  0.108367   4.962328  4.502312
mutant  20080516_R1  118.218591  0.125038  15.854259  2.147336
        20080516_R2  100.430859  0.141710   4.881230  1.942621
        20080606_R1  115.283626  0.141710   2.051983  1.459881
        20080606_R2   62.705870  0.166718   2.858902  1.270616
        20080606_R3  256.557788  0.175054   5.784696  1.311904
        20080624_R2   31.396813  0.133374   1.946375  1.185967
        20080624_R3  123.712174  0.125039   2.804247  1.827629
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1, itertools, hashlib
z=ret1.open_zip(); rets=ret1.load_retinas(z)
# unit duplicates within a recording: fraction of spikes of the smaller train with a partner within 0.5 ms
for R in rets:
    for rec in R["recordings"]:
        sp=rec["spikes"]; hi=[]
        for a,b in itertools.combinations(range(len(sp)),2):
            x,y=sp[a],sp[b]
            if len(x)==0 or len(y)==0: continue
            s,l=(x,y) if len(x)<=len(y) else (y,x)
            i=np.searchsorted(l,s); i=np.clip(i,1,len(l)-1)
            d=np.minimum(np.abs(l[i]-s),np.abs(l[i-1]-s))
            f=(d<0.0005).mean()
            if f>0.2: hi.append((a,b,round(f,2),len(x),len(y)))
        if hi: print(R["retina"],rec["index"],hi)
        # sorted / ranges
        for c,t in enumerate(sp):
            if len(t) and (np.any(np.diff(t)<0)): print("unsorted",R["retina"],rec["index"],c)
# identical trains across all recordings
seen={}
for R in rets:
    for rec in R["recordings"]:
        for c,t in enumerate(rec["spikes"]):
            k=hashlib.md5(np.round(t,5).tobytes()).hexdigest()
            if len(t)>0: seen.setdefault(k,[]).append((R["retina"],rec["index"],c,len(t)))
print([v for v in seen.values() if len(v)>1])
# empty trains
for R in rets:
    for rec in R["recordings"]:
        e=[c for c,t in enumerate(rec["spikes"]) if len(t)==0]
        if e: print("empty",R["retina"],rec["index"],e)
# spike times relative to stimulus end
for R in rets:
    for rec in R["recordings"]:
        end=rec["onset"]+rec["nframes"]*rec["frame"]
        mx=max(t.max() for t in rec["spikes"] if len(t)); mn=min(t.min() for t in rec["spikes"] if len(t))
        print(R["retina"],rec["index"],ret1.kind(rec),"onset %.2f end %.2f spikes %.3f-%.2f frame %.6f"%(rec["onset"],end,mn,mx,rec["frame"]), rec["start"])
EOF
```

```
20080516_R2 0 [(9, 11, np.float64(0.98), 16827, 13621), (27, 32, np.float64(0.99), 38735, 42602)]
20080516_R2 1 [(9, 11, np.float64(0.99), 12727, 11288), (27, 32, np.float64(0.99), 28488, 29628)]
20080516_R2 2 [(9, 11, np.float64(0.99), 13547, 11432), (18, 21, np.float64(0.23), 12571, 565), (27, 32, np.float64(0.97), 23361, 23785)]
20080606_R2 0 [(3, 4, np.float64(0.97), 3757, 3711)]
20080606_R2 1 [(3, 4, np.float64(0.93), 8747, 5437)]
20080624_R1 2 [(6, 7, np.float64(0.23), 12974, 148)]
20080624_R2 0 [(11, 20, np.float64(0.97), 1895, 1624)]
20080624_R2 1 [(11, 20, np.float64(1.0), 4043, 4081)]
20080624_R2 2 [(11, 20, np.float64(1.0), 6157, 6204)]
20080624_R3 0 [(22, 25, np.float64(0.96), 2625, 2785), (24, 28, np.float64(0.96), 1118, 1198), (24, 37, np.float64(0.94), 1118, 1547), (26, 31, np.float64(1.0), 3624, 3554), (28, 37, np.float64(0.93), 1198, 1547)]
20080624_R3 1 [(22, 25, np.float64(0.97), 2734, 2733), (24, 28, np.float64(0.96), 1844, 1827), (24, 37, np.float64(0.94), 1844, 1796), (26, 31, np.float64(1.0), 1213, 1203), (28, 37, np.float64(0.97), 1827, 1796)]
20080624_R3 2 [(22, 25, np.float64(0.98), 1092, 1128), (24, 28, np.float64(0.97), 391, 395), (24, 37, np.float64(0.95), 391, 406), (26, 31, np.float64(1.0), 251, 247), (28, 37, np.float64(0.97), 395, 406)]
20080628_R2 0 [(2, 4, np.float64(0.92), 14761, 14258), (22, 26, np.float64(0.95), 18353, 18281)]
20080628_R3 0 [(13, 18, np.float64(1.0), 9553, 9955)]
20080628_R3 1 [(13, 18, np.float64(0.99), 9762, 10215)]
unsorted 20080628_R4 0 0
unsorted 20080628_R4 0 1
unsorted 20080628_R4 0 3
unsorted 20080628_R4 0 4
unsorted 20080628_R4 0 5
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1
z=ret1.open_zip(); rets=ret1.load_retinas(z)
R={r["retina"]:r for r in rets}
t=R["20080628_R4"]["recordings"][0]["spikes"][0]
d=np.diff(t); i=np.where(d<0)[0]; print(len(t), len(i), i[:10], t[i[:5]], t[i[:5]+1], d[d<0][:10])
bits=ret1.ran1_bits(z, 80*60*96000)
for name in ["20080702_R4","20080606_R1","20080606_R2","20080606_R3","20080702_R1","20080628_R4"]:
    for rec in R[name]["recordings"]:
        S=ret1.stimulus(rec,bits); C=ret1.counts(rec)
        h,n=ret1.sta(S,C,nlag=15); hn,_=ret1.sta(S,np.roll(C,C.shape[0]//2,axis=0),nlag=15)
        pk=np.abs(h).reshape(len(n),-1).max(1); pn=np.abs(hn).reshape(len(n),-1).max(1)
        lag=[np.unravel_index(np.argmax(np.abs(x)),x.shape)[1] for x in h]
        print(name,rec["index"],ret1.kind(rec),"ratios",np.round(pk/pn,2)[:12],"lags",lag[:12])
EOF
```

```
13793 1 [13222] [1439.8349] [720.0203] [-719.8146]
20080702_R4 0 vbars ratios [0.99 0.96 1.19 0.93 1.01 0.77 1.03 0.94 0.86 1.05 1.08 1.08] lags [np.int64(10), np.int64(6), np.int64(1), np.int64(5), np.int64(13), np.int64(14), np.int64(9), np.int64(13), np.int64(13), np.int64(1), np.int64(11), np.int64(14)]
20080702_R4 1 checker ratios [5.39 3.92 4.64 3.83 3.06 3.44 4.52 4.12 2.95 3.78 4.35 5.04] lags [np.int64(4), np.int64(4), np.int64(4), np.int64(9), np.int64(4), np.int64(5), np.int64(4), np.int64(5), np.int64(4), np.int64(5), np.int64(4), np.int64(4)]
20080606_R1 0 vbars ratios [1.02 1.21 1.7  1.74] lags [np.int64(6), np.int64(9), np.int64(9), np.int64(8)]
20080606_R1 1 hbars ratios [1.02 1.19 1.39 1.3 ] lags [np.int64(8), np.int64(7), np.int64(7), np.int64(8)]
20080606_R1 2 checker ratios [1.19 1.88 2.98 1.18] lags [np.int64(6), np.int64(7), np.int64(7), np.int64(13)]
20080606_R2 0 vbars ratios [1.34 1.02 1.86 1.15 1.17 2.19] lags [np.int64(9), np.int64(9), np.int64(5), np.int64(10), np.int64(10), np.int64(10)]
20080606_R2 1 checker ratios [1.93 3.04 3.35 1.76 2.4  2.03] lags [np.int64(9), np.int64(10), np.int64(7), np.int64(8), np.int64(10), np.int64(10)]
20080606_R2 2 hbars ratios [1.33 0.93 1.6  0.94 1.31 1.15] lags [np.int64(9), np.int64(14), np.int64(7), np.int64(8), np.int64(9), np.int64(8)]
20080606_R3 0 vbars ratios [1.15] lags [np.int64(9)]
20080606_R3 1 hbars ratios [1.18] lags [np.int64(11)]
20080606_R3 2 checker ratios [1.61] lags [np.int64(9)]
20080702_R1 0 vbars ratios [2.37 2.51 0.9 ] lags [np.int64(13), np.int64(13), np.int64(12)]
20080702_R1 1 checker ratios [5.6  8.26 1.08] lags [np.int64(4), np.int64(4), np.int64(14)]
20080628_R4 0 vbars ratios [6.1  2.76 5.51 6.67 1.21 9.42 5.29 3.44 1.07 5.61 2.7  2.33] lags [np.int64(6), np.int64(8), np.int64(5), np.int64(5), np.int64(7), np.int64(4), np.int64(7), np.int64(6), np.int64(5), np.int64(7), np.int64(9), np.int64(7)]
20080628_R4 1 checker ratios [6.8  3.38 5.39 6.76 1.6  6.97 6.64 6.99 1.42 7.72
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1
z=ret1.open_zip(); rets=ret1.load_retinas(z)
for R in rets:
    for rec in R["recordings"]:
        segs=[]
        for c,t in enumerate(rec["spikes"]):
            i=np.where(np.diff(t)<0)[0]
            if len(i):
                b=np.split(t,i+1)
                segs.append((c,[(len(x),round(x[0],2),round(x[-1],2)) for x in b]))
        if segs: print(R["retina"],rec["index"],ret1.kind(rec),"end %.1f"%(rec["onset"]+rec["nframes"]*rec["frame"]),len(segs),"cells; e.g.",segs[:3])
EOF
```

```
20080628_R4 0 vbars end 1500.0 14 cells; e.g. [(0, [(13223, np.float64(0.03), np.float64(1439.83)), (570, np.float64(720.02), np.float64(779.99))]), (1, [(5242, np.float64(1.29), np.float64(1440.0)), (369, np.float64(720.36), np.float64(779.69))]), (3, [(31355, np.float64(0.03), np.float64(1439.89)), (1404, np.float64(720.03), np.float64(779.99))])]
20080628_R4 1 checker end 1500.0 15 cells; e.g. [(0, [(12704, np.float64(0.17), np.float64(1439.91)), (305, np.float64(720.06), np.float64(779.87))]), (1, [(11079, np.float64(2.14), np.float64(1439.94)), (668, np.float64(720.05), np.float64(779.66))]), (2, [(18789, np.float64(0.15), np.float64(1439.98)), (825, np.float64(720.02), np.float64(779.98))])]
20080628_R5 1 checker end 1201.0 15 cells; e.g. [(0, [(22594, np.float64(0.08), np.float64(1199.99)), (2, np.float64(2.05), np.float64(2.06))]), (3, [(13316, np.float64(1.33), np.float64(1199.97)), (2, np.float64(2.0), np.float64(2.02))]), (5, [(13183, np.float64(1.3), np.float64(1199.98)), (1, np.float64(2.05), np.float64(2.05))])]
20080628_R6 0 vbars end 1497.0 11 cells; e.g. [(0, [(33643, np.float64(0.04), np.float64(1439.97)), (1630, np.float64(720.05), np.float64(779.71))]), (3, [(21809, np.float64(1.03), np.float64(1439.83)), (951, np.float64(720.03), np.float64(776.25))]), (4, [(36706, np.float64(0.03), np.float64(1439.89)), (1200, np.float64(720.02), np.float64(779.76))])]
20080628_R6 1 checker end 1500.0 13 cells; e.g. [(0, [(40241, np.float64(0.37), np.float64(1439.92)), (1211, np.float64(720.01), np.float64(779.94))]), (1, [(31507, np.float64(0.04), np.float64(1439.99)), (1382, np.float64(720.01), np.float64(780.0))]), (2, [(46025, np.float64(0.1), np.float64(1439.98)), (1837, np.float64(720.08), np.float64(779.99))])]
20080702_R1 0 vbars end 1499.8 2 cells; e.g. [(1, [(22126, np.float64(0.39), np.float64(1439.84)), (831, np.float64(720.02), np.float64(779.56))]), (2, [(2768, np.float64(1.3), np.float64(1439.32)), (112, np.float64(722.04), np.float64(779.37))])]
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1, copy
z=ret1.open_zip(); rets=ret1.load_retinas(z)
R={r["retina"]:r for r in rets}
bits=ret1.ran1_bits(z, 640*96000)
def ratio(rec,spk):
    r=dict(rec); r["spikes"]=spk
    S=ret1.stimulus(r,bits); C=ret1.counts(r)
    h,n=ret1.sta(S,C,15); hn,_=ret1.sta(S,np.roll(C,C.shape[0]//2,axis=0),15)
    return np.round(np.abs(h).reshape(len(n),-1).max(1)/np.abs(hn).reshape(len(n),-1).max(1),2), n
for name in ["20080628_R4","20080628_R6","20080702_R1"]:
    rec=R[name]["recordings"][0]
    tails=[];heads=[]
    for t in rec["spikes"]:
        i=np.where(np.diff(t)<0)[0]
        if len(i): heads.append(t[:i[0]+1]); tails.append(t[i[0]+1:])
        else: heads.append(t); tails.append(np.array([]))
    for off in [0,720]:
        print(name,"tail +%d"%off, ratio(rec,[x+off for x in tails]))
    print(name,"head only",ratio(rec,heads)[0])
# 0702_R4: scan onset offset and frame
rec=R["20080702_R4"]["recordings"][0]
for frame in [rec["frame"],0.0166718]:
    for doff in [-1,-0.5,-0.1,0,0.1,0.5,1,2]:
        r=dict(rec); r["frame"]=frame; r["onset"]=rec["onset"]+doff
        r["spikes"]=[t[t<300] for t in rec["spikes"]]
        print("0702_R4 frame %.6f onset%+.1f"%(frame,doff), np.median(ratio(r,r["spikes"])[0]))
EOF
```

```
20080628_R4 tail +0 (array([0.73, 1.07,  nan, 0.91, 0.97, 1.09, 0.97, 0.9 , 1.21, 1.06, 1.06,
       0.9 , 0.96, 0.96, 1.15]), array([ 570.,  369.,    0., 1404.,   87., 1167.,  181.,  342.,  102.,
        197.,   64.,   19.,  727.,  822.,  247.], dtype=float32))
20080628_R4 tail +720 (array([1.4 , 0.92,  nan, 1.44, 0.95, 1.89, 1.42, 0.93, 0.95, 1.6 , 1.13,
       0.9 , 1.66, 1.31, 1.02]), array([ 570.,  369.,    0., 1404.,   87., 1166.,  181.,  342.,  102.,
        197.,   64.,   19.,  727.,  822.,  247.], dtype=float32))
20080628_R4 head only [6.02 2.58 5.51 6.71 1.22 9.19 5.45 3.63 0.95 5.5  2.44 2.29 6.96 4.85
 2.31]
20080628_R6 tail +0 (array([0.99,  nan,  nan, 1.12, 1.07, 1.14, 1.32, 1.17, 0.95, 1.1 , 1.01,
       1.09, 0.97]), array([1630.,    0.,    0.,  951., 1200., 1446., 1938.,  189., 1110.,
       2045., 1759., 2320., 1570.], dtype=float32))
20080628_R6 tail +720 (array([1.17,  nan,  nan, 1.38, 1.65, 1.34, 1.62, 1.41, 1.07, 1.14, 1.11,
       1.06, 2.07]), array([1615.,    0.,    0.,  951., 1185., 1393., 1919.,  189., 1064.,
       2022., 1752., 2170., 1565.], dtype=float32))
20080628_R6 head only [9.58 6.28 9.56 7.37 7.48 5.42 9.21 4.81 3.26 8.46 6.96 3.14 9.51]
20080702_R1 tail +0 (array([ nan, 0.85, 0.83]), array([  0., 831., 112.], dtype=float32))
20080702_R1 tail +720 (array([ nan, 0.95, 1.06]), array([  0., 831., 112.], dtype=float32))
20080702_R1 head only [2.37 2.68 0.86]
0702_R4 frame 0.016665 onset-1.0 1.04
0702_R4 frame 0.016665 onset-0.5 1.025
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1
z=ret1.open_zip(); rets=ret1.load_retinas(z)
R={r["retina"]:r for r in rets}
bits=ret1.ran1_bits(z, 640*96000)
rec=R["20080702_R4"]["recordings"][0]
for dx,dy,x,y in [(1,480,640,480),(4,480,640,480),(640,2,640,480),(640,1,640,480),(2,480,640,480)]:
    r=dict(rec); r.update(dx=dx,dy=dy,x=x,y=y); r["spikes"]=[t[t<600] for t in rec["spikes"]]
    S=ret1.stimulus(r,bits); C=ret1.counts(r)
    h,n=ret1.sta(S,C,15); hn,_=ret1.sta(S,np.roll(C,C.shape[0]//2,axis=0),15)
    print(dx,dy,np.round(np.abs(h).reshape(len(n),-1).max(1)/np.abs(hn).reshape(len(n),-1).max(1),2))
EOF
```

```
1 480 [0.99 1.18 1.16 1.22 1.24 1.08 1.14 1.17 1.09 0.9  1.01 0.81]
4 480 [1.03 0.97 0.91 1.11 1.03 0.87 1.18 0.83 0.83 0.92 0.96 0.9 ]
640 2 [1.19 0.99 1.05 0.93 0.83 1.   1.12 1.06 1.06 1.08 1.03 1.  ]
640 1 [0.94 1.02 0.91 1.07 1.04 1.11 0.91 1.01 0.89 1.02 0.96 1.2 ]
2 480 [1.14 1.08 1.43 1.39 0.95 1.04 0.89 1.1  1.19 0.92 1.08 1.1 ]
```

**Agent**

The bar stimulus of 20080702_R4 cannot be recovered under any tile layout I tried, so I'll record it as a finding. Now the questions file. Let me look at an existing one for the format.

**Agent calls Bash**

```bash
cd  ls questions; f=$(ls questions/*.yaml | head -1); head -40 $f; curl -sI https://crcnsarchive.s3-us-west-2.amazonaws.com/ret-1/crcns_ret-1.zip | grep -i -E "last-modified|etag"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -rn "questions" tools/*.py .github/workflows/*.yml docs/pipeline.md | head -30
```

```
tools/build_site.py:278:    (papers/manifest.yaml), each claims file's last check, and each attempt's open questions."""
tools/build_site.py:281:    checks, questions = {}, {}
tools/build_site.py:285:    for path in sorted((ROOT / "questions").glob("*.yaml")):
tools/build_site.py:287:        q = q.get("questions", []) if isinstance(q, dict) else q
tools/build_site.py:288:        questions[key_of_dir(path.stem)] = sum(1 for x in q if not x.get("answered"))
tools/build_site.py:289:    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions}
tools/build_site.py:424:                  ("attempt", "Attempt"), ("questions", "Questions"), ("verified", "Verified")]
tools/build_site.py:432:    inputs = data.get("pipeline") or {"papers": {}, "checks": {}, "questions": {}}
tools/build_site.py:442:        open_q = inputs["questions"].get(d, 0)
tools/build_site.py:454:            "questions": ("todo", f"{open_q} open") if open_q else ("none", ""),
tools/build_site.py:1007:CHART_STEPS = [(k, label) for k, label in PIPELINE_STEPS if k != "questions"]
tools/build_site.py:1068:  check, the attempt, the questions it raised, and verification. {len(waiting):,} targets are waiting on a person,
tools/datasets.py:9:files in the repository (claims/, questions/, transcripts/, attempt branches, the paper store) are
.github/workflows/attempt.yml:261:            paths=(attempts claims entries README.md); [ ! -d questions ] || paths+=(questions)
.github/workflows/attempt.yml:327:            allowed="^((attempts|claims|entries|questions)/.*$FOLDER|README\.md$)"
.github/workflows/papers.yml:6:# questions (`answer`). Started by hand from the Actions tab or with
.github/workflows/papers.yml:13:# claims/<folder>/ and questions/<folder>.yaml, and its transcript leaves out everything under
.github/workflows/papers.yml:236:          paths=("claims/$FOLDER"); [ ! -e "questions/$FOLDER.yaml" ] || paths+=("questions/$FOLDER.yaml")
.github/workflows/pap
[... 2 more lines not kept]
```

**Agent**

Writing the questions file (step 1.6): the one method detail that could change outcomes is which bar recording to use per retina.

**Agent calls Write**

```json
{
 "file_path": "questions/crcns-ret-1.yaml",
 "content": "questions:\n- claim: fig9d-rf-size-similar\n  question: Which flickering-bar recording of a retina gives a cell's spike-triggered average, its\n    firing rate and its LN fit? The data set holds, per retina, one or two recordings of vertical\n    bars (full height) at 8.3 or 16.6 um, and for six retinas also one of horizontal bars (full\n    width) at the same width; retina 20080624_R2 has two vertical-bar recordings at 16.6 um and\n    20080624_R3 one more at 41.5 um. The claims file names bars of 8.3 or 16.6 um but not their\n    orientation, nor what is done when a retina has more than one such recording. The same\n    question applies to fig9e-slower-time-course, fig9f-lower-firing-rate,\n    fig9g-threshold-unaltered, fig9h-gain-reduced and s3-receptive-field-surrounds. Tested here\n    under three readings, (A) the first vertical-bar recording at 8.3 or 16.6 um, (B) all\n    vertical-bar recordings at 8.3 or 16.6 um pooled (spikes and frames together), (C) the\n    horizontal-bar recording where the retina has one, otherwise as A.\n  passage: Methods, Electrophysiology, \"To map spatio-temporal receptive fields, we projected\n    gratings of adjacent thin bars (8.3 or 16.6 μm width). Each bar flickered black or white\n    according to a pseudo-random binary sequence (16.6 ms frame duration).\" Figure 9F legend,\n    \"Average firing rate observed during stimulation with flickering gratings.\"\n  why: The measures differ between recordings of the same cells (the receptive field profile\n    along a different axis, a different number of spikes and so a different noise level, a\n    different firing rate), and the readings change the six mutant and one control retina with\n    horizontal bars and the mutant retina with two vertical recordings, so a band comparison\n    near its limit could change.\n"
}
```

```
File created successfully at: questions/crcns-ret-1.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-ret-1-lefebvre-2008/ret1.py",
 "old_string": "# --- cumulative histograms and their bands ---------------------------------------",
 "new_string": "# --- recordings and per-cell measures --------------------------------------------\n\nREADINGS = (\"A\", \"B\", \"C\")\n\n\ndef bar_recordings(retina: dict, reading: str) -> list[dict]:\n    \"\"\"The flickering-bar recordings of 8.3 or 16.6 um used for a retina under a reading.\n\n    A: the first vertical-bar recording; B: all vertical-bar recordings, pooled; C: the\n    horizontal-bar recording where there is one, otherwise as A. The readings are this attempt's\n    (questions/crcns-ret-1.yaml); the claims file names the bar widths only.\n    \"\"\"\n    ok = [r for r in retina[\"recordings\"] if kind(r) != \"checker\" and round(bar_width_um(r), 1) in (8.3, 16.6)]\n    vb = [r for r in ok if kind(r) == \"vbars\"]\n    hb = [r for r in ok if kind(r) == \"hbars\"]\n    if reading == \"A\":\n        return vb[:1]\n    if reading == \"B\":\n        return vb\n    if reading == \"C\":\n        return hb[:1] if hb else vb[:1]\n    raise ValueError(reading)\n\n\ndef split_trains(rec: dict) -> list[tuple[np.ndarray, np.ndarray]]:\n    \"\"\"Each train as (head, tail): the spikes up to the first decrease of time, and the rest.\"\"\"\n    out = []\n    for t in rec[\"spikes\"]:\n        i = np.where(np.diff(t) < 0)[0]\n        out.append((t[: i[0] + 1], t[i[0] + 1 :]) if len(i) else (t, t[:0]))\n    return out\n\n\ndef with_tail_shift(rec: dict, offset: float) -> dict:\n    \"\"\"A copy of the recording whose trailing out-of-order segments are moved by offset seconds.\"\"\"\n    r = dict(rec)\n    r[\"spikes\"] = [np.concatenate([h, tl + offset]) for h, tl in split_trains(rec)]\n    return r\n\n\ndef in_window(rec: dict, t: np.ndarray) -> int:\n    return int(np.sum((t >= rec[\"onset\"]) & (t < rec[\"onset\"] + rec[\"nframes\"] * rec[\"frame\"])))\n\n\ndef measure_retina(retina: dict, recs: list[dict], bits: np.ndarray, ln: bool = True) -> list[dict]:\n    \"\"\"Every per-cell measure of the claims, from the recordings given (pooled when several).\n\n    Returns one dict per cell: spikes used, firing rate, the ratio of the STA's peak to that of a\n    null STA (spike counts circularly shifted by half the recording), FWHM, time to peak and\n    surround under each separation, LN parameters under each fit and form, and b(x) and a(t) of\n    the null STA's separation for reference.\n    \"\"\"\n    if not recs:\n        return []\n    ncell = retina[\"ncell\"]\n    hs, ns, nulls, data = [], [], [], []\n    spikes = np.zeros(ncell)\n    duration = 0.0\n    for rec in recs:\n        S = stimulus(rec, bits)\n        C = counts(rec)\n        h, n = sta(S, C)\n        hn, _ = sta(S, np.roll(C, C.shape[0] // 2, axis=0))\n        hs.append(h * n[:, None, None])\n        nulls.append(hn * n[:, None, None])\n        ns.append(n)\n        spikes += [in_window(rec, t) for t in rec[\"spikes\"]]\n        duration += rec[\"nframes\"] * rec[\"frame\"]\n        data.append((S, C) if ln else None)\n    n = np.sum(ns, axis=0)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        h = np.sum(hs, axis=0) / n[:, None, None]\n        hn = np.sum(nulls, axis=0) / n[:, None, None]\n    width = bar_width_um(recs[0])\n    frame = recs[0][\"frame\"]\n    out = []\n    ys = [generator(S, np.nan_to_num(h)) for S, _ in data] if ln else None\n    for c in range(ncell):\n        d = {\"retina\": retina[\"retina\"], \"animal\": retina[\"animal\"], \"group\": group(retina[\"animal\"]),\n             \"cell\": c, \"recordings\": \"+\".join(str(r[\"index\"]) for r in recs), \"kind\": kind(recs[0]),\n             \"bar_um\": round(width, 1), \"spikes_sta\": float(n[c]), \"rate_hz\": spikes[c] / duration}\n        pk, pn = np.nanmax(np.abs(h[c])) if n[c] else np.nan, np.nanmax(np.abs(hn[c])) if n[c] else np.nan\n        d[\"peak_ratio\"] = pk / pn if n[c] else np.nan\n        for sep in (\"svd\", \"peak\"):\n            b, a = separate(h[c], sep)\n            bn, _ = separate(hn[c], sep)\n            d[f\"fwhm_{sep}\"] = fwhm(b, width)\n            for pr in (\"frame\", \"parabolic\"):\n                d[f\"ttp_{sep}_{pr}\"] = time_to_peak(a, frame, pr)\n            for frac in (0.1, 0.2):\n                d[f\"surround_{sep}_{int(frac * 100)}\"] = surround(b, frac)\n                d[f\"null_surround_{sep}_{int(frac * 100)}\"] = surround(bn, frac)\n        if ln:\n            y = np.concatenate([yy[c] for yy in ys])\n            r = np.concatenate([C[:, c] / rec[\"frame\"] for (_, C), rec in zip(data, recs)])\n            for fit in (\"frame\", \"binned\"):\n                for form in (\"printed\", \"continuous\"):\n                    p = fit_ln(y, r, fit, form) if n[c] else {\"B\": np.nan, \"G\": np.nan, \"theta\": np.nan}\n                    d[f\"theta_{fit}_{form}\"] = p[\"theta\"]\n                    d[f\"gain_{fit}_{form}\"] = p[\"G\"]\n                    d[f\"base_{fit}_{form}\"] = p[\"B\"]\n        out.append(d)\n    return out\n\n\ndef duplicate_pairs(rec: dict, tol: float = 0.0005, frac: float = 0.5) -> list[tuple[int, int, float]]:\n    \"\"\"Pairs of units in a recording where more than frac of the smaller train has a spike of the\n    other within tol seconds (a standard check for one neuron sorted twice).\"\"\"\n    sp = [np.sort(t) for t in rec[\"spikes\"]]\n    out = []\n    for a in range(len(sp)):\n        for b in range(a + 1, len(sp)):\n            x, y = sp[a], sp[b]\n            if len(x) == 0 or len(y) == 0:\n                continue\n            s, l = (x, y) if len(x) <= len(y) else (y, x)\n            i = np.clip(np.searchsorted(l, s), 1, len(l) - 1)\n            d = np.minimum(np.abs(l[i] - s), np.abs(l[i - 1] - s))\n            f = float((d < tol).mean())\n            if f > frac:\n                out.append((a, b, f))\n    return out\n\n\n# --- cumulative histograms and their bands ---------------------------------------"
}
```

```
The file entries/crcns-ret-1-lefebvre-2008/ret1.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Running all three readings end to end to time them and preview the results.

**Agent calls Bash**

```bash
cd $TMPDIR && . ex/bin/activate && cd entries/crcns-ret-1-lefebvre-2008 && python - <<'EOF'
import numpy as np, ret1, time, pandas as pd, os
t0=time.time()
z=ret1.open_zip(); rets=ret1.load_retinas(z)
bits=ret1.ran1_bits(z, 640*96057)
rows=[]
for rd in ret1.READINGS:
    for R in rets:
        for d in ret1.measure_retina(R, ret1.bar_recordings(R,rd), bits):
            d["reading"]=rd; rows.append(d)
    print(rd, time.time()-t0)
df=pd.DataFrame(rows); df.to_pickle(os.environ["TMPDIR"]+"/meas.pkl")
pd.set_option("display.width",250); pd.set_option("display.max_columns",50)
print(df.groupby(["reading","group"]).median(numeric_only=True).T)
EOF
```

```
A 46.91159272193909
B 90.40600991249084
C 129.0860984325409
reading                             A                                        B                                        C                           
group                             bax       control       mutant           bax       control       mutant           bax       control       mutant
cell                         1.000000     12.000000    13.500000      1.000000     12.000000    13.500000      1.000000     12.000000    13.500000
bar_um                      16.600000     16.600000    16.600000     16.600000     16.600000    16.600000     16.600000     16.600000    16.600000
spikes_sta               14557.000000  10570.500000  3747.500000  14557.000000  10570.500000  5276.000000  14557.000000  10342.000000  3619.500000
rate_hz                      9.725188      9.017525     3.818510      9.725188      9.017525     4.030618      9.725188      8.946737     3.430130
peak_ratio                   2.265676      4.104671     1.882628      2.265676      4.104671     2.105729      2.265676      3.795271     1.699820
fwhm_svd                   195.820164    156.197586   116.411762    195.820164    156.197586   123.173466    195.820164    166.503505   117.051563
ttp_svd_frame                0.241702      0.108367     0.125039      0.241702      0.108367     0.125039      0.241702      0.108367     0.141710
ttp_svd_parabolic            0.239652      0.111106     0.132783      0.239652      0.111106     0.129798      0.239652      0.111790     0.135708
surround_svd_10              1.000000      1.000000     1.000000      1.000000      1.000000     1.000000      1.000000      1.000000     1.000000
null_surround_svd_10         1.000000      1.000000     1.000000      1.000000      1.000000     1.000000      1.000000      1.000000     1.000000
surround_svd_20              1.000000      0.000000     1.000000      1.000000      0.000000     0.000000      1.000000      0.000000     1.000000
null_surround_svd_20         
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/make_nb.py <<'PYEOF'
import nbformat as nbf, sys
cells = []
def md(s): cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    cells.append(c)

md(open(sys.argv[1] + "/header.md").read())

code('''
import hashlib
import io
import re
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pypdf
import requests
from scipy import stats

import ret1

pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 300)
warnings.filterwarnings("ignore", category=RuntimeWarning)

started = time.time()
z = ret1.open_zip()
retinas = ret1.load_retinas(z)
by_name = {R["retina"]: R for R in retinas}
nbits = max((r["x"] // r["dx"]) * (r["y"] // r["dy"]) * r["nframes"] for R in retinas for r in R["recordings"])
bits = ret1.ran1_bits(z, nbits)
print(f"CRCNS {ret1.DATASET_ID} ({ret1.VERSION}, doi:{ret1.DATASET_DOI}): {len(retinas)} retina files and "
      f"{nbits:,} stimulus bits loaded in {time.time() - started:.0f} s")
''')

md('''
## Data check

Each check of the description against the values is stated under its output.
''')

code('''
# Integrity of the zip: its MD5, streamed in memory, against the data set's checksums.md5.
sums = dict(line.split()[::-1] for line in ret1.read_text("checksums.md5").splitlines() if line.strip())
md5 = hashlib.md5()
with requests.get(ret1.BASE_URL + ret1.ZIP_NAME, stream=True, timeout=120) as r:
    for chunk in r.iter_content(2**20):
        md5.update(chunk)
print("checksums.md5:", sums)
print("MD5 of", ret1.ZIP_NAME, "as streamed:", md5.hexdigest(), "; matches checksums.md5:",
      md5.hexdigest() == sums[ret1.ZIP_NAME] == ret1.ZIP_MD5)
print("\\nMembers read (size in bytes and CRC-32 from the zip directory):")
for info in z.infolist():
    if info.filename.startswith(ret1.PREFIX) and not info.is_dir():
        print(f"  {info.filename:40s} {info.file_size:>10,d}  {info.CRC:08x}")
''', ["sanity"])

code('''
# The description's table of retinas against the files.
pdf = pypdf.PdfReader(io.BytesIO(requests.get(ret1.BASE_URL + "docs/crcns_ret-1_data_description.pdf", timeout=60).content))
text = "\\n".join(p.extract_text() for p in pdf.pages)
described = {m[0]: (int(m[1]), m[2].strip()) for m in re.findall(r"(\\d{8}_R\\d)\\s*\\(\\s*(\\d+) cells\\):\\s*([^\\n]+)", text)}
info = pd.DataFrame([{
    "retina": R["retina"], "label": R["animal"], "group": ret1.group(R["animal"]), "cells": R["ncell"],
    "described_cells": described.get(R["retina"], (None, None))[0],
    "described_label": described.get(R["retina"], (None, None))[1],
    "recordings": len(R["recordings"]),
    "stimuli": ", ".join(f"{ret1.kind(r)} {ret1.bar_width_um(r) if ret1.kind(r) != 'checker' else r['dx'] * r['pixelsize']:.1f} um "
                         f"{r['frame'] * 1000:.2f} ms x {r['nframes']}" for r in R["recordings"]),
} for R in retinas])
print(info.to_string(index=False))
print("\\nRetinas in the description:", len(described), "; files:", len(retinas))
print("Cell counts and labels agree with the description for every retina:",
      bool((info.cells == info.described_cells).all() and (info.label == info.described_label).all()))
print("\\nCells by label:"); print(info.groupby("label").cells.agg(["count", "sum"]).rename(columns={"count": "retinas", "sum": "cells"}).to_string())
print("\\nCells by group used here (mutant = KO without Bax, control = WT):")
print(info.groupby("group").cells.agg(["count", "sum"]).rename(columns={"count": "retinas", "sum": "cells"}).to_string())
print("\\nStimulus types in the data set:", sorted({r["type"] for R in retinas for r in R["recordings"]}))
print("Seeds:", sorted({r["seed"] for R in retinas for r in R["recordings"]}), "; pixel sizes (um):",
      sorted({r["pixelsize"] for R in retinas for r in R["recordings"]}))
print("Frame lengths (ms):", sorted({round(r["frame"] * 1000, 3) for R in retinas for r in R["recordings"]}))
print("Experimenter:", sorted({R["experimenter"] for R in retinas}), "; dates:", sorted({R["date"] for R in retinas}))
''', ["sanity"])

md('''
The 16 files match the description's table in cell counts and genotype labels. Every recording is
binary white noise drawn from RAN1 with seed -10000: vertical bars (full height), horizontal bars
(full width) or checkerboards. There are no flashing spots, flashes of different intensity, moving
bars or drifting gratings, so the stimuli of Figure 9A, 9B and 9C and of the rod and cone test
are not in the data set. The pixel size is 8.3 um as stated, so the bars are 8.3, 16.6 and (one
recording) 41.5 um wide, the widths the Methods give except the last. Frames last 16.67 ms (60 Hz)
for the bars, as the Methods state, and 33.3 ms for some checkerboards; two recordings of 20080702
state 16.665 and 16.669 ms.

The labels give 200 mutant cells in 10 retinas (Chx10-Cre 87, Pax6-Cre 113), 3 cells from one
Bax -/- mutant retina, and 122 control cells in 5 retinas, 95 of them labelled "chx10 het". The
paper's Figure 9 has 115 mutant and 143 control cells, and names its controls Pax6-Cre;
Pcdh-gamma +/f-del or Pcdh-gamma f-del/f-del without Cre; it names no Chx10-Cre heterozygous
controls. The files do not say which part of the Pax6-Cre retinas was recorded (the paper used
their peripheral region only), nor the age of the mice, nor the allele.
''')

code('''
# ran1.bin against the RAN1 generator of ran1.m, and the bit order.
check = ret1.ran1(-10000, 20000) >= 0.5
with z.open(ret1.PREFIX + "ran1.bin") as f:
    raw = np.frombuffer(f.read(2500), dtype=np.uint8)
for order in ("little", "big"):
    agree = (np.unpackbits(raw, bitorder=order)[:20000].astype(bool) == check).mean()
    print(f"first 20000 bits, {order}-endian bit order: {agree:.4f} agree with RAN1(seed -10000) >= 0.5")
print("ran1.bin holds", z.getinfo(ret1.PREFIX + "ran1.bin").file_size * 8, "bits; the longest stimulus needs", nbits)
''', ["sanity"])

code('''
# Spike times: units, order, and range against the stimulus window.
rows = []
for R in retinas:
    for rec in R["recordings"]:
        end = rec["onset"] + rec["nframes"] * rec["frame"]
        parts = ret1.split_trains(rec)
        tails = [tl for _, tl in parts if len(tl)]
        allt = np.concatenate([t for t in rec["spikes"] if len(t)])
        rows.append({"retina": R["retina"], "rec": rec["index"], "kind": ret1.kind(rec), "onset_s": round(rec["onset"], 2),
                     "stim_end_s": round(end, 1), "first_spike_s": round(allt.min(), 3), "last_spike_s": round(allt.max(), 1),
                     "spikes_after_end": int((allt > end).sum()),
                     "unsorted_trains": len(tails), "head_ends_s": round(max((h.max() for h, tl in parts if len(tl)), default=np.nan), 1),
                     "tail_span_s": (f"{min(t.min() for t in tails):.1f}-{max(t.max() for t in tails):.1f}" if tails else ""),
                     "tail_spikes": int(sum(len(t) for t in tails))})
spk = pd.DataFrame(rows)
print(spk.to_string(index=False))
print("\\nRecordings with out-of-order spike times:", int((spk.unsorted_trains > 0).sum()), "of", len(spk),
      "; trains affected:", int(spk.unsorted_trains.sum()), "; spikes in the out-of-order segments:", int(spk.tail_spikes.sum()))
''', ["sanity"])

code('''
# Where do the out-of-order segments belong? STA of the tail spikes alone, at their stored times and
# moved by 720 s (to 1440-1500 s, the part of the recording that has no spikes otherwise).
def peak_ratios(rec, trains, nlag=15):
    r = dict(rec); r["spikes"] = trains
    S, C = ret1.stimulus(r, bits), ret1.counts(r)
    h, n = ret1.sta(S, C, nlag)
    hn, _ = ret1.sta(S, np.roll(C, C.shape[0] // 2, axis=0), nlag)
    with np.errstate(invalid="ignore"):
        return np.abs(h).reshape(len(n), -1).max(1) / np.abs(hn).reshape(len(n), -1).max(1), n

tail_rows = []
for R in retinas:
    rec = R["recordings"][0]
    parts = ret1.split_trains(rec)
    if ret1.kind(rec) == "checker" or not any(len(tl) for _, tl in parts):
        continue
    stored, n = peak_ratios(rec, [tl for _, tl in parts])
    moved, _ = peak_ratios(rec, [tl + 720.0 for _, tl in parts])
    ok = n >= 50
    tail_rows.append({"retina": R["retina"], "rec": rec["index"], "cells_with_50_tail_spikes": int(ok.sum()),
                      "median_ratio_stored": round(float(np.median(stored[ok])), 2), "median_ratio_moved_720s": round(float(np.median(moved[ok])), 2),
                      "cells_higher_when_moved": int((moved[ok] > stored[ok]).sum())})
print(pd.DataFrame(tail_rows).to_string(index=False))
''', ["sanity"])

md('''
Spike times are in seconds from the start of each recording and begin before the stimulus onset
(about 1 s), as the example script assumes. In every recording that lasts 1500 s (the vertical bars
and checkerboards of 20080628_R4 and R6 and of 20080702_R1 and R4), the trains are not sorted:
they run from 0 to 1440 s and then hold a second segment of spikes between 720 and 780 s. The
recordings hold no spikes after 1440 s otherwise, though their stimulus runs to 1500 s. Moved by
720 s, to 1440 to 1500 s, these segments give higher STA peaks over the null than where they are
stored, in most cells of the larger retinas (table above). The segments are
consistent with the last minute of each recording stored with the wrong offset, but this is
not proven. The main analysis uses the spike times as deposited; a variant moves the segments.
(One checkerboard recording, 20080628_R5, has 1 or 2 spikes near 2 s out of order in several
cells; it is not used.)
''')

code('''
# Units sorted twice: pairs with more than half of the smaller train's spikes within 0.5 ms of the other's.
dups = []
for R in retinas:
    for rec in R["recordings"]:
        for a, b, f in ret1.duplicate_pairs(rec):
            dups.append({"retina": R["retina"], "rec": rec["index"], "group": ret1.group(R["animal"]), "unit_a": a, "unit_b": b, "coincident": round(f, 3)})
dups = pd.DataFrame(dups)
pairs = dups.groupby(["retina", "group", "unit_a", "unit_b"]).coincident.agg(["min", "max", "count"]).reset_index()
print(pairs.to_string(index=False))
print("\\nDistinct pairs:", len(pairs), "; by group:", pairs.groupby("group").size().to_dict())
# Each pair in the first vertical-bar recording, and the second unit dropped in the variant
first_vb = {R["retina"]: ret1.bar_recordings(R, "A")[0]["index"] for R in retinas}
drop = set()
for _, p in dups.iterrows():
    if p.rec == first_vb[p.retina]:
        drop.add((p.retina, int(p.unit_b)))
print("Units dropped in the variant without duplicates (second of each pair in the vertical-bar recording):", len(drop))
print("Identical spike trains in two files: none found" if len({(R["retina"], len(t), round(float(t.sum()), 3)) for R in retinas for t in R["recordings"][0]["spikes"]})
      == sum(R["ncell"] for R in retinas) else "some trains repeat across files")
''', ["sanity"])

md('''
No recording is deposited twice: no spike train repeats across files or units. Within recordings,
the pairs above share 70 to 100% of their spikes within 0.5 ms in every recording of the retina,
so each pair is most likely one neuron sorted twice. All units are kept in the main analysis, as
the claims count all units; a variant drops the second unit of each pair.
''')

code('''
# Clock: does the stimulus, rebuilt from its onset and frame length, line up with the spikes? Per
# recording, the STA peak over that of a null STA (spike counts circularly shifted by half the
# recording), and the lag of the STA peak. A response aligned to the stimulus gives ratios well
# above 1 at a consistent lag; misaligned timing gives ratios near 1.
clock = []
for R in retinas:
    for rec in R["recordings"]:
        if ret1.kind(rec) == "checker" and R["retina"] not in ("20080702_R4", "20080702_R1", "20080606_R1", "20080606_R2", "20080606_R3"):
            continue
        ratio, n = peak_ratios(rec, rec["spikes"], nlag=ret1.STA_FRAMES)
        S, C = ret1.stimulus(rec, bits), ret1.counts(rec)
        h, _ = ret1.sta(S, C)
        lag_ms = np.array([(np.unravel_index(np.nanargmax(np.abs(x)), x.shape)[1] + 0.5) * rec["frame"] * 1000 if n[i] else np.nan
                           for i, x in enumerate(h)])
        clock.append({"retina": R["retina"], "group": ret1.group(R["animal"]), "rec": rec["index"], "kind": ret1.kind(rec),
                      "cells": len(n), "median_ratio": round(float(np.nanmedian(ratio)), 2), "cells_ratio_above_2": int((ratio > 2).sum()),
                      "median_peak_lag_ms": round(float(np.nanmedian(lag_ms)), 0)})
clock = pd.DataFrame(clock)
print(clock.to_string(index=False))
''', ["sanity"])

md('''
For most bar recordings the STA peaks lie well above the null at lags of about 100 to 140 ms, so
the stimulus as rebuilt shares the clock of the spikes. The vertical bars of 20080702_R4 are the
exception: none of its 12 cells has an STA above the null (median ratio about 1), while the same
cells give clear STAs to the checkerboard of the same retina. Neither shifting the onset by up to 2
s, nor the usual 16.672 ms frame, nor other bar layouts, recovered a response while preparing (not
run here). So the stimulus of that recording cannot be rebuilt from its description, and its 12
mutant cells enter the main analysis with STAs of noise. The weak ratios of the three 20080606
retinas (all mutant) are matched by weak checkerboard STAs, so they are read as weak responses,
not as misalignment; the alignment there is consistent with the data, not shown. A variant
leaves out 20080702_R4.
''')

md('''
## Measures

Every per-cell measure, under each reading of which bar recording is used (A, B, C; see
`questions/crcns-ret-1.yaml`), and, under reading A, with the out-of-order spike segments moved by
720 s. The Bax -/- retina (3 cells) is measured but belongs to neither group: the paper did not use
Bax double mutants for Figure 9, and the claims define the groups without them.
''')

code('''
t0 = time.time()
rows = []
for reading in ret1.READINGS:
    for R in retinas:
        for d in ret1.measure_retina(R, ret1.bar_recordings(R, reading), bits):
            rows.append({"reading": reading, **d})
for R in retinas:
    recs = [ret1.with_tail_shift(r, 720.0) for r in ret1.bar_recordings(R, "A")]
    for d in ret1.measure_retina(R, recs, bits):
        rows.append({"reading": "A, segments moved", **d})
cells = pd.DataFrame(rows)
cells["duplicate"] = [(r, c) in drop for r, c in zip(cells.retina, cells.cell)]
print(f"measured in {time.time() - t0:.0f} s")
print(cells.groupby(["reading", "group"]).agg(cells=("cell", "size"), no_spikes=("spikes_sta", lambda s: int((s == 0).sum())),
                                              bar_um=("bar_um", lambda s: sorted(s.unique())), kind=("kind", lambda s: sorted(s.unique()))).to_string())
num = ["rate_hz", "peak_ratio", "fwhm_svd", "fwhm_peak", "ttp_svd_frame", "ttp_peak_frame", "theta_frame_continuous", "gain_frame_continuous"]
print("\\nRanges under reading A (min, max):")
print(cells[cells.reading == "A"].groupby("group")[num].agg(["min", "max"]).T.round(3).to_string())
''', ["sanity"])

code('''
GROUPS = ("mutant", "control")
CI = ("binomial", "dkw", "bootstrap")


def split(df, col):
    return df[df.group == "mutant"][col].to_numpy(float), df[df.group == "control"][col].to_numpy(float)


def judge(df, cols, rng, label=None):
    """For each measure column and CI reading: medians, KS test, and whether the 95% bands separate."""
    out = []
    for col in cols:
        m, c = split(df, col)
        m, c = m[np.isfinite(m)], c[np.isfinite(c)]
        ks = stats.ks_2samp(m, c)
        for ci in CI:
            r = ret1.compare_bands(m, c, ci, rng)
            out.append({**({"variant": label} if label else {}), "measure": col, "ci": ci, "n_mut": r["n_mutant"], "n_ctl": r["n_control"],
                        "median_mut": np.median(m), "median_ctl": np.median(c), "ks_p": ks.pvalue,
                        "separate": r["separate"], "mutant_larger_pts": r["mutant_right"], "mutant_smaller_pts": r["mutant_left"],
                        "sep_range": (f"{r['range'][0]:.3g} to {r['range'][1]:.3g}" if r["range"] else "")})
    return pd.DataFrame(out)


def by_retina(df, cols):
    return df[df.group.isin(GROUPS)].groupby(["group", "retina"])[cols].agg(["median", "size"]).round(3)


def variants(rng, cols):
    """The same comparison, reading A, on subsets and on the corrected spike times."""
    A = cells[cells.reading == "A"]
    sets = {
        "all units (main)": A,
        "without duplicate units": A[~A.duplicate],
        "without 20080702_R4": A[A.retina != "20080702_R4"],
        "out-of-order segments moved 720 s": cells[cells.reading == "A, segments moved"],
        "mutant Chx10-Cre only": A[(A.group == "control") | A.animal.str.contains("chx10") & (A.group == "mutant")],
        "mutant Pax6-Cre only": A[(A.group == "control") | A.animal.str.contains("pax6") & (A.group == "mutant")],
        "control Pax6-Cre het only": A[(A.group == "mutant") | (A.animal == "WT (pax6 het)")],
        "cells with STA peak ratio above 2": A[A.peak_ratio > 2],
        "16.6 um bars only": A[A.bar_um == 16.6],
    }
    return pd.concat([judge(d[d.group.isin(GROUPS)], cols, rng, label=k) for k, d in sets.items()], ignore_index=True)


def ecdf_plot(ax, df, col, title, xlabel, scale=1.0):
    for g, colour in (("mutant", "tab:red"), ("control", "black")):
        v = np.sort(df[df.group == g][col].dropna().to_numpy() * scale)
        ax.step(v, np.arange(1, len(v) + 1) / len(v), where="post", color=colour, label=f"{g} ({len(v)})")
        lo, hi = ret1.band(v, v, "binomial")
        ax.fill_between(v, lo, hi, step="post", color=colour, alpha=0.15)
    ax.set_title(title, fontsize=9); ax.set_xlabel(xlabel); ax.set_ylabel("cumulative fraction"); ax.legend(fontsize=8)
''')

# ---- claim sections
md('''
## fig9-cell-counts

> Figure 9C to 9H report 115 RGCs from mutant retinas and 143 RGCs from control retinas.
> Expected 115 (tolerance 11.5) mutant and 143 (14.3) control cells, counted as the units of the
> data set's mutant and control recordings, all units and units with a flicker response.
''')
code('''
A = cells[cells.reading == "A"]
counts = pd.DataFrame({
    "all units": A.groupby("group").size(),
    "units with spikes in the bar recording": A[A.spikes_sta > 0].groupby("group").size(),
    "STA peak ratio above 1.5": A[A.peak_ratio > 1.5].groupby("group").size(),
    "STA peak ratio above 2": A[A.peak_ratio > 2].groupby("group").size(),
    "all units without duplicates": A[~A.duplicate].groupby("group").size(),
}).fillna(0).astype(int)
counts.loc["mutant + bax"] = counts.loc["mutant"] + counts.loc["bax"]
print(counts.to_string())
print("\\nExpected: mutant 115 (103.5 to 126.5), control 143 (128.7 to 157.3)")
print("Mutant cells by Cre line:", A[A.group == "mutant"].animal.value_counts().to_dict())
print("Control cells by label:", A[A.group == "control"].animal.value_counts().to_dict())
print("No count of control units can exceed", int(counts.loc["control", "all units"]), "(all control units), below the lower bound 128.7")
''', ["claim:fig9-cell-counts"])
md('**Result: RESULT_COUNTS**')

md('''
## fig9d-rf-size-similar

> Receptive field centre size varies greatly among RGCs, but its distribution is similar in
> control and mutant retinas.

FWHM of |b(x)| (um), under the two separations of h and the three band readings, and the three
readings of which bar recording is used. A claim of absence: reproduced when the bands overlap
under every combination.
''')
code('''
rng = np.random.default_rng(904)
fw = pd.concat([judge(cells[(cells.reading == rd) & cells.group.isin(GROUPS)], ["fwhm_svd", "fwhm_peak"], rng).assign(recording=rd)
                for rd in ret1.READINGS], ignore_index=True)
print(fw.round(4).to_string(index=False))
print("\\nCombinations:", len(fw), "; bands separate in", int(fw.separate.sum()),
      "; of these with mutant at smaller sizes:", int((fw.separate & (fw.mutant_smaller_pts > 0) & (fw.mutant_larger_pts == 0)).sum()))
print("\\nSpread (5th to 95th percentile, um), reading A, svd:")
for g in GROUPS:
    v = cells[(cells.reading == "A") & (cells.group == g)].fwhm_svd.dropna()
    print(f"  {g}: {v.quantile(0.05):.1f} to {v.quantile(0.95):.1f}; cells at one bar width or less: {(v <= cells[(cells.reading == 'A') & (cells.group == g)].bar_um.loc[v.index]).sum()} of {len(v)}")
print("\\nBy retina (reading A):")
print(by_retina(cells[cells.reading == "A"], ["fwhm_svd", "fwhm_peak", "bar_um"]).to_string())
''', ["claim:fig9d-rf-size-similar"])
code('''
rng = np.random.default_rng(9041)
v = variants(rng, ["fwhm_svd", "fwhm_peak"])
print(v.round(4).to_string(index=False))
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
A = cells[cells.reading == "A"]
ecdf_plot(axes[0], A, "fwhm_svd", "Centre FWHM, reading A, svd (binomial band)", "um")
ecdf_plot(axes[1], A[A.peak_ratio > 2], "fwhm_svd", "Same, cells with STA peak ratio above 2", "um")
for ax in axes: ax.set_xlim(0, 600)
plt.tight_layout(); plt.show()
print("Cells beyond 600 um (not shown):", int((A.fwhm_svd > 600).sum()), "; all units:", int(A.fwhm_svd.notna().sum()))
''', ["claim:fig9d-rf-size-similar"])
md('**Result: RESULT_FIG9D**')

md('''
## s3-receptive-field-surrounds

> Some control and mutant RGCs have receptive field surrounds of opposite sign to the centre, so
> lateral inhibition functions in mutant circuits.

A lobe of b(x) of opposite sign to the centre on both flanks, deeper than 10% (a) or 20% (b) of
the centre peak. Reproduced when, under every reading, at least one mutant and one control cell
have one. The same rule applied to the null STA (spike counts shifted by half the recording) is
shown as the reference for noise.
''')
code('''
rows = []
for rd in ret1.READINGS:
    d = cells[(cells.reading == rd) & cells.group.isin(GROUPS)]
    for sep in ("svd", "peak"):
        for frac in (10, 20):
            for g in GROUPS:
                x = d[d.group == g]
                strong = x[x.peak_ratio > 2]
                rows.append({"recording": rd, "separation": sep, "depth_pct": frac, "group": g, "cells": len(x),
                             "with_surround": int(x[f"surround_{sep}_{frac}"].sum()),
                             "null_with_surround": int(x[f"null_surround_{sep}_{frac}"].sum()),
                             "ratio_above_2": len(strong), "ratio_above_2_with_surround": int(strong[f"surround_{sep}_{frac}"].sum())})
sur = pd.DataFrame(rows)
print(sur.to_string(index=False))
ok = sur.groupby(["recording", "separation", "depth_pct"]).with_surround.min()
print("\\nReadings in which both groups have at least one cell with a surround:", int((ok > 0).sum()), "of", len(ok))
print("By retina (reading A, svd, 20%):")
A = cells[(cells.reading == "A") & cells.group.isin(GROUPS)]
print(A.groupby(["group", "retina"]).agg(cells=("cell", "size"), surround=("surround_svd_20", "sum"), null=("null_surround_svd_20", "sum")).to_string())
''', ["claim:s3-receptive-field-surrounds"])
md('**Result: RESULT_S3**')

md('''
## fig9e-slower-time-course

> The time course of the light response is significantly slower in mutant retina, measured as
> the time to peak of the temporal integration function a(t).

Time to peak (s) of a(t), under both separations, both peak readings, the three band readings and
the three recording readings. Reproduced when under every combination the bands separate with the
mutant curve at longer times.
''')
code('''
rng = np.random.default_rng(905)
tcols = [f"ttp_{s}_{p}" for s in ("svd", "peak") for p in ("frame", "parabolic")]
tt = pd.concat([judge(cells[(cells.reading == rd) & cells.group.isin(GROUPS)], tcols, rng).assign(recording=rd)
                for rd in ret1.READINGS], ignore_index=True)
print(tt.round(4).to_string(index=False))
slower = tt.separate & (tt.mutant_larger_pts > 0) & (tt.mutant_smaller_pts == 0)
print("\\nCombinations:", len(tt), "; separate with mutant at longer times:", int(slower.sum()),
      "; separate the other way:", int((tt.separate & (tt.mutant_smaller_pts > 0)).sum()), "; overlap:", int((~tt.separate).sum()))
print("Median difference, mutant minus control (ms), range over combinations:",
      f"{(tt.median_mut - tt.median_ctl).min() * 1000:.1f} to {(tt.median_mut - tt.median_ctl).max() * 1000:.1f}; KS p at most {tt.ks_p.max():.2g}")
print("\\nBy retina (reading A):")
print(by_retina(cells[cells.reading == "A"], ["ttp_svd_frame", "ttp_svd_parabolic"]).to_string())
''', ["claim:fig9e-slower-time-course"])
code('''
rng = np.random.default_rng(9051)
v = variants(rng, ["ttp_svd_frame", "ttp_svd_parabolic"])
print(v.round(4).to_string(index=False))
fig, ax = plt.subplots(figsize=(5, 3.5))
A = cells[cells.reading == "A"]
ecdf_plot(ax, A, "ttp_svd_parabolic", "Time to peak of a(t), reading A, svd, parabolic", "ms", scale=1000)
plt.tight_layout(); plt.show()
print("Range shown (ms):", round(A.ttp_svd_parabolic.min() * 1000, 1), "to", round(A.ttp_svd_parabolic.max() * 1000, 1))
''', ["claim:fig9e-slower-time-course"])
md('**Result: RESULT_FIG9E**')

md('''
## fig9f-lower-firing-rate

> Mutant RGCs fire at much lower rates than control RGCs in response to flickering gratings.

Spike count over the duration of the flicker stimulus, per cell. Reproduced when the mutant curve
lies at lower rates and the bands separate under every band reading (and here every recording
reading).
''')
code('''
rng = np.random.default_rng(906)
fr = pd.concat([judge(cells[(cells.reading == rd) & cells.group.isin(GROUPS)], ["rate_hz"], rng).assign(recording=rd)
                for rd in ret1.READINGS], ignore_index=True)
fr["median_ratio_mut_ctl"] = fr.median_mut / fr.median_ctl
print(fr.round(4).to_string(index=False))
lower = fr.separate & (fr.mutant_smaller_pts > 0) & (fr.mutant_larger_pts == 0)
print("\\nCombinations:", len(fr), "; separate with mutant at lower rates:", int(lower.sum()))
print("\\nBy retina (reading A):")
print(by_retina(cells[cells.reading == "A"], ["rate_hz"]).to_string())
''', ["claim:fig9f-lower-firing-rate"])
code('''
rng = np.random.default_rng(9061)
v = variants(rng, ["rate_hz"])
v["median_ratio_mut_ctl"] = v.median_mut / v.median_ctl
print(v.round(4).to_string(index=False))
fig, ax = plt.subplots(figsize=(5, 3.5))
A = cells[cells.reading == "A"]
ecdf_plot(ax, A, "rate_hz", "Firing rate during flickering bars, reading A", "Hz")
ax.set_xscale("log"); plt.tight_layout(); plt.show()
print("Range (Hz):", round(A.rate_hz.min(), 3), "to", round(A.rate_hz.max(), 1), "; cells at 0 Hz (not on the log axis):", int((A.rate_hz == 0).sum()))
''', ["claim:fig9f-lower-firing-rate"])
md('**Result: RESULT_FIG9F**')

md('''
## fig9g-threshold-unaltered

> In a Linear-Nonlinear model fitted to the flicker responses, the response threshold of mutant
> RGCs is unaltered.

Theta (in units of the generator's standard deviation), under both fits, both forms, the three
band readings and the three recording readings. A claim of absence: reproduced when the bands
overlap under every combination.
''')
code('''
rng = np.random.default_rng(907)
lcols = [f"theta_{f}_{m}" for f in ("frame", "binned") for m in ("printed", "continuous")]
th = pd.concat([judge(cells[(cells.reading == rd) & cells.group.isin(GROUPS)], lcols, rng).assign(recording=rd)
                for rd in ret1.READINGS], ignore_index=True)
print(th.round(4).to_string(index=False))
print("\\nCombinations:", len(th), "; bands separate:", int(th.separate.sum()),
      "; with mutant at higher thresholds:", int((th.separate & (th.mutant_larger_pts > 0) & (th.mutant_smaller_pts == 0)).sum()),
      "; overlap:", int((~th.separate).sum()))
A = cells[(cells.reading == "A") & cells.group.isin(GROUPS)]
print("LN fits with no value (no spikes):", int(A.theta_frame_printed.isna().sum()), "of", len(A))
print("\\nBy retina (reading A):")
print(by_retina(cells[cells.reading == "A"], ["theta_frame_continuous", "theta_binned_continuous"]).to_string())
''', ["claim:fig9g-threshold-unaltered"])
code('''
rng = np.random.default_rng(9071)
v = variants(rng, ["theta_frame_continuous", "theta_binned_printed"])
print(v.round(4).to_string(index=False))
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
A = cells[cells.reading == "A"]
ecdf_plot(axes[0], A, "theta_frame_continuous", "Threshold, frame fit, continuous form", "theta (SD of y)")
ecdf_plot(axes[1], A, "theta_binned_printed", "Threshold, binned fit, printed form", "theta (SD of y)")
plt.tight_layout(); plt.show()
print("Ranges:", A.theta_frame_continuous.agg(["min", "max"]).round(2).tolist(), A.theta_binned_printed.agg(["min", "max"]).round(2).tolist())
''', ["claim:fig9g-threshold-unaltered"])
md('**Result: RESULT_FIG9G**')

md('''
## fig9h-gain-reduced

> In the same Linear-Nonlinear model, the gain of mutant RGCs is reduced.

G (Hz per standard deviation of the generator) from the same fits. Reproduced when under every
combination the mutant curve lies at lower gains and the bands separate.
''')
code('''
rng = np.random.default_rng(908)
gcols = [f"gain_{f}_{m}" for f in ("frame", "binned") for m in ("printed", "continuous")]
gn = pd.concat([judge(cells[(cells.reading == rd) & cells.group.isin(GROUPS)], gcols, rng).assign(recording=rd)
                for rd in ret1.READINGS], ignore_index=True)
gn["median_ratio_mut_ctl"] = gn.median_mut / gn.median_ctl
print(gn.round(4).to_string(index=False))
lower = gn.separate & (gn.mutant_smaller_pts > 0) & (gn.mutant_larger_pts == 0)
print("\\nCombinations:", len(gn), "; separate with mutant at lower gains:", int(lower.sum()),
      "; separate the other way:", int((gn.separate & (gn.mutant_larger_pts > 0)).sum()), "; overlap:", int((~gn.separate).sum()))
print("By form, combinations with mutant lower and separate:", gn.assign(lower=lower).groupby(gn.measure.str.split("_").str[-1]).lower.agg(["sum", "size"]).to_dict())
print("\\nBy retina (reading A):")
print(by_retina(cells[cells.reading == "A"], ["gain_frame_printed", "gain_frame_continuous"]).to_string())
''', ["claim:fig9h-gain-reduced"])
code('''
rng = np.random.default_rng(9081)
v = variants(rng, ["gain_frame_printed", "gain_frame_continuous"])
v["median_ratio_mut_ctl"] = v.median_mut / v.median_ctl
print(v.round(4).to_string(index=False))
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
A = cells[cells.reading == "A"]
ecdf_plot(axes[0], A, "gain_frame_printed", "Gain, frame fit, printed form", "G (Hz per SD of y)")
ecdf_plot(axes[1], A, "gain_frame_continuous", "Gain, frame fit, continuous form", "G (Hz per SD of y)")
for ax in axes: ax.set_xlim(-5, 150)
plt.tight_layout(); plt.show()
print("Ranges:", A.gain_frame_printed.agg(["min", "max"]).round(1).tolist(), A.gain_frame_continuous.agg(["min", "max"]).round(1).tolist(),
      "; cells outside -5 to 150 (printed, continuous):", int(((A.gain_frame_printed < -5) | (A.gain_frame_printed > 150)).sum()),
      int(((A.gain_frame_continuous < -5) | (A.gain_frame_continuous > 150)).sum()))
print(f"Run time of the notebook: {(time.time() - started) / 60:.1f} min")
''', ["claim:fig9h-gain-reduced"])
md('**Result: RESULT_FIG9H**')

md(open(sys.argv[1] + "/summary.md").read())

nb = nbf.v4.new_notebook(); nb.cells = cells
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
nbf.write(nb, sys.argv[2])
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open("make_nb.py").read()
old='''print("Identical spike trains in two files: none found" if len({(R["retina"], len(t), round(float(t.sum()), 3)) for R in retinas for t in R["recordings"][0]["spikes"]})
      == sum(R["ncell"] for R in retinas) else "some trains repeat across files")'''
new='''seen = {}
for R in retinas:
    for rec in R["recordings"]:
        for c, t in enumerate(rec["spikes"]):
            if len(t):
                seen.setdefault(hashlib.md5(np.sort(t).round(4).tobytes()).hexdigest(), []).append((R["retina"], rec["index"], c))
print("Spike trains that occur more than once, across all files, recordings and units:", sum(len(v) > 1 for v in seen.values()))'''
assert old in s; s=s.replace(old,new); open("make_nb.py","w").write(s)
EOF
echo "# header placeholder" > header.md; echo "## Summary
placeholder" > summary.md
cd entries/crcns-ret-1-lefebvre-2008
cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
pypdf
requests
scipy
EOF
. $TMPDIR/ex/bin/activate && python $TMPDIR/gen/make_nb.py $TMPDIR/gen reproduce_lefebvre_2008.ipynb && uv pip install -q nbconvert ipykernel nbformat 2>&1 | tail -1; time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/out.ipynb reproduce_lefebvre_2008.ipynb 2>&1 | tail -3
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/gen/make_nb.py", line 1, in <module>
    import nbformat as nbf, sys
ModuleNotFoundError: No module named 'nbformat'
Available subcommands: migrate troubleshoot trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.089s
user	0m0.076s
sys	0m0.015s
```

**Agent calls Bash**

```bash
. $TMPDIR/ex/bin/activate && uv pip install -q nbconvert ipykernel nbformat 2>&1 | tail -1; python $TMPDIR/gen/make_nb.py $TMPDIR/gen reproduce_lefebvre_2008.ipynb && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/out.ipynb reproduce_lefebvre_2008.ipynb 2>&1 | tail -3
```

```
[NbConvertApp] Converting notebook reproduce_lefebvre_2008.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 433312 bytes to /tmp/claude-1001/out.ipynb

real	4m37.846s
user	14m26.241s
sys	0m5.087s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
sel=sys.argv[2:] 
for i,c in enumerate(nb["cells"]):
    if c["cell_type"]!="code": continue
    tags=c["metadata"].get("tags",[])
    if sel and not any(s in t for s in sel for t in tags+[str(i)]): continue
    print(f"##### cell {i} {tags}")
    for o in c.get("outputs",[]):
        if "text" in o: print("".join(o["text"]))
        elif o.get("output_type")=="error": print(o["ename"],o["evalue"])
        elif "data" in o and "text/plain" in o["data"]: print("".join(o["data"]["text/plain"])[:300])
EOF
. $TMPDIR/ex/bin/activate; python $TMPDIR/show.py $TMPDIR/out.ipynb sanity
```

```
##### cell 3 ['sanity']
checksums.md5: {'crcns_ret-1.zip': '4b9390ddc51c72d6f66563cb02e48fe8', 'docs/crcns_ret-1_data_description.docx': '1b66fe25386b4d1cc14e66b6f719a985', 'docs/crcns_ret-1_data_description.pdf': 'eca35a17912488ad1ddf1e5231005aa5', 'filelist.txt': 'f7edda46d58d4b57d71f40b8bffc1a0c'}
MD5 of crcns_ret-1.zip as streamed: 4b9390ddc51c72d6f66563cb02e48fe8 ; matches checksums.md5: True

Members read (size in bytes and CRC-32 from the zip directory):
  crcns_ret-1/Analysis_example.m                2,729  6ea8dd24
  crcns_ret-1/Data/20080516_R1.mat          1,515,345  531bd383
  crcns_ret-1/Data/20080516_R2.mat          4,462,406  b9f975a5
  crcns_ret-1/Data/20080606_R1.mat            217,459  4685c94c
  crcns_ret-1/Data/20080606_R2.mat            425,996  815618ca
  crcns_ret-1/Data/20080606_R3.mat            112,553  b5feea39
  crcns_ret-1/Data/20080624_R1.mat          6,263,599  ba9d6008
  crcns_ret-1/Data/20080624_R2.mat          1,950,808  f5225245
  crcns_ret-1/Data/20080624_R3.mat          1,619,650  76043d56
  crcns_ret-1/Data/20080628_R2.mat          2,376,244  f958f564
  crcns_ret-1/Data/20080628_R3.mat          1,478,450  eb92fe7b
  crcns_ret-1/Data/20080628_R4.mat          1,854,783  496142bb
  crcns_ret-1/Data/20080628_R5.mat          4,919,162  a8593154
  crcns_ret-1/Data/20080628_R6.mat          4,834,679  2fffe4cf
  crcns_ret-1/Data/20080628_R7.mat            617,052  1b221e72
[... 194 more lines not kept]
```

**Agent**

Data checks all ran. Now the claim outputs:

**Agent calls Bash**

```bash
. $TMPDIR/ex/bin/activate; python $TMPDIR/show.py $TMPDIR/out.ipynb claim:fig9-cell claim:fig9d claim:s3
```

```
##### cell 18 ['claim:fig9-cell-counts']
              all units  units with spikes in the bar recording  STA peak ratio above 1.5  STA peak ratio above 2  all units without duplicates
group                                                                                                                                          
bax                   3                                       3                         2                       2                             3
control             122                                     122                       113                     107                           118
mutant              200                                     200                       126                      93                           189
mutant + bax        203                                     203                       128                      95                           192

Expected: mutant 115 (103.5 to 126.5), control 143 (128.7 to 157.3)
Mutant cells by Cre line: {'KO (pax6)': 113, 'KO (chx10)': 87}
Control cells by label: {'WT (chx10 het)': 95, 'WT (pax6 het)': 27}
No count of control units can exceed 122 (all control units), below the lower bound 128.7

##### cell 21 ['claim:fig9d-rf-size-similar']
  measure        ci  n_mut  n_ctl  median_mut  median_ctl   ks_p  separate  mutant_larger_pts  mutant_smaller_pts   sep_range recording
 fwhm_svd  binomial    200    122    116.4118    156.1976 0.0000      True                  0                 225 20.2 to 171         A
 fwhm_svd       dkw    200    122    116.4118    156.1976 0.0000      True                  0                 145 80.5 to 156         A
 fwhm_svd bootstrap    200    122    116.4118    156.1976 0.0000      True                  0                 226 20.2 to 171         A
fwhm_peak  binomial    200    122     93.6992    150.7826 0.0000      True                  0                 262 9.24 to 172         A
fwhm_peak       dkw    200    122     93.6992    150.7826 0.0000      True    
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/ex/bin/activate; python $TMPDIR/show.py $TMPDIR/out.ipynb claim:fig9e claim:fig9f | grep -v "^<Figure"
```

```
##### cell 28 ['claim:fig9e-slower-time-course']
           measure        ci  n_mut  n_ctl  median_mut  median_ctl  ks_p  separate  mutant_larger_pts  mutant_smaller_pts       sep_range recording
     ttp_svd_frame  binomial    200    122      0.1250      0.1084   0.0      True                 87                   0  0.075 to 0.392         A
     ttp_svd_frame       dkw    200    122      0.1250      0.1084   0.0      True                 41                   0 0.0917 to 0.158         A
     ttp_svd_frame bootstrap    200    122      0.1250      0.1084   0.0      True                 87                   0  0.075 to 0.392         A
 ttp_svd_parabolic  binomial    200    122      0.1328      0.1111   0.0      True                311                   0 0.0813 to 0.389         A
 ttp_svd_parabolic       dkw    200    122      0.1328      0.1111   0.0      True                226                   0  0.0974 to 0.16         A
 ttp_svd_parabolic bootstrap    200    122      0.1328      0.1111   0.0      True                311                   0 0.0812 to 0.389         A
    ttp_peak_frame  binomial    200    122      0.1250      0.1084   0.0      True                 76                   1  0.025 to 0.392         A
    ttp_peak_frame       dkw    200    122      0.1250      0.1084   0.0      True                 31                   0 0.0917 to 0.142         A
    ttp_peak_frame bootstrap    200    122      0.1250      0.1084   0.0      True                 76                   1  0.025 to 0.392         A
ttp_peak_parabolic  binomial    200    122      0.1258      0.1094   0.0      True                301                   1  0.028 to 0.395         A
ttp_peak_parabolic       dkw    200    122      0.1258      0.1094   0.0      True                207                   0    0.1 to 0.152         A
ttp_peak_parabolic bootstrap    200    122      0.1258      0.1094   0.0      True                300                   1  0.028 to 0.395         A
     ttp_svd_frame  binomia
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/ex/bin/activate; python $TMPDIR/show.py $TMPDIR/out.ipynb claim:fig9g claim:fig9h | grep -v "^<Figure"
```

```
<persisted-output>
Output too large (35.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/679a0e33-a61b-431a-ac52-8f9b495398df/tool-results/bjk3ydj4r.txt

Preview (first 2KB):
##### cell 36 ['claim:fig9g-threshold-unaltered']
                measure        ci  n_mut  n_ctl  median_mut  median_ctl   ks_p  separate  mutant_larger_pts  mutant_smaller_pts         sep_range recording
    theta_frame_printed  binomial    200    122      1.6851      0.0072 0.0000      True                270                   0     -2.26 to 2.25         A
    theta_frame_printed       dkw    200    122      1.6851      0.0072 0.0000      True                104                   0   0.00497 to 1.82         A
    theta_frame_printed bootstrap    200    122      1.6851      0.0072 0.0000      True                273                   0     -2.27 to 2.26         A
 theta_frame_continuous  binomial    200    122      1.1227      0.4360 0.0000      True                264                   0    -0.844 to 1.59         A
 theta_frame_continuous       dkw    200    122      1.1227      0.4360 0.0000      True                153                   0    0.0434 to 1.39         A
 theta_frame_continuous bootstrap    200    122      1.1227      0.4360 0.0000      True                264                   0    -0.893 to 1.59         A
   theta_binned_printed  binomial    200    122      1.8127     -0.0226 0.0000      True                247                   0     -1.73 to 1.93         A
   theta_binned_printed       dkw    200    122      1.8127     -0.0226 0.0000      True                134                   0   -0.0311 to 1.85         A
   theta_binned_printed bootstrap    200    122      1.8127     -0.0226 0.0000      True                245                   0     -1.73 to 1.93         A
theta_binned_continuous  binomial    200    122      1.0044      0.4730 0.0000      True                291                   0     -1.04 to 1.8
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/ex/bin/activate; python $TMPDIR/show.py $TMPDIR/out.ipynb claim:fig9g claim:fig9h | grep -v "^<Figure" | grep -E "#####|Combinations|By form|LN fits|Ranges|variant|ratio above 2|without|moved|only|main|^ +(gain|theta).*(A|B|C)$" | grep -E "#####|Combinations|By form|LN fits|Ranges|variant|ratio above 2|Pax6|main|frame_continuous|binned_continuous" | cut -c1-220
```

```
##### cell 36 ['claim:fig9g-threshold-unaltered']
 theta_frame_continuous  binomial    200    122      1.1227      0.4360 0.0000      True                264                   0    -0.844 to 1.59         A
 theta_frame_continuous       dkw    200    122      1.1227      0.4360 0.0000      True                153                   0    0.0434 to 1.39         A
 theta_frame_continuous bootstrap    200    122      1.1227      0.4360 0.0000      True                264                   0    -0.893 to 1.59         A
 theta_frame_continuous  binomial    200    122      0.9320      0.4360 0.0000      True                216                   0    -0.844 to 1.49         B
 theta_frame_continuous       dkw    200    122      0.9320      0.4360 0.0000      True                 66                   0    0.282 to 0.767         B
 theta_frame_continuous bootstrap    200    122      0.9320      0.4360 0.0000      True                219                   0     -0.893 to 1.5         B
 theta_frame_continuous  binomial    200    122      1.1852      0.3828 0.0000      True                263                   0    -0.818 to 1.71         C
 theta_frame_continuous       dkw    200    122      1.1852      0.3828 0.0000      True                192                   0    -0.184 to 1.43         C
 theta_frame_continuous bootstrap    200    122      1.1852      0.3828 0.0000      True                268                   0    -0.844 to 1.71         C
Combinations: 36 ; bands separate: 36 ; with mutant at higher thresholds: 36 ; overlap: 0
LN fits with no value (no spikes): 0 of 322
##### cell 37 ['claim:fig9g-threshold-unaltered']
                          variant                measure        ci  n_mut  n_ctl  median_mut  median_ctl   ks_p  separate  mutant_larger_pts  mutant_smaller_pts       sep_range
                 all units (main) theta_frame_continuous  binomial    200    122      1.1227      0.4360 0.0000      True                264                   0  -0.844 to 1.59
        
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open("make_nb.py").read()
old='''print("\\nBy retina (reading A):")
print(by_retina(cells[cells.reading == "A"], ["ttp_svd_frame", "ttp_svd_parabolic"]).to_string())'''
new='''print("Combinations that also separate the other way:")
print(tt[tt.separate & (tt.mutant_smaller_pts > 0)][["recording", "measure", "ci", "mutant_larger_pts", "mutant_smaller_pts"]].to_string(index=False))
for rd in ret1.READINGS:
    d = cells[(cells.reading == rd) & cells.group.isin(GROUPS)]
    fast = d[d.ttp_peak_frame < 0.03]
    print(f"  reading {rd}: cells with time to peak (peak separation) below 30 ms: "
          f"{fast.groupby('group').size().to_dict()}; their STA peak ratios {np.round(np.sort(fast.peak_ratio.to_numpy()), 2).tolist()}")
print("\\nBy retina (reading A):")
print(by_retina(cells[cells.reading == "A"], ["ttp_svd_frame", "ttp_svd_parabolic"]).to_string())'''
assert old in s; s=s.replace(old,new)
s=s.replace("md('**Result: RESULT_COUNTS**')","md(R['COUNTS'])").replace("md('**Result: RESULT_FIG9D**')","md(R['FIG9D'])").replace("md('**Result: RESULT_S3**')","md(R['S3'])").replace("md('**Result: RESULT_FIG9E**')","md(R['FIG9E'])").replace("md('**Result: RESULT_FIG9F**')","md(R['FIG9F'])").replace("md('**Result: RESULT_FIG9G**')","md(R['FIG9G'])").replace("md('**Result: RESULT_FIG9H**')","md(R['FIG9H'])")
s=s.replace("cells = []\n","cells = []\nimport re as _re\nR = dict(_re.findall(r'^@@ (\\w+)\\n(.*?)(?=^@@ |\\Z)', open(sys.argv[1] + '/results.md').read(), _re.S | _re.M))\nR = {k: v.strip() for k, v in R.items()}\n",1)
open("make_nb.py","w").write(s)
EOF
grep -n "RESULT_\|R\['" make_nb.py | head
```

```
Traceback (most recent call last):
  File "<stdin>", line 13, in <module>
AssertionError
359:md('**Result: RESULT_COUNTS**')
397:md('**Result: RESULT_FIG9D**')
431:md('**Result: RESULT_S3**')
467:md('**Result: RESULT_FIG9E**')
500:md('**Result: RESULT_FIG9F**')
537:md('**Result: RESULT_FIG9G**')
577:md('**Result: RESULT_FIG9H**')
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/gen/make_nb.py",
 "offset": 450,
 "limit": 20
}
```

```
450	print("\\nCombinations:", len(tt), "; separate with mutant at longer times:", int(slower.sum()),
451	      "; separate the other way:", int((tt.separate & (tt.mutant_smaller_pts > 0)).sum()), "; overlap:", int((~tt.separate).sum()))
452	print("Median difference, mutant minus control (ms), range over combinations:",
453	      f"{(tt.median_mut - tt.median_ctl).min() * 1000:.1f} to {(tt.median_mut - tt.median_ctl).max() * 1000:.1f}; KS p at most {tt.ks_p.max():.2g}")
454	print("\\nBy retina (reading A):")
455	print(by_retina(cells[cells.reading == "A"], ["ttp_svd_frame", "ttp_svd_parabolic"]).to_string())
456	''', ["claim:fig9e-slower-time-course"])
457	code('''
458	rng = np.random.default_rng(9051)
459	v = variants(rng, ["ttp_svd_frame", "ttp_svd_parabolic"])
460	print(v.round(4).to_string(index=False))
461	fig, ax = plt.subplots(figsize=(5, 3.5))
462	A = cells[cells.reading == "A"]
463	ecdf_plot(ax, A, "ttp_svd_parabolic", "Time to peak of a(t), reading A, svd, parabolic", "ms", scale=1000)
464	plt.tight_layout(); plt.show()
465	print("Range shown (ms):", round(A.ttp_svd_parabolic.min() * 1000, 1), "to", round(A.ttp_svd_parabolic.max() * 1000, 1))
466	''', ["claim:fig9e-slower-time-course"])
467	md('**Result: RESULT_FIG9E**')
468	
469	md('''
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1001/gen/make_nb.py",
 "old_string": "print(\"\\\\nBy retina (reading A):\")\nprint(by_retina(cells[cells.reading == \"A\"], [\"ttp_svd_frame\", \"ttp_svd_parabolic\"]).to_string())",
 "new_string": "print(\"Combinations that also separate the other way:\")\nprint(tt[tt.separate & (tt.mutant_smaller_pts > 0)][[\"recording\", \"measure\", \"ci\", \"mutant_larger_pts\", \"mutant_smaller_pts\", \"sep_range\"]].to_string(index=False))\nfor rd in ret1.READINGS:\n    d = cells[(cells.reading == rd) & cells.group.isin(GROUPS)]\n    fast = d[d.ttp_peak_frame < 0.03]\n    print(f\"  reading {rd}: cells with time to peak (peak separation, frame) below 30 ms: \"\n          f\"{fast.groupby('group').size().to_dict()}; their STA peak ratios {np.round(np.sort(fast.peak_ratio.to_numpy()), 2).tolist()}\")\nprint(\"\\\\nBy retina (reading A):\")\nprint(by_retina(cells[cells.reading == \"A\"], [\"ttp_svd_frame\", \"ttp_svd_parabolic\"]).to_string())"
}
```

```
The file /tmp/claude-1001/gen/make_nb.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open("make_nb.py").read()
for k in ["COUNTS","FIG9D","S3","FIG9E","FIG9F","FIG9G","FIG9H"]:
    s=s.replace(f"md('**Result: RESULT_{k}**')",f"md(R['{k}'])")
s=s.replace("cells = []\n","cells = []\nimport re as _re\nR = dict(_re.findall(r'^@@ (\\w+)\\n(.*?)(?=^@@ |\\Z)', open(sys.argv[1] + '/results.md').read(), _re.S | _re.M))\nR = {k: v.strip() for k, v in R.items()}\n",1)
open("make_nb.py","w").write(s)
EOF
grep -n "R\['\|_re" make_nb.py
```

```
3:import re as _re
4:R = dict(_re.findall(r'^@@ (\w+)\n(.*?)(?=^@@ |\Z)', open(sys.argv[1] + '/results.md').read(), _re.S | _re.M))
37:retinas = ret1.load_retinas(z)
69:pdf = pypdf.PdfReader(io.BytesIO(requests.get(ret1.BASE_URL + "docs/crcns_ret-1_data_description.pdf", timeout=60).content))
196:first_vb = {R["retina"]: ret1.bar_recordings(R, "A")[0]["index"] for R in retinas}
267:        for d in ret1.measure_retina(R, ret1.bar_recordings(R, reading), bits):
270:    recs = [ret1.with_tail_shift(r, 720.0) for r in ret1.bar_recordings(R, "A")]
271:    for d in ret1.measure_retina(R, recs, bits):
308:def by_retina(df, cols):
362:md(R['COUNTS'])
386:print(by_retina(cells[cells.reading == "A"], ["fwhm_svd", "fwhm_peak", "bar_um"]).to_string())
400:md(R['FIG9D'])
434:md(R['S3'])
465:print(by_retina(cells[cells.reading == "A"], ["ttp_svd_frame", "ttp_svd_parabolic"]).to_string())
477:md(R['FIG9E'])
497:print(by_retina(cells[cells.reading == "A"], ["rate_hz"]).to_string())
510:md(R['FIG9F'])
534:print(by_retina(cells[cells.reading == "A"], ["theta_frame_continuous", "theta_binned_continuous"]).to_string())
547:md(R['FIG9G'])
569:print(by_retina(cells[cells.reading == "A"], ["gain_frame_printed", "gain_frame_continuous"]).to_string())
[... 2 more lines not kept]
```

**Agent**

Now the header, conclusions and summary texts.

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/header.md <<'EOF'
# Reproducing Lefebvre et al. (2008), Figure 9, from CRCNS ret-1

**Paper.** Lefebvre JL, Zhang Y, Meister M, Wang X, Sanes JR (2008). Gamma-Protocadherins regulate
neuronal survival but are dispensable for circuit formation in retina. *Development*
135:4141-4151. [doi:10.1242/dev.027912](https://doi.org/10.1242/dev.027912). The claims file was
written from the NIH author manuscript in PubMed Central (PMC2644426), with its Methods, Results,
Discussion and figure legends; the supplementary figures were not available to it. The paper
links no analysis code.

**Data set.** CRCNS ret-1, "Multi-electrode recordings from retinal ganglion cells" (Zhang, Asari
and Meister 2014), [doi:10.6080/K0RF5RZT](https://doi.org/10.6080/K0RF5RZT), read from the public
S3 bucket `crcnsarchive` under `ret-1/`. CRCNS data sets are not versioned, so the version is
recorded as `unversioned`. There is one form of the data set to choose: the paper (2008) predates
it and cites none, and the bucket holds one zip file, `crcns_ret-1.zip` (71,871,914 bytes), whose
MD5 in the data set's `checksums.md5` is `4b9390ddc51c72d6f66563cb02e48fe8`; the data check
below streams the zip and confirms that sum, and lists the CRC-32 of every member read, so that a
later change is detectable. The description is version 0.8 (2 September 2014) and the files in
the zip are dated 2014. The zip is opened in place over range requests; nothing is written to disk.

**What the data set holds.** Spike times of 325 sorted units from 16 isolated retinas (5 dates in
2008), each file labelled with a genotype, and their responses to binary white noise only:
flickering vertical and horizontal bars and checkerboards, drawn from the RAN1 generator whose
bits are in the zip. It holds none of the histology of Figures 1 to 8, and none of the flashing
spots, flashes, moving bars or gratings of Figure 9A to 9C.

**Outside inputs.** None.

| Claim | Tested here |
|---|---|
| fig1-broad-expression, fig2-postnatal-localization, fig3-synaptic-localization, s1-chx10-recombination, fig4h-inl-ipl-thinner, fig4-alleles-equivalent, fig4i-cell-type-loss, fig5-postnatal-onset, fig5-increased-apoptosis, fig6f-amacrine-loss-central, fig6f-neighbours, fig7-laminar-targeting, fig8ad-bax-rescue, fig8el-synapse-density, fig8mn-bax-laminar | Blocked: histology, not in the data set |
| fig9a-response-variety, fig9c-on-off-index | Blocked: no flashing-spot recordings |
| fig9-rod-cone | Blocked: no flashes of two intensities |
| fig9b-direction-selective | Blocked: no moving gratings or bars |
| fig9-cell-counts | Tested |
| fig9d-rf-size-similar | Tested |
| s3-receptive-field-surrounds | Tested |
| fig9e-slower-time-course | Tested |
| fig9f-lower-firing-rate | Tested |
| fig9g-threshold-unaltered | Tested |
| fig9h-gain-reduced | Tested |

**Which bar recording.** The claims file names bars of 8.3 or 16.6 um but not their orientation,
nor what to do when a retina has more than one such recording. This was asked
(`questions/crcns-ret-1.yaml`), and every claim on the bars is tested under three readings: (A)
the first vertical-bar recording of each retina, (B) all its vertical-bar recordings pooled, (C)
its horizontal-bar recording where it has one, otherwise as A. Each claim's outcome is the one all
readings give.
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/results.md <<'EOF'
@@ COUNTS
**Result: not reproduced.** The data set's labels give 200 mutant units (87 Chx10-Cre, 113
Pax6-Cre) and 122 control units, against 115 (103.5 to 126.5) and 143 (128.7 to 157.3). Counting
only units whose STA peak is more than 1.5 times the null's gives 126 mutant units, inside the
tolerance, but no count of control units can exceed 122, below the lower bound. So the control
count misses under any reading of "units with a flicker response". The 3 units of the Bax -/-
retina are in neither group.
@@ FIG9D
**Result: not reproduced.** In all 18 combinations of recording reading, separation and band, the
95% bands separate with the mutant centres smaller (reading A, svd: median 116 against 156 um, KS
p below 1e-4). Much of the difference comes from mutant cells with weak STAs. Among cells whose STA
peak is more than twice the null's (93 mutant, 107 control) the medians are 143 and 158 um (KS
p = 0.11), the binomial and bootstrap bands separate only between 82 and 101 um, and the DKW bands
overlap. The bands also separate without the duplicate units, without 20080702_R4, with the
out-of-order spikes moved, and with 16.6 um bars only.
@@ S3
**Result: reproduced by the criterion, but the test does not show surrounds.** In all 12
readings at least one mutant and one control cell have a lobe of opposite sign on both flanks
(reading A, svd, 20%: 102 of 200 mutant and 16 of 122 control cells). The same rule applied to
null STAs (spike counts shifted by half the recording) is met by 194 to 198 of 200 mutant and 119
to 121 of 122 control cells. So noise alone meets the rule, and the result is no evidence for
or against surrounds.
@@ FIG9E
**Result: reproduced.** In all 36 combinations the 95% bands separate with the mutant curve at
longer times, and the mutant medians exceed the control medians by 16.1 to 33.3 ms (KS p at most
2e-09). In 8 combinations (peak separation, binomial and bootstrap bands, readings A and C) the
bands also separate the other way, at 1 or 2 values below 30 ms. FAST_SENTENCE The separation at
longer times holds in those combinations too. It holds in every variant, including the cells with
clear STAs (93 mutant, 107 control) and each Cre line alone.
@@ FIG9F
**Result: reproduced.** In all 9 combinations the bands separate with the mutant curve at lower
rates. Under reading A the mutant median is 3.82 Hz against 9.02 Hz for controls (ratio 0.42;
0.38 to 0.45 over the readings). By retina the mutant medians range from 1.9 to 15.9 Hz and the
control medians from 3.8 to 23.6 Hz. Every variant gives a lower mutant median. With the Pax6-Cre
mutants alone (ratio 0.68), and in the cells with clear STAs (0.65), the DKW bands overlap while
the binomial and bootstrap bands still separate.
@@ FIG9G
**Result: not reproduced.** The paper finds the threshold unaltered. Here the bands separate in
all 36 combinations, with mutant thresholds higher (reading A, frame fit: median 1.12 against
0.44 SD of the generator in the continuous form, 1.69 against 0.01 in the printed form). Part of
this comes from mutant cells with weak STAs, whose generator predicts little of the rate. Among
cells with clear STAs the medians are 0.85 against 0.41 (frame fit, continuous form); the DKW bands
overlap there, while the binomial and bootstrap bands still separate.
@@ FIG9H
**Result: blocked (methods_underspecified).** The readings of the nonlinearity's form disagree.
With the printed form (B + G y above theta), mutant gains are lower and the bands separate in all
18 combinations (reading A, frame fit: median 17.9 against 23.1 Hz per SD, ratio 0.77). With the
continuous form (B + G (y - theta)), the bands overlap in 14 of 18 combinations and the medians are
close (29.5 against 30.8, KS p = 0.89). Among cells with clear STAs neither form gives lower mutant
gains (printed 23.1 against 23.4, continuous 33.1 against 31.0).
EOF
cat > $TMPDIR/gen/summary.md <<'EOF'
## Summary

| Claim | Outcome |
|---|---|
| 15 histology claims (Figures 1 to 8, Supplementary Figure 1) | Blocked: data missing |
| fig9a-response-variety, fig9c-on-off-index, fig9-rod-cone, fig9b-direction-selective | Blocked: data missing |
| fig9-cell-counts: 115 mutant and 143 control cells | Not reproduced (200 and 122) |
| fig9d-rf-size-similar: centre size similar | Not reproduced (mutant smaller) |
| s3-receptive-field-surrounds | Reproduced by the criterion; the rule is met by noise |
| fig9e-slower-time-course | Reproduced |
| fig9f-lower-firing-rate | Reproduced |
| fig9g-threshold-unaltered | Not reproduced (mutant higher) |
| fig9h-gain-reduced | Blocked: methods underspecified (the forms of the nonlinearity disagree) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.**

- The groups are the data set's labels. They hold 200 mutant and 122 control units, where the
  paper has 115 and 143. The control retinas are mostly labelled "WT (chx10 het)", a genotype the
  paper does not list among its controls. The files do not say which region of the Pax6-Cre
  retinas was recorded, so the mutant group cannot be restricted to the periphery as the paper's
  was. The Bax -/- retina is left out, as the paper did not use Bax mutants for Figure 9.
- All units are used, as the claims file reads the legend's counts; the paper does not say
  whether it kept every unit. Many mutant units have weak or no receptive fields (STA peak below
  twice that of the null in 107 of 200 mutant units and 15 of 122 control units). Their noisy
  STAs give small centres, a high LN threshold and a low printed-form gain, and they carry much
  of the differences in Figure 9D, 9G and 9H.
- Which bar recording is used is not fixed by the claims file. Three readings were run and all
  agree on every outcome.
- The 95% bands are built in the three ways the claims file names, as the paper does not say how
  its bands were made. The LN fit and the separation of h follow the claims file's readings.
- The mutant retinas include all 8.3 um bar recordings; all control retinas were stimulated with
  16.6 um bars. The results hold with the 16.6 um recordings alone.

**What was found about the data set.**

- It holds only the white-noise part of Figure 9: none of the histology of Figures 1 to 8, and no
  flashing spots, flashes, moving bars or gratings (Figure 9A to 9C).
- Its unit counts (200 mutant, 122 control) and control genotypes differ from the paper's Figure
  9 (115 and 143). The data set does not say how its units relate to the paper's.
- In all 9 recordings that last 1500 s, the spike trains run to 1440 s and then hold a second
  segment between 720 and 780 s. This is consistent with the last minute stored with the wrong
  time offset, and the trains are not sorted.
- The stimulus of the vertical-bar recording of 20080702_R4 cannot be rebuilt from its
  description: none of its 12 units has an STA, though all 12 respond to the checkerboard of the
  same retina. Its frame length (16.665 ms) also differs from the others'.
- 16 pairs of units share 70 to 100% of their spikes within 0.5 ms, most likely single neurons
  sorted twice.
- The files do not give the age, the Pcdh-gamma allele, the recorded region of the Pax6-Cre
  retinas, or which units are ganglion cells of which type.
- `ran1.bin` matches the RAN1 generator of `ran1.m` with seed -10000, read least significant bit
  first, and the description's table of retinas, cells and labels matches the files.
EOF
cd entries/crcns-ret-1-lefebvre-2008 && . $TMPDIR/ex/bin/activate && python $TMPDIR/gen/make_nb.py $TMPDIR/gen reproduce_lefebvre_2008.ipynb && echo built
```

```
built
```

**Agent**

Checking one detail before fixing the text: whether the sorted trains in those recordings run past 1440 s.

**Agent calls Bash**

```bash
. $TMPDIR/ex/bin/activate && python - <<'EOF'
import numpy as np, ret1
z=ret1.open_zip(); rets={R["retina"]:R for R in ret1.load_retinas(z)}
for n in ["20080628_R4","20080628_R6","20080702_R1","20080702_R4"]:
    for rec in rets[n]["recordings"]:
        for c,(h,tl) in enumerate(ret1.split_trains(rec)):
            if len(tl)==0: print(n,rec["index"],c,"sorted; n=",len(h),"max",h.max() if len(h) else None, "in 1440-1500:",((h>1440)).sum(), "in 720-780:",((h>720)&(h<780)).sum())
EOF
```

```
20080628_R4 0 2 sorted; n= 18383 max 1499.893 in 1440-1500: 755 in 720-780: 729
20080628_R6 0 1 sorted; n= 30127 max 1499.9442 in 1440-1500: 1155 in 720-780: 1187
20080628_R6 0 2 sorted; n= 34791 max 1496.2391 in 1440-1500: 1452 in 720-780: 1427
20080702_R1 0 0 sorted; n= 14577 max 1499.8581 in 1440-1500: 554 in 720-780: 583
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open("make_nb.py").read()
old='''print(pd.DataFrame(tail_rows).to_string(index=False))'''
new='''print(pd.DataFrame(tail_rows).to_string(index=False))
print("\\nTrains without an out-of-order segment in the same recordings: spikes in 1440-1500 s and in 720-780 s")
for R in retinas:
    for rec in R["recordings"]:
        parts = ret1.split_trains(rec)
        if any(len(tl) for _, tl in parts) and rec["nframes"] * rec["frame"] > 1450:
            for c, (h, tl) in enumerate(parts):
                if not len(tl):
                    print(f"  {R['retina']} rec {rec['index']} unit {c}: {int((h > 1440).sum())} and {int(((h > 720) & (h < 780)).sum())}")'''
assert old in s; s=s.replace(old,new)
old='''In every recording that lasts 1500 s (the vertical bars
and checkerboards of 20080628_R4 and R6 and of 20080702_R1 and R4), the trains are not sorted:
they run from 0 to 1440 s and then hold a second segment of spikes between 720 and 780 s. The
recordings hold no spikes after 1440 s otherwise, though their stimulus runs to 1500 s.'''
new='''In the 8 recordings of 20080628_R4 and R6 and of 20080702_R1 and R4
(vertical bars and checkerboards, each of 1500 s), almost every train is out of order: it runs from
0 to 1440 s and then holds a second segment of spikes between 720 and 780 s, though the stimulus
runs to 1500 s. The few trains in these recordings that are in order have spikes between 1440 and
1500 s, about as many as between 720 and 780 s (list above).'''
assert old in s; s=s.replace(old,new)
open("make_nb.py","w").write(s)
s=open("summary.md").read()
old='''- In all 9 recordings that last 1500 s, the spike trains run to 1440 s and then hold a second
  segment between 720 and 780 s. This is consistent with the last minute stored with the wrong
  time offset, and the trains are not sorted.'''
new='''- In the 8 recordings of four retinas (20080628_R4 and R6, 20080702_R1 and R4), 93 of 97 spike
  trains run to 1440 s and then hold a second segment between 720 and 780 s, so they are not
  sorted. This is consistent with their last minute (1440 to 1500 s) stored with a 720 s offset in
  place of 1440 s.'''
assert old in s; s=s.replace(old,new); open("summary.md","w").write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && sed -i 's/93 of 97 spike/82 of 86 spike/' summary.md && grep -n "82 of 86" summary.md; cd entries/crcns-ret-1-lefebvre-2008 && cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-ret-1-lefebvre-2008
type: reproduction
title: Retinal ganglion cell responses in Pcdh-gamma mutant retina (Lefebvre et al. 2008)
description: Tests the findings of Lefebvre, Zhang, Meister, Wang and Sanes (2008) on CRCNS data set
  ret-1, which holds multielectrode recordings of 325 units from 16 mutant and control mouse retinas
  stimulated with flickering bars and checkerboards. It compares receptive field size, response
  time course, firing rate and Linear-Nonlinear model threshold and gain between Pcdh-gamma mutant
  and control retinas (Figure 9D to 9H). The histology of Figures 1 to 8 and the flash, spot and
  grating experiments of Figure 9A to 9C are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_lefebvre_2008.ipynb
  title: Reproducing Lefebvre et al. (2008), Figure 9, from CRCNS ret-1
  runtime_minutes: 5
helpers:
- ret1.py
related:
- id: crcns:ret-1/unversioned
  relation: uses_data
- id: doi:10.1242/dev.027912
  relation: reproduces
EOF
cat ../001453-fouke-2025/entry.yaml | head -3; cat schemas/entry.schema.json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d['properties']['related'],indent=0)[:800])"
```

```
43:- In the 8 recordings of four retinas (20080628_R4 and R6, 20080702_R1 and R4), 82 of 86 spike
schema_version: 1
name: 001453-fouke-2025
type: reproduction
{
"type": "array",
"minItems": 1,
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"id",
"relation"
],
"properties": {
"id": {
"description": "A dataset as <archive>:<id>[/<version>] (dandi:000003/0.220126.1855), doi:<doi>, or entry:<name>.",
"type": "string",
"pattern": "^(dandi:[0-9]{6}(/.+)?|doi:10\\.[0-9]{4,9}/.+|entry:[a-z0-9]+(-[a-z0-9]+)*|[a-z][a-z0-9-]*:[^\\s/]+(/\\S+)?)$"
},
[... 11 more lines not kept]
```

**Agent**

Rebuilding the notebook, then lock and the full check-and-run.

**Agent calls Bash**

```bash
. $TMPDIR/ex/bin/activate && python $TMPDIR/gen/make_nb.py $TMPDIR/gen reproduce_lefebvre_2008.ipynb && cd  && python tools/entry.py lock entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -3
```

```
File "tools/entry.py", line 53, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
deactivate 2>/dev/null; which python; python -c "import yaml, jsonschema, nbformat; print('ok')" && python tools/entry.py lock entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -3
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
ok
wrote entries/crcns-ret-1-lefebvre-2008/requirements.lock.txt
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -8
```

```
[31m    [39m[31mprint("[39m
          ^
[31mSyntaxError[39m[31m:[39m unterminated string literal (detected at line 24)



0 error(s)
FAIL  reproduce_lefebvre_2008.ipynb  (20 s)

real	0m33.209s
user	0m21.464s
sys	0m3.305s
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open("make_nb.py").read()
old='print("\nTrains without'
assert old in s
s=s.replace(old,'print("\\\\nTrains without'); open("make_nb.py","w").write(s)
EOF
grep -n 'Trains without' make_nb.py; cd entries/crcns-ret-1-lefebvre-2008 && $TMPDIR/ex/bin/python $TMPDIR/gen/make_nb.py $TMPDIR/gen reproduce_lefebvre_2008.ipynb && cd ../.. && time python tools/entry.py all entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -4
```

```
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
AssertionError
168:print("\nTrains without an out-of-order segment in the same recordings: spikes in 1440-1500 s and in 720-780 s")


0 error(s)
FAIL  reproduce_lefebvre_2008.ipynb  (19 s)

real	0m32.073s
user	0m21.420s
sys	0m3.887s
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && sed -i 's/print("\\nTrains without/print("\\\\nTrains without/' make_nb.py && grep -n 'Trains without' make_nb.py && cd entries/crcns-ret-1-lefebvre-2008 && $TMPDIR/ex/bin/python $TMPDIR/gen/make_nb.py $TMPDIR/gen reproduce_lefebvre_2008.ipynb && cd ../.. && time python tools/entry.py all entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -4
```

```
168:print("\\nTrains without an out-of-order segment in the same recordings: spikes in 1440-1500 s and in 720-780 s")
Installed kernelspec registry-crcns-ret-1-lefebvre-2008 in executed/crcns-ret-1-lefebvre-2008/.venv/share/jupyter/kernels/registry-crcns-ret-1-lefebvre-2008
0 error(s)
pass  reproduce_lefebvre_2008.ipynb  (284 s)

real	4m56.803s
user	14m49.083s
sys	0m8.339s
```

**Agent**

Passes in 284 s. Now checking the outputs in the executed copy, starting with the fast-peak cells and the new spike check:

**Agent calls Bash**

```bash
ls executed/crcns-ret-1-lefebvre-2008/; $TMPDIR/ex/bin/python $TMPDIR/show.py executed/crcns-ret-1-lefebvre-2008/reproduce_lefebvre_2008.ipynb claim:fig9e | grep -v Figure | sed -n '/Combinations:/,/By retina/p'; $TMPDIR/ex/bin/python $TMPDIR/show.py executed/crcns-ret-1-lefebvre-2008/reproduce_lefebvre_2008.ipynb 8; $TMPDIR/ex/bin/python $TMPDIR/show.py executed/crcns-ret-1-lefebvre-2008/reproduce_lefebvre_2008.ipynb claim:fig9h | tail -3
```

```
reproduce_lefebvre_2008.ipynb
result.json
Combinations: 36 ; separate with mutant at longer times: 28 ; separate the other way: 8 ; overlap: 0
Median difference, mutant minus control (ms), range over combinations: 16.1 to 33.3; KS p at most 2e-09
Combinations that also separate the other way:
recording            measure        ci  mutant_larger_pts  mutant_smaller_pts       sep_range
        A     ttp_peak_frame  binomial                 76                   1  0.025 to 0.392
        A     ttp_peak_frame bootstrap                 76                   1  0.025 to 0.392
        A ttp_peak_parabolic  binomial                301                   1  0.028 to 0.395
        A ttp_peak_parabolic bootstrap                300                   1  0.028 to 0.395
        C     ttp_peak_frame  binomial                 75                   2  0.025 to 0.392
        C     ttp_peak_frame bootstrap                 76                   2  0.025 to 0.392
        C ttp_peak_parabolic  binomial                298                   2 0.0283 to 0.387
        C ttp_peak_parabolic bootstrap                297                   2 0.0283 to 0.387
  reading A: cells with time to peak (peak separation, frame) below 30 ms: {'mutant': 4}; their STA peak ratios [0.86, 0.96, 0.96, 1.05]
  reading B: cells with time to peak (peak separation, frame) below 30 ms: {'mutant': 3}; their STA peak ratios [0.86, 0.96, 0.96]
  reading C: cells with time to peak (peak separation, frame) below 30 ms: {'mutant': 4}; their STA peak ratios [0.9, 0.96, 0.96, 1.05]

By retina (reading A):
##### cell 8 ['sanity']
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open("results.md").read()
s=s.replace("FAST_SENTENCE","They come from 3 or 4 mutant cells whose a(t) peaks within 30 ms and whose STA peak is no larger than the null's\n(ratios 0.86 to 1.05), cells without a measurable receptive field.")
open("results.md","w").write(s)
EOF
grep -n "ratios 0.86" results.md
```

```
28:(ratios 0.86 to 1.05), cells without a measurable receptive field. The separation at
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
hist = ["fig1-broad-expression","fig2-postnatal-localization","fig3-synaptic-localization","s1-chx10-recombination",
"fig4h-inl-ipl-thinner","fig4-alleles-equivalent","fig4i-cell-type-loss","fig5-postnatal-onset","fig5-increased-apoptosis",
"fig6f-amacrine-loss-central","fig6f-neighbours","fig7-laminar-targeting","fig8ad-bax-rescue","fig8el-synapse-density","fig8mn-bax-laminar"]
out=[]
for h in hist:
    out.append(f"""- claim: {h}
  outcome: blocked
  blocked_by: data_missing
  notes: The claim rests on histology (sections, dissociated cells or counts of stained cells). The
    data set holds only spike times and white-noise stimuli from the multielectrode recordings, and
    the paper names no other deposit of its images or counts.
""")
open("/tmp/claude-1001/hist.yaml","w").write("".join(out))
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/head.yaml <<'EOF'
schema_version: 2
id: crcns-ret-1-lefebvre-2008-01
dataset:
  archive: crcns
  id: ret-1
  version: unversioned
  doi: 10.6080/K0RF5RZT
paper: doi:10.1242/dev.027912
date: 2026-10-20
entry: crcns-ret-1-lefebvre-2008
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-10
outcomes:
EOF
cat > $TMPDIR/fig9.yaml <<'EOF'
- claim: fig9-cell-counts
  outcome: not_reproduced
  notebook: reproduce_lefebvre_2008.ipynb
  output: claim:fig9-cell-counts
  measured:
  - 200
  - 122
  notes: The data set's labels give 200 mutant units (87 Chx10-Cre in 6 retinas, 113 Pax6-Cre in 4)
    and 122 control units (95 labelled "WT (chx10 het)" in 3 retinas, 27 "WT (pax6 het)" in 2),
    against 115 (103.5 to 126.5) and 143 (128.7 to 157.3). Every unit fired during the bar
    stimulus. Units whose STA peak exceeds 1.5 times the null's number 126 mutant (inside the
    tolerance) and 113 control; above 2 times, 93 and 107. No count of control units can exceed
    122, so the control count misses under any reading of a flicker response. Without the second
    unit of each duplicate pair, 189 and 118. The Bax -/- retina (3 units) is in neither group.
  deviations:
  - The claims file asks also for the count of units with a flicker response without defining
    one; the counts above two thresholds of the STA peak over a null STA are shown as a standard
    choice, and none can change the outcome.
  - The control retinas are as the data set labels them; 95 of the 122 control units carry a label
    ("WT (chx10 het)") that the paper's description of its controls does not include.
- claim: fig9a-response-variety
  outcome: blocked
  blocked_by: data_missing
  notes: The data set holds no flashing-spot recordings; every recording is binary white noise
    (flickering bars or checkerboards). The claim also depends on fig9c-on-off-index, blocked for
    the same reason. The paper names no other deposit.
- claim: fig9c-on-off-index
  outcome: blocked
  blocked_by: data_missing
  notes: The On-Off index needs the flashing-spot experiment of Figure 9A, which is not in the data
    set; every recording is binary white noise.
- claim: fig9-rod-cone
  outcome: blocked
  blocked_by: data_missing
  notes: The data set holds no flashes, dim or bright; every recording is binary white noise at
    one luminance range, so the criterion's pair of intensities is absent.
- claim: fig9b-direction-selective
  outcome: blocked
  blocked_by: data_missing
  notes: The data set holds no moving gratings or moving bars; every recording is binary white
    noise. It also depends on fig9a-response-variety, which is blocked.
- claim: fig9d-rf-size-similar
  outcome: not_reproduced
  notebook: reproduce_lefebvre_2008.ipynb
  output: claim:fig9d-rf-size-similar
  notes: In all 18 combinations (3 recording readings, 2 separations, 3 bands) the 95% bands
    separate, with mutant centres smaller; reading A, svd, median 116 against 156 um (KS p below
    1e-4), peak separation 94 against 151 um. The bands also separate without duplicate units,
    without 20080702_R4, with the out-of-order spikes moved and with 16.6 um bars only. Much of
    the difference comes from mutant units with weak STAs (107 of 200 mutant and 15 of 122 control
    units have an STA peak less than twice the null's). Among units above that, the medians are 143
    and 158 um (KS p = 0.11), the binomial and bootstrap bands separate only between 82 and 101 um,
    and the DKW bands overlap. With Pax6-Cre mutants alone the svd DKW bands overlap too.
  deviations:
  - The bar recording used per retina is not fixed by the claims file; three readings were run
    (asked in questions/crcns-ret-1.yaml) and give the same outcome.
  - All mutant retinas recorded with 8.3 um bars (5) are mutant; every control retina was
    recorded with 16.6 um bars. The result is the same with 16.6 um recordings alone.
  - The mutant group cannot be restricted to the peripheral region of the Pax6-Cre retinas, as the
    data set does not say where they were recorded.
- claim: s3-receptive-field-surrounds
  outcome: reproduced
  notebook: reproduce_lefebvre_2008.ipynb
  output: claim:s3-receptive-field-surrounds
  notes: Under all 12 readings (3 recording readings, 2 separations, depths of 10% and 20%) at
    least one mutant and one control unit have a lobe of opposite sign on both flanks of b(x);
    reading A, svd, 20%, 102 of 200 mutant and 16 of 122 control units. The same rule applied to null
    STAs (spike counts shifted by half the recording) is met by 194 to 198 of 200 mutant and 119 to
    121 of 122 control units, so the rule is met by noise. The outcome follows the criterion, but the
    result is no evidence for or against surrounds.
  deviations:
  - The bar recording used per retina is not fixed by the claims file; three readings were run.
- claim: fig9e-slower-time-course
  outcome: reproduced
  notebook: reproduce_lefebvre_2008.ipynb
  output: claim:fig9e-slower-time-course
  notes: In all 36 combinations (3 recording readings, 2 separations, 2 peak readings, 3 bands)
    the bands separate with the mutant curve at longer times; mutant medians exceed control ones by
    16.1 to 33.3 ms (reading A, svd, frame, 125 against 108 ms), KS p at most 2e-09. In 8
    combinations (peak separation, binomial and bootstrap bands, readings A and C) the bands also
    separate the other way at 1 or 2 values below 30 ms, from 3 or 4 mutant units whose STA peak is
    no larger than the null's (ratios 0.86 to 1.05). The result holds in every variant, including
    units with clear STAs (93 mutant, 107 control) and each Cre line alone. The statement's
    "significantly" has no named test in the paper; the KS test is shown.
  deviations:
  - The criterion does not say how to treat bands that separate in both directions. Here the
    mutant curve is read as lying at longer times when the bands separate with the mutant at longer
    times and the medians agree. Under the stricter reading, that no point may separate the other
    way, 28 of 36 combinations meet it and the outcome would be blocked.
  - The bar recording used per retina is not fixed by the claims file; three readings were run.
  - Lag j is placed at (j + 0.5) frames, the data set's example script's convention; the offset
    is the same for every unit.
- claim: fig9f-lower-firing-rate
  outcome: reproduced
  notebook: reproduce_lefebvre_2008.ipynb
  output: claim:fig9f-lower-firing-rate
  notes: In all 9 combinations (3 recording readings, 3 bands) the bands separate with the mutant
    curve at lower rates; reading A, median 3.82 against 9.02 Hz (ratio 0.42; 0.38 to 0.45 over
    readings). By retina, mutant medians 1.9 to 15.9 Hz, control 3.8 to 23.6 Hz. Every variant gives
    a lower mutant median; with Pax6-Cre mutants alone (ratio 0.68) and among units with clear STAs
    (0.65), the DKW bands overlap while the binomial and bootstrap bands separate.
  deviations:
  - The rate is that during the bar recordings used for the other measures; the claims file does
    not say which flicker recording, and the three readings agree.
- claim: fig9g-threshold-unaltered
  outcome: not_reproduced
  notebook: reproduce_lefebvre_2008.ipynb
  output: claim:fig9g-threshold-unaltered
  notes: In all 36 combinations (3 recording readings, 2 fits, 2 forms, 3 bands) the bands
    separate, with mutant thresholds higher; reading A, frame fit, median 1.12 against 0.44 SD of the
    generator (continuous form) and 1.69 against 0.01 (printed form). Part of this comes from mutant
    units with weak STAs, whose generator predicts little of the rate; among units with clear STAs
    the medians are 0.85 against 0.41 (frame fit, continuous form), the DKW bands overlap, and the
    binomial and bootstrap bands still separate.
  deviations:
  - The bar recording used per retina is not fixed by the claims file; three readings were run.
  - Theta is searched on 99 quantiles of y for the frame fit and at every split between the 20 bin
    centres for the binned fit, a standard choice of resolution.
- claim: fig9h-gain-reduced
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_lefebvre_2008.ipynb
  output: claim:fig9h-gain-reduced
  notes: The readings of the nonlinearity's form disagree. With the printed form (B + G y above
    theta), mutant gains are lower and the bands separate in all 18 combinations (reading A, frame
    fit, median 17.9 against 23.1 Hz per SD, ratio 0.77). With the continuous form (B + G (y -
    theta)), the bands overlap in 14 of 18 (median 29.5 against 30.8, KS p = 0.89). Among units with
    clear STAs neither form gives lower mutant gains (printed 23.1 against 23.4, continuous 33.1
    against 31.0).
  deviations:
  - The bar recording used per retina is not fixed by the claims file; three readings were run.
EOF
cat > $TMPDIR/tail.yaml <<'EOF'
findings:
- kind: data_missing
  statement: The data set holds only the white-noise recordings behind Figure 9D to 9H. The
    histology of Figures 1 to 8 and Supplementary Figure 1, and the flashing-spot, flash, moving-bar
    and grating recordings of Figure 9A to 9C, are not in it, and the paper names no other deposit.
    Of the paper's 28 claims, 19 cannot be tested.
- kind: selection_undocumented
  statement: The data set holds 200 mutant and 122 control units (and 3 from a Bax -/- mutant),
    where the paper's Figure 9 has 115 mutant and 143 control cells. The data set does not say how
    its units relate to the paper's, which were kept, or why the counts differ.
- kind: paper_inconsistency
  statement: The data set labels 95 of its 122 control units "WT (chx10 het)", while the paper's
    Figure 9 legend gives the controls as Pax6-Cre;Pcdh-gamma +/f-del or Pcdh-gamma f-del/f-del
    without Cre. The labels and the paper disagree on what the controls were.
- kind: format_error
  statement: In the 8 recordings of 20080628_R4, 20080628_R6, 20080702_R1 and 20080702_R4, 82 of 86
    spike trains are not in time order. Each runs to 1440 s and then holds a second segment between
    720 and 780 s, though the stimulus runs to 1500 s. The 4 trains in order have spikes between 1440
    and 1500 s, about as many as between 720 and 780 s, and moving the segments by 720 s raises their
    STA peaks over the null in most units. This is consistent with the last minute stored with a 720 s
    offset in place of 1440 s. One checkerboard recording (20080628_R5) has 1 or 2 spikes near 2 s out
    of order in 15 units.
- kind: metadata_error
  statement: The stimulus of the vertical-bar recording of 20080702_R4 cannot be rebuilt from its
    description. None of its 12 units has an STA above the null (median ratio 0.96), while all 12
    respond to the checkerboard of the same retina (median ratio 3.88). Its stated frame length,
    16.665 ms, differs from the 16.672 ms of the other bar recordings, and its spikes end at 1440 s
    against a stated 1499 s of stimulus.
- kind: other
  statement: 16 pairs of units share 70 to 100% of their spikes within 0.5 ms in every recording of
    their retina (12 pairs in mutant retinas, 4 in a control retina), most likely single neurons
    sorted twice. The data set does not mark them.
- kind: metadata_insufficient
  statement: The files do not give the age of the mice, the Pcdh-gamma allele (the paper's Results
    say fcon3 and its Figure 9 legend f-del), the region recorded in the Pax6-Cre retinas (the paper
    used their periphery only), or the cell type of the units.
verifications: []
EOF
cat $TMPDIR/head.yaml $TMPDIR/hist.yaml $TMPDIR/fig9.yaml $TMPDIR/tail.yaml > attempts/crcns-ret-1-lefebvre-2008-01.yaml
python -c "import yaml; d=yaml.safe_load(open('attempts/crcns-ret-1-lefebvre-2008-01.yaml')); print(len(d['outcomes']))"
```

```
26
```

**Agent calls Bash**

```bash
f=attempts/crcns-ret-1-lefebvre-2008-01.yaml; sed -i 's/Of the paper.s 28 claims, 19 cannot be tested./Of the 26 claims, 19 cannot be tested./; s/All mutant retinas recorded with 8.3 um bars (5) are mutant;/All 5 retinas recorded with 8.3 um bars are mutant;/; /^verifications: \[\]$/d' $f; grep -nE "^\s+[^-#][^:]*: .*: " $f | grep -v "^\s*[a-z_]*: [^:]*$" | head; grep -n "—\|rather\|\*\*" $f entries/crcns-ret-1-lefebvre-2008/ret1.py questions/crcns-ret-1.yaml $TMPDIR/gen/*.md | grep -v "Result:" | head
```

```
entries/crcns-ret-1-lefebvre-2008/ret1.py:75:    f = fsspec.open(BASE_URL + ZIP_NAME, block_size=2**20).open()
entries/crcns-ret-1-lefebvre-2008/ret1.py:327:        Sgg = Syy - 2 * grid * Sy + grid ** 2 * k
entries/crcns-ret-1-lefebvre-2008/ret1.py:331:    det = n * Sgg - Sg ** 2
/tmp/claude-1001/gen/header.md:3:**Paper.** Lefebvre JL, Zhang Y, Meister M, Wang X, Sanes JR (2008). Gamma-Protocadherins regulate
/tmp/claude-1001/gen/header.md:10:**Data set.** CRCNS ret-1, "Multi-electrode recordings from retinal ganglion cells" (Zhang, Asari
/tmp/claude-1001/gen/header.md:20:**What the data set holds.** Spike times of 325 sorted units from 16 isolated retinas (5 dates in
/tmp/claude-1001/gen/header.md:26:**Outside inputs.** None.
/tmp/claude-1001/gen/header.md:42:**Which bar recording.** The claims file names bars of 8.3 or 16.6 um but not their orientation,
/tmp/claude-1001/gen/summary.md:18:**How the analysis differs from the paper's.**
/tmp/claude-1001/gen/summary.md:37:**What was found about the data set.**
```

**Agent**

Removing the bold labels (only the "**Result:**" openers may be bold):

**Agent calls Bash**

```bash
cd $TMPDIR/gen && sed -i -E 's/^\*\*(Paper|Data set|What the data set holds|Outside inputs|Which bar recording)\.\*\*/\1./' header.md && sed -i -E 's/^\*\*(How the analysis differs from the paper.s|What was found about the data set)\.\*\*/### \1/' summary.md && grep -n "\*\*" header.md summary.md; grep -c "" results.md; cd  && python tools/entry.py check entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -5
```

```
51
0 error(s)
```

**Agent calls Bash**

```bash
cat > entries/crcns-ret-1-lefebvre-2008/README.md <<'EOF'
# Lefebvre, Zhang, Meister, Wang & Sanes (2008) from CRCNS ret-1

Tests the findings of [Lefebvre et al. (2008)](https://doi.org/10.1242/dev.027912) that can be
tested on [CRCNS ret-1](https://doi.org/10.6080/K0RF5RZT), which holds multielectrode recordings
of 325 units from 16 Pcdh-gamma mutant and control mouse retinas, stimulated with flickering bars
and checkerboards (Figure 9D to 9H). The histology of Figures 1 to 8 and the flash, spot and
grating experiments of Figure 9A to 9C are not in it.

| Claim | Outcome |
|---|---|
| Figure 9 counts, 115 mutant and 143 control cells | Not reproduced (200 and 122) |
| Receptive field centre size similar in mutant and control | Not reproduced (mutant smaller) |
| Some mutant and control cells have surrounds | Reproduced by the criterion, which noise also meets |
| Slower time course in mutants | Reproduced |
| Lower firing rate in mutants | Reproduced |
| LN threshold unaltered in mutants | Not reproduced (mutant higher) |
| LN gain reduced in mutants | Blocked: methods underspecified |
| Figure 9A to 9C and rod and cone responses (four claims) | Blocked: data missing |
| Figures 1 to 8 and Supplementary Figure 1, histology (15 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set's unit counts and control genotypes differ from the paper's, many mutant units have
weak or no receptive fields, the spike trains of four retinas hold a misplaced last minute, and
the bar stimulus of one retina cannot be rebuilt from its description. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/crcns-ret-1-lefebvre-2008-01.yaml`](../../attempts/crcns-ret-1-lefebvre-2008-01.yaml).

- `reproduce_lefebvre_2008.ipynb`: the analysis. It takes about five minutes, streaming the
  data set's zip from the CRCNS S3 bucket.
- `ret1.py`: loading the zip in place, rebuilding the white-noise stimulus from `ran1.bin`, and
  the spike-triggered average, its separation, the LN fit and the 95% bands of the cumulative
  histograms. Other notebooks on this data set can import it.
EOF
cd entries/crcns-ret-1-lefebvre-2008 && $TMPDIR/ex/bin/python $TMPDIR/gen/make_nb.py $TMPDIR/gen reproduce_lefebvre_2008.ipynb && cd ../.. && time python tools/entry.py all entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -3
```

```
Installed kernelspec registry-crcns-ret-1-lefebvre-2008 in executed/crcns-ret-1-lefebvre-2008/.venv/share/jupyter/kernels/registry-crcns-ret-1-lefebvre-2008
0 error(s)
pass  reproduce_lefebvre_2008.ipynb  (277 s)

real	4m50.089s
user	14m27.263s
sys	0m8.171s
```

**Agent**

Passes in 277 s. Confirming the executed numbers are unchanged, then the handover:

**Agent calls Bash**

```bash
P=$TMPDIR/ex/bin/python; E=executed/crcns-ret-1-lefebvre-2008/reproduce_lefebvre_2008.ipynb; $P $TMPDIR/show.py $E claim: | grep -E "^Combinations|Readings in which|No count|reading A: cells" ; $P $TMPDIR/show.py $E claim:fig9h | grep "Run time"; python tools/entry.py handover entries/crcns-ret-1-lefebvre-2008 2>&1 | tail -3; ls executed/crcns-ret-1-lefebvre-2008/handover; git status --short
```

```
No count of control units can exceed 122 (all control units), below the lower bound 128.7
Combinations: 18 ; bands separate in 18 ; of these with mutant at smaller sizes: 18
Readings in which both groups have at least one cell with a surround: 12 of 12
Combinations: 36 ; separate with mutant at longer times: 28 ; separate the other way: 8 ; overlap: 0
Combinations that also separate the other way:
  reading A: cells with time to peak (peak separation, frame) below 30 ms: {'mutant': 4}; their STA peak ratios [0.86, 0.96, 0.96, 1.05]
Combinations: 9 ; separate with mutant at lower rates: 9
Combinations: 36 ; bands separate: 36 ; with mutant at higher thresholds: 36 ; overlap: 0
Combinations: 36 ; separate with mutant at lower gains: 22 ; separate the other way: 0 ; overlap: 14
Run time of the notebook: 4.5 min
wrote executed/crcns-ret-1-lefebvre-2008/handover
10.1242-dev.027912.yaml
reproduce_lefebvre_2008.ipynb
ret1.py
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
[... 8 more lines not kept]
```

**Agent**

Some untracked dotfiles appeared in the repo root that I did not create. Checking what they are:

**Agent calls Bash**

```bash
ls -la .bashrc .gitconfig .mcp.json .profile scripts .idea .vscode 2>&1 | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 20 20:18 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 20 20:18 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 20 20:18 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 20 20:18 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 20 20:18 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 20 20:18 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 20 20:18 scripts
```

**Agent**

I've done steps 1 to 6 of the Author section. `tools/entry.py all` passes (0 check errors, notebook runs in 277 s) and the verifier's handover package is built in `executed/crcns-ret-1-lefebvre-2008/handover/`. Nothing is committed. I added `entries/crcns-ret-1-lefebvre-2008/`, `attempts/crcns-ret-1-lefebvre-2008-01.yaml` and `questions/crcns-ret-1.yaml`. Some untracked dotfiles (`.bashrc`, `scripts` and others) appeared in the repo root; they are sandbox device mounts, not my files, and should not be committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| 15 histology claims (Figures 1 to 8, Supplementary Figure 1) | blocked, data_missing |
| fig9a-response-variety, fig9c-on-off-index, fig9-rod-cone, fig9b-direction-selective | blocked, data_missing (no spots, flashes, bars or gratings in the data set) |
| fig9-cell-counts | not_reproduced (200 mutant and 122 control units, against 115 and 143) |
| fig9d-rf-size-similar | not_reproduced (bands separate in 18 of 18 combinations; mutant centres smaller, 116 against 156 um) |
| s3-receptive-field-surrounds | reproduced by the criterion, but null STAs meet the rule in 97 to 99% of cells, so it is no evidence |
| fig9e-slower-time-course | reproduced (36 of 36 separate, mutant slower by 16 to 33 ms) |
| fig9f-lower-firing-rate | reproduced (9 of 9; median rate ratio 0.38 to 0.45) |
| fig9g-threshold-unaltered | not_reproduced (36 of 36 separate, mutant threshold higher) |
| fig9h-gain-reduced | blocked, methods_underspecified (printed form 18 of 18 lower; continuous form overlaps in 14 of 18) |

### 2. The dataset and the question asked

**Version.** CRCNS ret-1 has no versions, so it is recorded as `unversioned`. There is only one form to pin: the paper predates the data set and cites none. The notebook streams the whole zip in memory and confirms its MD5 against `checksums.md5`, and lists each member's CRC-32 so a later change is detectable.

**Contents.** 16 retinas and 325 units, all stimulated with binary white noise only: vertical bars, horizontal bars and checkerboards. `ran1.bin` matches RAN1 with seed -10000, read least significant bit first. The file table matches the description.

**Problems found:**
- **Group sizes and labels.** The paper has 115 mutant and 143 control cells; the files hold 200 mutant and 122 control units. 95 of the control units are labelled "WT (chx10 het)", which is not among the paper's stated controls.
- **Misplaced spikes.** In 8 recordings from 4 retinas, 82 of 86 spike trains are out of order. They run to 1440 s and then hold a segment at 720 to 780 s. This fits the last minute (1440 to 1500 s) being stored with the wrong offset.
- **Broken stimulus in one recording.** The vertical-bar stimulus of 20080702_R4 cannot be rebuilt from its description. None of its 12 units shows a receptive field, though all 12 respond to the checkerboard in the same retina.
- **Duplicate units.** 16 pairs of units share 70 to 100% of their spikes within 0.5 ms, most likely one neuron sorted twice.
- **Missing metadata.** The files give no age, no allele, no recorded region for the Pax6-Cre retinas and no cell types.
- **Weak mutant responses.** 107 of 200 mutant units have weak or no receptive fields. They carry much of the 9D and 9G differences. A variant restricted to units with clear receptive fields is shown for every claim.

**Question asked** (`questions/crcns-ret-1.yaml`): which bar recording per retina to use (orientation, and retinas with more than one recording), citing the Methods passage on bars of 8.3 or 16.6 um. I ran three readings; they agree on every outcome.

### 3. Protocol gaps

1. **"Units with a flicker response" (fig9-cell-counts) is undefined.** I showed two STA-strength thresholds as a standard choice. No threshold can change the outcome, since there are only 122 control units in total.
2. **The protocol says how to count recordings deposited twice, not units sorted twice.** I kept all units, as the claims file reads the counts, and ran a variant without the duplicates.
3. **The criteria don't say what to do when bands separate in both directions (fig9e).** In 8 of 36 combinations there is also a 1 or 2 point reverse separation below 30 ms, from noise-only units. I read the claim as met and recorded it as a deviation. Under the stricter reading, 28 of 36 meet it and the claim would be blocked; the verifier should look at this.
4. **A criterion can be met by noise (s3).** The protocol gives no rule for when a criterion's own null meets it. I kept the criterion's outcome and said plainly in the notes that it is no evidence.
5. **The step 2 clock check assumes trial tables.** For continuous white noise I used the STA peak against a circularly shifted null and the lag of the peak.
6. **The schema has no `kind` for disagreement between the paper and the data set's labels.** I used `paper_inconsistency` for the control genotype mismatch.
7. **`archives.md` says to give MD5s for the files read, but only the zip has one.** I also printed each member's CRC-32 from the zip directory.

### 4. Runtime and failures
The notebook takes about 4.6 minutes (277 s in the clean run). There were two string-escaping errors in my notebook generator along the way, both fixed. Nothing failed in the final run.

## End of run

67 turns, 35 minutes, result: success.
