# wirtshafter-2020 · claims-check · run 42936491710

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i wirts; cat claims/wirtshafter-2020.yaml; grep -n -A40 '"Reader"\|^## Reader\|Reader' docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/wirtshafter-2020.yaml"
}
```

```
1	# Claims for Wirtshafter & Wilson (2020), eLife 9:e55252, "Differences in reward biased spatial
2	# representations in the lateral septum and hippocampus", doi:10.7554/elife.55252, on CRCNS data set
3	# hc-29 (doi:10.6080/K0NG4NV8).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC7274787, open access), as JATS XML flattened to text under
8	# paper/: main text, Materials and methods, the legends of Figures 1 to 7 and of all their figure
9	# supplements (Figure 2 S1, Figure 3 S1 and S2, Figure 5 S1 to S5, Figure 6 S1 and S2, Figure 7 S1
10	# to S3). The paper has no other supplementary file. No PDF was supplied; no claim rests on a
11	# number shown only in a figure. The extraction garbles the bits/spike formula (its letters are
12	# spaced out) and the FRAI formula ("FRAI = F1 F2 / (F1+F2)", the minus sign lost); the code settles
13	# the second. The data set's description (paper/hc-29.data-description.txt) was read only to know
14	# what it holds: sorted spike times of LS and HPC units, one file per region, labelled by session
15	# date, tetrode and cluster, and "time files for all sessions". It does not name position data.
16	#
17	# Code read: https://github.com/elifesciences-publications/data_analysis, commit 5c6320a9
18	# (2020-06-04), the eLife archived copy linked from Data and code availability (MATLAB; the live
19	# repository github.com/hsw28/data_analysis is at d0ea9e54, 2024-02-06, and was not used). In
20	# hannah-in-use/matlab: decode_pos/bitsperspike.m, bitspersec.m and MASSmutualinfo.m (with
[... 969 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -n 'Reader' docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 43,140p docs/protocol.md; python tools/claims_check.py claims/wirtshafter-2020.yaml paper/10.7554-elife.55252.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 140,220p docs/protocol.md; wc -c paper/10.7554-elife.55252.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55252.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55252.txt",
 "offset": 162,
 "limit": 171
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "statistic\|'p'\|\"p\"\|required\|checks" tools/claims_check.py | head -60; ls schemas 2>/dev/null; grep -rl "checks" claims/*.yaml | head -3
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
92:        for s in c.get("statistics", []):
93:            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
101:          f"{values} statistical values, {problems} problems")
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -n -A12 "^checks" claims/alasfour-2024.yaml | head -30
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
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs']['statistic'],indent=1)); print(json.dumps(s['properties'].get('checks'),indent=1)[:1500])"
```

```
{
 "type": "object",
 "additionalProperties": false,
 "anyOf": [
  {
   "required": [
    "p"
   ]
  },
  {
   "required": [
    "ci"
   ]
  }
 ],
 "properties": {
  "about": {
   "description": "What the test compares or the interval bounds, when the claim has more than one, e.g. 'GPi against VLa onset times'.",
   "type": "string"
  },
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/elifesciences-publications/data_analysis dacode 2>&1 | tail -2; cd dacode 2>/dev/null && git log -1 --format='%h %ad' && ls hannah-in-use/matlab | head
```

```
5c6320a Thu Jun 4 16:47:01 2020 +0100
Hcorr.m
LSevents.m
LSlfpcompare.m
LStrigger.m
REMdetect.m
REMdetect2.m
STA.m
STAfake.m
STAshuffledStats.m
abovetheta.m
Shell cwd was reset to
```

**Agent**

I have the paper read and the code cloned. Next I'm spot-checking the code details the criteria cite.

**Agent calls Bash**

```bash
cd $TMPDIR/dacode/hannah-in-use/matlab; grep -n -i "frai\|F1\b\|F2\b" bulk/MASSplacefieldnumDIRECTIONAL.m | head -30; echo ---; grep -n "1950\|0\.5\b\|>= *.5\|< *.5" decode_pos/bitsperspike.m bulk/MASSplacefieldnum.m | head; echo ---; grep -n "15\|20" bulk/MASSplacefieldnumDIRECTIONALtrials.m | head -30
```

```
21:FRAI = [];
418:        F1 = 0;
419:        F2 = 0;
423:          if F1<=(nansum(flattenednewspikegraph)./2) & isnan(flattenednewspikegraph(ts))==0
424:            F1 = F1+flattenednewspikegraph(ts);
426:        elseif F1>=(nansum(flattenednewspikegraph)./2) & isnan(flattenednewspikegraph(ts))==0
427:            F2 = F2+flattenednewspikegraph(ts);
435:        FRAItemp = ((F1/F1t)-(F2/F2t)) ./ ((F1/F1t)+(F2/F2t));
498:        FRAI(end+1) = FRAItemp;
501:        FRAI(end+1) = FRAItemp.*-1;
619:allsizescenters = [alldir; allsizes; allcenterXmax; allcenterYmax; allskew; alldirskew; allavpfrate; allmaxpfrate; posQuadmax'; FRAI]';
---
decode_pos/bitsperspike.m:122:if length(~isnan(chart(:))==1)>=1950
bulk/MASSplacefieldnum.m:281:        if fsize>=15 & max(curr(:))>=chartlinmean+(2*(chartlinstd))
bulk/MASSplacefieldnum.m:425:        if maxrate < .5
bulk/MASSplacefieldnum.m:446:    %maximum firing rate >= .5hz
---
71:      noposdate = strsplit(currentname,'date_'); %splitting at year rat12_2018_08_20_time
73:      noposdate = strsplit(noposdate,'_position'); %rat12_2018_08_20
139:      vel(1,:) = smoothdata(vel(1,:), 'gaussian', 30); %originally had this at 30, trying with 15 now
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dacode/hannah-in-use/matlab; f=$(find . -name CCpairs.m | head -1); echo $f; grep -n -i "crosscorr\|randperm\|mean(\|3\*3.5\|\/3\|third\|20\*3.5\|lead" $f | head -40
```

```
./bulk/CCpairs.m
167:  %maybe put in some criteria for position here??? dont know. not sure we want crosscorr along whole track
168:  %now you have the pair, so have to find crosscorr.
173:  div = floor(length(posTime)./3);
183:%HPCtrain = HPCtrain(randperm(length(HPCtrain)));
184:%    LStrain = LStrain(randperm(length(LStrain)));
187:  [CC,lags,bounds] = crosscorr(HPCtrain, LStrain, 'NumLags', binzzz); %bins are 10ms, so 100ms is 10 on each side
188:  CCshuffled = crosscorr(HPCtrain, LStrain(randperm(length(LStrain))), 'NumLags', binzzz); %bins are 10ms, so 100ms is 10 on each side
190:  allaverage(end+1) = nanmean(CC);
191:  minusaverage(end+1) = nanmean(CC(1:binzzz));
192:  plusaverage(end+1) = nanmean(CC(binzzz:end));
198:  div = floor(length(posTime)./3);
203:  [CC,lags,bounds] = crosscorr(HPCtrain, LStrain, 'NumLags', binzzz); %bins are 10ms, so 100ms is 10 on each side
204:  CCshuffled = crosscorr(HPCtrain, LStrain(randperm(length(LStrain))), 'NumLags', binzzz); %bins are 10ms, so 100ms is 10 on each side
207:  %startallaverage(end+1) = nanmean(CC)-nanmean(CCshuffled);
208:  startallaverage(end+1) = nanmean(CC);
210:  startminusaverage(end+1) = nanmean(CC(1:binzzz));
211:  startplusaverage(end+1) = nanmean(CC(binzzz:end));
219:  [CC,lags,bounds] = crosscorr(HPCtrain, LStrain, 'NumLags', binzzz); %bins are 10ms, so 100ms is 10 on each side
220:  CCshuffled = crosscorr(HPCtrain, LStrain(randperm(length(LStrain))), 'NumLags', binzzz); %bins are 10ms, so 100ms is 10 on each side
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dacode/hannah-in-use/matlab; grep -n "3\.5\|dist" bulk/CCpairs.m | head -20
```

```
130:    dis = pdist([currentxHPC,currentyHPC;currentxLS,currentyLS], 'euclidean'); %distance between centers
131:    if dis <= 3.5*20 %if distance is less than 16cm, save index
135:  %  if dis <= 3.5*20 && dis >= 3.5*3 %if distance is less than 16cm, save index
139:    if dis >= 3.5*100
161:  DISTANCEBETWEEN = pdist([currentxHPC, currentyHPC; currentxLS, currentyLS]); %INDLUDE
404:%output distance from reward, distance from eachother, and cross corr all, +100, and -100, max
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "    the unit's mean rate above 12 cm/s, laid over the fast periods only; for 454 units from 378\n    recorded, units are drawn with replacement in either reading. The t-test's df (818) does not\n    match 454 + 378 - 2 = 830; it is noted, not used.",
 "new_string": "    the unit's mean rate above 12 cm/s, laid over the fast periods only. Which recorded units the\n    454 are built from is also open (454 is near the 452 LS units recorded, not the 378 included);\n    the readings are (i) one artificial unit per recorded LS unit, 452 in all, and (ii) the 378\n    included LS cells, cycled to 454. The t-test's df (818) matches neither 454 + 378 - 2 = 830 nor\n    454 + 452 - 2 = 904; it is noted, not used."
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "    value: 2\n    tolerance: 0\n  criterion: A multiple linear regression, per cell, of the bin firing rates on the bins' mean speed\n    and acceleration (Results). Open, no code found for it. The cells are the LS place cells (the\n    supplement's title says \"LS firing rate\"); the bins are read as the 2 cm place field bins\n    above 12 cm/s, which reading (a) takes from the smoothed map and reading (b) from the unsmoothed\n    map; acceleration is the derivative of the smoothed speed. Reproduced when, under one reading,\n    the median r2 is within 0.054 to 0.066 and at most 3 cells exceed 0.5; partially reproduced\n    when the median r2 is below 0.1 and at most 5 cells exceed 0.5.",
 "new_string": "    value: 2\n    tolerance: 1\n  criterion: A multiple linear regression, per cell, of the bin firing rates on the bins' mean speed\n    and acceleration (Results). Open, no code found for it. The cells are the LS place cells (the\n    supplement's title says \"LS firing rate\"); the bins are read as all bins of the 2 cm rate map\n    of the place field analysis, above 12 cm/s, which reading (a) takes from the smoothed map and\n    reading (b) from the unsmoothed map; acceleration as the derivative of the smoothed speed is a\n    standard choice, the paper not defining it. The count's tolerance is one cell, since 10% of 2\n    is below the smallest step. Reproduced when, under one reading, the median r2 is within 0.054\n    to 0.066 and at most 3 cells exceed 0.5 (fewer than 2 also supports the claim)."
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "    experience on the track ( Figure 4G–H )\n  statistics:\n  - about: first five against last five runs, per cm from centre\n    test: two-tailed two sample t-test\n    p: 0.05\n    p_relation: <\n  depends_on:",
 "new_string": "    experience on the track ( Figure 4G–H )\n  depends_on:"
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "    offsets but +18 and +20 cm in CA1 and -18 cm in LS (two-tailed two sample t-tests, read at\n    p < 0.05 uncorrected, as the legend gives no correction).",
 "new_string": "    offsets but +18 and +20 cm in CA1 and -18 cm in LS (two-tailed two sample t-tests; the legend\n    gives neither a threshold nor a correction, so p < 0.05 uncorrected, the level the paper uses\n    elsewhere, is the reading)."
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "  source: Results, CA1 and LS place fields have different skew, paragraph 2; Figure 5E\n  quote: skew values",
 "new_string": "  source: Results, CA1 and LS place fields have different skew, paragraph 2; Figure 5E; the ramp\n    from Discussion, paragraph 8\n  quote: skew values"
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "    Reproduced when, under one reading, the CA1 away regression gives p < 0.01 and both LS\n    regressions p > 0.05; the r2 is reported against 0.07.",
 "new_string": "    Reproduced when, under one reading, the CA1 away regression gives p < 0.01 with r2 within\n    tolerance and both LS regressions p > 0.05."
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "choice-side indicator per field (df 320). The arm tests have df 364 and 334, near twice the\n    field totals; they are read",
 "new_string": "choice-side indicator per field (df 320). The arm tests have df 364 and 334; 334 is\n    2 x 168 - 2, while 364 matches no CA1 count in the paper (2 x 154 - 2 = 306); they are read"
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "    fig6de-choice-side-bias, per direction (df 218 and 254 are near twice the 110 away and 138\n    toward LS fields).",
 "new_string": "    fig6de-choice-side-bias, per direction (df 218 is 2 x 110 - 2 for the away LS fields; df 254\n    does not match the 138 toward fields, 2 x 138 - 2 = 274)."
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "  criterion: A claim of absence, judged on the paper's one way ANOVAs over the three locations. The\n    df (115 fields) is fewer than all located LS fields (146); readings are (a) the LS fields of\n    matched HPC-LS pairs, (b) all located LS fields. Reproduced when both ANOVAs give p > 0.05\n    under reading (a), the paper's sample as its df suggests; not reproduced when either gives\n    p < 0.05; reading (b) is shown as a variant.",
 "new_string": "  criterion: A claim of absence, judged on the paper's one way ANOVAs over the three locations. The\n    df gives 115 fields, which matches neither all located LS fields (146) nor the matched pairs\n    (about 92, from 36 forced-arm pairs and df 67 and 54 in fig7a-crosscorr-choice), so the sample\n    is open; readings are (a) the LS fields of matched HPC-LS pairs, (b) all located LS fields.\n    Reproduced when both ANOVAs give p > 0.05; not reproduced when either gives p < 0.05. The\n    outcome is the one both readings give; if they differ, the author adopts the one the paper\n    best supports, as an assumption, and shows the other."
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "    choice-side cross-correlation is not due to closer field centres; forced and\n    choice pairs do not differ in centre distance, and after",
 "new_string": "    choice-side cross-correlation is not due to closer field centres; forced and\n    choice pairs do not differ in centre distance (choice and middle pairs differ by a small 3 cm),\n    and after"
}
```

```
<tool_use_error>String to replace not found in file.
String:     choice-side cross-correlation is not due to closer field centres; forced and
    choice pairs do not differ in centre distance, and after</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "  criterion: The session split into three equal parts of its position time base (CCpairs.m), the\n    pair measure computed in each.",
 "new_string": "  criterion: The session split into three equal parts of its position time base (CCpairs.m), the\n    pair measure computed in each. CCpairs.m stores the raw mean for the first third and the\n    shuffle-subtracted mean for the middle and last thirds; the Methods' shuffle-subtracted\n    measure in all three is the main reading, the code's mix a variant."
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirtshafter-2020.yaml",
 "old_string": "forced and\n    choice pairs do not differ in centre distance, and after removing",
 "new_string": "forced and\n    choice pairs do not differ in centre distance (choice and middle pairs differ by a small 3 cm),\n    and after removing"
}
```

```
The file claims/wirtshafter-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> claims/wirtshafter-2020.yaml <<'EOF'
checks:
- date: 2026-11-11
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2b-poisson-control. The criterion drew the 454 artificial units with replacement from the 378 included LS cells, a step the paper does not give. 454 is near the 452 LS units recorded, so the source set is now named open, with readings (i) one per recorded LS unit and (ii) the 378 cells cycled to 454; the df note now says 818 fits neither.
  - fig3s1-speed-acceleration. The expected count had tolerance 0 while the criterion accepted up to 3 cells. Set the tolerance to 1 with its reason (10% of 2 is below one cell). Removed the partial rule (median below 0.1, at most 5 cells), thresholds the paper does not give. Said the bins are all bins of the 2 cm map and that the acceleration definition is a standard choice.
  - fig4gh-firing-increases. Removed the statistics entry with p < 0.05; the Figure 4G-H legend prints no p-value or threshold. The criterion keeps p < 0.05 and now says it is a reading.
  - fig5e-reward-proximate-skew. The statement's ramp on reward approach comes from Discussion paragraph 8, not from the quoted sentence; added it to the source.
  - fig5s2-skew-distance. The criterion called the r2 reported only, while it is an expected value with a tolerance; the criterion now requires it within tolerance.
  - fig6de-choice-side-bias. The criterion said df 364 and 334 are near twice the field totals; 334 is 2 x 168 - 2, but 364 fits no CA1 count (2 x 154 - 2 = 306). Corrected the note.
  - fig6g-ls-choice-by-direction. The criterion said df 254 is near twice the 138 toward LS fields; it is not (274). Corrected the note.
  - fig7s2-ls-rates-by-location. The criterion judged on matched-pair LS fields as the sample the df suggests; df 112 (115 fields) fits neither the 146 located LS fields nor the about 92 matched pairs. The sample is now named open, both readings run, outcome per the protocol's rule for readings that differ.
  - fig7s3-pair-distance-control. The statement left out the small (3 cm) significant choice against middle centre distance difference that its statistics record; added.
  - fig7c-thirds. CCpairs.m (commit 5c6320a9, checked) stores the raw mean for the first third and the shuffle-subtracted mean for the other two; named the Methods' subtracted measure as the main reading and the code's mix as a variant.
  - Checker. The two VALUE NOT FOUND flags (fig5s5-skew-frai, 9e-13 and 9e-10) come from the garbled "p<9 -13" and "p<9 -10" in the text; the readings 9e-13 and 9e-10 are kept, as the criterion says.
  - Open, not settled from the paper. The Methods' "equal to or less than" for the field boundary, the 0.05 Hz against 0.5 Hz rate rules, the coverage rule, the X2 6.03 against 12.7, the CA1 arm test printed as t(364)=2.34 with p > 0.05, and the forced against choice arm for the 20 ms lag stay as the readings the file names.
EOF
python tools/claims_check.py claims/wirtshafter-2020.yaml paper/10.7554-elife.55252.txt; grep -n ': .*: ' claims/wirtshafter-2020.yaml | grep -v '^\s*#' | grep -v "quote:\|statistic:" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short
```

```
M claims/wirtshafter-2020.yaml
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

The claims file is ready for an attempt. I made 10 corrections to individual claims and added the check entry under `checks`.

**Checker result:** `claims/wirtshafter-2020.yaml: 31 claims, 31 quotes, 44 statistical values, 2 problems`. Both problems are in `fig5s5-skew-frai`. The text extraction garbles two p-value bounds ("p<9 -13" and "p<9 -10"), so the checker can't find them. Reading them as 9e-13 and 9e-10 is correct, and I kept them. The count of statistical values dropped from 45 to 44 because I removed one entry (`fig4gh-firing-increases`, below).

**Changes, by claim:**
- **fig2b-poisson-control:** The criterion drew the 454 artificial units with replacement from the 378 included LS cells, a step the paper doesn't give. 454 is close to the 452 LS units recorded, so which units they come from is now named as open, with two readings. The note now says the t-test's df of 818 fits neither count.
- **fig3s1-speed-acceleration:** The expected count of 2 cells had tolerance 0, but the criterion accepted up to 3. I set the tolerance to 1 and gave the reason (10% of 2 is less than one cell). I removed a "partially reproduced" rule whose thresholds (median below 0.1, at most 5 cells) the paper doesn't give. I also clarified which bins are used and said the acceleration definition is a standard choice.
- **fig4gh-firing-increases:** Removed the statistics entry with p < 0.05. The legend prints no p-value or threshold, so the criterion now names p < 0.05 as a reading.
- **fig5e-reward-proximate-skew:** The statement's "LS fields ramp up firing on reward approach" comes from Discussion paragraph 8, not from the quoted sentence. I added that paragraph to the source.
- **fig5s2-skew-distance:** The r2 of 0.07 is an expected value with a tolerance, but the criterion said it was only reported. The criterion now requires it to be within tolerance.
- **fig6de-choice-side-bias:** The note said both arm-test dfs are close to twice the field totals. That holds for LS (334 = 2 × 168 − 2) but not for CA1: 364 matches no CA1 count (2 × 154 − 2 = 306). Corrected the note.
- **fig6g-ls-choice-by-direction:** The df of 254 doesn't match the 138 toward-reward LS fields (that would be 274). Corrected the note.
- **fig7s2-ls-rates-by-location:** The criterion judged on the LS fields of matched pairs, as "the sample the df suggests". The df implies 115 fields, which matches neither the 146 located LS fields nor the roughly 92 matched pairs. The sample is now named as open, both readings are run, and the protocol's rule applies when they disagree.
- **fig7s3-pair-distance-control:** Its statistics record a small but significant 3 cm difference in centre distance between choice and middle pairs, which the statement left out. Added it.
- **fig7c-thirds:** The analysis code (`CCpairs.m`, commit 5c6320a9, which I cloned and checked) uses the raw cross-correlation mean for the first third but subtracts the shuffle for the middle and last thirds. The Methods subtract the shuffle throughout; that is now the main reading, with the code's mix as a variant.

**Checked and left unchanged:** every count, percentage, df and field total I could recompute agrees with the paper. All the paper's main findings have a claim, and none comes from outside the paper. The code details I spot-checked also match: the FRAI formula, the 0.5 Hz rule, the 1950-bin coverage rule, the 15 and 20 cm lap windows and the 3 cm line that is commented out.

**Still open** (each is named as a reading in the file, not settled):
- The Methods say the field boundary is where firing is "equal to or less than" 1 SD above the mean; the Results and the code say at or above.
- Rate cut-off: 0.05 Hz in the Methods against 0.5 Hz in the code.
- What counts as full track coverage.
- The location chi-squared value: 6.03 in the Results against 12.7 in the legend.
- The CA1 arm test, printed as t(364) = 2.34 with p > 0.05, which that df doesn't allow.
- The 20 ms lag: the Results put it on the choice arm, the legend on the forced arm.

**Ready:** yes. Nothing was committed or pushed.

## End of run

29 turns, 3 minutes, $1.33 at API prices, result: success.
