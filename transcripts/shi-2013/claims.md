# shi-2013 · claims · run 42662922518

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,192p docs/protocol.md; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat papers/datasets/shi-2013.yaml; head -80 claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00223.2012.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,60p paper/ppc-1.data-description.txt; sed -n 1,80p tools/claims_check.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -l "archive: crcns" claims/*.yaml | head -3
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
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"; head -40 claims/deweese-2004.yaml
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1152-jn.00223.2012.pdf')
for i in [2,3,4,5]:
    d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
print('ok')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm mutool; python -c "import pypdfium2" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
```

**Agent**

Let me try reading the PDF directly for the garbled signs.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00223.2012.pdf",
 "pages": "3-5"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import pypdf; print(pypdf.__version__)" 2>&1; python -c "import pdfminer; print('pdfminer')" 2>&1; python - <<'E'
import re,zlib
b=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
for m in re.finditer(rb'/Differences\s*\[(.*?)\]',b,re.S): print(m.group(1)[:400])
for m in re.finditer(rb'/BaseFont\s*/(\S+)',b): print(m.group(1))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'E'
import re,zlib
b=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
out=[]
for m in re.finditer(rb'stream\r?\n(.*?)endstream',b,re.S):
    try: out.append(zlib.decompress(m.group(1)))
    except Exception: pass
print(len(out))
allb=b+b''.join(out)
for m in set(re.findall(rb'/BaseFont\s*/(\S+?)[/\s>]',allb)): print(m)
for m in re.finditer(rb'/Differences\s*\[(.*?)\]',allb,re.S): print(m.group(1)[:300])
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'E' > $TMPDIR/pdftext.txt; wc -c $TMPDIR/pdftext.txt
import re,zlib
b=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
objs={}
for m in re.finditer(rb'(\d+) 0 obj(.*?)endobj',b,re.S):
    objs[int(m.group(1))]=m.group(2)
def stream(o):
    m=re.search(rb'stream\r?\n(.*?)endstream',o,re.S)
    try: return zlib.decompress(m.group(1))
    except: return None
# font objects: map obj number -> (basefont, differences)
fontinfo={}
for n,o in objs.items():
    if b'/Type /Font' in o or b'/Type/Font' in o:
        bf=re.search(rb'/BaseFont\s*/(\S+?)[/\s>]',o)
        enc=re.search(rb'/Encoding\s+(\d+) 0 R',o)
        diff=None
        d=re.search(rb'/Differences\s*\[(.*?)\]',o,re.S)
        if enc and enc.group(1) and int(enc.group(1)) in objs:
            d=re.search(rb'/Differences\s*\[(.*?)\]',objs[int(enc.group(1))],re.S)
        if d:
            toks=d.group(1).split(); code=None; diff={}
            for t in toks:
                if t[:1]==b'/': diff[code]=t[1:].decode(); code+=1
                else: code=int(t)
        fontinfo[n]=(bf.group(1).decode() if bf else '?',diff)
names={'H11005':'=','H11021':'<','H11022':'>','H11006':'±','H11002':'−','H11003':'×','H11011':'~','H9024':'Ω','H9268':'σ','H9262':'μ','H11341':'|','minus':'−'}
# pages
for n,o in sorted(objs.items()):
    if re.search(rb'/Type\s*/Page[^s]',o):
        res=o
        r=re.search(rb'/Resources\s+(\d+) 0 R',o)
        if r: res=objs[int(r.group(1))]
        fm={}
        f=re.search(rb'/Font\s*<<(.*?)>>',res,re.S)
        if not f:
            f2=re.search(rb'/Font\s+(\d+) 0 R',res)
            if f2: f=re.search(rb'<<(.*)>>',objs[int(f2.group(1))],re.S)
        for k,v in re.findall(rb'/(\S+?)\s+(\d+) 0 R',f.group(1)): fm[k.decode()]=fontinfo.get(int(v),('?',None))
        cs=re.findall(rb'/Contents\s*\[?([\d 0R\s]+)\]?',o)
        refs=[int(x) for x in re.findall(rb'(\d+) 0 R',cs[0])] if cs else []
        print('=== PAGE obj',n)
        for rf in refs:
            s=stream(objs[rf]) or b''
            cur=None;line=[]
            for t in re.finditer(rb'/(\S+)\s+[\d.]+\s+Tf|\((?:\\.|[^\\)])*\)|(T\*|Td|TD|Tm|ET)',s):
                if t.group(1): cur=fm.get(t.group(1).decode(),('?',None)); continue
                if t.group(2):
                    line.append(' '); continue
                raw=t.group(0)[1:-1]
                raw=re.sub(rb'\\([0-7]{1,3})',lambda m:bytes([int(m.group(1),8)]),raw)
                raw=re.sub(rb'\\(.)',rb'\1',raw)
                if cur and 'Math' in cur[0] or (cur and 'Greek' in cur[0]):
                    for c in raw:
                        nm=(cur[1] or {}).get(c,str(c)); line.append('{'+names.get(nm,nm)+'}')
                else: line.append(raw.decode('latin1'))
            print(''.join(line))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'E' > $TMPDIR/pdftext.txt; wc -c $TMPDIR/pdftext.txt; grep -o "/[A-Za-z0-9]* [0-9.]* Tf" $TMPDIR/raw.txt 2>/dev/null | sort | uniq -c | head
import re,zlib
b=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
for m in re.finditer(rb'stream\r?\n(.*?)endstream',b,re.S):
    try: s=zlib.decompress(m.group(1))
    except: continue
    if b'BT' not in s or b'Tf' not in s: 
        if b'/Font' in s or b'Differences' in s or b'BaseFont' in s: print('OBJSTREAM', s[:3000].decode('latin1'))
        continue
    cur='';line=[]
    for t in re.finditer(rb'/(\S+)\s+[\d.]+\s+Tf|\((?:\\.|[^\\)])*\)|(T\*|Td|TD|Tm|ET)',s):
        if t.group(1): cur=t.group(1).decode(); continue
        if t.group(2): line.append(' '); continue
        raw=t.group(0)[1:-1]
        raw=re.sub(rb'\\([0-7]{1,3})',lambda m:bytes([int(m.group(1),8)]),raw)
        raw=re.sub(rb'\\(.)',rb'\1',raw)
        if cur.startswith('F') and cur not in ('F1','F2'):
            line.append('{'+cur+':'+','.join(str(c) for c in raw)+'}' if all(c<32 for c in raw) else raw.decode('latin1'))
        else: line.append(raw.decode('latin1'))
    print('=== STREAM'); print(''.join(line))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -c "=== STREAM" pdftext.txt; grep -o "{[^}]*}" pdftext.txt | sort | uniq -c | sort -rn | head -30; grep -n "OBJSTREAM" pdftext.txt | head
```

```
29
    107 {F4:5}
     51 {F4:6}
     16 {F4:2}
      7 {F5:2}
      7 {F4:3}
      5 {F4:1}
      4 {F5:}
      4 {F5:6}
      3 {F8:}
      3 {F5:5}
      3 {F5:3}
      3 {F4:}
      2 {F8:3}
      2 {F8:2}
      2 {F8:1}
      2 {F5:7}
      2 {F5:4}
      1 {F5:1}
      1 {F4:8}
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -o "<</Type /Font[^>]*MathematicalPi-One[^>]*>>\|<</Type /Font[^>]*Universal-Greek[^>]*>>\|<</Type /Encoding /Differences \[[^]]*\] >>" pdftext.txt
```

```
<</Type /Encoding /Differences [1 /H20851 /H20852 /H20863 ] >>
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'E'
import re,zlib
b=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
for m in re.finditer(rb'stream\r?\n(.*?)endstream',b,re.S):
    try: s=zlib.decompress(m.group(1))
    except: continue
    if b'ObjStm' in m.group(0)[:0] or (b'BaseFont' in s and b'BT' not in s):
        hdr=s.split(b'<<',1)[0].split()
        pairs=list(zip(hdr[0::2],hdr[1::2]))
        first=s.index(b'<<')
        for i,(num,off) in enumerate(pairs):
            start=first+int(off); end=first+int(pairs[i+1][1]) if i+1<len(pairs) else len(s)
            body=s[start:end]
            if int(num) in (70,74,2428,99,96,102) or b'Differences' in body:
                print(num.decode(), body[:300].decode('latin1'))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'E'
import re
t=open('pdftext.txt',encoding='utf-8').read()
m4={'1':'~','2':'<','3':'=','4':'Ω','5':'±','6':'−','7':'×','8':'>'}
m5={'1':'σ','2':'=','3':'−','4':'×','5':'|','6':'μ','7':'θ'}
t=re.sub(r'\{F4:([\d,]*)\}',lambda m:''.join(m4.get(c,'?') for c in m.group(1).split(',') if c),t)
t=re.sub(r'\{F5:([\d,]*)\}',lambda m:''.join(m5.get(c,'?') for c in m.group(1).split(',') if c),t)
open('dec.txt','w').write(t)
E
grep -o ".\{60\}[<>=±~−].\{40\}" dec.txt | grep -v "^<<\|Type /" | head -120
```

```
urroundedeachreachtarget,andabehavioral windowwitharadiusof ~ 6.5¡ofvisualanglesurroundedthecentral Þ
redwithaone-factormultivariate analysisofvariance(MANOVA, P < 0.05).Variabilityalongthe horizontal( x
 )axeswerealsocompared betweenconditionswithLeveneÕstest( P < 0.05).Allanalyseswere conductedonpositi
utionalAnimalCareandUseCommit- tee.Single-cellrecordings( N = 343;219from monkeyX and124 from monkeyB
dextracellularly withvarnish-coatedtungstenmicroelectrodes( ~ 1-to2-M Ω imped- anceat1kHz).Singleacti
getlocationbysmoothingthespiketrainswithaGaussian kernel( σ = 50ms).Atthesingle-cellleveltheeffectsof
riodwere assessedwithatwo-factoranalysisofvariance(ANOVA, P < 0.05; factors:targetlocation,visualcond
basedpurelyonthe preferredlocationintheNVcondition): INDX 2 = {F8:1} (V pv − NV pnv )ÚNV pnv {F8:2} ×
erencesinFFbetweenconditionsweperformedapermutationtest ( P < 0.05).Thatis,werandomlyassignedpairsofs
etweencon - ditionswereassessedwiththeKruskal-Wallistest( P < 0.05). Atthepopulationlevel,wealsocompu
etweentheselattertwo datasetsweperformedapermutationtest( P < 0.05),usingthesame proceduredescribedab
opulationactivityonthattrial(Pougetet al.2000): P ( r | S ) = {F8:3} i = 1 n P ( r i | S ) = {F8:3} i
sofwhichdirectionmaximizedthelikelihood ofobserving r : θ r = argmax[ P ( r | S )]( 4 ) where θ r ist
ormancewasbootstrappedacross thecellswithinthepopulation( N = 200).Thepercentagesof correctlyandincor
ositiondataobtainedfromallbehavioralsessionsinone animal( N = 124sessions);theaveragecoordinatesofthe
s andtargets)withasigniÞcantdifferenceinmeanpositionwas 6.9 ± 1.5%(MANOVA, P < 0.05).Similarly,theave
nvari- abilityalongthehorizontal,vertical,anddepthaxeswere5 ± 1.9%,4.7 ± 1.6%,and6 ± 0.9%,respectivel
edbydifferencesinactivityacrosstargetsbetween approximately − 2and − 1.5s)aswellastunedpositional dis
ingthestaticholdingperiod indicatedamaineffectofposition( P < 0.05)butnoeffectof thevisualconditionsa
quired movementvector(mainand/orinteractioneffects;ANOVA, P < 
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -o "interaction( P.\{30\}\|INDX 1 .\{40\}\|.\{20\}Meredith.\{80\}\|.\{40\}inthe NV condition the.\{60\}" dec.txt | head
```

```
modal (NV)condition(MeredithandStein1986):  A B 3D Monitor Display Mirror  Workspace y z x  Off On Fixation 
INDX 1 = {F8:1} (V pnv − NV pnv )ÚNV pnv {F8:2}
INDX 1 ,whichisbasedpurelyonthe preferredlocati
interaction( P = 0.52; P = 0.64).Thusthisneu
INDX 1 ; Eq.1 )foralloftheneuronsrecordedinthis
INDX 1 wasnegative.Thepercentage ofcellswithneg
INDX 1 waslowestforthecellsshowninFig.4 B (77%)
INDX 1 wasleastnegative( − 13%).Incontrast,the 
INDX 1 appeartobeassociatedwithbothchangesintun
 31:6661Ð6673,2011. MeredithMA,SteinBE. Visual,auditory,andsomatosensoryconvergence oncellsinsuperiorcollicu
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 60,156p paper/ppc-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls tools/ | head -30; grep -rn "variants\|checks:" claims/deweese-2004.yaml | head -5; tail -30 claims/deweese-2004.yaml
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
migrate_paper_first.py
notify.py
[... 41 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/shi-2013.yaml",
 "content": "# Claims for Shi, Apker & Buneo (2013), J Neurophysiol 109:2097-2107, on CRCNS data set ppc-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),\n# with its Methods, Results, Discussion, Table 1 and the legends of Figures 1 to 6. The paper\n# has no supplement. It links no analysis code, so none was read. The PDF could not be\n# rendered here, and the extracted text prints the signs =, <, >, ~, plus/minus, minus and\n# times as a replacement character. They were read from the PDF's font encodings (the\n# Differences arrays of Universal-GreekwithMathPi and MathematicalPi-One). Every significance\n# statement prints \"P < 0.05\"; the example cell's vision and interaction effects are\n# \"P = 0.52; P = 0.64\"; values \"a +/- b\" are mean plus/minus spread; INDX1 means are -13% and\n# -31%, the tuning split -24% and -40%, INDX2 means -9%, -13% and -13%; Table 1 y values carry\n# a minus sign where the text shows the glyph; the Fig. 4 outliers are \"indexes > 1.5 times the\n# interquartile range\"; the sample sizes are \"N = 343\" cells and \"N = 200\" for the bootstrap.\n#\n# The paper writes \"(test, P < 0.05)\" both after significant results and after results it\n# calls not significant (correlations \"identical ... permutation test, P < 0.05\"; eye\n# positions \"neither ... differed ... P < 0.05\"). Read with the Methods, which give each test\n# as \"(test, P < 0.05)\", the bound is the threshold the test used. It is recorded as a\n# statistic only where the finding is a significant difference.\n#\n# Data the paper used. Two head-fixed rhesus monkeys (monkey X, monkey B) reached in a 3D\n# virtual environment, seeing the wrist as a green cursor, from a central start position to\n# one of eight targets in a frontal plane (0 to 315 degrees in 45 degree steps, 0 degrees\n# rightward, ipsilateral to the reaching arm), arranged in a rectangle 5 cm by 4 cm apart for\n# monkey X and a square 5 cm apart for monkey B. After target acquisition the target went off\n# (after 300 ms, X; 400 ms, B), a central yellow fixation point came on, and once it was\n# fixated a static holding period of 800 to 1,200 ms followed, with the arm held at the target\n# and the eyes at the centre. On half the trials the arm cursor stayed visible during the hold\n# (Vision, V) and on the others it was blanked (No Vision, NV). Five trials per target were\n# run; the decoder trains on four trials and tests on the fifth per target, so the five are\n# read here as five per target in each condition (80 trials a session). Analysis is of the\n# last 800 ms of the hold unless stated. Arm position was tracked at 250 Hz (Phoenix\n# Technologies), eye position at 120 Hz. 343 single neurons (219 monkey X, 124 monkey B) in\n# superficial area 5 of the SPL, one per session (Table 1 gives 219 and 124 sessions; the\n# Results give 343 sessions), isolated with a window discriminator (Plexon), spike times at\n# 2.5 kHz. Measured variables: spike times, trial events, arm endpoint position (x horizontal,\n# y vertical, z depth, cm) and eye position.\n#\n# The CRCNS data set, by its title and description, holds the sorted spikes and strobed event\n# codes of these sessions (Plexon and Matlab files, with an event code list and an analog file\n# per session), with some extra behavioural training files the description says were used only\n# for exploration. Whether it holds arm and eye position, and how V and NV trials are marked,\n# is the author's to find.\n#\n# Method details fixed by the paper, used throughout. Mean firing rate in the last 800 ms of\n# the hold. Single-cell effects by a two-factor ANOVA (target location by visual condition,\n# with interaction, P < 0.05). Preferred location is the target of maximal NV mean rate. FF is\n# the slope of spike count variance against spike count mean across cells, through the origin,\n# at the NV preferred location. Details the paper does not fix are named in each criterion.\nschema_version: 2\npaper: doi:10.1152/jn.00223.2012\nclaims:\n- id: behavior-mean-position-sessions\n  statement: Few sessions showed a significant difference in mean arm endpoint position between\n    V and NV at a target; the average percentage across animals and targets was 6.9 +/- 1.5%\n    (one-factor MANOVA, P < 0.05).\n  source: Results, Behavior, paragraph 1\n  quote: The average percentage of sessions (across animals and targets) with a significant\n    difference in mean position was 6.9\n  expected:\n  - quantity: percentage of sessions with a significant V against NV difference in mean endpoint\n      position, averaged across animals and targets\n    value: 6.9\n    tolerance: 1.5\n    unit: \"%\"\n  criterion: Method from Materials and Methods, Behavioral analysis. For each session and\n    target, the mean endpoint position (x, y, z) of each trial over the last 800 ms of the hold;\n    V trials against NV trials by a one-factor MANOVA at P < 0.05 (with two groups every MANOVA\n    statistic gives the same exact test). The tolerance is the paper's stated spread. Open, and\n    both readings are shown, (a) the mean of the 16 animal and target percentages, (b) the\n    percentage pooled over all session and target pairs. Reproduced when either reading is\n    within tolerance.\n- id: behavior-variability-sessions\n  statement: Few sessions showed a significant difference in endpoint variability between V and\n    NV; along the horizontal, vertical and depth axes the average percentages were 5 +/- 1.9%,\n    4.7 +/- 1.6% and 6 +/- 0.9% (Levene's test, P < 0.05).\n  source: Results, Behavior, paragraph 1\n  quote: Similarly, the average percentages of sessions with a significant difference in\n    variability along the horizontal, vertical, and depth axes were 5\n  expected:\n  - quantity: percentage of sessions with a significant variability difference, horizontal (x)\n    value: 5\n    tolerance: 1.9\n    unit: \"%\"\n  - quantity: percentage of sessions with a significant variability difference, vertical (y)\n    value: 4.7\n    tolerance: 1.6\n    unit: \"%\"\n  - quantity: percentage of sessions with a significant variability difference, depth (z)\n    value: 6\n    tolerance: 0.9\n    unit: \"%\"\n  criterion: Method from Materials and Methods, Behavioral analysis. Per session, target and\n    axis, the trial mean endpoint positions of V trials against NV trials by Levene's test at P\n    < 0.05. Tolerances are the paper's stated spreads. Open, and every reading is shown, the\n    centre of Levene's test (mean, as in Levene's original test, or median, the Brown-Forsythe\n    form), and the averaging (the mean of the 16 animal and target percentages, or pooled over\n    session and target pairs). Reproduced when all three axes are within tolerance under one\n    reading.\n- id: table1-endpoint-means\n  statement: Mean endpoint positions per target in the V and NV conditions are those of Table 1,\n    and differ between conditions by at most 0.1 cm at every target, coordinate and animal.\n  source: Table 1\n  inferred: Values read from Table 1, whose legend gives only the units and the sample; no\n    sentence states them. The at most 0.1 cm difference is a reading of the table, used in the\n    Results to say the holding behavior was largely the same.\n  criterion: For each animal, target, condition and axis, the mean over sessions of the session\n    mean endpoint position over the last 800 ms of the hold (219 sessions, monkey X; 124,\n    monkey B). The 96 values of Table 1 are listed in the expected values, in the order monkey\n    X then B, targets 0 to 315 degrees, x, y, z, NV then V. Each tolerance is the SD Table 1\n    gives for that cell (the paper's stated spread). The origin of the tracker frame is not\n    given; if the dataset's frame differs from the table's by a constant offset per animal and\n    axis, the comparison is also made after removing the mean offset, and that is recorded as\n    a deviation. Reproduced when at least 90% of the values are within tolerance and the V\n    minus NV difference is at most 0.1 cm (plus 10%) everywhere.\n- id: table1-endpoint-sd\n  statement: The across-session SDs of endpoint position per target are those of Table 1, about\n    0.5 to 1.3 cm for monkey X and 0.4 to 0.6 cm for monkey B.\n  source: Table 1\n  inferred: Values read from Table 1; no sentence states them.\n  depends_on:\n  - table1-endpoint-means\n  criterion: The SD over sessions of the session mean endpoint positions, for each animal,\n    target, condition and axis, in the order of table1-endpoint-means. Expected values are the\n    96 SDs of Table 1, at 10%. Reproduced when at least 90% are within tolerance.\n- id: fig3-example-neuron\n  statement: An example neuron fired most when the hand was held at the lower left target (225\n    degrees) in both V and NV; its hold-period rate showed a main effect of position (P < 0.05)\n    but no effect of vision (P = 0.52) and no interaction (P = 0.64).\n  source: Results, Neurophysiology, paragraphs 1 and 2; Figure 3\n  quote: For both the V and NV conditions, discharge was greatest when the animal held its hand\n    at the target located in the lower left part of the workspace (225\n  statistics:\n  - about: main effect of position\n    test: two-factor ANOVA\n    p: 0.05\n    p_relation: \"<\"\n    n: one neuron, 8 targets, V and NV trials\n  - about: main effect of the visual conditions\n    test: two-factor ANOVA\n    p: 0.52\n    n: one neuron\n  - about: position by visual conditions interaction\n    test: two-factor ANOVA\n    p: 0.64\n    n: one neuron\n  expected:\n  - quantity: P of the vision main effect\n    value: 0.52\n    tolerance: 0.052\n  - quantity: P of the interaction\n    value: 0.64\n    tolerance: 0.064\n  criterion: The paper does not identify the neuron (no session or unit name). With the ANOVA of\n    hold-period rates (Materials and Methods), the claim is reproduced when at least one neuron\n    has its maximal mean rate at 225 degrees in both conditions, a position main effect at P <\n    0.05, and vision and interaction P values within the tolerances. The candidates found are\n    listed. When none is found the claim is not reproduced, and the closest neuron is shown.\n- id: movement-epoch-tuning\n  statement: In a 500 ms epoch centred on movement onset, 41% (139 of 343) of neurons were\n    modulated by the movement vector (main and/or interaction effects, ANOVA, P < 0.05).\n  source: Results, Neurophysiology, paragraph 2\n  quote: when data during a 500-ms epoch centered on movement onset were analyzed, 41% (139/\n    343) of the neurons were found to be modulated by the required movement vector\n  expected:\n  - quantity: neurons modulated by movement vector\n    value: 139\n    tolerance: 13.9\n    unit: neurons\n  criterion: The two-factor ANOVA of the Methods (target by visual condition, P < 0.05) on the\n    mean rate in the 500 ms centred on movement onset; a cell counts when the target main effect\n    or the interaction is significant. Open, as the paper does not define movement onset,\n    readings (a) an event code marking movement onset, if the data hold one, (b) the time the\n    arm cursor leaves the start window, read from arm position. Reproduced when a reading is\n    within tolerance.\n- id: hold-position-main-effect\n  statement: In the 800 ms static holding period, 39% (135 of 343) of neurons showed a significant\n    main effect of position.\n  source: Results, Neurophysiology, paragraph 2\n  quote: When data from the 800-ms static holding period were considered, 39% (135/343) of the\n    neurons showed a significant main effect of position\n  expected:\n  - quantity: neurons with a position main effect\n    value: 135\n    tolerance: 13.5\n    unit: neurons\n  criterion: Two-factor ANOVA (target location by visual condition, with interaction) on each\n    neuron's mean firing rate per trial in the last 800 ms of the hold, P < 0.05 (Materials and\n    Methods, Analysis of neurophysiological data). The rate is the spike count over the window\n    divided by 0.8 s, a standard choice; the paper's smoothed PSTH (Gaussian, sigma 50 ms)\n    averaged over the window is shown as a variant. The design is balanced with five trials per\n    cell of the design; where trials are missing, type II sums of squares are used, a standard\n    choice.\n- id: hold-vision-main-effect\n  statement: Only 13% (44 of 343) of neurons showed a main effect of the visual conditions in the\n    holding period.\n  source: Results, Neurophysiology, paragraph 2\n  quote: while only 13% (44/343) showed a main effect of the visual conditions\n  expected:\n  - quantity: neurons with a vision main effect\n    value: 44\n    tolerance: 4.4\n    unit: neurons\n  depends_on:\n  - hold-position-main-effect\n  criterion: The ANOVA of hold-position-main-effect; count of neurons with a significant visual\n    condition main effect. Reproduced within tolerance, and when fewer neurons have a vision\n    effect than a position effect.\n- id: hold-interaction\n  statement: Interaction effects of position and vision were found in 9% (27 of 343) of neurons.\n  source: Results, Neurophysiology, paragraph 2\n  quote: Interaction effects of position and vision were found in 9% (27/343) of the neurons\n  expected:\n  - quantity: neurons with a position by vision interaction\n    value: 27\n    tolerance: 2.7\n    unit: neurons\n  depends_on:\n  - hold-position-main-effect\n  criterion: The ANOVA of hold-position-main-effect; count of neurons with a significant\n    interaction. The printed numbers disagree (27/343 is 7.9%; 9% of 343 is 31), so the readings\n    are (a) 27 neurons, (b) 9% of 343, 31 neurons (tolerance 3.1). Reproduced when the count is\n    within tolerance under either reading.\n- id: hold-subepochs\n  statement: Similar percentages were found when the first 400 ms and the last 400 ms of the hold\n    were analyzed separately, 31%, 9% and 5% and 29%, 10% and 4% for position main effect,\n    vision main effect and interaction.\n  source: Results, Neurophysiology, paragraph 2\n  quote: Similar percentages were noted when the first 400 ms and the last 400 ms of the holding\n    period were separately analyzed (31/9/5% and 29/10/4%, respectively)\n  expected:\n  - quantity: first 400 ms, position main effect\n    value: 31\n    tolerance: 3.1\n    unit: \"%\"\n  - quantity: first 400 ms, vision main effect\n    value: 9\n    tolerance: 0.9\n    unit: \"%\"\n  - quantity: first 400 ms, interaction\n    value: 5\n    tolerance: 0.5\n    unit: \"%\"\n  - quantity: last 400 ms, position main effect\n    value: 29\n    tolerance: 2.9\n    unit: \"%\"\n  - quantity: last 400 ms, vision main effect\n    value: 10\n    tolerance: 1\n    unit: \"%\"\n  - quantity: last 400 ms, interaction\n    value: 4\n    tolerance: 0.4\n    unit: \"%\"\n  depends_on:\n  - hold-position-main-effect\n  criterion: The ANOVA of hold-position-main-effect on the first and the last 400 ms of the\n    analyzed 800 ms window, percentages of 343 neurons. Reproduced when at least five of the six\n    values are within tolerance; partially when three or four are.\n- id: hold-overall-effects\n  statement: Over the full hold, 44% of neurons showed some effect of position (main and/or\n    interaction), 19% some effect of vision, and 11% effects of both position and vision.\n  source: Results, Neurophysiology, paragraph 2\n  quote: Overall, during the full holding period, 44% of the neurons showed some effect of\n    position (cells with main and/or interaction effects) while 19% showed either main or\n    interaction effects of the visual conditions. ... 11% of the neurons demonstrated effects of\n    both position and vision (main effects of both factors and/or interaction effects)\n  expected:\n  - quantity: neurons with any position effect\n    value: 44\n    tolerance: 4.4\n    unit: \"%\"\n  - quantity: neurons with any vision effect\n    value: 19\n    tolerance: 1.9\n    unit: \"%\"\n  - quantity: neurons with effects of both position and vision\n    value: 11\n    tolerance: 1.1\n    unit: \"%\"\n  depends_on:\n  - hold-position-main-effect\n  criterion: The ANOVA of hold-position-main-effect, percentages of 343 neurons. Any position\n    effect is a position main effect or interaction; any vision effect is a vision main effect\n    or interaction; both is both main effects or the interaction (the paper's definitions).\n- id: correlation-endpoint-datasets\n  statement: Correlations between V and NV responses were the same where mean endpoint positions\n    differed between conditions (r = 0.9301) and where they did not (r = 0.9281), so firing rate\n    differences did not reflect endpoint differences.\n  source: Results, Neurophysiology, paragraph 3\n  quote: We found that the correlations were identical for these two data sets (r for data set\n    1 ... 0.9301; r for data set 2 ... 0.9281; permutation test\n  expected:\n  - quantity: Spearman r, V against NV responses, endpoints differed (data set 1)\n    value: 0.9301\n    tolerance: 0.093\n  - quantity: Spearman r, V against NV responses, endpoints the same (data set 2)\n    value: 0.9281\n    tolerance: 0.093\n  depends_on:\n  - behavior-mean-position-sessions\n  criterion: Methods, Analysis of neurophysiological data, paragraph on Spearman correlations.\n    Data set 1 is the session and target pairs with a significant MANOVA (behavior-mean-position-sessions),\n    data set 2 the others. The response is the hold-period mean firing rate. Open, as the paper\n    does not say what a response pair is, readings (a) the V and NV mean rates of each cell at\n    each target, (b) single trials paired by order within cell and target. The difference\n    between the two r values is tested by the permutation test of the FF (pairs pooled and\n    randomly assigned to two groups of the original sizes, 1,000 times, P < 0.05, two-sided, a\n    standard choice). A claim of absence; reproduced when the permutation test does not find a\n    difference at P < 0.05 and both r values are within tolerance. The paper prints \"P < 0.05\"\n    with \"identical\"; it is read as the test's threshold (see the header) and not recorded as a\n    result.\n- id: fig4-indx1-negative\n  statement: For most cells INDX1 was negative (activity lower with vision than without), with\n    84%, 77%, 85% and 84% negative among all cells, Position Only, Position/Vision and Vision\n    Only cells (338, 110, 38 and 27 cells after outlier removal).\n  source: Results, Neurophysiology, paragraph 4; Figure 4A-D\n  quote: The percentage of cells with negative indexes was fairly consistent across the\n    different populations (84%, 77%, 85%, and 84% for the populations shown in Fig. 4, A-D,\n    respectively)\n  expected:\n  - quantity: negative INDX1, all cells\n    value: 84\n    tolerance: 8.4\n    unit: \"%\"\n  - quantity: negative INDX1, Position Only cells\n    value: 77\n    tolerance: 7.7\n    unit: \"%\"\n  - quantity: negative INDX1, Position/Vision cells\n    value: 85\n    tolerance: 8.5\n    unit: \"%\"\n  - quantity: negative INDX1, Vision Only cells\n    value: 84\n    tolerance: 8.4\n    unit: \"%\"\n  - quantity: cells after outlier removal, all\n    value: 338\n    tolerance: 33.8\n    unit: cells\n  - quantity: Position Only cells\n    value: 110\n    tolerance: 11\n    unit: cells\n  - quantity: Position/Vision cells\n    value: 38\n    tolerance: 3.8\n    unit: cells\n  - quantity: Vision Only cells\n    value: 27\n    tolerance: 2.7\n    unit: cells\n  depends_on:\n  - hold-overall-effects\n  criterion: INDX1 = (Vpnv - NVpnv) / NVpnv x 100, with NVpnv the mean hold rate at the target of\n    maximal NV rate and Vpnv the V rate at that target (Eq. 1). Groups from the ANOVA (Fig. 4\n    legend) - Position Only has a position main effect and no vision main effect or\n    interaction; Position/Vision has both main effects or the interaction; Vision Only has a\n    vision main effect and no position main effect or interaction. Outliers are removed as in\n    the Fig. 4 legend, \"indexes > 1.5 times the interquartile range\", 5 cells in all. Open,\n    readings (a) Tukey fences (below Q1 - 1.5 IQR or above Q3 + 1.5 IQR) over all cells, (b) the\n    same fences within each group, (c) index above 1.5 times the IQR of all cells. Cells with an\n    NV peak rate of 0 have no index and are left out (a standard choice). Reproduced when the\n    four percentages are within tolerance under a reading; the group sizes are reported and\n    compared.\n- id: fig4-indx1-means\n  statement: Mean INDX1 was least negative for Position Only cells (-13%) and most negative for\n    Position/Vision cells (-31%).\n  source: Results, Neurophysiology, paragraphs 4 and 5; Figure 4B, C\n  quote: the mean INDX1 was least negative ... In contrast, the average index was most negative in\n    the population of cells showing both positional and visual modulation by the ANOVA\n  expected:\n  - quantity: mean INDX1, Position Only cells\n    value: -13\n    tolerance: 1.3\n    unit: \"%\"\n  - quantity: mean INDX1, Position/Vision cells\n    value: -31\n    tolerance: 3.1\n    unit: \"%\"\n  depends_on:\n  - fig4-indx1-negative\n  criterion: INDX1 and groups as in fig4-indx1-negative, after outlier removal under each of its\n    readings. Reproduced when both means are within tolerance under a reading and the\n    Position/Vision mean is the most negative and the Position Only mean the least negative of\n    the four populations of Fig. 4.\n- id: indx1-tuning-shift\n  statement: Among Position/Vision cells, those with their maximal response at the same or an\n    adjacent location in the two conditions (22 of 38, 58%) had a mean INDX1 of -24%, and the\n    others a more negative mean of -40%.\n  source: Results, Neurophysiology, paragraph 5\n  quote: Position/Vision cells that had their maximum responses at the same or immediately\n    adjacent locations in the two conditions (22/38; 58%) had an average index of\n  expected:\n  - quantity: Position/Vision cells with same or adjacent preferred location\n    value: 22\n    tolerance: 2.2\n    unit: cells\n  - quantity: mean INDX1 of those cells\n    value: -24\n    tolerance: 2.4\n    unit: \"%\"\n  - quantity: mean INDX1 of the other Position/Vision cells\n    value: -40\n    tolerance: 4\n    unit: \"%\"\n  depends_on:\n  - fig4-indx1-negative\n  criterion: Preferred locations are the targets of maximal mean hold rate in V and in NV.\n    Open, the meaning of adjacent, readings (a) neighbours on the ring of eight directions (45\n    degrees apart), (b) neighbours on the 3 by 3 grid of target positions, including diagonals\n    (so 0 and 90 degrees are adjacent). Reproduced when the three values are within tolerance\n    under a reading.\n- id: indx2-means\n  statement: With an index based on each condition's own preferred location (INDX2), rate\n    differences were weaker but still biased toward suppression, with means of -9%, -13% and -13%\n    for Position Only, Vision Only and Position/Vision cells.\n  source: Results, Neurophysiology, paragraph 5\n  quote: rate differences between conditions were not strong but were still biased toward\n    suppression, with average indexes of\n  expected:\n  - quantity: mean INDX2, Position Only\n    value: -9\n    tolerance: 0.9\n    unit: \"%\"\n  - quantity: mean INDX2, Vision Only\n    value: -13\n    tolerance: 1.3\n    unit: \"%\"\n  - quantity: mean INDX2, Position/Vision\n    value: -13\n    tolerance: 1.3\n    unit: \"%\"\n  depends_on:\n  - fig4-indx1-negative\n  criterion: INDX2 = (Vpv - NVpnv) / NVpnv x 100, Vpv the V rate at the V preferred location\n    (Eq. 2). Groups and outlier readings as in fig4-indx1-negative (outliers on INDX1, reading\n    (i), or on INDX2, reading (ii), as the paper does not say). Reproduced when the three means\n    are negative and within tolerance under a reading.\n- id: rate-variance-nv-higher\n  statement: Spike rate variance at the NV preferred location tended to be higher in NV than in V,\n    on average 56 against 30 (spikes/s)^2 across cells.\n  source: Results, Neurophysiology, paragraph 6\n  quote: the average variance (across cells) at the peak location in the NV condition was 56\n    (spikes/s)2, while in the V condition the average variance was 30 (spikes/s)2\n  expected:\n  - quantity: mean across cells of NV rate variance\n    value: 56\n    tolerance: 5.6\n    unit: (spikes/s)^2\n  - quantity: mean across cells of V rate variance\n    value: 30\n    tolerance: 3\n    unit: (spikes/s)^2\n  criterion: For each cell, the variance across trials of the hold-period rate at the NV\n    preferred location, in each condition, averaged over cells (Methods, paragraph on neural\n    variability). Open, readings (a) all 343 cells, (b) the cells left after the Fig. 4 outlier\n    removal; and sample variance (n - 1), a standard choice, with the population variance shown.\n    The paper reports a trend and no test. Reproduced when both means are within tolerance\n    under a reading.\n- id: fig5-fano-factor\n  statement: The Fano factor was significantly larger in NV (1.54) than in V (1.13) (permutation\n    test, P < 0.05).\n  source: Results, Neurophysiology, paragraph 6; Figure 5\n  quote: Statistical analysis revealed that the FF was significantly larger in the NV condition\n    (permutation test\n  statistics:\n  - test: permutation test, 1,000 permutations\n    p: 0.05\n    p_relation: \"<\"\n    n: spike count means and variances of all cells after outlier removal, at the NV peak location\n  expected:\n  - quantity: FF, V\n    value: 1.13\n    tolerance: 0.113\n  - quantity: FF, NV\n    value: 1.54\n    tolerance: 0.154\n  criterion: Methods, paragraphs on FF. Spike counts in the last 800 ms of the hold at the NV\n    preferred location; for each cell the count mean and variance over trials in each\n    condition; FF is the slope of variance on mean through the origin, by least squares (a\n    standard choice for a line through the origin). Permutation test as the Methods give it,\n    the 2N (mean, variance) pairs pooled and randomly split into two groups of N, FF difference\n    computed, 1,000 times; P is the fraction of permuted differences at least the observed\n    one, two-sided (a standard choice; one-sided shown). Open, which cells are outliers (Fig. 5\n    legend \"after outlier removal\"), readings (a) the 5 cells removed for Fig. 4, (b) Tukey\n    outliers (1.5 IQR) on the count means or variances. Reproduced when NV FF exceeds V FF with\n    P < 0.05 and both FFs are within tolerance, under a reading.\n- id: cv2-larger-nv\n  statement: The squared coefficient of variation of interspike intervals (CV2) was also\n    significantly larger in NV than in V (Kruskal-Wallis test, P < 0.05).\n  source: Results, Neurophysiology, paragraph 6\n  quote: Interestingly, the CV2, which assesses variability in the interspike intervals, was also\n    significantly larger in the NV condition\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.05\n    p_relation: \"<\"\n    n: CV2 of each cell in V and in NV\n  criterion: Methods, CV2 paragraph. CV2 = (SD / mean of ISIs)^2 per cell and condition, at the\n    NV preferred location, ISIs within the last 800 ms of the hold. Open, readings (a) ISIs\n    pooled over the trials, (b) CV2 per trial averaged over trials. Cells with fewer than two\n    ISIs in a condition are left out (a standard choice). V against NV cell values by a\n    Kruskal-Wallis test. Reproduced when the NV median exceeds the V median with P < 0.05 under\n    a reading.\n- id: fig6-decoding-vv\n  statement: A maximum-likelihood decoder trained and tested on V data decoded hand position with\n    an average accuracy across targets of 91.6 +/- 9%.\n  source: Results, Neurophysiology, paragraph 7; Figure 6, top left\n  quote: For example, when data from the full 800 ms of the holding period were used, average\n    decoding accuracy across targets in the V conditions was 91.6\n  expected:\n  - quantity: decoding accuracy, trained and tested on V\n    value: 91.6\n    tolerance: 9\n    unit: \"%\"\n  criterion: Methods, decoding paragraph and Eqs. 3 and 4. All 343 neurons treated as\n    simultaneously recorded; Poisson likelihood of the spike counts in the last 800 ms of the\n    hold; lambda per cell and target is the mean count over four training trials; the held-out\n    trial is decoded as the target of maximal likelihood; repeated so each of the five trials is\n    the test trial; accuracy per target is the fraction of the five correct, averaged over the\n    eight targets. Bootstrapped across cells, N = 200. Tolerance is the paper's stated spread.\n    Open, readings for each, (i) the trials of different cells joined by their order within\n    target and condition (a standard choice, as no other pairing exists); (ii) bootstrap,\n    (a) 200 resamples of the cells with replacement, (b) resampled populations of 200 cells;\n    (iii) a lambda of 0 is replaced by a small constant (1e-3 spikes, a standard choice).\n    Reproduced when the accuracy is within tolerance under a reading.\n- id: fig6-decoding-nvnv\n  statement: Trained and tested on NV data, the decoder's accuracy fell to 81.9 +/- 18.0%.\n  source: Results, Neurophysiology, paragraph 7; Figure 6, bottom right\n  quote: In contrast, when the decoder was both trained and tested with data from the NV\n    conditions (Fig. 6, bottom right) decoding accuracy fell to 81.9\n  expected:\n  - quantity: decoding accuracy, trained and tested on NV\n    value: 81.9\n    tolerance: 18\n    unit: \"%\"\n  depends_on:\n  - fig6-decoding-vv\n  criterion: The decoder of fig6-decoding-vv on NV trials, under its readings. Reproduced within\n    tolerance.\n- id: decoding-v-better-than-nv\n  statement: Decoding accuracy was significantly higher in V than in NV (t-test, P < 0.05), a small\n    but significant role of vision in representing limb position.\n  source: Results, Neurophysiology, paragraph 7\n  quote: The difference in decoding performance between the V and NV conditions was statistically\n    significant\n  statistics:\n  - test: t-test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - fig6-decoding-vv\n  - fig6-decoding-nvnv\n  criterion: The paper names a t-test and not its samples. Readings (a) paired t-test over the\n    eight per-target accuracies, (b) two-sample t-test over the 200 bootstrap accuracies of each\n    condition, (c) two-sample t-test over the eight per-target accuracies. Reproduced when V\n    accuracy exceeds NV accuracy with P < 0.05 under a reading; every reading is shown.\n- id: fig6-decoding-cross\n  statement: Training and testing on different conditions gave lower accuracies, 60.7 +/- 22%\n    trained on NV and tested on V and 69.1 +/- 17% trained on V and tested on NV, so decoding\n    degraded whenever NV data were used.\n  source: Figure 6 legend; Results, Neurophysiology, paragraphs 7 and 8\n  quote: Results from the analyses where the decoder was trained and tested with data from\n    different conditions reinforce the idea that decoding of limb position degraded somewhat\n    whenever data from the NV condition were used\n  expected:\n  - quantity: accuracy, trained on NV, tested on V\n    value: 60.7\n    tolerance: 22\n    unit: \"%\"\n  - quantity: accuracy, trained on V, tested on NV\n    value: 69.1\n    tolerance: 17\n    unit: \"%\"\n  depends_on:\n  - fig6-decoding-vv\n  criterion: Decoder of fig6-decoding-vv. Open, the cross-condition scheme, readings (a) lambda\n    from four trials of one condition and the held-out trial order of the other, as in the\n    leave-one-out, (b) lambda from all five trials of one condition and all five trials of the\n    other tested. Reproduced when both accuracies are within tolerance and both are below the\n    V/V accuracy, under a reading.\n- id: decoding-subepochs\n  statement: Decoding was less accurate with shorter windows, but did not differ between the first\n    and the last 400 ms of the hold, in V or in NV.\n  source: Results, Neurophysiology, paragraph 7; Discussion, Additional factors, paragraph 2\n  quote: While accuracy decreased with shorter windows, no difference in decoding performance was\n    found when the first 400 ms and the last 400 ms of the holding period were compared\n  depends_on:\n  - fig6-decoding-vv\n  - decoding-v-better-than-nv\n  criterion: The decoder of fig6-decoding-vv on the first and the last 400 ms of the analysed\n    window, in V and in NV. A claim of absence. The paper names no test for this comparison;\n    the test it uses for decoding performance is the t-test of decoding-v-better-than-nv, at P\n    < 0.05, with its sample readings. Reproduced when the 400 ms accuracies are below the 800 ms\n    accuracy and the t-test finds no first against last difference in either condition; the\n    differences are given either way.\n- id: decoding-nonsignificant-cells\n  statement: Neurons with no ANOVA effect of position, vision or interaction still decoded\n    position above chance at some targets, and slightly better in V than in NV (20% against\n    14%), though this difference was not significant.\n  source: Results, Neurophysiology, paragraph 8\n  quote: Interestingly, average decoding accuracy was also slightly higher in the V condition\n    than in the NV condition in this subset of cells (20% vs. 14%), similar in trend to what was\n    observed for the entire population, though this difference was not statistically\n    significant\n  expected:\n  - quantity: decoding accuracy, V, cells without ANOVA effects\n    value: 20\n    tolerance: 2\n    unit: \"%\"\n  - quantity: decoding accuracy, NV, cells without ANOVA effects\n    value: 14\n    tolerance: 1.4\n    unit: \"%\"\n  depends_on:\n  - hold-overall-effects\n  - decoding-v-better-than-nv\n  criterion: The decoder of fig6-decoding-vv on the neurons with no significant effect in the\n    ANOVA of hold-position-main-effect. Chance is 12.5% (eight targets). The paper names no test\n    for above chance or for V against NV here; the V against NV test is the t-test of\n    decoding-v-better-than-nv, at P < 0.05, with its readings, and above chance is a target\n    with accuracy above 12.5% in both conditions (the paper gives no test). Reproduced when\n    both accuracies are within tolerance, V exceeds NV, the t-test is not significant, and some\n    target is above chance in both conditions.\n- id: eye-position-no-difference\n  statement: Neither mean eye position nor the variance of its horizontal or vertical component\n    differed between V and NV for any target (MANOVA and Levene's test).\n  source: Discussion, Additional factors influencing neural responses, paragraph 3\n  quote: We found that neither the average eye positions nor the variances of the horizontal or\n    vertical components of eye position differed between the V and NV conditions for any target\n  criterion: A claim of absence. Per target, the trial mean eye positions (horizontal, vertical)\n    in the last 800 ms of the hold, V against NV by a one-factor MANOVA, and each component's\n    variance by Levene's test, at P < 0.05 as printed. Open, readings (a) per animal, trials\n    pooled over sessions, (b) per session, the claim then read as the share of significant\n    sessions near the 5% expected by chance. The paper's \"for any target\" fits (a); (b) is a\n    variant. Reproduced when no target shows a difference under (a); the effects are given\n    either way.\n- id: aborted-trials-nv\n  statement: In one animal, as the behavioral window around the reach targets was made smaller,\n    aborted trials increased in both conditions, and were significantly more frequent on NV\n    trials for smaller windows (t-test, P < 0.05), so the animals used vision to hold position.\n  source: Discussion, Additional factors influencing neural responses, paragraph 1\n  quote: We found that as the window size decreased the number of aborted trials increased for\n    both the NV and V conditions and, moreover, the number of these aborted trials was\n    significantly greater on NV trials for smaller window sizes\n  statistics:\n  - test: t-test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: The paper gives this test from Shi and Buneo (2009), an abstract, and gives neither\n    the animal, the window sizes, the unit of the t-test nor how aborts are counted. It needs\n    the aborted trials and the window size of each, in sessions where the window was varied.\n    Readings (a) per session and window size, NV against V abort rate by a paired t-test, (b)\n    the same by a two-sample t-test. Reproduced when, under a reading, aborts rise as the window\n    shrinks in both conditions and are more frequent in NV at the smallest windows with P <\n    0.05. When the data hold no such sessions, the claim cannot be tested.\n- id: longer-hold-no-difference\n  statement: In a subset of sessions with the minimum hold extended to 1,200 ms, neither behavior\n    nor neural responses differed appreciably.\n  source: Discussion, Additional factors influencing neural responses, paragraph 1\n  quote: In a subset of experimental sessions we extended the minimum duration of the holding\n    period out to 1,200 ms and found no appreciable differences in either the behavior of the\n    animals or the neural responses\n  criterion: A claim of absence that cites a preliminary abstract (Shi and Buneo 2009); the paper\n    names no test, no measure and the sessions. Read here with the paper's own measures, the\n    share of cells with a vision effect (hold-overall-effects) and the V against NV decoding\n    difference (decoding-v-better-than-nv) in sessions with a minimum hold of 1,200 ms against\n    the others, by a chi-square test of the counts and the t-test of decoding-v-better-than-nv,\n    at P < 0.05. Reproduced when neither differs. The choice of measures is an assumption.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'E'
import re
L=open('paper/10.1152-jn.00223.2012.txt',encoding='utf-8').read().splitlines()[547:661]
rows=[];animal=None;tgt=None;vals=[]
for l in L:
    l=l.strip()
    if l.startswith('Monkey'): animal=l.split()[1]; continue
    if l.endswith('°'): tgt=l[:-1]; continue
    m=re.match(r'^(�?)([\d.]+) �([\d.]+)$',l)
    if m:
        v=float(m.group(2))*(-1 if m.group(1) else 1); vals.append((animal,tgt,v,float(m.group(3))))
print(len(vals))
axes=['x','y','z'];conds=['NV','V']
out_m=[];out_s=[]
for i,(a,t,v,s) in enumerate(vals):
    k=i%6; ax=axes[k//2]; c=conds[k%2]
    q=f"monkey {a}, {t} degrees, {ax}, {c}"
    out_m.append(f"  - quantity: mean endpoint, {q}\n    value: {v}\n    tolerance: {s}\n    unit: cm")
    out_s.append(f"  - quantity: SD of endpoint, {q}\n    value: {s}\n    tolerance: {round(s*0.1,3)}\n    unit: cm")
p='claims/shi-2013.yaml'; t=open(p).read()
t=t.replace("""    a deviation. Reproduced when at least 90% of the values are within tolerance and the V
    minus NV difference is at most 0.1 cm (plus 10%) everywhere.
""","""    a deviation. Reproduced when at least 90% of the values are within tolerance and the V
    minus NV difference is at most 0.1 cm (plus 10%) everywhere.
  expected:
"""+"\n".join(out_m)+"\n",1)
t=t.replace("""    96 SDs of Table 1, at 10%. Reproduced when at least 90% are within tolerance.
""","""    96 SDs of Table 1, at 10%. Reproduced when at least 90% are within tolerance.
  expected:
"""+"\n".join(out_s)+"\n",1)
open(p,'w').write(t)
# max diff check
import itertools
d=max(abs(vals[i][2]-vals[i+1][2]) for i in range(0,96,2)); print('max V-NV diff',d)
print(min(v[3] for v in vals[:48]),max(v[3] for v in vals[:48]),min(v[3] for v in vals[48:]),max(v[3] for v in vals[48:]))
E
python tools/claims_check.py claims/shi-2013.yaml paper/10.1152-jn.00223.2012.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'E'
import re
p='claims/shi-2013.yaml'; t=open(p).read()
t=t.replace("""  quote: Results from the analyses where the decoder was trained and tested with data from
    different conditions reinforce""","""  quote: Results from the analyses where the decoder ... was trained and tested with data from
    different conditions reinforce""")
open(p,'w').write(t)
L=open('paper/10.1152-jn.00223.2012.txt',encoding='utf-8').read().splitlines()[547:661]
vals=[];a=t0=None
for l in L:
    l=l.strip()
    if l.startswith('Monkey'): a=l.split()[1]; continue
    if l.endswith('°'): t0=l; continue
    m=re.match(r'^(�?)([\d.]+) �([\d.]+)$',l)
    if m: vals.append((a,t0,float(m.group(2))*(-1 if m.group(1) else 1)))
for i in range(0,96,2):
    if abs(vals[i][2]-vals[i+1][2])>0.075: print(vals[i],vals[i+1])
E
python tools/claims_check.py claims/shi-2013.yaml paper/10.1152-jn.00223.2012.txt; grep -n "[a-z]: [a-z]" claims/shi-2013.yaml | grep -v "^\S*:\s*- \|^[0-9]*:  *[a-z_]*: " | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'E'
p='claims/shi-2013.yaml'; t=open(p).read()
t=t.replace("""and differ between conditions by at most 0.1 cm at every target, coordinate and animal.""","""and differ between conditions by at most 0.11 cm at every target, coordinate and animal.""")
t=t.replace("""The at most 0.1 cm difference is""","""The at most 0.11 cm difference is""")
t=t.replace("""minus NV difference is at most 0.1 cm (plus 10%) everywhere.""","""minus NV difference of the means is at most 0.11 cm (plus 10%) everywhere.""")
open(p,'w').write(t)
import yaml
d=yaml.safe_load(t)
def walk(x,k=''):
    if isinstance(x,dict):
        for a,b in x.items(): walk(b,k+'.'+str(a))
    elif isinstance(x,list):
        for b in x: walk(b,k)
    elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x): print(k,x[:80])
walk(d)
E
grep -c "0.11 cm" claims/shi-2013.yaml; python tools/claims_check.py claims/shi-2013.yaml paper/10.1152-jn.00223.2012.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short; python -c "
import yaml;d=yaml.safe_load(open('claims/shi-2013.yaml'));c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum(len(x['statistics']) for x in c if 'statistics' in x))"
```

```
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
?? claims/shi-2013.yaml
?? scripts
28 26 5 28 7
```

**Agent**

I've written `claims/shi-2013.yaml`, and the quote checker passes it: 28 claims, 26 quotes, 7 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record (PyMuPDF text of the journal PDF): Methods, Results, Discussion, Table 1 and the legends of Figures 1 to 6. The paper has no supplement and links no code, so no code was read. The text prints the math signs (=, <, >, ±, minus, ~) as a broken character, and the PDF could not be rendered here. I recovered the signs from the PDF's font encodings instead; the decoded signs are listed in the file's opening comment.

**Counts.**
- **Claims:** 28, all findings.
- **Quotes:** 26. Table 1's means and its SDs have no sentence stating them, so those two claims carry an `inferred` note.
- **Statistics:** 7 entries across 5 claims.
  - The example neuron of Fig. 3: P < 0.05 for position, P = 0.52 for vision, P = 0.64 for the interaction.
  - The Fano factor permutation test.
  - The CV2 Kruskal-Wallis test.
  - The V against NV decoding t-test.
  - The aborted-trials t-test.
- **Criteria:** all 28 claims have one.
- **A reading of the paper's notation:** it prints "P < 0.05" even after results it calls not significant. I read that as the test's threshold, so it is recorded as a statistic only where the finding is a significant difference.

**Details left open, and the readings named:**
- **Trials per target:** the paper says five. Read as five per target in each condition, because the decoder trains on four trials and tests on the fifth.
- **Session averaging (behavior):** the mean of the 16 animal-by-target percentages, or pooled over all session-target pairs. Levene's test centred on the mean or on the median.
- **Table 1:** the origin of the tracker frame is not given, so values are compared directly and again after removing a constant offset.
- **Example neuron (Fig. 3):** it is not identified; any neuron matching its tuning and P values counts.
- **Movement onset:** not defined. An event code marking onset, or the time the arm leaves the start window.
- **The 9% (27/343) interaction count:** 27/343 is 7.9%, so the readings are 27 cells or 9% (31 cells).
- **The V–NV correlations:** what a response pair is (cell-by-target mean rates, or single trials paired by order). The permutation test is taken as two-sided.
- **Fig. 4 outliers:** Tukey fences over all cells, the same fences within each group, or an index above 1.5 times the IQR. For INDX2, whether outliers are removed on INDX1 or on INDX2.
- **"Adjacent" preferred location:** neighbours on the ring of eight directions, or on the 3 by 3 grid including diagonals.
- **Rate variance:** all 343 cells or the cells left after outlier removal.
- **Fano factor outliers:** the 5 cells removed for Fig. 4, or Tukey outliers on the count means or variances.
- **CV2:** intervals pooled over trials, or computed per trial and averaged.
- **Decoding:**
  - Bootstrap: 200 resamples of the cells, or resampled populations of 200 cells.
  - The cross-condition scheme: leave-one-out across conditions, or train on all five trials of one condition and test on all five of the other.
  - The t-test's samples: paired over the 8 targets, unpaired over the 8 targets, or unpaired over the 200 bootstraps.
- **Tests the paper does not name:** the first against last 400 ms decoding comparison, the cells without ANOVA effects, and the extended-hold sessions. Each takes the paper's decoding t-test (or, for the extended hold, a chi-square test of the cell counts) as its reading.
- **Eye position:** per animal, or per session.

**Missing from the paper that claims needed:**
- **Aborted trials and the 1,200 ms hold:** both rest on an abstract (Shi and Buneo 2009). The paper gives no window sizes, test units or sessions, so these two claims are probably underspecified.
- **No identifier for the example neuron.**
- **No analysis code.**

## End of run

27 turns, 6 minutes, $1.84 at API prices, result: success.
