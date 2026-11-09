# 000688 · claims-check · run 39901682990

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/000688/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 96,220p docs/protocol.md
```

```
- `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/000688/*.yaml; python tools/claims_check.py claims/000688/10.1016-j.neuron.2018.09.030.yaml paper/10.1016-j.neuron.2018.09.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat -n claims/000688/*.yaml | sed -n 25,400p
```

```
25	#
    26	# Data the paper used, as it reports them:
    27	# - Subjects: two male rhesus macaques, Monkey C (11.7 kg) and Monkey M (10.5 kg), with 96-channel
    28	#   Utah arrays in M1 and PMd (Blackrock Cerebus), spikes sorted offline (Plexon Offline Sorter)
    29	#   over all three epochs of a session together.
    30	# - Task: instructed-delay center-out reaching with a 2-D planar manipulandum, eight targets on a
    31	#   circle of 8 cm (6 cm in Monkey C's first three sessions), 2 cm square targets; hold 0.5 to 1.5
    32	#   s, instructed delay 0.5 to 1.5 s, auditory go cue, 1 s to reach, 0.5 s target hold. Handle
    33	#   position at 1 kHz.
    34	# - Sessions: each has a Baseline epoch, a perturbation epoch and a Washout epoch. Curl field (CF)
    35	#   sessions: 85 degree velocity-dependent field, k = 0.15 N s/cm, CW or CCW; Baseline 170 to 225
    36	#   rewards, Force 201 to 337, Washout 153 to 404. Monkey C three CW and two CCW, Monkey M four
    37	#   CCW (9 sessions). Visuomotor rotation (VR) sessions: 30 degree rotation of the cursor, CW or
    38	#   CCW; Baseline 154 to 217 successful trials, Rotation 219 to 316, Washout 162 to 348. Monkey C
    39	#   two CW and two CCW, Monkey M three CCW (7 sessions). The Methods and Figure 6 legend count 9 CF
    40	#   and 7 VR, 16 sessions in all; the Figure 2C legend shows two CW and five CCW CF sessions and the
    41	#   Figure 7 legend one CW and four CCW VR sessions, which do not add up to these counts.
    42	# - Neurons: 137 to 256 PMd and 55 to 93 M1 per session in Monkey C, 66 to 121 PMd and 26 to 51 M1
    43	#   in Monkey M. Cells with high coincidence across channels excluded. GLM analyses use neurons
    44	#   above 5 Hz trial-averaged rate (918 M1, 2221 PMd pooled over all sessions); the covariance
[... 356 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat -n claims/000688/*.yaml | sed -n 400,800p; python tools/claims_check.py claims/000688/10.1016-j.neuron.2018.09.030.yaml paper/10.1016-j.neuron.2018.09.030.txt | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l paper/10.1016-j.neuron.2018.09.030.txt; ls checks 2>/dev/null; grep -n "checks" -r claims/000689/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1060,1100p claims/000689/*.yaml
```

```
test: one-way ANOVA
    statistic: F(2, 25) = 4.324
    p: 0.024
  - about: global BLA cKO, control against pre-acquisition cKO
    test: one-way ANOVA, Holm-Sidak's multiple comparisons test
    p: 0.019
  - about: global BLA cKO, control against post-acquisition cKO
    test: one-way ANOVA, Holm-Sidak's multiple comparisons test
    p: 0.99
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1g-pvt-global-cko-reward, criterion now names the measure as open (z-score or raw percent), since the effect size of 20.52 reads like a percentage and the Methods describe a z-score.
  - fig1h-global-cko-no-shock-effect, added the legend's mouse counts per region, noted that t(14) is printed for 8 and 9 PVT mice, and named the Methods' freezing rule in the criterion.
  - ed2-glutamate-corelease, noted that the vHPC t = 28.03 does not fit its P or effect size.
  - ed6-somatic-no-change, added the two missing tone-airpuff tests (MGN, vHPC) and the CIs of the MGN and vHPC tone-sucrose tests; the criterion already judged six tests.
  - fig4-recording-count, corrected the note on 684 neurons (the excluded BLA-CeA neuron is kept for basal firing, so it does not explain the gap) and added that the Figure 4e degrees of freedom sum to 685 neurons.
[... 9 more lines not kept]
```

**Agent**

Checker passes (0 problems). Now reading the paper to verify claims.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.txt",
 "offset": 700,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Figure S[1-7]\b\|Supplementary\|supp" paper/10.1016-j.neuron.2018.09.030.txt | sed -n 1,80p | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.txt",
 "offset": 1380,
 "limit": 970
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I'll check the figure panels the claims read p-values and asterisks from (S6, S7, S5F).

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; python -c "import fitz; print(fitz.__doc__)"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.supp8.pdf",
 "pages": "5-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import importlib
for m in ['pypdf','pdfminer','pdfplumber','PyPDF2','pypdfium2']:
    try: importlib.import_module(m); print(m,'ok')
    except Exception as e: print(m,'no')
"
```

```
pypdf no
pdfminer no
pdfplumber no
PyPDF2 no
pypdfium2 no
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp8.pdf','rb').read()
streams=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
print(len(streams))
out=[]
for i,s in enumerate(streams):
    try: t=zlib.decompress(s)
    except Exception: continue
    if b'Tj' in t or b'TJ' in t:
        out.append((i,len(t),t[:300]))
for o in out[:10]: print(o)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/pdftxt.py <<'EOF'
import re,zlib,sys
d=open(sys.argv[1],'rb').read()
streams=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
idx=int(sys.argv[2])
t=zlib.decompress(streams[idx]).decode('latin1')
tok=re.findall(r'\[(?:[^\]\\]|\\.)*\]|\((?:[^)\\]|\\.)*\)|/[^\s/\[\(<]+|[^\s\[\(/]+',t)
stack=[];x=y=0;lx=ly=0;lead=0;ctm=[1,0,0,1,0,0];cs=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
tm=[1,0,0,1,0,0];tlm=tm[:]
for k in tok:
    if k=='q': cs.append(ctm[:]); stack=[]
    elif k=='Q': ctm=cs.pop() if cs else ctm; stack=[]
    elif k=='cm': ctm=mul([float(v) for v in stack[-6:]],ctm); stack=[]
    elif k=='BT': tm=[1,0,0,1,0,0];tlm=tm[:];stack=[]
    elif k=='Tm': tm=[float(v) for v in stack[-6:]];tlm=tm[:];stack=[]
    elif k in('Td','TD'):
        tx,ty=float(stack[-2]),float(stack[-1]);
        if k=='TD': lead=-ty
        tlm=mul([1,0,0,1,tx,ty],tlm);tm=tlm[:];stack=[]
    elif k=='TL': lead=float(stack[-1]);stack=[]
    elif k=='T*': tlm=mul([1,0,0,1,0,-lead],tlm);tm=tlm[:];stack=[]
    elif k in('Tj','TJ',"'",'"'):
        s=stack[-1] if stack else ''
        txt=''.join(re.findall(r'\((.*?)(?<!\\)\)',s)) if s.startswith('[') else s[1:-1]
        m=mul(tm,ctm)
        print(f'{m[4]:8.1f} {m[5]:8.1f} {txt}')
        stack=[]
    else: stack.append(k)
EOF
python $TMPDIR/pdftxt.py paper/10.1016-j.neuron.2018.09.030.supp8.pdf 1 | grep -v "^.\{18\}[A-Za-z(]\{0\}$" | awk '$2>250' | head -150
```

Result: not kept, because it reads the paper's text.

**Agent**

Figure S7 p-value positions are consistent with the claims' model assignments. Now Figure S6 and S5.

**Agent calls Bash**

```bash
cd  python $TMPDIR/pdftxt.py paper/10.1016-j.neuron.2018.09.030.supp8.pdf 6 | awk '$2>300'; echo ---; python $TMPDIR/pdftxt.py paper/10.1016-j.neuron.2018.09.030.supp8.pdf 7 | awk '$2>230' | grep -i "p =\|M1\|PMd\|cells\|Early\|Late\|^ *[0-9.]* *[0-9.]* [EF]$"
```

Result: not kept, because it reads the paper's text.

**Agent**

S5F and S6D/E asterisk/p-value positions also match the claims. Checking Figure 3/4 panel letters next.

**Agent calls Bash**

```bash
cd  for f in 3 4 6; do echo "== supp$f"; python - <<EOF
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp$f.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
for i,s in enumerate(ss):
    try: t=zlib.decompress(s)
    except Exception: continue
    if b'Tj' in t or b'TJ' in t: print(i,len(t))
EOF
done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  for f in 3 4 6; do echo "== supp$f"; python $TMPDIR/pdftxt.py paper/10.1016-j.neuron.2018.09.030.supp$f.pdf 1 2>&1 | grep -E " [A-G]$|p =|Lag|Force Trials|Model Error|Count|cells|Plan|Move|\*|Canonical|Mahal" ; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp6.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
# find re ops and color ops sequentially, with cm
toks=re.findall(r'[-\d.]+|[A-Za-z*]+|/\S+',t)
st=[];col=None;ctm=[1,0,0,1,0,0];cs=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
for k in toks:
    if re.match(r'^[-\d.]+$',k): st.append(float(k)); continue
    if k=='q': cs.append(ctm[:])
    elif k=='Q': ctm=cs.pop() if cs else ctm
    elif k=='cm' and len(st)>=6: ctm=mul(st[-6:],ctm)
    elif k in('k','rg','g','sc','scn') : col=(k,tuple(st[-4:]) if k=='k' else tuple(st[-3:]))
    elif k=='re' and len(st)>=4:
        x,y,w,h=st[-4:]; X=x*ctm[0]+ctm[4]; Y=y*ctm[3]+ctm[5]
        if 185<X<310 and 0<Y<160: print(f'{X:7.1f} {Y:7.1f} w={w*ctm[0]:5.1f} h={h*ctm[3]:6.1f} {col}')
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp6.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
toks=re.findall(r'[-\d.]+|[A-Za-z*]+|/\S+',t)
st=[];fill=None;stroke=None;ctm=[1,0,0,1,0,0];cs=[];pts=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def tr(x,y): return (x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5])
for k in toks:
    if re.match(r'^[-\d.]+$',k): st.append(float(k)); continue
    if k=='q': cs.append(ctm[:])
    elif k=='Q': ctm=cs.pop() if cs else ctm
    elif k=='cm': ctm=mul(st[-6:],ctm)
    elif k in('k','g','rg'): fill=tuple(st[-4:] if k=='k' else st[-1:] if k=='g' else st[-3:])
    elif k in('K','G','RG'): stroke=tuple(st[-4:] if k=='K' else st[-1:] if k=='G' else st[-3:])
    elif k in('m','l'): pts.append(tr(*st[-2:]))
    elif k=='re': x,y,w,h=st[-4:]; pts+= [tr(x,y),tr(x+w,y+h)]
    elif k in('f','F','f*','S','s','B','B*','b','n'):
        if pts:
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if 195<min(xs)<305 and 15<min(ys)<160 and max(xs)-min(xs)<15:
                print(f'{k:2} x {min(xs):6.1f}-{max(xs):6.1f} y {min(ys):6.1f}-{max(ys):6.1f} fill={fill} stroke={stroke}')
        pts=[]
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python $TMPDIR/pdftxt.py paper/10.1016-j.neuron.2018.09.030.supp6.pdf 1 | grep -E "Potent|Null|M1|Force|Baseline"; python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp6.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
toks=re.findall(r'[-\d.]+|[A-Za-z*]+|/\S+',t)
st=[];stroke=None;fill=None;ctm=[1,0,0,1,0,0];cs=[];pts=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def tr(x,y): return (x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5])
for k in toks:
    if re.match(r'^[-\d.]+$',k): st.append(float(k)); continue
    if k=='q': cs.append(ctm[:])
    elif k=='Q': ctm=cs.pop() if cs else ctm
    elif k=='cm': ctm=mul(st[-6:],ctm)
    elif k in('K','G','RG'): stroke=tuple(st[-4:] if k=='K' else st[-1:] if k=='G' else st[-3:])
    elif k in('k','g','rg'): fill=tuple(st[-4:] if k=='k' else st[-1:] if k=='g' else st[-3:])
    elif k in('m','l'): pts.append(tr(*st[-2:]))
    elif k in('f','F','f*','S','s','B','b','n'):
        if pts:
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if min(xs)<190 and 15<min(ys)<165 and max(xs)-min(xs)<25 and max(ys)-min(ys)<3 and (stroke!=(0.0,) or fill!=(0.0,)):
                print(f'{k} x {min(xs):6.1f}-{max(xs):6.1f} y {min(ys):6.1f} stroke={stroke} fill={fill}')
        pts=[]
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp6.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
toks=re.findall(r'[-\d.]+|[A-Za-z*]+|/\S+',t)
st=[];stroke=None;fill=None;ctm=[1,0,0,1,0,0];cs=[];pts=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def tr(x,y): return (x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5])
for k in toks:
    if re.match(r'^[-\d.]+$',k): st.append(float(k)); continue
    if k=='q': cs.append(ctm[:])
    elif k=='Q': ctm=cs.pop() if cs else ctm
    elif k=='cm': ctm=mul(st[-6:],ctm)
    elif k in('K','G','RG'): stroke=tuple(st[-4:] if k=='K' else st[-1:] if k=='G' else st[-3:])
    elif k in('k','g','rg'): fill=tuple(st[-4:] if k=='k' else st[-1:] if k=='g' else st[-3:])
    elif k in('m','l','c','v','y'): pts.append(tr(*st[-2:]))
    elif k in('f','F','f*','S','s','B','b','n'):
        if pts:
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if max(xs)<200 and 15<min(ys)<170 and (len(pts)>20 or (min(xs)>30 and max(xs)<50)):
                print(f'{k} n={len(pts)} x {min(xs):6.1f}-{max(xs):6.1f} y {min(ys):6.1f}-{max(ys):6.1f} stroke={stroke} fill={fill}')
        pts=[]
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp6.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
for w in ['(Potent)','(Null)','(M1)']:
    for m in re.finditer(re.escape(w),t):
        print(w, repr(t[max(0,m.start()-200):m.start()])[-200:])
        print()
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

Figure 6E's movement-window asterisk is on the M1 bar (legend swatch colors confirm it), so that part of fig6e's statement holds. Checking the plan/move window bars in 6D.

**Agent calls Bash**

```bash
cd  python $TMPDIR/pdftxt.py paper/10.1016-j.neuron.2018.09.030.supp6.pdf 1 | awk '$2<40 && $1<200'; python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp6.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
toks=re.findall(r'[-\d.]+|[A-Za-z*]+|/\S+',t)
st=[];ctm=[1,0,0,1,0,0];cs=[];pts=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def tr(x,y): return (x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5])
for k in toks:
    if re.match(r'^[-\d.]+$',k): st.append(float(k)); continue
    if k=='q': cs.append(ctm[:])
    elif k=='Q': ctm=cs.pop() if cs else ctm
    elif k=='cm': ctm=mul(st[-6:],ctm)
    elif k in('m','l'): pts.append(tr(*st[-2:]))
    elif k=='re': x,y,w,h=st[-4:]; pts+=[tr(x,y),tr(x+w,y+h)]
    elif k in('f','F','f*','S','s','B','b','n'):
        if pts:
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if max(xs)<200 and (150<min(ys)<162 or min(ys)<30) and max(xs)-min(xs)>4: print(k,[(round(a,1),round(b,1)) for a,b in pts][:6])
        pts=[]
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

Correction found: the 6D movement window ends at 0.40 s, not 0.45 s. Now checking which models appear in Figure S7F.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp8.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
toks=re.findall(r'[-\d.]+|[A-Za-z*]+|/\S+',t)
st=[];fill=None;stroke=None;ctm=[1,0,0,1,0,0];cs=[];pts=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def tr(x,y): return (x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5])
for k in toks:
    if re.match(r'^[-\d.]+$',k): st.append(float(k)); continue
    if k=='q': cs.append(ctm[:])
    elif k=='Q': ctm=cs.pop() if cs else ctm
    elif k=='cm': ctm=mul(st[-6:],ctm)
    elif k in('k','g','rg'): fill=tuple(round(v,2) for v in (st[-4:] if k=='k' else st[-1:] if k=='g' else st[-3:]))
    elif k in('K','G','RG'): stroke=tuple(round(v,2) for v in (st[-4:] if k=='K' else st[-1:] if k=='G' else st[-3:]))
    elif k in('m','l'): pts.append(tr(*st[-2:]))
    elif k=='re': x,y,w,h=st[-4:]; pts+=[tr(x,y),tr(x+w,y+h)]
    elif k in('f','F','f*','S','s','B','b','n'):
        if pts:
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if (355<min(xs)<520 and 280<min(ys)<420 and max(xs)-min(xs)<8 and max(ys)-min(ys)>2) or (280<min(xs)<520 and 730<min(ys)<760 and max(xs)-min(xs)<12):
                print(f'{k:2} x {min(xs):6.1f}-{max(xs):6.1f} y {min(ys):6.1f}-{max(ys):6.1f} fill={fill} stroke={stroke}')
        pts=[]
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp8.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[1]).decode('latin1')
t=re.sub(r'\((?:[^)\\]|\\.)*\)','',t)
toks=re.findall(r'-?\d*\.?\d+|[A-Za-z*]+|/\S+',t)
st=[];fill=None;stroke=None;ctm=[1,0,0,1,0,0];cs=[];pts=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def tr(x,y): return (x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5])
for k in toks:
    if re.match(r'^-?\d*\.?\d+$',k): st.append(float(k)); continue
    try:
      if k=='q': cs.append(ctm[:])
      elif k=='Q': ctm=cs.pop() if cs else ctm
      elif k=='cm': ctm=mul(st[-6:],ctm)
      elif k in('k','g','rg'): fill=tuple(round(v,2) for v in (st[-4:] if k=='k' else st[-1:] if k=='g' else st[-3:]))
      elif k in('K','G','RG'): stroke=tuple(round(v,2) for v in (st[-4:] if k=='K' else st[-1:] if k=='G' else st[-3:]))
      elif k in('m','l'): pts.append(tr(*st[-2:]))
      elif k=='re': x,y,w,h=st[-4:]; pts+=[tr(x,y),tr(x+w,y+h)]
      elif k in('f','F','f*','S','s','B','b','n'):
        if pts:
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if (355<min(xs)<520 and 280<min(ys)<420 and max(xs)-min(xs)<8 and max(ys)-min(ys)>2) or (280<min(xs)<520 and 730<min(ys)<760 and max(xs)-min(xs)<12):
                print(f'{k:2} x {min(xs):6.1f}-{max(xs):6.1f} y {min(ys):6.1f}-{max(ys):6.1f} fill={fill} stroke={stroke}')
        pts=[]
    except Exception: pts=[]
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

S7F's asterisks sit on Null-M1 and PC-M1 in CF only, so figs7f holds. Quick check of S6D/E bar colors under the asterisks.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2018.09.030.supp8.pdf','rb').read()
ss=re.findall(rb'stream\r?\n(.*?)endstream',d,re.S)
t=zlib.decompress(ss[6]).decode('latin1')
t=re.sub(r'\((?:[^)\\]|\\.)*\)','',t)
toks=re.findall(r'-?\d*\.?\d+|[A-Za-z*]+|/\S+',t)
st=[];fill=None;stroke=None;ctm=[1,0,0,1,0,0];cs=[];pts=[]
def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
def tr(x,y): return (x*ctm[0]+y*ctm[2]+ctm[4], x*ctm[1]+y*ctm[3]+ctm[5])
for k in toks:
    if re.match(r'^-?\d*\.?\d+$',k): st.append(float(k)); continue
    try:
      if k=='q': cs.append(ctm[:])
      elif k=='Q': ctm=cs.pop() if cs else ctm
      elif k=='cm': ctm=mul(st[-6:],ctm)
      elif k in('k','g','rg'): fill=tuple(round(v,2) for v in (st[-4:] if k=='k' else st[-1:] if k=='g' else st[-3:]))
      elif k in('K','G','RG'): stroke=tuple(round(v,2) for v in (st[-4:] if k=='K' else st[-1:] if k=='G' else st[-3:]))
      elif k in('m','l'): pts.append(tr(*st[-2:]))
      elif k=='re': x,y,w,h=st[-4:]; pts+=[tr(x,y),tr(x+w,y+h)]
      elif k in('f','F','f*','S','s','B','b','n'):
        if pts:
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if 60<min(xs)<380 and 330<min(ys)<430 and 3<max(xs)-min(xs)<9 and max(ys)-min(ys)>2 and k!='S':
                print(f'{k:2} x {min(xs):6.1f}-{max(xs):6.1f} y {min(ys):6.1f}-{max(ys):6.1f} stroke={stroke}')
        pts=[]
    except Exception: pts=[]
    st=[]
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

All figure-derived p-values and asterisks in the claims match the PDFs. Applying the corrections I found.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "    which the paper does not name; every CF session is computed. Open (deviation) whether the\n    diagonal (variances) enters the correlation; both are run. Reproduced when at least one CF\n    session has all its block r values at or above 0.85 - 0.085 in M1 and 0.93 - 0.093 in PMd.",
 "new_string": "    which the paper does not name; every CF session is computed. Open (deviation) whether the\n    diagonal (variances) enters the correlation; both are run. Open (deviation) which neurons the\n    r values pool, since the Results call them a representative session and the Figure S2E legend\n    says \"all combinations of neurons recorded in each of the nine CF sessions\"; readings (a) one\n    session at a time, (b) the pairs of all nine CF sessions pooled into one correlation per block.\n    Reproduced when, under reading (a), at least one CF session has all its block r values at or\n    above 0.85 - 0.085 in M1 and 0.93 - 0.093 in PMd, or, under reading (b), the pooled block r\n    values meet the same bounds."
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "    Methods, Single neuron covariance; subsample size not given, readings half and half of\n    Baseline). The paper gives no test.",
 "new_string": "    Methods, Single neuron covariance; the subsample size is not given, read as two random halves\n    of Baseline compared with each other, as in Figure S2D). The paper gives no test."
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "  source: Results, PMd to M1 mapping is unchanged throughout adaptation to a visuomotor rotation,\n    paragraph 2; Figure S3B\n  quote: Additionally",
 "new_string": "  source: Results, PMd to M1 mapping is unchanged throughout adaptation to a visuomotor rotation,\n    paragraph 2; Figure S3B (the Results cite it as Figure S2B, which shows CF example neurons; the\n    VR covariance summary is Figure S3B)\n  quote: Additionally"
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "    of -35 ms; partially reproduced when the lag is significantly negative and outside tolerance.\n    The end-of-Force lags (9 CF sessions) are reported, with their mean sign.",
 "new_string": "    of -35 ms and the mean end-of-Force lag over the 9 CF sessions (same method on a block of\n    trials from the end of Force, STAR Methods) is also negative; partially reproduced when the\n    Baseline lag is significantly negative and either it is outside tolerance or the end-of-Force\n    mean lag is not negative. The paper gives no test for the end-of-Force lags."
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "  - about: Null subspace, planning window, Early against Late Force\n    p: 0.05\n    p_relation: \"<\"",
 "new_string": "  - about: Null subspace, planning window, Early against Late Force\n    p: 0.05\n    p_relation: \"<\"\n  - about: M1, movement window, Early against Late Force (asterisk on the M1 bars of Figure 6E)\n    p: 0.05\n    p_relation: \"<\""
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "    0 s and 0.25 to 0.45 s from go cue); the blocks,",
 "new_string": "    0 s and 0.25 to 0.40 s from go cue, on an axis from -0.5 to 0.8 s); the blocks,"
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "    second reading). Reproduced when, under every reading, the null planning change is larger in\n    Force 4 at p < 0.05 and exceeds the potent and M1 planning changes in Force 4.",
 "new_string": "    second reading). Reproduced when, under every reading, the null planning change is larger in\n    Force 4 at p < 0.05 and exceeds the potent and M1 planning changes in Force 4, and the M1\n    movement-window change is larger in Force 4 at p < 0.05; partially reproduced when the null\n    planning result holds and the M1 movement result does not."
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "    Washout blocks of O2; cells selected as M6 on the Baseline training data. Two-sided two-sample",
 "new_string": "    Washout blocks of O2; cells selected as M6 on the Baseline training data. Which Baseline trials\n    train the models is not given (STAR Methods, Training the GLMs, says only \"trained the GLMs\n    using Baseline data\"); readings (a) all Baseline reward trials, (b) the last 50% of Baseline\n    reward trials, as for Force. Two-sided two-sample"
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "    or all PMd neurons (PMdsn-M1); Force as fig4d-null-m1-fails-early per monkey, Washout as",
 "new_string": "    or all PMd neurons (PMdsn-M1). The kinematic covariates are open: the STAR Methods (Covariate\n    inputs to the GLMs) say \"For Figure S7C, D, we performed a control in which we repeated the GLM\n    models for the CF task using only the velocity inputs\", while the S7C and S7D legends describe\n    single-neuron inputs only; readings (a) position, velocity and acceleration as M4, (b) velocity\n    only. Force as fig4d-null-m1-fails-early per monkey, Washout as"
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry.

**Agent calls Bash**

```bash
cd  f=claims/000688/10.1016-j.neuron.2018.09.030.yaml; tail -c 200 $f | od -c | tail -3; cat >> $f <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - figs2-covariance-preserved-example, the criterion now names as open whether the r values are per session (Results, "representative session") or pooled over the nine CF sessions (Figure S2E legend), and judges both.
  - figs3a-covariance-like-baseline-split, rewrote the garbled subsample note as two random halves of Baseline, the split Figure S2D describes.
  - figs3b-covariance-preserved-vr, the source now says the Results cite Figure S2B while the VR covariance summary is Figure S3B.
  - fig6c-null-leads-potent, the statement says output-null also led at the end of Force (Results, "during both Baseline and at the end of Force"), so the criterion now judges the end-of-Force mean lag sign as well.
  - fig6e-planning-change-in-null, the movement window read from Figure 6D is 0.25 to 0.40 s after go cue, not 0.45 s (bar ends at the 0.4 tick; axis -0.5 to 0.8 s); added the M1 movement-window p < 0.05 entry (the Figure 6E movement asterisk is on the M1 bars by the legend colors) and made the criterion judge that part of the statement.
  - fig5-washout-null-m1, the criterion now names as open which Baseline trials train the Washout models (all Baseline reward trials or the last 50%), since the Methods say only "Baseline data".
  - figs7cd-single-neuron-models, the criterion now names as open the kinematic covariates, since the Methods say the Figure S7C,D control used only velocity inputs and the legends do not.
  - checked against the figure PDFs, by text and colour positions, the model each printed p-value or asterisk belongs to in Figures 3E, 6E, S5F, S6D, S6E, S7A, S7B, S7D, S7E and S7F; all agree with the claims.
  - open, fig2d-cf-behavioral-adaptation, fig7bc-vr-behavior-similar, figs3a-covariance-like-baseline-split, figs4c-null-potent-index-centered, fig4c-null-tracks-behavior and figs7e-dimensionality-range, the paper gives no test for these qualitative findings; the session counts, t-tests, correlation and index thresholds in their criteria are judging rules of the reader, recorded as deviations.
  - open, figs5e-pot-null-similar-training, the paper gives no test for "similar accuracy"; the Kolmogorov-Smirnov test is borrowed from the Early against Late rpR2 comparisons (Figures 3E, S5F).
  - open, figs5f-rpr2-distributions, the legend calls Null-M1 significant at p = 0.04 although the paper sets p = 0.01 for all GLM comparisons; the criterion judges at 0.05 and reports 0.01.
  - open, the session counts of the Figure 2C (seven CF) and Figure 7 (five VR) legends do not match the 9 CF and 7 VR sessions of the Methods; the claims use the Methods counts.
EOF
python tools/claims_check.py $f paper/10.1016-j.neuron.2018.09.030.txt | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000688/10.1016-j.neuron.2018.09.030.yaml; sed -i 's/The kinematic covariates are open: the STAR Methods/The kinematic covariates are open. The STAR Methods/' $f; grep -n ': [^ ]' $f | grep -v '^[0-9]*:\s*\(- \)\?[a-z_]*: ' | grep -v '^[0-9]*:#' | head; python tools/claims_check.py $f paper/10.1016-j.neuron.2018.09.030.txt | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/000688/*.yaml; git status --short
```

```
M claims/000688/10.1016-j.neuron.2018.09.030.yaml
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
?? scripts
```

**Agent**

The claims file is ready for an attempt. The last check says `ready: true`, and all changes are in `claims/000688/`; nothing is committed.

**Checker result:** `claims/000688/10.1016-j.neuron.2018.09.030.yaml: 28 claims, 27 quotes, 30 statistical values, 0 problems`. It was also 0 problems before my edits, with one fewer statistical value.

The PDF pages could not be rendered as images here, so I read the figures by parsing the PDF drawing data: text positions and colour swatches. That way I matched each printed p-value and asterisk to its model in Figures 3E, 6E, S5F, S6D/E, S7A/B, S7D, S7E and S7F. Every assignment in the claims is correct.

**Changes, by claim:**
- **figs2-covariance-preserved-example:** the Results call the r values one representative session. The Figure S2E legend says they cover all nine CF sessions. The criterion now names both readings and judges both.
- **figs3a-covariance-like-baseline-split:** rewrote a garbled note. The Baseline subsample is now read as two random halves of Baseline, as Figure S2D describes.
- **figs3b-covariance-preserved-vr:** the source now says the Results cite Figure S2B, but the VR covariance summary is in Figure S3B.
- **fig6c-null-leads-potent:** the statement says output-null also led at the end of Force, but the criterion did not test that. It now also requires a negative mean lag at the end of Force.
- **fig6e-planning-change-in-null:**
  - The movement window ends at 0.40 s after the go cue, not 0.45 s; the bar in Figure 6D ends at the 0.4 tick.
  - The movement-window asterisk is on the M1 bars, going by the legend colours. I added that p < 0.05 entry, and the criterion now tests the M1 part of the statement.
- **fig5-washout-null-m1:** which Baseline trials train the Washout models is now named as open, with two readings: all Baseline reward trials, or the last 50% of them.
- **figs7cd-single-neuron-models:** the Methods say the Figure S7C,D control used velocity inputs only, and the legends don't say. The kinematic covariates are now an open detail with two readings.

**Still open (recorded in the file):**
- **No test in the paper:** for fig2d, fig7bc, figs3a, figs4c, fig4c and figs7e, the paper gives no test. The session counts, t-tests and thresholds in their criteria are the first reader's own judging rules.
- **figs5e-pot-null-similar-training:** the Kolmogorov-Smirnov test is borrowed from a different comparison in the paper.
- **figs5f-rpr2-distributions:** the legend calls p = 0.04 significant, while the paper's threshold for these comparisons is 0.01.
- **Session counts:** the Figure 2C and Figure 7 legends list 7 CF and 5 VR sessions, against 9 and 7 in the Methods. The claims use the Methods counts.

Every main finding listed in the Discussion has a claim, and every claim comes from this paper.

## End of run

41 turns, 5 minutes, result: success.
