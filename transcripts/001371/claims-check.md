# 001371 · claims-check · run 39667823642

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001371/ paper/; grep -n -A40 -i "reader" docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 115,152p docs/protocol.md; python tools/claims_check.py claims/001371/10.1038-s41467-025-60122-8.yaml paper/10.1038-s41467-025-60122-8.txt; cat claims/001371/10.1038-s41467-025-60122-8.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001371/10.1038-s41467-025-60122-8.yaml paper/10.1038-s41467-025-60122-8.txt 2>&1 | tail -40; wc -l claims/001371/*.yaml paper/10.1038-s41467-025-60122-8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "limit": 450
}
```

```
1	# Claims for Prince, Cushing, Yassine, Katragadda, Roberts & Singer (2025), "New information
2	# triggers prospective codes to adapt for flexible navigation", Nat. Commun. 16, 4822, on
3	# dandiset 001371.
4	#
5	# Provenance: written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions),
6	# 2026-10-21, protocol pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
7	#
8	# Text read: the version of record, as served by Europe PMC (PMC12102184), full text with
9	# Methods, figure legends and Data and Code availability; the Supplementary Information PDF
10	# (41467_2025_60122_MOESM1_ESM: Supplementary Tables 1 and 2, Supplementary Figures 1 to 14
11	# with legends); the Peer Review File (MOESM3). The Reporting Summary (MOESM2) had no
12	# extractable text and was not needed. The Source Data file was not available and was not
13	# used. No figure was read from a PDF page.
14	#
15	# Code read: https://github.com/stephprince/update-project, commit
16	# d8557f031f45cb04532484a8a4f730af954a881d (2025-05-23). It holds the whole Python analysis:
17	# update_task_figure_generator.py (which analysis and parameters make each figure),
18	# decoding/bayesian_decoder_analyzer.py (encoder and decoder), decoding/
19	# bayesian_decoder_aggregator.py and bayesian_decoder_visualizer.py (alignment, goal arm
20	# integration, windows, trial selection, residual GLM, SVM prediction, commitment
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "e-11\|e-08\|e-07\|e-05\|10−\|× 10" paper/10.1038-s41467-025-60122-8.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk 'length>0' 10.1038-s41467-025-60122-8.txt | wc -c; grep -n "Supplementary Table 2\|^Methods\|^Results\|^Discussion\|Supplementary Figure 1\b" 10.1038-s41467-025-60122-8.txt | head -30
```

```
<persisted-output>
Output too large (113.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/051954fd-5ef8-42e1-af00-3b0beea81541/tool-results/byxy5szdq.txt

Preview (first 2KB):
334411
7:2873 ncomms Nature Communications Nat Commun Nature Publishing Group PMC12102184 12102184 12102184 40410173 10.1038/s41467-025-60122-8 New information triggers prospective codes to adapt for flexible navigation Prince Stephanie M 1 Cushing Sarah Danielle 1 Yassine Teema A 1 Katragadda Navya 1 Roberts Tyler C 1 Singer Annabelle C 1 ✉ 1 Coulter Department of Biomedical Engineering, Emory University and Georgia Institute of Technology, Atlanta, GA USA ✉ Corresponding author. 24 5 2025 16 4822 4822 24 5 2025 © The Author(s) 2025 Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/ . Previous version available: This article is based on a previously available preprint posted on bioRxiv on November 1, 2023: " New information triggers prospective codes to adapt for flexibl
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' 10.1038-s41467-025-60122-8.txt | sort -t: -k2 -n -r | head; sed -n 8,60p 10.1038-s41467-025-60122-8.txt | cut -c1-200
```

```
7: 113557
234: 278
210: 259
280: 246
274: 246
100: 241
252: 237
204: 230
226: 229
230: 226

[HYPERLINKS]
https://creativecommons.org/licenses/by-nc-nd/4.0/
PMC10634986
https://dandiarchive.org/dandiset/001371
https://github.com/stephprince/update-project
10.1037/h0061626
18870876
10.1016/j.neuron.2018.10.002
30359611
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 7p 10.1038-s41467-025-60122-8.txt | fold -s -w 2000 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; grep -n "Supplementary\|SUPPLEMENT\|Peer Review\|REVIEWER" 10.1038-s41467-025-60122-8.txt | awk -F: '$1>8' | head -20
```

```
57 /tmp/claude-1001/main.txt
295:SUPPLEMENTARY INFORMATION 
314:SUPPLEMENTARY TABLES 
433:Supplementary Table 1. Experimental metadata for all recording sessions.  
2174:Supplementary Table 2. Statistical analysis details.  
2185:SUPPLEMENTARY FIGURES 
2187: Supplementary Figure 1. Additional update task behavioral metrics and task details. 
2279:indicate animal identification number in color corresponding to bar graph. See Supplementary Table 
2291:Supplementary Figure 2. Separate and concurrent representation of each goal arm and Bayesian 
2443:Supplementary Figure 3. Differences in goal arm representations between the original and update cue. 
2648:Supplementary Figure 4. Hippocampal position decoding in each animal. 
2697:Supplementary Figure 5. Bayesian decoding of position for prefrontal cortex. 
2905:Supplementary Figure 6. Theta phase modulation of position representations for stay and delay only 
2920:post-hoc, see Supplementary Table 2 for statistical details.  
2993:Supplementary Figure 7. Bayesian decoding validation of prefrontal choice representation. 
3174:Supplementary Figure 8. Prefrontal choice decoding in each animal. 
3224:Supplementary Figure 9. Bayesian decoding of choice representation in hippocampus. 
3366:Supplementary Figure 10. Transient increase in decoding of new goal arms on stay trials. 
3474:Supplementary Figure 11. Generalized linear model inputs and outputs to control for differences in 
3597:Supplementary Figure 12. Hippocampal position codes do not significantly differ on correct and 
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt"
}
```

```
1	2873 ncomms Nature Communications Nat Commun Nature Publishing Group PMC12102184 12102184 12102184 40410173 10.1038/s41467-025-60122-8 New information triggers prospective codes to adapt for flexible navigation Prince Stephanie M 1 Cushing Sarah Danielle 1 Yassine Teema A 1 Katragadda Navya 1 Roberts Tyler C 1 Singer Annabelle C 1 ✉ 1 Coulter Department of Biomedical Engineering, Emory University and Georgia Institute of Technology, Atlanta, GA USA ✉ Corresponding author. 24 5 2025 16 4822 4822 24 5 2025 © The Author(s) 2025 Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/ . Previous version available: This article is based on a previously available preprint posted on bioRxiv on November 1, 2023: " New information triggers prospective codes to adapt for flexible navigation ". Abstract Navigating a dynamic world requires rapidly updating choices by integrating past experiences with new information. In hippocampus and prefrontal cortex, neural activity representing future goals is theorized to support 
2	navigat
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 33
}
```

```
33	prefrontal cortex activity can represent both planned non-local positions and current position, albeit with lower spatial specificity than CA1 32 , 40 – 42 . In agreement with prior studies examining representations of current spatial position, we find prefrontal cortex exhibits spatial coding but with lower precision than CA1 40 . While the update cue did not induce a significant increase in prefrontal representation of goal arms, such representations may still be occurring and supporting task performance even if they do not dynamically increase with new pivotal information 32 , 41 . Overall, these results show that hippocampal prospective coding does not preferentially overrepresent the planned trajectory, but a general increase in prospective coding occurs when new, crucial information is presented in an environment. Importantly, non-local goal coding of the new, upcoming goal increases more when animals need to produce a larger trajectory change in response to the new information. Our findings show that the representation of new possible goals in hippocampus reflects the animals’ need to consider new information in relationship to their current decision. These findings may explain variation in the ability to predict upcoming choices from hippocampal activity across studies. We propose that the non-local spiking events might reflect moments of representation of possible outcomes to the animals at a faster timescale scale than other noted behavioral deliberation events such as vicarious trial and error 9 , 20 . While animals decrease their velocity slightly after the update cue is presented, the animals do not often pause at the update cue or choice point on the virtual reality track and thus do not exhibit traditional vicarious trial and error behavioral features during these moments of non-local coding. These non-local codes might be triggered not only by new information about goals, but also by task-relevant information more generally. Recent work found that
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "offset": 450,
 "limit": 450
}
```

```
450	    p: 0.0011
451	    corrected: Tukey
452	    n: 1295 switch trials
453	  expected:
454	  - quantity: retrospective, switch
455	    value: 0.12
456	    tolerance: 0.012
457	  - quantity: initial arm, switch
458	    value: 0.13
459	    tolerance: 0.013
460	  - quantity: new arm, switch
461	    value: 0.14
462	    tolerance: 0.014
463	  depends_on:
464	  - fig2e-hpc-goal-increase
465	  criterion: As fig2e-hpc-goal-increase with a third zone, the retrospective zone, the first 0.15 of the
466	    track (Results); the code integrates linearized positions 5 to 50 (quantify_aligned_data with prospective_reps).
467	    LME with zone as predictor on correct switch trials, Tukey contrasts. Reproduced when both goal arms
468	    exceed the retrospective zone with p < 0.05.
469	- id: sfig3c-retrospective-unchanged
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 295,440p 10.1038-s41467-025-60122-8.txt
```

```
SUPPLEMENTARY INFORMATION 
 
 
 
New information triggers prospective codes to adapt for flexible navigation 
 
Authors 
Stephanie M. Prince, Sarah Danielle Cushing, Teema A. Yassine, Navya Katragadda, Tyler C. Roberts, 
Annabelle C. Singer 
 
 
Includes 
2 Tables 
14 Figures 
 
 

=== page 2 ===
Page 2 of 38 
SUPPLEMENTARY TABLES 
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 440,900p 10.1038-s41467-025-60122-8.txt | tr '\n' '|' | sed 's/ *| */|/g'
```

```
classification (see Methods).|***Number of trials indicate all completed trials during recording sessions.|||=== page 3 ===|Page 3 of 38|Panel Data|Group size|Percentiles|[minimum,|25th, median,|75th,|maximum]|Statistical|method|Comparison|Test|statistic|P-value|Notatio|n|Figure|1b|Proportion|correct|n = 6252|windows of|40 trials in 66|sessions from|7 animals|Delay only|trials: 0.13,|0.53, 0.67,|0.87, 1.00;|switch trials:|0.27, 0.67,|0.80, 0.87,|1.00|Wilcoxon|signed-rank|test|Switch trials vs.|50% correct|W =|48.5|3.410e-11|****|Delay only trials|vs. 50% correct|W =|125.5|6.197e-10|****|Figure|2e|Hippocampal|position|decoding;|posterior|probability|density|integrated by|goal arm|Switch: n =|1295 trials|Delay only: n|= 926 trials|initial, switch:|0.00, 0.03,|0.10, 0.19,|0.87; new,|switch: 0.00,|0.04, 0.10,|0.21, 0.97;|initial, delay|only: 0.00,|0.02, 0.07,|0.15, 0.88;|new, delay|only: 0.00,|0.02, 0.08,|0.16, 1.00|Linear mixed|effects|model;|ANOVA,|Tukey post-|hoc pairwise|test|Trial type|(switch, delay|only), goal arm|F(4400.|90) =|21.79|5.286e-14|****|Switch vs. delay|only, initial goal|Z = -5.87 2.630e-8|****|Switch vs. delay|only, new goal|Z = -5.39 4.157e-7|****|Figure|2e|Hippocampal|position|decoding;|difference in|initial vs. new|goal arm|posterior|probability|density|Switch: n =|1295 trials|Delay only: n|= 926 trials|Switch: -0.95,|-0.11, 0.00,|0.10, 0.87;|delay only: -|0.99, -0.08, -|0.00, 0.07,|0.88|Linear mixed|effects|model;|ANOVA|Trial type|(switch, delay|only)|F(2205.|71) =|0.08|0.7806|ns|Figure|2e|Hippocampal|position|decoding;|difference in|initial vs. new|Switch: n =|56 sessions,|Delay only: n|= 56 sessions|Same as|above|Wilcoxon|signed-rank|test|Switch vs. zero|W = 676 0.3216|ns|Delay only vs|zero|W = 706 0.4554|ns||Figure|2g|Prefrontal|position|decoding;|posterior|probability|Switch: n =|1109 trials|Delay only: n|= 798 trials|Initial, switch:|0.00, 0.00,|0.03, 0.09,|0.80; new,|switch: 0.00,|Linear mixed|effects|model;|ANOVA,|Tukey post-|Trial type|(
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 900,1500p 10.1038-s41467-025-60122-8.txt | tr '\n' '|' | sed 's/ *| */|/g'
```

```
model|New arm, first|half vs. second|half|F(2533.|71) =|11.22|0.0008|***|Figure|3c, d|Hippocampal|position|decoding; theta|timescale|comparing trial|types after|update cue|Switch: n =|1295 trials;|Stay: n = 552|trials; delay|only: n = 927|trials|Same as|above for|switch trials;|For delay only|trials: initial, -|p to 0: 0.00,|0.10, 0.12,|0.14, 0.42;|initial, 0 to p:|Linear mixed|effects|model;|ANOVA|Tukey post-|hoc pairwise|test|Trial type|(switch, delay|only), initial goal|arm|F(5496.|53) =|27.48|1.450e-27|****|Switch vs. delay|only, first half of|theta cycle|Z = -5.79 1.083e-7|****|Switch vs. delay|only, second|half|Z = -8.46 5.851e-14|****||=== page 6 ===|Page 6 of 38|0.00, 0.09,|0.11, 0.13,|0.35; new, -p|to 0: 0.00,|0.10, 0.12,|0.14, 0.32;|new, 0 to p:|0.00, 0.09,|0.11, 0.13,|0.38;|Stay vs. delay|only, first half|Z = 0.50 0.9961|ns|Stay vs. delay|only,|Second half|Z = -0.84 0.9594|ns|Switch vs. stay,|first half|Z = -5.43 8.382e-7|****|Switch vs. stay,|second half|Z = -6.28 4.956e-9|****|Figure|3c|Hippocampal|position|decoding; theta|timescale|update trial|types|Switch: n =|1295 trials;|Stay: n = 552|trials; delay|only: n = 927|trials|Same as|above|Linear mixed|effects|model;|ANOVA|Tukey post-|hoc pairwise|test|Trial type|(switch, delay|only), new goal|arm|F(5500.|03) =|13.96|1.367e-13|****|Switch vs. delay|only, first half|Z = -5.26 2.163e-6|****|Switch vs. delay|only, second|half|Z = -4.94 1.179e-5|****|Stay vs. delay|only, first half|Z = -1.36 0.7534|ns|Stay vs. delay|only,|Second half|Z = -2.76 0.0634|ns|Switch vs. stay,|first half|Z = -3.02 0.0303|*|Switch vs. stay,|second half|Z = -1.27 0.8041|ns|Figure|4A|Accuracy of the|LSTM choice|output|original cue:|n = 66|session|averages;|delay cue: n =|66 session|averages;|update cue: n|= 66 session|averages;|delay2 cue: n|= 66 session|averages|original cue:  -|2.62, -0.97, -|0.91, -0.82, -|0.60; delay|cue: -1.13, -|0.79, -0.66, -|0.50, -0.07;|update cue: -|1.07, -0.58, -|0.41, -0.29, -|0.01; delay2|cue:  -0.72, -|0.
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1500,2185p 10.1038-s41467-025-60122-8.txt | tr '\n' '|' | sed 's/ *| */|/g'
```

```
stay: -0.92, -|0.12, -0.00,|0.04, 0.58.|ANOVA,|Tukey post-|hoc pairwise|test|Stay vs. switch|T = -2.62 0.0240|*|Stay vs. delay|only|T = 2.57 0.0273|*|Figure|5f|Prefrontal|choice|decoding;|posterior|probability|density|integrated by|goal arm and|difference|Switch: n =|1109 trials,|Stay: n = 483|trials,|Delay only: n|= 798 trials|initial, stay:|0.00, 0.05,|0.10, 0.20,|0.70; new,|stay: 0.00,|0.02, 0.07,|0.13, 0.66|Linear mixed|effects|model;|ANOVA,|Tukey post-|hoc pairwise|test|Trial type|(switch, stay,|delay only),|choice|F(4739.|91) =|55.44|3.584e-56|****|Stay vs. switch,|initial choice|Z = 6.77 1.908e-10|****|Stay vs. delay|only, initial|choice|Z = 3.68 0.0032|**|Stay vs. switch,|new choice|Z = -3.46 0.0072|**|Stay vs. delay|only, new choice|Z = -1.29 0.7914|ns|Figure|5f|Prefrontal|choice|decoding;|Difference in|initial vs. new|choice|posterior|probability|density|Switch: n =|1109 trials,|Stay: n = 483|trials,|Delay only: n|= 798 trials|stay: -0.66, -|0.04, 0.03,|0.13, 0.70|Linear mixed|effects|model;|ANOVA,|Tukey post-|hoc pairwise|test|Trial type|(switch, stay,|delay only)|F(2370.|62) =|76.21|8.356e-33|****|Stay vs. switch|T = 6.86|< 4.462e-61|****|Stay vs. delay|only|T = 3.25 0.0033|**|Figure|6b|Hippocampal|position|decoding;|posterior|probability|density|integrated by|goal arm|Switch,|correct: n =|1295 trials,|Switch,|incorrect: n =|407 trials|initial, correct:|-0.50, -0.21, -|0.04, 0.22,|2.09; initial,|incorrect: -|0.43, -0.22, -|0.04, 0.18,|1.88; new,|correct: -0.47,|-0.20, -0.03,|0.25, 1.72;|new,|incorrect: -|0.45, -0.24, -|0.08, 0.13,|2.27|Linear mixed|effects|model;|ANOVA,|Tukey post-|hoc pairwise|test|Trial outcome|(correct,|incorrect), goal|arm|F(3283.|78) =|4.99|0.0019|**|Correct vs.|incorrect, initial|goal|Z = 1.75 0.2967|ns|Correct vs.|incorrect,|New goal|Z = 3.51 0.0025|**||=== page 10 ===|Page 10 of 38|Figure|6b|Hippocampal|position|decoding;|difference in|initial vs. new|goal arm|posterior|probability|density|Switch,|correct: n =|1295 trials,|Switch
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "offset": 899,
 "limit": 450
}
```

```
899	    statistic: F(2533.71) = 11.22
900	    p: 0.0008
901	    n: 1295 switch trials
902	  - about: initial arm, first against second half, as the text prints
903	    test: linear mixed effects model
904	    p: 0.6496
905	  - about: initial arm, first against second half, as Supplementary Table 2 prints
906	    test: linear mixed effects model
907	    statistic: F(2533.36) = 0.65
908	    p: 0.4203
909	  - about: central arm, first against second half
910	    test: linear mixed effects model
911	    statistic: F(2533.33) = 119.77
912	    p: 2.868e-27
913	  depends_on:
914	  - fig3c-theta-phase-segregation
915	  criterion: As fig3c-theta-phase-segregation, one LME per arm with phase half as predictor (Supplementary
916	    Table 2), correct switch trials, 0 to 1.5 s. Reproduced when the new arm gives p < 0.05 and the initial
917	    arm, a claim of absence judged on the same test, gives p >= 0.05. The text and the table print different
918	    initial arm p values (0.6496, 0.4203); both are above 0.05.
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "offset": 1348,
 "limit": 420
}
```

```
1348	  source: Results, Goal codes for updating behaviors are not due simply to new visual information, paragraph
1349	    3; Figure 5f right
1350	  quote: Furthermore, the difference between initial and new choice decoding was significantly different
1351	    between trial types ( p < 4.462e−61 initial-new for switch vs. stay, p = 0.0033 initial-new for stay
1352	    vs. delay only)
1353	  statistics:
1354	  - about: initial minus new by trial type
1355	    test: linear mixed effects model, ANOVA
1356	    statistic: F(2370.62) = 76.21
1357	    p: 8.356e-33
1358	    n: 1109 switch, 483 stay, 798 delay only trials
1359	  - about: stay against switch
1360	    test: linear mixed effects model, Tukey post-hoc pairwise test
1361	    statistic: T = 6.86
1362	    p: 4.462e-61
1363	    p_relation: <
1364	    corrected: Tukey
1365	  - about: stay against delay only
1366	    test: linear mixed effects model, Tukey post-hoc pairwise test
1367	    statistic: T = 3.25
[... 390 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 2185,3000p 10.1038-s41467-025-60122-8.txt | awk 'length>25' | tr '\n' ' ' | fold -s -w 3000
```

```
Supplementary Figure 1. Additional update task behavioral metrics and task details.  a. Durations of events during behavioral task across trial types. Left, total trial duration from trial start  to choice being made (Delay only: black, switch: purple). (delay only: 20.93 ± 0.09 seconds, n = 7313  trials, switch: 20.79 ± 0.23 seconds, n = 1886 trials). Right, durations for different cue phases of the  task across trial types. Original cue to choice indicates period from original cue offset until choice  made, equivalent to the duration of the delay phase for delay only trials. No values recorded for 1st  delay, update, and 2nd delay for delay only trials since there were no cue updates and the duration of  the delay is captured by the ‘original to choice made’ metric.  Task performance per animal delay1 delay2 delay3 delay4  b. Performance across trial types by individual animal during recording sessions. Colored numbers  indicate animal identification number in color corresponding to bar graph. See Supplementary Table  1 for individual animal metadata.  c. Performance for delay only trials across different delay durations during the warmup training at the  start of each session. Delay 1 n = 58 sessions, delay 2 n = 58 sessions, delay 3 n = 57 sessions, delay 4  d. Trajectories of additional behavioral metrics across delay only (black) and switch(purple) trials. Note  that the lateral position is restricted to a very small distance for the center arm of the environment.  Supplementary Figure 2. Separate and concurrent representation of each goal arm and Bayesian  decoding validation for hippocampal position  a. Reconstructed electrode insertion paths from histological data registered to Allen mouse atlas. Each  line indicates a separate electrode shank or probe if individual shanks could not be isolated.  Hippocampal CA1, prelimbic cortex, and infralimbic cortex regions highlighted.   Goal arm representations all trials in encoding model b. Example histological imag
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 3000,4200p 10.1038-s41467-025-60122-8.txt | awk 'length>25' | tr '\n' ' ' | fold -s -w 3000; echo; grep -n "Peer Review\|REVIEWER\|Reviewer" 10.1038-s41467-025-60122-8.txt | head
```

```
<persisted-output>
Output too large (148.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/051954fd-5ef8-42e1-af00-3b0beea81541/tool-results/bwqe0a88d.txt

Preview (first 2KB):
Decoded choice - longer timescale around update cue onset initial - new prob. density Motor response triggered average time around motor response (s) Choice representations 1.5-0.5s before update cue prob. density after update onset initial - new prob. density prob. density after update onset initial - new prob. density b. Left, Confusion matrix (decoded choice from prefrontal neural activity compared to actual choice  estimate from behavioral data) for all delay only trials. Right, cumulative distribution of decoding  errors where error is measured as the absolute difference between the actual position and the peak  c. Decoding output (posterior probability density) before and after the update cue is presented at a  longer timescale (10 seconds before and after). The heatmap shows a rapid decrease in the initial  choice (blue) and increase in the new choice (pink) representations after the update cue. Average  across all recording sessions for switch trials. Heatmap indicates which choices are most strongly  decoded by the spiking activity of all prefrontal neurons. Blue and pink indicate decoding of initial and  new choices, respectively. Animals’ actual choice estimate (yellow dashed line) shown over the same  time window. Data from both left and right trial types were combined.   d. Neural activity aligned to motor response times on an individual trial basis. Motor responses were  identified as the moment the rotational velocity began decelerating (the differential of the velocity  signal switched from positive to negative). Top, difference between initial and new choice decoding  outputs. Bottom, initial and new choice decoding outputs.  Mean ± SEM across trials shown.  e. i left, probability density decoding of the in
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "=== page\|Peer Review\|REVIEWER COMMENTS\|Reviewer #" 10.1038-s41467-025-60122-8.txt | awk -F: '$1>3700' | head -20
```

```
3714:=== page 34 ===
3726:=== page 35 ===
3826:=== page 36 ===
3849:=== page 37 ===
3954:=== page 38 ===
3975:=== page 1 ===
3977:=== page 2 ===
3979:=== page 3 ===
3984:=== page 1 ===
3985:Peer Review File
3992:Reviewer #1 
4029:=== page 2 ===
4075:Reviewer #2 
4088:=== page 3 ===
4147:=== page 4 ===
4164:Reviewer #1 
4188:Reviewer #2 
4191:=== page 5 ===
4196:Open Access This Peer Review File is licensed under a Creative Commons Attribution 4.0 International License, which
4201:The images or other third party material in this Peer Review File are included in the article’s Creative Commons license,
```

**Agent calls Bash**

```bash
cd paper; sed -n 3000,3975p 10.1038-s41467-025-60122-8.txt | awk 'length>40' | tr '\n' ' ' | fold -s -w 3000
```

```
Decoded choice - longer timescale around update cue onset Choice representations 1.5-0.5s before update cue b. Left, Confusion matrix (decoded choice from prefrontal neural activity compared to actual choice  estimate from behavioral data) for all delay only trials. Right, cumulative distribution of decoding  errors where error is measured as the absolute difference between the actual position and the peak  c. Decoding output (posterior probability density) before and after the update cue is presented at a  longer timescale (10 seconds before and after). The heatmap shows a rapid decrease in the initial  choice (blue) and increase in the new choice (pink) representations after the update cue. Average  across all recording sessions for switch trials. Heatmap indicates which choices are most strongly  decoded by the spiking activity of all prefrontal neurons. Blue and pink indicate decoding of initial and  new choices, respectively. Animals’ actual choice estimate (yellow dashed line) shown over the same  time window. Data from both left and right trial types were combined.   d. Neural activity aligned to motor response times on an individual trial basis. Motor responses were  identified as the moment the rotational velocity began decelerating (the differential of the velocity  signal switched from positive to negative). Top, difference between initial and new choice decoding  outputs. Bottom, initial and new choice decoding outputs.  Mean ± SEM across trials shown.  e. i left, probability density decoding of the initial (left) and new (right) prefrontal choice codes on  switch (purple) versus delay only (grey) trials during the 1.5-0.5s prior to update cue presentation  for correct trials. Colored points and line indicate mean ± 95% CI computed with n = 1000 bootstrap  samples. (initial p = 0.0031; new p = 0.1967; Initial, delay only: 0.13 ± 0.01, n = 792 trials; initial,  switch: 0.11 ± 0.00, n = 1099 trials; new, delay only: 0.07 ± 0.00, n = 792 trials; new, switch
[... 5 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    trials; (b) the per-session fractions averaged over sessions. Reproduced when all three fractions\n    are within tolerance under one reading.'",
 "new_string": "    trials; (b) the per-session fractions averaged over sessions. Reproduced when all three fractions\n    are within tolerance under one reading. Note: the paper''s own counts do not give these fractions.\n    Supplementary Table 1 lists 8104 delay, 1840 switch and 717 stay completed trials (0.76, 0.17,\n    0.07), and the Results counts (7172 delay only, 1840 switch) with the 717 stay trials give 0.74, 0.19,\n    0.07; both fall outside the tolerances, so the percentages read as the task''s programmed trial\n    probabilities (Methods). The realized fractions are reported beside the result.'"
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    delay on switch trials runs from original cue offset to update cue onset. The second delay is open;\n    readings (a) second delay onset (t_delay2) to choice made, (b) update cue onset to choice made. The",
 "new_string": "    delay on switch trials runs from original cue offset to update cue onset. The second delay is open;\n    readings (a) second delay onset (t_delay2) to choice made, (b) update cue onset to choice made. The\n    Results do not say which trials the 6.02 s second delay covers (Methods give a second delay on stay\n    and update trials); readings for it (e) switch trials, (f) switch and stay trials pooled. The"
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    (delay only, switch, stay; Methods \"we used all trial types ... to build our encoding model as a control\"),\n    decoding the held-out trials. Supplementary Fig. 2f lists 1322 switch and 4538 delay only trials,\n    which suggests all outcomes; readings (a) correct trials as in Figure 2e, (b) correct and incorrect.\n    Reproduced when both arms remain higher on switch than on delay only trials with Tukey p < 0.05 under\n    every reading.",
 "new_string": "    (delay only, switch, stay; Methods \"we used all trial types ... to build our encoding model as a control\").\n    Which trials are decoded is open. Supplementary Fig. 2f lists 1322 switch and 4538 delay only trials;\n    4538 is close to the 926 held-out correct delay only trials of Figure 2e divided by 0.2 (about 4630),\n    so the decoded trials do not look restricted to a 20% test set. Readings (a) encoder built from all\n    trials of all types and every trial decoded with it; (b) encoder from 80% of all trial types, the\n    held-out 20% decoded. Readings for outcome (c) correct trials as in Figure 2e (1322 is near the 1295\n    correct switch trials), (d) correct and incorrect. Trial counts under each reading are reported against\n    1322 and 4538. Reproduced when both arms remain higher on switch than on delay only trials with Tukey\n    p < 0.05 under every reading."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "  criterion: CA1 choice decoding as fig4f-pfc-choice-flips. The window is open; readings (a) 0 to 1.5\n    s (Methods), (b) 0 to 2 s (code, plot_goal_coding_stats with time_window (0, 2) for this panel). Reproduced\n    when, under every reading, initial is lower and new higher on switch trials with p < 0.05.",
 "new_string": "  criterion: CA1 choice decoding as fig4f-pfc-choice-flips, over 0 to 1.5 s after the cue (Methods quantification\n    window). Variant (code, plot_goal_coding_stats with time_window (0, 2) for this panel), 0 to 2 s, shown\n    but not deciding, since the Methods come first where they disagree with the code. Reproduced when\n    initial is lower and new higher on switch trials with p < 0.05."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    Table 2 does for Figures 2e and 2g); and the window readings of fig4h-hpc-choice-switches. Reproduced",
 "new_string": "    Table 2 does for Figures 2e and 2g); window 0 to 1.5 s as fig4h-hpc-choice-switches. Reproduced"
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent**

Now the GLM criteria. Where the Methods and the code disagree, the Methods come first:

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    What the GLM is fit on is open; readings (a) across all trial types and animals (Methods), (b) per\n    session on the switch trials of the comparison (code, by_session=True). Trial value the mean residual\n    in the window; LME with outcome by arm, Tukey contrasts. Reproduced when, under every reading, the\n    new arm contrast gives p < 0.05 with correct higher.'",
 "new_string": "    The GLM is fit on the bins of all trial types and animals together (Methods \"across all trial types\n    and animals\"); the code fits it per session on the switch trials of the comparison (by_session=True),\n    which is shown as a variant and does not decide, since the Methods come first where they disagree\n    with the code. Trial value the mean residual in the window; LME with outcome by arm, Tukey contrasts.\n    Reproduced when the new arm contrast gives p < 0.05 with correct higher.'"
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    for the initial arm, under its GLM readings. Reproduced when p >= 0.05 under every reading; not reproduced\n    when p < 0.05 under every reading; otherwise blocked as methods_underspecified.",
 "new_string": "    for the initial arm, with its Methods GLM (the per-session code GLM shown as a variant). Reproduced\n    when p >= 0.05; not reproduced when p < 0.05."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    the initial arm contrast gives p < 0.05 with incorrect higher under every GLM reading.",
 "new_string": "    the initial arm contrast gives p < 0.05 with incorrect higher (Methods GLM; code GLM as a variant)."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "  criterion: PFC choice decoding with the residuals and readings of fig6b-hpc-new-lower-incorrect, switch\n    trials of both outcomes, 0 to 1.5 s. Reproduced when, under every reading, the new choice contrast\n    gives p < 0.05 with correct higher.",
 "new_string": "  criterion: PFC choice decoding with the residuals of fig6b-hpc-new-lower-incorrect (Methods GLM; code\n    GLM as a variant), switch trials of both outcomes, 0 to 1.5 s. Reproduced when the new choice contrast\n    gives p < 0.05 with correct higher."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    for the initial choice over 0 to 1.5 s and over -1.5 to 0 s. Reproduced when both give p >= 0.05 under\n    every GLM reading; not reproduced when either gives p < 0.05 under every reading; otherwise blocked\n    as methods_underspecified.",
 "new_string": "    for the initial choice over 0 to 1.5 s and over -1.5 to 0 s, Methods GLM (code GLM as a variant). Reproduced\n    when both give p >= 0.05; not reproduced when either gives p < 0.05."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    for switch trials\"). Reproduced when all three p >= 0.05 under every GLM reading; not reproduced when\n    any p < 0.05 under every reading; otherwise blocked as methods_underspecified.",
 "new_string": "    for switch trials\"), Methods GLM (code GLM as a variant). Reproduced when all three p >= 0.05; not\n    reproduced when any p < 0.05."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001371/10.1038-s41467-025-60122-8.yaml",
 "old_string": "    contrast gives p < 0.05 with correct higher and the new contrast p < 0.05 with incorrect higher, under\n    every GLM reading.",
 "new_string": "    contrast gives p < 0.05 with correct higher and the new contrast p < 0.05 with incorrect higher (Methods\n    GLM; code GLM as a variant)."
}
```

```
The file claims/001371/10.1038-s41467-025-60122-8.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  grep -n "^checks\|^[a-z_]*:" claims/001371/*.yaml; tail -3 claims/001371/*.yaml; grep -rn "checks:" claims/*/*.yaml | head -3
```

```
124:schema_version: 2
125:dataset:
128:paper: doi:10.1038/s41467-025-60122-8
129:claims:
    (positive, which fits the quartile means of the Figure 7e legend and the sentence quoted) and Supplementary
    Table 2 (negative). Reproduced when rho > 0 with p < 0.05; a result with rho < 0 and p < 0.05 matches
    only the table and is partially reproduced; not reproduced when p >= 0.05.
claims/000005/10.1038-nn.4412.yaml:1092:checks:
claims/000006/10.1038-s41586-018-0642-9.yaml:746:checks:
claims/000008/10.1038-s41586-020-2907-3.yaml:964:checks:
```

**Agent calls Bash**

```bash
cd  sed -n '1092,1110p' claims/000005/10.1038-nn.4412.yaml
```

```
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/001371/10.1038-s41467-025-60122-8.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - trial-mix. Added that the paper's own counts do not give 65/25/10% (Supplementary Table 1 gives 0.76, 0.17 and 0.07; the Results counts give 0.74, 0.19 and 0.07), so the percentages read as programmed trial probabilities. The realized fractions are to be reported. Expected values unchanged, so the claim is likely to fail on the paper's own numbers.
  - task-timing. The Results do not say which trials the 6.02 s second delay covers, and the Methods give a second delay on both stay and update trials. Added readings for switch trials alone and for switch and stay pooled.
  - sfig2f-all-trials-encoder. The criterion decoded only held-out trials, but Supplementary Fig. 2f's 4538 delay only trials is about 926/0.2, so the paper does not seem to restrict decoding to a 20% test set. Made the encoder/test split open, with readings (all trials in-sample, 80/20 held out) beside the outcome readings.
  - fig4h-hpc-choice-switches. Made 0 to 2 s (code) a variant and 0 to 1.5 s (Methods) the deciding window, since the protocol puts the Methods before the code where they disagree. Changed fig4h-hpc-choices-equal to match.
  - fig6b-hpc-new-lower-incorrect. The Methods fit the GLM "across all trial types and animals" and the code fits it per session. Made the Methods GLM decide and the code GLM a variant, since they disagree and the Methods come first. Changed fig6b-hpc-initial-no-difference, fig6-hpc-pre-cue-initial-higher-incorrect, fig6d-pfc-new-lower-incorrect, fig6d-pfc-initial-no-difference, sfig12-delay-hpc-no-outcome-difference and sfig12-delay-pfc-outcome-difference to match.
  - Checked and left unchanged. Every statistic, expected value and tolerance against the text, Supplementary Table 2 and the legends. The checker's five unmatched values (3.41e-11, 2.63e-08, 1.02e-07, 4.49e-05, 1.33e-05) are the paper's numbers without their trailing zeros.
  - Open. tuning-tiles-track, decoding-validation, fig1d-heading-switch, fig4d-pfc-precedes-movement, fig4g-hpc-slower-than-pfc and sfig7d-pfc-before-motor-single-trials use measures and thresholds the paper does not give (it reports no test for them). The criteria say so, but their pass rules were set by the reader.
  - Open. The code facts cited throughout (stephprince/update-project at d8557f0) were not re-read in this check.
  - Open. Supplementary findings with no claim, none of them main findings - theta segregation on delay only trials (Supplementary Fig. 6b), equal CA1 and PFC choice decoding (Supplementary Fig. 9e, p = 0.3364 and 0.9985), the stay-trial difference over 0 to 0.5 s (Supplementary Fig. 10b right), and performance against warm-up delay length (Supplementary Fig. 1c, no numbers given).
EOF
python tools/claims_check.py claims/001371/10.1038-s41467-025-60122-8.yaml paper/10.1038-s41467-025-60122-8.txt 2>&1 | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/001371/*.yaml | grep -n "  - .*: \|—\|rather"; git diff --stat; git status --short
```

```
claims/001371/10.1038-s41467-025-60122-8.yaml | 78 ++++++++++++++++++---------
 1 file changed, 52 insertions(+), 26 deletions(-)
 M claims/001371/10.1038-s41467-025-60122-8.yaml
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

The claims file for DANDI:001371 is ready for an attempt (`ready: true`). I made seven corrections, all in criteria; no claim ids, statistics or expected values changed. Nothing is committed.

**Checker result:** `52 claims, 52 quotes, 105 statistical values, 5 problems`. All quotes match word for word. The 5 problems are p-values the checker could not find: 3.41e-11, 2.63e-08, 1.02e-07, 4.49e-05 and 1.33e-05. Each is the paper's own number with its trailing zero dropped (the paper prints 3.410e-11, and so on), so they are correct.

I checked every statistic, expected value and tolerance against the main text, Supplementary Tables 1 and 2, and the figure legends. All are the paper's own numbers.

**Changes, by claim**
- **trial-mix:** the paper's own trial counts do not give 65/25/10%. Supplementary Table 1 gives 76/17/7%, and the Results counts give 74/19/7%. Both are outside the tolerances, so the percentages are read as the task's programmed trial probabilities. The criterion now says so and asks for the actual fractions to be reported. The expected values are unchanged, so this claim will probably fail even on the paper's own numbers.
- **task-timing:** the paper does not say which trials the 6.02 s second delay covers. I added two readings: switch trials only, and switch and stay trials together.
- **sfig2f-all-trials-encoder:** the criterion assumed only a held-out 20% of trials was decoded. The legend's 4538 delay only trials is about 926 / 0.2, so the decoded trials do not look like a 20% test set. The split is now open, with both readings named.
- **fig4h-hpc-choice-switches** and **fig4h-hpc-choices-equal:** the Methods set the window at 0 to 1.5 s and the authors' code uses 0 to 2 s. The protocol puts the Methods first, so 0 to 1.5 s now decides the outcome and 0 to 2 s is shown as a variant.
- **fig6b-hpc-new-lower-incorrect:** the Methods fit the speed-and-rotation model (GLM) "across all trial types and animals"; the code fits it per session. The Methods version now decides and the code's version is a variant. I made the same change in the six claims that use these residuals: fig6b-hpc-initial-no-difference, fig6-hpc-pre-cue-initial-higher-incorrect, fig6d-pfc-new-lower-incorrect, fig6d-pfc-initial-no-difference, sfig12-delay-hpc-no-outcome-difference and sfig12-delay-pfc-outcome-difference.

**What remains open** (recorded in the `checks` entry)
- Six claims rest on measures and pass rules the first reader chose, because the paper reports no test for them: tuning-tiles-track, decoding-validation, fig1d-heading-switch, fig4d-pfc-precedes-movement, fig4g-hpc-slower-than-pfc and sfig7d-pfc-before-motor-single-trials. Their criteria say this.
- I did not re-read the authors' code (stephprince/update-project at d8557f0), so the code details quoted in the criteria are taken on trust.
- Four supplementary findings have no claim. None is a main finding:
  - theta segregation on delay only trials (Supplementary Fig. 6b);
  - equal CA1 and prefrontal choice decoding (Supplementary Fig. 9e);
  - the stay-trial difference over 0 to 0.5 s (Supplementary Fig. 10b, right);
  - performance against warm-up delay length (Supplementary Fig. 1c, which gives no numbers).

Every main finding in the paper has a claim, and all claims come from this paper.

## End of run

38 turns, 4 minutes, result: success.
