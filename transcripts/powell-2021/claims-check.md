# powell-2021 · claims-check · run 45639052647

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80; cat claims/powell-2021.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## [A-QS-Z]/' docs/protocol.md; python tools/claims_check.py claims/powell-2021.yaml paper/10.7554-elife.60454.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/powell-2021.yaml"
}
```

```
1	# Claims for Powell, Haddad, Gorur-Shandilya & Marder (2021), eLife 10, e60454,
2	# doi:10.7554/elife.60454, tested on ZENODO:3924718.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-25, following docs/protocol.md (Reader, protocol version pilot-18). No data of the
6	# dataset were seen; only its title and description on the archive (the paper's title and
7	# abstract: evoked gastric mill and pyloric rhythms of Cancer borealis recorded from 7 to 23 C).
8	#
9	# Text read: the version of record as served by Europe PMC (PMC7889077, open access JATS,
10	# flattened to paper/10.7554-elife.60454.txt), with Results, Discussion, Materials and methods,
11	# the figure legends of Figures 1 to 6 and the legends of the four figure supplements (Figure 2,
12	# figure supplement 1; Figure 3, figure supplement 1; Figure 4, figure supplements 1 and 2).
13	# The paper has no other supplementary text. The legend of Figure 5f is garbled in the text
14	# ("Ratios of LG to PD cycle period were n across temperature"); the Results sentence that
15	# reports the same test is quoted instead.
16	#
17	# Code read: https://github.com/marderlab/gastric at commit
18	# fa07d36a7e57fc7787a9a8e2fed72300b1a8e6e2 (2020-11-17), the commit the paper cites as archived
19	# at Software Heritage, and the later head 7a82b1f9a2239f46d73ae86d2cc70de8226d89be
20	# (2021-09-09), which differs in fig_phase_relationships.m (a prep-by-prep Rayleigh test on the
[... 484 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; cat paper/10.7554-elife.60454.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/838442a2-82a8-407d-9234-d34081ddd9a4/tool-results/bsztcik3y.txt",
 "offset": 14
}
```

```
File content (27124 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
cd  grep -n '^## ' paper/*.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (22 claims, 0 problems). Now reading the Results and Methods against the claims.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.60454.txt",
 "offset": 25,
 "limit": 124
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.60454.txt",
 "offset": 149,
 "limit": 128
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes. Reading the paper, I found off-by-one paragraph sources and a fig6e criterion that the paper's own numbers would fail. Next I'll try to check the cited code.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/marderlab/gastric.git && cd gastric && git log --oneline | head -3 && git cat-file -t fa07d36a7e57fc7787a9a8e2fed72300b1a8e6e2; ls; ls paper-figures +gastric 2>/dev/null | head -60
```

```
7a82b1f minor fixes
fa07d36 fixed a bug where an unpaired t-test was used
e83cf9e cleaned up PD_hyp a bit
commit
+PDhyp
+gastric
README.md
dan_data_analysis.m
gastric.sublime-project
integer_coupling_spont.m
mara_data_analysis.m
paper-figures
sara_data_analysis.m
spont_vs_evoked.m
stylesheet.xsl
test.m
+gastric:
+model
BurstPeriodsVsTime.m
PlotISITriggeredBy.m
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && git checkout -q fa07d36 && cat paper-figures/fig_phase_relationships.m +gastric/measurePhase.m && echo ===== && cat +gastric/plotIntegerCoupling.m && echo ==== && cat +gastric/integerCoupling.m && echo ==== && git diff fa07d36 7a82b1f --stat
```

```
clearvars
close all
addpath('../')

colors = gastric.colors;

data = gastric.getEvokedData();

min_temp = 5;
max_temp = 25;


% make sure spiketimes are sorted
for i = 1:length(data)
	data(i).PD = sort(data(i).PD);
	data(i).LG = sort(data(i).LG);
end


% compute burst metrics of all LG neurons
[... 796 more lines not kept]
```

**Agent**

The archived code confirms readings for Figures 5 and 6 (pooled Rayleigh test with at least 100 starts; KS shuffle of 100 draws each). Checking the remaining code citations.

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && git diff fa07d36 7a82b1f -- paper-figures/fig_phase_relationships.m +gastric/plotIntegerCoupling.m paper-figures/PD_hyp.m | head -150; echo =====; cat paper-figures/fig_burst_period.m; echo ====; cat +gastric/q10.m
```

```
diff --git a/+gastric/plotIntegerCoupling.m b/+gastric/plotIntegerCoupling.m
index 3105a63..fcffcc6 100644
--- a/+gastric/plotIntegerCoupling.m
+++ b/+gastric/plotIntegerCoupling.m
@@ -259,10 +259,10 @@ ph.edge(1).Color = base_color;
 ph.edge(2).Color = base_color;
 
 % now plot the null distribution which we obtain by randomizing numerators and denominators
-rand_rem = rem(datasample(all_y,1e4)./datasample(all_x,1e4),1);
-rand_rem(isnan(rand_rem)) = [];
-null_y = histcounts(rand_rem,linspace(0,1,nbins+1),'Normalization','cdf');
-plot(ax.remainders,x,null_y,'k')
+% rand_rem = rem(datasample(all_y,1e4)./datasample(all_x,1e4),1);
+% rand_rem(isnan(rand_rem)) = [];
+% null_y = histcounts(rand_rem,linspace(0,1,nbins+1),'Normalization','cdf');
+% plot(ax.remainders,x,null_y,'k')
 
 
 
diff --git a/paper-figures/PD_hyp.m b/paper-figures/PD_hyp.m
[... 465 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && grep -n -i "10.06\|10.98\|9.17\|0.911\|3.44\|0.313\|901_046\|0006\|0079" paper-figures/fig_integer_coupling.m | head; echo ===; grep -n "ibis\|min_spikes\|999_017\|100\b\|< *100\|>= *100" paper-figures/PD_hyp.m | head -20; echo ===; grep -n "ibis\|min_spikes\|30\|600\|120\|polyfit\|fit" paper-figures/fig_evoked_slowdown.m +gastric/BurstPeriodsVsTime.m | head -30; echo ===; grep -n "830\|ibis\|min_spikes" paper-figures/fig_spont_rhythms.m | head; echo ===; head -60 paper-figures/fig_within_prep_spont_evoked_comparison.m
```

```
47:example_data = '901_046';
53:show_these = {'0006','0079'};
54:show_these_rasters = {'0006', '0015','0026','0041','0053','0062','0084','0072','0079'};
138:text(24,2.53,'T_{LG} = 9.17s','FontSize',14,'Parent',ax.raw_data(1));
142:th = text(39,1.5,'T_{LG}/T_{PD}=10.06','FontSize',14,'Parent',ax.raw_data(1));
148:text(2,2.53,'T_{LG} = 3.44s','FontSize',14,'Parent',ax.raw_data(2));
152:th = text(10.4,1.5,'T_{LG}/T_{PD}=10.98','FontSize',14,'Parent',ax.raw_data(2));
===
16:	data{i} = crabsort.computePeriods(data{i},'neurons',{'LG'},'ibis',1,'min_spikes_per_burst',5);
17:	data{i} = crabsort.computePeriods(data{i},'neurons',{'PD'},'ibis',.25,'min_spikes_per_burst',2);
67:C.path_name = fullfile(fileparts(data_root),'999_017' );
74:colors = colormaps.redula(100);
80:	C.file_name = ['999_017_' file_names{i} '.mat'];
118:	lgn = (veclib.interleave(veclib.subSample(lgn,100,@min),veclib.subSample(lgn,100,@max)));
119:	pdn = (veclib.interleave(veclib.subSample(pdn,100,@min),veclib.subSample(pdn,100,@max)));
121:	time = (1:length(lgn))*C.dt*100;
124:	temp = round(interp1(linspace(min_temp,max_temp,100),1:100,temp));
169:		if length(this_data(j).PD) < 100
188:		if length(this_data(j).LG) < 100
208:		if length(this_data(j).LG) < 100
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import math
for n,z in [(40,7.5),(50,7.5),(100,7.5),(40,13),(40,0.15)]:
  Rn=math.sqrt(z*n); print(n,z,math.exp(math.sqrt(1+4*n+4*(n*n-Rn*Rn))-(1+2*n)))
"
```

```
40 7.5 0.0004175317502515961
50 7.5 0.000443483899355911
100 7.5 0.0004971501222209677
40 13 7.833171993352261e-07
40 0.15 0.8621863251489033
```

**Agent**

The code matches most of what the file cites. Applying the corrections now.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='claims/powell-2021.yaml'
s=open(p).read()
reps=[
("""temperature-sensitive,
    paragraphs 2 and 3; Figure 4a and 4b""","""temperature-sensitive,
    paragraphs 1 and 2; Figure 4a and 4b"""),
("""  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,
    paragraph 3; Figure 4c
""","""  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,
    paragraph 2; Figure 4c
"""),
("""  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,
    paragraph 3; Figure 4c legend""","""  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,
    paragraph 2; Figure 4c legend"""),
("""  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,
    paragraph 2; Figure 4, figure supplement 1""","""  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,
    paragraph 1; Figure 4, figure supplement 1"""),
("""temperature range,
    paragraphs 4 and 5; Figure 5b, 5d and 5e""","""temperature range,
    paragraph 4; Figure 5b, 5d and 5e"""),
("""temperature range,
    paragraphs 4 and 5; Figure 5c, 5d and 5e""","""temperature range,
    paragraph 4; Figure 5c, 5d and 5e"""),
("""temperature range,
    paragraph 5; Figure 5e""","""temperature range,
    paragraph 4; Figure 5e"""),
]
for a,b in reps:
    assert s.count(a)==1,a; s=s.replace(a,b)
a="""temperature range,
    paragraph 5; Figure 5f"""
assert s.count(a)==2; s=s.replace(a,"""temperature range,
    paragraph 4; Figure 5f""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now the content edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/powell-2021.yaml",
 "old_string": "    10 preparations, and the evoked rhythms remained regular at high temperature.",
 "new_string": "    10 preparations."
}
```

```
The file claims/powell-2021.yaml has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/powell-2021.yaml",
 "old_string": "    variation of LG burst periods (bursts as in the Methods) at each temperature step with at\n    least three periods. Reproduced",
 "new_string": "    variation of LG burst periods (bursts as in the Methods) at each temperature step with at\n    least three periods (the minimum is a choice made here). Reproduced"
}
```

```
The file claims/powell-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/powell-2021.yaml",
 "old_string": "    intervals overlap. Reproduced when, under one reading, three of the four preparations are\n    similar and one is not.",
 "new_string": "    intervals overlap. Reproduced when, under one reading, three of the four preparations are\n    similar and one is not. The paper gives no measure for the similarity of LG spike and burst\n    timing (the ISIs of Figure 3, figure supplement 1b); the ISIs of each stretch are shown and\n    this part is not judged. Of the four spontaneous files the script lists (941_006, 901_086,\n    901_080, 901_062), 941_006 is not among the ten evoked preparations of getEvokedData.m; the\n    author reports which preparations the four are."
}
```

```
The file claims/powell-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/powell-2021.yaml",
 "old_string": "    file. Reproduced when, under one reading, both ratios are within 10% of the labels and\n    within 0.2 of an integer.",
 "new_string": "    file. Reproduced when, under one reading, both ratios are within 10% of the labels and\n    within 0.2 of an integer (the 0.2 is a choice made here; the paper says only \"close to an\n    integer\"). The paper gives no measure of PD bursts ending \"shortly before\" LG burst starts;\n    for each file the time from the end of the last PD burst to each LG burst start is shown,\n    and this part is not judged."
}
```

```
The file claims/powell-2021.yaml has been updated successfully.
```

**Agent**

Now the Rayleigh test criteria for Figure 6b and 6e.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/powell-2021.yaml",
 "old_string": "    is open, as the Methods, the archived code and the later code differ. Readings (a) Methods,\n    the first 40 LG burst starts of each preparation and temperature, combinations with fewer\n    than 40 excluded; (b) the later code (commit 7a82b1f), the first 50, combinations with\n    fewer than 50 excluded; (c) the archived code, all burst starts of a temperature pooled over\n    preparations, temperatures with fewer than 100 excluded. Under (a) z cannot exceed 40, so\n    the reported z of 45 fits (b) or (c) better. Reproduced when, under one reading, every\n    tested combination has p < 0.05 and the largest p and the range of z agree with p < 4e-4\n    and 7.5 to 45 (widened by 10%, 6.75 to 49.5); partially reproduced when every combination\n    is significant but the p or z bounds are not met.",
 "new_string": "    differs between the Methods, the archived code and the later code. The Methods are followed\n    for the main result: (a) the first 40 LG burst starts of each preparation and temperature,\n    combinations with fewer than 40 excluded, each tested individually. The code's choices are\n    variants: (b) the later code (commit 7a82b1f), the first 50, combinations with fewer than\n    50 excluded; (c) the archived code, all burst starts of a temperature pooled over\n    preparations, temperatures with fewer than 100 excluded. Under (a) z cannot exceed 40, so\n    the reported upper z of 45 cannot be met under the Methods. Reproduced when, under (a),\n    every tested combination has p < 4e-4 (widened by 10%, p < 4.4e-4) and every z lies within\n    7.5 to 45 widened by 10% (6.75 to 49.5); partially reproduced when every combination has\n    p < 0.05 but these bounds are not met. The variants are reported against the same bounds."
}
```

```
The file claims/powell-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/powell-2021.yaml",
 "old_string": "  criterion: The same test and sample readings as fig6b-lg-phase-locked, with DG burst starts.\n    Reproduced when, under the reading that reproduced the LG claim (or any reading if none\n    did), at least one combination has p >= 0.05 and the largest DG z is below the smallest LG\n    z of fig6b-lg-phase-locked. The p and z ranges are reported against 0.001 to 0.85 and 0.15\n    to 13.",
 "new_string": "  criterion: The same test as fig6b-lg-phase-locked, with DG burst starts, the Methods sample\n    (a) for the main result and the code's samples (b) and (c) as variants. The paper gives no\n    measure of \"much smaller\"; the paper's own ranges overlap (DG z up to 13, LG z from 7.5), so\n    it is read here as the median DG z over the tested combinations being below the median LG\n    z of fig6b-lg-phase-locked under the same sample (a choice made here). Reproduced when at\n    least one combination has p >= 0.05 and the median DG z is below the median LG z. The p and\n    z ranges are reported against 0.001 to 0.85 and 0.15 to 13."
}
```

```
The file claims/powell-2021.yaml has been updated successfully.
```

**Agent**

Adding the `checks` entry and re-running the checker.

**Agent calls Bash**

```bash
cd  cat >> claims/powell-2021.yaml <<'EOF'
checks:
- date: 2026-11-25
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4b-periods-decrease-all-preps, fig4c-q10-about-2, fig4c-q10-pd-lg-not-different and fig4s1-slowdown-after-stimulation, source paragraphs corrected (the section has two paragraphs in the text; the quoted sentences are in paragraphs 1 and 2).
  - fig5d-lg-pd-integer-coupled, fig5d-dg-pd-not-coupled, fig5e-lg-area-exceeds-dg, fig5f-ratio-independent-of-temperature and fig5f-ratio-range, source corrected to paragraph 4 (the integer coupling section has four paragraphs; the quoted sentences are all in the fourth).
  - fig3-evoked-7-to-21-in-9-of-10, dropped "the evoked rhythms remained regular at high temperature" from the statement; the paper says it of the example preparation at 23 C, outside the quoted finding, and the criterion did not test it.
  - fig2a-less-regular-at-high-temperature, named the minimum of three periods per step as a choice made here.
  - fig3s1-spontaneous-and-evoked-similar, the statement includes similar LG spike and burst timing, for which the paper gives no measure; named as shown and not judged. Noted that 941_006, one of the four spontaneous files in fig_within_prep_spont_evoked_comparison.m, is not in the ten preparations of getEvokedData.m.
  - fig5a-example-ratios, named the 0.2 distance to an integer as a choice made here, and the PD end before LG start part of the statement as shown and not judged, since the paper gives no measure.
  - fig6b-lg-phase-locked, the three samples were equal readings; per protocol the Methods sample (first 40 starts per preparation and temperature) is now the main result and the code samples (later code first 50, archived code pooled with at least 100) are variants. The p bound is now judged with its 10% tolerance.
  - fig6e-dg-not-phase-locked, the criterion required the largest DG z to be below the smallest LG z, which the paper's own ranges (DG z up to 13, LG z from 7.5) fail; replaced with a comparison of median z, named as a choice, with the same sample rule as fig6b-lg-phase-locked.
  - Open, fig6b-lg-phase-locked, the reported LG z of up to 45 cannot occur with the Methods sample of 40 starts (z = nR^2 is at most n), so the paper's numbers likely come from a pooled sample as in the archived code.
  - Open, fig6e-dg-not-phase-locked, the reported DG ranges are not consistent with each other; a Rayleigh z of 13 gives p near 1e-6 for any sample size, below the reported smallest p of 0.001.
  - Open, fig5a-example-ratios, the expected ratios 10.06 and 10.98 are the labels drawn in Figure 5a (fig_integer_coupling.m); the text gives only ~10 and ~11.
  - Checked the code citations against https://github.com/marderlab/gastric at fa07d36 and 7a82b1f (burst thresholds, Q10 per burst, KS shuffle of 100 draws each, area computation, Rayleigh pooling at 100 starts, Spearman on 7 to 21 C, PD_hyp.m thresholds, slowdown script); they match the file.
EOF
python tools/claims_check.py claims/powell-2021.yaml paper/10.7554-elife.60454.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/    for the main result: (a) the first 40/    for the main result, (a) the first 40/' claims/powell-2021.yaml; grep -n ': ' claims/powell-2021.yaml | grep -v '^[0-9]*: *-\? *[a-z_]*: ' | head; python tools/claims_check.py claims/powell-2021.yaml paper/10.7554-elife.60454.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/^    variants: (b) the later code/    variants, (b) the later code/' claims/powell-2021.yaml; grep -nE '^ {4,}[^#]*[^ ]: ' claims/powell-2021.yaml; python tools/claims_check.py claims/powell-2021.yaml paper/10.7554-elife.60454.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nE '—|rather' claims/powell-2021.yaml; python -c "import yaml;d=yaml.safe_load(open('claims/powell-2021.yaml'));print(d['checks'][-1]['ready'],len(d['checks'][-1]['changes']))"; rm -rf $TMPDIR/gastric
```

```
121:    similarities in LG spike and burst timing ( Figure 3—figure supplement 1b ) and rhythm cycle
122:    period (mean ± SD; Figure 3—figure supplement 1c )
203:    4—figure supplement 1 ) of the gastric mill rhythm with time since stimulation
219:  quote: Figure 4—figure supplement 2c shows that the gastric mill rhythm cycle period steadily
231:  quote: Figure 4—figure supplement 2d shows that in all nine preparations, the gastric mill
True 12
```

**Agent**

I've checked and corrected `claims/powell-2021.yaml`, and I think it is ready for an attempt. Nothing was committed or pushed.

**Checker result** (after my edits): `claims/powell-2021.yaml: 22 claims, 22 quotes, 7 statistical values, 0 problems`

I also compared the file's code citations with https://github.com/marderlab/gastric at commits fa07d36 and 7a82b1f. They match: burst thresholds, the per-burst Q10, the significance test's shuffle (100 draws of each period), the area measure, the pooled phase test, the 7 to 21 C Spearman test, and the `PD_hyp.m` and slowdown script settings.

**Changes, by claim**
- **Wrong paragraph in `source`**, corrected against the paper text:
  - `fig4b-periods-decrease-all-preps`, `fig4c-q10-about-2`, `fig4c-q10-pd-lg-not-different` and `fig4s1-slowdown-after-stimulation`: that section has only two paragraphs.
  - `fig5d-lg-pd-integer-coupled`, `fig5d-dg-pd-not-coupled`, `fig5e-lg-area-exceeds-dg` and both `fig5f` claims: the quoted sentences are all in paragraph 4.
- **`fig3-evoked-7-to-21-in-9-of-10`**: removed "the evoked rhythms remained regular at high temperature" from the statement. The paper says it only of the example preparation at 23 C, and the criterion never tested it.
- **`fig2a-less-regular-at-high-temperature`**: the minimum of three periods per step is now marked as a choice made here.
- **`fig3s1-spontaneous-and-evoked-similar`**:
  - The paper gives no measure for similar spike and burst timing, so that part is now shown but not judged.
  - Added a note that `941_006`, one of the script's four spontaneous files, is not among the ten evoked preparations.
- **`fig5a-example-ratios`**:
  - "Within 0.2 of an integer" is now marked as a choice made here.
  - "PD bursts end shortly before LG bursts start" has no measure in the paper, so it is now shown but not judged.
- **`fig6b-lg-phase-locked`**: the protocol says to follow the Methods and treat the code's choices as variants, but the file treated three samples as equal readings.
  - The main result now uses the Methods sample: the first 40 burst starts per preparation and temperature.
  - The two code samples are variants: the first 50 per preparation (later code) and all starts pooled across preparations with at least 100 (archived code).
  - The p bound is now judged with its 10% tolerance.
- **`fig6e-dg-not-phase-locked`**: the criterion required every DG z to be below every LG z. The paper's own ranges would fail that (DG z goes up to 13, LG z starts at 7.5). I replaced it with a comparison of median z, marked as a choice made here, using the same samples as the LG claim.

**Still open** (recorded under `checks`)
- **LG upper z**: the reported LG z of 45 cannot occur with the Methods sample, because z is at most n = 40. The paper's number probably comes from the pooled sample in the archived code.
- **DG ranges**: the reported DG numbers contradict each other. A z of 13 gives p near 1e-6, below the reported smallest p of 0.001.
- **`fig5a` expected values**: 10.06 and 10.98 are the labels drawn in Figure 5a (from `fig_integer_coupling.m`). The text says only "~10" and "~11".

**Ready**: yes. The last `checks` entry has `ready: true`.

## End of run

25 turns, 3 minutes, $1.41 at API prices, result: success.
