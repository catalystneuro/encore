# allen-2026 · author · run 45691797114

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper | head -50
```

```
<persisted-output>
Output too large (49.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/cd917b31-9544-4a88-a70b-5a892167255d/tool-results/b9jlubtqy.txt

Preview (first 2KB):
Wed Nov 25 20:14:18 UTC 2026
# Protocol for an attempt

Version: `pilot-19`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/cd917b31-9544-4a88-a70b-5a892167255d/tool-results/b9jlubtqy.txt"
}
```

```
1	Wed Nov 25 20:14:18 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-19`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 874 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/allen-2026.yaml; ls paper; cat papers/datasets/allen-2026.yaml; ls entries/fouke-2025; ls /tmp/dryad/rjdfn2zqz/439366/ -la
```

```
<persisted-output>
Output too large (54.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/cd917b31-9544-4a88-a70b-5a892167255d/tool-results/bbc7nnsun.txt

Preview (first 2KB):
# Claims for Allen, Yan, Kuan et al. (2026), Communications Biology 9:229, "Neurometabolic
# rewiring in squid (Sepioteuthis lessoniana) optic lobes drives behavioral plasticity and visual
# integration under environmental acidification", on Dryad dataset doi:10.5061/dryad.rjdfn2zqz.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
# protocol pilot-19 as stated in docs/protocol.md.
#
# Text read: the version of record (Communications Biology PDF, uploaded by Ben Dichter), its
# extracted text with the main text, Methods, figure legends and the one supplement PDF
# (Supplementary Figures 1 to 5 and Supplementary Tables 1 to 5). Figure pages 3, 7, 8, 9 and 10
# of the PDF were opened only to read the significance letters of Figures 1B to 1F, 2D and 2H and
# the axes of Figure 3C and 3D. The supplementary data files the Methods name ("Supplementary
# data: DET Results" and "GSEA results") are not under paper/; only the claim
# chronic-nachr-subunits-down rests on them.
#
# Code read: none. The paper links no code repository. Its Data availability says the
# bioinformatics code and "custom scripts, if any" are in the Dryad deposit itself, which the
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/cd917b31-9544-4a88-a70b-5a892167255d/tool-results/bbc7nnsun.txt"
}
```

```
1	# Claims for Allen, Yan, Kuan et al. (2026), Communications Biology 9:229, "Neurometabolic
2	# rewiring in squid (Sepioteuthis lessoniana) optic lobes drives behavioral plasticity and visual
3	# integration under environmental acidification", on Dryad dataset doi:10.5061/dryad.rjdfn2zqz.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
5	# protocol pilot-19 as stated in docs/protocol.md.
6	#
7	# Text read: the version of record (Communications Biology PDF, uploaded by Ben Dichter), its
8	# extracted text with the main text, Methods, figure legends and the one supplement PDF
9	# (Supplementary Figures 1 to 5 and Supplementary Tables 1 to 5). Figure pages 3, 7, 8, 9 and 10
10	# of the PDF were opened only to read the significance letters of Figures 1B to 1F, 2D and 2H and
11	# the axes of Figure 3C and 3D. The supplementary data files the Methods name ("Supplementary
12	# data: DET Results" and "GSEA results") are not under paper/; only the claim
13	# chronic-nachr-subunits-down rests on them.
14	#
15	# Code read: none. The paper links no code repository. Its Data availability says the
16	# bioinformatics code and "custom scripts, if any" are in the Dryad deposit itself, which the
17	# reader does not open; statistics were run in GraphPad Prism v10.2.3 and R v4.3.2 (logistic
18	# regression). Where the deposit's scripts fix a detail left open here, the author may take it
19	# from them, citing the file.
20	#
[... 1013 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/dryad/rjdfn2zqz/439366/; cat README.md; for f in *.csv; do echo "=== $f"; cat "$f"; echo; done
```

```
# Physiological and behavioral dataset of squid exposed to ocean acidification

Dataset DOI: [10.5061/dryad.rjdfn2zqz](10.5061/dryad.rjdfn2zqz)

## Description of the data and file structure

This dataset includes the raw experimental data from individual squid, comprising routine metabolic rate (RMR), ammonia excretion, behavioral analysis results, and electroretinogram (ERG) recordings. Additionally, the R scripts for  data analysis and visualization are also provided here. 

There were three groups in this dataset: control (normal seawater, pH 8.2) and two ocean acidification (OA) groups (pH 7.8) exposed for 7 days (acute) or 90 days (chronic).

### Files and variables

#### File: Carbonate_calibration.csv

**Description:** This file, to be used together with Squid_Hemolymph.csv, provides the calculation procedures for deriving hemolymph pCO~2~ and [HCO~3~-]~.~ The calculations use a hemolymph-specific pKa1 of 6.10 (Truchot, 1976) to better reflect the buffering properties of cephalopod blood, and αCO2 values appropriate for 32 ppt salinity at 25°C. Carbonate chemistry calculations also incorporate the carbonic acid dissociation constants of Mehrbach et al. (1973), refitted by Dickson and Millero (1987).

#### File: Squid_Behavioral_assessment.csv

**Description:** We provide the results of the novel tank test for three groups of squid: a **control** group (pH 8.1) and two ocean acidification (OA, pH 7.8) groups exposed for different durations, 7 days (acute) and 90 days (chronic). The Group column labels these as **acute-OA** and **chronic-OA**. 

[... 477 more lines not kept]
```

**Agent**

Status: the deposit holds small per-squid CSVs plus a 316 MB zip. Listing the zip next.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "
import zipfile
z=zipfile.ZipFile('/tmp/dryad/rjdfn2zqz/439366/squid.zip')
for i in z.infolist(): print(i.file_size, i.filename)
" | head -300; python -c "
import zipfile
z=zipfile.ZipFile('/tmp/dryad/rjdfn2zqz/439366/squid.zip'); print(len(z.infolist()))"
```

```
0 squid/
0 squid/squid/
5673 squid/squid/Bash_scripts.sh
1264 squid/squid/ExN50.stats
672 squid/squid/README.md
91128868 squid/squid/RSEM.isoform.counts.matrix
21834 squid/squid/R_scritps.Rmd
315805639 squid/squid/Squid.RData
8
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "
import zipfile
z=zipfile.ZipFile('/tmp/dryad/rjdfn2zqz/439366/squid.zip')
for n in ['squid/squid/README.md','squid/squid/ExN50.stats','squid/squid/Bash_scripts.sh','squid/squid/R_scritps.Rmd']:
  print('=====',n); print(z.read(n).decode('utf-8','replace'))
with z.open('squid/squid/RSEM.isoform.counts.matrix') as f:
  for k in range(4): print(f.readline()[:400])
"
```

```
<persisted-output>
Output too large (29.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/cd917b31-9544-4a88-a70b-5a892167255d/tool-results/bwpnjyzmi.txt

Preview (first 2KB):
===== squid/squid/README.md
# Overview
The Shell and R scripts that used for the publication "Neurometabolic rewiring in optic lobes of squid drives behavioral plasticity and visual integration under environmental acidification".
.
├── bash_scripts/               # Shell scripts for assembly and preprocessing
├── ExN50.stats/                # ExN50 result of de novo transcriptome
├── R_scripts/                  # R scripts for statistical analysis and visualization
├── RSEM.isoform.counts.matrix/ # Matrix of Transcript abundance
├── Squid.RData                 # R workspace files with processed data
└── README.md                   # This file



===== squid/squid/ExN50.stats
Ex	ExN50	num_genes
1	266	1
[... 104 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/cd917b31-9544-4a88-a70b-5a892167255d/tool-results/bwpnjyzmi.txt",
 "offset": 110
}
```

````
110	95	964	155739
111	96	831	209322
112	97	705	286505
113	98	593	399398
114	99	484	593131
115	100	475.549115913556	610324
116	
117	===== squid/squid/Bash_scripts.sh
118	```{bash}
119	# Quality control
120	## Estimate the quality of RAW data
121	fastqc -t 28 -o input_path/${input_samples} output_path/${samples}
122	
123	## Trim adaptors and quality control
124	fastp -w 16 -q 30 -f 15 -t 1 \
125	-h report_path/${samples}_fastp.html \
126	-i input_path/${samples}_R1.fastq.gz \
127	-o output_path/${samples}_R1.filtered.fastq.gz \
128	-I input_path/${samples}_R2.fastq.gz \
129	-O output_path/${samples}_R2.filtered.fastq.gz
[... 796 more lines not kept]
````

**Agent calls Bash**

```bash
date -u; which R Rscript conda mamba micromamba; python --version; pip list 2>/dev/null | grep -i -E "rdata|pyreadr|pandas|numpy|scipy|statsmodels|pydeseq|gseapy" ; cat docs/archives.md | sed -n '/Dryad/,/^## /p' | head -80
```

```
Wed Nov 25 20:14:48 UTC 2026
Python 3.13.18
## Dryad

- **Datasets.** A Dryad dataset, named by its DOI's suffix without the
  `dryad.` prefix: `10.5061/dryad.bvq83bkk9` is `DRYAD:bvq83bkk9`, in folders
  `dryad-bvq83bkk9` (Dryad DOIs ignore case). The registry's list,
  `targets/dryad.json`, is built from chosen DOIs by
  `tools/build_dryad_targets.py`, which reads each dataset's metadata, latest
  version and file list from the public API v2; for now it holds three datasets
  outside neuroscience, to test the pipeline on a general-purpose repository.
  The papers are the dataset's related works marked `primary_article` (and
  `preprint`); related works marked `software` are the paper's code, usually on
  Zenodo.
- **Versions.** The DOI always resolves to the latest version, and versions
  have no DOIs of their own. Each version has an id in the API
  (`/api/v2/versions/<id>`), which is `published_version` in the target list
  and pins it; a version's number (`versionNumber`) counts metadata edits as
  well as file changes, so it is not a pin. Record the version id under
  `dataset: version` and the DOI under `dataset: doi`, and give in the notebook
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in entries/fouke-2025/README.md; head -c 3000 entries/fouke-2025/omr.py; cat attempts/fouke-2025-01.yaml | head -250
```

```
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
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 348 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://datadryad.org/api/v2/versions/439366/files | python -m json.tool | grep -E '"(path|size|digest|digestType|status)"'; curl -s "https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.rjdfn2zqz/versions" | python -c "
import json,sys; d=json.load(sys.stdin)
for v in d['_embedded']['stash:versions']: print(v['_links']['self']['href'], v.get('versionNumber'), v.get('versionStatus'), v.get('publicationDate'), v.get('lastModificationDate'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.rjdfn2zqz" | python -c "
import json,sys; d=json.load(sys.stdin)
print({k:d.get(k) for k in ['title','versionNumber','versionStatus','publicationDate','lastModificationDate','license']}); print(d['_links'].get('stash:version')); print(d.get('relatedWorks')); print(d.get('abstract','')[:1500]); print(d.get('methods','')[:3000]); print(d.get('usageNotes',''))"; cat entries/fouke-2025/reproduce_fouke_2025.ipynb | python -c "
import json,sys; nb=json.load(sys.stdin)
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('---')"
```

Result: the fetched text is not kept.

**Agent**

Status: one public Dryad version (439366), small per-squid CSVs plus a zip with the R workspace, the RSEM count matrix and ExN50 stats. Checking whether the R workspace can be read in Python.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q rv && . rv/bin/activate && uv pip install -q rdata pandas numpy 2>&1 | tail -2; python -c "
import zipfile
z=zipfile.ZipFile('/tmp/dryad/rjdfn2zqz/439366/squid.zip')
with z.open('squid/squid/Squid.RData') as f: print(f.read(16))
"
```

```
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x06\x9c\xfd\x05TVQ'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . rv/bin/activate && /usr/bin/time -v python -c "
import zipfile, gzip, rdata, io, time
t=time.time()
z=zipfile.ZipFile('/tmp/dryad/rjdfn2zqz/439366/squid.zip')
raw=gzip.decompress(z.read('squid/squid/Squid.RData'))
print('decompressed', len(raw)/1e6, 'MB', time.time()-t)
p=rdata.parser.parse_data(raw)
print('parsed', time.time()-t)
obj=p.object
# top-level pairlist names
names=[]
o=obj
while o is not None and getattr(o,'info',None) is not None and o.info.type.name=='LIST':
    tag=o.tag
    names.append((tag.value if tag is not None else None, o.value[0].info.type.name, o.value[0].attributes is not None))
    o=o.value[1]
for n in names: print(n)
" 2>&1 | grep -v -E "^\s+(Page|Minor|Volun|Invol|Swaps|File sys|Socket|Signals|Average|Exit|Percent|System time|User time)" | tail -60
```

```
decompressed 1111.841634 MB 4.738471746444702
parsed 270.5585539340973
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'vst', attributes=None, tag=None, referenced_object=None), 'S4', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'.Anno_clusterProfiler_Env', attributes=None, tag=None, referenced_object=None), 'ENV', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'gse.Normal', attributes=None, tag=None, referenced_object=None), 'VEC', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'behavior_and_physiology_data', attributes=None, tag=None, referenced_object=None), 'VEC', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'.Random.seed', attributes=None, tag=None, referenced_object=None), 'INT', False)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'.GO_clusterProfiler_Env', attributes=None, tag=None, referenced_object=None), 'ENV', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'rawMatrix', attributes=None, tag=None, referenced_object=None), 'REAL', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'.GOSemSimEnv', attributes=None, tag=None, referenced_object=None), 'ENV', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, object=False, attributes=False, tag=False, gp=64, reference=0), value=b'dds', attributes=None, tag=None, referenced_object=None), 'S4', True)
(RObject(info=RObjectInfo(type=<RObjectType.CHAR: 9>, obje
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; grep -n -E "\"data\"|with_labels|elsewhere|link" schemas/attempt*.json | head -30; sed -n 1,80p tools/entry.py | head -80
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
205:          "description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.",
547:              "data",
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

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
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "dryad\|LOCAL_PATH\|staged" tools/entry.py | head -30; sed -n 530,600p schemas/attempt.schema.json; ls entries | head -100 | tr '\n' ' '; grep -l "dryad" entries/*/entry.yaml
```

```
72:LOCAL_PATH = re.compile(r"""["'](?:~/|/(?:Users|home|tmp|mnt|media|Volumes|data|scratch)/|[A-Za-z]:[\\/])""")
487:    if any(not _local_data(code, m.start() + 1) for m in LOCAL_PATH.finditer(code)):
              "paper_inconsistency",
              "other"
            ]
          },
          "statement": {
            "type": "string",
            "minLength": 1
          },
          "found": {
            "description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").",
            "enum": [
              "on_prompt"
            ]
          },
          "about": {
            "description": "What the finding is about. `data`: the dataset's files or metadata, including where they differ from what the paper says they hold. `paper`: the paper, its methods or its published code, with nothing wrong in the files. Unset: by its kind (docs/protocol.md): `methods_unavailable`, `code_mismatch` and `paper_inconsistency` are about the paper, the other kinds about the data. `other` and `selection_undocumented` must say.",
            "enum": [
              "data",
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 460,500p tools/entry.py; grep -n "_local_data" -A15 tools/entry.py | head -30; cat entries/dias-2025/entry.yaml; ls entries/dias-2025; grep -n "dryad" entries/dias-2025/*.py | head
```

```
if notebook in present and tag:
                nb = nbformat.read(entry_dir / notebook, as_version=4)
                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
    return report


def _local_data(code: str, start: int) -> bool:
    """Whether a local path in the code is inside the dataset directory `encore check` gave (ENCORE_LOCAL_DATA):
    the one local path an entry on a local dataset may name."""
    allowed = os.environ.get("ENCORE_LOCAL_DATA", "").rstrip("/")
    return bool(allowed) and code.startswith(allowed, start) and code[start + len(allowed):start + len(allowed) + 1] in ("/", "'", '"')


# A generator made with no seed, or a draw from numpy's global generator that no cell seeds: the results would differ
# from one run to the next (docs/protocol.md, Author, step 3).
UNSEEDED = re.compile(r"\bdefault_rng\(\s*\)|\bRandomState\(\s*\)")
GLOBAL_DRAW = re.compile(r"\bnp\.random\.(?:permutation|shuffle|choice|rand|randn|randint|normal|uniform)\(")


[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,120p entries/dias-2025/wingallom.py
```

```
"""Loading, model fitting and summaries for Dryad dataset bvq83bkk9 (version 333377).

Dias, Lemoine, Yanco, Zimova, Bay & Weeks (2025), Proc. R. Soc. B, doi:10.1098/rspb.2024.2556.

The dataset's Data.zip holds the specimens (`morphdata.csv`), the climate of each species and year
for the three classes (`ed_FHY.csv`, `ed_AHYspring.csv`, `ed_AHYfall.csv`, already scaled within
species), the phylogeny (`chitree.rds`) and catalogue numbers (`catnodata.csv`). Dryad needs a token
to download, so the workflow stages the files of the pinned version in `STAGED`, checked against the
SHA-256 of Dryad's file list; they are read from there into memory and never written.

Where the parameters come from (all from the claims file, which takes them from the paper's code,
Zenodo doi:10.5281/zenodo.14226724, Code.zip, Script01_MainAnalyses.R, Script02_SupplementAnalyses.R
and lm_mod.stan):

- Log transform and scaling within species over all specimens, the class split, the climate
  columns selected by number from the merged climate table, the dropping of species-years with a
  missing value, and the year coding: `prepare`, as Script01 (main models) and Script02
  (preliminary models) do. Column numbers are those of R's `merge` output, which `r_merge`
  rebuilds.
- The outlier filter of the Methods (five median absolute deviations), readings (a) to (d) of the
[... 100 more lines not kept]
```

**Agent**

Writing the helper with a skipping R-serialization reader.

**Agent calls Bash**

```bash
mkdir -p entries/allen-2026 && cat > entries/allen-2026/squidoa.py <<'EOF'
"""Loading for Dryad dataset rjdfn2zqz (version 439366), squid under ocean acidification.

Allen, Yan, Kuan et al. (2026), Communications Biology 9:229, doi:10.1038/s42003-025-09506-6.

The dataset holds one CSV per measurement (per squid, with its group), the hemolymph carbonate
calculations, and squid.zip, which holds the authors' R workspace `Squid.RData`, the RSEM count
matrix, the ExN50 statistics of the assembly and their shell and R scripts. Dryad needs a token to
download, so the workflow stages the files of the pinned version in `STAGED`, checked against the
SHA-256 of Dryad's file list; they are read from there into memory and never written.

`read_rdata` reads R's serialization format (XDR, version 2 or 3) and builds only the top-level
objects asked for, skipping the rest; the workspace is 1.1 GB uncompressed, and a general reader
(the `rdata` package) needs about 12 GB and 5 minutes for it. R objects become `RObj` (type,
value, attributes): numeric vectors are numpy arrays, character vectors lists of str (None for
NA), lists Python lists, pairlists lists of (tag, value). `df_from` turns a data.frame into pandas.

No analysis parameter is set here; the claims' methods are in the notebook, with their sources.
"""

from __future__ import annotations

import gzip
import hashlib
import io
import struct
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

DRYAD_ID = "rjdfn2zqz"
DRYAD_VERSION = "439366"
STAGED = Path("/tmp") / "dryad" / DRYAD_ID / DRYAD_VERSION  # where the workflow stages them (docs/archives.md)
SHA256 = {  # Dryad file list, https://datadryad.org/api/v2/versions/439366/files
    "Carbonate_calibration.csv": "31c3cb7319a7866914a2aaac1c414e84f4d172ba0046948b683bf95ae0f38902",
    "README.md": "6358bb541d7437d091326ba3dae5fe26001e369cd3873bd090e727f8be7a699b",
    "Squid_Ammonia.csv": "9ebf5ec10209d345c658c4968533ba96e630afc06fbbe2b05731f604e4fdba8d",
    "Squid_Behavioral_assessment.csv": "53cc4017d75ae7392a9b3177d73086abfe80850e9080367fd47f73acd5c8f6f0",
    "Squid_CFF.csv": "cae6cb27a6373b51706c526fb605937e5d40cddb7ab45ec1514213fab4ec2c85",
    "Squid_ERG.csv": "f679f6b4edfb42f154202001c5bca30891a1cbb1951f3b2f5d7d7641339c8001",
    "Squid_Hemolymph.csv": "eafdc713c4b50303a2ede1fc7852cb7d184edbe1e259a70a108217de490654e9",
    "Squid_normalized_total_distance.csv": "1d6ccf12641cc879c13c8818534fb236f350fe84a5f1fa2fda1422fd468c1e5e",
    "Squid_normalized_velocities.csv": "323742b0f9c84aa4d93ae62c085faf54cf1f5f79105e4e9fc3ec1cb2ad794fde",
    "Squid_Prey_Capture.csv": "fbb32ca33344fd3906c8684823b7783e7386d359e6c7573d378faed122832dc1",
    "Squid_RMR.csv": "9d643e82fe3094eea53a5bc967302201f41a47e63ce3c5960dba0efde982c9a8",
    "squid.zip": "60ba0ca6d534fb2b7353593b320ec8dc81073872748915b89a0867e040807d93",
}
ZIP_DIR = "squid/squid/"
GROUPS = ["Control", "Acute-OA", "Chronic-OA"]


def check_files() -> dict[str, str]:
    """SHA-256 of every staged file against Dryad's file list; returns name -> 'ok' or the digest found."""
    out = {}
    for name, want in SHA256.items():
        h = hashlib.sha256()
        with open(STAGED / name, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 22), b""):
                h.update(chunk)
        out[name] = "ok" if h.hexdigest() == want else h.hexdigest()
    return out


def read_csv(name: str) -> pd.DataFrame:
    """One of the dataset's CSV files (UTF-8 with a byte order mark), group names as in GROUPS."""
    df = pd.read_csv(STAGED / name, encoding="utf-8-sig")
    for col in df.columns:
        if col.lower() == "group":
            df[col] = df[col].str.strip().replace({"control": "Control", "Acute-OA": "Acute-OA"})
    return df


def zip_names() -> list[tuple[str, int]]:
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        return [(i.filename, i.file_size) for i in z.infolist()]


def zip_text(name: str) -> str:
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        return z.read(ZIP_DIR + name).decode("utf-8", "replace")


def count_matrix_rows() -> tuple[list[str], int]:
    """Header and number of transcript rows of RSEM.isoform.counts.matrix, read as a stream."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z, z.open(ZIP_DIR + "RSEM.isoform.counts.matrix") as f:
        header = f.readline().decode().rstrip("\n").split("\t")
        n = sum(1 for _ in f)
    return header, n


def read_count_matrix() -> pd.DataFrame:
    """RSEM.isoform.counts.matrix: transcripts by samples (expected counts)."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z, z.open(ZIP_DIR + "RSEM.isoform.counts.matrix") as f:
        header = f.readline().decode().rstrip("\n").split("\t")
        df = pd.read_csv(f, sep="\t", header=None, index_col=0, dtype={i: np.float64 for i in range(1, len(header) + 1)})
    df.columns = header
    df.index.name = None
    return df


# --- R serialization ----------------------------------------------------------

@dataclass
class RObj:
    type: str
    value: object = None
    attr: dict = field(default_factory=dict)

    def __getitem__(self, key):
        """A named element of a list, or an attribute (S4 slot) by name."""
        if self.type in ("list", "pairlist"):
            names = self.attr.get("names")
            if self.type == "pairlist":
                for tag, v in self.value:
                    if tag == key:
                        return v
            elif names is not None and key in names.value:
                return self.value[names.value.index(key)]
        if key in self.attr:
            return self.attr[key]
        raise KeyError(key)

    def names(self):
        if self.type == "pairlist":
            return [t for t, _ in self.value]
        n = self.attr.get("names")
        return list(n.value) if n is not None else None


_TYPES = {10: "logical", 13: "integer", 14: "double", 15: "complex", 24: "raw"}
_SPECIAL = {254: "NULL", 253: "globalenv", 252: "unbound", 251: "missing", 250: "basenamespace",
            242: "emptyenv", 241: "baseenv"}


class _Reader:
    def __init__(self, buf: bytes):
        self.b = memoryview(buf)
        self.p = 0
        self.refs: list = []

    def int(self) -> int:
        v = struct.unpack_from(">i", self.b, self.p)[0]
        self.p += 4
        return v

    def length(self) -> int:
        n = self.int()
        if n == -1:
            hi, lo = struct.unpack_from(">ii", self.b, self.p)
            self.p += 8
            n = (hi << 32) + lo
        return n

    def charsxp(self, keep: bool):
        n = self.int()
        if n == -1:
            return None
        s = self.p
        self.p += n
        return bytes(self.b[s:s + n]).decode("utf-8", "replace") if keep else None

    def item(self, keep: bool):
        flags = self.int()
        t = flags & 0xFF
        has_attr, has_tag = bool(flags & 0x200), bool(flags & 0x400)
        if t in _SPECIAL:
            return RObj(_SPECIAL[t])
        if t == 255:  # REFSXP
            i = flags >> 8
            if i == 0:
                i = self.int()
            return self.refs[i - 1]
        if t in (247, 248, 249):  # PERSISTSXP, PACKAGESXP, NAMESPACESXP
            self.int()
            n = self.int()
            v = RObj("namespace", [self.item(True).value for _ in range(n)])
            self.refs.append(v)
            return v
        if t == 1:  # SYMSXP
            v = RObj("symbol", self.item(True).value)
            self.refs.append(v)
            return v
        if t == 4:  # ENVSXP: contents skipped
            self.int()
            v = RObj("environment")
            self.refs.append(v)
            for _ in range(4):
                self.item(False)
            return v
        if t in (2, 3, 5, 6, 17, 239, 240):  # pairlist-like, read iteratively along the CDR
            out, first_attr = [], None
            while True:
                attr = self.item(keep) if has_attr else None
                if first_attr is None:
                    first_attr = attr
                tag = self.item(True).value if has_tag else None
                car = self.item(keep)
                out.append((tag, car))
                flags = self.int()
                t2 = flags & 0xFF
                if t2 not in (2, 3, 5, 6, 17, 239, 240):
                    self.p -= 4
                    self.item(keep)  # the final CDR, normally NULL
                    break
                has_attr, has_tag = bool(flags & 0x200), bool(flags & 0x400)
            v = RObj("pairlist" if t in (2, 239) else "language", out if keep else None)
            if keep and first_attr is not None:
                v.attr = _attr_dict(first_attr)
            return v
        if t in (7, 8):  # SPECIALSXP, BUILTINSXP
            n = self.int()
            self.p += n
            return RObj("builtin")
        if t == 9:
            return RObj("char", self.charsxp(keep))
        if t in _TYPES:
            n = self.length()
            size = {10: 4, 13: 4, 14: 8, 15: 16, 24: 1}[t]
            s = self.p
            self.p += n * size
            val = None
            if keep:
                dt = {10: ">i4", 13: ">i4", 14: ">f8", 15: ">c16", 24: "u1"}[t]
                val = np.frombuffer(self.b[s:s + n * size], dtype=dt).astype(dt[1:] if t != 24 else "u1")
            v = RObj(_TYPES[t], val)
        elif t == 16:  # STRSXP
            n = self.length()
            vals = []
            for _ in range(n):
                self.int()  # CHARSXP flags
                vals.append(self.charsxp(keep))
            v = RObj("character", vals if keep else None)
        elif t in (19, 20):  # VECSXP, EXPRSXP
            n = self.length()
            v = RObj("list", [self.item(keep) for _ in range(n)])
        elif t == 25:  # S4SXP
            v = RObj("S4")
        elif t == 22:  # EXTPTRSXP
            v = RObj("externalptr")
            self.refs.append(v)
            self.item(False)
            self.item(False)
        elif t == 23:  # WEAKREFSXP
            v = RObj("weakref")
            self.refs.append(v)
        elif t == 238:  # ALTREP: class info, state, attributes
            info = self.item(True)
            state = self.item(keep)
            attr = self.item(keep)
            cls = info.value[0][1].value if info.value else None
            v = _altrep(cls, state) if keep else RObj("altrep")
            if keep and attr.type == "pairlist":
                v.attr = _attr_dict(attr)
            return v
        else:
            raise ValueError(f"unsupported R type {t} at byte {self.p}")
        if has_attr:
            a = self.item(keep)
            if keep:
                v.attr = _attr_dict(a)
        return v


def _attr_dict(a: RObj) -> dict:
    return {tag: val for tag, val in a.value} if a is not None and a.type == "pairlist" else {}


def _altrep(cls: str, state: RObj) -> RObj:
    """The ALTREP classes R writes for compact sequences and deferred strings."""
    if cls in ("compact_intseq", "compact_realseq"):
        n, start, step = state.value[:3]
        seq = start + step * np.arange(int(n))
        return RObj("integer" if cls == "compact_intseq" else "double", seq.astype(int if cls == "compact_intseq" else float))
    if cls == "deferred_string":
        src = state.value[0][1] if state.type == "pairlist" else state
        return RObj("character", [None if x is None else str(x) for x in np.asarray(src.value).tolist()])
    if cls == "wrap_real" or cls == "wrap_integer" or cls == "wrap_string" or cls == "wrap_logical":
        return state.value[0][1] if state.type == "pairlist" else state
    raise ValueError(f"unsupported ALTREP class {cls}")


def read_rdata(keep: set[str]) -> dict[str, RObj]:
    """The top-level objects named in `keep` from Squid.RData (others are skipped, not built)."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        raw = gzip.decompress(z.read(ZIP_DIR + "Squid.RData"))
    if raw[:5] != b"RDX3\n" and raw[:5] != b"RDX2\n":
        raise ValueError("not an R workspace")
    r = _Reader(raw[5:])
    r.p += 2  # "X\n"
    version = r.int()
    r.int()
    r.int()
    if version == 3:
        n = r.int()
        r.p += n  # native encoding
    out = {}
    # The workspace is a pairlist of (name, object); walk it, building only the objects asked for.
    while True:
        flags = r.int()
        if flags & 0xFF != 2:
            break
        if flags & 0x200:
            r.item(False)
        tag = r.item(True).value if flags & 0x400 else None
        obj = r.item(tag in keep)
        if tag in keep:
            out[tag] = obj
    del raw
    return out


def top_level_names() -> list[tuple[str, str]]:
    """Name and R type of every object in Squid.RData, without building any of them."""
    with zipfile.ZipFile(STAGED / "squid.zip") as z:
        raw = gzip.decompress(z.read(ZIP_DIR + "Squid.RData"))
    r = _Reader(raw[5:])
    r.p += 2
    version = r.int()
    r.int()
    r.int()
    if version == 3:
        r.p += r.int()
    out = []
    while True:
        flags = r.int()
        if flags & 0xFF != 2:
            break
        if flags & 0x200:
            r.item(False)
        tag = r.item(True).value if flags & 0x400 else None
        start = r.p
        t = struct.unpack_from(">i", r.b, start)[0] & 0xFF
        r.item(False)
        out.append((tag, {25: "S4", 19: "list", 14: "double", 13: "integer", 16: "character", 4: "environment"}.get(t, str(t)), r.p - start))
    return out


def r_class(o: RObj) -> list[str]:
    c = o.attr.get("class")
    return list(c.value) if c is not None else []


def as_py(o: RObj):
    """An atomic R vector as numpy or list, with NA as nan or None."""
    if o.type == "integer" or o.type == "logical":
        v = o.value.astype(float)
        v[o.value == -2147483648] = np.nan
        return v
    return o.value


def df_from(o: RObj) -> pd.DataFrame:
    """A data.frame (or a list of equal-length vectors) as pandas, factors as their labels."""
    cols = {}
    for name, col in zip(o.names(), o.value):
        if "factor" in r_class(col):
            levels = col.attr["levels"].value
            cols[name] = [None if x == -2147483648 else levels[x - 1] for x in col.value]
        else:
            cols[name] = as_py(col)
    df = pd.DataFrame(cols)
    rn = o.attr.get("row.names")
    if rn is not None and rn.type == "character":
        df.index = rn.value
    return df


def s4_dataframe(o: RObj) -> pd.DataFrame:
    """An S4Vectors DataFrame (DESeqResults and the like) as pandas."""
    ld = o["listData"]
    df = pd.DataFrame({n: as_py(v) for n, v in zip(ld.names(), ld.value)})
    rn = o.attr.get("rownames")
    if rn is not None and rn.type == "character":
        df.index = rn.value
    return df


def matrix(o: RObj) -> pd.DataFrame:
    """A numeric R matrix with its dimnames."""
    nr, nc = o.attr["dim"].value
    arr = np.asarray(o.value).reshape((nc, nr)).T
    dn = o.attr.get("dimnames")
    rows = cols = None
    if dn is not None:
        rows = dn.value[0].value if dn.value[0].type == "character" else None
        cols = dn.value[1].value if dn.value[1].type == "character" else None
    return pd.DataFrame(arr, index=rows, columns=cols)
EOF
cd entries/allen-2026 && . $TMPDIR/rv/bin/activate && /usr/bin/time -f "%e s %M KB" python -c "
import squidoa
for n in squidoa.top_level_names(): print(n)
"
```

```
5.72 s 2869344 KB
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python -c "
import zipfile,gzip,struct,squidoa
z=zipfile.ZipFile(squidoa.STAGED/'squid.zip'); raw=gzip.decompress(z.read('squid/squid/Squid.RData'))
print(raw[:60])
"
```

```
b'RDX3\nX\n\x00\x00\x00\x03\x00\x04\x05\x01\x00\x03\x05\x00\x00\x00\x00\x05UTF-8\x00\x00\x04\x02\x00\x00\x00\x01\x00\x04\x00\t\x00\x00\x00\x03vst\x00\x01\x03\x19\x00\x00\x04\x02\x00\x00\x00\x01\x00'
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python - <<'EOF'
import re
p='squidoa.py'; s=open(p).read()
s=s.replace("""    if version == 3:
        r.p += r.int()
    out = []""","""    if version == 3:
        n = r.int()
        r.p += n
    out = []""")
open(p,'w').write(s)
EOF
/usr/bin/time -f "%e s %M KB" python -c "
import squidoa
for n in squidoa.top_level_names(): print(n)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    for n in squidoa.top_level_names(): print(n)
             ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "entries/allen-2026/squidoa.py", line 336, in top_level_names
    r.item(False)
    ~~~~~~^^^^^^^
  File "entries/allen-2026/squidoa.py", line 260, in item
    a = self.item(keep)
  File "entries/allen-2026/squidoa.py", line 199, in item
    car = self.item(keep)
  File "entries/allen-2026/squidoa.py", line 198, in item
    tag = self.item(True).value if has_tag else None
          ~~~~~~~~~^^^^^^
  File "entries/allen-2026/squidoa.py", line 190, in item
    self.item(False)
    ~~~~~~~~~^^^^^^^
  File "entries/allen-2026/squidoa.py", line 199, in item
    car = self.item(keep)
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python - <<'EOF'
p='squidoa.py'; s=open(p).read()
s=s.replace("""        elif t == 25:  # S4SXP""","""        elif t == 21:  # BCODESXP (compiled closures in environments), skipped
            self.int()
            self._bc1()
            v = RObj("bytecode")
        elif t == 25:  # S4SXP""")
s=s.replace("""def _attr_dict(a: RObj) -> dict:""","""def _bc1(self) -> None:
    self.item(False)  # the code vector
    for _ in range(self.int()):
        t = self.int()
        if t == 21:
            self._bc1()
        elif t in (2, 6, 243, 244, 239, 240):
            self._bclang(t)
        else:
            self.item(False)


def _bclang(self, t: int) -> None:
    if t == 243:  # BCREPREF
        self.int()
        return
    if t in (244, 2, 6, 239, 240):
        if t == 244:  # BCREPDEF
            self.int()
            t = self.int()
        if t in (239, 240):
            self.item(False)
        self.item(False)  # tag
        self._bclang(self.int())
        self._bclang(self.int())
        return
    self.item(False)


_Reader._bc1 = _bc1
_Reader._bclang = _bclang


def _attr_dict(a: RObj) -> dict:""")
open(p,'w').write(s)
EOF
/usr/bin/time -f "%e s %M KB" python -c "
import squidoa
for n in squidoa.top_level_names(): print(n)
"
```

```
('vst', 'S4', 29026895)
('.Anno_clusterProfiler_Env', 'environment', 208882693)
('gse.Normal', 'list', 150631635)
('behavior_and_physiology_data', 'list', 20587)
('.Random.seed', 'integer', 2512)
('.GO_clusterProfiler_Env', 'environment', 132668711)
('rawMatrix', 'double', 130146714)
('.GOSemSimEnv', 'environment', 19284427)
('dds', 'S4', 59275700)
('.GOTERM_Env', 'environment', 72819297)
('.ancCache', 'environment', 144)
('ddssva', 'S4', 49840422)
('resNormal', 'list', 9920564)
('matrix', 'double', 74588595)
('df', 'list', 662)
('.SemSimCache', 'environment', 329087)
('vstsva.adj.limma', 'S4', 31562997)
('svseq', 'list', 1110278)
('vstsva.adj', 'S4', 31562997)
('ddssva.adj', 'S4', 60254172)
[... 2 more lines not kept]
```

**Agent**

Parser works: 19 s and 2.9 GB to walk the whole workspace. Now looking at the behavioural/physiology list and the RNA-seq objects.

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python -c "
import squidoa as s, pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
o=s.read_rdata({'behavior_and_physiology_data','df'})
b=o['behavior_and_physiology_data']
print(b.names())
for n,v in zip(b.names(), b.value):
    print('=====',n, v.type, s.r_class(v))
    try:
        d=s.df_from(v); print(d.shape); print(d.to_string())
    except Exception as e: print('ERR',e, v.attr.keys())
print(s.df_from(o['df']))
"
```

```
['F1B', 'F1C', 'F1D', 'F1E', 'F1F', 'F2C', 'F2G', 'F2F', 'F2E', 'F2D', 'F2H', 'F2I', 'F3C', 'F3D', 'S2', 'S3']
===== F1B list ['grouped_df', 'tbl_df', 'tbl', 'data.frame']
(33, 2)
         group   value
0      Control  15.363
1     Acute-OA  15.271
2   Chronic-OA  26.413
3      Control  21.718
4     Acute-OA  25.326
5   Chronic-OA  24.999
6      Control  22.513
7     Acute-OA  26.234
8   Chronic-OA  22.084
9      Control  18.266
10    Acute-OA  22.841
11  Chronic-OA  20.734
12     Control  11.046
13    Acute-OA  17.850
14  Chronic-OA  25.312
15     Control  19.222
[... 653 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && /usr/bin/time -f "%e s %M KB" python -c "
import squidoa as s, pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_columns',20)
o=s.read_rdata({'gse.Normal','resNormal','svseq','vstsva.adj.limma'})
g=o['gse.Normal']; print(g.names())
a=g['AvsCT']; print(a.type, s.r_class(a), list(a.attr.keys()))
r=s.df_from(a['result']); print(r.shape); print(r.head(3).T)
for k in a.attr:
    v=a.attr[k]; print(k, v.type, (len(v.value) if v.value is not None and hasattr(v.value,'__len__') else v.value) )
rn=o['resNormal']; print(rn.names()); x=rn['AvsCT']; print(s.r_class(x), list(x.attr.keys()))
d=s.s4_dataframe(x); print(d.shape); print(d.head())
sv=o['svseq']; print(sv.names()); print(s.matrix(sv['sv']) if 'dim' in sv['sv'].attr else sv['sv'].value)
v=o['vstsva.adj.limma']; print(s.r_class(v), list(v.attr.keys()))
"
```

```
['AvsCT', 'CvsCT']
S4 ['gseaResult'] ['result', 'organism', 'setType', 'geneSets', 'geneList', 'keytype', 'permScores', 'params', 'gene2Symbol', 'readable', 'termsim', 'method', 'dr', 'class']
(87, 12)
                                                        GO:0005198                                         GO:0005840                                         GO:0003735
ONTOLOGY                                                        MF                                                 CC                                                 MF
ID                                                      GO:0005198                                         GO:0005840                                         GO:0003735
Description                           structural molecule activity                                           ribosome                 structural constituent of ribosome
setSize                                                      486.0                                              294.0                                              258.0
enrichmentScore                                          -0.473753                                          -0.526378                                          -0.524835
NES                                                      -2.517823                                          -2.624092                                          -2.596069
pvalue                                                         0.0                                                0.0                                                0.0
p.adjust                                                       0.0                                                0.0                                                0.0
qvalue                                                         0.0                                                0.0                                                0.0
rank                                                       15456.0                                          
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']
print(json.dumps(o['properties'],indent=0)[:6000]); print(o.get('required'))
print(list(s['properties'].keys()))
"
```

```
{
"claim": {
"description": "Claim id from the target's claims file.",
"type": "string"
},
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
],
"description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
},
"blocked_by": {
"description": "Required when outcome is blocked.",
"enum": [
"data_missing",
"metadata_insufficient",
"methods_underspecified",
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; wc -c paper/*.txt; grep -n -i -E "statistic|GraphPad|Tukey|Welch|Kruskal|logistic|two-way|normality|Shapiro|outlier|excluded|mantle length|fresh mass|ROUT|Brown-Forsythe" paper/10.1038-s42003-025-09506-6.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 570,602p paper/10.1038-s42003-025-09506-6.txt; sed -n 600,720p paper/10.1038-s42003-025-09506-6.txt; sed -n 1700,1900p paper/10.1038-s42003-025-09506-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1900,2150p paper/10.1038-s42003-025-09506-6.txt | tr '\n' '|' | sed 's/| *|/|/g' | fold -w 250
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/allen-2026 && . $TMPDIR/rv/bin/activate && /usr/bin/time -f "%e s %M KB" python -c "
import squidoa as s, pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_columns',20); pd.set_option('display.max_colwidth',60)
h,n=s.count_matrix_rows(); print(h, n)
o=s.read_rdata({'DB','gse.Normal','rawMatrix'})
D=o['DB']; print(D.names(), [ (x.type, len(x.value) if x.value is not None else None) for x in D.value])
for nm,v in zip(D.names(), D.value):
    if v.type=='list' and v.attr.get('names'): print(nm, v.names()); print(s.df_from(v).head())
    else: print(nm, v.value[:5] if v.value is not None else v)
c=s.df_from(o['gse.Normal']['CvsCT']['result']); a=s.df_from(o['gse.Normal']['AvsCT']['result'])
print(len(a), len(c), (a.NES<0).sum(), (a.NES>0).sum(), (c.NES<0).sum(), (c.NES>0).sum())
print(c.groupby([c.ONTOLOGY, c.NES>0]).size())
p=o['gse.Normal']['AvsCT']['params']; print(p.names(), [x.value for x in p.value])
rm=o['rawMatrix']; m=s.matrix(rm); print(m.shape, list(m.columns)); print(m.index[:3])
"
```

```
['Ct_8.1_Gill-1', 'Ct_8.1_OL-1', 'Ct_8.1_OL-2', 'Ct_8.1_OL-3', 'Ct_8.1_OL-4', 'Ph_7.8_OL-1', 'Ph_7.8_OL-2', 'Ph_7.8_OL-3', 'Ph_7.8_OL-4', 'Ph_7.8_OL-5', 'Ph_7.8C-OL-1', 'Ph_7.8C-OL-2', 'Ph_7.8C-OL-3', 'Re_8.1_OL-1', 'Re_8.1_OL-2', 'Re_8.1_OL-3'] 902413
['name', 'id', 'db'] [('list', 2), ('list', 2), ('list', 2)]
name ['GID', 'PNAME']
                GID                                            PNAME
0    DN162_c0_g1_i8       Transcription initiation protein SPT3-like
1  DN2995_c0_g1_i50                                 Titin isoform X2
2  DN24363_c0_g1_i6             Uncharacterized protein LOC115214248
3  DN40630_c0_g1_i4                     Zinc finger protein 665-like
4  DN17736_c0_g1_i9  Transglutaminase-like domain-containing protein
id ['GID', 'PID']
                GID         PID
0    DN162_c0_g1_i8  A0A210QFG3
1  DN2995_c0_g1_i50  A0A7E6FUJ8
2  DN24363_c0_g1_i6  A0A7E6EZI8
3  DN40630_c0_g1_i4  A0A8B8C3L9
4  DN17736_c0_g1_i9  A0A812EG04
db ['GID', 'DB']
                GID  DB
0    DN162_c0_g1_i8  tr
1  DN2995_c0_g1_i50  tr
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "pK|solubility|αCO2|Eq\. ?\(?[12]|equation" paper/10.1038-s42003-025-09506-6.txt | head; sed -n 255,300p paper/10.1038-s42003-025-09506-6.txt; grep -n -i -E "data availability" -A12 paper/10.1038-s42003-025-09506-6.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent**

Now writing the statistics helpers and the notebook.

**Agent calls Bash**

```bash
cd entries/allen-2026 && cat >> squidoa.py <<'EOF'


# --- statistics ---------------------------------------------------------------
# The tests the paper names (Methods, "Statistics and reproducibility"; Supplementary Tables 1 to 4),
# written out here because GraphPad Prism's Welch ANOVA and Dunnett's T3 have no SciPy equivalent.

def welch_anova(groups: list[np.ndarray]) -> dict:
    """Welch's one-way ANOVA (Welch 1951), as GraphPad Prism reports it: W, df1, df2, p."""
    from scipy import stats
    k = len(groups)
    n = np.array([len(g) for g in groups], float)
    m = np.array([np.mean(g) for g in groups])
    v = np.array([np.var(g, ddof=1) for g in groups])
    w = n / v
    mw = np.sum(w * m) / np.sum(w)
    a = np.sum(w * (m - mw) ** 2) / (k - 1)
    lam = np.sum((1 - w / w.sum()) ** 2 / (n - 1))
    b = 1 + 2 * (k - 2) / (k ** 2 - 1) * lam
    f = a / b
    df2 = (k ** 2 - 1) / (3 * lam)
    return {"W": f, "df1": k - 1, "df2": df2, "p": stats.f.sf(f, k - 1, df2)}


def _smm_cdf(c: float, k: int, df: float) -> float:
    """Studentized maximum modulus distribution: P(max of k |t| <= c) with df degrees of freedom."""
    from scipy import integrate, stats
    s = stats.chi(df, scale=1 / np.sqrt(df))
    f = lambda x: (2 * stats.norm.cdf(c * x) - 1) ** k * s.pdf(x)
    hi = s.ppf(1 - 1e-12)
    return integrate.quad(f, 0, hi, limit=200)[0]


def dunnett_t3(groups: dict[str, np.ndarray], level: float = 0.95) -> pd.DataFrame:
    """Dunnett's T3 (Dunnett 1980): every pair, Welch standard error and df, studentized maximum
    modulus with k = number of comparisons. Mean difference is first minus second, as Prism prints."""
    from scipy import optimize
    names = list(groups)
    pairs = [(a, b) for i, a in enumerate(names) for b in names[i + 1:]]
    k = len(pairs)
    rows = []
    for a, b in pairs:
        x, y = np.asarray(groups[a]), np.asarray(groups[b])
        va, vb = np.var(x, ddof=1) / len(x), np.var(y, ddof=1) / len(y)
        se = np.sqrt(va + vb)
        df = (va + vb) ** 2 / (va ** 2 / (len(x) - 1) + vb ** 2 / (len(y) - 1))
        d = x.mean() - y.mean()
        t = abs(d) / se
        p = 1 - _smm_cdf(t, k, df)
        crit = optimize.brentq(lambda c: _smm_cdf(c, k, df) - level, 0.5, 50)
        rows.append({"comparison": f"{a} vs {b}", "mean_diff": d, "ci_low": d - crit * se,
                     "ci_high": d + crit * se, "df": df, "p_adj": max(p, 0.0)})
    return pd.DataFrame(rows)


def oneway(groups: dict[str, np.ndarray]) -> dict:
    """Ordinary one-way ANOVA with Tukey's multiple comparisons (scipy.stats.tukey_hsd)."""
    from scipy import stats
    vals = [np.asarray(v, float) for v in groups.values()]
    f, p = stats.f_oneway(*vals)
    n = sum(len(v) for v in vals)
    grand = np.concatenate(vals).mean()
    ss_t = sum(len(v) * (v.mean() - grand) ** 2 for v in vals)
    ss_r = sum(((v - v.mean()) ** 2).sum() for v in vals)
    tk = stats.tukey_hsd(*vals)
    names = list(groups)
    pairs = {f"{names[i]} vs {names[j]}": tk.pvalue[i, j]
             for i in range(len(names)) for j in range(i + 1, len(names))}
    return {"F": f, "df1": len(vals) - 1, "df2": n - len(vals), "p": p, "SS_treat": ss_t,
            "SS_resid": ss_r, "eta2": ss_t / (ss_t + ss_r), "tukey": pairs}


def describe(groups: dict[str, np.ndarray]) -> pd.DataFrame:
    """n, mean, SD and SEM per group."""
    return pd.DataFrame({g: {"n": len(v), "mean": np.mean(v), "sd": np.std(v, ddof=1),
                             "sem": np.std(v, ddof=1) / np.sqrt(len(v))} for g, v in groups.items()}).T


def by_group(df: pd.DataFrame, col: str, group_col: str = "Group") -> dict[str, np.ndarray]:
    """Values of `col` per group, in the order of GROUPS, NA dropped."""
    return {g: df.loc[df[group_col] == g, col].dropna().to_numpy(float) for g in GROUPS}


def auc(y: np.ndarray, score: np.ndarray) -> float:
    """Area under the ROC curve (the Mann-Whitney statistic, ties counted half)."""
    from scipy import stats
    r = stats.rankdata(score)
    n1 = int(y.sum())
    n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def plotpca(assay: pd.DataFrame, ntop: int = 500) -> tuple[pd.DataFrame, np.ndarray]:
    """DESeq2's plotPCA: the `ntop` rows of highest variance, prcomp centred and unscaled; returns
    sample scores and the fraction of variance of each component."""
    v = assay.var(axis=1, ddof=1)
    top = assay.loc[v.sort_values(ascending=False).index[:ntop]]
    x = top.T.to_numpy()
    x = x - x.mean(axis=0)
    u, s, vt = np.linalg.svd(x, full_matrices=False)
    scores = pd.DataFrame(u * s, index=assay.columns, columns=[f"PC{i + 1}" for i in range(len(s))])
    return scores, s ** 2 / np.sum(s ** 2)


def remove_batch_effect(assay: pd.DataFrame, design: np.ndarray, covariates: np.ndarray) -> pd.DataFrame:
    """limma's removeBatchEffect with covariates: fit each row on [design, covariates] by least
    squares and subtract the covariates' part."""
    x = np.column_stack([design, covariates])
    beta, *_ = np.linalg.lstsq(x, assay.to_numpy().T, rcond=None)
    out = assay.to_numpy() - (covariates @ beta[design.shape[1]:]).T
    return pd.DataFrame(out, index=assay.index, columns=assay.columns)


def s4_assay(o: RObj) -> pd.DataFrame:
    """The first assay of a SummarizedExperiment (DESeqTransform), with its row and column names."""
    a = o["assays"]["data"]["listData"].value[0]
    m = matrix(a)
    return m
EOF
uv pip install -q scipy statsmodels matplotlib nbconvert ipykernel nbformat 2>&1 | tail -1; python -c "
import squidoa as s, numpy as np
h=s.read_csv('Squid_Hemolymph.csv'); print(h.columns.tolist()); g=s.by_group(h,'Hemolymph pH'); print(s.describe(g)); print(s.welch_anova(list(g.values()))); print(s.dunnett_t3(g))
"
```

```
Exit code 1
error: No virtual environment found; run `uv venv` to create an environment, or pass `--system` to install into a non-virtual environment
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import squidoa as s, numpy as np
  File "entries/allen-2026/squidoa.py", line 30, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd entries/allen-2026 && . $TMPDIR/rv/bin/activate && uv pip install -q scipy statsmodels matplotlib nbconvert ipykernel nbformat 2>&1 | tail -1; python -c "
import squidoa as s, numpy as np
h=s.read_csv('Squid_Hemolymph.csv'); print(h.columns.tolist()); g=s.by_group(h,'Hemolymph pH'); print(s.describe(g)); print(s.welch_anova(list(g.values()))); print(s.dunnett_t3(g))
"
```

```
['Hemolymph pH', 'Hemolymph PCO2 (µatm)', 'Hemolymph [HCO3-] (mmol l-1)', 'Group']
              n      mean        sd       sem
Control     7.0  7.091714  0.020014  0.007565
Acute-OA    6.0  7.144500  0.088496  0.036128
Chronic-OA  9.0  7.174556  0.067552  0.022517
{'W': np.float64(6.347073619060113), 'df1': 2, 'df2': np.float64(9.195963839767906), 'p': np.float64(0.01854243832708639)}
               comparison  mean_diff    ci_low   ci_high        df     p_adj
0     Control vs Acute-OA  -0.052786 -0.174479  0.068908  5.439316  0.459802
1   Control vs Chronic-OA  -0.082841 -0.150354 -0.015329  9.742234  0.017334
2  Acute-OA vs Chronic-OA  -0.030056 -0.153414  0.093303  8.808317  0.858052
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python -c "
import squidoa as s, numpy as np
h=s.read_csv('Squid_Hemolymph.csv')
for c in h.columns[1:3]:
  g=s.by_group(h,c); print(s.describe(g)); print(s.welch_anova(list(g.values()))); print(s.dunnett_t3(g))
for f,c in [('Squid_RMR.csv',0),('Squid_Ammonia.csv',0)]:
  d=s.read_csv(f); g=s.by_group(d,d.columns[0]); print(s.describe(g)); print(s.oneway(g)); print(s.oneway({k:np.log10(v) for k,v in g.items()}))
"
```

```
n         mean          sd         sem
Control     7.0  1057.369000  234.087356   88.476704
Acute-OA    6.0  1583.800167  284.396911  116.104553
Chronic-OA  9.0  2778.711667  613.410884  204.470295
{'W': np.float64(29.814996122318643), 'df1': 2, 'df2': np.float64(12.03567401430269), 'p': np.float64(2.173375675673258e-05)}
               comparison    mean_diff  ...         df     p_adj
0     Control vs Acute-OA  -526.431167  ...   9.752557  0.014276
1   Control vs Chronic-OA -1721.342667  ...  10.772731  0.000030
2  Acute-OA vs Chronic-OA -1194.911500  ...  11.995312  0.000796

[3 rows x 6 columns]
              n       mean        sd       sem
Control     7.0   3.562429  0.899503  0.339980
Acute-OA    6.0   5.895667  0.680348  0.277751
Chronic-OA  9.0  11.079778  2.240151  0.746717
{'W': np.float64(42.83901966169275), 'df1': 2, 'df2': np.float64(12.541039109608223), 'p': np.float64(2.4832403895928e-06)}
               comparison  mean_diff    ci_low   ci_high         df     p_adj
0     Control vs Acute-OA  -2.333238 -3.557729 -1.108748  10.870856  0.000754
1   Control vs Chronic-OA  -7.517349 -9.800519 -5.234180  11.028642  0.000005
2  Acute-OA vs Chronic-OA  -5.184111 -7.435536 -2.932687  10.058761  0.000195
[... 12 more lines not kept]
```

**Agent**

Ammonia ANOVA matches the paper exactly (F = 6.382, p = 0.008038); RMR means match but the deposit has 26 squid against the paper's 29. Writing the notebook now.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/nb1.py <<'PYEOF'
# Part 1 of the notebook generator: header, data check, physiology.
CELLS = []
def md(s, tags=None): CELLS.append(("markdown", s.strip("\n"), tags or []))
def code(s, tags=None): CELLS.append(("code", s.strip("\n"), tags or []))

md(r'''
# Reproducing Allen, Yan, Kuan et al. (2026) from Dryad rjdfn2zqz

**Paper.** Allen, Yan, Kuan et al. (2026). Neurometabolic rewiring in squid (*Sepioteuthis lessoniana*)
optic lobes drives behavioral plasticity and visual integration under environmental acidification.
*Communications Biology* 9:229. [doi:10.1038/s42003-025-09506-6](https://doi.org/10.1038/s42003-025-09506-6).
The claims file (`claims/allen-2026.yaml`) was written from the version of record and its
supplement (Supplementary Figures 1 to 5, Supplementary Tables 1 to 5).

**Dataset.** Dryad [doi:10.5061/dryad.rjdfn2zqz](https://doi.org/10.5061/dryad.rjdfn2zqz), version id
439366 (API `/api/v2/versions/439366`, version number 6, published 2026-04-29). The paper cites the
dataset's DOI, which resolves to the latest version, and no version. 439366 is the latest and the
only version the API lists, so it is the one pinned. The files are read from the directory where
the workflow stages them, after checking each against the SHA-256 of Dryad's file list (below).

**What the dataset holds.** One CSV per measure, a value per squid with its group: routine
metabolic rate, ammonia excretion, hemolymph pH, PCO2 and [HCO3-] (with the calculation of PCO2 and
[HCO3-] in `Carbonate_calibration.csv`), normalized distance and velocity, time in the upper, left
and front zones, prey capture, hunt duration and strike attempts, critical flicker fusion per
squid, and the ERG ratio as group means per stimulus frequency. `squid.zip` holds the authors'
shell and R scripts, the ExN50 statistics of the assembly, the RSEM count matrix (902,413
transcripts by 16 samples) and their R workspace `Squid.RData`, which holds the DESeq2, sva and
GSEA objects of the transcriptome analysis and the per-figure tables of Figures 1 to 3 and
Supplementary Figures 2 and 3. Not in the dataset: the 3-D tracks, ERG traces, per-squid ERG
spectra, seawater chemistry, body mass and mantle length, and the RNA-seq reads (in SRA).

**Outside data.** None is used. The transcriptomic claims are marked `data: elsewhere` (SRA
PRJNA1204452, TSA GLBY01000000) in the claims file; they are tested here on the count matrix and the
authors' DESeq2, sva and GSEA objects that this dataset holds, as the reads would have to be
re-assembled with Trinity (100 GB of memory in the authors' script) to start from SRA.

| Claim | Tested here |
|---|---|
| fig1b-metabolic-rate, fig1c-ammonia-excretion | yes, deposited rates |
| fig1d-blood-ph, fig1e-blood-pco2, fig1f-blood-bicarbonate | yes, deposited values |
| methods-body-size | blocked, data missing (no mass or mantle length) |
| stable5-seawater-chemistry | blocked, data missing (no seawater chemistry) |
| sfig2-distance-unchanged, fig2c-velocity-unchanged | yes, deposited per-squid values |
| fig2d-acute-upper-zone, fig2e-left-right-unchanged, fig2f-front-back-unchanged | yes, deposited zone percentages |
| stable3-acute-shallower | blocked, data missing (no depth or tracks) |
| fig2g-attack-willingness, fig2h-hunt-duration, fig2i-strike-attempts | yes |
| sfig3-prey-velocity-unchanged | yes, table `S3` of the R workspace |
| fig3c-ratio-declines | yes, deposited group means per frequency |
| sfig4a-amplitude-attenuation | blocked, data missing (no ERG traces) |
| fig3d-cff-unchanged, fig3d-cff-variance | yes, deposited CFF per squid |
| rnaseq-assembly | yes, except the mapping rate (not deposited) |
| fig4a-pca, sfig5b-acute-clusters-with-control | yes, the authors' batch-corrected VST matrix |
| fig4b to fig4fgh, chronic-nachr-subunits-down, optic-lobe-no-ion-regulation | yes, the authors' GSEA results |
''')

code(r'''
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

import squidoa as sq

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
pd.set_option("display.max_rows", 200)
pd.set_option("display.max_colwidth", 80)
warnings.filterwarnings("ignore", category=FutureWarning)
started = time.time()
print(f"Dryad {sq.DRYAD_ID}, version id {sq.DRYAD_VERSION}")
print("SHA-256 against Dryad's file list:", sq.check_files())
''')

md("## Data check")

code(r'''
print("Files in squid.zip (bytes):")
for name, size in sq.zip_names():
    print(f"  {size:>11,}  {name}")
csvs = {n: sq.read_csv(n) for n in sorted(sq.SHA256) if n.endswith(".csv")}
for name, df in csvs.items():
    print(f"\n{name}: {df.shape[0]} rows; columns {list(df.columns)}")
    if "Group" in df.columns:
        print("  rows per group:", df.Group.value_counts().reindex(sq.GROUPS + sorted(set(df.Group) - set(sq.GROUPS))).dropna().astype(int).to_dict())
    num = df.select_dtypes("number")
    if len(num.columns):
        print(num.describe().loc[["count", "min", "max"]].round(4).to_string())
''', ["sanity"])

md(r'''
Group sizes against the paper. Routine metabolic rate: 11, 9 and 6 squid (26), where the Fig. 1
legend gives n = 8 to 12 and Supplementary Table 1's ANOVA has 26 residual degrees of freedom, that
is 29 squid. Ammonia: 5, 9, 7 (21, as the ANOVA's df). Hemolymph: 7, 6, 9, as Supplementary Table 2.
Distance and velocity: 15, 8, 11, as Supplementary Table 3's df. Zone durations: 15, 9, 11, one
acute-OA squid more than the ANOVA's df (31 residual df, 34 squid). Prey capture: 46, 36, 22, as the
logistic regression's n. CFF: 3, 3, 6 (Fig. 3D, n = 3 to 6). The ERG file holds group means and
SDs per stimulus frequency, not values per squid. The README calls the hemolymph PCO2 column
"(atm)"; its header and values are in µatm (785.9 to 3861.9).
''')

code(r'''
t0 = time.time()
ws = sq.read_rdata({"behavior_and_physiology_data", "df", "svseq", "vst", "vstsva.adj", "vstsva.adj.limma",
                    "resNormal", "gse.Normal", "DB"})
print(f"read Squid.RData objects in {time.time() - t0:.0f} s")
bp = ws["behavior_and_physiology_data"]
fig_tables = {n: sq.df_from(v) for n, v in zip(bp.names(), bp.value)}
for n, d in fig_tables.items():
    gcol = "group" if "group" in d.columns else ("Group" if "Group" in d.columns else None)
    counts = d.dropna(subset=[c for c in d.columns if c not in ("group", "Group")][:1]).groupby(gcol).size().to_dict() if gcol else None
    print(f"{n}: {d.shape}, columns {list(d.columns)}, non-missing per group {counts}")
''', ["sanity"])

code(r'''
# The per-figure tables of the R workspace against the CSV files: same values per group?
pairs = {"F1B": ("Squid_RMR.csv", 0), "F1C": ("Squid_Ammonia.csv", 0), "F1D": ("Squid_Hemolymph.csv", 0),
         "F1E": ("Squid_Hemolymph.csv", 1), "F1F": ("Squid_Hemolymph.csv", 2), "F2C": ("Squid_normalized_total_distance.csv", 0),
         "S2": ("Squid_normalized_total_distance.csv", 0), "F2D": ("Squid_Behavioral_assessment.csv", 0),
         "F2E": ("Squid_Behavioral_assessment.csv", 1), "F2F": ("Squid_Behavioral_assessment.csv", 2),
         "F2H": ("Squid_Prey_Capture.csv", 2), "F2I": ("Squid_Prey_Capture.csv", 3), "F3D": ("Squid_CFF.csv", 0)}
for fig, (fname, ci) in pairs.items():
    d = fig_tables[fig].dropna()
    d["group"] = d["group"].replace({"Acute": "Acute-OA", "Chronic": "Chronic-OA"})
    c = csvs[fname]
    same = all(np.allclose(np.sort(d.loc[d.group == g, "value"]), np.sort(c.loc[c.Group == g, c.columns[ci]].dropna()))
               if (d.group == g).sum() == c.loc[c.Group == g, c.columns[ci]].notna().sum() else False for g in sq.GROUPS)
    print(f"{fig} against {fname} column {c.columns[ci]!r}: same values per group: {same}")
v = csvs["Squid_normalized_velocities.csv"]; dist = csvs["Squid_normalized_total_distance.csv"]
ratio = v.iloc[:, 0].to_numpy() / dist.iloc[:, 0].to_numpy()
print("\nvelocity / distance per squid (s^-1): min", ratio.min().round(8), "max", ratio.max().round(8), "-> 1/600 =", round(1 / 600, 8))
print("Groups in the same order in both files:", bool((v.Group.to_numpy() == dist.Group.to_numpy()).all()))
''', ["sanity"])

md(r'''
The R workspace's figure tables hold the same values as the CSV files (table `F2C`, which the
script plots as Figure 2C, holds the distances, not the velocities). Velocity is distance divided
by 600 s for every squid, so the two files carry one measure. The workspace's `S3` table is the
only copy of the prey shrimp velocities (Supplementary Fig. 3).
''')

code(r'''
cc = csvs["Carbonate_calibration.csv"]
alpha, pka = 0.0312, 6.10   # as printed in each row of Carbonate_calibration.csv
pco2 = cc["TCO2 (mM)"] / ((1 + 10 ** (cc["pH"] - pka)) * alpha) * 1e3
hco3 = cc["TCO2 (mM)"] - alpha * pco2 / 1e3
hem = csvs["Squid_Hemolymph.csv"]
print("Recomputed PCO2 (Eq. 1, alpha 0.0312, pKa1 6.10) minus Carbonate_calibration PCO2: max |diff| =",
      round(float(np.abs(pco2 - cc["PCO₂ (μatm)"]).max()), 2), "uatm")
print("Recomputed minus Squid_Hemolymph PCO2: max |diff| =", round(float(np.abs(pco2.to_numpy() - hem.iloc[:, 1].to_numpy()).max()), 3))
print("Recomputed [HCO3-] (Eq. 2) minus Squid_Hemolymph: max |diff| =", round(float(np.abs(hco3.to_numpy() - hem.iloc[:, 2].to_numpy()).max()), 4))
print("pH identical in both files:", bool(np.allclose(cc.pH.to_numpy(), hem.iloc[:, 0].to_numpy())))
''', ["sanity"])

md(r'''
The hemolymph PCO2 and [HCO3-] follow from pH and total CO2 by Eqs. 1 and 2 with αCO2 = 0.0312 and
pKa1 = 6.10, as the calibration file prints. The README attributes pKa1 6.10 to Truchot (1976)
(the Methods' ref. 65, Carcinus maenas hemolymph).
''')

# --- fig1b
md(r'''
## fig1b-metabolic-rate

> Routine metabolic rate was 16.9 (control), 18.9 (acute-OA) and 23.9 (chronic-OA) umol O2 per g
> fresh mass per h; chronic-OA squid had a 41% higher rate than controls, and acute-OA did not
> differ from either.

The deposit gives the rate per squid; untransformed one-way ANOVA and Tukey's test (Supplementary
Table 1).
''')
code(r'''
rmr = sq.by_group(csvs["Squid_RMR.csv"], csvs["Squid_RMR.csv"].columns[0])
print(sq.describe(rmr).round(3).to_string())
res = sq.oneway(rmr)
print(f"\nANOVA F({res['df1']},{res['df2']}) = {res['F']:.3f}, p = {res['p']:.6f}; SS treatment {res['SS_treat']:.1f}, residual {res['SS_resid']:.1f}, eta^2 = {res['eta2']:.3f}")
print("Paper: F(2,26) = 4.473, p = 0.021407; SS treatment 235.4, residual 684.2, total 919.6")
print("Tukey adjusted p:", {k: round(v, 4) for k, v in res["tukey"].items()})
inc = 100 * (rmr["Chronic-OA"].mean() / rmr["Control"].mean() - 1)
print(f"Chronic-OA over control: +{inc:.1f}%")
''', ["claim:fig1b-metabolic-rate"])
md(r'''
**Result: reproduced.** The means are 16.88, 18.93 and 23.88 µmol O2 g-1 h-1, chronic-OA 41.5%
above control; the ANOVA gives p = 0.0375 and Tukey's test separates control from chronic-OA (p =
0.030) but neither from acute-OA. The deposit holds 26 squid, three fewer than the paper's ANOVA
(F(2,23) = 3.80 here against F(2,26) = 4.473).
''')

md(r'''
## fig1c-ammonia-excretion

> Ammonia excretion was similar in control (3.3) and acute-OA (2.9 umol per g per h) squid and
> lower in chronic-OA squid (1.6), about 52% and 45% below control and acute-OA.

One-way ANOVA on log10 rates and Tukey's test (Supplementary Table 1).
''')
code(r'''
amm = sq.by_group(csvs["Squid_Ammonia.csv"], csvs["Squid_Ammonia.csv"].columns[0])
print(sq.describe(amm).round(3).to_string())
res = sq.oneway({g: np.log10(v) for g, v in amm.items()})
print(f"\nANOVA on log10: F({res['df1']},{res['df2']}) = {res['F']:.3f}, p = {res['p']:.6f}; SS treatment {res['SS_treat']:.4f}, residual {res['SS_resid']:.4f}; eta^2 = {res['eta2']:.3f}")
print("Paper: F(2,18) = 6.382, p = 0.008038; SS 0.3563 and 0.5025")
print("Tukey adjusted p (log10):", {k: round(v, 4) for k, v in res["tukey"].items()})
raw = sq.oneway(amm)
print(f"Variant, untransformed: F = {raw['F']:.3f}, p = {raw['p']:.4f}; Tukey", {k: round(v, 4) for k, v in raw["tukey"].items()})
m = {g: v.mean() for g, v in amm.items()}
print(f"Reduction of chronic-OA against control {100 * (1 - m['Chronic-OA'] / m['Control']):.1f}%, against acute-OA {100 * (1 - m['Chronic-OA'] / m['Acute-OA']):.1f}%")
''', ["claim:fig1c-ammonia-excretion"])
md(r'''
**Result: reproduced.** Means 3.34, 2.86 and 1.61 µmol g-1 h-1, reductions of 51.8% and 43.6%. The
ANOVA on log rates gives F(2,18) = 6.382, p = 0.008038, the paper's values; Tukey separates chronic-OA
from control (p = 0.009) and acute-OA (p = 0.038), not control from acute-OA (p = 0.52).
''')

md(r'''
## fig1d-blood-ph, fig1e-blood-pco2, fig1f-blood-bicarbonate

> Blood pH was higher in chronic-OA squid (7.17) than in controls (7.09); acute-OA squid were
> intermediate (7.15) and differed from neither.
>
> Blood PCO2 rose 1.5-fold under acute-OA (1583.8 uatm) and 2.6-fold under chronic-OA (2778.7 uatm)
> from 1057.4 uatm in controls, and all three groups differ.
>
> Blood [HCO3-] rose 1.7-fold under acute-OA (5.90 mmol/l) and 3.1-fold under chronic-OA (11.08
> mmol/l) from 3.56 mmol/l in controls, and all three groups differ.

PCO2 and [HCO3-] as deposited. Welch's ANOVA and Dunnett's T3 (Methods, Statistics; Supplementary
Table 2), implemented in `squidoa.welch_anova` and `squidoa.dunnett_t3`.
''')
code(r'''
blood = {}
for col, key in zip(hem.columns[:3], ["pH", "PCO2", "HCO3"]):
    g = sq.by_group(hem, col)
    blood[key] = g
    w = sq.welch_anova(list(g.values()))
    print(f"--- {col}")
    print(sq.describe(g).round(3).to_string())
    print(f"Welch's ANOVA W = {w['W']:.3f}, df 2, {w['df2']:.3f}, p = {w['p']:.3g}")
    print(sq.dunnett_t3(g).round(4).to_string(index=False))
    if key != "pH":
        m = {k: v.mean() for k, v in g.items()}
        print(f"fold change acute/control {m['Acute-OA'] / m['Control']:.2f}, chronic/control {m['Chronic-OA'] / m['Control']:.2f}")
print("\nPaper (Supplementary Table 2): pH W = 5.983, df 2, 9.196, p = 0.00965; PCO2 W = 27.653, df 2, 9.379; HCO3 W = 39.545, df 2, 12.59")
''', ["claim:fig1d-blood-ph", "claim:fig1e-blood-pco2", "claim:fig1f-blood-bicarbonate"])
md(r'''
**Result: fig1d-blood-ph reproduced.** Means 7.092, 7.145 and 7.175 (n = 7, 6, 9); Welch's ANOVA p
= 0.019 (W = 6.35 against the paper's 5.983, with the same df 2, 9.196); Dunnett's T3 separates
control from chronic-OA (p = 0.017) and neither pair with acute-OA (p = 0.46 and 0.86).

**Result: fig1e-blood-pco2 reproduced.** Means 1057.4, 1583.8 and 2778.7 µatm, fold changes 1.50
and 2.63; Welch's p = 2.2e-05; all three pairs differ (p = 0.014, 3e-05 and 0.0008). This
Welch's W (29.8, df 2, 12.0) differs from the paper's (27.653, df 2, 9.379) on the same values.

**Result: fig1f-blood-bicarbonate reproduced.** Means 3.56, 5.90 and 11.08 mmol/l, fold changes
1.66 and 3.11; Welch's p = 2.5e-06; all pairs differ (p ≤ 0.0008).
''')

md(r'''
## methods-body-size, stable5-seawater-chemistry, stable3-acute-shallower

Blocked, data missing. No file holds fresh mass or mantle length, seawater pH or PCO2 (the
carbonate calculation file covers hemolymph only), or the depth of the squid (only the percentage
of time in each zone is deposited; the 3-D tracks are not).
''')
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python -c "
import squidoa as s, numpy as np
b=s.read_csv('Squid_Behavioral_assessment.csv')
for c in b.columns[:3]:
  g=s.by_group(b,c); r=s.oneway(g); print(c, 'all9', round(r['SS_treat'],1), round(r['F'],4), [round(x.mean(),1) for x in g.values()])
  a=g['Acute-OA']
  for i in range(len(a)):
    gg=dict(g); gg['Acute-OA']=np.delete(a,i); r=s.oneway(gg); print('  drop',i,a[i], round(r['SS_treat'],1), round(r['F'],4), round(gg['Acute-OA'].mean(),1))
d=s.read_csv('Squid_normalized_total_distance.csv'); g=s.by_group(d,d.columns[0]); print(s.describe(g)); print(stats.kruskal(*g.values()) if False else '')
from scipy import stats; print(stats.kruskal(*g.values()))
"
```

```
Duration in Upper zone (%) all9 25222.0 12.1413 [np.float64(30.0), np.float64(83.1), np.float64(14.7)]
  drop 0 99.0 21782.1 10.2453 81.1
  drop 1 100.0 21694.1 10.2153 81.0
  drop 2 0.6 31374.6 19.012 93.4
  drop 3 91.43333 22454.1 10.4957 82.1
  drop 4 100.0 21694.1 10.2153 81.0
  drop 5 99.56667 21732.2 10.2282 81.1
  drop 6 97.76667 21890.9 10.2832 81.3
  drop 7 100.0 21694.1 10.2153 81.0
  drop 8 59.63333 25397.6 12.0689 86.0
Duration in Left zone (%) all9 456.8 0.27 [np.float64(55.8), np.float64(48.2), np.float64(57.1)]
  drop 0 41.3 337.0 0.1933 49.1
  drop 1 52.93333 480.0 0.2751 47.6
  drop 2 11.06667 86.4 0.0525 52.9
  drop 3 99.5 1311.4 0.843 41.8
  drop 4 32.73333 248.3 0.1436 50.1
  drop 5 67.06667 688.5 0.4001 45.9
  drop 6 80.6 924.0 0.5531 44.2
  drop 7 47.36667 408.3 0.2338 48.3
  drop 8 1.333333 42.9 0.027 54.1
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/nb2.py <<'PYEOF'
md(r'''
## sfig2-distance-unchanged

> Total distance travelled during the 10 min exploration did not differ between groups (132.9,
> 124.4 and 147.3 mantle lengths for control, acute-OA and chronic-OA).

The deposit gives the normalized distance per squid (the 3-D tracks are not deposited, so Eq. 3 and
the handling of untracked samples cannot be applied). Kruskal-Wallis at p < 0.05 (Supplementary
Table 3).
''')
code(r'''
dist_g = sq.by_group(dist, dist.columns[0])
print(sq.describe(dist_g).round(2).to_string())
kw = stats.kruskal(*dist_g.values())
n = sum(len(v) for v in dist_g.values())
print(f"\nKruskal-Wallis H = {kw.statistic:.4f}, p = {kw.pvalue:.6f}; epsilon^2 = {kw.statistic / (n - 1):.4f}")
print("Paper: KW = 0.4124, p = 0.813689")
''', ["claim:sfig2-distance-unchanged"])
md(r'''
**Result: reproduced.** Means 132.9, 124.4 and 147.4 mantle lengths (15, 8, 11 squid);
Kruskal-Wallis H = 0.4124, p = 0.8137, the paper's values; effect size ε² = 0.013.
''')

md(r'''
## fig2c-velocity-unchanged

> Mean swimming velocity during the 10 min exploration did not differ between groups (0.2, 0.21
> and 0.25 mantle lengths per s for control, acute-OA and chronic-OA).

Velocity per squid as deposited, which is the distance over 600 s (data check). Kruskal-Wallis at
p < 0.05. The velocity file has 8 acute-OA squid, so no 9th squid is shown.
''')
code(r'''
vel_g = sq.by_group(v, v.columns[0])
print(sq.describe(vel_g).round(4).to_string())
kw = stats.kruskal(*vel_g.values())
print(f"\nKruskal-Wallis H = {kw.statistic:.4f}, p = {kw.pvalue:.6f}; epsilon^2 = {kw.statistic / (sum(len(x) for x in vel_g.values()) - 1):.4f}")
print("Paper: KW = 0.4124, p = 0.813689")
''', ["claim:fig2c-velocity-unchanged"])
md(r'''
**Result: reproduced.** Means 0.222, 0.207 and 0.246 mantle lengths/s; the control mean rounds to
0.2 and lies within 0.15 to 0.25. Kruskal-Wallis H = 0.4124, p = 0.8137.
''')

md(r'''
## fig2d-acute-upper-zone, fig2e-left-right-unchanged, fig2f-front-back-unchanged

> Acute-OA squid spent most of the exploration in the upper half of the arena (86.0%), more than
> control (30.0%) and chronic-OA (14.7%) squid, which did not differ from each other.
>
> Acidification did not change the preference for the left or right side of the arena (55.8%,
> 54.1% and 57.1% of the trial on the left for control, acute-OA and chronic-OA).
>
> Acidification did not change the preference for the front or back of the arena (58.3%, 80.0%
> and 66.1% of the trial near the front wall for control, acute-OA and chronic-OA).

The deposit gives the percentage per squid; the zone boundaries and the denominator (readings (a)
and (b) of the criteria) were applied before deposit and cannot be varied here. The file has 9
acute-OA squid where the paper's ANOVAs have 8 (31 residual df). Each acute-OA squid is left out in
turn, and the one whose exclusion gives the paper's sums of squares (Supplementary Table 3) is
taken as the paper's set; all 9 are shown as a variant. Untransformed one-way ANOVA and Tukey's test;
for left and front, log10 as a variant (zeros left out).
''')
code(r'''
beh = csvs["Squid_Behavioral_assessment.csv"]
paper_ss = {"Duration in Upper zone (%)": 25398, "Duration in Left zone (%)": 42.93, "Duration in Front zone (%)": 2437}
acute_rows = beh.index[beh.Group == "Acute-OA"]
rows = []
for drop in acute_rows:
    r = {"left_out_row": drop}
    for col in paper_ss:
        g = sq.by_group(beh.drop(index=drop), col)
        r[col.split(" ")[2] + "_SS"] = round(sq.oneway(g)["SS_treat"], 1)
    rows.append(r)
loo = pd.DataFrame(rows)
print("Treatment sums of squares with one acute-OA squid left out (paper: upper 25398, left 42.93, front 2437):")
print(loo.to_string(index=False))
dist_to_paper = sum((loo[c.split(" ")[2] + "_SS"] - s) ** 2 / s ** 2 for c, s in paper_ss.items())
paper_drop = int(loo.left_out_row[dist_to_paper.idxmin()])
print("\nLeft out to match the paper: row", paper_drop, beh.loc[paper_drop].to_dict())
''', ["claim:fig2d-acute-upper-zone", "finding-zone-extra-acute-squid"])
code(r'''
zone_res = {}
for col, claim in [("Duration in Upper zone (%)", "fig2d"), ("Duration in Left zone (%)", "fig2e"), ("Duration in Front zone (%)", "fig2f")]:
    for label, data in [("paper set (8 acute-OA)", beh.drop(index=paper_drop)), ("all 9 acute-OA", beh)]:
        g = sq.by_group(data, col)
        r = sq.oneway(g)
        zone_res[(claim, label)] = r
        d = sq.describe(g)
        print(f"--- {col}, {label}")
        print("  mean:", d["mean"].round(1).to_dict(), " SD:", d["sd"].round(1).to_dict(), " n:", d["n"].astype(int).to_dict())
        print(f"  ANOVA F({r['df1']},{r['df2']}) = {r['F']:.4f}, p = {r['p']:.6f}, SS treatment {r['SS_treat']:.1f}, residual {r['SS_resid']:.1f}, eta^2 = {r['eta2']:.3f}")
        print("  Tukey adjusted p:", {k: round(x, 4) for k, x in r["tukey"].items()})
        if claim != "fig2d":
            lg = {k: np.log10(x[x > 0]) for k, x in g.items()}
            rl = sq.oneway(lg)
            print(f"  variant log10 (zeros left out: {sum(int((x == 0).sum()) for x in g.values())}): F = {rl['F']:.4f}, p = {rl['p']:.4f}")
print("\nPaper: upper F(2,31) = 12.07, p = 0.000133; left F = 0.02705, p = 0.973; front F = 1.326, p = 0.280")
''', ["claim:fig2d-acute-upper-zone", "claim:fig2e-left-right-unchanged", "claim:fig2f-front-back-unchanged"])
md(r'''
**Result: fig2d-acute-upper-zone reproduced.** Leaving out the ninth acute-OA squid of the file
(59.6% upper, 1.3% left, 6.7% front) gives the paper's three sums of squares (25397.6, 42.9,
2436.7), and with it means of 30.0, 86.0 and 14.7%, F(2,31) = 12.07, p = 0.00013; Tukey separates
acute-OA from control and chronic-OA, not control from chronic-OA. With all 9 acute-OA squid the
acute-OA mean is 83.1% and the pattern is the same.

**Result: fig2e-left-right-unchanged reproduced.** Means 55.8, 54.1 and 57.1%; F(2,31) = 0.027,
p = 0.97 (the paper's values; with all 9, F = 0.27, p = 0.77).

**Result: fig2f-front-back-unchanged reproduced.** Means 58.3, 80.0 and 66.1%; F(2,31) = 1.326, p =
0.28 (with all 9, F = 0.52, p = 0.60).
''')

md(r'''
## fig2g-attack-willingness

> Acidified conditions reduced the proportion of squid that attacked prey (logistic regression, pH
> p = 0.0422) with no effect of exposure duration (p = 0.2461); acute-OA and chronic-OA squid were
> 64.7% and 42.3% less likely to attack than controls.

Logistic regression (binomial GLM, logit) of attack on pH and exposure time, readings (a) to (c) of
the criterion. Reading (c) uses the measured tank pH of Supplementary Table 5 (8.20, 7.81, 7.80),
paper values used as covariate codes.
''')
code(r'''
pc = csvs["Squid_Prey_Capture.csv"]
pc = pc.rename(columns={pc.columns[0]: "attack", pc.columns[2]: "hunt_s", pc.columns[3]: "attempts"})
counts = pc.groupby("Group").attack.agg(["sum", "count"]).reindex(sq.GROUPS)
print(counts.rename(columns={"sum": "attacked", "count": "squid"}).to_string())
prop = counts["sum"] / counts["count"]
print("\nReduction against control:", {g: round(100 * (1 - prop[g] / prop["Control"]), 1) for g in sq.GROUPS[1:]})
codings = {
    "(a) nominal pH, days in condition 90/7/90": ({"Control": 8.2, "Acute-OA": 7.8, "Chronic-OA": 7.8}, {"Control": 90, "Acute-OA": 7, "Chronic-OA": 90}),
    "(b) nominal pH, days of acidification 0/7/90": ({"Control": 8.2, "Acute-OA": 7.8, "Chronic-OA": 7.8}, {"Control": 0, "Acute-OA": 7, "Chronic-OA": 90}),
    "(c) tank pH 8.20/7.81/7.80, days 90/7/90": ({"Control": 8.20, "Acute-OA": 7.81, "Chronic-OA": 7.80}, {"Control": 90, "Acute-OA": 7, "Chronic-OA": 90}),
    "(c) tank pH 8.20/7.81/7.80, days 0/7/90": ({"Control": 8.20, "Acute-OA": 7.81, "Chronic-OA": 7.80}, {"Control": 0, "Acute-OA": 7, "Chronic-OA": 90}),
}
for label, (ph, days) in codings.items():
    d = pc.assign(pH=pc.Group.map(ph), time=pc.Group.map(days))
    fit = smf.glm("attack ~ pH + time", data=d, family=sm.families.Binomial()).fit()
    print(f"\n{label}")
    print(fit.summary2().tables[1][["Coef.", "Std.Err.", "z", "P>|z|"]].round(6).to_string())
    print(f"null deviance {fit.null_deviance:.2f} on {int(fit.df_model + fit.df_resid)} df, residual {fit.deviance:.2f} on {int(fit.df_resid)} df, AIC {fit.aic:.2f}, ROC area {sq.auc(d.attack.to_numpy(), fit.fittedvalues.to_numpy()):.4f}")
print("\nPaper (Supplementary Table 4): pH 2.734246 (SE 1.345676, p = 0.0422), time 0.008351 (SE 0.00762, p = 0.2461); residual deviance 127.58; ROC area 0.6992")
''', ["claim:fig2g-attack-willingness"])
md(r'''
**Result: reproduced.** 29 of 46, 8 of 36 and 8 of 22 squid attacked, reductions of 64.7% and
42.3%. Under reading (a) the pH coefficient is 2.734 (p = 0.042) and the time coefficient 0.00835
(p = 0.246), with residual deviance 127.58 and ROC area 0.699, as the paper prints; the intercept is
-22.64 against the printed 22.36. Lower pH lowers the odds of attack.
''')

md(r'''
## fig2h-hunt-duration

> Acute-OA squid took about 2.5 times longer to capture prey than controls (262.2 against 106.7 s,
> p = 0.03); chronic exposure did not affect hunt duration.

One-way ANOVA on log10 durations and Tukey's test (Supplementary Table 4), squid that attacked.
''')
code(r'''
hunt = sq.by_group(pc[pc.attack == 1], "hunt_s")
print(sq.describe(hunt).round(1).to_string())
r = sq.oneway({g: np.log10(x) for g, x in hunt.items()})
print(f"\nANOVA on log10: F({r['df1']},{r['df2']}) = {r['F']:.3f}, p = {r['p']:.4f}; SS {r['SS_treat']:.3f} and {r['SS_resid']:.3f}; eta^2 = {r['eta2']:.3f}")
print("Paper: F(2,42) = 3.372, p = 0.0439; SS 2.374 and 14.79 (on the log10 scale, these differ; see below)")
print("Tukey adjusted p (log10):", {k: round(x, 4) for k, x in r["tukey"].items()})
rn = sq.oneway({g: np.log(x) for g, x in hunt.items()})
print(f"Natural log: SS {rn['SS_treat']:.3f} and {rn['SS_resid']:.3f}, F = {rn['F']:.3f}")
raw = sq.oneway(hunt)
print(f"Variant, untransformed: F = {raw['F']:.3f}, p = {raw['p']:.4f}; Tukey", {k: round(x, 4) for k, x in raw["tukey"].items()})
print(f"Fold change acute/control: {hunt['Acute-OA'].mean() / hunt['Control'].mean():.2f}")
''', ["claim:fig2h-hunt-duration"])

md(r'''
## fig2i-strike-attempts

> Most squid struck prey successfully within 1 to 2 attempts, strike attempts did not differ
> between groups, and every squid that attempted to hunt captured its prey.
''')
code(r'''
att = pc[pc.attack == 1]
frac = (att.attempts <= 2).groupby(att.Group).mean().reindex(sq.GROUPS)
print(f"Attacking squid: {len(att)}; with 1 or 2 attempts: {(att.attempts <= 2).sum()} ({100 * (att.attempts <= 2).mean():.1f}%)")
print("Per group:", frac.round(3).to_dict())
print("Attempts per group:", {g: np.bincount(att.loc[att.Group == g, "attempts"].astype(int)).tolist() for g in sq.GROUPS})
print("Squid with attempts but no capture (attack 0 with attempts recorded):", int(pc[(pc.attack == 0) & pc.attempts.notna()].shape[0]),
      "; captures with no duration:", int(att.hunt_s.isna().sum()))
kw = stats.kruskal(*[att.loc[att.Group == g, "attempts"] for g in sq.GROUPS])
print(f"Kruskal-Wallis H = {kw.statistic:.3f}, p = {kw.pvalue:.4f} (paper: 2.568, p = 0.2769)")
''', ["claim:fig2i-strike-attempts"])
md(r'''
**Result: reproduced.** 37 of 45 attacking squid (82%) needed 1 or 2 attempts; Kruskal-Wallis H =
2.568, p = 0.277, the paper's values. The file codes squid as captured (1) or not (0), and every
squid with recorded attempts has a capture time; it has no record of squid that struck and missed
for good, so "every squid that attempted captured" holds as far as the file can show it.
''')

md(r'''
## sfig3-prey-velocity-unchanged

> The velocity of the prey shrimp was not affected by CO2 treatment, time (10 and 20 min) or their
> interaction.

Only table `S3` of the R workspace holds these values. Ordinary two-way ANOVA (pH by time; Methods,
Statistics), type III sums of squares as GraphPad Prism reports for unequal cells, type II as a
variant.
''')
code(r'''
s3 = fig_tables["S3"]
print(s3.round(4).to_string())
print("\nNon-missing per column:", s3.notna().sum().to_dict())
a, b = s3["pH 8.1 10-20 Min"].dropna().to_numpy(), s3["pH 7.8 10-20 Min"].dropna().to_numpy()
print("pH 8.1 10-20 Min and pH 7.8 10-20 Min identical:", len(a) == len(b) and bool(np.array_equal(a, b)))
''', ["finding-shrimp-duplicate-column"])
code(r'''
long = s3.melt(var_name="cond", value_name="velocity").dropna()
long["pH"] = long.cond.str.slice(3, 6)
long["time"] = long.cond.str.slice(7)
print(long.groupby(["pH", "time"]).velocity.agg(["count", "mean", "sem"]).round(4).to_string())
for label, d in [("as deposited", long), ("pH 7.8 10-20 Min left out (a copy of pH 8.1 10-20 Min)", long[long.cond != "pH 7.8 10-20 Min"])]:
    for typ in (3, 2):
        fit = smf.ols("velocity ~ C(pH, Sum) * C(time, Sum)" if typ == 3 else "velocity ~ C(pH) * C(time)", data=d).fit()
        tab = sm.stats.anova_lm(fit, typ=typ)
        print(f"\n{label}, type {typ['III' if False else 0] if False else ('III' if typ == 3 else 'II')}:")
        print(tab.round(4).to_string())
''', ["claim:sfig3-prey-velocity-unchanged"])
md(r'''
**Result: reproduced.** On the table as deposited no term has p < 0.05 (two-way ANOVA, type III
and type II). The CO2 10 to 20 min column is a copy of the control 10 to 20 min column (8 values,
identical), so the deposited data cannot show what the CO2 shrimp did at 20 min; leaving that
column out, no term has p < 0.05 either. A repeated-measures variant is not run: no shrimp
identifier links the columns, and the CO2 columns hold 11 and 8 values.
''')
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open('nb2.py').read()
s=s.replace("""print(f"\\n{label}, type {typ['III' if False else 0] if False else ('III' if typ == 3 else 'II')}:")""","""print(f"\\n{label}, type {'III' if typ == 3 else 'II'}:")""")
open('nb2.py','w').write(s)
EOF
grep -n "type {" nb2.py
```

```
225:        print(f"\n{label}, type {'III' if typ == 3 else 'II'}:")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/nb3.py <<'PYEOF'
md(r'''
## fig3c-ratio-declines

> As stimulus frequency increased, the ratio of maximum response frequency to stimulus frequency
> decreased in all three groups, markedly above 40 Hz.

The deposit holds the group mean (and SD) of the ratio per stimulus frequency, not the per-squid
spectra, so the criterion is applied to these deposited means. Frequencies with no value in a group
are left out of that group.
''')
code(r'''
erg = csvs["Squid_ERG.csv"]
wide = erg.pivot(index="Frequency", columns="Group", values="mean_value")[sq.GROUPS]
print(wide.round(3).to_string())
print("\nRows with an SD (more than one squid):", erg.sd_value.notna().sum(), "of", len(erg), "; SD missing where only one squid?")
for g in sq.GROUPS:
    s = wide[g].dropna()
    ref = s.loc[20]
    above = s[s.index > 40]
    not_below = above[above >= ref]
    hi = s.index.max()
    print(f"\n{g}: ratio at 20 Hz {ref:.4f}; frequencies above 40 Hz with a value {list(above.index)}")
    print(f"  not below the 20 Hz value: {not_below.round(4).to_dict()}")
    print(f"  at the highest frequency ({hi} Hz) {s.loc[hi]:.4f}; lowest {s.min():.4f} at {s.idxmin()} Hz; difference {s.loc[hi] - s.min():.4f}")
    print(f"  mean ratio up to 50 Hz {s[s.index <= 50].mean():.3f}, above 50 Hz {s[s.index > 50].mean():.3f}")
''', ["claim:fig3c-ratio-declines"])
md(r'''
**Result: not reproduced.** In no group is the mean ratio below its 20 Hz value at every frequency
above 40 Hz: control is at 0.998 (45 Hz) and 0.990 (50 Hz) against 0.977 at 20 Hz, acute-OA at 0.998
(45 Hz) and 1.062 (57.5 Hz), chronic-OA at 1.039 (47 Hz). In control and acute-OA the ratio stays
near 1 to 45 or 50 Hz and falls to 0.28 to 0.51 above 50 Hz; chronic-OA falls at 40 and 42 Hz
(0.39, 0.37) and returns near 1 at 47 Hz. The highest frequency is lowest or within 0.1 of it in
control and acute-OA, not in chronic-OA (0.361 against 0.252). The decline the statement describes
is present above 50 Hz in the deposited means; the criterion's "every frequency above 40 Hz" is not met.
''')

md(r'''
## sfig4a-amplitude-attenuation

Blocked, data missing: the ERG traces and spectra are not deposited; `Squid_ERG.csv` holds only the
ratio of maximum response frequency to stimulus frequency.

## fig3d-cff-unchanged

> Critical flicker fusion frequency did not differ between treatments (control 50.8, acute-OA 50.8,
> chronic-OA 47.7 Hz).

Reading (b) of the criterion: the CFF the deposit gives per squid (3, 3 and 6 squid). Reading (a),
CFF for every squid from its ratios, cannot be run, as the per-squid ratios are not deposited. As a
reference, the highest frequency at which the deposited group mean ratio is at least 0.9 is printed.
One-way ANOVA at p < 0.05, with Tukey's test.
''')
code(r'''
cff_df = csvs["Squid_CFF.csv"]
cff = sq.by_group(cff_df, cff_df.columns[0])
d = sq.describe(cff)
print(d.round(3).to_string())
r = sq.oneway(cff)
print(f"\nANOVA F({r['df1']},{r['df2']}) = {r['F']:.3f}, p = {r['p']:.4f}; eta^2 = {r['eta2']:.3f}")
print("Tukey adjusted p:", {k: round(x, 4) for k, x in r["tukey"].items()})
kw = stats.kruskal(*cff.values())
print(f"Variant, Kruskal-Wallis H = {kw.statistic:.3f}, p = {kw.pvalue:.4f}")
for g in sq.GROUPS:
    s = wide[g].dropna()
    print(f"{g}: highest frequency with group mean ratio >= 0.9: {s[s >= 0.9].index.max()} Hz")
''', ["claim:fig3d-cff-unchanged"])
md(r'''
**Result: reproduced.** Means 50.7, 50.7 and 47.7 Hz (n = 3, 3, 6); one-way ANOVA F(2,9) = 0.37, p =
0.70, so no difference is found.
''')

md(r'''
## fig3d-cff-variance

> The standard deviation of CFF was 4 to 5 times higher in the acidified groups than in controls.

Sample SDs (n - 1) of the deposited CFF per squid.
''')
code(r'''
sd = d["sd"]
print("SD:", sd.round(3).to_dict())
print(f"SD ratio acute-OA/control {sd['Acute-OA'] / sd['Control']:.2f}, chronic-OA/control {sd['Chronic-OA'] / sd['Control']:.2f} (criterion: 3.6 to 5.5)")
lev = stats.levene(*cff.values(), center="median")
print(f"Not judged: Brown-Forsythe test of equal variances, p = {lev.pvalue:.3f}")
''', ["claim:fig3d-cff-variance"])
md(r'''
**Result: reproduced.** SDs 1.15, 6.03 and 5.32 Hz; ratios 5.22 (acute-OA) and 4.60 (chronic-OA),
both in 3.6 to 5.5. With 3 control squid the control SD rests on three values.
''')

md(r'''
## rnaseq-assembly

> The de novo transcriptome assembly (...) had 902,413 transcripts, an N50 of 476 bp overall and
> 2038 bp for the top 78% of expressed transcripts, read mapping rates above 97% (mean 99.51%), and
> 69,368 transcripts after expression filtering.

The transcript count is that of the deposited RSEM matrix; E78N50 and N50 are read from the
deposited `ExN50.stats` (Trinity's contig_ExN50_statistic.pl output, `Bash_scripts.sh`), as the
assembly FASTA is not in the dataset. The filter is applied to the 15 optic lobe columns of the
matrix as the deposited `R_scritps.Rmd` does it (reading (a): rows with a non-zero mean, rounded,
then at least 10 counts in at least 3 samples); reading (b) and the 12 samples of the three groups
alone are variants. Mapping rates are not deposited.
''')
code(r'''
header, n_rows = sq.count_matrix_rows()
print("RSEM.isoform.counts.matrix columns:", header)
print("transcripts (rows):", n_rows)
exn50 = pd.read_csv(pd.io.common.StringIO(sq.zip_text("ExN50.stats")), sep="\t")
print(exn50.columns.tolist(), len(exn50), "rows")
print("E78N50:", exn50.loc[exn50.Ex == 78, "ExN50"].item(), " maximum ExN50 from Ex 25 on:", exn50.loc[exn50.Ex >= 25, "ExN50"].max(),
      " N50 at Ex 100:", round(exn50.loc[exn50.Ex == 100, "ExN50"].item(), 1), " num_genes at Ex 100:", exn50.loc[exn50.Ex == 100, "num_genes"].item())
counts = sq.read_count_matrix()
ol = [c for c in counts.columns if "_OL" in c or "-OL" in c]
raw = counts[ol]
kept_mean = raw[raw.mean(axis=1) != 0]
rounded = np.round(kept_mean)
filt_a = int(((rounded >= 10).sum(axis=1) >= 3).sum())
filt_b = int(((kept_mean.sum(axis=1) >= 10) & ((kept_mean > 0).sum(axis=1) >= 3)).sum())
grp12 = [c for c in ol if not c.startswith("Re_")]
r12 = np.round(raw[grp12][raw[grp12].mean(axis=1) != 0])
filt_12 = int(((r12 >= 10).sum(axis=1) >= 3).sum())
print(f"\nOptic lobe columns: {len(ol)}; rows with non-zero mean {len(kept_mean)}")
print(f"(a) at least 10 counts in at least 3 of 15 samples: {filt_a}")
print(f"(b) total >= 10 and detected in >= 3 samples: {filt_b}")
print(f"variant, (a) on the 12 samples of the three groups: {filt_12}")
res_n = {k: len(sq.s4_dataframe(v)) for k, v in zip(ws["resNormal"].names(), ws["resNormal"].value)}
print("Rows of the deposited DESeq2 results (resNormal):", res_n)
del counts, raw, kept_mean, rounded, r12
''', ["claim:rnaseq-assembly"])
md(r'''
**Result: reproduced, except the mapping rate, which is not in the dataset.** 902,413 transcripts,
E78N50 2038 bp and N50 475.5 bp (476) in the deposited statistics, and 69,368 transcripts after the
filter of the deposited script (reading (a)), the row count of the authors' DESeq2 results.
''')
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/nb4.py <<'PYEOF'
md(r'''
## fig4a-pca

> In a PCA of optic lobe transcriptomes, acute-OA samples lay near controls along PC1 (35% of
> variance), while chronic-OA samples diverged along PC1 and PC2 (15%).

The authors' objects: `vstsva.adj.limma` is the VST of the DESeq2 fit with design ~SV1 + SV2 +
condition, with the two surrogate variables of `svseq` removed by limma's removeBatchEffect
(reading (a); `R_scritps.Rmd`, "Limma adjust for the visualization"). The cell first checks that
the deposited matrix equals that removal applied to `vstsva.adj`. Reading (b), the known batches
removed the same way, is applied to `vst` (the VST of the fit with design ~condition). PCA as
DESeq2's plotPCA (500 most variable rows, centred, unscaled). The script runs plotPCA on all 15
samples and keeps the 12 of the three groups (`x[1:12,]`), and also calls it on the 12 alone; both
are shown. The control spread on a PC is the range of the control samples on it.
''')
code(r'''
coldata = sq.df_from(ws["df"])
limma_mat = sq.s4_assay(ws["vstsva.adj.limma"])
adj_mat = sq.s4_assay(ws["vstsva.adj"])
vst_mat = sq.s4_assay(ws["vst"])
print("VST matrices (rows x samples):", limma_mat.shape, adj_mat.shape, vst_mat.shape)
print("samples:", list(limma_mat.columns))
print(coldata.to_string())
sv = sq.matrix(ws["svseq"]["sv"]).to_numpy()
print("surrogate variables:", sv.shape[1], "(n.sv =", int(ws["svseq"]["n.sv"].value[0]), ")")
conds = pd.Categorical(coldata["condition"], categories=["Ct_8.1", "pH_7.8", "pH_7.8C", "Re_8.1"])
design = pd.get_dummies(conds, drop_first=True).astype(float).to_numpy()
design = np.column_stack([np.ones(len(conds)), design])
check = sq.remove_batch_effect(adj_mat, design, sv)
print("max |deposited limma matrix - removeBatchEffect(vstsva.adj, ~condition, SVs)|:", float(np.abs(check.to_numpy() - limma_mat.to_numpy()).max()))
batch = np.where(coldata["batch"].to_numpy() == 1, 1.0, -1.0)[:, None]   # contr.sum coding, as removeBatchEffect(batch=)
mat_b = sq.remove_batch_effect(vst_mat, design, batch)
label = {"Ct_8.1": "Control", "pH_7.8": "Acute-OA", "pH_7.8C": "Chronic-OA", "Re_8.1": "Re_8.1"}
groups15 = coldata["condition"].map(label).to_numpy()
''', ["claim:fig4a-pca"])
code(r'''
def pca_summary(mat, cols, name):
    scores, frac = sq.plotpca(mat[cols])
    g = pd.Series(groups15, index=mat.columns)[cols]
    sc = scores.loc[cols, ["PC1", "PC2"]]
    cen = sc.groupby(g.to_numpy()).mean()
    ctrl = sc[g.to_numpy() == "Control"]
    spread = ctrl.max() - ctrl.min()
    keep = g.to_numpy() != "Re_8.1"
    out = {"reading": name, "PC1 %": round(100 * frac[0], 1), "PC2 %": round(100 * frac[1], 1),
           "|acute-control| PC1": abs(cen.loc["Acute-OA", "PC1"] - cen.loc["Control", "PC1"]),
           "|chronic-control| PC1": abs(cen.loc["Chronic-OA", "PC1"] - cen.loc["Control", "PC1"]),
           "|chronic-control| PC2": abs(cen.loc["Chronic-OA", "PC2"] - cen.loc["Control", "PC2"]),
           "control range PC1": spread["PC1"], "control range PC2": spread["PC2"]}
    return out, sc[keep].assign(group=g.to_numpy()[keep])

all15 = list(limma_mat.columns)
first12 = all15[:12]
rows, plots = [], {}
for name, mat, cols in [("(a) SVs removed, PCA on 15 (script)", limma_mat, all15), ("(a) SVs removed, PCA on 12", limma_mat, first12),
                        ("(b) batch removed, PCA on 15", mat_b, all15), ("(b) batch removed, PCA on 12", mat_b, first12)]:
    o, sc = pca_summary(mat, cols, name)
    rows.append(o)
    plots[name] = sc
pca_tab = pd.DataFrame(rows).set_index("reading")
pca_tab["acute nearer control on PC1"] = pca_tab["|acute-control| PC1"] < pca_tab["|chronic-control| PC1"]
pca_tab["chronic separated PC1"] = pca_tab["|chronic-control| PC1"] > pca_tab["control range PC1"]
pca_tab["chronic separated PC2"] = pca_tab["|chronic-control| PC2"] > pca_tab["control range PC2"]
print(pca_tab.round(2).T.to_string())
print("\nPaper: PC1 35%, PC2 15%")
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
for ax, name in zip(axes, ["(a) SVs removed, PCA on 15 (script)", "(a) SVs removed, PCA on 12"]):
    sc = plots[name]
    for g, c in zip(sq.GROUPS, ["tab:green", "tab:orange", "tab:purple"]):
        ax.scatter(sc.loc[sc.group == g, "PC1"], sc.loc[sc.group == g, "PC2"], label=g, color=c)
    ax.set_title(name, fontsize=9); ax.set_xlabel("PC1"); ax.set_ylabel("PC2")
axes[0].legend(fontsize=8)
plt.tight_layout(); plt.show()
print("All points are within the axes.")
''', ["claim:fig4a-pca"])

md(r'''
## sfig5b-acute-clusters-with-control

> After batch-effect removal, acute-OA samples clustered closer to controls than chronic-OA samples
> did.

Euclidean distances between the 12 samples on the batch-corrected matrix, all rows, as the
script's "Supplementary Figure S5A" chunk computes them (`dist(t(assay(vstsva.adj.limma)[,1:12]))`);
reading (b) on the batch-removed matrix as a variant.
''')
code(r'''
from scipy.spatial.distance import pdist, squareform
for name, mat in [("(a) SVs removed", limma_mat), ("(b) batch removed", mat_b)]:
    x = mat[first12]
    dm = pd.DataFrame(squareform(pdist(x.T.to_numpy())), index=first12, columns=first12)
    g = pd.Series(groups15[:12], index=first12)
    ac = dm.loc[g == "Acute-OA", g == "Control"].to_numpy().mean()
    cc = dm.loc[g == "Chronic-OA", g == "Control"].to_numpy().mean()
    within = dm.loc[g == "Control", g == "Control"].to_numpy()[np.triu_indices(4, 1)].mean()
    print(f"{name}: mean distance acute-OA to control {ac:.1f}, chronic-OA to control {cc:.1f}, control to control {within:.1f}; max {dm.to_numpy().max():.1f}")
''', ["claim:sfig5b-acute-clusters-with-control"])

md(r'''
## GSEA results (fig4b to fig4fgh, chronic-nachr-subunits-down, optic-lobe-no-ion-regulation)

GSEA is not re-run: clusterProfiler, the authors' AnnotationForge GO database and R are not in
this Python environment. The authors' `gse.Normal` objects are read: gseGO results for acute-OA
(AvsCT) and chronic-OA (CvsCT) against control, run with the parameters of the Methods (checked
below against the objects' stored parameters). The cell checks that each object's ranked gene list
is the shrunken log2 fold change of the deposited DESeq2 results `resNormal`.
''')
code(r'''
gse = {k: v for k, v in zip(ws["gse.Normal"].names(), ws["gse.Normal"].value)}
res = {k: sq.s4_dataframe(v) for k, v in zip(ws["resNormal"].names(), ws["resNormal"].value)}
gres = {}
for k, o in gse.items():
    p = o["params"]
    print(k, "params:", {n: (x.value[0] if len(x.value) else None) for n, x in zip(p.names(), p.value)},
          "| setType", o["setType"].value, "| gene sets in object", len(o["geneSets"].value))
    gl = o["geneList"]
    gl = pd.Series(gl.value, index=gl.attr["names"].value)
    r = res[k].dropna(subset=["padj"])["log2FoldChange"]
    common = gl.index.intersection(r.index)
    print(f"  ranked list {len(gl)} genes; resNormal with padj {len(r)}; shared {len(common)}; max |difference| {np.abs(gl[common] - r[common]).max():.2e}")
    t = sq.df_from(o["result"])
    gres[k] = t
    print(f"  significant sets {len(t)} (max p.adjust {t['p.adjust'].max():.4f}); NES < 0: {(t.NES < 0).sum()}, NES > 0: {(t.NES > 0).sum()}")
    print("  by ontology and sign:", t.groupby(["ONTOLOGY", np.where(t.NES > 0, "up", "down")]).size().to_dict())
A, C = gres["AvsCT"], gres["CvsCT"]
''', ["sanity"])

md(r'''
## fig4b-shared-down-sets

> Only 2 of 36 GO gene sets were down-regulated under both acute and chronic acidification,
> organelle inner membrane and mitochondrial inner membrane.

Readings of "36" from the criterion: (a) sets down-regulated in either treatment, (b) all sets of
the Venn diagram (significant in either treatment). The deposited script's Figure 4C chunk shows
the sets significant in both treatments (`intersect(CvsCT ID, AvsCT ID)`, `showCategory = 36`);
that count is shown as a variant.
''')
code(r'''
downA, downC = set(A.ID[A.NES < 0]), set(C.ID[C.NES < 0])
upA, upC = set(A.ID[A.NES > 0]), set(C.ID[C.NES > 0])
both_down = downA & downC
print("Down in both:", len(both_down), A.set_index("ID").loc[sorted(both_down), "Description"].to_dict())
print("(a) down in either:", len(downA | downC))
print("(b) all sets in the Venn diagram (significant in either):", len(set(A.ID) | set(C.ID)))
print("variant, significant in both (script's Fig. 4C):", len(set(A.ID) & set(C.ID)))
print("Venn regions: A- only", len(downA - set(C.ID)), "| C- only", len(downC - set(A.ID)), "| A+ ", len(upA), "| C+", len(upC),
      "| A- and C+", len(downA & upC), "| A+ and C-", len(upA & downC), "| A+ and C+", len(upA & upC))
''', ["claim:fig4b-shared-down-sets"])

code(r'''
def find(table, pattern, sign):
    t = table[table.Description.str.contains(pattern, case=False, regex=True)]
    t = t[t.NES < 0] if sign < 0 else t[t.NES > 0]
    return t[["ID", "ONTOLOGY", "Description", "NES", "p.adjust"]]

def family_table(table, families, sign):
    rows = []
    for fam, pat in families.items():
        hit = find(table, pat, sign)
        rows.append({"family": fam, "pattern": pat, "terms": len(hit),
                     "examples": "; ".join(f"{d} ({n:.2f})" for d, n in zip(hit.Description[:3], hit.NES[:3]))})
    return pd.DataFrame(rows)
''')

md(r'''
## fig4c-acute-ridge

> Acute acidification suppressed gene sets of lipid, carboxylic acid and organic acid metabolism,
> transferase and endopeptidase complexes and ribosomal subunits, and up-regulated cell-cell
> adhesion.

Each family is matched on the term names (case-insensitive) of the acute-OA results, all of which
have BH-adjusted p < 0.05.
''')
code(r'''
fam_c = {"cellular lipid metabolic process": r"cellular lipid metabolic process", "carboxylic acid metabolic process": r"carboxylic acid metabolic process",
         "organic acid metabolic process": r"organic acid metabolic process", "transferase complex": r"transferase complex",
         "endopeptidase complex": r"endopeptidase complex", "ribosomal subunit": r"ribosomal subunit"}
t_down = family_table(A, fam_c, -1)
t_up = family_table(A, {"cell-cell adhesion": r"cell-cell adhesion"}, +1)
print(pd.concat([t_down.assign(direction="down"), t_up.assign(direction="up")]).to_string(index=False))
print("\nAll acute-OA up-regulated sets:", A.loc[A.NES > 0, ["Description", "NES", "p.adjust"]].round(4).to_dict("records"))
''', ["claim:fig4c-acute-ridge"])

md(r'''
## fig4d-acute-tree

> Under acute acidification down-regulated clusters included mitochondrial and energy metabolism
> (respirasome, electron transport chain complex IV, mitochondrial envelope), fatty acid
> biosynthesis and elongase activity, organelle and protein localization, and ncRNA
> ribonucleoprotein and 3'-end RNA processing.

Matched in the acute-OA down-regulated sets; the script's tree uses those not significant in
chronic-OA, shown as a variant.
''')
code(r'''
fam_d = {"respirasome": r"respirasome", "complex IV": r"cytochrome[- ]c oxidase|complex IV", "mitochondrial envelope": r"mitochondrial envelope",
         "fatty acid biosynthesis or elongase": r"fatty acid biosynthe|elongase", "organelle or protein localization": r"organelle localization|protein localization",
         "ncRNA ribonucleoprotein or 3'-end processing": r"ribonucleoprotein|3'-end"}
print(family_table(A, fam_d, -1).to_string(index=False))
a_only = A[~A.ID.isin(C.ID)]
print("\nVariant, acute-OA down and not significant in chronic-OA (script's Fig. 4D), sets:", int((a_only.NES < 0).sum()))
print(family_table(a_only, fam_d, -1)[["family", "terms"]].to_string(index=False))
''', ["claim:fig4d-acute-tree"])

md(r'''
## fig4e-chronic-synaptic-down

> Under chronic acidification down-regulated gene sets included postsynaptic membrane, synaptic
> membrane, transmitter-gated channel activity and neurotransmitter receptor activity, NAD(P)H
> dehydrogenase activity, respiratory electron transport, cell adhesion molecules and prefoldin
> complex.
''')
code(r'''
fam_e = {"postsynaptic membrane": r"^postsynaptic membrane$", "synaptic membrane": r"^synaptic membrane$",
         "transmitter-gated channel activity": r"transmitter-gated", "neurotransmitter receptor activity": r"neurotransmitter receptor activity",
         "NAD(P)H dehydrogenase": r"NAD\(P\)H dehydrogenase|NADH dehydrogenase", "respiratory electron transport chain": r"respiratory electron transport",
         "cell adhesion": r"cell adhesion", "prefoldin complex": r"prefoldin"}
print(family_table(C, fam_e, -1).to_string(index=False))
print("\nAll chronic-OA down-regulated sets:")
print(C.loc[C.NES < 0, ["ONTOLOGY", "Description", "NES", "p.adjust"]].sort_values("NES").round(4).to_string(index=False))
''', ["claim:fig4e-chronic-synaptic-down"])

md(r'''
## fig4fgh-chronic-up

> Chronic acidification up-regulated 82 cellular component, 308 biological process and 128
> molecular function gene sets, including vesicle, endosome and Golgi components, purine
> biosynthesis and carbohydrate catabolism, ribonucleoprotein and ubiquitin-related activities,
> and oxidoreductase, hydrolase and transporter activities.

Counts per ontology of the chronic-OA sets with NES > 0 (the criterion). The script's Figure 4F to
H chunk takes the chronic-OA up sets not down in acute-OA and passes them to simplifyEnrichment's
GO_similarity, which keeps only terms it finds in the GO database; that subset is shown as a
variant (GO_similarity's filter cannot be run here).
''')
code(r'''
up = C[C.NES > 0]
print("Chronic-OA up-regulated sets per ontology:", up.groupby("ONTOLOGY").size().to_dict(), "(paper CC 82, BP 308, MF 128)")
up_script = up[~up.ID.isin(A.ID[A.NES < 0])]
print("Variant, up and not down in acute-OA:", up_script.groupby("ONTOLOGY").size().to_dict())
fam_f = {"vesicle": r"vesicle", "endosome": r"endosom", "Golgi": r"golgi", "purine biosynthesis": r"purine.*biosynthe",
         "carbohydrate catabolism": r"carbohydrate catabol", "ribonucleoprotein": r"ribonucleoprotein", "ubiquitin": r"ubiquitin",
         "oxidoreductase": r"oxidoreductase", "hydrolase": r"hydrolase", "transporter activity": r"transporter activity"}
print(family_table(up, fam_f, +1).to_string(index=False))
''', ["claim:fig4fgh-chronic-up"])

md(r'''
## chronic-nachr-subunits-down

> Chronic acidification down-regulated transcripts of several nicotinic acetylcholine receptor
> subunits (alpha-7, alpha-10 and beta-4) in the optic lobes.

Transcripts are identified by the protein names of the authors' annotation table (`DB$name`, the
table the script passes to AnnotationForge). Reading (a): core enrichment genes of a chronic-OA
down-regulated synaptic set (fig4e); reading (b): negative shrunken log2 fold change, chronic-OA
against control (`resNormal$CvsCT`).
''')
code(r'''
names_tab = sq.df_from(ws["DB"]["name"])
nachr = names_tab[names_tab.PNAME.str.contains(r"acetylcholine receptor", case=False, na=False)]
print("Annotated transcripts naming an acetylcholine receptor:", len(nachr))
sub = {"alpha-7": r"alpha[- ]?7(?!\d)", "alpha-10": r"alpha[- ]?10(?!\d)", "beta-4": r"beta[- ]?4(?!\d)"}
syn = C[(C.NES < 0) & C.Description.str.contains(r"synap|transmitter|neurotransmitter", case=False)]
core = set("/".join(syn.core_enrichment).split("/"))
print("Chronic-OA down synaptic sets:", list(syn.Description), "; core enrichment genes:", len(core))
rC = res["CvsCT"]
for s_name, pat in sub.items():
    tx = nachr[nachr.PNAME.str.contains(r"nicotinic|neuronal", case=False) & nachr.PNAME.str.contains(pat, case=False)]
    tx = tx[~tx.PNAME.str.contains("like protein|associated", case=False)]
    rows = rC.reindex(tx.GID)
    print(f"\n{s_name}: {len(tx)} transcripts; in core enrichment {int(tx.GID.isin(core).sum())}; tested in DESeq2 {int(rows.log2FoldChange.notna().sum())}")
    if len(tx):
        print(pd.concat([tx.set_index("GID").PNAME, rows[["baseMean", "log2FoldChange", "padj"]]], axis=1).round(4).to_string())
''', ["claim:chronic-nachr-subunits-down"])

md(r'''
## optic-lobe-no-ion-regulation

> No change was seen in optic lobe transcripts associated with acid-base or ion regulatory
> processes.

GO terms whose names contain "pH", "acid-base", "bicarbonate", "proton", "chloride" or "ion
transmembrane transport" (the criterion), significant in either treatment.
''')
code(r'''
pat = r"\bpH\b|acid-base|bicarbonate|proton|chloride|ion transmembrane transport"
for k, t in gres.items():
    hit = t[t.Description.str.contains(pat, case=True, regex=True) | t.Description.str.contains(r"acid-base|bicarbonate|proton|chloride|ion transmembrane transport", case=False)]
    print(f"{k}: {len(hit)} significant terms")
    if len(hit):
        print(hit[["ONTOLOGY", "Description", "NES", "p.adjust"]].round(4).to_string(index=False))
''', ["claim:optic-lobe-no-ion-regulation"])
PYEOF
cat > $TMPDIR/gen/build.py <<'PYEOF'
import nbformat, sys
CELLS = []
def md(s, tags=None): CELLS.append(("markdown", s.strip("\n"), tags or []))
def code(s, tags=None): CELLS.append(("code", s.strip("\n"), tags or []))
ns = {"md": md, "code": code, "CELLS": CELLS}
import os
d = os.path.dirname(__file__)
for part in sorted(f for f in os.listdir(d) if f.startswith("nb") and f.endswith(".py")):
    src = open(os.path.join(d, part)).read().replace("CELLS = []\n", "", 1)
    src = src.replace("def md(s, tags=None): CELLS.append((\"markdown\", s.strip(\"\\n\"), tags or []))\n", "").replace("def code(s, tags=None): CELLS.append((\"code\", s.strip(\"\\n\"), tags or []))\n", "")
    exec(src, ns)
nb = nbformat.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
for kind, src, tags in CELLS:
    c = nbformat.v4.new_markdown_cell(src) if kind == "markdown" else nbformat.v4.new_code_cell(src)
    if tags: c.metadata["tags"] = tags
    nb.cells.append(c)
for c in nb.cells:
    c.pop("id", None)
nbformat.write(nb, sys.argv[1])
print(len(nb.cells), "cells")
PYEOF
cd entries/allen-2026 && . $TMPDIR/rv/bin/activate && python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb && date -u && /usr/bin/time -f "%e s %M KB" jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/out.ipynb reproduce_allen_2026.ipynb 2>&1 | tail -5
```

```
/tmp/claude-1001/rv/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
76 cells
Wed Nov 25 20:30:24 UTC 2026

[31mIndexError[39m: list index out of range

Command exited with non-zero status 1
37.68 s 3304672 KB
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && sed -i 's/^for c in nb.cells:\n    c.pop("id", None)//' $TMPDIR/gen/build.py && python - <<'EOF'
s=open('/tmp/claude-1001/gen/build.py').read().replace('for c in nb.cells:\n    c.pop("id", None)\n','')
open('/tmp/claude-1001/gen/build.py','w').write(s)
EOF
cat > $TMPDIR/gen/show.py <<'EOF'
import nbformat, sys
nb = nbformat.read(sys.argv[1], as_version=4)
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
for i, c in enumerate(nb.cells):
    if i < start or c.cell_type != "code": continue
    print(f"##### cell {i} {c.metadata.get('tags', [])}")
    for o in c.get("outputs", []):
        if o.output_type == "stream": print(o.text[-6000:])
        elif o.output_type == "error": print("ERROR", o.ename, o.evalue, "\n".join(o.traceback[-3:])[-3000:])
        elif "text/plain" in o.get("data", {}): print(o.data["text/plain"][:2000])
EOF
python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb && jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output $TMPDIR/out.ipynb reproduce_allen_2026.ipynb 2>&1 | tail -1; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 0 | sed 's/\x1b\[[0-9;]*m//g' | head -150
```

```
76 cells
[NbConvertApp] Writing 191823 bytes to /tmp/claude-1001/out.ipynb
##### cell 1 []
Dryad rjdfn2zqz, version id 439366

SHA-256 against Dryad's file list: {'Carbonate_calibration.csv': 'ok', 'README.md': 'ok', 'Squid_Ammonia.csv': 'ok', 'Squid_Behavioral_assessment.csv': 'ok', 'Squid_CFF.csv': 'ok', 'Squid_ERG.csv': 'ok', 'Squid_Hemolymph.csv': 'ok', 'Squid_normalized_total_distance.csv': 'ok', 'Squid_normalized_velocities.csv': 'ok', 'Squid_Prey_Capture.csv': 'ok', 'Squid_RMR.csv': 'ok', 'squid.zip': 'ok'}

##### cell 3 ['sanity']
Files in squid.zip (bytes):
            0  squid/
            0  squid/squid/
        5,673  squid/squid/Bash_scripts.sh
        1,264  squid/squid/ExN50.stats
          672  squid/squid/README.md
   91,128,868  squid/squid/RSEM.isoform.counts.matrix
       21,834  squid/squid/R_scritps.Rmd
  315,805,639  squid/squid/Squid.RData

Carbonate_calibration.csv: 22 rows; columns ['sample_name', 'group', 'pH', 'TCO2 (mM)', 'PCO2 Calculation with Values', 'PCO₂ (μatm)', 'HCO₃⁻ (mM)']
           pH  TCO2 (mM)  PCO₂ (μatm)  HCO₃⁻ (mM)
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 15 | sed 's/\x1b\[[0-9;]*m//g' | head -320
```

```
##### cell 17 ['claim:fig1d-blood-ph', 'claim:fig1e-blood-pco2', 'claim:fig1f-blood-bicarbonate']
--- Hemolymph pH
              n   mean     sd    sem
Control     7.0  7.092  0.020  0.008
Acute-OA    6.0  7.145  0.088  0.036
Chronic-OA  9.0  7.175  0.068  0.023
Welch's ANOVA W = 6.347, df 2, 9.196, p = 0.0185

            comparison  mean_diff  ci_low  ci_high     df  p_adj
   Control vs Acute-OA    -0.0528 -0.1745   0.0689 5.4393 0.4598
 Control vs Chronic-OA    -0.0828 -0.1504  -0.0153 9.7422 0.0173
Acute-OA vs Chronic-OA    -0.0301 -0.1534   0.0933 8.8083 0.8581
--- Hemolymph PCO2 (µatm)
              n      mean       sd      sem
Control     7.0  1057.369  234.087   88.477
Acute-OA    6.0  1583.800  284.397  116.105
Chronic-OA  9.0  2778.712  613.411  204.470
Welch's ANOVA W = 29.815, df 2, 12.036, p = 2.17e-05

            comparison  mean_diff     ci_low    ci_high      df  p_adj
[... 300 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python - <<'EOF'
p='squidoa.py'; s=open(p).read()
s=s.replace("""        df = pd.read_csv(f, sep="\\t", header=None, index_col=0, dtype={i: np.float64 for i in range(1, len(header) + 1)})""","""        df = pd.read_csv(f, sep="\\t", header=None, index_col=0).astype(np.float64)""")
open(p,'w').write(s)
EOF
grep -n "astype(np.float64)" squidoa.py; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 54 | sed 's/\x1b\[[0-9;]*m//g' | head -300
```

```
97:        df = pd.read_csv(f, sep="\t", header=None, index_col=0).astype(np.float64)
##### cell 55 ['claim:fig4a-pca']
VST matrices (rows x samples): (69368, 15) (69368, 15) (69368, 15)
samples: ['Ct_8.1_1', 'Ct_8.1_2', 'Ct_8.1_3', 'Ct_8.1_4', 'Ph_7.8_1', 'Ph_7.8_2', 'Ph_7.8_3', 'Ph_7.8_4', 'Ph_7.8_5', 'Ph_7.8C_1', 'Ph_7.8C_2', 'Ph_7.8C_3', 'Re_8.1_1', 'Re_8.1_2', 'Re_8.1_3']
          batch condition
Ct_8.1_1      1    Ct_8.1
Ct_8.1_2      1    Ct_8.1
Ct_8.1_3      1    Ct_8.1
Ct_8.1_4      2    Ct_8.1
Ph_7.8_1      1    pH_7.8
Ph_7.8_2      1    pH_7.8
Ph_7.8_3      1    pH_7.8
Ph_7.8_4      2    pH_7.8
Ph_7.8_5      2    pH_7.8
Ph_7.8C_1     2   pH_7.8C
Ph_7.8C_2     2   pH_7.8C
Ph_7.8C_3     2   pH_7.8C
Re_8.1_1      1    Re_8.1
Re_8.1_2      1    Re_8.1
Re_8.1_3      1    Re_8.1
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "36|Venn|ridge" paper/10.1038-s42003-025-09506-6.txt | grep -v -E "^\s*[0-9]+:\s*[0-9]+\.\s" | head -20; grep -n -i "PC2\|PC1\|principal" paper/10.1038-s42003-025-09506-6.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 886,905p paper/10.1038-s42003-025-09506-6.txt; grep -n -B2 -A6 "Cellular components (CC) showed" paper/10.1038-s42003-025-09506-6.txt | head -30; ls questions | head; ls questions | grep allen
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u
```

```
Wed Nov 25 20:33:34 UTC 2026
```

**Agent**

Plenty of time left (20:33 UTC). Updating the notebook with the findings cells, variants, and conclusions that match the printed numbers.

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s = open('nb1.py').read()
old_start = s.index("code(r'''\ncc = csvs[\"Carbonate_calibration.csv\"]")
old_end = s.index("# --- fig1b")
s = s[:old_start] + r'''code(r"""
cc = csvs["Carbonate_calibration.csv"]
alpha, pka = 0.0312, 6.10   # as printed in each row of Carbonate_calibration.csv
eq1 = cc["TCO2 (mM)"] / ((1 + 10 ** (cc["pH"] - pka)) * alpha) * 1e3   # Eq. 1 as the file's formula column writes it
print(cc[["sample_name", "PCO2 Calculation with Values", "PCO₂ (μatm)"]].head(3).to_string(index=False))
print("\nThe formula as written, evaluated (first rows):", eq1.head(3).round(1).tolist())
ratio = eq1 / cc["PCO₂ (μatm)"]
print(f"Formula value / PCO2 printed beside it: min {ratio.min():.4f}, max {ratio.max():.4f}")
hem = csvs["Squid_Hemolymph.csv"]
print("Squid_Hemolymph PCO2 equals the printed PCO2 of Carbonate_calibration (max |diff|):",
      round(float(np.abs(hem.iloc[:, 1].to_numpy() - cc["PCO₂ (μatm)"].to_numpy()).max()), 3))
hco3_dep = cc["TCO2 (mM)"] - alpha * cc["PCO₂ (μatm)"] / 1e3
hco3_eq = cc["TCO2 (mM)"] - alpha * eq1 / 1e3
print("Eq. 2 with the printed PCO2 reproduces the deposited [HCO3-] (max |diff|):", round(float(np.abs(hco3_dep.to_numpy() - hem.iloc[:, 2].to_numpy()).max()), 4))
print("Eq. 2 with the formula's PCO2 differs from the deposited [HCO3-] by up to", round(float(np.abs(hco3_eq.to_numpy() - hem.iloc[:, 2].to_numpy()).max()), 3), "mmol/l")
print("pH identical in both files:", bool(np.allclose(cc.pH.to_numpy(), hem.iloc[:, 0].to_numpy())))
""", ["sanity", "finding-pco2-factor-10"])

md(r"""
The deposited hemolymph PCO2 is a tenth of what the formula printed beside it gives: each row
writes Eq. 1 with αCO2 = 0.0312 and pKa1 = 6.10 and "×10³", which evaluates to 10 times the PCO2
printed in the same row (and in `Squid_Hemolymph.csv` and the paper). The deposited [HCO3-] follows
from Eq. 2 with the printed PCO2. The README attributes pKa1 6.10 to Truchot (1976) (the Methods'
ref. 65, Carcinus maenas hemolymph) and gives no unit for αCO2, so the data cannot say which of
the two is right; the fold changes of PCO2 between groups are the same either way.
""")

''' + s[old_end:]
s = s.replace('''**Result: fig1d-blood-ph reproduced.** Means 7.092, 7.145 and 7.175 (n = 7, 6, 9); Welch's ANOVA p
= 0.019 (W = 6.35 against the paper's 5.983, with the same df 2, 9.196); Dunnett's T3 separates
control from chronic-OA (p = 0.017) and neither pair with acute-OA (p = 0.46 and 0.86).

**Result: fig1e-blood-pco2 reproduced.** Means 1057.4, 1583.8 and 2778.7 µatm, fold changes 1.50
and 2.63; Welch's p = 2.2e-05; all three pairs differ (p = 0.014, 3e-05 and 0.0008). This
Welch's W (29.8, df 2, 12.0) differs from the paper's (27.653, df 2, 9.379) on the same values.

**Result: fig1f-blood-bicarbonate reproduced.** Means 3.56, 5.90 and 11.08 mmol/l, fold changes
1.66 and 3.11; Welch's p = 2.5e-06; all pairs differ (p ≤ 0.0008).''', '''**Result: fig1d-blood-ph reproduced.** Means 7.092, 7.145 and 7.175 (n = 7, 6, 9); Welch's ANOVA p
= 0.0185 (W = 6.347 against the paper's 5.983, with the same df 2, 9.196); Dunnett's T3 separates
control from chronic-OA (p = 0.017) and neither pair with acute-OA (p = 0.46 and 0.86).

**Result: fig1e-blood-pco2 reproduced.** Means 1057.4, 1583.8 and 2778.7 µatm, fold changes 1.50
and 2.63; Welch's p = 2.2e-05; all three pairs differ (p = 0.014, below 0.0001 and 0.0008). This
Welch's W (29.815, df 2, 12.04) differs from the paper's (27.653, df 2, 9.379) on the same values.
The values are a tenth of what the deposit's own Eq. 1 gives (data check); the fold changes and
tests do not depend on that factor.

**Result: fig1f-blood-bicarbonate reproduced.** Means 3.56, 5.90 and 11.08 mmol/l, fold changes
1.65 and 3.11; Welch's p = 2.5e-06; all pairs differ (p ≤ 0.0008).''')
s = s.replace('''code(r\'\'\'
blood = {}''', '''code(r\'\'\'
blood = {}''')
open('nb1.py','w').write(s)

s = open('nb2.py').read()
s = s.replace('''print("Paper: F(2,42) = 3.372, p = 0.0439; SS 2.374 and 14.79 (on the log10 scale, these differ; see below)")''', '''print("Paper: F(2,42) = 3.372, p = 0.0439; SS 2.374 and 14.79")''')
s = s.replace('''print(f"Fold change acute/control: {hunt['Acute-OA'].mean() / hunt['Control'].mean():.2f}")
\'\'\', ["claim:fig2h-hunt-duration"])''', '''print(f"Fold change acute/control: {hunt['Acute-OA'].mean() / hunt['Control'].mean():.2f}")
\'\'\', ["claim:fig2h-hunt-duration"])
md(r\'\'\'
**Result: reproduced.** Means 106.7 s (control) and 262.2 s (acute-OA), 2.46-fold; the ANOVA on log10
durations gives F(2,42) = 3.372, p = 0.0439 with the paper's sums of squares; Tukey separates
acute-OA from control (p = 0.035) and chronic-OA (109.5 s) from neither (p = 0.72 and 0.32).
\'\'\')''')
s = s.replace('''**Result: reproduced.** 37 of 45 attacking squid (82%) needed 1 or 2 attempts;''', '''**Result: reproduced.** 38 of 45 attacking squid (84.4%) needed 1 or 2 attempts (control 89.7%,
acute-OA and chronic-OA 75%);''')
# fig2g
s = s.replace('''\'\'\', ["claim:fig2g-attack-willingness"])
md(r\'\'\'
**Result: reproduced.** 29 of 46, 8 of 36 and 8 of 22 squid attacked, reductions of 64.7% and
42.3%. Under reading (a) the pH coefficient is 2.734 (p = 0.042) and the time coefficient 0.00835
(p = 0.246), with residual deviance 127.58 and ROC area 0.699, as the paper prints; the intercept is
-22.64 against the printed 22.36. Lower pH lowers the odds of attack.
\'\'\')''', '''\'\'\', ["claim:fig2g-attack-willingness"])
code(r\'\'\'
f2g = fig_tables["F2G"]
print("Table F2G of the R workspace (Figure 2G):")
print(f2g.to_string(index=False))
print("\\nSquid in Squid_Prey_Capture.csv:", pc.Group.value_counts().reindex(sq.GROUPS).to_dict())
print("Attackers implied by F2G (Mean% x N):", {g: round(m * n / 100, 2) for g, m, n in zip(f2g.group, f2g.Mean, f2g.N)})
\'\'\', ["claim:fig2g-attack-willingness", "finding-prey-capture-chronic-missing"])
code(r\'\'\'
# Variant: the per-squid outcomes the F2G counts imply (the CSV's squid plus the chronic-OA non-attackers it lacks).
n_att = {g: int(round(m * n / 100)) for g, m, n in zip(f2g.group, f2g.Mean, f2g.N)}
n_tot = dict(zip(f2g.group, f2g.N.astype(int)))
rec = pd.DataFrame([{"Group": g, "attack": int(i < n_att[g])} for g in sq.GROUPS for i in range(n_tot[g])])
ph, days = codings["(a) nominal pH, days in condition 90/7/90"]
d = rec.assign(pH=rec.Group.map(ph), time=rec.Group.map(days))
fit = smf.glm("attack ~ pH + time", data=d, family=sm.families.Binomial()).fit()
print("Variant, counts of table F2G (", {g: f"{n_att[g]} of {n_tot[g]}" for g in sq.GROUPS}, "), reading (a):")
print(fit.summary2().tables[1][["Coef.", "Std.Err.", "z", "P>|z|"]].round(6).to_string())
print(f"null deviance {fit.null_deviance:.2f}, residual {fit.deviance:.2f} on {int(fit.df_resid)} df, AIC {fit.aic:.2f}, ROC area {sq.auc(d.attack.to_numpy(), fit.fittedvalues.to_numpy()):.4f}")
print("Reduction against control:", {g: round(100 * (1 - (n_att[g] / n_tot[g]) / (n_att['Control'] / n_tot['Control'])), 1) for g in sq.GROUPS[1:]})
\'\'\', ["claim:fig2g-attack-willingness"])
md(r\'\'\'
**Result: not reproduced.** The per-squid file holds 46, 36 and 11 squid, with 29, 8 and 8 attacks:
the control and acute-OA counts match, the chronic-OA count does not (8 of 11 against the paper's 8
of 22), so the chronic-OA reduction is -15.4% against the paper's 42.3%. On this file, under reading
(a) the pH term is not significant (coefficient -1.12, p = 0.55) and the time term is (p = 0.0045);
readings (b) and (c) give a significant pH term (p = 0.0002) together with a significant time term.
No reading meets the criterion. The workspace's own Figure 2G table gives 22 chronic-OA squid
(36.36% attacking, 8 of 22); with those counts reading (a) gives the paper's model (pH 2.734, p =
0.042; time 0.00835, p = 0.246; ROC area 0.699). The difference comes from 11 chronic-OA squid
missing from the per-squid file.
\'\'\')''')
# sfig3 variant replace
a = s.index('for label, d in [("as deposited", long)')
b = s.index("''', [\"claim:sfig3-prey-velocity-unchanged\"])")
s = s[:a] + '''for typ in (3, 2):
    fit = smf.ols("velocity ~ C(pH, Sum) * C(time, Sum)" if typ == 3 else "velocity ~ C(pH) * C(time)", data=long).fit()
    print(f"\\nas deposited, type {'III' if typ == 3 else 'II'}:")
    print(sm.stats.anova_lm(fit, typ=typ).round(4).to_string())
x0, x1 = s3["pH 8.1 0-10 Min"].dropna(), s3["pH 7.8 0-10 Min"].dropna()
t = stats.ttest_ind(x0, x1, equal_var=False)
mw = stats.mannwhitneyu(x0, x1)
print(f"\\nVariant, 0-10 min only (the 10-20 min CO2 column is a copy): control {x0.mean():.3f} (n {len(x0)}) against CO2 {x1.mean():.3f} (n {len(x1)}); Welch t p = {t.pvalue:.3f}, Mann-Whitney p = {mw.pvalue:.3f}")
''' + s[b:]
s = s.replace('''**Result: reproduced.** On the table as deposited no term has p < 0.05 (two-way ANOVA, type III
and type II). The CO2 10 to 20 min column is a copy of the control 10 to 20 min column (8 values,
identical), so the deposited data cannot show what the CO2 shrimp did at 20 min; leaving that
column out, no term has p < 0.05 either. A repeated-measures variant is not run: no shrimp
identifier links the columns, and the CO2 columns hold 11 and 8 values.''', '''**Result: reproduced.** On the table as deposited no term has p < 0.05 (two-way ANOVA: pH p =
0.84, time p = 0.11, interaction p = 0.84, type III; type II the same to two decimals). The CO2 10
to 20 min column is a copy of the control 10 to 20 min column (8 identical values, where the
legend gives 11 CO2 shrimp), so the deposited data cannot show what the CO2 shrimp did at 20 min.
At 0 to 10 min alone, control and CO2 shrimp do not differ (Welch t p = 0.67). A
repeated-measures variant is not run: no shrimp identifier links the columns, and the CO2 columns
hold 11 and 8 values.''')
open('nb2.py','w').write(s)

s = open('nb3.py').read()
s = s.replace('''is present above 50 Hz in the deposited means; the criterion's "every frequency above 40 Hz" is not met.''', '''is present above 50 Hz in the deposited means; the criterion's "every frequency above 40 Hz" is not met.''')
s = s.replace('''(0.39, 0.37) and returns near 1 at 47 Hz. The highest frequency is lowest or within 0.1 of it in
control and acute-OA, not in chronic-OA (0.361 against 0.252).''', '''(0.39, 0.37) and returns near 1 at 47 Hz. The ratio at the highest frequency (65 Hz) is the lowest
in acute-OA (0.300) but not within 0.1 of the lowest in control (0.391 against 0.284 at 62.5 Hz)
or chronic-OA (0.361 against 0.252).''')
s = s.replace('''**Result: reproduced.** Means 50.7, 50.7 and 47.7 Hz (n = 3, 3, 6); one-way ANOVA F(2,9) = 0.37, p =
0.70, so no difference is found.''', '''**Result: reproduced.** Means 50.7, 50.7 and 47.7 Hz (n = 3, 3, 6); one-way ANOVA F(2,9) = 0.541, p
= 0.60 (η² = 0.11), so no difference is found; Tukey p ≥ 0.68 for every pair.''')
s = s.replace('''**Result: reproduced.** SDs 1.15, 6.03 and 5.32 Hz; ratios 5.22 (acute-OA) and 4.60 (chronic-OA),
both in 3.6 to 5.5. With 3 control squid the control SD rests on three values.''', '''**Result: reproduced.** SDs 1.15, 6.03 and 5.47 Hz; ratios 5.22 (acute-OA) and 4.73 (chronic-OA),
both in 3.6 to 5.5. With 3 control squid the control SD rests on three values; a Brown-Forsythe test
does not find the variances to differ (p = 0.61), which is not judged.''')
s = s.replace('''**Result: reproduced, except the mapping rate, which is not in the dataset.**''', '''**Result: reproduced for the four values the dataset holds; the mapping rate is not in it.**''')
open('nb3.py','w').write(s)
EOF
grep -c "Result" nb1.py nb2.py nb3.py
```

```
nb1.py:5
nb2.py:9
nb3.py:4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s = open('nb1.py').read()
s = s.replace("""''', ["sanity"])

md(r'''
Group sizes against the paper.""", """''', ["sanity", "finding-not-deposited"])

code(r'''
rmr_file = csvs["Squid_RMR.csv"]
print("Squid_RMR.csv squid per group:", rmr_file.Group.value_counts().reindex(sq.GROUPS).to_dict(), "total", len(rmr_file))
print("Supplementary Table 1: F(2,26), total df 28, so 29 squid")
''', ["finding-rmr-count"])

md(r'''
Group sizes against the paper.""")
open('nb1.py','w').write(s)

s = open('nb4.py').read()
s = s.replace('''pca_tab["chronic separated PC2"] = pca_tab["|chronic-control| PC2"] > pca_tab["control range PC2"]''', '''pca_tab["chronic separated PC2"] = pca_tab["|chronic-control| PC2"] > pca_tab["control range PC2"]
for name, sc in plots.items():
    ctrl = sc[sc.group == "Control"]
    pca_tab.loc[name, "control SD PC1"] = ctrl.PC1.std()
    pca_tab.loc[name, "control SD PC2"] = ctrl.PC2.std()
    chron = sc[sc.group == "Chronic-OA"]
    pca_tab.loc[name, "chronic outside control range PC2"] = int(((chron.PC2 > ctrl.PC2.max()) | (chron.PC2 < ctrl.PC2.min())).sum())
pca_tab["chronic separated PC2 (SD reading)"] = pca_tab["|chronic-control| PC2"] > pca_tab["control SD PC2"]''')
s = s.replace('''print("All points are within the axes.")
\'\'\', ["claim:fig4a-pca"])''', '''print("All points are within the axes.")
print(plots["(a) SVs removed, PCA on 12"].round(2).to_string())
\'\'\', ["claim:fig4a-pca"])
md(r\'\'\'
**Result: partially reproduced.** On the authors' batch-corrected matrix (reading (a)), the PCA of
the 12 samples of the three groups gives PC1 35.0% and PC2 15.0%, the paper's values (the script's
PCA of all 15 samples gives 29.0% and 13.5%). Acute-OA lies near the controls on PC1 (centroid
distance 3.5 against 62.9 for chronic-OA), and chronic-OA is separated from the controls on PC1
(62.9 against a control range of 13.4). On PC2 the chronic-OA centroid is 18.0 from the control
centroid, less than the control range (29.6) though more than the control SD; the criterion's
"spread" is read as the range (an assumption, see the record), under which PC2 separation fails.
Reading (b), known batches removed, gives PC1 above 90% and does not match.
\'\'\')''')
s = s.replace('''\'\'\', ["claim:sfig5b-acute-clusters-with-control"])''', '''\'\'\', ["claim:sfig5b-acute-clusters-with-control"])
md(r\'\'\'
**Result: reproduced.** On the batch-corrected matrix the mean distance from acute-OA to control
samples is 187.7, from chronic-OA to control 255.2 (control to control 197.7); reading (b) gives the
same order (729.5 against 868.1).
\'\'\')''')
s = s.replace('''\'\'\', ["claim:fig4b-shared-down-sets"])''', '''\'\'\', ["claim:fig4b-shared-down-sets"])
md(r\'\'\'
**Result: partially reproduced.** Exactly two sets are down-regulated in both treatments, organelle
inner membrane and mitochondrial inner membrane. The count of 36 is not matched under the
criterion's readings ((a) 122 sets down in either treatment, (b) 646 in the Venn diagram); the sets
significant in both treatments, which the deposited script plots in Figure 4C and the Results call
"the intersect GSEA ridgeplot", number 36. This reading is asked of a reader.
\'\'\')''')
s = s.replace('''\'\'\', ["claim:fig4c-acute-ridge"])''', '''\'\'\', ["claim:fig4c-acute-ridge"])
md(r\'\'\'
**Result: reproduced.** In the acute-OA results each named family has at least one down-regulated
term (cellular lipid metabolic process NES -1.39, carboxylic and organic acid metabolic process
-1.47, transferase complex -1.62, endopeptidase complex -1.92, three ribosomal subunit terms -1.75
to -2.24), and cell-cell adhesion is up (NES 1.45).
\'\'\')''')
s = s.replace('''\'\'\', ["claim:fig4d-acute-tree"])''', '''\'\'\', ["claim:fig4d-acute-tree"])
md(r\'\'\'
**Result: reproduced.** Every named family has down-regulated acute-OA terms (respirasome, complex
IV, mitochondrial envelope, fatty acid biosynthesis and elongase activity, protein localization,
RNA 3'-end processing and ribonucleoprotein complex biogenesis), also within the 51 sets of the
script's tree.
\'\'\')''')
s = s.replace('''\'\'\', ["claim:fig4e-chronic-synaptic-down"])''', '''\'\'\', ["claim:fig4e-chronic-synaptic-down"])
md(r\'\'\'
**Result: reproduced.** Among the 40 chronic-OA down-regulated sets are postsynaptic membrane (NES
-1.91), synaptic membrane (-1.92), transmitter-gated channel activity (-1.80), neurotransmitter
receptor activity (-1.83), NAD(P)H dehydrogenase (quinone) activity (-1.89), respiratory electron
transport chain (-1.55), cell adhesion (-1.40) and prefoldin complex (-2.02).
\'\'\')''')
s = s.replace('''\'\'\', ["claim:fig4fgh-chronic-up"])''', '''\'\'\', ["claim:fig4fgh-chronic-up"])
md(r\'\'\'
**Result: partially reproduced.** Every named family has up-regulated chronic-OA terms. Counted as
the criterion defines them, the up-regulated sets are 101 CC (82 ± 8.2 expected), 321 BP (308 ±
30.8) and 133 MF (128 ± 12.8): CC is out of tolerance. The script's subset, up in chronic-OA and
not down in acute-OA, gives 82 CC, 314 BP and 128 MF, the paper's CC and MF counts.
\'\'\')''')
s = s.replace('''\'\'\', ["claim:chronic-nachr-subunits-down"])''', '''\'\'\', ["claim:chronic-nachr-subunits-down"])
md(r\'\'\'
**Result: reproduced.** Under reading (a), each subunit has transcripts among the core enrichment
genes of the chronic-OA down-regulated synaptic sets (alpha-7 2 of 4 transcripts, alpha-10 10 of
29, beta-4 1 of 1). Under reading (b) the tested alpha-7 and beta-4 transcripts have negative
shrunken log2 fold changes (-0.64, -1.03; -0.87) and most alpha-10 transcripts do (14 of 17
tested; 3 positive); none has an adjusted p below 0.09.
\'\'\')''')
s = s.replace('''\'\'\', ["claim:optic-lobe-no-ion-regulation"])''', '''\'\'\', ["claim:optic-lobe-no-ion-regulation"])
md(r\'\'\'
**Result: not reproduced.** No acute-OA term matches, but three chronic-OA terms do, all
up-regulated: transition metal ion transmembrane transporter activity (NES 2.13, adjusted p =
0.004), organic anion transmembrane transporter activity (1.87, p = 0.033; it matches "ion
transmembrane transport" inside "anion") and metal cation:proton antiporter activity (1.70, p =
0.034). Among the chronic-OA down-regulated sets are also several ion channel activity terms (cell
of fig4e), which the criterion's words do not match.
\'\'\')''')
open('nb4.py','w').write(s)
EOF
grep -c Result $TMPDIR/gen/nb4.py
```

```
10
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s = open('nb4.py').read()
s = s.replace('''    print(f"\\n{s_name}: {len(tx)} transcripts; in core enrichment {int(tx.GID.isin(core).sum())}; tested in DESeq2 {int(rows.log2FoldChange.notna().sum())}")''', '''    print(f"\\n{s_name}: {len(tx)} transcripts; in core enrichment {int(tx.GID.isin(core).sum())}; with a fold change {int(rows.log2FoldChange.notna().sum())}, "
          f"negative {int((rows.log2FoldChange < 0).sum())}; smallest adjusted p {rows.padj.min():.4f}")''')
open('nb4.py','w').write(s)
EOF
cat > $TMPDIR/gen/nb5.py <<'PYEOF'
md(r'''
## Summary

| Claim | Outcome |
|---|---|
| fig1b-metabolic-rate | reproduced (26 squid deposited, 29 in the paper's ANOVA) |
| fig1c-ammonia-excretion | reproduced (the paper's F and p exactly) |
| fig1d-blood-ph | reproduced |
| fig1e-blood-pco2 | reproduced (values a tenth of the deposit's own Eq. 1) |
| fig1f-blood-bicarbonate | reproduced |
| methods-body-size | blocked, data missing |
| stable5-seawater-chemistry | blocked, data missing |
| sfig2-distance-unchanged | reproduced (the paper's H and p exactly) |
| fig2c-velocity-unchanged | reproduced |
| fig2d-acute-upper-zone | reproduced (paper's set found by leaving out one acute-OA squid) |
| stable3-acute-shallower | blocked, data missing |
| fig2e-left-right-unchanged | reproduced |
| fig2f-front-back-unchanged | reproduced |
| fig2g-attack-willingness | not reproduced (11 chronic-OA squid missing from the per-squid file) |
| fig2h-hunt-duration | reproduced |
| fig2i-strike-attempts | reproduced |
| sfig3-prey-velocity-unchanged | reproduced (CO2 20 min column is a copy of control) |
| fig3c-ratio-declines | not reproduced (criterion's "every frequency above 40 Hz") |
| sfig4a-amplitude-attenuation | blocked, data missing |
| fig3d-cff-unchanged | reproduced |
| fig3d-cff-variance | reproduced |
| rnaseq-assembly | reproduced (mapping rate not deposited) |
| fig4a-pca | partially reproduced (assumption on "spread") |
| sfig5b-acute-clusters-with-control | reproduced |
| fig4b-shared-down-sets | partially reproduced (count 36 under the script's reading only; asked) |
| fig4c-acute-ridge | reproduced |
| fig4d-acute-tree | reproduced |
| fig4e-chronic-synaptic-down | reproduced |
| fig4fgh-chronic-up | partially reproduced (CC count 101 against 82) |
| chronic-nachr-subunits-down | reproduced |
| optic-lobe-no-ion-regulation | not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

How the analysis differs from the paper's. The deposit holds derived values per squid, so the
rates, distances, zone percentages and CFF are taken as deposited, not recomputed from raw
recordings. The transcriptomic claims are tested on the authors' count matrix and their saved
DESeq2, sva and GSEA objects, not from the reads; GSEA is not re-run. Welch's ANOVA and Dunnett's T3
are implemented here; the Welch W for pH and PCO2 and the Dunnett's T3 intervals differ from
those Supplementary Table 2 prints on the same values, without changing which pairs differ.

What was found about the dataset. The CO2 10 to 20 min column of the prey shrimp table is a copy
of the control 10 to 20 min column. The prey capture file lacks 11 chronic-OA squid that the
workspace's Figure 2G table and the paper count. The hemolymph PCO2 values are a tenth of what the
formula printed beside them gives. The zone file holds an acute-OA squid the paper's analysis
left out, unmarked. The metabolic rate file has 26 squid against the paper's 29. The 3-D tracks,
ERG recordings, seawater chemistry, body mass and mantle length, which the paper's Data
availability statement places in the deposit, are not in it.
''')
code(r'''
import resource
print(f"Notebook time {time.time() - started:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
''')
PYEOF
cd entries/allen-2026 && . $TMPDIR/rv/bin/activate && python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb && jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output $TMPDIR/out.ipynb reproduce_allen_2026.ipynb 2>&1 | tail -1; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 0 | sed 's/\x1b\[[0-9;]*m//g' | grep -n -A12 -E "ERROR|finding-pco2|finding-rmr|F2G|Variant, counts|0-10 min only|PC2 %|chronic outside|negative [0-9]|Notebook time|transcripts \(rows|\(a\) at least|\(b\) total|variant, \(a\)|Rows of the dep" | head -150
```

```
91 cells
[NbConvertApp] Writing 205495 bytes to /tmp/claude-1001/out.ipynb
86:##### cell 4 ['finding-rmr-count']
87-Squid_RMR.csv squid per group: {'Control': 11, 'Acute-OA': 9, 'Chronic-OA': 6} total 26
88-Supplementary Table 1: F(2,26), total df 28, so 29 squid
89-
90-##### cell 6 ['sanity']
91-read Squid.RData objects in 24 s
92-F1B: (33, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 9, 'Chronic-OA': 6, 'Control': 11}
93-F1C: (27, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 9, 'Chronic-OA': 7, 'Control': 5}
94-F1D: (27, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 6, 'Chronic-OA': 9, 'Control': 7}
95-F1E: (27, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 6, 'Chronic-OA': 9, 'Control': 7}
96-F1F: (27, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 6, 'Chronic-OA': 9, 'Control': 7}
97-F2C: (45, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 8, 'Chronic-OA': 11, 'Control': 15}
98:F2G: (3, 4), columns ['group', 'Mean', 'SD', 'N'], non-missing per group {'Acute-OA': 1, 'Chronic-OA': 1, 'Control': 1}
99-F2F: (45, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 9, 'Chronic-OA': 11, 'Control': 15}
100-F2E: (45, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 9, 'Chronic-OA': 11, 'Control': 15}
101-F2D: (45, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 9, 'Chronic-OA': 11, 'Control': 15}
102-F2H: (87, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 8, 'Chronic-OA': 8, 'Control': 29}
103-F2I: (87, 2), columns ['group', 'value'], non-missing per group {'Acute-OA': 8, 'Chronic-OA': 8, 'Control': 29}
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python - <<'EOF'
p='squidoa.py'; s=open(p).read()
s=s.replace('''def read_count_matrix() -> pd.DataFrame:
    """RSEM.isoform.counts.matrix: transcripts by samples (expected counts)."""''','''def read_count_matrix() -> pd.DataFrame:
    """RSEM.isoform.counts.matrix: transcripts by samples (expected counts). The header names 16
    samples and each row holds a transcript id and 15 values; as R's read.csv(row.names = 1) does
    in the authors' script, the first header name is taken as that of the id column."""''')
s=s.replace('''        df = pd.read_csv(f, sep="\\t", header=None, index_col=0).astype(np.float64)
    df.columns = header''','''        df = pd.read_csv(f, sep="\\t", header=None, index_col=0).astype(np.float64)
    df.columns = header[1:] if len(header) == df.shape[1] + 1 else header''')
open(p,'w').write(s)
s=open('/tmp/claude-1001/gen/nb3.py').read()
s=s.replace('''counts = sq.read_count_matrix()
ol = [c for c in counts.columns if "_OL" in c or "-OL" in c]''','''with __import__("zipfile").ZipFile(sq.STAGED / "squid.zip") as z, z.open(sq.ZIP_DIR + "RSEM.isoform.counts.matrix") as f:
    f.readline()
    first = f.readline().decode().rstrip("\\n").split("\\t")
print(f"header names {len(header)} samples; a data row holds an id and {len(first) - 1} values")
counts = sq.read_count_matrix()
ol = [c for c in counts.columns if "_OL" in c or "-OL" in c]
ws_raw = sq.matrix(sq.read_rdata({"rawMatrix"})["rawMatrix"])
same = np.array_equal(counts[ol].to_numpy(), ws_raw.loc[["TRINITY_" + i if not i.startswith("TRINITY_") else i for i in ws_raw.index] if False else ws_raw.index].to_numpy()) if False else None
ws_raw.index = ["TRINITY_" + i for i in ws_raw.index]
aligned = counts[ol].reindex(ws_raw.index)
print("Workspace rawMatrix", ws_raw.shape, "; equals the file's 15 value columns, read as the script reads them:",
      bool(np.allclose(aligned.to_numpy(), ws_raw.to_numpy())))
del ws_raw, aligned''')
s=s.replace('''\'\'\', ["claim:rnaseq-assembly"])''','''\'\'\', ["claim:rnaseq-assembly", "finding-count-matrix-header"])''')
open('/tmp/claude-1001/gen/nb3.py','w').write(s)
s=open('/tmp/claude-1001/gen/nb2.py').read()
s=s.replace("At 0 to 10 min alone, control and CO2 shrimp do not differ (Welch t p = 0.67).","At 0 to 10 min alone, control and CO2 shrimp do not differ (Welch t p = 0.65).")
open('/tmp/claude-1001/gen/nb2.py','w').write(s)
EOF
sed -i 's/^same = np.array_equal.*$//' $TMPDIR/gen/nb3.py
python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb && /usr/bin/time -f "%e s %M KB" jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output $TMPDIR/out.ipynb reproduce_allen_2026.ipynb 2>&1 | tail -1; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 55 | sed 's/\x1b\[[0-9;]*m//g' | head -60; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 0 | grep -c ERROR; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 85 | tail -5
```

```
91 cells
56.56 s 4148592 KB
##### cell 56 ['claim:rnaseq-assembly', 'finding-count-matrix-header']
RSEM.isoform.counts.matrix columns: ['Ct_8.1_Gill-1', 'Ct_8.1_OL-1', 'Ct_8.1_OL-2', 'Ct_8.1_OL-3', 'Ct_8.1_OL-4', 'Ph_7.8_OL-1', 'Ph_7.8_OL-2', 'Ph_7.8_OL-3', 'Ph_7.8_OL-4', 'Ph_7.8_OL-5', 'Ph_7.8C-OL-1', 'Ph_7.8C-OL-2', 'Ph_7.8C-OL-3', 'Re_8.1_OL-1', 'Re_8.1_OL-2', 'Re_8.1_OL-3']
transcripts (rows): 902413
['Ex', 'ExN50', 'num_genes'] 100 rows
E78N50: 2038.0  maximum ExN50 from Ex 25 on: 2038.0  N50 at Ex 100: 475.5  num_genes at Ex 100: 610324
header names 16 samples; a data row holds an id and 15 values

Workspace rawMatrix (902413, 15) ; equals the file's 15 value columns, read as the script reads them: False


Optic lobe columns: 15; rows with non-zero mean 516034
(a) at least 10 counts in at least 3 of 15 samples: 67088
(b) total >= 10 and detected in >= 3 samples: 168025
variant, (a) on the 12 samples of the three groups: 58906
Rows of the deposited DESeq2 results (resNormal): {'AvsCT': 69368, 'CvsCT': 69368}

##### cell 59 ['claim:fig4a-pca']
VST matrices (rows x samples): (69368, 15) (69368, 15) (69368, 15)
[... 47 more lines not kept]
```

**Agent**

The deposited count file does not equal the workspace's `rawMatrix`, and the filter gives 67,088, not 69,368. Investigating the column alignment.

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python -c "
import squidoa as s, numpy as np, pandas as pd
c=s.read_count_matrix()
w=s.matrix(s.read_rdata({'rawMatrix'})['rawMatrix']); w.index=['TRINITY_'+i for i in w.index]
c=c.reindex(w.index)
print('rows matched', c.notna().all(axis=1).sum(), len(w))
# correlation of each ws column with each file column
C=np.corrcoef(np.log1p(np.vstack([w.to_numpy().T, c.to_numpy().T])))[:15,15:]
print(pd.DataFrame(C, index=w.columns, columns=c.columns).round(3).to_string())
for j in range(15):
  for k in range(15):
    if np.allclose(w.iloc[:,j].to_numpy(), c.iloc[:,k].to_numpy()): print('equal', w.columns[j], c.columns[k])
r=np.round(w); r=r[w.mean(axis=1)!=0]; print('filter on ws rawMatrix', ((r>=10).sum(axis=1)>=3).sum())
"
```

```
rows matched 902413 902413
           Ct_8.1_OL-1  Ct_8.1_OL-2  Ct_8.1_OL-3  Ct_8.1_OL-4  Ph_7.8_OL-1  Ph_7.8_OL-2  Ph_7.8_OL-3  Ph_7.8_OL-4  Ph_7.8_OL-5  Ph_7.8C-OL-1  Ph_7.8C-OL-2  Ph_7.8C-OL-3  Re_8.1_OL-1  Re_8.1_OL-2  Re_8.1_OL-3
Ct_8.1_1         0.629        1.000        0.783        0.823        0.497        0.695        0.715        0.816        0.479         0.482         0.508         0.500        0.479        0.807        0.706
Ct_8.1_2         0.648        0.783        1.000        0.835        0.540        0.807        0.818        0.801        0.527         0.533         0.554         0.544        0.524        0.812        0.812
Ct_8.1_3         0.653        0.823        0.835        1.000        0.521        0.729        0.748        0.848        0.501         0.506         0.537         0.532        0.511        0.824        0.744
Ct_8.1_4         0.467        0.497        0.540        0.521        1.000        0.503        0.513        0.499        0.857         0.864         0.832         0.806        0.797        0.539        0.505
Ph_7.8_1         0.590        0.695        0.807        0.729        0.503        1.000        0.860        0.697        0.492         0.502         0.496         0.478        0.461        0.745        0.851
Ph_7.8_2         0.605        0.715        0.818        0.748        0.513        0.860        1.000        0.719        0.501         0.511         0.508         0.489        0.472        0.766        0.847
Ph_7.8_3         0.623        0.816        0.801        0.848        0.499        0.697        0.719        1.000        0.472         0.476         0.506         0.500        0.480        0.808        0.711
Ph_7.8_4         0.476        0.479        0.527        0.501        0.857        0.492        0.501        0.472        1.000         0.878         0.850         0.832        0.826        0.525        0.495
Ph_7.8_5         0.468        0.482        0.533        0.506        0.864        0.502        0.511 
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python - <<'EOF'
p='squidoa.py'; s=open(p).read()
s=s.replace('''    """RSEM.isoform.counts.matrix: transcripts by samples (expected counts). The header names 16
    samples and each row holds a transcript id and 15 values; as R's read.csv(row.names = 1) does
    in the authors' script, the first header name is taken as that of the id column."""''','''    """RSEM.isoform.counts.matrix: transcripts by samples (expected counts). The header names 16
    samples and each row holds a transcript id and 15 values. `names="r"` names them as R's
    read.csv(row.names = 1) does in the authors' script (the first header name taken as that of the
    id column); `names="first"` gives the values the first 15 header names, which the notebook
    shows is the right reading (the last sample, Re_8.1_OL-3, has no values)."""''')
s=s.replace('def read_count_matrix() -> pd.DataFrame:','def read_count_matrix(names: str = "first") -> pd.DataFrame:')
s=s.replace('''    df.columns = header[1:] if len(header) == df.shape[1] + 1 else header''','''    df.columns = header[1:] if names == "r" else header[:df.shape[1]]''')
open(p,'w').write(s)

g='/tmp/claude-1001/gen/nb3.py'; s=open(g).read()
a=s.index('with __import__("zipfile")')
b=s.index("del ws_raw, aligned")
s=s[:a]+'''with __import__("zipfile").ZipFile(sq.STAGED / "squid.zip") as z, z.open(sq.ZIP_DIR + "RSEM.isoform.counts.matrix") as f:
    f.readline()
    first = f.readline().decode().rstrip("\\n").split("\\t")
print(f"header names {len(header)} samples; a data row holds an id and {len(first) - 1} values")
ws_raw = sq.matrix(sq.read_rdata({"rawMatrix"})["rawMatrix"])
ws_raw.index = ["TRINITY_" + i for i in ws_raw.index]
print("Workspace rawMatrix (the script's 15 optic lobe samples):", ws_raw.shape, list(ws_raw.columns))
for how in ("r", "first"):
    cm = sq.read_count_matrix(how).reindex(ws_raw.index)
    match = {wc: next((fc for fc in cm.columns if np.array_equal(cm[fc].to_numpy(), ws_raw[wc].to_numpy())), None) for wc in ws_raw.columns}
    print(f"\\nFile columns named as {'R read.csv(row.names = 1) does' if how == 'r' else 'the first 15 header names'}; workspace column -> identical file column:")
    print(match)
    del cm
'''+s[b:].replace("del ws_raw, aligned","")
# replace the filter part to use ws_raw
s=s.replace('''counts = sq.read_count_matrix()
ol = [c for c in counts.columns if "_OL" in c or "-OL" in c]
raw = counts[ol]''','''raw = ws_raw''')
s=s.replace('''grp12 = [c for c in ol if not c.startswith("Re_")]''','''grp12 = [c for c in raw.columns if not c.startswith("Re_")]''')
s=s.replace('''print(f"\\nOptic lobe columns: {len(ol)}; rows with non-zero mean {len(kept_mean)}")''','''counts = sq.read_count_matrix("first")
fr = counts[[c for c in counts.columns if "OL" in c]]
fr = np.round(fr[fr.mean(axis=1) != 0])
print(f"\\nOn the workspace's 15 optic lobe samples; rows with non-zero mean {len(kept_mean)}")''')
s=s.replace('''print(f"variant, (a) on the 12 samples of the three groups: {filt_12}")''','''print(f"variant, (a) on the 12 samples of the three groups: {filt_12}")
print(f"variant, (a) on the file's 14 optic lobe columns (Re_8.1_OL-3 missing): {int(((fr >= 10).sum(axis=1) >= 3).sum())}")''')
s=s.replace("del counts, raw, kept_mean, rounded, r12","del counts, fr, raw, kept_mean, rounded, r12, ws_raw")
s=s.replace('''The transcript count is that of the deposited RSEM matrix; E78N50 and N50 are read from the
deposited `ExN50.stats` (Trinity's contig_ExN50_statistic.pl output, `Bash_scripts.sh`), as the
assembly FASTA is not in the dataset. The filter is applied to the 15 optic lobe columns of the
matrix as the deposited `R_scritps.Rmd` does it (reading (a): rows with a non-zero mean, rounded,
then at least 10 counts in at least 3 samples); reading (b) and the 12 samples of the three groups
alone are variants. Mapping rates are not deposited.''','''The transcript count is that of the deposited RSEM matrix; E78N50 and N50 are read from the
deposited `ExN50.stats` (Trinity's contig_ExN50_statistic.pl output, `Bash_scripts.sh`), as the
assembly FASTA is not in the dataset. The count file's header names 16 samples while its rows hold
15 values; the cell matches its columns to the workspace's `rawMatrix`, the 15 optic lobe samples
the script used. The filter is applied to `rawMatrix` as the deposited `R_scritps.Rmd` does it
(reading (a): rows with a non-zero mean, rounded, then at least 10 counts in at least 3 samples);
reading (b), the 12 samples of the three groups alone, and the file's own 14 optic lobe columns
are variants. Mapping rates are not deposited.''')
open(g,'w').write(s)
EOF
grep -n "ws_raw\|fr = \|counts = " $TMPDIR/gen/nb3.py | head -20
```

```
121:ws_raw = sq.matrix(sq.read_rdata({"rawMatrix"})["rawMatrix"])
122:ws_raw.index = ["TRINITY_" + i for i in ws_raw.index]
123:print("Workspace rawMatrix (the script's 15 optic lobe samples):", ws_raw.shape, list(ws_raw.columns))
125:    cm = sq.read_count_matrix(how).reindex(ws_raw.index)
126:    match = {wc: next((fc for fc in cm.columns if np.array_equal(cm[fc].to_numpy(), ws_raw[wc].to_numpy())), None) for wc in ws_raw.columns}
139:counts = sq.read_count_matrix("first")
140:fr = counts[[c for c in counts.columns if "OL" in c]]
141:fr = np.round(fr[fr.mean(axis=1) != 0])
149:del counts, fr, raw, kept_mean, rounded, r12, ws_raw
```

**Agent calls Bash**

```bash
sed -n 105,160p $TMPDIR/gen/nb3.py
```

```
(reading (a): rows with a non-zero mean, rounded, then at least 10 counts in at least 3 samples);
reading (b), the 12 samples of the three groups alone, and the file's own 14 optic lobe columns
are variants. Mapping rates are not deposited.
''')
code(r'''
header, n_rows = sq.count_matrix_rows()
print("RSEM.isoform.counts.matrix columns:", header)
print("transcripts (rows):", n_rows)
exn50 = pd.read_csv(pd.io.common.StringIO(sq.zip_text("ExN50.stats")), sep="\t")
print(exn50.columns.tolist(), len(exn50), "rows")
print("E78N50:", exn50.loc[exn50.Ex == 78, "ExN50"].item(), " maximum ExN50 from Ex 25 on:", exn50.loc[exn50.Ex >= 25, "ExN50"].max(),
      " N50 at Ex 100:", round(exn50.loc[exn50.Ex == 100, "ExN50"].item(), 1), " num_genes at Ex 100:", exn50.loc[exn50.Ex == 100, "num_genes"].item())
with __import__("zipfile").ZipFile(sq.STAGED / "squid.zip") as z, z.open(sq.ZIP_DIR + "RSEM.isoform.counts.matrix") as f:
    f.readline()
    first = f.readline().decode().rstrip("\n").split("\t")
print(f"header names {len(header)} samples; a data row holds an id and {len(first) - 1} values")
ws_raw = sq.matrix(sq.read_rdata({"rawMatrix"})["rawMatrix"])
ws_raw.index = ["TRINITY_" + i for i in ws_raw.index]
print("Workspace rawMatrix (the script's 15 optic lobe samples):", ws_raw.shape, list(ws_raw.columns))
for how in ("r", "first"):
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/rv/bin/activate && python - <<'EOF'
g='/tmp/claude-1001/gen/nb3.py'; s=open(g).read()
s=s.replace('''    del cm

raw = counts[ol]''','''    del cm
\'\'\', ["claim:rnaseq-assembly", "finding-count-matrix-columns"])
code(r\'\'\'
raw = ws_raw''')
s=s.replace('''\'\'\', ["claim:rnaseq-assembly", "finding-count-matrix-header"])''','''\'\'\', ["claim:rnaseq-assembly"])''')
s=s.replace('''**Result: reproduced for the four values the dataset holds; the mapping rate is not in it.** 902,413 transcripts,
E78N50 2038 bp and N50 475.5 bp (476) in the deposited statistics, and 69,368 transcripts after the
filter of the deposited script (reading (a)), the row count of the authors' DESeq2 results.''','''**Result: reproduced for the four values the dataset holds; the mapping rate is not in it.** 902,413
transcripts, E78N50 2038 bp and N50 475.5 bp (476) in the deposited statistics, and 69,368
transcripts after the filter of the deposited script on the workspace's `rawMatrix` (reading (a)),
the row count of the authors' DESeq2 results. The deposited count file cannot give this number by
itself: its 15 value columns are the workspace's gill sample and the first 14 optic lobe samples,
and Re_8.1_OL-3 is missing; read with the script's `read.csv(row.names = 1)`, every name is shifted
by one sample.''')
open(g,'w').write(s)
EOF
python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb && /usr/bin/time -f "%e s %M KB" jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output $TMPDIR/out.ipynb reproduce_allen_2026.ipynb 2>&1 | tail -1; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 55 | sed 's/\x1b\[[0-9;]*m//g' | head -30; python $TMPDIR/gen/show.py $TMPDIR/out.ipynb 0 | grep -c ERROR
```

```
92 cells
59.29 s 3922516 KB
##### cell 56 ['claim:rnaseq-assembly', 'finding-count-matrix-columns']
RSEM.isoform.counts.matrix columns: ['Ct_8.1_Gill-1', 'Ct_8.1_OL-1', 'Ct_8.1_OL-2', 'Ct_8.1_OL-3', 'Ct_8.1_OL-4', 'Ph_7.8_OL-1', 'Ph_7.8_OL-2', 'Ph_7.8_OL-3', 'Ph_7.8_OL-4', 'Ph_7.8_OL-5', 'Ph_7.8C-OL-1', 'Ph_7.8C-OL-2', 'Ph_7.8C-OL-3', 'Re_8.1_OL-1', 'Re_8.1_OL-2', 'Re_8.1_OL-3']
transcripts (rows): 902413
['Ex', 'ExN50', 'num_genes'] 100 rows
E78N50: 2038.0  maximum ExN50 from Ex 25 on: 2038.0  N50 at Ex 100: 475.5  num_genes at Ex 100: 610324
header names 16 samples; a data row holds an id and 15 values

Workspace rawMatrix (the script's 15 optic lobe samples): (902413, 15) ['Ct_8.1_1', 'Ct_8.1_2', 'Ct_8.1_3', 'Ct_8.1_4', 'Ph_7.8_1', 'Ph_7.8_2', 'Ph_7.8_3', 'Ph_7.8_4', 'Ph_7.8_5', 'Ph_7.8C_1', 'Ph_7.8C_2', 'Ph_7.8C_3', 'Re_8.1_1', 'Re_8.1_2', 'Re_8.1_3']


File columns named as R read.csv(row.names = 1) does; workspace column -> identical file column:
{'Ct_8.1_1': 'Ct_8.1_OL-2', 'Ct_8.1_2': 'Ct_8.1_OL-3', 'Ct_8.1_3': 'Ct_8.1_OL-4', 'Ct_8.1_4': 'Ph_7.8_OL-1', 'Ph_7.8_1': 'Ph_7.8_OL-2', 'Ph_7.8_2': 'Ph_7.8_OL-3', 'Ph_7.8_3': 'Ph_7.8_OL-4', 'Ph_7.8_4': 'Ph_7.8_OL-5', 'Ph_7.8_5': 'Ph_7.8C-OL-1', 'Ph_7.8C_1': 'Ph_7.8C-OL-2', 'Ph_7.8C_2': 'Ph_7.8C-OL-3', 'Ph_7.8C_3': 'Re_8.1_OL-1', 'Re_8.1_1': 'Re_8.1_OL-2', 'Re_8.1_2': 'Re_8.1_OL-3', 'Re_8.1_3': None}


File columns named as the first 15 header names; workspace column -> identical file column:
{'Ct_8.1_1': 'Ct_8.1_OL-1', 'Ct_8.1_2': 'Ct_8.1_OL-2', 'Ct_8.1_3': 'Ct_8.1_OL-3', 'Ct_8.1_4': 'Ct_8.1_OL-4', 'Ph_7.8_1': 'Ph_7.8_OL-1', 'Ph_7.8_2': 'Ph_7.8_OL-2', 'Ph_7.8_3': 'Ph_7.8_OL-3', 'Ph_7.8_4': 'Ph_7.8_OL-4', 'Ph_7.8_5': 'Ph_7.8_OL-5', 'Ph_7.8C_1': 'Ph_7.8C-OL-1', 'Ph_7.8C_2': 'Ph_7.8C-OL-2', 'Ph_7.8C_3': 'Ph_7.8C-OL-3', 'Re_8.1_1': 'Re_8.1_OL-1', 'Re_8.1_2': 'Re_8.1_OL-2', 'Re_8.1_3': None}

##### cell 57 ['claim:rnaseq-assembly']
[... 13 more lines not kept]
```

**Agent**

All cells run without error in 59 s, 3.9 GB peak. Now the entry files, the attempt record and the reader questions.

**Agent calls Bash**

```bash
date -u; cd  cat questions/README.md | head -60; head -40 questions/bech-2026.yaml; python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
for k in ['datasets','provenance','inputs','missing_datasets']: print(k, json.dumps(s['properties'][k])[:1500])
"
```

```
Wed Nov 25 20:39:19 UTC 2026
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
settle is a question for the paper's authors, recorded in the claim's notes and as a
`methods_unavailable` finding in the attempt. Files from before protocol `pilot-11` also hold
questions about method details, asked under the earlier rule.
dandiset: "001847"
paper: doi:10.7554/elife.109717
questions:
- claim: fig2d-auditory-a1-frontal
  asked: 2026-11-04
  question: The opening comment's null (i) for the opto map shuffles the block labels of whole blocks
    and recomputes ΔP(Lick) against the control trials. Under that null the laser trials keep their
    outcomes and only their context labels move, so an effect of the laser that is shared by both
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l -i "dryad\|^paper:" questions/*.yaml | head -5; head -5 $(grep -l -i "dryad" questions/*.yaml | head -1) 2>/dev/null; grep -rn "questions" tools/entry.py | head -10; cat entries/dias-2025/requirements.in
```

```
questions/ashworth-2025.yaml
questions/athalye-2023.yaml
questions/bech-2026.yaml
questions/bellvila-2026.yaml
questions/bennett-2024.yaml
# Questions from attempt dias-2025-01 (author, 2026-10-27) about the claims file
# claims/dryad-bvq83bkk9/10.1098-rspb.2024.2556.yaml. Each is asked under docs/protocol.md, Author,
# step 1.6. The attempt applied the criteria as written and showed ten further seed sets.
dataset: DRYAD:bvq83bkk9
paper: doi:10.1098/rspb.2024.2556
cmdstanpy
matplotlib
numpy
pandas
rdata
```

**Agent**

Now writing the entry files, questions and attempt record.

**Agent calls Bash**

```bash
cat > entries/allen-2026/requirements.in <<'EOF'
matplotlib
numpy
pandas
scipy
statsmodels
EOF
cat > entries/allen-2026/entry.yaml <<'EOF'
schema_version: 1
name: allen-2026
type: reproduction
title: Squid under ocean acidification, physiology, behaviour, vision and optic lobe transcriptome (Allen et al. 2026)
description: Tests the findings of Allen, Yan, Kuan et al. (2026) on Dryad dataset rjdfn2zqz, which holds
  per-squid metabolic, hemolymph, behavioural and critical flicker fusion values, group means of the ERG
  response ratio, and the authors' RSEM count matrix and R workspace with their DESeq2, sva and GSEA
  results for the optic lobe transcriptome. It reruns the paper's tests on the per-squid values, reads
  the transcriptomic results from the workspace with a streaming R-serialization reader, and checks the
  files against each other and against the paper.
license: Apache-2.0
notebooks:
- path: reproduce_allen_2026.ipynb
  title: Reproducing Allen et al. (2026) from Dryad rjdfn2zqz
  runtime_minutes: 2
helpers:
- squidoa.py
related:
- id: dryad:rjdfn2zqz/439366
  relation: uses_data
- id: doi:10.1038/s42003-025-09506-6
  relation: reproduces
EOF
cat > questions/allen-2026.yaml <<'EOF'
# Questions from attempt allen-2026-01 (author, 2026-11-25) about the claims file
# claims/allen-2026.yaml. Each is asked under docs/protocol.md, Author, step 1.6. The attempt applied
# the criteria as written and showed the reading the questions propose as a variant.
dataset: DRYAD:rjdfn2zqz
paper: doi:10.1038/s42003-025-09506-6
questions:
- claim: fig4b-shared-down-sets
  asked: 2026-11-25
  question: The criterion reads "36" as (a) the sets down-regulated in either treatment or (b) all sets
    of the Venn diagram. The Results sentence goes on to cite "the intersect GSEA ridgeplot", and the
    deposited script (squid.zip, R_scritps.Rmd, Figure 4C chunk) plots the sets significant in both
    treatments with showCategory = 36. Should the criterion's readings include the sets significant
    in both treatments, in any direction?
  passage: Results, RNA-seq profiling in the optic lobes, paragraph 2, "only 2 out of 36 GO gene sets
    were down-regulated in both acute and chronic acidified conditions ... as indicated in the
    intersect GSEA ridgeplot"; Figure 4C legend, "Ridge plots comparing normalized enrichment scores
    (NES) of significantly altered GO terms between acute (left) and chronic (right) OA versus control".
  why: In the authors' GSEA results the two shared down-regulated sets are the two the paper names,
    but reading (a) gives 122 sets and (b) 646, so the claim is recorded as partially reproduced. The
    sets significant in both treatments number 36, which would make it reproduced.
- claim: fig4fgh-chronic-up
  asked: 2026-11-25
  question: The criterion counts every chronic-OA set with positive NES per ontology. The legend speaks
    of "clustered and simplified terms", and the deposited script (Figure 4F-H chunk) takes the
    chronic-OA up-regulated sets that are not down-regulated in acute-OA and passes them to
    simplifyEnrichment. Is the paper's count (82 CC, 308 BP, 128 MF) that subset?
  passage: Figure 4 legend, "Heatmaps of upregulated GO terms under chronic acidification, displaying
    clustered and simplified terms for F cellular components (CC, 82 gene sets), G biological
    processes (BP, 308 gene sets), and H molecular functions (MF, 128 gene sets)".
  why: Counted as the criterion says, the authors' results give 101 CC (out of the 82 ± 8.2
    tolerance), 321 BP and 133 MF, so the claim is partially reproduced. The script's subset gives
    82 CC, 314 BP and 128 MF, all within tolerance.
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/attempt.py <<'PYEOF'
import yaml
NB = "reproduce_allen_2026.ipynb"
def o(claim, outcome, notes, measured=None, deviations=None, blocked_by=None, assumed=None, output=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if output:
        d["notebook"] = NB
        d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed: d["assumed"] = True
    return d

AS_DEPOSITED = "The per-squid values are taken as deposited; the raw recordings they were computed from are not in the dataset."
outcomes = [
 o("fig1b-metabolic-rate", "reproduced",
   "Means 16.88, 18.93 and 23.88 umol O2 g-1 h-1 (11, 9 and 6 squid), chronic-OA 41.5% above control. One-way ANOVA F(2,23) = 3.80, p = 0.0375, eta^2 = 0.25; Tukey control against chronic-OA p = 0.030, control against acute-OA p = 0.64, acute-OA against chronic-OA p = 0.17. The paper's ANOVA has 29 squid, F(2,26) = 4.473, p = 0.021 (SS 235.4 and 684.2 against 191.3 and 578.9 here); the deposited means equal the paper's means to the printed digits.",
   [16.88, 18.93, 23.88, 41.5],
   [AS_DEPOSITED, "26 squid where the paper's ANOVA has 29 (finding)."]),
 o("fig1c-ammonia-excretion", "reproduced",
   "Means 3.34, 2.86 and 1.61 umol g-1 h-1 (5, 9, 7 squid); reductions of chronic-OA 51.8% against control and 43.6% against acute-OA. One-way ANOVA on log10 rates F(2,18) = 6.382, p = 0.008038, the paper's values and sums of squares; Tukey control against chronic-OA p = 0.009, acute-OA against chronic-OA p = 0.038, control against acute-OA p = 0.52. Untransformed, F = 4.49, p = 0.026.",
   [3.34, 2.86, 1.61, 51.8, 43.6], [AS_DEPOSITED]),
 o("fig1d-blood-ph", "reproduced",
   "Means 7.092, 7.145 and 7.175 (7, 6, 9 squid). Welch's ANOVA W = 6.347, df 2, 9.196, p = 0.0185; the paper prints W = 5.983 with the same df and p = 0.00965. Dunnett's T3 control against chronic-OA p = 0.017, control against acute-OA p = 0.46, acute-OA against chronic-OA p = 0.86 (paper 0.015, 0.391, 0.754). The intervals here are wider than the paper's (control against chronic-OA -0.150 to -0.015 against -0.129 to -0.036).",
   [7.092, 7.145, 7.175],
   ["Welch's ANOVA and Dunnett's T3 are implemented in squidoa.py (Welch 1951; studentized maximum modulus with k = 3); GraphPad Prism, which the paper used, was not available, and its W and intervals differ from these on the same values."]),
 o("fig1e-blood-pco2", "reproduced",
   "Means 1057.4, 1583.8 and 2778.7 uatm, fold changes 2.63 (chronic-OA) and 1.50 (acute-OA). Welch's ANOVA W = 29.815, df 2, 12.04, p = 2.2e-05 (paper 27.653, df 2, 9.379, p < 0.0001). Dunnett's T3 p = 0.014 (control against acute-OA), below 0.0001 (control against chronic-OA) and 0.0008 (acute-OA against chronic-OA). The deposited PCO2 is a tenth of what the formula printed beside each value in Carbonate_calibration.csv gives (finding); fold changes and tests are the same under either scale.",
   [1057.4, 1583.8, 2778.7, 2.63, 1.50],
   ["PCO2 as deposited (the criterion), not derived again; the deposit's own Eq. 1 with alpha 0.0312 and pKa1 6.10 gives values 10 times larger.", "Welch's ANOVA and Dunnett's T3 implemented in squidoa.py, as for fig1d-blood-ph."]),
 o("fig1f-blood-bicarbonate", "reproduced",
   "Means 3.56, 5.90 and 11.08 mmol/l, fold changes 3.11 (chronic-OA) and 1.65 (acute-OA). Welch's ANOVA W = 42.84, df 2, 12.54, p = 2.5e-06 (paper 39.545, df 2, 12.59). Dunnett's T3 p = 0.0008, below 0.0001 and 0.0002. Eq. 2 with the printed PCO2 gives the deposited [HCO3-] (max difference 0.0006); with the formula's tenfold PCO2 the values would be up to 1.08 mmol/l lower.",
   [3.56, 5.90, 11.08, 3.11, 1.65],
   ["[HCO3-] as deposited (the criterion).", "Welch's ANOVA and Dunnett's T3 implemented in squidoa.py, as for fig1d-blood-ph."]),
 o("methods-body-size", "blocked",
   "No file of the dataset holds fresh mass or mantle length (file list and every column in the notebook's data check). Only rates already divided by mass and distances already divided by mantle length are deposited.",
   blocked_by="data_missing", output=False),
 o("stable5-seawater-chemistry", "blocked",
   "No file holds seawater pH, total alkalinity or PCO2. Carbonate_calibration.csv, which the README describes as carbonate calculations, holds the hemolymph calculation only. The paper's Data availability lists carbonate chemistry calculations in the deposit.",
   blocked_by="data_missing", output=False),
 o("sfig2-distance-unchanged", "reproduced",
   "Means 132.9, 124.4 and 147.4 mantle lengths (15, 8, 11 squid); Kruskal-Wallis H = 0.4124, p = 0.8137, the paper's values; epsilon^2 = 0.013.",
   [132.9, 124.4, 147.4],
   ["Distance per squid as deposited; Eq. 3 and the handling of untracked samples cannot be applied, as the 3-D tracks are not in the dataset."]),
 o("fig2c-velocity-unchanged", "reproduced",
   "Means 0.2215, 0.2074 and 0.2456 mantle lengths/s; the control mean lies within 0.15 to 0.25. Kruskal-Wallis H = 0.4124, p = 0.8137, the paper's values (the velocities are the distances over 600 s for every squid, so the test is the same). The velocity file has 8 acute-OA squid, so there is no ninth squid to show.",
   [0.2215, 0.2074, 0.2456], [AS_DEPOSITED]),
 o("fig2d-acute-upper-zone", "reproduced",
   "The zone file holds 9 acute-OA squid; leaving out the ninth (59.6% upper, 1.3% left, 6.7% front) gives the paper's treatment sums of squares for all three zones (25397.6, 42.9, 2436.7), and no other single exclusion comes near. With it, means 30.0, 86.0 and 14.7%, F(2,31) = 12.07, p = 0.000133, eta^2 = 0.44; Tukey control against acute-OA p = 0.0012, acute-OA against chronic-OA p = 0.0001, control against chronic-OA p = 0.47. With all 9 acute-OA squid, acute-OA 83.1%, F(2,32) = 12.14, p = 0.00012 and the same Tukey pattern.",
   [30.0, 86.0, 14.7],
   ["Zone percentages as deposited, so the denominator readings (a) and (b) of the criterion cannot be told apart.", "The paper's 8 acute-OA squid are identified by matching the sums of squares of Supplementary Table 3; the dataset does not mark the excluded squid."]),
 o("stable3-acute-shallower", "blocked",
   "Mean depth needs the vertical coordinate of the tracks, which are not in the dataset; only the percentage of time in the upper zone is deposited.",
   blocked_by="data_missing", output=False),
 o("fig2e-left-right-unchanged", "reproduced",
   "With the paper's 8 acute-OA squid (see fig2d-acute-upper-zone) means 55.8, 54.1 and 57.1%; one-way ANOVA F(2,31) = 0.027, p = 0.973 (the paper's values), eta^2 = 0.002. Log10 variant (one zero left out) F = 0.10, p = 0.90. With all 9 acute-OA squid, F = 0.27, p = 0.77.",
   [55.8, 54.1, 57.1], ["The ninth acute-OA squid is left out to match the paper, as for fig2d-acute-upper-zone."]),
 o("fig2f-front-back-unchanged", "reproduced",
   "With the paper's 8 acute-OA squid means 58.3, 80.0 and 66.1%; one-way ANOVA F(2,31) = 1.326, p = 0.280 (the paper's values), eta^2 = 0.079. Log10 variant (two zeros left out) F = 1.63, p = 0.21. With all 9, F = 0.52, p = 0.60.",
   [58.3, 80.0, 66.1], ["The ninth acute-OA squid is left out to match the paper, as for fig2d-acute-upper-zone.", "The front/back divide was applied before deposit; the halfway assumption of the criterion cannot be checked."]),
 o("fig2g-attack-willingness", "not_reproduced",
   "Squid_Prey_Capture.csv holds 46 control, 36 acute-OA and 11 chronic-OA squid, with 29, 8 and 8 attacks. Control and acute-OA counts match the paper; chronic-OA is 8 of 11 against 8 of 22, so its reduction is -15.4% against 42.3% (acute-OA 64.8%). Reading (a) on the file gives pH coefficient -1.117 (p = 0.55) and time 0.0269 (p = 0.0045), residual deviance 111.63, ROC area 0.714; readings (b) and (c) give pH p = 0.0002 with time p = 0.004. No reading meets the criterion (pH p < 0.05 with lower attack at lower pH, time p >= 0.05, counts matching). The R workspace's Figure 2G table (F2G) gives 22 chronic-OA squid with 36.36% attacking; with those counts reading (a) gives the paper's model exactly (pH 2.734246, p = 0.0422; time 0.008351, p = 0.246; deviances 142.28 and 127.58; ROC area 0.6992; intercept -22.64). The result therefore turns on 11 chronic-OA squid missing from the per-squid file.",
   [29, 8, 8, 64.8, -15.4, -1.117, 111.63, 0.7141],
   ["Measured values are those of the per-squid file under reading (a); the counts of the workspace's F2G table are shown as a variant."]),
 o("fig2h-hunt-duration", "reproduced",
   "Means 106.7 s (control, 29 squid), 262.2 s (acute-OA, 8) and 109.5 s (chronic-OA, 8), acute-OA 2.46-fold control. ANOVA on log10 durations F(2,42) = 3.372, p = 0.0439 with the paper's sums of squares (2.374 and 14.79); Tukey control against acute-OA p = 0.035 (paper 0.03), chronic-OA against control p = 0.72 and against acute-OA p = 0.32. Untransformed, F = 4.26, p = 0.021.",
   [106.7, 262.2, 2.46]),
 o("fig2i-strike-attempts", "reproduced",
   "38 of 45 attacking squid (84.4%) needed 1 or 2 attempts (control 89.7%, acute-OA and chronic-OA 75%). Kruskal-Wallis H = 2.568, p = 0.2769, the paper's values. The file codes capture as success or fail and every squid with attempts has a capture time; it records no squid that struck and failed, so the capture part holds as far as the file can show."),
 o("sfig3-prey-velocity-unchanged", "reproduced",
   "Table S3 of the R workspace, the only copy of these data: two-way ANOVA (pH by time) gives pH p = 0.84, time p = 0.11, interaction p = 0.84 (type III; type II pH 0.83, time 0.11, interaction 0.84). The CO2 10-20 min column is identical to the control 10-20 min column (8 values; the legend gives 11 CO2 shrimp), so the deposited data cannot show the CO2 shrimp at 20 min (finding). At 0-10 min alone, control 0.224 and CO2 0.170 cm/s, Welch t p = 0.65, Mann-Whitney p = 0.44.",
   deviations=["A repeated-measures variant is not run: no shrimp identifier links the time points, and the CO2 columns hold 11 and 8 values.", "Type III sums of squares as the main reading (Prism's choice for unequal cells, a standard choice); type II shown."]),
 o("fig3c-ratio-declines", "not_reproduced",
   "The dataset holds only group means per stimulus frequency. In no group is the mean ratio below its 20 Hz value at every frequency above 40 Hz: control 0.998 (45 Hz) and 0.990 (50 Hz) against 0.977 at 20 Hz; acute-OA 0.998 (45 Hz) and 1.062 (57.5 Hz); chronic-OA 1.039 (47 Hz) against 0.996. The 65 Hz value is the lowest in acute-OA (0.300) but more than 0.1 above the lowest in control (0.391 against 0.284) and chronic-OA (0.361 against 0.252). The decline the statement describes is there above 50 Hz: mean ratio up to 50 Hz 1.00, 0.97 and 0.80, above 50 Hz 0.38, 0.53 and 0.43 (control, acute-OA, chronic-OA). The criterion's every-frequency-above-40-Hz condition fails, partly on single-squid means (rows without an SD).",
   deviations=["The criterion's per-squid FFT analysis cannot be run: the ERG traces and spectra are not deposited. The deposited group means of the ratio are used."]),
 o("sfig4a-amplitude-attenuation", "blocked",
   "Needs ERG traces or spectra; the dataset holds only the ratio of maximum response frequency to stimulus frequency as group means (Squid_ERG.csv) and CFF per squid.",
   blocked_by="data_missing", output=False),
 o("fig3d-cff-unchanged", "reproduced",
   "Reading (b), the CFF the dataset gives per squid (3, 3, 6 squid): means 50.67, 50.67 and 47.67 Hz; one-way ANOVA F(2,9) = 0.541, p = 0.60, eta^2 = 0.11; Tukey p >= 0.68 for every pair; Kruskal-Wallis p = 0.65. Reading (a) cannot be run (no per-squid ratios). From the deposited group mean ratios, the highest frequency with a mean of at least 0.9 is 50, 57.5 and 47 Hz.",
   [50.67, 50.67, 47.67],
   ["Only reading (b) can be run; the per-squid ratios of reading (a) are not deposited."]),
 o("fig3d-cff-variance", "reproduced",
   "Sample SDs 1.155, 6.028 and 5.465 Hz; ratios 5.22 (acute-OA) and 4.73 (chronic-OA), both in 3.6 to 5.5. The control SD rests on 3 squid. Not judged, a Brown-Forsythe test p = 0.61.",
   [5.22, 4.73]),
 o("rnaseq-assembly", "reproduced",
   "Transcripts 902,413 (rows of the count matrix and of the workspace's rawMatrix); E78N50 2038 bp and N50 475.5 bp from the deposited ExN50.stats; 69,368 transcripts after the filter of the deposited script (reading (a)) applied to the workspace's rawMatrix, the row count of the authors' DESeq2 results. Reading (b) gives 172,901. The mean mapping rate is not in the dataset and is not tested; the other four values are within tolerance. The deposited count file alone gives 66,006 (its own 14 optic lobe columns), as it lacks Re_8.1_OL-3 (finding).",
   deviations=["Assembly statistics read from the deposited ExN50.stats (Trinity's output), as the assembly FASTA is not in the dataset; the TSA record was not used.", "The mapping rate (99.51%) is not tested: no alignment log is deposited, and realigning the SRA reads is outside what this run can do.", "Tested on the dataset's count matrix and R workspace, not on the SRA reads the claims file names under where."]),
 o("fig4a-pca", "partially_reproduced",
   "The deposited vstsva.adj.limma equals removeBatchEffect of vstsva.adj with the two surrogate variables (max difference 1.4e-14). Reading (a), PCA of the 12 samples of the three groups: PC1 35.0%, PC2 15.0%, the paper's values. Acute-OA centroid 3.5 from control on PC1 against 62.9 for chronic-OA; chronic-OA separated from control on PC1 (62.9 against a control range of 13.4). On PC2 the chronic-OA centroid is 18.0 from control, less than the control range 29.6 and more than the control SD 12.8; 1 of 3 chronic-OA samples lies outside the control range. Under the range reading the PC2 separation fails, under the SD reading it holds. The script's PCA of all 15 samples gives 29.0% and 13.5%. Reading (b), known batches removed, gives PC1 above 90%.",
   [35.0, 15.0],
   ["Tested on the authors' saved VST matrices, not recomputed from counts with DESeq2 and sva.", "Assumption. The criterion's control spread is read as the range of the 4 control samples on each PC, so that chronic-OA must lie beyond the control samples to count as separated, which is how the paper's \"significant divergence along both PC1 and PC2\" is read here; under the SD reading the claim would be reproduced. The paper gives no measure of divergence."],
   assumed=True),
 o("sfig5b-acute-clusters-with-control", "reproduced",
   "Euclidean distances on the batch-corrected matrix (12 samples, 69,368 rows): mean acute-OA to control 187.7, chronic-OA to control 255.2, control to control 197.7, maximum 286.1. Reading (b) gives the same order (729.5 against 868.1).",
   deviations=["Tested on the authors' saved VST matrix."]),
 o("fig4b-shared-down-sets", "partially_reproduced",
   "In the authors' GSEA results exactly 2 sets are down-regulated in both treatments, organelle inner membrane and mitochondrial inner membrane. The count 36 is not matched under the criterion's readings, (a) 122 sets down in either treatment and (b) 646 sets in the Venn diagram. The sets significant in both treatments, which the deposited script plots in Figure 4C and the Results call the intersect GSEA ridgeplot, number 36; this reading is asked of a reader (questions/allen-2026.yaml).",
   [2],
   ["GSEA is not re-run (clusterProfiler, the authors' AnnotationForge database and R are not in this environment); the authors' saved gseaResult objects are read. Their stored parameters match the Methods, and their ranked lists equal the shrunken fold changes of the saved DESeq2 results."]),
 o("fig4c-acute-ridge", "reproduced",
   "In the acute-OA results (87 sets, all BH-adjusted p < 0.05) each named family has a down-regulated term: cellular lipid metabolic process (NES -1.39), carboxylic acid and organic acid metabolic process (-1.47), transferase complex (-1.62), endopeptidase complex (-1.92), ribosomal subunit (-2.24, also large and small subunits); cell-cell adhesion is up (1.45).",
   deviations=["The authors' saved GSEA results are read, not re-run (see fig4b-shared-down-sets)."]),
 o("fig4d-acute-tree", "reproduced",
   "Down-regulated in acute-OA: respirasome and mitochondrial respirasome (-1.86, -2.15), respiratory chain complex IV (-1.84, -2.00), mitochondrial envelope (-2.01), fatty acid biosynthetic process (-1.79) and fatty acid elongase activity (-1.88), protein localization to membrane (-1.72) and to organelle (-1.63), RNA 3'-end processing (-1.87) and ribonucleoprotein complex biogenesis (-1.53). All also among the 51 sets of the script's tree (acute-OA down, not significant in chronic-OA).",
   deviations=["The authors' saved GSEA results are read, not re-run."]),
 o("fig4e-chronic-synaptic-down", "reproduced",
   "Among 40 chronic-OA down-regulated sets: postsynaptic membrane (NES -1.91), synaptic membrane (-1.92), transmitter-gated channel activity (-1.80), neurotransmitter receptor activity (-1.83), NAD(P)H dehydrogenase (quinone) activity (-1.89), respiratory electron transport chain (-1.55), cell adhesion (-1.40) and prefoldin complex (-2.02).",
   deviations=["The authors' saved GSEA results are read, not re-run."]),
 o("fig4fgh-chronic-up", "partially_reproduced",
   "Chronic-OA sets with positive NES, per ontology: 101 CC (82 +- 8.2 expected), 321 BP (308 +- 30.8) and 133 MF (128 +- 12.8); CC is out of tolerance. Every named family has an up-regulated term (vesicle 29 terms, endosome 4, Golgi 12, purine biosynthesis 6, carbohydrate catabolic process 1, ribonucleoprotein 5, ubiquitin 13, oxidoreductase 4, hydrolase 10, transporter activity 4). The script's subset, up in chronic-OA and not down in acute-OA, gives 82 CC, 314 BP and 128 MF; whether the paper counts that subset is asked of a reader.",
   [101, 321, 133],
   ["The authors' saved GSEA results are read, not re-run. simplifyEnrichment's GO_similarity, which the script applies before counting, cannot be run here."]),
 o("chronic-nachr-subunits-down", "reproduced",
   "Transcripts named by the authors' annotation table (DB name): alpha-7 4, alpha-10 29, beta-4 1. Reading (a), core enrichment genes of the 7 chronic-OA down-regulated synaptic sets (59 genes) include 2 alpha-7, 10 alpha-10 and the 1 beta-4 transcript. Reading (b), shrunken log2 fold change chronic-OA against control: alpha-7 2 of 2 tested negative (-0.64, -1.03), alpha-10 14 of 17 negative, beta-4 negative (-0.87); no transcript has adjusted p below 0.09.",
   deviations=["Subunits identified from the protein names of the authors' annotation table, the table the script passes to AnnotationForge; the Supplementary GSEA results file the paper cites was not available."]),
 o("optic-lobe-no-ion-regulation", "not_reproduced",
   "No acute-OA term matches the criterion's words. Three chronic-OA terms do, all up-regulated: transition metal ion transmembrane transporter activity (NES 2.13, adjusted p = 0.004), organic anion transmembrane transporter activity (1.87, p = 0.033, matched through \"anion transmembrane transport\") and metal cation:proton antiporter activity (1.70, p = 0.034). The chronic-OA down-regulated sets also include several ion channel activity terms (for example monoatomic ion gated channel activity, NES -1.59), which the criterion's words do not match.",
   deviations=["The authors' saved GSEA results are read, not re-run."]),
]

findings = [
 {"kind": "format_error", "about": "data", "severity": "critical",
  "statement": "RSEM.isoform.counts.matrix in squid.zip names 16 samples in its header (Ct_8.1_Gill-1 and 15 optic lobe samples) but each row holds a transcript id and 15 values. Matched against the authors' rawMatrix in Squid.RData, the 15 value columns are the gill sample and the first 14 optic lobe samples; Re_8.1_OL-3 has no values. Read as the authors' script reads it (read.csv with row.names = 1), every sample name shifts by one, so the gill sample is labelled Ct_8.1_OL-1, and the expression filter gives 67,088 or 66,006 transcripts in place of the paper's 69,368, which the workspace's rawMatrix gives.",
  "notebook": NB, "output": "finding-count-matrix-columns"},
 {"kind": "other", "about": "data", "severity": "critical",
  "statement": "In the prey shrimp table of the R workspace (behavior_and_physiology_data$S3, the only copy of the Supplementary Figure 3 data), the column \"pH 7.8 10-20 Min\" is identical to \"pH 8.1 10-20 Min\" (8 values), so the CO2-exposed shrimp at 20 min are the control shrimp's values; the legend gives 11 CO2 shrimp.",
  "notebook": NB, "output": "finding-shrimp-duplicate-column"},
 {"kind": "data_missing", "about": "data", "severity": "major",
  "statement": "Squid_Prey_Capture.csv holds 11 chronic-OA squid (8 attacked), where the paper, its logistic regression and the workspace's Figure 2G table (F2G, N = 22, 36.36% attacking) have 22. The 11 missing chronic-OA squid change the logistic regression of Figure 2G: on the file the pH effect is not significant under the paper's coding.",
  "notebook": NB, "output": "finding-prey-capture-chronic-missing"},
 {"kind": "other", "about": "data", "severity": "major",
  "statement": "In Carbonate_calibration.csv each row prints Eq. 1 with alphaCO2 0.0312, pKa1 6.10 and a factor 10^3, which evaluates to 10.0 times the PCO2 printed in the same row (for example 4.20/[(1+10.35)x0.0312]x10^3 = 11,859 against 1186.2 uatm). Squid_Hemolymph.csv and the paper report the smaller values, and the deposited [HCO3-] follows Eq. 2 with them. Either the formula or the values are off by a factor of 10; the files do not say which, and alphaCO2 has no unit.",
  "notebook": NB, "output": "finding-pco2-factor-10"},
 {"kind": "data_missing", "about": "data", "severity": "major",
  "statement": "The paper's Data availability statement places the behavioural tracking data, ERG recordings and carbonate chemistry calculations in this deposit. The dataset holds only per-squid summaries of the tracking (distance, velocity, zone percentages), group means and SDs of the ERG response ratio per frequency (no traces, spectra or per-squid values), CFF per squid, and the hemolymph carbonate calculation; there are no 3-D tracks, depth, ERG recordings, seawater chemistry, body masses or mantle lengths. Four of the paper's findings cannot be tested and three others only on the deposited summaries.",
  "notebook": NB, "output": "finding-not-deposited"},
 {"kind": "selection_undocumented", "about": "data", "severity": "minor",
  "statement": "Squid_Behavioral_assessment.csv holds 9 acute-OA squid, where the paper's ANOVAs (F(2,31)) and the distance and velocity files have 8. Leaving out the ninth row (59.6% upper, 1.3% left, 6.7% front) gives the paper's sums of squares for all three zones; nothing in the files marks it as excluded. With it, the acute-OA upper-zone mean is 83.1% against the paper's 86.0%.",
  "notebook": NB, "output": "finding-zone-extra-acute-squid"},
 {"kind": "data_missing", "about": "data", "severity": "minor",
  "statement": "Squid_RMR.csv holds 26 squid (11, 9, 6), where Supplementary Table 1's ANOVA has 29 (F(2,26)); the deposited means equal the paper's to the printed digits.",
  "notebook": NB, "output": "finding-rmr-count"},
 {"kind": "identifier_missing", "about": "data", "severity": "minor",
  "statement": "No file gives a squid identifier, tank or rearing batch, so values cannot be linked across files (for example which acute-OA squid of the zone file is missing from the distance file) or checked against the paper's sampling across four tanks per treatment."},
 {"kind": "metadata_error", "about": "data", "severity": "minor",
  "statement": "The README gives the hemolymph PCO2 unit as atm; the column header and values are in uatm (785.9 to 3861.9). The README also calls the control group pH 8.1 for the behavioural file and pH 8.2 elsewhere."},
 {"kind": "methods_unavailable",
  "statement": "Question for the authors. Figure 4A says chronic-OA samples showed significant divergence along both PC1 and PC2. How was divergence along PC2 judged? On the deposited batch-corrected matrix the chronic-OA centroid is 18.0 units from the control centroid on PC2, more than the control SD (12.8) but less than the range of the four control samples (29.6); the attempt assumed the range."},
 {"kind": "paper_inconsistency",
  "statement": "Supplementary Table 4 prints the logistic regression intercept as 22.364913 with z = -2.163; the coefficients and the counts of the paper give -22.64 (z = -2.16), so the printed sign is wrong."},
 {"kind": "code_mismatch",
  "statement": "The deposited R_scritps.Rmd computes the Figure 4A PCA on all 15 samples (including Re_8.1) and keeps 12 (x[1:12,]), which gives PC1 29.0% and PC2 13.5%; the figure's 35% and 15% come from a PCA of the 12 samples alone, which the chunk's last line also calls."},
]

rec = {
 "schema_version": 3,
 "id": "allen-2026-01",
 "datasets": [{"archive": "dryad", "id": "rjdfn2zqz", "version": "439366", "doi": "10.5061/dryad.rjdfn2zqz", "relation": "primary"}],
 "paper": "doi:10.1038/s42003-025-09506-6",
 "date": "2026-11-25",
 "entry": "allen-2026",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
   "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-19"},
   "runner": {"platform": "GitHub Actions", "url": "https://github.com/encorescience/encore-registry/actions/runs/45691797114"}},
 "inputs": [],
 "outcomes": outcomes,
 "findings": findings,
}
order = ["fig1b-metabolic-rate","fig1c-ammonia-excretion","fig1d-blood-ph","fig1e-blood-pco2","fig1f-blood-bicarbonate","methods-body-size","stable5-seawater-chemistry","fig2c-velocity-unchanged","sfig2-distance-unchanged","fig2d-acute-upper-zone","stable3-acute-shallower","fig2e-left-right-unchanged","fig2f-front-back-unchanged","fig2g-attack-willingness","fig2h-hunt-duration","fig2i-strike-attempts","sfig3-prey-velocity-unchanged","fig3c-ratio-declines","sfig4a-amplitude-attenuation","fig3d-cff-unchanged","fig3d-cff-variance","rnaseq-assembly","fig4a-pca","sfig5b-acute-clusters-with-control","fig4b-shared-down-sets","fig4c-acute-ridge","fig4d-acute-tree","fig4e-chronic-synaptic-down","fig4fgh-chronic-up","chronic-nachr-subunits-down","optic-lobe-no-ion-regulation"]
byid = {x["claim"]: x for x in outcomes}
assert set(byid) == set(order), set(order) ^ set(byid)
rec["outcomes"] = [byid[c] for c in order]
del rec["inputs"]
with open("attempts/allen-2026-01.yaml", "w") as f:
    f.write("# Attempt on Allen, Yan, Kuan et al. (2026) with Dryad rjdfn2zqz version 439366 (docs/protocol.md).\n")
    yaml.safe_dump(rec, f, sort_keys=False, allow_unicode=True, width=100)
print("written")
PYEOF
cd  && python $TMPDIR/gen/attempt.py && grep -c "claim:" attempts/allen-2026-01.yaml
```

```
written
58
```

**Agent calls Bash**

```bash
python -c "
import yaml; c=yaml.safe_load(open('claims/allen-2026.yaml')); a=yaml.safe_load(open('attempts/allen-2026-01.yaml'))
ci=[x['id'] for x in c['claims']]; ai=[x['claim'] for x in a['outcomes']]; print(len(ci), len(ai), set(ci)^set(ai))
import nbformat; nb=nbformat.read('entries/allen-2026/reproduce_allen_2026.ipynb',4)
tags=set(t for cl in nb.cells for t in cl.metadata.get('tags',[])); print(sorted(t for t in tags if t.startswith('finding')))
print(sorted(set('claim:'+x for x in ai)-tags))
"
```

```
31 31 set()
['finding-count-matrix-columns', 'finding-not-deposited', 'finding-pco2-factor-10', 'finding-prey-capture-chronic-missing', 'finding-rmr-count', 'finding-shrimp-duplicate-column', 'finding-zone-extra-acute-squid']
['claim:methods-body-size', 'claim:sfig4a-amplitude-attenuation', 'claim:stable3-acute-shallower', 'claim:stable5-seawater-chemistry']
```

**Agent**

Now the README, then lock and run.

**Agent calls Bash**

```bash
cat > entries/allen-2026/README.md <<'EOF'
# Allen, Yan, Kuan et al. (2026) from Dryad rjdfn2zqz

Tests the findings of [Allen et al. (2026)](https://doi.org/10.1038/s42003-025-09506-6) on
[Dryad rjdfn2zqz](https://doi.org/10.5061/dryad.rjdfn2zqz), version id 439366. The dataset holds
per-squid values for metabolism, ammonia excretion, hemolymph acid-base state, exploration,
predation and critical flicker fusion, group means of the ERG response ratio, and the authors' RSEM
count matrix and R workspace with their DESeq2, sva and GSEA results for the optic lobes.

| Claim | Outcome |
|---|---|
| Metabolic rate, ammonia excretion, blood pH, PCO2 and bicarbonate (Fig. 1B to 1F) | Reproduced |
| Distance, velocity, time in upper, left and front zones (Fig. 2C to 2F, Supplementary Fig. 2) | Reproduced |
| Attack willingness, logistic regression (Fig. 2G) | Not reproduced |
| Hunt duration and strike attempts (Fig. 2H, 2I); prey shrimp velocity (Supplementary Fig. 3) | Reproduced |
| ERG ratio declines above 40 Hz (Fig. 3C) | Not reproduced |
| CFF unchanged, CFF variance (Fig. 3D) | Reproduced |
| Assembly statistics, sample distances, GSEA families, nAChR subunits | Reproduced |
| PCA (Fig. 4A), shared down-regulated sets (Fig. 4B), chronic up-regulated counts (Fig. 4F to 4H) | Partially reproduced |
| No change in acid-base or ion regulatory transcripts | Not reproduced |
| Body size, seawater chemistry, mean depth, ERG amplitude | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/allen-2026-01.yaml`](../../attempts/allen-2026-01.yaml). It reports, among other
things, that the deposited count matrix has lost a column and is mislabelled when read as the
authors' script reads it, that the prey shrimp table repeats the control column for the CO2 group,
and that the prey capture file lacks 11 chronic-OA squid.

- `reproduce_allen_2026.ipynb`: the analysis. It takes about a minute and about 4 GB of memory,
  most of it reading the R workspace.
- `squidoa.py`: reading the staged files, a streaming reader for R's serialization format that
  builds only the workspace objects asked for, and the tests the paper names (Welch's ANOVA,
  Dunnett's T3, one-way ANOVA with Tukey's test, DESeq2's PCA, limma's removeBatchEffect).
EOF
cd  && date -u && python tools/entry.py lock entries/allen-2026 2>&1 | tail -3 && python tools/entry.py all entries/allen-2026 2>&1 | tail -15
```

```
Wed Nov 25 20:41:41 UTC 2026
wrote allen-2026/requirements.lock.txt (Python 3.13, with hashes)
error: attempts/allen-2026-01.yaml: claim 'rnaseq-assembly' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'fig4a-pca' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'sfig5b-acute-clusters-with-control' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'fig4b-shared-down-sets' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'fig4c-acute-ridge' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'fig4d-acute-tree' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'fig4e-chronic-synaptic-down' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'fig4fgh-chronic-up' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'chronic-nachr-subunits-down' was tested on data in another archive; list them under `inputs`
error: attempts/allen-2026-01.yaml: claim 'optic-lobe-no-ion-regulation' was tested on data in another archive; list them under `inputs`
10 error(s)
```

**Agent calls Bash**

```bash
grep -n "was tested on data in another archive" -B25 tools/entry.py | head -60
```

```
406-                report.error(where, f"`findings_review` rates finding {number}, which the attempt rated itself")
407-            seen.add(number)
408-        # A verification round's review of a finding points at the finding by its number in the record.
409-        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
410-            for item in rnd.get("findings") or []:
411-                if item["finding"] > len(attempt.get("findings") or []):
412-                    report.error(where, f"verification round {r} reviews finding {item['finding']}, and the record "
413-                                        f"has {len(attempt.get('findings') or [])} findings")
414-        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
415-        # does not bind: the revision after it may change outcomes, and round 2 reviews them.
416-        agreed = {}
417-        for rnd in (attempt.get("verifications") or [])[1:]:
418-            for r in rnd["results"]:
419-                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
420-        kinds = lookup(kinds_by_target, attempt) or {}
421-        for outcome in attempt.get("outcomes", []):
422-            # A claim on data in another archive names where they are, so it is never blocked for missing data,
423-            # and when it is tested the archive is an input. Only the latest attempt is held to this: the
424-            # claims file is shared, and an earlier attempt may predate the claim's `elsewhere`.
425-            if kinds.get(outcome.get("claim")) == "elsewhere" and path == mine[-1]:
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 20 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=GLBY00000000&retmode=json" | head -c 600; echo; curl -s -m 20 "https://www.ncbi.nlm.nih.gov/Traces/wgs/GLBY01?display=metadata" -o /dev/null -w "%{http_code}\n"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=3140589440&retmode=json" | python -m json.tool | head -60; curl -s -m 30 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=3140589440&rettype=gb&retmode=text" | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=GLBY00000000.1&retmode=json" | python -c "import json,sys; d=json.load(sys.stdin)['result']; u=d['uids'][0]; print(d[u]['accessionversion'], d[u]['slen'], d[u]['title'])"
. $TMPDIR/rv/bin/activate && python - <<'EOF'
g='/tmp/claude-1001/gen/nb3.py'; s=open(g).read()
s=s.replace('''res_n = {k: len(sq.s4_dataframe(v)) for k, v in zip(ws["resNormal"].names(), ws["resNormal"].value)}''','''tsa = sq.tsa_summary()
print(f"NCBI TSA {tsa['accessionversion']} ({tsa['title']}): {tsa['slen']:,} sequences, against {n_rows:,} transcripts in the count matrix "
      f"({100 * (tsa['slen'] / n_rows - 1):.1f}%)")
res_n = {k: len(sq.s4_dataframe(v)) for k, v in zip(ws["resNormal"].names(), ws["resNormal"].value)}''')
s=s.replace('''reading (b), the 12 samples of the three groups alone, and the file's own 14 optic lobe columns
are variants. Mapping rates are not deposited.''','''reading (b), the 12 samples of the three groups alone, and the file's own 14 optic lobe columns
are variants. Mapping rates are not deposited. The number of sequences of the public assembly, NCBI
TSA GLBY00000000.1 (the claims file's `where`), is read from its master record as a variant of the
transcript count.''')
s=s.replace('''the row count of the authors' DESeq2 results. The deposited count file cannot give this number by''','''the row count of the authors' DESeq2 results. The public TSA assembly holds 870,834 sequences, 3.5%
fewer than the count matrix and within the 10% tolerance. The deposited count file cannot give this number by''')
open(g,'w').write(s)
p='entries/allen-2026/squidoa.py'; s=open(p).read()
s=s.replace('''# --- R serialization ----''','''TSA_ACCESSION = "GLBY00000000.1"   # the paper's assembled transcriptome (Data availability), NCBI TSA


def tsa_summary() -> dict:
    """NCBI's summary of the TSA master record (E-utilities esummary): its version, title and number
    of sequences (`slen` of a master record)."""
    import json
    import urllib.request
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&retmode=json&id="
           + TSA_ACCESSION)
    with urllib.request.urlopen(url, timeout=60) as r:
        d = json.load(r)["result"]
    rec = d[d["uids"][0]]
    if rec["accessionversion"] != TSA_ACCESSION:
        raise ValueError(f"NCBI returned {rec['accessionversion']}, not {TSA_ACCESSION}")
    return {k: rec[k] for k in ("accessionversion", "title", "slen", "updatedate")}


# --- R serialization ----''')
open(p,'w').write(s)
EOF
cd  && python - <<'EOF'
s=open('/tmp/claude-1001/gen/attempt.py').read()
s=s.replace('''del rec["inputs"]''','''rec["inputs"] = [{"what": "Number of sequences of the paper's assembled transcriptome, from the NCBI TSA master record (E-utilities esummary), for the transcript count of rnaseq-assembly. The other transcriptomic claims were tested on the count matrix and R workspace in the dataset, which the authors derived from the same reads (SRA BioProject PRJNA1204452), not on the reads.", "source": "NCBI TSA GLBY00000000.1 (GLBY01000000), https://www.ncbi.nlm.nih.gov/nuccore/GLBY00000000.1"}]
rec = {k: rec[k] for k in ["schema_version", "id", "datasets", "paper", "date", "entry", "provenance", "inputs", "outcomes", "findings"]}''')
s=s.replace('''"Transcripts 902,413 (rows of the count matrix and of the workspace's rawMatrix);''','''"Transcripts 902,413 (rows of the count matrix and of the workspace's rawMatrix); the public TSA assembly GLBY00000000.1 holds 870,834 sequences (3.5% fewer, within tolerance either way);''')
s=s.replace('''"Assembly statistics read from the deposited ExN50.stats (Trinity's output), as the assembly FASTA is not in the dataset; the TSA record was not used."''','''"Assembly statistics read from the deposited ExN50.stats (Trinity's output), as the assembly FASTA is not in the dataset; of the TSA record only its sequence count is used."''')
open('/tmp/claude-1001/gen/attempt.py','w').write(s)
EOF
python $TMPDIR/gen/attempt.py && cd entries/allen-2026 && python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python $TMPDIR/gen/attempt.py && cd entries/allen-2026 && $TMPDIR/rv/bin/python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb && cd ../.. && python tools/entry.py lock entries/allen-2026 2>&1 | tail -1 && python tools/entry.py all entries/allen-2026 2>&1 | tail -15; date -u
```

```
written
92 cells
wrote allen-2026/requirements.lock.txt (Python 3.13, with hashes)
Installed kernelspec registry-allen-2026 in executed/allen-2026/.venv/share/jupyter/kernels/registry-allen-2026
0 error(s)
pass  reproduce_allen_2026.ipynb  (65 s)
Wed Nov 25 20:43:42 UTC 2026
```

**Agent**

Entry checks pass and the notebook runs clean in 65 s. Now reading the executed copy against every conclusion.

**Agent calls Bash**

```bash
ls executed/allen-2026/; $TMPDIR/rv/bin/python - <<'EOF' | sed 's/\x1b\[[0-9;]*m//g' > $TMPDIR/exec.txt; wc -l $TMPDIR/exec.txt
import nbformat
nb = nbformat.read('executed/allen-2026/reproduce_allen_2026.ipynb', as_version=4)
for i, c in enumerate(nb.cells):
    if c.cell_type == "markdown":
        if c.source.startswith("**Result") or "Result:" in c.source: print(f"=== MD {i}\n{c.source}\n")
        continue
    print(f"##### cell {i} {c.metadata.get('tags', [])}")
    for o in c.get("outputs", []):
        if o.output_type == "stream": print(o.text[:5000])
        elif o.output_type == "error": print("ERROR", o.ename, o.evalue)
EOF
grep -n "ERROR\|TSA\|Warning" $TMPDIR/exec.txt | head
```

```
reproduce_allen_2026.ipynb
result.json
847 /tmp/claude-1001/exec.txt
437:executed/allen-2026/.venv/lib/python3.13/site-packages/pandas/core/internals/blocks.py:1651: RuntimeWarning: invalid value encountered in multiply
571:NCBI TSA GLBY00000000.1 (TSA: Sepioteuthis lessoniana, transcriptome shotgun assembly): 870,834 sequences, against 902,413 transcripts in the count matrix (-3.5%)
578:the row count of the authors' DESeq2 results. The public TSA assembly holds 870,834 sequences, 3.5%
819:executed/allen-2026/.venv/lib/python3.13/site-packages/pandas/core/internals/blocks.py:1651: RuntimeWarning: invalid value encountered in multiply
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/exec.txt",
 "offset": 160,
 "limit": 300
}
```

```
160	Acute-OA    9.0  2.857  1.459  0.486
161	Chronic-OA  7.0  1.611  0.468  0.177
162	
163	ANOVA on log10: F(2,18) = 6.382, p = 0.008038; SS treatment 0.3563, residual 0.5025; eta^2 = 0.415
164	Paper: F(2,18) = 6.382, p = 0.008038; SS 0.3563 and 0.5025
165	Tukey adjusted p (log10): {'Control vs Acute-OA': np.float64(0.524), 'Control vs Chronic-OA': np.float64(0.0092), 'Acute-OA vs Chronic-OA': np.float64(0.0383)}
166	
167	Variant, untransformed: F = 4.486, p = 0.0263; Tukey {'Control vs Acute-OA': np.float64(0.6979), 'Control vs Chronic-OA': np.float64(0.0317), 'Acute-OA vs Chronic-OA': np.float64(0.0778)}
168	Reduction of chronic-OA against control 51.8%, against acute-OA 43.6%
169	
170	=== MD 16
171	**Result: reproduced.** Means 3.34, 2.86 and 1.61 µmol g-1 h-1, reductions of 51.8% and 43.6%. The
172	ANOVA on log rates gives F(2,18) = 6.382, p = 0.008038, the paper's values; Tukey separates chronic-OA
173	from control (p = 0.009) and acute-OA (p = 0.038), not control from acute-OA (p = 0.52).
174	
175	##### cell 18 ['claim:fig1d-blood-ph', 'claim:fig1e-blood-pco2', 'claim:fig1f-blood-bicarbonate']
176	--- Hemolymph pH
177	              n   mean     sd    sem
178	Control     7.0  7.092  0.020  0.008
179	Acute-OA    6.0  7.145  0.088  0.036
[... 280 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/exec.txt",
 "offset": 460,
 "limit": 390
}
```

```
460	C(pH):C(time)  0.0063   1.0  0.0393  0.8442
461	Residual       4.9958  31.0     NaN     NaN
462	
463	Variant, 0-10 min only (the 10-20 min CO2 column is a copy): control 0.224 (n 8) against CO2 0.170 (n 11); Welch t p = 0.646, Mann-Whitney p = 0.442
464	
465	=== MD 45
466	**Result: reproduced.** On the table as deposited no term has p < 0.05 (two-way ANOVA: pH p =
467	0.84, time p = 0.11, interaction p = 0.84, type III; type II the same to two decimals). The CO2 10
468	to 20 min column is a copy of the control 10 to 20 min column (8 identical values, where the
469	legend gives 11 CO2 shrimp), so the deposited data cannot show what the CO2 shrimp did at 20 min.
470	At 0 to 10 min alone, control and CO2 shrimp do not differ (Welch t p = 0.65). A
471	repeated-measures variant is not run: no shrimp identifier links the columns, and the CO2 columns
472	hold 11 and 8 values.
473	
474	##### cell 47 ['claim:fig3c-ratio-declines']
475	Group      Control  Acute-OA  Chronic-OA
476	Frequency                               
477	10.0         0.977     0.977       0.977
478	20.0         0.977     0.977       0.996
479	30.0         1.042     1.042         NaN
[... 369 more lines not kept]
```

**Agent**

Conclusions match the outputs apart from two small slips (velocity means rounded, and the number of synaptic sets in the nAChR note). Fixing and re-running.

**Agent calls Bash**

```bash
sed -i 's/\*\*Result: reproduced.\*\* Means 0.222, 0.207 and 0.246 mantle lengths\/s; the control mean rounds to/**Result: reproduced.** Means 0.2215, 0.2074 and 0.2456 mantle lengths\/s; the control mean rounds to/' $TMPDIR/gen/nb2.py && grep -c "0.2215, 0.2074" $TMPDIR/gen/nb2.py && sed -i 's/core enrichment genes of the 7 chronic-OA down-regulated synaptic sets (59 genes)/core enrichment genes of the 10 chronic-OA down-regulated synaptic sets (59 genes)/' $TMPDIR/gen/attempt.py && grep -c "10 chronic-OA down-regulated synaptic" $TMPDIR/gen/attempt.py && python $TMPDIR/gen/attempt.py && (cd entries/allen-2026 && $TMPDIR/rv/bin/python $TMPDIR/gen/build.py reproduce_allen_2026.ipynb) && python tools/entry.py all entries/allen-2026 2>&1 | tail -3 && python tools/entry.py handover entries/allen-2026 2>&1 | tail -5; date -u
```

```
1
1
written
92 cells
Installed kernelspec registry-allen-2026 in executed/allen-2026/.venv/share/jupyter/kernels/registry-allen-2026
0 error(s)
pass  reproduce_allen_2026.ipynb  (63 s)
wrote executed/allen-2026/handover
Wed Nov 25 20:45:34 UTC 2026
```

**Agent calls Bash**

```bash
git status --short; grep -n -i "—\|\brather\b" entries/allen-2026/* attempts/allen-2026-01.yaml questions/allen-2026.yaml 2>/dev/null | head; ls executed/allen-2026/handover
```

```
M tools/build_site.py
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
?? attempts/allen-2026-01.yaml
?? entries/allen-2026/
?? questions/allen-2026.yaml
?? scripts
allen-2026.yaml
reproduce_allen_2026.ipynb
squidoa.py
```

**Agent**

The attempt is recorded, the entry's checks pass (0 errors), the notebook runs clean in 63 s with a 3.9 GB peak, and the verifier's handover is built in `executed/allen-2026/handover/`. Nothing is committed.

## 1. Outcomes (31 claims)

| Claim | Outcome |
|---|---|
| fig1b-metabolic-rate | reproduced |
| fig1c-ammonia-excretion | reproduced (the paper's F and p exactly) |
| fig1d-blood-ph, fig1e-blood-pco2, fig1f-blood-bicarbonate | reproduced |
| methods-body-size, stable5-seawater-chemistry, stable3-acute-shallower, sfig4a-amplitude-attenuation | blocked, data_missing |
| sfig2-distance-unchanged, fig2c-velocity-unchanged | reproduced (the paper's H and p exactly) |
| fig2d-acute-upper-zone, fig2e-left-right-unchanged, fig2f-front-back-unchanged | reproduced |
| fig2g-attack-willingness | not reproduced |
| fig2h-hunt-duration, fig2i-strike-attempts, sfig3-prey-velocity-unchanged | reproduced |
| fig3c-ratio-declines | not reproduced |
| fig3d-cff-unchanged, fig3d-cff-variance | reproduced |
| rnaseq-assembly | reproduced (mapping rate not in the dataset, so not tested) |
| fig4a-pca | partially reproduced, rests on an assumption |
| sfig5b-acute-clusters-with-control | reproduced |
| fig4b-shared-down-sets, fig4fgh-chronic-up | partially reproduced |
| fig4c, fig4d, fig4e, chronic-nachr-subunits-down | reproduced |
| optic-lobe-no-ion-regulation | not reproduced |

**Why the three not-reproduced claims failed:**
- **fig2g:** the per-squid file lacks 11 chronic-OA squid. The workspace's own Figure 2G table has 22, and with those counts the paper's model comes out exactly.
- **fig3c:** the ratio stays near 1 up to about 50 Hz, so "below the 20 Hz value at every frequency above 40 Hz" fails in all groups.
- **optic-lobe-no-ion-regulation:** three ion-transport terms are significant under chronic-OA.

## 2. Dataset, assumptions and questions

**What the dataset holds.** One version is public (439366). It has per-squid CSVs and `squid.zip`, which holds the authors' scripts, the ExN50 statistics, the RSEM count matrix and their R workspace (1.1 GB). The workspace contains the DESeq2, sva and GSEA results and the per-figure tables. I wrote a streaming reader for R's file format in `squidoa.py`, because the general `rdata` package needed 12 GB and 5 minutes. The RNA-seq claims were therefore tested on the authors' own objects; the only outside input is the TSA record's sequence count.

**Findings about the data:**
- **Critical:** the count matrix header names 16 samples but each row has 15 values. The values are the gill sample plus 14 optic lobe samples; `Re_8.1_OL-3` is missing. Read the way the authors' script reads it, every sample name shifts by one.
- **Critical:** in the workspace's shrimp-velocity table, the CO2 10 to 20 min column is an exact copy of the control column.
- **Major:** the prey capture file is missing 11 chronic-OA squid.
- **Major:** the deposited hemolymph PCO2 values are one tenth of what the formula printed beside them in `Carbonate_calibration.csv` gives. The files don't show which of the two is wrong.
- **Major:** the 3-D tracks, ERG recordings, seawater chemistry, mass and mantle length are not deposited, although the paper's Data availability says they are.
- **Minor:** the zone file has a 9th acute-OA squid the paper left out, unmarked. Leaving out that one row gives the paper's sums of squares exactly.
- **Minor:** the metabolic rate file has 26 squid against the paper's 29.
- **Minor:** no squid identifiers, and the README gives the PCO2 unit as "atm".

**Paper-side findings:** the sign of the logistic regression intercept in Supplementary Table 4 is wrong, and the PCA chunk of the deposited script disagrees with the figure.

**Assumption:** for fig4a, the control "spread" is read as the range of the control samples. Under the SD reading the claim would be reproduced. This is recorded as a `methods_unavailable` question for the paper's authors.

**Questions to a reader** (`questions/allen-2026.yaml`):
- fig4b: the "36" is the sets significant in both treatments. The paper calls it "the intersect GSEA ridgeplot" and the script plots exactly 36. Neither of the criterion's readings matches.
- fig4fgh: the paper's counts (82, 314, 128) match the script's subset (up in chronic-OA and not down in acute-OA), not all up-regulated sets (101, 321, 133).

## 3. Protocol issues

1. Claims marked `data: elsewhere` (SRA/TSA) whose processed data are actually in the dataset have no category. `entry.py check` requires `inputs` for them. I tested them on the dataset's objects and added the TSA sequence count as a real input, noted in the record.
2. The protocol does not say how to judge a criterion that lists readings when the paper's own code settles a different one (fig4b). The claims header permits taking open details from the deposit's scripts, but the protocol says to test as written. I tested as written, showed the code's reading as a variant, and asked a reader.
3. "Measured" has no way to mark an expected value that cannot be measured (the mapping rate). I left `measured` out for rnaseq-assembly and gave the values in the notes.
4. The protocol does not cover tests with no SciPy equivalent (GraphPad's Welch W and Dunnett's T3). I implemented them; Welch W and the T3 intervals differ from Supplementary Table 2 without changing any conclusion. This is recorded as a deviation.
5. The rating guide doesn't fit a duplicated column that anyone comparing columns can see but that silently corrupts an analysis. I rated it critical, citing the "deposited as two" example. The verifier should review that rating.

## 4. Runtime and failures

The run took about 40 minutes (20:07 to 20:46 UTC). The notebook runs in about 63 s. During development the general `rdata` parse took 5 minutes and 12 GB, which is why I replaced it. A first read of the count matrix failed on its header mismatch, which is how the critical finding above was found. Nothing failed in the final run.

## End of run

70 turns, 32 minutes, $7.72 at API prices, result: success.
