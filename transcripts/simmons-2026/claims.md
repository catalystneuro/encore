# simmons-2026 · claims · run 42919613520

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "Reader" docs/protocol.md | head; ls paper/; wc -l paper/*; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md
```

```
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
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.adq8840.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== \|Supplement\|supplement\|github\|zenodo\|Data and materials\|code" paper/10.1126-sciadv.adq8840.txt | sed -n 1,80p
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.adq8840.txt",
 "offset": 1005,
 "limit": 402
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and supplement (Figs. S1 to S9) are all there. Next I'm checking the dataset listing and the code the paper links on Zenodo.

**Agent calls Bash**

```bash
cd  cat papers/datasets/simmons-2026.yaml; ls papers/ | head; grep -rl "001777" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | head
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1126/sciadv.adq8840
datasets:
- archive: dandi
  id: '001777'
  relation: primary
datasets
keys.yaml
manifest.yaml
match
renamed.yaml
triage.yaml
./transcripts/fujimoto-2026/001773/recorder.md
./transcripts/001777/claims-report.md
./transcripts/001777/claims.md
./transcripts/001777/claims-check.md
./transcripts/001777/claims-check-report.md
./papers/triage.yaml
./papers/manifest.yaml
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims | grep -i simmons; ls claims | grep 001777; head -30 transcripts/001777/claims-report.md; python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
for x in (it if isinstance(it,list) else it.values()):
    if '001777' in json.dumps(x)[:300]: print(json.dumps(x,indent=1)[:3000])
"
```

```
I didn't write the claims file. A safety classifier stopped my response while I was writing `claims/001777/10.1126-sciadv.adq8840.yaml`, so nothing was saved and `claims/001777/` doesn't exist. No quotes were checked and nothing is committed.

What I read before the stop:

- **Text**: the version of record (Science Advances, 9 September 2026, CC BY) in `paper/10.1126-sciadv.adq8840.txt`, with the full main text, Methods and figure legends. The supplement (Figs. S1 to S9) is present too. I opened PDF pages 3, 4, 6 and 8 for Fig. 2B's time axis (the train runs from 2 to 4 s of a 6-s sweep), Fig. 3B's cell count (about 45 cells) and the direction of Fig. 5F (the inhibitor-treated group fires faster). Nothing the claims need is missing from the paper.
- **Code**: `doi:10.5281/zenodo.10855006`, which resolves to version `doi:10.5281/zenodo.17297995` and holds one Mathematica notebook, "Code Sample.nb". It computes the spike rate per episode as spike count divided by episode length, takes the median over a stable window chosen by eye, and builds the PSTH. The window limits, bin width, trigger time and dropped episodes are placeholders in the code. Spike detection was done in Clampfit, with no settings given.
- **Outside data**: per-figure raw data and analyses are on Zenodo (`doi:10.5281/zenodo.15881780`). There are no folders for Figs. S1, S5, S6 or S8. Fig. 6D draws on Dopabase and GEO GSE271781. Fig. S5 comes from Gonzalez-Rodriguez et al. 2021.
- **Not read**: the protocols on protocols.io, because their API needs a login.

**Details the paper leaves open, for whoever writes the file:**

- **Fig. 3B**: the text gives n = 10 and the legend n = 45.
- **Fig. 3D**: the text gives P = 0.13 and the legend P = 0.06.
- **Fig. 4A and 4B**: the text gives P = 0.02 and P = 0.19; the legends give P < 0.01 and P = 0.16.
- **Unnamed tests**: Figs. 6C, 7D, 7E, 7H, S3 and S4D don't name their test.
- **Stable window**: the code chooses it by eye. Possible readings are all episodes, o
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL https://zenodo.org/api/records/10855006 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('id'),d.get('doi'),d['metadata'].get('title'),d['metadata'].get('version'));[print(f['key'],f['links']['self'],f['size']) for f in d.get('files',[])]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o code.nb "https://zenodo.org/api/records/17297995/files/Code%20Sample.nb/content"; python3 - <<'E'
import re
s=open('code.nb').read()
# extract strings in Cell[BoxData ... approximate: print text cells and input lines
for m in re.finditer(r'Cell\[(.{0,1500}?)",\s*"(Input|Text|Title|Section|Subsection|Code)"',s,re.S):
    t=m.group(1)
    t=re.sub(r'\\\[(\w+)\]','',t)
    print('---',m.group(2)); print(re.sub(r'\s+',' ',t)[:900])
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
import re
s=open('code.nb').read()
s=s.split('(* End of Notebook Content *)')[0]
# tokens: quoted strings
out=[]
for m in re.finditer(r'"((?:[^"\\]|\\.)*)"|Cell\[|"Input"|"Subsection"|"Text"',s):
    g=m.group(1)
    if g is None: continue
    if g in ('Input','Subsection','Text','Section','Output','Title'): out.append('\n['+g+']\n'); continue
    if g.startswith('ExpressionUUID') : continue
    out.append(g.replace('\\"','"').replace('\\<','').replace('\\>',''))
t=''.join(' '+x if re.match(r'\w',x) and out and re.search(r'\w$',''.join(out[-1:])) else x for x in out)
t=re.sub(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\\\n?[0-9a-f]+','',t)
print(t[:12000])
E
```

```
Detect Mean Spike rate per trial/episode
[Subsection]
],

Cell[BoxData[
 RowBox[{
  RowBox[{, , 
   RowBox[{
    RowBox[{
    , , , , , , , , , , , 
     , , , , , , , , , , 
     , }], , , 
    RowBox[{, , , , }]}], , }], 
  , 
  RowBox[{
   RowBox[{
    RowBox[{, , 
     RowBox[{, , 
      RowBox[{FILENAME.atf","Table"];\[IndentingNewLine]baseTrim=base[[4;;-1]];\neps=Range[First[baseTrim[[-1]]]];
[Input]
[... 408 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
import re
s=open('code.nb').read().split('(* End of Notebook Content *)')[0]
# split into Cell[ chunks
cells=re.split(r'\nCell\[',s)
for c in cells:
    kind=re.search(r'"(Input|Subsection|Text|Section|Title|Output)"\s*,?\s*(\n|CellChangeTimes|ExpressionUUID|CellLabel)',c)
    toks=re.findall(r'"((?:[^"\\]|\\.)*)"',c)
    toks=[t for t in toks if t not in ('Input','Subsection','Text','Section','Output','Title') and not re.match(r'^[0-9a-f]{8}-',t)]
    txt=''.join(t if not re.match(r'^\w',t) else ' '+t for t in toks)
    txt=txt.replace('\\[IndentingNewLine]','\n').replace('\\n','\n').replace('\\<','').replace('\\>','').replace('\\"','"')
    if txt.strip(): print('=====',kind.group(1) if kind else '?'); print(txt[:2500])
E
```

```
===== Subsection
 Detect Mean Spike rate per trial/episode
===== ?
(*  Pull  in  Axon  text  file  records  of  detected  spikes  exported  from  ClampFit,  trim  the  Header *)
 base= Import["FILENAME.atf","Table"];
 baseTrim= base[[ 4;;- 1]];
 eps= Range[ First[ baseTrim[[- 1]]]];
===== Input
(* Count  detected  events  per  episode/ trial,  divide  event #  by  EPISODE_LENGTH*)
(* Ignores  Structure  inside  trial,  but  avoides  weird  elements  in  imported  lists*)
 traceEvents= Table[ baseTrim[[ i, 1]],{ i, Length[ baseTrim]}];
 traceCounts= Table[ Count[ traceEvents, i],{ i, eps}];
 traceWindow= EPISODE_LENGTH;
 rates= traceCounts/ traceWindow;
 Max[ rates];
===== Input
(* Visualize  spike  rate  over  time  to  identify  stable  baselines  from  START  to  END  for  measurement*)
 epsOK= eps;
 ListPlot[ Transpose[{ epsOK, rates[[ epsOK]]}], PlotRange\[Rule]{ 0, Ceiling[ Max[ rates], 10]}, PlotStyle\[Rule] PointSize[ 0.02], GridLines\[Rule] Automatic]
===== Input
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if str(x.get('id',x.get('identifier','')))=='001777' or x.get('dandiset')=='001777': print(json.dumps(x,indent=1)[:4000]); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
grep -n -A12 "001777" papers/manifest.yaml | head -30
```

```
{
 "dandiset": "001777",
 "name": "Astrocytes mediate the dopaminergic modulation of tonic GABAergic signaling in Substanta nigra",
 "published_version": "0.260521.2201",
 "asset_count": 412,
 "size_gb": 18.19,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1101/2024.03.27.586699",
   "title": "Astrocytes mediate the dopaminergic modulation of tonic GABAergic signaling in substantia nigra",
   "relation": "IsSupplementTo",
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001777/versions/0.260521.2201/info/ | python3 -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d['name']);print(d.get('description'));print(d.get('assetsSummary',{}).get('variableMeasured'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for r in 10850896 17296457; do curl -sL https://zenodo.org/api/records/$r | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('id'),d.get('doi'),d['metadata'].get('title'));print(d['metadata'].get('description','')[:600]);[print(' ',f['key'],f['size']) for f in d.get('files',[])[:40]]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; which pdftoppm; python3 -c "import fitz" && python3 -c "
import fitz;d=fitz.open('paper/10.1126-sciadv.adq8840.pdf')
for p in [2,3,5,7]:
    d[p].get_pixmap(dpi=110).save(f'p{p+1}.png')
print('ok')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.adq8840.pdf",
 "pages": "3-8"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I can't render the PDF pages with the tools installed, so I'll try installing PyMuPDF into a temp directory to read the figures.

**Agent calls Bash**

```bash
cd $TMPDIR; pip install -q --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python3 -c "
import fitz;d=fitz.open('paper/10.1126-sciadv.adq8840.pdf')
for p in [1,2,3,4,5,7]:
    d[p].get_pixmap(dpi=100).save(f'p{p+1}.png')
print('ok')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.png"
}
```

Result: no output.

**Agent**

Figures checked (Fig. 2B train at 2 to 4 s of a 6-s sweep; Fig. 3B about 45 cells; Fig. 5F inhibitor group higher). Now looking at a recent claims file for the header format, then writing.

**Agent calls Bash**

```bash
cd  ls -t claims | head -3; f=claims/$(ls -t claims | head -1); sed -n 1,60p $f; grep -n "kind:\|open\b\|readings" claims/*.yaml | head -5; sed -n 1,40p tools/claims_check.py
```

```
plitt-2021.yaml
kim-2022.yaml
zaimi-2018.yaml
# Claims for Plitt & Giocomo (2021), Nature Neuroscience 24, 705-714, on dandiset 000054.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md (reader, steps 1 to 4).
#
# Text read: the NIH author manuscript in PubMed Central (PMC8893323, NIHMS1780011), full text
# with Results, Discussion, Methods, the main and Extended Data figure legends, and the
# supplementary information PDF (Supplementary Figs. 1 to 4, the simulations of earlier morph
# studies). It is the accepted manuscript, not the version of record. No main-text PDF was
# available, so no figure was read from an image; claims shown only in a figure are read from
# legends and Results. The Supplementary Video and the Reporting Summary were not read.
#
# Code read: https://github.com/GiocomoLab/PlittGiocomo_2021 (linked under Code availability),
# at two commits. dca5a57 (2020-10-28) is the last commit before publication; its analysis is in
# notebooks/*.ipynb (PlotAllPlaceCells, PlotPopSimMats, SFReg, DataLLR, NullModels4GrumpyPantsReviewer,
# SingleCellSimMats, SingleCellNMF, KWTA_EmpiricalPrior, TheoreticalSimMats) and morph_analyses/*.py;
# its main_figs and extended_data_figs notebooks are empty. 9230b0a (2026-04-16, HEAD) is a refactor
# under src/morph_analyses and notebooks/main_figs that reads the NWB files; its README says it holds
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps({k:v for k,v in s.items() if k!='\$defs'},indent=1)[:2500])
d=s.get('\$defs',{})
for k,v in d.items(): print(k, list(v.get('properties',{}).keys()), v.get('required'))
"; sed -n 60,80p claims/plitt-2021.yaml | head -5; grep -n "^[a-z_]*:" claims/plitt-2021.yaml | head
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
p=s['properties']['claims']['items']['properties']
for k,v in p.items(): print(k,':',v.get('description','')[:300], v.get('enum',''))
print(list(s['properties'].keys()))
"
```

```
id : Stable within the file, e.g. fig2b. 
statement : The finding in one or two sentences, in words. Not a copy of the figure. 
source : Where the paper shows it, precise enough to find without searching: a figure panel, e.g. 'Figure 2B', or a section and paragraph, e.g. 'Results, Place fields, paragraph 3'. 
kind : A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source data, code or deposits). Links are not findings of the paper and are counted apart from them. ['finding', 'link']
quote : The sentence of the paper that states the finding, word for word, from the place `source` names, so a reader can check the statement against the paper. Cut with '...' where it runs long. From the full text. 
inferred : For a finding with no quote: why the statement is the author's reading and not a sentence of the paper, e.g. 'Numbers from Supplementary Table 1; no sentence states them.' 
expected : The reported numbers the claim rests on, each with a tolerance: one, or a list. 
statistics : The statistical support the paper reports for the finding: one entry per test or interval, as the paper gives it. A record of the paper, not a target with a tolerance (that is `expected`). 
criterion : For a claim without a number, how it will be judged. Written before the analysis is run. 
depends_on : Ids of claims in this file whose result this one uses. 
data : What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in anoth ['dataset', 'with_labels', 'with_inputs', 'elsewhere']
where : For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A3 "^\s*36\.\|^\s*25\.\|^\s*40\.\|^\s*31\." paper/10.1126-sciadv.adq8840.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; PYTHONPATH=$TMPDIR/pylib python3 -c "
import pymupdf as fitz;d=fitz.open('paper/10.1126-sciadv.adq8840.pdf')
d[6].get_pixmap(dpi=100).save('p7.png')
s=fitz.open('paper/10.1126-sciadv.adq8840.supp.pdf'); print(len(s))
for p in [6,8]: s[p].get_pixmap(dpi=90).save(f's{p+1}.png')
" 2>&1 | grep -v Warn
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s7.png"
}
```

Result: no output.

**Agent**

I have what I need: the full text, Methods and supplement, plus the code (one Mathematica notebook). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/simmons-2026.yaml",
 "content": "# Claims for Simmons et al. (2026), Science Advances 12, eadq8840, tested on dandiset 001777.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md (reader, steps 1 to 4).\n#\n# Text read: the version of record (Science Advances, 9 September 2026, CC BY), full text with\n# Results, Discussion, Materials and Methods and figure legends, and its supplement PDF\n# (sciadv.adq8840_sm.pdf, Figs. S1 to S9). PDF pages 3, 4, 5, 6, 7 and 8 and supplement page 7\n# were opened to read Fig. 2B (the train runs from 2 to 4 s of a 6-s sweep), Fig. 3B (about 45\n# cells are plotted), Fig. 5F (the inhibitor-treated group fires faster) and Fig. S6 (WT against\n# KO, marked n.s.).\n#\n# Code read: the paper's code deposit, doi:10.5281/zenodo.10855006, which resolves to record\n# 17297995 (doi:10.5281/zenodo.17297995), one Mathematica notebook, \"Code Sample.nb\". It holds\n# three parts. (1) \"Detect Mean Spike rate per trial/episode\" imports the spike events exported\n# from Clampfit (.atf), counts events per episode, divides by EPISODE_LENGTH to give a rate per\n# episode, plots the rates \"to identify stable baselines from START to END\", and takes the median\n# rate over episodes START to END. (2) \"Collect Spiketimes across episodes into Histogram\" builds a\n# PSTH (findPSTHMini) as spike counts summed over episodes in bins of BINWIDTH, divided by bin\n# width times the number of episodes, relative to TIMEZERO, after dropping \"Glitched Episodes\"\n# (BADEP1, BADEP2). (3) Down-sampling and segmenting traces for figures. Every window, bin width,\n# trigger time and dropped episode is a placeholder. Spike detection itself was done in Clampfit;\n# its settings are not given in the paper or the code.\n#\n# Data the paper used. Male and female mice (C57BL/6J, DAT-Cre, PV-Cre, Aldh1a1-2A-iCre and\n# Aldh1a1-2A-iCre/DAT-2A-Flpo). Ex vivo sagittal or coronal slices with the SNr, 240 um, recorded\n# at 32 to 33 C (Methods). SNr neurons were recorded in cell-attached mode for spike rate, before\n# and after bath application of a drug (quinpirole 2 uM, gabazine 10 uM, CNO, SCH39166 2 uM, NPPB,\n# disulfiram 10 uM, DEAB 10 uM, rasagiline 10 uM, NNC-711, SNAP-5114 20 uM), in slices from mice\n# injected with Chronos in GPe (Figs. 1, 2), Gi-DREADD in GPe (Fig. 4), Gq- or Gi-DREADD under GFAP\n# in SNr (Figs. 7, S4), ALDH1A1 shRNA in SNc (Fig. 5) or Cre-dependent Gi-DREADD in SNc of DAT-Cre\n# mice (Figs. 6, S3), and in low glucose (Fig. S8) or at room temperature (Fig. S4). Whole-cell\n# voltage clamp at -60 mV with a Cs+ electrode gave optically (Fig. 1) or electrically (Fig. 4A)\n# evoked IPSCs. SNc neurons were recorded for Fig. S3. Other data are two-photon PercevalHR imaging\n# in SNc dopaminergic neurons (Fig. S9), RNAscope for D2R and S100B (Figs. 7A, S7), fluorescence\n# images of ALDH1A1+ and ALDH1A1- dendrites (Fig. 5A, B), fast-scan cyclic voltammetry in striatum\n# (Fig. S6), and outside expression data (Fig. 6D, Fig. S5). The n of each test is a number of\n# neurons (Fig. 3B, 5D), except where the legend says mice or cells and mice. The dandiset's title\n# is the paper's; its description says it holds \"binary files of electrophysiology data\", and its\n# variables are VoltageClampSeries and VoltageClampStimulusSeries.\n#\n# Outside data. The paper's raw data and analyses per figure are deposited at\n# doi:10.5281/zenodo.10850896 (resolves to record 15881780, \"Data Files and Analysys for ...\", with\n# folders for Figs. 1 to 7, S2, S3, S4, S7 and S9). The key resource table is\n# doi:10.5281/zenodo.17296457. Fig. 6D uses Dopabase (ref. 36, Gaertner et al. 2025, eLife 13,\n# RP101035). Fig. S5 is a table from Gonzalez-Rodriguez et al. 2021, doi:10.1038/s41586-021-04059-0.\n#\n# Common method, used by the criteria below (cited as M1 to M6).\n# M1 Spike rate. Spikes detected in Clampfit 10.3 (Methods, Analysis and statistics; the code\n#    imports Clampfit event exports). Detection settings are given nowhere; this cannot be fixed\n#    from the paper, so the author uses a standard threshold detection on the cell-attached current\n#    and reports it. Rate per episode is the spike count divided by the episode length (code, part\n#    1). A cell's rate in a condition is the median of its per-episode rates over a stable window\n#    (code, part 1). Which episodes form the stable window is chosen by eye in the code and not\n#    given in the paper. Readings: (a) all episodes of each condition; (b) the last stable stretch\n#    of each condition, for a drug the episodes from 6 min after the start of application, when\n#    the time courses of Fig. 7G have reached their steady level (the whole drug period when it\n#    is shorter than 6 min). A claim holds when its result holds under either reading.\n# M2 Percent change. The paper gives changes as \"roughly 30%\", \"about 50%\", \"28% mean increase\" and\n#    the Discussion calls them \"modal\". Readings: (a) the mean over cells of each cell's percent\n#    change; (b) the percent change of the group mean rates; (c) the median over cells of each\n#    cell's percent change. Where the paper writes \"mean\", readings (a) and (b) only.\n# M3 Tests. As named in each figure legend (paired t test for before and after in the same cell,\n#    Welch's t test for groups of cells, Wilcoxon or Mann-Whitney where named), at P < 0.05\n#    (Methods, Analysis and statistics). Sidedness is not stated; tests are two-sided (the\n#    GraphPad Prism default, a standard choice) and a one-sided result is shown as a variant.\n#    Where a legend names no test for a before and after comparison in the same cells, the paired\n#    t test used by the other such legends is the main reading and the Wilcoxon signed-rank test a\n#    variant.\n# M4 Before and after. The control value is from the recording before the drug; the drug value is\n#    from the same cell after bath application (legends, \"before and after bath application\").\n#    For an occlusion experiment the control is the cell in the first drug and the second value\n#    after the second drug is added (Figs. 3D, 5G, 5H, 6A, 6E, 7E, 7F).\n# M5 Units of n. Neurons, as in the legends; the attempt reports the number of mice where the\n#    dataset gives it. Where the text and the legend give different n or P for the same test, both\n#    are recorded and the claim holds when the result matches either.\n# M6 Absence. A claim that a drug had no effect is judged on the paper's test in M3 at P < 0.05:\n#    reproduced when the test does not find the effect, not reproduced when it does, with the size\n#    of the change given either way.\nschema_version: 2\npaper: doi:10.1126/sciadv.adq8840\nclaims:\n- id: fig1c-quinpirole-reduces-gpe-ipsc\n  statement: The D2R agonist quinpirole (2 uM) reduces the amplitude of optogenetically evoked\n    GPe IPSCs in SNr neurons by roughly 30%.\n  source: Results, D2R agonists inhibited phasic GABA release from GPe terminals, paragraph 1;\n    Figure 1C\n  quote: Quinpirole reduced the amplitude of the GPe evoked inhibitory postsynaptic currents\n    (IPSCs) by roughly 30% (P = 0.02 and n = 5)\n  statistics:\n  - test: paired t test\n    p: 0.02\n    n: 5 neurons\n  expected:\n  - quantity: reduction in GPe evoked IPSC amplitude with quinpirole\n    value: 30\n    tolerance: 3\n    unit: \"%\"\n  criterion: Whole-cell voltage clamp at -60 mV, Cs+ internal, optical stimulation of Chronos in\n    GPe axons (Results, paragraph 1). IPSC amplitude is how the paper does not say; read as the\n    peak of the evoked current from the pre-stimulus baseline, averaged over sweeps in each\n    condition (a standard choice, stated as one). Reproduced when a two-sided paired t test of\n    before against after quinpirole has P < 0.05 with amplitudes lower after, and the reduction\n    is within tolerance under one reading of M2.\n- id: fig1e-ppr-rises\n  statement: Quinpirole raises the paired-pulse ratio of GPe evoked IPSCs at a 50 ms interval,\n    consistent with a presynaptic site of action.\n  source: Results, D2R agonists inhibited phasic GABA release from GPe terminals, paragraph 1;\n    Figure 1D and 1E\n  quote: Consistent with a presynaptic locus of the modulation, the paired-pulse ratio of GPe\n    evoked IPSCs rose in the presence of quinpirole (P = 0.02 and n = 6)\n  statistics:\n  - test: paired t test\n    p: 0.02\n    n: 6 neurons\n  criterion: Paired pulses 50 ms apart (Fig. 1D legend). Paired-pulse ratio as the second IPSC\n    peak over the first; the paper does not define it, and whether the second peak is taken from\n    the pre-pulse baseline or from the decaying first IPSC is open. Readings (a) second peak from\n    the baseline before the first pulse; (b) second peak from the current just before the second\n    pulse. Reproduced when, under one reading, a two-sided paired t test has P < 0.05 with the\n    ratio higher after quinpirole.\n- id: fig2c-quinpirole-attenuates-gpe-inhibition\n  statement: A 2-s, 30-Hz optogenetic train of GPe inputs inhibits SNr spiking, and quinpirole\n    attenuates this inhibition.\n  source: Results, D2R agonists inhibited phasic GABA release from GPe terminals, paragraph 2;\n    Figure 2A to 2C\n  quote: As expected, quinpirole attenuated the ability of GPe stimulation to slow the spiking of\n    SNr neurons (P = 0.02 and n = 8)\n  statistics:\n  - test: Wilcoxon matched-pairs signed rank test\n    p: 0.02\n    n: 8 neurons\n  criterion: Cell-attached recording, 6-s sweeps with the 2-s, 30-Hz train from 2 to 4 s (Fig. 2A\n    and 2B). Percent inhibition is \"change in discharge rate/basal discharge rate\" (Fig. 2C\n    legend), with the basal rate from 0 to 2 s and the rate during the train from 2 to 4 s of\n    each condition's PSTH, built as in the code (part 2) over the condition's episodes. The\n    paper gives no bin width; the rates are taken over the whole windows, so the bin does not\n    matter. A per-sweep percent inhibition, its median over sweeps, is shown as a variant.\n    Reproduced when a two-sided Wilcoxon signed-rank test of control against quinpirole has P <\n    0.05 with less inhibition in quinpirole.\n- id: fig2b-inhibition-wanes\n  statement: The GPe train initially suppresses SNr spiking strongly, and the inhibition wanes\n    during the 2-s train.\n  source: Results, D2R agonists inhibited phasic GABA release from GPe terminals, paragraph 2;\n    Figure 2A and 2B\n  quote: Initially, this stimulation effectively suppressed SNr activity, but the efficacy of this\n    inhibition waned with time (Fig. 2, A to C)\n  criterion: The paper reports no test. From each cell's control PSTH (code, part 2), the rate in\n    the first 0.5 s of the train (2 to 2.5 s) and in the last 0.5 s (3.5 to 4 s); the 0.5-s\n    windows are a choice made here, as the paper gives none. Reproduced when the last window's\n    rate is higher than the first in the PSTH pooled over the 8 cells and in more than half of\n    the cells.\n- id: fig3a-quinpirole-increases-rate\n  statement: Quinpirole alone, with no GPe stimulation, raises the basal spike rate of SNr neurons,\n    by about 50% in cell-attached recordings.\n  source: Results, D2R agonists lowered tonic GABA release, paragraph 1; Figure 3A\n  quote: One of the unexpected observations in these experiments was the elevation in the basal\n    spiking rate of SNr neurons with bath application of quinpirole, in the absence of GPe axon\n    stimulation (P < 0.01 and n = 8) (Fig. 3A). The quinpirole-induced elevation in discharge rate\n    was about 50% when monitored in cell-attached mode.\n  statistics:\n  - test: paired t test\n    p: 0.01\n    p_relation: \"<\"\n    n: 8 neurons\n  expected:\n  - quantity: increase in SNr spike rate with quinpirole\n    value: 50\n    tolerance: 5\n    unit: \"%\"\n  criterion: Spike rates as in M1, before and after quinpirole (M4). Reproduced when a two-sided\n    paired t test has P < 0.05 with rates higher after, and the increase is within tolerance\n    under one reading of M2.\n- id: fig3b-gabazine-increases-rate\n  statement: Gabazine raises the basal spike rate of SNr neurons by roughly 25%, showing that they\n    are tonically inhibited through GABAA receptors.\n  source: Results, D2R agonists lowered tonic GABA release, paragraph 1; Figure 3B\n  quote: Bath application of gabazine (10 μM) increased the basal spiking rate of SNr neurons\n    recorded in cell-attached mode by roughly 25%, suggesting that they were tonically inhibited by\n    activation of GABAARs (P < 0.01 and n = 10)\n  statistics:\n  - about: as given in the Results\n    test: not named in the Results\n    p: 0.01\n    p_relation: \"<\"\n    n: 10 neurons\n  - about: as given in the Figure 3B legend\n    test: paired t test\n    p: 0.01\n    p_relation: \"<\"\n    n: 45 neurons\n  expected:\n  - quantity: increase in SNr spike rate with gabazine\n    value: 25\n    tolerance: 2.5\n    unit: \"%\"\n  criterion: Spike rates as in M1, before and after gabazine 10 uM at 32 to 33 C (M4). The Results\n    give n = 10 and the legend n = 45 (Fig. 3B plots about 45 cells; Fig. S4E has 44 at\n    physiological temperature, Fig. S1 has 39). The test uses every control cell with gabazine\n    alone the dataset holds, and the count is reported (M5). Reproduced when a two-sided paired t\n    test has P < 0.05 with rates higher after, and the increase is within tolerance under one\n    reading of M2.\n- id: fig3d-gabazine-occludes-quinpirole\n  statement: In the presence of gabazine, quinpirole does not change SNr spike rate.\n  source: Results, D2R agonists lowered tonic GABA release, paragraph 1; Figure 3D\n  quote: Indeed, in the presence of gabazine, quinpirole did not modulate SNr spiking rate (P =\n    0.13 and n = 7)\n  statistics:\n  - about: as given in the Results\n    test: not named in the Results\n    p: 0.13\n    n: 7 neurons\n  - about: as given in the Figure 3D legend\n    test: paired t test\n    p: 0.06\n    n: 7 neurons\n  criterion: A claim of absence (M6). Cells pretreated with gabazine, rate before and after\n    quinpirole (M1, M4). Reproduced when a two-sided paired t test gives P >= 0.05; not reproduced\n    when it gives P < 0.05. The change in rate is reported either way.\n- id: figs1-gabazine-effect-vs-base-rate\n  statement: The increase in SNr spike rate with gabazine is weakly and positively correlated with\n    the basal rate.\n  source: Supplementary Figure S1\n  quote: Summary data and linear regression of a weak positive correlation between basal discharge\n    rate and the effect of gabazine R2 = 0.11, n = 39\n  expected:\n  - quantity: R2 of the linear regression of the gabazine change in rate on basal rate\n    value: 0.11\n    tolerance: 0.011\n  criterion: Per cell, the basal rate and the change in rate (Hz) after gabazine (M1, M4), the axes\n    of Fig. S1 being \"Base Rate\" and \"Delta\". An ordinary least squares fit of the change on the\n    basal rate over the cells of fig3b-gabazine-increases-rate. Reproduced when the slope is\n    positive and R2 is within tolerance.\n  depends_on:\n  - fig3b-gabazine-increases-rate\n- id: fig4a-gpe-gi-dreadd-reduces-ipsc\n  statement: Activating Gi-DREADD in GPe with CNO reduces the amplitude of electrically evoked IPSCs\n    in SNr neurons, similar in size to the quinpirole effect on optogenetically evoked IPSCs.\n  source: Results, Tonic GABA release was not derived from GPe terminals or astrocytes, paragraph\n    1; Figure 4A\n  quote: Bath application of the DREADD agonist clozapine-N-oxide (CNO) reduced the amplitude of\n    electrically evoked IPSCs in voltage-clamped SNr neurons (P = 0.02 and n = 4) (Fig. 4A). This\n    modulation was similar in magnitude to that seen in optogenetically evoked IPSCs following D2R\n    stimulation.\n  statistics:\n  - about: as given in the Results\n    test: not named in the Results\n    p: 0.02\n    n: 4 neurons\n  - about: as given in the Figure 4A legend\n    test: paired t test\n    p: 0.01\n    p_relation: \"<\"\n    n: 4 neurons\n  criterion: IPSC amplitude as in fig1c-quinpirole-reduces-gpe-ipsc, before and after CNO.\n    Reproduced when a two-sided paired t test has P < 0.05 with amplitudes lower after, and the\n    percent reduction (M2) is within 10 percentage points of the reduction found for\n    fig1c-quinpirole-reduces-gpe-ipsc; the paper gives no measure of \"similar\", so this margin is\n    a choice made here, and the two reductions are reported.\n  depends_on:\n  - fig1c-quinpirole-reduces-gpe-ipsc\n- id: fig4b-gpe-gi-dreadd-no-rate-change\n  statement: Inhibiting GPe terminals with Gi-DREADD does not change the basal spike rate of SNr\n    neurons, so GPe terminals do not contribute to tonic GABA release.\n  source: Results, Tonic GABA release was not derived from GPe terminals or astrocytes, paragraph\n    1; Figure 4B\n  quote: However, CNO application had no effect on the basal spiking rate of SNr neurons recorded\n    in cell-attached mode, arguing that GPe terminals were not contributing to tonic GABA release\n    (P = 0.19 and n = 5)\n  statistics:\n  - about: as given in the Results\n    test: not named in the Results\n    p: 0.19\n    n: 5 neurons\n  - about: as given in the Figure 4B legend\n    test: paired t test\n    p: 0.16\n    n: 5 neurons\n  criterion: A claim of absence (M6). Rate before and after CNO in slices with GPe Gi-DREADD (M1,\n    M4). Reproduced when a two-sided paired t test gives P >= 0.05.\n- id: figs4b-astrocyte-gq-increases-rate\n  statement: Activating Gq-DREADD in SNr astrocytes with CNO raises the basal spike rate of SNr\n    neurons.\n  source: Results, Tonic GABA release was not derived from GPe terminals or astrocytes, paragraph\n    2; Figure S4B\n  quote: In these slices, bath application of the DREADD agonist CNO elevated the basal spiking rate\n    of SNr neurons recorded in cell-attached mode (P = 0.03 and n = 8)\n  statistics:\n  - test: paired t test\n    p: 0.03\n    n: 8 neurons\n  criterion: Rate before and after CNO in slices with GFAP-hM3 Gq-DREADD in SNr (M1, M4).\n    Reproduced when a two-sided paired t test has P < 0.05 with rates higher after.\n- id: figs4c-nppb-decreases-rate\n  statement: The bestrophin1 inhibitor NPPB lowers SNr spike rate, so bestrophin1 channels in\n    astrocytes are not releasing GABA onto SNr neurons.\n  source: Results, Tonic GABA release was not derived from GPe terminals or astrocytes, paragraph\n    2; Figure S4C\n  quote: In line with the notion that astrocytes were exciting (not inhibiting) SNr neurons, bath\n    application of the bestrophin1 inhibitor NPPB decreased SNr spiking rate (P = 0.03 and n = 6)\n  statistics:\n  - test: paired t test\n    p: 0.03\n    n: 6 neurons\n  criterion: Rate before and after NPPB (M1, M4); the NPPB concentration is not given. Reproduced\n    when a two-sided paired t test has P < 0.05 with rates lower after.\n- id: figs2a-d1-antagonist-increases-rate\n  statement: The D1R antagonist SCH39166 (2 uM) raises SNr spike rate significantly, by a small\n    amount (about 10%).\n  source: Results, Dopamine enhanced tonic GABA release from dSPN terminals, paragraph 1; Figure\n    S2A; Discussion, Tonic GABAergic signaling..., paragraph 2\n  quote: Bath application of SCH39166 (2 μM) did significantly elevate SNr spiking rate (P = 0.02\n    and n = 12) ... the modal change in spiking rate produced by antagonizing D1Rs was small (∼10%)\n  statistics:\n  - test: paired t test\n    p: 0.02\n    n: 12 neurons\n  expected:\n  - quantity: change in SNr spike rate with SCH39166\n    value: 10\n    tolerance: 1\n    unit: \"%\"\n  criterion: Rate before and after SCH39166 (M1, M4). Reproduced when a two-sided paired t test\n    has P < 0.05 with rates higher after, and the change is within tolerance under one reading of\n    M2. The Discussion's \"modal\" makes reading (c) of M2 the closest to the text, but all three\n    are shown.\n- id: figs2b-quinpirole-larger-than-d1\n  statement: Quinpirole raises SNr spike rate more than the D1R antagonist does.\n  source: Figure S2B; Results, Dopamine enhanced tonic GABA release from dSPN terminals, paragraph 1\n  quote: Bath applied D2R agonist elevates SNr firing rate significantly more than bath applied D1R\n    antagonist. Unpaired T-test, n = 8 D2R / 12 D1R, p = 0.03.\n  statistics:\n  - test: unpaired t test\n    p: 0.03\n    n: 8 quinpirole and 12 SCH39166 neurons\n  criterion: Per cell, the fold change in rate (after over before, the axis of Fig. S2B) for the\n    cells of fig3a-quinpirole-increases-rate and figs2a-d1-antagonist-increases-rate. Reproduced\n    when a two-sided unpaired t test has P < 0.05 with the quinpirole fold change higher. The\n    paper does not say whether variances were pooled; Student's test is the main reading, as the\n    legend says \"Unpaired T-test\" where others say Welch's, and Welch's test is a variant.\n  depends_on:\n  - fig3a-quinpirole-increases-rate\n  - figs2a-d1-antagonist-increases-rate\n- id: fig5ab-aldh1a1-dendrites-in-snr\n  statement: The dendrites of ALDH1A1+ dopaminergic neurons course through much of the dorsoventral\n    extent of the SNr, in rostral and caudal sections.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    1; Figure 5A and 5B\n  quote: In both rostral and caudal regions, the dendrites of ALDH1A1+ dopaminergic neurons coursed\n    through much of dorsoventral extent of SNr\n  criterion: The paper shows this with images of Aldh1a1-2A-iCre/DAT-2A-Flpo mice injected with\n    Con/Fon-YFP and Coff/Fon-mCherry and gives no measure. Reproduced when, in rostral and caudal\n    coronal sections, YFP-labelled processes are found across the dorsal, middle and ventral\n    thirds of the SNr outline. Not testable when the dataset holds no such images.\n- id: fig5d-shrna-higher-rate\n  statement: SNr neurons from mice with ALDH1A1 knocked down in the SNc by shRNA fire faster than\n    control SNr neurons.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    2; Figure 5D\n  quote: In ex vivo, cell-attached recordings from SNr neurons, the basal spiking rate was\n    significantly higher than in controls (P < 0.001 and n = 18 control/15 shRNA)\n  statistics:\n  - test: Welch's t test\n    p: 0.001\n    p_relation: \"<\"\n    n: 18 control and 15 shRNA neurons\n  criterion: Basal rate per cell (M1, the control condition). Which control cells form the 18 is\n    not said; readings (a) the control cells recorded alongside the shRNA experiments, as the\n    dataset labels them; (b) the same 18 control cells as Fig. 5F, which also gives n = 18\n    control. Reproduced when, under one reading, a two-sided Welch's t test has P < 0.05 with the\n    shRNA cells faster.\n- id: fig5e-shrna-gabazine-no-change\n  statement: In SNr neurons from ALDH1A1 shRNA mice, gabazine does not significantly change the\n    basal spike rate.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    2; Figure 5E\n  quote: Moreover, bath application of gabazine did not significantly change the basal spiking rate\n    of SNr neurons from ALDH1A1 shRNA treated mice (P = 0.05 and n = 15)\n  statistics:\n  - test: paired t test\n    p: 0.05\n    n: 15 neurons\n  criterion: A claim of absence (M6). Rate before and after gabazine in shRNA slices (M1, M4).\n    Reproduced when a two-sided paired t test gives P >= 0.05. The paper's own P sits at the\n    threshold, so the change in rate and its P are reported in full.\n- id: fig5f-aldh-inhibitors-higher-rate\n  statement: SNr neurons in slices pretreated with the aldehyde dehydrogenase inhibitors DEAB or\n    disulfiram fire faster than control neurons.\n  source: Figure 5F\n  quote: Example trace and summary data of SNr spiking from control neurons and neurons pretreated\n    with ALDH1A1 antagonists DEAB or disulfiram. Welch's t test, n = 18 control/18 blocked, P <\n    0.01.\n  statistics:\n  - test: Welch's t test\n    p: 0.01\n    p_relation: \"<\"\n    n: 18 control and 18 inhibitor-treated neurons\n  criterion: Basal rate per cell (M1) in control slices and in slices with DEAB or disulfiram,\n    pooled, as the legend pools them; the 18 treated cells are more than the 5 and 5 of Fig. 5G\n    and 5H, so all cells recorded in either inhibitor are used. Reproduced when a two-sided\n    Welch's t test has P < 0.05 with the treated cells faster.\n- id: fig5g-disulfiram-blocks-gabazine\n  statement: In slices treated with disulfiram (10 uM), gabazine no longer changes SNr spike rate.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    3; Figure 5G\n  quote: Disulfiram blocked the effect of gabazine (P = 0.40 and n = 5)\n  statistics:\n  - test: paired t test\n    p: 0.4\n    n: 5 neurons\n  criterion: A claim of absence (M6). Rate before and after gabazine in disulfiram (M1, M4).\n    Reproduced when a two-sided paired t test gives P >= 0.05.\n- id: fig5h-deab-blocks-gabazine\n  statement: In slices treated with DEAB (10 uM), gabazine does not change SNr spike rate.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    3; Figure 5H\n  quote: As with disulfiram, gabazine had no effect on DEAB-exposed SNr neurons (P = 0.10 and n =\n    5)\n  statistics:\n  - test: paired t test\n    p: 0.1\n    n: 5 neurons\n  criterion: A claim of absence (M6). Rate before and after gabazine in DEAB (M1, M4). Reproduced\n    when a two-sided paired t test gives P >= 0.05.\n- id: fig6a-rasagiline-blocks-gabazine\n  statement: In slices incubated in the MAO-B inhibitor rasagiline (10 uM), gabazine has no\n    discernible effect on SNr spike rate.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    4; Figure 6A\n  quote: Incubating brain slices in the irreversible MAO-B antagonist rasagiline (10 μM) blunted any\n    discernible effect of gabazine on the spiking rate of SNr neurons (P = 0.23 and n = 9)\n  statistics:\n  - test: paired t test\n    p: 0.23\n    n: 9 neurons\n  criterion: A claim of absence (M6). Rate before and after gabazine in rasagiline (M1, M4).\n    Reproduced when a two-sided paired t test gives P >= 0.05.\n- id: figs3-snc-gi-dreadd-slows-snc\n  statement: Activating Gi-DREADD in SNc dopaminergic neurons of DAT-Cre mice with CNO slows their\n    spiking, by 19% on average.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    5; Figure S3\n  quote: bath application of the DREADD activator CNO significantly slowed the spiking rate of SNc\n    dopaminergic neurons (mean reduction of 19%, P = 0.02 and n = 6)\n  statistics:\n  - test: not named\n    p: 0.02\n    n: 6 neurons\n  expected:\n  - quantity: mean reduction in SNc spike rate with CNO\n    value: 19\n    tolerance: 1.9\n    unit: \"%\"\n  criterion: SNc neurons, rate before and after CNO (M1, M4). The test is not named (M3, paired t\n    test main, Wilcoxon variant). Reproduced when the test has P < 0.05 with rates lower after\n    and the mean reduction is within tolerance under reading (a) or (b) of M2.\n- id: fig6c-snc-gi-dreadd-no-snr-change\n  statement: Slowing SNc dopaminergic neurons with Gi-DREADD does not increase SNr spike rate, so\n    activity-dependent vesicular release is not the route of GABA release.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    5; Figure 6C\n  quote: However, CNO application did not increase the spiking rate in SNr (P = 0.29 and n = 8)\n  statistics:\n  - test: not named\n    p: 0.29\n    n: 8 neurons\n  criterion: A claim of absence (M6). SNr rate before and after CNO in DAT-Cre mice with\n    Cre-dependent Gi-DREADD in SNc (M1, M4). The test is not named; it is judged on a two-sided\n    paired t test (M3), with the Wilcoxon signed-rank test shown as a variant. Reproduced when\n    the test gives P >= 0.05.\n  depends_on:\n  - figs3-snc-gi-dreadd-slows-snc\n- id: fig6d-gat1-enriched-aldh1a1\n  statement: In Dopabase, GAT-1 expression is enriched in ALDH1A1+ dopaminergic neurons, with\n    roughly one-third of ventral SNc dopaminergic neurons in clusters 4 and 10 expressing both.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    6; Figure 6D\n  quote: Queries of Dopabase (36) revealed that GAT-1 expression was enriched in ALDH1A1+\n    dopaminergic neurons (Fig. 6D); roughly one-third of the ventral SNc dopaminergic neurons in\n    clusters 4 and 10 had detectable levels of both transcripts.\n  data: elsewhere\n  where: Dopabase, from Gaertner et al. 2025, eLife 13, RP101035 (ref. 36); no version or accession\n    is given in the paper\n  expected:\n  - quantity: fraction of ventral SNc dopaminergic neurons in clusters 4 and 10 with both Slc6a1\n      and Aldh1a1 detected\n    value: 33\n    tolerance: 3.3\n    unit: \"%\"\n  criterion: Detection threshold and cluster labels as Dopabase defines them; \"detectable\" read as\n    a count above zero. Reproduced when the fraction is within tolerance and Slc6a1 expression is\n    higher in Aldh1a1-expressing cells than in other dopaminergic cells.\n- id: fig6e-nnc711-blocks-gabazine\n  statement: In slices incubated in the GAT-1 antagonist NNC-711, gabazine fails to increase SNr\n    spike rate, so GABA is released through GAT-1.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    6; Figure 6E\n  quote: In the presence of NNC-711, bath application of gabazine failed to increase SNr firing\n    rate (P = 0.32 and n = 6)\n  statistics:\n  - test: paired t test\n    p: 0.32\n    n: 6 neurons\n  criterion: A claim of absence (M6). Rate before and after gabazine in NNC-711 (M1, M4); the\n    NNC-711 concentration is not given. Reproduced when a two-sided paired t test gives P >= 0.05.\n- id: figs8-low-glucose-blocks-gabazine\n  statement: With extracellular glucose lowered to 2.5 mM, gabazine does not significantly increase\n    SNr spike rate.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    7; Figure S8A\n  quote: When extracellular glucose concentration is lowered to 2.5 mM, gabazine does not\n    significantly increase SNr spiking. Paired T-test, n = 8, p = 0.10 .\n  statistics:\n  - test: paired t test\n    p: 0.1\n    n: 8 neurons\n  criterion: A claim of absence (M6). Rate before and after gabazine in 2.5 mM glucose aCSF (M1,\n    M4). Reproduced when a two-sided paired t test gives P >= 0.05.\n- id: figs9c-vigabatrin-lowers-perceval\n  statement: The GABA-T inhibitor vigabatrin lowers the PercevalHR ATP/ADP ratio in SNc\n    dopaminergic neurons.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    8; Figure S9B and S9C\n  quote: Bath application of the GABA-T inhibitor Vigabatrin (44) decreased the PercevalHR ratio,\n    consistent with a drop in mitochondrial ATP generation\n  statistics:\n  - test: Wilcoxon matched pairs signed rank test\n    p: 0.002\n    n: 10 neurons from 10 mice (7 wild type with a TH-promoter probe, 3 Aldh1a1-cre with a\n      Cre-dependent probe, pooled)\n  criterion: Two-photon PercevalHR imaging; F950/F820 ratio per time point after background\n    subtraction from a cytosolic region (Methods, 2PLSM optical workstation and PercevalHR\n    experiments), in 1.5 mM glucose aCSF. Per cell, the baseline ratio (the stable baseline of\n    four acquisitions) against the ratio in vigabatrin 20 uM (Fig. S9 legend); which vigabatrin\n    acquisitions are used is open, readings (a) the last acquisition before oligomycin; (b) the\n    mean of all vigabatrin acquisitions. Reproduced when, under one reading, a two-sided Wilcoxon\n    signed-rank test has P < 0.05 with the ratio lower in vigabatrin.\n- id: figs9de-vigabatrin-lowers-oxphos\n  statement: Vigabatrin lowers the oligomycin-sensitive (OXPHOS) contribution to cytosolic ATP in\n    SNc dopaminergic neurons and leaves the 2-DG-sensitive (glycolytic) contribution unchanged.\n  source: Results, SNc dopaminergic neurons directly contributed to tonic GABA release, paragraph\n    8; Figure S9D and S9E\n  quote: Consistent with engagement of the GABA shunt, GABA-T inhibition selectively decreased the\n    mitochondrial contribution to maintenance of cytosolic ATP levels.\n  statistics:\n  - about: oligomycin-sensitive contribution, control against vigabatrin\n    test: Mann-Whitney test\n    p: 0.0017\n    n: 6 control cells from 5 mice and 10 vigabatrin cells from 10 mice\n  - about: 2-DG-sensitive contribution, control against vigabatrin\n    test: Mann-Whitney test\n    p: 0.367\n    n: 6 control cells from 5 mice and 10 vigabatrin cells from 10 mice\n  criterion: Percent oligomycin-sensitive and percent 2-DG-sensitive contributions to the\n    PercevalHR ratio (Fig. S9D, E axes), computed as the drop in ratio after oligomycin 10 uM and\n    after 2-DG 3.5 mM, each as a percent of the ratio before that step (Methods; Fig. S9 legend);\n    the paper does not give the formula, and the other reading, each drop as a percent of the\n    baseline ratio, is shown. Reproduced when, under one reading, a two-sided Mann-Whitney test\n    gives P < 0.05 for the oligomycin-sensitive part (lower in vigabatrin) and P >= 0.05 for the\n    2-DG-sensitive part.\n- id: fig7a-d2r-in-snr-astrocytes\n  statement: D2R transcripts colocalise with the astrocyte marker S100B in about a third of SNr\n    astrocytes, 37% in lateral and 32% in medial SNr.\n  source: Results, Astrocytic D2Rs promote GABA uptake through GAT-3 transporters, paragraph 1;\n    Figure 7A; Figure S7\n  quote: The two were colocalized in a significant fraction of both lateral and medial SNr\n    astrocytes (lateral SNr... mean ratio of D2R-positive astrocytes = 37 ± 4%; medial SNr... mean\n    ratio of D2R-positive astrocytes = 32 ± 4%; n = 3 mice/516 astrocytes)\n  expected:\n  - quantity: D2R-positive fraction of S100B astrocytes, lateral SNr\n    value: 37\n    tolerance: 4\n    unit: \"%\"\n  - quantity: D2R-positive fraction of S100B astrocytes, medial SNr\n    value: 32\n    tolerance: 4\n    unit: \"%\"\n  - quantity: D2R-positive fraction of S100B astrocytes, overall (Fig. S7, mean)\n    value: 35\n    tolerance: 15\n    unit: \"%\"\n  criterion: RNAscope for D2R and S100B in SNr (Fig. 7A, Fig. S7). Tolerances are the paper's own\n    spread (the plus or minus 4% the text gives, and the SD of 15% Fig. S7 gives). The ratio is\n    per image or section and averaged (Fig. 7A plots many points for 3 mice); the paper does not\n    give the rule for calling an astrocyte D2R-positive, which the attempt states. Reproduced\n    when the three fractions are within tolerance.\n- id: fig7d-astrocyte-gi-increases-rate\n  statement: Activating Gi-DREADD in SNr astrocytes with CNO raises SNr spike rate, by 28% on\n    average.\n  source: Results, Astrocytic D2Rs promote GABA uptake through GAT-3 transporters, paragraph 1;\n    Figure 7C and 7D\n  quote: Bath application of CNO to activate hM4Di significantly increased the spiking rate of SNr\n    neurons (28% mean increase, P < 0.01 and n = 10)\n  statistics:\n  - test: not named\n    p: 0.01\n    p_relation: \"<\"\n    n: 10 neurons\n  expected:\n  - quantity: mean increase in SNr spike rate with CNO, GFAP-hM4Di\n    value: 28\n    tolerance: 2.8\n    unit: \"%\"\n  criterion: Rate before and after CNO in slices with GFAP-hM4Di in SNr (M1, M4). The test is not\n    named (M3, paired t test main, Wilcoxon variant). Reproduced when the test has P < 0.05 with\n    rates higher after, and the mean increase is within tolerance under reading (a) or (b) of M2.\n- id: fig7e-gabazine-occludes-astrocyte-gi\n  statement: When gabazine is applied first, CNO activation of astrocytic Gi-DREADD no longer\n    increases SNr spike rate.\n  source: Results, Astrocytic D2Rs promote GABA uptake through GAT-3 transporters, paragraph 1;\n    Figure 7E\n  quote: The CNO effect on SNr spiking rate was occluded by application of gabazine, directly\n    implicating astrocytic regulation of GABA (P = 0.10 and n = 11)\n  statistics:\n  - test: not named\n    p: 0.1\n    n: 11 neurons\n  criterion: A claim of absence (M6). Rate in gabazine before and after CNO (M1, M4), GFAP-hM4Di\n    slices. Judged on a two-sided paired t test (M3), Wilcoxon as a variant. Reproduced when the\n    test gives P >= 0.05.\n- id: fig7f-snap5114-decreases-rate\n  statement: The GAT-3 antagonist SNAP-5114 (20 uM) lowers SNr spike rate, by 23%.\n  source: Results, Astrocytic D2Rs promote GABA uptake through GAT-3 transporters, paragraph 2;\n    Figure 7F\n  quote: The GAT-3–selective antagonist significantly decreased SNr firing rate (23% decrease, P =\n    0.02 and n = 19)\n  statistics:\n  - test: paired t test\n    p: 0.02\n    n: 19 neurons\n  expected:\n  - quantity: decrease in SNr spike rate with SNAP-5114\n    value: 23\n    tolerance: 2.3\n    unit: \"%\"\n  criterion: Rate before and after SNAP-5114 (M1, M4). Reproduced when a two-sided paired t test\n    has P < 0.05 with rates lower after, and the decrease is within tolerance under one reading\n    of M2.\n- id: fig7f-snap5114-occludes-quinpirole\n  statement: In the presence of SNAP-5114, quinpirole has no effect on SNr spike rate.\n  source: Results, Astrocytic D2Rs promote GABA uptake through GAT-3 transporters, paragraph 2;\n    Figure 7F\n  quote: In the presence of the GAT-3 antagonist, bath application of quinpirole had no effect on\n    SNr spiking rate (P = 0.27)\n  statistics:\n  - test: Welch's t test\n    p: 0.27\n  criterion: A claim of absence (M6). Rates in SNAP-5114 and in SNAP-5114 with quinpirole (M1),\n    from the cells of fig7f-snap5114-decreases-rate that received quinpirole; the paper gives no n\n    for this test. Judged on the paper's test as written, a two-sided Welch's t test of the two\n    sets of rates as unpaired groups; a paired t test is shown as a variant. Reproduced when the\n    Welch's test gives P >= 0.05.\n  depends_on:\n  - fig7f-snap5114-decreases-rate\n- id: fig7h-nnc711-increases-rate\n  statement: The GAT-1 antagonist NNC-711 alone raises SNr spike rate, by 36%.\n  source: Results, Astrocytic D2Rs promote GABA uptake through GAT-3 transporters, paragraph 3;\n    Figure 7G and 7H\n  quote: Indeed, the bath application of GAT-1 antagonist NNC-711 alone upon SNr neurons\n    significantly increased mean firing rate (36% increase, P < 0.01 and n = 6)\n  statistics:\n  - test: not named\n    p: 0.01\n    p_relation: \"<\"\n    n: 6 neurons\n  expected:\n  - quantity: increase in SNr mean firing rate with NNC-711\n    value: 36\n    tolerance: 3.6\n    unit: \"%\"\n  criterion: Rate before and after NNC-711 (M1, M4). The test is not named (M3, paired t test\n    main, Wilcoxon variant). Reproduced when the test has P < 0.05 with rates higher after, and\n    the increase is within tolerance under reading (a) or (b) of M2 (\"mean firing rate\").\n- id: figs4d-room-temperature-gabazine-no-change\n  statement: At room temperature (20 to 22 C), gabazine does not change SNr spike rate.\n  source: Results, Astrocytic D2Rs promote GABA uptake through GAT-3 transporters, paragraph 3;\n    Figure S4D\n  quote: lowering the temperature of the slice to 20° to 22°C (from 32°C) blunted the ability of\n    gabazine to accelerate SNr spiking rate (P = 0.05 and n = 7)\n  statistics:\n  - test: not named\n    p: 0.05\n    n: 7 neurons\n  criterion: A claim of absence (M6). Rate before and after gabazine at 20 to 22 C (M1, M4).\n    Judged on a two-sided paired t test (M3), Wilcoxon as a variant. Reproduced when the test\n    gives P >= 0.05. The paper's P sits at the threshold, so the change and its P are reported\n    in full.\n- id: figs4e-temperature-reduces-gabazine-effect\n  statement: The fold change in SNr spike rate with gabazine is smaller at room temperature than at\n    physiological temperature.\n  source: Figure S4E\n  quote: Summary data comparison of the SNr neuron firing rate fold change following gabazine\n    treatment at physiological (30oC) and room temperature (20oC) Mann- Whitney test, n = 44/7, p <\n    0.0001.\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 44 physiological-temperature and 7 room-temperature neurons\n  criterion: Per cell, gabazine fold change (after over before, M1, M4) for the cells of\n    fig3b-gabazine-increases-rate and figs4d-room-temperature-gabazine-no-change. The legend says\n    30 C, the Results and Methods 32 to 33 C; the physiological group is the cells recorded at the\n    standard bath temperature. Reproduced when a two-sided Mann-Whitney test gives P < 0.05 with\n    the room-temperature fold changes lower.\n  depends_on:\n  - fig3b-gabazine-increases-rate\n  - figs4d-room-temperature-gabazine-no-change\n- id: figs6-aldh1a1-ko-da-release-unchanged\n  statement: Deleting ALDH1A1 does not change electrically evoked dopamine release in striatum,\n    measured by fast-scan cyclic voltammetry, for single pulses, 5-pulse trains or the paired-pulse\n    ratio.\n  source: Figure S6\n  quote: Deletion of ALDH1A1 does not affect basal dopamine release.\n  criterion: A claim of absence. FSCV in coronal striatal slices as in the Methods (Fast-scan\n    cyclic voltammetry), peak DA concentration for 1 pulse (first of the pair) and for 5 pulses at\n    25 Hz, and the paired-pulse ratio at 15 s; WT against Aldh1a1 KO (Fig. S6B labels), with\n    recording sites as points. The paper names no test (the panels say n.s.) and does not\n    describe the KO mice; judged on a two-sided unpaired t test at P < 0.05 (the paper's\n    between-group test in Fig. S2B), with Mann-Whitney as a variant. Reproduced when none of the\n    three comparisons gives P < 0.05.\n- id: figs5-gat-expression-in-snc\n  statement: In SNc dopaminergic neurons, Slc6a1 (GAT-1) has the most reads among the GAT genes,\n    followed by Slc6a12, with little Slc6a11 (GAT-3) and no Slc6a13.\n  source: Figure S5\n  quote: Table of GAT (1-4) expression in SNC dopaminergic cells.\n  data: elsewhere\n  where: Gonzalez-Rodriguez et al. 2021, Nature, doi:10.1038/s41586-021-04059-0 (as cited in the\n    Figure S5 legend); no accession is given\n  expected:\n  - quantity: Slc6a1 reads\n    value: 2118.494118\n    tolerance: 211.8\n  - quantity: Slc6a12 reads\n    value: 1444.866233\n    tolerance: 144.5\n  - quantity: Slc6a11 reads\n    value: 13.86342026\n    tolerance: 1.39\n  - quantity: Slc6a13 reads\n    value: 0\n    tolerance: 0\n  criterion: The numbers are in the table only; the quote is its title. The ordering is read from\n    the table. Reproduced when the four values are within tolerance in the cited data, with the\n    normalisation that source uses.\n"
}
```

```
File created successfully at: claims/simmons-2026.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/simmons-2026.yaml paper/10.1126-sciadv.adq8840.txt; grep -n "—\|rather" claims/simmons-2026.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 40,140p tools/claims_check.py
```

```
def flattenings(raw: str) -> list[str]:
    """The text with inline tags removed, with every tag as a space, and both without spaces."""
    tight = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", re.sub(INLINE, "", raw, flags=re.I)))
    loose = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", raw))
    return [tight, loose, tight.replace(" ", ""), loose.replace(" ", "")]


def quote_found(quote: str, texts: list[str]) -> bool:
    fragments = [f for f in (norm(x).strip(" .,;") for x in quote.split("...")) if f]
    for text in texts:
        frags = fragments if " " in text else [f.replace(" ", "") for f in fragments]
        pos = 0
        for f in frags:
            i = text.find(f, pos)
            if i < 0:
                break
            pos = i + len(f)
        else:
            return True
    return False
[... 52 more lines not kept]
```

**Agent**

Most failures are line-end hyphens the text file kept (e.g. "modula-/tion"). I'll locate each break and cut the quotes around it.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import sys,yaml,re
sys.path.insert(0,'tools')
from claims_check import norm, flattenings
t=flattenings(open('paper/10.1126-sciadv.adq8840.txt').read())[0]
d=yaml.safe_load(open('claims/simmons-2026.yaml'))
for c in d['claims']:
    q=c.get('quote')
    if not q: continue
    for f in [norm(x).strip(' .,;') for x in q.split('...')]:
        if f in t: continue
        # find longest prefix found
        words=f.split(' '); k=len(words)
        while k>0 and ' '.join(words[:k]) not in t: k-=1
        print(c['id'],'| ok up to:',' '.join(words[max(0,k-3):k]),'| fails at:',' '.join(words[k:k+4]))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='claims/simmons-2026.yaml'
s=open(p).read()
R=[
("locus of the modulation, the paired-pulse","locus of the ... the paired-pulse"),
("quote: As expected, quinpirole attenuated","quote: quinpirole attenuated"),
("quote: Initially, this stimulation","quote: this stimulation"),
("experiments was the elevation in the basal","experiments was the ... in the basal"),
("quote: Bath application of gabazine (10 μM) increased the basal spiking rate of SNr neurons\n    recorded","quote: gabazine (10 μM) increased the basal spiking rate of SNr ...\n    recorded"),
("(CNO) reduced the amplitude of\n    electrically","(CNO) reduced the ... of\n    electrically"),
("similar in magnitude to that","similar in ... to that"),
("In these slices, bath application of the DREADD","In these slices, bath ... of the DREADD"),
("regions, the dendrites of ALDH1A1+","regions, the ... of ALDH1A1+"),
("MAO-B antagonist rasagiline (10 μM)","MAO-B antagonist ... (10 μM)"),
("did not increase the spiking rate in SNr","did not increase the ... rate in SNr"),
("(Fig. 6D); roughly one-third","(Fig. 6D) ... one-third"),
("consistent with a drop in mitochondrial ATP generation","consistent with a drop in mitochondrial ATP"),
("quote: Consistent with engagement of the GABA shunt, GABA-T inhibition selectively decreased","quote: with engagement of the GABA shunt, GABA-T inhibition ... decreased"),
("spiking rate of SNr\n    neurons (28% mean","spiking rate of SNr\n    ... (28% mean"),
("occluded by application of gabazine, directly","occluded by application of ... directly"),
("no effect on\n    SNr spiking rate (P = 0.27)","no effect on\n    SNr ... rate (P = 0.27)"),
("quote: lowering the temperature of the slice","quote: lowering the ... of the slice"),
]
for a,b in R:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w').write(s)
E
python tools/claims_check.py claims/simmons-2026.yaml paper/10.1126-sciadv.adq8840.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All quotes pass. Last, a check for colon-space in plain scalars, em dashes and "rather".

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/simmons-2026.yaml; grep -nv "^\s*#" claims/simmons-2026.yaml | grep -E "^[0-9]+:\s+[^#]*\S: " | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head; git status --short claims/
```

```
?? claims/simmons-2026.yaml
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/simmons-2026.yaml'))['claims']
print(len(d),sum('statistics' in c for c in d),sum('criterion' in c for c in d),sum('expected' in c for c in d),[c['id'] for c in d if c.get('data')=='elsewhere'])"
```

```
38 31 38 12 ['fig6d-gat1-enriched-aldh1a1', 'figs5-gat-expression-in-snc']
```

**Agent**

I wrote `claims/simmons-2026.yaml`, and the quote checker passes it: 38 claims, 38 quotes, 36 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record (Science Advances, 9 September 2026) with full Results, Methods and legends, plus the supplement (Figs. S1 to S9). I opened PDF pages for Figs. 2 to 7 and S6 to read panels. Nothing the claims need was missing.

**Code read.** The code deposit (doi:10.5281/zenodo.10855006, now record 17297995) is one Mathematica notebook, "Code Sample.nb". It computes:
- spike rate per episode as spike count divided by episode length;
- a cell's rate as the median over a "stable" window that is chosen by eye;
- a PSTH.

Every window, bin and dropped episode in it is a placeholder. Spikes were detected in Clampfit, with no settings given anywhere.

**The file.**
- All 38 claims have a quote and a criterion; 31 have statistics and 12 have expected values.
- 15 are claims that a drug had no effect, each judged on the paper's own test.
- Two use outside data (`data: elsewhere`): Fig. 6D uses Dopabase, and Fig. S5 is a table from Gonzalez-Rodriguez et al. 2021.
- The opening comment names the paper's raw-data deposit on Zenodo (doi:10.5281/zenodo.10850896), but no claim's `data` field points to it.

**Details left open, with the readings named:**
- **Stable window (M1):** (a) all episodes of each condition; (b) for a drug, episodes from 6 min after application starts, which is when the Fig. 7G time courses level off.
- **Percent changes (M2):** (a) mean of per-cell changes; (b) change in group means; (c) median of per-cell changes. Only (a) and (b) where the paper says "mean".
- **Sidedness of tests:** not stated. Two-sided is used (the Prism default), with one-sided shown as a variant.
- **Unnamed tests (Figs. 6C, 7D, 7E, 7H, S3, S4D):** paired t test, with Wilcoxon as a variant.
- **Paired-pulse ratio (Fig. 1E):** the second peak measured either from the baseline before the first pulse, or from the current just before the second pulse.
- **IPSC amplitude (Figs. 1C, 4A):** not defined; peak from the pre-stimulus baseline is used and stated as a standard choice.
- **Fig. 2C percent inhibition:** basal rate from 0 to 2 s and train rate from 2 to 4 s, read from the figure; the PSTH value is the main one and a per-sweep median is a variant.
- **Fig. 2B waning:** the paper reports no test; I fixed 0.5-s windows at the start and end of the train.
- **Fig. 5D control group:** either the cells recorded alongside the shRNA experiments, or the same 18 control cells as Fig. 5F.
- **Fig. S2B test:** Student's unpaired t test, with Welch's as a variant.
- **Fig. 7F, quinpirole in SNAP-5114:** judged on Welch's test as the paper wrote it (an unpaired test on before and after values), with a paired t test as a variant.
- **Fig. S9:** which vigabatrin acquisitions count, and how the percent oligomycin- and 2-DG-sensitive parts are computed.
- **Fig. 4A "similar magnitude":** the paper gives no measure, so I fixed a margin of 10 percentage points.
- **Spike detection settings:** given nowhere.

**Where the text and the legends disagree** (both values are recorded, and a claim holds if the result matches either):
- Fig. 3B: n = 10 in the text, 45 in the legend.
- Fig. 3D: P = 0.13 in the text, 0.06 in the legend.
- Fig. 4A: P = 0.02 in the text, P < 0.01 in the legend.
- Fig. 4B: P = 0.19 in the text, 0.16 in the legend.
- Fig. S4E: the legend says 30 °C, the Methods say 32 to 33 °C.

**Missing from the paper:**
- Concentrations for NPPB, NNC-711 and CNO.
- The n for the Fig. 7F quinpirole test.
- How the Aldh1a1 KO mice in Fig. S6 were made, and which test was used there (the panels only say n.s.).
- The rule for calling an astrocyte D2R-positive (Fig. 7A).
- An accession or version for Dopabase and for the Fig. S5 source.

Two of the paper's P values sit right at the 0.05 threshold (Fig. 5E and S4D), so the size of each change is to be reported in full. The dandiset lists only voltage-clamp series, so the imaging, RNAscope and FSCV claims may not be testable on it; finding out is the author's job.

## End of run

38 turns, 6 minutes, $2.19 at API prices, result: success.
