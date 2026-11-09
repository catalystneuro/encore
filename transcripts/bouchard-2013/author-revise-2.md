# 000019 · author-revise-2 · run 39721031259

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat transcripts/000019/verifier-2-report.md; ls entries/000019-bouchard-2013 entries/000019-bouchard-2013/*; grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i "step 6\|Hand over\|round 2\|proposed"
```

```
## 1. Outcomes

The claims file has 22 claims, and the attempt record gives an outcome for each of them. I agree with all 22: data-composition is partially reproduced; active-electrodes is blocked (methods_underspecified); fig1c-e and the seven spatial claims are blocked (metadata_insufficient); fig1f-h is not reproduced; suppfig6 is reproduced; fig3d is not reproduced; pca, fig4a, suppfig11, fig4c-d, fig4ef, fig5d and suppfig13 are blocked (methods_underspecified); fig5c and suppfig9 are not reproduced. Every count, range and measured value in the record matches the printed outputs (cells 20, 23, 26, 29, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64).

Three places where the claims file may misread the paper. I report these and have not corrected them:
- **suppfig13:** a reading reproduces only if the pair count is 4623. That count is fixed by which syllables the dataset holds, not by the effect the paper reports. Read strictly, every reading is not reproduced.
- **suppfig6:** grouping electrodes by their largest weight almost guarantees the result. The test also holds on permuted weights in 94 of 96 readings (cell 34).
- **suppfig9:** jaw against larynx is judged at p > 0.05, but the paper says P > 0.2. This does not change the outcome, since the measured p is 5e-11.

## 2. Sentences the outputs do not support

- **Attempt record, fig2a-lips-dorsal notes:** "the median z coordinate of the top 10% of lips weights is above that of the tongue weights in EC2 (36.6 against 15.6) and GP31." Cell 32 prints `GP31: ... Tongue no window`, so there is no GP31 comparison. This is for information only and affects no outcome.
- **README:** "The claims blocked as methods underspecified depend on details the paper does not fix: [CV set, baseline, z-scoring, projection]". **Summary (cell 66):** "The blocked outcomes of the state-space claims and of active-electrodes come from these readings giving different results." Neither holds for fig5d. Cell 58 shows its split comes from the rea
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 360,470p docs/protocol.md; ls; ls attempts 2>/dev/null | grep 000019; find . -path ./paper -prune -o -name "*000019*" -print | head
```

```
part.
  - `not_reproduced`: the analysis ran and the result differs.
  - `blocked`: the claim could not be tested; give `blocked_by` and say why.
    When the paper states a chance level or false-positive rate for a
    selection, compute it with your procedure. If yours is far from the
    paper's, the procedures differ, and the outcome is `blocked` with
    `methods_underspecified` even though the analysis ran.

  The criterion decides the outcome. Where the claim's statement says more
  than the criterion tests (a p-value, a second condition), the notes say
  whether that part holds.
- **`deviations`**: every way the test differed from the paper's method or
  data. One session of four, a substituted model, a threshold the paper does
  not state.
- **`notes`**: the numbers behind the outcome, stated factually.
- **`measured`**: the value obtained, or one per expected value in the same
  order. When several readings match, record the first reading the criterion
  lists.
- **`proposed`**: on an outcome, a change of outcome found after the last
  verification round, with its `reason` (see "Hand over for verification").
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cat questions/000019.yaml | head -80; wc -l questions/000019.yaml attempts/000019-bouchard-2013-01.yaml; grep -n "verifications:" -A3 attempts/000019-bouchard-2013-01.yaml
```

```
# Questions from attempt 000019-bouchard-2013-01 (author, 2026-10-21) about the claims file
# claims/000019/10.1038-nature11911.yaml. Each is asked under docs/protocol.md, Author, step 1.6; the
# attempt runs every reading it can see and records the claims whose outcome depends on the answer.
dandiset: "000019"
paper: doi:10.1038/nature11911
questions:
- claim: pca-nine-components
  also: [fig4a-consonant-clusters, suppfig11-co-clustering, fig4c-d-hierarchy, fig4ef-feature-correlations,
    fig5c-separability-timing, fig5d-separability-coupling, suppfig13-consonant-vowel-distance,
    suppfig9-pc-articulator-weights]
  asked: 2026-10-21
  question: Before the PCA, is each electrode's high gamma z-scored over its whole concatenated (CV x
    time) series (`row`), or across syllables separately at each time point (`time`)? The second
    removes the mean time course shared by all syllables. Is the same z-scored input projected onto
    the PCs to give the state K(s, t)?
  passage: Methods, PCA and Cortical-State Space, "Each electrode's time series was z-scored across
    syllables to normalize response variability across electrodes."
  why: With `row` the nine PCs explain 0.60 to 0.64 of the variance (within 0.6 +- 0.06), with `time`
    0.49 to 0.55 (mostly outside). Consonant-vowel distances exceed consonant-consonant distances
    under `row` and not under `time` (suppfig13), and the hierarchy and late feature-correlation
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,116p questions/000019.yaml; echo ----; cat attempts/000019-bouchard-2013-01.yaml
```

```
<persisted-output>
Output too large (43.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/263ae97e-6a85-4ff7-b611-bdc1b0b9953b/tool-results/bxu8s9awa.txt

Preview (first 2KB):
  passage: Methods, Data acquisition and Signal Processing, "High-γ power was z-scored relative to
    the mean and standard deviation of baseline data for each channel."
  why: The rest period has lower high gamma than the rest of the block in most blocks, so z-scores
    are larger. The mean active-electrode count is 34.0 per subject with every CV and 27.0 with CVs
    of 15 or more renditions (paper about 30, tolerance 27 to 33), against 7.0 to 24.3 under the
    claims file's readings. The attempt shows it as a variant, not a reading.
  answer: >-
    Yes. The Methods say only "High-γ power was z-scored relative to the mean and standard
    deviation of baseline data for each channel" and never define baseline data; a silent
    rest period is as plausible a reading as the two the file named. The header now lists it
    as baseline reading (c), run with (a) and (b), so active-electrodes and the claims that
    use Hγ judge it as a reading and not as a variant. Claims and expected values unchanged.
  answered: 2026-10-22
- claim: fig2a-lips-dorsal
  also: [fig2b-somatotopic-sequence, suppfig3b-spatial-clustering, suppfig3d-cross-subject,
    suppfig3f-dv-sequence, suppfig5-intermediate-organization, suppfig7-no-latency-difference,
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000019-bouchard-2013-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000019-bouchard-2013-01
3	dataset:
4	  archive: dandi
5	  id: "000019"
6	  version: 0.220126.2148
7	  doi: 10.48324/dandi.000019/0.220126.2148
8	paper: doi:10.1038/nature11911
9	date: 2026-10-21
10	entry: 000019-bouchard-2013
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	  runner:
20	    platform: GitHub Actions
[... 598 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python - <<'EOF'
import json
nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if i in (0,3,10,32,58,59,66,67) :
        print('=====',i,c['cell_type']); print(s[:6000])
EOF
cat README.md; cat ../../transcripts/000019/verifier-1-report.md | grep -n "B3" -A12 | head -40
```

```
===== 0 markdown
# Reproducing Bouchard et al. (2013) from dandiset 000019

Paper. Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of
human sensorimotor cortex for speech articulation. *Nature* 495, 327-332.
[doi:10.1038/nature11911](https://doi.org/10.1038/nature11911). The claims file
(`claims/000019/10.1038-nature11911.yaml`) was written from the NIH author manuscript in PubMed
Central (PMC3606666) with its supplement, and checked by a second reader.

Dandiset. [DANDI:000019](https://dandiarchive.org/dandiset/000019/0.220126.2148),
"Human ECoG speaking consonant-vowel syllables", version 0.220126.2148. The paper cites no
version of the dandiset (it predates it). This is the only published version; the draft has the
same 31 assets and the same size, so the published version is pinned.

What the dandiset holds. Raw ECoG (256 channels, 3051.76 Hz) of 31 recording blocks from four
subjects (EC2, EC9, GP31, GP33), with a trial table per block (syllable, start, C-V transition
and stop times), a `bad` flag and an anatomical label per electrode, 3-D electrode coordinates for
two subjects, and a rest period per block. The microphone signal was removed (dandiset
description), and no high gamma is stored, so high gamma is computed here from the raw voltage.
The paper's subjects are EC2, EC33 and EC31; EC2, GP33 and GP31 are taken to be them (see the data
[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
ls ../../transcripts/000019/; python - <<'EOF'
import json
nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'GP31' in s and ('36.6' in s or 'top 10%' in s) and c['cell_type']=='markdown': print('=====',i); print(s)
    if i==32:
        for o in c.get('outputs',[]): print(''.join(o.get('text','')))
EOF
```

```
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
===== 31
## Spatial claims (blocked)

fig2a-lips-dorsal, fig2b-somatotopic-sequence, suppfig3b-spatial-clustering,
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i in (32,33,3,8):
    c=nb['cells'][i]
    print('=====',i, c['cell_type'])
    if c['cell_type']=='markdown': print(''.join(c['source']))
    for o in c.get('outputs',[]): print(''.join(o.get('text',''))[:3000])
EOF
grep -n "B3\b\|B3\." ../../transcripts/000019/verifier-1-report.md | head
```

```
===== 32 code
===== 33 markdown
## suppfig6-mixed-tuning

> Single electrodes show a clear preferred articulator and also carry weights for other
> articulators.
===== 3 code
===== 8 code
```

**Agent calls Bash**

```bash
grep -n "B3" ../../transcripts/000019/verifier-1-report.md | head; ls ../../executed/ 2>/dev/null; sed -n 1,60p ../../tools/entry.py | head -60
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
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "thi" ../../transcripts/000019/verifier-1-report.md | head -20
```

```
7:| data-composition | partially_reproduced | Three subjects, 3051.76 Hz (within 1 Hz). But there is no audio, the subjects have 19/19/19 consonants and 57+55+57 = 169 CVs, renditions run from 2 to 107, and GP33's hemisphere cannot be determined (cells 8, 18). |
8:| active-electrodes | blocked (methods_underspecified) | With all CVs, no baseline gives a mean in 27–33 (24.3, 21.3, 34.0). With 15+ CVs only `rest` does (27.0), which is partial. The split comes from GP31's /thi/, which has 2 renditions (GP31 counts 49→9 and 43→0, cell 20). |
20:| pca-nine-components | blocked (methods_underspecified) | The `row` z-scoring gives 0.598–0.661, within 0.54–0.66 in 11 of 12 combinations. The `time` z-scoring gives 0.49–0.564; under the `pre`/`whole` baselines it falls outside in 7 of 8 (cell 32). 16 readings are in, 8 out. |
32:1. **[does not affect a conclusion] Cell 5: an unchecked statement about file contents.** The line "only acquisition/ElectricalSeries is present" is a hard-coded print, not a check. The DANDI asset metadata for `sub-EC2_ses-EC2-B1.nwb` lists `ProcessingModule` and `Spectrum`, and the dandiset summary lists both. The notebook never looks at them. A spectrum is not audio, but this is unverified.
33:2. **[affects a conclusion] Cells 10 and 18: subject identity is assumed.** GP31 = EC31 and GP33 = EC33 is an assumption. GP33 has no coordinates, so the one right-hemisphere subject cannot be confirmed. GP31 is the subject with only 18 consonants that have all three vowels (/tha/ and /thu/ are missing, /thi/ has 2 renditions). That fits the paper's 54-CV subject but is not stated.
34:3. **[affects a conclusion] active-electrodes and the 15+/all CV split generally.** One GP31 CV with 2 renditions (/thi/) drives the threshold count. Removing it takes GP31 from 43–49 active electrodes to 0–9 under `pre` and `whole`. It also flips silhouettes (cell 34, GP31 k = 2 at 0.78 against 0.37) and the fig4ef late-window tests. Many methods_underspecified outcomes come fr
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
ls ../../schemas; grep -n "" ../../schemas/*question* 2>/dev/null | head -60; grep -n "question" ../../docs/protocol.md | head -30
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
28:`author`, `author-answers` when questions were answered, `verifier-1`,
163:### 6. Answer questions
166:(author, step 6). A reader answers each question from the paper, in the claims
167:file, and marks it answered in `questions/<folder>.yaml`. An answer
270:   you find it in the paper. Add a question to `questions/<folder>.yaml`
271:   (`claim`, `question`, the passage of the paper that bears on it if you
274:   `methods_underspecified` until the question is answered. A reader answers from the paper (reader, step 6), and
410:where the claims file misreads the paper is reported, as a question for a
```

**Agent calls Bash**

```bash
sed -n 155,185p ../../docs/protocol.md; sed -n 262,285p ../../docs/protocol.md; sed -n 20,40p ../../docs/protocol.md
```

```
mechanically); that each source points at the place; that the statistics are
the paper's and are results, not thresholds; that every part of every
criterion's method is taken from the paper or its code, as cited; and that the
paper's main findings each have a claim. The checker corrects what it can
show is wrong, and records each change, with its reason, under `checks` at
the end of the file. A claims file is ready for an attempt when its last check
says so.

### 6. Answer questions

When an attempt needs something the claims file does not give, the author asks
(author, step 6). A reader answers each question from the paper, in the claims
file, and marks it answered in `questions/<folder>.yaml`. An answer
the paper does not give is said to be that: the claim stays as it is, and the
author treats the detail as open (step 3, on details none of the sources fix).

## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
ls ../../claims/000019/; python - <<'EOF'
import yaml
d=yaml.safe_load(open('../../claims/000019/10.1038-nature11911.yaml'))
for c in d['claims']:
    if c['id'] in ('suppfig13-consonant-vowel-distance','suppfig6-mixed-tuning','suppfig9-pc-articulator-weights'):
        print(yaml.safe_dump(c, allow_unicode=True, width=110))
EOF
```

```
10.1038-nature11911.yaml
criterion: As in Methods (analysis of representational overlap) for the electrodes of claim fig2a-lips-dorsal. Electrodes
  grouped by their largest W_iA; for each, the positive weights as a percentage of their sum; the group means. Reproduced
  when, in every group, the preferred articulator has the largest mean percentage and at least one other articulator
  has a mean percentage above zero. The paper gives no number, so the group means are reported.
depends_on:
- fig2a-lips-dorsal
id: suppfig6-mixed-tuning
quote: This analysis revealed clear preferred tuning for individual articulators at single electrodes (Fig. 2c,
  electrodes categorized according to the strongest articulator representation), and also demonstrated that single
  electrodes had functional representations of multiple articulators
source: Results, Spatial Representation of Articulators, paragraph 2; Supplementary Figure 6
statement: Single electrodes show a clear preferred articulator and also carry weights for other articulators.

criterion: Per subject, nine-PC states of each CV at -25 ms (consonant) and +250 ms (vowel). For each unordered
  pair of CVs in a subject, the consonant-consonant distance, the vowel-vowel distance and the consonant-vowel distance
  (OPEN, which of the pair at which time; readings (a) the mean of the two cross pairings, (b) i at -25 ms and j
  at +250 ms). 4623 is read as the pairs within subjects (1596 + 1596 + 1431). Paired Wilcoxon signed-rank tests
  over the pairs pooled over subjects, Bonferroni for 3. Reproduced when all three orderings hold with corrected
  p < 1e-10 and the pair count is 4623.
[... 55 more lines not kept]
```

**Agent**

Now the edits. Notebook cells first.

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='reproduce_bouchard_2013.ipynb'
nb=json.load(open(p))
def rep(i,a,b):
    s=''.join(nb['cells'][i]['source'])
    assert a in s,(i,a)
    s=s.replace(a,b)
    nb['cells'][i]['source']=s.splitlines(keepends=True)
rep(10,"EC9 has 24\nconsonant labels","EC9 has 23\nconsonant labels")
rep(59,"The readings of the claim give different outcomes, and the reading of R decides the split:\nwith the mean of three feature sets all 120 readings fail.",
"The readings of the claim give different outcomes, and two of them decide the split: the\nreading of R (with the mean of three feature sets all 120 readings fail) and the reading of the\nclusters (with k-means clusters all 48 readings fail, the 24 with the matching feature set among\nthem). The baseline, z-scoring, projection and CV set give similar mixes at every level.")
rep(66,"The blocked outcomes of the state-space claims and of\nactive-electrodes come from these readings giving different results; the paper cannot settle\nthem.",
"The blocked outcomes of active-electrodes and of the state-space claims other than\nfig5d come from these readings giving different results; the paper cannot settle them. That of\nfig5d comes from the claims file's readings of R and of the clusters, which split it at every\nlevel of the readings above.")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; tail -c 200 reproduce_bouchard_2013.ipynb | od -c | tail -3; git show HEAD:entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb | tail -c 50 | od -c | tail -3
```

```
.../000019-bouchard-2013/reproduce_bouchard_2013.ipynb    | 15 +++++++++------
 1 file changed, 9 insertions(+), 6 deletions(-)
0000260  \n       "   n   b   f   o   r   m   a   t   _   m   i   n   o
0000300   r   "   :       5  \n   }  \n
0000310
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000019-bouchard-2013/README.md",
 "old_string": "them open, so every reading is run and the outcomes differ between readings. The attempt record, with the reasons",
 "new_string": "them open, so every reading is run and the outcomes differ between readings. The separability\ncoupling is the exception: its outcomes differ between the claims file's own readings of the\nclusters and of the feature set used, not between those of the details above. The attempt record, with the reasons"
}
```

```
The file entries/000019-bouchard-2013/README.md has been updated successfully.
```

**Agent calls Bash**

```bash
sed -n 1,80p bouchard.py | grep -n "def process_blocks" ; grep -n "def process_blocks" -A40 bouchard.py | head -60
```

```
365:def process_blocks(block_assets: list[dict], log=print) -> list[dict]:
366-    """process_block over several files, fetching the next file while one is processed."""
367-    out = []
368-    with ThreadPoolExecutor(1) as ex:
369-        nxt = ex.submit(fetch, block_assets[0]["url"], block_assets[0]["size"])
370-        for i, a in enumerate(block_assets):
371-            buf = nxt.result()
372-            if i + 1 < len(block_assets):
373-                nxt = ex.submit(fetch, block_assets[i + 1]["url"], block_assets[i + 1]["size"])
374-            out.append(process_block(a, buf))
375-            del buf
376-            log(f"{a['path']}: {len(out[-1]['kept'])} trials")
377-    return out
378-
379-
380-def load_subject(blocks: list[dict], exclude_invalid: bool = False) -> dict:
381-    """Pool the blocks of one subject into per-syllable mean z-scored high gamma.
382-
383-    Electrodes flagged bad in any block are left out of the subject's analyses (`good`). Returns
384-    `cvs` (sorted (consonant, vowel) pairs), `counts` (renditions per CV), `H[baseline]`
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='reproduce_bouchard_2013.ipynb'
nb=json.load(open(p))
i=3
s=''.join(nb['cells'][i]['source'])
a='print(f"processed {sum(len(v) for v in blocks.values())} blocks in {time.time() - started:.0f} s")'
assert a in s
s=s.replace(a,a+'\nstreamed = sum(a["size"] for a in ASSETS if a["path"].split("/")[0][4:] in B.SUBJECTS)\nprint(f"streamed {streamed / 1e9:.1f} GB of raw ECoG")')
nb['cells'][i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
grep -n "SUBJECTS =" bouchard.py
```

```
61:SUBJECTS = ["EC2", "GP31", "GP33"]   # EC9 is in the dandiset but not in the paper
```

**Agent**

Now running the entry (takes ~20 minutes).

**Agent calls Bash**

```bash
cd ../.. && python tools/entry.py all entries/000019-bouchard-2013 2>&1 | tail -30
```

```
Installed kernelspec registry-000019-bouchard-2013 in executed/000019-bouchard-2013/.venv/share/jupyter/kernels/registry-000019-bouchard-2013
0 error(s)
pass  reproduce_bouchard_2013.ipynb  (1290 s)
```

**Agent**

Run passed. Now checking the new outputs against every conclusion.

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    t=''.join(''.join(o.get('text','')) if 'text' in o else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
    if i in (3,8,32,67): print('=====',i); print(t[:3000])
    elif t: print('=====',i, 'len',len(t)); 
EOF
```

```
===== 2 len 75
===== 3
processed 24 blocks in 998 s
streamed 39.0 GB of raw ECoG

===== 5 len 10266
===== 6 len 171
===== 8
EC2: 2628 trials, 57 distinct CVs, 19 consonants; renditions per CV 10 to 58; labels that are not CVs of the task: {}
    CVs missing: []; CVs with fewer than 15 renditions: {'thi': 10}; more than 100: {}
EC9: 1653 trials, 57 distinct CVs, 19 consonants; renditions per CV 7 to 46; labels that are not CVs of the task: {np.str_('dhee'): 8, np.str_(''): 6, np.str_('dhoo'): 6, np.str_('chee'): 5, np.str_('dhaa'): 5, np.str_('jee'): 2, np.str_('skee'): 1, np.str_('ya'): 1, np.str_('kay'): 1, np.str_('chaa'): 1, np.str_('choo'): 1}
    CVs missing: []; CVs with fewer than 15 renditions: {'thi': 12, 'thu': 10, 'tha': 7}; more than 100: {}
GP31: 5285 trials, 55 distinct CVs, 19 consonants; renditions per CV 2 to 107; labels that are not CVs of the task: {}
    CVs missing: ['tha', 'thu']; CVs with fewer than 15 renditions: {'thi': 2}; more than 100: {'la': 107, 'di': 106, 'da': 105, 'ga': 105, 'sha': 105, 'ha': 105, 'bi': 105, 'ni': 105, 'hi': 105, 'li': 105, 'yu': 105, 'ka': 104, 'na': 104, 'sa': 104, 'va': 104, 'ti': 104, 'ki': 104, 'mi': 104, 'shi': 104, 'si': 104, 'du': 104, 'nu': 104, 'ba': 103, 'ta': 103, 'shu': 103, 'hu': 103, 'ma': 102, 'ra': 102, 'ya': 102, 'wi': 102, 'tu': 102, 'lu': 102, 'wa': 101}
GP33: 1458 trials, 57 distinct CVs, 19 consonants; renditions per CV 22 to 28; labels that are not CVs of the task: {}
    CVs missing: []; CVs with fewer than 15 renditions: {}; more than 100: {}
Labels merged as misspellings: {('EC2', np.str_('she')): 2, ('EC9', np.str_('ha')): 1, ('EC9', np.str_('she')): 1, ('GP33', np.str_('ha')): 2}
Spellings merged: 'she' -> 'shee', 'ha' -> 'haa'. Paper: 19, 19 and 18 consonants, 168 CVs (57 + 57 + 54), 15 to 100 renditions each.

===== 9 len 3836
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json,re
nb=json.load(open('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if i==20: print('==20\n',t)
    if i==58: print('==58\n', t[t.find('Outcome over'):])
    for line in t.splitlines():
        if line.startswith('Outcome over') and i!=58: print(i,line)
EOF
```

```
==20
 subject  CVs  consonants  vowels  min_renditions  max_renditions  CVs_below_15  CVs_above_100  consonants_with_all_3_vowels_and_15+ hemisphere_from_x
    EC2   57          19       3              10              58             1              0                                    18              left
   GP31   55          19       3               2             107             1             33                                    18              left
   GP33   57          19       3              22              28             0              0                                    19           unknown
Subjects in the dandiset: ['EC2', 'EC9', 'GP31', 'GP33'] | of the paper's (EC2, EC31, EC33), by assumed correspondence: 3
Distinct CVs over the three subjects: 169 (paper 168); with CVs of fewer than 15 renditions left out: 167
ECoG sampling rate: [np.float64(3051.7578), np.float64(3051.7578125)] Hz (3052 +- 1)
Audio in the files: none (removed for HIPAA, dandiset description)

23 Outcome over readings: differ by reading: not reproduced 1, partially 1
29 Outcome over readings: not reproduced
34 Outcome over readings: reproduced
37 Outcome over readings (substitute acoustic onset): not reproduced
40 Outcome over readings: differ by reading: not reproduced 8, reproduced 16
43 Outcome over readings: differ by reading: not reproduced 23, partially 1
46 Outcome over readings: differ by reading: not reproduced 10, partially 38
49 Outcome over readings: differ by reading: not reproduced 20, partially 28
52 Outcome over readings (Euclidean; Hamming is a variant): differ by reading: partially 14, reproduced 10
55 Outcome over readings: not reproduced
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013 && python - <<'EOF'
import json
p='reproduce_bouchard_2013.ipynb'
nb=json.load(open(p))
i=59
s=''.join(nb['cells'][i]['source'])
a="The baseline, z-scoring, projection and CV set give similar mixes at every level."
assert a in s
s=s.replace(a,"Every level of the baseline, z-scoring,\nprojection and CV set has both reproduced and not reproduced readings.")
nb['cells'][i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
sed -i 's/It takes about 20 minutes, 14 of them streaming$/It takes about 21 minutes, about 16 of them streaming/; s/^  about 42 GB of raw ECoG and computing high gamma\./  39 GB of raw ECoG and computing high gamma./' README.md; grep -n "minutes" -A1 README.md
```

```
41:- `reproduce_bouchard_2013.ipynb`: the analysis. It takes about 21 minutes, about 16 of them streaming
42-  39 GB of raw ECoG and computing high gamma.
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('../../schemas/attempt.schema.json'));
v=d['properties']['verifications'];print(json.dumps(v,indent=1)[:3000])"
```

```
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 49 more lines not kept]
```

**Agent**

Now the attempt record edits: notes for fig2a and fig5d, the round-1 B3 gap, and the round-2 record.

**Agent calls Bash**

```bash
cd ../.. && python - <<'EOF'
p='attempts/000019-bouchard-2013-01.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a
    s=s.replace(a,b)
rep("""    and suppfig9. For information only, the median z coordinate of the top 10% of lips weights is
    above that of the tongue weights in EC2 (36.6 against 15.6) and GP31. The answer""",
"""    and suppfig9. For information only, under the first reading the median z coordinate of the top
    10% of lips weights is above that of the tongue weights in EC2 (36.6 against 15.6); GP31 has no
    tongue window in that reading, so it gives no comparison. The answer""")
rep("""    the first run. The reading of R decides the split; with the mean of three feature sets all 120
    readings fail.""",
"""    the first run. Two readings of the claims file decide the split, that of R and that of the
    clusters. With the mean of three feature sets all 120 readings fail, and with k-means clusters
    all 48 fail, the 24 with the matching feature set among them. Every level of the baseline,
    z-scoring, projection and CV set has both reproduced and not reproduced readings, so the split
    does not come from these details.""")
rep("""      49 to 9 and 43 to 0). One GP31 CV with 2 renditions drives the threshold count, and many methods_underspecified
      outcomes come from this split (B3).""",
"""      49 to 9 and 43 to 0). One GP31 CV with 2 renditions drives the threshold count. It also flips silhouettes
      (GP31 k = 2 at 0.78 against 0.37) and the fig4ef late-window tests. Many methods_underspecified outcomes
      come from this split (B3).""")
rep("""    inputs and compared the transcription of Supplementary Figure 1d with the supplement.
""","""    inputs and compared the transcription of Supplementary Figure 1d with the supplement. Cell numbers in
    the reasons are those of the round-1 notebook.
""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> attempts/000019-bouchard-2013-01.yaml <<'EOF'
- date: '2026-10-22'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full executed notebook of the run after round 1, with its conclusions and summary,
    the README, the helper module, the attempt record and the claims file. The verifier also read the paper,
    read the `separability` code of the helper module and checked the transcription of Supplementary Figure
    12 against the image in the supplement PDF. Cell numbers in the reasons are those of the round-2 notebook.
  results:
  - claim: data-composition
    agrees: true
    outcome: partially_reproduced
    reason: 'Agrees. B2 is still open and bears on this conclusion: that GP31 is EC31 and GP33 is EC33 remains
      an assumption, and GP33''s hemisphere cannot be checked. It is recorded as a deviation; no field in
      the files can settle it. Cell 10, a note and not a conclusion, says "EC9 has 24 consonant labels";
      cell 8 gives 19 plus /ch/, /dh/, /j/ and /sk/, which is 23.'
    response: Outcome kept. Cell 10 now says 23 consonant labels, as cell 8 prints. The identity of GP31 and
      GP33 stays an assumption, recorded as a deviation and a finding, since no field in the files settles it.
  - claim: active-electrodes
    agrees: true
    outcome: blocked
    reason: 'Agrees. B3 is still open: GP31''s /thi/, with 2 renditions, alone creates the CV-set split. The
      one reading within tolerance (rest, 15+ CVs: 27.0) relies on trials the files mark as ECoG artifacts.
      Without them, GP31''s count falls from 31 to 2 and the mean to 15.0. The blocked outcome stands, but
      under every variant tried no reading supports about 30 electrodes. The round-1 record dropped part of
      B3: that the /thi/ split also flips GP31''s silhouettes and the fig4ef late-window tests.'
    response: Outcome kept; the notes already state the artifact variant and the fall from 31 to 2. The round-1
      reason now carries the dropped part of B3.
  - claim: fig1c-e-articulator-electrodes
    agrees: true
    outcome: blocked
    reason: Agrees (metadata_insufficient). The round-1 cell numbers in the record are stale; "cell 22 prints
      `[]`" now refers to cell 26.
    response: Outcome kept. The round-1 entry now says its cell numbers are those of the round-1 notebook.
  - claim: fig1f-h-phonetic-contrasts
    agrees: true
    outcome: not_reproduced
    reason: Agrees. The counts and values in the record match the printed outputs.
    response: Outcome kept. No change.
  - claim: fig2a-lips-dorsal
    agrees: true
    outcome: blocked
    reason: 'Agrees (metadata_insufficient). The notes say "the median z coordinate of the top 10% of lips
      weights is above that of the tongue weights in EC2 (36.6 against 15.6) and GP31." Cell 32 prints `GP31:
      ... Tongue no window`, so there is no GP31 comparison. This is for information only and affects no outcome.'
    response: Outcome kept. The notes now give the EC2 comparison only and say that GP31 has no tongue window
      in that reading.
  - claim: fig2b-somatotopic-sequence
    agrees: true
    outcome: blocked
    reason: Agrees (metadata_insufficient).
    response: Outcome kept. No change.
  - claim: suppfig3b-spatial-clustering
    agrees: true
    outcome: blocked
    reason: Agrees (metadata_insufficient).
    response: Outcome kept. No change.
  - claim: suppfig3d-cross-subject
    agrees: true
    outcome: blocked
    reason: Agrees (metadata_insufficient).
    response: Outcome kept. No change.
  - claim: suppfig3f-dv-sequence
    agrees: true
    outcome: blocked
    reason: Agrees (metadata_insufficient).
    response: Outcome kept. No change.
  - claim: suppfig5-intermediate-organization
    agrees: true
    outcome: blocked
    reason: Agrees (metadata_insufficient).
    response: Outcome kept. No change.
  - claim: suppfig6-mixed-tuning
    agrees: true
    outcome: reproduced
    reason: 'Agrees. A place where the claims file may misread the paper: grouping electrodes by their largest
      weight almost guarantees the result, and the test also holds on permuted weights in 94 of 96 readings
      (cell 34). It is reproduced under a criterion that barely discriminates; the outcome is correct under
      that criterion, but it shows little.'
    response: Outcome kept, as the criterion decides it; the notes already say the test barely discriminates.
      The point is now a question for a reader in questions/000019.yaml; the claim is not changed.
  - claim: fig3d-timing-sequence
    agrees: true
    outcome: not_reproduced
    reason: Agrees. The counts and values in the record match the printed outputs.
    response: Outcome kept. No change.
  - claim: suppfig7-no-latency-difference
    agrees: true
    outcome: blocked
    reason: Agrees (metadata_insufficient).
    response: Outcome kept. No change.
  - claim: pca-nine-components
    agrees: true
    outcome: blocked
    reason: Agrees (methods_underspecified).
    response: Outcome kept. No change.
  - claim: fig4a-consonant-clusters
    agrees: true
    outcome: blocked
    reason: Agrees (methods_underspecified).
    response: Outcome kept. No change.
  - claim: suppfig11-co-clustering
    agrees: true
    outcome: blocked
    reason: Agrees (methods_underspecified). The Supplementary Figure 12 transcription was checked against the
      image extracted from the supplement PDF, and all 15 consonant rows and the 4 vowel rows match cell 16.
    response: Outcome kept. No change.
  - claim: fig4c-d-hierarchy
    agrees: true
    outcome: blocked
    reason: Agrees (methods_underspecified).
    response: Outcome kept. No change.
  - claim: fig4ef-feature-correlations
    agrees: true
    outcome: blocked
    reason: Agrees (methods_underspecified).
    response: Outcome kept. No change.
  - claim: fig5c-separability-timing
    agrees: true
    outcome: not_reproduced
    reason: Agrees. The `separability` code in `bouchard.py` now leaves out a token's pairs with its own copies,
      correctly (B7 resolved).
    response: Outcome kept. No change.
  - claim: fig5d-separability-coupling
    agrees: true
    outcome: blocked
    reason: 'Agrees (methods_underspecified). The README sentence that the claims blocked as methods underspecified
      depend on the CV set, baseline, z-scoring and projection, and the summary''s "The blocked outcomes of
      the state-space claims and of active-electrodes come from these readings giving different results", do
      not hold for fig5d. Cell 58 shows its split comes from the reading of R (all 120 "mean of three" readings
      fail) and from the cluster reading (all 48 k-means readings fail); the four listed factors show similar
      mixes at every level. Cell 59 and the notes, "the reading of R decides the split", are incomplete: with
      the matching feature set, k-means clusters still fail all 24 readings, so the cluster reading also splits
      the outcome.'
    response: Outcome kept. Cell 59, the notes, the summary and the README now say that the readings of R and
      of the clusters decide the split, with the k-means count (48 of 48 fail, the 24 with the matching set
      among them), and that every level of the four other details has both reproduced and not reproduced readings.
  - claim: suppfig13-consonant-vowel-distance
    agrees: true
    outcome: blocked
    reason: 'Agrees. A place where the claims file may misread the paper: a reading reproduces only if the pair
      count is 4623, a count fixed by which syllables the dataset holds, not by the effect the paper reports.
      Read strictly, every reading is not reproduced. Its outcome stays blocked only because the attempt treats
      the pair-count failure as partial, which rests on that claims-file issue.'
    response: Outcome kept, as verified; the notes already say that read strictly every reading is not reproduced.
      The pair-count condition is now a question for a reader in questions/000019.yaml; the claim is not changed.
  - claim: suppfig9-pc-articulator-weights
    agrees: true
    outcome: not_reproduced
    reason: 'Agrees. A place where the claims file may misread the paper: jaw against larynx is judged at p >
      0.05, but the paper says P > 0.2. This does not change the outcome, since the measured p is 5e-11.'
    response: Outcome kept. The threshold is now a question for a reader in questions/000019.yaml; the claim
      is not changed, and no reading is near either threshold.
EOF
tail -5 questions/000019.yaml
```

```
Sylvian Fissure" (Methods), and gives no way to derive these distances from grid
    geometry, unlabelled coordinates or atlas labels. The header's vSMC definition now says
    so; the spatial claims stay blocked as metadata_insufficient when the dataset lacks
    these positions. Claims unchanged.
  answered: 2026-10-22
```

**Agent calls Bash**

```bash
ls paper; grep -rn "4623\|4,623" paper | head; grep -rn "strongest articulator" paper | head -3
```

```
<persisted-output>
Output too large (51.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/263ae97e-6a85-4ff7-b611-bdc1b0b9953b/tool-results/b2wx2f1zs.txt

Preview (first 2KB):
10.1038-nature11911.supp.pdf
10.1038-nature11911.txt
paper/10.1038-nature11911.txt:7:Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC3606666 PMC3606666.1 3606666 3606666 NIHMS436351 23426266 10.1038/nature11911 NIHMS436351 NIHPA436351 1 Article Functional Organization of Human Sensorimotor Cortex for Speech Articulation Bouchard Kristofer E. 1 2 Mesgarani Nima 1 2 Johnson Keith 3 Chang Edward F. 1 2 4 1 Departments of Neurological Surgery and Physiology, University of California, San Francisco 2 Center for Integrative Neuroscience, University of California, San Francisco 3 Department of Linguistics, University of California, Berkeley 4 UCSF Epilepsy Center, University of California, San Francisco Correspondence and requests for materials should be addressed to E.F.C. ( [removed: an e-mail address] ) 20 2 2013 21 3 2013 495 7441 221018 327 332 24 01 2013 21 09 2013 21 09 2013 11 10 2026 Users may view, print, copy, download and text and data- mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms Speaking is one of the most complex actions we perform, yet nearly all of us learn to do it effortlessly. Production of fluent speech requires the precise, coordinated movement of multiple articulators (e.g., lips, jaw, tongue, larynx) over rapid time scales. Here, we used high-resolution, multi-electrode cortical recordings during the production of consonant-vowel syllables to determine the organization of speech sensorimotor cortex in humans. We found speech articulator representations that were somatotopically arr
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -o ".\{0,300\}4623.\{0,100\}" paper/10.1038-nature11911.txt | head -3; grep -o ".\{0,200\}P > 0.2.\{0,50\}\|.\{0,200\}P > 0\.2.\{0,50\}" paper/10.1038-nature11911.txt | head; grep -o ".\{0,100\}strongest articulator.\{0,100\}" paper/10.1038-nature11911.txt | head -2
```

Result: not kept, because it reads the paper's text.

**Agent**

Adding the three claims-file points as open questions for a reader.

**Agent calls Bash**

```bash
cat >> questions/000019.yaml <<'EOF'
- claim: suppfig13-consonant-vowel-distance
  asked: 2026-10-22
  question: The criterion makes a pair count of 4623 a condition of reproduction. Is the count meant as
    part of the result, or as a description of the paper's data, so that a dataset with other syllables
    (4677 or 4567 pairs here) is judged on the three orderings and their p-values alone?
  passage: Results, Dynamics of Phonetic Representations, "(P < 10 −10 for all comparisons, WSRT, n =
    4623 for all, Supplementary Figure 11 )"; Supplementary Figure 13 legend, "n = 4623 for all".
  why: Raised by the round-2 verifier as a place where the claims file may misread the paper. The count is
    fixed by which syllables the dataset holds (data-composition), not by the effect. Read strictly, no
    reading can reproduce; on the orderings alone 36 of 48 readings would reproduce and 12 would not, so
    the claim would stay blocked as methods_underspecified with reproduced and not reproduced readings.
- claim: suppfig6-mixed-tuning
  asked: 2026-10-22
  question: The criterion groups electrodes by their largest weight and asks that each group's preferred
    articulator have the largest mean share. Does the paper's "clear preferred tuning" mean more than this
    grouping gives, for example a share well above what weights shuffled across electrodes give?
  passage: Results, Spatial Representation of Articulators, "This analysis revealed clear preferred tuning
    for individual articulators at single electrodes (Fig. 2c, electrodes categorized according to the
    strongest articulator representation)"
  why: Raised by the round-2 verifier as a place where the claims file may misread the paper. Grouping by
    the largest weight puts the preferred articulator first almost by construction; the test holds on
    weights permuted across each subject's electrodes in 94 of 96 readings. Under a criterion that
    compares with such a null the outcome could differ.
- claim: suppfig9-pc-articulator-weights
  asked: 2026-10-22
  question: The criterion judges jaw against larynx as not differing at p > 0.05, while the legend reports
    P > 0.2. Which threshold should the absence be judged at?
  passage: Supplementary Figure 9a legend, "while the difference between jaw and larynx was not
    significant (P > 0.2)"
  why: Raised by the round-2 verifier as a place where the claims file may misread the paper. It does not
    change the outcome here (corrected p = 5e-11), but it would for a dataset with p between 0.05 and 0.2.
EOF
python -c "import yaml;yaml.safe_load(open('questions/000019.yaml'));yaml.safe_load(open('attempts/000019-bouchard-2013-01.yaml'))" && grep -n "—\|rather" questions/000019.yaml attempts/000019-bouchard-2013-01.yaml entries/000019-bouchard-2013/README.md | head; grep -o "suppfig13 orderings\|orderings alone" /dev/null
```

```
(Bash completed with no output)
```

**Agent**

Edits done; re-running the entry so the executed copy carries the final text.

**Agent calls Bash**

```bash
python tools/entry.py all entries/000019-bouchard-2013 2>&1 | tail -4
```

```
Installed kernelspec registry-000019-bouchard-2013 in executed/000019-bouchard-2013/.venv/share/jupyter/kernels/registry-000019-bouchard-2013
0 error(s)
pass  reproduce_bouchard_2013.ipynb  (1253 s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if i in (3,67): print(i,t)
    for line in t.splitlines():
        if line.startswith('Outcome over'): print(i,line)
EOF
git status --short
```

```
3 processed 24 blocks in 967 s
streamed 39.0 GB of raw ECoG

23 Outcome over readings: differ by reading: not reproduced 1, partially 1
29 Outcome over readings: not reproduced
34 Outcome over readings: reproduced
37 Outcome over readings (substitute acoustic onset): not reproduced
40 Outcome over readings: differ by reading: not reproduced 8, reproduced 16
43 Outcome over readings: differ by reading: not reproduced 23, partially 1
46 Outcome over readings: differ by reading: not reproduced 10, partially 38
49 Outcome over readings: differ by reading: not reproduced 20, partially 28
52 Outcome over readings (Euclidean; Hamming is a variant): differ by reading: partially 14, reproduced 10
55 Outcome over readings: not reproduced
58 Outcome over readings: differ by reading: not reproduced 145, partially 15, reproduced 80
61 Outcome over readings: differ by reading: not reproduced 12, partially 36
64 Outcome over readings: not reproduced
67 notebook ran in 20.7 min

 M attempts/000019-bouchard-2013-01.yaml
 M entries/000019-bouchard-2013/README.md
[... 13 more lines not kept]
```

**Agent**

No outcome changed. The verifier agreed with all 22 outcomes, so nothing went under `proposed`. The re-run (`tools/entry.py all`) passed with 0 check errors, and every outcome count it printed is the same as before, so the record's numbers stand.

**Corrected**
- **fig2a-lips-dorsal notes:** these now compare EC2 only (36.6 against 15.6). GP31 has no tongue window in that reading, so it gives no comparison.
- **fig5d split:** cell 59, the notes, the notebook summary and the README now say that two of the claims file's own readings decide the split. With the mean of three feature sets as R, all 120 readings fail. With k-means clusters, all 48 fail, including the 24 with the matching feature set. Every level of baseline, z-scoring, projection and CV set has both reproduced and not reproduced readings. The summary and README no longer say that fig5d's blocked outcome comes from those four details.
- **Cell 10:** EC9 has 23 consonant labels, not 24, matching cell 8.
- **README run time:** cell 3 now prints how much data is streamed (39.0 GB, not the 42 GB the README claimed). The README now says about 21 minutes, about 16 of them streaming 39 GB and computing high gamma. The run printed 967 s for processing and 20.7 min in total.
- **Round-1 record:**
  - The active-electrodes reason now includes the part of B3 it had dropped: the /thi/ split also flips GP31's silhouettes and the fig4ef late-window tests.
  - The round-1 `reviewed` field now says its cell numbers are those of the round-1 notebook.

**Added**
- **Round-2 entry under `verifications`:** for each claim it records agreement, the verifier's outcome, its reason quoted or closely paraphrased, and my response.
- **Three new questions in `questions/000019.yaml`:** these cover the places where the verifier thinks the claims file may misread the paper. They are unanswered.
  - **suppfig13:** whether the 4623 pair count should be a condition for reproduction.
  - **suppfig6:** whether "clear preferred tuning" needs more than grouping by the largest weight gives.
  - **suppfig9:** whether jaw against larynx should be judged at p > 0.05 or at the paper's P > 0.2.

**Not done**
- I did not change any claim, as the rules say; the three points above wait for a reader.
- I left the round-1 "the verifier asked for" sentences as they were. The verifier said that paraphrase was acceptable.
- B2 (GP31 and GP33 identity) and B3 (the /thi/ split) remain open. Nothing in the files can settle them, and they are recorded as a deviation and in the notes.
- Untracked dotfiles and a `scripts` folder appeared at the repo root, which I did not create, and I left them alone. Nothing is committed.

## End of run

30 turns, 46 minutes, result: success.
