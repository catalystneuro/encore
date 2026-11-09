# 000404 · claims-check · run 39975665811

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/000404/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 96,220p docs/protocol.md; python tools/claims_check.py claims/000404/10.1016-j.cub.2023.06.027.yaml paper/10.1016-j.cub.2023.06.027.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/000404/10.1016-j.cub.2023.06.027.yaml; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000404/10.1016-j.cub.2023.06.027.yaml"
}
```

```
1	# Claims for Athalye, Khanna, Gowda, Orsborn, Costa & Carmena (2023), "Invariant neural dynamics
2	# drive commands to control different movements", Current Biology 33, 2962-2976, on dandiset 000404
3	# ("Monkey 2D cursor BMI").
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
5	# pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
6	#
7	# Text read: the accepted author manuscript in PubMed Central (PMC10527529, NIHMS1910377), full text
8	# (paper/10.1016-j.cub.2023.06.027.txt): Summary, Results, Discussion, STAR Methods, all figure
9	# legends, and the supplement (NIHMS1910377-supplement-2.pdf, extracted into the same file):
10	# legends of Figures S1 to S6, Table S1 (comparisons with shuffled data, Figures 3 to 5) and Table
11	# S2 (simulation statistics, Figure 6). The columns of Tables S1 and S2 were read from the
12	# supplement PDF (pages 15 and 16), as the text extraction splits them into cells. The version of
13	# record is not open access. The bioRxiv preprint (10.1101/2021.08.27.457931, the paper the
14	# dandiset names) is also under paper/ and was not used; the version of record replaces it.
15	#
16	# Code read: https://github.com/pkhanna104/bmi_dynamics_code at commit 416187366f84f2b7367ac54205aa321480e1acd1
17	# (2023-06-04; archived as Zenodo 10.5281/zenodo.8006653). It holds the preprocessing of the HDF and
18	# decoder files (prelim_analysis.py, resim_ppf/ppf_pa.py), the model fitting
19	# (online_analysis/generate_models*.py), the analyses behind each figure (online_analysis/
20	# plot_fr_diffs.py, plot_pred_fr_diffs.py, generalization_plots.py, pred_fwd.py, util_fcns.py),
[... 906 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000404/10.1016-j.cub.2023.06.027.yaml",
 "offset": 927
}
```

```
927	    statistic: N = 1629, z = 14.18
928	    p: 1.22e-45
929	  - about: dynamics-predicted distances, Monkey G, pooled
930	    test: linear mixed effect model, command identity and session as random effects
931	    statistic: N = 4674, z = 33.1
932	    p: 3.92e-240
933	  - about: dynamics-predicted distances, Monkey J, pooled
934	    test: linear mixed effect model, command identity and session as random effects
935	    statistic: N = 1629, z = 22.5
936	    p: 5.93e-112
937	  criterion: For commands used in more than five conditions, each pair of conditions with 15 or
938	    more occurrences; neural distance is the decoder-null population distance between the two
939	    conditions' mean activity (true, or predicted by the dynamics model), behavior distance the L2
940	    norm of the difference of their command subtrajectories (Methods, Correlating neural distance
941	    with behavior). statsmodels mixedlm of neural on behavior distance with a random intercept per
942	    command and session (plot_pred_fr_diffs.py 2335-2760). Reproduced when, in each monkey, the
943	    pooled slope is positive with p < 0.001 for both true and predicted distances.
944	- id: figs6k-next-command-pairs
945	  statement: Across pairs of conditions, the dynamics-predicted distance between the next commands
946	    that follow the same command correlates with the true distance.
[... 157 more lines not kept]
```

**Agent**

Checker reports 0 problems across 29 claims. Now reading the paper to check each claim's content.

**Agent calls Bash**

```bash
cd  wc -lc paper/10.1016-j.cub.2023.06.027.txt; ls ..; ls / | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2023.06.027.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2023.06.027.txt",
 "offset": 400,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2023.06.027.txt",
 "offset": 700,
 "limit": 80
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Figure S\|Table S" paper/10.1016-j.cub.2023.06.027.txt | awk -F: '$1>900' | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2023.06.027.txt",
 "offset": 1120,
 "limit": 330
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2023.06.027.txt",
 "offset": 1449,
 "limit": 590
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
from scipy import stats
for t,df in [(7.182,8),(7.182,17),(5.141,3),(5.141,7)]: print(t,df,2*stats.t.sf(t,df))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy import stats
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd  ls; python -c "import scipy; print(scipy.__version__)" 2>&1; ls .venv 2>/dev/null
```

```
Exit code 2
LICENSE
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import math
def pdf(x,v): return math.gamma((v+1)/2)/(math.sqrt(v*math.pi)*math.gamma(v/2))*(1+x*x/v)**(-(v+1)/2)
def sf(t,v):
  # integrate t..t+L with simpson then tail substitution
  n=200000; a=t; b=t+2000.0; h=(b-a)/n
  s=pdf(a,v)+pdf(b,v)+sum((4 if i%2 else 2)*pdf(a+i*h,v) for i in range(1,n))
  return s*h/3
for t,df in [(7.182,8),(7.182,17),(5.141,3),(5.141,7)]: print(t,df,2*sf(t,df))"
```

```
7.182 8 9.40925309628505e-05
7.182 17 1.5346306740407836e-06
5.141 3 0.01426012914567977
5.141 7 0.0013372567326800098
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='claims/000404/10.1016-j.cub.2023.06.027.yaml'
s=open(p).read()
reps=[
("""  source: Results, BMI to study neural population control of movement, paragraph 3; Methods,
    Neuroprosthetic tasks""",
"""  source: Results, BMI to study neural population control of movement, paragraph beginning "To
    study control of diverse movements"; Methods, Neuroprosthetic tasks"""),
("""  source: Results, BMI to study neural population control of movement, paragraph 4; Figure S1B;
    Methods, Conditions that used a command regularly""",
"""  source: Results, BMI to study neural population control of movement, paragraph beginning
    "Importantly, the BMI enabled us"; Figure S1B; Methods, Conditions that used a command regularly"""),
("""  source: Figure 4C legend; Results, Invariant dynamics predict the different neural activity
    patterns used to issue the same command, paragraph 4; Table S1 (rows 4C)""",
"""  source: Figure 4C legend; Results, Invariant dynamics predict the different neural activity
    patterns used to issue the same command, paragraph beginning "On the level of single time
    points"; Table S1 (rows 4C)"""),
("""  statement: Invariant dynamics predict 20% to 40% of the condition-specific component of neural
    activity (the part not explained by the command alone), far above shuffle dynamics.
  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph 5; Figure 4F; Table S1 (row 4F)""",
"""  statement: Invariant dynamics predict 20% to 40% of the condition-specific component of neural
    activity (the part not explained by the command alone), significantly more than shuffle
    dynamics.
  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph beginning "The invariant dynamics model also predicted"; Figure 4F;
    Table S1 (row 4F)"""),
("""  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph 5; Figure 4G""",
"""  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph beginning "The invariant dynamics model also predicted"; Figure 4G"""),
("""  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph 2; Figure S3B and S3C""",
"""  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph beginning "We found that the dynamics were low-dimensional"; Figure
    S3B and S3C legends"""),
("""  source: Figure S5B legend; Results, Invariant dynamics predict the different neural activity
    patterns used to issue the same command, paragraph 4""",
"""  source: Figure S5B legend; Results, Invariant dynamics predict the different neural activity
    patterns used to issue the same command, paragraph beginning "On the level of single time
    points\""""),
("""  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph 2; Figure S5F""",
"""  source: Results, Invariant dynamics predict the different neural activity patterns used to issue
    the same command, paragraph beginning "We found that the dynamics were low-dimensional"; Figure
    S5F legend"""),
("""  source: Figure S6C and S6D legends; Results, Invariant dynamics predict the different neural
    activity patterns used to issue the same command, paragraph 6""",
"""  source: Figure S6C and S6D legends; Results, Invariant dynamics predict the different neural
    activity patterns used to issue the same command, paragraph beginning "Finally, the dynamics
    model preserved structure\""""),
# figs5b readings
("""Held-out R2 pooled over neurons. The paper's N
    (18 and 8) is twice the number of sessions, while the code pairs one R2 per session
    (plot_pred_fr_diffs.py 192); readings, (a) one pair per session; (b) one pair per session and
    task. Reproduced when, under one reading, a paired t-test gives p < 0.05 in each monkey with the
    model with dynamics higher.""",
"""Held-out R2 pooled over neurons. One pair per session, as the
    Methods say ("session was paired") and the code does (plot_pred_fr_diffs.py 192); the paper's N
    (18 and 8) counts the two R2 values of each of the 9 and 4 sessions, as its p-values are those
    of a paired t-test with 8 and 3 degrees of freedom (T = -7.182 gives p = 9.4e-05 with 8; T =
    -5.141 gives p = 0.0143 with 3). Reproduced when a paired t-test gives p < 0.05 in each monkey
    with the model with dynamics higher."""),
# fig4c legend support
("""trained without the bins issuing that command (the code also drops bins whose
    command at t-1 is that command, generalization_plots.py 940-1080)""",
"""trained without the bins issuing that command (Figure S4A legend, activity that
    transitions to and from the command is left out; the code drops bins whose command at t or t-1
    is that command, generalization_plots.py 940-1080)"""),
# figs6cd normalization
("""for
    the population (decoder-null L2 norm divided by the square root of its dimension)""",
"""for
    the population (decoder-null L2 norm divided by the square root of the number of neurons,
    Methods, Analysis of activity issuing a given command)"""),
# fig6d absence
("""Reproduced when the LME gives p
    >= 0.05 in each monkey and the Wilcoxon p >= 0.05 in every session; not reproduced when the
    LME finds a difference; the effect size is reported either way.""",
"""Reproduced when the LME gives p
    >= 0.05 in each monkey and the Wilcoxon p >= 0.05 in every session; not reproduced when the
    LME, or the Wilcoxon in any session, finds a difference; the effect size is reported either
    way."""),
# fig5e about
("""  - about: condition left-out dynamics, Monkey J sessions""",
"""  - about: condition left-out dynamics, each session"""),
]
for a,b in reps:
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000404/10.1016-j.cub.2023.06.027.yaml",
 "old_string": "    p: 0.136\n  - about: Full Dynamics Model, each session",
 "new_string": "    p: 0.136\n  - about: No Dynamics Model of the decoder-null comparison against shuffle, Monkey G, pooled\n    test: linear mixed effect model, session as random effect\n    statistic: z = 0.611, N = 4482\n    p: 0.541\n  - about: No Dynamics Model of the decoder-null comparison against shuffle, Monkey J, pooled\n    test: linear mixed effect model, session as random effect\n    statistic: z = 0.449, N = 2250\n    p: 0.654\n  - about: Full Dynamics Model, each session"
}
```

```
The file claims/000404/10.1016-j.cub.2023.06.027.yaml has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000404/10.1016-j.cub.2023.06.027.yaml",
 "old_string": "per tuple the decoder-null population distance (as in\n    fig3d) and the mean of its 1000-sample null (Methods, Simulated activity issuing a given\n    command; the code draws condition-sized subsamples of the matched pool, LQR/analyze_lqr.py\n    177-326).",
 "new_string": "per tuple the decoder-null population distance (as in\n    fig3d) and the mean of its null. The Methods compare each model with its own behavior-preserving\n    shuffle (Methods, Simulated activity issuing a given command) and do not give the number of\n    shuffles for the simulations; the code draws condition-sized subsamples of the matched pool\n    (LQR/analyze_lqr.py 177-326). Readings, (a) behavior-preserving shuffle of the simulated\n    activity, 1000 shuffles as for the recorded data; (b) the code's subsampling."
}
```

```
The file claims/000404/10.1016-j.cub.2023.06.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000404/10.1016-j.cub.2023.06.027.yaml",
 "old_string": "the No Dynamics and Decoder-null models give LME p >= 0.05 in each monkey. Partially",
 "new_string": "the No Dynamics models (of both comparisons) and the Decoder-null model give LME p >= 0.05 in\n    each monkey, and Mann-Whitney p >= 0.05 in every session (Figure 6G and 6H legends). Partially"
}
```

```
The file claims/000404/10.1016-j.cub.2023.06.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000404/10.1016-j.cub.2023.06.027.yaml",
 "old_string": "null; distances are divided by the bootstrap mean. Session and pooled tests as in the shared\n    method.",
 "new_string": "null; distances are divided by the bootstrap mean. The Statistics Summary names the\n    behavior-preserving shuffle for Figures S1D and S1E, but that shuffle permutes activity and\n    leaves commands unchanged, so it gives no null for command distances; the subsampling of the\n    Methods section and the legend is the test. Session and pooled tests as in the shared method."
}
```

```
The file claims/000404/10.1016-j.cub.2023.06.027.yaml has been updated successfully.
```

**Agent**

Now appending the checks entry.

**Agent calls Bash**

```bash
cd  f=claims/000404/10.1016-j.cub.2023.06.027.yaml; grep -n "^checks" $f; tail -c 200 $f | od -c | tail -3; cat >> $f <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - conditions-per-session, figs1b-conditions-per-command, fig4c-dynamics-predict-activity-given-command, fig4f-condition-specific-component, fig4g-majority-predicted, figs3-low-dimensional-decaying-dynamics, figs5b-dynamics-beyond-behavior, figs5f-nonlinear-no-better and figs6cd-pairwise-distances-predicted, sources now name the Results paragraph by its opening words; several paragraph numbers were off by one (the cited sentences of fig4c, fig4f, fig4g, figs5b and figs6cd are in paragraphs 5, 6, 6, 5 and 7 of their section), and numbering is ambiguous where equations split paragraphs.
  - fig4f-condition-specific-component, statement says "significantly more than shuffle dynamics" in place of "far above", which the paper does not say (Figure 4F legend, "significantly more variance").
  - figs5b-dynamics-beyond-behavior, reading (b) (one pair per session and task) removed; the paper's p-values are those of paired t-tests with 8 and 3 degrees of freedom (T = -7.182 gives p = 9.4e-05 with 8, T = -5.141 gives p = 0.0143 with 3), so the pairs are the 9 and 4 sessions, as the Methods say, and N counts the R2 values.
  - fig4c-dynamics-predict-activity-given-command, the leaving out of transitions to and from a left-out command is now cited to the Figure S4A legend, which states it, and not to the code alone.
  - figs6cd-pairwise-distances-predicted, population distance is normalized by the square root of the number of neurons (Methods), not of the null-space dimension; this does not change r or the slope.
  - fig6d-decoder-null-dynamics-no-saving, the absence is also not reproduced when the per-session Wilcoxon finds a difference, as the paper's test includes the sessions (0/9 [0/4]).
  - fig6g-ofc-uses-distinct-patterns, added the Table S2 statistics for the decoder-null comparison's own No Dynamics Model against shuffle (Figure 6H, z = 0.611 and 0.449), and the criterion now requires that absence too and the per-session Mann-Whitney absences of the legends.
  - fig6g-ofc-uses-distinct-patterns, the null had only the code's subsampling; the Methods name the behavior-preserving shuffle for the simulations and give no shuffle count, so both are now readings.
  - figs1d-command-subtrajectories-differ, the criterion now says why the Statistics Summary's "behavior-preserving shuffle" for Figures S1D and S1E is not used (that shuffle leaves commands unchanged); the Methods and the legend give subsampling of the matched pool.
  - fig5e-next-command, the "about" of the condition left-out statistic says "each session", as its n covers both monkeys.
  - Open, the code line references (the repository at 416187366f84) could not be re-read in this check; the method details cited to the code alone are taken as written.
  - Open, fig4g-majority-predicted and fig5f-condition-specific-next-command read "vast majority" and "majority" as a fraction above 0.5, and fig5d-four-dimensions uses two readings of "more accurately than the rest" made by the reader; the paper gives no rule for either.
  - Open, the units of the single-neuron distances and errors (fig3b, fig4de, Hz) and of the next-command error (fig5f) are not stated in the paper; they rest on the code.
  - Open, most claims need the decoder (Kalman gain, or the PPF parameters for Monkey J); whether the dataset holds it is the author's to find.
EOF
python tools/claims_check.py $f paper/10.1016-j.cub.2023.06.027.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "rather\|—" claims/000404/*.yaml; git status --short
```

```
M claims/000404/10.1016-j.cub.2023.06.027.yaml
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

I checked the claims file for DANDI:000404 against the paper and made ten corrections. Four points stay open, none of which blocks an attempt, so I marked the file ready. Nothing is committed.

**Checker result:** `29 claims, 29 quotes, 57 statistical values, 0 problems`. The count went from 55 to 57 statistical values because I added two to fig6g.

**Changes, by claim**
- **Sources for conditions-per-session, figs1b, fig4c, fig4f, fig4g, figs3, figs5b, figs5f, figs6cd:** each now names its Results paragraph by its opening words. Five of the numbers were off by one (fig4c, fig4f, fig4g, figs5b, figs6cd). Counting paragraphs is also unreliable where equations split them.
- **fig4f:** the statement said the result was "far above" the shuffle, which the paper does not say. It now says "significantly more than shuffle dynamics", as the Figure 4F legend does.
- **figs5b:** I removed the reading that paired by session and task. The paper's own p-values only work as paired t-tests over sessions (8 and 3 degrees of freedom: T = -7.182 gives p = 9.4e-05, T = -5.141 gives p = 0.0143). So the pairs are the 9 and 4 sessions, as the Methods say, and the paper's N of 18 and 8 counts R2 values.
- **fig4c:** leaving out the transitions to and from a left-out command is now cited to the Figure S4A legend, which states it, and not only to the code.
- **figs6cd:** the population distance is divided by the square root of the number of neurons (Methods), not of the null-space dimension. This does not change r or the slope.
- **fig6d:** this is a claim that something is absent. It is now also not reproduced when the Wilcoxon test finds a difference in any session, because the paper's test covers the sessions too.
- **fig6g:**
  - I added the Table S2 statistics for the decoder-null comparison's own No Dynamics model against shuffle (Figure 6H).
  - The criterion now requires that absence and the per-session Mann-Whitney absences.
  - The null now has two readings: the Methods' behavior-preserving shuffle and the code's subsampling.
- **figs1d:** the criterion now says why the Statistics Summary's "behavior-preserving shuffle" is not the test here. That shuffle leaves commands unchanged, so the Methods' subsampling of the matched pool is the test.
- **fig5e:** the "about" field of the condition left-out statistic now says "each session".

**Open**
- I could not re-read the paper's code in this check, so method details cited only to code line numbers are taken as the first reader wrote them.
- fig4g and fig5f read "vast majority" and "majority" as more than half. fig5d uses two readings of "more accurately than the rest" that the first reader chose. The paper gives no rule for any of these.
- The paper gives no unit for the single-neuron distances and errors (fig3b, fig4de) or for the next-command error (fig5f). Hz comes from the code.
- Most claims need the decoder parameters. Whether the dataset holds them is for the author to find.

**Ready:** yes (`ready: true`).

## End of run

23 turns, 3 minutes, result: success.
