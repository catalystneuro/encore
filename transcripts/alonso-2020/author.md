# alonso-2020 · author · run 46075031684

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (67.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/283751a0-5555-4472-a728-1ba51d6532f2/tool-results/bbeo90p65.txt

Preview (first 2KB):
Fri Nov 27 22:15:47 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/283751a0-5555-4472-a728-1ba51d6532f2/tool-results/bbeo90p65.txt"
}
```

```
1	Fri Nov 27 22:15:47 UTC 2026
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
[... 1001 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper entries/fouke-2025 questions | head -50; ls entries | grep alonso; ls attempts | grep alonso; cat claims/alonso-2020.yaml; cat papers/datasets/alonso-2020.yaml
```

```
<persisted-output>
Output too large (43.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/283751a0-5555-4472-a728-1ba51d6532f2/tool-results/bpe60ccn9.txt

Preview (first 2KB):
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.7554-elife.55470.pdf
10.7554-elife.55470.txt

questions:
README.md
amjad-2025.yaml
asari-2009.yaml
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/283751a0-5555-4472-a728-1ba51d6532f2/tool-results/bpe60ccn9.txt",
 "offset": 60
}
```

```
60	# on them use the sentences of the main text that describe them. The PDF could not be rendered
61	# here, so no figure was read from it; the pie-chart counts of Figure 10B are therefore not
62	# recorded.
63	#
64	# Code. The paper's only deposit is the dataset itself. Its Data availability says "Code and
65	# parameters to reproduce the results in this work was uploaded to Dryad", and the archive
66	# lists a single zip of about 99 kB. As the reader may not open the dataset, that code was not
67	# read. Where these criteria leave a detail open and the deposited code fixes it, the author
68	# follows the code and says so; where the code disagrees with the Methods, the Methods govern
69	# the main result and the code's choice is a variant (protocol, Reader, step 2).
70	#
71	# The data. No recordings. The paper simulates a three-cell model of the crustacean pyloric
72	# network (PD, the AB-PD pacemaker kernel in one compartment; LP; PY) after Prinz et al. 2004.
73	# Each cell is a single compartment with eight currents (INa, ICaT, ICaS, IA, IKCa, IKd, IH,
74	# Ileak) and 13 state variables; seven chemical synapses of two types (glutamatergic and
75	# cholinergic). Each model is 31 maximal conductances plus three calcium time constants and 24
76	# Q10 values (shared across cells), Tref = 10 degrees C, Q10 in [1, 2] for conductances and
77	# [1, 4] for time scales. Simulated with RK4 at dt = 0.05 ms from V = -51 mV, gating variables 0
78	# and [Ca] = 5 uM. 36 temperature-compensated models are studied, each with a six-character
79	# name. The Methods list the model of each figure. Figure 1, 4?6W66 (the second character is
[... 533 more lines not kept]
```

**Agent calls Bash**

```bash
ls -laR /tmp/dryad/m31b1h7/94811/ | head; cat docs/archives.md | sed -n '/Dryad/,/^## [A-Z]/p' | head -120
```

```
/tmp/dryad/m31b1h7/94811/:
total 108
drwxr-xr-x 2 runner runner  4096 Nov 27 22:11 .
drwxr-xr-x 3 runner runner  4096 Nov 27 22:11 ..
-rw-r--r-- 1 runner runner 99026 Nov 27 22:11 alonso_marder_tempcomp_2019_root.zip
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
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/dryad/m31b1h7/94811/ && python -c "
import zipfile
z=zipfile.ZipFile('alonso_marder_tempcomp_2019_root.zip')
for i in z.infolist(): print(i.filename,i.file_size)
"; curl -s https://datadryad.org/api/v2/versions/94811/files | python -m json.tool | head -60; curl -s "https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.m31b1h7/versions" | python -c "import json,sys;d=json.load(sys.stdin);[print(v['_links']['self'],v.get('versionNumber'),v.get('publicationDate'),v.get('versionStatus')) for v in d['_embedded']['stash:versions']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/z && cd $TMPDIR/z && python -c "
import zipfile
z=zipfile.ZipFile('/tmp/dryad/m31b1h7/94811/alonso_marder_tempcomp_2019_root.zip')
z.extractall('.', [n for n in z.namelist() if not n.startswith('__MACOSX') and not n.endswith('.DS_Store')])
"; cd alonso_marder_tempcomp_2019_root; cat README.txt compilejava.py; ls parameters_and_ci | wc -l; cat parameters_and_ci/cis_network.txt; echo; cat parameters_and_ci/p-4X6W66*
```

```
This code implements and simulates the model studied in,  

Leandro M. Alonso, and Eve Marder, "Temperature compensation in a small rhythmic circuit", (2019)

**********
OVERVIEW:
**********

The model is implemented in java. You need to compile the java code and create a .jar file. The python scripts call the compiled java .jar file to simulate the models and plot the solutions. 
IMPORTANT: to use the python scripts you need to provide the absolute path to the parameters_and_ci folder and to the java .jar file

*************
REQUIREMENTS
*************

- You need a java development kit to compile the code. (javaSDK https://www.oracle.com/technetwork/java/javase/downloads/index.html) 
java comes installed by default in many operating systems. 
To check if you have a running java and javac open a terminal and type 

> java -version
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
which java javac; java -version 2>&1; cd $TMPDIR/z/alonso_marder_tempcomp_2019_root/standaloneCodePyloricTempComp; cat PrinzNetworkWithTemperature_full_eu_slow_same_q10s_rk4.java integratePyloricNetwork_slow_full_temp_sameq10s_rk4*.java Integrador.java
```

```
/usr/bin/java
/usr/bin/javac
openjdk version "25.0.5.1" 2026-11-17 LTS
OpenJDK Runtime Environment Temurin-25.0.5.1+2 (build 25.0.5.1+2-LTS)
OpenJDK 64-Bit Server VM Temurin-25.0.5.1+2 (build 25.0.5.1+2-LTS, mixed mode, sharing)
package standaloneCodePyloricTempComp;
import standaloneCodePyloricTempComp.RealVector;
import standaloneCodePyloricTempComp.RealVectorField;
import standaloneCodePyloricTempComp.singleCompTemperature_slow_explicit;

public class PrinzNetworkWithTemperature_full_eu_slow_same_q10s_rk4 extends RealVectorField {
	public RealVector p;
	public int dim = (13*3) + 7;
	public double temp;
	public double reftemp;
	singleCompTemperature_slow_explicit cell1;
	singleCompTemperature_slow_explicit cell2;
	singleCompTemperature_slow_explicit cell3;
	int celldim ;
	
[... 412 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/z/alonso_marder_tempcomp_2019_root/standaloneCodePyloricTempComp; cat singleCompTemperature_slow_explicit.java; grep -n "FileToVector" -A25 FileUtil.java | head -40
```

```
package standaloneCodePyloricTempComp;
import standaloneCodePyloricTempComp.RealVector;
import standaloneCodePyloricTempComp.RealVectorField;

public class singleCompTemperature_slow_explicit extends RealVectorField {
	public RealVector p;
	public int dim = 13;
	public double temp;
	public double reftemp;
	
	public singleCompTemperature_slow_explicit(){
		super("singleCompTemp");	
		int pdim =45;
		this.p = new RealVector(pdim);
		this.dim= 13;
		this.reftemp= 10;	
	}
	
	public void setRefTemp(double newreftemp){
		this.reftemp = newreftemp;
[... 278 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/z/alonso_marder_tempcomp_2019_root/python-code; cat integratePyloricSQ10s_onlyvoltagetraces_RK4_pname.py integratePyloricSQ10s_remove_gA_onesteps_twotemps_RK4.py
```

```
from pylab import *
import os 
import time
import string
import random


# This script simulates the models calling the compiled java code and plots it using standard python plotting tools


# pathtomodels='[removed: a home directory path]/3.0.workspace/marderLab/pyloric_networks_temp_javacode/parameters_and_ci/'
# pathtoci='[removed: a home directory path]/3.0.workspace/marderLab/pyloric_networks_temp_javacode/parameters_and_ci/cis_network.txt'    
# pathtojava = '[removed: a home directory path]/3.0.workspace/marderLab/pyloric_networks_temp_javacode/temp.jar'
# pathtosaveresults='[removed: a home directory path]/3.0.workspace/marderLab/pyloric_networks_temp_javacode/simulations-onlytraces/'

os.getcwd()
pathtoci=os.getcwd()+'/parameters_and_ci/cis_network.txt'    
pathtojava = os.getcwd()+'/temp.jar'

pathtosaveresults=os.getcwd()+'/simulations-traces/'
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/z/alonso_marder_tempcomp_2019_root/python-code; grep -n "def \|thres\|200\|-50\|-20" plotPyloricTempUtils.py | head -80; grep -n "def \|nsecs\|temps\|dt\b\|dt=\|transient\|glob" integratePyloricSQ10s_currentscapes_RK4_mp.py | head -40
```

```
2:def plotPyloricNetworkParameters(p):
122:def plotConductancesModelsColors(pop):
271:def plotConductancesModelsColorsShapes(pop):
422:def plotCurrentScape(trace, currents):      
461:    swthres=-50        
465:    plot(t,ones(len(t))*swthres,ls='dashed',color='black',lw=0.75)
466:    vlines(1,-50,-20,lw=1)
512:def plotCurrentScapePyloricNetwork(casetemp, xmin, xmax):  
646:    plot(-50*ones(len(AB)),color='black', ls='dashed')
647:    vlines(0,-50,-20,color='black',lw=2)
650:    plot(-50*ones(len(AB))-90,color='black', ls='dashed')
652:    plot(-50*ones(len(AB))-(2*90),color='black', ls='dashed')
5:import glob 
13:def getDownwardCrossings(thres,V):
20:def job(pathtoci,pathtostore,pathtojava,pathtop,nsecs,temp,dt,transient):
23:    excommand = 'java -cp  ' +pathtojava+' standaloneCodePyloricTempComp.integratePyloricNetwork_slow_full_temp_sameq10s_rk4_fullout_droptransient ' + pathtoci + ' ' + pathtop
24:    command = excommand +' ' + str(nsecs)+' '+str(temp) + ' '+str(dt)+  ' '+ str(transient)+ ' > ' + fname 
52:modelparameters = glob.glob(pathtomodels+'p-*.txt') 
55:# modelparameters = glob.glob(pathtomodels+'p-WWZ3CN*.txt') #figure 8
56:# modelparameters = glob.glob(pathtomodels+'p-FGFKQS*.txt') #figure 9
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/z/alonso_marder_tempcomp_2019_root/python-code; sed -n 1,50p integratePyloricSQ10s_currentscapes_RK4_mp.py; sed -n 100,140p integratePyloricSQ10s_currentscapes_RK4_mp.py; sed -n 160,200p integratePyloricSQ10s_currentscapes_RK4_mp.py; cat getCurrents.py | head -150
```

```
# -*- coding: utf-8 -*-
from pylab import * 
import os
import string
import glob 
import time
from getCurrents import *
from plotCurrentsTraces_rk4 import * 
from plotPyloricTempUtils import * 
import multiprocessing
from multiprocessing import Pool

def getDownwardCrossings(thres,V):
    times=[]
    for i in arange(0,len(V)-1):
        if(V[i]>thres and V[i+1]<=thres):
            times.append(i)
    return array(times)

def job(pathtoci,pathtostore,pathtojava,pathtop,nsecs,temp,dt,transient):
[... 263 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/z/alonso_marder_tempcomp_2019_root/python-code; sed -n 422,460p plotPyloricTempUtils.py
```

```
def plotCurrentScape(trace, currents):      
    fig = figure(figsize=(4,4))
        
    c0=array(currents)
    cpos= c0.copy()
    cpos[c0<0]=0    
    cneg=c0.copy()
    cneg[c0>0]=0
    
    normapos = sum(abs(array(cpos)),axis=0)
    normaneg = sum(abs(array(cneg)),axis=0)
    npPD=normapos
    nnPD=normaneg
    cnorm=c0.copy()
    cnorm[c0>0]=(abs(c0)/normapos)[c0>0]
    cnorm[c0<0]=-(abs(c0)/normaneg)[c0<0]
    
    resy=1000
    impos=zeros((resy,shape(cnorm)[-1])) 
    imneg=zeros((resy,shape(cnorm)[-1]))     
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n "Materials and methods\|Classification scheme\|Parameters used in this study\|Finding parameters\|Membrane potential and current\|Data availability\|References" paper/10.7554-elife.55470.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55470.txt",
 "offset": 613,
 "limit": 245
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55470.txt",
 "offset": 150,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in entries/fouke-2025/README.md; head -c 3000 entries/fouke-2025/omr.py; python tools/entry.py --help 2>&1 | head -30
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
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "tmp/dryad\|local path\|staged\|dryad" tools/entry.py | head -30; grep -n "timeout\|max_minutes\|max-minutes" tools/entry.py | head
```

```
468:    """Whether a local path in the code is inside the dataset directory `encore check` gave (ENCORE_LOCAL_DATA):
469:    the one local path an entry on a local dataset may name."""
488:        report.error(where, "names a local path; stream the data from the archive")
29:that takes longer than --max-minutes fails, even if it ran without error.
553:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
554:                   max_minutes: float) -> int:
560:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
607:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
618:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
625:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
627:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
656:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
663:        if ok and seconds > max_minutes * 60:
```

**Agent calls Bash**

```bash
sed -n 455,500p tools/entry.py; grep -n "default=" tools/entry.py | head
```

```
if path != mine[-1]:
                continue
            if notebook and notebook not in listed:
                report.error(path.relative_to(ROOT), f"notebook {notebook!r} is not in the entry")
            tag = outcome.get("output")
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
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "LOCAL_PATH =" -A4 tools/entry.py; grep -rn "tmp/dryad\|DRYAD_ROOT\|staged" tools/*.py docs/archives.md | head; grep -rln "dryad" entries/*/ 2>/dev/null | head
```

```
72:LOCAL_PATH = re.compile(r"""["'](?:~/|/(?:Users|home|tmp|mnt|media|Volumes|data|scratch)/|[A-Za-z]:[\\/])""")
73-LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)
74-
75-
76-class Report:
tools/stage_files.py:28:    staged = [a for a in ALL.values() if a.stage]
tools/stage_files.py:30:        keys = [t["key"] for t in datasets.targets() if t["archive"] in {a.key for a in staged}]
tools/stage_files.py:41:            print(f"::warning::{datasets.label(key)}: no {', '.join(missing)}, so its files are not staged")
tools/stage_files.py:50:            print(f"::error::{datasets.label(key)}: the files were not staged: {type(err).__name__}: {err}")
tools/submission.py:15:`pack` reads the changes a run left staged in a checkout of the registry (`git add`), against the commit checked out:
tools/submission.py:134:def staged(root: Path) -> tuple[list[str], list[str]]:
tools/submission.py:148:    changed, removed = staged(root)
docs/archives.md:120:  `/tmp/dryad/<id>/<version id>/` and checks each against the SHA-256 the file
docs/archives.md:470:   repository's secrets. The access sentence then points agents to the staged
entries/brudner-2026/reproduce_brudner_2026.ipynb
entries/dias-2025/autumn_ahy_main_c.ipynb
entries/dias-2025/entry.yaml
entries/dias-2025/wingallom.py
entries/dias-2025/stan_models.ipynb
entries/dias-2025/reproduce_dias_2025.ipynb
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "dryad\|DRYAD\|staged\|tmp" entries/dias-2025/wingallom.py | head -20
```

```
52:DRYAD_ID = "bvq83bkk9"
53:DRYAD_VERSION = "333377"
54:STAGED = Path("/tmp") / "dryad" / DRYAD_ID / DRYAD_VERSION  # where the workflow stages them (docs/archives.md)
55:SHA256 = {  # Dryad file list, https://datadryad.org/api/v2/versions/333377/files
136:def check_staged() -> dict[str, str]:
137:    """SHA-256 of each staged file; raises if any differs from Dryad's file list."""
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev -p 3.12 2>&1 | tail -2; source dev/bin/activate && uv pip install -q numba numpy scipy pandas matplotlib 2>&1 | tail -2; python -c "import numba;print(numba.__version__)"; nproc; free -g; date -u
```

```
0.68.1
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
Swap:              2           0           2
Fri Nov 27 22:17:16 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p entries/alonso-2020
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "entries/alonso-2020/pyloric.py",
 "content": "\"\"\"Loading, simulation and measures for the temperature-compensated pyloric networks of Dryad m31b1h7.\n\nAlonso & Marder (2020), \"Temperature compensation in a small rhythmic circuit\", eLife 9:e55470,\ndoi:10.7554/eLife.55470. The dataset (doi:10.5061/dryad.m31b1h7, version id 94811, the only\npublished version) is one zip, alonso_marder_tempcomp_2019_root.zip, holding the authors' Java model,\ntheir Python driver scripts, one initial-condition file (cis_network.txt) and one parameter file per\nmodel (p-<NAME>.score.<score>.txt, 132 numbers each). Dryad needs a token to download, so the\nworkflow stages the file under /tmp/dryad/m31b1h7/94811/ before the run (docs/archives.md, \"Dryad\");\nit is read there in place, into memory, and checked against the MD5 that Dryad's file list gives.\n\nWhere things come from:\n\n- The model is a line-by-line port of the deposited Java classes\n  PrinzNetworkWithTemperature_full_eu_slow_same_q10s_rk4.java (network, synapses, Q10 of the\n  synapses), singleCompTemperature_slow_explicit.java (each cell) and Integrador.java (RK4), into\n  numba. Parameter layout, per cell 37 numbers: 8 maximal conductances (Na, CaT, CaS, A, KCa, Kd, H,\n  leak), EL, ENa, EK, EH, 23 Q10 values (indices 12 to 34), tau_Ca / 10 (index 35), injected\n  current (36); then 7 synaptic conductances and 14 synaptic Q10 values, of which the Java uses\n  0 (glutamatergic g), 1 (cholinergic g), 7 (glutamatergic tau) and 8 (cholinergic tau). As in the\n  Java, the Q10 values of the PD (first) cell are used for all three cells. Choices kept from the\n  Java: C = 10, area 0.628, caF 0.94, Ca0 0.05 uM, [Ca]out 3000 uM, synaptic bound 20 ms,\n  Vth = -35 mV, Delta = 5 mV, Eglut = -70 mV, Echol = -80 mV, k = 1/40 and 1/100 per ms.\n- dt = 0.05 ms and RK4 (Materials and methods, The model, last paragraph; the Java drivers' dt\n  argument). Initial state cis_network.txt (V = -51 mV, gates 0, [Ca] = 5 uM, synapses 0), as the\n  Methods say.\n- Temperature ramps: the deposit holds no ramp code. The temperature is updated at every step,\n  linearly in time (an assumption; the Results give only the start, end and duration of a ramp).\n- Spike times: the paper and the deposit give no spike detection rule. A spike is an upward\n  crossing of SPIKE_THRESHOLD = -20 mV (an assumption, the standard choice for these models,\n  whose spikes peak well above 0 mV and whose slow waves stay below the -50 mV slow-wave threshold\n  of the Methods; a variant at 0 mV is computed where the claims rest on it).\n- Bursts and the classification scheme: Materials and methods, \"Classification scheme\": spiking\n  when CV of ISI < 0.1 (tonic when the lag d between spike onset and the -50 mV slow-wave crossing\n  is under 20 ms, else single-spike bursting); otherwise spikes grouped into bursts with a 200 ms\n  gap; regular bursting when CV(dc) < 1, CV(fb) < 0.1 and mean(dc) > 0; irregular bursting when\n  mean(dc) > 0 and CV(dc) > 1 or CV(fb) > 0.1; irregular spiking when mean(dc) = 0; quiescent when\n  there is no more than 1 ISI. Duty cycle is burst duration over period (Results, Duty cycle and\n  phase maintenance). The lag d is read as the time from each spike to the nearest preceding\n  downward... see `classify_cell`, which takes it as the median over spikes of the time from the\n  last upward crossing of -50 mV to the spike (an assumption: the Methods do not say how d is\n  formed).\n- Triphasic (Classification scheme): the three cells' burst frequencies within 5% and the cells\n  firing in the right order. The order is read as LP bursts starting before PY bursts within the\n  PD cycle: the median phase of LP onsets is below that of PY onsets, both in (0, 1) (an\n  assumption; the paper does not say how order is tested). `triphasic(..., strict=True)` asks it\n  of every cycle, a variant.\n- Currents (for currentscapes): the deposit's getCurrents.py computes the eight intrinsic currents\n  as g m^q h (V - E) times the area; the synaptic current into each cell is the sum of its\n  synapses' currents (as integratePyloricSQ10s_currentscapes_RK4_mp.py adds them). Shares follow\n  plotCurrentScape in plotPyloricTempUtils.py: positive currents (outward) over the sum of the\n  positive ones, negative (inward) over the sum of the negative ones.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport re\nimport zipfile\nfrom pathlib import Path\n\nimport numpy as np\nfrom numba import njit\n\nDRYAD_ID = \"m31b1h7\"\nDRYAD_VERSION = \"94811\"\nDRYAD_DOI = \"doi:10.5061/dryad.m31b1h7\"\nZIP_NAME = \"alonso_marder_tempcomp_2019_root.zip\"\nZIP_MD5 = \"37766522dabaaa620d4c44264e76e686\"  # Dryad file list, https://datadryad.org/api/v2/versions/94811/files\nSTAGED = Path(\"/tmp\") / \"dryad\" / DRYAD_ID / DRYAD_VERSION  # where the workflow stages the file\nROOT = \"alonso_marder_tempcomp_2019_root/\"\n\nDT = 0.05                 # ms, Methods\nSPIKE_THRESHOLD = -20.0   # mV, assumption (see module docstring)\nSLOW_WAVE = -50.0         # mV, Methods\nBURST_GAP = 0.2           # s, Methods, Classification scheme\nCURRENTS = [\"Na\", \"CaT\", \"CaS\", \"A\", \"KCa\", \"Kd\", \"H\", \"Leak\"]\nCELLS = [\"PD\", \"LP\", \"PY\"]\n\n\n# --- loading ----------------------------------------------------------------------------------\n\ndef read_zip_bytes() -> bytes:\n    return (STAGED / ZIP_NAME).read_bytes()\n\n\ndef digests(raw: bytes) -> dict:\n    md5 = hashlib.md5(raw).hexdigest()\n    if md5 != ZIP_MD5:\n        raise ValueError(f\"{ZIP_NAME}: MD5 {md5} differs from Dryad's file list ({ZIP_MD5})\")\n    return {\"md5\": md5, \"sha256\": hashlib.sha256(raw).hexdigest(), \"bytes\": len(raw)}\n\n\ndef open_zip(raw: bytes) -> zipfile.ZipFile:\n    return zipfile.ZipFile(io.BytesIO(raw))\n\n\ndef model_files(z: zipfile.ZipFile) -> dict:\n    \"\"\"Model name -> member name of its parameter file.\"\"\"\n    out = {}\n    for n in z.namelist():\n        m = re.match(re.escape(ROOT) + r\"parameters_and_ci/p-([A-Z0-9]{6})\\.score\\.([0-9.]+)\\.txt$\", n)\n        if m:\n            out[m.group(1)] = n\n    return dict(sorted(out.items()))\n\n\ndef read_vector(z: zipfile.ZipFile, member: str) -> np.ndarray:\n    return np.array([float(s) for s in z.read(member).decode().split()])\n\n\ndef load_models(z: zipfile.ZipFile) -> dict:\n    return {name: read_vector(z, member) for name, member in model_files(z).items()}\n\n\ndef load_ci(z: zipfile.ZipFile) -> np.ndarray:\n    return read_vector(z, ROOT + \"parameters_and_ci/cis_network.txt\")\n\n\ndef score_of(member: str) -> float:\n    return float(re.search(r\"\\.score\\.([0-9.]+)\\.txt$\", member).group(1))\n\n\ndef conductances(p: np.ndarray) -> np.ndarray:\n    \"\"\"3 x 8 maximal conductances (PD, LP, PY; CURRENTS order).\"\"\"\n    return np.array([p[37 * c:37 * c + 8] for c in range(3)])\n\n\ndef q10_conductances(p):\n    return p[[12, 15, 18, 21, 24, 27, 30, 33]]\n\n\ndef q10_timescales(p):\n    \"\"\"Q10 values the Java uses for time scales: 11 gating variables and tau_Ca.\"\"\"\n    return p[[13, 14, 16, 17, 19, 20, 31, 28, 25, 22, 23, 34]]\n\n\ndef q10_synapses(p):\n    return p[111 + 7 + np.array([0, 1, 7, 8])]\n\n\ndef scaled(p: np.ndarray, current: int, fraction: float) -> np.ndarray:\n    \"\"\"Copy of p with one intrinsic maximal conductance scaled in all three cells, as the deposit's\n    integratePyloricSQ10s_remove_gA_onesteps_twotemps_RK4.py does.\"\"\"\n    q = p.copy()\n    for c in range(3):\n        q[37 * c + current] *= fraction\n    return q\n\n\n# --- the model (port of the deposited Java) ---------------------------------------------------\n\n@njit(cache=True)\ndef _factors(p, T, f):\n    x = (T - 10.0) / 10.0\n    gi = (12, 15, 18, 21, 24, 27, 30, 33)\n    for k in range(8):\n        f[k] = p[gi[k]] ** x\n    ti = (13, 14, 16, 17, 19, 20, 31, 28, 25, 22, 23, 34)\n    for k in range(12):\n        f[8 + k] = p[ti[k]] ** (-x)\n    f[20] = p[118] ** x        # glutamatergic g\n    f[21] = p[119] ** x        # cholinergic g\n    f[22] = p[125] ** (-x)     # glutamatergic tau\n    f[23] = p[126] ** (-x)     # cholinergic tau\n    f[24] = T\n\n\n@njit(cache=True)\ndef _boltz(V, A, B):\n    return 1.0 / (1.0 + np.exp((V + A) / B))\n\n\n@njit(cache=True)\ndef _taux(V, CT, DT_, AT, BT):\n    return CT - DT_ / (1.0 + np.exp((V + AT) / BT))\n\n\n@njit(cache=True)\ndef _spectau(V, CT, DT_, AT, BT, AT2, BT2):\n    return CT + DT_ / (np.exp((V + AT) / BT) + np.exp((V + AT2) / BT2))\n\n\n@njit(cache=True)\ndef _syn_ss(Vpre):\n    return 1.0 / (1.0 + np.exp((-35.0 - Vpre) / 5.0))\n\n\n@njit(cache=True)\ndef _cell_currents(y, o, p, po, f, out):\n    \"\"\"The eight intrinsic currents (nA, positive outward) of the cell with state offset o and\n    parameter offset po.\"\"\"\n    V = y[o]\n    T = f[24]\n    caRev = ((8.314e3 * (273.15 + T)) / (2.0 * 96485.33)) * np.log(3000.0 / y[o + 12])\n    A = 0.628\n    out[0] = p[po + 0] * f[0] * y[o + 1] ** 3 * y[o + 2] * (V - p[po + 9]) * A\n    out[1] = p[po + 1] * f[1] * y[o + 3] ** 3 * y[o + 4] * (V - caRev) * A\n    out[2] = p[po + 2] * f[2] * y[o + 5] ** 3 * y[o + 6] * (V - caRev) * A\n    out[3] = p[po + 3] * f[3] * y[o + 10] ** 3 * y[o + 11] * (V - p[po + 10]) * A\n    out[4] = p[po + 4] * f[4] * y[o + 9] ** 4 * (V - p[po + 10]) * A\n    out[5] = p[po + 5] * f[5] * y[o + 8] ** 4 * (V - p[po + 10]) * A\n    out[6] = p[po + 6] * f[6] * y[o + 7] * (V - p[po + 11]) * A\n    out[7] = p[po + 7] * f[7] * (V - p[po + 8]) * A\n\n\n@njit(cache=True)\ndef _syn_currents(y, p, f, out):\n    \"\"\"Synaptic current into PD, LP and PY (nA, positive outward), as in the Java.\"\"\"\n    VAB, VLP, VPY = y[0], y[13], y[26]\n    s = y[39:46]\n    g = p[111:118]\n    out[0] = f[20] * g[6] * s[6] * (VAB + 70.0)\n    out[1] = (f[20] * g[2] * s[2] * (VLP + 70.0) + f[21] * g[3] * s[3] * (VLP + 80.0)\n              + f[20] * g[5] * s[5] * (VLP + 70.0))\n    out[2] = (f[20] * g[0] * s[0] * (VPY + 70.0) + f[21] * g[1] * s[1] * (VPY + 80.0)\n              + f[20] * g[4] * s[4] * (VPY + 70.0))\n\n\n@njit(cache=True)\ndef _rhs(y, p, f, dy, cur, syn):\n    _syn_currents(y, p, f, syn)\n    for c in range(3):\n        o = 13 * c\n        po = 37 * c\n        V = y[o]\n        _cell_currents(y, o, p, po, f, cur)\n        iapp = -(p[po + 36] + syn[c])\n        tot = 0.0\n        for k in range(8):\n            tot += cur[k]\n        dy[o] = (-tot + iapp) / 10.0\n        IntCa = y[o + 12]\n        dy[o + 1] = (_boltz(V, 25.5, -5.29) - y[o + 1]) / (_taux(V, 1.32, 1.26, 120.0, -25.0) * f[8])\n        dy[o + 2] = (_boltz(V, 48.9, 5.18) - y[o + 2]) / (\n            _taux(V, 0.0, -0.67, 62.9, -10.0) * _taux(V, 1.50, -1.00, 34.9, 3.60) * f[9])\n        dy[o + 3] = (_boltz(V, 27.1, -7.20) - y[o + 3]) / (_taux(V, 21.7, 21.3, 68.1, -20.5) * f[10])\n        dy[o + 4] = (_boltz(V, 32.1, 5.50) - y[o + 4]) / (_taux(V, 105.0, 89.8, 55.0, -16.9) * f[11])\n        dy[o + 5] = (_boltz(V, 33.0, -8.1) - y[o + 5]) / (_spectau(V, 1.40, 7.00, 27.0, 10.0, 70.0, -13.0) * f[12])\n        dy[o + 6] = (_boltz(V, 60.0, 6.20) - y[o + 6]) / (_spectau(V, 60.0, 150.0, 55.0, 9.00, 65.0, -16.0) * f[13])\n        dy[o + 7] = (_boltz(V, 70.0, 6.0) - y[o + 7]) / (_taux(V, 272.0, -1499.0, 42.2, -8.73) * f[14])\n        dy[o + 8] = (_boltz(V, 12.3, -11.8) - y[o + 8]) / (_taux(V, 7.20, 6.40, 28.3, -19.2) * f[15])\n        dy[o + 9] = ((IntCa / (IntCa + 3.0)) * _boltz(V, 28.3, -12.6) - y[o + 9]) / (\n            _taux(V, 90.3, 75.1, 46.0, -22.7) * f[16])\n        dy[o + 10] = (_boltz(V, 27.2, -8.70) - y[o + 10]) / (_taux(V, 11.6, 10.4, 32.9, -15.2) * f[17])\n        dy[o + 11] = (_boltz(V, 56.9, 4.90) - y[o + 11]) / (_taux(V, 38.6, 29.2, 38.9, -26.5) * f[18])\n        dy[o + 12] = (-0.94 * (cur[1] + cur[2]) - IntCa + 0.05) / (p[po + 35] * 10.0 * f[19])\n    VAB, VLP, VPY = y[0], y[13], y[26]\n    pre = (VAB, VAB, VAB, VAB, VLP, VPY, VLP)\n    glut = (True, False, True, False, True, True, True)\n    for k in range(7):\n        ss = _syn_ss(pre[k])\n        if glut[k]:\n            tau = f[22] * (1.0 - ss) * 40.0\n        else:\n            tau = f[23] * (1.0 - ss) * 100.0\n        dy[39 + k] = (ss - y[39 + k]) / (tau + 20.0)\n\n\n@njit(cache=True)\ndef _run(y0, p, T0, T1, nsteps, dt, thr, rec_every, rec_start, full, hist_start, hist_lo, hist_bin, nbins):\n    \"\"\"RK4 from y0 for nsteps; temperature linear from T0 to T1 over the run. Returns the final\n    state, upward crossings of thr per cell (time in ms, interpolated), upward and downward\n    crossings of -50 mV, the recorded traces (V of each cell, or the full state when `full`, every\n    rec_every steps from step rec_start) and voltage histograms from step hist_start.\"\"\"\n    n = y0.shape[0]\n    y = y0.copy()\n    k1 = np.empty(n); k2 = np.empty(n); k3 = np.empty(n); k4 = np.empty(n); tmp = np.empty(n)\n    cur = np.empty(8); syn = np.empty(3)\n    f = np.empty(25)\n    maxev = int(nsteps * dt / 2.0) + 16           # at most one event per 2 ms\n    spk = np.zeros((3, maxev)); nspk = np.zeros(3, np.int64)\n    swu = np.zeros((3, maxev)); nswu = np.zeros(3, np.int64)\n    swd = np.zeros((3, maxev)); nswd = np.zeros(3, np.int64)\n    nrec = 0\n    if rec_every > 0 and nsteps > rec_start:\n        nrec = (nsteps - rec_start + rec_every - 1) // rec_every\n    width = n if full else 3\n    rec = np.zeros((nrec, width))\n    hist = np.zeros((3, nbins))\n    ri = 0\n    ramp = T1 != T0\n    _factors(p, T0, f)\n    for i in range(nsteps):\n        if ramp:\n            _factors(p, T0 + (T1 - T0) * i / nsteps, f)\n        if rec_every > 0 and i >= rec_start and (i - rec_start) % rec_every == 0:\n            if full:\n                for j in range(n):\n                    rec[ri, j] = y[j]\n            else:\n                rec[ri, 0] = y[0]; rec[ri, 1] = y[13]; rec[ri, 2] = y[26]\n            ri += 1\n        if hist_start >= 0 and i >= hist_start:\n            for c in range(3):\n                b = int((y[13 * c] - hist_lo) / hist_bin)\n                if 0 <= b < nbins:\n                    hist[c, b] += 1\n        _rhs(y, p, f, k1, cur, syn)\n        for j in range(n):\n            tmp[j] = y[j] + 0.5 * dt * k1[j]\n        _rhs(tmp, p, f, k2, cur, syn)\n        for j in range(n):\n            tmp[j] = y[j] + 0.5 * dt * k2[j]\n        _rhs(tmp, p, f, k3, cur, syn)\n        for j in range(n):\n            tmp[j] = y[j] + dt * k3[j]\n        _rhs(tmp, p, f, k4, cur, syn)\n        for c in range(3):\n            v0 = y[13 * c]\n            o = 13 * c\n            v1 = y[o] + dt / 6.0 * (k1[o] + 2.0 * k2[o] + 2.0 * k3[o] + k4[o])\n            t0 = i * dt\n            if v0 < thr <= v1 and nspk[c] < maxev:\n                spk[c, nspk[c]] = t0 + dt * (thr - v0) / (v1 - v0); nspk[c] += 1\n            if v0 < -50.0 <= v1 and nswu[c] < maxev:\n                swu[c, nswu[c]] = t0 + dt * (-50.0 - v0) / (v1 - v0); nswu[c] += 1\n            if v0 >= -50.0 > v1 and nswd[c] < maxev:\n                swd[c, nswd[c]] = t0 + dt * (-50.0 - v0) / (v1 - v0); nswd[c] += 1\n        for j in range(n):\n            y[j] = y[j] + dt / 6.0 * (k1[j] + 2.0 * k2[j] + 2.0 * k3[j] + k4[j])\n    return y, spk, nspk, swu, nswu, swd, nswd, rec, hist\n\n\nclass Sim:\n    \"\"\"Result of one simulation. Times in seconds from the start of the run.\"\"\"\n\n    def __init__(self, out, dt, seconds, T0, T1, rec_every, rec_start, hist_lo, hist_bin):\n        y, spk, nspk, swu, nswu, swd, nswd, rec, hist = out\n        self.final = y\n        self.spikes = [spk[c, :nspk[c]] / 1000.0 for c in range(3)]\n        self.sw_up = [swu[c, :nswu[c]] / 1000.0 for c in range(3)]\n        self.sw_down = [swd[c, :nswd[c]] / 1000.0 for c in range(3)]\n        self.rec = rec\n        self.rec_dt = dt * rec_every / 1000.0\n        self.rec_t0 = rec_start * dt / 1000.0\n        self.hist = hist\n        self.hist_edges = hist_lo + hist_bin * np.arange(hist.shape[1] + 1)\n        self.seconds, self.T0, self.T1 = seconds, T0, T1\n\n    def temperature(self, t):\n        return self.T0 + (self.T1 - self.T0) * np.asarray(t) / self.seconds\n\n    def window(self, t0, t1):\n        \"\"\"Spike times of each cell within [t0, t1), shifted to start at 0.\"\"\"\n        return [s[(s >= t0) & (s < t1)] - t0 for s in self.spikes]\n\n\ndef simulate(p, temp, seconds, y0, temp_end=None, dt=DT, thr=SPIKE_THRESHOLD, rec_every=0,\n             rec_from=0.0, full=False, hist_from=None, hist_lo=-100.0, hist_bin=0.1, nbins=1600):\n    T1 = temp if temp_end is None else temp_end\n    nsteps = int(round(seconds * 1000.0 / dt))\n    rec_start = int(round(rec_from * 1000.0 / dt))\n    hs = -1 if hist_from is None else int(round(hist_from * 1000.0 / dt))\n    out = _run(np.asarray(y0, float), np.asarray(p, float), float(temp), float(T1), nsteps, dt, thr,\n               rec_every, rec_start, full, hs, hist_lo, hist_bin, nbins)\n    return Sim(out, dt, seconds, float(temp), float(T1), rec_every, rec_start, hist_lo, hist_bin)\n\n\ndef currents_from_states(states, p, temp):\n    \"\"\"Per cell: an array (9, n) of the 8 intrinsic currents and the synaptic current (nA,\n    positive outward), from full states recorded at a fixed temperature.\"\"\"\n    f = np.empty(25)\n    _factors(np.asarray(p, float), float(temp), f)\n    return _currents_loop(states, np.asarray(p, float), f)\n\n\n@njit(cache=True)\ndef _currents_loop(states, p, f):\n    n = states.shape[0]\n    out = np.zeros((3, 9, n))\n    cur = np.empty(8); syn = np.empty(3)\n    for i in range(n):\n        y = states[i]\n        _syn_currents(y, p, f, syn)\n        for c in range(3):\n            _cell_currents(y, 13 * c, p, 37 * c, f, cur)\n            for k in range(8):\n                out[c, k, i] = cur[k]\n            out[c, 8, i] = syn[c]\n    return out\n\n\ndef shares(curr):\n    \"\"\"Currentscape shares (plotCurrentScape): outward (positive) share of each current in the\n    total outward current, inward (negative) share in the total inward current. curr is (k, n).\"\"\"\n    pos = np.clip(curr, 0, None)\n    neg = np.clip(-curr, 0, None)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        out_sh = pos / pos.sum(axis=0)\n        in_sh = neg / neg.sum(axis=0)\n    return np.nan_to_num(out_sh), np.nan_to_num(in_sh)\n\n\n# --- spikes, bursts and the classification scheme ---------------------------------------------\n\ndef bursts(spikes, gap=BURST_GAP):\n    \"\"\"Group spike times into bursts with a temporal threshold (Methods): returns (starts, ends,\n    counts).\"\"\"\n    s = np.asarray(spikes)\n    if len(s) == 0:\n        return np.array([]), np.array([]), np.array([], int)\n    breaks = np.where(np.diff(s) > gap)[0]\n    first = np.r_[0, breaks + 1]\n    last = np.r_[breaks, len(s) - 1]\n    return s[first], s[last], last - first + 1\n\n\ndef burst_stats(spikes, gap=BURST_GAP):\n    \"\"\"Per cycle: burst frequency (1 / time between successive burst starts), duty cycle (burst\n    duration over period), as the Methods and the Results define them. The last burst is dropped\n    (no period).\"\"\"\n    st, en, cnt = bursts(spikes, gap)\n    if len(st) < 2:\n        return dict(starts=st, ends=en, counts=cnt, period=np.array([]), freq=np.array([]),\n                    dc=np.array([]))\n    period = np.diff(st)\n    dur = (en - st)[:-1]\n    return dict(starts=st, ends=en, counts=cnt, period=period, freq=1.0 / period, dc=dur / period)\n\n\ndef _cv(x):\n    x = np.asarray(x, float)\n    return np.std(x) / np.mean(x) if len(x) and np.mean(x) != 0 else np.inf\n\n\ndef classify_cell(spikes, sw_up):\n    \"\"\"Methods, Classification scheme. Returns one of: quiescent, tonic spiking, single-spike\n    bursting, regular bursting, irregular bursting, irregular spiking, other.\"\"\"\n    s = np.asarray(spikes)\n    if len(s) - 1 <= 1:\n        return \"quiescent\"\n    isi = np.diff(s)\n    if _cv(isi) < 0.1:\n        # lag d between spike onset and the last upward slow-wave crossing before it\n        up = np.asarray(sw_up)\n        idx = np.searchsorted(up, s) - 1\n        lags = np.where(idx >= 0, s - up[np.clip(idx, 0, None)], np.inf)\n        d = np.median(lags)\n        return \"tonic spiking\" if d < 0.020 else \"single-spike bursting\"\n    b = burst_stats(s)\n    if len(b[\"dc\"]) == 0:\n        return \"other\"\n    mdc = np.mean(b[\"dc\"])\n    if mdc > 0 and _cv(b[\"dc\"]) < 1 and _cv(b[\"freq\"]) < 0.1:\n        return \"regular bursting\"\n    if mdc > 0 and (_cv(b[\"dc\"]) > 1 or _cv(b[\"freq\"]) > 0.1):\n        return \"irregular bursting\"\n    if mdc == 0:\n        return \"irregular spiking\"\n    return \"other\"\n\n\ndef phases(spk3):\n    \"\"\"Burst onsets and offsets of LP and PY (and PD offset) in units of the PD period, from each\n    PD burst start, per PD cycle; nan where a cell has no burst start in the cycle.\"\"\"\n    pd = burst_stats(spk3[0])\n    out = {k: [] for k in [\"PD off\", \"LP on\", \"LP off\", \"PY on\", \"PY off\"]}\n    bl = burst_stats(spk3[1]); bp = burst_stats(spk3[2])\n    st = pd[\"starts\"]\n    for i in range(len(st) - 1):\n        t0, T = st[i], st[i + 1] - st[i]\n        out[\"PD off\"].append((pd[\"ends\"][i] - t0) / T)\n        for name, b in ((\"LP\", bl), (\"PY\", bp)):\n            k = np.where((b[\"starts\"] >= t0) & (b[\"starts\"] < st[i + 1]))[0]\n            if len(k):\n                out[name + \" on\"].append((b[\"starts\"][k[0]] - t0) / T)\n                out[name + \" off\"].append((b[\"ends\"][k[0]] - t0) / T)\n            else:\n                out[name + \" on\"].append(np.nan)\n                out[name + \" off\"].append(np.nan)\n    return {k: np.array(v) for k, v in out.items()}\n\n\ndef triphasic(spk3, strict=False):\n    \"\"\"Methods: triphasic when the three cells' burst frequencies agree within 5% and they fire in\n    the right order (PD, LP, PY). Frequencies are each cell's mean burst frequency; agreement is\n    (max - min) / max <= 0.05. Order (an assumption) as in the module docstring.\"\"\"\n    fr = []\n    for s in spk3:\n        b = burst_stats(s)\n        if len(b[\"freq\"]) < 2:\n            return False\n        fr.append(np.mean(b[\"freq\"]))\n    fr = np.array(fr)\n    if (fr.max() - fr.min()) / fr.max() > 0.05:\n        return False\n    ph = phases(spk3)\n    lp, py = ph[\"LP on\"], ph[\"PY on\"]\n    if strict:\n        return bool(np.all(np.isfinite(lp)) and np.all(np.isfinite(py)) and np.all(lp < py))\n    if np.mean(np.isfinite(lp)) < 0.5 or np.mean(np.isfinite(py)) < 0.5:\n        return False\n    a, b = np.nanmedian(lp), np.nanmedian(py)\n    return bool(0 < a < b < 1)\n\n\ndef classify(sim, t0, t1):\n    \"\"\"Cell classes of PD, LP, PY and the network class over [t0, t1) of a simulation.\"\"\"\n    spk = sim.window(t0, t1)\n    sw = [u[(u >= t0) & (u < t1)] - t0 for u in sim.sw_up]\n    cls = [classify_cell(spk[c], sw[c]) for c in range(3)]\n    net = \"triphasic\" if triphasic(spk) else \"not triphasic\"\n    return cls + [net]\n"
}
```

```
File created successfully at: entries/alonso-2020/pyloric.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/z/alonso_marder_tempcomp_2019_root && javac ./standaloneCodePyloricTempComp/*java 2>&1 | tail -3; time java -cp . standaloneCodePyloricTempComp.integratePyloricNetwork_slow_full_temp_sameq10s_rk4 ./parameters_and_ci/cis_network.txt ./parameters_and_ci/p-4X6W66.score.32.736714734.txt 3 18 0.05 > $TMPDIR/j.txt; wc -l $TMPDIR/j.txt
```

```
real	0m0.701s
user	0m0.972s
sys	0m0.167s
60000 /tmp/claude-1001/j.txt
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && source $TMPDIR/dev/bin/activate && python -c "
import time, numpy as np, pyloric as P
raw=P.read_zip_bytes(); print(P.digests(raw)); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
print(len(M), list(M)[:5], ci.shape)
p=M['4X6W66']
t=time.time(); s=P.simulate(p,18,3,ci,rec_every=1); print('first',time.time()-t)
t=time.time(); s=P.simulate(p,18,20,ci); print('20s',time.time()-t)
s=P.simulate(p,18,3,ci,rec_every=1)
j=np.loadtxt('$TMPDIR/j.txt'); print(j.shape, s.rec.shape, np.abs(j-s.rec).max(), np.abs(j-s.rec)[:20000].max())
"
```

```
{'md5': '37766522dabaaa620d4c44264e76e686', 'sha256': '327279e2c4553c0b946bf230260caf0f7321e36bc5201ad7d65bbe6638d2df08', 'bytes': 99026}
38 ['0SHNMD', '2RO5K6', '4R2719', '4X6W66', '71G6LA'] (46,)
first 2.052701950073242
20s 0.690650463104248
(60000, 3) (60000, 3) 3.087872180174145e-09 2.437996471371662e-10
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && sed -i 's/@njit(cache=True)/@njit(cache=True, fastmath=True)/' pyloric.py && source $TMPDIR/dev/bin/activate && python -c "
import time, numpy as np, pyloric as P
raw=P.read_zip_bytes(); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
p=M['4X6W66']
s=P.simulate(p,18,3,ci,rec_every=1)
t=time.time(); s=P.simulate(p,18,20,ci); print('20s',time.time()-t)
t=time.time(); s2=P.simulate(p,10,20,ci,temp_end=25); print('20s ramp',time.time()-t)
s=P.simulate(p,18,3,ci,rec_every=1)
j=np.loadtxt('$TMPDIR/j.txt'); print(np.abs(j-s.rec).max())
"
```

```
Exit code 1
/bin/bash: line 1: cd: entries/alonso-2020: No such file or directory
```

**Agent calls Bash**

```bash
sed -i 's/@njit(cache=True)/@njit(cache=True, fastmath=True)/' pyloric.py && source $TMPDIR/dev/bin/activate && python -c "
import time, numpy as np, pyloric as P
raw=P.read_zip_bytes(); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
p=M['4X6W66']
s=P.simulate(p,18,3,ci,rec_every=1)
t=time.time(); s=P.simulate(p,18,20,ci); print('20s',time.time()-t)
t=time.time(); s2=P.simulate(p,10,20,ci,temp_end=25); print('20s ramp',time.time()-t)
s=P.simulate(p,18,3,ci,rec_every=1)
j=np.loadtxt('$TMPDIR/j.txt'); print(np.abs(j-s.rec).max())
"
```

```
20s 0.6275744438171387
20s ramp 0.7090826034545898
1.0898190794250695e-08
```

**Agent calls Bash**

```bash
sed -i 's/@njit(cache=True, fastmath=True)/@njit(cache=True)/' pyloric.py && source $TMPDIR/dev/bin/activate && python -c "
import time, numpy as np, pyloric as P
raw=P.read_zip_bytes(); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
names=list(M)
G=np.array([np.r_[P.conductances(M[n]).ravel(), M[n][[35,72,109]], M[n][111:118]] for n in names])
Q=np.array([M[n][12:35] for n in names])
# identical G?
from itertools import combinations
for a,b in combinations(range(len(names)),2):
    if np.allclose(G[a],G[b]): print('same G',names[a],names[b], np.allclose(Q[a],Q[b]))
    if np.allclose(Q[a],Q[b]): print('same Q',names[a],names[b])
# q10 of cells 2,3 equal to cell1?
print(all(np.allclose(M[n][12:35],M[n][49:72]) and np.allclose(M[n][12:35],M[n][86:109]) for n in names))
print('inj', set(float(M[n][36]) for n in names), set(float(M[n][73]) for n in names))
print('E', set(tuple(M[n][8:12]) for n in names))
qs=np.array([P.q10_conductances(M[n]) for n in names]); qt=np.array([P.q10_timescales(M[n]) for n in names]); qsyn=np.array([P.q10_synapses(M[n]) for n in names])
print(qs.min(),qs.max(),qt.min(),qt.max(),qsyn.min(axis=0),qsyn.max(axis=0))
print('unused q10', np.unique(np.array([M[n][[26,29,32]] for n in names])), np.unique(np.array([M[n][118+np.array([2,3,4,5,6,9,10,11,12,13])] for n in names])))
"
```

```
same G 0SHNMD B7SD0L False
same G 0SHNMD LE8W3F False
same G 2RO5K6 KMNLBC False
same G 4R2719 WWZ3CN False
same G 4X6W66 EF84RN False
same G 4X6W66 FGFKQS False
same G 72TVF2 P1LH61 False
same G B7SD0L LE8W3F False
same G EF84RN FGFKQS False
same G HX40PF OPLRCP False
same G J9U8SQ TGCEVM False
same G Q0H92I R2PNKE False
same G RMZ8KZ VNROH5 False
True
inj {0.0} {0.0}
E {(np.float64(-50.0), np.float64(30.0), np.float64(-80.0), np.float64(-20.0))}
1.0 1.4985 1.0 3.973 [1.002 1.012 1.621 1.318] [1.489 1.499 3.997 3.91 ]
unused q10 [1.] [1.]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python -c "
import time, numpy as np, pyloric as P
from multiprocessing import Pool
raw=P.read_zip_bytes(); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
def job(n):
    s=P.simulate(M[n],10,20,ci)
    spk=s.window(10,20)
    out=[n]
    for c in range(3):
        b=P.burst_stats(spk[c]); out+= [round(np.mean(b['freq']),3) if len(b['freq']) else None, round(np.mean(b['dc']),3) if len(b['dc']) else None]
    return out+P.classify(s,10,20)
t=time.time()
with Pool(4) as pool: R=pool.map(job,list(M))
print(time.time()-t)
for r in R: print(r)
"
```

```
15.257721900939941
['0SHNMD', np.float64(1.065), np.float64(0.224), np.float64(1.069), np.float64(0.236), np.float64(1.069), np.float64(0.248), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['2RO5K6', np.float64(1.1), np.float64(0.205), np.float64(1.115), np.float64(0.229), np.float64(1.1), np.float64(0.217), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['4R2719', np.float64(0.99), np.float64(0.142), np.float64(0.987), np.float64(0.292), np.float64(0.987), np.float64(0.217), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['4X6W66', np.float64(1.067), np.float64(0.218), np.float64(1.088), np.float64(0.266), np.float64(1.064), np.float64(0.231), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['71G6LA', np.float64(1.303), np.float64(0.192), np.float64(1.302), np.float64(0.208), np.float64(1.338), np.float64(0.236), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['72TVF2', np.float64(1.377), np.float64(0.208), np.float64(1.376), np.float64(0.192), np.float64(1.407), np.float64(0.206), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['B7SD0L', np.float64(1.065), np.float64(0.224), np.float64(1.069), np.float64(0.236), np.float64(1.069), np.float64(0.248), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['CG4J30', np.float64(1.266), np.float64(0.16), np.float64(1.262), np.float64(0.199), np.float64(1.298), np.float64(0.27), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['ED50XO', np.float64(1.005), np.float64(0.224), np.float64(1.001), np.float64(0.263), np.float64(1.031), np.float64(0.176), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['EF84RN', np.float64(1.067), np.float64(0.218), np.float64(1.088), np.float64(0.266), np.float64(1.064), np.float64(0.231), 'regular bursting', 'regular bursting', 'regular bursting', 'triphasic']
['FGFKQS
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^Figure [0-9]*\. " paper/10.7554-elife.55470.txt; sed -n 120,149p paper/10.7554-elife.55470.txt; grep -n "Figure 8\. \|Figure 9\. \|Figure 10\. " -A8 paper/10.7554-elife.55470.txt | head -60; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/alonso-2020/pyloric.py",
 "old_string": "  phase maintenance). The lag d is read as the time from each spike to the nearest preceding\n  downward... see `classify_cell`, which takes it as the median over spikes of the time from the\n  last upward crossing of -50 mV to the spike (an assumption: the Methods do not say how d is\n  formed).",
 "new_string": "  phase maintenance). The lag d is taken as the median over spikes of the time from the last\n  upward crossing of -50 mV to the spike (an assumption: the Methods do not say how d is formed).\n  The classes are computed over the analysed window only."
}
```

```
The file entries/alonso-2020/pyloric.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && uv pip install -q jupytext nbconvert ipykernel 2>&1 | tail -1; jupytext --version
```

```
1.19.7
```

**Agent calls Bash**

```bash
cat >> entries/alonso-2020/pyloric.py <<'EOF'


# --- parallel jobs (run in worker processes) ---------------------------------------------------

def pmap(fn, tasks, procs=4):
    """Map fn over tasks in `procs` processes (the runner has 4 CPUs)."""
    from multiprocessing import get_context
    with get_context("fork").Pool(procs) as pool:
        return pool.map(fn, tasks, chunksize=1)


def run_fixed(task):
    """task = (key, p, y0, temp, seconds, drop). Simulates at a fixed temperature and returns, for
    the window after `drop` seconds, the spike times and upward slow-wave crossings of each cell
    (times from the window start), the four classes, and the final state."""
    key, p, y0, temp, seconds, drop = task
    s = simulate(p, temp, seconds, y0)
    return dict(key=key, temp=temp, spikes=s.window(drop, seconds),
                sw_up=[u[u >= drop] - drop for u in s.sw_up], classes=classify(s, drop, seconds),
                final=s.final, length=seconds - drop)


def run_states(task):
    """task = (key, p, y0, temp, seconds, record). Simulates and returns the full state at every
    step of the last `record` seconds, with the spike times in that window (times from its
    start)."""
    key, p, y0, temp, seconds, record = task
    s = simulate(p, temp, seconds, y0, rec_every=1, rec_from=seconds - record, full=True)
    return dict(key=key, temp=temp, states=s.rec, dt=s.rec_dt,
                spikes=s.window(seconds - record, seconds), classes=classify(s, seconds - record, seconds))


def run_ramp(task):
    """task = (key, p, y0, legs), legs a list of (T_start, T_end, seconds). Runs the legs one after
    the other from y0 and returns per leg the spike times (s from the leg start) and temperatures
    of the spikes."""
    key, p, y0, legs = task
    y = np.asarray(y0, float)
    out = []
    for T0, T1, sec in legs:
        s = simulate(p, T0, sec, y, temp_end=T1)
        out.append(dict(T0=T0, T1=T1, seconds=sec, spikes=s.spikes, sw_up=s.sw_up))
        y = s.final
    return dict(key=key, legs=out)


def peaks_after(V, idx, n):
    """Index of the maximum of V in the n samples after each index in idx."""
    return np.array([i + int(np.argmax(V[i:i + n])) for i in idx if i + n <= len(V)], int)


def dominant_summary(task):
    """currentscapes-dominant-currents, in a worker: simulate, compute shares and count, per cell,
    the spikes where Na holds the largest inward share in the 1 ms before the peak and Kd the
    largest outward share in the 1 ms after it, and the largest inward and outward currents over
    the 5% of time with the lowest voltage."""
    key, p, y0, temp, seconds, record = task
    r = run_states((key, p, y0, temp, seconds, record))
    st = r["states"]
    curr = currents_from_states(st, p, temp)
    n1 = int(round(0.001 / r["dt"]))
    res = []
    for c in range(3):
        V = st[:, 13 * c]
        out_sh, in_sh = shares(curr[c])
        cross = np.where((V[:-1] < SPIKE_THRESHOLD) & (V[1:] >= SPIKE_THRESHOLD))[0]
        pk = peaks_after(V, cross, int(round(0.003 / r["dt"])))
        pk = pk[(pk - n1 >= 0) & (pk + n1 < len(V))]
        na = kd = 0
        for i in pk:
            na += int(np.argmax(in_sh[:, i - n1:i].mean(axis=1)) == 0)
            kd += int(np.argmax(out_sh[:, i:i + n1].mean(axis=1)) == 5)
        low = V <= np.quantile(V, 0.05)
        top_in = int(np.argmax(in_sh[:, low].mean(axis=1)))
        top_out = int(np.argmax(out_sh[:, low].mean(axis=1)))
        both = np.maximum(in_sh[:, low].mean(axis=1), out_sh[:, low].mean(axis=1))
        res.append(dict(cell=CELLS[c], spikes=len(pk), na_first=na, kd_after=kd, low_in=top_in,
                        low_out=top_out, low_top2=sorted(np.argsort(both)[-2:].tolist())))
    return dict(key=key, temp=temp, cells=res, classes=r["classes"])
EOF
date -u
```

```
Fri Nov 27 22:22:02 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/alonso-2020/reproduce_alonso_2020.py",
 "content": "# %% [markdown]\n# # Reproducing Alonso & Marder (2020) from Dryad m31b1h7\n#\n# Paper: Alonso LM, Marder E (2020). Temperature compensation in a small rhythmic circuit. eLife\n# 9:e55470, doi:10.7554/eLife.55470. The claims file, `claims/alonso-2020.yaml`, was written from\n# the version of record (main text, legends and Methods; the figure supplements' legends were not\n# in the text read).\n#\n# Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811, one file,\n# `alonso_marder_tempcomp_2019_root.zip` (99,026 bytes, MD5 37766522dabaaa620d4c44264e76e686 from\n# Dryad's file list; its SHA-256 is printed below). Version 94811 is pinned because it is the only\n# published version of the dataset (the versions list of the API gives one, published 2020-12-07),\n# and the paper cites the dataset by its DOI, which resolves to it. Dryad needs a token to\n# download, so the workflow stages the file before the run and the notebook reads it in place,\n# into memory (docs/archives.md, \"Dryad\").\n#\n# The paper has no recordings. The dataset holds the authors' Java model, Python driver scripts,\n# initial conditions and the parameters of each model network. Every claim is tested by simulating\n# the deposited models with a numba port of the deposited Java (`pyloric.py`), checked against the\n# Java below when a Java compiler is present.\n#\n# This is the first of three notebooks. `ramps.ipynb` tests the claims on temperature ramps\n# (figs2-ramp-largest-isi, figs3-duty-cycle-variable-across-models, fig8a-hysteresis-quiescence,\n# fig8-up-down-ramps, fig8b-pathological-attractor) and `voltage_distributions.ipynb` the claims\n# on membrane potential distributions (fig2-lp-spike-amplitude-threshold,\n# fig2s1-peak-voltage-diverse).\n#\n# | Claim | Notebook | Tested |\n# |---|---|---|\n# | deposit-models | this | tested |\n# | fig1c-frequency-q10-phase-constant | this | tested |\n# | fig1s1-three-models | this | tested |\n# | all-models-compensated | this | tested |\n# | intermediate-temperature-failures | this | blocked (data_missing) |\n# | figs2-ramp-largest-isi | ramps | tested |\n# | figs3-duty-cycle-variable-across-models | ramps | tested |\n# | fig2-lp-spike-amplitude-threshold | voltage_distributions | tested |\n# | fig2s1-peak-voltage-diverse | voltage_distributions | tested |\n# | fig3-current-amplitudes | this | tested |\n# | fig4-currentscapes-reorganize | this | tested |\n# | currentscapes-dominant-currents | this | tested |\n# | fig5-a-to-kca-tradeoff | this | tested |\n# | fig6-crash-different-mechanisms | this | tested |\n# | fig6s1-crash-mechanisms | this | tested (7 of 8 models) |\n# | fig7-high-temperature-slow-timescales | this | blocked (data_missing, 3 of 5 models absent) |\n# | fig8a-hysteresis-quiescence | ramps | tested |\n# | fig8-up-down-ramps | ramps | tested |\n# | fig8b-pathological-attractor | ramps | tested |\n# | fig9a-remove-a-current | this | tested |\n# | fig9b-remove-kca-current | this | tested |\n# | fig10a-graded-removal | this | tested |\n# | fig10b-complete-removal-differs | this | tested |\n\n# %%\nimport os\nimport re\nimport resource\nimport shutil\nimport subprocess\nimport tempfile\nimport time\nfrom collections import Counter\nfrom itertools import combinations\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\n\nimport pyloric as P\n\nT_START = time.time()\npd.set_option(\"display.width\", 200, \"display.max_columns\", 40, \"display.max_rows\", 200)\n\nraw = P.read_zip_bytes()\nDIG = P.digests(raw)\nZ = P.open_zip(raw)\nMODELS = P.load_models(Z)\nFILES = P.model_files(Z)\nCI = P.load_ci(Z)\nNAMES = list(MODELS)\nprint(DIG)\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nmembers = [i for i in Z.infolist() if not i.filename.startswith(\"__MACOSX/\")]\nprint(f\"{len(Z.infolist())} members in the zip, {len(members)} outside __MACOSX/\")\nfor i in members:\n    print(f\"  {i.filename:110s} {i.file_size:7d}\")\nprint()\nprint(\"parameter files:\", len(FILES), \"models\")\nlengths = Counter(len(p) for p in MODELS.values())\nprint(\"numbers per parameter file:\", dict(lengths), \"(3 cells x 37 + 7 synaptic g + 14 synaptic Q10 = 132)\")\nprint(\"initial conditions:\", len(CI), \"numbers; per cell V, 11 gates, [Ca]:\")\nfor c in range(3):\n    print(\"  \", P.CELLS[c], CI[13 * c:13 * c + 13])\nprint(\"   synapses\", CI[39:])\nG = pd.DataFrame({n: P.conductances(MODELS[n]).ravel() for n in NAMES},\n                 index=[f\"{c} g{k}\" for c in P.CELLS for k in P.CURRENTS]).T\nprint(\"\\nmaximal conductances (uS), range over models:\")\nprint(G.agg([\"min\", \"max\"]).T.to_string())\ntauca = pd.DataFrame({n: MODELS[n][[35, 72, 109]] * 10 for n in NAMES}, index=[\"PD\", \"LP\", \"PY\"]).T\nprint(\"\\ntau_Ca (ms; the files hold tau_Ca / 10 and the Java multiplies by 10):\")\nprint(tauca.agg([\"min\", \"max\"]).to_string())\nprint(\"\\nsynaptic conductances (uS), range:\", np.round(np.min([MODELS[n][111:118] for n in NAMES], 0), 4),\n      np.round(np.max([MODELS[n][111:118] for n in NAMES], 0), 4))\nrev = {tuple(MODELS[n][37 * c + 8:37 * c + 12]) for n in NAMES for c in range(3)}\nprint(\"reversal potentials (EL, ENa, EK, EH), all cells and models:\", rev)\nprint(\"injected current, all cells and models:\", {MODELS[n][37 * c + 36] for n in NAMES for c in range(3)})\nsame_q = all(np.array_equal(MODELS[n][12:35], MODELS[n][49:72]) and np.array_equal(MODELS[n][12:35], MODELS[n][86:109])\n             for n in NAMES)\nprint(\"Q10 values identical in the three cells of every model:\", same_q)\n\n# %% [markdown]\n# Check of the search space of the Methods (Finding parameters): gNa and gKCa in [0, 1000], the\n# other intrinsic conductances in [0, 100], leak in [0, 10], tau_Ca in [0, 2000] ms, synapses in\n# [0, 0.05] uS.\n\n# %%\nlim = {\"gNa\": 1000, \"gCaT\": 100, \"gCaS\": 100, \"gA\": 100, \"gKCa\": 1000, \"gKd\": 100, \"gH\": 100, \"gLeak\": 10}\nover = [(n, col, G.loc[n, col]) for n in NAMES for col in G.columns if G.loc[n, col] > lim[col.split()[1]]]\nprint(\"intrinsic conductances outside the stated search space:\", len(over))\nfor o in over[:20]:\n    print(\"  \", o)\nprint(\"tau_Ca outside [0, 2000] ms:\", int((tauca.values > 2000).sum()), \"of\", tauca.size,\n      \"; max\", tauca.values.max())\nsyn = np.array([MODELS[n][111:118] for n in NAMES])\nprint(\"synaptic conductances above 0.05 uS:\", int((syn > 0.05).sum()), \"of\", syn.size, \"; max\", syn.max())\n\n# %% [markdown]\n# The port. The deposit's Java is compiled into a temporary directory (outside the dataset) and\n# run for 3 s at 18 degrees C on one model, when a Java compiler is installed; the port's voltage\n# traces are compared with its output. The port was also checked this way while preparing.\n\n# %%\ndef java_check(name=\"4X6W66\", seconds=3, temp=18):\n    if not (shutil.which(\"javac\") and shutil.which(\"java\")):\n        print(\"no Java compiler here; comparison not run\")\n        return None\n    with tempfile.TemporaryDirectory() as d:\n        src = [m for m in Z.namelist() if m.startswith(P.ROOT + \"standaloneCodePyloricTempComp/\") and m.endswith(\".java\")]\n        pkg = Path(d) / \"standaloneCodePyloricTempComp\"\n        pkg.mkdir()\n        for m in src:\n            (pkg / Path(m).name).write_bytes(Z.read(m))\n        (Path(d) / \"ci.txt\").write_bytes(Z.read(P.ROOT + \"parameters_and_ci/cis_network.txt\"))\n        (Path(d) / \"p.txt\").write_bytes(Z.read(FILES[name]))\n        subprocess.run([\"javac\"] + [str(pkg / Path(m).name) for m in src], check=True, cwd=d)\n        out = subprocess.run([\"java\", \"-cp\", d, \"standaloneCodePyloricTempComp.integratePyloricNetwork_slow_full_temp_sameq10s_rk4\",\n                              \"ci.txt\", \"p.txt\", str(seconds), str(temp), \"0.05\"], cwd=d, capture_output=True,\n                             text=True, check=True).stdout\n    j = np.array([[float(x) for x in line.split()] for line in out.strip().splitlines()])\n    s = P.simulate(MODELS[name], temp, seconds, CI, rec_every=1)\n    print(f\"{name}, {seconds} s at {temp} C: Java {j.shape}, port {s.rec.shape}; \"\n          f\"largest difference in V {np.abs(j - s.rec).max():.2e} mV\")\n    return np.abs(j - s.rec).max()\n\njava_diff = java_check()\n\n# %% [markdown]\n# ### Model names: the Methods' list against the deposit\n#\n# The Methods (Parameters used in this study) name 25 models. The deposit's file names are\n# compared with them exactly, and then allowing the letter O for the digit 0 and a swap of two\n# neighbouring characters.\n\n# %%\nMETHODS_NAMES = {\n    \"Figure 1\": [\"4?6W66\"], \"Figure 1-S1\": [\"WWZ3CN\", \"FGFKQS\", \"71G6LA\"], \"Figure 1-S2\": [\"PLKTEM\"],\n    \"Figure 2\": [\"G7P2WE\"], \"Figure 2-S1\": [\"G7P2WE\", \"4?6W66\", \"MAXTTP\"], \"Figure 3\": [\"4?6W66\", \"SJR46Y\"],\n    \"Figure 4\": [\"WWZ3CN\"], \"Figure 5\": [\"FGFKQS\"], \"Figure 6\": [\"FGFKQS\", \"71G6LA\"],\n    \"Figure 6-S1\": [\"B7SDOL\", \"J9U8SQ\", \"4R2719\", \"R3VIEW\", \"Q8FBN1\", \"RMZ8KZ\", \"EF84RN\", \"SJR46Y\"],\n    \"Figure 7\": [\"J9U8SQ\", \"G81PUL\", \"G7EOZ8\", \"SAXT8Y\", \"KNMLBC\"], \"Figure 8\": [\"OSHNMD\", \"H5AIZR\"],\n    \"Figure 9\": [\"WWZ3CN\", \"FGFKQS\"], \"Figure 10\": [\"4?6W66\"],\n}\n\ndef norm(s):\n    return s.replace(\"O\", \"0\")\n\ndef match(name):\n    if name in MODELS:\n        return name, \"exact\"\n    pat = re.compile(\"^\" + norm(name).replace(\"?\", \".\") + \"$\")\n    hits = [n for n in NAMES if pat.match(norm(n))]\n    if len(hits) == 1:\n        return hits[0], \"O read as 0\" if \"?\" not in name else \"unreadable character matched\"\n    for n in NAMES:\n        a, b = norm(name), norm(n)\n        d = [i for i in range(6) if a[i] != b[i]]\n        if len(d) == 2 and d[1] == d[0] + 1 and a[d[0]] == b[d[1]] and a[d[1]] == b[d[0]]:\n            return n, \"two characters swapped\"\n    return None, \"not in the deposit\"\n\nuniq = sorted({n for v in METHODS_NAMES.values() for n in v})\nname_map = pd.DataFrame([(n, *match(n), \", \".join(k for k, v in METHODS_NAMES.items() if n in v)) for n in uniq],\n                        columns=[\"Methods\", \"deposit\", \"how\", \"figures\"])\nprint(name_map.to_string(index=False))\nM = {r.Methods: r.deposit for r in name_map.itertuples()}\nprint(\"\\nmodels in the deposit:\", len(NAMES), \"; named in the Methods and found:\", name_map.deposit.notna().sum(),\n      \"of\", len(name_map))\n\n# %% tags=[\"finding-model-names\"]\n# Four models the Methods name are not in the deposit, and four others are filed under other spellings.\nprint(\"deposit:\", len(P.model_files(Z)), \"parameter files;\", sorted(P.model_files(Z)))\nfor n in [\"Q8FBN1\", \"G81PUL\", \"G7EOZ8\", \"SAXT8Y\", \"OSHNMD\", \"B7SDOL\", \"KNMLBC\"]:\n    print(f\"  {n}: in deposit {n in P.model_files(Z)}\")\n\n# %% [markdown]\n# ### Models with the same maximal conductances\n#\n# The Results say 36 sets of maximal conductances were selected and Q10 values searched for each.\n# Models whose 31 conductances and three tau_Ca are identical are grouped here.\n\n# %% tags=[\"finding-shared-conductances\"]\nkey = {n: tuple(np.r_[P.conductances(MODELS[n]).ravel(), MODELS[n][[35, 72, 109]], MODELS[n][111:118]]) for n in NAMES}\ngroups = {}\nfor n in NAMES:\n    groups.setdefault(key[n], []).append(n)\nmulti = [g for g in groups.values() if len(g) > 1]\nprint(f\"{len(NAMES)} models, {len(groups)} distinct sets of maximal conductances; \"\n      f\"{len(multi)} sets carry more than one Q10 set:\")\nfor g in multi:\n    q = np.array([MODELS[n][12:35] for n in g])\n    print(f\"  {g}: Q10 sets differ: {not np.all(q == q[0])}\")\n\n# %% [markdown]\n# ## deposit-models\n#\n# > The deposit holds the code and the parameters of the paper's models, under the names the\n# > Methods give, and simulating them at 10 degrees C gives the control rhythm the models were\n# > fitted to, about 1 Hz with a PD duty cycle near 20% and LP and PY duty cycles near 25%.\n#\n# Each model simulated 20 s at 10 degrees C from the deposited initial conditions; the first 10 s\n# dropped (criterion). Burst frequency and duty cycle are per-cycle means (Methods, Finding\n# parameters, \"the average burst frequency\" and \"the average duty cycle\").\n\n# %% tags=[\"claim:deposit-models\"]\nr10 = P.pmap(P.run_fixed, [(n, MODELS[n], CI, 10.0, 20.0, 10.0) for n in NAMES])\nrows = []\nfor r in r10:\n    row = {\"model\": r[\"key\"]}\n    for c, cell in enumerate(P.CELLS):\n        b = P.burst_stats(r[\"spikes\"][c])\n        row[f\"f {cell}\"] = np.mean(b[\"freq\"]) if len(b[\"freq\"]) else np.nan\n        row[f\"dc {cell}\"] = np.mean(b[\"dc\"]) if len(b[\"dc\"]) else np.nan\n    row[\"NET\"] = r[\"classes\"][3]\n    rows.append(row)\nd10 = pd.DataFrame(rows).set_index(\"model\")\nok_f = d10[[f\"f {c}\" for c in P.CELLS]].sub(1.0).abs().le(0.1).all(axis=1)\nok_pd = d10[\"dc PD\"].sub(0.2).abs().le(0.02)\nok_lppy = d10[[\"dc LP\", \"dc PY\"]].sub(0.25).abs().le(0.025).all(axis=1)\nok_lppy20 = d10[[\"dc LP\", \"dc PY\"]].sub(0.2).abs().le(0.02).all(axis=1)\nd10[\"f ok\"], d10[\"PD dc ok\"], d10[\"LP PY dc ok (0.25)\"], d10[\"LP PY dc ok (0.20)\"] = ok_f, ok_pd, ok_lppy, ok_lppy20\nprint(d10.round(3).to_string())\nprint(\"\\nranges at 10 C:\", {c: (round(d10[c].min(), 3), round(d10[c].max(), 3)) for c in d10.columns[:6]})\nn_all = int((ok_f & ok_pd & ok_lppy).sum())\nn_all20 = int((ok_f & ok_pd & ok_lppy20).sum())\nprint(f\"\\nwithin tolerance on all values (LP, PY target 0.25): {n_all} of {len(d10)}\")\nprint(f\"within tolerance on all values (LP, PY target 0.20, variant): {n_all20} of {len(d10)}\")\nprint(\"within tolerance, frequency alone:\", int(ok_f.sum()), \"; PD duty cycle alone:\", int(ok_pd.sum()),\n      \"; LP and PY duty cycle (0.25) alone:\", int(ok_lppy.sum()), \"; (0.20):\", int(ok_lppy20.sum()))\nprint(\"triphasic at 10 C:\", int((d10.NET == \"triphasic\").sum()), \"of\", len(d10))\nprint(\"mean burst frequency over models and cells: %.3f Hz (median %.3f)\" %\n      (d10[[f\"f {c}\" for c in P.CELLS]].values.mean(), np.median(d10[[f\"f {c}\" for c in P.CELLS]].values)))\nqg = np.array([P.q10_conductances(MODELS[n]) for n in NAMES]); qt = np.array([P.q10_timescales(MODELS[n]) for n in NAMES])\nqs = np.array([P.q10_synapses(MODELS[n]) for n in NAMES])\nprint(\"Q10 of conductances: %.4f to %.4f (intrinsic), %.4f to %.4f (synaptic)\" % (qg.min(), qg.max(), qs[:, :2].min(), qs[:, :2].max()))\nprint(\"Q10 of time scales: %.4f to %.4f (intrinsic), %.4f to %.4f (synaptic)\" % (qt.min(), qt.max(), qs[:, 2:].min(), qs[:, 2:].max()))\nprint(\"all within [1, 2] and [1, 4]:\", bool(qg.min() >= 1 and qg.max() <= 2 and qs[:, :2].max() <= 2 and qs.min() >= 1\n                                             and qt.min() >= 1 and qt.max() <= 4 and qs[:, 2:].max() <= 4))\n\n# %% tags=[\"finding-frequency-at-10C\"]\n# Burst frequency at 10 C, 20 s simulated and the first 10 s dropped: the Methods' target is 1 Hz.\nprint(d10[[f\"f {c}\" for c in P.CELLS]].describe().round(3).to_string())\n\n# %% [markdown]\n# **Result: ...** (conclusion written after the run)\n\n# %% [markdown]\n# ## Simulations at 16 temperatures, 10 to 25 degrees C\n#\n# Every model at 10, 11, ..., 25 degrees C (Figure 1 legend: \"16 values of temperature between\n# 10 C - 25 C\", \"average values over 30 s\"). Each run is 40 s from the initial conditions; the\n# first 10 s are dropped (Methods, Finding parameters) and the last 30 s analysed.\n\n# %%\nTEMPS = np.arange(10, 26).astype(float)\nt0 = time.time()\nscan = P.pmap(P.run_fixed, [(n, MODELS[n], CI, T, 40.0, 10.0) for n in NAMES for T in TEMPS])\nSCAN = {(r[\"key\"], r[\"temp\"]): r for r in scan}\nprint(f\"{len(scan)} runs in {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\ndef summary(r):\n    out = {}\n    for c, cell in enumerate(P.CELLS):\n        b = P.burst_stats(r[\"spikes\"][c])\n        out[f\"f {cell}\"] = np.mean(b[\"freq\"]) if len(b[\"freq\"]) else np.nan\n        out[f\"dc {cell}\"] = np.mean(b[\"dc\"]) if len(b[\"dc\"]) else np.nan\n    ph = P.phases(r[\"spikes\"])\n    for k, v in ph.items():\n        out[k] = np.nanmean(v) if np.isfinite(v).any() else np.nan\n    out[\"NET\"] = r[\"classes\"][3]\n    return out\n\ndef table(name):\n    return pd.DataFrame([summary(SCAN[(name, T)]) for T in TEMPS], index=TEMPS.astype(int))\n\ndef q10_readings(f):\n    lf = np.log(f.values)\n    a = np.exp(10 * np.polyfit(TEMPS, lf, 1)[0])\n    b = (f.loc[25] / f.loc[10]) ** (10 / 15)\n    c = f.loc[20] / f.loc[10]\n    return a, b, c\n\nPH_COLS = [\"dc PD\", \"dc LP\", \"dc PY\", \"PD off\", \"LP on\", \"LP off\", \"PY on\", \"PY off\"]\n\ndef constancy(t):\n    \"\"\"Readings (i) range within 0.1 of a cycle, (ii) every value within 20% of its 10 C value.\"\"\"\n    rng = t[PH_COLS].max() - t[PH_COLS].min()\n    rel = (t[PH_COLS] / t.loc[10, PH_COLS] - 1).abs().max()\n    return rng, rel\n\ndef report(name):\n    t = table(name)\n    print(f\"model {name}\")\n    print(t.round(3).to_string())\n    f = t[[\"f PD\", \"f LP\", \"f PY\"]].mean(axis=1)\n    qa, qb, qc = q10_readings(f)\n    spread = (t[[\"f PD\", \"f LP\", \"f PY\"]].max(axis=1) / t[[\"f PD\", \"f LP\", \"f PY\"]].min(axis=1) - 1).max()\n    rng, rel = constancy(t)\n    print(f\"Q10 of burst frequency (mean of the three cells): (a) fit {qa:.3f}, (b) (f25/f10)^(10/15) {qb:.3f}, (c) f20/f10 {qc:.3f}\")\n    for c in P.CELLS:\n        print(f\"   {c}: (a) {q10_readings(t['f ' + c])[0]:.3f}, (b) {q10_readings(t['f ' + c])[1]:.3f}, (c) {q10_readings(t['f ' + c])[2]:.3f}\")\n    print(f\"largest spread between the cells' frequencies at one temperature: {100 * spread:.1f}%\")\n    print(\"range over temperatures (cycles):\", rng.round(3).to_dict())\n    print(\"largest relative change from 10 C:\", rel.round(3).to_dict())\n    print(f\"(i) all within 0.1 of a cycle: {bool((rng <= 0.1).all())}; (ii) all within 20% of 10 C: {bool((rel <= 0.2).all())}\")\n    rises = {c: bool(t.loc[25, 'f ' + c] > t.loc[10, 'f ' + c]) for c in P.CELLS}\n    print(\"frequency higher at 25 than at 10 C:\", rises, \"; network triphasic at\", int((t.NET == \"triphasic\").sum()), \"of 16\")\n    return t, (qa, qb, qc), rng, rel, rises\n\n# %% [markdown]\n# ## fig1c-frequency-q10-phase-constant\n#\n# > In the model of Figure 1, as temperature rises from 10 to 25 degrees C the burst frequency of\n# > all three cells increases with a Q10 near 2, while each cell's duty cycle and the phases of\n# > burst onsets and offsets stay approximately constant.\n#\n# Model 4?6W66 of the Methods is 4X6W66 in the deposit (the only match). Phases are measured from\n# each PD burst start in units of that PD cycle (Figure 1 legend).\n\n# %% tags=[\"claim:fig1c-frequency-q10-phase-constant\"]\nt1, q1, rng1, rel1, rises1 = report(M[\"4?6W66\"])\nfig, ax = plt.subplots(1, 3, figsize=(12, 3))\nfor c in P.CELLS:\n    ax[0].plot(t1.index, t1[\"f \" + c], \"o-\", label=c); ax[1].plot(t1.index, t1[\"dc \" + c], \"o-\", label=c)\nfor k in [\"PD off\", \"LP on\", \"LP off\", \"PY on\", \"PY off\"]:\n    ax[2].plot(t1.index, t1[k], \"o-\", label=k)\nax[0].set_ylabel(\"burst frequency (Hz)\"); ax[1].set_ylabel(\"duty cycle\"); ax[2].set_ylabel(\"phase\")\nfor a in ax: a.set_xlabel(\"temperature (C)\"); a.legend(fontsize=7)\nplt.tight_layout(); plt.show()\nprint(\"all plotted values are within the axes (autoscaled).\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig1s1-three-models\n#\n# > In three further models with different maximal conductances and Q10 values, the duty cycles\n# > and phases also stay approximately constant while the frequency increases from 10 to 25\n# > degrees C.\n\n# %% tags=[\"claim:fig1s1-three-models\"]\ns1 = {}\nfor n in [\"WWZ3CN\", \"FGFKQS\", \"71G6LA\"]:\n    s1[n] = report(M[n])\n    print()\nfor n, (t, q, rng, rel, rises) in s1.items():\n    print(f\"{n}: frequency rises in every cell {all(rises.values())}; constant (i) {bool((rng <= 0.1).all())}, \"\n          f\"(ii) {bool((rel <= 0.2).all())}; Q10 (a) {q[0]:.2f}\")\nprint(\"FGFKQS shares its maximal conductances with 4X6W66 (see the data check):\", key[\"FGFKQS\"] == key[\"4X6W66\"])\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## all-models-compensated\n#\n# > All 36 models produce a triphasic pyloric rhythm over the working range of 10 to 25 degrees\n# > C; for every set of maximal conductances tried, multiple sets of Q10 values that make the\n# > rhythm temperature robust could be found.\n#\n# The deposit holds 38 models; all are tested, and the counts are given over the 38.\n\n# %% tags=[\"claim:all-models-compensated\"]\nfails = pd.DataFrame({n: [SCAN[(n, T)][\"classes\"][3] != \"triphasic\" for T in TEMPS] for n in NAMES}, index=TEMPS.astype(int))\nper_model = fails.sum()\nprint(\"temperatures (of 16) at which the network is not triphasic, per model:\")\nprint(per_model.to_string())\nprint(f\"\\nmodels triphasic at all 16 temperatures: {int((per_model == 0).sum())} of {len(NAMES)}\")\nprint(f\"models failing at 1 or more temperatures: {per_model[per_model > 0].to_dict()}\")\nfor n in per_model[per_model > 0].index:\n    bad = fails.index[fails[n]].tolist()\n    print(f\"  {n}: not triphasic at {bad}; cell classes there:\", [SCAN[(n, float(T))]['classes'] for T in bad][:4])\nstrict = pd.DataFrame({n: [not P.triphasic(SCAN[(n, T)][\"spikes\"], strict=True) for T in TEMPS] for n in NAMES}, index=TEMPS.astype(int))\nprint(f\"\\nvariant, order required in every cycle: models triphasic at all 16 temperatures {int((strict.sum() == 0).sum())} of {len(NAMES)}\")\nprint(f\"\\nsets of maximal conductances with more than one deposited Q10 set: {len(multi)} of {len(groups)}\")\nfor g in multi:\n    print(f\"  {g}: compensated (triphasic at all 16) {[bool(per_model[n] == 0) for n in g]}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## intermediate-temperature-failures\n#\n# > Of the Q10 solutions that met the target at the control temperatures, 2 in 40 did not display\n# > the correct activity at temperatures in between.\n#\n# Blocked (data_missing): the deposit holds 38 parameter sets with no record of which solutions\n# were screened or discarded. The 38 are not the 40 screened solutions as far as the files show;\n# the count of models above is all that can be said.\n\n# %% [markdown]\n# ## fig3-current-amplitudes\n#\n# > In the PD cell of one model, from 10 to 25 degrees C the Na current peak more than doubles,\n# > the CaT current peak falls to about half despite its larger conductance, and the KCa current\n# > grows about six-fold; in a second model the Na current falls slightly and the KCa current\n# > falls moderately.\n#\n# PD cell, 13 s simulated, the first 10 s dropped and 3 s analysed, as the deposit's currentscape\n# script does (integratePyloricSQ10s_currentscapes_RK4_mp.py: transient = 10, nsecs = 3, dt = 0.05).\n# Readings of the peak: (a) the largest absolute value over the 3 s; (b) the mean over PD cycles\n# (PD burst start to the next) of each cycle's largest absolute value.\n\n# %%\ndef states(name, temp, seconds=13.0, record=3.0, p=None):\n    return P.run_states((name, MODELS[name] if p is None else p, CI, temp, seconds, record))\n\nST = {}\nfor n in [\"4X6W66\", \"SJR46Y\", \"WWZ3CN\", \"FGFKQS\", \"71G6LA\", \"J9U8SQ\"]:\n    for T in (10.0, 25.0):\n        ST[(n, T)] = states(n, T)\n\ndef cell_currents(r, name, c):\n    return P.currents_from_states(r[\"states\"], MODELS[name], r[\"temp\"])[c]\n\ndef peak_ratios(name):\n    out = {}\n    for rd in (\"a\", \"b\"):\n        pk = {}\n        for T in (10.0, 25.0):\n            r = ST[(name, T)]\n            cur = np.abs(cell_currents(r, name, 0))\n            if rd == \"a\":\n                pk[T] = cur.max(axis=1)\n            else:\n                st = P.burst_stats(r[\"spikes\"][0])[\"starts\"]\n                idx = (st / r[\"dt\"]).astype(int)\n                pk[T] = np.mean([cur[:, i:j].max(axis=1) for i, j in zip(idx[:-1], idx[1:])], axis=0)\n        out[rd] = pd.DataFrame({\"peak 10 C\": pk[10.0], \"peak 25 C\": pk[25.0], \"ratio\": pk[25.0] / pk[10.0]},\n                               index=P.CURRENTS + [\"Syn\"])\n    return out\n\n# %% tags=[\"claim:fig3-current-amplitudes\"]\nfig3 = {n: peak_ratios(n) for n in [\"4X6W66\", \"SJR46Y\"]}\nfor n, d in fig3.items():\n    for rd, t in d.items():\n        print(f\"{n}, PD, reading ({rd}):\"); print(t.round(3).to_string()); print()\n\ndef fig3_checks(a, b, rd):\n    A, B = fig3[a][rd][\"ratio\"], fig3[b][rd][\"ratio\"]\n    return {\"A Na > 2\": A[\"Na\"] > 2, \"A CaT 0.5 +- 0.05\": abs(A[\"CaT\"] - 0.5) <= 0.05, \"A KCa 6 +- 0.6\": abs(A[\"KCa\"] - 6) <= 0.6,\n            \"B Na < 1\": B[\"Na\"] < 1, \"B KCa < 1\": B[\"KCa\"] < 1}\n\nfor a, b in [(\"4X6W66\", \"SJR46Y\"), (\"SJR46Y\", \"4X6W66\")]:\n    for rd in (\"a\", \"b\"):\n        ch = fig3_checks(a, b, rd)\n        print(f\"A = {a}, B = {b}, reading ({rd}): {sum(ch.values())} of 5 hold: {ch}\")\nprint(\"\\ncell classes:\", {k: v[\"classes\"] for k, v in ST.items() if k[0] in (\"4X6W66\", \"SJR46Y\")})\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig4-currentscapes-reorganize\n#\n# > In the model of Figure 4, currentscapes differ between 10 and 25 degrees C; in PD the leak\n# > current's inward share is seen at both the start and end of the burst at 10 degrees C but\n# > mainly at the start at 25 degrees C, the A current's share is even across the burst at 10\n# > degrees C and larger at its start at 25 degrees C, and in all cells, most in LP and PY,\n# > temperature raises the KCa share toward the end of bursts.\n#\n# WWZ3CN, the same 3 s windows. A burst runs from its first to its last spike crossing (bursts\n# grouped with the 200 ms threshold). Shares are averaged over the samples of each part of each\n# burst, then over bursts. The A current's share is its outward share (IA is a potassium current).\n\n# %% tags=[\"claim:fig4-currentscapes-reorganize\"]\ndef burst_part_shares(r, name, c, frac):\n    cur = cell_currents(r, name, c)\n    out_sh, in_sh = P.shares(cur)\n    b = P.bursts(r[\"spikes\"][c])\n    res = {\"in start\": [], \"in end\": [], \"out start\": [], \"out end\": []}\n    for s, e, k in zip(*b):\n        if k < 2:\n            continue\n        i, j = int(s / r[\"dt\"]), int(e / r[\"dt\"])\n        w = max(1, int((j - i) * frac))\n        res[\"in start\"].append(in_sh[:, i:i + w].mean(axis=1)); res[\"in end\"].append(in_sh[:, j - w:j].mean(axis=1))\n        res[\"out start\"].append(out_sh[:, i:i + w].mean(axis=1)); res[\"out end\"].append(out_sh[:, j - w:j].mean(axis=1))\n    return {k: pd.Series(np.mean(v, axis=0), index=P.CURRENTS + [\"Syn\"]) for k, v in res.items()}, len(res[\"in start\"])\n\nfig4 = {}\nfor frac, label in [(1 / 3, \"a, thirds\"), (0.2, \"b, 20%\")]:\n    sh = {(c, T): burst_part_shares(ST[(\"WWZ3CN\", T)], \"WWZ3CN\", c, frac) for c in range(3) for T in (10.0, 25.0)}\n    pd10, pd25 = sh[(0, 10.0)][0], sh[(0, 25.0)][0]\n    leak10 = pd10[\"in end\"][\"Leak\"] / pd10[\"in start\"][\"Leak\"]\n    leak25 = pd25[\"in end\"][\"Leak\"] / pd25[\"in start\"][\"Leak\"]\n    a10 = pd10[\"out start\"][\"A\"] / pd10[\"out end\"][\"A\"]\n    a25 = pd25[\"out start\"][\"A\"] / pd25[\"out end\"][\"A\"]\n    kca = {P.CELLS[c]: (sh[(c, 10.0)][0][\"out end\"][\"KCa\"], sh[(c, 25.0)][0][\"out end\"][\"KCa\"]) for c in range(3)}\n    inc = {k: v[1] - v[0] for k, v in kca.items()}\n    print(f\"reading ({label}); bursts used per cell and temperature:\", {f\"{P.CELLS[c]} {int(T)}\": sh[(c, T)][1] for c, T in sh})\n    print(f\"  PD leak inward share, end over start: 10 C {leak10:.3f} (start {pd10['in start']['Leak']:.4f}, end {pd10['in end']['Leak']:.4f}); \"\n          f\"25 C {leak25:.3f} (start {pd25['in start']['Leak']:.4f}, end {pd25['in end']['Leak']:.4f})\")\n    print(f\"  PD A outward share, start over end: 10 C {a10:.3f}; 25 C {a25:.3f}\")\n    print(\"  KCa outward share at the end of bursts (10 C, 25 C):\", {k: tuple(round(x, 4) for x in v) for k, v in kca.items()})\n    print(\"  increase:\", {k: round(v, 4) for k, v in inc.items()})\n    parts = {\"leak\": leak25 < leak10, \"A\": (0.8 <= a10 <= 1.25) and a25 > a10,\n             \"KCa\": all(v > 0 for v in inc.values()) and inc[\"LP\"] > inc[\"PD\"] and inc[\"PY\"] > inc[\"PD\"]}\n    print(\"  parts that hold:\", parts)\n    fig4[label] = parts\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## currentscapes-dominant-currents\n#\n# > In all models and at all temperatures, spikes are driven first by INa and then by IKd, which\n# > then dominate the inward and outward currents, and when the cells are most hyperpolarized IH\n# > and the synaptic currents dominate.\n#\n# Every model, every cell, at 10, 15, 20 and 25 degrees C; 13 s simulated and the last 3 s used.\n\n# %% tags=[\"claim:currentscapes-dominant-currents\"]\nt0 = time.time()\ndom = P.pmap(P.dominant_summary, [(n, MODELS[n], CI, T, 13.0, 3.0) for n in NAMES for T in (10.0, 15.0, 20.0, 25.0)])\nprint(f\"{len(dom)} runs in {time.time() - t0:.0f} s\")\nrows = [dict(model=r[\"key\"], temp=r[\"temp\"], **c) for r in dom for c in r[\"cells\"]]\ndd = pd.DataFrame(rows)\nnsp = dd.spikes.sum()\nprint(f\"spikes: {nsp}; Na largest inward share in the 1 ms before the peak: {dd.na_first.sum() / nsp:.3f}; \"\n      f\"Kd largest outward share in the 1 ms after it: {dd.kd_after.sum() / nsp:.3f}\")\nnames9 = P.CURRENTS + [\"Syn\"]\ndd[\"low_in_name\"] = [names9[i] for i in dd.low_in]; dd[\"low_out_name\"] = [names9[i] for i in dd.low_out]\nprint(\"largest inward share at the lowest 5% of V:\", dd.low_in_name.value_counts().to_dict())\nprint(\"largest outward share at the lowest 5% of V:\", dd.low_out_name.value_counts().to_dict())\nmain = (dd.low_in == 6) & (dd.low_out == 8)\nvar = dd.low_top2.apply(lambda x: x == [6, 8])\nprint(f\"cases (model, cell, temperature) with H inward and Syn outward largest: {main.mean():.3f} of {len(dd)}\")\nprint(f\"variant, H and Syn the two largest shares on either side: {var.mean():.3f}\")\nprint(\"per cell:\", dd.assign(main=main).groupby(\"cell\").main.mean().round(3).to_dict())\nprint(\"per temperature:\", dd.assign(main=main).groupby(\"temp\").main.mean().round(3).to_dict())\nprint(\"per cell, Na and Kd fractions:\", dd.groupby(\"cell\")[[\"spikes\", \"na_first\", \"kd_after\"]].sum().assign(\n    na=lambda x: x.na_first / x.spikes, kd=lambda x: x.kd_after / x.spikes).round(3).to_dict(\"index\"))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5-a-to-kca-tradeoff\n#\n# > In the 20 ms after the PD burst, the share of the A current falls smoothly and the share of\n# > the KCa current rises smoothly as temperature goes from 10 to 25 degrees C ...\n#\n# FGFKQS (Methods) and J9U8SQ (legend, \"same model as in Figure 7A\"). PD, the 20 ms after the\n# last spike of each burst (from its -20 mV crossing), outward shares averaged over samples and\n# bursts, at the 16 temperatures; 13 s simulated, the last 3 s used.\n\n# %% tags=[\"claim:fig5-a-to-kca-tradeoff\"]\ndef end_shares(task):\n    r = P.run_states(task)\n    name, p = task[0], task[1]\n    cur = P.currents_from_states(r[\"states\"], p, r[\"temp\"])[0]\n    out_sh, _ = P.shares(cur)\n    st, en, k = P.bursts(r[\"spikes\"][0])\n    n20 = int(round(0.020 / r[\"dt\"]))\n    w = [out_sh[:, int(e / r[\"dt\"]):int(e / r[\"dt\"]) + n20].mean(axis=1) for e in en if int(e / r[\"dt\"]) + n20 <= out_sh.shape[1]]\n    return name, r[\"temp\"], np.mean(w, axis=0), len(w)\n\nres5 = P.pmap(end_shares, [(n, MODELS[n], CI, T, 13.0, 3.0) for n in [\"FGFKQS\", \"J9U8SQ\"] for T in TEMPS])\nfig5 = {}\nfor n in [\"FGFKQS\", \"J9U8SQ\"]:\n    t = pd.DataFrame([dict(zip(names9, s), T=T, bursts=b) for m, T, s, b in res5 if m == n]).set_index(\"T\")\n    rA = stats.spearmanr(t.index, t[\"A\"])[0]; rK = stats.spearmanr(t.index, t[\"KCa\"])[0]\n    cross = t.loc[10.0, \"A\"] > t.loc[10.0, \"KCa\"] and t.loc[25.0, \"KCa\"] > t.loc[25.0, \"A\"]\n    fig5[n] = dict(rA=rA, rK=rK, cross=cross)\n    print(n); print(t.round(3).to_string())\n    print(f\"  Spearman with temperature: A {rA:.3f}, KCa {rK:.3f}; A > KCa at 10 C and KCa > A at 25 C: {cross}\\n\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Simulations above 25 degrees C\n#\n# Every model at 26 to 35 degrees C, 40 s, the first 10 s dropped, as for the working range.\n# These runs serve fig6s1-crash-mechanisms (the crash temperature of each model) and the counts\n# reported for fig7-high-temperature-slow-timescales.\n\n# %%\nHOT = np.arange(26, 36).astype(float)\nt0 = time.time()\nhot = P.pmap(P.run_fixed, [(n, MODELS[n], CI, T, 40.0, 10.0) for n in NAMES for T in HOT])\nfor r in hot:\n    SCAN[(r[\"key\"], r[\"temp\"])] = r\nprint(f\"{len(hot)} runs in {time.time() - t0:.0f} s\")\ncrashT = {n: next((T for T in HOT if SCAN[(n, T)][\"classes\"][3] != \"triphasic\"), None) for n in NAMES}\nprint(\"lowest temperature above 25 C at which the network is not triphasic:\", crashT)\n\n# %% [markdown]\n# ## fig6-crash-different-mechanisms\n#\n# > Two models that are phase compensated at 10 and 25 degrees C crash at 30 degrees C with\n# > complete loss of PD activity, by different currents in each.\n#\n# FGFKQS and 71G6LA at 10, 25 and 30 degrees C. Classes from the 40 s runs (last 30 s); the\n# dominant currents from 13 s runs (last 3 s), largest mean inward and outward share in PD.\n\n# %% tags=[\"claim:fig6-crash-different-mechanisms\"]\ndef dominant_pair(r, name, c):\n    cur = P.currents_from_states(r[\"states\"], MODELS[name], r[\"temp\"])[c]\n    out_sh, in_sh = P.shares(cur)\n    return names9[int(np.argmax(in_sh.mean(axis=1)))], names9[int(np.argmax(out_sh.mean(axis=1)))]\n\nfig6 = {}\nfor n in [\"FGFKQS\", \"71G6LA\"]:\n    r30 = states(n, 30.0)\n    cl = {T: SCAN[(n, T)][\"classes\"] for T in (10.0, 25.0, 30.0)}\n    pair = dominant_pair(r30, n, 0)\n    nspk = len(SCAN[(n, 30.0)][\"spikes\"][0])\n    fig6[n] = dict(classes=cl, pair=pair, pd_spikes_30=nspk)\n    print(n, cl, f\"; PD spikes in the 30 s analysed at 30 C: {nspk}; PD dominant inward, outward at 30 C: {pair}\")\n    print(\"   PD V range at 30 C (last 3 s): %.1f to %.1f mV\" % (r30[\"states\"][:, 0].min(), r30[\"states\"][:, 0].max()))\nsame_pair = fig6[\"FGFKQS\"][\"pair\"] == fig6[\"71G6LA\"][\"pair\"]\nprint(\"dominant pairs the same in the two models:\", same_pair)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6s1-crash-mechanisms\n#\n# > In eight further models, currentscapes at crashed states show that the networks crash by\n# > different mechanisms in each case.\n#\n# The Methods name B7SDOL, J9U8SQ, 4R2719, R3VIEW, Q8FBN1, RMZ8KZ, EF84RN and SJR46Y. Q8FBN1 is not\n# in the deposit; B7SDOL is B7SD0L. The seven are tested.\n\n# %% tags=[\"claim:fig6s1-crash-mechanisms\"]\ns6 = [M[n] for n in METHODS_NAMES[\"Figure 6-S1\"] if M[n]]\nprint(\"models tested:\", s6)\npat = {}\nfor n in s6:\n    T = crashT[n]\n    if T is None:\n        print(f\"{n}: triphasic at every temperature up to 35 C\"); continue\n    r = states(n, T)\n    pat[n] = tuple(dominant_pair(r, n, c) for c in range(3))\n    print(f\"{n}: crashes at {T:.0f} C, classes {SCAN[(n, T)]['classes']}; dominant (inward, outward) per cell {pat[n]}\")\ndistinct = len(set(pat.values()))\nprint(f\"\\nmodels that crash below 35 C: {sum(crashT[n] is not None and crashT[n] < 35 for n in s6)} of {len(s6)}; \"\n      f\"distinct patterns: {distinct}\")\nprint(\"models sharing a pattern:\", [(a, b) for a, b in combinations(pat, 2) if pat[a] == pat[b]])\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7-high-temperature-slow-timescales\n#\n# > At temperatures above 25 degrees C the models crash in different ways (quiescence,\n# > subthreshold oscillations, or irregular activity), and in five models at 29 to 34 degrees C\n# > time scales much longer than the 1 s period at 10 degrees C emerge.\n#\n# Blocked (data_missing): three of the five models of Figure 7 (G81PUL, G7EOZ8, SAXT8Y) are not in\n# the deposit. The two that are (J9U8SQ at 34 C, KNMLBC filed as KMNLBC at 30 C), and FGFKQS at\n# 34 C (the variant for panel A), are shown for information.\n\n# %%\ndef longest_gaps(r):\n    out = []\n    for c in range(3):\n        s = r[\"spikes\"][c]\n        ev = np.r_[0.0, s, r[\"length\"]]\n        out.append(np.max(np.diff(ev)))\n    return out\n\nfor n, T in [(\"J9U8SQ\", 34.0), (\"KMNLBC\", 30.0), (\"FGFKQS\", 34.0)]:\n    r = SCAN[(n, T)]\n    print(f\"{n} at {T:.0f} C: classes {r['classes']}; longest interval without a spike per cell (s, 30 s window, edges included): \"\n          f\"{np.round(longest_gaps(r), 2)}\")\ncnt = Counter()\nfor n in NAMES:\n    for T in HOT:\n        cl = SCAN[(n, T)][\"classes\"]\n        if cl[3] != \"triphasic\":\n            cnt[tuple(cl[:3])] += 1\nprint(\"\\ncell classes (PD, LP, PY) of non-triphasic networks over all models at 26 to 35 C:\")\nfor k, v in cnt.most_common(12):\n    print(f\"  {v:4d}  {k}\")\n\n# %% [markdown]\n# ## fig9a-remove-a-current\n#\n# > Removing the A current at 10 degrees C makes the network irregular, while the same deletion at\n# > 25 degrees C leaves a nearly normal triphasic rhythm except for irregular PY bursting.\n#\n# WWZ3CN. Timings: (code) the deposit's integratePyloricSQ10s_remove_gA_onesteps_twotemps_RK4.py,\n# 10 s transient, 5 s control, then 10 s with IA removed from the final state; (Results) 20 s of\n# control, then 20 s with IA removed; (legend) removal at 4 s, the length after it taken as 20 s.\n# Classes over the period after removal, its first 2 s dropped (criterion).\n\n# %%\nTIMINGS = {\"code\": (15.0, 10.0), \"Results\": (20.0, 20.0), \"legend\": (4.0, 20.0)}\n\ndef removal(name, current, temp, control, after):\n    p = MODELS[name]\n    s1 = P.simulate(p, temp, control, CI)\n    s2 = P.simulate(P.scaled(p, current, 0.0), temp, after, s1.final)\n    before = P.classify(s1, max(0.0, control - 10.0), control)\n    return before, P.classify(s2, 2.0, after), s1, s2\n\ndef mean_freq(sim, t0, t1):\n    f = []\n    for s in sim.window(t0, t1):\n        b = P.burst_stats(s)\n        f.append(np.mean(b[\"freq\"]) if len(b[\"freq\"]) else np.nan)\n    return np.round(f, 3)\n\n# %% tags=[\"claim:fig9a-remove-a-current\"]\nfig9a = {}\nfor tm, (ctl, aft) in TIMINGS.items():\n    for T in (10.0, 25.0):\n        b, a, s1, s2 = removal(\"WWZ3CN\", 3, T, ctl, aft)\n        fig9a[(tm, T)] = a\n        print(f\"{tm:8s} {T:.0f} C: before {b}; after removal {a}\")\nfor tm in TIMINGS:\n    a10, a25 = fig9a[(tm, 10.0)], fig9a[(tm, 25.0)]\n    p10 = a10[3] != \"triphasic\" and any(x in (\"irregular bursting\", \"irregular spiking\") for x in a10[:3])\n    p25 = a25[0] == \"regular bursting\" and a25[1] == \"regular bursting\" and a25[2] == \"irregular bursting\"\n    p25b = a25[2] == \"irregular bursting\"\n    print(f\"{tm}: 10 C part {p10}; 25 C part {p25} (PY irregular {p25b})\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig9b-remove-kca-current\n#\n# > In another model, removing the KCa current at 10 degrees C slows the rhythm but keeps it\n# > triphasic, while the same deletion at 25 degrees C silences the network ...\n#\n# FGFKQS (Methods; also the deposit's script, \"Fig. 13B\") and J9U8SQ (legend), the same timings.\n\n# %% tags=[\"claim:fig9b-remove-kca-current\"]\nfig9b = {}\nfor n in [\"FGFKQS\", \"J9U8SQ\"]:\n    for tm, (ctl, aft) in TIMINGS.items():\n        b10, a10, s1, s2 = removal(n, 4, 10.0, ctl, aft)\n        f_before, f_after = mean_freq(s1, max(0.0, ctl - 10.0), ctl), mean_freq(s2, 2.0, aft)\n        b25, a25, _, _ = removal(n, 4, 25.0, ctl, aft)\n        ok10 = b10[3] == \"triphasic\" and a10[3] == \"triphasic\" and np.nanmean(f_after) < np.nanmean(f_before)\n        ok25 = all(x == \"quiescent\" for x in a25[:3])\n        fig9b[(n, tm)] = ok10 and ok25\n        print(f\"{n}, {tm}: 10 C before {b10} f {f_before}, after {a10} f {f_after}; 25 C after {a25}; \"\n              f\"10 C part {ok10}, 25 C part {ok25}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig10a-graded-removal\n#\n# > In the model of Figure 10A, reducing gNa to 75% makes LP burst irregularly and the network\n# > non-triphasic at 10 degrees C but not at 25 degrees C; ...\n#\n# 4X6W66, each of gNa, gKCa, gCaT and gCaS at 100, 75, 50, 25 and 0% in all three cells, at 10 and\n# 25 degrees C; 20 s from the initial conditions, the first 10 s dropped (criterion).\n\n# %% tags=[\"claim:fig10a-graded-removal\"]\nFR = [1.0, 0.75, 0.5, 0.25, 0.0]\nCUR10 = {\"Na\": 0, \"KCa\": 4, \"CaT\": 1, \"CaS\": 2}\ntasks = [((cur, fr, T), P.scaled(MODELS[\"4X6W66\"], k, fr), CI, T, 20.0, 10.0) for cur, k in CUR10.items() for fr in FR for T in (10.0, 25.0)]\ng10 = {r[\"key\"]: r[\"classes\"] for r in P.pmap(P.run_fixed, tasks)}\nfor cur in CUR10:\n    for T in (10.0, 25.0):\n        print(f\"{cur} at {T:.0f} C\")\n        print(pd.DataFrame([g10[(cur, fr, T)] for fr in FR], index=[f\"{int(100 * fr)}%\" for fr in FR],\n                           columns=[\"PD\", \"LP\", \"PY\", \"NET\"]).to_string())\nchecks10 = {\n    \"Na 75% 10 C: LP irregular bursting, NET not triphasic\": g10[(\"Na\", 0.75, 10.0)][1] == \"irregular bursting\" and g10[(\"Na\", 0.75, 10.0)][3] != \"triphasic\",\n    \"Na 75% 25 C: NET triphasic\": g10[(\"Na\", 0.75, 25.0)][3] == \"triphasic\",\n    \"KCa every step 10 C: NET triphasic\": all(g10[(\"KCa\", fr, 10.0)][3] == \"triphasic\" for fr in FR),\n    \"KCa 0% 25 C: all quiescent\": all(x == \"quiescent\" for x in g10[(\"KCa\", 0.0, 25.0)][:3]),\n    \"CaT and CaS 0%: not triphasic at both, classes differ\": all(\n        g10[(c, 0.0, 10.0)][3] != \"triphasic\" and g10[(c, 0.0, 25.0)][3] != \"triphasic\" and g10[(c, 0.0, 10.0)][:3] != g10[(c, 0.0, 25.0)][:3]\n        for c in (\"CaT\", \"CaS\")),\n}\nfor k, v in checks10.items():\n    print(f\"{v!s:5s}  {k}\")\nprint(\"matching:\", sum(checks10.values()), \"of 5\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig10b-complete-removal-differs\n#\n# > Across the 36 models, the response to complete removal of a current differs between 10 and 25\n# > degrees C in about half of the models for most currents; most models respond differently for\n# > CaT, while removing H gives the same state (quiescence) at both temperatures.\n#\n# All 38 deposited models, each current at 0% at 10 and 25 degrees C, 20 s with the first 10 s\n# dropped.\n\n# %% tags=[\"claim:fig10b-complete-removal-differs\"]\nt0 = time.time()\ntasks = [((n, k, T), P.scaled(MODELS[n], k, 0.0), CI, T, 20.0, 10.0) for n in NAMES for k in range(8) for T in (10.0, 25.0)]\ng0 = {r[\"key\"]: r[\"classes\"] for r in P.pmap(P.run_fixed, tasks)}\nprint(f\"{len(tasks)} runs in {time.time() - t0:.0f} s\")\nrows = []\nfor k, cur in enumerate(P.CURRENTS):\n    diff_a = np.mean([g0[(n, k, 10.0)] != g0[(n, k, 25.0)] for n in NAMES])\n    diff_b = np.mean([g0[(n, k, 10.0)][3] != g0[(n, k, 25.0)][3] for n in NAMES])\n    sameq = sum(g0[(n, k, 10.0)] == g0[(n, k, 25.0)] and all(x == \"quiescent\" for x in g0[(n, k, 10.0)][:3]) for n in NAMES)\n    rows.append(dict(current=cur, differ_all_classes=diff_a, differ_NET=diff_b, same_and_quiescent=sameq))\nt10b = pd.DataFrame(rows).set_index(\"current\")\nprint(t10b.round(3).to_string())\nprint(\"\\nclasses after complete removal of H:\", Counter(tuple(g0[(n, 6, T)]) for n in NAMES for T in (10.0, 25.0)).most_common(5))\n\ndef judge10b(col, currents):\n    t = t10b.loc[currents]\n    others = [c for c in currents if c not in (\"CaT\", \"H\")]\n    cat = t[col].idxmax() == \"CaT\" and t.loc[\"CaT\", col] > 0.5\n    h = t.loc[\"H\", \"same_and_quiescent\"] >= 33\n    half = np.mean([0.3 <= t.loc[c, col] <= 0.7 for c in others])\n    return cat, h, half\n\nfor col in (\"differ_all_classes\", \"differ_NET\"):\n    for label, cur in ((\"8 currents\", P.CURRENTS), (\"7 without leak\", P.CURRENTS[:7])):\n        cat, h, half = judge10b(col, cur)\n        print(f\"reading {col}, {label}: CaT largest and > 0.5 {cat}; H same and quiescent in >= 33 {h}; \"\n              f\"fraction of other currents in [0.3, 0.7] {half:.2f}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (written after the run)\n\n# %%\nprint(f\"notebook run time {(time.time() - T_START) / 60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: entries/alonso-2020/reproduce_alonso_2020.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python - <<'EOF'
s=open('reproduce_alonso_2020.py').read()
old=s[s.index('def end_shares(task):'):s.index('res5 = ')]
s=s.replace(old,'')
s=s.replace('res5 = P.pmap(end_shares,','res5 = P.pmap(P.end_shares,')
open('reproduce_alonso_2020.py','w').write(s)
EOF
cat >> pyloric.py <<'EOF'


def end_shares(task):
    """fig5-a-to-kca-tradeoff, in a worker: mean outward shares in PD over the 20 ms after the
    last spike of each burst (from its threshold crossing)."""
    r = run_states(task)
    name, p = task[0], task[1]
    cur = currents_from_states(r["states"], p, r["temp"])[0]
    out_sh, _ = shares(cur)
    st, en, k = bursts(r["spikes"][0])
    n20 = int(round(0.020 / r["dt"]))
    w = [out_sh[:, int(e / r["dt"]):int(e / r["dt"]) + n20].mean(axis=1) for e in en
         if int(e / r["dt"]) + n20 <= out_sh.shape[1]]
    return name, r["temp"], np.mean(w, axis=0), len(w)
EOF
grep -n "end_shares" reproduce_alonso_2020.py
```

```
587:res5 = P.pmap(P.end_shares, [(n, MODELS[n], CI, T, 13.0, 3.0) for n in ["FGFKQS", "J9U8SQ"] for T in TEMPS])
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && jupytext --to ipynb -q reproduce_alonso_2020.py -o reproduce_alonso_2020.ipynb && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 reproduce_alonso_2020.ipynb --output $TMPDIR/A.ipynb 2>&1 | tail -20; date -u
```

```
Fri Nov 27 22:24:51 UTC 2026
[36mFile [39m[32m~/work/encore-registry/encore-registry/entries/alonso-2020/pyloric.py:512[39m, in [36mpmap[39m[34m(fn, tasks, procs)[39m
[32m    510[39m [38;5;28;01mfrom[39;00m[38;5;250m [39m[34;01mmultiprocessing[39;00m[38;5;250m [39m[38;5;28;01mimport[39;00m get_context
[32m    511[39m [38;5;28;01mwith[39;00m get_context([33m"[39m[33mfork[39m[33m"[39m).Pool(procs) [38;5;28;01mas[39;00m pool:
[32m--> [39m[32m512[39m     [38;5;28;01mreturn[39;00m [30;43mpool[39;49m[30;43m.[39;49m[30;43mmap[39;49m[30;43m([39;49m[30;43mfn[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mtasks[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mchunksize[39;49m[30;43m=[39;49m[30;43m1[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/multiprocessing/pool.py:367[39m, in [36mPool.map[39m[34m(self, func, iterable, chunksize)[39m
[32m    362[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mmap[39m([38;5;28mself[39m, func, iterable, chunksize=[38;5;28;01mNone[39;00m):
[32m    363[39m [38;5;250m    [39m[33;03m'''[39;00m
[32m    364[39m [33;03m    Apply `func` to each element in `iterable`, collecting the results[39;00m
[32m    365[39m [33;03m    in a list that is returned.[39;00m
[32m    366[39m [33;03m    '''[39;00m
[32m--> [39m[32m367[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43m_map_async[39;49m[30;43m([39;49m[30;43mfunc[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43miterable[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmapstar[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mchunksize[39;49m[30;43m)[39;49m[30;43m.[39;49m[30;43mget[39;49m[30;43m([39;49m[30;43m)[39;49m

[36mFile [39m[32m~/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/multiprocessing/pool.py:774[39m, in [36mApplyResult.get[39m[34m(self, timeout)[39m
[32m   
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('pyloric.py').read()
old="""        up = np.asarray(sw_up)
        idx = np.searchsorted(up, s) - 1"""
new="""        up = np.asarray(sw_up)
        if len(up) == 0:
            return "tonic spiking"   # V never crosses -50 mV upward in the window: no slow wave (assumption)
        idx = np.searchsorted(up, s) - 1"""
assert old in s
s=s.replace(old,new)
open('pyloric.py','w').write(s)
EOF
source $TMPDIR/dev/bin/activate && date -u && jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600 reproduce_alonso_2020.ipynb --output $TMPDIR/A.ipynb 2>&1 | tail -3; date -u
```

```
Fri Nov 27 22:35:40 UTC 2026
[NbConvertApp] Converting notebook reproduce_alonso_2020.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 229828 bytes to /tmp/claude-1001/A.ipynb
Fri Nov 27 22:49:42 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF' > A_out.txt
import nbformat
nb=nbformat.read('A.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"===== cell {i} tags={c.metadata.get('tags')}")
    for o in c.get('outputs',[]):
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
        elif 'text/plain' in o.get('data',{}): print(o.data['text/plain'][:2000])
EOF
wc -l A_out.txt; head -150 A_out.txt
```

```
600 A_out.txt
===== cell 1 tags=None
{'md5': '37766522dabaaa620d4c44264e76e686', 'sha256': '327279e2c4553c0b946bf230260caf0f7321e36bc5201ad7d65bbe6638d2df08', 'bytes': 99026}

===== cell 3 tags=['sanity']
137 members in the zip, 66 outside __MACOSX/
  alonso_marder_tempcomp_2019_root/                                                                                    0
  alonso_marder_tempcomp_2019_root/.DS_Store                                                                       14340
  alonso_marder_tempcomp_2019_root/compilejava.py                                                                    198
  alonso_marder_tempcomp_2019_root/parameters_and_ci/                                                                  0
  alonso_marder_tempcomp_2019_root/parameters_and_ci/.DS_Store                                                      6148
  alonso_marder_tempcomp_2019_root/parameters_and_ci/cis_network.txt                                                 106
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-0SHNMD.score.18.6198193193.txt                               3309
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-2RO5K6.score.13.9094188223.txt                               3309
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-4R2719.score.26.8426738694.txt                               3309
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-4X6W66.score.32.736714734.txt                                3309
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-71G6LA.score.44.0018579077.txt                               3309
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-72TVF2.score.16.1275919617.txt                               3309
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-B7SD0L.score.21.7288155631.txt                               3309
  alonso_marder_tempcomp_2019_root/parameters_and_ci/p-CG4J30.score.10.2328432089.txt                               3309
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && uv pip install -q pymupdf 2>&1|tail -1; python -c "
import fitz
d=fitz.open('paper/10.7554-elife.55470.pdf')
p=d[18]
t=p.get_text()
i=t.find('search space of allowed')
print(t[i:i+700])
p=d[20]; t=p.get_text(); i=t.find('Figure 1'); print(t[i:i+200])
for b in d[20].get_text('rawdict')['blocks']:
  for l in b.get('lines',[]):
    for s in l['spans']:
      txt=''.join(c['c'] for c in s['chars'])
      if '6W66' in txt or txt.strip() in ('4','6W66'): print(repr(txt), s['font'])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python -c "
import pymupdf
d=pymupdf.open('paper/10.7554-elife.55470.pdf')
for pg in range(17,20):
  for b in d[pg].get_text('rawdict')['blocks']:
    for l in b.get('lines',[]):
      line=''.join(''.join(c['c'] for c in s['chars'])+'|'+s['font'][-4:]+'| ' for s in l['spans'])
      if 'search' in line or 'syn' in line or 'Ca 2' in line or '10' in line and ('[' in line or 'gNa' in line): print(pg, line[:300])
" | grep -i "gNa\|gsyn\|search\|tCa\|t Ca" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,420p $TMPDIR/A_out.txt
```

```
J6OK9B  1.186  0.226  1.194  0.210  1.187  0.242  triphasic  False     False               False               False
J9U8SQ  1.440  0.194  1.446  0.256  1.441  0.251  triphasic  False      True                True               False
KMNLBC  1.100  0.205  1.115  0.229  1.100  0.217  triphasic  False      True               False               False
KV0BR4  1.623  0.224  1.627  0.250  1.623  0.197  triphasic  False     False               False               False
LE8W3F  1.065  0.224  1.069  0.236  1.069  0.248  triphasic   True     False                True               False
MAXTTP  1.461  0.195  1.481  0.196  1.460  0.253  triphasic  False      True               False               False
ML4GPK  1.379  0.197  1.366  0.198  1.366  0.287  triphasic  False      True               False               False
NJP4RT  1.425  0.175  1.425  0.212  1.441  0.242  triphasic  False     False               False               False
OPLRCP  1.297  0.174  1.299  0.267  1.296  0.249  triphasic  False     False                True               False
P1LH61  1.377  0.208  1.376  0.192  1.407  0.206  triphasic  False      True               False                True
PCR6RP  1.308  0.193  1.312  0.248  1.308  0.183  triphasic  False      True               False               False
PLKTEM  1.361  0.178  1.340  0.167  1.339  0.296  triphasic  False     False               False               False
Q0H92I  1.181  0.171  1.156  0.248  1.156  0.258  triphasic  False     False                True               False
R00977  1.061  0.160  1.032  0.222  1.032  0.259  triphasic   True     False               False               False
R2PNKE  1.181  0.171  1.156  0.248  1.156  0.258  triphasic  False     False                True               False
R3VIEW  1.545  0.187  1.536  0.236  1.537  0.307  triphasic  False      True               False               False
RMZ8KZ  1.234  0.231  1.234  0.219  1.234  0.181  triphasic  False     False               False                True
SJR46Y  1.2
[... 253 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 420,600p $TMPDIR/A_out.txt
```

```
reading (a, thirds); bursts used per cell and temperature: {'PD 10': 3, 'PD 25': 9, 'LP 10': 3, 'LP 25': 9, 'PY 10': 3, 'PY 25': 9}
  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over end: 10 C 1.278; 25 C 1.348
  KCa outward share at the end of bursts (10 C, 25 C): {'PD': (np.float64(0.6174), np.float64(0.406)), 'LP': (np.float64(0.1542), np.float64(0.443)), 'PY': (np.float64(0.1573), np.float64(0.3818))}
  increase: {'PD': np.float64(-0.2114), 'LP': np.float64(0.2888), 'PY': np.float64(0.2246)}
  parts that hold: {'leak': np.False_, 'A': np.False_, 'KCa': False}
reading (b, 20%); bursts used per cell and temperature: {'PD 10': 3, 'PD 25': 9, 'LP 10': 3, 'LP 25': 9, 'PY 10': 3, 'PY 25': 9}
  PD leak inward share, end over start: 10 C nan (start 0.0000, end 0.0000); 25 C nan (start 0.0000, end 0.0000)
  PD A outward share, start over end: 10 C 1.278; 25 C 1.385
  KCa outward share at the end of bursts (10 C, 25 C): {'PD': (np.float64(0.6537), np.float64(0.4496)), 'LP': (np.float64(0.1595), np.float64(0.499)), 'PY': (np.float64(0.1737), np.float64(0.4233))}
  increase: {'PD': np.float64(-0.2041), 'LP': np.float64(0.3396), 'PY': np.float64(0.2496)}
  parts that hold: {'leak': np.False_, 'A': np.False_, 'KCa': False}

/tmp/claude-1001/ipykernel_10/2873223091.py:19: RuntimeWarning: invalid value encountered in scalar divide
  leak10 = pd10["in end"]["Leak"] / pd10["in start"]["Leak"]
/tmp/claude-1001/ipykernel_10/2873223091.py:20: RuntimeWarning: invalid value encountered in scalar divide
  leak25 = pd25["in end"]["Leak"] / pd25["in start"]["Leak"]

===== cell 37 tags=['claim:currentscapes-dominant-currents']
152 runs in 32 s
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && sed -i 's/@njit(cache=True)/@njit(cache=True, error_model="numpy")/' pyloric.py && grep -c 'error_model="numpy"' pyloric.py && source $TMPDIR/dev/bin/activate && python -c "
import numpy as np, pyloric as P, time
raw=P.read_zip_bytes(); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
t=time.time()
R=P.pmap(P.run_fixed,[(n,M[n],ci,T,40.0,10.0) for n in list(M) for T in (33.0,35.0)])
print(time.time()-t)
for r in R:
  if not np.isfinite(r['final']).all(): print('nonfinite',r['key'],r['temp'])
print([ (r['key'],r['temp'],r['classes']) for r in R][:12])
"
```

```
10
43.632235288619995
nonfinite G7P2WE 33.0
nonfinite G7P2WE 35.0
nonfinite INPO74 33.0
nonfinite INPO74 35.0
nonfinite J9U8SQ 35.0
nonfinite NJP4RT 33.0
nonfinite NJP4RT 35.0
nonfinite R00977 33.0
nonfinite R00977 35.0
nonfinite SJR46Y 33.0
nonfinite SJR46Y 35.0
[('0SHNMD', 33.0, ['quiescent', 'quiescent', 'quiescent', 'not triphasic']), ('0SHNMD', 35.0, ['quiescent', 'quiescent', 'quiescent', 'not triphasic']), ('2RO5K6', 33.0, ['quiescent', 'quiescent', 'quiescent', 'not triphasic']), ('2RO5K6', 35.0, ['quiescent', 'quiescent', 'quiescent', 'not triphasic']), ('4R2719', 33.0, ['regular bursting', 'irregular spiking', 'irregular bursting', 'not triphasic']), ('4R2719', 35.0, ['irregular bursting', 'irregular spiking', 'quiescent', 'not triphasic']), ('4X6W66', 33.0, ['irregular bursting', 'regular bursting', 'irregular bursting', 'not triphasic']), ('4X6W66', 35.0, ['irregular bursting', 'regular bursting', 'other', 'not triphasic']), ('71G6LA', 33.0, ['quiescent', 'tonic spiking', 'quiescent', 'not triphasic']), ('71G6LA', 35.0, ['quiescent', 'tonic spiking', 'quiescent', 'not triphasic']), ('72TVF2', 33.0, ['irregular bursting', 'irregular bursting', 'regular bursting', 'not triphasic']), ('72TVF2', 35.0, ['irregular bursting', 'irregular bursting', 'regular bursting', 'triphasic'])]
```

**Agent calls Bash**

```bash
cd $TMPDIR/z/alonso_marder_tempcomp_2019_root && java -cp . standaloneCodePyloricTempComp.integratePyloricNetwork_slow_full_temp_sameq10s_rk4 ./parameters_and_ci/cis_network.txt ./parameters_and_ci/p-G7P2WE.score.17.175833658.txt 40 35 0.05 > $TMPDIR/g.txt; grep -n -m2 "NaN\|Infinity" $TMPDIR/g.txt; wc -l $TMPDIR/g.txt; awk 'NR%20000==0' $TMPDIR/g.txt | head -5
```

```
2042:-47.445028104449584 NaN -47.44835119614421
2043:NaN NaN NaN
800000 /tmp/claude-1001/g.txt
NaN NaN NaN
NaN NaN NaN
NaN NaN NaN
NaN NaN NaN
NaN NaN NaN
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python - <<'EOF'
s=open('pyloric.py').read()
s=s.replace("""        self.final = y
""","""        self.final = y
        self.finite = bool(np.isfinite(y).all())   # False when the integration diverged (NaN)
""")
s=s.replace('''    """Cell classes of PD, LP, PY and the network class over [t0, t1) of a simulation."""
''','''    """Cell classes of PD, LP, PY and the network class over [t0, t1) of a simulation. A run whose
    state became NaN (the RK4 diverged, as the deposited Java does too) is labelled
    "numerical failure"."""
    if not sim.finite:
        return ["numerical failure"] * 3 + ["not triphasic"]
''')
open('pyloric.py','w').write(s)
EOF
grep -n "numerical failure" pyloric.py
```

```
503:    "numerical failure"."""
505:        return ["numerical failure"] * 3 + ["not triphasic"]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python - <<'EOF'
s=open('reproduce_alonso_2020.py').read()
a=s.index('# %% [markdown]\n# Check of the search space')
b=s.index('# %% [markdown]\n# The port.')
s=s[:a]+s[b:]
old='''crashT = {n: next((T for T in HOT if SCAN[(n, T)]["classes"][3] != "triphasic"), None) for n in NAMES}
print("lowest temperature above 25 C at which the network is not triphasic:", crashT)'''
new='''failed = sorted((r["key"], r["temp"]) for r in SCAN.values() if r["classes"][0] == "numerical failure")
print(f"runs whose integration diverged (NaN), of {len(NAMES) * (len(TEMPS) + len(HOT))}:", len(failed), failed)
crashT = {n: next((T for T in HOT if SCAN[(n, T)]["classes"][3] != "triphasic" and SCAN[(n, T)]["classes"][0] != "numerical failure"), None)
          for n in NAMES}
print("lowest temperature above 25 C at which the network is not triphasic (diverged runs skipped):", crashT)'''
assert old in s; s=s.replace(old,new)
# finding cell after hot scan
old2='''# %% [markdown]
# ## fig6-crash-different-mechanisms'''
new2='''# %% tags=["finding-diverges-at-high-temperature"]
# The deposited integrator (RK4, dt = 0.05 ms, from the deposited initial conditions) returns NaN for some
# models at high temperature. The port gives NaN where the Java does: G7P2WE at 35 C, LP first, after about 0.1 s.
s35 = P.simulate(MODELS["G7P2WE"], 35.0, 0.2, CI, rec_every=1)
bad = np.where(~np.isfinite(s35.rec).all(axis=1))[0]
print("G7P2WE, 35 C: first sample with NaN", bad[0] if len(bad) else None, "of", len(s35.rec), "(step 0.05 ms);",
      "V there:", s35.rec[bad[0] - 1] if len(bad) else None)
print("models with a diverged run at 26 to 35 C:", sorted({n for n, T in failed}))

# %% [markdown]
# ## fig6-crash-different-mechanisms'''
assert old2 in s; s=s.replace(old2,new2)
open('reproduce_alonso_2020.py','w').write(s)
EOF
grep -n "Check of the search" reproduce_alonso_2020.py; date -u
```

```
/bin/bash: line 1: cd: entries/alonso-2020: No such file or directory
118:# Check of the search space of the Methods (Finding parameters): gNa and gKCa in [0, 1000], the
Fri Nov 27 22:52:00 UTC 2026
```

**Agent calls Bash**

```bash
pwd; python - <<'EOF'
s=open('reproduce_alonso_2020.py').read()
a=s.index('# %% [markdown]\n# Check of the search space')
b=s.index('# %% [markdown]\n# The port.')
s=s[:a]+s[b:]
old='''crashT = {n: next((T for T in HOT if SCAN[(n, T)]["classes"][3] != "triphasic"), None) for n in NAMES}
print("lowest temperature above 25 C at which the network is not triphasic:", crashT)'''
new='''failed = sorted((r["key"], r["temp"]) for r in SCAN.values() if r["classes"][0] == "numerical failure")
print(f"runs whose integration diverged (NaN), of {len(NAMES) * (len(TEMPS) + len(HOT))}:", len(failed), failed)
crashT = {n: next((T for T in HOT if SCAN[(n, T)]["classes"][3] != "triphasic" and SCAN[(n, T)]["classes"][0] != "numerical failure"), None)
          for n in NAMES}
print("lowest temperature above 25 C at which the network is not triphasic (diverged runs skipped):", crashT)'''
assert old in s; s=s.replace(old,new)
old2='''# %% [markdown]
# ## fig6-crash-different-mechanisms'''
new2='''# %% tags=["finding-diverges-at-high-temperature"]
# The deposited integrator (RK4, dt = 0.05 ms, from the deposited initial conditions) returns NaN for some
# models at high temperature. The port gives NaN where the Java does: G7P2WE at 35 C, LP first, after about 0.1 s.
s35 = P.simulate(MODELS["G7P2WE"], 35.0, 0.2, CI, rec_every=1)
bad = np.where(~np.isfinite(s35.rec).all(axis=1))[0]
print("G7P2WE, 35 C: first sample with NaN", bad[0] if len(bad) else None, "of", len(s35.rec), "(step 0.05 ms);",
      "V there:", s35.rec[bad[0] - 1] if len(bad) else None)
print("models with a diverged run at 26 to 35 C:", sorted({n for n, T in failed}))

# %% [markdown]
# ## fig6-crash-different-mechanisms'''
assert old2 in s; s=s.replace(old2,new2)
open('reproduce_alonso_2020.py','w').write(s)
EOF
grep -n "Check of the search\|finding-diverges" reproduce_alonso_2020.py
```

```
entries/alonso-2020
604:# %% tags=["finding-diverges-at-high-temperature"]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('reproduce_alonso_2020.py').read()
s=s.replace('s6 = [M[n] for n in METHODS_NAMES["Figure 6-S1"] if M[n]]','s6 = [M[n] for n in METHODS_NAMES["Figure 6-S1"] if isinstance(M[n], str)]')
open('reproduce_alonso_2020.py','w').write(s)
EOF
cat >> pyloric.py <<'EOF'


# --- ramps and voltage distributions -------------------------------------------------------------

def cycle_largest_isi(spikes, gap=BURST_GAP):
    """Per burst cycle (one burst start to the next): the burst start time and the largest ISI in
    the cycle, which is the interburst interval when the cell bursts."""
    s = np.asarray(spikes)
    st, en, cnt = bursts(s, gap)
    out_t, out_isi = [], []
    for a, b in zip(st[:-1], st[1:]):
        seg = s[(s >= a) & (s <= b)]
        if len(seg) >= 2:
            out_t.append(a)
            out_isi.append(np.max(np.diff(seg)))
    return np.array(out_t), np.array(out_isi)


def window_measures(spk3, t0, t1):
    """Per cell, over [t0, t1): mean duty cycle, mean burst frequency, median per-cycle largest ISI;
    and whether the network is triphasic in the window."""
    w = [s[(s >= t0) & (s < t1)] - t0 for s in spk3]
    out = []
    for s in w:
        b = burst_stats(s)
        t, isi = cycle_largest_isi(s)
        out.append((np.mean(b["dc"]) if len(b["dc"]) else np.nan,
                    np.mean(b["freq"]) if len(b["freq"]) else np.nan,
                    np.median(isi) if len(isi) else np.nan))
    return np.array(out), triphasic(w)


def spike_shapes(V, dt_ms, thr=SPIKE_THRESHOLD, dvdt=10.0):
    """fig2-lp-spike-amplitude-threshold readings (a). For each upward crossing of thr: the peak
    (largest V in the 3 ms after), the trough (lowest V between the previous peak, at most 30 ms
    back, and the crossing), and the threshold (V at the first sample after the trough where
    dV/dt exceeds dvdt mV/ms, a standard choice). Returns arrays of peak, trough, threshold."""
    cross = np.where((V[:-1] < thr) & (V[1:] >= thr))[0]
    n3, n30 = int(round(3 / dt_ms)), int(round(30 / dt_ms))
    d = np.diff(V) / dt_ms
    peaks, troughs, ths = [], [], []
    prev = -10 ** 9
    for i in cross:
        if i + n3 > len(V):
            break
        a = max(prev, i - n30, 0)
        if i - a < 2:
            prev = i + int(np.argmax(V[i:i + n3]))
            continue
        k = a + int(np.argmin(V[a:i + 1]))
        up = np.where(d[k:i + 1] > dvdt)[0]
        pk = i + int(np.argmax(V[i:i + n3]))
        peaks.append(V[pk]); troughs.append(V[k]); ths.append(V[k + up[0]] if len(up) else np.nan)
        prev = pk
    return np.array(peaks), np.array(troughs), np.array(ths)


def run_distribution(task):
    """task = (key, p, y0, temp, seconds, last, dt, every). Simulates `seconds` at dt from y0 and
    keeps V of each cell every `every` steps over the last `last` seconds (Methods, Membrane
    potential and current shares distributions: 30 s, dt = 0.001, the last 10 s, 5 x 10^5
    samples). Returns, per cell, the histogram (0.1 mV bins from -100 mV), mean V, the upper
    envelope (highest V), the lowest V and the spike shape summaries."""
    key, p, y0, temp, seconds, last, dt, every = task
    s = simulate(p, temp, seconds, y0, dt=dt, rec_every=every, rec_from=seconds - last)
    V3 = s.rec
    res = []
    edges = -100.0 + 0.1 * np.arange(1601)
    for c in range(3):
        V = V3[:, c]
        h, _ = np.histogram(V, edges)
        pk, tr, th = spike_shapes(V, dt * every)
        res.append(dict(cell=CELLS[c], n=len(V), mean=float(np.mean(V)), vmax=float(np.max(V)), vmin=float(np.min(V)),
                        hist=h, spikes=len(pk), peak=float(np.mean(pk)) if len(pk) else np.nan,
                        amp=float(np.mean(pk - tr)) if len(pk) else np.nan,
                        thr=float(np.nanmean(th)) if len(th) and np.isfinite(th).any() else np.nan))
    return dict(key=key, temp=temp, finite=s.finite, cells=res)
EOF
python -c "import ast;ast.parse(open('pyloric.py').read())"; date -u
```

```
Fri Nov 27 22:52:47 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('pyloric.py').read()
s=s.replace("out.append(dict(T0=T0, T1=T1, seconds=sec, spikes=s.spikes, sw_up=s.sw_up))","out.append(dict(T0=T0, T1=T1, seconds=sec, spikes=s.spikes, sw_up=s.sw_up, finite=s.finite))")
open('pyloric.py','w').write(s)
EOF
grep -n "finite=s.finite" pyloric.py
```

```
552:        out.append(dict(T0=T0, T1=T1, seconds=sec, spikes=s.spikes, sw_up=s.sw_up, finite=s.finite))
680:    return dict(key=key, temp=temp, finite=s.finite, cells=res)
```

**Agent**

Now the ramps notebook.

**Agent calls Write**

```json
{
 "file_path": "entries/alonso-2020/ramps.py",
 "content": "# %% [markdown]\n# # Alonso & Marder (2020), temperature ramps, from Dryad m31b1h7\n#\n# Paper: Alonso LM, Marder E (2020), eLife 9:e55470, doi:10.7554/eLife.55470; claims in\n# `claims/alonso-2020.yaml` (version of record, main text, legends and Methods).\n#\n# Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811 (the only published version, so the\n# one pinned), file `alonso_marder_tempcomp_2019_root.zip` (MD5 from Dryad's file list checked on\n# load; SHA-256 printed below). The models are simulated with the port in `pyloric.py`; the main\n# notebook, `reproduce_alonso_2020.ipynb`, compares it with the deposited Java and checks the data.\n#\n# Two ramp protocols, every deposited model (38):\n#\n# - up: 10 to 25 degrees C over 60 min (Results, Duty cycle and phase maintenance, paragraph 5,\n#   \"ramps from 10 C to 25 C over 60 min\"), for figs2-ramp-largest-isi and\n#   figs3-duty-cycle-variable-across-models;\n# - updown: 10 to 35 degrees C in 30 min and back to 10 degrees C at the same rate (Results,\n#   Hysteresis and multistability, paragraph 1), for fig8a-hysteresis-quiescence,\n#   fig8-up-down-ramps and fig8b-pathological-attractor.\n#\n# The deposit holds no ramp code; the temperature is updated at every step, linearly in time, and\n# each ramp starts from the deposited initial conditions at its first temperature (assumptions).\n#\n# | Claim | Tested |\n# |---|---|\n# | figs2-ramp-largest-isi | tested |\n# | figs3-duty-cycle-variable-across-models | tested |\n# | fig8a-hysteresis-quiescence | tested |\n# | fig8-up-down-ramps | tested (main ramp reading only) |\n# | fig8b-pathological-attractor | tested |\n\n# %%\nimport resource\nimport time\nfrom itertools import combinations\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\n\nimport pyloric as P\n\nT_START = time.time()\npd.set_option(\"display.width\", 200, \"display.max_columns\", 40, \"display.max_rows\", 200)\nraw = P.read_zip_bytes()\nprint(P.digests(raw))\nZ = P.open_zip(raw)\nMODELS = P.load_models(Z)\nCI = P.load_ci(Z)\nNAMES = list(MODELS)\n\n# %% [markdown]\n# ## Data check and the runs\n#\n# A subset (one model, 60 s of each ramp) was timed while preparing; the full runs take about 3\n# min of one CPU per model and ramp. Every model is run on 4 processes.\n\n# %% tags=[\"sanity\"]\nprint(len(NAMES), \"models:\", NAMES)\nprint(\"parameters per model:\", {len(p) for p in MODELS.values()}, \"; initial state:\", len(CI), \"numbers\")\nt0 = time.time()\nUP = {r[\"key\"]: r for r in P.pmap(P.run_ramp, [(n, MODELS[n], CI, [(10.0, 25.0, 3600.0)]) for n in NAMES])}\nprint(f\"up ramps: {time.time() - t0:.0f} s\")\nt0 = time.time()\nUD = {r[\"key\"]: r for r in P.pmap(P.run_ramp, [(n, MODELS[n], CI, [(10.0, 35.0, 1800.0), (35.0, 10.0, 1800.0)]) for n in NAMES])}\nprint(f\"up-down ramps: {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nprint(\"runs that diverged (NaN):\", [n for n in NAMES if not UP[n][\"legs\"][0][\"finite\"]],\n      [(n, i) for n in NAMES for i in range(2) if not UD[n][\"legs\"][i][\"finite\"]])\nspk = pd.DataFrame({n: [len(s) for s in UP[n][\"legs\"][0][\"spikes\"]] + [len(s) for leg in UD[n][\"legs\"] for s in leg[\"spikes\"]]\n                    for n in NAMES}, index=[\"up PD\", \"up LP\", \"up PY\", \"ud-up PD\", \"ud-up LP\", \"ud-up PY\", \"ud-down PD\", \"ud-down LP\", \"ud-down PY\"]).T\nprint(\"spike counts per run and cell:\")\nprint(spk.describe().round(0).to_string())\n\n# %% [markdown]\n# ## figs2-ramp-largest-isi\n#\n# > During a temperature ramp from 10 to 25 degrees C over 60 min, the spiking patterns change in\n# > complicated ways and the largest ISI decreases monotonically, in step with the rising burst\n# > frequency.\n#\n# PLKTEM, the up ramp. The largest ISI of each burst cycle (burst start to the next); per window,\n# its median over the cycles that start in the window. Readings: windows of 1 degree C (4 min) and\n# of 1 min.\n\n# %% tags=[\"claim:figs2-ramp-largest-isi\"]\nleg = UP[\"PLKTEM\"][\"legs\"][0]\nres2 = {}\nfor label, w in ((\"a, 4 min\", 240.0), (\"b, 1 min\", 60.0)):\n    edges = np.arange(0, 3600.0 + 1e-9, w)\n    temps = 10 + 15 * (edges[:-1] + w / 2) / 3600\n    out = {}\n    for c, cell in enumerate(P.CELLS):\n        t, isi = P.cycle_largest_isi(leg[\"spikes\"][c])\n        med = np.array([np.median(isi[(t >= a) & (t < b)]) if ((t >= a) & (t < b)).any() else np.nan for a, b in zip(edges[:-1], edges[1:])])\n        ok = np.isfinite(med)\n        rho = stats.spearmanr(temps[ok], med[ok])[0]\n        inc = np.where(np.diff(med[ok]) > 0)[0]\n        out[cell] = dict(rho=rho, increases=len(inc), windows=int(ok.sum()), first=med[ok][0], last=med[ok][-1])\n        if label.startswith(\"a\"):\n            print(cell, \"median largest ISI per window (s):\", np.round(med, 3))\n    res2[label] = out\n    print(f\"reading ({label}):\", {k: {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in out.items()})\n    print(\"   cells with Spearman below -0.9:\", sum(v[\"rho\"] < -0.9 for v in out.values()))\nfig, ax = plt.subplots(1, 3, figsize=(12, 3), sharey=True)\nfor c, cell in enumerate(P.CELLS):\n    t, isi = P.cycle_largest_isi(leg[\"spikes\"][c])\n    ax[c].plot(10 + 15 * t / 3600, isi, \".\", ms=1); ax[c].set_title(cell); ax[c].set_xlabel(\"temperature (C)\")\n    print(f\"{cell}: per-cycle largest ISI from {isi.min():.3f} to {isi.max():.3f} s, {len(isi)} cycles\")\nax[0].set_ylabel(\"largest ISI per cycle (s)\"); plt.tight_layout(); plt.show()\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## figs3-duty-cycle-variable-across-models\n#\n# > Across the 36 models the LP duty cycle depends on temperature in different ways, so that the\n# > duty cycle distributions differ from model to model.\n#\n# Per-burst LP duty cycles over the up ramp, every deposited model (38, so 703 pairs); two-sample\n# Kolmogorov-Smirnov test per pair. The variant with the 16 fixed temperatures is in the main\n# notebook's simulations and is not repeated here.\n\n# %% tags=[\"claim:figs3-duty-cycle-variable-across-models\"]\nDC = {n: P.burst_stats(UP[n][\"legs\"][0][\"spikes\"][1])[\"dc\"] for n in NAMES}\nsumm = pd.DataFrame({n: dict(bursts=len(d), median=np.median(d), lo=np.min(d), hi=np.max(d)) for n, d in DC.items()}).T\nprint(summ.round(3).to_string())\npv = np.array([stats.ks_2samp(DC[a], DC[b]).pvalue for a, b in combinations(NAMES, 2)])\nprint(f\"\\npairs: {len(pv)}; with p < 0.05: {(pv < 0.05).sum()} ({(pv < 0.05).mean():.3f})\")\ndup = [(\"0SHNMD\", \"B7SD0L\"), (\"4X6W66\", \"FGFKQS\"), (\"J9U8SQ\", \"TGCEVM\")]\nfor a, b in dup:\n    print(f\"   same conductances, different Q10: {a} vs {b}: KS p = {stats.ks_2samp(DC[a], DC[b]).pvalue:.2e}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig8a-hysteresis-quiescence\n#\n# > During a temperature ramp from 10 to 35 degrees C and back, the PD cell of one model becomes\n# > quiescent before reaching 35 degrees C and resumes spiking on the way down at a temperature\n# > about 2 degrees C lower than where it stopped ...\n#\n# OSHNMD of the Methods is 0SHNMD in the deposit (the letter O read as the digit 0); H5AIZR is the\n# variant.\n\n# %% tags=[\"claim:fig8a-hysteresis-quiescence\"]\ndef fig8a(name):\n    up, down = UD[name][\"legs\"]\n    su, sd = up[\"spikes\"][0], down[\"spikes\"][0]\n    if len(su) == 0 or len(sd) == 0:\n        print(name, \"no PD spikes on a leg\"); return None\n    t_last = su[-1]; T_last = 10 + 25 * t_last / 1800\n    t_first = sd[0]; T_first = 35 - 25 * t_first / 1800\n    gap_up = 1800 - t_last\n    print(f\"{name}: last PD spike on the up ramp at {t_last:.1f} s ({T_last:.2f} C); first PD spike on the down ramp at \"\n          f\"{t_first:.1f} s after its start ({T_first:.2f} C); quiescent for {gap_up + t_first:.1f} s across the top; \"\n          f\"difference {T_last - T_first:.2f} C\")\n    lu = np.diff(su); print(f\"   longest PD ISI on the up ramp before the last spike: {lu.max():.2f} s\")\n    return T_last, T_first, T_last - T_first, t_last\n\nr8a = fig8a(\"0SHNMD\")\nr8a_var = fig8a(\"H5AIZR\")\nfor n in NAMES:\n    up, down = UD[n][\"legs\"]\n    if len(up[\"spikes\"][0]) and up[\"spikes\"][0][-1] < 1790:\n        print(f\"   models whose PD stops before 35 C on the up ramp: {n}, last spike at {10 + 25 * up['spikes'][0][-1] / 1800:.2f} C\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig8-up-down-ramps\n#\n# > In 34 of the 36 models the spiking patterns over the working range are similar but not\n# > identical on the up and down ramps ...\n#\n# The updown ramp; per cell and per 1 degree window from 10 to 25 degrees C (72 s each), mean duty\n# cycle, mean burst frequency and median per-cycle largest ISI on each leg; similar when all are\n# within 10% between legs in every window and the network is triphasic in every window on both.\n# The second ramp reading (10 to 25 degrees C over 60 min and back) is not run here (see the\n# summary).\n\n# %% tags=[\"claim:fig8-up-down-ramps\"]\ndef legs_compare(name):\n    up, down = UD[name][\"legs\"]\n    worst, trip, ident = 0.0, True, True\n    for k in range(15):\n        a, b = 72.0 * k, 72.0 * (k + 1)                   # up: 10+k to 11+k C\n        da, db = 1800 - 72.0 * (k + 1), 1800 - 72.0 * k     # down: the same temperatures\n        mu, tu = P.window_measures(up[\"spikes\"], a, b)\n        md, td = P.window_measures(down[\"spikes\"], da, db)\n        rel = np.abs(md / mu - 1)\n        worst = max(worst, np.nanmax(rel) if np.isfinite(rel).any() else np.inf)\n        if not np.isfinite(rel).all():\n            worst = np.inf\n        trip = trip and tu and td\n    nu = [len(s[s < 1080]) for s in up[\"spikes\"]]\n    nd = [len(s[s >= 720]) for s in down[\"spikes\"]]\n    return worst, trip, nu, nd\n\nrows = []\nfor n in NAMES:\n    worst, trip, nu, nd = legs_compare(n)\n    rows.append(dict(model=n, largest_rel_diff=worst, triphasic_all_windows=trip, similar=bool(worst <= 0.1 and trip),\n                     spikes_up=sum(nu), spikes_down=sum(nd)))\nt8 = pd.DataFrame(rows).set_index(\"model\")\nprint(t8.round(3).to_string())\nprint(f\"\\nsimilar (within 10% and triphasic in every window): {int(t8.similar.sum())} of {len(t8)}\")\nprint(f\"identical spike counts on the two legs (10 to 25 C): {int((t8.spikes_up == t8.spikes_down).sum())}\")\nfor thr in (0.05, 0.1, 0.2):\n    print(f\"   threshold {thr:.2f}: similar {int(((t8.largest_rel_diff <= thr) & t8.triphasic_all_windows).sum())}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig8b-pathological-attractor\n#\n# > In a second model hysteresis is marked; at high temperatures it produces ISIs as long as about\n# > 1 s while spiking at all temperatures, and its PD cell passes from regular bursting into a\n# > pathological state that persists on the down ramp until about 20 degrees C.\n#\n# H5AIZR (0SHNMD the variant). PD classified in successive 1 min windows of the updown ramp.\n\n# %% tags=[\"claim:fig8b-pathological-attractor\"]\ndef fig8b(name):\n    up, down = UD[name][\"legs\"]\n    spikes = np.r_[up[\"spikes\"][0], 1800 + down[\"spikes\"][0]]\n    swu = np.r_[up[\"sw_up\"][0], 1800 + down[\"sw_up\"][0]]\n    cls, temps = [], []\n    for k in range(60):\n        a, b = 60.0 * k, 60.0 * (k + 1)\n        s = spikes[(spikes >= a) & (spikes < b)] - a\n        u = swu[(swu >= a) & (swu < b)] - a\n        cls.append(P.classify_cell(s, u))\n        mid = a + 30\n        temps.append(10 + 25 * mid / 1800 if mid < 1800 else 35 - 25 * (mid - 1800) / 1800)\n    cls = np.array(cls); temps = np.array(temps)\n    nspk = [int(((spikes >= 60 * k) & (spikes < 60 * (k + 1))).sum()) for k in range(60)]\n    rb = cls == \"regular bursting\"\n    left_up = not rb[:30].all()\n    # return: the start of the last run of regular bursting windows on the down ramp\n    k = 59\n    while k >= 30 and rb[k]:\n        k -= 1\n    T_return = temps[k + 1] if k < 59 else np.nan\n    sel = (spikes >= 1500) & (spikes < 2100)\n    longest = np.diff(spikes[sel]).max() if sel.sum() > 1 else np.nan\n    print(f\"{name}: PD classes per minute:\")\n    for i in range(0, 60, 6):\n        print(\"   \", [f\"{temps[j]:.1f}C {cls[j]}\" for j in range(i, i + 6)])\n    print(f\"   spikes in every window {min(nspk) > 0} (fewest {min(nspk)}); regular bursting in the first window {rb[0]}; \"\n          f\"leaves regular bursting on the up ramp {left_up}; returns to it for good on the down ramp at {T_return:.2f} C; \"\n          f\"longest PD ISI between 25 and 35 min {longest:.3f} s\")\n    return dict(all_spiking=min(nspk) > 0, early_rb=bool(rb[0]), left=left_up, T_return=T_return, longest=longest)\n\nr8b = fig8b(\"H5AIZR\")\nr8b_var = fig8b(\"0SHNMD\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (written after the run)\n\n# %%\nprint(f\"notebook run time {(time.time() - T_START) / 60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: entries/alonso-2020/ramps.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('ramps.py').read()
s=s.replace('NAMES = list(MODELS)','NAMES = ["PLKTEM","0SHNMD","H5AIZR","4X6W66"]')
open('/tmp/claude-1001/ramps_dev.py','w').write(s)
EOF
cp pyloric.py $TMPDIR/ && cd $TMPDIR && sed -i 's/3600\.0/360.0/g; s/1800\.0/180.0/g' ramps_dev.py && jupytext --to ipynb -q ramps_dev.py -o ramps_dev.ipynb && time jupyter nbconvert --to notebook --execute --allow-errors ramps_dev.ipynb --output ramps_dev_out.ipynb 2>&1 | tail -1; python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/ramps_dev_out.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        if o.output_type=='stream': print(o.text[:2500])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
```

```
[NbConvertApp] Writing 86742 bytes to ramps_dev_out.ipynb

real	0m48.257s
user	3m2.323s
sys	0m1.941s
{'md5': '37766522dabaaa620d4c44264e76e686', 'sha256': '327279e2c4553c0b946bf230260caf0f7321e36bc5201ad7d65bbe6638d2df08', 'bytes': 99026}

4 models: ['PLKTEM', '0SHNMD', 'H5AIZR', '4X6W66']
parameters per model: {132} ; initial state: 46 numbers

up ramps: 24 s

up-down ramps: 22 s; peak memory 0.25 GB
runs that diverged (NaN): [] []
spike counts per run and cell:
        up PD   up LP   up PY  ud-up PD  ud-up LP  ud-up PY  ud-down PD  ud-down LP  ud-down PY
count     4.0     4.0     4.0       4.0       4.0       4.0         4.0         4.0         4.0
mean   5602.0  6213.0  7276.0    2871.0    3844.0    3826.0      2698.0      3505.0      3427.0
std     800.0   905.0  2017.0     464.0     581.0     671.0       521.0       733.0      1044.0
min    4712.0  5321.0  5429.0    2320.0    3408.0    3071.0      2223.0      2938.0      2489.0
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python - <<'EOF'
s=open('pyloric.py').read()
old="""        if ramp:
            _factors(p, T0 + (T1 - T0) * i / nsteps, f)"""
new="""        if ramp and i % 20 == 0:
            _factors(p, T0 + (T1 - T0) * (i + 10) / nsteps, f)"""
assert old in s; s=s.replace(old,new)
s=s.replace("""- Temperature ramps: the deposit holds no ramp code. The temperature is updated at every step,
  linearly in time (an assumption; the Results give only the start, end and duration of a ramp).""","""- Temperature ramps: the deposit holds no ramp code. The temperature changes linearly in time
  and the temperature factors are updated every 20 steps (1 ms), at the temperature of the middle
  of those 20 steps (an assumption; the Results give only the start, end and duration of a ramp;
  over 1 ms a 60 min ramp moves by less than 1e-5 degrees C).""")
open('pyloric.py','w').write(s)
EOF
source $TMPDIR/dev/bin/activate && python -c "
import time, pyloric as P
raw=P.read_zip_bytes(); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
P.simulate(M['PLKTEM'],10,1,ci,temp_end=11)
t=time.time(); s=P.simulate(M['PLKTEM'],10,60,ci,temp_end=25); print('60 s ramp', time.time()-t)
t=time.time(); s=P.simulate(M['PLKTEM'],10,60,ci); print('60 s fixed', time.time()-t)
"
```

```
60 s ramp 1.8651092052459717
60 s fixed 1.844886064529419
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python - <<'EOF'
s=open('ramps.py').read()
s=s.replace('''# Two ramp protocols, every deposited model (38):
#
# - up: 10 to 25 degrees C over 60 min (Results, Duty cycle and phase maintenance, paragraph 5,
#   "ramps from 10 C to 25 C over 60 min"), for figs2-ramp-largest-isi and
#   figs3-duty-cycle-variable-across-models;
# - updown: 10 to 35 degrees C in 30 min and back to 10 degrees C at the same rate (Results,
#   Hysteresis and multistability, paragraph 1), for fig8a-hysteresis-quiescence,
#   fig8-up-down-ramps and fig8b-pathological-attractor.''','''Two ramp protocols:
#
# - up: 10 to 25 degrees C over 60 min (Results, Duty cycle and phase maintenance, paragraph 5,
#   "ramps from 10 C to 25 C over 60 min"), model PLKTEM, for figs2-ramp-largest-isi;
# - updown: 10 to 35 degrees C in 30 min and back to 10 degrees C at the same rate (Results,
#   Hysteresis and multistability, paragraph 1), every deposited model (38), for
#   fig8a-hysteresis-quiescence, fig8-up-down-ramps and fig8b-pathological-attractor.
#
# The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
# reading, would add about 35 min to this notebook (38 models x 3600 s at about 67 simulated
# seconds per second on the runner's 4 CPUs, measured on a subset); it is not run, and that claim
# is tested in the main notebook on its variant, the 16 fixed temperatures.''')
s=s.replace('''# | figs3-duty-cycle-variable-across-models | tested |
''','')
s=s.replace('''UP = {r["key"]: r for r in P.pmap(P.run_ramp, [(n, MODELS[n], CI, [(10.0, 25.0, 3600.0)]) for n in NAMES])}
print(f"up ramps: {time.time() - t0:.0f} s")
t0 = time.time()
UD = {r["key"]: r for r in P.pmap(P.run_ramp, [(n, MODELS[n], CI, [(10.0, 35.0, 1800.0), (35.0, 10.0, 1800.0)]) for n in NAMES])}
print(f"up-down ramps: {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
print("runs that diverged (NaN):", [n for n in NAMES if not UP[n]["legs"][0]["finite"]],
      [(n, i) for n in NAMES for i in range(2) if not UD[n]["legs"][i]["finite"]])
spk = pd.DataFrame({n: [len(s) for s in UP[n]["legs"][0]["spikes"]] + [len(s) for leg in UD[n]["legs"] for s in leg["spikes"]]
                    for n in NAMES}, index=["up PD", "up LP", "up PY", "ud-up PD", "ud-up LP", "ud-up PY", "ud-down PD", "ud-down LP", "ud-down PY"]).T''','''tasks = [("UP " + "PLKTEM", MODELS["PLKTEM"], CI, [(10.0, 25.0, 3600.0)])]
tasks += [(n, MODELS[n], CI, [(10.0, 35.0, 1800.0), (35.0, 10.0, 1800.0)]) for n in NAMES]
out = P.pmap(P.run_ramp, tasks)
UP = {"PLKTEM": out[0]}
UD = {r["key"]: r for r in out[1:]}
print(f"ramps: {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
print("runs that diverged (NaN):", [n for n in UP if not UP[n]["legs"][0]["finite"]],
      [(n, i) for n in NAMES for i in range(2) if not UD[n]["legs"][i]["finite"]])
print("PLKTEM up ramp, spikes per cell:", [len(s) for s in UP["PLKTEM"]["legs"][0]["spikes"]])
spk = pd.DataFrame({n: [len(s) for leg in UD[n]["legs"] for s in leg["spikes"]]
                    for n in NAMES}, index=["up PD", "up LP", "up PY", "down PD", "down LP", "down PY"]).T''')
a=s.index('# %% [markdown]\n# ## figs3-duty-cycle-variable-across-models')
b=s.index('# %% [markdown]\n# ## fig8a-hysteresis-quiescence')
s=s[:a]+s[b:]
open('ramps.py','w').write(s)
EOF
grep -n "figs3\|UP\[" ramps.py | head
```

```
/bin/bash: line 1: cd: entries/alonso-2020: No such file or directory
16:#   figs3-duty-cycle-variable-across-models;
27:# | figs3-duty-cycle-variable-across-models | tested |
68:print("runs that diverged (NaN):", [n for n in NAMES if not UP[n]["legs"][0]["finite"]],
70:spk = pd.DataFrame({n: [len(s) for s in UP[n]["legs"][0]["spikes"]] + [len(s) for leg in UD[n]["legs"] for s in leg["spikes"]]
87:leg = UP["PLKTEM"]["legs"][0]
116:# ## figs3-duty-cycle-variable-across-models
125:# %% tags=["claim:figs3-duty-cycle-variable-across-models"]
126:DC = {n: P.burst_stats(UP[n]["legs"][0]["spikes"][1])["dc"] for n in NAMES}
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ramps.py').read()
old_hdr = s[s.index('# Two ramp protocols'):s.index('# The deposit holds no ramp code')]
s=s.replace(old_hdr,'''# Two ramp protocols:
#
# - up: 10 to 25 degrees C over 60 min (Results, Duty cycle and phase maintenance, paragraph 5,
#   "ramps from 10 C to 25 C over 60 min"), model PLKTEM, for figs2-ramp-largest-isi;
# - updown: 10 to 35 degrees C in 30 min and back to 10 degrees C at the same rate (Results,
#   Hysteresis and multistability, paragraph 1), every deposited model (38), for
#   fig8a-hysteresis-quiescence, fig8-up-down-ramps and fig8b-pathological-attractor.
#
# The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
# reading, would add about 35 min to this notebook (38 models x 3600 s at about 67 simulated
# seconds per second on 4 CPUs, measured on a subset); it is not run, and that claim is tested
# in the main notebook on its variant, the 16 fixed temperatures.
#
''')
s=s.replace('''# | figs3-duty-cycle-variable-across-models | tested |
''','')
old=s[s.index('UP = {r["key"]'):s.index('print("spike counts per run and cell:")')]
s=s.replace(old,'''tasks = [("UP PLKTEM", MODELS["PLKTEM"], CI, [(10.0, 25.0, 3600.0)])]
tasks += [(n, MODELS[n], CI, [(10.0, 35.0, 1800.0), (35.0, 10.0, 1800.0)]) for n in NAMES]
out = P.pmap(P.run_ramp, tasks)
UP = {"PLKTEM": out[0]}
UD = {r["key"]: r for r in out[1:]}
print(f"ramps: {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
print("runs that diverged (NaN):", [n for n in UP if not UP[n]["legs"][0]["finite"]],
      [(n, i) for n in NAMES for i in range(2) if not UD[n]["legs"][i]["finite"]])
print("PLKTEM up ramp, spikes per cell:", [len(s) for s in UP["PLKTEM"]["legs"][0]["spikes"]])
spk = pd.DataFrame({n: [len(s) for leg in UD[n]["legs"] for s in leg["spikes"]] for n in NAMES},
                   index=["up PD", "up LP", "up PY", "down PD", "down LP", "down PY"]).T
''')
a=s.index('# %% [markdown]\n# ## figs3-duty-cycle-variable-across-models')
b=s.index('# %% [markdown]\n# ## fig8a-hysteresis-quiescence')
s=s[:a]+s[b:]
s=s.replace("# A subset (one model, 60 s of each ramp) was timed while preparing; the full runs take about 3\n# min of one CPU per model and ramp. Every model is run on 4 processes.",
"# A subset (four models, 360 s ramps) was timed while preparing: about 67 simulated seconds per\n# second on 4 processes, so about 35 min for these runs.")
open('ramps.py','w').write(s)
EOF
grep -n "figs3\|UP\[\|subset" ramps.py | head
```

```
20:# The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
22:# seconds per second on 4 CPUs, measured on a subset); it is not run, and that claim is tested
59:# A subset (four models, 360 s ramps) was timed while preparing: about 67 simulated seconds per
72:print("runs that diverged (NaN):", [n for n in UP if not UP[n]["legs"][0]["finite"]],
74:print("PLKTEM up ramp, spikes per cell:", [len(s) for s in UP["PLKTEM"]["legs"][0]["spikes"]])
92:leg = UP["PLKTEM"]["legs"][0]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('reproduce_alonso_2020.py').read()
anchor='''# %% [markdown]
# ## intermediate-temperature-failures'''
new='''# %% [markdown]
# ## figs3-duty-cycle-variable-across-models
#
# > Across the 36 models the LP duty cycle depends on temperature in different ways, so that the
# > duty cycle distributions differ from model to model.
#
# The criterion's main reading is the 60 min ramp of every model, which is not run (it would add
# about 35 min; see `ramps.ipynb`). This is its variant: per-burst LP duty cycles from the 16
# fixed temperatures (30 s each), pooled per model; two-sample Kolmogorov-Smirnov test for every
# pair of the 38 deposited models (703 pairs).

# %% tags=["claim:figs3-duty-cycle-variable-across-models"]
DC = {n: np.concatenate([P.burst_stats(SCAN[(n, T)]["spikes"][1])["dc"] for T in TEMPS]) for n in NAMES}
summ = pd.DataFrame({n: dict(bursts=len(d), median=np.median(d), lo=np.min(d), hi=np.max(d)) for n, d in DC.items()}).T
print(summ.round(3).to_string())
pv = np.array([stats.ks_2samp(DC[a], DC[b]).pvalue for a, b in combinations(NAMES, 2)])
print(f"\\npairs: {len(pv)}; with p < 0.05: {(pv < 0.05).sum()} ({(pv < 0.05).mean():.3f})")
for g in multi:
    for a, b in combinations(g, 2):
        print(f"   same conductances, different Q10: {a} vs {b}: KS p = {stats.ks_2samp(DC[a], DC[b]).pvalue:.2e}")
lp = pd.DataFrame({n: [np.mean(P.burst_stats(SCAN[(n, T)]["spikes"][1])["dc"]) for T in TEMPS] for n in NAMES}, index=TEMPS.astype(int))
rho = lp.apply(lambda c: stats.spearmanr(lp.index, c)[0])
print("Spearman correlation of mean LP duty cycle with temperature, per model: from %.2f to %.2f; "
      "below -0.5: %d, above 0.5: %d, between: %d" % (rho.min(), rho.max(), (rho < -0.5).sum(), (rho > 0.5).sum(),
                                                      ((rho >= -0.5) & (rho <= 0.5)).sum()))

# %% [markdown]
# **Result: ...**

''' + anchor
assert anchor in s
s=s.replace(anchor,new,1)
s=s.replace("# | figs3-duty-cycle-variable-across-models | ramps | tested |","# | figs3-duty-cycle-variable-across-models | this | tested (variant reading) |")
s=s.replace("# (figs2-ramp-largest-isi, figs3-duty-cycle-variable-across-models, fig8a-hysteresis-quiescence,\n# fig8-up-down-ramps, fig8b-pathological-attractor)","# (figs2-ramp-largest-isi, fig8a-hysteresis-quiescence, fig8-up-down-ramps,\n# fig8b-pathological-attractor)")
open('reproduce_alonso_2020.py','w').write(s)
EOF
grep -n "figs3" reproduce_alonso_2020.py | head
```

```
36:# | figs3-duty-cycle-variable-across-models | this | tested (variant reading) |
403:# ## figs3-duty-cycle-variable-across-models
413:# %% tags=["claim:figs3-duty-cycle-variable-across-models"]
```

**Agent calls Write**

```json
{
 "file_path": "entries/alonso-2020/voltage_distributions.py",
 "content": "# %% [markdown]\n# # Alonso & Marder (2020), membrane potential distributions, from Dryad m31b1h7\n#\n# Paper: Alonso LM, Marder E (2020), eLife 9:e55470, doi:10.7554/eLife.55470; claims in\n# `claims/alonso-2020.yaml` (version of record, main text, legends and Methods).\n#\n# Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811 (the only published version, so the\n# one pinned), file `alonso_marder_tempcomp_2019_root.zip` (MD5 from Dryad's file list checked on\n# load; SHA-256 printed below). The models are simulated with the port in `pyloric.py`, compared\n# with the deposited Java in `reproduce_alonso_2020.ipynb`.\n#\n# Method (Materials and methods, Membrane potential and current shares distributions): each\n# temperature simulated from the deposited initial conditions for 30 s at dt = 0.001 ms; the last\n# 10 s used; 5 x 10^5 samples per distribution, so V is kept every 20 steps (0.02 ms). Histograms\n# in 0.1 mV bins (a plotting choice).\n#\n# The Methods use 101 temperatures. At dt = 0.001 ms one temperature costs about 1500 simulated\n# seconds at dt = 0.05 (50 times the steps), about 23 s of the runner's 4 CPUs, so 101\n# temperatures would take about 40 min. This notebook uses 26 temperatures, 10 to 25 degrees C in\n# steps of 0.6 degrees C, for G7P2WE, and 6 (10, 13, 16, 19, 22, 25 degrees C, all on that grid)\n# for 4X6W66 and MAXTTP.\n#\n# | Claim | Tested |\n# |---|---|\n# | fig2-lp-spike-amplitude-threshold | tested (26 of 101 temperatures) |\n# | fig2s1-peak-voltage-diverse | tested (6 temperatures) |\n\n# %%\nimport resource\nimport time\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\n\nimport pyloric as P\n\nT_START = time.time()\npd.set_option(\"display.width\", 200, \"display.max_columns\", 40, \"display.max_rows\", 200)\nraw = P.read_zip_bytes()\nprint(P.digests(raw))\nZ = P.open_zip(raw)\nMODELS = P.load_models(Z)\nCI = P.load_ci(Z)\n\n# %% [markdown]\n# ## Data check and the runs\n\n# %% tags=[\"sanity\"]\nprint(len(MODELS), \"models; used here: G7P2WE, 4X6W66 (4?6W66 of the Methods), MAXTTP\")\nT26 = np.round(10 + 0.6 * np.arange(26), 1)\nT6 = np.array([10.0, 13.0, 16.0, 19.0, 22.0, 25.0])\ntasks = [((\"G7P2WE\", T), MODELS[\"G7P2WE\"], CI, T, 30.0, 10.0, 0.001, 20) for T in T26]\ntasks += [((n, T), MODELS[n], CI, T, 30.0, 10.0, 0.001, 20) for n in (\"4X6W66\", \"MAXTTP\") for T in T6]\nt0 = time.time()\nDIST = {r[\"key\"]: r for r in P.pmap(P.run_distribution, tasks)}\nprint(f\"{len(tasks)} runs in {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nprint(\"all runs finite:\", all(r[\"finite\"] for r in DIST.values()))\nprint(\"samples per distribution:\", {r[\"cells\"][0][\"n\"] for r in DIST.values()})\nrows = [dict(model=k[0], T=k[1], cell=c[\"cell\"], mean=c[\"mean\"], vmin=c[\"vmin\"], vmax=c[\"vmax\"], spikes=c[\"spikes\"]) for k, r in DIST.items() for c in r[\"cells\"]]\nD = pd.DataFrame(rows)\nprint(\"V range over all runs: %.1f to %.1f mV\" % (D.vmin.min(), D.vmax.max()))\nprint(D.groupby([\"model\", \"cell\"])[[\"mean\", \"vmin\", \"vmax\", \"spikes\"]].agg([\"min\", \"max\"]).round(1).to_string())\n\n# %% [markdown]\n# ## fig2-lp-spike-amplitude-threshold\n#\n# > In the LP cell of the model of Figure 2, spike amplitude decreases and the spike threshold\n# > depolarizes as temperature rises from 10 to 25 degrees C.\n#\n# G7P2WE, LP. Amplitude readings: (a) mean spike peak minus the mean trough before each spike\n# (`pyloric.spike_shapes`); (b) the upper envelope, the highest V in the distribution. Threshold\n# reading (a): V where dV/dt first exceeds 10 mV/ms after the trough before each spike. Threshold\n# reading (b), where the distribution's spike region begins, is not computed (see the summary).\n\n# %% tags=[\"claim:fig2-lp-spike-amplitude-threshold\"]\nlp = pd.DataFrame([dict(T=T, amp_a=DIST[(\"G7P2WE\", T)][\"cells\"][1][\"amp\"], envelope_b=DIST[(\"G7P2WE\", T)][\"cells\"][1][\"vmax\"],\n                        threshold_a=DIST[(\"G7P2WE\", T)][\"cells\"][1][\"thr\"], spikes=DIST[(\"G7P2WE\", T)][\"cells\"][1][\"spikes\"],\n                        peak=DIST[(\"G7P2WE\", T)][\"cells\"][1][\"peak\"], mean_V=DIST[(\"G7P2WE\", T)][\"cells\"][1][\"mean\"]) for T in T26]).set_index(\"T\")\nprint(lp.round(2).to_string())\nr_amp_a = stats.spearmanr(lp.index, lp.amp_a)[0]\nr_amp_b = stats.spearmanr(lp.index, lp.envelope_b)[0]\nr_thr_a = stats.spearmanr(lp.index, lp.threshold_a, nan_policy=\"omit\")[0]\nprint(f\"\\nSpearman with temperature: amplitude (a) {r_amp_a:.3f}, upper envelope (b) {r_amp_b:.3f}, threshold (a) {r_thr_a:.3f}\")\nprint(f\"amplitude (a) from {lp.amp_a.iloc[0]:.1f} to {lp.amp_a.iloc[-1]:.1f} mV; envelope from {lp.envelope_b.iloc[0]:.1f} to \"\n      f\"{lp.envelope_b.iloc[-1]:.1f} mV; threshold (a) from {lp.threshold_a.iloc[0]:.1f} to {lp.threshold_a.iloc[-1]:.1f} mV\")\nfor d in (5.0, 20.0):\n    th = []\n    for T in T26:\n        V = None\n    print(f\"(threshold dV/dt criterion {d} mV/ms is not rerun here; the summary records it)\") if d == 20.0 else None\nfig, ax = plt.subplots(1, 2, figsize=(10, 3))\nedges = -100 + 0.1 * np.arange(1601)\nH = np.array([DIST[(\"G7P2WE\", T)][\"cells\"][1][\"hist\"] for T in T26]).T\nax[0].imshow(np.log10(H + 1), aspect=\"auto\", origin=\"lower\", extent=[T26[0], T26[-1], -100, 60], cmap=\"gray_r\")\nax[0].set_xlabel(\"temperature (C)\"); ax[0].set_ylabel(\"V (mV)\"); ax[0].set_title(\"LP, G7P2WE: log10(count + 1)\")\nax[1].plot(lp.index, lp.amp_a, \"o-\", label=\"amplitude (a)\"); ax[1].plot(lp.index, lp.threshold_a, \"o-\", label=\"threshold (a)\")\nax[1].plot(lp.index, lp.envelope_b, \"o-\", label=\"upper envelope (b)\"); ax[1].legend(fontsize=7); ax[1].set_xlabel(\"temperature (C)\")\nplt.tight_layout(); plt.show()\nprint(\"histogram axis -100 to 60 mV; samples outside it:\", int(sum(DIST[(\"G7P2WE\", T)][\"cells\"][1][\"n\"] - DIST[(\"G7P2WE\", T)][\"cells\"][1][\"hist\"].sum() for T in T26)))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig2s1-peak-voltage-diverse\n#\n# > The effect of temperature on the membrane potential differs across models; in three example\n# > models the peak voltage of spikes decreases, increases, or stays relatively constant with\n# > temperature, and cells can become more depolarized or more hyperpolarized.\n#\n# G7P2WE (left), 4X6W66 (middle, 4?6W66 of the Methods) and MAXTTP (right); upper envelope (highest\n# V) of every cell at 10 and 25 degrees C. Decrease or increase: a change of more than 5 mV in that\n# direction in any cell; constant: within 5 mV in every cell (2 and 10 mV variants).\n\n# %% tags=[\"claim:fig2s1-peak-voltage-diverse\"]\nenv = pd.DataFrame({(n, c): [DIST[(n, T)][\"cells\"][k][\"vmax\"] for T in T6] for n in (\"G7P2WE\", \"4X6W66\", \"MAXTTP\")\n                    for k, c in enumerate(P.CELLS)}, index=T6)\nmv = pd.DataFrame({(n, c): [DIST[(n, T)][\"cells\"][k][\"mean\"] for T in T6] for n in (\"G7P2WE\", \"4X6W66\", \"MAXTTP\")\n                   for k, c in enumerate(P.CELLS)}, index=T6)\nprint(\"upper envelope (mV):\"); print(env.round(2).to_string())\nprint(\"\\nmean V (mV):\"); print(mv.round(2).to_string())\nchg = env.loc[25.0] - env.loc[10.0]\nmchg = mv.loc[25.0] - mv.loc[10.0]\nprint(\"\\nchange of the upper envelope, 25 minus 10 C (mV):\", chg.round(2).to_dict())\nprint(\"change of the mean V, 25 minus 10 C (mV):\", mchg.round(2).to_dict())\nfor d in (2.0, 5.0, 10.0):\n    dec = bool((chg[\"G7P2WE\"] < -d).any()); inc = bool((chg[\"4X6W66\"] > d).any()); const = bool((chg[\"MAXTTP\"].abs() <= d).all())\n    print(f\"bound {d:.0f} mV: G7P2WE decreases {dec}; 4X6W66 increases {inc}; MAXTTP constant {const}\")\nprint(\"mean V rises in\", int((mchg > 0).sum()), \"cells and falls in\", int((mchg < 0).sum()), \"of 9\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (written after the run)\n\n# %%\nprint(f\"notebook run time {(time.time() - T_START) / 60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: entries/alonso-2020/voltage_distributions.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('voltage_distributions.py').read()
old=s[s.index('for d in (5.0, 20.0):'):s.index('fig, ax = plt.subplots(1, 2')]
s=s.replace(old,'')
open('voltage_distributions.py','w').write(s)
EOF
source $TMPDIR/dev/bin/activate && python -c "
import time, numpy as np, pyloric as P
raw=P.read_zip_bytes(); z=P.open_zip(raw); M=P.load_models(z); ci=P.load_ci(z)
for T in (10.0,25.0):
  t=time.time(); r=P.run_distribution(('x',M['G7P2WE'],ci,T,3.0,1.0,0.001,20)); print(time.time()-t)
  for c in r['cells']: print(T, {k:(round(v,2) if isinstance(v,float) else v) for k,v in c.items() if k!='hist'})
"
```

```
4.786808729171753
10.0 {'cell': 'PD', 'n': 50000, 'mean': -49.44, 'vmax': -48.8, 'vmin': -50.29, 'spikes': 0, 'peak': nan, 'amp': nan, 'thr': nan}
10.0 {'cell': 'LP', 'n': 50000, 'mean': -39.65, 'vmax': 12.61, 'vmin': -44.77, 'spikes': 8, 'peak': 12.6, 'amp': 51.98, 'thr': -27.43}
10.0 {'cell': 'PY', 'n': 50000, 'mean': -46.75, 'vmax': -46.11, 'vmin': -47.29, 'spikes': 0, 'peak': nan, 'amp': nan, 'thr': nan}
4.647683620452881
25.0 {'cell': 'PD', 'n': 50000, 'mean': -43.16, 'vmax': -3.57, 'vmin': -55.99, 'spikes': 14, 'peak': -11.68, 'amp': 19.38, 'thr': -27.32}
25.0 {'cell': 'LP', 'n': 50000, 'mean': -36.77, 'vmax': -1.81, 'vmin': -55.54, 'spikes': 17, 'peak': -11.76, 'amp': 18.37, 'thr': -27.68}
25.0 {'cell': 'PY', 'n': 50000, 'mean': -36.44, 'vmax': -2.24, 'vmin': -59.29, 'spikes': 35, 'peak': -8.45, 'amp': 23.26, 'thr': -27.12}
```

**Agent calls Bash**

```bash
cat > requirements.in <<'EOF'
ipykernel
matplotlib
numba
numpy
pandas
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: alonso-2020
type: reproduction
title: Temperature compensation in a model pyloric network (Alonso and Marder 2020)
description: Tests the findings of Alonso and Marder (2020) on Dryad m31b1h7, which holds the authors' Java model of a
  three-cell pyloric network, their Python scripts, and the parameters of 38 temperature-compensated models. Every
  claim is tested by simulating the deposited models with a port of the deposited Java, at fixed temperatures, on
  temperature ramps, with currents removed, and at high temperatures where the networks crash.
license: Apache-2.0
notebooks:
- path: reproduce_alonso_2020.ipynb
  title: Reproducing Alonso and Marder (2020) from Dryad m31b1h7
  runtime_minutes: 15
- path: ramps.ipynb
  title: Temperature ramps (Alonso and Marder 2020)
  runtime_minutes: 35
- path: voltage_distributions.ipynb
  title: Membrane potential distributions (Alonso and Marder 2020)
  runtime_minutes: 15
helpers:
- pyloric.py
related:
- id: dryad:m31b1h7/94811
  relation: uses_data
- id: doi:10.7554/elife.55470
  relation: reproduces
EOF
grep -n "ipykernel\|requirements" ../fouke-2025/requirements.in ../dias-2025/requirements.in 2>/dev/null | head -3; source $TMPDIR/dev/bin/activate && jupytext --to ipynb -q reproduce_alonso_2020.py -o reproduce_alonso_2020.ipynb && date -u && jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600 reproduce_alonso_2020.ipynb --output $TMPDIR/A.ipynb 2>&1 | tail -1; date -u
```

```
Fri Nov 27 22:56:37 UTC 2026
[NbConvertApp] Writing 227833 bytes to /tmp/claude-1001/A.ipynb
Fri Nov 27 23:09:51 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF' > A_out.txt
import nbformat
nb=nbformat.read('A.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"===== cell {i} tags={c.metadata.get('tags')}")
    for o in c.get('outputs',[]):
        if o.output_type=='stream': print(o.text[:5000])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
grep -n "ERROR" A_out.txt; awk '/cell 2[5-9] tags=..claim:figs3/,0' A_out.txt | grep -v "^[0-9A-Z]\{6\} " | head -150
```

```
===== cell 27 tags=['claim:figs3-duty-cycle-variable-across-models']
        bursts  median     lo     hi


pairs: 703; with p < 0.05: 703 (1.000)
   same conductances, different Q10: 0SHNMD vs B7SD0L: KS p = 2.18e-06
   same conductances, different Q10: 0SHNMD vs LE8W3F: KS p = 2.72e-10
   same conductances, different Q10: B7SD0L vs LE8W3F: KS p = 8.37e-03
   same conductances, different Q10: 2RO5K6 vs KMNLBC: KS p = 1.46e-45
   same conductances, different Q10: 4R2719 vs WWZ3CN: KS p = 1.76e-46
   same conductances, different Q10: 4X6W66 vs EF84RN: KS p = 2.53e-15
   same conductances, different Q10: 4X6W66 vs FGFKQS: KS p = 1.66e-16
   same conductances, different Q10: EF84RN vs FGFKQS: KS p = 2.54e-02
   same conductances, different Q10: 72TVF2 vs P1LH61: KS p = 4.66e-17
   same conductances, different Q10: HX40PF vs OPLRCP: KS p = 2.29e-22
   same conductances, different Q10: J9U8SQ vs TGCEVM: KS p = 2.88e-12
   same conductances, different Q10: Q0H92I vs R2PNKE: KS p = 2.42e-64
   same conductances, different Q10: RMZ8KZ vs VNROH5: KS p = 4.37e-05
Spearman correlation of mean LP duty cycle with temperature, per model: from -1.00 to 0.98; below -0.5: 23, above 0.5: 3, between: 12

[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/cell 4[3-9] tags/,0' $TMPDIR/A_out.txt | grep -v "^ *[0-9]*  *[0-9]" | head -80
```

```
===== cell 44 tags=None
380 runs in 208 s
runs whose integration diverged (NaN), of 988: 29 [('G7P2WE', np.float64(31.0)), ('G7P2WE', np.float64(32.0)), ('G7P2WE', np.float64(33.0)), ('G7P2WE', np.float64(34.0)), ('G7P2WE', np.float64(35.0)), ('INPO74', np.float64(33.0)), ('INPO74', np.float64(34.0)), ('INPO74', np.float64(35.0)), ('J9U8SQ', np.float64(34.0)), ('J9U8SQ', np.float64(35.0)), ('NJP4RT', np.float64(26.0)), ('NJP4RT', np.float64(27.0)), ('NJP4RT', np.float64(28.0)), ('NJP4RT', np.float64(29.0)), ('NJP4RT', np.float64(32.0)), ('NJP4RT', np.float64(33.0)), ('NJP4RT', np.float64(34.0)), ('NJP4RT', np.float64(35.0)), ('R00977', np.float64(26.0)), ('R00977', np.float64(27.0)), ('R00977', np.float64(28.0)), ('R00977', np.float64(29.0)), ('R00977', np.float64(32.0)), ('R00977', np.float64(33.0)), ('R00977', np.float64(34.0)), ('R00977', np.float64(35.0)), ('SJR46Y', np.float64(33.0)), ('SJR46Y', np.float64(34.0)), ('SJR46Y', np.float64(35.0))]
lowest temperature above 25 C at which the network is not triphasic (diverged runs skipped): {'0SHNMD': np.float64(33.0), '2RO5K6': np.float64(33.0), '4R2719': np.float64(32.0), '4X6W66': np.float64(27.0), '71G6LA': np.float64(29.0), '72TVF2': np.float64(29.0), 'B7SD0L': np.float64(32.0), 'CG4J30': None, 'ED50XO': np.float64(29.0), 'EF84RN': np.float64(30.0), 'FGFKQS': np.float64(30.0), 'G7P2WE': np.float64(28.0), 'H5AIZR': np.float64(30.0), 'HX40PF': np.float64(28.0), 'INPO74': np.float64(27.0), 'J6OK9B': np.float64(31.0), 'J9U8SQ': np.float64(29.0), 'KMNLBC': np.float64(27.0), 'KV0BR4': np.float64(34.0), 'LE8W3F': np.float64(27.0), 'MAXTTP': np.float64(32.0), 'ML4GPK': None, 'NJP4RT': np.float64(30.0), 'OPLRCP': np.float64(26.0), 'P1LH61': np.float64(29.0), 'PCR6RP': np.float64(30.0), 'PLKTEM': None, 'Q0H92I': np.float64(31.0), 'R00977': np.float64(30.0), 'R2PNKE': np.float64(27.0), 'R3VIEW': np.float64(30.0), 'RMZ8KZ': np.float64(29.0), 'SJR46Y': np.float64(26.0), 'TGCEVM': np.float64(32.0), 'VNROH5': np.float64(27.0),
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 590,625p tools/entry.py
```

```
return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
    the run left it, each within the time limit asked for now, and not older than REUSE_DAYS. Else None."""
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python - <<'EOF'
s=open('reproduce_alonso_2020.py').read()
s=s.replace('''print("\\ncell classes:", {k: v["classes"] for k, v in ST.items() if k[0] in ("4X6W66", "SJR46Y")})
''','')
s=s.replace('''    leak10 = pd10["in end"]["Leak"] / pd10["in start"]["Leak"]
    leak25 = pd25["in end"]["Leak"] / pd25["in start"]["Leak"]''','''    with np.errstate(invalid="ignore", divide="ignore"):
        leak10 = pd10["in end"]["Leak"] / pd10["in start"]["Leak"]
        leak25 = pd25["in end"]["Leak"] / pd25["in start"]["Leak"]''')
open('reproduce_alonso_2020.py','w').write(s)
EOF
grep -c "cell classes:" reproduce_alonso_2020.py; source $TMPDIR/dev/bin/activate && for n in ramps voltage_distributions; do jupytext --to ipynb -q $n.py -o $n.ipynb; done; date -u; for n in voltage_distributions ramps; do jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600 $n.ipynb --output $TMPDIR/$n.out.ipynb 2>&1 | tail -1; date -u; done
```

```
0
Fri Nov 27 23:10:29 UTC 2026
[NbConvertApp] Writing 78803 bytes to /tmp/claude-1001/voltage_distributions.out.ipynb
Fri Nov 27 23:23:34 UTC 2026
[NbConvertApp] Writing 89418 bytes to /tmp/claude-1001/ramps.out.ipynb
Fri Nov 27 23:55:49 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import nbformat
for f in ['voltage_distributions.out.ipynb','ramps.out.ipynb']:
    nb=nbformat.read(f,4)
    print('#########',f)
    for i,c in enumerate(nb.cells):
        if c.cell_type!='code': continue
        print(f"===== cell {i} tags={c.metadata.get('tags')}")
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text[:7000])
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
```

```
######### voltage_distributions.out.ipynb
===== cell 1 tags=None
{'md5': '37766522dabaaa620d4c44264e76e686', 'sha256': '327279e2c4553c0b946bf230260caf0f7321e36bc5201ad7d65bbe6638d2df08', 'bytes': 99026}

===== cell 3 tags=['sanity']
38 models; used here: G7P2WE, 4X6W66 (4?6W66 of the Methods), MAXTTP

38 runs in 783 s; peak memory 0.25 GB
all runs finite: True
samples per distribution: {500000}
V range over all runs: -63.0 to 23.9 mV
             mean        vmin        vmax       spikes     
              min   max   min   max   min   max    min  max
model  cell                                                
4X6W66 LP   -43.3 -42.8 -51.8 -50.3  -0.4   7.1     97  237
       PD   -45.4 -43.3 -54.9 -53.5  14.2  20.5     80  348
       PY   -45.9 -44.8 -55.8 -54.8  16.4  22.7     70  261
G7P2WE LP   -44.7 -42.9 -53.7 -51.7  -1.8  16.7    114  433
       PD   -45.2 -43.1 -54.1 -53.0  -4.1  15.1     88  381
       PY   -45.3 -41.6 -57.8 -55.6  -1.1  12.6     79  612
[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "model 71G6LA" -A26 $TMPDIR/A_out.txt | tail -10; grep -n "fig1s1\|WWZ3CN: frequency\|FGFKQS: frequency\|71G6LA: frequency\|FGFKQS shares" $TMPDIR/A_out.txt; awk '/claim:fig10b/,0' $TMPDIR/A_out.txt; grep -n "cell classes (PD, LP, PY)" -A14 $TMPDIR/A_out.txt
```

```
262-H5AIZR    0
263-HX40PF    0
264-INPO74    0
265-J6OK9B    0
266-J9U8SQ    0
267-KMNLBC    0
268-KV0BR4    0
269-LE8W3F    0
270-MAXTTP    2
271-ML4GPK    0
188:===== cell 21 tags=['claim:fig1s1-three-models']
===== cell 65 tags=['claim:fig10b-complete-removal-differs']
608 runs in 167 s
         differ_all_classes  differ_NET  same_and_quiescent
current                                                    
Na                    0.237       0.000                  29
CaT                   0.974       0.474                   1
CaS                   0.605       0.079                  13
A                     0.737       0.579                   0
KCa                   0.316       0.026                   0
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 225,250p $TMPDIR/A_out.txt
```

```
16  1.523  0.242  1.525  0.255  1.524  0.234   0.242  0.417   0.673  0.723   0.957  triphasic
17  1.586  0.260  1.597  0.233  1.587  0.231   0.260  0.427   0.665  0.724   0.955  triphasic
18  1.744  0.245  1.743  0.230  1.743  0.227   0.245  0.427   0.657  0.732   0.959  triphasic
19  1.819  0.275  1.821  0.205  1.820  0.213   0.275  0.443   0.648  0.737   0.951  triphasic
20  2.026  0.249  2.026  0.220  2.026  0.195   0.249  0.436   0.656  0.742   0.936  triphasic
21  2.187  0.244  2.188  0.199  2.186  0.216   0.244  0.442   0.642  0.743   0.959  triphasic
22  2.341  0.265  2.349  0.185  2.341  0.225   0.265  0.453   0.641  0.746   0.971  triphasic
23  2.575  0.225  2.581  0.202  2.575  0.209   0.225  0.438   0.642  0.743   0.952  triphasic
24  2.705  0.261  2.711  0.160  2.705  0.214   0.261  0.461   0.623  0.737   0.952  triphasic
25  3.029  0.224  3.029  0.167  3.029  0.229   0.224  0.442   0.609  0.723   0.952  triphasic
Q10 of burst frequency (mean of the three cells): (a) fit 1.991, (b) (f25/f10)^(10/15) 2.027, (c) f20/f10 1.930
   PD: (a) 1.992, (b) 2.029, (c) 1.934
   LP: (a) 1.989, (b) 2.021, (c) 1.922
   PY: (a) 1.993, (b) 2.031, (c) 1.936
largest spread between the cells' frequencies at one temperature: 1.0%
range over temperatures (cycles): {'dc PD': 0.067, 'dc LP': 0.121, 'dc PY': 0.058, 'PD off': 0.067, 'LP on': 0.078, 'LP off': 0.076, 'PY on': 0.041, 'PY off': 0.043}
largest relative change from 10 C: {'dc PD': 0.239, 'dc LP': 0.431, 'dc PY': 0.17, 'PD off': 0.239, 'LP on': 0.205, 'LP off': 0.089, 'PY on': 0.059, 'PY off': 0.033}
(i) all within 0.1 of a cycle: False; (ii) all within 20% of 10 C: False
frequency higher at 25 than at 10 C: {'PD': True, 'LP': True, 'PY': True} ; network triphasic at 16 of 16

[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import nbformat
nb=nbformat.read('A.ipynb',4)
for c in nb.cells:
    if 'claim:fig1s1-three-models' in c.metadata.get('tags',[]):
        t=''.join(o.get('text','') for o in c.outputs)
        i=t.find('model 71G6LA'); print(t[i:])
"; date -u
```

```
model 71G6LA
     f PD  dc PD   f LP  dc LP   f PY  dc PY  PD off  LP on  LP off  PY on  PY off        NET
10  1.301  0.192  1.300  0.197  1.312  0.252   0.192  0.388   0.584  0.625   0.885  triphasic
11  1.373  0.198  1.372  0.197  1.372  0.238   0.198  0.394   0.592  0.623   0.861  triphasic
12  1.449  0.183  1.448  0.210  1.455  0.222   0.183  0.395   0.605  0.615   0.840  triphasic
13  1.524  0.182  1.524  0.206  1.534  0.216   0.182  0.393   0.600  0.608   0.829  triphasic
14  1.618  0.170  1.618  0.184  1.619  0.210   0.170  0.392   0.576  0.605   0.815  triphasic
15  1.727  0.169  1.724  0.172  1.724  0.202   0.169  0.389   0.562  0.601   0.803  triphasic
16  1.826  0.171  1.832  0.171  1.826  0.193   0.171  0.391   0.565  0.602   0.794  triphasic
17  1.924  0.174  1.934  0.178  1.924  0.238   0.174  0.397   0.578  0.606   0.844  triphasic
18  2.040  0.171  2.041  0.188  2.046  0.260   0.171  0.396   0.584  0.607   0.867  triphasic
19  2.164  0.165  2.164  0.203  2.164  0.270   0.165  0.399   0.603  0.611   0.880  triphasic
20  2.274  0.157  2.274  0.222  2.274  0.251   0.157  0.400   0.623  0.613   0.864  triphasic
21  2.376  0.150  2.376  0.241  2.386  0.228   0.150  0.400   0.641  0.614   0.845  triphasic
22  2.500  0.159  2.500  0.218  2.507  0.226   0.159  0.404   0.622  0.620   0.848  triphasic
23  2.622  0.162  2.622  0.217  2.622  0.243   0.162  0.407   0.624  0.625   0.868  triphasic
24  2.751  0.158  2.751  0.228  2.754  0.259   0.158  0.407   0.636  0.630   0.891  triphasic
25  2.885  0.156  2.885  0.234  2.885  0.259   0.156  0.410   0.645  0.638   0.897  triphasic
Q10 of burst frequency (mean of the three cells): (a) fit 1.712, (b) (f25/f10)^(10/15) 1.698, (c) f20/f10 1.743
   PD: (a) 1.713, (b) 1.701, (c) 1.748
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && grep -c "Result: \.\.\." reproduce_alonso_2020.py ramps.py voltage_distributions.py; grep -n "^# ## \|Result: \.\.\." reproduce_alonso_2020.py | grep -B1 "Result" | grep "##"
```

```
reproduce_alonso_2020.py:15
ramps.py:4
voltage_distributions.py:2
214:# ## deposit-models
330:# ## fig1c-frequency-q10-phase-constant
355:# ## fig1s1-three-models
375:# ## all-models-compensated
403:# ## figs3-duty-cycle-variable-across-models
442:# ## fig3-current-amplitudes
503:# ## fig4-currentscapes-reorganize
556:# ## currentscapes-dominant-currents
590:# ## fig5-a-to-kca-tradeoff
643:# ## fig6-crash-different-mechanisms
673:# ## fig6s1-crash-mechanisms
735:# ## fig9a-remove-a-current
780:# ## fig9b-remove-kca-current
804:# ## fig10a-graded-removal
839:# ## fig10b-complete-removal-differs
```

**Agent calls Bash**

```bash
cat > $TMPDIR/concl.py <<'PYEOF'
import re, sys
def fill(path, texts, summary):
    s = open(path).read()
    parts = s.split("# **Result: ...**")
    assert len(parts) == len(texts) + 1, (path, len(parts))
    out = parts[0]
    for t, p in zip(texts, parts[1:]):
        lines = t.strip().split("\n")
        out += "# " + "\n# ".join(lines) + p
    out = out.replace("# ## Summary\n#\n# (written after the run)", "# ## Summary\n#\n# " + "\n# ".join(summary.strip().split("\n")))
    open(path, "w").write(out)

FAIL = "A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method."

A = [
"""**Result: not reproduced.** The deposit holds the model code and 38 parameter sets, not 36. Of
the 21 model names in the Methods, 17 are found (13 as printed, 2 with the letter O read as the
digit 0, 1 at the unreadable character, 1 with two characters swapped) and 4 are absent. Every
Q10 is within [1, 2] for conductances and [1, 4] for time scales. All 38 networks are triphasic
at 10 C, but only 3 of 38 models are within tolerance on every value (frequency 1 +- 0.1 Hz alone:
10 of 38; mean frequency over models and cells 1.246 Hz), and 0 of 38 with the 0.20 LP and PY
target of the variant.""",
"""**Result: partially reproduced.** In 4X6W66 the Q10 of burst frequency is 1.927 (fit), 1.982
(end points) and 1.937 (f20 / f10), within 2 +- 0.2 under every reading, and the three cells'
frequencies differ by at most 0.8%. Duty cycles and phases are not constant under either reading:
the LP duty cycle spans 0.11 of a cycle (reading i, bound 0.1) and changes by up to 34% from its
10 C value (reading ii, bound 20%); every other duty cycle and phase stays within 0.1 of a cycle.""",
"""**Result: not reproduced.** In WWZ3CN, FGFKQS and 71G6LA the frequency rises from 10 to 25 C in
every cell (Q10 by the fit 2.05, 1.99 and 1.71), but none meets either reading of constancy: the
largest ranges are 0.171 (WWZ3CN, LP offset), 0.121 (FGFKQS, LP duty cycle) and 0.102 (71G6LA, PY
offset) of a cycle, and the largest changes from 10 C are 34%, 43% and 24%. FGFKQS has the same
maximal conductances as 4X6W66, with other Q10 values.""",
"""**Result: partially reproduced.** 36 of the 38 deposited models are triphasic at all 16
temperatures from 10 to 25 C; ED50XO (not triphasic at 19 and 21 C, all cells irregular bursting)
and MAXTTP (10 and 14 C, LP irregular bursting) are not. With the order required in every cycle, 35
of 38 are. The deposit holds more than one Q10 set for 9 of its 27 distinct sets of maximal
conductances, and every one of those 20 models is compensated, so multiple Q10 sets are found for
some, not all, sets of conductances in the deposit.""",
"""**Result: reproduced** (on the criterion's variant reading, 16 fixed temperatures; the ramp
reading was not run). All 703 pairs of the 38 models have LP duty-cycle distributions that differ
at p < 0.05 (two-sample Kolmogorov-Smirnov), including every pair that shares its maximal
conductances (largest p 0.025). Model medians and ranges are in the table; the mean LP duty cycle
falls with temperature in 23 models (Spearman below -0.5), rises in 3 and neither in 12.""",
"""**Result: partially reproduced.** In 4X6W66 (panel A as listed) the PD Na peak grows 2.42-fold
(more than 2), the CaT peak falls to 0.486 of its 10 C value (0.5 +- 0.05), and the KCa peak grows
8.9-fold (reading a) or 9.1-fold (reading b), outside 6 +- 0.6. In SJR46Y the Na peak falls to
0.81 and the KCa peak to 0.80. Four of the five parts hold under both readings; with the panels
swapped, none does.""",
"""**Result: not reproduced.** In WWZ3CN the PD leak current has no inward share inside the bursts
at either temperature (0.0000 at start and end; with all leak reversal potentials at -50 mV it is
outward while V is above -50 mV), so the leak part cannot hold. The PD A share at the start over
the end of the burst is 1.278 at 10 C, outside 0.8 to 1.25, and 1.348 (thirds) or 1.385 (20%) at
25 C. The KCa share at the end of bursts rises from 10 to 25 C in LP (+0.29, +0.34) and PY (+0.22,
+0.25) but falls in PD (-0.21, -0.20), so the KCa part fails too.""",
"""**Result: reproduced.** Over 38 models, 3 cells and 4 temperatures (26,868 spikes), Na holds the
largest inward share in the 1 ms before every spike peak (fraction 1.000) and Kd the largest
outward share in the 1 ms after it (1.000). At the 5% of time with the lowest voltage, H holds the
largest inward share in 456 of 456 cases and the synaptic current the largest outward share in
453 (KCa in 3), so both hold in 0.993 of cases, above the 0.9 bound.""",
"""**Result: reproduced.** In FGFKQS (the model the Methods name), over the 20 ms after the PD
burst the A share falls from 0.312 to 0.082 and the KCa share rises from 0.077 to 0.577 from 10 to
25 C (Spearman -1.000 and 1.000), with A above KCa at 10 C and KCa above A at 25 C. In J9U8SQ (the
legend's reading) both trends hold (-0.997, 0.953) but KCa exceeds A already at 10 C.""",
"""**Result: not reproduced.** FGFKQS and 71G6LA are triphasic at 10 and 25 C. At 30 C, 71G6LA's PD
is quiescent (no spike in 30 s), but FGFKQS's PD fires 1005 spikes in 30 s (class other), so the
complete loss of PD activity holds in one model of two. The dominant PD currents at 30 C differ
(H and KCa in FGFKQS, H and Syn in 71G6LA).""",
"""**Result: not reproduced.** Seven of the eight models are in the deposit (Q8FBN1 is absent).
All seven stop being triphasic below 35 C (at 26 to 32 C), but their dominant (inward, outward)
currents form 5 distinct patterns: B7SD0L, J9U8SQ and EF84RN share H and Syn in all three cells.
The criterion asks that no two share a pattern (reproduced) or at least six distinct among eight
(partially); with the eighth model at most six could be distinct.""",
"""**Result: partially reproduced.** In WWZ3CN, removing IA at 10 C leaves the network not
triphasic with irregular bursting cells under all three timings. At 25 C the network is never
the near-normal triphasic rhythm with only PY irregular: under the Results' timing (20 s, then 20
s without IA) all three cells burst irregularly and the network is not triphasic, so PY is
irregular but other cells are not regular, the criterion's partial case.""",
"""**Result: reproduced.** In FGFKQS (the Methods' model and the deposit's script), removing KCa at
10 C keeps the network triphasic and slows it (PD 1.061 to 0.904 Hz with the code's timing, 1.067
to 0.918 Hz with the Results' timing), and at 25 C all three cells are quiescent after removal.
The legend's timing (removal at 4 s, from the initial conditions) and J9U8SQ do not show it.""",
"""**Result: partially reproduced.** In 4X6W66, three of the five stated grid cells match: Na at
75% makes LP burst irregularly and the network not triphasic at 10 C and leaves it triphasic at 25
C; CaT and CaS at 0% give non-triphasic activity with different cell classes at the two
temperatures. KCa removal at 10 C leaves the network triphasic at 100 to 50% but not at 25% and
0% (PD and PY quiescent, LP tonic), and KCa at 0% at 25 C leaves LP tonic spiking, so not all
cells are quiescent.""",
"""**Result: not reproduced.** Across the 38 models, CaT has the largest fraction of models that
respond differently to complete removal at 10 and 25 C when all four classes are compared (0.974),
but complete removal of H gives the same, quiescent, state at both temperatures in 31 of 38 models,
below the criterion's 33. Comparing the network class alone, CaT is not the largest (0.474,
against A 0.579). Of the other currents, 2 of 6 (8 currents) or 2 of 5 (without leak) fall within
0.3 to 0.7 under the four-class reading.""",
]
A_sum = """| Claim | Outcome |
|---|---|
| deposit-models | not reproduced |
| fig1c-frequency-q10-phase-constant | partially reproduced |
| fig1s1-three-models | not reproduced |
| all-models-compensated | partially reproduced |
| intermediate-temperature-failures | blocked (data_missing) |
| figs2-ramp-largest-isi | reproduced (ramps notebook) |
| figs3-duty-cycle-variable-across-models | reproduced, variant reading |
| fig2-lp-spike-amplitude-threshold | partially reproduced (voltage_distributions notebook) |
| fig2s1-peak-voltage-diverse | reproduced (voltage_distributions notebook) |
| fig3-current-amplitudes | partially reproduced |
| fig4-currentscapes-reorganize | not reproduced |
| currentscapes-dominant-currents | reproduced |
| fig5-a-to-kca-tradeoff | reproduced |
| fig6-crash-different-mechanisms | not reproduced |
| fig6s1-crash-mechanisms | not reproduced (7 of 8 models) |
| fig7-high-temperature-slow-timescales | blocked (data_missing) |
| fig8a-hysteresis-quiescence | reproduced (ramps notebook) |
| fig8-up-down-ramps | blocked (too_large; main reading 22 of 38) |
| fig8b-pathological-attractor | not reproduced (ramps notebook) |
| fig9a-remove-a-current | partially reproduced |
| fig9b-remove-kca-current | reproduced |
| fig10a-graded-removal | partially reproduced |
| fig10b-complete-removal-differs | not reproduced |

""" + FAIL + """

How the analysis differs from the paper's: the models are simulated with a numba port of the
deposited Java, which matches it to 3e-9 mV over 3 s; spikes are upward crossings of -20 mV and
the network order is judged on median phases (assumptions, as the paper gives neither); the 38
deposited models are used where the paper says 36; the figure supplements' legends were not read.

What was found about the dataset: 38 models where the paper says 36; 4 models named in the Methods
absent (Q8FBN1, G81PUL, G7EOZ8, SAXT8Y) and 4 filed under other spellings; 27 distinct sets of
maximal conductances; the models' burst frequency at 10 C is 1.25 Hz on average, not the 1 Hz
target; and the deposited integrator diverges (NaN) for 6 models at some temperatures from 26 to
35 C."""
fill("reproduce_alonso_2020.py", A, A_sum)

B = [
"""**Result: reproduced.** On the 60 min ramp of PLKTEM the median per-cycle largest ISI falls in
every 4 min window, with no increase, in all three cells (PD 0.604 to 0.299 s, LP 0.613 to 0.301 s,
PY 0.522 to 0.251 s; Spearman -1.000 each). In 1 min windows the Spearman correlations are -0.998,
-0.998 and -0.994, with 7, 9 and 22 increases between windows.""",
"""**Result: reproduced.** On the updown ramp, 0SHNMD's PD fires its last spike on the up ramp at
34.16 C, stays quiescent across the top for 260 s and resumes at 32.22 C on the down ramp, 1.94 C
lower (2 +- 0.2). The last spike comes at 1740 s, not before 600 s as the legend says (not judged).
The variant H5AIZR differs by 0.05 C.""",
"""**Result: blocked (too_large).** On the main ramp reading (10 to 35 C and back over 60 min), 22
of 38 models are similar on the two legs (within 10% and triphasic in every 1 degree window; 9 at
5%, 28 at 20%), outside 34 +- 3; 6 models diverge numerically on this ramp and 10 others exceed the
10% bound or lose triphasic order. No model has identical spike counts on the two legs. The
second reading (10 to 25 C over 60 min and back) was not run.""",
"""**Result: not reproduced.** H5AIZR's PD spikes in every 1 min window, bursts regularly early on
the up ramp and leaves regular bursting at 28.8 C, but it is regular again at 32 to 35 C and on the
down ramp it returns to regular bursting for good at 17.08 C (20 +- 2), after isolated irregular
windows at 27.1, 22.1 and 17.9 C; its longest PD ISI between 25 and 35 min is 11.32 s (1 +- 0.1).
The variant 0SHNMD has PD windows with no spike.""",
]
B_sum = """| Claim | Outcome |
|---|---|
| figs2-ramp-largest-isi | reproduced |
| fig8a-hysteresis-quiescence | reproduced |
| fig8-up-down-ramps | blocked (too_large; main reading 22 of 38) |
| fig8b-pathological-attractor | not reproduced |

""" + FAIL + """

How the analysis differs from the paper's: the deposit has no ramp code, so the temperature is
changed linearly and the factors updated every 1 ms; each ramp starts from the deposited initial
conditions. The second ramp reading of fig8-up-down-ramps and the 60 min ramp of every model for
figs3-duty-cycle-variable-across-models were not run (about 68 and 35 min). On the updown ramp the
deposited integrator diverges (NaN) for G7P2WE, INPO74, J9U8SQ, NJP4RT, R00977 and SJR46Y."""
fill("ramps.py", B, B_sum)

C = [
"""**Result: partially reproduced.** In G7P2WE's LP cell the spike amplitude falls from 10 to 25 C
under both readings (peak minus trough 56.9 to 26.2 mV; upper envelope 16.7 to -1.8 mV; Spearman
-1.000 each). The threshold under reading (a) does not depolarize steadily (-27.8 to -27.5 mV,
Spearman -0.197); reading (b) was not computed. 26 of the Methods' 101 temperatures were run.""",
"""**Result: reproduced.** From 10 to 25 C the upper envelope falls in every cell of G7P2WE (by 19.1,
18.5 and 13.8 mV), rises in every cell of 4X6W66 (3.9, 7.3 and 6.3 mV; more than 5 mV in LP and
PY), and stays within 5 mV in every cell of MAXTTP (-1.5, -2.5 and 1.0 mV). The 2 mV variant loses
MAXTTP and the 10 mV variant loses 4X6W66. The mean V rises in 8 of the 9 cells and falls in one
(4X6W66 LP, -0.26 mV).""",
]
C_sum = """| Claim | Outcome |
|---|---|
| fig2-lp-spike-amplitude-threshold | partially reproduced |
| fig2s1-peak-voltage-diverse | reproduced |

""" + FAIL + """

How the analysis differs from the paper's: 26 temperatures (G7P2WE) and 6 (4X6W66, MAXTTP) in
place of 101; spike amplitude and threshold are read as stated in the claims file, threshold
reading (b) not computed. Nothing was found about the dataset beyond the main notebook."""
fill("voltage_distributions.py", C, C_sum)
PYEOF
python $TMPDIR/concl.py && grep -c "Result: \.\.\." reproduce_alonso_2020.py ramps.py voltage_distributions.py
```

```
Exit code 1
reproduce_alonso_2020.py:0
ramps.py:0
voltage_distributions.py:0
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ramps.py').read()
old="5%, 28 at 20%), outside 34 +- 3; 6 models diverge numerically on this ramp and 10 others exceed the\n# 10% bound or lose triphasic order."
assert old in s
s=s.replace(old,"5%, 28 at 20%), outside 34 +- 3. Six models diverge numerically on this ramp, MAXTTP's cells\n# fire no spike on the down leg below 25 C, and 9 others exceed the 10% bound or lose triphasic order.")
s=s.replace("# | fig8-up-down-ramps | tested (main ramp reading only) |","# | fig8-up-down-ramps | blocked (too_large); the main ramp reading is shown |")
open('ramps.py','w').write(s)
a=open('reproduce_alonso_2020.py').read()
a=a.replace("# | fig8-up-down-ramps | ramps | tested |","# | fig8-up-down-ramps | ramps | blocked (too_large); main reading shown |")
open('reproduce_alonso_2020.py','w').write(a)
EOF
grep -n "fig8-up-down-ramps |" reproduce_alonso_2020.py ramps.py
```

```
reproduce_alonso_2020.py:47:# | fig8-up-down-ramps | ramps | blocked (too_large); main reading shown |
reproduce_alonso_2020.py:965:# | fig8-up-down-ramps | blocked (too_large; main reading 22 of 38) |
ramps.py:32:# | fig8-up-down-ramps | blocked (too_large); the main ramp reading is shown |
ramps.py:268:# | fig8-up-down-ramps | blocked (too_large; main reading 22 of 38) |
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && for n in reproduce_alonso_2020 ramps voltage_distributions; do jupytext --to ipynb -q $n.py -o $n.ipynb && mv $n.py $TMPDIR/$n.src.py; done; rm -rf __pycache__; ls; cat > README.md <<'EOF'
# Alonso and Marder (2020) from Dryad m31b1h7

Tests the findings of [Alonso and Marder (2020)](https://doi.org/10.7554/eLife.55470) on
[Dryad m31b1h7](https://doi.org/10.5061/dryad.m31b1h7) (version id 94811), which holds the
authors' Java model of a three-cell pyloric network, their Python scripts and the parameters of
38 temperature-compensated models. The paper has no recordings: every claim is tested by
simulating the deposited models with a port of the deposited Java (`pyloric.py`), which matches the
Java to 3e-9 mV.

| Claim | Outcome |
|---|---|
| The deposit holds the paper's models, which give a 1 Hz rhythm at 10 C | Not reproduced |
| Figure 1: frequency Q10 near 2, duty cycles and phases constant | Partially reproduced |
| Figure 1, supplement 1: three more models | Not reproduced |
| All 36 models compensated over 10 to 25 C | Partially reproduced |
| 2 in 40 solutions failed between control temperatures | Blocked: data missing |
| Figure 1, supplement 2: largest ISI falls along a ramp | Reproduced |
| Figure 1, supplement 3: LP duty-cycle distributions differ across models | Reproduced |
| Figure 2: LP spike amplitude falls and threshold depolarizes | Partially reproduced |
| Figure 2, supplement 1: peak voltage falls, rises or stays | Reproduced |
| Figure 3: current amplitudes at two temperatures | Partially reproduced |
| Figure 4: currentscapes reorganize | Not reproduced |
| Na and Kd drive spikes; H and synaptic currents dominate at the trough | Reproduced |
| Figure 5: A to KCa trade-off after the PD burst | Reproduced |
| Figure 6: two models crash with loss of PD activity | Not reproduced |
| Figure 6, supplement 1: crashes by different mechanisms | Not reproduced |
| Figure 7: slow time scales at high temperature | Blocked: data missing |
| Figure 8A: hysteresis of PD quiescence | Reproduced |
| 34 of 36 models similar on up and down ramps | Blocked: too large |
| Figure 8B: pathological attractor | Not reproduced |
| Figure 9A: removing IA at 10 and 25 C | Partially reproduced |
| Figure 9B: removing IKCa at 10 and 25 C | Reproduced |
| Figure 10A: graded removal in one model | Partially reproduced |
| Figure 10B: complete removal across models | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The deposit holds 38 models where the paper says 36; four models the Methods name are absent and
four are filed under other spellings. The attempt record, with the reasons and the differences from
the paper's method, is [`attempts/alonso-2020-01.yaml`](../../attempts/alonso-2020-01.yaml).

- `reproduce_alonso_2020.ipynb`: the data check and most claims, at fixed temperatures (about 15
  min).
- `ramps.ipynb`: the claims on temperature ramps (about 35 min).
- `voltage_distributions.ipynb`: the membrane potential distributions of Figure 2 (about 15 min).
- `pyloric.py`: loading the deposit, the port of the model, the classification scheme of the
  Methods and the current shares. Other notebooks on this dataset can import it.
EOF
cd  && python tools/entry.py lock entries/alonso-2020 2>&1 | tail -5; date -u
```

```
entry.yaml
pyloric.py
ramps.ipynb
reproduce_alonso_2020.ipynb
requirements.in
voltage_distributions.ipynb
wrote alonso-2020/requirements.lock.txt (Python 3.13, with hashes)
Fri Nov 27 23:57:50 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/alonso-2020 2>&1 | tail -20; grep -i "numba\|numpy==" entries/alonso-2020/requirements.lock.txt | head
```

```
0 error(s)
    # via numba
numba==0.68.1 \
numpy==2.5.5 \
    #   numba
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/alonso-2020 2>&1 | tail -15; date -u
```

```
Fri Nov 27 23:57:57 UTC 2026
Installed kernelspec registry-alonso-2020 in executed/alonso-2020/.venv/share/jupyter/kernels/registry-alonso-2020
0 error(s)
pass  reproduce_alonso_2020.ipynb  (800 s)
pass  ramps.ipynb  (1922 s)
pass  voltage_distributions.ipynb  (778 s)
Sat Nov 28 00:56:27 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/alonso-2020 && ls && python - <<'EOF'
import nbformat,re
keys=['within tolerance on all values','Q10 of burst frequency (mean','models triphasic at all 16','pairs: 703','4 of 5 hold','spikes: 26868','Spearman with temperature: A','PD spikes in the 30 s','distinct patterns','25 C part','10 C part True, 25 C part True','matching:','reading differ_all_classes, 8','cells with Spearman','difference 1.94','similar (within 10%','returns to it for good','amplitude (a) from','mean V rises','largest difference in V','runs whose integration diverged','H inward and Syn','KS p =','largest relative change','PLKTEM up ramp']
for f in ['reproduce_alonso_2020.ipynb','ramps.ipynb','voltage_distributions.ipynb']:
    nb=nbformat.read(f,4)
    for c in nb.cells:
        if c.cell_type!='code': continue
        t=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
        for l in t.splitlines():
            if any(k in l for k in keys): print(f[:6], l[:230])
        for o in c.outputs:
            if o.output_type=='error': print('ERR',f)
EOF
```

```
ramps.ipynb
reproduce_alonso_2020.ipynb
result.json
voltage_distributions.ipynb
reprod 4X6W66, 3 s at 18 C: Java (60000, 3), port (60000, 3); largest difference in V 3.09e-09 mV
reprod within tolerance on all values (LP, PY target 0.25): 3 of 38
reprod within tolerance on all values (LP, PY target 0.20, variant): 0 of 38
reprod Q10 of burst frequency (mean of the three cells): (a) fit 1.927, (b) (f25/f10)^(10/15) 1.982, (c) f20/f10 1.937
reprod largest relative change from 10 C: {'dc PD': 0.14, 'dc LP': 0.344, 'dc PY': 0.209, 'PD off': 0.14, 'LP on': 0.097, 'LP off': 0.108, 'PY on': 0.033, 'PY off': 0.028}
reprod Q10 of burst frequency (mean of the three cells): (a) fit 2.048, (b) (f25/f10)^(10/15) 2.103, (c) f20/f10 2.190
reprod largest relative change from 10 C: {'dc PD': 0.185, 'dc LP': 0.337, 'dc PY': 0.177, 'PD off': 0.185, 'LP on': 0.172, 'LP off': 0.227, 'PY on': 0.181, 'PY off': 0.142}
reprod Q10 of burst frequency (mean of the three cells): (a) fit 1.991, (b) (f25/f10)^(10/15) 2.027, (c) f20/f10 1.930
reprod largest relative change from 10 C: {'dc PD': 0.239, 'dc LP': 0.431, 'dc PY': 0.17, 'PD off': 0.239, 'LP on': 0.205, 'LP off': 0.089, 'PY on': 0.059, 'PY off': 0.033}
reprod Q10 of burst frequency (mean of the three cells): (a) fit 1.712, (b) (f25/f10)^(10/15) 1.698, (c) f20/f10 1.743
reprod largest relative change from 10 C: {'dc PD': 0.218, 'dc LP': 0.227, 'dc PY': 0.236, 'PD off': 0.218, 'LP on': 0.059, 'LP off': 0.103, 'PY on': 0.039, 'PY off': 0.102}
reprod models triphasic at all 16 temperatures: 36 of 38
reprod variant, order required in every cycle: models triphasic at all 16 temperatures 35 of 38
reprod pairs: 703; with p < 0.05: 703 (1.000)
reprod    same conductances, different Q10: 0SHNMD vs B7SD0L: KS p = 2.18e-06
reprod    same conductances, different Q10: 0SHNMD vs LE8W3F: KS p = 2.72e-10
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -n 1,80p attempts/fouke-2025-01.yaml; grep -n "^[a-z_]*:" attempts/fouke-2025-01.yaml; grep -n "findings:" -A30 attempts/fouke-2025-01.yaml | head -45
```

```
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; python - <<'EOF'
import json,glob
f=[x for x in glob.glob('schemas/*') if 'attempt' in x][0]; print(f)
s=json.load(open(f))
def walk(d,path=''):
    if isinstance(d,dict):
        if 'properties' in d: print(path, list(d['properties']), d.get('required'))
        for k,v in d.items(): walk(v,path+'/'+k)
    elif isinstance(d,list):
        for v in d: walk(v,path)
walk(s)
EOF
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/attempt.schema.json
 ['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review'] ['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
/properties/datasets/items ['archive', 'id', 'version', 'modified', 'doi', 'relation'] ['archive', 'id', 'version', 'relation']
/properties/datasets/items/if ['archive'] None
/properties/datasets/items/then ['id'] None
/properties/missing_datasets/items ['archive', 'id', 'name', 'why'] ['why']
/properties/deprecated ['date', 'reason', 'superseded_by'] ['date', 'reason']
/properties/provenance ['kind', 'accountable', 'agent', 'runner', 'author_notes'] ['kind', 'accountable']
/properties/provenance/properties/accountable ['name', 'orcid', 'ror'] ['name']
/properties/provenance/properties/agent ['harness', 'model', 'protocol'] ['harness', 'model', 'protocol']
/properties/provenance/properties/runner ['platform', 'url'] ['platform']
/properties/outcomes/items ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed'] ['claim', 'outcome']
/properties/outcomes/items/properties/proposed ['outcome', 'blocked_by', 'reason'] ['outcome', 'reason']
/properties/outcomes/items/allOf/if ['outcome'] None
/properties/outcomes/items/allOf/if ['assumed'] ['assumed']
/properties/outcomes/items/allOf/then ['deviations', 'outcome'] ['deviations']
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cat questions/README.md | head -40; ls questions | grep alonso
```

```
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
```

**Agent**

Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/alonso-2020-01.yaml",
 "content": "schema_version: 3\nid: alonso-2020-01\ndatasets:\n- archive: dryad\n  id: m31b1h7\n  version: \"94811\"\n  doi: 10.5061/dryad.m31b1h7\n  relation: primary\npaper: doi:10.7554/elife.55470\ndate: 2026-11-27\nentry: alonso-2020\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-19\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/encorescience/encore-registry/actions/runs/46075031684\noutcomes:\n- claim: deposit-models\n  outcome: not_reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:deposit-models\n  measured:\n  - 1.246\n  - 0.192\n  - 0.239\n  notes: The deposit holds the Java model, the Python scripts, one initial-condition file and 38\n    parameter sets (the paper and the Dryad description say 36). Of the 21 model names in the\n    Methods, 13 are found as printed, 2 with the letter O read as the digit 0 (OSHNMD is 0SHNMD,\n    B7SDOL is B7SD0L), 1 at the character the text cannot render (4X6W66), 1 with two characters\n    swapped (KNMLBC is KMNLBC), and 4 are absent (Q8FBN1, G81PUL, G7EOZ8, SAXT8Y). Every Q10 is\n    within [1, 2] for conductances (largest 1.4985 intrinsic, 1.499 synaptic) and [1, 4] for\n    time scales (largest 3.973 and 3.997). At 10 C (20 s, first 10 s dropped) all 38 networks are\n    triphasic, but only 3 of 38 models have every value within tolerance; 10 of 38 are within\n    1 +- 0.1 Hz in every cell, 17 within 0.2 +- 0.02 for PD duty cycle, 14 within 0.25 +- 0.025\n    for LP and PY. The measured values are the means over models and cells of burst frequency\n    (1.246 Hz, range 0.987 to 1.627), PD duty cycle and LP and PY duty cycle. With the 0.20 LP and\n    PY target of the variant, 0 of 38. 3 is below the criterion's 18.\n  deviations:\n  - The 38 deposited models are used; the files do not say which 36 the paper means.\n  - The model is simulated with a numba port of the deposited Java, which matches the Java's\n    voltages to 3e-9 mV over 3 s (4X6W66 at 18 C; the notebook compiles and runs the Java when a\n    compiler is present).\n  - Burst frequency and duty cycle are per-cycle means, with spikes as upward crossings of -20\n    mV and bursts formed with the Methods' 200 ms threshold; the paper gives no spike threshold.\n- claim: fig1c-frequency-q10-phase-constant\n  outcome: partially_reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig1c-frequency-q10-phase-constant\n  measured:\n  - 1.927\n  notes: Model 4X6W66, 16 temperatures, 40 s each with the first 10 s dropped and 30 s averaged.\n    Frequency Q10 is 1.927 (fit), 1.982 (end points) and 1.937 (f20 over f10), within 2 +- 0.2\n    under every reading; the three cells' frequencies differ by at most 0.8% at any temperature.\n    Constancy fails under both readings because of the LP duty cycle, which spans 0.11 of a cycle\n    (bound 0.1) and changes by up to 34% from its 10 C value (bound 20%); PY duty cycle changes by\n    up to 21%. All other duty cycles and phases stay within 0.1 of a cycle (PD offset range 0.05,\n    LP onset 0.038, LP offset 0.08, PY onset 0.023, PY offset 0.047). The network is triphasic at\n    all 16 temperatures.\n  deviations:\n  - Simulations of 40 s with the first 10 s dropped (the Methods drop 10 s when scoring and the\n    Figure 1 legend averages over 30 s; the length of the run is not stated).\n- claim: fig1s1-three-models\n  outcome: not_reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig1s1-three-models\n  notes: In WWZ3CN, FGFKQS and 71G6LA the frequency rises from 10 to 25 C in every cell (Q10 by the\n    fit 2.05, 1.99, 1.71) and the network is triphasic at all 16 temperatures, but none meets\n    either reading of constancy. Largest ranges over temperature 0.171 (WWZ3CN, LP offset), 0.121\n    (FGFKQS, LP duty cycle), 0.102 (71G6LA, PY offset) of a cycle; largest changes from 10 C 34%,\n    43% and 24%. 71G6LA misses reading (i) by 0.002. FGFKQS has the same maximal conductances as\n    4X6W66, with different Q10 values, so the statement's \"different maximal conductances\" holds\n    for two of the three.\n  deviations:\n  - The same 40 s simulations as fig1c-frequency-q10-phase-constant, at its 16 temperatures (the\n    supplement's legend was not read).\n- claim: all-models-compensated\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:all-models-compensated\n  measured: 36\n  notes: 36 of the 38 deposited models are triphasic at all 16 temperatures. ED50XO fails at 19\n    and 21 C (all cells irregular bursting) and MAXTTP at 10 and 14 C (LP irregular bursting).\n    With the order required in every cycle (variant), 35 of 38. The deposit holds more than one Q10\n    set for 9 of its 27 distinct sets of maximal conductances (20 models), and all 20 are\n    compensated; the other 18 sets have one Q10 set each, so \"multiple sets for every G\" can be\n    shown only for those 9. The count 36 of 38 meets the partial bound of 34; whether the paper's\n    36 are these 36 cannot be told from the files. The question of how the firing order is tested\n    is for the paper's authors (finding 6).\n  deviations:\n  - Triphasic is read as the three cells' mean burst frequencies within 5% and the median LP\n    burst onset phase before the median PY onset phase, both within the PD cycle; the Methods say\n    \"fired in the right order\" without saying how it is tested. Assumed as the plainest reading;\n    the every-cycle variant gives 35 in place of 36.\n- claim: intermediate-temperature-failures\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The deposit holds 38 parameter sets with nothing that marks which solutions were screened\n    or discarded, and not the 40 solutions screened. Of the 38 deposited, 2 are not triphasic at\n    some temperature between 10 and 25 C (all-models-compensated).\n- claim: figs2-ramp-largest-isi\n  outcome: reproduced\n  notebook: ramps.ipynb\n  output: claim:figs2-ramp-largest-isi\n  notes: PLKTEM, 10 to 25 C over 60 min. The median per-cycle largest ISI falls in every 4 min (1\n    degree) window with no increase in all three cells (PD 0.604 to 0.299 s, LP 0.613 to 0.301 s,\n    PY 0.522 to 0.251 s; Spearman -1.000 each). In 1 min windows the Spearman correlations are\n    -0.998, -0.998 and -0.994, with 7, 9 and 22 increases between successive windows.\n  deviations:\n  - The deposit has no ramp code; the temperature is changed linearly and the temperature factors\n    updated every 1 ms, from the deposited initial conditions at 10 C.\n- claim: figs3-duty-cycle-variable-across-models\n  outcome: reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:figs3-duty-cycle-variable-across-models\n  measured: 1.0\n  notes: On the criterion's variant (per-burst LP duty cycles from the 16 fixed temperatures, 30 s\n    each), all 703 pairs of the 38 models differ at p < 0.05 (two-sample Kolmogorov-Smirnov),\n    including every pair that shares its maximal conductances (largest p 0.025, EF84RN against\n    FGFKQS). The mean LP duty cycle falls with temperature in 23 models (Spearman below -0.5),\n    rises in 3 and neither in 12. The main reading, the 60 min ramp of every model, was not run.\n  deviations:\n  - The ramp reading (38 models, 3600 s each) would add about 35 min to a notebook (measured on a\n    subset at about 67 simulated seconds per second on 4 processes) and was not run; the outcome\n    rests on the variant reading the criterion names.\n  - 703 pairs of 38 models, where the criterion counts 630 pairs of 36.\n- claim: fig2-lp-spike-amplitude-threshold\n  outcome: partially_reproduced\n  notebook: voltage_distributions.ipynb\n  output: claim:fig2-lp-spike-amplitude-threshold\n  notes: G7P2WE, LP, 26 temperatures from 10 to 25 C, 30 s at dt = 0.001 ms with the last 10 s\n    kept (5 x 10^5 samples, as the Methods say). The amplitude falls under both readings (peak\n    minus trough 56.9 to 26.2 mV; upper envelope 16.7 to -1.8 mV; Spearman -1.000 each). The\n    threshold under reading (a) stays near -28 mV (-27.8 to -27.5 mV, with a dip to -28.6 mV\n    between; Spearman -0.197), so it does not depolarize steadily. Reading (b), where the\n    distribution's spike region begins, was not computed, as neither the paper nor the claims file\n    says how that point is located; it could change the outcome to reproduced.\n  deviations:\n  - 26 of the Methods' 101 temperatures (steps of 0.6 C), as 101 at dt = 0.001 ms would take\n    about 40 min.\n  - Threshold reading (b) not computed.\n- claim: fig2s1-peak-voltage-diverse\n  outcome: reproduced\n  notebook: voltage_distributions.ipynb\n  output: claim:fig2s1-peak-voltage-diverse\n  notes: Upper envelope from 10 to 25 C, per cell. G7P2WE falls in every cell (-19.1, -18.5, -13.8\n    mV); 4X6W66 rises in every cell (3.9, 7.3, 6.3 mV, more than 5 mV in LP and PY); MAXTTP stays\n    within 5 mV in every cell (-1.5, -2.5, 1.0 mV). The 2 mV variant loses MAXTTP and the 10 mV\n    variant loses 4X6W66. The mean V rises in 8 of the 9 cells and falls in one (4X6W66 LP, -0.26\n    mV).\n  deviations:\n  - Six temperatures (10, 13, 16, 19, 22, 25 C) in place of 101; the criterion uses the 10 and\n    25 C values.\n- claim: fig3-current-amplitudes\n  outcome: partially_reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig3-current-amplitudes\n  measured:\n  - 0.486\n  - 8.945\n  notes: PD cell, 13 s with the last 3 s analysed, as the deposit's currentscape script does. In\n    4X6W66 the Na peak grows 2.42-fold, the CaT peak falls to 0.486 (0.5 +- 0.05) and the KCa peak\n    grows 8.95-fold (reading a) or 9.10-fold (reading b), outside 6 +- 0.6. In SJR46Y the Na peak\n    falls to 0.81 and the KCa peak to 0.80. Four of the five parts hold under both readings, the\n    criterion's partial case; with the panels swapped, none does.\n  deviations:\n  - The 13 s simulation with a 10 s transient and 3 s analysed is the deposit's script\n    integratePyloricSQ10s_currentscapes_RK4_mp.py (transient = 10, nsecs = 3); the paper does not\n    give it.\n- claim: fig4-currentscapes-reorganize\n  outcome: not_reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig4-currentscapes-reorganize\n  notes: WWZ3CN, 3 s at 10 and 25 C (3 and 9 bursts per cell). The PD leak current has no inward\n    share inside the bursts at either temperature (0.0000 at start and end; all leak reversal\n    potentials are -50 mV, and V stays above them between the first and last spike), so its part\n    cannot hold. The PD A share at the start over the end of the burst is 1.278 at 10 C, outside\n    0.8 to 1.25, and 1.348 (thirds) or 1.385 (20%) at 25 C. The KCa share at the end of the burst\n    rises in LP (+0.29, +0.34) and PY (+0.22, +0.25) but falls in PD (-0.21, -0.20). No part of the\n    criterion holds under either reading.\n  deviations:\n  - A burst runs from its first to its last spike; with the leak inward only below -50 mV, a burst\n    that includes the slow wave around it would be another reading, not named in the criterion\n    and not run.\n- claim: currentscapes-dominant-currents\n  outcome: reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:currentscapes-dominant-currents\n  measured: 0.993\n  notes: 38 models, 3 cells, 10, 15, 20 and 25 C, 26,868 spikes. Na has the largest inward share in\n    the 1 ms before every spike peak (1.000) and Kd the largest outward share in the 1 ms after it\n    (1.000). At the 5% of time with the lowest voltage, H holds the largest inward share in all 456\n    cases and the synaptic current the largest outward share in 453 (KCa in 3), so both hold in\n    0.993 of cases (PD 0.98, LP and PY 1.0). The variant gives the same 0.993.\n  deviations:\n  - The 38 deposited models.\n- claim: fig5-a-to-kca-tradeoff\n  outcome: reproduced\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig5-a-to-kca-tradeoff\n  notes: FGFKQS (the Methods' model), the 20 ms after the last spike of each PD burst, 16\n    temperatures. The A share falls from 0.312 to 0.082 and the KCa share rises from 0.077 to 0.577\n    (Spearman -1.000 and 1.000); A exceeds KCa at 10 C and KCa exceeds A at 25 C. In J9U8SQ (the\n    legend's reading) the trends hold (-0.997 and 0.953) but KCa already exceeds A at 10 C (0.304\n    against 0.197). The statement's part on the repolarization of the last spike is not tested\n    separately.\n  deviations:\n  - The window starts at the -20 mV crossing of the last spike of the burst (the claims file says\n    burst termination, last spike of the burst).\n- claim: fig6-crash-different-mechanisms\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig6-crash-different-mechanisms\n  notes: FGFKQS and 71G6LA are triphasic at 10 and 25 C. At 30 C (40 s, last 30 s), 71G6LA's PD is\n    quiescent (no spike), but FGFKQS's PD fires 1005 spikes (class other), so complete loss of PD\n    activity holds in one of the two models, and the criterion requires both. The dominant PD\n    currents at 30 C differ between the models (H and KCa in FGFKQS, H and Syn in 71G6LA).\n  deviations:\n  - Each temperature is simulated from the deposited initial conditions, as the deposit's scripts\n    do; how the paper reached 30 C (a ramp or a fresh start) is not stated, and the classes rest\n    on the -20 mV spike threshold (assumed).\n- claim: fig6s1-crash-mechanisms\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig6s1-crash-mechanisms\n  notes: Seven of the eight models are in the deposit; Q8FBN1 is not. All seven stop being\n    triphasic below 35 C (B7SD0L 32, J9U8SQ 29, 4R2719 32, R3VIEW 30, RMZ8KZ 29, EF84RN 30, SJR46Y\n    26 C, skipping runs that diverged), but the dominant (inward, outward) current pairs per cell\n    form 5 distinct patterns; B7SD0L, J9U8SQ and EF84RN share H and Syn in all three cells.\n    Reproduction needs every pattern distinct, and the partial case at least six distinct among\n    eight; with the missing model, at most six could be. So the outcome would be not reproduced or\n    at best partially reproduced with the eighth model.\n  deviations:\n  - Seven of the eight models; Q8FBN1 is not in the deposit.\n  - Crash temperatures come from simulations from the initial conditions at each temperature (40\n    s, last 30 s); runs whose integration diverged are skipped.\n- claim: fig7-high-temperature-slow-timescales\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Three of the five models (G81PUL, G7EOZ8, SAXT8Y) are not in the deposit. Of the two that\n    are, J9U8SQ at 34 C diverges numerically (NaN) from the initial conditions, and KMNLBC (KNMLBC\n    of the Methods) at 30 C is triphasic in the last 30 s of a 40 s run, with no gap between spikes\n    longer than 0.68 s. FGFKQS at 34 C (the panel A variant) is quiescent. Over all 38 models at 26\n    to 35 C, 81 of the non-triphasic runs have all cells quiescent, 29 diverged, and the rest mix\n    regular, irregular and other classes.\n- claim: fig8a-hysteresis-quiescence\n  outcome: reproduced\n  notebook: ramps.ipynb\n  output: claim:fig8a-hysteresis-quiescence\n  measured: 1.94\n  notes: 0SHNMD (OSHNMD of the Methods), 10 to 35 C in 30 min and back. PD fires its last spike on\n    the up ramp at 34.16 C (1739.7 s), stays quiescent for 260 s across the top, and resumes at\n    32.22 C on the down ramp, 1.94 C lower (2 +- 0.2). The legend's \"before 600 s\" is not met (the\n    last spike is at 1740 s), not judged. The variant H5AIZR differs by 0.05 C.\n  deviations:\n  - The ramp is implemented here (linear, factors updated every 1 ms), from the deposited initial\n    conditions at 10 C.\n- claim: fig8-up-down-ramps\n  outcome: blocked\n  blocked_by: too_large\n  notebook: ramps.ipynb\n  output: claim:fig8-up-down-ramps\n  notes: The criterion is met when either ramp reading gives a count within 34 +- 3. The first\n    reading (10 to 35 C and back over 60 min) was run, and 22 of 38 models are similar on the two\n    legs over 10 to 25 C (9 at a 5% bound, 28 at 20%). Six models diverge numerically on this ramp\n    (G7P2WE, INPO74, J9U8SQ, NJP4RT, R00977, SJR46Y), MAXTTP fires no spike on the down leg below\n    25 C, and 9 others exceed 10% or lose triphasic order in some window. No model has the same\n    spike count on both legs. The second reading (10 to 25 C over 60 min and back, 7200 s per\n    model) was estimated at about 68 min for 38 models (about 67 simulated seconds per second on 4\n    processes, measured on a subset), over the notebook limit, and was not run, so the outcome\n    cannot be decided.\n- claim: fig8b-pathological-attractor\n  outcome: not_reproduced\n  assumed: true\n  notebook: ramps.ipynb\n  output: claim:fig8b-pathological-attractor\n  measured:\n  - 17.08\n  - 11.32\n  notes: H5AIZR on the updown ramp, PD classified per minute. PD spikes in every window (at least 10\n    spikes), bursts regularly early on and leaves regular bursting at 28.8 C on the up ramp, so\n    the hysteresis part holds in that sense, but it is regular again from 32 to 35 C. On the way\n    down it returns to regular bursting for good at 17.08 C (20 +- 2), after isolated irregular\n    windows at 27.1, 22.1 and 17.9 C, and its longest PD ISI between 25 and 35 min is 11.32 s\n    (1 +- 0.1). Both numbers are out of tolerance. The variant 0SHNMD has PD windows with no spike.\n  deviations:\n  - The return temperature is read as the start of the last run of regular bursting windows on\n    the down ramp; the classification rests on the -20 mV spike threshold (assumed).\n- claim: fig9a-remove-a-current\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig9a-remove-a-current\n  notes: WWZ3CN. At 10 C the network is not triphasic after IA is removed, with irregular bursting\n    cells, under all three timings. At 25 C no timing leaves PD and LP regular with only PY\n    irregular. Under the Results' timing (20 s control, 20 s without IA) all three cells burst\n    irregularly and the network is not triphasic at 25 C, the criterion's partial case (PY\n    irregular, another cell not regular). The code's timing gives PD regular, LP and PY other; the\n    legend's gives PD and LP irregular, PY other.\n  deviations:\n  - Classes taken after removal with its first 2 s dropped (criterion), and resting on the -20 mV\n    spike threshold and the order test (assumed).\n- claim: fig9b-remove-kca-current\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig9b-remove-kca-current\n  notes: FGFKQS (the Methods' model, and the model of the deposit's KCa removal script). At 10 C\n    the network is triphasic before and after removal and slows (PD 1.061 to 0.904 Hz with the\n    code's timing, 1.067 to 0.918 Hz with the Results' timing); at 25 C all three cells are\n    quiescent after removal. The legend's timing (removal at 4 s from the initial conditions) does\n    not show it, nor does J9U8SQ under any timing (at 10 C it becomes not triphasic).\n  deviations:\n  - The classes rest on the -20 mV spike threshold and the order test (assumed).\n- claim: fig10a-graded-removal\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig10a-graded-removal\n  measured: 3\n  notes: 4X6W66, 20 s per condition with the first 10 s dropped. Three of the five stated grid cells\n    match. Na at 75% at 10 C makes LP (and PD and PY) burst irregularly with the network not\n    triphasic, and at 25 C the network stays triphasic; CaT and CaS at 0% are not triphasic at\n    either temperature, with different cell classes. KCa removal at 10 C keeps the network\n    triphasic at 75% and 50% but not at 25% and 0% (PD and PY quiescent, LP tonic spiking), and\n    KCa at 0% at 25 C leaves LP tonic spiking, so not every cell is quiescent.\n  deviations:\n  - Each condition simulated from the deposited initial conditions; the classes rest on the -20 mV\n    spike threshold and the order test (assumed).\n- claim: fig10b-complete-removal-differs\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_alonso_2020.ipynb\n  output: claim:fig10b-complete-removal-differs\n  notes: 38 models, each current at 0% at 10 and 25 C. Comparing all four classes, CaT has the\n    largest fraction responding differently (0.974), but complete removal of H gives the same,\n    quiescent, state at both temperatures in 31 of 38 models (the criterion asks at least 33), and\n    2 of the 6 other currents (8 currents; 2 of 5 without leak) fall within 0.3 to 0.7. Comparing\n    the network class alone, CaT is not the largest (0.474 against A 0.579) and H 31. Fractions\n    responding differently (four classes) Na 0.237, CaS 0.605, A 0.737, KCa 0.316, Kd 0.263, H\n    0.158, leak 0.711.\n  deviations:\n  - The 38 deposited models; the bound of 33 was set for 36.\n  - The classes rest on the -20 mV spike threshold and the order test (assumed).\nfindings:\n- kind: data_missing\n  severity: major\n  notebook: reproduce_alonso_2020.ipynb\n  output: finding-model-names\n  statement: Four models the Methods name are not in the deposit, Q8FBN1 (Figure 6, figure\n    supplement 1) and G81PUL, G7EOZ8 and SAXT8Y (Figure 7). Three of the five models of Figure 7\n    and one of the eight of its supplement cannot be simulated.\n- kind: metadata_error\n  severity: minor\n  notebook: reproduce_alonso_2020.ipynb\n  output: finding-model-names\n  statement: Four models are filed under names that differ from the Methods. OSHNMD and B7SDOL are\n    0SHNMD and B7SD0L (digit 0 for the letter O), KNMLBC is KMNLBC (two letters swapped), and the\n    Figure 1 model, printed with a symbol in its second place, is 4X6W66. Each is the only close\n    match among the 38 files.\n- kind: other\n  about: data\n  severity: minor\n  notebook: reproduce_alonso_2020.ipynb\n  output: finding-shared-conductances\n  statement: The deposit holds 38 parameter sets, where the paper and the Dryad description say 36,\n    and nothing in the files marks which 36 the paper studied. The 38 share 27 distinct sets of\n    maximal conductances; 9 of them carry two or three Q10 sets.\n- kind: other\n  about: data\n  severity: minor\n  notebook: reproduce_alonso_2020.ipynb\n  output: finding-frequency-at-10C\n  statement: At 10 C the deposited models burst at 1.25 Hz on average (0.99 to 1.63 Hz), and 10 of\n    38 are within 10% of the 1 Hz target the Methods give for the control rhythm; all 38 are\n    triphasic.\n- kind: other\n  about: data\n  severity: minor\n  notebook: reproduce_alonso_2020.ipynb\n  output: finding-diverges-at-high-temperature\n  statement: The deposited integrator (RK4, dt = 0.05 ms, the deposited initial conditions)\n    returns NaN for 6 of the 38 models at some temperatures from 26 to 35 C (29 of 380 runs), and\n    for the same 6 on the 10 to 35 C ramp. The deposited Java does the same (G7P2WE at 35 C gives\n    NaN after 0.1 s). Results at those temperatures cannot be computed at the paper's time step.\n- kind: methods_unavailable\n  statement: Questions for the paper's authors. (1) What voltage threshold detects a spike? This\n    attempt uses upward crossings of -20 mV. (2) How is \"fired in the right order\" tested for the\n    triphasic class? This attempt compares the median LP and PY burst onset phases within the PD\n    cycle; requiring the order in every cycle changes the compensated count from 36 to 35 of 38.\n    (3) How is the lag d between spike onset and the -50 mV crossing formed? This attempt takes the\n    median over spikes of the time from the last upward crossing. (4) How were the temperature\n    ramps run, and were high-temperature states (Figures 6 and 7) reached from a ramp or from the\n    initial conditions? (5) Which 36 of the 38 deposited models are the paper's? These choices\n    enter every classification-based outcome marked as assumed.\n"
}
```

```
File created successfully at: attempts/alonso-2020-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -nE "^\s{4,}.*: " attempts/alonso-2020-01.yaml | head; grep -n "—\|rather" attempts/alonso-2020-01.yaml entries/alonso-2020/README.md | head; python tools/entry.py check entries/alonso-2020 2>&1 | tail -8; date -u
```

```
15:    name: CatalystNeuro
17:    harness: Claude Code
18:    model: claude-opus-5-5
19:    protocol: pilot-19
21:    platform: GitHub Actions
22:    url: https://github.com/encorescience/encore-registry/actions/runs/46075031684
0 error(s)
Sat Nov 28 00:58:23 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && grep -c "rather\|—" *.ipynb pyloric.py README.md; cd ../.. && python tools/entry.py handover entries/alonso-2020 2>&1 | tail -5; ls executed/alonso-2020/handover/; git status --short | head -20
```

```
ramps.ipynb:0
reproduce_alonso_2020.ipynb:0
voltage_distributions.ipynb:0
pyloric.py:0
README.md:0
wrote executed/alonso-2020/handover
alonso-2020.yaml
pyloric.py
ramps.ipynb
reproduce_alonso_2020.ipynb
voltage_distributions.ipynb
 M tools/build_site.py
 M tools/runner/chain.sh
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/alonso-2020; date -u
```

```
total 252
drwxr-xr-x   4 runner runner  4096 Nov 27 23:58 .
drwxr-xr-x 358 runner runner 16384 Nov 27 22:17 ..
drwxr-xr-x   3 runner runner  4096 Nov 27 22:19 .claude
-rw-r--r--   1 runner runner  3105 Nov 27 23:57 README.md
drwxr-xr-x   2 runner runner  4096 Nov 28 00:04 __pycache__
-rw-r--r--   1 runner runner  1102 Nov 27 23:57 entry.yaml
-rw-r--r--   1 runner runner 30983 Nov 27 22:54 pyloric.py
-rw-r--r--   1 runner runner 18492 Nov 27 23:57 ramps.ipynb
-rw-r--r--   1 runner runner 68946 Nov 27 23:57 reproduce_alonso_2020.ipynb
-rw-r--r--   1 runner runner    46 Nov 27 22:56 requirements.in
-rw-r--r--   1 runner runner 81391 Nov 27 23:57 requirements.lock.txt
-rw-r--r--   1 runner runner 11630 Nov 27 23:57 voltage_distributions.ipynb
Sat Nov 28 00:58:39 UTC 2026
```

**Agent calls Bash**

```bash
find entries/alonso-2020/.claude | head; rm -rf entries/alonso-2020/__pycache__
```

```
entries/alonso-2020/.claude
entries/alonso-2020/.claude/.cc-writes
```

**Agent**

I've finished steps 1 to 5 of the Author section and run the handover (step 6). `entry.py all` passed: 0 check errors and all three notebooks ran in about 58 min. The handover package is in `executed/alonso-2020/handover/`. Nothing is committed.

The dataset is code, not recordings: one zip with the authors' Java model, their Python scripts and one parameter file per model network. So every claim is tested by simulating the deposited models. I ported the Java to Python with numba (`pyloric.py`), and it matches the deposited Java to within 3e-9 mV.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| deposit-models | not reproduced (3 of 38 models within tolerance at 10 °C) |
| fig1c-frequency-q10-phase-constant | partially reproduced (Q10 1.93 to 1.98; LP duty cycle not constant) |
| fig1s1-three-models | not reproduced (constancy fails in all three) |
| all-models-compensated | partially reproduced (36 of 38), assumed |
| intermediate-temperature-failures | blocked, data_missing |
| figs2-ramp-largest-isi | reproduced |
| figs3-duty-cycle-variable-across-models | reproduced, on the criterion's 16-temperature variant |
| fig2-lp-spike-amplitude-threshold | partially reproduced (amplitude falls; threshold reading (a) does not rise; (b) not computed) |
| fig2s1-peak-voltage-diverse | reproduced |
| fig3-current-amplitudes | partially reproduced (4 of 5 parts; KCa ratio 8.9, expected 6 ± 0.6) |
| fig4-currentscapes-reorganize | not reproduced |
| currentscapes-dominant-currents | reproduced |
| fig5-a-to-kca-tradeoff | reproduced (FGFKQS) |
| fig6-crash-different-mechanisms | not reproduced (FGFKQS PD still spikes at 30 °C), assumed |
| fig6s1-crash-mechanisms | not reproduced (7 of 8 models; 5 distinct patterns), assumed |
| fig7-high-temperature-slow-timescales | blocked, data_missing (3 of 5 models absent) |
| fig8a-hysteresis-quiescence | reproduced (1.94 °C) |
| fig8-up-down-ramps | blocked, too_large (first reading gives 22 of 38; second reading not run) |
| fig8b-pathological-attractor | not reproduced (17.1 °C and 11.3 s), assumed |
| fig9a-remove-a-current | partially reproduced, assumed |
| fig9b-remove-kca-current | reproduced (FGFKQS), assumed |
| fig10a-graded-removal | partially reproduced (3 of 5), assumed |
| fig10b-complete-removal-differs | not reproduced (H same and quiescent in 31 of 38, criterion asks 33), assumed |

## 2. Dataset, assumptions and questions

**Dataset** (Dryad version 94811, the only published version, so the one pinned):
- It holds 38 models, where the paper says 36. Nothing in the files says which 36 the paper studied. The 38 share 27 distinct sets of maximal conductances.
- Four models named in the Methods are absent: Q8FBN1, G81PUL, G7EOZ8 and SAXT8Y.
- Four are filed under other spellings: 0SHNMD (OSHNMD in the Methods), B7SD0L (B7SDOL), KMNLBC (KNMLBC) and 4X6W66 (printed with a symbol in its second place).
- At 10 °C the models burst at 1.25 Hz on average, against the Methods' 1 Hz target.
- The deposited integrator returns NaN for 6 models at some temperatures from 26 to 35 °C. The deposited Java does the same.

**Assumptions**, recorded as deviations:
- A spike is an upward crossing of -20 mV.
- "Fired in the right order" for the triphasic class is tested on the median LP and PY burst onset phases. Requiring the order in every cycle gives 35 of 38 compensated models instead of 36.
- The lag d of the classification scheme is the median time from the last -50 mV crossing to each spike.
- The deposit has no ramp code, so I implemented the ramps myself (linear, starting from the deposited initial conditions).

**Questions for the paper's authors** are recorded as a `methods_unavailable` finding: the spike threshold, the order test, how d is formed, how the ramps and the high-temperature states were run, and which 36 models are the paper's.

**Questions for a reader:** none. I found no place where the claims file misreads the paper.

## 3. Where the protocol was unclear or did not fit

1. Step 2's checks of clocks and trial alignment have nothing to apply to in a deposit of code and parameters. I checked the port against the deposited Java instead, inside the notebook, when a Java compiler is present.
2. archives.md asks for the SHA-256 that Dryad's file list gives, but the list gives only an MD5. I check the MD5 and print a SHA-256 that I computed.
3. The entry's hash covers markdown cells, so writing the conclusions after a run forces another full run, about 60 min here. Because the simulations are deterministic, I ran the notebooks once while preparing, wrote the conclusions from those numbers, and then made a single official run. The numbers came out identical.
4. When the criterion says "reproduced under any reading" and one reading is too large to run, the protocol does not say whether to report the reading that ran or to block. I blocked fig8-up-down-ramps as too_large and gave the first reading's result (22 of 38) in the notes.
5. The protocol describes the runner as 4 CPUs, but 4 processes gave only about 2 times the single-process throughput. I measured this on a subset and used it for the time estimates. Because of it, three things were cut down or left out:
   - the ramp reading of figs3, which I recorded as a deviation;
   - fig2, which ran 26 of the Methods' 101 temperatures;
   - the second ramp reading of fig8-up-down.
6. Several claims say "all 36 models" while the deposit holds 38. I used all 38 and noted it in the deviations.

## 4. Runtime and failures

- The session took about 2 h 45 min. The official run took 13, 32 and 13 min for the three notebooks.
- During development, the first runs of the main notebook failed in three places, all fixed before the official run:
  - an empty slow-wave crossing list in the classification;
  - numba raising on a division by zero, which I set to follow IEEE arithmetic as the Java does;
  - a NaN model mask in fig6s1.
- Nothing failed in the official run.
- Untracked dotfiles that I did not create (`.bashrc`, `.vscode` and others) are in the repository root. I left them alone; the workflow should not commit them.

## End of run

83 turns, 163 minutes, $8.27 at API prices, result: success.
