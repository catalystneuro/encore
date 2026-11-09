# 000061 · claims-check · run 39471816668

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000061/ paper/ | head -50; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 93,220p docs/protocol.md; python tools/claims_check.py claims/000061/10.1038-nn.4637.yaml paper/10.1038-nn.4637.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/000061/10.1038-nn.4637.yaml
```

```
<persisted-output>
Output too large (57.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/9383d2a1-38be-4ae2-8ed9-2064ce7b54c0/tool-results/b1t9iq5j7.txt

Preview (first 2KB):
# Claims for Girardeau, Inema & Buzsaki (2017), Nat. Neurosci. 20, 1634-1642, on dandiset 000061.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20, protocol
# pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4). The reader did not look at the
# dandiset's data or files; only its archive title and description, which name this paper.
#
# Why this file was rewritten. The earlier file was written from the abstract alone (the full text
# was not open then) and its methods were fixed by an agent. Read against the full text and the
# supplement on 2026-10-20, two of its claims were tested with measures the paper does not use:
# aversive-direction-stronger (the paper compares peri-ripple reactivation strength R of a run
# correlation template, Fig. 6b, not singular-vector patterns over all sleep bins) and
# reactivation-involves-ripple-up-cells (the paper compares post-NREM minus pre-NREM pair
# correlations across nine pair groups with a one-way ANOVA, Fig. 5a, not BLA pattern weights). The
# other claims of that file also used agent-chosen methods (SVD patterns, shuffled ripple windows)
# in place of the paper's EV/REV, Poisson ripple-modulation test and reactivation strength R, and
# many findings had no claim. Every criterion is now taken from the Online Methods, the legends,
# the supplement and the paper's code. Ids are kept where the finding is the same:
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000061/10.1038-nn.4637.yaml"
}
```

```
1	# Claims for Girardeau, Inema & Buzsaki (2017), Nat. Neurosci. 20, 1634-1642, on dandiset 000061.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20, protocol
3	# pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4). The reader did not look at the
4	# dandiset's data or files; only its archive title and description, which name this paper.
5	#
6	# Why this file was rewritten. The earlier file was written from the abstract alone (the full text
7	# was not open then) and its methods were fixed by an agent. Read against the full text and the
8	# supplement on 2026-10-20, two of its claims were tested with measures the paper does not use:
9	# aversive-direction-stronger (the paper compares peri-ripple reactivation strength R of a run
10	# correlation template, Fig. 6b, not singular-vector patterns over all sleep bins) and
11	# reactivation-involves-ripple-up-cells (the paper compares post-NREM minus pre-NREM pair
12	# correlations across nine pair groups with a one-way ANOVA, Fig. 5a, not BLA pattern weights). The
13	# other claims of that file also used agent-chosen methods (SVD patterns, shuffled ripple windows)
14	# in place of the paper's EV/REV, Poisson ripple-modulation test and reactivation strength R, and
15	# many findings had no claim. Every criterion is now taken from the Online Methods, the legends,
16	# the supplement and the paper's code. Ids are kept where the finding is the same:
17	# hpc-bla-reactivation-post-sleep (EV against REV, Fig. 3c), reactivation-peaks-at-ripples
18	# (Supplementary Fig. 11a), bla-ripple-up-subgroup (Fig. 4), reactivation-involves-ripple-up-cells
19	# (Fig. 5a), aversive-direction-stronger (Fig. 6b) and rats-learn-puff-location (Fig. 1b). The
20	# other 25 claims are new.
[... 1053 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/10.1038-nn.4637.txt; wc -c paper/10.1038-nn.4637.txt; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker flags 4 values it could not match. I'm reading the paper text now to check those and every claim.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4637.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4637.txt",
 "offset": 1111,
 "limit": 720
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "inferred\|checks\|ready\|changes\|p_relation\|def \|KEYS\|allowed" tools/claims_check.py | head -60; grep -rln "^checks:" claims | head -3; ls; ls -d */
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
105:def main() -> int:
LICENSE
README.md
attempts
bunfig.toml
claims
docs
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 55,105p tools/claims_check.py; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
print(json.dumps(s.get('properties',{}).get('checks'),indent=1)[:1500]);
c=s['\$defs'] if '\$defs' in s else s.get('definitions');print(list(c.keys()))"
```

```
if i < 0:
                break
            pos = i + len(f)
        else:
            return True
    return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
c=s['properties']['claims']['items'];print(json.dumps({k:v for k,v in c.items() if k!='properties'},indent=1)[:1500]);print(list(c['properties'].keys()))"
```

```
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "id",
  "statement",
  "source"
 ],
 "allOf": [
  {
   "not": {
    "required": [
     "quote",
     "inferred"
    ]
   }
  },
  {
   "if": {
    "properties": {
[... 36 more lines not kept]
```

**Agent**

I've confirmed the 4 flagged values by reading: the text prints them as "9.70 × 10−9" and "x10-05", which the checker doesn't match. Now editing the claims I found problems in.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "    when EV exceeds REV with p < 0.05 and the expected values hold (the mean EV - REV of 3.13 +-\n    0.73% s.e.m. is from Results, A subset of BLA cells, paragraph 1, Fig. 3d test); partially",
 "new_string": "    when EV exceeds REV with p < 0.05 and the expected values hold (the mean EV - REV of 3.13 +-\n    0.73% s.e.m. is from Results, BLA-hippocampus coordinated reactivations during NREM sleep,\n    paragraph 2, the Fig. 3d test); partially"
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "  - about: EV against REV over the first, second and third 20 min of NREM, all cell pairs\n    test: Wilcoxon signed rank tests\n    statistic: z = 3.91; z = 2.98; z = -0.71\n    p: 8.85e-5\n    n: 17 sessions in 3 rats",
 "new_string": "  - about: EV against REV, 0-20 min of post-NREM, all cell pairs\n    test: Wilcoxon signed rank test\n    statistic: z = 3.91\n    p: 8.85e-5\n    n: 17 sessions in 3 rats\n  - about: EV against REV, 20-40 min, all cell pairs\n    test: Wilcoxon signed rank test\n    statistic: z = 2.98\n    p: 0.00282\n    n: 17 sessions in 3 rats\n  - about: EV against REV, 40-60 min, all cell pairs\n    test: Wilcoxon signed rank test\n    statistic: z = -0.71\n    p: 0.14458\n    n: 17 sessions in 3 rats"
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "  statement: Hippocampus-BLA reactivations are not significant in REM sleep.",
 "new_string": "  statement: Hippocampus-BLA and hippocampus-piriform cortex reactivations are not significant in\n    REM sleep."
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "    p: 0.47583\n    n: 25 sessions in 3 rats\n  criterion: A claim of absence, judged on the paper's test. EV and REV (M4) from the REM bins of\n    pre- and post-sleep, sessions with more than 180 s of REM in each, pyramidal pairs; two-sided\n    Wilcoxon signed rank test of EV against REV. Reproduced when p >= 0.05, not reproduced when\n    p < 0.05; the median EV - REV is reported. All cell pairs shown as a variant.",
 "new_string": "    p: 0.47583\n    n: 25 sessions in 3 rats\n  - about: EV against REV, REM, hippocampus-piriform pyramidal pairs (Fig. 3d)\n    test: Wilcoxon signed rank test\n    p: 0.301\n    n: 15 sessions in 3 rats\n  criterion: A claim of absence, judged on the paper's test. EV and REV (M4) from the REM bins of\n    pre- and post-sleep, sessions with more than 180 s of REM in each, pyramidal pairs; two-sided\n    Wilcoxon signed rank test of EV against REV, for hippocampus-BLA pairs and for\n    hippocampus-piriform pairs (piriform units per M1). Reproduced when neither test has p < 0.05,\n    not reproduced when either does; the median EV - REV is reported. Hippocampus-BLA all cell\n    pairs shown as a variant. Central nuclei REM is in cen-no-reactivation and intra-structure REM\n    in intra-structure-reactivation."
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "  quote: Intra-structure reactivations for hippocampus and BLA.\n  statistics:",
 "new_string": "  inferred: No sentence states this finding. It is read from the tests in the Supplementary Fig. 4\n    legend (titled \"Intra-structure reactivations for hippocampus and BLA\"), with the REM part also\n    covered by the Results sentence that REM reactivations were not significant in any structure.\n  statistics:"
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "  - about: second, third and fourth quartiles separately (Supplementary Fig. 8a)\n    test: Wilcoxon signed rank one-tailed tests\n    statistic: z = 0.7839; z = 1.8873; z = 1.5420\n    p: 0.7834\n    n: 18, 16 and 39 cells",
 "new_string": "  - about: second quartile, upmodulated cells (Supplementary Fig. 8a)\n    test: Wilcoxon signed rank one-tailed test\n    statistic: z = 0.7839\n    p: 0.7834\n    n: 18 cells\n  - about: third quartile, upmodulated cells (Supplementary Fig. 8a)\n    test: Wilcoxon signed rank one-tailed test\n    statistic: z = 1.8873\n    p: 0.9704\n    n: 16 cells\n  - about: fourth quartile, upmodulated cells (Supplementary Fig. 8a)\n    test: Wilcoxon signed rank one-tailed test\n    statistic: z = 1.5420\n    p: 0.9384\n    n: 39 cells"
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "  criterion: A claim of absence, judged on the paper's test, a two-sided Wilcoxon signed rank test\n    across BLA cells of the sessions entering aversive-direction-stronger, safe against air puff\n    rate in the run epoch, for pyramidal cells and for all cells. The rate per O7, both readings,\n    laps per O1. Reproduced when neither test has p < 0.05; not reproduced when either does under\n    every reading. Median differences reported.",
 "new_string": "  criterion: A claim of absence, judged on the paper's test, a two-sided Wilcoxon signed rank test\n    across BLA cells, safe against air puff rate in the run epoch, for pyramidal cells and for all\n    cells. The paper gives no n and does not say which sessions enter; readings (a) the BLA cells\n    of the sessions entering aversive-direction-stronger (pyramidal) and direction-all-cell-pairs\n    (all cells); (b) all BLA cells of sessions with a run epoch. The rate per O7, both readings,\n    laps per O1. Reproduced when neither test has p < 0.05 under every reading; not reproduced\n    when either test has p < 0.05 under every reading; methods_underspecified when the readings\n    disagree. Median differences reported."
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "    post-run tests are reported.\n- id: dz-speed-slower-post-run",
 "new_string": "    post-run tests are reported.\n- id: each-rat-learns-puff-location\n  statement: The speed ratio changes across pre-run, run and post-run in each of the four rats\n    taken alone, indicating that every rat learned the new air puff location.\n  source: Supplementary Fig. 1b legend\n  quote: The reversal of ratio between pre and post RUN indicates that all animals learned the new\n    location during RUN and remembered it during post-RUN\n  statistics:\n  - about: speed ratio over pre-run, run and post-run, rat 1\n    test: one-way repeated measure ANOVA\n    statistic: F = 13.26, d.f. = 2\n    p: 0.000214\n    n: 11 sessions\n  - about: the same, rat 2\n    test: one-way repeated measure ANOVA\n    statistic: F = 7.02, d.f. = 2\n    p: 0.00556\n    n: 10 sessions\n  - about: the same, rat 3\n    test: one-way repeated measure ANOVA\n    statistic: F = 27.41, d.f. = 2\n    p: 3.9469e-7\n    n: 14 sessions\n  - about: the same, rat 4\n    test: one-way repeated measure ANOVA\n    statistic: F = 4.36, d.f. = 2\n    p: 0.021754\n    n: 16 sessions\n  depends_on:\n  - rats-learn-puff-location\n  criterion: The per-session speed ratios of rats-learn-puff-location (each O1 reading), split by\n    rat. Per rat, a one-way repeated-measures ANOVA over the three epochs (Supplementary Fig. 1b\n    legend). Reproduced when every rat has p < 0.05 and a post-run ratio above its pre-run ratio\n    (median over sessions); partially reproduced when three of the four rats do. The legend's\n    Bonferroni-corrected post hoc tests are shown but give no P values to match.\n- id: dz-speed-slower-post-run"
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "    right). Reproduced when p >= 0.05; not reproduced when p < 0.05. Median difference reported.",
 "new_string": "    right; Supplementary Fig. 11d prints P = 0.1972 for the same test). Reproduced when p >= 0.05;\n    not reproduced when p < 0.05. Median difference reported."
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000061/10.1038-nn.4637.yaml",
 "old_string": "    legend). Reproduced when every rat has p < 0.05 and a post-run ratio above its pre-run ratio\n    (median over sessions); partially reproduced when three of the four rats do. The legend's",
 "new_string": "    legend). Reproduced when every rat has p < 0.05; partially reproduced when three of the four\n    rats do. The legend's"
}
```

```
The file claims/000061/10.1038-nn.4637.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> claims/000061/10.1038-nn.4637.yaml <<'EOF'
checks:
- date: "2026-10-20"
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - The four values the quote checker flagged (9.70e-9, 8.85e-5, 7.75e-5, 6.45e-5) were confirmed by reading; the text prints them as "9.70 x 10-9" and "x10-05", forms the checker does not match.
  - hpc-bla-reactivation-post-sleep, the criterion cited the 3.13 +- 0.73% value to Results, A subset of BLA cells, paragraph 1; it is in Results, BLA-hippocampus coordinated reactivations during NREM sleep, paragraph 2. Corrected.
  - reactivation-all-cell-pairs, one statistics entry held three 20-min tests with only the first P; split into three entries with the P values of Supplementary Fig. 5a (8.85e-5, 0.00282, 0.14458).
  - contributing-up-cells-gain-increase, one statistics entry held the three lower quartile tests with only the second quartile P; split into three entries with the P values of Supplementary Fig. 8a (0.7834, 0.9704, 0.9384).
  - no-rem-reactivation, the paper says REM reactivations were not significant in any structure, citing Fig. 3c-e; the statement covered only hippocampus-BLA. Added the hippocampus-piriform REM test of Fig. 3d (P = 0.301, n = 15) to the statement, statistics and criterion.
  - intra-structure-reactivation, the quote was the figure title, which does not state the finding; replaced by an inferred note saying the finding is read from the Supplementary Fig. 4 legend tests.
  - bla-rate-same-across-directions, the criterion fixed the cells to the sessions of aversive-direction-stronger, which the paper does not say, and its outcome rule left the case of disagreeing readings undecided. Named the session sets as readings and added the methods_underspecified case.
  - ripple-rate-unchanged, noted in the criterion that Supplementary Fig. 11d prints P = 0.1972 for the test the main text gives as 0.192.
  - Added claim each-rat-learns-puff-location for the per-rat ANOVAs of Supplementary Fig. 1b ("all animals learned"), a finding with no claim.
  - Open, the paper's code (github.com/buzsakilab/papers) was not available to this check, so the details the criteria take from it (script names, smoothing, cell minimums, tails, run.signot, ExplainedVariance_Ultimate_IntraStruct.m, which is not in the header's list of scripts read) were not re-verified.
  - Open, no-rem-reactivation and M4 use more than 180 s of REM; the Methods say a minimum of 3 min. The difference cannot matter unless a session has exactly 180 s.
  - Open, habituation-over-days and ev-independent-of-firing-rate rest on readings of a figure the paper does not test; the criteria name them and fall back to methods_underspecified when they disagree.
EOF
python tools/claims_check.py claims/000061/10.1038-nn.4637.yaml paper/10.1038-nn.4637.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000061 && sed -i 's/- The four values the quote checker flagged (9.70e-9, 8.85e-5, 7.75e-5, 6.45e-5) were confirmed by reading; the text prints them as "9.70 x 10-9" and "x10-05"/- The five values the quote checker flags (9.70e-9, 8.85e-5, 7.75e-5, 6.45e-5, and 3.9469e-7 of the new claim) were confirmed by reading; the text prints them as "9.70 x 10-9" and "x10-05" or "x10-07"/' 10.1038-nn.4637.yaml && grep -n "five values" 10.1038-nn.4637.yaml && grep -nE '^[^#]*[^"]: [^"]*: ' 10.1038-nn.4637.yaml | grep -v "^\s*#" | head; cd ../.. && python tools/claims_check.py claims/000061/10.1038-nn.4637.yaml paper/10.1038-nn.4637.txt | tail -1
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for 000061 is fit for an attempt, and its new `checks` entry says `ready: true`. I made eight corrections and added one claim. The paper's code was not available to me, so the method details taken from it are still unchecked.

**Checker result:** `32 claims, 31 quotes, 67 statistical values, 5 problems`. All 5 are p-values the checker can't match against the paper's print format, such as "9.70 × 10−9" or "x10-05". I found each one in the text, so the file has no real problems. It passes schema validation and every quote matches word for word.

**Changes, by claim:**
- **hpc-bla-reactivation-post-sleep:** the criterion cited the wrong section for the 3.13 ± 0.73% value. It is in "BLA-hippocampus coordinated reactivations during NREM sleep", paragraph 2.
- **reactivation-all-cell-pairs:** one statistics entry held three tests (the three 20-minute periods) but only the first p-value. I split it into three entries with the supplement's values (8.85e-5, 0.00282, 0.14458).
- **contributing-up-cells-gain-increase:** the same problem for quartiles 2 to 4. Split into three, with p = 0.7834, 0.9704 and 0.9384.
- **no-rem-reactivation:** the paper says REM reactivations were not significant "in any structure". I added the hippocampus-piriform REM test (Fig. 3d, P = 0.301, n = 15) to the statement, statistics and criterion.
- **intra-structure-reactivation:** the quote was only a figure title, which does not state the finding. I replaced it with an `inferred` note saying the finding is read from the Supplementary Fig. 4 legend's tests.
- **bla-rate-same-across-directions:** the criterion picked a set of sessions the paper does not specify. I named the two plausible session sets as readings, and added the rule for when they disagree (`methods_underspecified`).
- **ripple-rate-unchanged:** noted that Supplementary Fig. 11d prints P = 0.1972 where the main text gives 0.192.
- **New claim `each-rat-learns-puff-location`:** covers the per-rat analyses of variance in Supplementary Fig. 1b ("all animals learned"), a finding that had no claim.

No claim ids were changed. The file's opening comment still says "25 other claims are new"; the checks entry records the added claim.

**Still open:**
- The details the criteria take from the paper's code are unchecked: script names, smoothing, cell minimums, test tails, `run.signot`. One cited script, `ExplainedVariance_Ultimate_IntraStruct.m`, is not in the file header's list of scripts read.
- The criteria require "more than 180 s" of REM, while the Methods say "a minimum of 3 min". This only matters for a session with exactly 180 s.
- **habituation-over-days** and **ev-independent-of-firing-rate** rest on readings of figures the paper never tests. Both name their readings and fall back to `methods_underspecified` when the readings disagree.

Nothing was committed.

## End of run

23 turns, 3 minutes, result: success.
