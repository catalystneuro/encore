# yang-2025 · claims · run 42716768005

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 195
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 175 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3614867.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 876,1087p paper/10.1109-tnsre.2025.3614867.txt | grep -n -i -E "github|code|data avail|supplement|===" ; cd $TMPDIR && rm -rf sx && mkdir sx && cd sx && unzip -q -o paper/10.1109-tnsre.2025.3614867.supp.docx && python3 -c "
import re
x=open('word/document.xml').read()
paras=re.findall(r'<w:p[ >].*?</w:p>',x,re.S)
for p in paras:
    t=''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p))
    if t.strip(): print(t)
"; ls word/media
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1040,1087p paper/10.1109-tnsre.2025.3614867.txt; cat claims/fouke-2025.yaml | head -150; ls claims | head; ls papers/datasets/yang-2025.yaml && cat papers/datasets/yang-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls -t claims | head -5; f=$(ls -t claims/*.yaml | head -1); head -40 $f; grep -n "^[a-z_]*:" claims/fouke-2025.yaml; grep -n -E "kind|data:|inferred" claims/fouke-2025.yaml | sort -u -k2 | head; grep -n -E "schema|required|keys|KEYS|allowed" tools/claims_check.py | head -30
```

```
zheng-2022.yaml
zaki-2024.yaml
zhuang-2025.yaml
zhu-2022.yaml
zhai-2025.yaml
# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
# was added by the check of 2026-10-28.
#
# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
# statistics"). Figure panels of the main paper were not available as images; values in the main
# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
#
# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,80p claims/zhuang-2025.yaml; cat schemas/claims.schema.json | head -200
```

```
# - Behaviour, histology, rotarod, locomotion and slice physiology: deposited by the paper at
#   Zenodo doi:10.5281/zenodo.15258978 (files Data_ICD_Fig1&2&5&6_CognitiveAssay.zip,
#   Data_ICD_Fig1_Rotarod_PPX.xlsx, Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx,
#   Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx, Data_ICD_A77636OpenField_Raw.zip,
#   Data_ICD_Fig5_DREADDLocomotion_Raw.zip, Data_ICD_FigS6_SliceValidation.xlsx and raw images).
#   Claims on them have data elsewhere. Delay discounting cohorts: PPX Ctrl 16 and Park 31 mice;
#   A77636 Ctrl 10 and Park 16; DREADD mCherry 15, hM4Di 12, hM3Dq 12. Each session has four blocks
#   (delays 0, 3, 6, 9 s) of 5 forced delayed/large, 5 forced immediate/small and 20 free choice
#   trials; the measure is the percentage of free choice trials, omissions excluded, on which the
#   delayed/large reward was chosen.
#
# Method shared by the electrophysiology claims, from the Supplementary Materials and methods
# ("In vivo electrophysiology" and "Experimental design & statistical analysis, In vivo
# electrophysiology"): firing rates in 1 min bins; baseline -30 to 0 min; the post-drug epoch
# 240 to 300 min, split into 241-270 and 271-300 min; a unit is 'increase' type when a Wilcoxon
# signed-rank test (p < 0.01) finds a significant increase against baseline in both 30 min post
# epochs, 'decrease' when a significant decrease in both, 'no change' when neither; optical
# identification by a PSTH around laser onset, the rate
# exceeding the 99% confidence interval of baseline within 15 ms of onset and staying above it for
# at least 15 ms, with light-evoked waveforms not distinguishable from spontaneous ones.
[... 221 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p schemas/claims.schema.json
```

```
"then": {
              "required": [
                "where"
              ]
            }
          }
        ]
      }
    },
    "checks": {
      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "date",
          "kind",
          "ready"
        ],
[... 134 more lines not kept]
```

**Agent**

Full text, Methods and supplement are present; the paper links no code. Now reading figures 3 to 6 from the PDF for values the text omits.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
for i in [3,4,5,6]:
    d[i].get_pixmap(dpi=150).save(f'p{i+1}.png')
print(len(d))
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && pdftoppm -r 130 -f 4 -l 7 -png paper/10.1109-tnsre.2025.3614867.pdf pg && ls $TMPDIR/pg*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "import pypdfium2" 2>&1; python3 -c "import pypdf; print('pypdf')" 2>&1; ls .venv 2>/dev/null | head -3; pip list 2>/dev/null | grep -i -E "pdf|mupdf|pillow"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf; print('pypdf')
    ^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pypdf'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3614867.pdf",
 "pages": "4-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --target $TMPDIR/pylib pymupdf -q 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python3 -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
for i in [2,3,4,5,6]:
    d[i].get_pixmap(dpi=140).save(f'p{i+1}.png')
"; ls $TMPDIR/p*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.png"
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
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python3 -W ignore -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
p=d[5]; r=p.rect
p.get_pixmap(dpi=300, clip=fitz.Rect(r.width*0.55,r.height*0.06,r.width*0.8,r.height*0.23)).save('f4b.png')
p=d[4]; p.get_pixmap(dpi=250, clip=fitz.Rect(r.width*0.5,r.height*0.06,r.width*0.95,r.height*0.42)).save('f3.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f4b.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3614867.supp-fig-S3.png"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001212/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001212/versions/draft/info/" | python3 -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('name')); print(d.get('description')); print(d.get('assetsSummary',{}).get('numberOfSubjects'), d.get('assetsSummary',{}).get('variableMeasured'))"
```

Result: the fetched text is not kept.

**Agent**

Text is complete (version of record, main text, Methods, supplement docx with Figs S1 to S3 and Table S1). Figures 3 to 6 were read from the PDF. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/yang-2025.yaml",
 "content": "# Claims for Yang, Ni, Sun, Xing, Wang, Zhang, Zhu & Xu (2025), IEEE Trans. Neural Syst. Rehabil.\n# Eng. 33:4008-4016, doi:10.1109/TNSRE.2025.3614867, on dandiset 001212.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dandiset's data or\n# files; only its title and description on the archive were read.\n#\n# Text read: the version of record (open access, CC BY-NC-ND), PDF supplied by a person, as text\n# (paper/10.1109-tnsre.2025.3614867.txt), with its one supplement, supp1-3614867.docx (Figures S1\n# to S3 with legends and Table S1). Figures 2 to 6 were read from the PDF (pages 4 to 7) for the\n# bars, significance marks and target boxes the text does not hold; Figure S2 from its image and\n# the transcription stored with the text; Figure S3 from its image.\n#\n# Code read: none. The paper links no code and gives no code or data availability statement. It\n# names two outside MATLAB toolboxes, the MVGC toolbox for conditional multivariate Granger\n# causality (ref. 37, Barnett and Seth 2014) and the HFO App (ref. 50), and says statistics are in\n# the figure legends; the software for statistics is not named.\n#\n# Data the paper used (Methods A to C). Male Sprague-Dawley rats, lithium-pilocarpine model of\n# temporal lobe epilepsy; 7 rats (R1 to R7) analysed, of 44 treated. Four depth electrodes per\n# rat, right hemisphere, DG, CA1, CA3 and ANT, each a recording strand and a bipolar stimulation\n# pair; LFP at 1 kHz (Intan RHD2132). Each rat had 4 baseline groups and 4 stimulation groups,\n# alternating (baseline, stimulation, baseline, ...), each recorded 5 to 10 days with at least 6\n# seizures. A stimulation group stimulates one site (each site once per rat) on closed-loop\n# seizure detection (cascade AdaBoost); 130 Hz biphasic pulses, 100 us, 200 uA, 5 s trains, 5 s\n# pause, repeated while seizure activity is detected. Each stimulation group's site was chosen at\n# random; it is a target group when the site matches the target computed from the preceding\n# baseline group's seizures (the node with significantly high weighted causal flow, cf_w, over the\n# first 5 s of seizure onset), and a non-target group otherwise. By Figure S2 there are 8 target\n# and 20 non-target groups (R2 has two target groups; every other rat one). The dandiset's\n# description matches (7 rats, 4-channel LFP, 4 baseline and 4 stimulation groups, 5 to 10 days,\n# at least 6 seizures per group).\n#\n# Measured variables: seizure duration, seizure frequency (seizures per hour), seizure duration\n# proportion (seizure time over recording time), PSD ratio by band, interictal spike (IIS) rate,\n# ripple (80-250 Hz) and fast ripple (250-500 Hz) rates.\n#\n# Method from the paper, shared by several claims.\n# - GC network (Methods B, C). cf_w from GC matrices of the 4 LFP channels (MVGC), over the first\n#   5 s after seizure onset in 1 s windows with 0.5 s overlap (9 windows). Target = node with\n#   significantly high positive cf_w.\n# - Normalization (Results B; Figure 6 legend). Stimulation-group values are normalized to the\n#   preceding baseline group (\"Each baseline group served as a reference for subsequent stimulation\n#   groups\"); ictal HFO rates are normalized to pre-stimulation data.\n# - PSD (Methods D). Welch PSD; bands delta 0.5-4, theta 4-8, alpha 8-12, beta 12-30, gamma 30-90,\n#   high gamma 90-120 Hz; band PSD sum over total PSD sum = PSD ratio. Stimulation groups, pre =\n#   seizure onset to stimulation start, post = 5 s after the first train; baseline groups, pre =\n#   0 to 5 s after onset, post = 10 to 15 s after onset.\n# - IIS (Methods F). Per channel, positive or negative peaks; peaks less than 200 ms apart keep the\n#   larger; peak width at most 100 ms; absolute height above mean + 5 SD of baseline. Interictal\n#   segments of 30 min at least one hour from seizures, no visible motion artifact, 10 to 15\n#   segments in early and late stages.\n# - HFO (Methods E). Short line length detector of the HFO App, then manual review; six 30 min\n#   interictal segments per recorded day.\n# - Statistics (Methods G). Mean +- SEM; paired t-test or Mann-Whitney for two samples;\n#   Kruskal-Wallis for several independent samples; alpha 0.05.\n#\n# Details these sources leave open, with the readings allowed, used by several claims.\n# - Seizure onset and end. The paper gives no rule for marking them offline. Readings are (a)\n#   seizure times deposited with the data; (b) onset and end marked from the LFP by a stated\n#   amplitude or line-length rule, as an assumption. Seizure duration is end minus onset.\n# - The sign of cf_w. Methods B defines it as \"the difference between the weighted in-degree and\n#   out-degree\", but says high positive values mean strong driving and Figure 2 highlights the\n#   \"strongest causal outflows\". Readings are (a) out-strength minus in-strength (causal outflow,\n#   as the interpretation and Figure 2 imply); (b) in-strength minus out-strength, as worded.\n# - GC settings. The VAR model order, the use of conditional (4-variable) against pairwise GC, any\n#   filtering, and how the 9 windows are combined are not given. Readings for combining are (a)\n#   cf_w per window, then averaged; (b) GC matrices averaged, then cf_w. Model order by AIC or BIC\n#   (the MVGC toolbox's own selection), capped at a stated maximum, is a standard choice. The test\n#   behind \"significantly high\" cf_w is not given; readings are (a) the node with the largest mean\n#   cf_w over the group's seizures; (b) a node whose cf_w over seizures is significantly above that\n#   of the other nodes (Kruskal-Wallis then pairwise Mann-Whitney, p < 0.05), more than one node\n#   allowed when they tie (Figure S2 lists two for some groups).\n# - Normalized values. The formula is not given. Readings are (a) relative change, each\n#   stimulation-group value divided by the preceding baseline group's mean, minus 1; (b) difference\n#   from the baseline mean (for seizure frequency in times/h, which is the unit Figure 3C prints);\n#   (c) z-score against the baseline group's seizures. Reading (a) fits the range of Figure 3B\n#   (all values within -1 and 1).\n# - Unit of analysis for target against non-target. Readings are (a) seizures pooled across rats\n#   (Figure 3B plots per-seizure points); (b) stimulation groups (8 target, 20 non-target).\n# - The pooled seizures for a stimulation group. Readings are (a) all its seizures; (b) only those\n#   that received stimulation.\n# - Channels. For PSD, IIS and HFO, which channels enter is not stated. Readings are (a) all four\n#   channels, each channel a sample; (b) the stimulated channel only (for PSD and ictal HFO).\nschema_version: 2\npaper: doi:10.1109/tnsre.2025.3614867\nclaims:\n- id: tables1-network-stable-short-term\n  statement: In every rat the cf_w vectors of seizure onset correlate more strongly between\n    seizures of the same baseline group than between seizures of different baseline groups\n    (Pearson r, intra-group against inter-group, Mann-Whitney).\n  source: Methods C, paragraph 2; Table S1; Figure S3\n  quote: Results indicated that seizures’ brain network and electrophysiological characteristics\n    were relatively consistent in the short term; significant differences were also observed\n    between groups (see Fig. S3 and Table S1 in Supplementary materials).\n  statistics:\n  - about: intra-group against inter-group r, R1, R2, R3, R5, R6 (each)\n    test: Mann-Whitney\n    p: 0.001\n    p_relation: \"<\"\n  - about: intra-group against inter-group r, R4\n    test: Mann-Whitney\n    p: 0.05\n    p_relation: \"<\"\n  - about: intra-group against inter-group r, R7 (printed \"0.71±0.41* **\", read as two stars)\n    test: Mann-Whitney\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - {quantity: R1 intra-group r, value: 0.72, tolerance: 0.30}\n  - {quantity: R1 inter-group r, value: -0.11, tolerance: 0.55}\n  - {quantity: R2 intra-group r, value: 0.47, tolerance: 0.57}\n  - {quantity: R2 inter-group r, value: 0.09, tolerance: 0.56}\n  - {quantity: R3 intra-group r, value: 0.77, tolerance: 0.19}\n  - {quantity: R3 inter-group r, value: 0.59, tolerance: 0.34}\n  - {quantity: R4 intra-group r, value: 0.81, tolerance: 0.46}\n  - {quantity: R4 inter-group r, value: 0.79, tolerance: 0.46}\n  - {quantity: R5 intra-group r, value: 0.74, tolerance: 0.34}\n  - {quantity: R5 inter-group r, value: 0.71, tolerance: 0.28}\n  - {quantity: R6 intra-group r, value: 0.61, tolerance: 0.34}\n  - {quantity: R6 inter-group r, value: 0.36, tolerance: 0.47}\n  - {quantity: R7 intra-group r, value: 0.81, tolerance: 0.36}\n  - {quantity: R7 inter-group r, value: 0.71, tolerance: 0.41}\n  criterion: Tolerances are the SDs Table S1 reports (mean +- SD over seizure pairs). From Methods\n    C and the Figure S3 legend, for each seizure of the four baseline groups the cf_w vector (4\n    nodes) over the first 5 s after onset; Pearson r between the vectors of every two seizures;\n    intra-group pairs are those within one baseline group, inter-group pairs those across groups;\n    Mann-Whitney test of intra against inter per rat. Open, with readings named, are (a) each\n    unordered pair once, or (b) every off-diagonal cell of the matrix (each pair twice), and\n    whether self-pairs (r = 1) enter the intra-group set, (c) excluded or (d) included; the cf_w\n    sign and window-combination readings of the opening comment apply. Reproduced when, under one\n    reading, intra-group r exceeds inter-group r with Mann-Whitney p < 0.05 in all 7 rats and at\n    least 10 of the 14 means lie within tolerance; partially reproduced when the direction and\n    significance hold in at least 5 rats.\n- id: fig2-r1-target-shifts\n  statement: In rat R1 the node with the highest cf_w at seizure onset changes across the four\n    baseline groups (ANT, ANT, CA3, DG), while the cf_w pattern is consistent within each group.\n  source: Results A, paragraph 1; Figure 2A-B\n  quote: For instance, in rat R1, as shown in Fig. 2A, the c f w vector values within one baseline\n    group remain relative consistent, indicating stable network’s connectivity over short periods.\n    However, over time, the structure and strength of the brain network connections change\n    significantly, reflecting long-term differences (Fig. 2B).\n  expected:\n  - {quantity: R1 seizures in baseline groups 1 to 4 (Figure 2A columns), value: 34, tolerance: 0}\n  criterion: The target nodes are those boxed in Figure 2A and red in Figure 2B (baseline 1 ANT,\n    2 ANT, 3 CA3, 4 DG), which agree with the R1 row of Figure S2. Figure 2A shows 9, 9, 7 and 9\n    seizures; a different count is reported and does not decide the claim. Computed as in\n    tables1-network-stable-short-term, under the GC readings of the opening comment. Reproduced\n    when, under one reading, the node with the highest mean cf_w in each of R1's four baseline\n    groups is the one named; partially reproduced when three of the four match.\n- id: figs2-target-assignment\n  statement: Across the 7 rats, the targets computed from each baseline group's seizures, compared\n    with the site stimulated in the next group, give 8 target and 20 non-target stimulation groups\n    as Figure S2 shows.\n  source: Figure S2; Methods C, paragraph 3\n  inferred: Read from Figure S2 (image and the transcription stored with the text); no sentence\n    lists the targets. Per rat, baseline 1 to 4 targets and the site then stimulated are R1 ANT to\n    CA1, ANT to CA3, CA3 to ANT, DG to DG; R2 DG and CA1 to DG, CA1 to ANT, CA1 to CA1, ANT to CA3;\n    R3 CA3 to CA3, CA3 to ANT, ANT to DG, CA3 and ANT to CA1; R4 CA3 to CA1, CA3 to DG, CA3 to ANT,\n    CA3 to CA3; R5 CA3 and ANT to ANT, ANT to DG, ANT to CA1, ANT to CA3; R6 ANT to CA1, CA1 and CA3\n    to ANT, CA3 to DG, CA3 to CA3; R7 ANT to DG, ANT to ANT, ANT to CA1, ANT to CA3. Target groups\n    are R1 DG, R2 DG and CA1, R3 CA3, R4 CA3, R5 ANT, R6 CA3, R7 ANT, as boxed in Figure 3A.\n  expected:\n  - {quantity: target stimulation groups, value: 8, tolerance: 0}\n  - {quantity: non-target stimulation groups, value: 20, tolerance: 0}\n  criterion: The stimulated site of each group and the group order are taken from the dataset. The\n    targets are recomputed under the GC and significance readings of the opening comment. The\n    labels of Figure S2 are used for all later claims whatever this claim's outcome. Reproduced\n    when, under one reading, at least 24 of the 28 baseline groups give the Figure S2 target set\n    (a group with two listed targets matches when the computed set equals it, or under reading (a)\n    when the top node is one of them) and the target and non-target labels of all 28 stimulation\n    groups agree with Figure S2; partially reproduced when at least 18 baseline groups match.\n- id: fig3a-target-reduces-each-rat\n  statement: In each of the 7 rats, stimulation of the target site reduced normalized seizure\n    duration below the preceding baseline.\n  source: Results B, paragraph 1; Figure 3A\n  quote: At the individual level, 130 Hz highfrequency stimulation of the target sites\n    consistently reduced seizure duration.\n  depends_on:\n  - figs2-target-assignment\n  criterion: Seizure duration of each seizure in the 8 target groups, normalized to the preceding\n    baseline group under the readings of the opening comment. Reproduced when, under one reading,\n    the mean normalized duration is below zero (duration below the baseline mean) in all 8 target\n    groups; partially reproduced in 6 or 7. Figure 3A shows R1 DG near -0.10, R2 DG -0.37 and CA1\n    -0.09, R3 CA3 -0.23, R4 CA3 -0.14, R5 ANT -0.33, R6 CA3 -0.21, R7 ANT -0.13 (read from the\n    bars, reported for comparison, not judged).\n- id: fig3a-nontarget-can-lengthen\n  statement: Stimulation of some non-target sites increased seizure duration above the preceding\n    baseline.\n  source: Results B, paragraphs 1 and 2; Figure 3A\n  quote: In some cases, non-target sites stimulation ... increased seizure duration, worsening the\n    severity of seizures.\n  depends_on:\n  - figs2-target-assignment\n  criterion: Normalized as in fig3a-target-reduces-each-rat. Figure 3A shows positive means for\n    non-target R1 CA3 and ANT, R2 CA3, R3 DG and ANT, R4 DG and ANT, R5 CA1, R6 DG, R7 DG (10 of\n    20, read from the bars). Reproduced when, under one reading, at least 5 of the 20 non-target\n    groups have a positive mean normalized duration; not reproduced when fewer than 2 do. The\n    count, and which groups, are reported.\n- id: fig3a-per-rat-site-differences\n  statement: Within rats R2, R3, R4, R5 and R7 the four stimulation sites differ in normalized\n    seizure duration (Kruskal-Wallis), while in R1 and R6 no pair of sites differs.\n  source: Figure 3A\n  inferred: Read from the significance bars of Figure 3A, whose legend names the KW test; no\n    sentence states which pairs differ. As read, R2 DG against CA3 (p < 0.001) and CA3 against\n    ANT (p < 0.01); R3 DG against CA1 (p < 0.01), DG against CA3 (p < 0.001), CA3 against ANT\n    (p < 0.05); R4 DG against CA1 (p < 0.05), DG against CA3 (p < 0.01); R5 CA1 against CA3\n    (p < 0.05), CA1 against ANT (p < 0.01); R7 DG against CA3 (p < 0.05), DG against ANT (p < 0.01).\n  statistics:\n  - about: four sites within each rat\n    test: Kruskal-Wallis\n    p: 0.05\n    p_relation: \"<\"\n    n: seizures of each rat's four stimulation groups\n  depends_on:\n  - figs2-target-assignment\n  criterion: Per rat, a Kruskal-Wallis test of per-seizure normalized durations across the four\n    stimulation groups, then pairwise post hoc tests. The post hoc test is not named; readings are\n    (a) Dunn's test with Bonferroni-type adjustment (the usual post hoc for KW); (b) Dunn's test\n    unadjusted. Reproduced when, under one reading, at least 8 of the 11 significant pairs listed\n    are significant and R1 and R6 have none; partially reproduced when at least 5 are.\n- id: fig3a-target-vs-nontarget-total\n  statement: Pooled over rats, target-site stimulation shortened normalized seizure duration\n    (-0.26 +- 0.03) significantly more than non-target stimulation (0.038 +- 0.03).\n  source: Results B, paragraph 1; Figure 3A, Total panel\n  quote: Overall, target site stimulation (normalized seizure duration reduction −0.26 ± 0.03)\n    significantly shortened seizure duration compared to non-target site stimulation (normalized\n    seizure duration reduction 0.038 ± 0.03).\n  statistics:\n  - test: Mann-Whitney\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - {quantity: target stimulation normalized seizure duration, value: -0.26, tolerance: 0.03}\n  - {quantity: non-target stimulation normalized seizure duration, value: 0.038, tolerance: 0.03}\n  depends_on:\n  - figs2-target-assignment\n  criterion: Tolerances are the SEMs reported. Normalization, unit of analysis and seizure set\n    under the readings of the opening comment; Mann-Whitney test of target against non-target.\n    Reproduced when, under one reading, both means are within tolerance and the test gives\n    p < 0.001 with target lower; partially reproduced when target is lower with p < 0.05 but a mean\n    falls outside tolerance or p is between 0.001 and 0.05.\n- id: fig3a-some-nontarget-shorten\n  statement: Five non-target stimulations (R2 ANT, R3 CA1, R4 CA1, R5 CA3, R7 CA3) also\n    significantly shortened seizure duration, but less than the target site of the same rat.\n  source: Results B, paragraph 1; Figure 3A\n  quote: Although some nontarget site stimulations1 (R2’s ANT, R3’s CA1, R4’s CA1, R5’s CA3, and\n    R7’s CA3) also significantly shortened seizure duration, they were generally less effective\n    than target sites.\n  depends_on:\n  - figs2-target-assignment\n  criterion: The test for \"significantly shortened\" is not given; Figure 3A marks only comparisons\n    between sites. Readings are (a) Mann-Whitney of the group's seizure durations against those of\n    the preceding baseline group; (b) one-sample Wilcoxon signed-rank of the normalized durations\n    against zero; (c) one-sample t-test of the normalized durations against zero; alpha 0.05\n    (Methods G). Reproduced when, under one reading, at least 4 of the 5 named groups are\n    significantly shorter than baseline and in at least 4 of the 5 rats the mean normalized\n    duration of the named group is above (less negative than) that of the rat's target group (for\n    R2 the DG target, the more effective of its two); partially reproduced when 3 of each hold.\n    Which other non-target groups also pass is reported.\n- id: fig3b-same-site-target-vs-nontarget\n  statement: For the same site, stimulation as a target shortened normalized seizure duration more\n    than stimulation of that site as a non-target, significantly for DG, CA3 and ANT but not CA1.\n  source: Figure 3B\n  quote: (B) Comparison of seizure duration reduction when the same stimulation site served as both\n    the target and non-target stimulation site.\n  statistics:\n  - about: DG, target against non-target\n    p: 0.001\n    p_relation: \"<\"\n  - about: CA3, target against non-target\n    p: 0.001\n    p_relation: \"<\"\n  - about: ANT, target against non-target\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - figs2-target-assignment\n  criterion: Per site, per-seizure normalized durations of target groups at that site against\n    non-target groups at that site, pooled across rats (Figure 3B plots per-seizure points). Target\n    groups by site are DG (R1, R2), CA1 (R2), CA3 (R3, R4, R6), ANT (R5, R7). The test is not\n    named in the legend; following Methods G for independent samples, Mann-Whitney is used, with\n    an unpaired t-test shown as a variant. Reproduced when, under one normalization reading, DG,\n    CA3 and ANT each show target lower with p < 0.05; partially reproduced for two of the three.\n    The CA1 result is reported, and the claim's CA1 part holds when it is not significant.\n- id: seizure-duration-proportion\n  statement: Target stimulation reduced normalized seizure duration proportion (-0.06 +- 0.04)\n    significantly compared with non-target stimulation (0.36 +- 0.14).\n  source: Results B, paragraph 2\n  quote: As shown in Fig. 3B, target site stimulation significantly reduced seizure duration\n    proportion (−0.06 ± 0.04, p < 0.05) compared to non-target stimulation (0.36 ± 0.14), likely\n    due to the substantial reduction in seizure duration.\n  statistics:\n  - p: 0.05\n    p_relation: \"<\"\n  expected:\n  - {quantity: target stimulation normalized seizure duration proportion, value: -0.06, tolerance: 0.04}\n  - {quantity: non-target stimulation normalized seizure duration proportion, value: 0.36, tolerance: 0.14}\n  depends_on:\n  - figs2-target-assignment\n  criterion: Tolerances are the SEMs reported. Seizure duration proportion is total seizure time\n    over total recording time of a group (Results B), so the unit is the stimulation group (8\n    target, 20 non-target), normalized to the preceding baseline group's proportion under readings\n    (a) relative change or (b) difference. The text cites Figure 3B, which plots normalized seizure\n    duration by site, not this quantity; no figure shows these values. The test is not named;\n    Mann-Whitney (Methods G, as used in Figure 3A and 3C) is used. Reproduced when, under one\n    reading, both means lie within tolerance and target is lower with p < 0.05; partially\n    reproduced when target is lower with p < 0.05 but a mean falls outside tolerance.\n- id: fig3c-frequency-no-difference\n  statement: Seizure frequency change did not differ between target (0.02 +- 0.17 times/h) and\n    non-target stimulation (-0.11 +- 0.19 times/h).\n  source: Results B, paragraph 2; Figure 3C\n  quote: There was no significant difference in seizure frequency improvement between target site\n    stimulation (0.02 ± 0.17 times/h) and nontarget site stimulation (−0.11 ± 0.19 times/h)\n    (Fig. 3C).\n  expected:\n  - {quantity: target stimulation normalized seizure frequency, value: 0.02, tolerance: 0.17, unit: seizures/h}\n  - {quantity: non-target stimulation normalized seizure frequency, value: -0.11, tolerance: 0.19, unit: seizures/h}\n  depends_on:\n  - figs2-target-assignment\n  criterion: A claim of absence, judged on the paper's test, Mann-Whitney (Figure 3C legend) at\n    p < 0.05, of target against non-target stimulation groups (seizures per hour of recording,\n    one value per group), normalized to the preceding baseline group as a difference in times/h,\n    the unit Figure 3C prints (relative change shown as a variant). Reproduced when the test is not\n    significant; not reproduced when it is. The difference of means and p are reported, and whether\n    the means lie within tolerance.\n- id: fig4b-psd-target-bands\n  statement: After target stimulation the change in PSD ratio was larger in low bands (alpha, and\n    theta or beta) and more negative in gamma than after sham (baseline) or non-target stimulation.\n  source: Results C, paragraph 2; Figure 4B; Discussion, paragraphs 1 and 4\n  quote: After target site stimulation, the proportion of PSD in the alpha and beta bands\n    significantly increased (p < 0.05), while the gamma band proportion significantly decreased\n    (p < 0.05) compared to baseline and non-target stimulation groups.\n  statistics:\n  - about: theta, as marked in Figure 4B\n    test: Kruskal-Wallis\n    p: 0.05\n    p_relation: \"<\"\n  - about: alpha, as marked in Figure 4B\n    test: Kruskal-Wallis\n    p: 0.01\n    p_relation: \"<\"\n  - about: gamma, as marked in Figure 4B\n    test: Kruskal-Wallis\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - figs2-target-assignment\n  criterion: The bands that rise disagree within the paper. The Results text says alpha and beta;\n    Figure 4B marks theta (p < 0.05), alpha (p < 0.01) and gamma (p < 0.01), and the Abstract and\n    Discussion say theta and alpha. Readings are (i) alpha and theta up, gamma down (Figure 4B,\n    Discussion); (ii) alpha and beta up, gamma down (Results text). Method from Methods D, Welch PSD\n    ratios per band in the pre and post windows given in the opening comment, for baseline (sham),\n    target and non-target seizures. Open, with readings, are the change measure ((a) (post - pre) /\n    pre of the ratio; (b) log2(post / pre); (c) post - pre; Figure 4B's gamma mean near -1.3 is\n    impossible as a mean relative change, so (a) may not be what was plotted); the Welch segment\n    length (1 s and 0.5 s Hann windows with 50% overlap are the standard choices); the total\n    range ((a) 0.5 to 120 Hz, the bands' span and Figure 4C's axis; (b) 0 to 500 Hz); channels as\n    in the opening comment; the unit (seizure-channel pairs pooled). Test, Kruskal-Wallis across\n    the three conditions (Figure 4B legend) with Dunn's post hoc. Reproduced when, under one\n    reading of the method and one of the bands, target differs from both sham and non-target in\n    the named direction with p < 0.05 in all three bands; partially reproduced when alpha and\n    gamma hold.\n- id: fig4b-psd-other-bands-unchanged\n  statement: In the other bands (delta and high gamma, and whichever of theta and beta is not\n    named as changed) the change in PSD ratio did not differ between conditions.\n  source: Results C, paragraph 2; Figure 4B\n  quote: No significant differences were found in other frequency bands.\n  depends_on:\n  - figs2-target-assignment\n  criterion: A claim of absence, judged on the paper's test, Kruskal-Wallis across sham, target and\n    non-target (Figure 4B legend) at p < 0.05, computed as in fig4b-psd-target-bands. Delta and\n    high gamma are judged in every reading; beta under reading (i) and theta under reading (ii).\n    Reproduced when no judged band shows a significant difference under the reading that\n    fig4b-psd-target-bands adopts (both shown when that claim was decided by neither); not\n    reproduced when any does. Effect sizes are reported.\n- id: fig5b-iis-post-seizure\n  statement: The IIS rate 15 s to 45 s after seizures was lower after target stimulation than\n    after non-target stimulation.\n  source: Results D, paragraph 1; Figure 5B\n  quote: Target stimulation significantly reduced the IIS rate within 15s to 45s post-seizure\n    compared to non-target stimulation (Fig. 5B).\n  statistics:\n  - p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - figs2-target-assignment\n  criterion: IIS detected as in Methods F on all channels, in the 180 s before seizure onset and\n    the 180 s after seizure end (Figure 5B time axis), as a rate per second. Open, with readings,\n    are the bin width ((a) 1 s; (b) 5 s; Figure 5B curves are fine-grained), the baseline for the\n    5 SD threshold ((a) the 180 s pre-seizure stretch; (b) the interictal segments of Methods F),\n    the peak width measure (width at half prominence, a standard choice), and the test and its\n    unit, which the legend does not name ((a) Mann-Whitney of per seizure-channel mean rates over\n    15 to 45 s; (b) paired t-test across the time bins of 15 to 45 s, target curve against\n    non-target curve, as the inset suggests). Reproduced when, under one reading, target is lower\n    with p < 0.001; partially reproduced when target is lower with p < 0.05.\n- id: fig5c-interictal-iis-no-difference\n  statement: Interictal IIS rates did not differ between stimulated and non-stimulated sites in\n    either target or non-target stimulation groups.\n  source: Results D, paragraph 2; Figure 5C\n  quote: During the interictal period, IIS rate at stimulated and non-stimulated sites in both\n    target and non-target stimulation groups showed no significant differences (Fig. 5C).\n  depends_on:\n  - figs2-target-assignment\n  criterion: A claim of absence. IIS rates from 30 min interictal segments as in Methods F, per\n    channel, in four sets (target group stimulated site, target group other sites, non-target\n    group stimulated site, non-target group other sites). The legend names no test; Methods G\n    gives Kruskal-Wallis for several independent samples, which is the test judged, at p < 0.05,\n    with pairwise Mann-Whitney shown as a variant. The unit (per segment-channel, or per group and\n    channel mean) is open; both are shown. Reproduced when the Kruskal-Wallis test is not\n    significant; not reproduced when it is. Medians (Figure 5C shows about 0.3 to 0.4 per s) are\n    reported.\n- id: fig5d-iis-seizure-correlation\n  statement: Interictal IIS rate correlates positively with seizure frequency (r = 0.57).\n  source: Results D, paragraph 2; Figure 5D\n  quote: Fig. 5D shows a positive correlation between interictal IIS rate and seizure frequency\n    (r = 0.57), indicating that higher interictal IIS rate may predict increased seizure risk.\n  expected:\n  - {quantity: Pearson r of z-scored IIS rate and seizure rate, value: 0.57, tolerance: 0.057}\n  criterion: Figure 5D plots z-scored IIS rate (per s) against z-scored seizure rate (per h), with\n    about 50 points. Pearson correlation (the paper's correlation method, Methods C). The unit of a\n    point and the z-scoring are open; readings are (a) one point per recording day, z-scored within\n    rat; (b) one point per group (baseline and stimulation, 56 groups), z-scored within rat;\n    (c) as (a) or (b) z-scored over all rats. Reproduced when, under one reading, r is within\n    tolerance and positive; partially reproduced when r is positive and significant (p < 0.05) but\n    outside tolerance.\n- id: fig6cd-interictal-hfo-no-difference\n  statement: Interictal ripple and fast ripple rates, normalized to the preceding baseline, did not\n    differ between target and non-target stimulation.\n  source: Results E, paragraph 1; Figure 6C-D\n  quote: Results revealed no significant differences in ripples and fast ripples during the\n    interictal period between target stimulation and non-target stimulation (Fig. 6C, D)\n  depends_on:\n  - figs2-target-assignment\n  criterion: A claim of absence, judged on the paper's test, the paired t-test of the Figure 6\n    legend, at p < 0.05, for ripples and fast ripples separately. HFOs detected by short line\n    length (HFO App, ref. 50) in six 30 min interictal segments per day; the window length,\n    threshold and filter are not given, so the HFO App defaults are used, and the manual review\n    cannot be repeated (automatic detections are used, a deviation). Fast ripples at 1 kHz sampling\n    are filtered from 250 Hz to just below the 500 Hz Nyquist limit. Rates normalized to the\n    preceding baseline group (relative change). The pairing is not defined, as the groups are\n    independent; readings are (a) by rat, each rat's target-group mean against the mean of its\n    non-target groups; (b) unpaired t-test across groups. Reproduced when the test is not\n    significant for either band under the paired reading (a); not reproduced when it is. Means and\n    p under both readings are reported.\n- id: fig6e-ictal-ripples-no-difference\n  statement: During seizures, ripple rates normalized to pre-stimulation did not differ between\n    target and non-target stimulation.\n  source: Results E, paragraph 2; Figure 6E\n  quote: During the ictal period, electrical stimulation showed limited effects on ripple\n    regulation, with no significant difference between target and non-target stimulation.\n  depends_on:\n  - figs2-target-assignment\n  criterion: A claim of absence, judged on the paper's test, the paired t-test of the Figure 6\n    legend, at p < 0.05, target against non-target. Ictal ripple rates in the post window normalized\n    to the pre window (relative change); the windows are not stated for HFOs and are taken from\n    Methods D (pre from onset to stimulation start, post 5 s after the first train; for baseline\n    seizures 0 to 5 s and 10 to 15 s), as Figure 6E-F also shows a Baseline group. Pairing readings\n    as in fig6cd-interictal-hfo-no-difference. Reproduced when the test is not significant under\n    reading (a); not reproduced when it is.\n- id: fig6f-ictal-fast-ripples-reduced\n  statement: During seizures, target stimulation reduced the fast ripple rate, normalized to\n    pre-stimulation, compared with baseline and with non-target stimulation.\n  source: Results E, paragraphs 2 and 3; Figure 6F\n  quote: However, Fig. 6F demonstrates that target stimulation significantly reduced fast ripple\n    frequency, closely associated with the pathological processes of epileptic seizures [61].\n  statistics:\n  - about: target against baseline\n    test: paired T-test\n    p: 0.05\n    p_relation: \"<\"\n  - about: target against non-target\n    test: paired T-test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - figs2-target-assignment\n  criterion: Computed as in fig6e-ictal-ripples-no-difference, for fast ripples. Figure 6F shows\n    target near -0.25, baseline near 0.2 and non-target near 0.1 (read from the plot, for\n    comparison only). Reproduced when, under one pairing reading, the target mean is below both\n    others with p < 0.05 for each comparison; partially reproduced when one comparison holds.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2025.yaml",
 "old_string": "  quote: Overall, target site stimulation (normalized seizure duration reduction −0.26 ± 0.03)\n    significantly shortened seizure duration compared to non-target site stimulation (normalized\n    seizure duration reduction 0.038 ± 0.03).",
 "new_string": "  quote: Overall, target site stimulation ... significantly shortened seizure duration compared to\n    non-target site stimulation"
}
```

```
The file claims/yang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/yang-2025.yaml paper/10.1109-tnsre.2025.3614867.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -E "—|rather" claims/yang-2025.yaml; grep -v "^#" claims/yang-2025.yaml | grep -n ": .*: " | head; git status --short claims/
```

```
26:  - {quantity: R1 intra-group r, value: 0.72, tolerance: 0.30}
27:  - {quantity: R1 inter-group r, value: -0.11, tolerance: 0.55}
28:  - {quantity: R2 intra-group r, value: 0.47, tolerance: 0.57}
29:  - {quantity: R2 inter-group r, value: 0.09, tolerance: 0.56}
30:  - {quantity: R3 intra-group r, value: 0.77, tolerance: 0.19}
31:  - {quantity: R3 inter-group r, value: 0.59, tolerance: 0.34}
32:  - {quantity: R4 intra-group r, value: 0.81, tolerance: 0.46}
33:  - {quantity: R4 inter-group r, value: 0.79, tolerance: 0.46}
34:  - {quantity: R5 intra-group r, value: 0.74, tolerance: 0.34}
35:  - {quantity: R5 inter-group r, value: 0.71, tolerance: 0.28}
?? claims/yang-2025.yaml
```

**Agent**

I wrote `claims/yang-2025.yaml`, and the quote checker reports 19 claims, 17 quotes, 15 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record, with its one supplement (`supp1-3614867.docx`: Figures S1 to S3 and Table S1). I read Figures 2 to 6 from the PDF and Figures S2 and S3 from their images. The paper links no code and has no code or data availability statement. It names two outside MATLAB toolboxes: MVGC for the Granger causality network and the HFO App for high-frequency oscillation detection.

**Claims:**
- **Counts:** 19 claims. 17 have quotes and 2 are marked `inferred`: the target assignment read from Fig. S2, and the pairs of sites that differ within each rat, read from the bars of Fig. 3A.
- **Statistics:** 15 entries, from Table S1, Fig. 3, Fig. 4B, Fig. 5B and Fig. 6F.
- **Criteria:** all 19 claims have one. 7 are claims of absence, each judged on the paper's own test.
- **Coverage:** network stability (Table S1, Fig. 2), target selection (Fig. S2), seizure duration, duration proportion and frequency (Fig. 3), PSD ratio by band (Fig. 4), interictal spike rate (Fig. 5) and ripples and fast ripples (Fig. 6).

**Details the paper leaves open, and the readings named:**
- **Seizure onset and end:** no offline rule. (a) seizure times deposited with the data; (b) a stated amplitude or line-length rule, as an assumption.
- **Sign of the causal flow measure (cf_w):** the Methods define it as in-degree minus out-degree, but the text and Fig. 2 treat it as outflow. (a) out minus in; (b) in minus out, as worded.
- **Granger causality settings:**
  - Model order is not given; selection by AIC or BIC is used as a standard choice.
  - How the 9 windows are combined: (a) cf_w per window, then averaged; (b) matrices averaged, then cf_w.
  - The test behind a "significantly high" cf_w: (a) the node with the highest mean; (b) Kruskal-Wallis then pairwise tests, allowing ties.
- **Normalization formula:** (a) relative change; (b) difference from the baseline mean; (c) z-score.
- **Unit of analysis:** (a) seizures pooled across rats; (b) stimulation groups (8 target, 20 non-target).
- **Seizures counted per stimulation group:** all of them, or only those that received stimulation.
- **Channels:** all four, or the stimulated one only.
- **Fig. 3A and Fig. 3B:**
  - The post hoc test after Kruskal-Wallis is not named: Dunn's test, adjusted or unadjusted.
  - The test behind "significantly shortened" for the five non-target sites: Mann-Whitney against baseline, Wilcoxon against zero, or a t-test against zero.
  - Fig. 3B's test is not named; Mann-Whitney is used, with a t-test as a variant.
- **PSD:**
  - The change measure: relative change, log ratio or difference. The plotted gamma mean of about -1.3 cannot be a mean relative change.
  - Welch segment length is not given; standard choices are used.
  - The total frequency range: 0.5 to 120 Hz, or 0 to 500 Hz.
- **Interictal spikes:**
  - The rate's bin width: 1 s or 5 s.
  - The baseline for the 5 SD threshold: the 180 s before the seizure, or the interictal segments.
  - The test for Fig. 5B: Mann-Whitney per seizure and channel, or a paired test over time bins.
  - The unit of a point in Fig. 5D (per day or per group) and how it was z-scored.
- **HFOs:**
  - The "paired T-test" for independent groups: paired by rat, or unpaired.
  - Detector parameters are not given, so the HFO App defaults are used.
  - The manual review cannot be repeated, which is recorded as a deviation.
  - The ictal windows are not stated; those of the PSD Methods are used.

**Places where the paper is inconsistent or garbled:**
- **PSD bands:** the Results say alpha and beta rise, but Fig. 4B, the Abstract and the Discussion say theta and alpha. Both readings are named.
- **Duration proportion:** the text gives -0.06 against 0.36 and cites Fig. 3B, but that panel plots normalized seizure duration. No figure shows the proportion values, and their test is not named.
- **Table S1:** R7's significance mark is garbled ("0.71±0.41* **"); I recorded it as p < 0.01.
- **Table S1 tolerances:** I used the table's reported SDs, as the protocol says for a stated spread, which makes them loose.

Nothing a claim needed was missing from the paper beyond these unstated details.

## End of run

27 turns, 5 minutes, $1.48 at API prices, result: success.
