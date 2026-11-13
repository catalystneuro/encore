# rich-2014 · claims-check · run 43123535883

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i rich; cat claims/rich-2014.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i -e 1255635; wc -l claims/rich-2014.yaml; python tools/claims_check.py claims/rich-2014.yaml paper/10.1126-science.1255635.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/rich-2014.yaml"
}
```

```
1	# Claims for Rich, Liaw & Lee (2014), Science 345:814-817, "Large environments reveal the
2	# statistical structure governing hippocampal representations", tested on CRCNS data set hc-31.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-11, protocol as stated in docs/protocol.md (version pilot-14, Reader).
5	#
6	# Text read: the version of record (paper/10.1126-science.1255635.txt, PyMuPDF text of the
7	# publisher PDF, supplied by a person) and its supplement (rich.sm.pdf: Materials and Methods,
8	# Supplementary Text, Figs. S1 to S18 with legends, references). The supplement PDF was rendered
9	# to read Figs. S5, S7, S15 and S17; the main PDF was rendered to read Fig. 3.
10	# Missing from the text read: the last page of the article (p. 817) has a damaged content stream
11	# in the PDF supplied. Its text columns survive, but Fig. 4 (panels A to C), the Fig. 4 legend,
12	# references 30 and 31 and the acknowledgments neither render nor appear in the text. The Fig. 4
13	# results are stated in the main text and its methods in the supplement, so those claims are
14	# kept, but every detail the Fig. 4 legend would fix (the correlation used in Fig. 4A, the range
15	# of sizes in Fig. 4B, what Fig. 4C plots) is named as open below.
16	# Code: the paper links no analysis code; none was read. The data set's own example script is
17	# part of the data set, not of the paper, and was not read.
18	#
19	# Data the paper used. Five adult male Long-Evans rats, one microdrive of 16 tetrodes over right
20	# dorsal CA1 each; spikes (600-6000 Hz, 32 kHz) and LFP. Only tetrodes localized to CA1 by
[... 749 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/10.1126-science.1255635.txt; cat paper/10.1126-science.1255635.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ccdc603d-0a08-484e-9cdf-ba438849e39f/tool-results/bymfgzwgu.txt",
 "offset": 60,
 "limit": 400
}
```

```
60	Science
61	2014 by the American Association for the Advancement of Science; all rights reserved. The title 
62	Copyright
63	American Association for the Advancement of Science, 1200 New York Avenue NW, Washington, DC 20005. 
64	(print ISSN 0036-8075; online ISSN 1095-9203) is published weekly, except the last week in December, by the
65	Science 
66	 on August 14, 2014
67	www.sciencemag.org
68	Downloaded from 
69	 on August 14, 2014
70	www.sciencemag.org
71	Downloaded from 
72	 on August 14, 2014
73	www.sciencemag.org
74	Downloaded from 
75	 on August 14, 2014
76	www.sciencemag.org
77	Downloaded from 
78	 on August 14, 2014
79	www.sciencemag.org
[... 380 more lines not kept]
```

**Agent**

Main text read; the checker passed (27 claims, 0 problems). Now reading the supplement text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ccdc603d-0a08-484e-9cdf-ba438849e39f/tool-results/bymfgzwgu.txt",
 "offset": 459,
 "limit": 700
}
```

```
459	29. H. S. Milner-Brown, R. B. Stein, R. Yemm, J. Physiol. 230,
460	359–370 (1973).
461	
462	
463	##### Supplement: rich.sm.pdf (the Supplementary Materials: Materials and Methods, Supplementary Text, Figs. S1 to S18, References; supplied by a person)
464	
465	www.sciencemag.org/content/345/6198/814/suppl/DC1 
466	 
467	 
468	 
469	Supplementary Materials for 
470	 
471	Large environments reveal the statistical structure governing hippocampal 
472	representations 
473	P. Dylan Rich,* Hua-Peng Liaw, Albert K. Lee* 
474	 
475	 
476	*Corresponding author. E-mail: [removed: an e-mail address] (P.D.R.); [removed: an e-mail address] (A.K.L.) 
477	 
478	Published 15 August 2014, Science 345, 814 (2014) 
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ccdc603d-0a08-484e-9cdf-ba438849e39f/tool-results/bymfgzwgu.txt",
 "offset": 1158,
 "limit": 500
}
```

```
1158	with respect to the room. Nondirectional fields contributed half counts to their two 
1159	directions. (B) The distribution of fields relative to the distance to the nearest track 
1160	corner. (C) The distribution of the number of fields as a function of the animal’s average 
1161	velocity in 5 cm spatial bins along the track. Null models were made by shuffling the 
1162	locations of the same number of fields as were counted randomly along the track and 
1163	recalculating the distributions. The expected values for the shuffle and 95% confidence 
1164	intervals were calculated from 2000 such simulations. 
1165	 
1166	
1167	 
1168	 
1169	 
1170	25 
1171	 
1172	 
1173	 
1174	 
1175	Fig. S11. Field propensities are preserved along the track. The correlation between the 
1176	number of fields in the first three sections of track (which constitutes approximately the 
1177	first half of the total length of the track) and the last section of track (which constitutes 
[... 263 more lines not kept]
```

**Agent**

Paper and supplement read. Checking the protocol's Reader section and how other files format `checks`.

**Agent calls Bash**

```bash
cd  grep -n -i -A40 "^#* *Reader" docs/protocol.md | head -150; grep -l "^checks:" claims/*.yaml | head -3
```

```
28:Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
29-workflow (roles `claims`, `claims-check` and `answer`), the only runs that
30-write the claims file. The other runs are made with the
31-[Agent run](../.github/workflows/attempt.yml) workflow, one role at a time:
32-`author`, `author-answers` when a reader answered a question on the claims
33-file, `verifier-1`, `author-revise-1`, `verifier-2`, `author-revise-2`, and,
34-when the last of these proposes changes of outcome, `verifier-3` and `author-revise-3`. Each run's
35-transcript and final report are kept in
36-[`transcripts/<paper>/`](../transcripts). Records are filed under the paper's
37-key, its first author's surname and year (`tingley-2021`; papers/keys.yaml),
38-and the datasets it is tested on are listed in `papers/datasets/<paper>.yaml`
39-([paper-first.md](paper-first.md)). A dataset's folder name is its identifier
40-on DANDI and `<archive>-<id>` otherwise ([archives.md](archives.md)). The
41-pipeline is described in [pipeline.md](pipeline.md).
42-
43:## Reader
44-
45-### 1. Get the paper
46-
47-The workflow puts the paper's full text, and its PDF where there is one, under
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 125,200p docs/protocol.md; grep -n -A12 "^checks:" claims/alasfour-2024.yaml | head -30
```

```
treating a detail as open.
   - A detail none of them fixes is recorded as a deviation that says so.
     If it cannot change the outcome (a plotting bin, a random seed), use a
     standard choice and say that it is one. If it could change the outcome
     (how folds are formed, what a measure is compared with, how a penalty
     is chosen), the criterion names the readings the paper's text allows,
     before the analysis, and the notebook runs each of them. The outcome is
     the one they all give; when they give different outcomes, the author
     adopts the reading the paper best supports, as an assumption, or blocks
     the claim as `methods_underspecified` when no choice is defensible
     (author, step 1.6), with every result shown. An outcome that rests on a
     choice the paper does not make is marked as resting on an assumption.
   - For a claim of absence ("no difference", "did not change"), the
     criterion names the test and threshold the paper used. The claim is
     reproduced when that test does not find the effect and not reproduced
     when it does; give the size of the effect either way. The rule for
     several readings does not apply: absence is judged on the paper's test
     alone, as written, even when the test mixes in a condition that does
     not belong (show the cleaner test as a variant).
   - If a criterion turns out unable to decide (two candidates tied), break
[... 69 more lines not kept]
```

**Agent**

Now checking the schema for how reported ranges are expressed, and rendering the figures the file reads values from (S7A, S15, S17, Fig. 3E).

**Agent calls Bash**

```bash
cd  ls tools/ | head -50; grep -rn -i "range\|low\b\|high\b\|minimum\|maximum" tools/claims_check.py | head -30; grep -rn "schema" docs/*.md | head
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
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; python - <<'E'
import json,glob
for f in glob.glob('schemas/claims*'):
    s=json.load(open(f))
    def find(o,path=''):
        if isinstance(o,dict):
            for k,v in o.items():
                if k=='expected': print(f,path,json.dumps(v)[:1500])
                find(v,path+'/'+k)
        elif isinstance(o,list):
            for i in o: find(i,path)
    find(s)
E
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/claims.schema.json /properties/claims/items/properties {"description": "The reported numbers the claim rests on, each with a tolerance: one, or a list.", "oneOf": [{"$ref": "#/$defs/expected"}, {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/expected"}}]}
schemas/claims.schema.json /$defs {"type": "object", "additionalProperties": false, "required": ["quantity", "value"], "properties": {"quantity": {"type": "string"}, "value": {"type": "number"}, "tolerance": {"type": "number", "minimum": 0}, "unit": {"type": "string"}}}
```

**Agent**

No range type exists in the schema, so I'll leave fig3c-recruitment-fraction's range entries. Rendering the supplement pages for S7, S15, S17 and main Fig. 3.

**Agent calls Bash**

```bash
cd  python - <<'E'
import fitz,os
d=os.environ['TMPDIR']
s=fitz.open('paper/10.1126-science.1255635.supp-rich.sm.pdf')
print(len(s))
for i,p in enumerate(s):
    t=p.get_text()
    for k in ['Fig. S7.','Fig. S15.','Fig. S17.','Fig. S11.']:
        if k in t: print(k,i)
m=fitz.open('paper/10.1126-science.1255635.pdf'); print(len(m))
m[3].get_pixmap(dpi=150).save(d+'/main4.png')
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; python -c "import pymupdf" 2>&1; ls ~/.local/bin 2>/dev/null | head; pip list 2>/dev/null | grep -i -e pdf -e mupdf
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pymupdf
ModuleNotFoundError: No module named 'pymupdf'
```

**Agent**

No local PDF renderer; I'll read the figure pages through the PDF reader directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.1255635.supp-rich.sm.pdf",
 "pages": "21-21"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.1255635.supp-rich.sm.pdf",
 "pages": "29-31"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The PDF reader cannot render pages here (no poppler), so I can't verify values read from figures (S7A means, S17 points, Fig. 3E spacing, S15B line). I'll record that as open. Making the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    discovery rate)\n  statistics:\n  - test: Anderson-Darling goodness of fit, each cell, uniform locations and exponential intervals\n    p: 0.05\n    p_relation: \">\"\n    corrected: false discovery rate (Benjamini-Hochberg)\n    n: 61 cells from 5 rats\n  expected:",
 "new_string": "    discovery rate)\n  expected:"
}
```

```
<tool_use_error>String to replace not found in file.
String:     discovery rate)
  statistics:
  - test: Anderson-Darling goodness of fit, each cell, uniform locations and exponential intervals
    p: 0.05
    p_relation: ">"
    corrected: false discovery rate (Benjamini-Hochberg)
    n: 61 cells from 5 rats
  expected:</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    Darling test, 0/5 pFDR<0.05)\n  statistics:\n  - test: Anderson-Darling goodness of fit against uniform, pooled by number of fields\n    p: 0.05\n    p_relation: \">\"\n    corrected: false discovery rate\n    n: 5 groups (cells with 1 to 5 fields)\n  depends_on:",
 "new_string": "    Darling test, 0/5 pFDR<0.05)\n  depends_on:"
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    expectation (253 exp(-mean)), and the test gives p < 0.05 under both readings, pooled and in\n    at least four of the five animals; partially reproduced when it holds pooled but in fewer\n    animals.",
 "new_string": "    expectation (n exp(-mean), for the pooled cells and for each animal's), and the test gives p <\n    0.05 under both readings, pooled and in each of the five animals (Fig. S7A legend, \"The fits\n    for individual animals are poor\"); partially reproduced when it holds pooled but in fewer\n    animals."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    value and the 95% interval per bin (legend). The bin widths of A to C (for C, of velocity) and\n    what counts as a corner are not given; standard choices (30 degree angle bins, 1 m distance\n    bins, 5 cm/s velocity bins, a corner where the track turns by 45 degrees or more) are used and\n    each is a deviation.",
 "new_string": "    value and the 95% interval per bin (legend). The bin widths of A to C (for C, of velocity) are\n    not given; standard choices (30 degree angle bins, 1 m distance bins, 5 cm/s velocity bins)\n    are used and each is a deviation. What counts as a corner is not given and changes the\n    distances measured, so it is open, with readings Y-a, every vertex of the track's scale model\n    (Methods, Position tracking) where the direction changes by 45 degrees or more; Y-b, by 90\n    degrees or more."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    no Spearman correlation between bin centre and count residual (observed minus shuffle mean) at\n    p < 0.05 for B and C. Reproduced when all three panels pass under both readings; not\n    reproduced when any panel fails under both.",
 "new_string": "    no Spearman correlation between bin centre and count residual (observed minus shuffle mean) at\n    p < 0.05 for B and C. Reproduced when all three panels pass under both readings of T (and of\n    Y for B); not reproduced when any panel fails under all of them."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    tolerance, the recruitment test gives p > 0.05 under both readings of K, and the counts are\n    still overdispersed by the tests of fig3b-overdispersion; not reproduced when the recruitment\n    test gives p < 0.05 under both.",
 "new_string": "    tolerance and the recruitment test gives p > 0.05 under both readings of K; not reproduced\n    when the recruitment test gives p < 0.05 under both. The refitted r and p, and the dispersion\n    tests of fig3b-overdispersion on the new counts, are reported."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    R-a, Pearson; R-b, Spearman. Reproduced when, under one reading, both pooled values are within\n    tolerance with p < 0.05 and fewer than three of the five animals show a significant correlation\n    (p < 0.05) of the same sign on that axis; partially reproduced when the pooled values hold and\n    the per-animal pattern does not.",
 "new_string": "    R-a, Pearson; R-b, Spearman. What \"not consistent within individual animals\" means is not\n    given; readings N-a, fewer than three of the five animals show a significant correlation (p <\n    0.05) of the pooled sign on that axis; N-b, at least one animal has a correlation of the\n    opposite sign on that axis. Reproduced when, under one reading of R, both pooled values are\n    within tolerance with p < 0.05 and, under one reading of N, the per-animal pattern holds on\n    both axes; partially reproduced when the pooled values hold and the per-animal pattern does\n    not."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    the claim is judged on the widest interval of L over which the proportion stays inside 4.5 to\n    11% (the range widened by 10% of each bound); reproduced when that interval spans at least a\n    factor of 10 in L. Before any analysis, note that the printed parameters give about 16% at 48 m\n    and 20% at 10 to 20 m, with 5 to 10% for L of roughly 200 to 600 m (and near 1 m); the\n    interval, its position, and the proportion of single-field cells among all cells (reading\n    X-a) and among place cells (reading X-b) are reported.",
 "new_string": "    the claim is judged on the widest interval of L over which the proportion stays inside 4.5 to\n    11% (the range widened by 10% of each bound); reproduced when, under one reading, that\n    interval spans at least a factor of 10 in L. The denominator is open, with readings X-a, all\n    cells (the formula above); X-b, place cells, r p_L^r (1 - p_L) / (1 - p_L^r). Before any\n    analysis, note that the printed parameters under X-a give about 16% at 48 m and 20% at 10 to\n    20 m, with 5 to 10% for L of roughly 150 to 550 m (and near 1 to 2 m); the interval and its\n    position under each reading are reported."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "adjusted for false discovery rate)\n  statistics:\n  - test: Anderson-Darling goodness of fit, each cell, uniform locations and exponential intervals\n    p: 0.05\n    p_relation: \">\"\n    corrected: false discovery rate (Benjamini-Hochberg)\n    n: 61 cells from 5 rats\n  expected:",
 "new_string": "adjusted for false discovery rate)\n  expected:"
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    model, and the equal-rate proportion for pairs both larger than 20 m is below 0.05 (the\n    legend of Fig. S18 says it falls to almost zero for larger environments under a high rate);\n    the full matrices are shown. The low and high equal rates of Fig. S18 are not given; half and\n    twice the fitted mean are shown as variants.",
 "new_string": "    model; the full matrices are shown. The low and high equal rates of Fig. S18 are not given;\n    half and twice the fitted mean are shown as variants, with the Fig. S18 legend's statement\n    that the high-rate proportion is almost zero between larger environments checked on the\n    twice-the-mean variant."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    track time counts as \"in the environment\" is open, with readings E-a, novel-section exploration of\n    RUN1 only; E-b, all RUN1 time on the track. The plus-or-minus value is a spread across cells,\n    so tolerances are 10%. \"Tightly correlated\" names no test or threshold; the test is a\n    Spearman correlation between rate and number of fields, p < 0.05 and positive, with rho\n    reported. Reproduced when, under one reading, both values are within tolerance, every cell\n    without fields has a lower rate than the median cell with fields (a one-sided Mann-Whitney\n    test at p < 0.05), and the correlation holds.",
 "new_string": "    track time counts as \"in the environment\" is open, with readings Z-a, novel-section exploration of\n    RUN1 only; Z-b, all RUN1 time on the track. The plus-or-minus value is a spread across cells,\n    so tolerances are 10%. \"Lower than cells with at least one place field\" and \"tightly\n    correlated\" name no test; the tests are a one-sided Mann-Whitney test of the rates of cells\n    without fields against those of cells with fields, and a Spearman correlation between rate\n    and number of fields, each at p < 0.05 in the stated direction, with rho reported. Reproduced\n    when, under one reading, both values are within tolerance and both tests hold."
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    40 m are used (S-a), with every 10 m as a check (S-b). No test is reported. The test is that of\n    Fig. 3C, applied to each curve against the Lomax with the parameters of fig3b-negbin-fit,\n    censored at 48 - s (K-a). Reproduced when no forward or reverse curve differs at p < 0.05 after\n    Benjamini-Hochberg adjustment over the curves, under both spacings;",
 "new_string": "    40 m are used (V-a), with every 10 m as a check (V-b). No test is reported. The test is that of\n    Fig. 3C, applied to each curve against the Lomax with the parameters of fig3b-negbin-fit,\n    censored at 48 - s (K-a). Reproduced when no forward or reverse curve differs at p < 0.05 after\n    Benjamini-Hochberg adjustment over the curves, under both spacings V-a and V-b;"
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/rich-2014.yaml",
 "old_string": "    value: 0.22\n    tolerance: 0.02",
 "new_string": "    value: 0.22\n    tolerance: 0.015"
}
```

```
The file claims/rich-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Edits done. Appending the `checks` entry and re-running the checker.

**Agent calls Bash**

```bash
cd  cat >> claims/rich-2014.yaml <<'E'
checks:
- date: 2026-11-11
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-individual-poisson. Removed the statistics entry (Anderson-Darling, FDR, p 0.05 recorded as ">"); "0/61 cells with P < 0.05" counts cells by a threshold, a method and not a result. The count stays as the expected value 0.
  - figs6-few-field-cells-uniform. Removed the statistics entry for the same reason; "0/5 pFDR<0.05" counts groups by a threshold. The criterion keeps the test.
  - fig3b-overdispersion. The statement says the fit is poor in each animal (Fig. S7A legend, "The fits for individual animals are poor"), but the criterion accepted four of five; it now needs all five, and the zero-field expectation is computed per animal with that animal's n and mean.
  - figs10-no-track-or-speed-influence. The corner definition (45 degrees) was called a standard choice, but it changes the distances panel B measures and the paper does not define a corner; it is now open, with readings Y-a (45 degrees) and Y-b (90 degrees).
  - figs15-higher-threshold. Removed the condition that the counts stay overdispersed; the Fig. S15 legend says only that the gamma-Poisson model describes the counts and the recruitment as for all fields, and names no dispersion test. The dispersion tests are now reported.
  - figs16-anatomy. "Not consistent within individual animals" was operationalized one way (fewer than three animals significant) as if the paper fixed it; it is now open, with readings N-a (that rule) and N-b (an animal with the opposite sign).
  - fig4b-single-field-proportion. The criterion named X-a and X-b but judged on X-a only; it now judges under either and gives the X-b formula. The note on the printed parameters is corrected to 150 to 550 m and 1 to 2 m (r p_L^r (1 - p_L) with r 0.57, p 0.14 gives about 8.5% at 200 m, 4.7% at 600 m, 6% at 1 m and 10% at 2 m).
  - fig4c-active-subsets. Removed the requirement that the fitted equal-rate proportion between environments over 20 m be below 0.05; the Fig. S18 legend says that of the high-rate condition, not of the fitted one, and the fitted equal rate (3.5 fields per 48 m) gives about 0.25 for 20 m against 50 m. The statement is now checked on the twice-the-mean variant.
  - figs5-silent-cells-low-rate. The criterion required every cell without fields to lie below the median cell with fields and called that a Mann-Whitney test; the paper compares the groups only, so the test is now the Mann-Whitney test alone, named as a reading. Readings renamed Z-a and Z-b, as E-a and E-b were already used in fig2-individual-poisson.
  - fig3e-memoryless-recruitment. Spacing readings renamed V-a and V-b, as S-a and S-b were already used in fig2-individual-poisson.
  - figs17-propensity-across-environments. The tolerance of the between-environment median was 0.02, but the criterion sets it to the half-width of the interval it reads (0.20 to 0.23), 0.015; set to 0.015.
  - Open. The values read from figures (Fig. S7A means per animal, the Fig. S17 points and intervals, the Fig. 3E spacing of about 5 m, the Fig. S15B threshold line) could not be checked; no PDF renderer was available in this run. They agree with what the text allows (the S7A means give a pooled mean between 3.2 and 3.6, against 3.5 from r and p).
  - Open. fig3c-extrapolation-500m. The printed parameters give about 436 m (410 to 480 m within their rounding), outside the 10% tolerance of 500 m; the paper's "~500 m" is approximate and its inset cannot be read, so the tolerance is kept and the result rests on the unrounded fit.
  - Open. fig4b-single-field-proportion. The factor of 10 in L that stands for "a wide range" is not from the paper, and the printed parameters give under a factor of 4 under either reading; the Fig. 4B legend, which would fix the range of sizes and the denominator, is missing from the text supplied.
E
python tools/claims_check.py claims/rich-2014.yaml paper/10.1126-science.1255635.txt; grep -n ": " claims/rich-2014.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: " | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes. Confirming the YAML parses and no value contains ": ".

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/rich-2014.yaml'))
print(len(d['checks'][-1]['changes']))
" ; grep -v '^\s*#' claims/rich-2014.yaml | grep -nE '[^ ]: .*: |^\s+[^-a-z_ ].*: ' | head; grep -c '—' claims/rich-2014.yaml; grep -ci 'rather' claims/rich-2014.yaml
```

```
14
0
0
```

**Agent**

I checked `claims/rich-2014.yaml` against the paper and supplement and made 11 changes; the file is ready for an attempt. Three problems remain open, listed below. Nothing was committed.

**Checker:** `claims/rich-2014.yaml: 27 claims, 27 quotes, 15 statistical values, 0 problems`. It said 17 statistical values before my edits; the two I removed account for the difference.

**Changes, by claim**
- **fig2-individual-poisson, figs6-few-field-cells-uniform:** removed the statistics entries. "0/61 cells with P < 0.05" and "0/5 pFDR<0.05" count cells or groups against a threshold, so they are method, not results. The 0 count stays as an expected value.
- **fig3b-overdispersion:** the statement says the fit is poor in each animal, as the Fig. S7A legend does, but the criterion accepted four of five animals. It now needs all five, and the expected number of cells with no field is computed per animal.
- **figs10-no-track-or-speed-influence:** the paper never defines a corner, and the 45-degree rule had been called a standard choice even though it changes panel B. It is now open, with two readings: 45 degrees or 90 degrees.
- **figs15-higher-threshold:** removed the requirement that the counts stay overdispersed. The S15 legend names no such test. The dispersion is now only reported.
- **figs16-anatomy:** the paper does not say what "not consistent within individual animals" means. It is now open, with two readings: fewer than three animals significant, or at least one animal with the opposite sign.
- **fig4b-single-field-proportion:** the criterion named two denominators (all cells, place cells) but judged on all cells only; it now judges on either and gives the formula for the second. I also corrected the note on the printed parameters: 5 to 10% falls at about 150 to 550 m and 1 to 2 m.
- **fig4c-active-subsets:** removed the condition that the fitted equal-rate proportion between environments over 20 m be below 0.05. The S18 legend says that of its high-rate condition only. The fitted equal-rate model gives about 0.25 for 20 m against 50 m, so the condition would have failed even on the paper's own model. The legend's statement is now checked on the twice-the-mean variant.
- **figs5-silent-cells-low-rate:** the criterion required every cell without fields to fall below the median cell with fields, which the paper never says. It now uses a one-sided Mann-Whitney group test, named as a reading. Its readings are renamed Z-a and Z-b, because E-a and E-b were already used in fig2.
- **fig3e-memoryless-recruitment:** the spacing readings are renamed V-a and V-b, because S-a and S-b were already used in fig2.
- **figs17-propensity-across-environments:** set the tolerance on the between-environment value to 0.015 (was 0.02). That is the half-width of 0.20 to 0.23, the rule the criterion itself states.

**Open**
- **Figure readings unchecked:** no PDF renderer was available, so I could not check the values read from figures: the S7A per-animal means, the S17 points and intervals, the roughly 5 m spacing in Fig. 3E, and the S15B threshold line. The S7A means are at least consistent with the text: they imply a pooled mean of 3.2 to 3.6, against 3.5 from r and p.
- **fig3c-extrapolation-500m:** the printed parameters give about 436 m, outside 500 ± 50 m. The paper says only "~500 m", so the result depends on the unrounded fit.
- **fig4b-single-field-proportion:** the "factor of 10 in L" standing for "a wide range" is not from the paper. The printed parameters give under a factor of 4, so as written the claim would likely fail on them. The Fig. 4B legend, which would settle the range of sizes and the denominator, is missing from the text supplied.

Every main finding has a claim, and none comes from outside the paper.

## End of run

31 turns, 4 minutes, $1.44 at API prices, result: success.
