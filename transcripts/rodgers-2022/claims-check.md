# 000231 · claims-check · run 40004254761

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000231/ paper/ | head -50; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md; python tools/claims_check.py claims/000231/10.1038-s41597-022-01728-1.yaml paper/10.1038-s41597-022-01728-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/000231/10.1038-s41597-022-01728-1.yaml
```

```
<persisted-output>
Output too large (39.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e49e42a1-7a33-4dc0-acbf-5289a95fca2d/tool-results/btraohkyu.txt

Preview (first 2KB):
# Claims for Rodgers (2022, Sci Data 9, 620) on dandiset 000231.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Source: the version of record, full text as served by Europe PMC
# (paper/10.1038-s41597-022-01728-1.txt), read from its Background & Summary, Methods, Data
# Records, Technical Validation, Usage Notes, Code availability, Tables 1 to 6 and the legends of
# Figs. 1 to 3. No PDF was stored, so no figure was seen; Fig. 2c (error rates per training set)
# is known only from its legend and the Technical Validation text. The paper is a data
# descriptor with no supplement and reports no statistical tests, so no claim has statistics.
# The bioRxiv preprint (10.1101/2022.05.10.491259, version 1) is also under paper/; it was
# compared for the reported counts (15 mice, 115 sessions, 18,514 trials, 63,979,800 frames,
# 88.9 h, 33.8 h, 44/115, 7433 frames, 2.8 pixels, 90 trials, 95%), which are the same, and
# was not otherwise used.
#
# Code read: https://github.com/cxrodgers/NwbDandiData2022 at commit
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/10.1038-s41597-022-01728-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e49e42a1-7a33-4dc0-acbf-5289a95fca2d/tool-results/bpacf7rzg.txt"
}
```

```
1	   161 paper/10.1038-s41597-022-01728-1.txt
2	   454 paper/10.1101-2022.05.10.491259.txt
3	   615 total
4	DOI: 10.1038/s41597-022-01728-1
5	Version: as served by europe_pmc
6	Source: europe_pmc+crossref (paper-text-fetcher)
7	Stored: 2026-10-21
8	Extracted: as fetched
9	------------------------------------------------------------------------
10	pmc Sci Data Sci Data Scientific Data 2052-4463 Nature Publishing Group UK London 9561117 1728 10.1038/s41597-022-01728-1 Data Descriptor A detailed behavioral, videographic, and neural dataset on object recognition in mice http://orcid.org/0000-0003-1762-3450 Rodgers Chris C. [removed: an e-mail address] grid.189967.8 0000 0001 0941 6502 Department of Neurosurgery, Emory University, Atlanta, GA 30322 USA 13 10 2022 13 10 2022 2022 9 620 16 5 2022 12 9 2022 © The Author(s) 2022 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ . Mice adeptly use their whiskers to touch, recognize, and learn about objects in their environment. This behavior is enabled by computations performed by populations of neurons in the somatosensory cortex. To understand these computations, we trained mice to use their wh
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
t=open('paper/10.1038-s41597-022-01728-1.txt').read()
i=t.find('pos_dist_thresh = 17')
print(t[i-200:i+9000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
t=open('paper/10.1038-s41597-022-01728-1.txt').read()
i=t.find('pos_dist_thresh')
print(i, len(t)); print(t[i-100:i+8000])"
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the claims file in full.

**Agent calls Read**

```json
{
 "file_path": "claims/000231/10.1038-s41597-022-01728-1.yaml"
}
```

```
1	# Claims for Rodgers (2022, Sci Data 9, 620) on dandiset 000231.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol as stated in docs/protocol.md (version pilot-10).
4	#
5	# Source: the version of record, full text as served by Europe PMC
6	# (paper/10.1038-s41597-022-01728-1.txt), read from its Background & Summary, Methods, Data
7	# Records, Technical Validation, Usage Notes, Code availability, Tables 1 to 6 and the legends of
8	# Figs. 1 to 3. No PDF was stored, so no figure was seen; Fig. 2c (error rates per training set)
9	# is known only from its legend and the Technical Validation text. The paper is a data
10	# descriptor with no supplement and reports no statistical tests, so no claim has statistics.
11	# The bioRxiv preprint (10.1101/2022.05.10.491259, version 1) is also under paper/; it was
12	# compared for the reported counts (15 mice, 115 sessions, 18,514 trials, 63,979,800 frames,
13	# 88.9 h, 33.8 h, 44/115, 7433 frames, 2.8 pixels, 90 trials, 95%), which are the same, and
14	# was not otherwise used.
15	#
16	# Code read: https://github.com/cxrodgers/NwbDandiData2022 at commit
17	# 33d610b63e8f43594d380443bf70ac1e4e6a48d0 (2022-04-30), linked in Usage Notes. It holds only
18	# UsageNotes.ipynb, which loads sub-231CR/sub-231CR_ses-20190921T144923_behavior+ecephys+image.nwb
19	# from dandiset 000231 and prints the trials table, the C2 angle, the C2 contacts, raw neural
20	# data and the units table. Its printed outputs disagree with the paper's NWB names. It reads
[... 582 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -E "88.9 hours|size of the dataset|In order to determine how mice|This dataset could be used|Here, we present the entire|We previously used these|Neural circuitry|Even in fully trained|For a subset|stopped at one of three|We purchased breeder|C0 here for simplicity|excluded sessions with fewer|neural and video timebase were|Since the camera ran|did not interpolate over gaps|distance between site centers|spanned 1280|Every  session|^Background|^Methods|^Technical|orthogonal|precise timing" 10.1101-2022.05.10.491259.txt | cut -c1-200
```

```
11:Mice adeptly use their whiskers to touch, recognize, and learn about objects in their environment. This ability is enabled by computations performed by populations of neurons in the somatosensory c
19:Neural circuitry in the brain controls this motor exploration and processes the resulting sensory input. We recorded neural activity from the barrel cortex 7 , which processes somatosensory input f
21:We previously used these data to identify how mice discriminated and detected shapes 6 . We found that shape discrimination mice compared the prevalence of contacts across whiskers, a comparison co
23:Here, we present the entire behavioral, video, and neural datasets that we collected during these tasks, available at https://dandiarchive.org/dandiset/000231 . The dataset includes 88.9 hours of b
49:On each trial, a linear servo motor moved a curved shape into the range of the whiskers on the right side of the mouse’s face. The shape stopped at one of three different positions (close, medium, 
59:As described in our previous publication 6 , the original experiments were conducted at Columbia University, under the supervision and approval of the Columbia University Institutional Animal Care 
65:On most trials, the stimuli were chosen at random. These “random trials” are the primary data that we analyzed. However, on other “non-random trials”, the stimuli were chosen specifically to counte
71:In order to determine how mice explored the shapes and what sensory evidence they used to make their decision, we used a Photonfocus DR1-D1312IE-100-G2-8 camera to collect high-speed video of the w
73:Using this video, our goal was to assess the entire extent of each of the four whiskers (C0-C3) on every frame, identify which whisker was which, and detect every contact made on the shape. The siz
107:For a subset (44/115) of the behavioral sessions we report here, we also recorded neuronal activity in identified columns of the barrel cortex. Located within the primary somatosensory co
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>=13 && NR<=60 && length>0 {print NR": "substr($0,1,110)}' 10.1101-2022.05.10.491259.txt; awk 'NR>=360 && NR<=372 && length>0 {print NR": "substr($0,1,110)}' 10.1101-2022.05.10.491259.txt
```

```
13: ## Background & Summary
15: Active sensing is the process of moving the body in order to learn about the world 1 . For instance, animals c
17: To study this, we previously 6 trained head-fixed mice to discriminate concave from convex shapes using only t
19: Neural circuitry in the brain controls this motor exploration and processes the resulting sensory input. We re
21: We previously used these data to identify how mice discriminated and detected shapes 6 . We found that shape d
23: Here, we present the entire behavioral, video, and neural datasets that we collected during these tasks, avail
25: Description of dataset Panel A shows data from the raw video whereas panels B-E show data from the NWB file. A
27: ## Description of dataset
29: Panel A shows data from the raw video whereas panels B-E show data from the NWB file. All panels show the same
31: A) Typical frames within the video. 8 markers from each of 4 whiskers shown here, but not included in the raw 
33: B) Times of whisker contacts (color raster) and licks (black raster).
35: C) Angle of each of the four whiskers (colors as in panel A).
37: (D) 64 channels of raw neural data. Highpassed at 3 Hz for display here. Spikes are visible as quick vertical 
39: E) Spike times from identified individual excitatory (red) and inhibitory (blue) neurons.
41: This dataset will be useful for understanding the motor control strategies mice use to direct their whiskers t
43: ## Methods
45: ## Two behavioral tasks
47: We trained two groups of mice to perform one of two tasks: shape discrimination (concave vs convex) or shape d
49: On each trial, a linear servo motor moved a curved shape into the range of the whiskers on the right side of t
51: Mice could move their whiskers, make contacts on the shape, and lick left or right at any time during the tria
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>=61 && NR<=140 && length>0 {print NR": "substr($0,1,90)}' 10.1101-2022.05.10.491259.txt; awk 'NR>=215 && NR<=240 && length>0 {print NR": "substr($0,1,90)}' 10.1101-2022.05.10.491259.txt; grep -n "^## " 10.1101-2022.05.10.491259.txt | sed -n 1,80p
```

```
61: ## Session control, and trial types to be dropped from analysis
63: For both tasks, the behavior was controlled by a desktop computer connected to an Arduino.
65: On most trials, the stimuli were chosen at random. These “random trials” are the primary d
67: On some sessions, we also delivered optogenetic stimulation (laser light) to the brain for
69: ## High-speed videography and whisker tracking
71: In order to determine how mice explored the shapes and what sensory evidence they used to 
73: Using this video, our goal was to assess the entire extent of each of the four whiskers (C
75: Most modern algorithms for tracking animal position require a training set, in which a hum
77: We used a deep convolutional neural network developed for tracking the position of human b
79: To address this, we iteratively 1) selected unlabeled “challenge frames” that were difficu
81: An iterative method for training a pose tracking network. This figure is adapted from Supp
83: ## An iterative method for training a pose tracking network. This figure is adapted from S
85: A) Example frames demonstrating the quality of the whisker tracking. Within each pair of f
87: 1) the whisker was obscured by a paw;
89: 2) whiskers were nearly overlapping;
91: 3) a “doublet” whisker emerged from the same follicle;
93: 4) the whisker was nearly out of frame;
95: 5) motion blurred the tips;
97: 6) a similar-looking distractor hair was attached to the end of the whisker.
99: B) We used an iterative procedure to train the network, repeatedly identifying “challenge 
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>=331 && NR<=361 && length>0 {print NR": "substr($0,1,90)}' 10.1101-2022.05.10.491259.txt
```

```
331: ## Validation of pose tracking data
333: As reported previously 6 , we rigorously validated the accuracy of our whisker tracking, b
335: Moreover, performance on the typical frame is not particularly important: in the majority 
337: We began by defining four disjoint types of whisker tracking errors, all defined with resp
339: “poorly traced”: The extent of the whisker is not traced correctly. For example, the tip i
341: “incorrectly classified”: The wrong label is assigned. For example, whisker C2 is correctl
343: “false positive”: A non-whisker object is reported as a whisker, or the same whisker objec
345: “false negative”: The whisker is present in the frame, but is not labeled. This is possibl
347: We used an iterative procedure to train our algorithm, which was critical to its success.
349: First, we chose n = 7433 frames randomly from all sessions for which we had video, applied
351: We trained a neural network on that dataset, and used it to label all the frames in all th
353: Of all these frames, we chose the frames on which the network was most likely to have made
355: We manually evaluated and corrected every challenge frame, using the previous generation w
357: We repeated steps 2-4 four times, to generate curated datasets 2-5.
359: As reported previously 6 , each type of error is nearly zero (<0.2%) on dataset 1, which i
361: In all cases we used doubly held-out cross validation: splitting the data into train, tune
```

**Agent calls Bash**

```bash
cd paper; for p in "reached its final position" "Only the first lick" "timeout, typically" "rarely made contact" "roughly equal proportion" "postnatal days" "Since the camera ran" "orthogonal" "precise timing"; do echo "$p: $(grep -n "$p" 10.1101-2022.05.10.491259.txt | cut -d: -f1 | tr '\n' ' ')"; done
```

```
reached its final position: 
Only the first lick: 53 
timeout, typically: 53 
rarely made contact: 55 
roughly equal proportion: 59 
postnatal days: 59 
Since the camera ran: 137 
orthogonal: 21 
precise timing: 11
```

**Agent calls Bash**

```bash
cd paper; sed -n 51p 10.1101-2022.05.10.491259.txt; sed -n 21p 10.1101-2022.05.10.491259.txt
```

```
Mice could move their whiskers, make contacts on the shape, and lick left or right at any time during the trial. We took as their “choice lick” the first lick that occurred in a period of time called the “response window”, which began exactly 2 seconds after the linear servo motor started moving the shape toward the mouse. If we define t = 0 as the opening of the response window, then the shape begins moving toward the mouse at t = -2 s, and reaches its final position between -0.8 s and -0.4 s, depending on whether the final position was close, medium, or far.
We previously used these data to identify how mice discriminated and detected shapes 6 . We found that shape discrimination mice compared the prevalence of contacts across whiskers, a comparison computation enabled by tuning changes in the barrel cortex. In contrast, shape detection mice simply responded to the total number of contacts across all whiskers, and in that case barrel cortex neurons maintained their expected tuning. We have also reported that barrel cortex represents sensory and motor variables in approximately orthogonal subspaces, which could be useful for generalization to novel conditions 8 . This flexible neural representation of the body and world could be useful for the active touch behaviors that mice evolved to do, which are more complex than the ones we study in the lab.
```

**Agent**

Checker passes (38 claims, 0 problems). I found a few substantive issues and several wrong paragraph pointers; applying fixes now.

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p='claims/000231/10.1038-s41597-022-01728-1.yaml'
s=open(p).read()
reps=[
("""  source: Methods, High-speed videography and whisker tracking, paragraph 1; Background &
    Summary, last paragraph""","""  source: Methods, High-speed videography and whisker tracking, paragraph 2; Background &
    Summary, paragraph 5"""),
("""  source: Background & Summary, last paragraph
  quote: includes 88.9""","""  source: Background & Summary, paragraph 5
  quote: includes 88.9"""),
("""  source: Methods, Two behavioral tasks, paragraph 1; Table 6 (servo_position)""","""  source: Methods, Two behavioral tasks, paragraph 2; Table 6 (servo_position)"""),
("""  criterion: Reproduced when the servo_position values over all trials with a shape (stimulus
    not "nothing") are exactly the set close, medium, far, and each occurs in every session's
    trials to analyse; partially reproduced when the set is right but some session lacks one.""","""  criterion: Reproduced when the servo_position values over all trials with a shape (stimulus
    not "nothing") are exactly the set close, medium, far; not reproduced otherwise. The paper
    does not say that every session used all three, so the positions present in each session
    are reported and do not enter the outcome."""),
("""  source: Methods, Two behavioral tasks, paragraph 1
  quote: which began exactly""","""  source: Methods, Two behavioral tasks, paragraph 3
  quote: which began exactly"""),
("""5 ms) after motor onset on at least 95% of trials and the motor stops between 0.8 and 0.4
    s before it, with close, medium and far ordered as the paper gives. Otherwise blocked; the""","""5 ms) after motor onset on at least 95% of trials and the motor stops between 0.8 and 0.4
    s before it. The paper does not say which position arrives first, so the stop time per
    position is reported and its order is not judged. Otherwise blocked; the"""),
("""  source: Methods, Two behavioral tasks, paragraph 1; Table 6 (outcome, choice)""","""  source: Methods, Two behavioral tasks, paragraph 4; Table 6 (outcome, choice)"""),
("""    timeout, typically 9 s long.
  source: Methods, Two behavioral tasks, paragraph 1""","""    timeout, typically 9 s long.
  source: Methods, Two behavioral tasks, paragraph 4"""),
("""  source: Methods, Alignment of multiple data streams, paragraph 2""","""  source: Methods, Alignment of multiple data streams, paragraph 4"""),
("""    readings run; not reproduced when the ISI part fails; blocked as methods_underspecified
    when the readings of the firing-rate part disagree.""","""    readings run; not reproduced when the ISI part fails or the firing-rate part fails under
    both readings; blocked as methods_underspecified when the readings of the firing-rate part
    disagree."""),
("""  criterion: Reproduced when every unit has exactly one interval, all its spikes fall inside
    it, and the interval lies within the span of the session's raw neural timestamps (within
    one sample).""","""  criterion: Reproduced when every unit has exactly one interval, all its spikes fall inside
    it, and the interval's start and stop equal the first and last raw neural timestamps of the
    session (within one sample), as Table 5 says it gives the start and stop of the neural
    recording; partially reproduced when the interval lies within that span but does not match
    its ends."""),
("""  source: Methods, Two behavioral tasks, paragraph 2
  quote: but this whisker""","""  source: Methods, Two behavioral tasks, paragraph 5
  quote: but this whisker"""),
("""  source: Methods, Two behavioral tasks, paragraph 3
  quote: We purchased""","""  source: Methods, Two behavioral tasks, paragraph 7
  quote: We purchased"""),
("""  statement: In the original study, shape discrimination mice compared the prevalence of
    contacts across whiskers, while shape detection mice responded to the total number of
    contacts across all whiskers.
  source: Background & Summary, paragraph 3 (findings of ref. 8)""","""  statement: In the original study, shape discrimination mice compared the prevalence of
    contacts across whiskers, a computation enabled by tuning changes in barrel cortex, while
    shape detection mice responded to the total number of contacts across all whiskers and
    barrel cortex neurons kept their expected tuning.
  source: Background & Summary, paragraph 4 (findings of ref. 8)"""),
("""    contrast, shape detection mice simply responded to the total number of contacts across all
    whiskers
  criterion:""","""    contrast, shape detection mice simply responded to the total number of contacts across all
    whiskers, and in that case barrel cortex neurons maintained their expected tuning
  criterion:"""),
]
for a,b in reps:
    assert s.count(a)==1,a
    s=s.replace(a,b)
s=s.rstrip('\n')+'\n'+"""- id: prior-orthogonal-subspaces
  statement: In earlier work on these data, barrel cortex represented sensory and motor
    variables in approximately orthogonal subspaces.
  source: Background & Summary, paragraph 4 (finding of ref. 10)
  quote: We have also reported that barrel cortex represents sensory and motor variables in
    approximately orthogonal subspaces, which could be useful for generalization to novel
    conditions
  criterion: A finding of ref. 10, restated here without any method; this paper gives no
    variables, model or measure of orthogonality for it. Blocked as methods_underspecified under
    this claims file; a test needs the methods of ref. 10.
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - "dataset-size, neural-hours: source corrected to Background & Summary paragraph 5 (the 88.9 h sentence is followed by the Fig. 1 legend and another paragraph, so it is not the last) and High-speed videography paragraph 2 (the size sentence follows the camera paragraph). Paragraph breaks are taken from the preprint text, whose wording matches here, as the version of record text has none."
  - "servo-positions: source corrected to Two behavioral tasks paragraph 2; the criterion no longer requires every position in every session, which the paper does not say; per-session positions are reported only."
  - "response-window-timing: source corrected to paragraph 3; the criterion asked for close, medium and far 'ordered as the paper gives', but the paper does not say which position arrives first, so the order is now reported and not judged."
  - "outcome-consistency, reward-and-timeout: source corrected to Two behavioral tasks paragraph 4, where the first-lick and timeout sentences are."
  - "c0-rare-contacts: source corrected to paragraph 5. subjects-sex-age-strain: source corrected to paragraph 7."
  - "video-timebase: source corrected to Alignment of multiple data streams paragraph 4 (the F/200 sentence follows the Fig. 3 legend)."
  - "unit-quality-isi: the outcome rule left a firing-rate failure under both readings undecided; it is now not reproduced."
  - "units-obs-intervals: the criterion only asked that the interval lie within the raw timestamps, less than the statement and Table 5 (the start and stop of the neural recording); it now asks that the ends match, with lying within as partial."
  - "prior-task-strategies: statement and quote extended with the barrel cortex tuning part of the same sentences (tuning changes in discrimination, expected tuning kept in detection), which the statement left out; source corrected to Background & Summary paragraph 4."
  - "prior-orthogonal-subspaces: added; the paper's other stated earlier finding on these data (ref. 10, Background & Summary paragraph 4) had no claim."
  - "Open: the abstract says the neurons responded with precise timing to whisker contacts and motion; no sentence of the main text, Methods or legends states or measures it, so no claim was written."
  - "Open: several outcome thresholds are not the paper's (99% and 95% in choice-time-first-lick and outcome-consistency, more than half the sessions or mice in forced-alternation-start, behavior-clock-drift, c0-rare-contacts and video-format, 1% of 30 kHz in neural-timestamps, the sex readings in subjects-sex-age-strain); each criterion says the paper gives none, and they were kept."
  - "Open: the tracking claims (tracking-mean-error, tracking-error-dataset1, tracking-error-challenge) need the curated training sets and held-out predictions, which the paper does not place among the deposits; they will likely be blocked."
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/000231/10.1038-s41597-022-01728-1.yaml paper/10.1038-s41597-022-01728-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short && python -c "import yaml;d=yaml.safe_load(open('claims/000231/10.1038-s41597-022-01728-1.yaml'));print(len(d['claims']),d['checks'][-1]['ready'])" && git diff | grep '^+' | grep -n -i -E 'rather|—' || true
```

```
M claims/000231/10.1038-s41597-022-01728-1.yaml
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
39 True
```

**Agent**

I checked the claims file for DANDI:000231 against the paper and made 13 corrections and one addition. The file is ready for an attempt.

**Checker:** `claims/000231/10.1038-s41597-022-01728-1.yaml: 39 claims, 39 quotes, 0 statistical values, 0 problems`. It was 38 claims before I added one.

**Changes, by claim:**
- **Wrong paragraph pointers fixed:**
  - `dataset-size` and `neural-hours`: Background & Summary paragraph 5, which is not the last paragraph; High-speed videography paragraph 2.
  - `servo-positions`: Two behavioral tasks, paragraph 2.
  - `response-window-timing`: paragraph 3.
  - `outcome-consistency` and `reward-and-timeout`: paragraph 4.
  - `c0-rare-contacts`: paragraph 5.
  - `subjects-sex-age-strain`: paragraph 7.
  - `video-timebase`: Alignment of multiple data streams, paragraph 4.
  - `prior-task-strategies`: Background & Summary, paragraph 4.

  The paper's text file has no paragraph breaks, so I counted them in the preprint, whose wording is the same in these places.
- **`servo-positions`:** the criterion required all three positions in every session, which the paper never says. Now only the set of positions decides the outcome, and positions per session are just reported.
- **`response-window-timing`:** the criterion judged an order of close, medium and far "as the paper gives", but the paper does not say which position arrives first. The order is now reported and not judged.
- **`unit-quality-isi`:** the outcome rule did not cover the firing-rate part failing under both readings. That case is now "not reproduced".
- **`units-obs-intervals`:** the criterion only asked that the interval lie inside the recording, which is weaker than Table 5 (the interval is the recording's start and stop). It now asks that the ends match; lying inside counts as partial.
- **`prior-task-strategies`:** the statement and quote left out the barrel cortex tuning half of the paper's sentences. Both now include it.
- **`prior-orthogonal-subspaces`:** added. This was the paper's other stated earlier finding on these data (ref. 10) and had no claim. It is blocked because the paper gives no method for it.

**Still open (recorded in `checks`):**
- The abstract says the neurons "responded with precise timing to whisker contacts and motion". Nothing in the main text or legends states or measures this, so it has no claim.
- Several pass/fail thresholds were chosen by the first agent, not taken from the paper (for example 99%/95% agreement, "more than half the sessions or mice", within 1% of 30 kHz, and the sex-ratio readings). Each criterion says the paper gives no threshold, and I kept them.
- The three tracking-accuracy claims need the hand-labelled training frames and the network's held-out predictions. The paper does not list these among the deposits, so those claims will probably be blocked.

**Ready:** `ready: true`. Only that one file changed, and nothing was committed.

## End of run

17 turns, 3 minutes, result: success.
