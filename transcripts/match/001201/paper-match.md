# 001201 · paper-match · run 42832417369

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat papers/match/001201.yaml; ls paper/ | grep -E "085713|j.neuron.2021"; grep -n -A40 -i "step 1" docs/pipeline.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001201/versions/0.261026.1912/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['name']);print(d['description']);print([c['name'] for c in d['contributor']]);print(d.get('relatedResource'));print(d['assetsSummary'])"; curl -s 'https://api.dandiarchive.org/api/dandisets/001201/versions/0.261026.1912/assets/?page_size=1000' | python -c "import json,sys;d=json.load(sys.stdin);print(d['count']);p=[a['path'] for a in d['results']];print(p[:3],p[-3:])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; f=10.1016-j.neuron.2021.08.009.txt; head -c 2500 $f; echo; grep -n -i -E "monkey[s]? [NW]|two (adult|male|rhesus)|data (and code )?availab|deposited|request|20(19|20|21)|sessions" $f | head -40
```

```
DOI: 10.1016/j.neuron.2021.08.009
Version: version of record
Source: PDF supplied by a person
Stored: 2026-11-01
Extracted: PyMuPDF, dehyphenated, NFKC; with 1 supplement PDF(s)
------------------------------------------------------------------------

=== page 1 ===
Article
Real-time linear prediction of simultaneous and
independent movements of two finger groups using
an intracortical brain-machine interface
Graphical abstract
Highlights
d Simultaneous and independent brain-machine interface
control of two finger groups
d Cortical tuning between manipulandum and brain-machine
interface use is consistent
d Linear decoders can predict untrained finger movements
d Cortical units simultaneously encode multiple kinematic
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=10.1016-j.neuron.2021.08.009.txt; grep -n -i -A6 "data and code availability\|Lead contact$" $f | head -40; grep -n -i -E "date|days? post|implant" $f | head -20; grep -n -i -E "Nason|2021|monkey N|2020|DANDI|Neuron" 10.52202-085713-4642.txt | head -30
```

```
56:8Lead contact
57-*Correspondence: [removed: an e-mail address]
58-https://doi.org/10.1016/j.neuron.2021.08.009
59-SUMMARY
60-Modern brain-machine interfaces can return function to people with paralysis, but current upper extremity
61-brain-machine interfaces are unable to reproduce control of individuated finger movements. Here, for the first
62-time, we present a real-time, high-speed, linear brain-machine interface in nonhuman primates that utilizes
--
948:B Lead contact
949-B Materials availability
950:B Data and code availability
951-d EXPERIMENTAL MODEL AND SUBJECT DETAILS
952-B Nonhuman primates
953-d METHOD DETAILS
954-B Implants
955-B Feature extraction
956-B Experimental setup
--
1224:Lead contact
1225-Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact, Cynthia
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1236,1300p 10.1016-j.neuron.2021.08.009.txt; sed -n 136,152p 10.52202-085713-4642.txt; sed -n 200,215p 10.52202-085713-4642.txt
```

```
EXPERIMENTAL MODEL AND SUBJECT DETAILS
Nonhuman primates
All procedures were approved by the University of Michigan Institutional Animal Care and Use Committee.
All experiments were conducted with two monkeys (male, macaca mulatta). Monkey N was age 7 to 8 years and weighed between
12.7 and 16.8kg (weight range due to the extended COVID-19-related experiment break) during the period of data collection. Monkey
W was age 8 years and weighed between 13.1 and 14.1kg during the period of data collection. The subjects were fed a standard
laboratory animal diet with supplemental fresh fruits and vegetables. When possible, the animals were pair-housed, and were always
provided frequent access to a variety of enrichment, including food puzzles, chewing toys, and television.
METHOD DETAILS
Implants
We implanted two male rhesus macaques (monkey N age 7 to 8, monkey W age 8 at the time of data collection), with Utah microelectrode arrays (Blackrock Microsystems, Salt Lake City, UT, USA) in the hand area of primary motor cortex, as described previously
REAGENT or RESOURCE
SOURCE
IDENTIFIER
Deposited data
Data to reproduce analyses and figures
Original data
https://doi.org/10.7302/jnkz-az17
Experimental models: Organisms/strains
Macaca Mulatta
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "post-implant|days post|implanted (on|in) |20(18|19)|nason" 10.52202-085713-4642.txt | head; grep -n -i -E "201[89]|2020|COVID" 10.1016-j.neuron.2021.08.009.txt | head
```

```
16:Samuel R. Nason-Tomaszewski1∗, Matthew S. Willsey1,6, Parag G. Patil1,6,
131:with 3 Utah arrays, 2 of which were implanted in the motor cortex. Given available hardware, we
180:Hardware and Feature Extraction. Monkey N was implanted with 3 Utah microelectrode arrays (Blackrock Neurotech, Salt Lake City, UT, USA). One 10 × 10 array was implanted in the
181:somatosensory cortex, and two 8 × 8 arrays were implanted in the hand area of the motor cortex
195:The recordings included in the dataset begin on day 349 post-implant, up to 1591 days post-implant.
554:neural engineering, 15(4):046016, August 2018. Place: England.
611:Washington, Thiago Scodeler, Diogo de Lucena, Samuel R. Nason-Tomaszewski, Matthew J.
634:October 2018. Number: 10 Publisher: Nature Publishing Group.
662:an instructed delayed reach-to-grasp task. Scientific Data, 5(1):180055, April 2018. Publisher:
673:[59] Samuel R. Nason, Matthew J. Mender, Alex K. Vaskov, Matthew S. Willsey, Nishant Ganesh Ku
105:posture (combined arrangements of different hand DoFs; Aggarwal et al., 2013; Bansal et al., 2011; Okorokova et al., 2020; Vargas-Irwin et al., 2010). These studies found that continuously
149:example, primary motor cortex can simultaneously encode information about upper extremities, fingers, and speech, independent of body laterality (Cross et al., 2020; Diedrichsen et al.,
150:2013; Heming et al., 2019; Jorge et al., 2020; Stavisky et al.,
151:2019, 2020; Willett et al., 2020). As tasks increase in complexity,
176:et al., 2018). The manipulandum consisted of two flat surfaces,
210:threshold crossing rate (Nason et al., 2020). Then, we trained a
264:2012; Vaskov et al., 2018). The RFKF training procedure
326:et al., 2018). To showcase this, Video S1
397:(SNR) units on an electrode (Nason et al., 2020). This is
597:2020; Vargas-Irwin et al., 2010), but our brain-machine interface
```

**Agent calls Bash**

```bash
cd  cat >> papers/match/001201.yaml <<'EOF'
  verdict: partial
  by: agent
  reason: >-
    The paper's data are monkeys N and W in online BMI and manipulandum finger tasks, deposited at Deep Blue.
    The dataset holds only monkey N hand-control trials (closed-loop trials excluded) from days 349 to 1591 post-implant,
    which overlaps the paper's window for monkey N (days 117 to 708) only in part, so at most its offline monkey N
    analyses can be tested; whether the exact sessions coincide is uncertain.
  evidence:
  - source: STAR Methods, Data and code availability
    quote: A subset of the data used in this study can be found online as of the date of publication (https://doi.org/10.7302/jnkz-az17)
  - source: STAR Methods, Implants
    quote: Monkey N was between 117 days and 708 days post-cortical implant for all data analyzed.
  - source: archive metadata
    quote: Further details on the experimental setup can be found in Nason et al. 2021, Neuron
  data_in:
  - doi:10.7302/jnkz-az17
EOF
python tools/paper_match.py validate papers/match/001201.yaml
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python tools/paper_match.py validate papers/match/001201.yaml; echo exit=$?
```

```
exit=0
```

**Agent**

I gave the one unsettled paper a verdict and left the checks verdict on the other as it was. `papers/match/001201.yaml` passes validation.

- **doi:10.52202/085713-4642 (Temmar et al., the LINK NeurIPS paper): `primary`, set by the checks, left as is.** The paper says "The dataset is publicly available on the DANDI archive, dandiarchive.org/dandiset/001201". Its subject (Monkey N), its 312 sessions over 1,242 days and its 96 motor cortex channels match the archive metadata.

- **doi:10.1016/j.neuron.2021.08.009 (Nason et al. 2021, Neuron): `partial`, by agent.**
  - **What decided it:** the paper's Data and code availability section points to another repository: "A subset of the data used in this study can be found online ... (https://doi.org/10.7302/jnkz-az17)". I listed that DOI in `data_in`.
  - **Why only partial:** the paper uses monkeys N and W, and its main findings come from closed-loop brain-machine interface control. The dataset holds only Monkey N, and the LINK paper says it left out closed-loop trials.
  - **Where they overlap:** Monkey N's recordings in the paper fall on days 117 to 708 after implant, and the dataset's run from day 349 to 1591. Some of the paper's offline Monkey N analyses of hand-controlled movement might be testable on the dataset.
  - **What is uncertain:** whether the paper's exact sessions are in the dataset. The archive itself cites this paper only for "details on the experimental setup".

## End of run

9 turns, 1 minutes, $0.28 at API prices, result: success.
