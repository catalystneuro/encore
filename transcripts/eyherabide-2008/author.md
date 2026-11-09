# crcns-ia-1 · author · run 41885596452

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs paper claims/crcns-ia-1 entries | head -50; wc -l docs/protocol.md README.md docs/design.md docs/archives.md
```

```
Wed Nov  4 18:21:20 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
[... 61 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 596 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md; sed -n 1,400p docs/archives.md
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
[... 409 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/design.md"
}
```

```
1	# Reproduction registry: design
2	
3	Status: draft for discussion. "Reproduction registry" is a working name.
4	
5	## Goal
6	
7	Agents work through the dandisets on the DANDI Archive that have an associated
8	paper. For each one, an agent tries to reproduce the paper's key findings and
9	figures from the open data, writes the analysis as a notebook, and registers it
10	here. People can deposit too, but most deposits are expected to come from
11	agents.
12	
13	This serves two purposes:
14	
15	1. **Check the data.** A finding that can be reproduced shows the dandiset is
16	   complete and accurate enough to support it. A finding that cannot be
17	   reproduced, with the reason, tells the data owner and the archive what is
18	   missing.
19	2. **Give analysts a starting point.** Someone who wants to test a new
20	   hypothesis on a dandiset starts from notebooks that already load the data
[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/crcns-ia-1/*.yaml; ls paper; ls entries/001453-fouke-2025; cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
<persisted-output>
Output too large (56.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b9f93dab-34d2-4022-b315-7f7507d47857/tool-results/bb9mmpw27.txt

Preview (first 2KB):
# Claims for Eyherabide, Rokem, Herz & Samengo (2008), "Burst firing is a neural code in an
# insect auditory system", Frontiers in Computational Neuroscience, on CRCNS data set ia-1
# (doi:10.6080/K0BG2KWB).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-04, protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record in PubMed Central (PMC2525941, open access), from Europe PMC
# full-text XML, as supplied under paper/, with its Materials and Methods, Results, Discussion,
# the legends of Figures 1 to 10 and Table 1. No PDF was supplied, so values shown only in
# figures (Figure 5, Figure 9B and the population histograms of Figure 7) could not be read.
# The paper has no supplement. It links no analysis code, so none was read. Some passages are
# garbled in the text and are named in the claims that use them (Results, Quantitative
# description, paragraph 7, "no <69%"; Qualitative description, paragraph 5, a ratio of
# sigma to itself).
#
# Data the paper used. Adult Locusta migratoria, intracellular recordings from auditory
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b9f93dab-34d2-4022-b315-7f7507d47857/tool-results/bb9mmpw27.txt"
}
```

```
1	# Claims for Eyherabide, Rokem, Herz & Samengo (2008), "Burst firing is a neural code in an
2	# insect auditory system", Frontiers in Computational Neuroscience, on CRCNS data set ia-1
3	# (doi:10.6080/K0BG2KWB).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-04, protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the version of record in PubMed Central (PMC2525941, open access), from Europe PMC
8	# full-text XML, as supplied under paper/, with its Materials and Methods, Results, Discussion,
9	# the legends of Figures 1 to 10 and Table 1. No PDF was supplied, so values shown only in
10	# figures (Figure 5, Figure 9B and the population histograms of Figure 7) could not be read.
11	# The paper has no supplement. It links no analysis code, so none was read. Some passages are
12	# garbled in the text and are named in the claims that use them (Results, Quantitative
13	# description, paragraph 7, "no <69%"; Qualitative description, paragraph 5, a ratio of
14	# sigma to itself).
15	#
16	# Data the paper used. Adult Locusta migratoria, intracellular recordings from auditory
17	# receptor axons in the tympanal nerve; 37 receptor cells from 23 animals. Each cell was tested
18	# with two or more stimuli, 132 sessions in all (a session is one cell in one stimulus
19	# condition), of which 86 passed the selection (mean rate near 100 Hz, trial-to-trial SD of the
20	# firing rate below 35 Hz). Stimuli were amplitude-modulated sine carriers at the cell's best
[... 961 more lines not kept]
```

**Agent**

Claims file read: 26 claims. Next, the data descriptor and the example entry's format.

**Agent calls Bash**

```bash
cat paper/ia-1.data-description.txt; cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ia-1/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)</IsTruncated>',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ia-1; curl -s $B/checksums.md5; curl -s $B/filelist.txt; curl -sI $B/crcns-ia1.zip | head; python3 -c "import fsspec,scipy,numpy; print(fsspec.__version__)"; which uv
```

```
f0740514fabc6995fe54b2a361b6c763  crcns-ia1.zip
acc5d91bbad403c5ac1d25876e275294  docs/crcns-ia1-CONDITIONS.txt
8d286e783e311ef00ff491d113f2c47d  docs/crcns-ia1-README.txt
69c40a5333390d058c4d41957a598abd  filelist.txt
# CRCNS.org 'ia-1' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 crcns-ia1.zip	47897577 (45.6 MB)
 docs/crcns-ia1-CONDITIONS.txt	1360 (1.3 KB)
 docs/crcns-ia1-README.txt	12386 (12.0 KB)
 checksums.md5	219
HTTP/1.1 200 OK
x-amz-id-2: fSjqOU/iQUrPHp3xF6IKdlftWAl5KOkhCKFMnD235NPzRzmixMLrewabDQnywIPNiyokH1qY0L8=
x-amz-request-id: XJZDMCSPG0M6RYD7
Date: Wed, 04 Nov 2026 18:21:36 GMT
Last-Modified: Wed, 11 Feb 2026 01:25:03 GMT
ETag: "f0740514fabc6995fe54b2a361b6c763"
x-amz-storage-class: INTELLIGENT_TIERING
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests numpy scipy pandas statsmodels matplotlib && python -c "
import fsspec,zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ia-1/crcns-ia1.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
names=z.namelist(); print(len(names))
import collections
for i in z.infolist()[:60]: print(i.file_size,i.filename)
"
```

```
2594
0 crcns-ia1/
6148 crcns-ia1/.DS_Store
0 crcns-ia1/Data1/
6148 crcns-ia1/Data1/.DS_Store
0 crcns-ia1/Data1/03-01-15-aa/
6148 crcns-ia1/Data1/03-01-15-aa/.DS_Store
8866 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig1_long.dat
80637 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig1_spikes.dat
8249 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig2_long.dat
83286 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig2_spikes.dat
199 crcns-ia1/Data1/03-01-15-aa/cell.dat
0 crcns-ia1/Data1/03-01-15-ab/
6148 crcns-ia1/Data1/03-01-15-ab/.DS_Store
8390 crcns-ia1/Data1/03-01-15-ab/03-01-15-ab_sig1_long.dat
342295 crcns-ia1/Data1/03-01-15-ab/03-01-15-ab_sig1_spikes.dat
7629 crcns-ia1/Data1/03-01-15-ab/03-01-15-ab_sig2_long.dat
317724 crcns-ia1/Data1/03-01-15-ab/03-01-15-ab_sig2_spikes.dat
209 crcns-ia1/Data1/03-01-15-ab/cell.dat
0 crcns-ia1/Data1/03-01-16-ab/
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,collections,re
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ia-1/crcns-ia1.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
infos=z.infolist()
d1=[i for i in infos if '/Data1/' in i.filename]
dirs=sorted({i.filename.split('/')[2] for i in d1 if len(i.filename.split('/'))>3})
print('Data1 dirs',len(dirs)); print(dirs)
ext=collections.Counter(re.sub(r'.*?(_sig\d_)?','',i.filename.split('/')[-1]) if i.filename.split('/')[2] in dirs else 'x' for i in d1)
print(collections.Counter(i.filename.split('/')[-1].split('_')[-1] for i in d1))
for i in infos:
  p=i.filename.split('/')
  if len(p)<=4 and not p[-1]=='' : print(i.file_size,i.filename)
" 2>&1 | head -120
```

```
Data1 dirs 76
['03-01-15-aa', '03-01-15-ab', '03-01-16-ab', '03-01-30-ad', '03-01-30-ae', '03-02-14-aa', '03-02-18-ab', '03-02-25-ac', '03-02-25-aj', '03-03-05-ab', '03-03-05-ac', '03-03-06-aa', '03-03-06-ab', '03-03-14-aa', '03-03-14-ab', '03-03-14-ac', '03-03-14-ad', '03-03-18-aa', '03-03-18-ab', '03-03-18-ac', '03-03-18-ad', '03-03-18-ae', '03-03-21-aa', '03-03-21-ab', '03-03-21-ac', '03-04-02-aa', '03-04-04-aa', '03-04-08-aa', '03-04-08-ab', '03-04-08-ac', '03-04-11-aa', '03-04-11-ab', '03-04-15-aa', '03-04-16-aa', '03-04-16-ab', '03-04-16-ac', '03-04-16-ad', '03-04-16-ae', '03-04-16-af', '03-04-16-ag', '03-04-23-aa', '03-04-23-ab', '03-04-23-ac', '03-04-23-ad', '03-04-23-ae', '03-04-23-af', '03-04-23-ag', '03-04-23-ah', '03-04-23-ai', '03-04-23-aj', '03-04-25-ac', '03-04-25-ad', '03-04-25-ae', '03-04-25-af', '03-04-25-ag', '03-04-25-ah', '03-04-30-aa', '03-04-30-ac', '03-05-02-aa', '03-05-02-ab', '03-05-02-ac', '03-05-02-ad', '03-05-02-ae', '03-05-06-aa', '03-05-06-ab', '03-05-06-ac', '03-05-09-ab', '03-05-09-ac', '03-05-09-ad', '03-06-27-ab', '03-06-27-ac', '03-06-27-ae', '03-06-27-af', '03-06-27-ag', '03-07-03-aa', 'stimuli']
Counter({'long.dat': 150, 'spikes.dat': 150, '': 77, 'cell.dat': 75, 'Store': 71, 'co200.dat': 5, 'rates': 1, 'singlecells.txt': 1, 'co100.dat': 1, 'co1600.dat': 1, 'co25.dat': 1, 'co400.dat': 1, 'co50.dat': 1, 'co800.dat': 1, 'stimtodB.m': 1})
6148 crcns-ia1/.DS_Store
6148 crcns-ia1/Data1/.DS_Store
6148 crcns-ia1/Data1/03-01-15-aa/.DS_Store
8866 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig1_long.dat
80637 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig1_spikes.dat
8249 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig2_long.dat
83286 crcns-ia1/Data1/03-01-15-aa/03-01-15-aa_sig2_spikes.dat
199 crcns-ia1/Data1/03-01-15-aa/cell.dat
6148 crcns-ia1/Data1/03-01-15-ab/.DS_Store
8390 crcns-ia1/Data1/03-01-15-ab/03-01-15-ab_sig1_long.dat
342295 crcns-ia1/Data1/03-01-15-ab/03-01-15-ab_sig1_spikes.dat
7629 crcns-ia1/Data1/03-01-15-ab/03-01-15-ab_sig2_long.da
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ia-1/crcns-ia1.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for i in z.infolist():
  n=i.filename
  if '/Data1/' in n and (n.split('/')[2]=='stimuli' or n.count('/')==2): print(i.file_size,n)
r=lambda n: z.read('crcns-ia1/Data1/'+n).decode('latin1')
print(r('singlecells.txt'))
for d in ['03-01-15-aa','03-04-23-aa','03-06-27-ab']: print(d, r(d+'/cell.dat'))
s=r('03-01-15-aa/03-01-15-aa_sig1_spikes.dat'); print(s[:1500])
print(r('03-01-15-aa/03-01-15-aa_sig1_long.dat')[:800])
print(r('stimuli/stimtodB.m'))
" 2>&1
```

```
0 crcns-ia1/Data1/
6148 crcns-ia1/Data1/.DS_Store
20035 crcns-ia1/Data1/firing_rates
606 crcns-ia1/Data1/singlecells.txt
0 crcns-ia1/Data1/stimuli/
6148 crcns-ia1/Data1/stimuli/.DS_Store
3814227 crcns-ia1/Data1/stimuli/gauss_st12_co200.dat
3553306 crcns-ia1/Data1/stimuli/gauss_st3_co200.dat
3627347 crcns-ia1/Data1/stimuli/gauss_st6_co100.dat
3627795 crcns-ia1/Data1/stimuli/gauss_st6_co1600.dat
3627459 crcns-ia1/Data1/stimuli/gauss_st6_co200.dat
3624752 crcns-ia1/Data1/stimuli/gauss_st6_co25.dat
3628097 crcns-ia1/Data1/stimuli/gauss_st6_co400.dat
3627537 crcns-ia1/Data1/stimuli/gauss_st6_co50.dat
3627474 crcns-ia1/Data1/stimuli/gauss_st6_co800.dat
3649737 crcns-ia1/Data1/stimuli/gaussModality_co200.dat
3583656 crcns-ia1/Data1/stimuli/lmd_co200.dat
117 crcns-ia1/Data1/stimuli/stimtodB.m
03-01-15-ab
03-01-16-ab
[... 423 more lines not kept]
```

**Agent**

The data set has 75 Data1 experiment directories (2 stimuli each, 150 sessions), a `singlecells.txt` with 43 cell rows, a `firing_rates` file, and the stimulus files. Next: parse every session.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ia-1/crcns-ia1.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
t=z.read('crcns-ia1/Data1/firing_rates').decode('latin1'); print(t[:3000]); print(len(t.splitlines()))
s=z.read('crcns-ia1/Data1/stimuli/gauss_st6_co200.dat').decode('latin1'); print(s[:600]); print(len(s.splitlines()))
s=z.read('crcns-ia1/Data1/03-04-23-aa/03-04-23-aa_sig1_spikes.dat').decode('latin1'); print(s[:1200])
"
```

```
./03-01-15-aa/03-01-15-aa_sig1_spikes.dat
gaussModality_co200
(n=90) firing rate = 50.09 +/- 126.82 [Hz]
------------------------------------------
./03-01-15-aa/03-01-15-aa_sig2_spikes.dat
lmd_co200
(n=89) firing rate = 57.21 +/- 123.70 [Hz]
------------------------------------------
./03-01-15-ab/03-01-15-ab_sig1_spikes.dat
gaussModality_co200
(n=476) firing rate = 39.32 +/- 117.17 [Hz]
------------------------------------------
./03-01-15-ab/03-01-15-ab_sig2_spikes.dat
lmd_co200
(n=476) firing rate = 36.68 +/- 100.45 [Hz]
------------------------------------------
./03-01-16-ab/03-01-16-ab_sig1_spikes.dat
gauss_st6_co200
(n=109) firing rate = 41.15 +/- 79.10 [Hz]
------------------------------------------
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-neuro.10.003.2008.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-neuro.10.003.2008.txt",
 "offset": 242,
 "limit": 143
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the paper. Now I'll check the attempt schema and the entry tool's expectations, then write the loader.

**Agent calls Bash**

```bash
ls schemas tools; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
[... 292 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[6000:12000])"; grep -n "crcns\|related\|def check\|install" tools/entry.py | head -60
```

```
cked"
]
},
"blocked_by": {
"description": "Required when outcome is blocked.",
"enum": [
"data_missing",
"metadata_insufficient",
"methods_underspecified",
"data_unreadable",
"too_large",
"not_runnable",
"other"
]
},
"reason": {
"type": "string",
"minLength": 1
}
}
[... 314 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 143,330p tools/entry.py
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

[... 168 more lines not kept]
```

**Agent**

Now the loader in the helper module. I'll survey every session (stimulus, trials, rates, headers) before analysing.

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-ia-1-eyherabide-2008/ia1.py",
 "content": "\"\"\"Loading and burst measures for CRCNS data set ia-1 (locust auditory receptors, Data1).\n\nEyherabide, Rokem, Herz & Samengo (2008), Frontiers in Computational Neuroscience,\ndoi:10.3389/neuro.10.003.2008.\n\nThe data set is one zip file in the public CRCNS bucket, streamed with fsspec and read in\nplace with zipfile; nothing is written to disk. CRCNS data sets are not versioned: the MD5 sum\nof the zip in the data set's checksums.md5 (`ZIP_MD5`) is checked against the object's ETag\nwhen the zip is opened, so that a change of the file is detected.\n\nData1 holds one directory per experiment (`03-04-23-aa`), each with two stimuli (`sig1`,\n`sig2`). `*_spikes.dat` holds the spike times (microseconds from the stimulus trigger) of the\nrepeated 1 s presentations, trial after trial, each trial behind a `#` header; `cell.dat` names\nthe two stimulus files and the intensity they were played at (the maximal intensity, the mean\nplus 3 SD, data descriptor); `singlecells.txt` lists the experiments made on one cell. The\nstimulus files hold the AM signal in volts at 20 kHz for 10 s; `stimtodB.m` converts them to dB.\n\nWhere the parameters come from (claims file, opening comment, and the paper's Methods):\n\n- `DT = 0.1 ms` bins and the analysis window 200 to 1000 ms: Methods, Burst identification,\n  paragraph 2, and Electrophysiology and stimulus design, paragraph 5 (\"the first 200 msec of\n  each trial were discarded\").\n- The burst test (`burst_limit`): Methods, Burst identification, paragraphs 4 to 6: a first peak\n  of C_s below 5 ms, bounded on its right by a minimum below 1.25 / cutoff that differs from\n  the maximum by more than the sum of their error bars, Delta = sigma / sqrt(N). The readings\n  of the open details (1) to (3) of the claims file are arguments: `peak` \"a\" (first local\n  maximum for tau > 0) or \"b\" (largest value in 0 < tau < 5 ms); `minimum` \"a\" (first local\n  minimum after the peak that differs significantly from the maximum) or \"b\" (lowest value\n  between the peak and 1.25 / cutoff, required to differ significantly); `nmode` \"a\" (N the\n  number of product terms at each tau) or \"b\" (N the number of trials).\n- Bursts (`bursts_of_trial`): consecutive spikes whose ISIs are within the domain of the first\n  peak, 0 to the position of the minimum (paragraph 7); a burst is dated by its first spike.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nimport zipfile\nfrom dataclasses import dataclass, field\n\nimport fsspec\nimport numpy as np\nimport requests\n\nCRCNS_ID = \"ia-1\"\nVERSION = \"unversioned\"\nDATASET_DOI = \"10.6080/K0BG2KWB\"\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com\"\nZIP_URL = f\"{BUCKET}/{CRCNS_ID}/crcns-ia1.zip\"\nZIP_MD5 = \"f0740514fabc6995fe54b2a361b6c763\"   # crcns-ia1.zip in ia-1/checksums.md5\nROOT = \"crcns-ia1/Data1/\"\n\nDT = 1e-4                  # s, 0.1 ms bins (Methods, Burst identification)\nT_TRIAL = 1.0              # s, stimulus length\nT0, T1 = 0.2, 1.0          # s, analysis window (Methods: first 200 ms discarded)\nSTIM_RATE = 20000.0        # Hz, stimulus files (data descriptor)\nPEAK_MAX = 5e-3            # s, first peak below 5 ms (Methods)\nMIN_FACTOR = 1.25          # minimum below 1.25 / cutoff (Methods)\n\n# The seven protocols of Table 1, (SD dB, cutoff Hz) -> protocol number.\nPROTOCOLS = {(6, 200): 1, (3, 200): 2, (12, 200): 3, (6, 25): 4, (6, 100): 5, (6, 400): 6, (6, 800): 7}\n\n\ndef open_zip() -> zipfile.ZipFile:\n    \"\"\"Open the data set's zip in place, after checking its ETag against checksums.md5.\"\"\"\n    etag = requests.head(ZIP_URL, timeout=60).headers[\"ETag\"].strip('\"')\n    if etag != ZIP_MD5:\n        raise RuntimeError(f\"crcns-ia1.zip has changed: ETag {etag}, checksums.md5 {ZIP_MD5}\")\n    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())\n\n\n@dataclass\nclass Session:\n    \"\"\"One cell (experiment directory) in one stimulus condition.\"\"\"\n    exp: str                  # experiment directory, e.g. 03-04-23-aa\n    sig: int                  # 1 or 2\n    stimulus: str             # stimulus file name without .dat, from cell.dat\n    intensity: float          # dB, maximal intensity from cell.dat\n    cell_cutoff: float        # Hz, from cell.dat\n    trials: list = field(repr=False)   # spike times per trial, s, all spikes of the file\n    header: dict = field(default_factory=dict)   # first trial's header, when an OEL header\n    offline: bool = False     # off-line spike detection (OFFOEL header)\n\n    @property\n    def sd_cut(self):\n        m = re.fullmatch(r\"(?:gauss_)?st(\\d+)_co(\\d+)\", self.stimulus)\n        return (int(m.group(1)), int(m.group(2))) if m else None\n\n    @property\n    def protocol(self):\n        return PROTOCOLS.get(self.sd_cut)\n\n    @property\n    def cutoff(self):\n        return self.sd_cut[1] if self.sd_cut else self.cell_cutoff\n\n    @property\n    def name(self):\n        return f\"{self.exp}_sig{self.sig}\"\n\n    @property\n    def n_trials(self):\n        return len(self.trials)\n\n\ndef parse_spikes(text: str):\n    \"\"\"Split a *_spikes.dat file into trials (s) and return the first header's fields.\n\n    Each trial starts with a block of `#` lines; spike times are in microseconds.\"\"\"\n    trials, header, current, in_header = [], {}, None, False\n    for line in text.splitlines():\n        line = line.strip()\n        if line.startswith(\"#\"):\n            if not in_header:\n                current = []\n                trials.append(current)\n                in_header = True\n            if len(trials) == 1 and \":\" in line:\n                k, v = line[1:].split(\":\", 1)\n                header[k.strip()] = v.strip()\n            continue\n        in_header = False\n        if line:\n            current.append(float(line) * 1e-6)\n    return [np.asarray(t) for t in trials], header\n\n\ndef parse_cell(text: str):\n    \"\"\"The two stimuli of an experiment from cell.dat: {sig: (name, intensity dB, cutoff Hz)}.\"\"\"\n    out = {}\n    for m in re.finditer(r\"Signal\\s+(\\d)\\s*Name:\\s*(\\S+)\\s*Intensity:\\s*([\\d.]+)\\s*dB\\s*\"\n                         r\"Cut off frequency:\\s*([\\d.]+)\", text):\n        out[int(m.group(1))] = (m.group(2).removesuffix(\".dat\"), float(m.group(3)), float(m.group(4)))\n    return out\n\n\ndef load_sessions(z: zipfile.ZipFile):\n    \"\"\"Every Data1 session, in directory order.\"\"\"\n    names = z.namelist()\n    exps = sorted({n.split(\"/\")[2] for n in names\n                   if n.startswith(ROOT) and n.count(\"/\") >= 3 and n.split(\"/\")[2] != \"stimuli\"})\n    sessions = []\n    for exp in exps:\n        cell = parse_cell(z.read(f\"{ROOT}{exp}/cell.dat\").decode(\"latin1\"))\n        for sig in (1, 2):\n            path = f\"{ROOT}{exp}/{exp}_sig{sig}_spikes.dat\"\n            if path not in names:\n                continue\n            text = z.read(path).decode(\"latin1\")\n            trials, header = parse_spikes(text)\n            stim, inten, cut = cell[sig]\n            sessions.append(Session(exp, sig, stim, inten, cut, trials, header,\n                                    offline=\"OFFOEL\" in text[:200]))\n    return sessions\n\n\ndef load_singlecells(z: zipfile.ZipFile):\n    \"\"\"Rows of singlecells.txt as lists of experiment names (one row per cell).\"\"\"\n    rows = []\n    for line in z.read(f\"{ROOT}singlecells.txt\").decode(\"latin1\").splitlines():\n        parts = line.split()\n        if parts:\n            date = parts[0][:-2]\n            rows.append([parts[0]] + [date + p for p in parts[1:]])\n    return rows\n\n\ndef load_stimulus_db(z: zipfile.ZipFile, stimulus: str, max_db: float, duration=T_TRIAL):\n    \"\"\"The AM signal in dB at 20 kHz over the first `duration` s, as stimtodB.m computes it:\n    20 log10(v / 2e-5), shifted so that its maximum over the whole 10 s file is `max_db`.\"\"\"\n    name = stimulus if stimulus.startswith((\"gauss\", \"lmd\")) else \"gauss_\" + stimulus\n    data = np.loadtxt(z.open(f\"{ROOT}stimuli/{name}.dat\"))\n    db = 20 / np.log(10) * np.log(data[:, 1] / 2.0e-5)\n    db = max_db - db.max() + db\n    t = data[:, 0] * 1e-6\n    keep = t < duration\n    return t[keep], db[keep]\n\n\n# ---------------------------------------------------------------- spike-train measures\n\ndef binned(trials, t0=T0, t1=T1, dt=DT):\n    \"\"\"Spike counts per trial and bin over [t0, t1): an (n_trials, n_bins) uint8 array.\"\"\"\n    nb = int(round((t1 - t0) / dt))\n    out = np.zeros((len(trials), nb), dtype=np.uint8)\n    for i, t in enumerate(trials):\n        k = np.floor((t[(t >= t0) & (t < t1)] - t0) / dt).astype(int)\n        np.add.at(out[i], k, 1)\n    return out\n\n\ndef trial_rates(trials, t0=T0, t1=T1):\n    \"\"\"Firing rate of each trial over [t0, t1), Hz.\"\"\"\n    return np.array([np.sum((t >= t0) & (t < t1)) / (t1 - t0) for t in trials])\n\n\ndef correlation(trials, max_lag, t0=T0, t1=T1, dt=DT):\n    \"\"\"C_s(tau) of Eq. 1 for tau = 0, dt, ..., max_lag, with its error bar.\n\n    rho is 1/dt in a bin with a spike and 0 otherwise; the bar is the trial and time average of\n    (rho(t) - rbar)(rho(t + tau) - rbar) over the pairs inside the window. Returns tau (s), C_s\n    (Hz^2), the SD of the product terms, and their number at each tau (n_trials * (n_bins - k)).\"\"\"\n    x = (binned(trials, t0, t1, dt) > 0).astype(float) / dt\n    n_tr, nb = x.shape\n    rbar = x.mean()\n    y = x - rbar\n    nlag = int(round(max_lag / dt)) + 1\n    # Sums of products and squared products for every lag, by FFT over time, summed over trials.\n    nfft = 1 << int(np.ceil(np.log2(2 * nb)))\n    f = np.fft.rfft(y, nfft, axis=1)\n    s1 = np.fft.irfft((f.conj() * f).sum(0), nfft)[:nlag]\n    f2 = np.fft.rfft(y ** 2, nfft, axis=1)\n    s2 = np.fft.irfft((f2.conj() * f2).sum(0), nfft)[:nlag]\n    count = n_tr * (nb - np.arange(nlag))\n    c = s1 / count\n    sd = np.sqrt(np.maximum(s2 / count - c ** 2, 0))\n    return np.arange(nlag) * dt, c, sd, count, n_tr\n\n\ndef burst_limit(trials, cutoff, peak=\"a\", minimum=\"a\", nmode=\"a\", dt=DT):\n    \"\"\"The limiting ISI of a session (s), or 0 when the first peak is not separable.\n\n    Methods, Burst identification: the first peak of C_s must lie below 5 ms; the minimum to its\n    right below 1.25 / cutoff; the two must differ by more than the sum of their error bars,\n    Delta = sigma / sqrt(N). Readings of the open details are given by `peak`, `minimum` and\n    `nmode` (see the module docstring). Also returns the details used.\"\"\"\n    max_lag = max(MIN_FACTOR / cutoff, PEAK_MAX) + 2 * dt\n    tau, c, sd, count, n_tr = correlation(trials, max_lag, dt=dt)\n    n = count if nmode == \"a\" else np.full_like(count, n_tr)\n    err = sd / np.sqrt(n)\n    info = dict(tau=tau, c=c, err=err)\n    lim_i = int(np.floor(MIN_FACTOR / cutoff / dt + 1e-9))\n    pk_i = int(np.floor(PEAK_MAX / dt + 1e-9))\n    # The peak, excluding tau = 0 (the self term).\n    if peak == \"a\":\n        cand = [i for i in range(1, min(pk_i, len(c) - 2) + 1) if c[i] > c[i - 1] and c[i] >= c[i + 1]]\n        if not cand:\n            return 0.0, info\n        ip = cand[0]\n    else:\n        ip = 1 + int(np.argmax(c[1:pk_i + 1]))\n        if ip == pk_i or c[ip] < c[ip + 1]:        # no maximum inside (0, 5 ms)\n            return 0.0, info\n    info[\"peak\"] = ip\n    sig = lambda j: c[ip] - c[j] > err[ip] + err[j]\n    if minimum == \"a\":\n        ims = [j for j in range(ip + 1, min(lim_i, len(c) - 2) + 1)\n               if c[j] < c[j - 1] and c[j] <= c[j + 1] and sig(j)]\n        if not ims:\n            return 0.0, info\n        im = ims[0]\n    else:\n        if lim_i <= ip:\n            return 0.0, info\n        im = ip + 1 + int(np.argmin(c[ip + 1:lim_i + 1]))\n        if not sig(im):\n            return 0.0, info\n    info[\"min\"] = im\n    return im * dt, info\n\n\ndef bursts_of_trial(t, limit):\n    \"\"\"Burst onsets and spike counts n of one trial: consecutive spikes with ISI <= limit form\n    one burst, dated by its first spike. With limit 0 every spike is a 1-burst.\"\"\"\n    t = np.sort(t)\n    if len(t) == 0:\n        return t, np.zeros(0, int)\n    new = np.r_[True, np.diff(t) > limit]\n    starts = np.flatnonzero(new)\n    n = np.diff(np.r_[starts, len(t)])\n    return t[starts], n\n\n\ndef bursts(trials, limit, t0=T0, t1=T1):\n    \"\"\"Bursts of every trial whose onset is in [t0, t1): (trial index, onset s, n, spike times).\n\n    Bursts are formed on the whole trial, so a burst that starts before t0 is not cut.\"\"\"\n    out = []\n    for i, t in enumerate(trials):\n        on, n = bursts_of_trial(t, limit)\n        keep = (on >= t0) & (on < t1)\n        out.append((np.full(keep.sum(), i), on[keep], n[keep]))\n    tr = np.concatenate([o[0] for o in out]) if out else np.zeros(0, int)\n    on = np.concatenate([o[1] for o in out]) if out else np.zeros(0)\n    n = np.concatenate([o[2] for o in out]) if out else np.zeros(0, int)\n    return tr, on, n\n"
}
```

```
File created successfully at: entries/crcns-ia-1-eyherabide-2008/ia1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-ia-1-eyherabide-2008 && . $TMPDIR/dev/bin/activate && time python -c "
import ia1,pickle,collections,numpy as np
z=ia1.open_zip()
S=ia1.load_sessions(z); sc=ia1.load_singlecells(z)
pickle.dump((S,sc),open('$TMPDIR/sess.pkl','wb'))
print(len(S))
print(collections.Counter(s.stimulus for s in S))
print(collections.Counter(s.protocol for s in S))
print(collections.Counter(s.offline for s in S))
for s in S[:3]+S[-3:]: print(s.name,s.stimulus,s.intensity,s.n_trials,s.header.get('desired firing rate (Hz)'),s.header.get('stimulus file','')[-25:], s.header.get('intensity (dB)'))
"
```

```
150
Counter({'gauss_st6_co200': 54, 'gaussModality_co200': 14, 'lmd_co200': 14, 'gauss_st6_co100': 11, 'gauss_st6_co800': 9, 'gauss_st6_co25': 9, 'gauss_st3_co200': 9, 'gauss_st12_co200': 8, 'gauss_st6_co400': 8, 'st6_co200': 7, 'st6_co50': 3, 'st6_co1600': 3, 'st6_co25': 1})
Counter({1: 61, None: 34, 5: 11, 4: 10, 7: 9, 2: 9, 3: 8, 6: 8})
Counter({False: 122, True: 28})
03-01-15-aa_sig1 gaussModality_co200 72.0 90 None  None
03-01-15-aa_sig2 lmd_co200 66.0 89 None  None
03-01-15-ab_sig1 gaussModality_co200 74.0 476 None  None
03-06-27-ag_sig2 st6_co1600 77.7 111 90 Info/gauss_st6_co1600.dat 77.6471
03-07-03-aa_sig1 st6_co200 67.8 112 100 rInfo/gauss_st6_co200.dat 67.8409
03-07-03-aa_sig2 st6_co50 69.3 111 100 orInfo/gauss_st6_co50.dat 69.2453

real	0m4.385s
user	0m1.536s
sys	0m0.139s
```

**Agent**

150 sessions load in 4 s; 116 use the paper's seven protocols. Now checks: headers against `cell.dat`, rates, trial counts, duplicates.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import ia1,pickle,collections,numpy as np, hashlib
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
mism=0
for s in S:
  h=s.header
  if h:
    hf=h['stimulus file'].split('/')[-1].removesuffix('.dat')
    if hf.replace('gauss_','')!=s.stimulus.replace('gauss_',''): print('stim mismatch',s.name,hf,s.stimulus)
    if abs(float(h['intensity (dB)'])-s.intensity)>0.1: print('int mismatch',s.name,h['intensity (dB)'],s.intensity)
    if int(h['signal'])!=s.sig: print('sig mismatch', s.name)
print(collections.Counter(s.header.get('desired firing rate (Hz)') for s in S))
print(collections.Counter(s.header.get('pause between stimuli (msec)') for s in S))
# rates
for s in S:
  r=ia1.trial_rates(s.trials); s.r=r
allsp=np.concatenate([np.concatenate(s.trials) for s in S]); print('spike time range',allsp.min(),allsp.max(), (allsp>1).mean())
# duplicates
hs=collections.defaultdict(list)
for s in S: hs[hashlib.md5(np.concatenate(s.trials).tobytes()).hexdigest()].append(s.name)
print([v for v in hs.values() if len(v)>1])
# trial-level duplicate first trial
ft=collections.defaultdict(list)
for s in S: ft[tuple(np.round(s.trials[0],5))].append(s.name)
print('dup first trial',[v for v in ft.values() if len(v)>1])
print('ntrials',min(s.n_trials for s in S),max(s.n_trials for s in S))
# repetition numbers in headers consistent?
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 8, in <module>
    hf=h['stimulus file'].split('/')[-1].removesuffix('.dat')
       ~^^^^^^^^^^^^^^^^^
KeyError: 'stimulus file'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import ia1,pickle,collections,numpy as np, hashlib
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
for s in S:
  h=s.header
  if 'stimulus file' in h:
    hf=h['stimulus file'].split('/')[-1].removesuffix('.dat')
    if hf.replace('gauss_','')!=s.stimulus.replace('gauss_',''): print('stim mismatch',s.name,hf,s.stimulus)
    if abs(float(h['intensity (dB)'])-s.intensity)>0.1: print('int mismatch',s.name,h['intensity (dB)'],s.intensity)
    if int(h['signal'])!=s.sig: print('sig mismatch', s.name)
  elif not s.offline: print('odd header',s.name,h)
print(collections.Counter(s.header.get('desired firing rate (Hz)') for s in S))
print(collections.Counter(s.header.get('pause between stimuli (msec)') for s in S))
allsp=np.concatenate([np.concatenate(s.trials) for s in S]); print('spike time range',allsp.min(),allsp.max(), (allsp>1).mean())
hs=collections.defaultdict(list)
for s in S: hs[hashlib.md5(np.concatenate(s.trials).tobytes()).hexdigest()].append(s.name)
print([v for v in hs.values() if len(v)>1])
ft=collections.defaultdict(list)
for s in S: ft[tuple(np.round(s.trials[0],5))].append(s.name)
print('dup first trial',[v for v in ft.values() if len(v)>1])
print('ntrials',min(s.n_trials for s in S),max(s.n_trials for s in S))
"
```

```
odd header 03-01-30-ad_sig1 {'repro call number': '0', 'mode': '3', 'signal': '1', 'carrier freq (kHz)': '14', 'stimulus length (msec)': '1000', 'pause between stimuli (msec)': '450', 'length of ramp (usec)': '1000', 'desired firing rate (Hz)': '100', 'standard deviation (dB)': '6', 'cut-off frequency (Hz)': '200', 'repetition number': '46', 'duration (msec)': '1000', 'intensity (dB)': '100'}
odd header 03-01-30-ad_sig2 {'repro call number': '0', 'mode': '3', 'signal': '2', 'carrier freq (kHz)': '14', 'stimulus length (msec)': '1000', 'pause between stimuli (msec)': '450', 'length of ramp (usec)': '1000', 'desired firing rate (Hz)': '100', 'standard deviation (dB)': '6', 'cut-off frequency (Hz)': '800', 'repetition number': '46', 'duration (msec)': '1000', 'intensity (dB)': '100'}
odd header 03-02-25-ac_sig1 {'repro call number': '0', 'mode': '3', 'signal': '1', 'carrier freq (kHz)': '3.53553', 'stimulus length (msec)': '1000', 'pause between stimuli (msec)': '700', 'length of ramp (usec)': '1000', 'desired firing rate (Hz)': '100', 'standard deviation (dB)': '6', 'cut-off frequency (Hz)': '200', 'repetition number': '1', 'duration (msec)': '1000', 'intensity (dB)': '74.6591'}
odd header 03-02-25-ac_sig2 {'repro call number': '0', 'mode': '3', 'signal': '2', 'carrier freq (kHz)': '3.53553', 'stimulus length (msec)': '1000', 'pause between stimuli (msec)': '700', 'length of ramp (usec)': '1000', 'desired firing rate (Hz)': '100', 'standard deviation (dB)': '6', 'cut-off frequency (Hz)': '400', 'repetition number': '1', 'duration (msec)': '1000', 'intensity (dB)': '74.4737'}
odd header 03-02-25-aj_sig1 {'repro call number': '0', 'mode': '3', 'signal': '1', 'carrier freq (kHz)': '5', 'stimulus length (msec)': '1000', 'pause between stimuli (msec)': '700', 'length of ramp (usec)': '1000', 'desired firing rate (Hz)': '100', 'standard deviation (dB)': '6', 'cut-off frequency (Hz)': '200', 'repetition number': '1', 'duration (msec)': '1000', 'intensity (dB)': '44.4828'}
od
[... 42 more lines not kept]
```

**Agent**

Headers agree with `cell.dat` on stimulus; intensities differ by under 1 dB mostly, with three larger gaps. No duplicate recordings. Now the selection quantities per session.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import ia1,pickle,collections,numpy as np
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
P=[s for s in S if s.protocol]
for lab,(a,b) in {'200-1000':(0.2,1.0),'0-1000':(0,1.0)}.items():
  m=np.array([ia1.trial_rates(s.trials,a,b).mean() for s in S]); sd=np.array([ia1.trial_rates(s.trials,a,b).std(ddof=1) for s in S])
  print(lab,'all150 mean rate',m.mean(),'sd',m.std(ddof=1),'median sd',np.median(sd), 'mean sd',sd.mean(),'n sd<35',(sd<35).sum())
  isp=np.array([s.protocol is not None for s in S])
  print('  in protocols',isp.sum(),'sd<35',(sd[isp]<35).sum(), 'mean sd', sd[isp].mean(), 'rates', np.percentile(m[isp],[0,25,50,75,100]))
  print('  SD distribution', np.percentile(sd,[0,10,25,50,75,90,100]).round(1))
"
```

```
200-1000 all150 mean rate 109.39542729887803 sd 15.488577768681205 median sd 5.774097886238179 mean sd 7.084297265950514 n sd<35 149
  in protocols 116 sd<35 115 mean sd 6.7755924665211165 rates [ 65.65441176 103.03841684 110.11734496 118.1102833  169.10194175]
  SD distribution [ 3.   3.7  4.5  5.8  7.9 10.5 40.9]
0-1000 all150 mean rate 114.08786146997117 sd 15.668672081042851 median sd 5.569192410983366 mean sd 6.664729448679005 n sd<35 150
  in protocols 116 sd<35 116 mean sd 6.300221484888262 rates [ 74.59677419 107.24       114.67550505 123.01336957 179.54368932]
  SD distribution [ 2.8  3.6  4.2  5.6  7.4  9.9 34.6]
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate && python -c "
import ia1,pickle,collections,numpy as np
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
exps=collections.defaultdict(list)
for s in S: exps[s.exp].append(s)
pair=[e for e,v in exps.items() if all(x.protocol for x in v)]
print('exps',len(exps),'both in protocols',len(pair))
print(collections.Counter(tuple(sorted(x.protocol for x in exps[e])) for e in pair))
print('other combos',collections.Counter(tuple(x.stimulus for x in v) for e,v in exps.items() if e not in pair))
cell_of={e:i for i,row in enumerate(sc) for e in row}
print('exps not in singlecells',[e for e in exps if e not in cell_of], 'rows',len(sc),'rows w/o data',[r for r in sc if not any(e in exps for e in r)])
pc={cell_of[e] for e in pair}; print('cells with protocol pairs',len(pc),'dates',len({e[:8] for e in pair}))
print('all cells',len({cell_of[e] for e in exps}),'all dates',len({e[:8] for e in exps}))
print('sessions in protocol pairs', 2*len(pair))
"
```

```
Exit code 1
Wed Nov  4 18:24:01 UTC 2026
Traceback (most recent call last):
  File "<string>", line 13, in <module>
    print('all cells',len({cell_of[e] for e in exps}),'all dates',len({e[:8] for e in exps}))
                           ~~~~~~~^^^
KeyError: '03-01-15-aa'
exps 75 both in protocols 55
Counter({(1, 5): 11, (1, 4): 10, (1, 7): 9, (1, 2): 9, (1, 3): 8, (1, 6): 8})
other combos Counter({('gaussModality_co200', 'lmd_co200'): 14, ('st6_co200', 'st6_co50'): 3, ('st6_co200', 'st6_co1600'): 3})
exps not in singlecells ['03-01-15-aa', '03-06-27-ae'] rows 43 rows w/o data []
cells with protocol pairs 33 dates 21
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time python -c "
import ia1,pickle,collections,numpy as np, itertools
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
P=[s for s in S if s.protocol]
res={}
for combo in itertools.product('ab','ab','ab'):
  cnt=collections.Counter(); tot=collections.Counter(); lims=[]
  for s in P:
    lim,_=ia1.burst_limit(s.trials,s.cutoff,*combo)
    tr,on,n=ia1.bursts(s.trials,lim)
    tot[s.protocol]+=1
    if (n>1).any() and lim>0: cnt[s.protocol]+=1
    lims.append(lim)
  print(combo,[cnt[p] for p in range(1,8)],[tot[p] for p in range(1,8)], 'bursting',sum(l>0 for l in lims), 'lim ms median',np.median([l for l in lims if l>0])*1e3)
"
```

```
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
('a', 'a', 'a') [6, 0, 2, 2, 5, 0, 0] [61, 9, 8, 10, 11, 8, 9] bursting 15 lim ms median 2.9000000000000004
('a', 'a', 'b') [0, 0, 0, 0, 0, 0, 0] [61, 9, 8, 10, 11, 8, 9] bursting 0 lim ms median nan
('a', 'b', 'a') [6, 0, 2, 2, 5, 0, 0] [61, 9, 8, 10, 11, 8, 9] bursting 15 lim ms median 4.1000000000000005
('a', 'b', 'b') [0, 0, 0, 0, 0, 0, 0] [61, 9, 8, 10, 11, 8, 9] bursting 0 lim ms median nan
('b', 'a', 'a') [53, 2, 8, 9, 10, 3, 0] [61, 9, 8, 10, 11, 8, 9] bursting 85 lim ms median 3.5
('b', 'a', 'b') [0, 0, 0, 0, 0, 0, 0] [61, 9, 8, 10, 11, 8, 9] bursting 0 lim ms median nan
('b', 'b', 'a') [53, 2, 8, 9, 10, 3, 0] [61, 9, 8, 10, 11, 8, 9] bursting 85 lim ms median 4.6
('b', 'b', 'b') [0, 0, 0, 0, 0, 0, 0] [61, 9, 8, 10, 11, 8, 9] bursting 0 lim ms median nan

real	0m32.080s
user	0m25.311s
sys	0m7.061s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time python -c "
import ia1,pickle,collections,numpy as np
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
P=[s for s in S if s.protocol]
out={k:[] for k in ['aa','ab','ba','bb']}
for s in P[:40]:
  tau,c,sd,count,ntr=ia1.correlation(s.trials,0.7999)
  for nm,n in [('a',count),('b',np.full_like(count,ntr))]:
    err=sd/np.sqrt(n)
    L=int(1.25/s.cutoff/ia1.DT)
    out[nm+'a'].append(err[:L+1].mean()/(c[:L+1].max()-c[:L+1].min()))
    out[nm+'b'].append(err.mean()/(c.max()-c.min()))
for k,v in out.items(): print(k, np.mean(v)*100, np.std(v,ddof=1)*100)
s=P[0]; tau,c,sd,count,ntr=ia1.correlation(s.trials,0.012)
print(s.name, s.cutoff); print(np.c_[tau[:80:2]*1e3,c[:80:2].round(0),(sd/np.sqrt(count))[:80:2].round(0)])
"
```

```
aa 0.07091698945860817 0.022654718440464575
ab 0.15002936556914048 0.036686656296915365
ba 6.318115643037019 2.0017296401545597
bb 7.399649960293974 1.8442267405205968
03-01-16-ab_sig1 200
[[ 0.0000e+00  9.3535e+05  1.0161e+04]
 [ 2.0000e-01 -8.9210e+03  1.3800e+02]
 [ 4.0000e-01 -8.9230e+03  1.3800e+02]
 [ 6.0000e-01 -8.9270e+03  1.3800e+02]
 [ 8.0000e-01 -8.9290e+03  1.3800e+02]
 [ 1.0000e+00 -8.8120e+03  1.7800e+02]
 [ 1.2000e+00 -8.9290e+03  1.3800e+02]
 [ 1.4000e+00 -8.9260e+03  1.3800e+02]
 [ 1.6000e+00 -8.9260e+03  1.3800e+02]
 [ 1.8000e+00 -8.9270e+03  1.3800e+02]
 [ 2.0000e+00 -8.9240e+03  1.3800e+02]
 [ 2.2000e+00 -8.9230e+03  1.3800e+02]
 [ 2.4000e+00 -8.9210e+03  1.3800e+02]
 [ 2.6000e+00 -8.9180e+03  1.3800e+02]
 [ 2.8000e+00 -8.9140e+03  1.3800e+02]
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='ia1.py'; s=open(p).read()
s=s.replace('''    count = n_tr * (nb - np.arange(nlag))
    c = s1 / count
    sd = np.sqrt(np.maximum(s2 / count - c ** 2, 0))
    return np.arange(nlag) * dt, c, sd, count, n_tr''','''    count = n_tr * (nb - np.arange(nlag))
    c = s1 / count
    sd = np.sqrt(np.maximum(s2 / count - c ** 2, 0))
    # Reading (c): each trial's own time average of the products; their SD over trials.
    per_trial = np.fft.irfft(f.conj() * f, nfft, axis=1)[:, :nlag] / (nb - np.arange(nlag))
    sd_trials = per_trial.std(axis=0, ddof=1)
    return np.arange(nlag) * dt, c, sd, count, n_tr, sd_trials''')
s=s.replace('''    (Hz^2), the SD of the product terms, and their number at each tau (n_trials * (n_bins - k))."""''','''    (Hz^2), the SD of the product terms, their number at each tau (n_trials * (n_bins - k)), the
    number of trials, and the SD over trials of each trial's time-averaged products."""''')
s=s.replace('''    tau, c, sd, count, n_tr = correlation(trials, max_lag, dt=dt)
    n = count if nmode == "a" else np.full_like(count, n_tr)
    err = sd / np.sqrt(n)''','''    tau, c, sd, count, n_tr, sd_trials = correlation(trials, max_lag, dt=dt)
    err = correlation_error(sd, count, n_tr, sd_trials, nmode)''')
s=s.replace('''def burst_limit(''','''def correlation_error(sd, count, n_tr, sd_trials, nmode):
    """Delta = sigma / sqrt(N) (Methods, Burst identification, paragraph 6) under reading
    "a" (sigma of the product terms, N their number), "b" (the same sigma, N the number of
    trials) or "c" (sigma over trials of each trial's C_s, N the number of trials)."""
    if nmode == "a":
        return sd / np.sqrt(count)
    if nmode == "b":
        return sd / np.sqrt(n_tr)
    return sd_trials / np.sqrt(n_tr)


def burst_limit(''')
s=s.replace('''  number of product terms at each tau) or "b" (N the number of trials).''','''  number of product terms at each tau) or "b" (N the number of trials), as the claims file
  gives them, and "c" (sigma the SD over trials of each trial's time-averaged C_s, N the number
  of trials), a third reading of "C_s (tau) can be interpreted as an average ... The error bar
  Delta of an average estimated from N samples reads Delta = sigma / sqrt(N)" (paragraph 6),
  added here because C_s is the trial average of per-trial averages.''')
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python -c "
import ia1,pickle,collections,numpy as np
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
P=[s for s in S if s.protocol]
out=collections.defaultdict(list)
for s in P:
  tau,c,sd,count,ntr,sdt=ia1.correlation(s.trials,0.7999)
  L=int(round(1.25/s.cutoff/ia1.DT))
  for nm in 'abc':
    err=ia1.correlation_error(sd,count,ntr,sdt,nm)
    out[nm+'a0'].append(err[:L+1].mean()/(c[:L+1].max()-c[:L+1].min()))
    out[nm+'b0'].append(err.mean()/(c.max()-c.min()))
    out[nm+'a1'].append(err[1:L+1].mean()/(c[1:L+1].max()-c[1:L+1].min()))
    out[nm+'b1'].append(err[1:].mean()/(c[1:].max()-c[1:].min()))
for k,v in sorted(out.items()): print(k, round(np.mean(v)*100,2), round(np.std(v,ddof=1)*100,2))
"
```

```
aa0 0.07 0.02
aa1 44.43 164.77
ab0 0.16 0.03
ab1 2.67 1.38
ba0 6.58 1.76
ba1 3970.79 14729.65
bb0 7.93 1.46
bb1 134.48 71.69
ca0 0.07 0.03
ca1 30.09 119.33
cb0 0.16 0.03
cb1 2.65 1.37
```

**Agent**

With τ = 0 (the self term) left out of the span and the whole lag range, N readings (a) and (c) both give 2.7% (SD 1.4%), inside the claim's 3.4 ± 1.5%. Now the classification with reading (c).

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time python -c "
import ia1,pickle,collections,numpy as np, itertools
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
P=[s for s in S if s.protocol]
L={}
for combo in [('a','a','c'),('a','b','c'),('b','a','c'),('b','b','c'),('b','a','a')]:
  cnt=collections.Counter(); lims=[]
  for s in P:
    lim,_=ia1.burst_limit(s.trials,s.cutoff,*combo)
    tr,on,n=ia1.bursts(s.trials,lim)
    if (n>1).any() and lim>0: cnt[s.protocol]+=1
    lims.append(lim)
  L[combo]=np.array(lims)
  print(combo,[cnt[p] for p in range(1,8)], 'bursting',sum(l>0 for l in lims), 'lim ms median',np.median([l for l in lims if l>0])*1e3)
print('agree ba c vs ba a', (L[('b','a','c')]==L[('b','a','a')]).mean())
"
```

```
('a', 'a', 'c') [6, 0, 2, 2, 5, 0, 0] bursting 15 lim ms median 2.9000000000000004
('a', 'b', 'c') [6, 0, 2, 2, 5, 0, 0] bursting 15 lim ms median 4.1000000000000005
('b', 'a', 'c') [53, 2, 8, 9, 10, 3, 0] bursting 85 lim ms median 3.5
('b', 'b', 'c') [53, 2, 8, 9, 10, 3, 0] bursting 85 lim ms median 4.6
('b', 'a', 'a') [53, 2, 8, 9, 10, 3, 0] bursting 85 lim ms median 3.5
agree ba c vs ba a 0.9913793103448276

real	0m26.033s
user	0m20.205s
sys	0m6.134s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import ia1,pickle,collections
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
by=collections.defaultdict(list)
for s in S: by[s.exp].append(s)
for row in sc:
  st=[(s.exp[-2:],s.stimulus.replace('gauss_','')) for e in row for s in by.get(e,[])]
  prot={s.protocol for e in row for s in by.get(e,[])}
  if len(prot)>=4: print(row, st)
print(collections.Counter(len({s.protocol for e in row for s in by.get(e,[])} - {None}) for row in sc))
"
```

```
['03-03-18-ab', '03-03-18-ac', '03-03-18-ad', '03-03-18-ae'] [('ab', 'st6_co200'), ('ab', 'st3_co200'), ('ac', 'st6_co200'), ('ac', 'st6_co800'), ('ad', 'st6_co200'), ('ad', 'st6_co800'), ('ae', 'st6_co200'), ('ae', 'st12_co200')]
['03-04-08-aa', '03-04-08-ab', '03-04-08-ac'] [('aa', 'gaussModality_co200'), ('aa', 'lmd_co200'), ('ab', 'st6_co200'), ('ab', 'st6_co800'), ('ac', 'st6_co200'), ('ac', 'st3_co200')]
['03-04-16-aa', '03-04-16-ab', '03-04-16-ac', '03-04-16-ad', '03-04-16-ae'] [('aa', 'st6_co200'), ('aa', 'st6_co400'), ('ab', 'st6_co200'), ('ab', 'st6_co800'), ('ac', 'st6_co200'), ('ac', 'st6_co25'), ('ad', 'gaussModality_co200'), ('ad', 'lmd_co200'), ('ae', 'st6_co200'), ('ae', 'st12_co200')]
['03-04-23-ad', '03-04-23-ae', '03-04-23-af', '03-04-23-ag', '03-04-23-ah', '03-04-23-ai', '03-04-23-aj'] [('ad', 'st6_co200'), ('ad', 'st6_co800'), ('ae', 'st6_co200'), ('ae', 'st12_co200'), ('af', 'gaussModality_co200'), ('af', 'lmd_co200'), ('ag', 'st6_co200'), ('ag', 'st6_co400'), ('ah', 'st6_co200'), ('ah', 'st6_co100'), ('ai', 'st6_co200'), ('ai', 'st6_co25'), ('aj', 'st6_co200'), ('aj', 'st3_co200')]
['03-04-25-ac', '03-04-25-ad', '03-04-25-ae'] [('ac', 'st6_co200'), ('ac', 'st6_co800'), ('ad', 'st6_co200'), ('ad', 'st12_co200'), ('ae', 'gaussModality_co200'), ('ae', 'lmd_co200')]
['03-05-02-ab', '03-05-02-ac', '03-05-02-ad', '03-05-02-ae'] [('ab', 'st6_co200'), ('ab', 'st3_co200'), ('ac', 'gaussModality_co200'), ('ac', 'lmd_co200'), ('ad', 'st6_co200'), ('ad', 'st6_co100'), ('ae', 'st6_co200'), ('ae', 'st6_co25')]
Counter({2: 22, 0: 7, 3: 7, 1: 3, 4: 2, 5: 1, 7: 1})
```

**Agent calls Read**

```json
{
 "file_path": "entries/crcns-ia-1-eyherabide-2008/ia1.py",
 "offset": 150,
 "limit": 30
}
```

```
150	            path = f"{ROOT}{exp}/{exp}_sig{sig}_spikes.dat"
151	            if path not in names:
152	                continue
153	            text = z.read(path).decode("latin1")
154	            trials, header = parse_spikes(text)
155	            stim, inten, cut = cell[sig]
156	            sessions.append(Session(exp, sig, stim, inten, cut, trials, header,
157	                                    offline="OFFOEL" in text[:200]))
158	    return sessions
159	
160	
161	def load_singlecells(z: zipfile.ZipFile):
162	    """Rows of singlecells.txt as lists of experiment names (one row per cell)."""
163	    rows = []
164	    for line in z.read(f"{ROOT}singlecells.txt").decode("latin1").splitlines():
165	        parts = line.split()
166	        if parts:
167	            date = parts[0][:-2]
168	            rows.append([parts[0]] + [date + p for p in parts[1:]])
169	    return rows
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='ia1.py'; s=open(p).read()
old=s[s.index('def load_stimulus_db'):s.index('# ---------------------------------------------------------------- spike-train measures')]
new='''def stimulus_file(stimulus: str) -> str:
    """The stimulus file a cell.dat name refers to (`st6_co200` is `gauss_st6_co200`)."""
    return stimulus if stimulus.startswith(("gauss", "lmd")) else "gauss_" + stimulus


def load_stimulus_shape(z: zipfile.ZipFile, stimulus: str, duration=1.05):
    """The AM signal in dB relative to its maximum over the whole 10 s file, at 20 kHz, over the
    first `duration` s. stimtodB.m computes 20 log10(v / 2e-5) and shifts it so that its maximum
    is the intensity played; adding the session's intensity (`Session.intensity`, from cell.dat)
    gives the stimulus in dB SPL. Reads 1.05 s so that windows up to 15 ms after a burst near the
    end of the 1 s trial are covered (the file is 10 s long)."""
    data = np.loadtxt(z.open(f"{ROOT}stimuli/{stimulus_file(stimulus)}.dat"))
    db = 20 / np.log(10) * np.log(data[:, 1] / 2.0e-5)
    keep = data[:, 0] * 1e-6 < duration
    return db[keep] - db.max()


'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
cat >> ia1.py <<'EOF'


def burst_counts(trials, limit, t0=T0, t1=T1):
    """Number of n-bursts for n = 1, 2, ... (index n - 1) with onset in [t0, t1)."""
    _, _, n = bursts(trials, limit, t0, t1)
    return np.bincount(n, minlength=2)[1:]


def average_n(counts):
    """Mean and SD of n under the probability counts / total (Table 1 legend)."""
    n = np.arange(1, len(counts) + 1)
    p = counts / counts.sum()
    m = (p * n).sum()
    return m, np.sqrt((p * (n - m) ** 2).sum())


# ---------------------------------------------------------------- information (Eqs. 3 and 10)

def burst_rates(trials, limit, bin_s, t0=T0, t1=T1):
    """r_n(t): trial-averaged rate of n-burst onsets in bins of `bin_s` over [t0, t1), Hz,
    as a dict n -> array."""
    tr, on, n = bursts(trials, limit, t0, t1)
    nb = int(round((t1 - t0) / bin_s))
    k = np.minimum(((on - t0) / bin_s).astype(int), nb - 1)
    out = {}
    for m in np.unique(n):
        out[int(m)] = np.bincount(k[n == m], minlength=nb) / (len(trials) * bin_s)
    return out


def information(rates, T=T1 - T0):
    """Per n: rbar_n (Hz), I_n(1) in bits per event (reading i: (1/T) times the integral of
    (r_n / rbar_n) log2(r_n / rbar_n)), and I'_n = rbar_n I_n(1) in bits/s (Eq. 10 divided by T).
    Reading ii, Eq. 10 as printed, is I_n(1) times T."""
    out = {}
    for n, r in rates.items():
        rbar = r.mean()
        q = r[r > 0] / rbar
        i1 = (q * np.log2(q)).sum() / len(r)
        out[n] = dict(rbar=rbar, i1=i1, rate=rbar * i1)
    return out


def line_fit(x, y):
    """Least-squares slope, its standard error, and the one- and two-sided p of slope != 0
    (t distribution, len(x) - 2 degrees of freedom; nan below three points)."""
    from scipy import stats
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 2:
        return np.nan, np.nan, np.nan, np.nan
    r = stats.linregress(x, y)
    if len(x) < 3:
        return r.slope, np.nan, np.nan, np.nan
    tval = r.slope / r.stderr if r.stderr > 0 else np.inf * np.sign(r.slope)
    p_two = 2 * stats.t.sf(abs(tval), len(x) - 2)
    p_greater = stats.t.sf(tval, len(x) - 2)
    return r.slope, r.stderr, p_greater, p_two


# ---------------------------------------------------------------- Pearson correlations (Eq. 11)

def burst_matrix(trials, limit, t0=T0, t1=T1, dt=DT):
    """n(t) per trial and bin: the spike count of the burst whose first spike is in the bin."""
    nb = int(round((t1 - t0) / dt))
    out = np.zeros((len(trials), nb), dtype=np.int16)
    for i, t in enumerate(trials):
        on, n = bursts_of_trial(t, limit)
        keep = (on >= t0) & (on < t1)
        np.add.at(out[i], ((on[keep] - t0) / dt).astype(int), n[keep])
    return out


def mean_sq_pearson(x, max_lag_bins, t_end_bins, include_zero=True):
    """Mean over t < t_end_bins and lags 0..max_lag_bins of c(t, tau)^2, Eq. 11: the Pearson
    coefficient across trials between bin t and bin t + tau, set to 0 where the denominator
    vanishes (the numerator then vanishes too)."""
    x = x.astype(float)
    xc = x - x.mean(0)
    var = (xc ** 2).mean(0)
    tot, cnt = 0.0, 0
    for k in range(0 if include_zero else 1, max_lag_bins + 1):
        a, b = xc[:, :t_end_bins], xc[:, k:k + t_end_bins]
        num = (a * b).mean(0)
        den = np.sqrt(var[:t_end_bins] * var[k:k + t_end_bins])
        c = np.where(den > 0, num / np.where(den > 0, den, 1), 0.0)
        tot += (c ** 2).sum()
        cnt += len(c)
    return tot / cnt


# ---------------------------------------------------------------- jitter

def jitter_events_a(onsets_by_trial, t0=T0, t1=T1, dt=DT):
    """Reading (a): events are the peaks of the onset histogram (0.1 ms bins), each event's
    onsets those between the troughs (local minima) on either side. Returns the mean over
    events with at least two onsets of the SD of onset times (s), or nan."""
    allon = np.concatenate(onsets_by_trial) if onsets_by_trial else np.zeros(0)
    if len(allon) < 2:
        return np.nan
    nb = int(round((t1 - t0) / dt))
    h = np.bincount(((allon - t0) / dt).astype(int).clip(0, nb - 1), minlength=nb).astype(float)
    # Troughs: bins where h is not above either neighbour; events are the stretches between.
    trough = np.r_[True, (h[1:-1] <= h[:-2]) & (h[1:-1] <= h[2:]), True]
    seg = np.cumsum(trough)
    k = ((allon - t0) / dt).astype(int).clip(0, nb - 1)
    sds = [allon[seg[k] == g].std(ddof=1) for g in np.unique(seg[k]) if (seg[k] == g).sum() >= 2]
    return np.mean(sds) if sds else np.nan


def jitter_events_b(onsets_by_trial, limit):
    """Reading (b): pooled onsets sorted in time; an event is a run of onsets whose gaps are
    within the session's first-peak domain (the limiting ISI). Mean over events with at least
    two onsets of their SD (s), or nan."""
    allon = np.sort(np.concatenate(onsets_by_trial)) if onsets_by_trial else np.zeros(0)
    if len(allon) < 2 or limit <= 0:
        return np.nan
    starts = np.flatnonzero(np.r_[True, np.diff(allon) > limit])
    ends = np.r_[starts[1:], len(allon)]
    sds = [allon[a:b].std(ddof=1) for a, b in zip(starts, ends) if b - a >= 2]
    return np.mean(sds) if sds else np.nan


# ---------------------------------------------------------------- burst-triggered averages

PRE, POST = 0.025, 0.015     # s, -25 to +15 ms around burst onset (Methods, nBTA ANOVA)


def segments(stim, onsets, pre=PRE, post=POST, rate=STIM_RATE):
    """Stimulus segments (rows) from onset - pre to onset + post, at the stimulus rate."""
    i0 = np.round(onsets * rate).astype(int)
    off = np.arange(-int(round(pre * rate)), int(round(post * rate)))
    return stim[i0[:, None] + off[None, :]], off / rate


def two_way_anova(groups):
    """Two-way ANOVA, factors group and column (frequency bin), for a list of (n_obs, n_cols)
    arrays: each observation has one value per column, so the design is proportional and the
    sums of squares are exact. Returns p of the group main effect and of the interaction."""
    from scipy import stats
    allx = np.concatenate(groups)
    N, F = allx.shape
    G = len(groups)
    m = allx.mean()
    mf = allx.mean(0)
    ss_g = sum(len(g) * F * (g.mean() - m) ** 2 for g in groups)
    ss_f = N * ((mf - m) ** 2).sum()
    ss_cells = sum(len(g) * ((g.mean(0) - m) ** 2).sum() for g in groups)
    ss_int = ss_cells - ss_g - ss_f
    ss_err = sum(((g - g.mean(0)) ** 2).sum() for g in groups)
    df_g, df_int, df_err = G - 1, (G - 1) * (F - 1), N * F - G * F
    ms_err = ss_err / df_err
    p_g = stats.f.sf(ss_g / df_g / ms_err, df_g, df_err)
    p_int = stats.f.sf(ss_int / df_int / ms_err, df_int, df_err) if df_int > 0 else 1.0
    return p_g, p_int


def central_peak(bta, t, search=(-PRE, 0.0)):
    """Index of the central maximum of a BTA (its maximum in `search`, which contains the
    upstroke before the burst) and of the minima flanking it (the nearest local minima on each
    side, or the window's ends)."""
    w = np.flatnonzero((t >= search[0]) & (t <= search[1]))
    ip = w[np.argmax(bta[w])]
    left = ip
    while left > 0 and bta[left - 1] <= bta[left]:
        left -= 1
    right = ip
    while right < len(bta) - 1 and bta[right + 1] <= bta[right]:
        right += 1
    return ip, left, right


def fwhm(bta, ip, baseline):
    """Full width at half height of the peak at ip above `baseline`, in samples."""
    half = baseline + (bta[ip] - baseline) / 2
    a = ip
    while a > 0 and bta[a - 1] > half:
        a -= 1
    b = ip
    while b < len(bta) - 1 and bta[b + 1] > half:
        b += 1
    return b - a + 1


# ---------------------------------------------------------------- direct method (Strong et al., 1998)

def nsb_entropy(counts_list, K, n_beta=200):
    """NSB entropy estimate (bits; Nemenman, Shafee & Bialek 2002, Nemenman et al. 2004) of each
    histogram in `counts_list` (arrays of the non-zero counts), for K possible words. The
    posterior over the Dirichlet concentration beta under the prior uniform in the expected
    entropy xi(beta) is evaluated on a log grid of beta, and the posterior mean entropy is its
    weighted average."""
    from scipy.special import gammaln, digamma, polygamma
    betas = np.logspace(-6, 4, n_beta)
    dxi = K * polygamma(1, K * betas + 1) - polygamma(1, betas + 1)
    lw = np.log(np.gradient(betas)) + np.log(np.abs(dxi))
    out = np.empty(len(counts_list))
    for j, c in enumerate(counts_list):
        c = np.asarray(c, float)
        N = c.sum()
        kb = K * betas
        ll = (gammaln(kb) - gammaln(N + kb)
              + (gammaln(c[:, None] + betas[None, :]) - gammaln(betas)[None, :]).sum(0))
        s = digamma(N + kb + 1) - ((c[:, None] + betas[None, :]) * digamma(c[:, None] + betas[None, :] + 1)).sum(0) / (N + kb) \
            - (K - len(c)) * betas * digamma(betas + 1) / (N + kb)
        lp = ll + lw
        w = np.exp(lp - lp.max())
        out[j] = (w * s).sum() / w.sum() / np.log(2)
    return out


def direct_information(trials, word_bins, bin_s=4e-4, t0=T0, t1=T1):
    """Information rate (bits/s) of binary words of `word_bins` bins of `bin_s` over [t0, t1):
    total entropy of the words over all times and trials minus the mean over time of the
    entropy of the words at that time across trials, both NSB-corrected, divided by the word
    duration. Words start at every bin."""
    x = (binned(trials, t0, t1, bin_s) > 0).astype(np.int64)
    n_tr, nb = x.shape
    L = word_bins
    words = np.zeros((n_tr, nb - L + 1), dtype=np.int64)
    for j in range(L):
        words = words * 2 + x[:, j:nb - L + 1 + j]
    K = 2 ** L
    _, tot = np.unique(words, return_counts=True)
    h_tot = nsb_entropy([tot], K)[0]
    hists = {}
    for col in words.T:
        _, c = np.unique(col, return_counts=True)
        key = tuple(sorted(c))
        hists[key] = hists.get(key, 0) + 1
    keys = list(hists)
    h = nsb_entropy([np.array(k) for k in keys], K)
    h_noise = sum(hists[k] * hk for k, hk in zip(keys, h)) / words.shape[1]
    return (h_tot - h_noise) / (L * bin_s)
EOF
. $TMPDIR/dev/bin/activate && python -c "import ia1"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import ia1,pickle,time,numpy as np
S,sc=pickle.load(open('$TMPDIR/sess.pkl','rb'))
P=[s for s in S if s.protocol]
s=P[5]
# sanity of nsb: uniform sample
rng=np.random.default_rng(0); x=rng.integers(0,256,200); _,c=np.unique(x,return_counts=True)
print('nsb uniform K256 N200',ia1.nsb_entropy([c],256), 'true 8')
for L in [1,4,8]:
  t=time.time(); print(L, ia1.direct_information(s.trials,L), time.time()-t)
lim,_=ia1.burst_limit(s.trials,s.cutoff,'b','a','a')
for b in [1e-4,4e-4]:
  inf=ia1.information(ia1.burst_rates(s.trials,lim,b))
  print(b, {n:(round(v['i1'],2),round(v['rate'],1)) for n,v in inf.items()}, sum(v['rate'] for v in inf.values()))
"
```

```
nsb uniform K256 N200 [7.93990992] true 8
1 104.37097533520796 0.019747257232666016
4 125.99095762941832 0.060520172119140625
8 166.53137169976614 0.09011101722717285
0.0001 {1: (np.float64(1.97), np.float64(62.8)), 2: (np.float64(3.85), np.float64(22.7)), 3: (np.float64(4.76), np.float64(14.3)), 4: (np.float64(5.15), np.float64(12.2)), 5: (np.float64(5.43), np.float64(11.4)), 6: (np.float64(5.86), np.float64(8.2)), 7: (np.float64(6.1), np.float64(8.9)), 8: (np.float64(6.7), np.float64(6.6)), 9: (np.float64(7.46), np.float64(3.6)), 10: (np.float64(8.41), np.float64(2.9)), 11: (np.float64(8.43), np.float64(4.5)), 12: (np.float64(10.16), np.float64(0.6))} 158.68036810211015
0.0004 {1: (np.float64(1.2), np.float64(38.1)), 2: (np.float64(2.49), np.float64(14.7)), 3: (np.float64(3.33), np.float64(10.0)), 4: (np.float64(3.79), np.float64(9.0)), 5: (np.float64(4.14), np.float64(8.7)), 6: (np.float64(4.6), np.float64(6.5)), 7: (np.float64(4.96), np.float64(7.2)), 8: (np.float64(5.52), np.float64(5.5)), 9: (np.float64(6.19), np.float64(3.0)), 10: (np.float64(7.37), np.float64(2.5)), 11: (np.float64(7.89), np.float64(4.3)), 12: (np.float64(8.73), np.float64(0.5))} 109.82630839639661
```

**Agent**

The direct method with NSB runs in about 0.1 s per word length per session, so every claim fits the time limit. I'll write the notebook now.

**Agent calls Bash**

```bash
date -u; python3 - <<'EOF'
p='entries/crcns-ia-1-eyherabide-2008/ia1.py'; s=open(p).read()
old=s[s.index('def mean_sq_pearson'):s.index('# ---------------------------------------------------------------- jitter')]
new='''def sq_pearson_by_lag(x, max_lag_bins, t_end_bins):
    """Mean over t < t_end_bins of c(t, tau)^2 for each lag 0..max_lag_bins, Eq. 11: the
    Pearson coefficient across trials between bin t and bin t + tau, set to 0 where the
    denominator vanishes (the numerator then vanishes too)."""
    x = x.astype(float)
    xc = x - x.mean(0)
    var = (xc ** 2).mean(0)
    out = np.empty(max_lag_bins + 1)
    for k in range(max_lag_bins + 1):
        a, b = xc[:, :t_end_bins], xc[:, k:k + t_end_bins]
        num = (a * b).mean(0)
        den = np.sqrt(var[:t_end_bins] * var[k:k + t_end_bins])
        c = np.where(den > 0, num / np.where(den > 0, den, 1), 0.0)
        out[k] = (c ** 2).mean()
    return out


'''
s=s.replace(old,new); open(p,'w').write(s)
EOF
```

```
Wed Nov  4 18:29:55 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(text):\n    cells.append(nbf.v4.new_markdown_cell(text.strip()))\n\n\ndef code(text, tags=None):\n    c = nbf.v4.new_code_cell(text.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Eyherabide, Rokem, Herz & Samengo (2008) on CRCNS ia-1\n\nPaper: H. G. Eyherabide, A. Rokem, A. V. M. Herz and I. Samengo (2008), \"Burst firing is a neural\ncode in an insect auditory system\", Frontiers in Computational Neuroscience,\n[doi:10.3389/neuro.10.003.2008](https://doi.org/10.3389/neuro.10.003.2008). The claims file\n(`claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml`) was written from the version of record in\nPubMed Central (PMC2525941), with its Methods and the legends of Figures 1 to 10 and Table 1; the\npaper has no supplement and links no code.\n\nDataset: CRCNS data set ia-1, [doi:10.6080/K0BG2KWB](https://doi.org/10.6080/K0BG2KWB), read from\nthe public bucket `crcnsarchive` (`ia-1/crcns-ia1.zip`), streamed and opened in place.\n\nVersion: CRCNS data sets are not versioned, so the version is recorded as `unversioned` and the\nfile read is pinned by its MD5 sum in the data set's `checksums.md5`: `crcns-ia1.zip`\nf0740514fabc6995fe54b2a361b6c763 (the helper checks the object's ETag against it before reading;\nthe object was last modified 2026-02-11). This is the only published state of the data set, so it\nis the one pinned. Only `Data1` is used: the data descriptor names it as the data of this paper;\n`Data2` (2004) is unpublished and used other stimuli.\n\n| Claim | Tested here |\n|---|---|\n| data-sessions-and-trials | tested |\n| table1-sessions-per-protocol | tested |\n| firing-rate-uniform | tested |\n| threshold-population | blocked: the thresholds are not in the data set |\n| table1-bursting-sessions | tested |\n| table1-isolated-spikes | tested |\n| table1-burst-length | tested |\n| fig5-burst-probability-vs-stimulus | tested |\n| fig3-correlation-shape | tested (the data part; the model panels need the thresholds) |\n| method-correlation-error | tested |\n| model-matches-classification | blocked: the model needs the thresholds s_TH |\n| fig6-bursts-less-correlated | tested |\n| fig7ab-information-per-burst-increases | tested |\n| fig7cd-occurrence-decreases | tested |\n| fig7ef-jitter-independent-of-n | tested |\n| fig7gh-information-rate | tested |\n| direct-method-comparison | tested |\n| fig8-nbta-differ | tested |\n| fig8-latency-decreases | tested |\n| fig8e-sigma-minimum | tested |\n| sigma-n-below-sta-sigma | tested |\n| fig9-nbta-not-concatenated-1bta | tested (data only; the model sessions need the thresholds) |\n| fig9c-population-nbta | tested |\n| fig10-burst-n-vs-height | tested |\n| firing-rate-no-effect-on-limit | tested |\n| model-reproduces-coding-trends | blocked: depends on model-matches-classification |\n\nNo step draws random numbers, so no seed is needed.\n\"\"\")\n\ncode(r\"\"\"\nimport collections\nimport itertools\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport ia1\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nprint(\"data set\", ia1.CRCNS_ID, ia1.VERSION, \"doi\", ia1.DATASET_DOI, \"zip md5\", ia1.ZIP_MD5)\nz = ia1.open_zip()\nsessions = ia1.load_sessions(z)\ncells = ia1.load_singlecells(z)\nshapes = {name: ia1.load_stimulus_shape(z, name) for name in sorted({s.stimulus for s in sessions})}\ncell_of = {e: i for i, row in enumerate(cells) for e in row}\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nWhat was loaded, and the checks of the description against the values. The data descriptor\nsays: spike times in microseconds from the stimulus trigger; trials of the first 1000 ms of the\nstimulus, 98 to 533 per stimulus; 700 ms pauses; two interleaved stimuli per experiment;\n`cell.dat` gives the stimulus names and intensities (the maximal intensity, mean plus 3 SD);\nstimulus files at 20 kHz, 10 s long; `singlecells.txt` lists the experiments made on one cell.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    r = ia1.trial_rates(s.trials)\n    rows.append(dict(session=s.name, exp=s.exp, date=s.exp[:8], cell=cell_of.get(s.exp, -1),\n                     stimulus=s.stimulus, protocol=s.protocol, cutoff=s.cutoff, intensity=s.intensity,\n                     header_intensity=float(s.header[\"intensity (dB)\"]) if \"intensity (dB)\" in s.header else np.nan,\n                     desired_rate=float(s.header[\"desired firing rate (Hz)\"]) if \"desired firing rate (Hz)\" in s.header else np.nan,\n                     pause_ms=float(s.header[\"pause between stimuli (msec)\"]) if \"pause between stimuli (msec)\" in s.header else np.nan,\n                     header_stim=s.header.get(\"stimulus file\", \"\").split(\"/\")[-1].removesuffix(\".dat\"),\n                     offline=s.offline, n_trials=s.n_trials, rate=r.mean(), rate_sd=r.std(ddof=1),\n                     rate_full=ia1.trial_rates(s.trials, 0, 1).mean(), rate_sd_full=ia1.trial_rates(s.trials, 0, 1).std(ddof=1)))\nD = pd.DataFrame(rows)\nprint(\"Data1 experiments:\", D.exp.nunique(), \" sessions:\", len(D), \" offline-sorted sessions (no OEL header):\", D.offline.sum())\nprint(\"experiments not listed in singlecells.txt:\", sorted(set(D.exp) - set(cell_of)))\nprint(\"cells (rows of singlecells.txt, plus experiments not listed):\", len(cells) + len(set(D.exp) - set(cell_of)),\n      \" recording dates:\", D.date.nunique())\nprint(\"\\nSessions by stimulus file (cell.dat):\")\nprint(D.groupby(\"stimulus\").agg(sessions=(\"session\", \"size\"), protocol=(\"protocol\", \"first\")).to_string())\nhdr = D[D.header_stim != \"\"]\nprint(\"\\nHeader stimulus agrees with cell.dat in\", (hdr.header_stim.str.replace(\"gauss_\", \"\") == hdr.stimulus.str.replace(\"gauss_\", \"\")).sum(),\n      \"of\", len(hdr), \"sessions with a stimulus line in the header\")\nd = (D.header_intensity - D.intensity).dropna()\nprint(\"header intensity minus cell.dat intensity (dB): n =\", len(d), \" median |diff|\", round(d.abs().median(), 2),\n      \" max |diff|\", round(d.abs().max(), 2), \" sessions over 1 dB:\", list(D.session[(D.header_intensity - D.intensity).abs() > 1]))\nprint(\"desired firing rate in headers:\", D.desired_rate.value_counts(dropna=False).to_dict())\nprint(\"pause between stimuli (ms) in headers:\", D.pause_ms.value_counts(dropna=False).to_dict())\nallsp = np.concatenate([np.concatenate(s.trials) for s in sessions])\nprint(\"\\nspike times (s): min\", allsp.min(), \" max\", allsp.max(), \" fraction after 1 s (in the pause):\", round((allsp > 1).mean(), 4))\nprint(\"trials per session: min\", D.n_trials.min(), \" max\", D.n_trials.max())\nprint(\"rate over 200-1000 ms (Hz): min\", round(D.rate.min(), 1), \" max\", round(D.rate.max(), 1))\nunsorted = sum(int((np.diff(t) <= 0).any()) for s in sessions for t in s.trials)\nprint(\"trials with unsorted or repeated spike times:\", unsorted)\nisi = np.concatenate([np.diff(t) for s in sessions for t in s.trials])\nprint(\"shortest ISI (ms):\", round(isi.min() * 1e3, 2), \" 0.1 ms quantile of ISIs (ms):\", round(np.quantile(isi, 0.001) * 1e3, 2))\nfor name, sh in shapes.items():\n    print(f\"stimulus {name}: {len(sh)} samples in the first 1.05 s at 20 kHz, dB re its 10 s maximum, range {sh.min():.1f} to {sh.max():.1f}, SD over 0-1 s {sh[:20000].std():.2f} dB\")\n# Duplicate recordings: identical spike trains or identical first trials.\nseen = collections.defaultdict(list)\nfor s in sessions:\n    seen[np.concatenate(s.trials).round(6).tobytes()].append(s.name)\n    seen[(\"first\", s.trials[0].round(6).tobytes())].append(s.name)\nprint(\"sessions with identical spike times or identical first trials:\", [v for v in seen.values() if len(v) > 1])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe stimulus files are named for their SD and cutoff (`gauss_st6_co200` is SD 6 dB, cutoff 200\nHz). Their SDs over the first second can be checked against the names (6 dB files near 6 dB).\n\n**Clock check.** Spikes and stimuli share the trial's clock if the spike-triggered average of the\nstimulus (STA) shows the upstroke a few ms before the spike, which the paper describes (Figure 1:\n\"responses typically appear after stimulus upstrokes with an delay of 3.4 msec\"). The contrast is\nthe same STA computed from the stimulus shifted by 100 ms, which keeps every property of the\nstimulus and the spike train except their alignment.\n\"\"\")\n\ncode(r\"\"\"\nP = [s for s in sessions if s.protocol]          # sessions in the paper's seven protocols\n\n\ndef stim_db(s):\n    return shapes[s.stimulus] + s.intensity\n\n\ndef spikes_in(s, t0=ia1.T0, t1=ia1.T1):\n    return np.concatenate([t[(t >= t0) & (t < t1)] for t in s.trials])\n\n\nrows = []\nfor s in P:\n    st = stim_db(s)\n    sp = spikes_in(s)\n    seg, tt = ia1.segments(st, sp)\n    sta = seg.mean(0) - st[4000:20000].mean()\n    seg2, _ = ia1.segments(st, sp - 0.1)\n    sta2 = seg2.mean(0) - st[4000:20000].mean()\n    rows.append(dict(session=s.name, protocol=s.protocol, sta_peak=sta.max(), lat_ms=-tt[np.argmax(sta[tt <= 0])] * 1e3,\n                     shifted_peak=sta2.max()))\nC = pd.DataFrame(rows)\nprint(\"STA peak above the mean stimulus (dB): median\", round(C.sta_peak.median(), 2), \" range\", round(C.sta_peak.min(), 2), \"to\", round(C.sta_peak.max(), 2))\nprint(\"with the stimulus shifted by 100 ms: median\", round(C.shifted_peak.median(), 2), \" range\", round(C.shifted_peak.min(), 2), \"to\", round(C.shifted_peak.max(), 2))\nprint(\"sessions whose STA peak exceeds the shifted one:\", (C.sta_peak > C.shifted_peak).sum(), \"of\", len(C))\nprint(\"latency of the STA maximum (ms): median\", C.lat_ms.median(), \" range\", C.lat_ms.min(), \"to\", C.lat_ms.max())\nprint(\"sessions where the true STA peak is under 1 dB:\", list(C.session[C.sta_peak < 1]))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## Session selection and burst identification\n\nKept sessions (claim data-sessions-and-trials). The paper keeps sessions whose trial-to-trial SD\nof the firing rate is below 35 Hz and whose mean rate is about 100 Hz. Readings, from the\ncriterion: (a) the SD condition alone; (b) the SD condition and a target rate of 100 Hz where\nthe header records one. Per-trial rates over 200 to 1000 ms, and over the whole 1 s as a\nvariant. Only sessions of the paper's seven protocols (Table 1) can be kept; the data set's other\nstimuli (`gaussModality_co200`, `lmd_co200`, cutoffs 50 and 1600 Hz) are not in the paper's design\n(Methods: \"The other signal could be one of six different stimulation protocols\").\n\nBursts, by the Methods (Burst identification), under every combination of the readings of the\nopen details (claims file, opening comment): peak (a) first local maximum, (b) largest value in\n0 < tau < 5 ms; minimum (a) first significant local minimum after the peak, (b) lowest value up\nto 1.25 / cutoff; error bar N (a) the number of product terms, (b) the number of trials, and (c)\nsigma the SD over trials of each trial's C_s with N the number of trials (added here, see\n`ia1.py`).\n\"\"\")\n\ncode(r\"\"\"\ndef kept(reading=\"a\", window=\"200-1000\"):\n    col = \"rate_sd\" if window == \"200-1000\" else \"rate_sd_full\"\n    out = []\n    for s in P:\n        row = D.loc[D.session == s.name].iloc[0]\n        ok = row[col] < 35\n        if reading == \"b\" and not np.isnan(row.desired_rate):\n            ok = ok and row.desired_rate == 100\n        if ok:\n            out.append(s)\n    return out\n\n\nKEPT = kept(\"a\")\nCOMBOS = list(itertools.product(\"ab\", \"ab\", \"abc\"))\nMAIN = (\"b\", \"a\", \"a\")\nlimits = {c: {s.name: ia1.burst_limit(s.trials, s.cutoff, *c)[0] for s in P} for c in COMBOS}\nfor c in COMBOS:\n    lim = limits[c]\n    nb = sum(lim[s.name] > 0 for s in KEPT)\n    print(\"peak %s, minimum %s, N %s: bursting %3d of %d kept; median limiting ISI %s ms\" % (\n        *c, nb, len(KEPT), np.round(np.median([lim[s.name] for s in KEPT if lim[s.name] > 0]) * 1e3, 2) if nb else \"-\"))\nLIM = limits[MAIN]\nBURSTING = [s for s in KEPT if LIM[s.name] > 0]\nprint(\"\\nmain reading\", MAIN, \": kept\", len(KEPT), \" bursting\", len(BURSTING))\n\"\"\")\n\n# ---------------------------------------------------------------- claim 1\nmd(r\"\"\"\n## data-sessions-and-trials\n\n> Thirty-seven receptor cells were recorded from 23 animals, giving 132 sessions, of which 86 met\n> the firing-rate and stationarity conditions; each stimulus was repeated 98 to 503 times, 172 on\n> average.\n\nData1 does not record the animal. The recording date is shown as a stand-in (one animal per\nday is an assumption the descriptor does not make); cells are the rows of `singlecells.txt`.\n\"\"\")\n\ncode(r\"\"\"\ndef describe(sel, label):\n    names = {s.name for s in sel}\n    d = D[D.session.isin(names)]\n    return dict(population=label, cells=d.cell.nunique() + (d.cell == -1).sum() - (1 if (d.cell == -1).any() else 0),\n                dates=d.date.nunique(), sessions=len(d), min_trials=d.n_trials.min(), max_trials=d.n_trials.max(),\n                mean_trials=round(d.n_trials.mean(), 1), mean_rate_sd=round(d.rate_sd.mean(), 2),\n                mean_rate_sd_full=round(d.rate_sd_full.mean(), 2))\n\n\ntab = pd.DataFrame([describe(sessions, \"all Data1 sessions\"),\n                    describe([s for s in sessions if s.stimulus.replace(\"gauss_\", \"\").startswith(\"st\")], \"Gaussian AM stimuli (any cutoff)\"),\n                    describe(P, \"seven protocols\"),\n                    describe(kept(\"a\"), \"kept (a), 200-1000 ms\"), describe(kept(\"b\"), \"kept (b), 200-1000 ms\"),\n                    describe(kept(\"a\", \"full\"), \"kept (a), 0-1000 ms\"), describe(kept(\"b\", \"full\"), \"kept (b), 0-1000 ms\")])\nprint(tab.to_string(index=False))\nprint(\"\\nsessions in the seven protocols with rate SD >= 35 Hz (200-1000 ms):\",\n      list(D.session[D.protocol.notna() & (D.rate_sd >= 35)]))\nprint(\"SD of the trial rates over the seven-protocol sessions (Hz): quantiles 0, 0.25, 0.5, 0.75, 0.9, 1:\",\n      np.quantile(D.rate_sd[D.protocol.notna()], [0, .25, .5, .75, .9, 1]).round(1))\nexpected = dict(cells=(37, 3.7), sessions_recorded=(132, 13.2), kept=(86, 8.6), min_trials=(98, 9.8), max_trials=(503, 50.3),\n                mean_trials=(172, 17.2), mean_rate_sd=(6, 0.6))\nprint(\"\\nexpected (value, tolerance):\", expected)\n\"\"\", tags=[\"claim:data-sessions-and-trials\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\n# ---------------------------------------------------------------- claim 2\nmd(r\"\"\"\n## table1-sessions-per-protocol\n\n> The 86 kept sessions divide among the seven stimulus protocols as 43 (6 dB, 200 Hz), 6 (3 dB,\n> 200 Hz), 7 (12 dB, 200 Hz), 7 (6 dB, 25 Hz), 8 (6 dB, 100 Hz), 7 (6 dB, 400 Hz) and 8 (6 dB, 800 Hz).\n\"\"\")\n\ncode(r\"\"\"\nT1_SESS = [43, 6, 7, 7, 8, 7, 8]\nrows = []\nfor label, sel in [(\"kept (a) 200-1000\", kept(\"a\")), (\"kept (b) 200-1000\", kept(\"b\")),\n                   (\"kept (a) 0-1000\", kept(\"a\", \"full\")), (\"kept (b) 0-1000\", kept(\"b\", \"full\")), (\"seven protocols\", P)]:\n    cnt = collections.Counter(s.protocol for s in sel)\n    vals = [cnt[p] for p in range(1, 8)]\n    rows.append(dict(population=label, **{f\"p{p}\": v for p, v in zip(range(1, 8), vals)},\n                     within_10pct=sum(abs(v - e) <= 0.1 * e for v, e in zip(vals, T1_SESS))))\nrows.append(dict(population=\"paper\", **{f\"p{p}\": v for p, v in zip(range(1, 8), T1_SESS)}, within_10pct=7))\nprint(pd.DataFrame(rows).to_string(index=False))\nexps = collections.defaultdict(list)\nfor s in P:\n    exps[s.exp].append(s.protocol)\nprint(\"\\nexperiments with both stimuli in the protocols, by pair:\",\n      dict(collections.Counter(tuple(sorted(v)) for v in exps.values() if len(v) == 2)))\n\"\"\", tags=[\"claim:table1-sessions-per-protocol\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- claim 3\nmd(r\"\"\"\n## firing-rate-uniform\n\n> The kept sessions had a mean firing rate of 113 Hz (SD 16 Hz) that did not differ significantly\n> across stimulus conditions (one-way ANOVA, p = 0.58).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor label, sel, col in [(\"kept (a), 200-1000 ms\", kept(\"a\"), \"rate\"), (\"kept (a), 0-1000 ms\", kept(\"a\", \"full\"), \"rate_full\"),\n                        (\"all seven-protocol sessions, 200-1000 ms\", P, \"rate\"), (\"all seven-protocol sessions, 0-1000 ms\", P, \"rate_full\"),\n                        (\"kept (b), 200-1000 ms\", kept(\"b\"), \"rate\")]:\n    d = D[D.session.isin({s.name for s in sel})]\n    groups = [g[col].values for _, g in d.groupby(\"protocol\")]\n    F, p = stats.f_oneway(*groups)\n    rows.append(dict(population=label, n=len(d), mean_rate=round(d[col].mean(), 1), sd_rate=round(d[col].std(ddof=1), 1),\n                     F=round(F, 2), p=round(p, 3)))\nprint(pd.DataFrame(rows).to_string(index=False))\nd = D[D.session.isin({s.name for s in KEPT})]\nprint(\"\\nmean rate by protocol (kept (a), 200-1000 ms):\", d.groupby(\"protocol\").rate.mean().round(1).to_dict())\n\"\"\", tags=[\"claim:firing-rate-uniform\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- claim 4\nmd(r\"\"\"\n## threshold-population (blocked)\n\n> The mean threshold of the cells at their best frequency was 58 dB (SD 14 dB).\n\nData1 holds spike times, `cell.dat` (stimulus names and the intensities they were played at) and\nthe stimuli. It holds no threshold, best-frequency or tuning (f-I) measurement: the listing below\nshows every kind of file in Data1. Blocked, `data_missing`.\n\"\"\")\n\ncode(r\"\"\"\nkinds = collections.Counter()\nfor n in z.namelist():\n    if n.startswith(ia1.ROOT) and not n.endswith(\"/\"):\n        base = n.split(\"/\")[-1]\n        kinds[base.split(\"_\")[-1] if \"_\" in base and n.count(\"/\") > 3 and \"stimuli\" not in n else (\"stimuli/\" + base if \"stimuli\" in n else base)] += 1\nprint(dict(kinds))\nprint(\"cell.dat keys:\", sorted({line.split(\":\")[0].strip() for n in z.namelist() if n.endswith(\"cell.dat\")\n                               for line in z.read(n).decode(\"latin1\").splitlines() if \":\" in line}))\n\"\"\", tags=[\"claim:threshold-population\"])\n\n# ---------------------------------------------------------------- claim 5\nmd(r\"\"\"\n## table1-bursting-sessions\n\n> The number of sessions with bursts of n > 1 depends on the stimulus, from none for 3 dB and for\n> 800 Hz to all 7 for 12 dB and 7 of 8 for 100 Hz; 40 of 43 reference sessions, 6 of 7 at 25 Hz\n> and 3 of 7 at 400 Hz.\n\nCounted over the kept sessions, under every combination of the burst-identification readings. The\nfraction of sessions is shown beside the counts, since the counts depend on how many sessions are\nkept.\n\"\"\")\n\ncode(r\"\"\"\nT1_BURST = [40, 0, 7, 6, 7, 3, 0]\ntol = [max(0.1 * e, 0) for e in T1_BURST]\n\n\ndef n_gt1_sessions(sel, lim):\n    cnt = collections.Counter()\n    for s in sel:\n        if lim[s.name] > 0 and (ia1.burst_counts(s.trials, lim[s.name])[1:] > 0).any():\n            cnt[s.protocol] += 1\n    return [cnt[p] for p in range(1, 8)]\n\n\nrows = []\nfor kr in [\"a\", \"b\"]:\n    sel = kept(kr)\n    tot = collections.Counter(s.protocol for s in sel)\n    for c in COMBOS:\n        v = n_gt1_sessions(sel, limits[c])\n        rows.append(dict(kept=kr, readings=\"\".join(c), **{f\"p{p}\": f\"{x}/{tot[p]}\" for p, x in zip(range(1, 8), v)},\n                         within=sum(abs(x - e) <= t for x, e, t in zip(v, T1_BURST, tol))))\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"paper:\", [f\"{a}/{b}\" for a, b in zip(T1_BURST, T1_SESS)])\n\"\"\", tags=[\"claim:table1-bursting-sessions\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- claim 6, 7\nmd(r\"\"\"\n## table1-isolated-spikes\n\n> The percentage of isolated spikes among all bursts of the bursting sessions depends on the\n> stimulus (74, 100, 62, 60, 55, 96 and 100% for protocols 1 to 7), and in every protocol isolated\n> spikes are the most probable burst.\n\"\"\")\n\ncode(r\"\"\"\nT1_ISO = [74, 100, 62, 60, 55, 96, 100]\n\n\ndef protocol_counts(sel, lim):\n    # Pooled n counts per protocol over the bursting sessions (all sessions where a protocol has none).\n    out = {}\n    for p in range(1, 8):\n        ses = [s for s in sel if s.protocol == p]\n        bur = [s for s in ses if lim[s.name] > 0]\n        use = bur if bur else ses\n        tot = np.zeros(40)\n        per = []\n        for s in use:\n            c = ia1.burst_counts(s.trials, lim[s.name])\n            tot[:len(c)] += c\n            per.append(c[0] / c.sum())\n        out[p] = (np.trim_zeros(tot, \"b\"), per, len(bur))\n    return out\n\n\nrows = []\nPC = {}\nfor c in COMBOS:\n    pc = protocol_counts(KEPT, limits[c])\n    PC[c] = pc\n    iso = [100 * pc[p][0][0] / pc[p][0].sum() for p in range(1, 8)]\n    iso_avg = [100 * np.mean(pc[p][1]) for p in range(1, 8)]\n    most = [int(np.argmax(pc[p][0]) + 1) for p in range(1, 8)]\n    rows.append(dict(readings=\"\".join(c), **{f\"p{p}\": round(v, 1) for p, v in zip(range(1, 8), iso)},\n                     within=sum(abs(v - e) <= 0.1 * e for v, e in zip(iso, T1_ISO)), most_probable_n=most,\n                     session_average=[round(v, 1) for v in iso_avg]))\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"paper:\", T1_ISO)\n\"\"\", tags=[\"claim:table1-isolated-spikes\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## table1-burst-length\n\n> The highest n and the average n depend on the stimulus; the longest bursts (up to 15 spikes,\n> average 2.10 with SD 3.67) occur at 25 Hz, and no bursts occur at 3 dB or at 800 Hz.\n\"\"\")\n\ncode(r\"\"\"\nEXP_HI = [9, 1, 8, 15, 9, 3, 1]\nEXP_AV = [1.3, 1, 1.5, 2.1, 1.7, 1.04, 1]\nEXP_SD = {1: 1.3, 3: 1.6, 4: 3.67, 5: 1.8, 6: 0.42}\nrows = []\nfor c in COMBOS:\n    pc = PC[c]\n    hi = [len(pc[p][0]) for p in range(1, 8)]\n    av = [ia1.average_n(pc[p][0])[0] for p in range(1, 8)]\n    sd = [ia1.average_n(pc[p][0])[1] for p in range(1, 8)]\n    ok = (sum(abs(h - e) <= 0.1 * e for h, e in zip(hi, EXP_HI)) + sum(abs(a - e) <= 0.1 * e for a, e in zip(av, EXP_AV))\n          + sum(abs(sd[p - 1] - e) <= 0.1 * e for p, e in EXP_SD.items()))\n    rows.append(dict(readings=\"\".join(c), highest_n=hi, average_n=[round(a, 2) for a in av], sd_n=[round(x, 2) for x in sd], within_of_19=ok))\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"paper: highest\", EXP_HI, \" average\", EXP_AV, \" SD\", EXP_SD)\n\"\"\", tags=[\"claim:table1-burst-length\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- fig5\nmd(r\"\"\"\n## fig5-burst-probability-vs-stimulus\n\n> The probability of generating isolated spikes is lowest, and high-n bursts most frequent, for\n> large amplitude fluctuations (12 dB) and cutoff frequencies around 100 Hz.\n\"\"\")\n\ncode(r\"\"\"\ndef pn_table(sel, lim, bursting_only):\n    rows = []\n    for s in sel:\n        if bursting_only and lim[s.name] <= 0:\n            continue\n        c = ia1.burst_counts(s.trials, lim[s.name]).astype(float)\n        c = np.r_[c, np.zeros(3)][:3] / c.sum()\n        rows.append(dict(protocol=s.protocol, P1=c[0], P2=c[1], P3=c[2]))\n    return pd.DataFrame(rows).groupby(\"protocol\").agg([\"mean\", \"std\", \"size\"])\n\n\nfor c in [MAIN, (\"b\", \"b\", \"a\"), (\"b\", \"a\", \"c\"), (\"a\", \"a\", \"a\")]:\n    for reading, bo in [(\"(a) all kept\", False), (\"(b) bursting only\", True)]:\n        t = pn_table(KEPT, limits[c], bo)\n        means = t.xs(\"mean\", axis=1, level=1)\n        cut = {25: 4, 100: 5, 200: 1, 400: 6, 800: 7}\n        sdp = {3: 2, 6: 1, 12: 3}\n        p1c = {k: means.P1.get(v, np.nan) for k, v in cut.items()}\n        p1s = {k: means.P1.get(v, np.nan) for k, v in sdp.items()}\n        print(f\"readings {''.join(c)}, sessions {reading}\")\n        print(\"  P(n=1) by cutoff:\", {k: round(v, 3) for k, v in p1c.items()}, \" lowest at\", min(p1c, key=p1c.get), \"Hz\")\n        print(\"  P(n=1) by SD:\", {k: round(v, 3) for k, v in p1s.items()}, \" lowest at\", min(p1s, key=p1s.get), \"dB\")\n        for col in [\"P2\", \"P3\"]:\n            print(f\"  {col} by cutoff:\", {k: round(means[col].get(v, np.nan), 3) for k, v in cut.items()},\n                  \" by SD:\", {k: round(means[col].get(v, np.nan), 3) for k, v in sdp.items()})\nt = pn_table(KEPT, LIM, False)\nprint(\"\\nmain reading, all kept: mean, SD and number of sessions per protocol\")\nprint(t.round(3).to_string())\n\"\"\", tags=[\"claim:fig5-burst-probability-vs-stimulus\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- fig3\nmd(r\"\"\"\n## fig3-correlation-shape\n\n> For a cell tested with all stimuli, larger stimulus SD gives correlation functions with sharper\n> peaks, and faster stimuli lead from multi-modal (25 Hz) to single-peaked (100, 200 Hz) to\n> shallower and broader correlation functions (400, 800 Hz).\n\n`singlecells.txt` lists one cell recorded in seven experiments, 03-04-23-ad to -aj, which together\nhold all seven protocols (six reference sessions, one of each other protocol): this is taken as the\ncell of Figure 3. C_s is normalised by the squared mean rate so that sessions compare. \"Sharper\"\nis read as (a) a higher first peak over the baseline (the mean of C_s/rbar^2 over 20 to 40 ms) and\n(b) a narrower first peak (full width at half height above that baseline). Peaks are counted on\nC_s/rbar^2 smoothed with a 1 ms running mean (a standard choice that keeps the ms-scale shape), as\nlocal maxima within 0 < tau <= 1.25 / cutoff that rise above the neighbouring minima by more than a\nprominence threshold; the threshold is not in the paper, so 0.05, 0.1 and 0.2 are shown.\n\"\"\")\n\ncode(r\"\"\"\nfrom scipy.signal import find_peaks\n\nfig3_cell = next(row for row in cells if \"03-04-23-ad\" in row)\nF3 = [s for s in P if s.exp in fig3_cell]\nrows = []\nfig, axes = plt.subplots(1, 2, figsize=(12, 4))\nfor s in F3:\n    tau, c, sd, count, ntr, sdt = ia1.correlation(s.trials, 0.06)\n    rb = ia1.binned(s.trials).astype(bool).mean() / ia1.DT\n    cn = c / rb ** 2\n    base = cn[(tau >= 0.02) & (tau <= 0.04)].mean()\n    sm = np.convolve(cn, np.ones(10) / 10, mode=\"same\")\n    sm[:6] = cn[:6]\n    lim_i = int(1.25 / s.cutoff / ia1.DT)\n    ip = 1 + np.argmax(cn[1:51])\n    height = cn[ip] - base\n    width = ia1.fwhm(cn, ip, base) * ia1.DT * 1e3\n    npk = {}\n    for prom in [0.05, 0.1, 0.2]:\n        pk, _ = find_peaks(sm[1:lim_i + 1], prominence=prom)\n        npk[prom] = len(pk)\n    rows.append(dict(session=s.name, sd=s.sd_cut[0], cutoff=s.cutoff, bursting=LIM[s.name] > 0,\n                     limit_ms=round(LIM[s.name] * 1e3, 1), peak_ms=round(tau[ip] * 1e3, 1), peak_height=round(height, 2),\n                     peak_fwhm_ms=round(width, 1), **{f\"peaks_prom{k}\": v for k, v in npk.items()}))\n    ax = axes[0] if s.sd_cut[1] == 200 else axes[1]\n    ax.plot(tau[1:] * 1e3, cn[1:], lw=0.8, label=f\"{s.sd_cut[0]} dB, {s.cutoff} Hz ({s.exp[-2:]})\")\nF3T = pd.DataFrame(rows)\nprint(F3T.to_string(index=False))\nfor ax, t in zip(axes, [\"cutoff 200 Hz\", \"SD 6 dB\"]):\n    ax.set(xlabel=\"tau (ms)\", ylabel=\"C_s / rbar^2\", title=t, ylim=(-1.5, 4))\n    ax.legend(fontsize=7)\nprint(\"values of C_s/rbar^2 above the axes (4):\", int(sum((r > 4).sum() for r in [0])))\nplt.show()\nref = F3T[(F3T.sd == 6) & (F3T.cutoff == 200)]\nprint(\"reference sessions: peak height range\", ref.peak_height.min(), \"to\", ref.peak_height.max(), \"; FWHM range\", ref.peak_fwhm_ms.min(), \"to\", ref.peak_fwhm_ms.max(), \"ms\")\n\"\"\", tags=[\"claim:fig3-correlation-shape\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- method-correlation-error\nmd(r\"\"\"\n## method-correlation-error\n\n> The temporal average of the estimated error of the correlation function was on average 3.4% (SD\n> 1.5%) of the span of C_s.\n\nDelta = sigma / sqrt(N) at each tau, averaged over tau, over max minus min of C_s, averaged over\nkept sessions. Readings: sigma and N (a), (b) and (c); tau range (a) 0 to 1.25 / cutoff, (b) the\nwhole range up to 800 ms. Whether tau = 0, where C_s holds the self term (rbar / dt, two orders of\nmagnitude above the rest), enters the span is not stated: both are shown.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in KEPT:\n    tau, c, sd, count, ntr, sdt = ia1.correlation(s.trials, 0.7999)\n    L = int(round(1.25 / s.cutoff / ia1.DT))\n    for nm in \"abc\":\n        err = ia1.correlation_error(sd, count, ntr, sdt, nm)\n        for rng_name, sl in [(\"(a) 0 to 1.25/cutoff\", slice(0, L + 1)), (\"(b) 0 to 800 ms\", slice(0, None))]:\n            for z0 in [True, False]:\n                ss = sl if z0 else slice(1, sl.stop)\n                rows.append(dict(session=s.name, N=nm, tau_range=rng_name, tau0=z0,\n                                 pct=100 * err[ss].mean() / (c[ss].max() - c[ss].min())))\nE = pd.DataFrame(rows)\nprint(E.groupby([\"N\", \"tau_range\", \"tau0\"]).pct.agg([\"mean\", \"std\", \"size\"]).round(2).to_string())\n\"\"\", tags=[\"claim:method-correlation-error\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- model-matches-classification\nmd(r\"\"\"\n## model-matches-classification (blocked)\n\n> A threshold-linear Poisson model with refractoriness and no free parameters classifies sessions\n> as bursting or not in agreement with the real data in 86% of sessions, and where both are\n> bursting their limiting ISIs differ by less than 1 ms in 81% of cases.\n\nThe model thresholds the stimulus at the cell's measured threshold s_TH before filtering (Eq. 2),\nand the criterion says the claim is not testable as the paper ran it if the data set does not hold\ns_TH. Data1 holds no threshold (see threshold-population). Blocked, `data_missing`; the dependent\nmodel-reproduces-coding-trends is blocked for the same reason.\n\"\"\")\n\n# ---------------------------------------------------------------- fig6\nmd(r\"\"\"\n## fig6-bursts-less-correlated\n\n> Representing the spike train as n-bursts reduces correlations between time bins; the mean\n> squared Pearson coefficient over t from 200 to 990 ms and tau from 0 to 10 ms is 2.89 times\n> larger (SD 1.49) for spikes than for bursts, on average over the bursting sessions.\n\nEq. 11 across trials at each (t, tau). Bin width (a) 0.1 ms, (b) 0.4 ms; tau = 0 included or not.\nThe spike variable is 1 when the bin holds a spike. Bursting sessions under the main burst\nreading; detail (4) reading (b) (bursting sessions that have bursts of n > 1) is shown too.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in BURSTING:\n    for bw in [1e-4, 4e-4]:\n        xs = (ia1.binned(s.trials, dt=bw) > 0).astype(np.int8)\n        xb = ia1.burst_matrix(s.trials, LIM[s.name], dt=bw)\n        nl, te = int(round(0.01 / bw)), int(round(0.79 / bw))\n        cs, cb = ia1.sq_pearson_by_lag(xs, nl, te), ia1.sq_pearson_by_lag(xb, nl, te)\n        has_n2 = (xb > 1).any()\n        rows.append(dict(session=s.name, bin_ms=bw * 1e3, n_gt1=has_n2, with_tau0=cs.mean() / cb.mean(),\n                         without_tau0=cs[1:].mean() / cb[1:].mean()))\nR6 = pd.DataFrame(rows)\nfor (bw, n2), g in R6.groupby([\"bin_ms\", \"n_gt1\"]):\n    pass\nsumm = []\nfor bw in [0.1, 0.4]:\n    for lab, g in [(\"(a) all bursting\", R6[R6.bin_ms == bw]), (\"(b) with n > 1\", R6[(R6.bin_ms == bw) & R6.n_gt1])]:\n        for col in [\"with_tau0\", \"without_tau0\"]:\n            summ.append(dict(bin_ms=bw, sessions=lab, tau0=col, n=len(g), mean_ratio=round(g[col].mean(), 2),\n                             sd_ratio=round(g[col].std(ddof=1), 2), frac_above_1=round((g[col] > 1).mean(), 3),\n                             min=round(g[col].min(), 2), max=round(g[col].max(), 2)))\nprint(pd.DataFrame(summ).to_string(index=False))\n\"\"\", tags=[\"claim:fig6-bursts-less-correlated\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- fig7\nmd(r\"\"\"\n## Information per burst (Figure 7): per-session measures\n\nFor every kept session, under the main burst reading, with the bin widths (a) 0.1 ms and (b) 0.4\nms: rbar_n, I_n(1) in bits per event (reading i; reading ii is T = 0.8 s times it), I'_n in bits/s,\nand the jitter of each n (readings (a) and (b) of the events). Fits are over the n values present.\n\"\"\")\n\ncode(r\"\"\"\nT = ia1.T1 - ia1.T0\ninfo = {}\nfor s in KEPT:\n    for bw in [1e-4, 4e-4]:\n        info[(s.name, bw)] = ia1.information(ia1.burst_rates(s.trials, LIM[s.name], bw))\n\n\ndef fit_rows(sel, bw):\n    rows = []\n    for s in sel:\n        inf = info[(s.name, bw)]\n        ns = np.array(sorted(inf))\n        i1 = np.array([inf[n][\"i1\"] for n in ns])\n        rbar = np.array([inf[n][\"rbar\"] for n in ns])\n        rate = np.array([inf[n][\"rate\"] for n in ns])\n        occ = rbar / rbar.sum()\n        row = dict(session=s.name, protocol=s.protocol, n_max=ns.max(), n_values=len(ns))\n        for name, y in [(\"i1\", i1), (\"i1_ii\", i1 * T), (\"occ_log2\", np.log2(occ)), (\"occ_ln\", np.log(occ)),\n                        (\"occ_log10\", np.log10(occ)), (\"rate\", rate)]:\n            sl, se, pg, p2 = ia1.line_fit(ns, y)\n            row.update({f\"{name}_slope\": sl, f\"{name}_se\": se, f\"{name}_pg\": pg, f\"{name}_p2\": p2})\n        row[\"total_rate\"] = rate.sum()\n        row[\"frac_gt1\"] = rate[ns > 1].sum() / rate.sum()\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\nF7 = {bw: fit_rows(BURSTING, bw) for bw in [1e-4, 4e-4]}\nprint(\"bursting sessions:\", len(BURSTING), \"; with at least 3 n values (a slope with an error):\",\n      int((F7[1e-4].n_values >= 3).sum()), \"; with 2:\", int((F7[1e-4].n_values == 2).sum()), \"; with 1:\", int((F7[1e-4].n_values == 1).sum()))\n\"\"\")\n\nmd(r\"\"\"\n## fig7ab-information-per-burst-increases\n\n> The information carried by each n-burst increases with n; every bursting session has a\n> significantly positive slope of I_n(1) against n, with an average slope of 1.5 bits (SD 0.7\n> bits) over 59 bursting cells.\n\nSignificance (a) slope more than one standard error above zero, (b) one-sided t-test p < 0.05.\nSessions with fewer than three n values have no error for the slope and count as not significant.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor bw in [1e-4, 4e-4]:\n    f = F7[bw]\n    for norm, col in [(\"(i) bits per event\", \"i1\"), (\"(ii) Eq. 10 as printed\", \"i1_ii\")]:\n        for subset, g in [(\"(a) all bursting\", f), (\"(b) n_max > 1\", f[f.n_max > 1])]:\n            sig_a = (g[f\"{col}_slope\"] - g[f\"{col}_se\"] > 0)\n            sig_b = (g[f\"{col}_pg\"] < 0.05)\n            rows.append(dict(bin_ms=bw * 1e3, I1=norm, sessions=subset, n=len(g), mean_slope=round(g[f\"{col}_slope\"].mean(), 2),\n                             sd_slope=round(g[f\"{col}_slope\"].std(ddof=1), 2), positive=int((g[f\"{col}_slope\"] > 0).sum()),\n                             sig_a=int(sig_a.sum()), sig_b=int(sig_b.sum())))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"claim:fig7ab-information-per-burst-increases\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig7cd-occurrence-decreases\n\n> High-n bursts are rare; in every session the frequency of occurrence decreases significantly with\n> n, with an average slope of -2.6 (SD 0.7).\n\nSlope of the logarithm of rbar_n / sum rbar_n on n; logarithm (a) base 2, (b) natural, (c) base\n10. Significance as in fig7ab (negative here). The occurrence does not depend on the bin width.\n\"\"\")\n\ncode(r\"\"\"\nf = F7[1e-4]\nrows = []\nfor col in [\"occ_log2\", \"occ_ln\", \"occ_log10\"]:\n    for subset, g in [(\"(a) all bursting\", f), (\"(b) n_max > 1\", f[f.n_max > 1])]:\n        rows.append(dict(log=col, sessions=subset, n=len(g), mean_slope=round(g[f\"{col}_slope\"].mean(), 2),\n                         sd_slope=round(g[f\"{col}_slope\"].std(ddof=1), 2), negative=int((g[f\"{col}_slope\"] < 0).sum()),\n                         sig_a=int((g[f\"{col}_slope\"] + g[f\"{col}_se\"] < 0).sum()), sig_b=int(((1 - g[f\"{col}_pg\"]) < 0.05).sum())))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"claim:fig7cd-occurrence-decreases\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig7ef-jitter-independent-of-n\n\n> The jitter of the first spike of a burst is roughly independent of n in 80% of the bursting\n> sessions, and the mean slope of jitter against n is -0.03 ms (SD 0.2 ms).\n\nJitter per n is the mean over events of the SD of the onset times. Events (a) peaks of the onset\nhistogram in 0.1 ms bins, between the troughs on either side; (b) runs of pooled onsets whose\ngaps are within the session's limiting ISI. Slopes over the n values with a jitter (events with at\nleast two onsets); \"not significant\" is (a) |slope| below one standard error, (b) two-sided p >=\n0.05; sessions with fewer than three such n values have no test and are counted apart.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in BURSTING:\n    tr, on, n = ia1.bursts(s.trials, LIM[s.name])\n    row = dict(session=s.name)\n    for ev in \"ab\":\n        ns, js = [], []\n        for m in np.unique(n):\n            obt = [on[(n == m) & (tr == i)] for i in range(s.n_trials)]\n            j = ia1.jitter_events_a(obt) if ev == \"a\" else ia1.jitter_events_b(obt, LIM[s.name])\n            if np.isfinite(j):\n                ns.append(m)\n                js.append(j * 1e3)\n        sl, se, pg, p2 = ia1.line_fit(ns, js)\n        row.update({f\"{ev}_slope\": sl, f\"{ev}_se\": se, f\"{ev}_p2\": p2, f\"{ev}_nvals\": len(ns),\n                    f\"{ev}_j1\": js[0] if ns and ns[0] == 1 else np.nan})\n    rows.append(row)\nJ = pd.DataFrame(rows)\nsumm = []\nfor ev in \"ab\":\n    g = J[J[f\"{ev}_nvals\"] >= 3]\n    summ.append(dict(events=ev, sessions_with_test=len(g), no_test=int((J[f\"{ev}_nvals\"] < 3).sum()),\n                     mean_slope_ms=round(J[f\"{ev}_slope\"].mean(), 3), sd_slope_ms=round(J[f\"{ev}_slope\"].std(ddof=1), 3),\n                     pct_not_sig_a=round(100 * (g[f\"{ev}_slope\"].abs() < g[f\"{ev}_se\"]).mean(), 1),\n                     pct_not_sig_b=round(100 * (g[f\"{ev}_p2\"] >= 0.05).mean(), 1),\n                     median_jitter_n1_ms=round(J[f\"{ev}_j1\"].median(), 3)))\nprint(pd.DataFrame(summ).to_string(index=False))\n\"\"\", tags=[\"claim:fig7ef-jitter-independent-of-n\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig7gh-information-rate\n\n> The information rate of n-bursts decreases with n (average slope -11 bits/s, SD 16 bits/s), yet\n> bursts with n > 1 together carry on average 47% of the total information over the bursting cells.\n\nI'_n = rbar_n I_n(1) (bits/s), the same under readings (i) and (ii) of I_n(1).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor bw in [1e-4, 4e-4]:\n    f = F7[bw]\n    for subset, g in [(\"(a) all bursting\", f), (\"(b) n_max > 1\", f[f.n_max > 1])]:\n        rows.append(dict(bin_ms=bw * 1e3, sessions=subset, n=len(g), mean_slope=round(g.rate_slope.mean(), 1),\n                         sd_slope=round(g.rate_slope.std(ddof=1), 1), negative=int((g.rate_slope < 0).sum()),\n                         mean_frac_gt1_pct=round(100 * g.frac_gt1.mean(), 1), sd_frac_pct=round(100 * g.frac_gt1.std(ddof=1), 1),\n                         mean_total_bits_s=round(g.total_rate.mean(), 1)))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"claim:fig7gh-information-rate\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- direct method\nmd(r\"\"\"\n## direct-method-comparison\n\n> Information rates from the burst code are highly correlated with those of the direct method (R =\n> 0.95), averaging 191 against 222 bits/s, the direct method being higher in all sessions but one\n> by 31 bits/s on average, so the burst code keeps about 85% of the information.\n\nDirect method on binary words of 0.4 ms bins, words starting at every bin over 200 to 1000 ms,\nentropies NSB-corrected (`ia1.nsb_entropy`). Readings (a) the rate at 8 bins (3.2 ms), (b) a\nlinear extrapolation in 1 / word length over 1 to 8 bins. The burst-code rate is I' of\nfig7gh (non-bursting sessions as all 1-bursts), with bins (a) 0.1 ms and (b) 0.4 ms. Sessions (a)\nall kept, (b) bursting.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in KEPT:\n    rates = [ia1.direct_information(s.trials, L) for L in range(1, 9)]\n    sl, ic, *_ = stats.linregress(1 / np.arange(1, 9), rates)\n    row = dict(session=s.name, bursting=LIM[s.name] > 0, direct_8=rates[-1], direct_extrap=ic)\n    for bw in [1e-4, 4e-4]:\n        row[f\"burst_{bw * 1e3:.1f}\"] = sum(v[\"rate\"] for v in info[(s.name, bw)].values())\n    rows.append(row)\nDM = pd.DataFrame(rows)\nsumm = []\nfor dcol in [\"direct_8\", \"direct_extrap\"]:\n    for bcol in [\"burst_0.1\", \"burst_0.4\"]:\n        for lab, g in [(\"(a) kept\", DM), (\"(b) bursting\", DM[DM.bursting])]:\n            diff = g[dcol] - g[bcol]\n            summ.append(dict(direct=dcol, burst=bcol, sessions=lab, n=len(g), R=round(np.corrcoef(g[dcol], g[bcol])[0, 1], 3),\n                             mean_direct=round(g[dcol].mean(), 1), sd_direct=round(g[dcol].std(ddof=1), 1),\n                             mean_burst=round(g[bcol].mean(), 1), sd_burst=round(g[bcol].std(ddof=1), 1),\n                             mean_diff=round(diff.mean(), 1), sd_diff=round(diff.std(ddof=1), 1),\n                             direct_higher=f\"{int((diff > 0).sum())}/{len(g)}\",\n                             lost_pct=round(100 * (1 - g[bcol].mean() / g[dcol].mean()), 1)))\nprint(pd.DataFrame(summ).to_string(index=False))\n\"\"\", tags=[\"claim:direct-method-comparison\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- nBTA\nmd(r\"\"\"\n## Burst-triggered averages: per-session measures\n\nFor each bursting session (main reading), the stimulus in dB (stimulus file shifted to the\nintensity in `cell.dat`, as `stimtodB.m` does) around every burst onset in 200 to 1000 ms, from\n-25 to +15 ms at 20 kHz (Methods, Estimation of burst-triggered averages). The central maximum of\nan nBTA is its maximum between -25 and 0 ms; tau_n is its distance to the onset (Eq. 13 and the\nsentence after it).\n\"\"\")\n\ncode(r\"\"\"\ndef p_two_sided_ttests(a, b):\n    return stats.ttest_ind(a, b, axis=0).pvalue\n\n\nBTA = {}\nfor s in BURSTING:\n    st = stim_db(s)\n    tr, on, n = ia1.bursts(s.trials, LIM[s.name])\n    seg = {}\n    for m in range(1, 5):\n        if (n == m).sum() >= 2:\n            seg[m], tt = ia1.segments(st, on[n == m])\n    sp = spikes_in(s)\n    sta_seg, tt = ia1.segments(st, sp)\n    BTA[s.name] = dict(seg=seg, tt=tt, sta_seg=sta_seg, on=on, n=n, tr=tr, mean_stim=st[4000:20000].mean())\nhave4 = [s for s in BURSTING if len(BTA[s.name][\"seg\"]) == 4]\nprint(\"bursting sessions:\", len(BURSTING), \"; with at least two bursts of each n = 1 to 4:\", len(have4))\n\"\"\")\n\nmd(r\"\"\"\n## fig8-nbta-differ\n\n> In every bursting cell the burst-triggered averages for n = 1 to 4 differ significantly (in the\n> example cell their central peaks grow higher and wider with n); 50 of the 58 bursting sessions\n> show significantly different central peaks in the time domain, the other eight having too few\n> bursts.\n\nTwo-way ANOVAs (frequency bin x n) on the real and the imaginary parts of the Fourier transform of\neach segment, each at 0.01 / 2; frequency bins (a) all, (b) up to the cutoff. Then at each time\npoint, t-tests of each nBTA against the three others, p < 0.01; a point is marked for n when all\nthree are significant. Central peak: from the minimum before to the minimum after the central\nmaximum. Readings (a) at least one marked point in the central peak of every n, (b) more than half\nof the points of every central peak marked.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in have4:\n    B = BTA[s.name]\n    tt = B[\"tt\"]\n    segs = [B[\"seg\"][m] for m in range(1, 5)]\n    ffts = [np.fft.rfft(g, axis=1) for g in segs]\n    freqs = np.fft.rfftfreq(len(tt), 1 / ia1.STIM_RATE)\n    row = dict(session=s.name, protocol=s.protocol, counts=[len(g) for g in segs])\n    for fr, sel in [(\"a\", slice(None)), (\"b\", freqs <= s.cutoff)]:\n        ps = []\n        for part in [np.real, np.imag]:\n            gs = [part(f)[:, sel] for f in ffts]\n            if part is np.imag:\n                gs = [g[:, 1:] for g in gs]          # the imaginary part of the 0 Hz bin is 0\n            ps.append(min(ia1.two_way_anova(gs)))\n        row[f\"anova_{fr}\"] = min(ps) < 0.01 / 2\n    btas = [g.mean(0) for g in segs]\n    marked = []\n    for i in range(4):\n        sig = np.ones(len(tt), bool)\n        for j in range(4):\n            if j != i:\n                sig &= p_two_sided_ttests(segs[i], segs[j]) < 0.01\n        ip, a, b = ia1.central_peak(btas[i], tt)\n        marked.append(sig[a:b + 1].mean())\n    row[\"peak_any\"] = all(m > 0 for m in marked)\n    row[\"peak_most\"] = all(m > 0.5 for m in marked)\n    row[\"marked_fraction\"] = [round(m, 2) for m in marked]\n    rows.append(row)\nN8 = pd.DataFrame(rows)\nprint(N8.to_string(index=False))\nfor fr in \"ab\":\n    g = N8[N8[f\"anova_{fr}\"]]\n    print(f\"\\nfrequency bins ({fr}): ANOVA significant in {len(g)} of {len(N8)} sessions with n = 1 to 4;\"\n          f\" central peaks differ (a) any point: {int(g.peak_any.sum())}, (b) most points: {int(g.peak_most.sum())}\")\nprint(\"bursting sessions (detail 4 (a)):\", len(BURSTING), \"; with bursts of n = 1 to 4 (two or more each):\", len(have4))\n\"\"\", tags=[\"claim:fig8-nbta-differ\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig8-latency-decreases\n\n> The latency between the stimulus upstroke and burst onset decreases with n, so that high or wide\n> deflections produce prompt responses with high-n bursts.\n\ntau_n per session with bursts of n = 1 to 4. Readings (a) tau_n decreasing from n = 1 to 4 (tau_4 <\ntau_1 with no increase between consecutive n) in the majority of those sessions; (b) the mean over\nsessions of tau_n decreasing from 1 to 4.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in have4:\n    B = BTA[s.name]\n    taus = [-B[\"tt\"][ia1.central_peak(B[\"seg\"][m].mean(0), B[\"tt\"])[0]] * 1e3 for m in range(1, 5)]\n    rows.append(dict(session=s.name, protocol=s.protocol, **{f\"tau{m}\": t for m, t in zip(range(1, 5), taus)},\n                     non_increasing=all(np.diff(taus) <= 0) and taus[3] < taus[0], tau4_below_tau1=taus[3] < taus[0]))\nLT = pd.DataFrame(rows)\nprint(LT.round(2).to_string(index=False))\nprint(\"\\n(a) sessions with tau_n decreasing from 1 to 4:\", int(LT.non_increasing.sum()), \"of\", len(LT),\n      \"; with tau_4 < tau_1:\", int(LT.tau4_below_tau1.sum()))\nprint(\"(b) mean tau_n (ms):\", LT[[\"tau1\", \"tau2\", \"tau3\", \"tau4\"]].mean().round(2).to_dict())\nprint(\"    Wilcoxon tau_1 vs tau_4: p =\", stats.wilcoxon(LT.tau1, LT.tau4).pvalue)\n\"\"\", tags=[\"claim:fig8-latency-decreases\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig8e-sigma-minimum\n\n> The standard deviation of the stimuli preceding an n-burst has a minimum at a position nearly the\n> same for all n; over the bursting cells the SD of the minimum's position across n = 1 to 4\n> averages 0.4 ms (SD 0.7 ms), roughly 0.05 times the inverse cutoff frequency.\n\nsigma_n(tau) by Eq. 14. Window for the minimum (a) -25 to 0 ms, (b) -25 to +15 ms. The SD across\nthe four n is the sample SD (N - 1), as MATLAB's `std`; the population SD (N) is shown too.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in have4:\n    B = BTA[s.name]\n    tt = B[\"tt\"]\n    row = dict(session=s.name, cutoff=s.cutoff)\n    for w, sel in [(\"a\", tt <= 0), (\"b\", tt <= tt.max())]:\n        pos = [tt[sel][np.argmin(B[\"seg\"][m].std(0, ddof=1)[sel])] * 1e3 for m in range(1, 5)]\n        row[f\"pos_{w}\"] = pos\n        row[f\"sd_{w}\"] = np.std(pos, ddof=1)\n        row[f\"sd0_{w}\"] = np.std(pos)\n    rows.append(row)\nSG = pd.DataFrame(rows)\nfor w in \"ab\":\n    for col in [f\"sd_{w}\", f\"sd0_{w}\"]:\n        x = SG[col]\n        xc = SG[col] * SG.cutoff * 1e-3\n        print(f\"window ({w}) {'N-1' if col.startswith('sd_') else 'N'}: mean SD of position {x.mean():.3f} ms (SD {x.std(ddof=1):.3f}),\"\n              f\" median {x.median():.3f}; times cutoff: mean {xc.mean():.4f} (SD {xc.std(ddof=1):.4f}), n = {len(x)}\")\nprint(\"\\nmedian position of the minimum (ms), window (a), per n:\", np.median(np.array(SG.pos_a.tolist()), 0))\n\"\"\", tags=[\"claim:fig8e-sigma-minimum\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## sigma-n-below-sta-sigma\n\n> In 98% of bursting cells, for all n, the SD of the stimuli preceding an n-burst is smaller than\n> the SD of the stimuli preceding all spikes, by a ratio of minima of 1.62 on average (SD 0.56).\n\n\"Smaller\" read as (a) the minimum of sigma_n below the minimum of sigma, (b) sigma_n below sigma at\nevery tau in -25 to +15 ms; n = 1 to 4. The ratio is min sigma over the mean over n of min sigma_n,\nminima over -25 to +15 ms (and over -25 to 0 ms as a variant).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in have4:\n    B = BTA[s.name]\n    tt = B[\"tt\"]\n    sig = B[\"sta_seg\"].std(0, ddof=1)\n    sn = [B[\"seg\"][m].std(0, ddof=1) for m in range(1, 5)]\n    rows.append(dict(session=s.name, a=all(x.min() < sig.min() for x in sn), b=all((x < sig).all() for x in sn),\n                     ratio=sig.min() / np.mean([x.min() for x in sn]),\n                     ratio_pre=sig[tt <= 0].min() / np.mean([x[tt <= 0].min() for x in sn])))\nSB = pd.DataFrame(rows)\nprint(f\"sessions: {len(SB)}; (a) min sigma_n < min sigma for all n: {100 * SB.a.mean():.1f}%; (b) at every tau: {100 * SB.b.mean():.1f}%\")\nprint(f\"ratio min sigma / mean_n min sigma_n: mean {SB.ratio.mean():.3f} (SD {SB.ratio.std(ddof=1):.3f}), range {SB.ratio.min():.3f} to {SB.ratio.max():.3f};\"\n      f\" window -25 to 0 ms: mean {SB.ratio_pre.mean():.3f} (SD {SB.ratio_pre.std(ddof=1):.3f})\")\n\"\"\", tags=[\"claim:sigma-n-below-sta-sigma\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- fig9\nmd(r\"\"\"\n## fig9-nbta-not-concatenated-1bta\n\n> The nBTA differs from n 1BTAs shifted by the burst's own ISIs and summed; for a large fraction of\n> cells the difference is significant, the fraction diminishing as n grows; results are similar\n> with shifted STAs.\n\nf_n(t) = sum over the burst's spikes of 1BTA(t - t_i) (Eq. 15). Summing n copies of a stimulus in\ndB only compares with the nBTA once the mean stimulus is subtracted (as the paper does for Figure\n9C); this is taken as the reading of Eq. 15, an assumption, and the average of the shifted copies\n(the sum over n) is shown as a variant. The 1BTA (or STA) is computed from -60 to +15 ms so that\nits shifts cover the window. Comparison over the interval between the minima flanking the central\nmaximum of the nBTA: two-way ANOVAs (frequency bin x group) on the real and imaginary parts of the\nFourier transform, at 0.01 / 2, with observations (a) each burst's segment against its own f_n\n(paired: ANOVA on the differences), (b) the segments and the f_n as two groups. Then t-tests at\neach time point (p < 0.01) and sessions with more than 70% of the interval significant.\n\"\"\")\n\ncode(r\"\"\"\ndef paired_anova(d):\n    # Differences segment - f_n per burst (rows) and frequency bin (columns): p of a mean\n    # difference (group main effect) and of its variation across bins (the interaction).\n    Nb, F = d.shape\n    m = d.mean()\n    mf = d.mean(0)\n    ss_err = ((d - mf) ** 2).sum()\n    df_err = (Nb - 1) * F\n    ms = ss_err / df_err\n    p_main = stats.f.sf(Nb * F * m ** 2 / ms, 1, df_err)\n    p_int = stats.f.sf(Nb * ((mf - m) ** 2).sum() / (F - 1) / ms, F - 1, df_err)\n    return min(p_main, p_int)\n\n\nrows = []\nfor s in BURSTING:\n    B = BTA[s.name]\n    st = stim_db(s)\n    ms = B[\"mean_stim\"]\n    tr, on, n = B[\"tr\"], B[\"on\"], B[\"n\"]\n    long_t0 = 0.06\n    one, tl = ia1.segments(st, on[n == 1], pre=long_t0)\n    allsp, _ = ia1.segments(st, spikes_in(s), pre=long_t0)\n    kernels = {\"1BTA\": one.mean(0) - ms, \"STA\": allsp.mean(0) - ms}\n    i_zero = int(round(long_t0 * ia1.STIM_RATE))\n    for m in [2, 3, 4]:\n        if m not in B[\"seg\"]:\n            continue\n        idx = np.flatnonzero(n == m)\n        seg = B[\"seg\"][m] - ms\n        tt = B[\"tt\"]\n        ip, a, b = ia1.central_peak(seg.mean(0), tt)\n        if b - a < 3:\n            continue\n        # spike offsets of each burst relative to its onset\n        trial_spikes = s.trials\n        for kname, ker in kernels.items():\n            for scale in [\"sum\", \"mean\"]:\n                fn = np.zeros_like(seg)\n                for r, k in enumerate(idx):\n                    t = trial_spikes[tr[k]]\n                    j = np.searchsorted(t, on[k])\n                    offs = t[j:j + m] - on[k]\n                    for o in offs:\n                        sh = int(round(o * ia1.STIM_RATE))\n                        fn[r] += ker[i_zero - 500 - sh:i_zero + 300 - sh]\n                    if scale == \"mean\":\n                        fn[r] /= m\n                x, y = seg[:, a:b + 1], fn[:, a:b + 1]\n                X, Y = np.fft.rfft(x, axis=1), np.fft.rfft(y, axis=1)\n                pa = min(paired_anova(np.real(X - Y)), paired_anova(np.imag(X - Y)[:, 1:]) if X.shape[1] > 2 else 1)\n                pb = min(min(ia1.two_way_anova([np.real(X), np.real(Y)])), min(ia1.two_way_anova([np.imag(X)[:, 1:], np.imag(Y)[:, 1:]])) if X.shape[1] > 2 else 1)\n                tp = stats.ttest_ind(x, y, axis=0).pvalue\n                rows.append(dict(session=s.name, n=m, kernel=kname, scale=scale, bursts=len(idx), anova_a=pa < 0.005, anova_b=pb < 0.005,\n                                 t_frac=(tp < 0.01).mean()))\nN9 = pd.DataFrame(rows)\nsumm = []\nfor (kname, scale, m), g in N9.groupby([\"kernel\", \"scale\", \"n\"]):\n    summ.append(dict(kernel=kname, scale=scale, n=m, sessions=len(g), anova_a_pct=round(100 * g.anova_a.mean(), 1),\n                     anova_b_pct=round(100 * g.anova_b.mean(), 1),\n                     t70_a_pct=round(100 * (g.anova_a & (g.t_frac > 0.7)).mean(), 1),\n                     t70_b_pct=round(100 * (g.anova_b & (g.t_frac > 0.7)).mean(), 1)))\nprint(pd.DataFrame(summ).to_string(index=False))\n\"\"\", tags=[\"claim:fig9-nbta-not-concatenated-1bta\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig9c-population-nbta\n\n> In the seven cells driven at 100 Hz cutoff and 6 dB, the population-average nBTAs show that\n> bursts with more spikes follow higher or wider stimulus deflections, with large spread across\n> cells.\n\nEach session's 1BTA, 2BTA and 3BTA minus its mean stimulus, shifted so that its central maximum\nsits at the mean tau_n over the sessions (shifting by tau_n, averaging and shifting back), averaged\nover the bursting protocol-5 sessions with at least two bursts of n = 1 to 3. Width (a) full width\nat half height, (b) between the minima flanking the central maximum.\n\"\"\")\n\ncode(r\"\"\"\np5 = [s for s in BURSTING if s.protocol == 5 and all(m in BTA[s.name][\"seg\"] for m in (1, 2, 3))]\nprint(\"protocol-5 sessions: kept\", sum(s.protocol == 5 for s in KEPT), \"; bursting\", sum(s.protocol == 5 for s in BURSTING),\n      \"; with n = 1 to 3:\", len(p5), [s.name for s in p5])\nfig, ax = plt.subplots(figsize=(6, 4))\nrows = []\nfor m in (1, 2, 3):\n    tt = BTA[p5[0].name][\"tt\"]\n    btas, peaks = [], []\n    for s in p5:\n        b = BTA[s.name][\"seg\"][m].mean(0) - BTA[s.name][\"mean_stim\"]\n        btas.append(b)\n        peaks.append(ia1.central_peak(b, tt)[0])\n    target = int(round(np.mean(peaks)))\n    aligned = np.array([np.roll(b, target - p) for b, p in zip(btas, peaks)])\n    avg = aligned.mean(0)\n    ip, a, b2 = ia1.central_peak(avg, tt)\n    rows.append(dict(n=m, height_dB=avg[ip], fwhm_ms=ia1.fwhm(avg, ip, 0.0) / 20, minima_width_ms=(b2 - a) / 20,\n                     spread_at_peak_dB=aligned[:, ip].std(ddof=1), tau_ms=-tt[ip] * 1e3))\n    ax.plot(tt * 1e3, avg, label=f\"{m}BTA\")\n    ax.fill_between(tt * 1e3, avg - aligned.std(0, ddof=1), avg + aligned.std(0, ddof=1), alpha=0.2)\nax.set(xlabel=\"time from burst onset (ms)\", ylabel=\"stimulus minus its mean (dB)\")\nax.legend()\nplt.show()\nF9C = pd.DataFrame(rows)\nprint(F9C.round(2).to_string(index=False))\n\"\"\", tags=[\"claim:fig9c-population-nbta\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- fig10\nmd(r\"\"\"\n## fig10-burst-n-vs-height\n\n> The probability of a burst with n spikes after a stimulus maximum depends on its height, low\n> excursions giving no response or an isolated spike and high ones doublets, triplets or 4-bursts;\n> all bursting cells show this.\n\nMethods (Relating burst probabilities to the height of stimulus excursions), per trial: each\nn-burst shifted back by tau_n; each local maximum of the stimulus in 200 to 1000 ms matched to the\nburst whose shifted onset is closest within [t0 - T, t0 + T]; a burst matched to more than one\nmaximum kept by the nearest, the other maxima counting as no response. T is the width of the\ncentral STA peak, (a) between its flanking minima, (b) full width at half height. P(n | h) in\nwindows of half-width 5% of the span of h, at 41 centres. Segregation (a) the h at which P(n | h)\npeaks increases with n for n = 0 to the largest n with bursts (up to 4); (b) the mean of h\nweighted by P(n | h) increases with n. Bursting sessions with bursts of n = 1 and 2 at least.\n\"\"\")\n\ncode(r\"\"\"\nfrom scipy.signal import argrelmax\n\n\ndef p_n_given_h(s, Twin):\n    B = BTA[s.name]\n    st = stim_db(s)\n    i0, i1 = int(ia1.T0 * ia1.STIM_RATE), int(ia1.T1 * ia1.STIM_RATE)\n    mx = argrelmax(st[i0:i1])[0] + i0\n    tmax, h = mx / ia1.STIM_RATE, st[mx]\n    tt = B[\"tt\"]\n    tau = {m: -tt[ia1.central_peak(B[\"seg\"][m].mean(0), tt)[0]] for m in B[\"seg\"]}\n    resp = []\n    for i in range(s.n_trials):\n        k = B[\"tr\"] == i\n        on, n = B[\"on\"][k], B[\"n\"][k]\n        sh = on - np.array([tau.get(m, tau[max(tau)]) for m in n])\n        best = np.full(len(tmax), -1)\n        for j, t0 in enumerate(tmax):\n            d = np.abs(sh - t0)\n            if len(d) and d.min() <= Twin:\n                best[j] = np.argmin(d)\n        r = np.zeros(len(tmax), int)\n        for bi in np.unique(best[best >= 0]):\n            js = np.flatnonzero(best == bi)\n            jbest = js[np.argmin(np.abs(tmax[js] - sh[bi]))]\n            r[jbest] = n[bi]\n        resp.append(r)\n    resp = np.concatenate(resp)\n    hh = np.tile(h, s.n_trials)\n    span = hh.max() - hh.min()\n    centres = np.linspace(hh.min(), hh.max(), 41)\n    nmax = min(4, resp.max())\n    P = np.array([[np.mean(resp[np.abs(hh - c) <= 0.05 * span] == m) if (np.abs(hh - c) <= 0.05 * span).any() else np.nan\n                   for c in centres] for m in range(nmax + 1)])\n    return centres, P, nmax\n\n\nrows = []\nexample = None\nfor s in BURSTING:\n    B = BTA[s.name]\n    if not (1 in B[\"seg\"] and 2 in B[\"seg\"]):\n        continue\n    tt = B[\"tt\"]\n    sta = B[\"sta_seg\"].mean(0) - B[\"mean_stim\"]\n    ip, a, b = ia1.central_peak(sta, tt)\n    for tw, Tw in [(\"a\", (b - a) / ia1.STIM_RATE), (\"b\", ia1.fwhm(sta, ip, 0.0) / ia1.STIM_RATE)]:\n        centres, Pm, nmax = p_n_given_h(s, Tw)\n        peak_h = [centres[np.nanargmax(p)] for p in Pm]\n        mean_h = [np.nansum(centres * p) / np.nansum(p) for p in Pm]\n        rows.append(dict(session=s.name, T=tw, T_ms=Tw * 1e3, nmax=nmax, peak_h=np.round(peak_h, 1), mean_h=np.round(mean_h, 1),\n                         a=all(np.diff(peak_h) > 0), b=all(np.diff(mean_h) > 0)))\n        if example is None and nmax == 4 and tw == \"a\":\n            example = (s.name, centres, Pm)\nH = pd.DataFrame(rows)\nfor tw in \"ab\":\n    g = H[H[\"T\"] == tw]\n    print(f\"T ({tw}): median T {g.T_ms.median():.2f} ms; sessions {len(g)}; segregation (a) peak h increasing: {int(g.a.sum())}\"\n          f\" ({100 * g.a.mean():.1f}%); (b) mean h increasing: {int(g.b.sum())} ({100 * g.b.mean():.1f}%)\")\nprint(H[H[\"T\"] == \"a\"].head(10).to_string(index=False))\nname, centres, Pm = example\nfig, ax = plt.subplots(figsize=(6, 4))\nfor m, p in enumerate(Pm):\n    ax.plot(centres, p, label=f\"n = {m}\")\nax.set(xlabel=\"height of the stimulus maximum h (dB)\", ylabel=\"P(n | h)\", title=name, ylim=(0, 1))\nax.legend()\nplt.show()\n\"\"\", tags=[\"claim:fig10-burst-n-vs-height\"])\n\nmd(\"**Result: ...**\")\n\n# ---------------------------------------------------------------- rate effect\nmd(r\"\"\"\n## firing-rate-no-effect-on-limit\n\n> The firing rate has practically no effect on the limiting ISI; a 50 Hz increase in rate shifts it\n> by less than 0.4 ms and raises the average n by less than 25%.\n\nReading (a), the same cell and stimulus at two target rates 50 Hz apart: the headers record target\nrates of 100 and 90 Hz only (Data check), so no pair exists. Reading (b): linear regressions over\nthe kept sessions of the limiting ISI (bursting sessions) and of the average n on the session's\nrate, scaled to 50 Hz; the increase of the average n is relative to its mean.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in KEPT:\n    c = ia1.burst_counts(s.trials, LIM[s.name])\n    rows.append(dict(session=s.name, protocol=s.protocol, rate=D.loc[D.session == s.name, \"rate\"].iloc[0],\n                     limit_ms=LIM[s.name] * 1e3, avg_n=ia1.average_n(c)[0]))\nRT = pd.DataFrame(rows)\npairs = D[D.protocol.notna()].groupby([\"cell\", \"stimulus\"]).desired_rate.agg(lambda x: sorted(set(x.dropna())))\nprint(\"cell and stimulus with more than one target rate:\", [k for k, v in pairs.items() if len(v) > 1])\nfor lab, g in [(\"all kept\", RT), (\"protocol 1 only\", RT[RT.protocol == 1])]:\n    gb = g[g.limit_ms > 0]\n    r1 = stats.linregress(gb.rate, gb.limit_ms)\n    r2 = stats.linregress(g.rate, g.avg_n)\n    print(f\"{lab}: limiting ISI slope {r1.slope:.4f} ms/Hz (p {r1.pvalue:.3g}, n {len(gb)}) -> shift for +50 Hz {50 * r1.slope:.3f} ms;\"\n          f\" average n slope {r2.slope:.5f} per Hz (p {r2.pvalue:.3g}, n {len(g)}) -> +50 Hz changes it by {100 * 50 * r2.slope / g.avg_n.mean():.1f}%\"\n          f\" of its mean {g.avg_n.mean():.3f}\")\n\"\"\", tags=[\"claim:firing-rate-no-effect-on-limit\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## model-reproduces-coding-trends (blocked)\n\nDepends on model-matches-classification, which is blocked (`data_missing`, no thresholds s_TH).\n\n## Summary\n\n...\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/crcns-ia-1-eyherabide-2008/reproduce_eyherabide_2008.ipynb\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Notebook drafted. Running it in the dev environment to find errors and time it.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && uv pip install -q nbformat nbconvert ipykernel jupyter_client 2>&1 | tail -2; python $TMPDIR/make_nb.py && cd entries/crcns-ia-1-eyherabide-2008 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_eyherabide_2008.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -30
```

```
session_average=[round(v, 1) for v in iso_avg]))
print(pd.DataFrame(rows).to_string(index=False))
print("paper:", T1_ISO)
------------------


[31m---------------------------------------------------------------------------[39m
[31mValueError[39m                                Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[10][39m[32m, line 24[39m
[32m     20[39m 
[32m     21[39m rows = []
[32m     22[39m PC = {}
[32m     23[39m [38;5;28;01mfor[39;00m c [38;5;28;01min[39;00m COMBOS:
[32m---> [39m[32m24[39m     pc = protocol_counts(KEPT, limits[c])
[32m     25[39m     PC[c] = pc
[32m     26[39m     iso = [[32m100[39m * pc[p][[32m0[39m][[32m0[39m] / pc[p][[32m0[39m].sum() [38;5;28;01mfor[39;00m p [38;5;28;01min[39;00m range([32m1[39m, [32m8[39m)]
[32m     27[39m     iso_avg = [[32m100[39m * np.mean(pc[p][[32m1[39m]) [38;5;28;01mfor[39;00m p [38;5;28;01min[39;00m range([32m1[39m, [32m8[39m)]

[36mCell[39m[36m [39m[32mIn[10][39m[32m, line 15[39m, in [36mprotocol_counts[39m[34m(sel, lim)[39m
[32m     11[39m         tot = np.zeros([32m40[39m)
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/tot = np.zeros(40)/tot = np.zeros(400)/' make_nb.py && . dev/bin/activate && python make_nb.py && cd entries/crcns-ia-1-eyherabide-2008 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_eyherabide_2008.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -30
```

```
03-04-23-ad_sig2   6     800     False       0.0      4.9         0.40           0.4               0              0              0
03-04-23-ae_sig1   6     200      True       4.1      3.5         2.35           0.4               1              1              1
03-04-23-ae_sig2  12     200      True       4.2      3.3         5.06           0.3               1              1              1
03-04-23-ag_sig1   6     200      True       4.6      3.9         1.40           0.5               1              1              1
03-04-23-ag_sig2   6     400     False       0.0      4.6         0.35           0.2               0              0              0
03-04-23-ah_sig1   6     200      True       4.7      4.2         1.29           0.5               1              1              1
03-04-23-ah_sig2   6     100      True       5.3      4.3         2.59           0.8               2              2              1
03-04-23-ai_sig1   6     200      True       4.7      4.5         1.14           0.5               1              1              1
03-04-23-ai_sig2   6      25      True       4.9      4.2         4.96           0.7              14              5              4
03-04-23-aj_sig1   6     200      True       4.7      4.0         1.75           0.5               1              1              1
03-04-23-aj_sig2   3     200     False       0.0      5.0         0.50           0.4               1              1              0
------------------

[31m---------------------------------------------------------------------------[39m
[31mAttributeError[39m                            Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[13][39m[32m, line 32[39m
[32m     28[39m print(F3T.to_string(index=[38;5;28;01mFalse[39;00m))
[32m     29[39m [38;5;28;01mfor[39;00m ax, t [38;5;28;01min[39;00m zip(axes, [[33m"cutoff 200 Hz"[39m, [33m"SD 6 dB"[39m]):
[32m     30[39m     ax.set(xlabel=[33m"tau (ms)"[39m, ylabel=[33m"C_s / rbar^2"[39m, title=t,
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='make_nb.py'; s=open(p).read()
s=s.replace('''rows = []
fig, axes = plt.subplots(1, 2, figsize=(12, 4))''','''rows = []
curves = []
fig, axes = plt.subplots(1, 2, figsize=(12, 4))''')
s=s.replace('''    ax = axes[0] if s.sd_cut[1] == 200 else axes[1]''','''    curves.append(cn[1:])
    ax = axes[0] if s.sd_cut[1] == 200 else axes[1]''')
s=s.replace('''print("values of C_s/rbar^2 above the axes (4):", int(sum((r > 4).sum() for r in [0])))''','''allc = np.concatenate(curves)
print("C_s/rbar^2 for tau > 0: range", allc.min().round(2), "to", allc.max().round(2), "; points outside the axes (-1.5 to 4):", int(((allc < -1.5) | (allc > 4)).sum()))''')
open(p,'w').write(s)
EOF
. dev/bin/activate && python make_nb.py && cd entries/crcns-ia-1-eyherabide-2008 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_eyherabide_2008.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -30
```

```
[NbConvertApp] Converting notebook reproduce_eyherabide_2008.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 435220 bytes to /tmp/claude-1001/out.ipynb

real	4m7.239s
user	3m13.952s
sys	0m34.989s
```

**Agent**

The whole notebook runs in 4 minutes. Reading the outputs now.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import nbformat
nb=nbformat.read('out.ipynb',4)
for i,c in enumerate(nb.cells):
  if c.cell_type!='code': continue
  print('=== cell',i,c.metadata.get('tags'))
  for o in c.outputs:
    if o.output_type=='stream': print(o.text[:6000])
    elif o.output_type=='error': print('ERR',o.ename,o.evalue)
" | head -400
```

```
<persisted-output>
Output too large (39.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b9f93dab-34d2-4022-b315-7f7507d47857/tool-results/bfdyhchkc.txt

Preview (first 2KB):
=== cell 1 None
data set ia-1 unversioned doi 10.6080/K0BG2KWB zip md5 f0740514fabc6995fe54b2a361b6c763

=== cell 3 ['sanity']
Data1 experiments: 75  sessions: 150  offline-sorted sessions (no OEL header): 28
experiments not listed in singlecells.txt: ['03-01-15-aa', '03-06-27-ae']
cells (rows of singlecells.txt, plus experiments not listed): 45  recording dates: 25

Sessions by stimulus file (cell.dat):
                     sessions  protocol
stimulus                               
gaussModality_co200        14       NaN
gauss_st12_co200            8       3.0
gauss_st3_co200             9       2.0
gauss_st6_co100            11       5.0
gauss_st6_co200            54       1.0
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b9f93dab-34d2-4022-b315-7f7507d47857/tool-results/bfdyhchkc.txt"
}
```

```
1	=== cell 1 None
2	data set ia-1 unversioned doi 10.6080/K0BG2KWB zip md5 f0740514fabc6995fe54b2a361b6c763
3	
4	=== cell 3 ['sanity']
5	Data1 experiments: 75  sessions: 150  offline-sorted sessions (no OEL header): 28
6	experiments not listed in singlecells.txt: ['03-01-15-aa', '03-06-27-ae']
7	cells (rows of singlecells.txt, plus experiments not listed): 45  recording dates: 25
8	
9	Sessions by stimulus file (cell.dat):
10	                     sessions  protocol
11	stimulus                               
12	gaussModality_co200        14       NaN
13	gauss_st12_co200            8       3.0
14	gauss_st3_co200             9       2.0
15	gauss_st6_co100            11       5.0
16	gauss_st6_co200            54       1.0
17	gauss_st6_co25              9       4.0
18	gauss_st6_co400             8       6.0
19	gauss_st6_co800             9       7.0
20	lmd_co200                  14       NaN
[... 381 more lines not kept]
```

**Agent**

Most claims ran. Several results need a second look: τ_n often hits the 0 ms edge of my search window, and the jitter readings either split or merge events. First the rest of the output.

**Agent calls Bash**

```bash
sed -n 380,480p /home/runner/.claude/projects/-home-runner-work-encore-encore/b9f93dab-34d2-4022-b315-7f7507d47857/tool-results/bfdyhchkc.txt | cut -c1-250 | grep -v "^03-0" ; date -u
```

```
=== cell 64 ['claim:fig8-latency-decreases']
         session  protocol  tau1  tau2  tau3  tau4  non_increasing  tau4_below_tau1
Wed Nov  4 18:41:26 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import nbformat
nb=nbformat.read('out.ipynb',4)
for i,c in enumerate(nb.cells):
  if c.cell_type!='code' or i<60: continue
  print('=== cell',i,c.metadata.get('tags'))
  for o in c.outputs:
    if o.output_type=='stream': print('\n'.join(l for l in o.text.splitlines() if not l.startswith('03-')))
"
```

```
=== cell 61 ['claim:fig8-nbta-differ']
         session  protocol                   counts  anova_a  anova_b  peak_any  peak_most          marked_fraction

frequency bins (a): ANOVA significant in 71 of 71 sessions with n = 1 to 4; central peaks differ (a) any point: 54, (b) most points: 11

frequency bins (b): ANOVA significant in 71 of 71 sessions with n = 1 to 4; central peaks differ (a) any point: 54, (b) most points: 11
bursting sessions (detail 4 (a)): 84 ; with bursts of n = 1 to 4 (two or more each): 71
=== cell 64 ['claim:fig8-latency-decreases']
         session  protocol  tau1  tau2  tau3  tau4  non_increasing  tau4_below_tau1

(a) sessions with tau_n decreasing from 1 to 4: 30 of 71 ; with tau_4 < tau_1: 69
(b) mean tau_n (ms): {'tau1': 5.75, 'tau2': 4.15, 'tau3': 3.14, 'tau4': 2.46}
    Wilcoxon tau_1 vs tau_4: p = 4.45723499370877e-12
=== cell 67 ['claim:fig8e-sigma-minimum']
window (a) N-1: mean SD of position 2.164 ms (SD 2.404), median 1.834; times cutoff: mean 0.3640 (SD 0.4745), n = 71
window (a) N: mean SD of position 1.874 ms (SD 2.082), median 1.589; times cutoff: mean 0.3153 (SD 0.4110), n = 71
window (b) N-1: mean SD of position 2.641 ms (SD 2.678), median 2.148; times cutoff: mean 0.4346 (SD 0.5047), n = 71
window (b) N: mean SD of position 2.287 ms (SD 2.319), median 1.860; times cutoff: mean 0.3763 (SD 0.4371), n = 71

median position of the minimum (ms), window (a), per n: [-6.65 -6.3  -5.   -6.25]
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('out.ipynb',4)
# collect code of cells up to fig10 definitions into a script, run on a few sessions
src=[]
for c in nb.cells:
    if c.cell_type=='code': src.append(c.source)
import re
code='\n'.join(src)
EOF
python3 - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/out.ipynb',4)
for c in nb.cells:
    if 'claim:fig10-burst-n-vs-height' in c.metadata.get('tags',[]):
        for o in c.outputs:
            if o.output_type=='stream': print(o.text[:3000])
EOF
```

```
/tmp/claude-1001/ipykernel_10/566981608.py:50: RuntimeWarning: invalid value encountered in scalar divide
  mean_h = [np.nansum(centres * p) / np.nansum(p) for p in Pm]

T (a): median T 7.40 ms; sessions 84; segregation (a) peak h increasing: 8 (9.5%); (b) mean h increasing: 19 (22.6%)
T (b): median T 3.05 ms; sessions 84; segregation (a) peak h increasing: 8 (9.5%); (b) mean h increasing: 19 (22.6%)
         session T  T_ms  nmax                         peak_h                         mean_h     a     b
03-01-16-ab_sig2 a  6.90     4 [29.2, 68.4, 62.3, 72.1, 58.6] [39.1, 57.3, 62.1, 68.2, 60.1] False False
03-02-14-aa_sig1 a  7.40     4 [32.8, 45.5, 54.4, 54.4, 55.0] [37.3, 46.9, 50.6, 49.8, 50.7] False False
03-02-14-aa_sig2 a 39.95     4 [44.2, 48.7, 44.2, 44.2, 44.2]  [nan, 46.3, 45.5, 45.3, 45.6] False False
03-02-18-ab_sig1 a  7.20     3       [48.8, 61.5, 68.5, 71.0]       [52.5, 62.3, 67.3, 69.2]  True  True
03-02-25-ac_sig1 a  7.45     4 [51.8, 64.5, 71.5, 74.0, 74.0] [55.8, 65.4, 70.3, 71.5, 73.5] False  True
03-02-25-ac_sig2 a  3.50     3       [51.7, 69.7, 72.0, 70.8]       [57.4, 68.3, 70.5, 71.6] False  True
03-02-25-aj_sig1 a  7.35     4 [21.8, 34.5, 43.4, 44.0, 41.5] [26.3, 34.9, 39.4, 39.6, 38.7] False False
03-03-05-ab_sig1 a  7.30     4 [40.8, 53.5, 62.4, 63.0, 60.5] [44.5, 53.6, 60.2, 61.1, 60.6] False False
03-03-05-ab_sig2 a  7.40     4 [44.6, 50.9, 54.5, 54.2, 52.8] [48.3, 50.1, 52.1, 52.7, 52.2] False False
03-03-05-ac_sig1 a  7.35     3       [37.8, 53.7, 59.4, 60.0]       [41.9, 50.9, 57.4, 58.1]  True  True
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ia-1-eyherabide-2008 && python3 - <<'EOF'
p='ia1.py'; s=open(p).read()
old=s[s.index('def jitter_events_b'):s.index('# ---------------------------------------------------------------- burst-triggered averages')]
new='''def jitter_events_b(onsets_by_trial, limit, dt=DT, t0=T0, t1=T1):
    """Reading (b): event centres are the bins of the onset histogram (0.1 ms), taken from the
    highest down; an event is the onsets not yet assigned that fall within the first-peak
    domain (the limiting ISI) centred on the bin, that is within limit / 2 of its centre. Mean
    over events with at least two onsets of their SD (s), or nan."""
    allon = np.sort(np.concatenate(onsets_by_trial)) if onsets_by_trial else np.zeros(0)
    if len(allon) < 2 or limit <= 0:
        return np.nan
    nb = int(round((t1 - t0) / dt))
    k = ((allon - t0) / dt).astype(int).clip(0, nb - 1)
    h = np.bincount(k, minlength=nb)
    free = np.ones(len(allon), bool)
    sds = []
    for b in np.argsort(-h, kind="stable"):
        if h[b] < 2:
            break
        c = t0 + (b + 0.5) * dt
        lo, hi = np.searchsorted(allon, [c - limit / 2, c + limit / 2], side="left")
        idx = np.arange(lo, hi)[free[lo:hi]]
        if len(idx) >= 2:
            sds.append(allon[idx].std(ddof=1))
        free[idx] = False
    return np.mean(sds) if sds else np.nan


'''
s=s.replace(old,new)
s=s.replace('''def central_peak(bta, t, search=(-PRE, 0.0)):
    """Index of the central maximum of a BTA (its maximum in `search`, which contains the
    upstroke before the burst) and of the minima flanking it (the nearest local minima on each
    side, or the window's ends)."""
    w = np.flatnonzero((t >= search[0]) & (t <= search[1]))''','''def central_peak(bta, t, search=None):
    """Index of the central maximum of a BTA and of the minima flanking it (the nearest local
    minima on each side, or the window's ends). The maximum is taken over the whole window
    unless `search` gives limits: Methods, "The time tau_n between the maximum of nBTA and
    tau = 0 (burst generation) is the average latency of the n-burst"."""
    w = np.arange(len(t)) if search is None else np.flatnonzero((t >= search[0]) & (t <= search[1]))''')
open(p,'w').write(s)
p='/tmp/claude-1001/make_nb.py'; s=open(p).read()
s=s.replace('''an nBTA is its maximum between -25 and 0 ms; tau_n is its distance to the onset (Eq. 13 and the
sentence after it).''','''an nBTA is its maximum over the window; tau_n is its distance to the onset (Eq. 13 and the
sentence after it: "The time tau_n between the maximum of nBTA and tau = 0").''')
s=s.replace('''Jitter per n is the mean over events of the SD of the onset times. Events (a) peaks of the onset
histogram in 0.1 ms bins, between the troughs on either side; (b) runs of pooled onsets whose
gaps are within the session's limiting ISI.''','''Jitter per n is the mean over events of the SD of the onset times. Events (a) peaks of the onset
histogram in 0.1 ms bins, between the troughs on either side; (b) onsets within the session's
first-peak domain (the limiting ISI) centred on an event centre, the centres being the histogram
bins taken from the highest down (`ia1.jitter_events_b`).''')
s=s.replace('''    resp = np.concatenate(resp)
    hh = np.tile(h, s.n_trials)''','''    resp = np.concatenate(resp)
    matched = int((resp > 0).sum())
    hh = np.tile(h, s.n_trials)''')
s=s.replace('''    return centres, P, nmax


rows = []''','''    return centres, P, nmax, matched


rows = []''')
s=s.replace('''        centres, Pm, nmax = p_n_given_h(s, Tw)
        peak_h = [centres[np.nanargmax(p)] for p in Pm]
        mean_h = [np.nansum(centres * p) / np.nansum(p) for p in Pm]
        rows.append(dict(session=s.name, T=tw, T_ms=Tw * 1e3, nmax=nmax, peak_h=np.round(peak_h, 1), mean_h=np.round(mean_h, 1),
                         a=all(np.diff(peak_h) > 0), b=all(np.diff(mean_h) > 0)))''','''        centres, Pm, nmax, matched = p_n_given_h(s, Tw)
        peak_h = [centres[np.nanargmax(p)] for p in Pm]
        mean_h = [np.nansum(centres * p) / np.nansum(p) for p in Pm]
        rows.append(dict(session=s.name, T=tw, T_ms=Tw * 1e3, nmax=nmax, matched=matched, peak_h=np.round(peak_h, 1),
                         mean_h=np.round(mean_h, 1), a=all(np.diff(peak_h) > 0), b=all(np.diff(mean_h) > 0),
                         a3=all(np.diff(peak_h[:4]) > 0), b3=all(np.diff(mean_h[:4]) > 0)))''')
s=s.replace('''          f" ({100 * g.a.mean():.1f}%); (b) mean h increasing: {int(g.b.sum())} ({100 * g.b.mean():.1f}%)")''','''          f" ({100 * g.a.mean():.1f}%); (b) mean h increasing: {int(g.b.sum())} ({100 * g.b.mean():.1f}%);"
          f" variant n = 0 to 3 only: (a) {int(g.a3.sum())}, (b) {int(g.b3.sum())}; maxima matched to a burst, median {g.matched.median():.0f}")
ga, gb = H[H["T"] == "a"].set_index("session"), H[H["T"] == "b"].set_index("session")
print("sessions where the two T readings match a different number of maxima:", int((ga.matched != gb.matched).sum()), "of", len(ga))''')
open(p,'w').write(s)
EOF
grep -n "search=(-PRE\|central_peak(" ia1.py $TMPDIR/make_nb.py | head
```

```
ia1.py:477:def central_peak(bta, t, search=None):
/tmp/claude-1001/make_nb.py:921:        ip, a, b = ia1.central_peak(btas[i], tt)
/tmp/claude-1001/make_nb.py:953:    taus = [-B["tt"][ia1.central_peak(B["seg"][m].mean(0), B["tt"])[0]] * 1e3 for m in range(1, 5)]
/tmp/claude-1001/make_nb.py:1081:        ip, a, b = ia1.central_peak(seg.mean(0), tt)
/tmp/claude-1001/make_nb.py:1142:        peaks.append(ia1.central_peak(b, tt)[0])
/tmp/claude-1001/make_nb.py:1146:    ip, a, b2 = ia1.central_peak(avg, tt)
/tmp/claude-1001/make_nb.py:1189:    tau = {m: -tt[ia1.central_peak(B["seg"][m].mean(0), tt)[0]] for m in B["seg"]}
/tmp/claude-1001/make_nb.py:1225:    ip, a, b = ia1.central_peak(sta, tt)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python make_nb.py && cd entries/crcns-ia-1-eyherabide-2008 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_eyherabide_2008.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -3 && cd $TMPDIR && python3 -c "
import nbformat
nb=nbformat.read('out.ipynb',4)
for i,c in enumerate(nb.cells):
  t=c.metadata.get('tags',[])
  if c.cell_type!='code' or not any(x in str(t) for x in ['fig8','fig7ef','fig10','fig9','sigma']): continue
  print('=== cell',i,t)
  for o in c.outputs:
    if o.output_type=='stream': print('\n'.join(l for l in o.text.splitlines() if not l.startswith('03-')))
    if o.output_type=='error': print(o.evalue)
"
```

```
[NbConvertApp] Converting notebook reproduce_eyherabide_2008.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 436469 bytes to /tmp/claude-1001/out.ipynb

real	4m7.580s
user	3m17.719s
sys	0m33.613s
=== cell 50 ['claim:fig7ef-jitter-independent-of-n']
events  sessions_with_test  no_test  mean_slope_ms  sd_slope_ms  pct_not_sig_a  pct_not_sig_b  median_jitter_n1_ms
     a                  83        1         -0.001        0.005           43.4           91.6                0.058
     b                  81        3          0.005        0.050           34.6           87.7                0.389
=== cell 61 ['claim:fig8-nbta-differ']
         session  protocol                   counts  anova_a  anova_b  peak_any  peak_most          marked_fraction

frequency bins (a): ANOVA significant in 71 of 71 sessions with n = 1 to 4; central peaks differ (a) any point: 60, (b) most points: 14

frequency bins (b): ANOVA significant in 71 of 71 sessions with n = 1 to 4; central peaks differ (a) any point: 60, (b) most points: 14
bursting sessions (detail 4 (a)): 84 ; with bursts of n = 1 to 4 (two or more each): 71
=== cell 64 ['claim:fig8-latency-decreases']
         session  protocol  tau1  tau2  tau3  tau4  non_increasing  tau4_below_tau1
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='make_nb.py'; s=open(p).read()
R = [
# 1 data-sessions-and-trials
"""**Result: partially reproduced.** The 116 sessions of the seven protocols come from 37 cells
recorded on 23 dates, the paper's 37 cells and 23 animals (if one animal was recorded per date, an
assumption, as Data1 does not record the animal). The 122 Gaussian AM sessions (any cutoff) are
within 10% of the paper's 132 sessions; all 150 Data1 sessions are not. The selection does not
reproduce: the SD < 35 Hz condition keeps 115 of the 116 sessions (113 with the 100 Hz target of
reading (b)), against 86, so the paper's selection removed sessions by a rule it does not state.
Over the kept sessions the trials range from 69 (outside 98 +/- 9.8) to 503 and average 160.3
(within 172 +/- 17.2), and the mean trial-to-trial SD of the rate is 6.48 Hz (within 6 +/- 0.6).""",
# 2
"""**Result: not reproduced.** None of the seven counts is within 10% of Table 1 under any reading:
the kept sessions are 60, 9, 8, 10, 11, 8 and 9 per protocol (reading (a), 200 to 1000 ms) against
43, 6, 7, 7, 8, 7 and 8. The data set holds every reference session paired with each other
protocol (55 experiments) and more reference sessions than the paper counts; the paper's 86 are a
subset whose selection is not stated.""",
# 3
"""**Result: reproduced.** Over the 115 kept sessions the mean rate is 110.2 Hz (within 113 +/- 16)
with SD 16.7 Hz (within 16 +/- 1.6), and a one-way ANOVA across the seven protocols finds no
difference (F = 0.49, p = 0.818). Over all seven-protocol sessions and with whole-trial rates the
ANOVA gives p = 0.809 and 0.471; whole-trial rates average 114.7 Hz (SD 16.9). The population is
115 sessions, not the paper's 86.""",
# 4 table1-bursting
"""**Result: not reproduced.** Under the main reading (peak b, minimum a, N a) the kept sessions
with bursts of n > 1 are 52/60, 2/9, 8/8, 9/10, 10/11, 3/8 and 0/9 against 40/43, 0/6, 7/7, 6/7,
7/8, 3/7 and 0/8: 2 of 7 counts within tolerance (400 and 800 Hz), and no combination of readings
does better. The pattern across protocols is the paper's (most reference, 12 dB, 25 Hz and 100 Hz
sessions burst; few at 400 Hz; none at 800 Hz), but the counts are higher because more sessions
are kept, and 2 of 9 sessions at 3 dB burst where the paper has none. Under peak reading (a) only
6/60 reference sessions burst, and with N the number of trials (b) none does.""",
# 5 isolated
"""**Result: partially reproduced.** Under the main reading the pooled percentage of isolated
spikes is 79.5, 77.7, 67.7, 78.1, 73.5, 95.0 and 100% against 74, 100, 62, 60, 55, 96 and 100%: 4
of 7 within tolerance (protocols 1, 3, 6, 7); 3 dB, 25 Hz and 100 Hz have fewer isolated spikes
than the paper at 3 dB and more at 25 and 100 Hz. No combination of readings brings more than 4
within tolerance. n = 1 is the most probable burst in every protocol under the main reading, as
the paper says.""",
# 6 burst length
"""**Result: not reproduced.** Under the main reading 7 of the 19 values are within tolerance
(highest n 7, 9, 8, 14, 7, 5, 1 against 9, 1, 8, 15, 9, 3, 1; average n 1.25, 1.30, 1.46, 1.85,
1.36, 1.05, 1.00 against 1.3, 1, 1.5, 2.1, 1.7, 1.04, 1), below the 10 the criterion needs for a
partial reproduction, and no combination of readings gives more than 7. The longest bursts are at
25 Hz (14 spikes) and 800 Hz has none, as in the paper, but 3 dB has bursts of up to 9 spikes in
its 2 bursting sessions.""",
# 7 fig5
"""**Result: reproduced.** Under the main reading the population average of P(n = 1) is lowest at
100 Hz among the cutoffs (0.755, against 0.806 at 25, 0.820 at 200, 0.982 at 400 and 1.000 at 800
Hz) and lowest at 12 dB among the SDs (0.686, against 0.820 at 6 and 0.957 at 3 dB), with all kept
sessions and with bursting sessions only. P(n = 2) and P(n = 3) are highest at 100 Hz and at 12 dB
over all kept sessions. With the bounding minimum read as the lowest value (b) the lowest P(n = 1)
moves to 25 Hz, where that reading gives very long bursts.""",
# 8 fig3
"""**Result: reproduced** (resting on the peak-counting threshold). In the cell recorded with all
seven protocols (03-04-23-ad to -aj) the first peak of C_s/rbar^2 rises above its baseline by 0.50
at 3 dB, 1.14 to 2.35 in the six 6 dB sessions and 5.06 at 12 dB, so it sharpens with SD under
reading (a); its width (b) does not order (0.4, 0.4 to 0.5, 0.3 ms). At 25 Hz C_s has 4 to 14
peaks, at 200 Hz one; at 100 Hz one peak at prominence 0.2 and two at 0.05 and 0.1. The 3 dB, 400
Hz and 800 Hz sessions have no separable first peak, as the paper names for Figures 3A, E and F.""",
# 9 corr error
"""**Result: reproduced** (resting on leaving tau = 0 out of the span). With sigma the SD of the
product terms and N their number (reading a), over the whole range of lags and without the
zero-lag self term, the error averages 2.69% (SD 1.37%) of the span of C_s, within 3.4 +/- 1.5%;
reading (c) gives 2.67%. With tau = 0 in the span every reading is below 0.2% or, with N the
number of trials, 6.5 to 7.9%; over 0 to 1.25 / cutoff without tau = 0 the values are unstable
(means 30 to 4000%).""",
# 10 fig6
"""**Result: reproduced.** Over the 84 bursting sessions the mean squared Pearson coefficient is
larger for spikes than for bursts in every session; the mean ratio is 1.99 (SD 0.85) with 0.1 ms
bins and 2.13 (SD 1.65) with 0.4 ms bins when tau = 0 is left out, within 2.89 +/- 1.49, and 1.31
and 1.21 when it is included (outside). All 84 bursting sessions have bursts of n > 1, so reading
(b) of the sessions is the same.""",
# 11 fig7ab
"""**Result: partially reproduced.** The information per burst rises with n: the mean slope is 2.14
bits (SD 0.85) with 0.1 ms bins and 1.85 (SD 0.73) with 0.4 ms bins in bits per event, and 1.71 and
1.48 for Eq. 10 as printed, all within 1.5 +/- 0.7; all 84 slopes are positive and 83 are
significant by both tests (the other session has only two n values, so no error for its slope).
The population is 84 bursting sessions, outside 59 +/- 5.9.""",
# 12 fig7cd
"""**Result: partially reproduced.** The log2 occurrence falls with n with a mean slope of -2.71
(SD 1.09), within -2.6 +/- 0.7 (natural log -1.88, log10 -0.82, outside); every slope is negative
and 83 of 84 are significant by reading (a), 81 by reading (b), so not every session, as the claim
states, but above 90%.""",
# 13 fig7ef
"""**Result: reproduced** (resting on how events are formed). With events read as onsets within the
first-peak domain around an event centre (b) the mean slope of jitter on n is 0.005 ms (SD 0.050),
within -0.03 +/- 0.2, and 87.7% of the 81 sessions with a test have a slope not significantly
different from 0 by the t-test, inside 80 +/- 8 (the bound is 88). With events between histogram
troughs (a) the slope is -0.001 ms but 91.6% are not significant (outside); with significance
read as one standard error, 43.4% and 34.6% (outside). The median jitter of 1-bursts is 0.389 ms
under (b) and 0.058 ms under (a).""",
# 14 fig7gh
"""**Result: not reproduced.** The information rate falls with n in all 84 sessions, but the mean
slope is -44.7 bits/s (SD 36.0) with 0.1 ms bins and -36.6 (SD 30.6) with 0.4 ms bins, outside -11
+/- 16, and bursts with n > 1 carry 36.3% and 38.6% of the information, outside 47 +/- 4.7. The
total rate averages 246.6 and 203.4 bits/s.""",
# 15 direct
"""**Result: partially reproduced.** With 0.4 ms bins for the burst code, over the 115 kept
sessions, R = 0.965, the direct method gives 204.3 bits/s (8 bins) and the burst code 183.6, a
mean difference of 20.7 bits/s, all within tolerance, and the burst code keeps 90% (10.1% lost,
outside 14 +/- 1.4). The direct method is higher in 94 of 115 sessions (82%), not in all but one.
Over the bursting sessions R = 0.950, 224.3 against 203.4 bits/s, difference 20.9, higher in 66 of
84. The extrapolated direct rate changes these by under 1 bit/s. With 0.1 ms bins the burst code
is above the direct method on average (227.3 against 204.3 bits/s).""",
# 16 fig8-nbta-differ
"""**Result: partially reproduced.** All 71 bursting sessions with at least two bursts of each n = 1
to 4 pass the frequency-domain ANOVA, with all frequency bins and with bins up to the cutoff. In
the time domain 60 of them have marked points in every central peak (a), outside 50 +/- 5, and 14
have most of every central peak marked (b). The 60 of 71 (85%) is the paper's proportion (50 of 58,
86%), but the bursting sessions number 84 (71 with n = 1 to 4), outside 58 +/- 5.8, because more
sessions are kept.""",
# 17 latency
"""**Result: reproduced.** The mean latency falls with n: 5.75, 4.13, 2.88 and -0.55 ms for n = 1 to
4 over 71 sessions (reading b); 43 of 71 sessions have tau_n decreasing from 1 to 4 (reading a),
all 71 have tau_4 < tau_1, and the Wilcoxon test of tau_1 against tau_4 gives p = 2.4e-13. A
negative tau_4 means the 4BTA reaches its maximum after the burst starts in some sessions.""",
# 18 fig8e
"""**Result: not reproduced.** The minimum of sigma_n lies near -6 ms for every n (medians -6.65,
-6.3, -5.0 and -6.25 ms), but the SD of its position across n = 1 to 4 averages 2.16 ms (SD 2.40)
in window (a) and 2.64 ms in window (b), outside 0.4 +/- 0.7, and 1.87 and 2.29 ms with the
population SD; times the cutoff it is 0.36 to 0.43, against 0.05.""",
# 19 sigma below
"""**Result: reproduced.** In 98.6% of the 71 sessions the minimum of sigma_n is below the minimum of
sigma for all n = 1 to 4 (reading a), within 98 +/- 9.8, and the ratio of the minima averages 1.604
(SD 0.278), within 1.62 +/- 0.56. Read as sigma_n below sigma at every tau (b), it holds in 1.4%.""",
# 20 fig9
"""**Result: reproduced** (resting on subtracting the mean stimulus before summing the 1BTAs). The
nBTA differs from the summed 1BTAs by the ANOVA in 100% of the sessions for n = 2, 3 and 4, with
paired (a) and grouped (b) observations, so the fraction does not grow with n; the share with more
than 70% of the interval significant falls from 94.0% (n = 2) to 86.7% and 54.9% (n = 4). With the
STA the ANOVA fractions are 100% (97.2% for n = 4 grouped) and the 70% share falls from 100% to
40.8%; with the average of the shifted copies in place of their sum the results are alike.""",
# 21 fig9c
"""**Result: reproduced.** Over the 10 bursting protocol-5 sessions (the paper has seven) the
population-average central peak is 3.22, 7.11 and 8.60 dB above the mean stimulus for n = 1, 2
and 3, and its width grows from 5.10 to 5.50 to 7.15 ms at half height (12.70, 13.50, 17.15 ms
between minima). The SD across sessions at the peak is 0.57, 0.74 and 1.28 dB.""",
# 22 fig10
"""**Result: not reproduced.** The h at which P(n | h) peaks increases from n = 0 to the largest n
(up to 4) in 8 of 84 bursting sessions (9.5%) under both widths T, and the P-weighted mean h
increases in 21 (25.0%), against all bursting cells. Restricted to n = 0 to 3, a variant outside
the criterion, the ordering holds in 44 and 48 of 84 sessions: the 4-bursts, which are few, most
often break it.""",
# 23 rate effect
"""**Result: reproduced** (reading b). No cell was recorded at two target rates (the headers hold 100
and 90 Hz only), so reading (a) cannot be formed. Across the kept sessions a 50 Hz higher rate goes
with a limiting ISI shorter by 0.189 ms (p = 0.488, 84 bursting sessions), below 0.44 ms, and an
average n higher by 13.6% (p = 0.0688), below 27.5%; within protocol 1 alone, -0.007 ms and
20.3%. These are differences between cells, not the within-cell change the paper may have
measured.""",
]
parts = s.split('**Result: ...**')
assert len(parts) == len(R) + 1, len(parts)
out = parts[0]
for r, rest in zip(R, parts[1:]):
    out += r.replace('\\\\', '\\') + rest
open(p,'w').write(out)
EOF
grep -c "Result:" $TMPDIR/make_nb.py
```

```
23
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import re
p='make_nb.py'; s=open(p).read()
s2,n=re.subn(r'md\("(\*\*Result:.*?)"\)\n', lambda m: 'md(r"""'+m.group(1)+'""")\n', s, flags=re.S)
print(n)
open(p,'w').write(s2)
EOF
. dev/bin/activate && python -c "import ast;ast.parse(open('$TMPDIR/make_nb.py').read())" && echo ok; date -u
```

```
22
ok
Wed Nov  4 18:48:02 UTC 2026
Shell cwd was reset to
```

**Agent**

Conclusions written. Now the summary section, then entry files.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='make_nb.py'; s=open(p).read()
i=s.index('md(r"""\n## model-reproduces-coding-trends (blocked)')
j=s.index('nb = nbf.v4.new_notebook()')
new='''md(r"""
## model-reproduces-coding-trends (blocked)

> The threshold-linear model with refractoriness reproduces the coding trends of the data, at
> single-cell and population level, though it is less precise in time than the real cells.

Depends on model-matches-classification, which is blocked (`data_missing`, no thresholds s_TH).
""")

md(r"""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| data-sessions-and-trials | partially reproduced |
| table1-sessions-per-protocol | not reproduced |
| firing-rate-uniform | reproduced |
| threshold-population | blocked: data missing |
| table1-bursting-sessions | not reproduced |
| table1-isolated-spikes | partially reproduced (assumed) |
| table1-burst-length | not reproduced |
| fig5-burst-probability-vs-stimulus | reproduced (assumed) |
| fig3-correlation-shape | reproduced (assumed) |
| method-correlation-error | reproduced (assumed) |
| model-matches-classification | blocked: data missing |
| fig6-bursts-less-correlated | reproduced (assumed) |
| fig7ab-information-per-burst-increases | partially reproduced (assumed) |
| fig7cd-occurrence-decreases | partially reproduced (assumed) |
| fig7ef-jitter-independent-of-n | reproduced (assumed) |
| fig7gh-information-rate | not reproduced (assumed) |
| direct-method-comparison | partially reproduced (assumed) |
| fig8-nbta-differ | partially reproduced (assumed) |
| fig8-latency-decreases | reproduced (assumed) |
| fig8e-sigma-minimum | not reproduced (assumed) |
| sigma-n-below-sta-sigma | reproduced (assumed) |
| fig9-nbta-not-concatenated-1bta | reproduced (assumed) |
| fig9c-population-nbta | reproduced (assumed) |
| fig10-burst-n-vs-height | not reproduced (assumed) |
| firing-rate-no-effect-on-limit | reproduced (assumed) |
| model-reproduces-coding-trends | blocked: data missing |

How the analysis differs from the paper's:

- Population. The paper keeps 86 of its 132 sessions by the rate SD (< 35 Hz) and a rate near
  100 Hz. In the data set that rule keeps 115 of the 116 sessions of the paper's seven protocols,
  so every population result here is over more sessions than the paper's (60 reference sessions
  against 43). The paper's other selection is not stated.
- Burst identification. The Methods leave open which maximum is the first peak, which minimum
  bounds it and what sigma and N are in the error bar. The first local maximum (peak reading a)
  falls on sampling fluctuations of the rising flank and leaves 15 of 115 sessions bursting; with
  N the number of trials the error bars are so wide that no session bursts. The main reading is
  the largest value below 5 ms, the first significant minimum after it, and N the number of product
  terms, under which the error bar is 2.7% of the span of C_s (the paper's 3.4%). Outcomes that
  rest on bursts are marked as resting on this choice.
- Thresholds. The data set holds no threshold s_TH, so the model of Eq. 2 and the claims on it
  are blocked.
- Smaller choices are stated in each section: the stimulus is the AM signal in dB from
  `stimtodB.m` with the intensity of `cell.dat`; f_n of Eq. 15 sums 1BTAs after subtracting the
  mean stimulus; peaks of C_s are counted with a prominence threshold.

What was found about the dataset:

- Data1 holds 150 sessions (75 experiments of two stimuli each) of 45 cells; 116 sessions from
  37 cells on 23 dates use the paper's seven protocols, the paper's 37 cells; 28 sessions use the
  `gaussModality` and `lmd` stimuli and 6 use cutoffs of 50 and 1600 Hz, which the paper does not
  mention. Nothing marks the 86 sessions the paper kept.
- Data1 records no animal, no threshold and no best frequency; `cell.dat` gives the intensity
  played. 28 sessions were sorted off-line and have no header.
- The intensity in three headers differs from `cell.dat` by more than 1 dB (up to 6.6 dB); the
  descriptor says 98 to 533 trials, the files hold 69 to 503; six sessions had pauses of 450 ms,
  not 700. Two experiments (03-01-15-aa, 03-06-27-ae) are missing from `singlecells.txt`.
- Spikes and stimuli share the trial clock: the STA peaks 5.6 ms (median) before the spike in
  every session and almost vanishes with the stimulus shifted by 100 ms.
""")

'''
s=s[:i]+new+s[j:]
open(p,'w').write(s)
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent**

Fixing a cell-count bug in `describe` (unlisted experiments were counted per session), then writing the entry files.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='make_nb.py'; s=open(p).read()
old='''    return dict(population=label, cells=d.cell.nunique() + (d.cell == -1).sum() - (1 if (d.cell == -1).any() else 0),'''
new='''    # cells: rows of singlecells.txt, plus each experiment it does not list
    return dict(population=label, cells=d.cell[d.cell >= 0].nunique() + d.exp[d.cell < 0].nunique(),'''
assert old in s
s=s.replace(old,new); open(p,'w').write(s)
EOF
cd entries/crcns-ia-1-eyherabide-2008
cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-ia-1-eyherabide-2008
type: reproduction
title: Burst coding in locust auditory receptors (Eyherabide et al. 2008)
description: Tests the findings of Eyherabide, Rokem, Herz and Samengo (2008) on CRCNS data set ia-1,
  which holds the spike times of locust auditory receptor cells under amplitude-modulated noise
  (Data1) and the stimuli. It identifies bursts from the spike-train correlation function, counts
  them per stimulus protocol, computes the information carried by bursts of each size and by the
  direct method, and the burst-triggered averages of the stimulus. The cells' thresholds, which
  the paper's model needs, are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_eyherabide_2008.ipynb
  title: Reproducing Eyherabide et al. (2008) from CRCNS ia-1
  runtime_minutes: 5
helpers:
- ia1.py
related:
- id: crcns:ia-1/unversioned
  relation: uses_data
- id: doi:10.3389/neuro.10.003.2008
  relation: reproduces
EOF
cat ../001453-fouke-2025/entry.yaml | head -3; python3 -c "import json;print(json.dumps(json.load(open('schemas/entry.schema.json'))['properties'].get('related'),indent=0)[:800])"
```

```
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
"relation": {
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && . $TMPDIR/dev/bin/activate && python $TMPDIR/make_nb.py && uv pip install -q pyyaml jsonschema 2>/dev/null; python tools/entry.py lock entries/crcns-ia-1-eyherabide-2008 2>&1 | tail -5; python tools/entry.py check entries/crcns-ia-1-eyherabide-2008 2>&1 | tail -20
```

```
wrote entries/crcns-ia-1-eyherabide-2008/requirements.lock.txt
0 error(s)
```

**Agent**

Check passes. Running the entry from a clean environment.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time python tools/entry.py all entries/crcns-ia-1-eyherabide-2008 2>&1 | tail -15; ls executed/crcns-ia-1-eyherabide-2008/
```

```
Installed kernelspec registry-crcns-ia-1-eyherabide-2008 in executed/crcns-ia-1-eyherabide-2008/.venv/share/jupyter/kernels/registry-crcns-ia-1-eyherabide-2008
0 error(s)
pass  reproduce_eyherabide_2008.ipynb  (250 s)

real	4m18.842s
user	3m11.093s
sys	0m34.466s
reproduce_eyherabide_2008.ipynb
result.json
```

**Agent calls Bash**

```bash
python3 -c "
import nbformat
nb=nbformat.read('executed/crcns-ia-1-eyherabide-2008/reproduce_eyherabide_2008.ipynb',4)
for i,c in enumerate(nb.cells):
  t=c.metadata.get('tags',[])
  if c.cell_type!='code': continue
  for o in c.outputs:
    if o.output_type=='stream' and o.name=='stderr': print('STDERR',i,o.text[:300])
    if o.output_type=='error': print('ERR',i)
  if 'claim:data-sessions-and-trials' in t or i in (3,):
    for o in c.outputs:
      if o.output_type=='stream': print(o.text[:1500])
"; git status --short
```

```
Data1 experiments: 75  sessions: 150  offline-sorted sessions (no OEL header): 28
experiments not listed in singlecells.txt: ['03-01-15-aa', '03-06-27-ae']
cells (rows of singlecells.txt, plus experiments not listed): 45  recording dates: 25

Sessions by stimulus file (cell.dat):
                     sessions  protocol
stimulus                               
gaussModality_co200        14       NaN
gauss_st12_co200            8       3.0
gauss_st3_co200             9       2.0
gauss_st6_co100            11       5.0
gauss_st6_co200            54       1.0
gauss_st6_co25              9       4.0
gauss_st6_co400             8       6.0
gauss_st6_co800             9       7.0
lmd_co200                  14       NaN
st6_co1600                  3       NaN
st6_co200                   7       1.0
st6_co25                    1       4.0
st6_co50                    3       NaN
[... 40 more lines not kept]
```

**Agent**

The run passes in 250 s. Checking that the executed copy's numbers match those my conclusions quote (from the earlier dev run).

**Agent calls Bash**

```bash
python3 -c "
import nbformat
a=nbformat.read('executed/crcns-ia-1-eyherabide-2008/reproduce_eyherabide_2008.ipynb',4)
b=nbformat.read('$TMPDIR/out.ipynb',4)
ta={str(c.metadata.get('tags')):''.join(o.get('text','') for o in c.outputs) for c in a.cells if c.cell_type=='code'}
tb={str(c.metadata.get('tags')):''.join(o.get('text','') for o in c.outputs) for c in b.cells if c.cell_type=='code'}
for k in ta:
  if k in tb and ta[k]!=tb[k]: print('DIFF',k)
"
```

```
DIFF ['claim:data-sessions-and-trials']
DIFF ['claim:fig10-burst-n-vs-height']
```

**Agent calls Bash**

```bash
python3 -c "
import nbformat
a=nbformat.read('executed/crcns-ia-1-eyherabide-2008/reproduce_eyherabide_2008.ipynb',4)
for c in a.cells:
  if 'claim:fig10-burst-n-vs-height' in c.metadata.get('tags',[]):
    for o in c.outputs:
      if o.output_type=='stream': print('\n'.join(l for l in o.text.splitlines() if not l.startswith('03-')))
"
```

```
/tmp/claude-1001/ipykernel_39/3011379996.py:51: RuntimeWarning: invalid value encountered in scalar divide
  mean_h = [np.nansum(centres * p) / np.nansum(p) for p in Pm]
T (a): median T 7.40 ms; sessions 84; segregation (a) peak h increasing: 8 (9.5%); (b) mean h increasing: 21 (25.0%); variant n = 0 to 3 only: (a) 44, (b) 48; maxima matched to a burst, median 8316
T (b): median T 3.05 ms; sessions 84; segregation (a) peak h increasing: 8 (9.5%); (b) mean h increasing: 21 (25.0%); variant n = 0 to 3 only: (a) 44, (b) 48; maxima matched to a burst, median 8174
sessions where the two T readings match a different number of maxima: 75 of 84
         session T  T_ms  nmax  matched                         peak_h                         mean_h     a     b    a3    b3
```

**Agent**

Only a temp path in a warning differs; the numbers match. Writing the attempt record now.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/make_attempt.py <<'EOF'
import yaml

NB = "reproduce_eyherabide_2008.ipynb"
BURST_ASSUMPTION = ("Burst identification takes the first peak as the largest value of C_s below 5 ms (peak reading b), "
    "the first local minimum after it that differs significantly from it (minimum reading a), and the error bar with sigma "
    "the SD of the product terms of Eq. 1 and N their number (reading a). Assumed because the first local maximum (reading a) "
    "falls on sampling fluctuations of the rising flank, which the Methods say the criteria reject (Burst identification, "
    "paragraph 5), and leaves 15 of 115 sessions bursting; with N the number of trials no session bursts; the main reading "
    "gives an error bar of 2.7% of the span of C_s, near the paper's 3.4% (paragraph 6). The notebook shows every combination.")
SELECTION = ("The kept sessions are the 115 of the 116 seven-protocol sessions with a trial-to-trial rate SD below 35 Hz "
    "(reading a of data-sessions-and-trials), not the paper's 86, whose selection is not stated.")


def oc(claim, outcome, notes, deviations=None, measured=None, assumed=None, blocked_by=None, output=True):
    d = dict(claim=claim, outcome=outcome)
    if blocked_by:
        d["blocked_by"] = blocked_by
    if assumed:
        d["assumed"] = True
    if output:
        d["notebook"] = NB
        d["output"] = f"claim:{claim}"
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    if deviations:
        d["deviations"] = deviations
    return d


outcomes = [
    oc("data-sessions-and-trials", "partially_reproduced",
       "The 116 sessions of the seven protocols come from 37 cells (rows of singlecells.txt) recorded on 23 dates; "
       "the 122 Gaussian AM sessions of any cutoff are within 10% of the paper's 132 (all 150 Data1 sessions are not). "
       "The SD < 35 Hz condition keeps 115 of the 116 (113 with a 100 Hz target, reading b; 116 with whole-trial rates), "
       "against 86. Over the 115 kept sessions trials range from 69 (outside 98 +/- 9.8) to 503 and average 160.3, and the "
       "mean trial-to-trial SD of the rate is 6.48 Hz (within 6 +/- 0.6). The kept count and the fewest trials are outside "
       "tolerance under every reading, the other values within.",
       deviations=["Data1 does not record the animal; the 23 recording dates stand in for the 23 animals, assuming one animal per date.",
                   "Sessions recorded are read as the 122 Gaussian AM sessions; the paper's 132 is not otherwise identifiable."],
       measured=[37, 23, 122, 115, 69, 503, 160.3, 6.48], assumed=True),
    oc("table1-sessions-per-protocol", "not_reproduced",
       "Kept sessions per protocol are 60, 9, 8, 10, 11, 8 and 9 (reading a, 200 to 1000 ms) against 43, 6, 7, 7, 8, 7 and 8; "
       "none within 10% under any reading. The data set holds 55 experiments pairing the reference with each other protocol "
       "(8 to 11 per protocol) and 6 more reference sessions paired with 50 or 1600 Hz stimuli.",
       measured=[60, 9, 8, 10, 11, 8, 9]),
    oc("firing-rate-uniform", "reproduced",
       "Over the 115 kept sessions the mean rate is 110.2 Hz (SD 16.7 Hz); one-way ANOVA across the seven protocols F = 0.49, "
       "p = 0.818. With whole-trial rates 114.7 Hz (SD 16.9), p = 0.471; over all seven-protocol sessions p = 0.809.",
       deviations=[SELECTION], measured=[110.2, 16.7]),
    oc("threshold-population", "blocked",
       "Data1 holds spike times, cell.dat (stimulus names, played intensities, cutoffs, same-cell links) and the stimulus "
       "files; no threshold, best-frequency or tuning measurement. The data descriptor says the best frequency was determined "
       "from f-I curves but does not deposit them for Data1.", blocked_by="data_missing"),
    oc("table1-bursting-sessions", "not_reproduced",
       "Under the main reading the kept sessions with bursts of n > 1 are 52/60, 2/9, 8/8, 9/10, 10/11, 3/8 and 0/9 against "
       "40/43, 0/6, 7/7, 6/7, 7/8, 3/7 and 0/8; 2 of 7 counts within tolerance, and no combination of readings (12) or kept "
       "reading does better. The fractions follow the paper's pattern except at 3 dB, where 2 of 9 sessions burst.",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=[52, 2, 8, 9, 10, 3, 0]),
    oc("table1-isolated-spikes", "partially_reproduced",
       "Under the main reading the pooled percentages of isolated spikes are 79.5, 77.7, 67.7, 78.1, 73.5, 95.0 and 100%; "
       "4 of 7 within tolerance (protocols 1, 3, 6, 7) and at most 4 under any combination. n = 1 is the most probable n in "
       "every protocol under the main reading. The averages over sessions are alike (79.2 to 100%).",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=[79.5, 77.7, 67.7, 78.1, 73.5, 95.0, 100.0], assumed=True),
    oc("table1-burst-length", "not_reproduced",
       "Under the main reading highest n 7, 9, 8, 14, 7, 5, 1, average n 1.25, 1.30, 1.46, 1.85, 1.36, 1.05, 1.00, SD of n "
       "0.54 (p1), 0.80 (p3), 2.12 (p4), 0.69 (p5), 0.23 (p6); 7 of 19 within tolerance, at most 7 under any combination. "
       "The longest bursts are at 25 Hz and 800 Hz has none, as in the paper; 3 dB has bursts of up to 9 spikes.",
       deviations=[SELECTION, BURST_ASSUMPTION],
       measured=[7, 9, 8, 14, 7, 5, 1, 1.25, 1.3, 1.46, 1.85, 1.36, 1.05, 1.0, 0.54, 0.8, 2.12, 0.69, 0.23]),
    oc("fig5-burst-probability-vs-stimulus", "reproduced",
       "Under the main reading, over all kept sessions, P(n = 1) is 0.806, 0.755, 0.820, 0.982 and 1.000 at 25, 100, 200, 400 "
       "and 800 Hz, lowest at 100 Hz, and 0.957, 0.820 and 0.686 at 3, 6 and 12 dB, lowest at 12 dB; the same with bursting "
       "sessions only. P(n = 2) and P(n = 3) are highest at 100 Hz and 12 dB over all kept sessions. With minimum reading b the "
       "lowest P(n = 1) moves to 25 Hz.",
       deviations=[SELECTION, BURST_ASSUMPTION], assumed=True),
    oc("fig3-correlation-shape", "reproduced",
       "The cell 03-04-23-ad to -aj of singlecells.txt was recorded with all seven protocols (six reference sessions). The "
       "first peak of C_s/rbar^2 above its baseline is 0.50 at 3 dB, 1.14 to 2.35 in the six 6 dB sessions and 5.06 at 12 dB "
       "(reading a, sharper with SD); its width does not order (reading b). C_s has 4 to 14 peaks at 25 Hz, one at 200 Hz, and "
       "one at 100 Hz at prominence 0.2 (two at 0.05 and 0.1); 3 dB, 400 and 800 Hz have no separable first peak. The model "
       "panels of Figure 3 are not tested (no thresholds).",
       deviations=["The cell is identified from singlecells.txt as the only one with all seven protocols; the paper does not name it.",
                   "Peaks are counted on C_s/rbar^2 smoothed over 1 ms as local maxima with a prominence above a threshold the paper does "
                   "not give; 0.05, 0.1 and 0.2 are shown and the outcome rests on 0.2 for the single peak at 100 Hz.",
                   BURST_ASSUMPTION], assumed=True),
    oc("method-correlation-error", "reproduced",
       "With sigma the SD of the product terms and N their number (reading a), over the whole lag range (reading b) and without "
       "tau = 0, the error averages 2.69% (SD 1.37%) of the span of C_s over the 115 kept sessions; reading c gives 2.67%. With "
       "tau = 0 in the span all readings give 0.06 to 0.16% or, with N the number of trials, 6.5 to 7.9%; over 0 to 1.25 / cutoff "
       "without tau = 0 the mean is unstable (30 to 4000%).",
       deviations=["The span of C_s leaves out tau = 0, where C_s holds the self term (two orders of magnitude above the rest); the "
                   "paper does not say. Assumed because the claims file's own detail (1) excludes the zero-lag self term from the peak.",
                   "A third reading of sigma and N (sigma the SD over trials of each trial's C_s, N the number of trials), from "
                   "paragraph 6 (\"C_s can be interpreted as an average\"), is shown beside the claims file's two."],
       measured=2.69, assumed=True),
    oc("model-matches-classification", "blocked",
       "The model thresholds the stimulus at the measured threshold s_TH before filtering (Eq. 2); the criterion makes the "
       "claim untestable as the paper ran it without s_TH, and Data1 holds none.", blocked_by="data_missing", output=False),
    oc("fig6-bursts-less-correlated", "reproduced",
       "Over the 84 bursting sessions the mean square Pearson coefficient is larger for spikes than for bursts in every session. "
       "Without tau = 0 the mean ratio is 1.99 (SD 0.85) with 0.1 ms bins and 2.13 (SD 1.65) with 0.4 ms bins, within "
       "2.89 +/- 1.49; with tau = 0, 1.31 and 1.21, outside. All 84 have bursts of n > 1.",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=1.99, assumed=True),
    oc("fig7ab-information-per-burst-increases", "partially_reproduced",
       "Mean slope of I_n(1) on n 2.14 bits (SD 0.85) with 0.1 ms bins and 1.85 (SD 0.73) with 0.4 ms bins in bits per event "
       "(reading i), 1.71 and 1.48 as Eq. 10 prints it (reading ii), all within 1.5 +/- 0.7. All 84 slopes are positive and 83 "
       "significant by both tests; the other session has only two n values. The bursting sessions number 84, outside 59 +/- 5.9.",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=[2.14, 84], assumed=True),
    oc("fig7cd-occurrence-decreases", "partially_reproduced",
       "Mean slope of log2 occurrence on n -2.71 (SD 1.09), within -2.6 +/- 0.7 (natural log -1.88, log10 -0.82). All 84 slopes "
       "are negative; 83 are significant by one standard error and 81 by the t-test, so not every session, but above 90%.",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=-2.71, assumed=True),
    oc("fig7ef-jitter-independent-of-n", "reproduced",
       "Events read as onsets within the first-peak domain around an event centre (reading b) give a mean slope of 0.005 ms "
       "(SD 0.050) and 87.7% of the 81 sessions with a test not significant by the two-sided t-test, within 80 +/- 8 (bound 88). "
       "Events between histogram troughs (reading a) give -0.001 ms and 91.6%; with significance read as one standard error "
       "43.4% and 34.6%. Median jitter of 1-bursts 0.389 ms (b) and 0.058 ms (a). Three sessions have fewer than three n values "
       "with a jitter and no test.",
       deviations=["How events are formed is open (Rokem et al., 2006 is cited for the definition). Reading b is implemented with "
                   "event centres taken as the 0.1 ms onset-histogram bins from the highest down and a window of the limiting ISI "
                   "centred on each; reading a fragments events (median jitter 0.058 ms, below the paper's 0.2 ms error bar).",
                   SELECTION, BURST_ASSUMPTION], measured=[87.7, 0.005], assumed=True),
    oc("fig7gh-information-rate", "not_reproduced",
       "The information rate falls with n in all 84 sessions; mean slope -44.7 bits/s (SD 36.0) with 0.1 ms bins and -36.6 "
       "(SD 30.6) with 0.4 ms bins, outside -11 +/- 16; bursts with n > 1 carry 36.3% and 38.6%, outside 47 +/- 4.7. Total "
       "rates average 246.6 and 203.4 bits/s.",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=[-44.7, 36.3], assumed=True),
    oc("direct-method-comparison", "partially_reproduced",
       "With the burst code in 0.4 ms bins over the 115 kept sessions, R = 0.965, direct (8 bins) 204.3 bits/s, burst code "
       "183.6, mean difference 20.7 (SD 21.4), all within tolerance; 10.1% lost, outside 14 +/- 1.4; the direct method is higher "
       "in 94 of 115 (82%), not all but one. Over the bursting sessions R = 0.950, 224.3 against 203.4, difference 20.9, higher "
       "in 66 of 84. Extrapolated direct rates differ by under 1 bit/s. With 0.1 ms bins the burst code exceeds the direct "
       "method on average (227.3 against 204.3).",
       deviations=["NSB entropies computed by this entry's implementation (ia1.nsb_entropy), not the authors' code, which is not public.",
                   SELECTION, BURST_ASSUMPTION], measured=[0.965, 204.3, 183.6, 20.7, 10.1], assumed=True),
    oc("fig8-nbta-differ", "partially_reproduced",
       "All 71 bursting sessions with at least two bursts of each n = 1 to 4 pass the ANOVA, with all frequency bins and with "
       "bins up to the cutoff. 60 have marked points in every central peak (reading a), outside 50 +/- 5, and 14 have most of "
       "every central peak marked (reading b). 60 of 71 (85%) matches the paper's 50 of 58 (86%); the bursting sessions number "
       "84, outside 58 +/- 5.8.",
       deviations=["The central peak runs between the minima flanking the nBTA's maximum over -25 to +15 ms, as the Methods define it "
                   "for Figure 9; the paper does not define it for Figure 8.", "Sessions need at least two bursts of each n = 1 to 4 "
                   "for the variances of the tests (detail 4 reading b).", SELECTION, BURST_ASSUMPTION],
       measured=[60, 84], assumed=True),
    oc("fig8-latency-decreases", "reproduced",
       "Mean tau_n 5.75, 4.13, 2.88 and -0.55 ms for n = 1 to 4 over 71 sessions (reading b); 43 of 71 sessions decrease from "
       "n = 1 to 4 (reading a); all 71 have tau_4 < tau_1 (Wilcoxon p = 2.4e-13).",
       deviations=[SELECTION, BURST_ASSUMPTION], assumed=True),
    oc("fig8e-sigma-minimum", "not_reproduced",
       "The minimum of sigma_n lies near -6 ms for every n (medians -6.65, -6.3, -5.0, -6.25 ms) but the SD of its position "
       "across n = 1 to 4 averages 2.16 ms (SD 2.40) in window a and 2.64 ms in window b (1.87 and 2.29 ms with the population "
       "SD), outside 0.4 +/- 0.7; times the cutoff 0.36 to 0.43, against 0.05.",
       deviations=["The SD across n is the sample SD (N - 1, MATLAB's default); the population SD is shown too.",
                   SELECTION, BURST_ASSUMPTION], measured=[2.16, 0.364], assumed=True),
    oc("sigma-n-below-sta-sigma", "reproduced",
       "In 98.6% of 71 sessions the minimum of sigma_n is below that of sigma for all n = 1 to 4 (reading a); the ratio of minima "
       "averages 1.604 (SD 0.278). At every tau (reading b) 1.4%.",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=[98.6, 1.604], assumed=True),
    oc("fig9-nbta-not-concatenated-1bta", "reproduced",
       "The ANOVA finds the nBTA different from the summed 1BTAs in 100% of sessions for n = 2, 3 and 4 (84, 83 and 71 sessions), "
       "paired and grouped, so the fraction does not grow; the share with over 70% of the interval significant falls from 94.0% "
       "to 86.7% and 54.9%. With the STA the ANOVA fractions are 97.2 to 100% and the 70% share falls from 100% to 40.8%. The "
       "average of the shifted copies gives the same picture. The model sessions are not tested.",
       deviations=["Eq. 15 sums 1BTAs of the stimulus in dB; the sum is taken after subtracting the session's mean stimulus, as the "
                   "paper does for Figure 9C, since a sum of n absolute levels cannot compare with an nBTA. The average of the "
                   "shifted copies is shown as a variant.",
                   "The paired ANOVA (reading a) tests the mean difference between each burst's segment and its own f_n and its "
                   "variation across frequency bins.", SELECTION, BURST_ASSUMPTION], assumed=True),
    oc("fig9c-population-nbta", "reproduced",
       "Over the 10 bursting protocol-5 sessions the population-average central peak is 3.22, 7.11 and 8.60 dB above the mean "
       "stimulus for n = 1, 2, 3, with half-height widths 5.10, 5.50 and 7.15 ms (12.70, 13.50, 17.15 ms between minima) and "
       "SD across sessions 0.57, 0.74 and 1.28 dB at the peak.",
       deviations=["10 protocol-5 sessions, where the paper has seven cells.", BURST_ASSUMPTION], assumed=True),
    oc("fig10-burst-n-vs-height", "not_reproduced",
       "The h at which P(n | h) peaks increases from n = 0 to the largest n (up to 4) in 8 of 84 bursting sessions (9.5%) and the "
       "P-weighted mean h in 21 (25.0%), under both widths T (median 7.40 and 3.05 ms), against all bursting cells. Restricted "
       "to n = 0 to 3 (outside the criterion) 44 and 48 of 84 hold.",
       deviations=["A stimulus maximum whose closest burst was assigned to a nearer maximum counts as no response; the Methods do "
                   "not say whether it is matched to another burst.", SELECTION, BURST_ASSUMPTION], measured=[9.5, 25.0], assumed=True),
    oc("firing-rate-no-effect-on-limit", "reproduced",
       "No cell was recorded at two target rates (headers hold 100 and 90 Hz), so reading a cannot be formed. Under reading b a "
       "50 Hz higher rate goes with a limiting ISI shorter by 0.189 ms (p = 0.488, 84 sessions) and an average n higher by 13.6% "
       "(p = 0.0688, 115 sessions); within protocol 1, 0.007 ms and 20.3%. These are differences between cells.",
       deviations=[SELECTION, BURST_ASSUMPTION], measured=[0.189, 13.6], assumed=True),
    oc("model-reproduces-coding-trends", "blocked",
       "Depends on model-matches-classification, blocked because Data1 holds no thresholds s_TH.",
       blocked_by="data_missing", output=False),
]

findings = [
    dict(kind="selection_undocumented", statement=(
        "The paper keeps 86 of 132 sessions by a trial-to-trial rate SD below 35 Hz and a rate near 100 Hz. In Data1 the SD "
        "rule keeps 115 of the 116 sessions of the paper's seven protocols (and all 116 with whole-trial rates), and nothing "
        "marks which sessions the paper kept; Table 1 counts 43 reference sessions where Data1 has 60 kept.")),
    dict(kind="data_missing", statement=(
        "Data1 holds no threshold, best frequency or f-I measurement for its cells, though the paper's model (Eq. 2) uses the "
        "measured threshold s_TH and the descriptor says the best frequency was determined from f-I curves.")),
    dict(kind="identifier_missing", statement=(
        "Data1 does not record the animal; the paper's 23 animals can only be matched to the 23 recording dates of the "
        "seven-protocol sessions by assuming one animal per date. Two experiments (03-01-15-aa, 03-06-27-ae) are missing "
        "from singlecells.txt.")),
    dict(kind="metadata_insufficient", statement=(
        "28 sessions use the stimuli gaussModality_co200 and lmd_co200 and 6 use cutoffs of 50 and 1600 Hz; the descriptor "
        "does not describe these stimuli and the paper does not use them. 28 sessions sorted off-line have no header, so their "
        "target rate and pause are not recorded.")),
    dict(kind="metadata_error", statement=(
        "The descriptor says the 1 s trials number 98 to 533; the files hold 69 to 503. The intensity in three trial headers "
        "differs from cell.dat by more than 1 dB (03-04-11-aa sig2, 03-04-16-ae sig2, 03-04-23-ae sig1, up to 6.6 dB), and "
        "six sessions of 03-01-30-ad, 03-02-25-ac and 03-02-25-aj had 450 ms pauses where the paper states 700 ms.")),
    dict(kind="methods_unavailable", statement=(
        "Questions for the paper's authors. (1) Burst identification; which maximum is the first peak of C_s (the first local "
        "maximum falls on fluctuations of the rising flank and leaves 15 of 115 sessions bursting, the largest value below 5 ms "
        "84), and what sigma and N are in Delta = sigma / sqrt(N) (the product terms and their number give 2.7% of the span "
        "when tau = 0 is left out of the span; N the number of trials gives no bursting session). (2) Which rule, besides the "
        "rate SD, removed the sessions not among the 86. (3) How events were formed for the jitter (Rokem et al., 2006). (4) "
        "Whether the mean stimulus was subtracted before summing 1BTAs in Eq. 15. (5) What separates a peak of C_s for the "
        "multi-modal and single-peaked shapes of Figure 3.")),
    dict(kind="paper_inconsistency", statement=(
        "The paper counts bursting sessions three ways, 63 with n > 1 in Table 1, 59 bursting cells for Figure 7B and 58 "
        "bursting sessions for Figure 8, without saying why.")),
]

attempt = dict(
    schema_version=2, id="crcns-ia-1-eyherabide-2008-01",
    dataset=dict(archive="crcns", id="ia-1", version="unversioned", doi="10.6080/K0BG2KWB"),
    paper="doi:10.3389/neuro.10.003.2008", date="2026-11-04", entry="crcns-ia-1-eyherabide-2008",
    provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
                    agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-13"),
                    runner=dict(platform="GitHub Actions", url="https://github.com/catalystneuro/encore/actions/runs/41885596452")),
    outcomes=outcomes, findings=findings)
with open("attempts/crcns-ia-1-eyherabide-2008-01.yaml", "w") as f:
    yaml.safe_dump(attempt, f, sort_keys=False, width=100, allow_unicode=True)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/make_attempt.py && grep -n ": " attempts/crcns-ia-1-eyherabide-2008-01.yaml | grep -v "^[0-9]*: *-\? *[a-z_]*: " | head; python tools/entry.py check entries/crcns-ia-1-eyherabide-2008
```

```
0 error(s)
```

**Agent**

Check passes. Correcting two misquoted numbers (fig7ab: 82 sessions significant by the t-test, not 83; isolated-spike session averages range 68.6 to 100%), then scanning for banned words.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/all 84 slopes are positive and 83 are\nsignificant/X/' make_nb.py && python3 - <<'EOF'
for p, pairs in {'/tmp/claude-1001/make_nb.py': [("all 84 slopes are positive and 83 are\nsignificant by both tests (the other session has only two n values, so no error for its slope).",
 "all 84 slopes are positive, 83 are\nsignificant by one standard error and 82 by the t-test (one session has only two n values, so no\nerror for its slope).")],
 '/tmp/claude-1001/make_attempt.py': [("All 84 slopes are positive and 83 \"\n       \"significant by both tests; the other session has only two n values.",
 "All 84 slopes are positive, 83 \"\n       \"significant by one standard error and 82 by the t-test; one session has only two n values."),
 ("The averages over sessions are alike (79.2 to 100%).", "The averages over sessions are alike (68.6 to 100%).")]}.items():
    s = open(p).read()
    for a, b in pairs:
        assert a in s, a[:40]
        s = s.replace(a, b)
    open(p, 'w').write(s)
EOF
grep -n "—\|rather\|genuinely\|actually\|worth noting" make_nb.py make_attempt.py entries/crcns-ia-1-eyherabide-2008/ia1.py | head
```

```
Shell cwd was reset to
```

**Agent**

Now the entry README, then the final lock, run and handover.

**Agent calls Bash**

```bash
cat > entries/crcns-ia-1-eyherabide-2008/README.md <<'EOF'
# Eyherabide, Rokem, Herz & Samengo (2008) from CRCNS ia-1

Tests the findings of [Eyherabide et al. (2008)](https://doi.org/10.3389/neuro.10.003.2008) that can
be tested on [CRCNS ia-1](https://doi.org/10.6080/K0BG2KWB), which holds the spike times of locust
auditory receptor cells driven by amplitude-modulated noise (Data1, the paper's data) and the
stimulus files. The cells' thresholds, which the paper's model needs, are not in the data set.

| Claim | Outcome |
|---|---|
| Cells, sessions and trials of the recordings | Partially reproduced |
| Kept sessions per stimulus protocol (Table 1) | Not reproduced |
| Firing rate 113 Hz, not different across protocols | Reproduced |
| Mean threshold 58 dB | Blocked: data missing |
| Bursting sessions per protocol (Table 1) | Not reproduced |
| Percentage of isolated spikes per protocol (Table 1) | Partially reproduced |
| Highest and average n per protocol (Table 1) | Not reproduced |
| Isolated spikes least likely at 12 dB and 100 Hz (Figure 5) | Reproduced |
| Shape of the correlation function across stimuli (Figure 3) | Reproduced |
| Error of the correlation function, 3.4% of its span | Reproduced |
| The model classifies sessions as the data do | Blocked: data missing |
| Bursts are less correlated than spikes (Figure 6) | Reproduced |
| Information per burst rises with n (Figure 7A, B) | Partially reproduced |
| Occurrence falls with n (Figure 7C, D) | Partially reproduced |
| Jitter does not depend on n (Figure 7E, F) | Reproduced |
| Information rate falls with n; n > 1 carry 47% (Figure 7G, H) | Not reproduced |
| Burst code against the direct method | Partially reproduced |
| Burst-triggered averages differ with n (Figure 8D) | Partially reproduced |
| Latency falls with n (Figure 8D) | Reproduced |
| Minimum of sigma_n at the same place for all n (Figure 8E) | Not reproduced |
| sigma_n below the SD of the stimuli before all spikes | Reproduced |
| nBTA differs from summed 1BTAs (Figure 9A, B) | Reproduced |
| Population nBTAs at 100 Hz (Figure 9C) | Reproduced |
| Burst size depends on the height of the stimulus maximum (Figure 10) | Not reproduced |
| Firing rate barely changes the limiting ISI | Reproduced |
| The model reproduces the coding trends | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's selection rule keeps 115 sessions in the data set where the paper kept 86, so the
counts of sessions differ from the paper's; and the Methods leave open details of burst
identification, for which the notebook shows every reading. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/crcns-ia-1-eyherabide-2008-01.yaml`](../../attempts/crcns-ia-1-eyherabide-2008-01.yaml).

- `reproduce_eyherabide_2008.ipynb`: the analysis. It takes about five minutes.
- `ia1.py`: streaming the zip from the CRCNS bucket, parsing spike and stimulus files, burst
  identification, information measures, the direct method with NSB entropies, and
  burst-triggered averages. Other notebooks on this data set can import it.
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/make_nb.py && python $TMPDIR/make_attempt.py && date -u && python tools/entry.py lock entries/crcns-ia-1-eyherabide-2008 | tail -1 && python tools/entry.py all entries/crcns-ia-1-eyherabide-2008 2>&1 | tail -3
```

```
Wed Nov  4 18:55:12 UTC 2026
wrote entries/crcns-ia-1-eyherabide-2008/requirements.lock.txt
Installed kernelspec registry-crcns-ia-1-eyherabide-2008 in executed/crcns-ia-1-eyherabide-2008/.venv/share/jupyter/kernels/registry-crcns-ia-1-eyherabide-2008
0 error(s)
pass  reproduce_eyherabide_2008.ipynb  (248 s)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python3 -c "
import nbformat
a=nbformat.read('executed/crcns-ia-1-eyherabide-2008/reproduce_eyherabide_2008.ipynb',4)
b=nbformat.read('$TMPDIR/out.ipynb',4)
ta={str(c.metadata.get('tags')):''.join(o.get('text','') for o in c.outputs if o.get('name')!='stderr') for c in a.cells if c.cell_type=='code'}
tb={str(c.metadata.get('tags')):''.join(o.get('text','') for o in c.outputs if o.get('name')!='stderr') for c in b.cells if c.cell_type=='code'}
print([k for k in ta if k in tb and ta[k]!=tb[k]])
" && python tools/entry.py handover entries/crcns-ia-1-eyherabide-2008 2>&1 | tail -3; ls executed/crcns-ia-1-eyherabide-2008/handover; git status --short | grep -v "^?? \.\|scripts"
```

```
["['claim:data-sessions-and-trials']"]
wrote executed/crcns-ia-1-eyherabide-2008/handover
10.3389-neuro.10.003.2008.yaml
ia1.py
reproduce_eyherabide_2008.ipynb
?? attempts/crcns-ia-1-eyherabide-2008-01.yaml
?? entries/crcns-ia-1-eyherabide-2008/
```

**Agent**

I've done steps 1 to 6 of the Author section for CRCNS ia-1 and run the handover. The entry passes `check` and runs clean in 248 s; nothing is committed. Files written: `entries/crcns-ia-1-eyherabide-2008/` (notebook, `ia1.py`, `entry.yaml`, `README.md`, lock files) and `attempts/crcns-ia-1-eyherabide-2008-01.yaml`. The verifier's package is in `executed/crcns-ia-1-eyherabide-2008/handover/`.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| data-sessions-and-trials | partially reproduced (assumed) |
| table1-sessions-per-protocol | not reproduced |
| firing-rate-uniform | reproduced |
| threshold-population | blocked: data_missing |
| table1-bursting-sessions | not reproduced |
| table1-isolated-spikes | partially reproduced (assumed) |
| table1-burst-length | not reproduced |
| fig5-burst-probability-vs-stimulus | reproduced (assumed) |
| fig3-correlation-shape | reproduced (assumed) |
| method-correlation-error | reproduced (assumed) |
| model-matches-classification | blocked: data_missing |
| fig6-bursts-less-correlated | reproduced (assumed) |
| fig7ab-information-per-burst-increases | partially reproduced (assumed) |
| fig7cd-occurrence-decreases | partially reproduced (assumed) |
| fig7ef-jitter-independent-of-n | reproduced (assumed) |
| fig7gh-information-rate | not reproduced (assumed) |
| direct-method-comparison | partially reproduced (assumed) |
| fig8-nbta-differ | partially reproduced (assumed) |
| fig8-latency-decreases | reproduced (assumed) |
| fig8e-sigma-minimum | not reproduced (assumed) |
| sigma-n-below-sta-sigma | reproduced (assumed) |
| fig9-nbta-not-concatenated-1bta | reproduced (assumed) |
| fig9c-population-nbta | reproduced (assumed) |
| fig10-burst-n-vs-height | not reproduced (assumed) |
| firing-rate-no-effect-on-limit | reproduced (assumed) |
| model-reproduces-coding-trends | blocked: data_missing |

Totals: 11 reproduced, 6 partially reproduced, 6 not reproduced, 3 blocked.

**(2) The dataset**
- **Selection:** The paper's stated selection rule cannot be recovered. Data1 has 150 sessions. The 116 that use the paper's seven protocols come from exactly the paper's 37 cells and 23 recording dates. But the stated rule (trial-to-trial rate SD below 35 Hz) keeps 115 of them, where the paper kept 86. Every session count therefore runs high (60 reference sessions against 43), while the bursting fractions per protocol follow the paper's pattern.
- **Missing data:** Data1 records no thresholds, best frequencies or animals, so the model claims and the threshold claim are blocked.
- **Metadata problems:**
  - 34 sessions use stimuli the paper never mentions, and the descriptor does not describe two of those stimulus types.
  - The descriptor gives 98 to 533 trials per session; the files hold 69 to 503.
  - In three sessions the header intensity differs from `cell.dat` by more than 1 dB (up to 6.6 dB).
  - Six sessions had 450 ms pauses where the paper states 700 ms.
  - Two experiments are missing from `singlecells.txt`.
- **Clock check:** It passes. The spike-triggered stimulus average (STA) peaks a median 5.6 ms before the spike in all 116 sessions, and almost vanishes when the stimulus is shifted by 100 ms.
- **Version:** CRCNS does not version data sets. I pinned the zip by the MD5 in `checksums.md5`; the helper checks the S3 ETag against it before reading.

**Assumptions** (the questions for the paper's authors are in the `methods_unavailable` finding):
- **Burst identification:** I took the first peak as the largest value below 5 ms. The first local maximum lands on noise and leaves only 15 of 115 sessions bursting. With N as the number of trials, no session bursts at all.
- **Correlation-function error:** I left τ = 0 out of the span of the correlation function. The result is then 2.7% against the paper's 3.4%.
- **Figure 9:** I subtracted the mean stimulus before summing the 1-spike burst averages in Eq. 15.
- **Figure 3:** I chose the peak-prominence threshold used to count peaks.
- **Jitter:** I chose how reading (b) groups burst onsets into events.
- **Animals:** I assumed one animal per recording date.

No questions to a reader.

**(3) Where the protocol was unclear or did not fit**
1. "Pin the most recent published version" does not fit an unversioned archive. I recorded `unversioned` and checked the MD5 against the ETag.
2. The protocol does not say whether the author may add a reading the claims file does not list. I added a third reading of σ and N (from paragraph 6) and the exclusion of τ = 0, shown beside the listed readings and marked as assumptions.
3. Many criteria define only "reproduced". I gave "partially" when the effect held and some expected values matched, and "not" otherwise.
4. There is no rule for expected session counts when the dataset keeps more sessions than the paper did. I judged by the criterion and reported the proportions in the notes.
5. It is unclear whether picking one of the claims file's own listed readings counts as an assumption. I marked `assumed` wherever the outcome depends on the burst reading.
6. The data-check examples assume a task with trials and labels. For stimulus-driven data I used the STA against a 100 ms-shifted stimulus as the contrast.

**(4) Runtime and failures**
The work ran from 18:18 to about 19:00 UTC. The notebook takes 248 s from a clean environment. Two development runs failed on bugs that are now fixed (an array size and a plot-range count). Nothing failed in the final run. Some untracked files (dotfiles, `scripts/`) at the repository root were already there and are not mine; I left them alone.

## End of run

59 turns, 39 minutes, $6.72 at API prices, result: success.
