# lee-2023 · author · run 44273539492

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper entries claims attempts | head -80
```

```
<persisted-output>
Output too large (43.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ac884f2a-1ac6-4c8b-8dff-1a8bebd86e1e/tool-results/beur9kple.txt

Preview (first 2KB):
Wed Nov 18 09:14:31 UTC 2026
# Protocol for an attempt

Version: `pilot-16`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ac884f2a-1ac6-4c8b-8dff-1a8bebd86e1e/tool-results/beur9kple.txt"
}
```

```
1	Wed Nov 18 09:14:31 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-16`. Record this version in the attempt's provenance.
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
[... 806 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; cat claims/lee-2023.yaml; ls entries/lee-2023 attempts/lee-2023* questions/lee-2023* 2>&1; cat papers/datasets/lee-2023.yaml
```

```
<persisted-output>
Output too large (65.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ac884f2a-1ac6-4c8b-8dff-1a8bebd86e1e/tool-results/bcerqw1dt.txt

Preview (first 2KB):
10.1126-science.adf6484.txt
# Claims for Lee, Dalley et al. (2023), Science 382, eadf6484, on dandiset 000636.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read. The author manuscript of the version of record in PubMed Central (PMC12229143,
# NIHMS2006139), as text (paper/10.1126-science.adf6484.txt). It has the structured summary,
# the Results, the Discussion, the Materials and Methods and the legends of Figures 1 to 6. It
# does not have the supplementary materials: the legends of figs. S1 to S9 and Data S1 and S2
# are missing, and no PDF was supplied, so no figure could be read. The bioRxiv preprint
# (doi:10.1101/2022.11.08.515739, paper/10.1101-2022.11.08.515739.txt) was read as well. Its
# Results and legends of Supplementary Figures 1 to 5 (an earlier numbering) give some test
# names that the version of record moves to its supplement; where a quote or a method is taken
# from the preprint the claim says so. The preprint has no human versus mouse section. Claims
# that cite figs. S1 to S9 of the version of record rest on the main text sentence that cites
# them, and the features shown in Figure 2H and fig. S8B are not named in any text read.
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ac884f2a-1ac6-4c8b-8dff-1a8bebd86e1e/tool-results/bcerqw1dt.txt"
}
```

```
1	10.1126-science.adf6484.txt
2	# Claims for Lee, Dalley et al. (2023), Science 382, eadf6484, on dandiset 000636.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read. The author manuscript of the version of record in PubMed Central (PMC12229143,
7	# NIHMS2006139), as text (paper/10.1126-science.adf6484.txt). It has the structured summary,
8	# the Results, the Discussion, the Materials and Methods and the legends of Figures 1 to 6. It
9	# does not have the supplementary materials: the legends of figs. S1 to S9 and Data S1 and S2
10	# are missing, and no PDF was supplied, so no figure could be read. The bioRxiv preprint
11	# (doi:10.1101/2022.11.08.515739, paper/10.1101-2022.11.08.515739.txt) was read as well. Its
12	# Results and legends of Supplementary Figures 1 to 5 (an earlier numbering) give some test
13	# names that the version of record moves to its supplement; where a quote or a method is taken
14	# from the preprint the claim says so. The preprint has no human versus mouse section. Claims
15	# that cite figs. S1 to S9 of the version of record rest on the main text sentence that cites
16	# them, and the features shown in Figure 2H and fig. S8B are not named in any text read.
17	#
18	# Code read. github.com/AllenInstitute/human_patchseq_gaba at commit 5eb357a (2023-11-28),
19	# linked under Data and materials availability. It holds one R notebook
20	# (scripts_gene_expression/acute_vs_culture_comparisons_update.Rmd; gene-expression analyses,
[... 738 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ac884f2a-1ac6-4c8b-8dff-1a8bebd86e1e/tool-results/bcerqw1dt.txt",
 "offset": 759
}
```

```
759	  statistics:
760	  - test: FDR-corrected Mann-Whitney test
761	    p: 0.0001
762	    p_relation: "<"
763	    corrected: FDR
764	  data: with_inputs
765	  depends_on:
766	  - cell-metadata-link
767	  criterion: Human Pvalb 2 is PVALB WFDC2 and L4-6 PVALB SULF1, human Sst 5 is SST CALB1
768	    (M_H_Hodge_cross_species_types in the metadata as a check); mouse Pvalb 2 is Pvalb Calb1 Sst,
769	    Pvalb Reln Itm2a, Pvalb Reln Tac1 and Pvalb Sema3e Kank4, mouse Sst 5 is Sst Calb2 Necab1,
770	    Sst Calb2 Pdlim5, Sst Mme Fam114a1, Sst Tac1 Htr1d and Sst Tac1 Tacr3 (ref. 16). The Results
771	    restrict to supragranular neurons; read as (a) somas in L2 or L3 in human and L2/3 in mouse
772	    and (b) all layers, the layer of mouse cells as ref. 16 gives it. Human acute and culture
773	    cells are pooled, as the main analysis does (fig. S9 separates them). Two-sided Mann-Whitney
774	    human against mouse, FDR-corrected across the features tested. Reproduced when sag,
775	    rheobase_i and AP width (width_rheo; width_short_square as a second reading) each differ at
776	    FDR p < 0.0001 in both types, under every reading; the directions are reported, as the
777	    Results do not state them.
778	- id: figs8b-firing-differs-pvalb2-only
[... 182 more lines not kept]
```

**Agent**

Read the protocol and the claims file (about 42 claims). Next: the repo docs, the example entry, and the dataset.

**Agent calls Bash**

```bash
cat README.md | head -80; echo ----; grep -n "" docs/archives.md | sed -n '1,200p' | head -150
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
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150
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
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/fouke-2025-01.yaml | grep -n -A3 "^[a-z_]*:" | head -80; ls schemas; ls questions | head -3; cat entries/fouke-2025/README.md | head -30
```

```
95:findings:
96-- kind: data_missing
97-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
98-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
--
165:verifications:
166-- date: '2026-10-14'
167-  kind: agent
168-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
README.md
asari-2009.yaml
ashworth-2025.yaml
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 240,330p attempts/fouke-2025-01.yaml; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"
```

```
outcome: blocked
  blocked_by: data_missing
  notes: Needs the imaging, the tail tracking and the registration to the mapzebrain atlas, none
    of which is in the dandiset.
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
[... 362 more lines not kept]
```

**Agent**

Now the dataset itself.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000636/versions/ | python3 -m json.tool | head -60; curl -s https://api.dandiarchive.org/api/dandisets/000636/ | python3 -m json.tool | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000636/versions/0.241120.0510/ | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d.get('description'));print(d.get('relatedResource'));print(d.get('assetsSummary'))"; curl -s "https://api.dandiarchive.org/api/dandisets/000636/versions/0.241120.0510/assets/?page_size=1000" > assets.json; python3 -c "
import json;d=json.load(open('assets.json'));r=d['results'];print(d['count'],len(r));
import collections
for a in r[:10]: print(a['path'],a['size'])
print(collections.Counter(a['path'].split('/')[0] for a in r).most_common(5), len(set(a['path'].split('/')[0] for a in r)))
s=sorted(a['size'] for a in r);print(s[0],s[len(s)//2],s[-1])"; grep -n -i "000636\|dandi" paper/*.txt | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
tail -c 3000 /home/runner/.claude/projects/-home-runner-work-encore-encore/ac884f2a-1ac6-4c8b-8dff-1a8bebd86e1e/tool-results/bvanohczi.txt; ls -la paper
```

```
ures by morphology type (Kruskal-Wallis ANOVA on ranks; P < 0.05, FDR corrected. Post-hoc Dunn’s test; * P < 0.05, ** P < 0.01, FDR corrected). ( D ) UMAP of all SST CALB1 neurons based on 253 genes differentially expressed between 10 DBC, MC, and sparse SST neurons. Neurons cluster into three main groups corresponding to morphology types (colored markers). Neurons with unknown morphologies are represented by gray markers. Fig. 5. Transcriptomic-type identity, spatial distribution, and multimodal properties of human DBCs. ( A ) Putative DBC morphologies mapped to transcriptomic type SST CALB1 or SST ADGRG6 and shown aligned to an average cortical template. Histograms to the right of the morphologies display average dendrite (darker color) and axon (lighter color) branch length by cortical depth (shading shows +/− 1 SD about mean; soma locations represented by black circles). (Bottom) Accompanying each reconstruction is the voltage response to a 1 s–long current step to a −90 pA and rheobase +80 pA for each respective DBC. ( B ) Spatial distribution for SST CALB1 and SST ADGRG6 revealed by MERFISH. ( C ) Four specific electrophysiology features shown as box or scatter plots for the SST CALB1 and SST ADGRG6 t-types with putative DBCs highlighted in green. ( D ) UMAP representation of transcriptomics (isolated to the SST subclass), electrophysiology, and morphology. SST CALB1 and SST ADGRG6 t-types are colored orange and brown, respectively, and qualitatively defined putative DBCs are highlighted in green. ( E ) 63× MIP inset corresponding to Fig. 4A showing axon horse-tail bundles and boutons. Fig. 6. Species differences in morphoelectric properties for homologous types Pvalb 2 and Sst 5. ( A ) Human and mouse representative morphologies, aligned to average cortical templates, from homologous types Pvalb 2 and Sst 5 with each t-type represented by different colors. ( B ) Box plots of select morphological features from humans (pink) and mice (gray) (FDR-corrected Mann-
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -o -n -i "dandi[^.]*\.\|github[^ ]*\|Data and materials availability[^.]*\.[^.]*\.[^.]*\." 10.1126-science.adf6484.txt | head; python3 - <<'E'
t=open('10.1126-science.adf6484.txt').read()
import re
for k in ['Electrophysiology','IPFX','sag','rheobase','Statistical analysis','Kruskal','Mann','84','UMAP','Days in culture','supragranular','Gouwens','Pvalb 2','depth-matched','depth','junction','Dunn']:
    print(k, [m.start() for m in re.finditer(k,t)][:15])
E
```

```
122244 10.1126-science.adf6484.txt
7:github.com/AllenInstitute/mfishtools
7:github.com/AllenInstitute/
7:github.com/AllenInstitute/skeleton_keys
7:Data and materials availability: All data from the study will be made available through BIL, DANDI, and NeMO repositories. Morphology reconstructions are available at the Brain Image Library (BIL) at https://doi.org/10.
7:github.com/AllenInstitute/human_patchseq_gaba
7:github.com/AllenInstitute/patchseqtools
7:github.com/alleninstitute/ipfx
7:github.com/AllenInstitute/neuron_morphology
7:github.com/AllenInstitute/skeleton_keys
7:github.com/AllenInstitute/scrattch/
Electrophysiology [59510, 78281, 116218]
IPFX [80514, 80632]
sag [21354, 26659, 33111, 37120, 40220, 40551, 79148, 79253]
rheobase [40225, 79293, 79304, 79360, 79728, 79769, 109281, 111010, 113463, 114044, 115156, 116827, 116840]
Statistical analysis [81981]
Kruskal [82412, 111117, 111654, 112697, 113012, 114184]
Mann [680, 82118, 82699, 108555, 108934, 109495, 110278, 116154, 117129]
84 [26, 458, 5689, 5698, 21137, 21585, 28710, 56751, 65694, 91598, 91815, 93691, 93871, 94056, 94418]
UMAP [19369, 20497, 20949, 21630, 22720, 23074, 23152, 23176, 28479, 28763, 36781, 37267, 40016, 85547, 85633]
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1126-science.adf6484.txt').read()
print(t[17000:42000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1126-science.adf6484.txt').read()
print(t[59400:62500]); print('.....'); print(t[77500:86000])"
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper read. Now checking network access to the paper's code repo and opening one NWB file.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/AllenInstitute/human_patchseq_gaba/commits/5eb357a; curl -s https://api.github.com/repos/AllenInstitute/human_patchseq_gaba/commits/5eb357a | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('sha'),d.get('commit',{}).get('committer'))"; which uv python3; python3 -c "import pynwb,h5py,remfile,ipfx" 2>&1
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -n "python" tools/entry.py | head -30; ls entries | head -3; grep -l ipfx entries/*/requirements.in
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
429:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
432:def python_of(entry_dir: Path) -> str:
433:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
436:    if entry.get("python"):
437:        return str(entry["python"])
446:def set_python(entry_dir: Path, version: str) -> None:
447:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
450:    line = f'python: "{version}"'
451:    if re.search(r"^python:.*$", text, re.M):
452:        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
462:    version = version or python_of(entry_dir)
463:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 425,470p tools/entry.py; cat entries/berg-2020/requirements.in entries/chartrand-2023/requirements.in; grep python: entries/berg-2020/entry.yaml entries/chartrand-2023/entry.yaml entries/fouke-2025/entry.yaml
```

```
# --- lock and run -------------------------------------------------------------

LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")


def python_of(entry_dir: Path) -> str:
    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
    (entries from before the field), else the registry's default for new entries, PYTHON_VERSION."""
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text()) or {}
    if entry.get("python"):
        return str(entry["python"])
    lock_file = entry_dir / "requirements.lock.txt"
    if lock_file.is_file():
        m = LOCK_VERSION.search(lock_file.read_text()[:2000])
        if m:
            return m.group(1)
    return PYTHON_VERSION


def set_python(entry_dir: Path, version: str) -> None:
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^PYTHON_VERSION" tools/entry.py; head -5 entries/chartrand-2023/requirements.lock.txt; grep -n "^ipfx\|^numpy\|^pandas\|^pynwb\|^hdmf\|^h5py\|^scipy" entries/chartrand-2023/requirements.lock.txt; grep -rn "ipfx" entries/chartrand-2023/*.py | head
```

```
63:PYTHON_VERSION = "3.13"
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
argschema==3.0.4
    # via ipfx
asn1crypto==1.5.1
27:h5py==3.16.0
33:hdmf==4.2.0
41:ipfx==2.1.2
70:numpy==2.5.4
96:pandas==3.1.0
122:pynwb==3.1.2
157:scipy==1.18.1
187:    from ipfx.stimulus import StimulusOntology
188:    import ipfx.json_utilities as ju
255:    from ipfx.sweep import Sweep
256:    import ipfx.qc_feature_extractor as qcfe
270:        import ipfx.stim_features as stf
322:def _patch_ipfx():
329:    import ipfx.stimulus_protocol_analysis as spa
[... 3 more lines not kept]
```

**Agent**

Setting up a working environment.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 dev && uv pip install -q --python dev/bin/python pynwb remfile h5py ipfx numpy pandas scipy statsmodels scikit-posthocs scikit-learn umap-learn requests matplotlib ipykernel nbconvert nbformat 2>&1 | tail -5; dev/bin/python -c "import ipfx, pynwb, umap; print(ipfx.__version__ if hasattr(ipfx,'__version__') else 'ok', pynwb.__version__)"
```

```
2.1.2 3.1.2
Shell cwd was reset to
```

**Agent**

Now fetching the code repository's tables at commit 5eb357a.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.github.com/repos/AllenInstitute/human_patchseq_gaba/git/trees/5eb357a1cea246c7c847b5608a8fc7e87ea95b58?recursive=1" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for t in d['tree']: print(t['type'],t.get('size'),t['path'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; mkdir -p repo; for f in LeeDalley_ephys_fx.csv LeeDalley_manuscript_metadata_v2.csv LeeDalley_morpho_features.csv dbc_calb1_ADGRG6.csv vgic_genes.csv DataS1_Donor_table.csv README.md acute.culture.locked_sstcalb1.ephys.csv cell_morphology_predictions_CALB1.csv; do curl -sL -o repo/$f https://raw.githubusercontent.com/AllenInstitute/human_patchseq_gaba/5eb357a1cea246c7c847b5608a8fc7e87ea95b58/data/$f; done; ls -la repo; cat repo/README.md; head -3 repo/LeeDalley_manuscript_metadata_v2.csv; head -2 repo/LeeDalley_ephys_fx.csv | cut -c1-3000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; dev/bin/python - <<'E'
import pandas as pd, json
m=pd.read_csv('repo/LeeDalley_manuscript_metadata_v2.csv')
print(m.shape); print(m.dtypes)
print(m.nwb_id.dropna().head(10).tolist(), m.nwb_id.notna().sum())
print(m.Has_ephys.value_counts(dropna=False))
print(m.condition.value_counts(dropna=False)); print(m.condition2.value_counts(dropna=False))
print(m.Revised_subclass_label.value_counts(dropna=False)); print(m.subclass_label.value_counts(dropna=False))
print(m['Transcriptomic_type '].nunique())
f=pd.read_csv('repo/LeeDalley_ephys_fx.csv'); print(f.shape, f.specimen_id.isin(m.specimen_id_x).sum())
a=json.load(open('assets.json'))['results']
paths=[x['path'] for x in a]
ses=[p.split('ses-')[1].split('_')[0] for p in paths]
print(len(set(ses)), ses[:3])
print('nwb_id sample', m.nwb_id.dropna().astype(str).head().tolist())
s=set(ses); print(sum(str(int(x)) in s for x in m.specimen_id_x), sum(str(x) in s for x in m.nwb_id.dropna()))
E
```

```
(779, 23)
specimen_id_x                      int64
cell_name                            str
Donor                                str
structure                            str
lobe                                 str
disease_category                     str
Transcriptomic_type                  str
M_H_Hodge_cross_species_types        str
condition                            str
condition2                           str
Days_In_culture                    int64
Has_morphology                    object
Has_ephys                         object
Qualitative_morphology_type          str
Cortical_layer                       str
subclass_label                       str
Revised_subclass_label               str
Virus                                str
Genes_Detected                     int64
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; dev/bin/python - <<'E'
import pandas as pd, json
m=pd.read_csv('repo/LeeDalley_manuscript_metadata_v2.csv')
a=json.load(open('assets.json'))['results']
ses=[x['path'].split('ses-')[1].split('_')[0] for x in a]
s=set(ses); print(len(s))
nid=m.nwb_id.dropna().astype('int64').astype(str)
print('nwb_id in dandiset', nid.isin(s).sum(), 'of', len(nid), 'unique', nid.nunique())
e=m[m.Has_ephys==True]; print('has_ephys with nwb', e.nwb_id.notna().sum(), e.nwb_id.dropna().astype('int64').astype(str).isin(s).sum())
print('without ephys but nwb', m[(m.Has_ephys!=True)&m.nwb_id.notna()].shape)
print('files not in table', len(s-set(nid)))
print(m.Virus.value_counts(dropna=False)); print(m.Qualitative_morphology_type.value_counts(dropna=False)); print(m.lobe.value_counts(dropna=False)); print(m.Days_In_culture.value_counts().sort_index())
print(m.Cortical_layer.value_counts(dropna=False)); print(m.Has_morphology.value_counts(dropna=False))
print(pd.read_csv('repo/dbc_calb1_ADGRG6.csv').head(30))
E
```

```
706
nwb_id in dandiset 691 of 735 unique 734
has_ephys with nwb 691 685
without ephys but nwb (44, 23)
files not in table 16
Virus
CN1390     379
NaN        313
CN1827      33
CN2039      30
CN1816      10
CN1817       3
unknown      3
CN1294       2
CN1408       2
CN1366       2
CN1418       1
CN1818       1
Name: count, dtype: int64
Qualitative_morphology_type
[... 77 more lines not kept]
```

**Agent**

Metadata links well: 685 of 705 ephys rows have a matching file. Now opening one NWB file.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > probe.py <<'E'
import json, time, remfile, h5py, pynwb, requests
a=json.load(open('assets.json'))['results']
x=a[2]; print(x['path'], x['size'])
r=requests.get(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/", allow_redirects=False); url=r.headers['location']; print(url[:100])
t=time.time()
f=h5py.File(remfile.File(url),'r'); io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print('open',time.time()-t)
print(nwb.session_description, nwb.identifier, nwb.session_id, nwb.institution, nwb.session_start_time)
print(nwb.subject)
print('icephys_electrodes', list(nwb.icephys_electrodes.keys())); e=list(nwb.icephys_electrodes.values())[0]; print(e)
print('devices',list(nwb.devices.keys()))
print('acq', len(nwb.acquisition), list(nwb.acquisition.keys())[:5]); print('stim',len(nwb.stimulus), list(nwb.stimulus.keys())[:5])
print('proc', {k:list(v.data_interfaces.keys()) for k,v in nwb.processing.items()})
k=list(nwb.acquisition.keys())[0]; s=nwb.acquisition[k]; print(type(s).__name__, s.fields.keys() if hasattr(s,'fields') else '')
for kk,v in s.fields.items():
    if kk!='data': print(' ',kk, v if not hasattr(v,'shape') else v.shape)
print('sweep table', nwb.sweep_table)
print(nwb.intracellular_recordings) 
print('lab_meta', nwb.lab_meta_data)
print('epochs', nwb.epochs)
for k,v in list(nwb.acquisition.items())[:40]: print(k, type(v).__name__, getattr(v,'stimulus_description',None), v.data.shape, getattr(v,'rate',None), getattr(v,'sweep_number',None))
E
dev/bin/python probe.py 2>&1 | head -120
```

```
/tmp/claude-1001/dev/lib/python3.13/site-packages/pynwb/core.py:52: UserWarning: Use of icephys_filtering is deprecated and will be removed in PyNWB 4.0. Use the IntracellularElectrode.filtering field instead
  warn(error_msg)
sub-727391446/sub-727391446_ses-727398050_icephys.nwb 46114943
https://dandiarchive.s3.amazonaws.com/blobs/c3c/782/c3c782db-548a-4166-8a26-cd47bfcc1e99?response-co
open 6.084917306900024
PLACEHOLDER e89b2201e83e4bdd07ee9a62659342cd1dfb8c6b2325a06c23bc1cb4dfbbf007 727398050 Allen Institute for Brain Science 2018-07-31 03:53:12.602000+00:00
subject pynwb.file.Subject at 0x136740297852304
Fields:
  age: P22995.0D
  description: Description of subject and where subject came from (e.g., breeder, if animal).
  sex: F
  species: Homo Sapiens
  subject_id: 727391446

icephys_electrodes ['electrode_0']
electrode_0 pynwb.icephys.IntracellularElectrode at 0x136740305562864
Fields:
  description: Headstage 0
  device: device_ITC18USB_Dev_0 pynwb.device.Device at 0x136740305565552
Fields:
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i 's/^k=list(nwb.acquisition.keys())\[0\]; s=.*$/k=None/; s/^for kk,v in s.fields.items():$/for kk,v in []:/' probe.py; dev/bin/python probe.py 2>&1 | grep -v Warn | sed -n '20,140p'
```

```
description: Harvard Bioscience (formerly HEKA/Instrutech) Model: ITC18USB


devices ['device_ITC18USB_Dev_0']
acq 72 ['data_00000_AD0', 'data_00001_AD0', 'data_00002_AD0', 'data_00003_AD0', 'data_00004_AD0']
stim 72 ['data_00000_DA0', 'data_00001_DA0', 'data_00002_DA0', 'data_00003_DA0', 'data_00004_DA0']
proc {'spikes': ['Sweep_10', 'Sweep_11', 'Sweep_12', 'Sweep_14', 'Sweep_16', 'Sweep_17', 'Sweep_18', 'Sweep_19', 'Sweep_20', 'Sweep_21', 'Sweep_22', 'Sweep_23', 'Sweep_4', 'Sweep_5', 'Sweep_6', 'Sweep_7', 'Sweep_8']}
sweep table sweep_table pynwb.icephys.SweepTable at 0x123915432215280
Fields:
  colnames: ['series' 'sweep_number']
  columns: (
    series_index <class 'hdmf.common.table.VectorIndex'>,
    series <class 'hdmf.common.table.VectorData'>,
    sweep_number <class 'hdmf.common.table.VectorData'>
  )
  description: A sweep table groups different PatchClampSeries together.
  id: id <class 'hdmf.common.table.ElementIdentifiers'>

None
lab_meta {}
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx; for k in ahp_delay_ratio width_suprathresh postap_slope norm_sq sag_area sag_peak_t sag_tau trough_slowdeltav adp_v hero find_hero first_isi_inv fast_trough_v_last sag_depol peak_ratio; do echo "== $k: $(grep -rl "$k" --include=*.py . | tr '\n' ' ')"; done; ls
```

```
== ahp_delay_ratio: 
== width_suprathresh: 
== postap_slope: 
== norm_sq: ./spike_train_features.py 
== sag_area: 
== sag_peak_t: 
== sag_tau: 
== trough_slowdeltav: 
== adp_v: ./feature_extractor.py 
== hero: ./stimulus_protocol_analysis.py ./plot_qc_figures.py ./data_set_features.py ./feature_record.py 
== find_hero: ./stimulus_protocol_analysis.py 
== first_isi_inv: 
== fast_trough_v_last: 
== sag_depol: 
== peak_ratio: 
__init__.py
__pycache__
_schemas.py
_version.py
attach_metadata
[... 39 more lines not kept]
```

**Agent**

IPFX's public package lacks about 15 of the 84 features (the Methods say custom code "will be released in a future version of IPFX"); I'll note that. Now timing the streaming of one cell's sweeps.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > probe2.py <<'E'
import json, time, remfile, h5py, requests, numpy as np, re
a=json.load(open('assets.json'))['results']
x=a[2]
url=requests.get(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/", allow_redirects=False).headers['location']
t=time.time()
f=h5py.File(remfile.File(url),'r')
acq=f['acquisition']; 
k='data_00012_AD0'; d=acq[k]
print(dict(d.attrs).keys())
for kk in d: print(kk, d[kk].shape if hasattr(d[kk],'shape') else '', d[kk].attrs.get('unit',''), d[kk].attrs.get('conversion',''), d[kk].chunks if hasattr(d[kk],'chunks') else '', d[kk].compression if hasattr(d[kk],'compression') else '')
c=d['comments'][()] if 'comments' in d else d.attrs.get('comments')
c=c.decode() if isinstance(c,bytes) else c
for line in c.split('\n'):
    if re.search('Bridge|Holding|Bias|Stim Scale|Wave Name|Amp|Capacitance|Neut|I-Clamp',line): print(line)
s=f['stimulus/presentation/data_00012_DA0']; print([ (kk, s[kk].attrs.get('unit',''), s[kk].attrs.get('conversion','')) for kk in s])
t=time.time(); v=d['data'][:]; i=s['data'][:]; print('read', time.time()-t, v.dtype, v[:3], i.max(), i.min())
E
dev/bin/python probe2.py 2>&1 | grep -v Warn
```

```
dict_keys(['comments', 'description', 'namespace', 'neurodata_type', 'object_id', 'stimulus_description', 'sweep_number'])
bias_current (1,) pA  None None
bridge_balance (1,) MOhm  None None
capacitance_compensation (1,) pF  None None
data (301000,) volts 0.001 (8192,) gzip
electrode     
gain (1,)   None None
starting_time (1,) Seconds  None None
HS#0:Stim Scale Factor: 0.80 
HS#0:I-Clamp Holding Level: 18.96 pA
[('data', 'amperes', np.float32(1e-12)), ('electrode', '', ''), ('gain', '', ''), ('starting_time', 'Seconds', '')]
read 0.05179882049560547 float32 [-61.375   -61.34375 -61.375  ] 80.0 0.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > survey.py <<'E'
import json, time, remfile, h5py, requests, collections, random, sys
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))['results']
random.seed(0); pick=random.sample(a,20)
def one(x):
    url=requests.get(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/", allow_redirects=False).headers['location']
    f=h5py.File(remfile.File(url),'r'); out=[]
    for k,d in f['acquisition'].items():
        out.append((d.attrs['neurodata_type'], d.attrs.get('stimulus_description'), d['data'].shape[0]))
    sid=f['general/subject/subject_id'][()] if 'general/subject/subject_id' in f else None
    return x['path'], out, sid
t=time.time()
c=collections.Counter()
with ThreadPoolExecutor(8) as ex:
    for p,out,sid in ex.map(one,pick):
        for o in out:
            if o[0]=='CurrentClampSeries': c[o[1]]+=1
print(time.time()-t)
for k,v in sorted(c.items()): print(k,v)
E
dev/bin/python survey.py 2>&1 | grep -v Warn
```

```
45.790485858917236
Blip_finder_DA_0 3
C1LSFINEST150112_DA_0 25
C1NSD1SHORT17110_DA_0 2
C1NSD2SHORT17110_DA_0 2
C1RP25PR1S141203_DA_0 4
C1SQCAPCHK141203_DA_0 50
C1SSFINEST150112_DA_0 11
C2CHIRP180503_DA_0 25
C2NSD1SHORT17110_DA_0 7
C2NSD2SHORT17110_DA_0 6
C2SSTRIPLE171103_DA_0 99
Rheo_Supra_backu_DA_0 34
Rheobase_finder_DA_0 4
X1PS_SubThresh_DA_0 152
X2LP_Search_DA_0 115
X3LP_Rheo_DA_0 104
X4PS_SupraThresh_DA_0 74
X5SP_Search_DA_0 212
X6SP_Rheo_DA_0 75
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx/defaults; ls; for k in X1PS X2LP X3LP X4PS X5SP X6SP X7Ramp C1LSFINEST subthreshold_171 Rheobase_finder Rheo_Supra C1SSFINEST C1RP25 C2SSTRIPLE; do echo "$k: $(grep -c "$k" stimulus_ontology.json)"; done; python3 -c "
import json;o=json.load(open('stimulus_ontology.json'))
for e in o:
  names=[t for x in e for t in (x if isinstance(x,list) else [x])]
  s=str(e)
  if any(k in s for k in ['X1PS','X4PS','X2LP','X3LP','X5SP','X6SP','X7Ramp','Rheo_Supra','subthreshold_171','Rheobase_finder']): print(e)
"
```

```
qc_criteria.json
stimulus_ontology.json
X1PS: 1
X2LP: 2
X3LP: 2
X4PS: 1
X5SP: 1
X6SP: 1
X7Ramp: 1
C1LSFINEST: 5
subthreshold_171: 1
Rheobase_finder: 1
Rheo_Supra: 1
C1SSFINEST: 4
C1RP25: 2
C2SSTRIPLE: 6
[['code', 'Rheobase_finder'], ['name', 'Test']]
[['code', 'subthreshold_171'], ['name', 'Long Square']]
[['code', 'X1PS_SubThresh'], ['name', 'Long Square']]
[['code', 'X3LP_Rheo'], ['name', 'Long Square']]
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx; sed -n 1,400p data_set_features.py | grep -n "def \|start\|end=\|SweepSet\|Analysis(" | head -80
```

```
70:def detection_parameters(stimulus_type):
74:def detection_parameters_from_stimulus_name(stimulus_name):
84:def record_errors(fn):
86:    def wrapper(*args, **kwargs):
97:def fallback_on_error(fallback_value=None, catch_errors=(Exception)):
98:    def fallback_on_error_decorator(fn):
100:        def wrapper(*args, **kwargs):
113:def extractors_for_sweeps(sweep_set,
115:                          reject_at_stim_start_interval=0,
120:                          start=None, end=None):
125:    sweep_set : SweepSet object
129:    reject_at_stim_start_interval :
132:    start :
152:        start=start,
153:        end=end,
156:        reject_at_stim_start_interval=reject_at_stim_start_interval)
158:    stfx = SpikeTrainFeatureExtractor(start, end)
165:def extract_sweep_features(data_set, sweep_table):
177:        sweep_set.align_to_start_of_epoch("experiment")
180:        for k in [ "start", "end" ]:
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx; sed -n 60,80p data_set_features.py; sed -n 194,345p data_set_features.py; grep -n "def \|hero\|39\|61" stimulus_protocol_analysis.py | head -60
```

```
SUBTHRESHOLD_LONG_SQUARE_MIN_AMPS = {
    20.0: -100.0,
    40.0: -200.0
    }

TEST_PULSE_DURATION_SEC = 0.4


def detection_parameters(stimulus_type):
    return DETECTION_PARAMETERS[stimulus_type]


def detection_parameters_from_stimulus_name(stimulus_name):
    try:
        stimulus_type = get_stimulus_type(stimulus_name)
        dp = detection_parameters(stimulus_type)
    except ValueError as e:
        logging.warning(f"Warning: {e}\nUsing default detection parameters")
        dp = detection_parameters(None)
def select_subthreshold_min_amplitude(stim_amps, decimals=0):
[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx; grep -n "def get_stim_characteristics" -A40 stim_features.py | head -60; grep -n "DETECTION_PARAMETERS" -A25 data_set_features.py | head -30; grep -n "class Sweep\b\|class Sweep(" -A30 sweep.py | head -40
```

```
5:def get_stim_characteristics(i, t, test_pulse=True):
6-    """
7-    Identify the start time, duration, amplitude, start index, and end index of a general stimulus.
8-    """
9-
10-    di = np.diff(i)
11-    di_idx = np.flatnonzero(di)   # != 0
12-    start_idx_idx = 2 if test_pulse else 0     # skip the first up/down (test pulse) if present
13-
14-    if len(di_idx[start_idx_idx:]) == 0:    # if no stimulus is found
15-        return None, None, 0.0, None, None
16-
17-    start_idx = di_idx[start_idx_idx] + 1   # shift by one to compensate for diff()
18-    end_idx = di_idx[-1]
19-    if start_idx >= end_idx: # sweep has been cut off before stimulus end
20-        return None, None, 0.0, None, None
21-
22-    start_time = float(t[start_idx])
23-    duration = float(t[end_idx] - t[start_idx-1])
24-
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx; grep -n "def \|noise\|1.5\|0.5\|500" qc_feature_extractor.py | head -60; cat defaults/qc_criteria.json
```

```
9:def extract_blowout(data_set, tags):
39:def extract_electrode_0(data_set, tags):
69:def extract_recording_date(data_set, tags):
81:def extract_clamp_seal(data_set, tags, manual_values=None):
120:def extract_input_and_access_resistance(data_set, tags, manual_values=None):
167:def extract_input_resistance(breakin_sweep,tags,manual_values):
188:def extract_initial_access_resistance(breakin_sweep,tags,manual_values):
209:def compute_input_access_resistance_ratio(ir, sr):
220:def cell_qc_features(data_set, manual_values=None):
263:def sweep_qc_features(data_set):
297:def check_sweep_integrity(sweep, is_ramp):
316:def current_clamp_sweep_stim_features(sweep):
340:def current_clamp_sweep_qc_features(sweep, is_ramp):
349:    # measure noise before stimulus
350:    idx0, idx1 = ep.get_first_noise_epoch(expt_start_idx, hz)  # count from the beginning of the experiment
351:    _, qc_features["pre_noise_rms_mv"] = qcf.measure_vm(voltage[idx0:idx1])
362:        idx0, idx1 = ep.get_last_noise_epoch(rec_end_idx, hz)
363:        _, rms_last_noise_epoch = qcf.measure_vm(voltage[idx0:idx1])
365:        rms_last_noise_epoch = None
369:    qc_features["post_noise_rms_mv"] = rms_last_noise_epoch
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx; sed -n 297,400p qc_feature_extractor.py
```

```
def check_sweep_integrity(sweep, is_ramp):

    tags = []

    for k,v in sweep.epochs.items():
        if not v:
            tags.append(F"{k} epoch is missing")

    if not is_ramp:
        if sweep.epochs["recording"] and sweep.epochs["experiment"]:
            if sweep.epochs["recording"][1] < sweep.epochs["experiment"][1]:
                tags.append("Recording stopped before completing the experiment epoch")

    if np.isnan(sweep.i).any():
        tags.append("Stimulus contains NaN values")

    return tags


def current_clamp_sweep_stim_features(sweep):
[... 69 more lines not kept]
```

**Agent**

Writing the helper module with loading, sweep QC and IPFX feature extraction.

**Agent calls Bash**

```bash
date -u; mkdir -p entries/lee-2023
```

```
Wed Nov 18 09:19:18 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev/lib/python3.13/site-packages/ipfx; grep -n "def \|norm_sq" spike_train_features.py | head -30; grep -n "def process\|features\[\"\|features\['\|\"adapt\"\|'adapt'" feature_extractor.py | head -40; sed -n 128,232p stimulus_protocol_analysis.py
```

```
8:def basic_spike_train_features(t, spikes_df, start, end, exclude_clipped=False):
36:def pause(t, spikes_df, start, end, cost_weight=1.0):
68:def burst(t, spikes_df, tol=0.5, pause_cost=1.0):
100:def delay(t, v, spikes_df, start, end):
123:def fit_fi_slope(stim_amps, avg_rates):
138:def get_isis(t, spikes):
147:def adaptation_index(isis):
155:def latency(t, spikes, start):
167:def average_rate(t, spikes, start, end):
193:def norm_diff(a):
210:def norm_sq_diff(a):
216:    norm_sq_diffs = np.square((a[1:] - a[:-1])) / np.square((a[1:] + a[:-1]))
217:    return norm_sq_diffs.mean()
220:def detect_pauses(isis, isi_types, cost_weight=1.0):
280:def detect_bursts(isis, isi_types, fast_tr_v, fast_tr_t, slow_tr_v, slow_tr_t,
402:def _score_burst_set(bursts, isis, delta_t, c_n=0.1, c_tx=0.01):
426:def _burstiness_index(in_burst_isis, out_burst_isis):
87:    def process(self, t, v, i):
264:    def process(self, t, v, i, spikes_df, extra_features=None, exclude_clipped=False):
274:            features['peak_deflect'] = subf.voltage_deflection(t, v, i, self.start, self.end, self.deflect_type)
[... 112 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/lee-2023/lee2023.py",
 "content": "\"\"\"Loading and measures for Lee, Dalley et al. (2023), Science 382, eadf6484, on dandiset 000636.\n\nThe dandiset holds one NWB file per neuron (Allen Institute MIES recordings, current clamp\nat 50 kHz). Cell labels come from the paper's code repository, AllenInstitute/human_patchseq_gaba\nat commit 5eb357a, matched by its `nwb_id` column, which equals the NWB session id.\n\nWhere parameters come from:\n- Sweep inclusion: Methods, \"Electrophysiology\" (patch-clamp recording paragraph): \"the bridge\n  balance was <20 MΩ and <15% of the Rinput; (ii) bias (leak) current 0 ± 100 pA; and (iii) root\n  mean square noise measurements in a short window (1.5 ms ...) and longer window (500 ms ...) were\n  <0.07 and 0.5 mV\". The noise windows are IPFX's own (qc_feature_extractor), which the paper\n  uses (\"Feature extraction was implemented using the IPFX python package\").\n- Features: Methods, \"Electrophysiology feature analysis\", computed with the IPFX package\n  (version in the lock file) through its LongSquareAnalysis, ShortSquareAnalysis and\n  RampAnalysis, with IPFX's defaults (sag at the sweep whose response is closest to -100 mV,\n  hero sweep at rheobase + 39 to 61 pA, input resistance from sweeps between -100 and 0 pA).\n  Column names follow the paper's table LeeDalley_ephys_fx.csv. Features that public IPFX does\n  not compute are left out (Methods: \"custom code used for chirps and some high-level features\n  will be released in a future version of IPFX\"); NOT_COMPUTED lists them.\n- Adaptation ratios: Methods, \"a ratio of the spike features between the first and third spike\n  (on the lowest amplitude stimulus to elicit at least four spikes)\". Read as third over first\n  spike; for the ISI, the second ISI over the first (the ISIs that end at the third and the\n  second spike). These are assumptions, checked against the paper's table in the link claim.\n- adapt_mean/max, isi_cv_mean/max, isi_norm_sq_var_mean/max: mean and maximum over the\n  spiking long square sweeps with at least four spikes, an assumption (the paper does not\n  define them); isi_norm_sq_var is IPFX's norm_sq_diff of the ISIs, an assumption.\n- Statistics helpers follow the claims file: Mann-Whitney (two-sided), Kruskal-Wallis with\n  Dunn's post hoc, Benjamini-Hochberg FDR.\n\"\"\"\nimport io\nimport json\nimport logging\nimport warnings\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET = \"000636\"\nVERSION = \"0.241120.0510\"\nAPI = \"https://api.dandiarchive.org/api\"\nCODE_REPO = \"AllenInstitute/human_patchseq_gaba\"\nCODE_COMMIT = \"5eb357a1cea246c7c847b5608a8fc7e87ea95b58\"\n\n# The 9 chirp columns of LeeDalley_ephys_fx.csv; the other 84 are the paper's 84 features\n# (claims file, header, reading a).\nCHIRP = [\"peak_ratio_chirp\", \"peak_freq_chirp\", \"3db_freq_chirp\", \"peak_impedance_chirp\",\n         \"low_freq_impedance_chirp\", \"sync_freq_chirp\", \"phase_peak_chirp\", \"phase_low_chirp\",\n         \"total_inductive_phase_chirp\"]\n# Of the 84, those public IPFX does not compute (custom code, Methods).\nNOT_COMPUTED = [\"width_suprathresh_ramp\", \"postap_slope_ramp\", \"width_suprathresh_short_square\",\n                \"postap_slope_short_square\", \"sag_peak_t\", \"sag_area\", \"width_suprathresh_rheo\",\n                \"postap_slope_rheo\", \"adp_v_last_rheo\", \"width_suprathresh_hero\", \"postap_slope_hero\",\n                \"ahp_delay_ratio_hero\", \"sag_depol\", \"sag_peak_t_depol\", \"sag_area_depol\",\n                \"ahp_delay_ratio_5spike\", \"trough_slowdeltav_rheo\", \"trough_slowdeltav_hero\", \"sag_tau\"]\n\nSPIKE_FEATURES = [\"upstroke_downstroke_ratio\", \"threshold_v\", \"width\", \"upstroke\", \"downstroke\"]\n\n\n# --- archive -------------------------------------------------------------------------------\n\ndef assets():\n    \"\"\"All assets of the pinned version, with path, size, asset_id and the session id.\"\"\"\n    out, url = [], f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000\"\n    while url:\n        r = requests.get(url, timeout=60)\n        r.raise_for_status()\n        d = r.json()\n        out += d[\"results\"]\n        url = d[\"next\"]\n    df = pd.DataFrame(out)[[\"asset_id\", \"path\", \"size\"]]\n    df[\"subject\"] = df.path.str.extract(r\"sub-([^/_]+)\")[0]\n    df[\"session\"] = df.path.str.extract(r\"ses-([^_]+)_\")[0]\n    return df\n\n\ndef version_metadata():\n    r = requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/\", timeout=60)\n    r.raise_for_status()\n    return r.json()\n\n\ndef s3_url(asset_id):\n    r = requests.get(f\"{API}/assets/{asset_id}/download/\", allow_redirects=False, timeout=60)\n    return r.headers[\"location\"]\n\n\ndef code_table(name):\n    \"\"\"A table from the paper's code repository at the pinned commit (data/<name>).\"\"\"\n    url = f\"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/data/{name}\"\n    r = requests.get(url, timeout=120)\n    r.raise_for_status()\n    return pd.read_csv(io.StringIO(r.text))\n\n\ndef metadata_table():\n    m = code_table(\"LeeDalley_manuscript_metadata_v2.csv\")\n    m.columns = [c.strip() for c in m.columns]\n    m[\"nwb_session\"] = m.nwb_id.map(lambda x: str(int(x)) if pd.notna(x) else None)\n    return m\n\n\n# --- reading a cell ------------------------------------------------------------------------\n\ndef _ontology():\n    from ipfx.stimulus import StimulusOntology\n    import ipfx.json_utilities as ju\n    from ipfx.dataset.create import get_ontology\n    return get_ontology()\n\n\ndef stim_kind(code, ontology):\n    \"\"\"'long_square', 'short_square', 'ramp' or None, from IPFX's stimulus ontology.\"\"\"\n    code = code.rsplit(\"_DA_\", 1)[0]\n    try:\n        names = set(ontology.find_one(code, tag_type=\"code\").tags(tag_type=\"name\"))\n    except (KeyError, ValueError):\n        return None\n    flat = {n for tag in names for n in (tag if isinstance(tag, (list, tuple)) else [tag])}\n    if \"Long Square\" in flat:\n        return \"long_square\"\n    if \"Short Square\" in flat:\n        return \"short_square\"\n    if \"Ramp\" in flat:\n        return \"ramp\"\n    return None\n\n\ndef read_cell(asset_id):\n    \"\"\"Stream one NWB file and return its file-level metadata and its long square, short square\n    and ramp current-clamp sweeps, with the per-sweep bias current and bridge balance.\"\"\"\n    from ipfx.sweep import Sweep\n    ont = _ontology()\n    f = h5py.File(remfile.File(s3_url(asset_id)), \"r\")\n    meta = {\"session_id\": f[\"general/session_id\"][()].decode() if \"general/session_id\" in f else None,\n            \"subject_id\": f[\"general/subject/subject_id\"][()].decode()\n            if \"general/subject/subject_id\" in f else None,\n            \"species\": f[\"general/subject/species\"][()].decode() if \"general/subject/species\" in f else None,\n            \"institution\": f[\"general/institution\"][()].decode() if \"general/institution\" in f else None,\n            \"session_start_time\": f[\"session_start_time\"][()].decode()}\n    sweeps, stim_codes = [], []\n    for name, d in f[\"acquisition\"].items():\n        if d.attrs[\"neurodata_type\"] != \"CurrentClampSeries\":\n            continue\n        code = d.attrs.get(\"stimulus_description\")\n        code = code.decode() if isinstance(code, bytes) else str(code)\n        stim_codes.append(code)\n        kind = stim_kind(code, ont)\n        if kind is None:\n            continue\n        sname = name.replace(\"_AD\", \"_DA\")\n        s = f[\"stimulus/presentation\"][sname]\n        rate = float(d[\"starting_time\"].attrs[\"rate\"])\n        vconv = float(d[\"data\"].attrs[\"conversion\"]) * 1e3   # to mV\n        iconv = float(s[\"data\"].attrs[\"conversion\"]) * 1e12  # to pA\n        v = d[\"data\"][:].astype(float) * vconv\n        i = s[\"data\"][:].astype(float) * iconv\n        n = min(len(v), len(i))\n        v, i = v[:n], i[:n]\n        bias = float(d[\"bias_current\"][0]) if \"bias_current\" in d else np.nan\n        bridge = float(d[\"bridge_balance\"][0]) if \"bridge_balance\" in d else np.nan\n        if d[\"bias_current\"].attrs.get(\"unit\", \"\") == \"Amperes\" if \"bias_current\" in d else False:\n            bias *= 1e12\n        t = np.arange(n) / rate\n        sw = Sweep(t, v, i, \"CurrentClamp\", rate, sweep_number=int(d.attrs[\"sweep_number\"]))\n        sweeps.append(dict(kind=kind, code=code, sweep=sw, rate=rate, bias_pa=bias,\n                           bridge_mohm=bridge, v_unit=d[\"data\"].attrs.get(\"unit\"),\n                           i_unit=s[\"data\"].attrs.get(\"unit\")))\n    f.close()\n    meta[\"stim_codes\"] = stim_codes\n    return meta, sweeps\n\n\ndef sweep_qc(sw):\n    \"\"\"Noise and leak criteria of the Methods for one sweep, on IPFX's QC measures.\"\"\"\n    import ipfx.qc_feature_extractor as qcfe\n    out = {\"bias_pa\": sw[\"bias_pa\"], \"bridge_mohm\": sw[\"bridge_mohm\"]}\n    try:\n        q = qcfe.current_clamp_sweep_qc_features(sw[\"sweep\"], sw[\"kind\"] == \"ramp\")\n        out[\"pre_noise_rms_mv\"] = q[\"pre_noise_rms_mv\"]\n        out[\"slow_noise_rms_mv\"] = q[\"slow_noise_rms_mv\"]\n    except Exception:\n        out[\"pre_noise_rms_mv\"] = out[\"slow_noise_rms_mv\"] = np.nan\n    out[\"pass_noise\"] = bool(out[\"pre_noise_rms_mv\"] < 0.07 and out[\"slow_noise_rms_mv\"] < 0.5)\n    out[\"pass_leak\"] = bool(abs(out[\"bias_pa\"]) <= 100) if np.isfinite(out[\"bias_pa\"]) else True\n    out[\"pass_bridge20\"] = bool(out[\"bridge_mohm\"] < 20) if np.isfinite(out[\"bridge_mohm\"]) else True\n    return out\n\n\n# --- features ------------------------------------------------------------------------------\n\ndef _spike_row(spikes, idx=0):\n    if spikes is None or len(spikes) <= idx:\n        return None\n    return spikes.iloc[idx]\n\n\ndef _shape(prefix, sp, out):\n    \"\"\"First-spike shape features of one sweep, named as in LeeDalley_ephys_fx.csv.\"\"\"\n    if sp is None:\n        return\n    for k in SPIKE_FEATURES:\n        out[f\"{k}_{prefix}\"] = sp.get(k, np.nan)\n    thr = sp.get(\"threshold_v\", np.nan)\n    out[f\"peak_deltav_{prefix}\"] = sp.get(\"peak_v\", np.nan) - thr\n    out[f\"fast_trough_deltav_{prefix}\"] = sp.get(\"fast_trough_v\", np.nan) - thr\n    if prefix != \"short_square\":\n        out[f\"trough_deltav_{prefix}\"] = sp.get(\"trough_v\", np.nan) - thr\n\n\ndef _train(prefix, sf, spikes, out):\n    out[f\"latency_{prefix}\"] = sf.get(\"latency\", np.nan)\n    out[f\"avg_rate_{prefix}\"] = sf.get(\"avg_rate\", np.nan)\n    out[f\"mean_isi_{prefix}\"] = sf.get(\"mean_isi\", np.nan)\n    fi = sf.get(\"first_isi\", np.nan)\n    out[f\"first_isi_inv_{prefix}\"] = 1.0 / fi if fi and np.isfinite(fi) and fi > 0 else np.nan\n    if prefix == \"hero\":\n        out[\"adapt_hero\"] = sf.get(\"adapt\", np.nan)\n        out[\"median_isi_hero\"] = sf.get(\"median_isi\", np.nan)\n        out[\"isi_cv_hero\"] = sf.get(\"isi_cv\", np.nan)\n        out[\"isi_norm_sq_var_hero\"] = _norm_sq(spikes)\n    if prefix == \"rheo\" and spikes is not None and len(spikes):\n        out[\"fast_trough_v_last_rheo\"] = spikes.iloc[-1].get(\"fast_trough_v\", np.nan)\n\n\ndef _norm_sq(spikes):\n    from ipfx.spike_train_features import norm_sq_diff\n    if spikes is None or len(spikes) < 3:\n        return np.nan\n    isis = np.diff(spikes[\"peak_t\"].values)\n    return float(norm_sq_diff(isis))\n\n\ndef long_square_features(sweeps):\n    import ipfx.data_set_features as dsf\n    import ipfx.stim_features as stf\n    import ipfx.stimulus_protocol_analysis as spa\n    from ipfx.sweep import SweepSet\n    from ipfx.stimulus import StimulusType\n    ss = SweepSet([s[\"sweep\"] for s in sweeps])\n    ss.align_to_start_of_epoch(\"experiment\")\n    start, dur, _, _, _ = stf.get_stim_characteristics(ss.sweeps[0].i, ss.sweeps[0].t)\n    spx, sptx = dsf.extractors_for_sweeps(ss, start=start, end=start + dur,\n                                          **dsf.detection_parameters(StimulusType.LONG_SQUARE))\n    an = spa.LongSquareAnalysis(spx, sptx, subthresh_min_amp=-100.0)\n    feat = an.analyze(ss)\n    out = {k: feat.get(k, np.nan) for k in [\"v_baseline\", \"rheobase_i\", \"fi_fit_slope\", \"sag\",\n                                            \"vm_for_sag\", \"input_resistance\", \"tau\"]}\n    spikes_set = feat[\"spikes_set\"]\n    sw_feat = an._sweep_features\n    for prefix, key in [(\"rheo\", \"rheobase_sweep\"), (\"hero\", \"hero_sweep\")]:\n        row = feat.get(key)\n        if row is None:\n            continue\n        idx = row.name\n        spikes = spikes_set[idx]\n        _shape(prefix, _spike_row(spikes), out)\n        _train(prefix, row, spikes, out)\n        out[f\"{prefix}_amp\"] = row.get(\"stim_amp\", np.nan)\n    # adaptation ratios, lowest amplitude sweep with at least four spikes\n    amps = sw_feat[\"stim_amp\"].values\n    n_spk = np.array([len(s) for s in spikes_set])\n    cand = np.where(n_spk >= 4)[0]\n    if len(cand):\n        j = cand[np.argmin(amps[cand])]\n        sp = spikes_set[j]\n        for k, col in [(\"width\", \"width_adapt_ratio\"), (\"upstroke\", \"upstroke_adapt_ratio\"),\n                       (\"downstroke\", \"downstroke_adapt_ratio\"), (\"peak_v\", \"peak_v_adapt_ratio\"),\n                       (\"threshold_v\", \"threshold_v_adapt_ratio\"), (\"fast_trough_v\", \"fast_trough_v_adapt_ratio\")]:\n            out[col] = sp[k].iloc[2] / sp[k].iloc[0]\n        isis = np.diff(sp[\"peak_t\"].values)\n        out[\"isi_adapt_ratio\"] = isis[1] / isis[0]\n    # summaries over spiking sweeps with at least four spikes\n    multi = [j for j in range(len(spikes_set)) if n_spk[j] >= 4]\n    if multi:\n        ad = [sw_feat[\"adapt\"].iloc[j] for j in multi]\n        cv = [sw_feat[\"isi_cv\"].iloc[j] for j in multi]\n        nsq = [_norm_sq(spikes_set[j]) for j in multi]\n        out.update(adapt_mean=np.nanmean(ad), adapt_max=np.nanmax(ad), isi_cv_mean=np.nanmean(cv),\n                   isi_cv_max=np.nanmax(cv), isi_norm_sq_var_mean=np.nanmean(nsq),\n                   isi_norm_sq_var_max=np.nanmax(nsq))\n    return out\n\n\ndef short_square_features(sweeps):\n    import ipfx.data_set_features as dsf\n    import ipfx.stim_features as stf\n    import ipfx.stimulus_protocol_analysis as spa\n    from ipfx.sweep import SweepSet\n    from ipfx.stimulus import StimulusType\n    ss = SweepSet([s[\"sweep\"] for s in sweeps])\n    ss.align_to_start_of_epoch(\"experiment\")\n    start, dur, _, _, _ = stf.get_stim_characteristics(ss.sweeps[0].i, ss.sweeps[0].t)\n    spx, sptx = dsf.extractors_for_sweeps(ss, est_window=[start, start + 0.001],\n                                          **dsf.detection_parameters(StimulusType.SHORT_SQUARE))\n    an = spa.ShortSquareAnalysis(spx, sptx)\n    feat = an.analyze(ss)\n    out = {}\n    cs = feat.get(\"common_amp_sweeps\")\n    if cs is None or len(cs) == 0:\n        return out\n    spikes = [feat[\"spikes_set\"][j] for j in cs.index]\n    first = pd.DataFrame([s.iloc[0] for s in spikes if len(s)])\n    if len(first):\n        _shape(\"short_square\", first.mean(numeric_only=True), out)\n    return out\n\n\ndef ramp_features(sweeps):\n    import ipfx.data_set_features as dsf\n    import ipfx.stim_features as stf\n    import ipfx.stimulus_protocol_analysis as spa\n    from ipfx.sweep import SweepSet\n    from ipfx.stimulus import StimulusType\n    ss = SweepSet([s[\"sweep\"] for s in sweeps])\n    ss.align_to_start_of_epoch(\"experiment\")\n    start, dur, _, _, _ = stf.get_stim_characteristics(ss.sweeps[0].i, ss.sweeps[0].t)\n    spx, sptx = dsf.extractors_for_sweeps(ss, start=start,\n                                          **dsf.detection_parameters(StimulusType.RAMP))\n    an = spa.RampAnalysis(spx, sptx)\n    feat = an.analyze(ss)\n    out = {}\n    spikes = [s for s in feat[\"spikes_set\"] if len(s)]\n    if spikes:\n        first = pd.DataFrame([s.iloc[0] for s in spikes])\n        m = first.mean(numeric_only=True)\n        _shape(\"ramp\", m, out)\n        out[\"threshold_i_ramp\"] = m.get(\"threshold_i\", np.nan)\n    return out\n\n\ndef cell_features(asset_id):\n    \"\"\"Everything this entry measures on one NWB file: metadata, sweep counts and QC, features.\"\"\"\n    warnings.filterwarnings(\"ignore\")\n    logging.disable(logging.WARNING)\n    rec = {\"asset_id\": asset_id}\n    try:\n        meta, sweeps = read_cell(asset_id)\n    except Exception as e:  # unreadable file: reported, never filled in\n        rec[\"error\"] = f\"read: {type(e).__name__}: {e}\"\n        return rec\n    rec.update({k: v for k, v in meta.items() if k != \"stim_codes\"})\n    rec[\"n_cc_sweeps\"] = len(meta[\"stim_codes\"])\n    rec[\"rates\"] = sorted({s[\"rate\"] for s in sweeps})\n    rec[\"units\"] = sorted({f\"{s['v_unit']}|{s['i_unit']}\" for s in sweeps})\n    qcs = [sweep_qc(s) for s in sweeps]\n    keep = [s for s, q in zip(sweeps, qcs) if q[\"pass_noise\"] and q[\"pass_leak\"] and q[\"pass_bridge20\"]]\n    for kind in [\"long_square\", \"short_square\", \"ramp\"]:\n        rec[f\"n_{kind}\"] = sum(s[\"kind\"] == kind for s in sweeps)\n        rec[f\"n_{kind}_qc\"] = sum(s[\"kind\"] == kind for s in keep)\n    rec[\"bridge_max\"] = float(np.nanmax([s[\"bridge_mohm\"] for s in keep])) if keep else np.nan\n    for kind, fn in [(\"long_square\", long_square_features), (\"short_square\", short_square_features),\n                     (\"ramp\", ramp_features)]:\n        sel = [s for s in keep if s[\"kind\"] == kind]\n        if not sel:\n            continue\n        try:\n            rec.update(fn(sel))\n        except Exception as e:\n            rec[f\"error_{kind}\"] = f\"{type(e).__name__}: {e}\"\n    # bridge balance < 15% of Rin (Methods): drop sweeps above and recompute long squares\n    rin = rec.get(\"input_resistance\", np.nan)\n    if np.isfinite(rin):\n        bad = [s for s in keep if np.isfinite(s[\"bridge_mohm\"]) and s[\"bridge_mohm\"] >= 0.15 * rin]\n        rec[\"n_bridge15_dropped\"] = len(bad)\n        if bad:\n            keep2 = [s for s in keep if s not in bad]\n            for kind, fn in [(\"long_square\", long_square_features), (\"short_square\", short_square_features),\n                             (\"ramp\", ramp_features)]:\n                sel = [s for s in keep2 if s[\"kind\"] == kind]\n                for k in [k for k in list(rec) if k.endswith(f\"_{kind}\") or kind == \"long_square\"]:\n                    pass\n                if sel:\n                    try:\n                        rec.update(fn(sel))\n                    except Exception as e:\n                        rec[f\"error_{kind}\"] = f\"{type(e).__name__}: {e}\"\n    return rec\n\n\ndef all_cell_features(asset_ids, workers=4):\n    \"\"\"cell_features over many files, in parallel processes, one file per process at a time.\"\"\"\n    with ProcessPoolExecutor(workers) as ex:\n        return pd.DataFrame(list(ex.map(cell_features, asset_ids, chunksize=1)))\n\n\n# --- statistics ----------------------------------------------------------------------------\n\ndef bh(p):\n    from statsmodels.stats.multitest import multipletests\n    p = np.asarray(p, float)\n    out = np.full_like(p, np.nan)\n    ok = np.isfinite(p)\n    if ok.any():\n        out[ok] = multipletests(p[ok], method=\"fdr_bh\")[1]\n    return out\n\n\ndef mannwhitney_table(df, features, group_col, a, b):\n    \"\"\"Two-sided Mann-Whitney per feature, a against b, with BH FDR across features.\"\"\"\n    from scipy.stats import mannwhitneyu\n    rows = []\n    for f in features:\n        x = df.loc[df[group_col] == a, f].dropna()\n        y = df.loc[df[group_col] == b, f].dropna()\n        if len(x) < 2 or len(y) < 2:\n            rows.append(dict(feature=f, n_a=len(x), n_b=len(y), p=np.nan))\n            continue\n        u, p = mannwhitneyu(x, y, alternative=\"two-sided\")\n        rows.append(dict(feature=f, n_a=len(x), n_b=len(y), median_a=x.median(), median_b=y.median(),\n                         U=u, p=p, rbc=1 - 2 * u / (len(x) * len(y))))\n    t = pd.DataFrame(rows)\n    t[\"p_fdr\"] = bh(t.p)\n    return t\n\n\ndef kruskal_dunn(df, feature, group_col, groups):\n    \"\"\"Kruskal-Wallis across groups and Dunn's post hoc with BH FDR over the pairs.\"\"\"\n    from scipy.stats import kruskal\n    import scikit_posthocs as sp\n    d = df[df[group_col].isin(groups)][[feature, group_col]].dropna()\n    samples = [d.loc[d[group_col] == g, feature].values for g in groups]\n    if min(len(s) for s in samples) < 1:\n        return np.nan, None, d.groupby(group_col)[feature].median()\n    h, p = kruskal(*samples)\n    dunn = sp.posthoc_dunn(d, val_col=feature, group_col=group_col, p_adjust=\"fdr_bh\")\n    return p, dunn.loc[groups, groups], d.groupby(group_col)[feature].agg([\"median\", \"count\"])\n\n\ndef neighbour_fraction(X, labels, k, same=True, among=None, query=None):\n    \"\"\"For each query row, the fraction of its k nearest neighbours (Euclidean, among the rows\n    flagged by `among`) whose label equals its own (same=True) or the given label.\"\"\"\n    from sklearn.neighbors import NearestNeighbors\n    X = np.asarray(X)\n    labels = np.asarray(labels)\n    among = np.ones(len(X), bool) if among is None else np.asarray(among)\n    query = np.ones(len(X), bool) if query is None else np.asarray(query)\n    ref = np.where(among)[0]\n    nn = NearestNeighbors(n_neighbors=k + 1).fit(X[ref])\n    _, ind = nn.kneighbors(X[query])\n    qidx = np.where(query)[0]\n    out = []\n    for qi, row in zip(qidx, ind):\n        nb = [ref[j] for j in row if ref[j] != qi][:k]\n        out.append(labels[nb])\n    return qidx, out\n\n\ndef zscore_impute(F):\n    F = F.astype(float)\n    F = F.fillna(F.median())\n    sd = F.std(ddof=0).replace(0, np.nan)\n    return ((F - F.mean()) / sd).fillna(0.0)\n\n\ndef umap_embed(Z, seed):\n    import umap\n    return umap.UMAP(random_state=seed).fit_transform(np.asarray(Z))\n"
}
```

```
File created successfully at: entries/lee-2023/lee2023.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/lee-2023; python3 - <<'E'
p='lee2023.py'; s=open(p).read()
s=s.replace("""                sel = [s for s in keep2 if s["kind"] == kind]
                for k in [k for k in list(rec) if k.endswith(f"_{kind}") or kind == "long_square"]:
                    pass
                if sel:""","""                sel = [s for s in keep2 if s["kind"] == kind]
                if sel:""")
s=s.replace("""    from ipfx.stimulus import StimulusOntology
    import ipfx.json_utilities as ju
    from ipfx.dataset.create import get_ontology
    return get_ontology()""","""    from ipfx.stimulus import StimulusOntology
    import ipfx.json_utilities as ju
    return StimulusOntology(ju.read(StimulusOntology.DEFAULT_STIMULUS_ONTOLOGY_FILE))""")
s=s.replace("""        if d["bias_current"].attrs.get("unit", "") == "Amperes" if "bias_current" in d else False:
            bias *= 1e12
""","")
open(p,'w').write(s)
E
grep -n "DEFAULT_STIMULUS_ONTOLOGY_FILE\|def find_one\|def tags" $TMPDIR/dev/lib/python3.13/site-packages/ipfx/stimulus.py
```

```
78:    def tags(self, tag_type=None, flat=False):
94:    DEFAULT_STIMULUS_ONTOLOGY_FILE = os.path.join(
151:    def find_one(self, tag, tag_type=None):
194:        ontology_data = ju.read(cls.DEFAULT_STIMULUS_ONTOLOGY_FILE)
```

**Agent**

Now timing on a few cells and comparing with the paper's feature table.

**Agent calls Bash**

```bash
cd entries/lee-2023; cat > $TMPDIR/t1.py <<'E'
import sys, time, resource
sys.path.insert(0,'.')
import lee2023 as L, pandas as pd, numpy as np
A=L.assets(); m=L.metadata_table(); fx=L.code_table('LeeDalley_ephys_fx.csv')
A=A.merge(m[['nwb_session','specimen_id_x']],left_on='session',right_on='nwb_session',how='left')
sub=A[A.specimen_id_x.notna()].sample(8,random_state=1)
t=time.time()
R=L.all_cell_features(sub.asset_id.tolist(),workers=4)
print('time',time.time()-t, 'MB in', sub['size'].sum()/1e6, 'maxrss parent MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3, 'children', resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e3)
R=R.merge(sub[['asset_id','specimen_id_x']],on='asset_id')
print(R.filter(regex='error|n_|rates|units').to_string())
cols=[c for c in fx.columns if c!='specimen_id' and c in R.columns]
print(len(cols))
F=fx.set_index('specimen_id').loc[R.specimen_id_x.astype(int)]
for c in cols:
    a=R[c].values.astype(float); b=F[c].values.astype(float)
    ok=np.isfinite(a)&np.isfinite(b)
    rel=np.abs(a[ok]-b[ok])/np.maximum(np.abs(b[ok]),1e-9)
    print(f"{c:35s} n={ok.sum()} within10%={np.mean(rel<0.1) if ok.sum() else np.nan:.2f}  ex {a[0]:.4g} vs {b[0]:.4g}")
E
$TMPDIR/dev/bin/python $TMPDIR/t1.py 2>&1 | grep -v Warn
```

```
time 2.117525577545166 MB in 261.034086 maxrss parent MB 104.136 children 142.536
                                                                    error  specimen_id_x
0  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   1.067605e+09
1  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   9.399783e+08
2  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   1.069754e+09
3  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   7.378403e+08
4  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   7.705599e+08
5  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   8.509170e+08
6  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   7.678010e+08
7  read: AttributeError: 'numpy.ndarray' object has no attribute 'decode'   8.576186e+08
0
```

**Agent calls Bash**

```bash
cd entries/lee-2023; python3 - <<'E'
p='lee2023.py'; s=open(p).read()
old=s[s.index('    meta = {"session_id"'):s.index('    sweeps, stim_codes = [], []')]
new='''    def txt(path):
        if path not in f:
            return None
        x = f[path][()]
        x = x.flat[0] if isinstance(x, np.ndarray) else x
        return x.decode() if isinstance(x, bytes) else str(x)
    meta = {k: txt(p) for k, p in [("session_id", "general/session_id"),
                                   ("subject_id", "general/subject/subject_id"),
                                   ("species", "general/subject/species"),
                                   ("institution", "general/institution"),
                                   ("session_start_time", "session_start_time")]}
'''
s=s.replace(old,new)
s=s.replace('''        code = d.attrs.get("stimulus_description")
        code = code.decode() if isinstance(code, bytes) else str(code)''','''        code = d.attrs.get("stimulus_description")
        code = code.flat[0] if isinstance(code, np.ndarray) else code
        code = code.decode() if isinstance(code, bytes) else str(code)''')
open(p,'w').write(s)
E
$TMPDIR/dev/bin/python $TMPDIR/t1.py 2>&1 | grep -v Warn
```

```
time 3.5859460830688477 MB in 261.034086 maxrss parent MB 104.2 children 145.244
                                      error  specimen_id_x
0  read: TypeError: unhashable type: 'list'   1.067605e+09
1  read: TypeError: unhashable type: 'list'   9.399783e+08
2  read: TypeError: unhashable type: 'list'   1.069754e+09
3  read: TypeError: unhashable type: 'list'   7.378403e+08
4  read: TypeError: unhashable type: 'list'   7.705599e+08
5  read: TypeError: unhashable type: 'list'   8.509170e+08
6  read: TypeError: unhashable type: 'list'   7.678010e+08
7  read: TypeError: unhashable type: 'list'   8.576186e+08
0
```

**Agent calls Bash**

```bash
cd entries/lee-2023; $TMPDIR/dev/bin/python -c "
import lee2023 as L
o=L._ontology()
for c in ['X4PS_SupraThresh_DA_0','C1LSFINEST150112_DA_0','C1SSFINEST150112_DA_0','X7Ramp_DA_0','subthreshold_171_DA_0','X6SP_Rheo_DA_0','C1RP25PR1S141203_DA_0','X5SP_Search_DA_0']:
  s=o.find_one(c.rsplit('_DA_',1)[0],tag_type='code'); print(c, s.tags(tag_type='name'), s.tags(tag_type='name',flat=True) if True else '')
" 2>&1 | grep -v Warn
```

```
X4PS_SupraThresh_DA_0 [['name', 'Long Square']] ['name', 'Long Square']
C1LSFINEST150112_DA_0 [['name', 'Long Square']] ['name', 'Long Square']
C1SSFINEST150112_DA_0 [['name', 'Short Square']] ['name', 'Short Square']
X7Ramp_DA_0 [['name', 'Ramp']] ['name', 'Ramp']
subthreshold_171_DA_0 [['name', 'Long Square']] ['name', 'Long Square']
X6SP_Rheo_DA_0 [['name', 'Short Square']] ['name', 'Short Square']
C1RP25PR1S141203_DA_0 [['name', 'Ramp']] ['name', 'Ramp']
X5SP_Search_DA_0 [['name', 'Search']] ['name', 'Search']
```

**Agent calls Bash**

```bash
cd entries/lee-2023; python3 - <<'E'
p='lee2023.py'; s=open(p).read()
s=s.replace('''        names = set(ontology.find_one(code, tag_type="code").tags(tag_type="name"))
    except (KeyError, ValueError):
        return None
    flat = {n for tag in names for n in (tag if isinstance(tag, (list, tuple)) else [tag])}''','''        flat = set(ontology.find_one(code, tag_type="code").tags(tag_type="name", flat=True))
    except (KeyError, ValueError):
        return None''')
open(p,'w').write(s)
E
$TMPDIR/dev/bin/python $TMPDIR/t1.py 2>&1 | grep -v Warn
```

```
time 14.115527868270874 MB in 261.034086 maxrss parent MB 104.312 children 1341.984
   session_id        session_start_time  n_cc_sweeps       rates            units  n_long_square  n_long_square_qc  n_short_square  n_short_square_qc  n_ramp  n_ramp_qc  mean_isi_rheo  mean_isi_hero  median_isi_hero  n_bridge15_dropped  specimen_id_x
0  1067604954  2020-12-02T21:46:00.265Z           45  [200000.0]  [volts|amperes]             15                15               3                  3       3          3            NaN       0.111932         0.124085                   0   1.067605e+09
1   939977608  2019-09-05T20:18:56.992Z           95   [50000.0]  [volts|amperes]             11                11               2                  2       3          3       0.217200       0.052082         0.054340                   0   9.399783e+08
2  1069754067  2020-12-11T22:14:41.879Z           70  [200000.0]  [volts|amperes]             23                21               2                  2       6          5            NaN       0.059611         0.060720                   0   1.069754e+09
3   737840111  2018-08-16T18:23:02.526Z           37   [50000.0]  [volts|amperes]              8                 8               4                  3       7          7            NaN       0.007220         0.007220                   0   7.378403e+08
4   770559733  2018-10-31T02:11:48.433Z           53   [50000.0]  [volts|amperes]              9                 9               7                  7       4          4       0.225980       0.086016         0.090900                   0   7.705599e+08
5   850916851  2019-04-12T18:34:06.935Z           34   [50000.0]  [volts|amperes]             13                13               2                  2       3          3            NaN       0.051361         0.047910                   0   8.509170e+08
6   767800905  2018-10-24T02:58:47.526Z           34   [50000.0]  [volts|amperes]             10                10               2                  2       3  
[... 67 more lines not kept]
```

**Agent**

Features match the paper's table exactly for most columns (8 cells in 14 s, so the full set takes about 20 min). The adaptation ratios differ; testing readings.

**Agent calls Bash**

```bash
cd entries/lee-2023; python3 - <<'E'
p='lee2023.py'; s=open(p).read()
s=s.replace('''        isis = np.diff(sp["peak_t"].values)
        out["isi_adapt_ratio"] = isis[1] / isis[0]''','''        isis = np.diff(sp["peak_t"].values)
        out["isi_adapt_ratio"] = isis[1] / isis[0]
        for mn in (4, 5):
            c2 = np.where(n_spk >= mn)[0]
            if len(c2):
                sp2 = spikes_set[c2[np.argmin(amps[c2])]]
                is2 = np.diff(sp2["peak_t"].values)
                out[f"_v{mn}_isi10"] = is2[1] / is2[0]
                if len(is2) > 2:
                    out[f"_v{mn}_isi20"] = is2[2] / is2[0]
                out[f"_v{mn}_width"] = sp2["width"].iloc[2] / sp2["width"].iloc[0]
                out[f"_v{mn}_thr"] = sp2["threshold_v"].iloc[2] / sp2["threshold_v"].iloc[0]''')
open(p,'w').write(s)
E
cat >> $TMPDIR/t1.py <<'E'
for c in [c for c in R.columns if c.startswith('_v')]:
    base={'isi10':'isi_adapt_ratio','isi20':'isi_adapt_ratio','width':'width_adapt_ratio','thr':'threshold_v_adapt_ratio'}[c.split('_')[2]]
    a=R[c].values.astype(float); b=F[base].values.astype(float); ok=np.isfinite(a)&np.isfinite(b)
    print(c, np.round(a,3), np.round(b,3))
E
$TMPDIR/dev/bin/python $TMPDIR/t1.py 2>&1 | grep "^_v"
```

```
_v4_isi10 [2.404 1.046 1.061 1.164 1.082 0.825 1.041 1.86 ] [3.558 1.274 1.204 5.601 1.103 0.85  1.42  6.355]
_v4_isi20 [ 3.608  1.304  1.151 13.724  1.23   0.991  1.17   0.614] [3.558 1.274 1.204 5.601 1.103 0.85  1.42  6.355]
_v4_width [1.074 1.    1.112 1.    1.044 1.12  1.    1.282] [1.099 1.067 1.149 1.211 1.07  1.125 1.04  1.459]
_v4_thr [0.891 1.028 0.948 0.995 0.988 0.924 1.05  0.833] [0.926 0.968 0.937 0.822 0.978 0.933 0.977 0.719]
_v5_isi10 [2.404 1.046 1.061 1.164 1.039 0.257 1.041 0.333] [3.558 1.274 1.204 5.601 1.103 0.85  1.42  6.355]
_v5_isi20 [ 3.608  1.304  1.151 13.724  1.056  0.406  1.17   2.32 ] [3.558 1.274 1.204 5.601 1.103 0.85  1.42  6.355]
_v5_width [1.074 1.    1.112 1.    1.047 1.083 1.    1.472] [1.099 1.067 1.149 1.211 1.07  1.125 1.04  1.459]
_v5_thr [0.891 1.028 0.948 0.995 0.976 0.978 1.05  0.701] [0.926 0.968 0.937 0.822 0.978 0.933 0.977 0.719]
```

**Agent calls Bash**

```bash
cd entries/lee-2023; python3 - <<'E'
p='lee2023.py'; s=open(p).read()
a=s.index('        for mn in (4, 5):'); b=s.index('    # summaries over spiking sweeps')
s=s[:a]+s[b:]
open(p,'w').write(s)
E
grep -n "isi_adapt_ratio\|summaries over" lee2023.py; date -u; cd $TMPDIR; uv pip install -q --python dev/bin/python rdata 2>&1|tail -2; for f in complete_patchseq_data_sets1.RData complete_patchseq_data_sets2.RData; do curl -sL -o repo/$f https://raw.githubusercontent.com/AllenInstitute/human_patchseq_gaba/5eb357a1cea246c7c847b5608a8fc7e87ea95b58/data/$f; done; ls -la repo/*.RData; dev/bin/python -c "
import rdata
for f in ['repo/complete_patchseq_data_sets1.RData','repo/complete_patchseq_data_sets2.RData']:
    p=rdata.parser.parse_file(f); c=rdata.conversion.convert(p)
    for k,v in c.items(): print(f,k,type(v), getattr(v,'shape',None))
"
```

Result: the fetched text is not kept.

**Agent**

The transcriptomes (50,281 genes x 778 cells) load in Python. Reading the paper's R notebook for the gene-expression methods.

**Agent calls Bash**

````bash
cd $TMPDIR; curl -sL -o repo/analysis.Rmd https://raw.githubusercontent.com/AllenInstitute/human_patchseq_gaba/5eb357a1cea246c7c847b5608a8fc7e87ea95b58/scripts_gene_expression/acute_vs_culture_comparisons_update.Rmd; grep -n '```{r' repo/analysis.Rmd | head -80
````

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 47,110p repo/analysis.Rmd; sed -n 325,400p repo/analysis.Rmd; sed -n 767,870p repo/analysis.Rmd
```

````
```{r load FACS data}
load("complete_facs_data_sets.RData")
```  
  
  
Load patch-seq meta-data and data.  
  
```{r load patchseq data}
load("complete_patchseq_data_sets.RData") # Includes datPatch, annoPatch, metaPatch

## Revert names to original Hodge et al names
a <- metaPatch$topLeaf_label
metaPatch$topLeaf_label <- as.character(lapply(strsplit(a," \\("),function(x) return(x[[1]][1])))
annoPatch$topLeaf_label <- metaPatch$topLeaf_label  # To avoid using the wrong cell type assignment below

## Update the morpho call on one cell
metaPatch$morpho_call[metaPatch$spec_id==893655882] = "SMC"
metaPatch$morpho_call[metaPatch$morpho_call=="SMC"] = "Sparse SST"
```
  
[... 224 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR; dev/bin/python -c "
import rdata, numpy as np
c=rdata.conversion.convert(rdata.parser.parse_file('repo/complete_patchseq_data_sets2.RData'))
mp=c['metaPatch']; ap=c['annoPatch']
print(list(mp.columns)); print(mp.head(2).T.to_string()[:3000])
d=c['datPatch2']; print(d.coords); x=np.asarray(d.values); print(x.dtype, x.max(), x.min(), (x>0).mean())
print([k for k in ap.columns if 'immune' in k.lower() or 'cond' in k.lower() or 'morph' in k.lower() or 'nms' in k.lower() or 'marker' in k.lower() or 'gene' in k.lower()])
"; sed -n 109,200p repo/analysis.Rmd
```

```
[np.str_('spec_id'), np.str_('cell_name_label'), np.str_('slice'), np.str_('Block'), np.str_('Donor'), np.str_('structure'), np.str_('disease_state'), np.str_('Tree_first_cl'), np.str_('Hodge_cross_species_types'), np.str_('Jeremy.celltype'), np.str_('condition'), np.str_('source'), np.str_('condition2'), np.str_('Days_In_culture'), np.str_('change.from.12_10_21.run'), np.str_('Has.Reconstuction.'), np.str_('morpho_call'), np.str_('In.L1.dataset.'), np.str_('Call'), np.str_('L1.t.type'), np.str_('subclass_label'), np.str_('postPatch'), np.str_('rigOperator'), np.str_('endPipetteR'), np.str_('rna_amplification_pass_fail'), np.str_('cell_specimen_project'), np.str_('DIV'), np.str_('Virus'), np.str_('percent_reads_aligned_to_exons'), np.str_('Genes.Detected'), np.str_('MALAT1_cpm'), np.str_('cluster_label'), np.str_('res_index'), np.str_('h_score'), np.str_('score'), np.str_('n_marker'), np.str_('res_index_pctile'), np.str_('last_map'), np.str_('topLeaf'), np.str_('topLeafValue'), np.str_('topLeaf_label'), np.str_('patched_cell_container'), np.str_('amplified_quantity_ng'), np.str_('percent_cdna_longer_than_400bp'), np.str_('exp_component_name'), np.str_('marker_genes'), np.str_('quality_score_label'), np.str_('marker_sum_norm_label'), np.str_('Norm_Marker_Sum.0.4_label'), np.str_('seurat_cluster_label'), np.str_('seurat_prediction_score_label'), np.str_('broad_class_label'), np.str_('Tree_second_cl'), np.str_('Tree_third_cl'), np.str_('Tree_first_bt'), np.str_('Tree_second_bt'), np.str_('Tree_third_bt'), np.str_('Tree_first_KL'), np.str_('Tree_second_KL'), np.str_('Tree_third_KL'), np.str_('Tree_first_cor'), np.str_('Tree_second_cor'), np.str_('Tree_third_cor'), np.str_('Tree_call'), np.str_('Old_call'), np.str_('PREVIOUS.Tree_first_cl_label_x'), np.str_('change.from.previous.lock.list'), np.str_('link_ims_20x')]
                                                                                                                                                             
[... 102 more lines not kept]
```

**Agent**

Plan settled. The NWB features match the paper's table, so I'll run the full extraction once now (about 20 min) to a temp file for development; the notebook will recompute it from the archive itself.

**Agent calls Bash**

```bash
cd entries/lee-2023; cat > $TMPDIR/full.py <<'E'
import sys, time, resource
sys.path.insert(0,'.')
import lee2023 as L, pandas as pd
A=L.assets()
t=time.time()
R=L.all_cell_features(A.asset_id.tolist(),workers=4)
R=A.merge(R,on='asset_id')
R.to_pickle(sys.argv[1])
print('time',time.time()-t,'children maxrss MB',resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e3)
print(R.filter(regex='^error').notna().sum())
E
date -u; timeout 3000 $TMPDIR/dev/bin/python $TMPDIR/full.py $TMPDIR/feat.pkl 2>&1 | grep -v Warn | tail -20; date -u
```

```
Wed Nov 18 09:23:26 UTC 2026
time 1249.195102930069 children maxrss MB 4249.28
error_long_square     47
error_short_square     4
dtype: int64
Wed Nov 18 09:44:16 UTC 2026
```

**Agent**

Full extraction took 21 min; one worker peaked at 4.2 GB, so the notebook will use 3 workers. Checking the 47 long-square failures.

**Agent calls Bash**

```bash
cd entries/lee-2023; $TMPDIR/dev/bin/python -c "
import pandas as pd
R=pd.read_pickle('$TMPDIR/feat.pkl')
print(R.error_long_square.dropna().str[:90].value_counts().head(10))
print(R.error_short_square.dropna().str[:90].value_counts())
print(R['rates'].astype(str).value_counts()); print(R['units'].astype(str).value_counts()); print(R.species.value_counts(), R.institution.value_counts())
print((R.session_id==R.session).mean(), (R.subject_id==R.subject).mean())
print(R[['n_long_square','n_long_square_qc','n_short_square_qc','n_ramp_qc']].describe())
"
```

```
error_long_square
ValueError: `ydata` must not be empty!                                                        28
FeatureError: Cannot fit f-I curve slope with less than two sweeps                             6
ValueError: Cannot find rheobase sweep in spiking sweeps with amplitudes:                      5
FeatureError: No spiking long square sweeps, cannot compute cell features.                     4
FeatureError: No subthreshold long square sweeps, cannot evaluate cell features.               2
FeatureError: No subthreshold long square sweeps with stim_amp in range [(-100.0, 0)] Cann     2
Name: count, dtype: int64
error_short_square
FeatureError: No spiking short square sweeps, cannot compute cell features.    4
Name: count, dtype: int64
rates
[50000.0]              625
[200000.0]              78
[]                       1
[25000.0, 50000.0]       1
[50000.0, 200000.0]      1
Name: count, dtype: int64
units
['volts|amperes']    705
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/lee-2023; python3 - <<'E'
p='lee2023.py'; s=open(p).read()
s=s.replace('''def long_square_features(sweeps):
    import ipfx.data_set_features as dsf''','''def _nan_on_error(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except (ValueError, RuntimeError, TypeError, IndexError) as e:
            return np.nan
        except Exception as e:  # IPFX's FeatureError
            if type(e).__name__ == "FeatureError":
                return np.nan
            raise
    wrapper.patched = True
    return wrapper


def _patch_ipfx():
    """A failed tau fit on one sweep, or an f-I slope with one spiking sweep, makes IPFX drop
    every long square feature of the cell; here they give NaN for that feature only."""
    import ipfx.subthresh_features as subf
    import ipfx.spike_train_features as strf
    import ipfx.stimulus_protocol_analysis as spa
    if not getattr(subf.time_constant, "patched", False):
        subf.time_constant = _nan_on_error(subf.time_constant)
        strf.fit_fi_slope = _nan_on_error(strf.fit_fi_slope)
        spa.subf = subf
        spa.strf = strf


def long_square_features(sweeps):
    _patch_ipfx()
    import ipfx.data_set_features as dsf''')
open(p,'w').write(s)
E
grep -n "^import\|^from\|subf\|strf" $TMPDIR/dev/lib/python3.13/site-packages/ipfx/stimulus_protocol_analysis.py | head; cat > $TMPDIR/redo.py <<'E'
import sys; sys.path.insert(0,'.')
import lee2023 as L, pandas as pd
R=pd.read_pickle(sys.argv[1])
bad=R[R.error_long_square.notna()]
N=L.all_cell_features(bad.asset_id.tolist(),workers=4)
print(N.error_long_square.dropna().str[:80].value_counts())
N=bad[['asset_id','path','size','subject','session']].merge(N,on='asset_id')
R=pd.concat([R[R.error_long_square.isna()],N],ignore_index=True)
R.to_pickle(sys.argv[1])
E
$TMPDIR/dev/bin/python $TMPDIR/redo.py $TMPDIR/feat.pkl 2>&1 | grep -v Warn
```

```
1:import numpy as np
2:import pandas as pd
3:import logging
4:from collections import Counter
5:from . import stim_features as stf
6:from . import subthresh_features as subf
7:from . import spike_train_features as strf
8:from .sweep import SweepSet
9:from . import error as er
162:        features["fi_fit_slope"] = strf.fit_fi_slope(spiking_sweep_features["stim_amp"].values,
error_long_square
ValueError: Cannot find rheobase sweep in spiking sweeps with amplitudes:           5
FeatureError: No spiking long square sweeps, cannot compute cell features.          4
FeatureError: No subthreshold long square sweeps with stim_amp in range [(-100.0    4
FeatureError: No subthreshold long square sweeps, cannot evaluate cell features.    3
Name: count, dtype: int64
```

**Agent**

Extraction now fails on only 16 cells, each for a recorded reason. Prototyping the link and composition analyses.

**Agent calls Bash**

```bash
cd entries/lee-2023; cat > $TMPDIR/p1.py <<'E'
import sys; sys.path.insert(0,'.')
import lee2023 as L, pandas as pd, numpy as np
R=pd.read_pickle(sys.argv[1]); m=L.metadata_table(); fx=L.code_table('LeeDalley_ephys_fx.csv')
print(m.columns.tolist())
D=R.merge(m,left_on='session',right_on='nwb_session',how='left',indicator=True)
print(D._merge.value_counts())
e=m[m.Has_ephys==True]
print('Has_ephys rows',len(e),'with nwb_id',e.nwb_session.notna().sum(),'found',e.nwb_session.isin(R.session).sum())
print('ephys rows in fx', e.specimen_id_x.isin(fx.specimen_id).sum(), 'fx rows', len(fx))
# NWB without row
nm=R[~R.session.isin(m.nwb_session.dropna())]; print('files without row',len(nm)); print(nm[['path','n_long_square']].to_string())
# metadata rows w/o Has_ephys but nwb in dandiset
x=m[(m.Has_ephys!=True)&m.nwb_session.isin(R.session)]; print('non-ephys rows with file in dandiset',len(x))
# duplicates in nwb_id
print(m.nwb_session.dropna().duplicated().sum(), m[m.nwb_session.duplicated(keep=False)&m.nwb_session.notna()][['specimen_id_x','cell_name','nwb_session','Has_ephys']])
# specimen vs nwb
print('nwb_id==specimen', (m.nwb_session==m.specimen_id_x.astype(str)).sum())
# agreement
D2=D[D._merge=='both'].merge(fx,left_on='specimen_id_x',right_on='specimen_id',suffixes=('','_paper'))
for c in ['rheobase_i','input_resistance','sag','width_rheo']:
    a=D2[c].astype(float); b=D2[c+'_paper'].astype(float); ok=a.notna()&b.notna()
    rel=(a-b).abs()/b.abs()
    print(c, ok.sum(), (rel[ok]<=0.1).mean())
allc=(D2[[c for c in ['rheobase_i','input_resistance','sag','width_rheo']]].notna().all(1))
E
$TMPDIR/dev/bin/python $TMPDIR/p1.py $TMPDIR/feat.pkl 2>&1 | grep -v Warn
```

```
allc=(D2[[c for c in ['rheobase_i','input_resistance','sag','width_rheo']]].notna().all(1))
['specimen_id_x', 'cell_name', 'Donor', 'structure', 'lobe', 'disease_category', 'Transcriptomic_type', 'M_H_Hodge_cross_species_types', 'condition', 'condition2', 'Days_In_culture', 'Has_morphology', 'Has_ephys', 'Qualitative_morphology_type', 'Cortical_layer', 'subclass_label', 'Revised_subclass_label', 'Virus', 'Genes_Detected', 'patched_cell_container', 'marker_sum_norm_label', 'broad_class_label', 'nwb_id', 'nwb_session']
_merge
both          691
left_only      16
right_only      0
Name: count, dtype: int64
Has_ephys rows 705 with nwb_id 691 found 685
ephys rows in fx 705 fx rows 704
files without row 16
                                                      path  n_long_square
176  sub-567704703/sub-567704703_ses-567737666_icephys.nwb             27
177  sub-567704703/sub-567704703_ses-567773605_icephys.nwb             26
178  sub-569800644/sub-569800644_ses-569870997_icephys.nwb             22
179  sub-571458187/sub-571458187_ses-571674350_icephys.nwb             20
180  sub-591270122/sub-591270122_ses-591326867_icephys.nwb             29
181  sub-591270122/sub-591270122_ses-591342850_icephys.nwb             25
182  sub-595536280/sub-595536280_ses-595591210_icephys.nwb             24
183  sub-595536280/sub-595536280_ses-595597605_icephys.nwb             22
184  sub-595536280/sub-595536280_ses-595715586_icephys.nwb             27
[... 16 more lines not kept]
```

**Agent**

Link holds (685 of 705 ephys rows found; features within 10% for 92 to 99% of cells). The metadata table has one duplicated row. Checking the morphology table columns next.

**Agent calls Bash**

```bash
cd $TMPDIR; dev/bin/python -c "
import pandas as pd
f=pd.read_csv('repo/LeeDalley_morpho_features.csv'); print(f.shape); print(list(f.columns))
m=pd.read_csv('repo/LeeDalley_manuscript_metadata_v2.csv'); m.columns=[c.strip() for c in m.columns]
print(f.iloc[:,0].isin(m.specimen_id_x).sum())
w=m[(m.Transcriptomic_type=='Inh L2-4 PVALB WFDC2')]
print(w.groupby(['condition',w.Has_morphology==True]).size())
print(m[m.Duplicated if False else m.specimen_id_x.duplicated(keep=False)].T)
"
```

```
(140, 53)
['Unnamed: 0', 'specimen_id', 'axon_bias_x', 'axon_bias_y', 'axon_depth_pc_0', 'axon_depth_pc_1', 'axon_depth_pc_2', 'axon_depth_pc_3', 'axon_emd_with_basal_dendrite', 'axon_exit_distance', 'axon_exit_theta', 'axon_extent_x', 'axon_extent_y', 'axon_frac_above_basal_dendrite', 'axon_frac_below_basal_dendrite', 'axon_frac_intersect_basal_dendrite', 'axon_max_branch_order', 'axon_max_euclidean_distance', 'axon_max_path_distance', 'axon_mean_contraction', 'axon_num_branches', 'axon_soma_percentile_x', 'axon_soma_percentile_y', 'axon_total_length', 'basal_dendrite_bias_x', 'basal_dendrite_bias_y', 'basal_dendrite_calculate_number_of_stems', 'basal_dendrite_extent_x', 'basal_dendrite_extent_y', 'basal_dendrite_frac_above_axon', 'basal_dendrite_frac_below_axon', 'basal_dendrite_frac_intersect_axon', 'basal_dendrite_max_branch_order', 'basal_dendrite_max_euclidean_distance', 'basal_dendrite_max_path_distance', 'basal_dendrite_mean_contraction', 'basal_dendrite_mean_diameter', 'basal_dendrite_num_branches', 'basal_dendrite_soma_percentile_x', 'basal_dendrite_soma_percentile_y', 'basal_dendrite_stem_exit_down', 'basal_dendrite_stem_exit_side', 'basal_dendrite_stem_exit_up', 'basal_dendrite_total_length', 'basal_dendrite_total_surface_area', 'soma_surface', 'soma_aligned_dist_from_pia', 'axon_over_basal_dendrite_extent_x', 'axon_over_basal_dendrite_extent_y', 'axon_extent_x_over_y', 'basal_dendrite_extent_x_over_y', 'axon_over_basal_dendrite_ratio_xy', 'axon_branch_freq']
0
condition  Has_morphology
acute      False             63
           True              16
culture    False             79
           True              10
dtype: int64
                                                     249                        250
specimen_id_x                                  819133824                  819133824
cell_name                      h19.03.002.12.01.01.01.04  h19.03.002.12.01.01.01.04
Donor                                         h19.03.002                 h19.03.002
[... 21 more lines not kept]
```

**Agent**

Morphology table has 16 acute and 10 culture PVALB WFDC2 reconstructions (the paper says 10 and 9). Writing the notebook now.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; dev/bin/python -c "
import pandas as pd
f=pd.read_csv('repo/LeeDalley_morpho_features.csv'); m=pd.read_csv('repo/LeeDalley_manuscript_metadata_v2.csv'); m.columns=[c.strip() for c in m.columns]
print(f.specimen_id.isin(m.specimen_id_x).sum())
d=pd.read_csv('repo/dbc_calb1_ADGRG6.csv'); print(d.Tube_id.isin(m.patched_cell_container).sum(), len(d), d.DBC.value_counts())
print(m[m.Qualitative_morphology_type.notna()][['Transcriptomic_type','Qualitative_morphology_type','lobe','nwb_id']].to_string())
x=m[m.patched_cell_container.isin(d.Tube_id[d.DBC=='yes'])]; print(x[['Transcriptomic_type','Qualitative_morphology_type','lobe']])
"
```

```
Wed Nov 18 09:47:17 UTC 2026
140
28 28 DBC
no     17
yes    11
Name: count, dtype: int64
     Transcriptomic_type Qualitative_morphology_type  lobe        nwb_id
59    Inh L1-3 SST CALB1                         DBC  TemL           NaN
68    Inh L1-3 SST CALB1                         DBC  TemL  6.893068e+08
240  Inh L3-5 SST ADGRG6                         DBC  FroL           NaN
267  Inh L3-5 SST ADGRG6                         DBC  TemL  8.197706e+08
268   Inh L1-3 SST CALB1                  Sparse SST  TemL  8.198915e+08
345   Inh L1-3 SST CALB1                         DBC  TemL  8.557830e+08
409   Inh L1-3 SST CALB1                         DBC  TemL  8.936471e+08
412   Inh L1-3 SST CALB1                          MC  TemL  8.937141e+08
419   Inh L1-3 SST CALB1                          MC  TemL  8.945275e+08
420   Inh L1-3 SST CALB1                         DBC  TemL  8.946105e+08
445  Inh L3-5 SST ADGRG6                         DBC  FroL  9.075850e+08
509   Inh L1-3 SST CALB1                  Sparse SST  TemL  9.418624e+08
536   Inh L1-3 SST CALB1                         DBC  OccL  9.669054e+08
[... 20 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Builds entries/lee-2023/reproduce_lee_2023.ipynb. With --dev, the extraction cell reads a cached\ntable instead, and the notebook is written to $TMPDIR for development only.\"\"\"\nimport sys, os\nimport nbformat as nbf\n\nDEV = \"--dev\" in sys.argv\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip()))\n\n\ndef code(s, tags=()):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = list(tags)\n    cells.append(c)\n\n\nmd(open(os.path.join(os.path.dirname(__file__), \"nb_header.md\")).read())\n\ncode(r'''\nimport time, zlib, resource, warnings, logging\nimport numpy as np, pandas as pd\nfrom scipy import stats\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport lee2023 as L\nwarnings.filterwarnings(\"ignore\")\nlogging.disable(logging.WARNING)\npd.set_option(\"display.width\", 200); pd.set_option(\"display.max_columns\", 40)\nKEY = \"lee-2023\"\ndef seed(claim, k=0):\n    \"\"\"Seed of a claim's generator (protocol, author step 3); k-th generator adds k.\"\"\"\n    return zlib.crc32(f\"{KEY}/{claim}\".encode()) + k\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\nT0 = time.time()\n''')\n\nmd(\"## Data\\n\\nThe asset list of the pinned version, the dandiset metadata, and the paper's tables from its code repository at commit 5eb357a (labels only; claim cell-metadata-link).\")\ncode(r'''\nA = L.assets()\nV = L.version_metadata()\nmeta = L.metadata_table()\nfx_paper = L.code_table(\"LeeDalley_ephys_fx.csv\")\nmorph = L.code_table(\"LeeDalley_morpho_features.csv\")\ndbc_tab = L.code_table(\"dbc_calb1_ADGRG6.csv\")\nFEATS84 = [c for c in fx_paper.columns if c != \"specimen_id\" and c not in L.CHIRP]\nprint(\"version\", L.VERSION, \"assets\", len(A), \"subjects\", A.subject.nunique(), \"sessions\", A.session.nunique(),\n      \"total GB\", round(A[\"size\"].sum() / 1e9, 2))\nprint(\"archive summary:\", {k: V[\"assetsSummary\"].get(k) for k in [\"numberOfFiles\", \"numberOfSubjects\", \"numberOfCells\"]})\nprint(\"metadata rows\", len(meta), \"unique specimens\", meta.specimen_id_x.nunique(), \"| feature table rows\", len(fx_paper),\n      \"| feature columns\", fx_paper.shape[1] - 1, \"of which chirp\", len(L.CHIRP), \"-> 84 =\", len(FEATS84))\n''')\n\nif DEV:\n    extraction = r'''\nR = pd.read_pickle(os.environ[\"LEE_CACHE\"])\n'''\nelse:\n    extraction = r'''\nt = time.time()\nR = L.all_cell_features(A.asset_id.tolist(), workers=3)\nR = A.merge(R, on=\"asset_id\")\nprint(f\"extraction {time.time() - t:.0f} s; peak memory of a worker {resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6:.2f} GB\")\n'''\nmd(\"## Feature extraction\\n\\nEvery NWB file is streamed and its long square, short square and ramp sweeps read; sweeps failing the Methods' QC are dropped, and IPFX computes the features (helper `cell_features`). This takes about 25 minutes.\")\ncode((\"import os\\n\" if DEV else \"\") + extraction.strip())\n\ncode(r'''\nFEATS = [c for c in FEATS84 if c in R.columns]\nprint(\"of the 84 features,\", len(FEATS), \"computed;\", len(set(FEATS84) - set(FEATS)), \"not computed by public IPFX:\",\n      sorted(set(FEATS84) - set(FEATS)))\nerr = R.filter(regex=\"^error\").notna()\nprint(\"files with a read error:\", int(err.get(\"error\", pd.Series(False)).sum()))\nfor c in err.columns:\n    if c != \"error\":\n        print(c, int(err[c].sum()), R[c].dropna().str.split(\":\").str[0].str[:60].value_counts().to_dict())\nm1 = meta.drop_duplicates()\nD = R.merge(m1, left_on=\"session\", right_on=\"nwb_session\", how=\"left\")\nD[\"has_row\"] = D.specimen_id_x.notna()\nD[\"subclass\"] = D.Revised_subclass_label\nD[\"ttype\"] = D.Transcriptomic_type\nD[\"ls_ok\"] = D.n_long_square_qc > 0\nE = D[D.has_row & D.ls_ok].copy()     # labelled cells with at least one QC-passing long square sweep\nprint(\"labelled files\", int(D.has_row.sum()), \"| with a QC-passing long square sweep\", len(E),\n      \"| with rheobase\", int(E.rheobase_i.notna().sum()), \"| with sag\", int(E.sag.notna().sum()))\n''')\n\nmd(\"## Data check\")\ncode(r'''\nprint(\"Files and subjects\")\nprint(\"  files\", len(R), \"subjects (sub- folders)\", R.subject.nunique(), \"| subject_id in file equals folder:\", bool((R.subject_id == R.subject).all()),\n      \"| session_id equals file name:\", bool((R.session_id == R.session).all()))\nprint(\"  species strings:\", R.species.value_counts().to_dict(), \"| institution:\", R.institution.value_counts().to_dict())\nprint(\"  archive summary says numberOfCells\", V[\"assetsSummary\"].get(\"numberOfCells\"), \"for\", len(R), \"files, one cell per file\")\nprint(\"Sampling rates of the analysed sweeps (Hz):\", R.rates.astype(str).value_counts().to_dict())\nprint(\"  the Methods state 'digitized at 50 kHz'; files at 200 kHz by session date:\")\nR[\"year\"] = R.session_start_time.str[:4]\nprint(pd.crosstab(R.year, R.rates.astype(str)))\nprint(\"Units (response|stimulus):\", R.units.astype(str).value_counts().to_dict())\nprint(\"Sweeps per file: long square\", R.n_long_square.describe()[[\"min\", \"50%\", \"max\"]].to_dict(),\n      \"| after QC\", R.n_long_square_qc.describe()[[\"min\", \"50%\", \"max\"]].to_dict())\nprint(\"  sweeps dropped by QC: long square %d of %d, short square %d of %d, ramp %d of %d\" % (\n      (R.n_long_square - R.n_long_square_qc).sum(), R.n_long_square.sum(), (R.n_short_square - R.n_short_square_qc).sum(),\n      R.n_short_square.sum(), (R.n_ramp - R.n_ramp_qc).sum(), R.n_ramp.sum()))\nprint(\"  sweeps dropped for bridge balance >= 15% of Rin (cells):\", int((R.n_bridge15_dropped > 0).sum()))\nprint(\"Labelled cells by condition and subclass (labelled files with a QC-passing long square sweep)\")\nprint(pd.crosstab(E.subclass, E.condition, margins=True))\nprint(\"Donors\", E.Donor.nunique(), \"| cells per donor median\", E.groupby(\"Donor\").size().median())\nprint(\"Ranges of the variables used\")\nfor c in [\"rheobase_i\", \"input_resistance\", \"sag\", \"vm_for_sag\", \"width_rheo\", \"width_short_square\", \"upstroke_downstroke_ratio_rheo\",\n          \"peak_deltav_rheo\", \"latency_rheo\", \"avg_rate_hero\", \"fi_fit_slope\", \"v_baseline\", \"tau\"]:\n    x = E[c].dropna()\n    print(f\"  {c:32s} n={len(x):3d} min={x.min():.4g} median={x.median():.4g} max={x.max():.4g}\")\nprint(\"Clock check: the first spike of the rheobase sweep follows stimulus onset; latency (s) over cells:\",\n      E.latency_rheo.describe()[[\"min\", \"50%\", \"max\"]].round(4).to_dict(), \"| negative:\", int((E.latency_rheo < 0).sum()),\n      \"| beyond the 1 s step:\", int((E.latency_rheo > 1.0).sum()))\nprint(\"  contrast: rate in the hero sweep (rheobase + 40 pA) against rheobase sweep, median\",\n      E.avg_rate_hero.median(), \"against\", E.avg_rate_rheo.median(), \"spikes/s; higher in\",\n      int((E.avg_rate_hero > E.avg_rate_rheo).sum()), \"of\", int(E[[\"avg_rate_hero\", \"avg_rate_rheo\"]].notna().all(1).sum()), \"cells\")\nprint(\"  hyperpolarizing sweep used for sag reaches\", E.vm_for_sag.describe()[[\"min\", \"50%\", \"max\"]].round(1).to_dict(), \"mV (target -100 mV)\")\nprint(\"Days in culture of culture cells:\", E[E.condition == \"culture\"].Days_In_culture.value_counts().sort_index().to_dict())\n''', tags=[\"sanity\"])\n\n# ---- link\nmd('''## cell-metadata-link\n\n> The dandiset's NWB files can be matched to the paper's per-cell metadata and feature tables in its code repository, and features recomputed from the files agree with those tables.\n\nMatched by `nwb_id` (the NWB session id). Reproduced when at least 90% of the `Has_ephys` rows are found and rheobase_i, input_resistance, sag and width_rheo are within 10% of the paper's table for at least 90% of cells with both values.''')\ncode(r'''\nephys_rows = m1[m1.Has_ephys == True]\nfound = ephys_rows.nwb_session.isin(R.session)\nprint(\"metadata rows\", len(meta), \"(one duplicated row:\", int(meta.duplicated().sum()), \") -> unique rows\", len(m1))\nprint(\"Has_ephys rows\", len(ephys_rows), \"| with nwb_id\", int(ephys_rows.nwb_session.notna().sum()),\n      \"| found in the dandiset\", int(found.sum()), f\"({found.mean():.1%})\")\nprint(\"  Has_ephys rows without nwb_id:\", int(ephys_rows.nwb_session.isna().sum()),\n      \"| nwb_id not in the dandiset:\", int((ephys_rows.nwb_session.notna() & ~found).sum()))\nprint(\"rows without Has_ephys whose nwb_id is in the dandiset:\", int(((m1.Has_ephys != True) & m1.nwb_session.isin(R.session)).sum()))\nnores = R[~R.session.isin(m1.nwb_session.dropna())]\nprint(\"NWB files without a metadata row:\", len(nores), \"| their sessions:\", nores.session.tolist())\nJ = D[D.has_row].merge(fx_paper, left_on=\"specimen_id_x\", right_on=\"specimen_id\", suffixes=(\"\", \"_paper\"))\nLINK = {}\nrows = []\nfor c in FEATS:\n    a, b = J[c].astype(float), J[c + \"_paper\"].astype(float)\n    ok = a.notna() & b.notna()\n    rel = ((a - b).abs() / b.abs().where(b != 0))[ok]\n    rows.append(dict(feature=c, n=int(ok.sum()), within10=(rel <= 0.1).mean(), median_rel_diff=rel.median(),\n                     missing_here=int((a.isna() & b.notna()).sum()), missing_paper=int((a.notna() & b.isna()).sum())))\nagree = pd.DataFrame(rows).set_index(\"feature\")\nfor c in [\"rheobase_i\", \"input_resistance\", \"sag\", \"width_rheo\"]:\n    LINK[c] = agree.loc[c, \"within10\"]\nprint(agree.loc[[\"rheobase_i\", \"input_resistance\", \"sag\", \"width_rheo\"]].round(3))\nfour = [\"rheobase_i\", \"input_resistance\", \"sag\", \"width_rheo\"]\nok4 = J[four].notna().all(1) & J[[f + \"_paper\" for f in four]].notna().all(1)\njoint = np.all([((J[f] - J[f + \"_paper\"]).abs() / J[f + \"_paper\"].abs() <= 0.1) for f in four], axis=0)[ok4.values]\nprint(f\"all four within 10% together: {joint.mean():.3f} of {ok4.sum()} cells (a stricter reading, shown only)\")\nprint(\"Agreement over all computed features (fraction of cells within 10%):\")\nprint(agree.within10.describe().round(3).to_dict())\nprint(\"features with fewer than 80% of cells within 10%:\", agree[agree.within10 < 0.8].within10.round(2).to_dict())\nlink_ok = found.mean() >= 0.9 and min(LINK.values()) >= 0.9\nprint(\"RESULT link:\", \"reproduced\" if link_ok else (\"partial\" if min(LINK.values()) >= 0.5 else \"not reproduced\"))\n''', tags=[\"claim:cell-metadata-link\"])\nmd(\"**Result: ...**\")\n\n# ---- composition\nmd('''## dataset-composition\n\n> The study characterized 778 human GABAergic neurons in layers 2 to 6, covering 44 of the 45 GABAergic t-types, with electrophysiology from 75 LAMP5/PAX6, 99 VIP, 149 SST and 352 PVALB neurons.\n\nCounted over the dandiset's files with a QC-passing long square sweep, labelled through the link, by (a) `Revised_subclass_label` and (b) `subclass_label`; 778 and 44 over all labelled cells. Cell-level QC (seal, access resistance) is not recomputed here.''')\ncode(r'''\nexp = {\"LAMP5/PAX6/Other\": 75, \"VIP\": 99, \"SST\": 149, \"PVALB\": 352}\nprint(\"neurons in the metadata table (unique specimens):\", m1.specimen_id_x.nunique(), \"| t-types:\", m1.Transcriptomic_type.nunique())\nprint(\"layers of the labelled cells:\", m1.Cortical_layer.value_counts(dropna=False).to_dict())\ncomp = pd.DataFrame({\"expected\": exp,\n                     \"a_revised\": E.Revised_subclass_label.value_counts(),\n                     \"b_subclass_label\": E.subclass_label.value_counts(),\n                     \"all_Has_ephys_rows_revised\": m1[m1.Has_ephys == True].Revised_subclass_label.value_counts()})\ncomp[\"a_within\"] = (comp.a_revised - comp.expected).abs() <= 0.1 * comp.expected\ncomp[\"b_within\"] = (comp.b_subclass_label - comp.expected).abs() <= 0.1 * comp.expected\nprint(comp)\nprint(\"files counted\", len(E), \"| sum of expected\", sum(exp.values()))\nprint(\"labelled files without a QC-passing long square sweep:\", int((D.has_row & ~D.ls_ok).sum()))\nprint(\"RESULT composition: reading a all within:\", bool(comp.a_within.all()), \"| reading b all within:\", bool(comp.b_within.all()))\n''', tags=[\"claim:dataset-composition\"])\nmd(\"**Result: ...**\")\n\nopen(os.path.join(os.path.dirname(__file__), \"nb_cells_part2.py\")).read()\nexec(open(os.path.join(os.path.dirname(__file__), \"nb_cells_part2.py\")).read())\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nout = sys.argv[1]\nnbf.write(nb, out)\nprint(\"wrote\", out, len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now the claim sections (part 2 of the builder).

**Agent calls Bash**

```bash
cd $TMPDIR; uv pip install -q --python dev/bin/python python-igraph 2>&1 | tail -1; dev/bin/python -c "import igraph; print(igraph.__version__)"; sed -n 933,990p repo/analysis.Rmd
```

````
1.0.0
```{r morpho of immune culture cells, fig.height=4, fig.width=6, warning=FALSE}
kpMCI  <- is.element(metaPatch$topLeaf_label,c("Inh L1-3 SST CALB1"))#,"Inh L3-5 SST ADGRG6"))
kpMCI  <- kpMCI&(metaPatch$condition2=="culture_immune")&!(is.element(metaPatch$morpho_call,c("","Unknown")))
offMCI <- rownames(datPatch)[rowMedians(datPatch[,kpMCI])<1]
kpGnMCI<- setdiff(names(keepGenes)[keepGenes],c(all_immune,offMCI))
datMCI <- datPatch[kpGnMCI,kpMCI]  # Exclude immune genes again, as well as genes not expressed in half the cells

metadataMCI <- data.frame(morpho = metaPatch$morpho_call[kpMCI])
rownames(metadataMCI) <- colnames(datMCI)
mci <- CreateSeuratObject(counts = datMCI, meta.data = metadataMCI)
mci <- FindVariableFeatures(mci,nfeatures = 250, verbose = FALSE) 
mci <- ScaleData(mci, verbose = FALSE)
mci <- RunPCA(mci, npcs = 5, verbose = FALSE)
mci2 <- RunUMAP(mci, reduction = "pca", dims = 1:5, verbose = FALSE, n.neighbors = 3)

DimPlot(mci2, reduction = "umap", group.by = "morpho",pt.size=4)
```
  
No separation by morphology using variable genes.  What about by DEX genes?  
[... 40 more lines not kept]
````

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_cells_part2.py",
 "content": "# Claim sections after dataset-composition; exec'd by build_nb.py (uses md, code).\n\n# ---------------- transcriptomes (elsewhere: the paper's code repository)\nmd('''## Transcriptomes from the paper's code repository\n\nThe claims on gene expression are `data: elsewhere`: the expression matrices are in the code repository at commit 5eb357a (`complete_patchseq_data_sets1/2.RData`, log2(CPM + 1), 778 cells), read here with the `rdata` package.''')\ncode(r'''\nX, metaP = L.transcriptomes()\nprint(\"expression matrix genes x cells\", X.shape, \"| value range\", float(X.values.min()), float(X.values.max()))\ncells_meta = m1.set_index(\"patched_cell_container\")\nprint(\"expression columns found in the metadata table:\", int(X.columns.isin(cells_meta.index).sum()), \"of\", X.shape[1])\nT = cells_meta.loc[X.columns]\ngenes_detected_here = (X > 0).sum(axis=0)\nprint(\"genes detected (>0) agrees with the Genes_Detected column for\", int((genes_detected_here.values == T.Genes_Detected.values).sum()), \"of\", len(T),\n      \"cells; median absolute difference\", float(np.median(np.abs(genes_detected_here.values - T.Genes_Detected.values))))\n''', tags=[\"sanity\"])\n\nmd('''## fig1b-more-genes-in-culture\n\n> Patch-seq neurons from slices in culture (2 to 16 days) had more genes detected than neurons from acute slices.\n\nTwo-sided Mann-Whitney, culture against acute (`condition`); reproduced when the culture median is higher at p < 0.0001.''')\ncode(r'''\ng = pd.DataFrame({\"genes\": genes_detected_here.values, \"condition\": T.condition.values, \"dic\": T.Days_In_culture.values})\nfor name, col in [(\"genes > 0 in the matrix\", \"genes\")]:\n    a, c = g[g.condition == \"acute\"][col], g[g.condition == \"culture\"][col]\n    u, p = stats.mannwhitneyu(c, a, alternative=\"two-sided\")\n    print(f\"{name}: acute n={len(a)} median={a.median():.0f}, culture n={len(c)} median={c.median():.0f}, U={u:.0f}, p={p:.3g}\")\na2, c2 = T[T.condition == \"acute\"].Genes_Detected, T[T.condition == \"culture\"].Genes_Detected\nprint(\"Genes_Detected column: medians\", a2.median(), c2.median(), \"p=%.3g\" % stats.mannwhitneyu(c2, a2).pvalue)\nprint(\"RESULT fig1b:\", bool(c.median() > a.median() and p < 1e-4))\n''', tags=[\"claim:fig1b-more-genes-in-culture\"])\nmd(\"**Result: ...**\")\n\nmd('''## figs1a-genes-across-days\n\n> The higher number of genes detected in culture is present at every day in culture sampled and stays consistent across days in culture.\n\nPearson's correlation of genes detected with days in culture over culture cells (holds when p >= 0.05), and the median at every day above the acute median.''')\ncode(r'''\ncg = g[g.condition == \"culture\"]\nr, p = stats.pearsonr(cg.dic, cg.genes)\nper_day = cg.groupby(\"dic\").genes.agg([\"median\", \"count\"])\nper_day[\"above_acute_median\"] = per_day[\"median\"] > a.median()\nprint(per_day.T)\nprint(f\"acute median {a.median():.0f}; Pearson r={r:.3f}, p={p:.3g}, n={len(cg)}\")\nrs, ps = stats.spearmanr(cg.dic, cg.genes)\nprint(f\"variant, Spearman rho={rs:.3f}, p={ps:.3g}\")\nprint(\"RESULT figs1a: consistency (p>=0.05):\", bool(p >= 0.05), \"| elevation at every day:\", bool(per_day.above_acute_median.all()))\n''', tags=[\"claim:figs1a-genes-across-days\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig1d-nms-no-difference\n\n> The normalized marker sum score does not differ between acute and culture neurons.\n\nA claim of absence, judged on the two-sided Mann-Whitney test of `marker_sum_norm_label`, acute against culture.''')\ncode(r'''\nnms_a = m1[m1.condition == \"acute\"].marker_sum_norm_label.dropna()\nnms_c = m1[m1.condition == \"culture\"].marker_sum_norm_label.dropna()\nu, p = stats.mannwhitneyu(nms_a, nms_c, alternative=\"two-sided\")\nprint(f\"acute n={len(nms_a)} median={nms_a.median():.3f}; culture n={len(nms_c)} median={nms_c.median():.3f}; U={u:.0f} p={p:.3g}; \"\n      f\"rank-biserial={1 - 2 * u / (len(nms_a) * len(nms_c)):.3f}\")\nprint(\"NMS range\", round(m1.marker_sum_norm_label.min(), 3), round(m1.marker_sum_norm_label.max(), 3))\nprint(\"RESULT fig1d: no difference (p>=0.05):\", bool(p >= 0.05))\n''', tags=[\"claim:fig1d-nms-no-difference\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig1c-marker-expression-correlated\n\n> For the top differentially expressed genes of each GABAergic subclass, average expression in acute and culture neurons is strongly correlated.\n\nReadings named by the criterion: Pearson or Spearman, log2(CPM + 1) or CPM, per subclass or pooled, genes ranked by differential expression in the Patch-seq cells (the snRNA-seq ranking needs the dissociated-nuclei reference, which the code repository does not hold: its notebook loads `complete_facs_data_sets.RData`, absent at 5eb357a). Patch-seq ranking: the 25 genes with the largest difference in mean log2(CPM + 1) between a subclass's cells and all other cells (a standard choice).''')\ncode(r'''\nsub_T = T.Revised_subclass_label.values\nrows = []\ntop = {}\nfor s in [\"LAMP5/PAX6/Other\", \"PVALB\", \"SST\", \"VIP\"]:\n    ins = sub_T == s\n    diff = X.loc[:, ins].mean(axis=1) - X.loc[:, ~ins].mean(axis=1)\n    top[s] = diff.sort_values(ascending=False).index[:25]\npts = {}\nfor scale in [\"log2\", \"cpm\"]:\n    for s in top:\n        ins = sub_T == s\n        Y = X.loc[top[s]]\n        if scale == \"cpm\":\n            Y = 2 ** Y - 1\n        ma = Y.loc[:, ins & (T.condition.values == \"acute\")].mean(axis=1)\n        mc = Y.loc[:, ins & (T.condition.values == \"culture\")].mean(axis=1)\n        pts[(scale, s)] = (ma, mc)\n        for test, fn in [(\"pearson\", stats.pearsonr), (\"spearman\", stats.spearmanr)]:\n            r, p = fn(ma, mc)\n            rows.append(dict(scale=scale, panel=s, test=test, r=r, p=p, n=len(ma)))\n    ma = pd.concat([pts[(scale, s)][0] for s in top]); mc = pd.concat([pts[(scale, s)][1] for s in top])\n    for test, fn in [(\"pearson\", stats.pearsonr), (\"spearman\", stats.spearmanr)]:\n        r, p = fn(ma, mc)\n        rows.append(dict(scale=scale, panel=\"pooled\", test=test, r=r, p=p, n=len(ma)))\nc1 = pd.DataFrame(rows)\nc1[\"holds\"] = (c1.p < 1e-4) & (c1.r > 0)\nprint(c1.round(6).to_string())\nper_sub = c1[c1.panel != \"pooled\"].groupby([\"scale\", \"test\"]).holds.all()\npooled = c1[c1.panel == \"pooled\"].set_index([\"scale\", \"test\"]).holds\nprint(\"per-subclass readings hold in every subclass:\", per_sub.to_dict()); print(\"pooled readings:\", pooled.to_dict())\nprint(\"cells acute/culture per subclass:\", pd.crosstab(T.Revised_subclass_label, T.condition).to_dict())\nprint(\"RESULT fig1c: all readings run hold:\", bool(per_sub.all() and pooled.all()))\n''', tags=[\"claim:fig1c-marker-expression-correlated\"])\nmd(\"**Result: ...**\")\n\nmd('''## figs2d-seven-channel-genes\n\n> Of 114 voltage-gated ion-channel genes, only seven differ in expression between culture and acute neurons.\n\nAs the code's chunks \"linear model gene expression WFDC2\" and \"fold change and ion channels WFDC2\": PVALB WFDC2 cells, genes with mean > 0.01, `lm(expression ~ condition + isImmune + condition*isImmune)` per gene, `apply(lm_pval, 2, p.adjust)` (Holm over each gene's three term p-values, as the code applies it per gene), channel genes from `vgic_genes.csv`, counted at adjusted p <= 0.01. isImmune is the paper's call (`condition2` ending in \"microglial\"). The code's `keepGenes` filter needs the dissociated-nuclei data, not in the repository, so it is not applied.''')\ncode(r'''\nvgic = L.code_table(\"vgic_genes.csv\")\nchannels = set(vgic[\"HGNC.symbol\"].dropna())\nwf = (T.Transcriptomic_type == \"Inh L2-4 PVALB WFDC2\").values\nXw = X.loc[:, wf]\nkeep = Xw.mean(axis=1) > 0.01\nXw = Xw[keep]\ncond = (T.condition.values[wf] == \"culture\").astype(float)\nimm = T.condition2.str.contains(\"microglial\").values[wf].astype(float)\nDm = np.column_stack([np.ones_like(cond), cond, imm, cond * imm])\nprint(\"PVALB WFDC2 cells\", int(wf.sum()), \"| by condition2\", pd.Series(T.condition2.values[wf]).value_counts().to_dict())\nY = Xw.values.T\nbeta, *_ = np.linalg.lstsq(Dm, Y, rcond=None)\nresid = Y - Dm @ beta\ndof = Dm.shape[0] - np.linalg.matrix_rank(Dm)\ns2 = (resid ** 2).sum(0) / dof\nXtXi = np.linalg.pinv(Dm.T @ Dm)\nse = np.sqrt(np.outer(np.diag(XtXi), s2))\nwith np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n    tval = beta / se\npv = 2 * stats.t.sf(np.abs(tval), dof)[1:]          # condition, isImmune, interaction\nfrom statsmodels.stats.multitest import multipletests\ndef holm_cols(P):\n    out = np.full_like(P, np.nan)\n    for j in range(P.shape[1]):\n        ok = np.isfinite(P[:, j])\n        if ok.any():\n            out[ok, j] = multipletests(P[ok, j], method=\"holm\")[1]\n    return out\nadj = holm_cols(pv)[0]\ngenes = Xw.index\nisch = genes.isin(channels)\nres = pd.DataFrame({\"p_condition\": pv[0], \"adj_per_gene\": adj, \"channel\": isch}, index=genes)\nres[\"holm_across_genes\"] = L.bh(res.p_condition) * np.nan\nokp = np.isfinite(res.p_condition)\nres.loc[okp, \"holm_across_genes\"] = multipletests(res.p_condition[okp], method=\"holm\")[1]\nres.loc[okp, \"bh_across_genes\"] = multipletests(res.p_condition[okp], method=\"fdr_bh\")[1]\nres[\"FC\"] = Xw.loc[:, cond == 1].mean(1) - Xw.loc[:, cond == 0].mean(1)\nchan = res[res.channel]\nprint(\"genes tested\", len(res), \"| channel genes in vgic list\", len(channels), \"| channel genes tested\", len(chan))\nn_main = int((chan.adj_per_gene <= 0.01).sum())\nprint(\"channel genes with adjusted p <= 0.01 (code's per-gene Holm):\", n_main)\nprint(chan[chan.adj_per_gene <= 0.01].sort_values(\"adj_per_gene\")[[\"p_condition\", \"adj_per_gene\", \"FC\"]].round(5))\nprint(\"variants: Holm across genes\", int((chan.holm_across_genes <= 0.01).sum()), \"| BH across genes\", int((chan.bh_across_genes <= 0.01).sum()),\n      \"| unadjusted p <= 0.01\", int((chan.p_condition <= 0.01).sum()))\nprint(\"RESULT figs2d: count\", n_main, \"channel genes tested\", len(chan))\n''', tags=[\"claim:figs2d-seven-channel-genes\"])\nmd(\"**Result: ...**\")\n\n# ---------------- DBCs\nmd('''## fig5a-dbc-two-ttypes\n\n> Morphologically classic double bouquet cells map to two t-types, SST CALB1 and SST ADGRG6.\n\nDBC calls from `dbc_calb1_ADGRG6.csv`; their t-types there (`Tree_first_cl`) against the tree mapping stored with the transcriptomes (`Tree_first_cl` of `metaPatch`) and the metadata table. The tree mapping itself is not re-run (it needs the MTG reference taxonomy).''')\ncode(r'''\ndbc_yes = dbc_tab[dbc_tab.DBC == \"yes\"].copy()\nmp = metaP.set_index(\"patched_cell_container\") if \"patched_cell_container\" in metaP.columns else None\ndbc_yes[\"tree_metaPatch\"] = mp.loc[dbc_yes.Tube_id, \"Tree_first_cl\"].values\ndbc_yes[\"ttype_metadata\"] = cells_meta.loc[dbc_yes.Tube_id, \"Transcriptomic_type\"].values\ndbc_yes[\"morph_metadata\"] = cells_meta.loc[dbc_yes.Tube_id, \"Qualitative_morphology_type\"].values\nprint(dbc_yes[[\"cell_name_label\", \"Tree_first_cl\", \"tree_metaPatch\", \"ttype_metadata\", \"morph_metadata\"]].to_string())\ncnt = dbc_yes.Tree_first_cl.value_counts()\nprint(\"DBCs by t-type:\", cnt.to_dict())\nprint(\"agree with metaPatch:\", int((dbc_yes.Tree_first_cl == dbc_yes.tree_metaPatch).sum()), \"| with metadata table:\",\n      int((dbc_yes.Tree_first_cl.str.strip() == dbc_yes.ttype_metadata.str.strip()).sum()), \"of\", len(dbc_yes))\nprint(\"metadata cells with Qualitative_morphology_type DBC:\", int((m1.Qualitative_morphology_type == \"DBC\").sum()))\n''', tags=[\"claim:fig5a-dbc-two-ttypes\"])\nmd(\"**Result: ...**\")\n\nmd('''## figs7a-dbc-regions\n\n> Six of seven DBCs in SST CALB1 come from temporal cortex and three of four DBCs in SST ADGRG6 from frontal cortex.\n\nRegion from the `lobe` column (the NWB files carry no region; see the data check). Over all DBCs and, as a variant, those with an NWB file in the dandiset.''')\ncode(r'''\ndbc_yes[\"lobe\"] = cells_meta.loc[dbc_yes.Tube_id, \"lobe\"].values\ndbc_yes[\"nwb_session\"] = cells_meta.loc[dbc_yes.Tube_id, \"nwb_session\"].values\ndbc_yes[\"in_dandiset\"] = dbc_yes.nwb_session.isin(R.session)\nprint(pd.crosstab(dbc_yes.Tree_first_cl, dbc_yes.lobe, margins=True))\nprint(\"with an NWB file in the dandiset:\"); print(pd.crosstab(dbc_yes[dbc_yes.in_dandiset].Tree_first_cl, dbc_yes[dbc_yes.in_dandiset].lobe, margins=True))\nca = dbc_yes[dbc_yes.Tree_first_cl.str.contains(\"CALB1\")]; ad = dbc_yes[dbc_yes.Tree_first_cl.str.contains(\"ADGRG6\")]\nmeas_regions = [int((ca.lobe == \"TemL\").sum()), len(ca), int((ad.lobe == \"FroL\").sum()), len(ad)]\nprint(\"RESULT figs7a-regions:\", meas_regions, \"expected [6, 7, 3, 4]\")\n''', tags=[\"claim:figs7a-dbc-regions\"])\nmd(\"**Result: ...**\")\n\nmd('''## figs7a-dbc-markers\n\n> Most DBCs strongly express CALB1, only one expresses CALB2, all but one express some SST, and TAC1, NOS1 and NPY expression is mixed.\n\n\"Strong\" is log2(CPM + 1) > 5 (the criterion's choice); detected is > 0.''')\ncode(r'''\nG = X.loc[[\"CALB1\", \"CALB2\", \"SST\", \"TAC1\", \"NOS1\", \"NPY\"], dbc_yes.Tube_id].T\nG.index = dbc_yes.cell_name_label + \" | \" + dbc_yes.Tree_first_cl.str.replace(\"Inh \", \"\")\nprint(G.round(2).to_string())\nn = len(G)\nstrong_calb1 = int((G.CALB1 > 5).sum()); calb2 = int((G.CALB2 > 0).sum()); sst = int((G.SST > 0).sum())\nmixed = {gname: int((G[gname] > 0).sum()) for gname in [\"TAC1\", \"NOS1\", \"NPY\"]}\nprint(f\"DBCs {n}: CALB1 > 5 in {strong_calb1}; CALB2 > 0 in {calb2}; SST > 0 in {sst}; detected TAC1/NOS1/NPY {mixed}\")\nprint(\"CALB1 > 3 (variant):\", int((G.CALB1 > 3).sum()), \"| CALB1 > 7:\", int((G.CALB1 > 7).sum()))\nok = strong_calb1 > n / 2 and calb2 == 1 and sst == n - 1 and all(0 < v < n for v in mixed.values())\nprint(\"RESULT figs7a-markers:\", ok)\n''', tags=[\"claim:figs7a-dbc-markers\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig4d-calb1-genes-by-morphology\n\n> A UMAP on 253 genes differentially expressed between DBC, MC and sparse SST neurons splits SST CALB1 neurons into three clusters that largely separate the morphology types.\n\nMain reading, the Methods (case iv): pairwise t tests (Seurat's `t`, a Welch test) between DBC, MC and sparse SST cells of SST CALB1, Bonferroni over all genes, adjusted p < 0.05, union of the three pairs. Cells read as (1) all SST CALB1 cells with a morphology call, (2) the culture microglial ones (the code's chunk). Variant, the code's chunk: one-against-rest t tests on the culture microglial cells with genes of median >= 1, counted at Seurat FindAllMarkers' default return threshold (p < 0.01); the code also drops its immune and `keepGenes` lists, which need data not in the repository. Morphology calls are `morpho_call` with the code's fix (cell 893655882 and \"SMC\" are sparse SST). The UMAP and clusters are run in Python (umap-learn, Louvain of networkx), not Seurat.''')\ncode(r'''\nmpc = metaP.copy()\nmpc[\"morpho_call\"] = mpc[\"morpho_call\"].astype(str)\nmpc.loc[mpc.spec_id.astype(str) == \"893655882\", \"morpho_call\"] = \"SMC\"\nmpc.loc[mpc.morpho_call == \"SMC\", \"morpho_call\"] = \"Sparse SST\"\nmpc[\"topLeaf\"] = mpc.topLeaf_label.astype(str).str.split(\" \\\\(\").str[0]\ncalb = mpc[mpc.topLeaf == \"Inh L1-3 SST CALB1\"]\nprint(\"SST CALB1 cells\", len(calb), \"| morphology calls:\", calb.morpho_call.value_counts().to_dict(),\n      \"| condition2 of called cells:\", calb[calb.morpho_call.isin([\"DBC\", \"MC\", \"Sparse SST\"])].condition2.value_counts().to_dict())\ntypes = [\"DBC\", \"MC\", \"Sparse SST\"]\ndef pairwise_de(cols_by_type):\n    gs = set()\n    out = {}\n    ng = X.shape[0]\n    for i in range(3):\n        for j in range(i + 1, 3):\n            A_, B_ = X[cols_by_type[types[i]]].values, X[cols_by_type[types[j]]].values\n            if A_.shape[1] < 2 or B_.shape[1] < 2:\n                out[(types[i], types[j])] = None\n                continue\n            with np.errstate(all=\"ignore\"):\n                t_, p_ = stats.ttest_ind(A_, B_, axis=1, equal_var=False)\n            p_ = np.where(np.isfinite(p_), p_, 1.0)\n            sig = X.index[np.minimum(p_ * ng, 1) < 0.05]\n            out[(types[i], types[j])] = len(sig)\n            gs |= set(sig)\n    return gs, out\ncols1 = {t_: calb[calb.morpho_call == t_].patched_cell_container.tolist() for t_ in types}\ncols2 = {t_: calb[(calb.morpho_call == t_) & calb.condition2.astype(str).str.contains(\"immune|microglial\")].patched_cell_container.tolist() for t_ in types}\nDE = {}\nfor name, cols in [(\"1 all called cells\", cols1), (\"2 culture microglial\", cols2)]:\n    gs, per = pairwise_de(cols)\n    DE[name] = gs\n    print(f\"reading {name}: cells {[len(cols[t_]) for t_ in types]}, per pair {per}, union {len(gs)}\")\nc3 = sum(cols2.values(), [])\nXc = X[c3]\nXc = Xc[Xc.median(axis=1) >= 1]\nlab3 = np.array([t_ for t_ in types for _ in cols2[t_]])\nvar = set()\nfor t_ in types:\n    with np.errstate(all=\"ignore\"):\n        _, p_ = stats.ttest_ind(Xc.values[:, lab3 == t_], Xc.values[:, lab3 != t_], axis=1, equal_var=False)\n    var |= set(Xc.index[np.nan_to_num(p_, nan=1) < 0.01])\nprint(\"variant (code's chunk, one against rest, p < 0.01, genes median >= 1):\", len(var), \"genes\")\nRES_253 = {k: len(v) for k, v in DE.items()}\nRES_253[\"variant\"] = len(var)\n''', tags=[\"claim:fig4d-calb1-genes-by-morphology\"])\ncode(r'''\nimport umap, networkx as nx\nfrom sklearn.decomposition import PCA\nfrom sklearn.neighbors import kneighbors_graph\ndef clusters_on(genes, npcs, nnb, sd):\n    Z = X.loc[sorted(genes), calb.patched_cell_container].T\n    Z = (Z - Z.mean()) / Z.std(ddof=0).replace(0, np.nan)\n    Z = Z.fillna(0).clip(-10, 10)\n    pcs = PCA(n_components=min(npcs, Z.shape[0] - 1, Z.shape[1]), random_state=sd).fit_transform(Z)\n    emb = umap.UMAP(n_neighbors=nnb, random_state=sd).fit_transform(pcs)\n    Gk = nx.from_scipy_sparse_array(kneighbors_graph(emb, 20 if len(emb) > 20 else len(emb) - 1, include_self=False))\n    comms = nx.community.louvain_communities(Gk, resolution=1, seed=sd)\n    lab = np.zeros(len(emb), int)\n    for ci, cm in enumerate(comms):\n        lab[list(cm)] = ci\n    return lab\nmc_ = calb.morpho_call.values\nfor name, genes, npcs, nnb in [(\"main, reading 1 genes, 30 PCs\", DE[\"1 all called cells\"], 30, 15),\n                               (\"variant genes, 6 PCs, 5 neighbours\", var, 6, 5)]:\n    if len(genes) < 3:\n        print(name, \": too few genes\"); continue\n    for off in SEED_OFFSETS:\n        lab = clusters_on(genes, npcs, nnb, seed(\"fig4d-calb1-genes-by-morphology\") + off)\n        tab = pd.crosstab(mc_, lab).loc[types]\n        major = tab.idxmax(axis=1)\n        frac = (tab.max(axis=1) / tab.sum(axis=1)).round(2)\n        sep = major.nunique() == 3 and (frac > 0.5).all()\n        print(f\"{name} seed+{off}: clusters {len(set(lab))}, majority cluster {major.to_dict()}, fraction {frac.to_dict()}, separated {sep}\")\n''', tags=[\"claim:fig4d-calb1-genes-by-morphology\"])\nmd(\"**Result: ...**\")\n\n# ---------------- PVALB WFDC2 acute vs culture\nmd('''## PVALB WFDC2, acute against culture\n\nThe electrophysiology claims below use the features computed here from the NWB files, labelled through cell-metadata-link.''')\ncode(r'''\nW = E[E.ttype == \"Inh L2-4 PVALB WFDC2\"].copy()\nprint(\"PVALB WFDC2 cells with a QC-passing long square sweep:\", W.condition.value_counts().to_dict(),\n      \"| by condition2\", W.condition2.value_counts().to_dict(), \"| donors\", W.Donor.nunique())\nMW_W = L.mannwhitney_table(W, FEATS, \"condition\", \"acute\", \"culture\")\nprint(\"features tested\", len(MW_W), \"| significant at BH-FDR < 0.05 across these features:\", int((MW_W.p_fdr < 0.05).sum()))\n''')\n\nmd('''## figs2b-wfdc2-ephys-43-of-84\n\n> In PVALB WFDC2 neurons, 43 of 84 electrophysiological features differ between the acute and culture paradigms.\n\nPer feature a two-sided Mann-Whitney, BH-FDR across features, at FDR p < 0.05. Only the features public IPFX computes are measured here. The count over all 84 is bounded: the missing features add at most their number to the count, and they change the BH adjustment of the others; the bounds take them all non-significant (p = 1) or all significant (p = 0).''')\ncode(r'''\np = MW_W.p.dropna().values\nn_missing = len(FEATS84) - len(p)\ndef bh_count(pvals):\n    return int((L.bh(pvals) < 0.05).sum())\nlo = bh_count(np.concatenate([p, np.ones(n_missing)]))\nhi = bh_count(np.concatenate([p, np.zeros(n_missing)]))\nown = bh_count(p)\nprint(f\"features with a test here {len(p)}; missing from the 84: {n_missing}\")\nprint(f\"significant over the features computed (BH over them): {own} of {len(p)} ({own / len(p):.1%}); paper 43 of 84 ({43/84:.1%})\")\nprint(f\"bounds for the count over 84: {lo} to {hi}; tolerance 38.7 to 47.3\")\nJ84 = W[[\"specimen_id_x\", \"condition\"]].merge(fx_paper, left_on=\"specimen_id_x\", right_on=\"specimen_id\")\nmw_paper = L.mannwhitney_table(J84, FEATS84, \"condition\", \"acute\", \"culture\")\nprint(\"variant, on the paper's own table for the same cells (all 84):\", int((mw_paper.p_fdr < 0.05).sum()), \"| all 93:\",\n      int((L.mannwhitney_table(J84, FEATS84 + L.CHIRP, \"condition\", \"acute\", \"culture\").p_fdr < 0.05).sum()))\nmix = MW_W[[\"feature\", \"p\"]].set_index(\"feature\").p.reindex(FEATS84)\nmix = mix.fillna(mw_paper.set_index(\"feature\").p)\nprint(\"variant, computed features with the paper's values for the missing ones:\", bh_count(mix.dropna().values))\nfor c2 in [\"culture\", \"culture_microglial\"]:\n    sub = W[W.condition2.isin([\"acute\", \"acute_microglial\", c2])]\n    t2 = L.mannwhitney_table(sub, FEATS, \"condition\", \"acute\", \"culture\")\n    print(f\"variant, culture cells restricted to {c2}: {int((t2.p_fdr < 0.05).sum())} of {len(t2)}\")\ninside = 38.7 <= lo and hi <= 47.3\noutside = hi < 38.7 or lo > 47.3\nprint(\"RESULT figs2b:\", \"inside\" if inside else (\"outside\" if outside else \"undecided\"), (lo, hi))\n''', tags=[\"claim:figs2b-wfdc2-ephys-43-of-84\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig1l-width-sag-differ\n\n> In PVALB WFDC2 neurons AP width and sag differ between acute and culture slices (sag is higher in culture), while interspike interval and input resistance do not.\n\nTwo-sided Mann-Whitney, BH-FDR across the features computed (the 84 cannot all be computed). Width read as rheo, hero, short square and ramp; ISI as mean_isi_rheo and mean_isi_hero.''')\ncode(r'''\nt = MW_W.set_index(\"feature\")\nshow = [\"sag\", \"width_rheo\", \"width_hero\", \"width_short_square\", \"width_ramp\", \"mean_isi_rheo\", \"mean_isi_hero\", \"input_resistance\"]\nprint(t.loc[show, [\"n_a\", \"n_b\", \"median_a\", \"median_b\", \"p\", \"p_fdr\", \"rbc\"]].to_string(float_format=lambda v: f\"{v:.4g}\"))\nsag_ok = t.loc[\"sag\", \"p_fdr\"] < 1e-4 and t.loc[\"sag\", \"median_b\"] > t.loc[\"sag\", \"median_a\"]\noutcomes = {}\nfor w in [\"width_rheo\", \"width_hero\", \"width_short_square\", \"width_ramp\"]:\n    for isi in [\"mean_isi_rheo\", \"mean_isi_hero\"]:\n        outcomes[(w, isi)] = bool(sag_ok and t.loc[w, \"p_fdr\"] < 1e-4 and t.loc[isi, \"p_fdr\"] >= 0.05 and t.loc[\"input_resistance\", \"p_fdr\"] >= 0.05)\nprint(\"sag higher in culture at FDR p < 1e-4:\", bool(sag_ok))\nfor k, v in outcomes.items():\n    print(k, v, \"| width direction culture/acute median ratio %.2f\" % (t.loc[k[0], \"median_b\"] / t.loc[k[0], \"median_a\"]))\nfor d in sorted(W.Donor.unique())[:0]:\n    pass\nprint(\"by condition and donor count: acute donors\", W[W.condition == \"acute\"].Donor.nunique(), \"culture donors\", W[W.condition == \"culture\"].Donor.nunique())\nprint(\"RESULT fig1l: all readings\", all(outcomes.values()), \"| any\", any(outcomes.values()))\n''', tags=[\"claim:fig1l-width-sag-differ\"])\nmd(\"**Result: ...**\")\n\nmd('''## figs2c-no-change-with-days\n\n> The features that differ in culture already differ at 2 days in culture and do not change with further days in culture.\n\nPearson's correlation of sag and of AP width with days in culture over culture PVALB WFDC2 cells, BH over the two; and the 2 DIC cells against the acute median.''')\ncode(r'''\nWc = W[W.condition == \"culture\"]\nacute_med = W[W.condition == \"acute\"][[\"sag\"] + [\"width_rheo\", \"width_hero\", \"width_short_square\", \"width_ramp\"]].median()\nprint(\"culture PVALB WFDC2 cells by days in culture:\", Wc.Days_In_culture.value_counts().sort_index().to_dict())\nprint(\"all 2 DIC cells in the dandiset:\", E[E.Days_In_culture == 2][[\"ttype\", \"subclass\"]].values.tolist())\nres = {}\nfor w in [\"width_rheo\", \"width_hero\", \"width_short_square\", \"width_ramp\"]:\n    ps, rs = [], []\n    for f in [\"sag\", w]:\n        d = Wc[[f, \"Days_In_culture\"]].dropna()\n        r, p = stats.pearsonr(d.Days_In_culture, d[f]); ps.append(p); rs.append(r)\n    pf = L.bh(ps)\n    res[w] = dict(r_sag=rs[0], p_sag=pf[0], r_width=rs[1], p_width=pf[1])\nprint(pd.DataFrame(res).T.round(4))\nearly = Wc[Wc.Days_In_culture == Wc.Days_In_culture.min()]\nprint(\"earliest DIC among culture PVALB WFDC2:\", int(Wc.Days_In_culture.min()), \"cells\", len(early))\nfor f in [\"sag\", \"width_rheo\", \"width_hero\", \"width_short_square\", \"width_ramp\"]:\n    print(f\"  {f}: earliest-DIC median {early[f].median():.4g}, acute median {acute_med[f]:.4g}, culture median {Wc[f].median():.4g}\")\nfor f in MW_W[MW_W.p_fdr < 0.05].feature:\n    pass\nsigf = MW_W[MW_W.p_fdr < 0.05].feature.tolist()\npp = []\nfor f in sigf:\n    d = Wc[[f, \"Days_In_culture\"]].dropna()\n    pp.append(stats.pearsonr(d.Days_In_culture, d[f])[1] if len(d) > 2 and d[f].nunique() > 1 else np.nan)\nprint(f\"variant, all {len(sigf)} differing features: significant correlations with DIC at BH < 0.05:\", int((L.bh(pp) < 0.05).sum()))\n''', tags=[\"claim:figs2c-no-change-with-days\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig1i-wfdc2-ephys-umap-overlap\n\n> In electrophysiology UMAP space of all 84 features, acute and culture PVALB WFDC2 neurons occupy a similar space.\n\nAll cells, the computed features z-scored with missing values at the median; for each PVALB WFDC2 cell, the fraction of its 15 nearest PVALB WFDC2 neighbours from the other condition, against 1000 label shuffles; in feature space and in a default umap-learn embedding.''')\ncode(r'''\nZ_all = L.zscore_impute(E[FEATS])\ndef cross_fraction(Xs, lab, mask, k):\n    qidx, nb = L.neighbour_fraction(Xs, lab, k, among=mask, query=mask)\n    own = lab[qidx]\n    frac = np.array([np.mean(n != o) for n, o in zip(nb, own)])\n    return {g_: frac[own == g_].mean() for g_ in np.unique(own)}\ndef overlap_test(Xs, lab, mask, k, rng, nshuf=1000):\n    obs = cross_fraction(Xs, lab, mask, k)\n    labm = lab.copy()\n    null = {g_: [] for g_ in obs}\n    idx = np.where(mask)[0]\n    for _ in range(nshuf):\n        labm[idx] = rng.permutation(lab[idx])\n        cf = cross_fraction(Xs, labm, mask, k)\n        for g_ in obs:\n            null[g_].append(cf[g_])\n    return {g_: (obs[g_], np.median(null[g_])) for g_ in obs}\nlabW = E.condition.values\nmaskW = (E.ttype == \"Inh L2-4 PVALB WFDC2\").values\nOUT_1i = {}\nfor off in SEED_OFFSETS:\n    sd = seed(\"fig1i-wfdc2-ephys-umap-overlap\") + off\n    emb = L.umap_embed(Z_all, sd)\n    rng = np.random.default_rng(seed(\"fig1i-wfdc2-ephys-umap-overlap\", 1) + off)\n    for space, Xs in [(\"features\", Z_all.values), (\"umap\", emb)]:\n        for k in ([15, 10, 30] if off == 0 else [15]):\n            r_ = overlap_test(Xs, labW, maskW, k, rng, nshuf=1000 if k == 15 else 200)\n            OUT_1i[(off, space, k)] = r_\n            print(f\"seed+{off} {space:8s} k={k}: \" + \", \".join(f\"{g_} cross {o:.3f} vs shuffle median {n:.3f} (ratio {o/n:.2f})\" for g_, (o, n) in r_.items()))\nholds = {key: all(o >= 0.5 * n for o, n in v.values()) for key, v in OUT_1i.items() if key[2] == 15}\nprint(\"criterion holds (k=15, both spaces) per seed offset:\", {off: holds[(off, \"features\", 15)] and holds[(off, \"umap\", 15)] for off in SEED_OFFSETS})\n''', tags=[\"claim:fig1i-wfdc2-ephys-umap-overlap\"])\nmd(\"**Result: ...**\")\n\n# ---------------- subclasses\nmd('''## fig2b-ephys-umap-subclasses\n\n> The four GABAergic subclasses are separable in electrophysiology feature space, with PVALB neurons occupying the most distinct region.\n\nFor each cell, the fraction of its 15 nearest neighbours of its own subclass (`Revised_subclass_label`), in feature space and a default umap-learn embedding.''')\ncode(r'''\nlabS = E.subclass.values\nshare = pd.Series(labS).value_counts(normalize=True)\nOUT_2b = {}\nfor off in SEED_OFFSETS:\n    emb = L.umap_embed(Z_all, seed(\"fig2b-ephys-umap-subclasses\") + off)\n    for space, Xs in ([(\"features\", Z_all.values)] if off == 0 else []) + [(\"umap\", emb)]:\n        qidx, nb = L.neighbour_fraction(Xs, labS, 15)\n        same = pd.Series([np.mean(n == labS[q]) for q, n in zip(qidx, nb)]).groupby(labS[qidx]).mean()\n        tab = pd.DataFrame({\"same_fraction\": same, \"share\": share, \"excess\": same - share})\n        ok = bool((tab.excess >= 0.2).all() and tab.same_fraction.idxmax() == \"PVALB\")\n        OUT_2b[(off, space)] = ok\n        print(f\"seed+{off} {space}: ok={ok}\"); print(tab.round(3).to_string())\nprint(\"by subclass, cells:\", pd.Series(labS).value_counts().to_dict())\n''', tags=[\"claim:fig2b-ephys-umap-subclasses\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig2f-ap-kinetics\n\n> APs of the PVALB subclass have the fastest kinetics, and LAMP5/PAX6 APs have the highest peak amplitude of the four subclasses.\n\nKruskal-Wallis with Dunn's post hoc (BH-FDR over pairs); short square features first, rheobase sweep second.''')\ncode(r'''\nSUBS = [\"LAMP5/PAX6/Other\", \"VIP\", \"SST\", \"PVALB\"]\ndef kd_report(df, f, gcol, groups):\n    p, dunn, med = L.kruskal_dunn(df, f, gcol, groups)\n    print(f\"--- {f}: KW p={p:.3g}\"); print(med.T.round(5).to_string()); print(\"Dunn FDR p:\"); print(dunn.map(lambda v: f\"{v:.2g}\").to_string())\n    return p, dunn, med\nres2f = {}\nfor sw in [\"short_square\", \"rheo\"]:\n    ok = True\n    for f, best, how in [(f\"width_{sw}\", \"PVALB\", \"min\"), (f\"upstroke_downstroke_ratio_{sw}\", \"PVALB\", \"min\"), (f\"peak_deltav_{sw}\", \"LAMP5/PAX6/Other\", \"max\")]:\n        p, dunn, med = kd_report(E, f, \"subclass\", SUBS)\n        m_ = med[\"median\"]\n        top_ = m_.idxmin() if how == \"min\" else m_.idxmax()\n        pair_ok = all(dunn.loc[best, o] < 0.05 for o in SUBS if o != best)\n        print(f\"  extreme group {top_} (expected {best}); Dunn p < 0.05 against every other: {pair_ok}\")\n        ok &= (top_ == best) and pair_ok\n        res2f[(sw, f)] = (top_ == best, pair_ok)\n    print(\"reading\", sw, \"holds:\", ok)\n''', tags=[\"claim:fig2f-ap-kinetics\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig2g-sag-by-subclass\n\n> LAMP5/PAX6 and VIP neurons have minimal sag compared with PVALB and SST neurons.''')\ncode(r'''\np, dunn, med = kd_report(E, \"sag\", \"subclass\", SUBS)\nm_ = med[\"median\"]\npairs = [(a_, b_) for a_ in [\"LAMP5/PAX6/Other\", \"VIP\"] for b_ in [\"PVALB\", \"SST\"]]\nok = all(m_[a_] < m_[b_] and dunn.loc[a_, b_] < 0.05 for a_, b_ in pairs)\nprint({f\"{a_} vs {b_}\": (round(m_[a_], 3), round(m_[b_], 3), float(dunn.loc[a_, b_])) for a_, b_ in pairs})\nprint(\"by condition (acute / culture) medians:\"); print(E.groupby([\"subclass\", \"condition\"]).sag.median().unstack().round(3))\nprint(\"RESULT fig2g:\", ok)\n''', tags=[\"claim:fig2g-sag-by-subclass\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig2h-several-features-distinct\n\n> Several additional electrophysiological features differ between the subclasses.\n\nKruskal-Wallis across subclasses for every computed feature, BH-FDR across features; counted outside width, upstroke/downstroke ratio, peak and sag features.''')\ncode(r'''\nrows = []\nfor f in FEATS:\n    d = E[[f, \"subclass\"]].dropna()\n    samples = [d[d.subclass == s][f].values for s in SUBS]\n    if min(len(s) for s in samples) < 2 or d[f].nunique() < 2:\n        continue\n    rows.append(dict(feature=f, p=stats.kruskal(*samples).pvalue))\nkw = pd.DataFrame(rows); kw[\"p_fdr\"] = L.bh(kw.p)\nexcl = kw.feature.str.contains(\"width|upstroke_downstroke_ratio|peak_deltav|sag\")\nother = kw[~excl & (kw.p_fdr < 0.05)].sort_values(\"p_fdr\")\nprint(\"features tested\", len(kw), \"| significant\", int((kw.p_fdr < 0.05).sum()), \"| outside width/ratio/peak/sag:\", len(other))\nn_dunn = 0\nfor f in other.feature:\n    _, dunn, _ = L.kruskal_dunn(E, f, \"subclass\", SUBS)\n    n_dunn += int((dunn.values[np.triu_indices(4, 1)] < 0.05).any())\nprint(\"of these, with at least one Dunn pair p < 0.05:\", n_dunn)\nprint(other.head(15).to_string(float_format=lambda v: f\"{v:.3g}\"))\n''', tags=[\"claim:fig2h-several-features-distinct\"])\nmd(\"**Result: ...**\")\n\n# ---------------- FRZB\nmd('''## fig3c-frzb-ephys-with-pvalb\n\n> Most SST FRZB neurons colocalize with the PVALB subclass in electrophysiology space.\n\nGroups: SST (`subclass_label` SST, not SST FRZB), PVALB (not SST FRZB), SST FRZB (t-type). Features z-scored over SST and PVALB cells; for each SST FRZB cell, its 15 nearest SST or PVALB neighbours.''')\ncode(r'''\nfrz = E.ttype == \"Inh L2-4 SST FRZB\"\nF3 = E[E.subclass_label.isin([\"SST\", \"PVALB\"])].copy()\nF3[\"grp\"] = np.where(F3.ttype == \"Inh L2-4 SST FRZB\", \"SST FRZB\", F3.subclass_label)\nprint(\"groups:\", F3.grp.value_counts().to_dict())\nZ3 = L.zscore_impute(F3[FEATS])\nlab3g = F3.grp.values\nfor off in SEED_OFFSETS:\n    emb = L.umap_embed(Z3, seed(\"fig3c-frzb-ephys-with-pvalb\") + off)\n    for space, Xs in ([(\"features\", Z3.values)] if off == 0 else []) + [(\"umap\", emb)]:\n        qidx, nb = L.neighbour_fraction(Xs, lab3g, 15, among=lab3g != \"SST FRZB\", query=lab3g == \"SST FRZB\")\n        pv_frac = np.array([np.mean(n == \"PVALB\") for n in nb])\n        print(f\"seed+{off} {space}: SST FRZB cells {len(pv_frac)}, with a PVALB majority {int((pv_frac > 0.5).sum())} ({(pv_frac > 0.5).mean():.2f}), \"\n              f\"mean PVALB fraction {pv_frac.mean():.2f}; PVALB share of reference {np.mean(lab3g[lab3g != 'SST FRZB'] == 'PVALB'):.2f}\")\n''', tags=[\"claim:fig3c-frzb-ephys-with-pvalb\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig3e-frzb-ap-like-pvalb\n\n> The AP upstroke/downstroke ratio and AP width of SST FRZB neurons align with fast-spiking PVALB neurons and differ from SST neurons.\n\nKruskal-Wallis over the three groups, Dunn's post hoc (BH-FDR); rheobase, short square and rheobase + 40 pA (hero) sweeps.''')\ncode(r'''\nG3 = [\"SST\", \"SST FRZB\", \"PVALB\"]\nres3e = {}\nfor sw in [\"rheo\", \"short_square\", \"hero\"]:\n    for f in [f\"upstroke_downstroke_ratio_{sw}\", f\"width_{sw}\"]:\n        p, dunn, med = kd_report(F3, f, \"grp\", G3)\n        m_ = med[\"median\"]\n        nearer = abs(m_[\"SST FRZB\"] - m_[\"PVALB\"]) < abs(m_[\"SST FRZB\"] - m_[\"SST\"])\n        res3e[f] = (bool(dunn.loc[\"SST FRZB\", \"SST\"] < 1e-4), bool(nearer), float(dunn.loc[\"SST FRZB\", \"PVALB\"]))\n        print(f\"  FRZB vs SST p<1e-4: {res3e[f][0]}; FRZB nearer PVALB: {nearer}; FRZB vs PVALB p={res3e[f][2]:.3g}\")\nprint(\"RESULT fig3e:\", all(v[0] and v[1] for v in res3e.values()), res3e)\n''', tags=[\"claim:fig3e-frzb-ap-like-pvalb\"])\nmd(\"**Result: ...**\")\n\nmd('''## figs6-sst-features-acute-culture\n\n> The upstroke/downstroke ratio and AP width of SST subclass neurons do not differ between acute and culture recordings.\n\nA claim of absence: two-sided Mann-Whitney, acute against culture, BH-FDR over the two features of a sweep reading; SST (`subclass_label`) with and without SST FRZB.''')\ncode(r'''\nanyd = False\nfor with_frzb in [True, False]:\n    S6 = E[(E.subclass_label == \"SST\") & (with_frzb | (E.ttype != \"Inh L2-4 SST FRZB\"))]\n    for sw in [\"rheo\", \"short_square\", \"hero\"]:\n        tt = L.mannwhitney_table(S6, [f\"upstroke_downstroke_ratio_{sw}\", f\"width_{sw}\"], \"condition\", \"acute\", \"culture\")\n        anyd |= bool((tt.p_fdr < 0.05).any())\n        print(f\"SST {'with' if with_frzb else 'without'} FRZB, {sw}:\"); print(tt[[\"feature\", \"n_a\", \"n_b\", \"median_a\", \"median_b\", \"p\", \"p_fdr\", \"rbc\"]].to_string(float_format=lambda v: f\"{v:.4g}\"))\nprint(\"RESULT figs6: any difference\", anyd)\n''', tags=[\"claim:figs6-sst-features-acute-culture\"])\nmd(\"**Result: ...**\")\n\n# ---------------- SST CALB1\nmd('''## fig4c-calb1-ephys-by-morphology\n\n> Within SST CALB1, sparse SST neurons tend to have lower sag, higher adaptation ratio and slightly delayed AP onset than DBCs and MCs, and MCs have the highest AP peak.\n\nSST CALB1 cells with a qualitative morphology type and a file here. Adaptation ratio is `isi_adapt_ratio` (the Methods' first-to-third spike ISI ratio as computed in the helper; its agreement with the paper's table is in cell-metadata-link); `adapt_hero` is shown as a variant only.''')\ncode(r'''\nC4 = E[(E.ttype == \"Inh L1-3 SST CALB1\") & E.Qualitative_morphology_type.notna()].copy()\nC4[\"mt\"] = C4.Qualitative_morphology_type\nprint(\"cells by type:\", C4.mt.value_counts().to_dict(), \"| metadata (all, with or without a file):\",\n      m1[m1.Transcriptomic_type == \"Inh L1-3 SST CALB1\"].Qualitative_morphology_type.value_counts().to_dict())\ncols = [\"sag\", \"isi_adapt_ratio\", \"latency_rheo\", \"latency_hero\", \"peak_deltav_rheo\", \"peak_deltav_hero\", \"adapt_hero\"]\nprint(C4[[\"specimen_id_x\", \"mt\"] + cols].sort_values(\"mt\").to_string(float_format=lambda v: f\"{v:.4g}\"))\nmed4 = C4.groupby(\"mt\")[cols].median()\nprint(med4.round(4).to_string())\nsp_, dbc_, mc_ = \"Sparse SST\", \"DBC\", \"MC\"\nst = {\n    \"sag lower\": bool(med4.loc[sp_, \"sag\"] < min(med4.loc[dbc_, \"sag\"], med4.loc[mc_, \"sag\"])),\n    \"adaptation higher\": bool(med4.loc[sp_, \"isi_adapt_ratio\"] > max(med4.loc[dbc_, \"isi_adapt_ratio\"], med4.loc[mc_, \"isi_adapt_ratio\"])),\n    \"latency higher (rheo)\": bool(med4.loc[sp_, \"latency_rheo\"] > max(med4.loc[dbc_, \"latency_rheo\"], med4.loc[mc_, \"latency_rheo\"])),\n    \"latency higher (hero)\": bool(med4.loc[sp_, \"latency_hero\"] > max(med4.loc[dbc_, \"latency_hero\"], med4.loc[mc_, \"latency_hero\"])),\n    \"MC peak highest (rheo)\": bool(med4[\"peak_deltav_rheo\"].idxmax() == mc_),\n    \"MC peak highest (hero)\": bool(med4[\"peak_deltav_hero\"].idxmax() == mc_),\n}\nprint(st)\nprint(\"variant, adapt_hero (adaptation index): sparse higher than DBC and MC:\",\n      bool(med4.loc[sp_, \"adapt_hero\"] > max(med4.loc[dbc_, \"adapt_hero\"], med4.loc[mc_, \"adapt_hero\"])))\nJc = C4[[\"specimen_id_x\", \"mt\"]].merge(fx_paper[[\"specimen_id\", \"isi_adapt_ratio\"]], left_on=\"specimen_id_x\", right_on=\"specimen_id\")\nprint(\"variant, the paper's own isi_adapt_ratio values for these cells, medians:\", Jc.groupby(\"mt\").isi_adapt_ratio.median().round(3).to_dict())\nfor f in [\"sag\", \"isi_adapt_ratio\", \"latency_rheo\", \"peak_deltav_rheo\"]:\n    d = C4[[f, \"mt\"]].dropna()\n    groups = [d[d.mt == t_][f].values for t_ in d.mt.unique() if (d.mt == t_).sum() > 0]\n    print(f\"  KW {f}: p={stats.kruskal(*groups).pvalue:.3g}\")\n''', tags=[\"claim:fig4c-calb1-ephys-by-morphology\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig5c-dbc-higher-sag\n\n> A higher sag ratio is a consistent and prominent feature of all DBCs.\n\nDBCs from `dbc_calb1_ADGRG6.csv`. Comparison (a) the other cells of SST CALB1 and SST ADGRG6, (b) MC and sparse SST cells of SST CALB1.''')\ncode(r'''\nE[\"is_dbc\"] = E.patched_cell_container.isin(dbc_yes.Tube_id)\ntwo = E[E.ttype.isin([\"Inh L1-3 SST CALB1\", \"Inh L3-5 SST ADGRG6\"])]\ndbc_e = two[two.is_dbc]\nprint(\"DBCs with a file and sag:\", int(dbc_e.sag.notna().sum()), \"of\", len(dbc_yes), \"| sag values\", dbc_e.sag.round(3).tolist(), dbc_e.ttype.str[4:].tolist())\ncomp_a = two[~two.is_dbc]\ncomp_b = E[(E.ttype == \"Inh L1-3 SST CALB1\") & E.Qualitative_morphology_type.isin([\"MC\", \"Sparse SST\"])]\nfor name, cmp_ in [(\"a\", comp_a), (\"b\", comp_b)]:\n    cm = cmp_.sag.median(); dm = dbc_e.sag.median()\n    u, p = stats.mannwhitneyu(dbc_e.sag.dropna(), cmp_.sag.dropna(), alternative=\"two-sided\")\n    print(f\"reading {name}: comparison n={cmp_.sag.notna().sum()} median {cm:.3f}; DBC median {dm:.3f}; DBCs above comparison median \"\n          f\"{int((dbc_e.sag > cm).sum())} of {int(dbc_e.sag.notna().sum())}; Mann-Whitney p={p:.3g}\")\n''', tags=[\"claim:fig5c-dbc-higher-sag\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig5d-dbc-ephys-intermingled\n\n> In electrophysiology space, DBCs of the SST CALB1 and SST ADGRG6 types are intermingled with other SST neurons.\n\nSST subclass cells (`subclass_label`), features z-scored over them; for each DBC, the fraction of its 10 nearest SST neighbours that are DBCs.''')\ncode(r'''\nS5 = E[E.subclass_label == \"SST\"].copy()\nZ5 = L.zscore_impute(S5[FEATS]); lab5 = np.where(S5.is_dbc, \"DBC\", \"other\")\nshare5 = np.mean(lab5 == \"DBC\")\nfor off in SEED_OFFSETS:\n    emb = L.umap_embed(Z5, seed(\"fig5d-dbc-ephys-intermingled\") + off)\n    for space, Xs in ([(\"features\", Z5.values)] if off == 0 else []) + [(\"umap\", emb)]:\n        qidx, nb = L.neighbour_fraction(Xs, lab5, 10, query=lab5 == \"DBC\")\n        fr = np.array([np.mean(n == \"DBC\") for n in nb])\n        print(f\"seed+{off} {space}: DBCs {len(fr)}, mean DBC fraction among 10 neighbours {fr.mean():.3f}; DBC share {share5:.3f}; \"\n              f\"ratio {fr.mean() / share5:.2f}; holds {fr.mean() <= 2 * share5}\")\n''', tags=[\"claim:fig5d-dbc-ephys-intermingled\"])\nmd(\"**Result: ...**\")\n\nmd('''## figs5-vip-enhancer-enrichment\n\n> Neurons labelled with the VIP enhancer AAV CN2039 did not map only to VIP types but were strongly enriched for VIP types.\n\nBy `Revised_subclass_label`; comparison (a) all cells without CN2039, (b) CN1390-only cells; two-sided Fisher exact test (the criterion's choice). Over all labelled cells, and over those with a file in the dandiset as a variant.''')\ncode(r'''\nfor name, M in [(\"all labelled cells\", m1), (\"cells with a file here\", m1[m1.nwb_session.isin(R.session)])]:\n    vip = M.Revised_subclass_label == \"VIP\"\n    cn = M.Virus == \"CN2039\"\n    print(f\"{name}: CN2039 cells {int(cn.sum())}, VIP among them {int((vip & cn).sum())} ({(vip & cn).sum() / cn.sum():.2f}); subclasses\",\n          M[cn].Revised_subclass_label.value_counts().to_dict())\n    for rd, other in [(\"a\", ~cn), (\"b\", M.Virus == \"CN1390\")]:\n        tab = [[int((vip & cn).sum()), int((~vip & cn).sum())], [int((vip & other).sum()), int((~vip & other).sum())]]\n        o, p = stats.fisher_exact(tab)\n        print(f\"  reading {rd}: comparison VIP fraction {tab[1][0] / sum(tab[1]):.3f} (n={sum(tab[1])}), odds ratio {o:.2f}, Fisher p={p:.3g}\")\n''', tags=[\"claim:figs5-vip-enhancer-enrichment\"])\nmd(\"**Result: ...**\")\n\n# ---------------- morphology (elsewhere)\nmd('''## Morphology features (elsewhere)\n\nThe morphology claims are `data: elsewhere`. They are tested on the paper's morphology feature table (`LeeDalley_morpho_features.csv`, 140 reconstructions, at commit 5eb357a); the features are not recomputed from the reconstructions at the Brain Image Library.''')\ncode(r'''\nMF = morph.drop(columns=[c for c in morph.columns if c.startswith(\"Unnamed\")]).merge(\n    m1, left_on=\"specimen_id\", right_on=\"specimen_id_x\", how=\"left\")\nMFEATS = [c for c in morph.columns if c not in (\"specimen_id\",) and not c.startswith(\"Unnamed\")]\nprint(\"reconstructions\", len(MF), \"| labelled\", int(MF.specimen_id_x.notna().sum()), \"| features\", len(MFEATS))\nprint(\"by subclass:\", MF.Revised_subclass_label.value_counts().to_dict())\nprint(\"soma depth range (um):\", MF.soma_aligned_dist_from_pia.min().round(1), MF.soma_aligned_dist_from_pia.max().round(1))\n''', tags=[\"sanity\"])\n\nmd('''## fig1g-wfdc2-morphology-unchanged\n\n> Fifty morphological features of depth-matched PVALB WFDC2 neurons do not differ between culture (n = 9) and acute (n = 10) slices.\n\nMann-Whitney per feature, BH over the 50 features (the 51 columns less soma depth, used for matching). Readings: (a) all PVALB WFDC2 reconstructions, (b) depth-matched, here the cells inside the depth range both groups share, (c) nearest-depth pairs.''')\ncode(r'''\nMW_ = MF[MF.Transcriptomic_type == \"Inh L2-4 PVALB WFDC2\"].copy()\nF50 = [c for c in MFEATS if c != \"soma_aligned_dist_from_pia\"]\nprint(\"PVALB WFDC2 reconstructions:\", MW_.condition.value_counts().to_dict(), \"| features\", len(F50))\nprint(MW_.groupby(\"condition\").soma_aligned_dist_from_pia.describe().round(1))\nlo_d = MW_.groupby(\"condition\").soma_aligned_dist_from_pia.min().max(); hi_d = MW_.groupby(\"condition\").soma_aligned_dist_from_pia.max().min()\nrb = MW_[MW_.soma_aligned_dist_from_pia.between(lo_d, hi_d)]\ncu = MW_[MW_.condition == \"culture\"]; ac = MW_[MW_.condition == \"acute\"].copy()\npick = []\nfor _, r_ in cu.sort_values(\"soma_aligned_dist_from_pia\").iterrows():\n    j = (ac.soma_aligned_dist_from_pia - r_.soma_aligned_dist_from_pia).abs().drop(pick, errors=\"ignore\").idxmin(); pick.append(j)\nrc = pd.concat([cu, ac.loc[pick]])\nfor name, d in [(\"a all\", MW_), (\"b shared depth range\", rb), (\"c nearest-depth pairs\", rc)]:\n    tt = L.mannwhitney_table(d, F50, \"condition\", \"acute\", \"culture\")\n    print(f\"reading {name}: acute {int((d.condition == 'acute').sum())}, culture {int((d.condition == 'culture').sum())}; \"\n          f\"features with FDR p < 0.05: {int((tt.p_fdr < 0.05).sum())}; smallest FDR p {tt.p_fdr.min():.3g}; smallest raw p {tt.p.min():.3g} ({tt.loc[tt.p.idxmin(), 'feature']})\")\n''', tags=[\"claim:fig1g-wfdc2-morphology-unchanged\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig2c-morph-umap-subclasses\n\n> The four subclasses are separable in morphological feature space, PVALB the most distinct.\n\nAs fig2b-ephys-umap-subclasses on the morphology features of the 140 reconstructed neurons.''')\ncode(r'''\nZM = L.zscore_impute(MF[MFEATS]); labM = MF.Revised_subclass_label.values\nshareM = pd.Series(labM).value_counts(normalize=True)\nfor off in SEED_OFFSETS:\n    emb = L.umap_embed(ZM, seed(\"fig2c-morph-umap-subclasses\") + off)\n    for space, Xs in ([(\"features\", ZM.values)] if off == 0 else []) + [(\"umap\", emb)]:\n        qidx, nb = L.neighbour_fraction(Xs, labM, 15)\n        same = pd.Series([np.mean(n == labM[q]) for q, n in zip(qidx, nb)]).groupby(labM[qidx]).mean()\n        tab = pd.DataFrame({\"same_fraction\": same, \"share\": shareM, \"excess\": same - shareM})\n        ok = bool((tab.excess >= 0.2).all() and tab.same_fraction.idxmax() == \"PVALB\")\n        print(f\"seed+{off} {space}: ok={ok}\"); print(tab.round(3).to_string())\n''', tags=[\"claim:fig2c-morph-umap-subclasses\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig2e-lamp5-shortest-extent\n\n> LAMP5/PAX6 neurons have the shortest soma-to-branch-tip Euclidean distance for both axon and dendrite.''')\ncode(r'''\nMF[\"subclass\"] = MF.Revised_subclass_label\nfor f in [\"axon_max_euclidean_distance\", \"basal_dendrite_max_euclidean_distance\"]:\n    p, dunn, med = kd_report(MF, f, \"subclass\", SUBS)\n    print(f\"  lowest median: {med['median'].idxmin()}\")\n''', tags=[\"claim:fig2e-lamp5-shortest-extent\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig3g-frzb-morphology-like-pvalb\n\n> SST FRZB neurons overlap more with PVALB than with SST neurons in morphology space, their horizontal axon extent and axon versus dendrite earth mover's distance resemble PVALB basket cells, and in co-clustering they fall more often into PVALB-dominated types.\n\nKruskal-Wallis with Dunn (BH-FDR) for `axon_extent_x` and `axon_emd_with_basal_dendrite`; co-clustering as the Methods (95% subsamples, shared nearest neighbour graph, fast-greedy, 500 resamplings, Ward linkage on the co-clustering matrix, cut at six clusters), with 10 and 20 graph neighbours. A cluster is PVALB- or SST-dominated by the majority `subclass_label` of its cells other than SST FRZB.''')\ncode(r'''\nM3 = MF[MF.subclass_label.isin([\"SST\", \"PVALB\"])].copy()\nM3[\"grp\"] = np.where(M3.Transcriptomic_type == \"Inh L2-4 SST FRZB\", \"SST FRZB\", M3.subclass_label)\nprint(\"groups:\", M3.grp.value_counts().to_dict())\nr3g = {}\nfor f in [\"axon_extent_x\", \"axon_emd_with_basal_dendrite\"]:\n    p, dunn, med = kd_report(M3, f, \"grp\", G3)\n    m_ = med[\"median\"]\n    r3g[f] = (bool(abs(m_[\"SST FRZB\"] - m_[\"PVALB\"]) < abs(m_[\"SST FRZB\"] - m_[\"SST\"])), float(dunn.loc[\"SST\", \"SST FRZB\"]))\nprint(\"nearer PVALB, Dunn SST vs FRZB p:\", r3g)\nimport igraph as ig\nfrom scipy.cluster.hierarchy import linkage, fcluster\nfrom scipy.spatial.distance import squareform\nZ3m = L.zscore_impute(M3[MFEATS]).values\ndef snn_fastgreedy(Xs, k):\n    from sklearn.neighbors import NearestNeighbors\n    _, ind = NearestNeighbors(n_neighbors=k + 1).fit(Xs).kneighbors(Xs)\n    sets = [set(r) for r in ind]\n    edges, w = [], []\n    for i in range(len(Xs)):\n        for j in ind[i][1:]:\n            if i < j or i not in ind[j]:\n                s = len(sets[i] & sets[j]) / len(sets[i] | sets[j])\n                if s > 0 and (min(i, j), max(i, j)) not in edges:\n                    edges.append((min(i, j), max(i, j))); w.append(s)\n    g_ = ig.Graph(n=len(Xs), edges=edges); g_.es[\"weight\"] = w\n    return np.array(g_.community_fastgreedy(weights=\"weight\").as_clustering().membership)\nfor off in SEED_OFFSETS:\n    rng = np.random.default_rng(seed(\"fig3g-frzb-morphology-like-pvalb\") + off)\n    for k in [10, 20]:\n        n = len(Z3m); co = np.zeros((n, n)); both = np.zeros((n, n))\n        for _ in range(500):\n            idx = np.sort(rng.choice(n, int(round(0.95 * n)), replace=False))\n            lab_ = snn_fastgreedy(Z3m[idx], k)\n            same = (lab_[:, None] == lab_[None, :]).astype(float)\n            co[np.ix_(idx, idx)] += same; both[np.ix_(idx, idx)] += 1\n        C = co / np.maximum(both, 1)\n        dist = 1 - C; np.fill_diagonal(dist, 0)\n        cl = fcluster(linkage(squareform(dist, checks=False), \"ward\"), 6, \"maxclust\")\n        M3[\"cl\"] = cl\n        dom = M3[M3.grp != \"SST FRZB\"].groupby(\"cl\").subclass_label.agg(lambda s: s.value_counts().idxmax() if len(s) else \"none\")\n        fz = M3[M3.grp == \"SST FRZB\"].cl.map(dom).fillna(\"none\").value_counts().to_dict()\n        if off == 0:\n            print(f\"k={k}:\"); print(pd.crosstab(M3.cl, M3.grp))\n        print(f\"seed+{off} k={k}: SST FRZB cells by cluster dominance {fz}\")\n''', tags=[\"claim:fig3g-frzb-morphology-like-pvalb\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig1h-wfdc2-morph-umap-overlap\n\n> In morphological UMAP space, culture and acute PVALB WFDC2 neurons occupy similar space in the PVALB-rich portion.\n\nThe measure of fig1i-wfdc2-ephys-umap-overlap with 5 neighbours on all reconstructions (z-scored morphology features); PVALB-rich part: most of each PVALB WFDC2 cell's 5 nearest neighbours among all cells are PVALB, for most cells of each group. Groups: all PVALB WFDC2 reconstructions, and the shared-depth subset of fig1g.''')\ncode(r'''\nlabC = MF.condition.values\nlabSub = MF.Revised_subclass_label.values\nfor setname, ids in [(\"all PVALB WFDC2\", MW_.specimen_id), (\"shared depth range\", rb.specimen_id)]:\n    maskM = MF.specimen_id.isin(ids).values\n    for off in SEED_OFFSETS:\n        emb = L.umap_embed(ZM, seed(\"fig1h-wfdc2-morph-umap-overlap\") + off)\n        rng = np.random.default_rng(seed(\"fig1h-wfdc2-morph-umap-overlap\", 1) + off)\n        for space, Xs in ([(\"features\", ZM.values)] if off == 0 else []) + [(\"umap\", emb)]:\n            ov = overlap_test(Xs, labC, maskM, 5, rng)\n            qidx, nb = L.neighbour_fraction(Xs, labSub, 5, query=maskM)\n            pv = np.array([np.mean(n == \"PVALB\") for n in nb]) > 0.5\n            rich = {g_: pv[labC[qidx] == g_].mean() for g_ in [\"acute\", \"culture\"]}\n            ok = all(o >= 0.5 * n_ for o, n_ in ov.values()) and all(v > 0.5 for v in rich.values())\n            print(f\"{setname} seed+{off} {space}: \" + \", \".join(f\"{g_} cross {o:.2f} vs shuffle {n_:.2f}\" for g_, (o, n_) in ov.items())\n                  + f\"; PVALB-majority fraction {({k: round(v, 2) for k, v in rich.items()})}; holds {ok}\")\n''', tags=[\"claim:fig1h-wfdc2-morph-umap-overlap\"])\nmd(\"**Result: ...**\")\n\nmd('''## fig5d-dbc-morph-umap\n\n> In morphological UMAP space, DBCs of the SST CALB1 and SST ADGRG6 types cluster near each other.\n\nSST subclass reconstructions (`subclass_label`), z-scored; for each DBC, the fraction of its 5 nearest SST neighbours that are DBCs; reproduced when the mean is at least twice the DBC share.''')\ncode(r'''\nMS = MF[MF.subclass_label == \"SST\"].copy()\nMS[\"is_dbc\"] = MS.patched_cell_container.isin(dbc_yes.Tube_id)\nZS = L.zscore_impute(MS[MFEATS]); labD = np.where(MS.is_dbc, \"DBC\", \"other\"); shareD = np.mean(labD == \"DBC\")\nttD = MS.Transcriptomic_type.values\nprint(\"SST reconstructions\", len(MS), \"| DBCs among them\", int(MS.is_dbc.sum()))\nfor off in SEED_OFFSETS:\n    emb = L.umap_embed(ZS, seed(\"fig5d-dbc-morph-umap\") + off)\n    for space, Xs in ([(\"features\", ZS.values)] if off == 0 else []) + [(\"umap\", emb)]:\n        qidx, nb = L.neighbour_fraction(Xs, labD, 5, query=labD == \"DBC\")\n        fr = np.array([np.mean(n == \"DBC\") for n in nb])\n        _, nbt = L.neighbour_fraction(Xs, ttD, 5, among=labD == \"DBC\", query=labD == \"DBC\")\n        own_tt = np.mean([np.mean(n == ttD[q]) for q, n in zip(qidx, nbt)])\n        print(f\"seed+{off} {space}: mean DBC fraction {fr.mean():.3f}, share {shareD:.3f}, ratio {fr.mean() / shareD:.2f}, holds {fr.mean() >= 2 * shareD}; \"\n              f\"own t-type among DBC neighbours {own_tt:.2f}\")\n''', tags=[\"claim:fig5d-dbc-morph-umap\"])\nmd(\"**Result: ...**\")\n\nmd(open(os.path.join(os.path.dirname(__file__), \"nb_summary.md\")).read())\ncode(r'''\nprint(f\"notebook runtime {(time.time() - T0) / 60:.1f} min; peak memory of this process {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n''')\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_cells_part2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/lee-2023; cat >> lee2023.py <<'E'


# --- transcriptomes (the paper's code repository) ----------------------------------------------

def transcriptomes():
    """The Patch-seq expression matrices of the code repository (log2(CPM + 1), genes x cells,
    columns named by tube id) and the per-cell table stored with them (metaPatch)."""
    import tempfile
    import rdata
    parts, meta = [], None
    for k in (1, 2):
        url = f"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/data/complete_patchseq_data_sets{k}.RData"
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        with tempfile.NamedTemporaryFile(suffix=".RData") as tmp:  # rdata reads from a path; removed on close
            tmp.write(r.content)
            tmp.flush()
            conv = rdata.conversion.convert(rdata.parser.parse_file(tmp.name))
        d = conv[f"datPatch{k}"]
        parts.append(pd.DataFrame(np.asarray(d.values), index=[str(g) for g in d.coords["dim_0"].values],
                                  columns=[str(c) for c in d.coords["dim_1"].values]))
        if "metaPatch" in conv:
            meta = conv["metaPatch"]
    X = pd.concat(parts, axis=1)
    meta = meta.copy()
    meta.columns = [str(c) for c in meta.columns]
    return X, meta
E
sed -i 's/calb.condition2.astype(str).str.contains("immune|microglial")/calb.condition2.astype(str).str.match(r"culture.*(immune|microglial)")/' $TMPDIR/nb_cells_part2.py; grep -n 'str.match' $TMPDIR/nb_cells_part2.py; $TMPDIR/dev/bin/python -c "
import rdata
c=rdata.conversion.convert(rdata.parser.parse_file('$TMPDIR/repo/complete_patchseq_data_sets2.RData'))
mp=c['metaPatch']; print(mp.condition2.value_counts(dropna=False)); print(mp.morpho_call.value_counts(dropna=False).head(10)); print(mp.patched_cell_container.head(2).tolist())"
```

```
254:cols2 = {t_: calb[(calb.morpho_call == t_) & calb.condition2.astype(str).str.match(r"culture.*(immune|microglial)")].patched_cell_container.tolist() for t_ in types}
condition2
culture           287
acute             181
culture_immune    180
acute_immune      130
Name: count, dtype: Int64
morpho_call
          758
DBC        11
MC          4
SMC         4
Basket      1
Name: count, dtype: Int64
['P1S4_170214_008_A01', 'P5S4_170509_207_A01']
```

**Agent calls Bash**

```bash
cd $TMPDIR; echo "# header placeholder" > nb_header.md; echo "## Summary placeholder" > nb_summary.md; dev/bin/python build_nb.py --dev $TMPDIR/dev_nb.ipynb && cp entries/lee-2023/lee2023.py $TMPDIR/ && cd $TMPDIR && date -u && LEE_CACHE=$TMPDIR/feat.pkl timeout 2400 dev/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=2000 dev_nb.ipynb --output dev_out.ipynb 2>&1 | tail -2; date -u
```

```
wrote --dev 114 cells
Wed Nov 18 09:52:42 UTC 2026
To see all available configurables, use `--help-all`.

Wed Nov 18 09:52:44 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i 's/^out = sys.argv\[1\]/out = sys.argv[-1]/' build_nb.py; rm -f ./--dev; dev/bin/python build_nb.py --dev $TMPDIR/dev_nb.ipynb && date -u && LEE_CACHE=$TMPDIR/feat.pkl timeout 2400 dev/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=2000 dev_nb.ipynb --output dev_out.ipynb 2>&1 | tail -2; date -u
```

```
wrote /tmp/claude-1001/dev_nb.ipynb 114 cells
Wed Nov 18 09:52:47 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 162838 bytes to dev_out.ipynb
Wed Nov 18 09:55:21 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > dump.py <<'E'
import nbformat, sys
nb=nbformat.read(sys.argv[1],4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': 
        if c.source.startswith('## '): print('\n#####', c.source.split('\n')[0])
        continue
    for o in c.get('outputs',[]):
        if o.output_type=='stream': print(o.text[:int(sys.argv[2]) if len(sys.argv)>2 else 6000])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue[:300])
        elif 'text/plain' in o.get('data',{}): print(o['data']['text/plain'][:2000])
E
dev/bin/python dump.py dev_out.ipynb 2>&1 | head -300
```

```
##### ## Data
version 0.241120.0510 assets 706 subjects 109 sessions 706 total GB 24.47
archive summary: {'numberOfFiles': 706, 'numberOfSubjects': 109, 'numberOfCells': 616}
metadata rows 779 unique specimens 778 | feature table rows 704 | feature columns 93 of which chirp 9 -> 84 = 84


##### ## Feature extraction
of the 84 features, 65 computed; 19 not computed by public IPFX: ['adp_v_last_rheo', 'ahp_delay_ratio_5spike', 'ahp_delay_ratio_hero', 'postap_slope_hero', 'postap_slope_ramp', 'postap_slope_rheo', 'postap_slope_short_square', 'sag_area', 'sag_area_depol', 'sag_depol', 'sag_peak_t', 'sag_peak_t_depol', 'sag_tau', 'trough_slowdeltav_hero', 'trough_slowdeltav_rheo', 'width_suprathresh_hero', 'width_suprathresh_ramp', 'width_suprathresh_rheo', 'width_suprathresh_short_square']
files with a read error: 0
error_long_square 16 {'FeatureError': 11, 'ValueError': 5}
error_short_square 4 {'FeatureError': 4}
labelled files 690 | with a QC-passing long square sweep 686 | with rheobase 675 | with sag 675


##### ## Data check
Files and subjects
  files 706 subjects (sub- folders) 109 | subject_id in file equals folder: True | session_id equals file name: True
  species strings: {'Homo Sapiens': 581, 'Homo sapiens': 125} | institution: {'Allen Institute for Brain Science': 706}
  archive summary says numberOfCells 616 for 706 files, one cell per file
Sampling rates of the analysed sweeps (Hz): {'[50000.0]': 625, '[200000.0]': 78, '[]': 1, '[25000.0, 50000.0]': 1, '[50000.0, 200000.0]': 1}
[... 279 more lines not kept]
```

**Agent**

Most sections run. Fixing three errors (column name, networkx, gene-count definition) and reading the remaining outputs.

**Agent calls Bash**

```bash
cd $TMPDIR; uv pip install -q --python dev/bin/python networkx 2>&1|tail -1; head -2 repo/vgic_genes.csv; dev/bin/python dump.py dev_out.ipynb 2>&1 | sed -n '300,600p'
```

```
Type,Family name,Target name,HGNC symbol
vgic,Voltage-gated calcium channels  (Ca<sub>V</sub>),Ca<sub>v</sub>1.1,CACNA1S


##### ## fig2b-ephys-umap-subclasses
seed+0 features: ok=False
                  same_fraction  share  excess
LAMP5/PAX6/Other          0.428  0.093   0.335
PVALB                     0.848  0.529   0.319
SST                       0.454  0.230   0.223
VIP                       0.341  0.147   0.193
seed+0 umap: ok=False
                  same_fraction  share  excess
LAMP5/PAX6/Other          0.377  0.093   0.284
PVALB                     0.881  0.529   0.352
SST                       0.429  0.230   0.198
VIP                       0.398  0.147   0.251

seed+1000 umap: ok=True
                  same_fraction  share  excess
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; dev/bin/python dump.py dev_out.ipynb 2>&1 | sed -n '600,900p'; dev/bin/python -c "
import sys; sys.path.insert(0,'.')
import lee2023 as L, numpy as np
X,mp=L.transcriptomes()
m=L.metadata_table().drop_duplicates().set_index('patched_cell_container').loc[X.columns]
for th in [0, 0.5, 1, 2, 3, np.log2(2), np.log2(11)]:
    c=(X>th).sum(0).values; print(th, np.mean(c==m.Genes_Detected.values), np.median(np.abs(c-m.Genes_Detected.values)))
print(mp['Genes.Detected'].head().tolist(), m.Genes_Detected.head().tolist())
"
```

```
##### ## fig5c-dbc-higher-sag
DBCs with a file and sag: 8 of 11 | sag values [0.412, 0.376, 0.564, 0.465, 0.481, 0.544, 0.363, 0.573, nan] ['L1-3 SST CALB1', 'L1-3 SST CALB1', 'L3-5 SST ADGRG6', 'L1-3 SST CALB1', 'L1-3 SST CALB1', 'L1-3 SST CALB1', 'L3-5 SST ADGRG6', 'L1-3 SST CALB1', 'L3-5 SST ADGRG6']
reading a: comparison n=73 median 0.389; DBC median 0.473; DBCs above comparison median 6 of 8; Mann-Whitney p=0.0276
reading b: comparison n=7 median 0.358; DBC median 0.473; DBCs above comparison median 8 of 8; Mann-Whitney p=0.0721


##### ## fig5d-dbc-ephys-intermingled
seed+0 features: DBCs 9, mean DBC fraction among 10 neighbours 0.133; DBC share 0.039; ratio 3.42; holds False
seed+0 umap: DBCs 9, mean DBC fraction among 10 neighbours 0.133; DBC share 0.039; ratio 3.42; holds False

seed+1000 umap: DBCs 9, mean DBC fraction among 10 neighbours 0.156; DBC share 0.039; ratio 3.99; holds False

seed+2000 umap: DBCs 9, mean DBC fraction among 10 neighbours 0.089; DBC share 0.039; ratio 2.28; holds False

seed+3000 umap: DBCs 9, mean DBC fraction among 10 neighbours 0.122; DBC share 0.039; ratio 3.14; holds False

seed+4000 umap: DBCs 9, mean DBC fraction among 10 neighbours 0.089; DBC share 0.039; ratio 2.28; holds False


##### ## figs5-vip-enhancer-enrichment
[... 203 more lines not kept]
```

**Agent**

Results so far are mostly in. Fixing figs2d (column is "HGNC symbol"), then checking whether the mouse comparison data (Gouwens et al. 2020) are reachable in the time left.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i 's/vgic\["HGNC.symbol"\]/vgic["HGNC symbol"]/' nb_cells_part2.py; curl -s https://api.dandiarchive.org/api/dandisets/000020/ | python3 -c "import json,sys;d=json.load(sys.stdin);v=d['most_recent_published_version'];print(v['version'],v['name'],v['asset_count'],v['size'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000020/versions/0.210913.1639/" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d.get('description','')[:1500]);print(d.get('relatedResource'))" 2>/dev/null | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
p='build_nb.py'; s=open(p).read()
s=s.replace('''print("Days in culture of culture cells:"''','''key = ["v_baseline", "rheobase_i", "input_resistance", "tau", "sag", "width_short_square", "threshold_i_ramp"]
kk = R[key].round(6).astype(str).agg("|".join, axis=1)
dup = R[R[key].notna().sum(1) >= 4][kk[R[key].notna().sum(1) >= 4].duplicated(keep=False)]
print("Deposited twice? files sharing identical values of", key, ":", len(dup), dup.session.tolist())
print("  files with the same file size:", int(R["size"].duplicated(keep=False).sum()))
print("Days in culture of culture cells:"''')
s=s.replace('''print("files counted", len(E), "| sum of expected", sum(exp.values()))''','''print("files counted", len(E), "| sum of expected", sum(exp.values()))
print("variant, cells with a rheobase computed here:", int(E.rheobase_i.notna().sum()), E[E.rheobase_i.notna()].Revised_subclass_label.value_counts().to_dict(),
      "| subclass_label:", E[E.rheobase_i.notna()].subclass_label.value_counts().to_dict())''')
open(p,'w').write(s)
p='nb_cells_part2.py'; s=open(p).read()
s=s.replace('''print("variant (code's chunk, one against rest, p < 0.01, genes median >= 1):", len(var), "genes")''','''print("variant (code's chunk, one against rest, p < 0.01, genes median >= 1):", len(var), "genes")
n_rows = 0
for t_ in types:
    pct_in = (Xc.values[:, lab3 == t_] > 0).mean(1); pct_out = (Xc.values[:, lab3 != t_] > 0).mean(1)
    with np.errstate(all="ignore"):
        _, p_ = stats.ttest_ind(Xc.values[:, lab3 == t_], Xc.values[:, lab3 != t_], axis=1, equal_var=False)
    n_rows += int(((np.nan_to_num(p_, nan=1) < 0.01) & (np.maximum(pct_in, pct_out) >= 0.1)).sum())
print("  as FindAllMarkers counts rows (a gene once per type), with its default min.pct 0.1:", n_rows)''')
open(p,'w').write(s)
E
dev/bin/python build_nb.py --dev $TMPDIR/dev_nb.ipynb && LEE_CACHE=$TMPDIR/feat.pkl timeout 2400 dev/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=2000 dev_nb.ipynb --output dev_out.ipynb 2>&1 | tail -1; dev/bin/python dump.py dev_out.ipynb 2>&1 | grep -n -A12 "Deposited\|variant, cells with a rheobase\|figs2d\|##### ## fig4d\|ERROR" | head -90
```

```
wrote /tmp/claude-1001/dev_nb.ipynb 114 cells
[NbConvertApp] Writing 169359 bytes to dev_out.ipynb
61:ERROR TypeError sequence item 5: expected str instance, float found
62-
63-##### ## cell-metadata-link
64-metadata rows 779 (one duplicated row: 1 ) -> unique rows 778
65-Has_ephys rows 704 | with nwb_id 690 | found in the dandiset 684 (97.2%)
66-  Has_ephys rows without nwb_id: 14 | nwb_id not in the dandiset: 6
67-rows without Has_ephys whose nwb_id is in the dandiset: 6
68-NWB files without a metadata row: 16 | their sessions: ['567737666', '567773605', '569870997', '571674350', '591326867', '591342850', '595591210', '595597605', '595715586', '601916346', '611610562', '611822740', '611901143', '847874997', '847908770', '855354224']
69-                    n  within10  median_rel_diff  missing_here  missing_paper
70-feature                                                                      
71-rheobase_i        650     0.922              0.0            12             20
72-input_resistance  650     0.945              0.0            12             20
73-sag               650     0.978              0.0            12             20
--
91:variant, cells with a rheobase computed here: 675 {'PVALB': 358, 'SST': 155, 'VIP': 99, 'LAMP5/PAX6/Other': 63} | subclass_label: {'PVALB': 286, 'SST': 227, 'VIP': 94, 'LAMP5/PAX6/Other': 68}
92-labelled files without a QC-passing long square sweep: 4
93-RESULT composition: reading a all within: False | reading b all within: False
94-
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i 's/kk = R\[key\].round(6).astype(str)/kk = R[key].astype(float).round(6).astype(str)/' build_nb.py; python3 - <<'E'
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
s=s.replace('''nb = nbf.v4.new_notebook()''','''import yaml
RES = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "nb_results.yaml")))
last = None
for c in cells:
    if c.cell_type == "code":
        for t in c.metadata.get("tags", []):
            if t.startswith("claim:"):
                last = t[6:]
    elif c.source.strip() == "**Result: ...**":
        c.source = "**Result: " + RES[last].strip() + "**" if False else "**Result: " + RES[last].strip().split(". ", 1)[0] + ".** " + (RES[last].strip().split(". ", 1)[1] if ". " in RES[last].strip() else "")
nb = nbf.v4.new_notebook()''')
open(p,'w').write(s)
E
grep -n "Result" build_nb.py | head
```

```
173:md("**Result: ...**")
198:md("**Result: ...**")
211:    elif c.source.strip() == "**Result: ...**":
212:        c.source = "**Result: " + RES[last].strip() + "**" if False else "**Result: " + RES[last].strip().split(". ", 1)[0] + ".** " + (RES[last].strip().split(". ", 1)[1] if ". " in RES[last].strip() else "")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
s=s.replace('''        c.source = "**Result: " + RES[last].strip() + "**" if False else "**Result: " + RES[last].strip().split(". ", 1)[0] + ".** " + (RES[last].strip().split(". ", 1)[1] if ". " in RES[last].strip() else "")''','''        head, _, rest = " ".join(RES[last].split()).partition(". ")
        c.source = f"**Result: {head.rstrip('.')}.** {rest}".strip()''')
open(p,'w').write(s)
E
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_results.yaml",
 "content": "cell-metadata-link: >-\n  reproduced. 684 of the 704 rows with electrophysiology (97.2%) have an NWB file, and rheobase,\n  input resistance, sag and width at rheobase computed here are within 10% of the paper's table for\n  92.2%, 94.5%, 97.8% and 98.8% of cells. All four agree together for 90.6% of cells. 16 files have\n  no metadata row, and the metadata table repeats one row. Some features computed here differ from\n  the table more often (isi_adapt_ratio within 10% for 27% of cells, fi_fit_slope 41%), so those\n  definitions are not the paper's.\ndataset-composition: >-\n  partially reproduced. The metadata table holds 778 neurons in 44 t-types, as the paper says.\n  Counted over the files here, reading (a) gives VIP 101, SST 158 and PVALB 363, within tolerance,\n  but LAMP5/PAX6 64 against 75. Reading (b) gives LAMP5/PAX6 69 and VIP 96 within tolerance, and SST\n  231 and PVALB 290 outside it. Cells with a rheobase number 675, the paper's total, but by subclass\n  they are 63, 99, 155 and 358.\nfig1b-more-genes-in-culture: >-\n  reproduced. Culture cells have more genes detected (median 12203 against 11259 genes above 0,\n  p = 4.3e-10; Genes_Detected column 7318 against 6802, p = 1.6e-05).\nfigs1a-genes-across-days: >-\n  reproduced. The median at every day in culture, 2 to 16, is above the acute median (11259), and\n  genes detected do not correlate with days in culture (Pearson r = 0.029, p = 0.54, n = 467).\nfig1d-nms-no-difference: >-\n  reproduced. NMS does not differ (medians 0.962 and 0.962, Mann-Whitney p = 0.38, rank-biserial\n  -0.037).\nfig1c-marker-expression-correlated: >-\n  reproduced, under an assumption. Every reading run gives r > 0 and p < 1e-4, per subclass (r 0.75\n  to 0.97) and pooled (r 0.87 to 0.92). The genes are ranked here in the Patch-seq cells; the\n  snRNA-seq ranking could not be run, as the reference data are not in the repository.\nfigs2d-seven-channel-genes: >-\n  blocked. The code's gene filter needs the dissociated-nuclei data, which the repository does not\n  hold. Without it 142 channel genes are tested, against the paper's 114, and 22 differ at adjusted\n  p <= 0.01. The procedure run is therefore not the paper's, and the count is not compared with 7.\nfig5a-dbc-two-ttypes: >-\n  reproduced. The 11 DBCs are 7 SST CALB1 and 4 SST ADGRG6, and the t-types of the DBC table agree\n  with the tree mapping stored with the transcriptomes and with the metadata table for all 11. The\n  tree mapping was not re-run.\nfigs7a-dbc-regions: >-\n  reproduced. Six of 7 SST CALB1 DBCs are from temporal cortex (one occipital) and 3 of 4 SST ADGRG6\n  DBCs from frontal cortex (one temporal). Two DBCs have no NWB file here. Over the 9 that have one,\n  the counts are 5 of 6 and 2 of 3.\nfigs7a-dbc-markers: >-\n  reproduced. Of 11 DBCs, 7 have CALB1 log2(CPM + 1) > 5, one expresses CALB2, 10 express SST, and\n  TAC1, NOS1 and NPY are detected in 7, 9 and 10. With a cut of 3 for strong CALB1 it is 10 of 11.\nfig4d-calb1-genes-by-morphology: >-\n  not reproduced. The Methods' pairwise t tests with Bonferroni correction find 2 genes over the 15\n  called SST CALB1 cells and none over the 10 culture microglial ones. The code's one-against-rest\n  variant finds 431 genes, or 451 rows counted as FindAllMarkers counts them; none of these is\n  within 228 to 278. The clusters cannot be built on 2 genes. On the variant genes three clusters\n  form, but DBCs do not have a majority cluster of their own under any of the five seeds.\nfigs2b-wfdc2-ephys-43-of-84: >-\n  blocked. 19 of the 84 features need code the paper has not released, so the count over 84 is\n  bounded between 39 and 61 and the tolerance (38.7 to 47.3) lies inside the bounds. Over the 65\n  features computed, 41 differ (63%, against the paper's 51%). On the paper's own table, the same\n  cells give 47 of 84.\nfig1l-width-sag-differ: >-\n  blocked. The readings disagree. Sag is higher in culture (median 0.284 against 0.110,\n  FDR p = 1.2e-14). AP width is wider in culture at FDR p < 1e-4 for the rheobase, hero and short\n  square sweeps, but not the ramp (FDR p = 0.0077). Input resistance does not differ (FDR p = 0.81).\n  The hero-sweep ISI does not differ (FDR p = 0.75), but the rheobase-sweep ISI does (FDR p = 0.016,\n  74 cells).\nfigs2c-no-change-with-days: >-\n  blocked. It depends on fig1l-width-sag-differ, and its own width readings disagree. Sag does not\n  correlate with days in culture (r = 0.07). Width does not correlate for the rheobase, hero and ramp\n  sweeps, but does for the short square (r = 0.37, FDR p = 0.0015). The one 2 DIC PVALB WFDC2 cell\n  has higher sag and wider APs than the acute median, as the culture group does.\nfig1i-wfdc2-ephys-umap-overlap: >-\n  not reproduced. In feature space, a culture PVALB WFDC2 cell has a mean of 0.19 acute cells among\n  its 15 nearest PVALB WFDC2 neighbours, against 0.45 for shuffled labels (ratio 0.43, under the\n  criterion's 0.5). Acute cells have a ratio of 0.72. In the UMAP embedding the ratios are 0.68 to\n  0.78 under all five seeds, which passes. With 30 neighbours the feature-space culture ratio is\n  0.49.\nfig2b-ephys-umap-subclasses: >-\n  not reproduced, narrowly. PVALB has the highest same-subclass fraction (0.85 in feature space,\n  0.87 to 0.88 in UMAP). In feature space the VIP excess over its share is 0.193, under the 0.2 the\n  criterion asks. In the UMAP of the claim's seed the SST excess is 0.198 (above 0.2 under three of\n  the five seeds).\nfig2f-ap-kinetics: >-\n  partially reproduced. PVALB APs have the narrowest width and the lowest upstroke/downstroke ratio,\n  with Dunn's p < 0.05 against every subclass, for both the short square and the rheobase sweep.\n  LAMP5/PAX6 have the highest median peak in both readings, but not significantly against VIP\n  (short square p = 0.08, rheobase p = 0.014) and SST (rheobase p = 0.061).\nfig2g-sag-by-subclass: >-\n  reproduced. The median sag is 0.10 for LAMP5/PAX6 and 0.15 for VIP, against 0.24 for PVALB and\n  0.30 for SST, and all four pairs differ (Dunn's p <= 1.9e-6).\nfig2h-several-features-distinct: >-\n  reproduced. 59 of 65 features differ across subclasses at FDR < 0.05. 44 of them are outside\n  width, ratio, peak and sag, and 43 of those have a significant Dunn pair.\nfig3c-frzb-ephys-with-pvalb: >-\n  reproduced. 72 of 73 SST FRZB cells have a PVALB majority among their 15 nearest SST or PVALB\n  neighbours in feature space, and 69 to 73 in UMAP across the five seeds.\nfig3e-frzb-ap-like-pvalb: >-\n  reproduced. For the rheobase, short square and hero sweeps, SST FRZB differs from SST in width and\n  upstroke/downstroke ratio (Dunn's p 7.6e-12 to 7.2e-09 for width, 2e-19 to 6.4e-11 for the ratio),\n  and its medians are nearer PVALB. SST FRZB still differs from PVALB in width (p 7.8e-05 to 0.0011)\n  but not in the ratio (p 0.067 to 0.88).\nfigs6-sst-features-acute-culture: >-\n  reproduced. Neither feature differs between acute and culture SST cells under any sweep reading,\n  with or without SST FRZB (smallest FDR p 0.22; rank-biserial -0.23 to 0.07).\nfig4c-calb1-ephys-by-morphology: >-\n  reproduced, under an assumption, on 14 cells. Sparse SST cells have the lowest median sag (0.300\n  against 0.473 and 0.509), the highest ISI adaptation ratio (1.75 against 1.14 and 1.37) and the\n  longest latency, and MCs the highest peak, under every reading. The ISI adaptation ratio\n  computed here does not match the paper's definition (27% of cells within 10%). The paper's own\n  values for these cells order the types the same way. No Kruskal-Wallis test of adaptation or\n  latency is significant (p = 0.16 and 0.11).\nfig5c-dbc-higher-sag: >-\n  partially reproduced. The DBC median sag (0.473, 8 DBCs) is above both comparison groups. All 8\n  DBCs are above the median of the MC and sparse SST cells (0.358, reading b). Only 6 of 8 are above\n  the median of the other SST CALB1 and ADGRG6 cells (0.389, reading a; Mann-Whitney p = 0.028).\nfig5d-dbc-ephys-intermingled: >-\n  not reproduced. The 9 DBCs have a mean of 0.133 DBCs among their 10 nearest SST neighbours, 3.4\n  times their share (0.039), in feature space and in UMAP. Over the five seeds the ratio is 2.3 to\n  4.0, above the criterion's 2.\nfigs5-vip-enhancer-enrichment: >-\n  reproduced. 19 of 30 CN2039 cells are VIP (0.63), against 0.138 of other cells (Fisher p = 1.7e-09)\n  and 0.053 of CN1390 cells (p = 1e-14). The other 11 are PVALB, SST or LAMP5/PAX6.\nfig1g-wfdc2-morphology-unchanged: >-\n  reproduced. No morphology feature differs at FDR p < 0.05 between acute and culture PVALB WFDC2\n  cells under any reading (smallest FDR p 0.09 to 0.20). The table holds 16 acute and 10 culture\n  reconstructions, against the paper's 10 and 9.\nfig2c-morph-umap-subclasses: >-\n  not reproduced. PVALB has the highest same-subclass fraction in both spaces (0.78 and 0.73).\n  LAMP5/PAX6 exceed their share by only 0.10 in feature space, and SST by 0.175 in the UMAP of the\n  claim's seed (0.14 to 0.21 over the five seeds).\nfig2e-lamp5-shortest-extent: >-\n  reproduced. LAMP5/PAX6 have the lowest median axon (434 um) and dendrite (171 um) maximum Euclidean\n  distance, with Kruskal-Wallis p = 4.6e-06 and 2.4e-04.\nfig3g-frzb-morphology-like-pvalb: >-\n  reproduced. SST FRZB medians of axon_extent_x (855) and axon_emd_with_basal_dendrite (15.7) are\n  near PVALB (910, 15.8) and differ from SST (Dunn's p 0.0008 and 0.0006). In co-clustering, 12 of 14\n  SST FRZB cells fall in PVALB-dominated clusters, for 10 and 20 neighbours and all five seeds.\nfig1h-wfdc2-morph-umap-overlap: >-\n  reproduced. Acute and culture PVALB WFDC2 reconstructions are mixed (cross-group fractions 0.30\n  to 0.72 against shuffled 0.40 to 0.66). In both readings, both spaces and all five seeds, at\n  least 88% of these cells have a PVALB majority among their 5 nearest neighbours.\nfig5d-dbc-morph-umap: >-\n  reproduced, but seed-sensitive. In feature space DBCs have a mean of 0.78 DBCs among their 5\n  nearest SST neighbours, 3.5 times their share (0.22). In the UMAP of the claim's seed the ratio is\n  2.02, and over the five seeds 1.54 to 2.59, under 2 for two of them.\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_results.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
p='/tmp/claude-1001/nb_results.yaml'; s=open(p).read()
s=s.replace("(Dunn's p 7.6e-12 to 7.2e-09 for width, 2e-19 to 6.4e-11 for the ratio)","(Dunn's p 2e-12 to 7.2e-09 for width, 1.1e-19 to 6.4e-11 for the ratio)")
s=s.replace("""but not significantly against VIP
  (short square p = 0.08, rheobase p = 0.014) and SST (rheobase p = 0.061).""","""but not significantly against VIP
  for the short square (p = 0.08) and against SST for the rheobase sweep (p = 0.061).""")
open(p,'w').write(s)
E
grep -c "p = 0.08" nb_results.yaml; date -u
```

```
1
Wed Nov 18 10:33:15 UTC 2026
Shell cwd was reset to
```

**Agent**

Analyses done on the cached features (10:33 UTC). Writing the notebook header, summary and entry files, then the real run from the archive.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_header.md",
 "content": "# Lee, Dalley et al. (2023) on dandiset 000636\n\nPaper: Lee BR, Dalley R, et al. \"Signature morphoelectric properties of diverse GABAergic interneurons in the human neocortex.\" Science 382, eadf6484 (2023), doi:10.1126/science.adf6484.\n\nDataset: [DANDI:000636](https://dandiarchive.org/dandiset/000636/0.241120.0510), \"Human interneuron patch-seq electrophysiology\", version 0.241120.0510 (doi:10.48324/dandi.000636/0.241120.0510): 706 NWB files, one neuron each, 109 donors, 24.5 GB. This is the only published version; the paper cites no version (its Data and materials availability says only that data \"will be made available through BIL, DANDI, and NeMO\"), so the most recent published version is pinned. Its content equals the draft's (same asset count and size).\n\nClaims: `claims/lee-2023.yaml`, written from the author manuscript of the version of record (PMC12229143) and the bioRxiv preprint (doi:10.1101/2022.11.08.515739). This run had the version-of-record text only (`paper/10.1126-science.adf6484.txt`); its supplementary legends are missing.\n\nLabels and other outside data come from the paper's code repository, [AllenInstitute/human_patchseq_gaba](https://github.com/AllenInstitute/human_patchseq_gaba) at commit 5eb357a1cea246c7c847b5608a8fc7e87ea95b58: the per-cell metadata (labels, matched to files by `nwb_id`), the paper's feature table (used only to check the features computed here), the morphology feature table, the DBC calls, the channel gene list and the transcriptomes. The electrophysiology features are computed from the NWB files with IPFX.\n\n| Claim | Data | Tested here |\n|---|---|---|\n| cell-metadata-link | labels | tested |\n| dataset-composition | labels | tested |\n| fig1b-more-genes-in-culture, figs1a-genes-across-days, fig1d-nms-no-difference, fig1c-marker-expression-correlated | code repository | tested |\n| figs2d-seven-channel-genes | code repository | run; blocked (gene filter needs data not in the repository) |\n| figs1-microglial-signature, fig1e-wfdc2-transcriptome-overlap, figs1de-mapping-unaffected, fig2a-patchseq-overlaps-snrnaseq, fig3-frzb-transcriptome-intermediate | code repository, snRNA-seq | blocked (Seurat in R; snRNA-seq reference) |\n| fig5a-dbc-two-ttypes, figs7a-dbc-regions, figs7a-dbc-markers, fig4d-calb1-genes-by-morphology | labels, code repository | tested |\n| figs2b-wfdc2-ephys-43-of-84, fig1l-width-sag-differ, figs2c-no-change-with-days | dataset | run; blocked (unreleased features; readings disagree) |\n| fig1i, fig2b, fig2f, fig2g, fig2h, fig3c, fig3e, figs6, fig4c, fig5c, fig5d-dbc-ephys-intermingled, figs5 | dataset with labels | tested |\n| fig1g, fig2c, fig2e, fig3g, fig1h, fig5d-dbc-morph-umap | morphology feature table | tested |\n| fig4a-calb1-morphology-types, fig5b-merfish-layers, fig5e-bouton-density, fig6b-species-morphology | reconstructions, MERFISH, images, mouse | blocked |\n| fig6c, fig6e, figs8b, figs9 | mouse data (Gouwens et al. 2020) | blocked |\n\nThe full extraction streams all 706 files and takes about 25 minutes.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_summary.md",
 "content": "## Summary\n\n| Claim | Outcome |\n|---|---|\n| cell-metadata-link | reproduced |\n| dataset-composition | partially reproduced |\n| fig1b-more-genes-in-culture | reproduced |\n| figs1a-genes-across-days | reproduced |\n| fig1d-nms-no-difference | reproduced |\n| fig1c-marker-expression-correlated | reproduced (assumption) |\n| figs2d-seven-channel-genes | blocked (other) |\n| fig5a-dbc-two-ttypes | reproduced |\n| figs7a-dbc-regions | reproduced |\n| figs7a-dbc-markers | reproduced |\n| fig4d-calb1-genes-by-morphology | not reproduced |\n| figs2b-wfdc2-ephys-43-of-84 | blocked (methods underspecified) |\n| fig1l-width-sag-differ | blocked (methods underspecified) |\n| figs2c-no-change-with-days | blocked (methods underspecified) |\n| fig1i-wfdc2-ephys-umap-overlap | not reproduced |\n| fig2b-ephys-umap-subclasses | not reproduced |\n| fig2f-ap-kinetics | partially reproduced |\n| fig2g-sag-by-subclass | reproduced |\n| fig2h-several-features-distinct | reproduced |\n| fig3c-frzb-ephys-with-pvalb | reproduced |\n| fig3e-frzb-ap-like-pvalb | reproduced |\n| figs6-sst-features-acute-culture | reproduced |\n| fig4c-calb1-ephys-by-morphology | reproduced (assumption) |\n| fig5c-dbc-higher-sag | partially reproduced |\n| fig5d-dbc-ephys-intermingled | not reproduced |\n| figs5-vip-enhancer-enrichment | reproduced |\n| fig1g-wfdc2-morphology-unchanged | reproduced |\n| fig2c-morph-umap-subclasses | not reproduced |\n| fig2e-lamp5-shortest-extent | reproduced |\n| fig3g-frzb-morphology-like-pvalb | reproduced |\n| fig1h-wfdc2-morph-umap-overlap | reproduced |\n| fig5d-dbc-morph-umap | reproduced (seed-sensitive) |\n| Seurat, snRNA-seq, MERFISH, bouton, reconstruction and mouse claims (13) | blocked |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.\n\nHow the analysis differs from the paper's. 19 of the 84 electrophysiology features need code the paper has not released, so the multivariate measures use the 65 that public IPFX computes. Cell-level QC (seal, access resistance) is not recomputed. The sweep QC of the Methods is applied. The UMAP claims are judged by the neighbour measures the claims file fixes, not by the paper's plots. The morphology claims use the paper's feature table. Seurat analyses are not run.\n\nWhat was found about the dataset. The files can be linked to the paper's tables through `nwb_id`, and the features computed from them match the paper's table for most cells. 16 files have no row in the paper's metadata, 20 rows with electrophysiology have no file, and the archive's summary gives 616 cells for 706 one-cell files. 80 files are sampled at 200 kHz where the Methods state 50 kHz. The files carry no cell type, region, layer, condition or days in culture, so every label comes from the code repository. Species is written two ways.\n"
}
```

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

**Agent calls Bash**

```bash
rm /tmp/claude-1001/nb_header.md /tmp/claude-1001/nb_summary.md; echo removed
```

```
removed
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_header.md",
 "content": "# Lee, Dalley et al. (2023) on dandiset 000636\n\nPaper: Lee BR, Dalley R, et al. \"Signature morphoelectric properties of diverse GABAergic interneurons in the human neocortex.\" Science 382, eadf6484 (2023), doi:10.1126/science.adf6484.\n\nDataset: [DANDI:000636](https://dandiarchive.org/dandiset/000636/0.241120.0510), \"Human interneuron patch-seq electrophysiology\", version 0.241120.0510 (doi:10.48324/dandi.000636/0.241120.0510): 706 NWB files, one neuron each, 109 donors, 24.5 GB. This is the only published version; the paper cites no version (its Data and materials availability says only that data \"will be made available through BIL, DANDI, and NeMO\"), so the most recent published version is pinned. Its content equals the draft's (same asset count and size).\n\nClaims: `claims/lee-2023.yaml`, written from the author manuscript of the version of record (PMC12229143) and the bioRxiv preprint (doi:10.1101/2022.11.08.515739). This run had the version-of-record text only (`paper/10.1126-science.adf6484.txt`); its supplementary legends are missing.\n\nLabels and other outside data come from the paper's code repository, [AllenInstitute/human_patchseq_gaba](https://github.com/AllenInstitute/human_patchseq_gaba) at commit 5eb357a1cea246c7c847b5608a8fc7e87ea95b58: the per-cell metadata (labels, matched to files by `nwb_id`), the paper's feature table (used only to check the features computed here), the morphology feature table, the DBC calls, the channel gene list and the transcriptomes. The electrophysiology features are computed from the NWB files with IPFX.\n\n| Claim | Data | Tested here |\n|---|---|---|\n| cell-metadata-link | labels | tested |\n| dataset-composition | labels | tested |\n| fig1b-more-genes-in-culture, figs1a-genes-across-days, fig1d-nms-no-difference, fig1c-marker-expression-correlated | code repository | tested |\n| figs2d-seven-channel-genes | code repository | run; blocked (gene filter needs data not in the repository) |\n| figs1-microglial-signature, fig1e-wfdc2-transcriptome-overlap, figs1de-mapping-unaffected, fig2a-patchseq-overlaps-snrnaseq, fig3-frzb-transcriptome-intermediate | code repository, snRNA-seq | blocked (Seurat in R; snRNA-seq reference) |\n| fig5a-dbc-two-ttypes, figs7a-dbc-regions, figs7a-dbc-markers, fig4d-calb1-genes-by-morphology | labels, code repository | tested |\n| figs2b-wfdc2-ephys-43-of-84, fig1l-width-sag-differ, figs2c-no-change-with-days | dataset | run; blocked (unreleased features; readings disagree) |\n| fig1i, fig2b, fig2f, fig2g, fig2h, fig3c, fig3e, figs6, fig4c, fig5c, fig5d-dbc-ephys-intermingled, figs5 | dataset with labels | tested |\n| fig1g, fig2c, fig2e, fig3g, fig1h, fig5d-dbc-morph-umap | morphology feature table | tested |\n| fig4a-calb1-morphology-types, fig5b-merfish-layers, fig5e-bouton-density, fig6b-species-morphology | reconstructions, MERFISH, images, mouse | blocked |\n| fig6c, fig6e, figs8b, figs9 | mouse data (Gouwens et al. 2020) | blocked |\n\nThe full extraction streams all 706 files and takes about 25 minutes.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_summary.md",
 "content": "## Summary\n\n| Claim | Outcome |\n|---|---|\n| cell-metadata-link | reproduced |\n| dataset-composition | partially reproduced |\n| fig1b-more-genes-in-culture | reproduced |\n| figs1a-genes-across-days | reproduced |\n| fig1d-nms-no-difference | reproduced |\n| fig1c-marker-expression-correlated | reproduced (assumption) |\n| figs2d-seven-channel-genes | blocked (other) |\n| fig5a-dbc-two-ttypes | reproduced |\n| figs7a-dbc-regions | reproduced |\n| figs7a-dbc-markers | reproduced |\n| fig4d-calb1-genes-by-morphology | not reproduced |\n| figs2b-wfdc2-ephys-43-of-84 | blocked (methods underspecified) |\n| fig1l-width-sag-differ | blocked (methods underspecified) |\n| figs2c-no-change-with-days | blocked (methods underspecified) |\n| fig1i-wfdc2-ephys-umap-overlap | not reproduced |\n| fig2b-ephys-umap-subclasses | not reproduced |\n| fig2f-ap-kinetics | partially reproduced |\n| fig2g-sag-by-subclass | reproduced |\n| fig2h-several-features-distinct | reproduced |\n| fig3c-frzb-ephys-with-pvalb | reproduced |\n| fig3e-frzb-ap-like-pvalb | reproduced |\n| figs6-sst-features-acute-culture | reproduced |\n| fig4c-calb1-ephys-by-morphology | reproduced (assumption) |\n| fig5c-dbc-higher-sag | partially reproduced |\n| fig5d-dbc-ephys-intermingled | not reproduced |\n| figs5-vip-enhancer-enrichment | reproduced |\n| fig1g-wfdc2-morphology-unchanged | reproduced |\n| fig2c-morph-umap-subclasses | not reproduced |\n| fig2e-lamp5-shortest-extent | reproduced |\n| fig3g-frzb-morphology-like-pvalb | reproduced |\n| fig1h-wfdc2-morph-umap-overlap | reproduced |\n| fig5d-dbc-morph-umap | reproduced (seed-sensitive) |\n| Seurat, snRNA-seq, MERFISH, bouton, reconstruction and mouse claims (13) | blocked |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.\n\nHow the analysis differs from the paper's. 19 of the 84 electrophysiology features need code the paper has not released, so the multivariate measures use the 65 that public IPFX computes. Cell-level QC (seal, access resistance) is not recomputed. The sweep QC of the Methods is applied. The UMAP claims are judged by the neighbour measures the claims file fixes, not by the paper's plots. The morphology claims use the paper's feature table. Seurat analyses are not run.\n\nWhat was found about the dataset. The files can be linked to the paper's tables through `nwb_id`, and the features computed from them match the paper's table for most cells. 16 files have no row in the paper's metadata, 20 rows with electrophysiology have no file, and the archive's summary gives 616 cells for 706 one-cell files. 79 files have sweeps sampled at 200 kHz where the Methods state 50 kHz. The files carry no cell type, region, layer, condition or days in culture, so every label comes from the code repository. Species is written two ways.\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_summary.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/lee-2023; python3 - <<'E'
p='lee2023.py'; s=open(p).read()
s=s.replace('''    sweeps, stim_codes = [], []''','''    meta["general_fields"] = ",".join(sorted(f["general"].keys()))
    ie = f["general/intracellular_ephys"] if "general/intracellular_ephys" in f else {}
    meta["electrode_location"] = ";".join(txt(f"general/intracellular_ephys/{k}/location") or "none"
                                          for k in ie if isinstance(ie[k], h5py.Group))
    sweeps, stim_codes = [], []''')
open(p,'w').write(s)
E
$TMPDIR/dev/bin/python -c "
import lee2023 as L
A=L.assets(); m,s=L.read_cell(A.asset_id[0]); print({k:v for k,v in m.items() if k!='stim_codes'})" 2>&1 | grep -v Warn
python3 - <<'E'
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
s=s.replace('''print("  archive summary says numberOfCells"''','''print("  fields under /general:", R.general_fields.value_counts().to_dict())
print("  electrode location:", R.electrode_location.value_counts().to_dict())
print("  archive summary says numberOfCells"''')
open(p,'w').write(s)
E
```

```
{'session_id': '643599465', 'subject_id': '643488707', 'species': 'Homo Sapiens', 'institution': 'Allen Institute for Brain Science', 'session_start_time': '2017-10-17T17:09:38.139Z', 'general_fields': 'data_collection,devices,generated_by,institution,intracellular_ephys,labnotebook,session_id,source_script,stimsets,subject,testpulse,user_comment', 'electrode_location': 'none;none'}
```

**Agent calls Bash**

```bash
cd  sed -n 565,600p tools/entry.py; grep -n "HARNESS =" -A3 tools/entry.py
```

```
print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
            print(f"error: could not build the environment ({' '.join(cmd[:3])})", file=sys.stderr)
            return 1

    results, failed = [], False
    for notebook in entry["notebooks"]:
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/lee-2023; cat > requirements.in <<'E'
h5py
ipfx
matplotlib
networkx
numpy
pandas
python-igraph
rdata
remfile
requests
scikit-learn
scikit-posthocs
scipy
statsmodels
umap-learn
E
cat > entry.yaml <<'E'
schema_version: 1
name: lee-2023
type: reproduction
title: Human GABAergic interneurons in acute and cultured slices (Lee, Dalley et al. 2023)
description: Tests the findings of Lee, Dalley et al. (2023) on dandiset 000636, which holds the
  Patch-seq electrophysiology of 706 human cortical GABAergic neurons from acute and cultured
  slices. Features are computed from the NWB files with IPFX and labelled through the paper's code
  repository, which also supplies the transcriptomes and morphology features used for the claims
  whose data are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_lee_2023.ipynb
  title: Reproducing Lee, Dalley et al. (2023) from dandiset 000636
  runtime_minutes: 30
helpers:
- lee2023.py
related:
- id: dandi:000636/0.241120.0510
  relation: uses_data
- id: doi:10.1126/science.adf6484
  relation: reproduces
E
cd $TMPDIR && dev/bin/python build_nb.py entries/lee-2023/reproduce_lee_2023.ipynb && cd  && python tools/entry.py lock entries/lee-2023 2>&1 | tail -3; python tools/entry.py check entries/lee-2023 2>&1 | tail -20
```

```
wrote entries/lee-2023/reproduce_lee_2023.ipynb 114 cells
wrote lee-2023/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent**

Entry checks pass. Writing the README before the real run (any later edit to the entry would force a re-run).

**Agent calls Write**

```json
{
 "file_path": "entries/lee-2023/README.md",
 "content": "# Lee, Dalley et al. (2023) from dandiset 000636\n\nTests the findings of [Lee, Dalley et al. (2023)](https://doi.org/10.1126/science.adf6484) on\n[DANDI:000636](https://dandiarchive.org/dandiset/000636/0.241120.0510), which holds the Patch-seq\nelectrophysiology of 706 human cortical GABAergic neurons from acute and cultured slices. The\nfeatures are computed from the NWB files with IPFX. Cell labels, transcriptomes and morphology\nfeatures come from the paper's code repository,\n[AllenInstitute/human_patchseq_gaba](https://github.com/AllenInstitute/human_patchseq_gaba) at commit\n5eb357a, as the files carry no cell type, region or condition.\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\nThe attempt record, with the outcome of each claim, the reasons and the differences from the\npaper's method, is [`attempts/lee-2023-01.yaml`](../../attempts/lee-2023-01.yaml). The notebook streams\nevery file and takes about 30 minutes.\n"
}
```

```
File created successfully at: entries/lee-2023/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  date -u; timeout 4500 python tools/entry.py all entries/lee-2023 2>&1 | tail -15; date -u
```

```
Wed Nov 18 10:34:33 UTC 2026

[36mFile [39m[32m~/work/encore/encore/executed/lee-2023/.venv/lib/python3.13/site-packages/pandas/core/apply.py:1350[39m, in [36mFrameApply.apply_series_generator[39m[34m(self)[39m
[32m   1347[39m results = {}
[32m   1349[39m [38;5;28;01mfor[39;00m i, v [38;5;129;01min[39;00m [38;5;28menumerate[39m(series_gen):
[32m-> [39m[32m1350[39m     results[i] = [30;43mself[39;49m[30;43m.[39;49m[30;43mfunc[39;49m[30;43m([39;49m[30;43mv[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43m*[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43margs[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43m*[39;49m[30;43m*[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mkwargs[39;49m[30;43m)[39;49m
[32m   1351[39m     [38;5;28;01mif[39;00m [38;5;28misinstance[39m(results[i], ABCSeries):
[32m   1352[39m         [38;5;66;03m# If we have a view on v, we need to make a copy because[39;00m
[32m   1353[39m         [38;5;66;03m#  series_generator will swap out the underlying data[39;00m
[32m   1354[39m         results[i] = results[i].copy(deep=[38;5;28;01mFalse[39;00m)

[31mTypeError[39m: sequence item 5: expected str instance, float found


0 error(s)
FAIL  reproduce_lee_2023.ipynb  (1608 s)
Wed Nov 18 11:01:29 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i 's/kk = R\[key\].astype(float).round(6).astype(str).agg("|".join, axis=1)/kk = R[key].astype(float).round(6).fillna(-1e9).map(repr).agg("|".join, axis=1)/' build_nb.py; grep -n "kk = " build_nb.py; dev/bin/python build_nb.py --dev $TMPDIR/dev_nb.ipynb && cp entries/lee-2023/lee2023.py $TMPDIR/ && VPY=executed/lee-2023/.venv/bin/python; $VPY -c "import pandas; print(pandas.__version__)"; LEE_CACHE=$TMPDIR/feat.pkl timeout 1200 $VPY -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1100 --ExecutePreprocessor.kernel_name=registry-lee-2023 dev_nb.ipynb --output dev_out2.ipynb 2>&1 | tail -3
```

```
128:kk = R[key].astype(float).round(6).fillna(-1e9).map(repr).agg("|".join, axis=1)
wrote /tmp/claude-1001/dev_nb.ipynb 114 cells
3.1.1

[31mAttributeError[39m: 'DataFrame' object has no attribute 'general_fields'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
s=s.replace('''R = pd.read_pickle(os.environ["LEE_CACHE"])
''','''R = pd.read_pickle(os.environ["LEE_CACHE"])
for c_ in ["general_fields", "electrode_location"]:
    R[c_] = R.get(c_, "dev")
''')
open(p,'w').write(s)
E
dev/bin/python build_nb.py --dev $TMPDIR/dev_nb.ipynb; VPY=executed/lee-2023/.venv/bin/python; LEE_CACHE=$TMPDIR/feat.pkl JUPYTER_PATH=executed/lee-2023/.venv/share/jupyter timeout 1200 $VPY -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1100 --ExecutePreprocessor.kernel_name=registry-lee-2023 dev_nb.ipynb --output dev_out2.ipynb 2>&1 | tail -3; dev/bin/python dump.py dev_out2.ipynb > dev2.txt; dev/bin/python dump.py dev_out.ipynb > dev1.txt; diff dev1.txt dev2.txt | head -60
```

```
wrote /tmp/claude-1001/dev_nb.ipynb 114 cells
['print("channel genes with adjusted p <= 0.01 (code\'s per-gene Holm):", n_main)', 'print(chan[chan.adj_per_gene <= 0.01].sort_values("adj_per_gene")[["p_condition", "adj_per_gene", "FC"]].round(5))', 'print("variants: Holm across genes", int((chan.holm_across_genes <= 0.01).sum()), "| BH across genes", int((chan.bh_across_genes <= 0.01).sum()),', '      "| unadjusted p <= 0.01", int((chan.p_condition <= 0.01).sum()))', 'print("RESULT figs2d: count", n_main, "channel genes tested", len(chan))']
-------------------

Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/dump.py", line 2, in <module>
    nb=nbformat.read(sys.argv[1],4)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbformat/__init__.py", line 171, in read
    with open(fp, encoding="utf8") as f:  # noqa: PTH123
         ~~~~^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dev_out2.ipynb'
1,851d0
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; VPY=executed/lee-2023/.venv/bin/python; LEE_CACHE=$TMPDIR/feat.pkl JUPYTER_PATH=executed/lee-2023/.venv/share/jupyter timeout 1200 $VPY -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1100 --ExecutePreprocessor.kernel_name=registry-lee-2023 dev_nb.ipynb --output dev_out2.ipynb 2>&1 | grep -v "^\s*$" | tail -25 | cut -c1-300
```

```
cell = self.execute_cell(cell, index, store_history=True)
  File "executed/lee-2023/.venv/lib/python3.13/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/asyncio/base_events.py", line 726, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "executed/lee-2023/.venv/lib/python3.13/site-packages/nbclient/client.py", line 1005, in async_execute_cell
    exec_reply = await self.task_poll_for_reply
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "executed/lee-2023/.venv/lib/python3.13/site-packages/nbclient/client.py", line 806, in _async_poll_for_reply
    error_on_timeout_execute_reply = await self._async_handle_timeout(timeout, cell)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "executed/lee-2023/.venv/lib/python3.13/site-packages/nbclient/client.py", line 856, in _async_handle_timeout
    raise CellTimeoutError.error_from_timeout_and_cell(
        "Cell execution timed out", timeout, cell
    )
nbclient.exceptions.CellTimeoutError: A cell timed out while it was being executed, after 1100 seconds.
The message was: Cell execution timed out.
Here is a preview of the cell contents:
[... 6 more lines not kept]
```

**Agent**

The figs2d cell hangs in the locked environment (it ran in seconds in my dev env). Profiling it.

**Agent calls Bash**

```bash
cd entries/lee-2023; VPY=executed/lee-2023/.venv/bin/python; timeout 600 $VPY - <<'E' 2>&1 | grep -v Warn
import time, numpy as np, pandas as pd
import lee2023 as L
t=time.time(); X, mp = L.transcriptomes(); print('load', time.time()-t)
m1=L.metadata_table().drop_duplicates(); T=m1.set_index('patched_cell_container').loc[X.columns]
wf=(T.Transcriptomic_type=="Inh L2-4 PVALB WFDC2").values
t=time.time(); Xw=X.loc[:,wf]; print('loc', time.time()-t)
t=time.time(); keep=Xw.mean(axis=1)>0.01; Xw=Xw[keep]; print('mean/filter', time.time()-t, Xw.shape)
cond=(T.condition.values[wf]=="culture").astype(float); imm=T.condition2.str.contains("microglial").values[wf].astype(float)
Dm=np.column_stack([np.ones_like(cond),cond,imm,cond*imm]); Y=Xw.values.T
t=time.time(); beta,*_=np.linalg.lstsq(Dm,Y,rcond=None); print('lstsq', time.time()-t)
from statsmodels.stats.multitest import multipletests
t=time.time()
for j in range(2000): multipletests(np.random.rand(3),method='holm')
print('2000 holm', time.time()-t)
E
```

```
load 3.891949415206909
loc 0.015088558197021484
mean/filter 0.030422210693359375 (40551, 168)
lstsq 0.0642096996307373
2000 holm 35.61598801612854
```

**Agent**

`multipletests` takes 18 ms per call in the locked statsmodels, and the cell calls it 40,551 times. Replacing it with a vectorized Holm.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
p='/tmp/claude-1001/nb_cells_part2.py'; s=open(p).read()
old=s[s.index('def holm_cols(P):'):s.index('adj = holm_cols(pv)[0]')]
new='''def holm_cols(P):
    """R's p.adjust(method = "holm") applied to each column of P (here, each gene's three term
    p-values), vectorized: sorted p times (m - rank), cumulative maximum, capped at 1."""
    m_ = P.shape[0]
    order = np.argsort(P, axis=0)
    ps = np.take_along_axis(P, order, axis=0)
    adj_s = np.minimum(1, np.maximum.accumulate(ps * (m_ - np.arange(m_))[:, None], axis=0))
    out = np.empty_like(P)
    np.put_along_axis(out, order, adj_s, axis=0)
    return out
chk = np.array([[0.01, 0.2], [0.04, 0.03], [0.03, 0.5]])
print("check against statsmodels on two columns:", np.allclose(holm_cols(chk), np.column_stack([multipletests(chk[:, j], method="holm")[1] for j in range(2)])))
'''
s=s.replace(old,new)
open(p,'w').write(s)
E
dev/bin/python build_nb.py --dev $TMPDIR/dev_nb.ipynb; VPY=executed/lee-2023/.venv/bin/python; date -u; LEE_CACHE=$TMPDIR/feat.pkl JUPYTER_PATH=executed/lee-2023/.venv/share/jupyter timeout 1500 $VPY -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1400 --ExecutePreprocessor.kernel_name=registry-lee-2023 dev_nb.ipynb --output dev_out2.ipynb 2>&1 | grep -v "^\s*$" | tail -3 | cut -c1-300; date -u; dev/bin/python dump.py dev_out2.ipynb > dev2.txt; dev/bin/python dump.py dev_out.ipynb > dev1.txt; diff dev1.txt dev2.txt | head -80
```

```
wrote /tmp/claude-1001/dev_nb.ipynb 114 cells
Wed Nov 18 11:39:50 UTC 2026
[NbConvertApp] Converting notebook dev_nb.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 177258 bytes to dev_out2.ipynb
Wed Nov 18 11:42:51 UTC 2026
19a20,21
>   fields under /general: {'dev': 706}
>   electrode location: {'dev': 706}
59a62,64
> Deposited twice? files sharing identical values of ['v_baseline', 'rheobase_i', 'input_resistance', 'tau', 'sag', 'width_short_square', 'threshold_i_ramp'] : 0 []
>   files with the same file size: 0
> Days in culture of culture cells: {2.0: 2, 3.0: 54, 4.0: 43, 5.0: 21, 6.0: 124, 7.0: 109, 8.0: 19, 9.0: 24, 10.0: 9, 11.0: 11, 12.0: 1, 13.0: 15, 14.0: 13, 15.0: 7, 16.0: 1}
61d65
< ERROR TypeError sequence item 5: expected str instance, float found
154a159
> check against statsmodels on two columns: True
238a244
> 
650a657
[... 8 more lines not kept]
```

**Agent**

Locked-environment test gives the same results as before and the notebook runs clean. Starting the full run from the archive (11:43 UTC).

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python build_nb.py entries/lee-2023/reproduce_lee_2023.ipynb && cd  && python tools/entry.py check entries/lee-2023 | tail -2 && date -u && timeout 4500 python tools/entry.py all entries/lee-2023 2>&1 | tail -5; date -u
```

```
wrote entries/lee-2023/reproduce_lee_2023.ipynb 114 cells
0 error(s)
Wed Nov 18 11:43:00 UTC 2026
Installed kernelspec registry-lee-2023 in executed/lee-2023/.venv/share/jupyter/kernels/registry-lee-2023
0 error(s)
pass  reproduce_lee_2023.ipynb  (1800 s)
Wed Nov 18 12:13:08 UTC 2026
```

**Agent**

Passed (30 min). Comparing the executed outputs with the development run.

**Agent calls Bash**

```bash
cd $TMPDIR; dev/bin/python dump.py executed/lee-2023/reproduce_lee_2023.ipynb > real.txt; diff dev2.txt real.txt | head -60; grep -n "extraction\|fields under\|electrode location\|runtime" real.txt
```

```
8a9,10
> extraction 1618 s; peak memory of a worker 4.28 GB
> 
20,21c22,23
<   fields under /general: {'dev': 706}
<   electrode location: {'dev': 706}
---
>   fields under /general: {'data_collection,devices,generated_by,institution,intracellular_ephys,labnotebook,session_id,source_script,stimsets,subject,testpulse,user_comment': 706}
>   electrode location: {'none;none': 705, 'none;none;none': 1}
302c304
< all 2 DIC cells in the dandiset: [['Inh L2-4 SST FRZB', 'PVALB'], ['Inh L2-4 PVALB WFDC2', 'PVALB']]
---
> all 2 DIC cells in the dandiset: [['Inh L2-4 PVALB WFDC2', 'PVALB'], ['Inh L2-4 SST FRZB', 'PVALB']]
318c320
< seed+0 features k=15: acute cross 0.408 vs shuffle median 0.564 (ratio 0.72), culture cross 0.191 vs shuffle median 0.446 (ratio 0.43)
---
> seed+0 features k=15: acute cross 0.408 vs shuffle median 0.563 (ratio 0.72), culture cross 0.191 vs shuffle median 0.446 (ratio 0.43)
320c322
< seed+0 features k=10: acute cross 0.378 vs shuffle median 0.558 (ratio 0.68), culture cross 0.159 vs shuffle median 0.452 (ratio 0.35)
---
[... 46 more lines not kept]
```

**Agent**

Row order differs from my cache, so UMAP and shuffle numbers moved slightly. Checking every difference against the conclusions.

**Agent calls Bash**

```bash
cd $TMPDIR; diff dev2.txt real.txt | sed -n '60,400p' | grep "^>" | cut -c1-250
```

```
> seed+4000 features k=15: acute cross 0.408 vs shuffle median 0.562 (ratio 0.73), culture cross 0.191 vs shuffle median 0.449 (ratio 0.43)
> seed+4000 umap     k=15: acute cross 0.418 vs shuffle median 0.562 (ratio 0.74), culture cross 0.320 vs shuffle median 0.446 (ratio 0.72)
> LAMP5/PAX6/Other          0.433  0.093   0.340
> PVALB                     0.844  0.529   0.314
> SST                       0.454  0.230   0.224
> seed+0 umap: ok=True
> LAMP5/PAX6/Other          0.410  0.093   0.317
> PVALB                     0.879  0.529   0.350
> SST                       0.448  0.230   0.218
> VIP                       0.409  0.147   0.262
> LAMP5/PAX6/Other          0.398  0.093   0.305
> PVALB                     0.874  0.529   0.345
> VIP                       0.397  0.147   0.250
> LAMP5/PAX6/Other          0.410  0.093   0.317
> PVALB                     0.876  0.529   0.347
> SST                       0.429  0.230   0.199
> VIP                       0.383  0.147   0.236
> LAMP5/PAX6/Other          0.410  0.093   0.317
> PVALB                     0.870  0.529   0.341
> SST                       0.446  0.230   0.216
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -A44 "##### ## fig2b" real.txt | grep -v "^[0-9]*-$" | head -50; grep -n -A12 "##### ## fig5d-dbc-ephys" real.txt
```

```
350:##### ## fig2b-ephys-umap-subclasses
351-seed+0 features: ok=False
352-                  same_fraction  share  excess
353-LAMP5/PAX6/Other          0.433  0.093   0.340
354-PVALB                     0.844  0.529   0.314
355-SST                       0.454  0.230   0.224
356-VIP                       0.341  0.147   0.193
357-seed+0 umap: ok=True
358-                  same_fraction  share  excess
359-LAMP5/PAX6/Other          0.410  0.093   0.317
360-PVALB                     0.879  0.529   0.350
361-SST                       0.448  0.230   0.218
362-VIP                       0.409  0.147   0.262
364-seed+1000 umap: ok=True
365-                  same_fraction  share  excess
366-LAMP5/PAX6/Other          0.398  0.093   0.305
367-PVALB                     0.874  0.529   0.345
368-SST                       0.431  0.230   0.201
369-VIP                       0.397  0.147   0.250
371-seed+2000 umap: ok=False
[... 33 more lines not kept]
```

**Agent**

Only the UMAP and shuffle numbers moved; outcomes are unchanged. Updating those conclusion sentences, then re-running so the executed copy matches the entry.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
p='/tmp/claude-1001/nb_results.yaml'; s=open(p).read()
rep=[("""In the UMAP embedding the ratios are 0.68 to
  0.78 under all five seeds, which passes. With 30 neighbours the feature-space culture ratio is
  0.49.""","""In the UMAP embedding the ratios are 0.69 to
  0.78 under all five seeds, which passes. With 30 neighbours the feature-space culture ratio is
  0.48."""),
("""PVALB has the highest same-subclass fraction (0.85 in feature space,
  0.87 to 0.88 in UMAP). In feature space the VIP excess over its share is 0.193, under the 0.2 the
  criterion asks. In the UMAP of the claim's seed the SST excess is 0.198 (above 0.2 under three of
  the five seeds).""","""PVALB has the highest same-subclass fraction (0.84 in feature space,
  0.87 to 0.88 in UMAP). In feature space the VIP excess over its share is 0.193, under the 0.2 the
  criterion asks. In the UMAP every excess is at least 0.2 under four of the five seeds, the claim's
  among them (SST 0.199 under the other)."""),
("""and 69 to 73 in UMAP across the five seeds.""","""and 71 to 73 in UMAP across the five seeds."""),
("""The 9 DBCs have a mean of 0.133 DBCs among their 10 nearest SST neighbours, 3.4
  times their share (0.039), in feature space and in UMAP. Over the five seeds the ratio is 2.3 to
  4.0, above the criterion's 2.""","""The 9 DBCs have a mean of 0.133 DBCs among their 10 nearest SST neighbours in
  feature space, 3.4 times their share (0.039). In UMAP the ratio is 2.6 under the claim's seed and
  2.3 to 3.7 over the five seeds, above the criterion's 2 throughout."""),
]
for a,b in rep:
    assert a in s, a[:40]
    s=s.replace(a,b)
open(p,'w').write(s)
E
dev/bin/python build_nb.py entries/lee-2023/reproduce_lee_2023.ipynb && cd  && python tools/entry.py check entries/lee-2023 | tail -1 && date -u && timeout 4500 python tools/entry.py all entries/lee-2023 2>&1 | tail -3; date -u
```

```
wrote entries/lee-2023/reproduce_lee_2023.ipynb 114 cells
0 error(s)
Wed Nov 18 12:13:39 UTC 2026
Installed kernelspec registry-lee-2023 in executed/lee-2023/.venv/share/jupyter/kernels/registry-lee-2023
0 error(s)
pass  reproduce_lee_2023.ipynb  (1797 s)
Wed Nov 18 12:43:42 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR; dev/bin/python dump.py executed/lee-2023/reproduce_lee_2023.ipynb > real2.txt; diff real.txt real2.txt | head; ls questions | head -2; sed -n 1,30p questions/asari-2009.yaml 2>/dev/null | head -5
```

```
9c9
< extraction 1618 s; peak memory of a worker 4.28 GB
---
> extraction 1616 s; peak memory of a worker 4.28 GB
450a451
> 
656a658
> 
661a664
> 
README.md
asari-2009.yaml
questions:
- claim: fig2-example-long-context
  question: The criterion says the example cell and probe are not identified and accepts any
    current-clamp cell with seven natural sound fragments and a probe tested after silence and
    two other fragments. Does the Figure 2 legend identify them? Figure 2A gives the cell's
Shell cwd was reset to
```

**Agent**

Rerun identical. Writing the attempt record now (12:44 UTC).

**Agent calls Bash**

```bash
cd  grep -n "^- id:" claims/lee-2023.yaml | awk '{print $3}' | tr '\n' ' '; echo; grep -c "^- id:" claims/lee-2023.yaml; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']; print(list(o.keys()))
f=s['properties']['findings']['items']; print(json.dumps(f)[:1500]); print(list(s['properties'].keys()))"
```

```
cell-metadata-link dataset-composition fig1b-more-genes-in-culture figs1-microglial-signature fig1c-marker-expression-correlated fig1d-nms-no-difference fig1g-wfdc2-morphology-unchanged figs2b-wfdc2-ephys-43-of-84 fig1l-width-sag-differ figs2c-no-change-with-days fig1i-wfdc2-ephys-umap-overlap figs2d-seven-channel-genes fig2b-ephys-umap-subclasses fig2c-morph-umap-subclasses fig2e-lamp5-shortest-extent fig2f-ap-kinetics fig2g-sag-by-subclass fig2h-several-features-distinct fig3c-frzb-ephys-with-pvalb fig3e-frzb-ap-like-pvalb figs6-sst-features-acute-culture fig3-frzb-transcriptome-intermediate fig3g-frzb-morphology-like-pvalb fig4a-calb1-morphology-types fig4c-calb1-ephys-by-morphology fig4d-calb1-genes-by-morphology fig5a-dbc-two-ttypes fig5b-merfish-layers figs7a-dbc-regions figs7a-dbc-markers fig5c-dbc-higher-sag fig5d-dbc-ephys-intermingled fig5e-bouton-density fig6b-species-morphology fig6c-species-ephys-umap fig6e-species-sag-rheobase-width figs8b-firing-differs-pvalb2-only figs9-species-differences-not-culture figs5-vip-enhancer-enrichment figs1a-genes-across-days fig1e-wfdc2-transcriptome-overlap fig1h-wfdc2-morph-umap-overlap figs1de-mapping-unaffected fig2a-patchseq-overlaps-snrnaseq fig5d-dbc-morph-umap 
45
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
{"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\
[... 1 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/lee-2023-01.yaml",
 "content": "schema_version: 3\nid: lee-2023-01\ndatasets:\n- archive: dandi\n  id: \"000636\"\n  version: 0.241120.0510\n  doi: 10.48324/dandi.000636/0.241120.0510\n  relation: primary\npaper: doi:10.1126/science.adf6484\ndate: 2026-11-18\nentry: lee-2023\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-16\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44273539492\ninputs:\n- what: Per-cell labels (LeeDalley_manuscript_metadata_v2.csv; t-type, subclass, condition, days in\n    culture, lobe, virus, qualitative morphology type, nwb_id), the paper's electrophysiology\n    feature table (LeeDalley_ephys_fx.csv, used only to check the features computed here and as\n    labelled variants) and the DBC calls (dbc_calb1_ADGRG6.csv).\n  source: https://github.com/AllenInstitute/human_patchseq_gaba at commit\n    5eb357a1cea246c7c847b5608a8fc7e87ea95b58\n- what: Patch-seq transcriptomes (complete_patchseq_data_sets1.RData and\n    complete_patchseq_data_sets2.RData, log2(CPM + 1) of 50281 genes in 778 cells, with metaPatch)\n    and the curated voltage-gated ion channel list (vgic_genes.csv), for the data elsewhere claims on\n    gene expression.\n  source: https://github.com/AllenInstitute/human_patchseq_gaba at commit\n    5eb357a1cea246c7c847b5608a8fc7e87ea95b58\n- what: Morphology feature table of the 140 reconstructions (LeeDalley_morpho_features.csv), for the\n    data elsewhere claims on morphology. The reconstructions themselves (Brain Image Library,\n    doi 10.35077/g.892) were not read.\n  source: https://github.com/AllenInstitute/human_patchseq_gaba at commit\n    5eb357a1cea246c7c847b5608a8fc7e87ea95b58\noutcomes:\n- claim: cell-metadata-link\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:cell-metadata-link\n  notes: Files are matched to metadata rows by nwb_id, which equals the NWB session id. 684 of the\n    704 unique rows with Has_ephys (97.2%) have a file; 14 of these rows have no nwb_id and 6 have\n    one that is not in the dandiset. 16 files have no metadata row, and 6 rows without Has_ephys\n    have a file. Of the cells with values on both sides, rheobase_i agrees within 10% for 92.2%\n    (650 cells), input_resistance 94.5%, sag 97.8% and width_rheo 98.8% (586 cells); the median\n    relative difference is 0 for all four. All four agree together for 90.6% of 586 cells, a\n    stricter reading shown only. Over the 65 features computed, a median of 93.6% of cells agree\n    within 10%. Seven features agree for less than 80% of cells (fi_fit_slope 41%, isi_cv_mean 46%,\n    adapt_mean 58%, isi_norm_sq_var_mean 60%, isi_norm_sq_var_max 71%, adapt_max 77%,\n    isi_adapt_ratio 27%), because their definitions here (assumptions in the helper) are not the\n    paper's.\n  deviations:\n  - The criterion is read per feature (each of the four features within 10% for at least 90% of\n    the cells with both values), as \"the cells with both values\" suggests; the joint reading\n    (90.6%) also passes.\n  - Cell-level QC (seal and access resistance) is not recomputed; the Methods' sweep QC is\n    applied (bridge balance, bias current, noise), which may explain part of the rheobase\n    disagreement.\n- claim: dataset-composition\n  outcome: partially_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:dataset-composition\n  measured:\n  - 778\n  - 44\n  - 64\n  - 101\n  - 158\n  - 363\n  notes: The metadata table holds 778 unique neurons in 44 t-types, as the paper says. Over the 686\n    labelled files with a QC-passing long square sweep, reading (a), Revised_subclass_label, gives\n    LAMP5/PAX6 64, VIP 101, SST 158 and PVALB 363; three are within tolerance and LAMP5/PAX6 is not\n    (64 against 75, tolerance 7.5). Reading (b), subclass_label, gives 69, 96, 231 and 290, two\n    within tolerance. The 675 cells with a rheobase computed here equal the paper's total (75 + 99\n    + 149 + 352), but split 63, 99, 155 and 358. All 704 rows with Has_ephys give 67, 111, 156 and\n    370 under reading (a), so the paper's 75 LAMP5/PAX6 cannot be counted from its own table either.\n    The metadata table lists layers 1 and 5_6 for some cells as well as 2 to 6.\n  deviations:\n  - Cell-level inclusion criteria (seal, access resistance) are not recomputed from the test\n    pulses; a cell counts when it has at least one long square sweep passing the Methods' sweep QC.\n- claim: fig1b-more-genes-in-culture\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig1b-more-genes-in-culture\n  notes: Genes above 0 in the expression matrix, culture median 12203 (n = 467) against acute 11259\n    (n = 311), two-sided Mann-Whitney p = 4.3e-10. With the Genes_Detected column of the metadata,\n    7318 against 6802, p = 1.6e-05. Both are below p = 0.0001.\n  deviations:\n  - The matrix count of genes above 0 does not equal the Genes_Detected column for any cell\n    (median difference 4394 genes); both are shown, and the test holds for both.\n- claim: figs1-microglial-signature\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: The criterion is the Seurat V4 clustering of the code's notebook (FindVariableFeatures,\n    ScaleData, RunPCA, RunUMAP, FindNeighbors and FindClusters at resolutions 0.001 and 0.1). Seurat\n    is an R package and cannot be installed in the entry's locked Python environment, and a Python\n    re-implementation would not be the paper's clustering. The paper's own calls are in the\n    metadata (condition2), 181 culture and 130 acute cells called microglial (metaPatch has 180\n    culture_immune), but testing them would only restate the labels.\n- claim: fig1c-marker-expression-correlated\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig1c-marker-expression-correlated\n  notes: Every reading run holds. Per subclass, Pearson r is 0.81 to 0.95 on log2(CPM + 1) and 0.82\n    to 0.97 on CPM, Spearman 0.75 to 0.94, all p < 1e-4 with 25 genes; pooled over 100 genes, r =\n    0.87 to 0.92. Cells per subclass, acute and culture, are 57 and 25 (LAMP5/PAX6), 145 and 258\n    (PVALB), 30 and 141 (SST), 79 and 43 (VIP).\n  deviations:\n  - The genes are the 25 with the largest difference in mean log2(CPM + 1) between a subclass's\n    Patch-seq cells and the other cells, a standard choice. The criterion's other reading, the\n    snRNA-seq ranking, could not be run, as the code repository does not hold the dissociated\n    nuclei data its notebook loads (complete_facs_data_sets.RData). The outcome rests on the\n    Patch-seq readings, an assumption.\n- claim: fig1d-nms-no-difference\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig1d-nms-no-difference\n  notes: marker_sum_norm_label, acute median 0.962 (n = 311) and culture 0.962 (n = 467), two-sided\n    Mann-Whitney p = 0.38, rank-biserial -0.037.\n  deviations:\n  - The NMS values are the paper's own column; they were not recomputed from the expression data.\n- claim: fig1g-wfdc2-morphology-unchanged\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig1g-wfdc2-morphology-unchanged\n  notes: The feature table has 16 acute and 10 culture PVALB WFDC2 reconstructions, not the paper's\n    10 and 9. No feature differs at FDR p < 0.05 under any reading. (a) All 26 cells, smallest FDR p\n    0.117 (smallest raw p 0.0029, soma_surface). (b) The 9 and 9 cells inside the depth range both\n    groups share, smallest FDR p 0.202. (c) Each culture cell with its nearest-depth acute cell, 10\n    and 10, smallest FDR p 0.090. Culture somas are shallower (median 535 against 837 um).\n  deviations:\n  - Tested on the paper's morphology feature table, not on features recomputed from the\n    reconstructions.\n  - The 50 features are the table's 51 columns less soma depth, which the matching uses. How the\n    paper depth-matched its 9 and 10 cells is not given; two matchings were run, and all readings\n    give the same outcome.\n- claim: figs2b-wfdc2-ephys-43-of-84\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs2b-wfdc2-ephys-43-of-84\n  notes: 19 of the 84 features (width_suprathresh, postap_slope, sag_area, sag_peak_t, sag_tau,\n    sag_depol, ahp_delay_ratio, trough_slowdeltav and adp_v_last features) are not computed by\n    public IPFX; the Methods say \"custom code used for chirps and some high-level features will be\n    released in a future version of IPFX\". Over the 65 features computed, 41 differ between 65\n    acute and 82 culture PVALB WFDC2 cells at BH-FDR p < 0.05 (63%, the paper 51%). Counting the 19\n    missing features as all non-significant or all significant bounds the count over 84 between 39\n    and 61, which contains the whole tolerance (38.7 to 47.3), so the outcome cannot be decided. As\n    variants, the paper's own table gives 47 of 84 for the same cells (53 of 93), and the computed\n    features with the paper's values for the missing 19 give 50. With culture restricted to cells\n    without (with) the microglial signature, 37 (30) of 65 differ.\n- claim: fig1l-width-sag-differ\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig1l-width-sag-differ\n  notes: The readings give different outcomes, so the claim is blocked as its criterion says. Sag is\n    higher in culture (median 0.284 against 0.110, FDR p = 1.2e-14). AP width is wider in culture\n    at FDR p < 1e-4 for the rheobase (FDR p = 5.6e-05), hero (6.6e-06) and short square (7.7e-05)\n    sweeps; the ramp gives FDR p = 0.0077. Input resistance does not differ (FDR p = 0.81). The ISI\n    of the hero sweep does not differ (FDR p = 0.75), but that of the rheobase sweep does (FDR p =\n    0.016, 74 cells with two or more spikes at rheobase). Six of the eight readings fail, the\n    three with the rheobase ISI and the two with the ramp width (one counted in both); under the\n    hero ISI with rheobase, hero or short square width the claim holds. FDR is taken over the 65\n    features computed, not the paper's 84. Open question for the authors, which sweep's ISI and\n    width Fig. 1L plots.\n  deviations:\n  - BH-FDR across the 65 computed features, as the 84 cannot all be computed.\n- claim: figs2c-no-change-with-days\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs2c-no-change-with-days\n  notes: It depends on fig1l-width-sag-differ, which is blocked, and its own width readings disagree.\n    Over 82 culture PVALB WFDC2 cells, sag does not correlate with days in culture (r = 0.07, FDR p\n    0.51 to 0.70). Width does not for the rheobase, hero and ramp sweeps (r -0.05 to 0.08) but does\n    for the short square (r = 0.37, FDR p = 0.0015). The one 2 DIC PVALB WFDC2 cell has sag 0.379\n    and width 0.54 to 0.61 ms, above the acute medians (0.110, 0.41 to 0.49 ms) as the culture\n    group is. Of the 41 features that differ, 4 correlate with days in culture at BH p < 0.05.\n- claim: fig1i-wfdc2-ephys-umap-overlap\n  outcome: not_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig1i-wfdc2-ephys-umap-overlap\n  notes: In feature space, culture PVALB WFDC2 cells have a mean of 0.191 acute cells among their 15\n    nearest PVALB WFDC2 neighbours, against a shuffle median of 0.446 (ratio 0.43, under the\n    criterion's 0.5); acute cells 0.408 against 0.563 (0.72). In the UMAP embedding the ratios are\n    0.69 to 0.78 under all five seeds, which passes. With 10 and 30 neighbours the feature-space\n    culture ratio is 0.36 and 0.48. The feature-space result does not depend on the seed beyond the\n    shuffle (0.43 under all five). Culture cells sit apart in the full feature space, consistent with\n    the 41 differing features.\n  deviations:\n  - The 65 computed features in place of 84.\n- claim: figs2d-seven-channel-genes\n  outcome: blocked\n  blocked_by: other\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs2d-seven-channel-genes\n  notes: The code's linear model (condition + isImmune + interaction, Holm over each gene's three\n    term p-values as apply(lm_pval, 2, p.adjust) does) was run on 168 PVALB WFDC2 transcriptomes and\n    the 40551 genes with mean > 0.01. The code also keeps only its keepGenes, which it builds from\n    the dissociated-nuclei data (complete_facs_data_sets.RData) and sex and mitochondrial gene\n    lists, none of which is in the repository. Without that filter 142 channel genes are tested,\n    against the paper's 114, so the procedure is not the paper's; 22 of them have adjusted p <=\n    0.01 (Holm across genes 6, BH across genes 22, unadjusted 26). The count is not judged against 7.\n- claim: fig2b-ephys-umap-subclasses\n  outcome: not_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig2b-ephys-umap-subclasses\n  notes: PVALB has the highest same-subclass fraction among 15 neighbours (0.844 in feature space,\n    0.870 to 0.879 in UMAP). In feature space the VIP fraction (0.341) exceeds its share (0.147) by\n    0.193, under the criterion's 0.2; the other three exceed by 0.22 to 0.34. In UMAP all four\n    exceed 0.2 under the claim's seed (smallest SST 0.218) and under three of the other four seeds\n    (SST 0.199 under +2000). The outcome is set by the feature space, which does not depend on the\n    seed, and misses by 0.007. 686 cells, PVALB 363, SST 158, VIP 101, LAMP5/PAX6 64.\n  deviations:\n  - The 65 computed features in place of 84.\n- claim: fig2c-morph-umap-subclasses\n  outcome: not_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig2c-morph-umap-subclasses\n  notes: Over 140 reconstructions, PVALB has the highest same-subclass fraction (0.78 in feature\n    space, 0.73 in UMAP under the claim's seed). In feature space LAMP5/PAX6 (13 cells) exceed their\n    share by 0.10 and VIP by 0.19, under 0.2. In UMAP SST exceeds by 0.175 under the claim's seed\n    and 0.14 to 0.21 over the five seeds (all four pass under one seed, +2000); the feature space\n    fails under all.\n  deviations:\n  - Tested on the paper's morphology feature table, all 51 columns, z-scored.\n- claim: fig2e-lamp5-shortest-extent\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig2e-lamp5-shortest-extent\n  notes: LAMP5/PAX6 (13 cells) have the lowest median axon_max_euclidean_distance (434 um; PVALB\n    639, VIP 707, SST 920) and basal_dendrite_max_euclidean_distance (171 um; SST 300, VIP 345,\n    PVALB 348). Kruskal-Wallis p = 4.6e-06 and 2.4e-04. Dunn's FDR p of LAMP5/PAX6 against the others\n    is 1.6e-06 to 7.9e-04 for the axon, and 3.5e-04 to 0.053 for the dendrite (SST 0.053).\n  deviations:\n  - Tested on the paper's morphology feature table.\n- claim: fig2f-ap-kinetics\n  outcome: partially_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig2f-ap-kinetics\n  notes: Both readings agree. PVALB has the narrowest AP (short square median 0.48 ms against 0.66\n    to 0.74; rheobase 0.52 against 0.74 to 0.80) and the lowest upstroke/downstroke ratio (1.81\n    against 2.25 to 2.38; 1.68 against 2.32 to 2.52), with Dunn's FDR p <= 7.1e-14 against every\n    subclass. LAMP5/PAX6 has the highest median peak (71.9 mV short square, 70.6 mV rheobase), but\n    not significantly against all others, VIP p = 0.08 for the short square and SST p = 0.061 for\n    the rheobase sweep, so the peak part fails the criterion. The kinetics part holds and the peak\n    part holds by medians only.\n- claim: fig2g-sag-by-subclass\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig2g-sag-by-subclass\n  notes: Median sag LAMP5/PAX6 0.100 and VIP 0.153 against PVALB 0.241 and SST 0.300; the four pairs\n    differ at Dunn's FDR p 8.7e-13 to 1.9e-06; Kruskal-Wallis p = 8.1e-18. By condition the\n    LAMP5/PAX6 median is 0.059 acute and 0.256 culture, near the PVALB culture median of 0.283.\n- claim: fig2h-several-features-distinct\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig2h-several-features-distinct\n  notes: 59 of 65 features differ across subclasses at BH-FDR p < 0.05 (Kruskal-Wallis); 44 are\n    outside width, upstroke/downstroke ratio, peak and sag, and 43 of these have a Dunn pair at p <\n    0.05. The strongest are tau, downstroke and input resistance.\n  deviations:\n  - The 65 computed features in place of 84.\n- claim: fig3c-frzb-ephys-with-pvalb\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig3c-frzb-ephys-with-pvalb\n  notes: 72 of 73 SST FRZB cells have a PVALB majority among their 15 nearest SST or PVALB\n    neighbours in feature space (mean PVALB fraction 0.85, PVALB share of the reference 0.65), and\n    71 to 73 in UMAP over the five seeds.\n  deviations:\n  - The 65 computed features in place of 84.\n- claim: fig3e-frzb-ap-like-pvalb\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig3e-frzb-ap-like-pvalb\n  notes: Under the rheobase, short square and hero sweeps, SST FRZB (68 to 72 cells) differs from SST\n    in width (Dunn's FDR p 2e-12 to 7.2e-09) and upstroke/downstroke ratio (1.1e-19 to 6.4e-11), with\n    medians nearer PVALB (ratio 1.69 against PVALB 1.68 and SST 2.32 at rheobase; width 0.60 against\n    0.52 and 0.80 ms). SST FRZB still differs from PVALB in width (p 7.8e-05 to 0.0011) but not in\n    the ratio (p 0.067 to 0.88).\n- claim: figs6-sst-features-acute-culture\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs6-sst-features-acute-culture\n  notes: Acute against culture SST cells (17 to 25 acute, 117 to 199 culture), with and without SST\n    FRZB, under three sweep readings, smallest FDR p 0.22. Culture widths are slightly lower (median\n    0.72 against 0.80 ms at rheobase with FRZB); rank-biserial -0.23 to 0.07.\n- claim: fig3-frzb-transcriptome-intermediate\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: The criterion needs the snRNA-seq reference (its top 20 DE genes, the SST FRZB nuclei) and\n    the Seurat integration of the code's notebook. The snRNA-seq data are on the Allen portal\n    without a pinned version, and Seurat cannot run in the locked Python environment.\n- claim: fig3g-frzb-morphology-like-pvalb\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig3g-frzb-morphology-like-pvalb\n  notes: SST FRZB (14 cells) median axon_extent_x 855 um (PVALB 910, SST 436) and\n    axon_emd_with_basal_dendrite 15.7 (PVALB 15.8, SST 43.9); SST against SST FRZB Dunn's FDR p =\n    0.0008 and 0.0006, SST FRZB against PVALB 0.72 and 0.88. In co-clustering cut at six clusters,\n    12 of 14 SST FRZB cells fall in PVALB-dominated clusters and 2 in SST-dominated ones, for 10 and\n    20 neighbours and all five seeds.\n  deviations:\n  - Tested on the paper's morphology feature table. The co-clustering's open parts (all columns as\n    features, the cut at six clusters, 10 and 20 neighbours) follow the criterion; dominance is\n    taken from the cells other than SST FRZB.\n- claim: fig4a-calb1-morphology-types\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Two of the criterion's four tests need axon length by layer (in L1, below the soma layer),\n    which the feature table does not hold; they need the layer-aligned reconstructions at the Brain\n    Image Library (doi 10.35077/g.892), which were not processed within the run's time. The\n    metadata lists 4 MC, 7 DBC (SST CALB1), 1 basket and 4 sparse SST cells in SST CALB1.\n- claim: fig4c-calb1-ephys-by-morphology\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig4c-calb1-ephys-by-morphology\n  notes: 14 SST CALB1 cells with a file (6 DBC, 3 MC, 4 sparse SST, 1 basket). Sparse SST median sag\n    0.300 against DBC 0.473 and MC 0.509; isi_adapt_ratio 1.75 against 1.14 and 1.37; latency at\n    rheobase 0.187 s against 0.070 and 0.079, at the hero sweep 0.030 against 0.019 and 0.022. MC\n    peak is highest (84.0 mV at rheobase, 83.1 at the hero sweep). All four statements hold under\n    every reading, by medians as the criterion says; Kruskal-Wallis p is 0.029 (sag), 0.16\n    (adaptation), 0.11 (latency) and 0.032 (peak). The adaptation index (adapt_hero) also puts\n    sparse SST highest.\n  deviations:\n  - The ISI adaptation ratio is computed as the second ISI over the first on the lowest sweep with\n    four or more spikes (an assumption, Methods \"a ratio of the spike features between the first and\n    third spike\"). It agrees with the paper's table for only 27% of cells. The paper's own values\n    for these cells order the types the same way (sparse SST 3.84, MC 1.93, DBC 1.39).\n- claim: fig4d-calb1-genes-by-morphology\n  outcome: not_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig4d-calb1-genes-by-morphology\n  measured: 2\n  notes: Under the Methods (pairwise Welch t tests, Bonferroni over 50281 genes, adjusted p < 0.05),\n    2 genes differ between the 7 DBC, 3 MC and 5 sparse SST cells of SST CALB1, and none among the\n    10 culture microglial ones (3, 3, 4; the legend's \"10\"). The code's one-against-rest variant\n    (culture microglial cells, genes of median >= 1, p < 0.01) gives 431 genes, or 451 rows as\n    FindAllMarkers counts them; neither is within 228 to 278. Its gene filters (keepGenes and the\n    immune genes) need data not in the repository. Clusters cannot be built on 2 genes. On the\n    variant genes three clusters form, but DBCs have no cluster with a majority of their own under\n    any of the five seeds (majority fractions 0.43 to 0.57).\n  deviations:\n  - Seurat's FindMarkers is run as Welch t tests in Python on the stored log2(CPM + 1); the UMAP\n    and clusters use umap-learn and the Louvain method of networkx, not Seurat.\n- claim: fig5a-dbc-two-ttypes\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig5a-dbc-two-ttypes\n  notes: The 11 DBCs of dbc_calb1_ADGRG6.csv are 7 SST CALB1 and 4 SST ADGRG6, and their t-types\n    agree with Tree_first_cl of metaPatch and the metadata table for all 11.\n  deviations:\n  - The tree mapping is not re-run (it needs the MTG reference taxonomy); its stored result is\n    compared.\n- claim: fig5b-merfish-layers\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The MERFISH data are not public at any location the paper gives (its Methods point only to\n    https://github.com/AllenInstitute/), and none was found in the dandiset or the code repository.\n    The axon part needs the layer-aligned reconstructions, not processed here. The Patch-seq soma\n    layers are in the metadata (Cortical_layer) but were not tabulated.\n- claim: figs7a-dbc-regions\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs7a-dbc-regions\n  measured:\n  - 6\n  - 7\n  - 3\n  - 4\n  notes: From the lobe column, 6 of 7 SST CALB1 DBCs are temporal (one occipital) and 3 of 4 SST\n    ADGRG6 DBCs frontal (one temporal). The NWB files carry no region. Over the 9 DBCs with a file in\n    the dandiset, 5 of 6 and 2 of 3.\n- claim: figs7a-dbc-markers\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs7a-dbc-markers\n  notes: Of 11 DBCs, 7 have CALB1 log2(CPM + 1) above 5 (values 1.8 to 9.1; 10 above 3), one has\n    CALB2 (an SST ADGRG6 DBC, 3.1), 10 have SST above 0 (one SST ADGRG6 DBC has none), and TAC1, NOS1\n    and NPY are detected in 7, 9 and 10.\n- claim: fig5c-dbc-higher-sag\n  outcome: partially_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig5c-dbc-higher-sag\n  notes: 8 of 11 DBCs have a file and a sag value (median 0.473). Reading (a), the other 73 SST CALB1\n    and SST ADGRG6 cells, median 0.389; 6 of 8 DBCs are above it; Mann-Whitney p = 0.028. Reading\n    (b), the 7 MC and sparse SST cells, median 0.358; all 8 DBCs are above it; p = 0.072. The median\n    is higher under both readings, but some DBCs fall below under (a).\n- claim: fig5d-dbc-ephys-intermingled\n  outcome: not_reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig5d-dbc-ephys-intermingled\n  notes: Among 232 SST subclass cells, the 9 DBCs with a file have a mean of 0.133 DBCs among their\n    10 nearest SST neighbours in feature space, 3.4 times their share (0.039). In UMAP the ratio is\n    2.6 under the claim's seed and 2.3 to 3.7 over the five seeds, above the criterion's 2. With 9\n    DBCs one shared neighbour moves the mean by 0.011, so the measure is coarse.\n  deviations:\n  - The 65 computed features in place of 84.\n- claim: fig5e-bouton-density\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Bouton density needs the 63x image stacks at the Brain Image Library and a counting method\n    the text read does not give (the fig. S7B legend is missing). Neither was available here.\n- claim: fig6b-species-morphology\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Needs mouse reconstructions of Gouwens et al. 2020, whose location the paper does not give,\n    and features recomputed with skeleton_keys for both species; not attempted within the run's\n    time.\n- claim: fig6c-species-ephys-umap\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The mouse recordings of Gouwens et al. 2020 are public (DANDI 000020, version 0.210913.1639,\n    4435 files, 142 GB), but selecting the mouse t-types of Pvalb 2 and Sst 5 needs the per-cell\n    mouse t-type labels, for which neither the paper nor this run found a pinned public source (a\n    DOI or a repository at a commit). Without them the cells cannot be selected, and no link claim\n    could be tested.\n- claim: fig6e-species-sag-rheobase-width\n  outcome: blocked\n  blocked_by: data_missing\n  notes: As fig6c-species-ephys-umap; the mouse t-type labels have no pinned public source. The human\n    side can be computed here (PVALB WFDC2, L4-6 PVALB SULF1 and SST CALB1 cells).\n- claim: figs8b-firing-differs-pvalb2-only\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig6e-species-sag-rheobase-width, which is blocked for lack of pinned mouse\n    labels.\n- claim: figs9-species-differences-not-culture\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig6e-species-sag-rheobase-width and figs8b-firing-differs-pvalb2-only, blocked\n    for lack of pinned mouse labels.\n- claim: figs5-vip-enhancer-enrichment\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs5-vip-enhancer-enrichment\n  notes: 19 of 30 CN2039 cells are VIP (0.63); the other 11 are PVALB 8, SST 2 and LAMP5/PAX6 1. The\n    VIP fraction is 0.138 in all other cells (odds ratio 10.8, Fisher p = 1.7e-09) and 0.053 in\n    CN1390 cells (odds ratio 30.9, p = 1e-14). All 30 CN2039 cells have a file in the dandiset; over\n    cells with a file the comparison fractions are 0.126 and 0.054. More than half of CN2039 cells\n    are VIP.\n- claim: figs1a-genes-across-days\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:figs1a-genes-across-days\n  notes: The median of genes above 0 is above the acute median (11259) at every day sampled, 2 to 16\n    (11300 to 15551; day 12 and day 16 have one cell each). Pearson r = 0.029, p = 0.54, n = 467\n    (Spearman rho = -0.017, p = 0.71).\n- claim: fig1e-wfdc2-transcriptome-overlap\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: The space is the Seurat integration of the Methods and the code's notebook (anchors on the\n    tree-mapping markers, 30 PCs), which cannot run in the locked Python environment.\n- claim: fig1h-wfdc2-morph-umap-overlap\n  outcome: reproduced\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig1h-wfdc2-morph-umap-overlap\n  notes: Over all 140 reconstructions, the 26 PVALB WFDC2 cells (and the 18 in the shared depth\n    range) have cross-condition fractions among 5 neighbours of 0.30 to 0.72, against shuffled 0.40\n    to 0.66, above half the shuffle in both spaces and all seeds; at least 88% of cells of each group\n    have a PVALB majority among their 5 nearest neighbours.\n  deviations:\n  - Tested on the paper's morphology feature table; the depth-matched set is the shared depth range\n    of fig1g-wfdc2-morphology-unchanged.\n- claim: figs1de-mapping-unaffected\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Both spaces are built with Seurat (integration, and the code's \"no data integration\" chunk),\n    which cannot run in the locked Python environment, and the four groups depend on the microglial\n    calls of figs1-microglial-signature.\n- claim: fig2a-patchseq-overlaps-snrnaseq\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Needs the human MTG snRNA-seq data (Allen portal, no pinned version) and the Seurat\n    integration, which cannot run in the locked Python environment.\n- claim: fig5d-dbc-morph-umap\n  outcome: reproduced\n  seed_sensitive: true\n  notebook: reproduce_lee_2023.ipynb\n  output: claim:fig5d-dbc-morph-umap\n  notes: Among 49 SST reconstructions with 11 DBCs (share 0.224), DBCs have a mean of 0.78 DBCs among\n    their 5 nearest SST neighbours in feature space (ratio 3.48). In UMAP the ratio is 2.02 under\n    the claim's seed, and 1.54 to 2.59 over the five seeds (+2000 1.54, +4000 1.62, under 2). Among\n    a DBC's DBC neighbours, 0.45 to 0.60 share its t-type.\n  deviations:\n  - Tested on the paper's morphology feature table.\nfindings:\n- kind: metadata_insufficient\n  statement: The NWB files hold no cell type, subclass, brain region, cortical layer, slice condition\n    (acute or culture), days in culture or virus; their electrode location is empty. Every label\n    the paper's analyses need comes from the code repository's metadata table, linked by its nwb_id\n    column.\n- kind: identifier_missing\n  statement: 16 of the 706 files have no row in the paper's metadata table (sessions 567737666,\n    567773605, 569870997, 571674350, 591326867, 591342850, 595591210, 595597605, 595715586,\n    601916346, 611610562, 611822740, 611901143, 847874997, 847908770, 855354224), so they cannot be\n    labelled. 20 metadata rows with Has_ephys have no file (14 without nwb_id, 6 whose nwb_id is\n    not in the dandiset).\n- kind: metadata_error\n  statement: The dandiset's assetsSummary gives numberOfCells 616, but the version holds 706 files of\n    one cell each.\n- kind: other\n  about: data\n  statement: 79 files have sweeps sampled at 200 kHz (all recorded in 2020 and 2021), where the Methods\n    state that data were digitized at 50 kHz; two files mix rates (25 and 50 kHz, 50 and 200 kHz).\n- kind: metadata_error\n  statement: The subject species is written \"Homo Sapiens\" in 581 files and \"Homo sapiens\" in 125.\n- kind: other\n  about: paper\n  statement: The paper's metadata table (LeeDalley_manuscript_metadata_v2.csv) repeats one row\n    (specimen 819133824), giving 779 rows for 778 cells. Its condition2 column calls 181 culture\n    cells microglial where metaPatch, stored with the transcriptomes, calls 180.\n- kind: methods_unavailable\n  statement: 19 of the paper's 84 electrophysiology features (width_suprathresh, postap_slope,\n    sag_area, sag_peak_t, sag_tau, the depolarizing sag features, ahp_delay_ratio, trough_slowdeltav\n    and adp_v_last) are computed by code the paper says \"will be released in a future version of\n    IPFX\"; public IPFX 2.1.2 does not compute them, so counts over 84 features (43 of 84 differ\n    between acute and culture) cannot be repeated. The definitions of the adaptation ratios and of\n    the mean and maximum ISI summaries are not given precisely enough to match the paper's table\n    (isi_adapt_ratio agrees for 27% of cells).\n- kind: methods_unavailable\n  statement: Which sweep stands for the interspike interval and AP width in Fig. 1L is not given. With\n    the rheobase-sweep ISI, the ISI differs between acute and culture PVALB WFDC2 cells (FDR p =\n    0.016), and with the hero-sweep ISI it does not (0.75). Could the authors say which sweeps\n    Fig. 1L and fig. S2C use?\n- kind: methods_unavailable\n  statement: The code's gene filter for the ion-channel and morphology-type gene analyses (keepGenes)\n    is built from dissociated-nuclei data (complete_facs_data_sets.RData) and sex and mitochondrial\n    gene lists that the repository does not hold, so figs. S2D (7 of 114 channel genes) and the\n    253 genes of Fig. 4D cannot be repeated from the repository.\n- kind: code_mismatch\n  statement: In the code's ion-channel analysis, apply(lm_pval, 2, p.adjust) adjusts each gene's three\n    term p-values with Holm, not across genes, and its comment calls this FDR correction.\n- kind: other\n  about: data\n  statement: The code repository's Genes_Detected column does not equal the number of genes above 0\n    in its own expression matrices for any of the 778 cells (median difference 4394 genes), and no\n    threshold on the stored log2(CPM + 1) reproduces it; how it was counted is not documented.\n- kind: data_missing\n  statement: The MERFISH data of Fig. 5B are not in the dandiset and the paper gives no public\n    location for them.\n- kind: other\n  about: paper\n  statement: The paper reports 75 LAMP5/PAX6, 99 VIP, 149 SST and 352 PVALB neurons with\n    electrophysiology. Its own metadata table gives 67, 111, 156 and 370 for the rows with Has_ephys\n    under the revised subclasses, and 675 cells with a rheobase here split 63, 99, 155 and 358, so\n    the selection behind the paper's counts is not documented.\n"
}
```

```
File created successfully at: attempts/lee-2023-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Checking a few numbers in the record against the executed output.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "variants: Holm\|seed+4000: clusters\|variant genes" real2.txt; date -u
```

```
187:variants: Holm across genes 1 | BH across genes 12 | unadjusted p <= 0.01 34
252:variant genes, 6 PCs, 5 neighbours seed+0: clusters 3, majority cluster {'DBC': 0, 'MC': 0, 'Sparse SST': 0}, fraction {'DBC': 0.43, 'MC': 1.0, 'Sparse SST': 0.8}, separated False
253:variant genes, 6 PCs, 5 neighbours seed+1000: clusters 3, majority cluster {'DBC': 2, 'MC': 1, 'Sparse SST': 1}, fraction {'DBC': 0.57, 'MC': 1.0, 'Sparse SST': 0.8}, separated False
254:variant genes, 6 PCs, 5 neighbours seed+2000: clusters 3, majority cluster {'DBC': 1, 'MC': 2, 'Sparse SST': 2}, fraction {'DBC': 0.43, 'MC': 1.0, 'Sparse SST': 0.8}, separated False
255:variant genes, 6 PCs, 5 neighbours seed+3000: clusters 3, majority cluster {'DBC': 0, 'MC': 0, 'Sparse SST': 0}, fraction {'DBC': 0.43, 'MC': 1.0, 'Sparse SST': 0.8}, separated False
257:variant genes, 6 PCs, 5 neighbours seed+4000: clusters 3, majority cluster {'DBC': 0, 'MC': 0, 'Sparse SST': 0}, fraction {'DBC': 0.43, 'MC': 1.0, 'Sparse SST': 0.8}, separated False
Wed Nov 18 12:46:05 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='attempts/lee-2023-01.yaml'; s=open(p).read()
rep=[("0.01 (Holm across genes 6, BH across genes 22, unadjusted 26)","0.01 (Holm across genes 1, BH across genes 12, unadjusted 34)"),
("""0.016, 74 cells with two or more spikes at rheobase). Six of the eight readings fail, the
    three with the rheobase ISI and the two with the ramp width (one counted in both); under the
    hero ISI with rheobase, hero or short square width the claim holds.""","""0.016, 74 cells with two or more spikes at rheobase). Five of the eight readings fail (the four
    with the rheobase ISI, and the ramp width with the hero ISI); under the hero ISI with
    rheobase, hero or short square width the claim holds."""),
("""On the
    variant genes three clusters form, but DBCs have no cluster with a majority of their own under
    any of the five seeds (majority fractions 0.43 to 0.57).""","""On the
    variant genes three clusters form, but under every one of the five seeds MC and sparse SST cells
    have their majority in the same cluster, and DBCs are split (largest share 0.43 to 0.57)."""),
("Among 232 SST subclass cells, the 9 DBCs","Among the SST subclass cells, the 9 DBCs"),
]
for a,b in rep:
    assert a in s, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
E
python3 - <<'E'
p='/tmp/claude-1001/nb_results.yaml'; s=open(p).read()
print('three clusters form, but DBCs do not have a majority cluster' in s)
E
grep -n "not reproduced. The Methods" -A6 /tmp/claude-1001/nb_results.yaml | tail -3
```

```
False
47-  form, but DBCs do not have a majority cluster of their own under any of the five seeds.
48-figs2b-wfdc2-ephys-43-of-84: >-
49-  blocked. 19 of the 84 features need code the paper has not released, so the count over 84 is
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
p='/tmp/claude-1001/nb_results.yaml'; s=open(p).read()
a=s.index("The clusters cannot be built on 2 genes.")
b=s.index("figs2b-wfdc2-ephys-43-of-84:")
s=s[:a]+"""The clusters cannot be built on 2 genes. On the variant genes three clusters
  form, but MC and sparse SST cells have their majority in the same cluster under all five seeds,
  so the three types are not separated.
"""+s[b:]
open(p,'w').write(s)
E
dev/bin/python build_nb.py entries/lee-2023/reproduce_lee_2023.ipynb && cd  && date -u && timeout 3000 python tools/entry.py all entries/lee-2023 2>&1 | tail -2; date -u
```

```
wrote entries/lee-2023/reproduce_lee_2023.ipynb 114 cells
Wed Nov 18 12:46:24 UTC 2026
error: attempts/lee-2023-01.yaml: claim 'fig5b-merfish-layers' has its data in another archive (`elsewhere`); test it there, or block it for the reason it cannot be tested, not `data_missing`
1 error(s)
Wed Nov 18 12:46:28 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='attempts/lee-2023-01.yaml'; s=open(p).read()
a="""- claim: fig5b-merfish-layers
  outcome: blocked
  blocked_by: data_missing
  notes: The MERFISH data"""
assert a in s
s=s.replace(a,"""- claim: fig5b-merfish-layers
  outcome: blocked
  blocked_by: other
  notes: The claims file marks this claim data elsewhere, and the registry's check does not allow
    data_missing for it, so it is blocked as other. The MERFISH data""")
open(p,'w').write(s)
E
python tools/entry.py check entries/lee-2023 | tail -3; date -u; timeout 3000 python tools/entry.py all entries/lee-2023 2>&1 | tail -2; date -u
```

```
0 error(s)
Wed Nov 18 12:46:37 UTC 2026
0 error(s)
pass  reproduce_lee_2023.ipynb  (1795 s)
Wed Nov 18 13:16:40 UTC 2026
```

**Agent calls Bash**

```bash
cd  $TMPDIR/dev/bin/python $TMPDIR/dump.py executed/lee-2023/reproduce_lee_2023.ipynb > $TMPDIR/real3.txt; diff $TMPDIR/real2.txt $TMPDIR/real3.txt | grep -v extraction | head; python tools/entry.py handover entries/lee-2023 2>&1 | tail -3; ls executed/lee-2023/handover/; git status --short | head; date -u
```

```
9c9
---
451d450
< 
658d656
< 
664d661
< 
wrote executed/lee-2023/handover
lee-2023.yaml
lee2023.py
reproduce_lee_2023.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git status --short | grep -v "^?? \.[a-z]" ; ls -la .bashrc | head -2
```

```
?? attempts/lee-2023-01.yaml
?? entries/lee-2023/
?? scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 18 09:10 .bashrc
```

**Agent calls Bash**

```bash
cd  ls -la scripts | head; ls entries/lee-2023
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 18 09:10 scripts
README.md
__pycache__
entry.yaml
lee2023.py
reproduce_lee_2023.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
cd  git check-ignore -q entries/lee-2023/__pycache__ && echo ignored; rm -rf entries/lee-2023/__pycache__; python tools/entry.py check entries/lee-2023 | tail -1; python tools/entry.py run entries/lee-2023 2>&1 | tail -2; date -u
```

```
ignored
0 error(s)
pass  reproduce_lee_2023.ipynb  (1795 s, reused)
reused the executed copies of 2026-11-18 13:16 UTC: nothing the run reads has changed since (hash 9aac4b276a24). Nothing was executed and no environment was built; --fresh runs it again.
Wed Nov 18 13:17:09 UTC 2026
```

**Agent**

I finished the attempt: the entry, the notebook and `attempts/lee-2023-01.yaml` are written, the checks pass, and the handover package is built in `executed/lee-2023/handover/`. Nothing is committed.

## 1. Outcomes (45 claims)

| Outcome | Claims |
|---|---|
| Reproduced (20) | cell-metadata-link, fig1b, figs1a, fig1d, fig1c (rests on an assumption), fig1g, fig1h, fig2e, fig2g, fig2h, fig3c, fig3e, figs6, fig3g, fig4c (rests on an assumption), fig5a, figs7a-dbc-regions, figs7a-dbc-markers, figs5, fig5d-dbc-morph-umap (depends on the seed: two of five seeds fall below the threshold) |
| Partially reproduced (3) | dataset-composition (LAMP5/PAX6 count is 64, the paper says 75), fig2f (LAMP5/PAX6 peak highest, but not significantly against every other subclass), fig5c (6 of 8 DBCs above the comparison median under reading a) |
| Not reproduced (5) | fig1i (feature space ratio 0.43, the criterion needs 0.5), fig2b (VIP excess 0.193, needs 0.2), fig2c, fig4d (2 genes, the paper says 253), fig5d-dbc-ephys-intermingled |
| Blocked (17) | figs2b, fig1l, figs2c, fig5e: methods underspecified. figs2d, fig5b: other. Five Seurat claims, fig4a, fig6b: not runnable. Four mouse ephys claims: data missing |

## 2. Dataset, assumptions and questions

**Dataset.** I pinned version 0.241120.0510, the only published version; the paper cites none.
- The 706 NWB files carry no cell type, region, layer, condition or days in culture. All labels come from the code repository (commit 5eb357a), linked by its `nwb_id` column.
- 684 of 704 metadata rows with electrophysiology have a file. 16 files have no metadata row.
- Features recomputed with IPFX match the paper's table: rheobase, input resistance, sag and AP width at rheobase agree within 10% for 92 to 99% of cells.
- The archive summary says 616 cells for 706 one-cell files.
- 79 files have sweeps at 200 kHz, where the Methods say 50 kHz.
- Species is spelled two ways, the metadata table repeats one row, and the repository's Genes_Detected column does not match its own expression matrix.

**Assumptions.**
- fig1c: genes are ranked within the Patch-seq cells, because the snRNA-seq reference is not in the repository.
- fig4c: my ISI adaptation ratio definition matches the paper's table for only 27% of cells. The paper's own values put the morphology types in the same order.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which sweep's ISI and width Fig. 1L and fig. S2C use.
- The 19 features computed by unreleased IPFX code.
- The gene filter (`keepGenes`), which needs data the repository lacks.

**Questions for a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. The prompt and the claims file mention the bioRxiv preprint, but `paper/` held only the version-of-record text. I relied on the claims file for the preprint details.
2. MERFISH (fig5b) has no public location, but the claims file marks it `elsewhere`. The protocol says such data should be `data_missing`, and `entry.py check` rejects that for `elsewhere` claims. I used `other` and explained why in the notes.
3. Several criteria say "block when readings differ", while protocol step 1.6 allows adopting the best-supported reading. I followed the claims file (fig1l, figs2c).
4. The protocol has no rule for a count over a feature set that can only be partly computed (figs2b: 65 of 84 features). I computed bounds on the full count (39 to 61). They contain the whole tolerance band, so I blocked the claim.
5. The mouse t-type labels (Gouwens et al. 2020) have no pinned source, though the recordings are at DANDI:000020. I blocked the four `with_inputs` mouse claims as `data_missing`, and fig6b (`elsewhere`) as `not_runnable`.
6. Seurat (R) cannot be installed in an entry's locked Python environment. I blocked the five Seurat claims as `not_runnable`.
7. Seeded UMAP and shuffle results depend on the order of rows. My development cache was in a different order, so these numbers moved slightly in the real run, with no outcome changing. The protocol could warn about this.
8. Any edit to the entry forces a full 30-minute re-run, and the "**Result:**" text lives in the notebook. Correcting two sentences cost two extra full runs.
9. The link criterion can be read per feature or for all four features together. Both pass (joint reading: 90.6%).

## 4. Runtime and failures

- The notebook takes 30 minutes, almost all of it streaming the 706 files; a worker peaks at 4.3 GB.
- The run went from 09:12 to 13:17 UTC.
- The first full run failed at the duplicate check (pandas 3 keeps missing values as floats after `astype(str)`).
- A test in the locked environment timed out on figs2d, because `multipletests` takes about 18 ms per call there; I replaced it with a vectorized Holm adjustment.
- Both were fixed, and the final run passed.

## End of run

101 turns, 243 minutes, $9.33 at API prices, result: success.
