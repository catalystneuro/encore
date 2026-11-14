# gao-2018 · claims-check · run 43585538118

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i gao; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80; cat claims/gao-2018.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i gao; awk '/^## Reader/,/^## Author/' docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/gao-2018.yaml"
}
```

```
1	# Claims for Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li (2018), "A
2	# cortico-cerebellar loop for motor planning", Nature 563, 113-116, doi:10.1038/s41586-018-0633-x,
3	# tested on DANDI:000007 and CRCNS:alm-4.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-14,
5	# protocol pilot-15 as stated in docs/protocol.md. It updates the file written 2026-11-10 under
6	# pilot-14 (and checked that day) for DANDI:000007 alone; ids are kept where the finding is the
7	# same, and the changes of that check are carried over.
8	#
9	# Text read: the version of record (PMC6212318, open access), Europe PMC JATS XML flattened, in
10	# paper/10.1038-s41586-018-0633-x.txt: main text, Methods, the legends of Extended Data Figs. 1 to
11	# 10, and the Supplementary Information (41586_2018_633_MOESM1_ESM.pdf, from the publisher; also
12	# paper/...supp1.pdf), whose text is appended: the Extended Data Fig. 10 discussion, the cerebellar
13	# circuitry discussion and Supplemental Table 1 (mice and hemispheres per experiment). supp2.pdf is
14	# the Nature reporting summary. The legends of the main Figs. 1 to 4 are not in the stored text,
15	# and there is no PDF of the main paper; values, significance marks and neuron counts given only in
16	# those legends or inside the figures are not used here (see the report of this run). Sources cite
17	# main-text paragraphs counting the opening summary paragraph as paragraph 1.
18	# Code: the paper links none. Its Code availability says "Software used for data analysis is
19	# available from the corresponding author upon reasonable request"; the reporting summary says
20	# "Custom analysis scripts and data will be deposited on CRCNS.org" and gives no identifier. The
[... 874 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/gao-2018.yaml",
 "offset": 894
}
```

```
894	  depends_on:
895	  - fig4f-fastigial-effect-persists
896	  datasets:
897	  - "000007"
898	  - crcns-alm-4
899	  criterion: As fig4-fastigial-activation-alm-latency and fig4f-fastigial-effect-persists on the
900	    ALM pyramidal neurons of the dentate sessions (3 mice, Supplemental Table 1). Reproduced when
901	    under one reading the latency is within tolerance (and the count, where the dataset holds all
902	    3 mice), and the fraction of significant neurons in bins starting 1 s or more after
903	    photostimulus offset is not above the comparison of fig4f-fastigial-effect-persists (same
904	    test, p >= 0.05) and is lower than the fastigial fraction in the same bins.
905	- id: fig4i-cd-control-separation
906	  statement: In control trials, ALM activity trajectories for "lick left" and "lick right"
907	    diverge along the coding direction during the sample epoch and stay separated through the
908	    delay epoch.
909	  source: Main text, paragraph 17; Figure 4h and 4i
910	  quote: In control trials, activity trajectories from "lick left" and "lick right" trials diverged
911	    from each other along the cd during the sample epoch and remained separated throughout the
912	    delay epoch
913	  datasets:
[... 162 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; python tools/claims_check.py claims/gao-2018.yaml paper/10.1038-s41586-018-0633-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; cat paper/10.1038-s41586-018-0633-x.txt | fold -s -w 200 | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ee9bb57f-80bf-4437-b1f4-bdf9b8bebbdc/tool-results/blng3tdvz.txt"
}
```

```
1	109919 paper/10.1038-s41586-018-0633-x.txt
2	 19435 paper/alm-4.data-description.txt
3	129354 total
4	DOI: 10.1038/s41586-018-0633-x
5	Version: version of record, PMC6212318 (open access)
6	Source: europepmc fullTextXML
7	Stored: 2026-11-06
8	Extracted: JATS XML flattened
9	------------------------------------------------------------------------
10	A cortico-cerebellar loop for motor planning
11	
12	Persistent and ramping neural activity in frontal cortex anticipates specific movements 1 – 6 . Preparatory activity is distributed across multiple brain regions 7 , 8 , but it is unclear which brain 
13	areas are involved and how this activity is mediated by multi-regional interactions. The cerebellum is a brain structure thought to be primarily involved in short timescale control of movement 9 – 12 
14	, but roles in cognitive processes have also been proposed 13 – 16 . In humans, cerebellar damage can cause defects in planning and working memory 13 . We report that persistent representation of 
15	information in frontal cortex during motor planning is dependent on the cerebellum. Mice performed a sensory discrimination task in which they used short-term memory to plan a future directional 
16	movement. A transient perturbation in the medial deep cerebellar nucleus (fastigial nucleus) disrupted correct subsequent responses, without hampering movement execution. Preparatory activity was 
17	observed in both frontal cortex and cerebellar nuclei, seconds before movement onset. Silencing frontal cortex activity abolished preparatory activity in the cerebellar nuclei. Fastigial activity was 
18	necessary for maintaining cortical preparatory activity. Fastigial output selectively targeted the behaviorally relevant part of frontal cortex through the thalamus, closing a cortico-cerebellar 
19	loop. Our results support the view that persistent neural dynamics during motor planning is maintained by multi-regional neural circuits 17 , and that cerebellar computations extend bey
[... 385 more lines not kept]
```

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1038-s41586-018-0633-x.txt | sed -n '400,700p'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ee9bb57f-80bf-4437-b1f4-bdf9b8bebbdc/tool-results/be2jgwsl6.txt",
 "offset": 10
}
```

```
10	a. Coronal sections showing CN lesion sites for all mice. Fastigial lesion, n=4; dentate lesion, n=4.
11	
12	b. Licking movement is not affected by fastigial lesion. Individual licks are shown as dots (blue, lick right; red, lick left). Licks are aligned to the onset of the ‘go’ cue (vertical line).
13	
14	c. Average lick rate within a lick bout and the duration of lick bouts are not affected by fastigial lesion. A lick bout is defined as a sequence of licks with inter-lick-interval less than 500 ms. 
15	Data from the fastigial-lesion mice only (n=4). Data are grouped by licking direction relative to the lesioned hemisphere: contralesional licking (blue) or ipsilesional licking (red).
16	
17	d. Coronal sections showing ChR2-EYFP expression in the fastigial and dentate nucleus. 9 mice were used for various fastigial ChR2 photo-activation experiments, and 10 mice were used for dentate ChR2 
18	photo-activation experiments. In 1 of the fastigial photo-activation mice, the injection of ChR2 virus missed the CN (not shown) and its data were excluded. 2 of the dentate photo-activation mice 
19	were subsequently used for lesion experiments (not shown). See Supplemental Table 1 for the list of mice and manipulated hemispheres in individual experiments.
20	
21	e. CN photo-activation during specific behavioral epochs. Top , experiment timeline. Photostimulation was for the entire task epoch (1.3 s). Bottom , behavioral performance. Left , fastigial 
22	photo-activation (n=6); right , dentate photo-activation (n=8). For fastigial photo-activation, average behavioral performance for control and photo-activation trials (S, sample epoch 
23	photo-activation; D, delay epoch; R, response epoch) is also shown. Gray lines show individual mice. Chance is 50%. For behavioral performance grouped by trial type, “lick left” and “lick right” 
24	trials are grouped by instructed licking direction relative to the manipulated hemisphere. Blue, contralateral; red, ipsilateral. Both hemisphe
[... 278 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ee9bb57f-80bf-4437-b1f4-bdf9b8bebbdc/tool-results/be2jgwsl6.txt",
 "offset": 302
}
```

```
302
```

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1038-s41586-018-0633-x.txt | sed -n '700,900p'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1038-s41586-018-0633-x.txt | sed -n '900,1000p'; ls papers/datasets/ | grep gao; cat papers/datasets/gao-2018.yaml; git log --oneline -5 -- claims/gao-2018.yaml; ls questions | grep gao
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*.yaml | head -3; f=$(grep -l "^checks:" claims/*.yaml | head -1); sed -n '/^checks:/,$p' $f | head -30; cat questions/gao-2018.yaml | head -40
```

```
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
  - fig6-sign-consistency. The tolerance of 0.9 allowed only 9 while the criterion accepted 8 to 10. Set the tolerance to 1 (10% of 9 rounded to a whole combination) and gave the reason.
  - Header O4. The SD of the channel was fixed as the whole recording, called a standard choice; it can change which blocks are dropped, so the readings (whole recording, the day's recording) are now named.
  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANOVA's observations are not given (Methods 2.2); named fold accuracies and participant means as readings. The absence claim is judged on fold accuracies with type II sums of squares, marked as resting on an assumption, with the others as variants. Said that p < 0.001 for a printed 0 is this file's reading.
  - fig5-pre-postcentral. The criterion cited Discussion paragraph 2 for the alpha sign; that paragraph gives theta and gamma only. The alpha sign is cited to Results 3.1 paragraph 6.
  - fig7-exceeds-group. The comparison of Figure 7 with Figure 2
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '40,200p' questions/gao-2018.yaml
```

```
(Bash completed with no output)
```

**Agent**

Checker passes (0 problems). I found a few things I can show are wrong from the paper. Making the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "#  - Mice. 70 in all (Supplemental Table 1). ALM recordings: 1309 single units in 10 mice over 39\n#    sessions during behavior with CN ChR2 photo-activation (Fig. 2, Fig. 4); 1194 putative",
 "new_string": "#  - Mice. 70 in all (Supplemental Table 1). ALM recordings: 1309 single units in 10 mice over 39\n#    sessions during behavior (Fig. 2); 1194 putative"
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "trials, are open; the paper\n#     says the epoch choice gave qualitatively similar results.",
 "new_string": "trials, are open; the paper\n#     says the epoch choice gave \"qualitatively similar preparatory activity\", which says nothing\n#     of the response epoch."
}
```

```
<tool_use_error>String to replace not found in file.
String: trials, are open; the paper
#     says the epoch choice gave qualitatively similar results.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "  statement: After fastigial lesion, the first lick to the contralesional side comes later after\n    the go cue than the first lick to the ipsilesional side, while lick rate within bouts and\n    bout duration are unchanged.",
 "new_string": "  statement: Fastigial lesions slow the initiation of contralesional licking after the go cue,\n    while lick rate within bouts and bout duration are unchanged."
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "  criterion: Time of the first lick after go cue onset (Methods, reaction time), per trial,\n    contralesional against ipsilesional licking, in the fastigial lesion mice after the lesion;\n    one-sided hierarchical bootstrap as in B1 at p < 0.05 (the Fig. 1e legend, not in the text\n    read, would give the paper's test). Reproduced when contralesional first licks are later. For",
 "new_string": "  criterion: Time of the first lick after go cue onset (Methods, reaction time), per trial, in the\n    fastigial lesion mice. What the slowing is relative to is not stated (open; readings (a)\n    contralesional licking after against before the lesion; (b) contralesional against\n    ipsilesional licking after the lesion). One-sided hierarchical bootstrap as in B1 at p < 0.05\n    (the Fig. 1e legend, not in the text read, would give the paper's test). Reproduced when under\n    one reading contralesional first licks are later. For"
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "the paper\n#     says the epoch choice gave qualitatively similar results. For",
 "new_string": "the paper\n#     says the epoch choice gave \"qualitatively similar preparatory activity\", which says nothing\n#     of the response epoch. For"
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "    performance on ipsilateral trials (more contralateral licks) with contralateral performance\n    not lowered. Reproduced when the ipsilateral performance drops with a one-sided bootstrap p <\n    0.05 (B1) and the contralateral drop, if any, is smaller and not significant.",
 "new_string": "    performance on ipsilateral trials (more contralateral licks) than on contralateral trials.\n    Reproduced when the ipsilateral performance drops with a one-sided bootstrap p < 0.05 (B1) and\n    the contralateral drop, if any, is smaller; its significance is reported."
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "    experiment (Supplemental Table 1). An ipsilateral bias is lower performance on contralateral\n    trials with ipsilateral performance not lowered. Reproduced when the contralateral drop has a\n    one-sided bootstrap p < 0.05 (B1) and the ipsilateral drop, if any, is smaller and not\n    significant.",
 "new_string": "    experiment (Supplemental Table 1). An ipsilateral bias is lower performance on contralateral\n    trials than on ipsilateral trials. Reproduced when the contralateral drop has a one-sided\n    bootstrap p < 0.05 (B1) and the ipsilateral drop, if any, is smaller; its significance is\n    reported."
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "    Reproduced when, under cerebellar cortex photostimulation, more than half of the fastigial\n    units decrease significantly and,",
 "new_string": "    Reproduced when, under cerebellar cortex photostimulation, more than half of the fastigial\n    units decrease significantly (the majority rule is this file's choice) and,"
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "  statistics:\n  - test: one-sided bootstrap\n    p: 0.0001\n    n: 15 mice (fastigial)",
 "new_string": "  statistics:\n  - about: the mark on the fastigial late delay proportion (the legend does not name the bar)\n    test: one-sided bootstrap\n    p: 0.0001\n    n: 15 mice (fastigial)"
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "the legend implies; open whether selectivity is from that window or from E2 over epochs, both\n    run). Reproduced when the contra-preferring fraction in the last 500 ms exceeds one half with\n    a one-sided bootstrap over mice (B1 resampling scheme) p < 0.001 and the first 500 ms\n    fraction does not differ from one half at p < 0.05.",
 "new_string": "the legend implies; open whether selectivity is from that window or from E2 over epochs, both\n    run). The legend gives \"***, p=0.0001, one-sided test, bootstrap\" without saying what is\n    compared (open; readings (a) the last 500 ms contra-preferring fraction against one half; (b)\n    the last 500 ms fraction against the first 500 ms fraction). Reproduced when under one reading\n    the last 500 ms contra-preferring fraction is the larger with a one-sided bootstrap over mice\n    (B1 resampling scheme) p < 0.001, the *** threshold of the paper's legends, and the first 500\n    ms fraction does not differ from one half at p < 0.05 (a two-sided bootstrap, this file's\n    choice; the paper reports no test for \"equal numbers\")."
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/gao-2018.yaml",
 "old_string": "    test, p >= 0.05) and is lower than the fastigial fraction in the same bins.",
 "new_string": "    test, p >= 0.05) and is lower than the fastigial fraction in the same bins (one-sided test of\n    two proportions at p < 0.05, this file's choice; the paper gives no test)."
}
```

```
The file claims/gao-2018.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  cat >> claims/gao-2018.yaml <<'EOF'
checks:
- date: 2026-11-14
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1e-fastigial-lesion-slow-initiation. The statement said contralesional first licks come later than ipsilesional ones; the paper says only that lesions "slowed initiation of contralesional licking", without the comparison. Restated as the paper has it, and the criterion now names the readings (after against before the lesion; contra- against ipsilesional after it).
  - fig1h-fastigial-activation-response-contra-bias, fig1k-inhibition-response-ipsi-bias. The criteria required the drop on the other trial type to be not significant, a condition the paper does not state. A bias is now judged as the larger drop on the trial type the paper names, with the significance of the other reported.
  - ed4g-fastigial-contra-late-delay. The Extended Data Fig. 4g legend gives p=0.0001 without saying what is compared; named the readings (against one half, against the first 500 ms) and said that the test of "equal numbers" in the early delay is this file's choice. Added an about to the statistic.
  - Header E3. It said the epoch choice gave "qualitatively similar results"; the Methods say "qualitatively similar preparatory activity". Quoted the Methods (also asked in questions/gao-2018.yaml).
  - Header, data. It said the 1309 ALM units of 10 mice were recorded with CN ChR2 photo-activation; the Methods say 9 of the 10 mice were. Removed the qualifier.
  - fig1j-photoinhibition-silences-fastigial. Said that the majority rule is this file's choice; the paper gives no count.
  - fig4g-dentate-effect-recovers. The comparison with the fastigial fraction had no test; named a one-sided test of two proportions as this file's choice.
  - Open. The legends of main Figs. 1 to 4 are not in the text and there is no PDF of the main paper; the tests and counts behind Fig. 1d, 1e, 1g, 1i, 2c, 3f and 4e to 4i are not known, and the criteria use the bootstrap of B1 or named choices in their place.
  - Open. Which photostimulus Fig. 1g (dentate) and Fig. 1h (delay bias) use, 0.455 s or 1.255 s; the Methods and Supplemental Table 1 disagree, and both readings stay.
  - Open. Whether the bilateral ALM photo-inhibition trials of Extended Data Fig. 10a to 10c come from this paper's recordings or from its refs. 1 and 2 (supplement, "Previously, we found"); ed10c-alm-inhibition-endpoints-predict names this.
  - Open. The header says the changes of the 2026-11-10 check are carried over, but the file held no checks list; that check could not be read here.
  - Open. Not given claims, as minor legend statements; Extended Data Fig. 4d (no correlation between lick modulation and preparatory activity) and Extended Data Fig. 8c (vGlut2 positive fastigial synapses in ALM-projecting thalamus, one case).
EOF
python tools/claims_check.py claims/gao-2018.yaml paper/10.1038-s41586-018-0633-x.txt; grep -n "—\|rather" claims/gao-2018.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The file is fit for an attempt, and the last check now says `ready: true`.

**Checker result:** `claims/gao-2018.yaml: 46 claims, 46 quotes, 17 statistical values, 0 problems`. It gave the same line before and after my edits.

**Changes, by claim** (each is also recorded under `checks`):
- **fig1e-fastigial-lesion-slow-initiation:** the statement said contralesional first licks come later than ipsilesional ones. The paper only says lesions "slowed initiation of contralesional licking" and does not say compared with what. I restated it as the paper has it. The criterion now names two readings: contralesional licking after against before the lesion, and contralesional against ipsilesional licking after the lesion.
- **fig1h-fastigial-activation-response-contra-bias** and **fig1k-inhibition-response-ipsi-bias:** both criteria required the drop on the other trial type to be not significant, which the paper never states. A bias is now judged as the larger, significant drop on the trial type the paper names. The other drop's significance is reported but does not decide the outcome.
- **ed4g-fastigial-contra-late-delay:** the Extended Data Fig. 4g legend gives p=0.0001 without saying what is compared. The criterion now names both readings (the late delay fraction against one half, or against the first 500 ms). It also says the test for "equal numbers" in the early delay is the file's own choice. I added an `about` to the statistic.
- **fig1j-photoinhibition-silences-fastigial:** the criterion now says the majority rule is the file's choice, since the paper gives no count.
- **fig4g-dentate-effect-recovers:** the comparison with the fastigial fraction had no test. I named a one-sided test of two proportions as the file's choice.
- **Header E3:** it paraphrased the Methods as "qualitatively similar results". The Methods say "qualitatively similar preparatory activity", which says nothing about the response epoch. I quoted the Methods. This is the point raised in the unanswered question in `questions/gao-2018.yaml`.
- **Header, data:** it said all 1309 ALM units came from recordings with CN photo-activation. The Methods say only 9 of the 10 mice were. I removed that wording.

**Still open:**
- The legends of main Figs. 1 to 4 are not in the text, and there is no PDF of the main paper. So the paper's tests and counts for Fig. 1d, 1e, 1g, 1i, 2c, 3f and 4e to 4i are unknown, and the criteria use the hierarchical bootstrap or named choices instead.
- The photostimulus behind Fig. 1g (dentate) and Fig. 1h (delay bias) could be 0.455 s or 1.255 s. The Methods and Supplemental Table 1 disagree, so both readings stay.
- The bilateral ALM photo-inhibition trials in Extended Data Fig. 10a to 10c may come from earlier studies the supplement cites, not from this paper's recordings.
- The header says changes from the 2026-11-10 check were carried over, but the file had no `checks` list, so I could not see that check.
- Two minor legend findings have no claim: Extended Data Fig. 4d (lick modulation does not correlate with preparatory activity) and Extended Data Fig. 8c (glutamatergic fastigial synapses in ALM-projecting thalamus, one case).

Every claim comes from this paper. No ids were changed, and nothing was committed.

## End of run

27 turns, 3 minutes, $1.36 at API prices, result: success.
