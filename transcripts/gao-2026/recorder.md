# 001683 · recorder · run 41681697815

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 001683; ls claims/001683 transcripts/001683; cat attempts/001683-gao-2026-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));import sys;print([x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '001683' in json.dumps(x)])"
```

```
<persisted-output>
Output too large (242KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e39a7acc-d567-487b-bc47-a5327728cd12/tool-results/bpiak7pf4.txt

Preview (first 2KB):
docs/pilot-notes/001687-xiao-2026-01.md
docs/pilot-notes/001746-liu-2026-01.md
docs/pilot-notes/001676-skromne-carrasco-2026-01.md
docs/pilot-notes/001702-chaunsali-2025-01.md
docs/pilot-notes/001605-funamizu-2016-01.md
| [001683](https://dandiarchive.org/dandiset/001683) | [Gao et al. 2026](https://doi.org/10.1109/tnsre.2025.3644273) | 7 | 5 | 8 | 2 | [`001683-gao-2026`](entries/001683-gao-2026) |
claims/001683:
10.1109-tnsre.2025.3644273.yaml

transcripts/001683:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in $(git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5) docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done; cat attempts/001683-gao-2026-01.yaml; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any(str(v)=='001683' for v in x.values()): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
```

```
<persisted-output>
Output too large (99KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e39a7acc-d567-487b-bc47-a5327728cd12/tool-results/bsb4jlf5s.txt

Preview (first 2KB):
=== docs/pilot-notes/001687-xiao-2026-01.md
# 001687, Xiao et al. 2026

Twelve claims reproduced, three partially, three not reproduced and 22 blocked,
16 for missing data and six for insufficient metadata; no outcome rests on an
assumption. Of the 41 claims, 40 are on the dandiset and one,
`fig6-model-telc-loses-map`, runs the paper's PrV circuit model from its code
repository and is counted apart: reproduced. The first verification round agreed
with 38 of the 41 outcomes as they stood and the second with all 41, and nothing
was proposed after the second, so there was no third round. It pins version
0.260821.2126, the latest published version; the paper cites none, and it holds
the same 191 assets as 0.260805.1529. The paper, Xiao, Severson et al.,
"Peri-head distance coding in the mouse brainstem" in Neuron, records units in
PrV of awake head-fixed mice while a wall passes the face at distances of 7 to
23 mm, and reports the proximity and map units of wild-type silicon-probe
recordings (Fig. 2, Figure S4), the decoding of wall distance from them (Fig. 3,
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e39a7acc-d567-487b-bc47-a5327728cd12/tool-results/bsb4jlf5s.txt"
}
```

```
1	=== docs/pilot-notes/001687-xiao-2026-01.md
2	# 001687, Xiao et al. 2026
3	
4	Twelve claims reproduced, three partially, three not reproduced and 22 blocked,
5	16 for missing data and six for insufficient metadata; no outcome rests on an
6	assumption. Of the 41 claims, 40 are on the dandiset and one,
7	`fig6-model-telc-loses-map`, runs the paper's PrV circuit model from its code
8	repository and is counted apart: reproduced. The first verification round agreed
9	with 38 of the 41 outcomes as they stood and the second with all 41, and nothing
10	was proposed after the second, so there was no third round. It pins version
11	0.260821.2126, the latest published version; the paper cites none, and it holds
12	the same 191 assets as 0.260805.1529. The paper, Xiao, Severson et al.,
13	"Peri-head distance coding in the mouse brainstem" in Neuron, records units in
14	PrV of awake head-fixed mice while a wall passes the face at distances of 7 to
15	23 mm, and reports the proximity and map units of wild-type silicon-probe
16	recordings (Fig. 2, Figure S4), the decoding of wall distance from them (Fig. 3,
17	Figure S5), the effect of cutting all but one whisker (Fig. 4), SpVi-TeLC mice
18	(Fig. 5, Fig. 6, Figure S6), GtACR optogenetics (Figure S6), tungsten recordings
19	(Figure S2), whisker kinematics from video (Figure S1) and a circuit model (Fig.
20	6). The claims were written from the accepted author manuscript in PubMed
[... 781 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e39a7acc-d567-487b-bc47-a5327728cd12/tool-results/bsb4jlf5s.txt",
 "offset": 802,
 "limit": 700
}
```

```
802	    corrects each set of multiple comparisons it is asked for on its own; the paper names no family. Reading
803	    (ii) is shown. Under reading (ii) the claim would be reproduced.
804	- claim: fig3b-percent-time-sham-vs-tfus
805	  outcome: not_reproduced
806	  notebook: seizure_metrics.ipynb
807	  output: claim:fig3b-percent-time-sham-vs-tfus
808	  notes: tFUS is lower than sham in all three named comparisons (by 11.4, 9.8 and 10.0 percentage points),
809	    but none is significant. Contralateral post 1 p = 0.075 (ordinary) and 0.097 (repeated), ipsilateral
810	    stimulation 0.14 and 0.16, ipsilateral post 1 0.13 and 0.15, between family; larger over all ten comparisons.
811	- claim: fig3c-interval-increase
812	  outcome: reproduced
813	  assumed: true
814	  notebook: seizure_metrics.ipynb
815	  output: claim:fig3c-interval-increase
816	  measured:
817	  - 27.4
818	  - 49.1
819	  - 27.8
820	  - 30.1
821	  - 51.9
[... 674 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001683; wc -c *-report.md ../../claims/001683/*; cat author-report.md
```

```
868 answer-report.md
 2247 author-answers-report.md
 5528 author-report.md
 4089 author-revise-1-report.md
 3458 author-revise-2-report.md
 2847 claims-check-report.md
 3606 claims-report.md
10581 verifier-1-report.md
 6083 verifier-2-report.md
37638 ../../claims/001683/10.1109-tnsre.2025.3644273.yaml
76945 total
I've done Author steps 1 to 6 on DANDI:001683, version 0.260109.2104. That is the only published version and the paper cites none, so I pinned it. The entry is `entries/001683-gao-2026/`: three notebooks and a helper, `tfus.py`. The record is `attempts/001683-gao-2026-01.yaml`. `entry.py check` reports 0 errors, `entry.py all` passes, and the handover is in `executed/001683-gao-2026/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2c-sham-duration-stable | not reproduced |
| fig2d-seizures-under-two-minutes | reproduced |
| fig2e-sham-count-stable | reproduced |
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001683; for f in author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-answers-report.md
There were no questions to answer, so no claim, notebook, conclusion or attempt record changed.

**Questions:** none. `questions/001683.yaml` does not exist and never has on any branch. My first author run asked a reader nothing. The reader's answer run (`transcripts/001683/answer-report.md`) found no questions and changed nothing. The claims file `claims/001683/10.1109-tnsre.2025.3644273.yaml` is the same as at my author run (`git diff caedd83398 HEAD` touches only the answer transcripts).

The attempt record does have three "Question for the authors" findings: which ANOVA type and Bonferroni families, which channels and sham onsets for Fig. 5B, and which segment and normalization for band power and AI. These are open method details for the paper's authors. None of them says the claims file misreads the paper, so no reader had to answer them and they stay as findings.

**Outcomes per claim:** all unchanged.
- **Reproduced (6):** fig2d, fig2e, fig2f (assumed), fig3a-count-reduction, fig3a-count-sham-vs-tfus, fig3b-percent-time-reduction, fig3c-interval-increase (assumed), fig3c-interval-sham-vs-tfus. That is eight claims, counting the two marked assumed.
- **Not reproduced:** fig2c, fig3b-sham-percent-time-no-change (assumed), fig3b-percent-time-sham-vs-tfus, fig3d, fig4-no-theta-alpha-gamma-power-change (assumed), figs4-sham-power-no-change (assumed), fig5ghi.
- **Partially reproduced:** fig4c, fig4ef, fig6.
- **Blocked:** figs5 (data_missing), figs7 (data_missing), fig5b (methods_underspecified), fig5cdj (data_missing).

**Entry runs:**
- `lock` rewrote the lock file with the same contents.
- `all` reported 0 check errors, and all three notebooks passed from a clean environment: `seizure_metrics` in 61 s, `eeg_blocks` in 849 s and `wild_type` in 438 s.
- I spot-checked a few numbers quoted in the record (for example F = 30.45, p = 0.0028 and p = 0.013), and they still appear in the executed outputs.
- `handover` wrote `executed/001683-
[... 157 more lines not kept]
```

**Agent**

I've read the attempt record and every report. Next, the claims file, for the paper details and the check log.

**Agent calls Bash**

```bash
cd  head -c 9000 claims/001683/*.yaml; echo; grep -n -i -E "check|change|open|source|pdf|supplement|code|version of record|author" claims/001683/*.yaml | head -80
```

```
# Claims for Gao, Frake, Durand and He (2026), "Transcranial Focused Ultrasound Stimulation
# Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy", IEEE Trans Neural Syst
# Rehabil Eng 34, doi:10.1109/tnsre.2025.3644273, on dandiset 001683 (same title on the archive;
# its description says the dataset is described in this paper).
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the NIH author manuscript (PMC12848950) as served by Europe PMC, stored under paper/:
# abstract, Introduction, Methods, Results, Discussion, Data Availability and the legends of Figs. 1
# to 6; and the supplement (supp1-3644273.pdf, 8 pages: ex-vivo scanning, target confirmation, Figs.
# S1 to S7). There is no PDF of the main paper, so values and significance marks drawn only inside
# Figs. 2 to 6 were not read; Figs. S4, S5 and S7 were viewed in the supplement PDF. The paper links
# no code; the only repository it names is the dandiset. No code was read.
#
# Data the paper used, as it reports them (Methods A to E, supplement):
#  - Rats. 16 adult male Sprague-Dawley rats in the epilepsy study, 10 tFUS (experimental) and 6
#    sham; 7 more in a mechanism study, 23 in all. The wild-type analysis (Fig. 5) uses all 23
#    (Fig. 5B, N = 23 per group). Isoflurane anesthesia throughout.
#  - Recordings. A 32-channel skull EEG probe (NeuroNexus HC32), aligned with bregma, and a
#    64-channel intracranial array in left S1 (AP -2, ML -2.5, DV -1.5 mm). Tucker-Davis system at
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 556,600p claims/001683/*.yaml
```

```
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2f-sham-percent-time-post3, criterion. Dropped the condition that post 3 is lower; the paper
    says only "significantly different", so the direction is reported and does not decide.
  - fig4-no-theta-alpha-gamma-power-change, criterion. Limited the absence to within-group
    comparisons against baseline; the Fig. 4 legend marks those apart from between-group
    differences and the sentence speaks of changes. Sham against tFUS is reported only.
  - fig5b-tfus-evoked-potentials, criterion. Replaced the made-up per-time-point paired t-test
    readings with the test of Methods F (two-way ANOVA, group by time point, Bonferroni post hoc,
    ordinary or repeated measures); named the pre-onset normalization as a standard baseline
    subtraction; changed "a run of significant time points" to at least one time point.
  - fig5cdj-wild-type-gamma-pli-decrease, statistics and criterion. Removed the tFUS against sham
    p < 0.05 entry for Fig. 5J and its use in the criterion; no sentence states significance and
    the header says the marks of Figs. 2 to 6 were not read, so the entry was not from the paper.
  - figs7-seizure-pli-s1-vs-non-s1, statement. The paper's sentence is hedged ("may reflect") and
    about wild-type against seizure rats; reworded to say that. Criterion now cites the Fig. S7A
[... 9 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001683-gao-2026-01.md",
 "content": "# 001683, Gao et al. 2026\n\nSeven claims reproduced (three on an assumption), five partially (two on an\nassumption), eight not reproduced (four on an assumption) and two blocked, one\nas methods underspecified and one for missing data. All 22 claims are on the\ndandiset. The first verification round agreed with 19 of the 22 outcomes as\nthey stood and the second with all 22, and nothing was proposed after the\nsecond, so there was no third round. It pins version 0.260109.2104, the only\npublished version; the paper cites none. The paper, Gao, Frake, Durand and He,\n\"Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits\nSeizures in a Rat Model of Epilepsy\" in IEEE Transactions on Neural Systems and\nRehabilitation Engineering, applies tFUS to the corpus callosum of rats with\nseizures induced by 4-AP in right S1, 10 tFUS and 6 sham, and reports the\nseizure metrics of the sham group (Fig. 2) and of both groups (Fig. 3), band\npower and the asymmetry index (AI) of the EEG (Fig. 4, Figures S4 and S5), the\nevoked potentials and phase lag index (PLI) of all 23 rats before 4-AP (Fig.\n5) and the PLI of the epileptic rats (Fig. 6, Figure S7). The claims were\nwritten from the NIH author manuscript in Europe PMC (PMC12848950) and its\nsupplement, without a PDF of the main paper, so the significance marks inside\nFigs. 2 to 6 were not read; the paper links no code. The check made five\nchanges and left three points open. Reproduced are\n`fig2d-seizures-under-two-minutes` (99.4% of 527 ipsilateral and 99.2% of 521\ncontralateral sham seizures under 120 s), `fig2e-sham-count-stable`,\n`fig2f-sham-percent-time-post3` (Bonferroni p = 0.040 in its family, 0.051 over\nall 25 comparisons, on three assumptions: BH635's files in time order, the\nrepeated-measures reading of the ANOVA and one family per set of comparisons),\n`fig3a-count-reduction` (8.7, 36.4, 41.9 and 10.5, 41.4, 42.4%),\n`fig3b-percent-time-reduction`, `fig3c-interval-increase`, on the interval read\nas the gap from one seizure's end to the next one's start, which gives the\npaper's six percentages to within 0.4 point, and `figs5-seizures-lower-ai`,\nwhich rests on AI computed on band power and on a pre-4-AP state taken from the\ngaps between the pulses of the PLV recordings. Partial are\n`fig3a-count-sham-vs-tfus` (post 1 only), `fig3c-interval-sham-vs-tfus`\n(contralateral only), `fig4c-beta-decrease` (post 1 but not the condition\nblock), `fig4ef-ai-increase`, which on band ratios would be not reproduced, and\n`figs7-seizure-pli-s1-vs-non-s1` (theta, and gamma under one reading). Not\nreproduced are `fig2c-sham-duration-stable` (mean durations fall from 49.6 to\n53.0 s at baseline to 34.8 to 35.7 s at post 3, block p = 0.00145 and 0.00037\nper rat), `fig3b-percent-time-sham-vs-tfus`, `fig3d-duration-decline`,\n`fig6-epileptic-pli-s1-decrease`, where the non-S1 PLI falls too, and\n`fig5ghi-low-band-pli-s1-only`, which rests on the PLV recordings standing for\nthe target-confirmation EEG and would otherwise be blocked; the three claims of\nabsence `fig3b-sham-percent-time-no-change`,\n`fig4-no-theta-alpha-gamma-power-change` and `figs4-sham-power-no-change` rest\non taking the repeated-measures reading as the paper's test, and under the\nordinary reading the first two would be reproduced and the third blocked.\n`fig5b-tfus-evoked-potentials` is blocked as methods underspecified, as 2 of 18\ncombinations of position, sham onsets and ANOVA find significant time points,\nand `fig5cdj-wild-type-gamma-pli-decrease` for missing data. The author's first\nrun gave 8 reproduced, 3 partially, 7 not reproduced and 4 blocked. The author\nasked no questions of a reader, so the answer and author-answers runs changed\nnothing. Round 1 disagreed with three outcomes and found that the\nrepeated-measures post hoc tests used a normal reference, that the per-trial\nPLI was biased by window length, so that the decrease in 100% of pairs was\nbias, that the EP intervals were not checked against the burst onsets, that\npre-4-AP EEG exists for 13 of the 16 epileptic rats, that AI on band ratios was\ncomputed and never tested, and that an increase under division was read with\nthe wrong sign; in reply t and F tests on Satterthwaite degrees of freedom,\nnine 20 ms sub-windows with trial-shuffled noise floors, an alignment check,\nthe pre-4-AP analyses and the ratio tests were added, and five outcomes changed,\nthree to the verifier's, `figs5` from blocked to reproduced and `figs7` from\nblocked to partially reproduced. Round 2 agreed with all 22, found the\nassumption flag missing on `fig4ef` and `fig5ghi`, and found sentences the\noutputs did not support (that the paper's within-group changes appear only\nunder the repeated-measures reading, six cut-off seizures where the variant\nleaves out 14 against 6, 16 epileptic rats with a PLV recording where 13 have\none, 0.70 for 0.6976, the scale of the raw EEG and the run times); in reply the\nflags were added, a question on which recordings the wild-type PLI used was\nadded to the findings and the text was corrected, and nothing was filed in\n`questions/001683.yaml`. The author's run took about 1 h 40 min (08:14 to 09:56\nUTC); the notebooks ran in 1, 13.5 and 7.7 min at first, 61, 849 and 438 s\nafter the author-answers run, 61 s, 26 min and 12 min after round 1, whose\nfirst full run failed on a transient network error that a retry in the\nhelper's range reads fixed, and the last two in 19.1 and 11.7 min at the end,\nwhile the eeg_blocks header still says about 22 minutes. Untracked files in\nthe working tree (`.bashrc`, `.idea`, `scripts` and others) were left alone.\n\nThe seizure label table of all 70 labelled EEG blocks gives its times in\nminutes, while NWB prescribes seconds (the stops reach 62.7 in blocks of 3750\ns); read as minutes the labels match the EEG, with 30 to 80 Hz power 2.5 to 50\ntimes higher inside them in all 136 block-hemispheres. The EEG of the resting\nbaseline of the target confirmation, the sham of Figs. 5E-F, is not in the\ndandiset, whose resting recordings hold only the intracranial LFP, and the\nfirst monitoring block after the first injection was not deposited. The EEG\nbefore the first 4-AP injection is there only as the PLV recordings, which\ncarry tFUS pulses, end 64 to 176 min before the baseline block and are not\ndescribed as pre-4-AP recordings; 13 of the 16 epileptic rats have one, and\nPLV files exist for 20 of the 23 wild-type rats (not BH638, BH642, BH644),\nwhile Fig. 5 gives N = 23. The five block files of sham rat BH635 are labelled\nBASELINE, SHAM, SHAM, BH636_post1 and BH635_post2, with no post3, and BH649's\npost 3 file has the session id None in its path. Every file gives the subject\nas \"HSD:WI rat\" of age P24W, while the paper used Sprague-Dawley rats of 3 to 6\nmonths. The ElectricalSeries of the EP files is described as \"EEG data\" though\nit holds the 64 intracranial channels of left S1, and the PLV files are\nlabelled 1Hz but 19 of 20 carry their pulses every 2 s. The files do not say\nwhich EEG channels were used to label the seizures (8 and 25 were read from the\ndrawing of Fig. S1), which channels cover S1 (given only in the notes of the\nPLV files) or which transducer position was chosen, so the tFUS EPs of Fig. 5B\ncannot be selected. The baseline AI of the labelling channels on band power is\nstrongly negative (sham -0.58 to -0.61, tFUS -0.24 to -0.29, and -0.17 to\n-0.26 before 4-AP), so the contralateral channel carries 1.7 to 4 times the\nipsilateral power, while on band ratios the AI is near 0. The target-confirmation\nLFP shows no clear evoked potential at any lag of the 2 s cycle (mean RMS 5.2\nuV from 0 to 200 ms against 6.8 uV later), although 1.4-1.5 kHz power marks the\nbursts at the interval starts in 13 of 23 CENTER recordings. Of the paper\nitself, Methods E gives the wild-type tFUS window as \"20 ms of stimulation\" of\nthe target confirmation, whose bursts last 67 ms. Questions are put to the\npaper's authors: whether the two-way ANOVA was ordinary or repeated measures and\nwhich comparisons formed each Bonferroni family; which channels, recording,\nsham onsets and time resolution were tested for Fig. 5B; over which segment\nband power, AI and seizure PLI were computed, what total the band power was\ndivided by, whether Eq. 1 was applied to band power or band ratio and how AI\nwas normalized; and whether the wild-type PLI was computed on the\ntarget-confirmation bursts or on the recordings labelled for PLV analysis.\n\nThe author's points on the protocol: a criterion's partial clause can be too\ngenerous, as fig6's made it partially reproduced though the non-S1 condition\nfails, and it was applied literally; neither the protocol nor the criteria say\nwhat to do with a blocked claim that has a testable part, so the testable\npart's numbers went into the notes; the absence rule refers to \"the paper's\ntest\" while the claims file leaves that test open, so one ANOVA reading was\nadopted by step 1.6 and used throughout; there is no single Bonferroni family\nfor all claims, so claims of one figure pass under different families; the PLV\nfiles fit the Methods better than the claims file's reading of the data, and\nthey were used as a deviation without asking a reader; and `entry.py` cannot\nrun a single notebook, so a one-line fix cost a full 22-minute rerun.\n"
}
```

```
File created successfully at: docs/pilot-notes/001683-gao-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n -E "—|rather|\*\*" docs/pilot-notes/001683-gao-2026-01.md; git status --short
```

```
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
?? docs/pilot-notes/001683-gao-2026-01.md
?? scripts
```

**Agent**

I wrote the notes in `docs/pilot-notes/001683-gao-2026-01.md`, which is the only file I added or changed; nothing is committed. The note has no em dashes, no "rather" and no bold. The untracked dotfiles and `scripts` in the checkout were there before and I left them alone. The dataset's `catalystneuro` field is empty, so the second paragraph does not open with the CatalystNeuro sentence.

# 001683, Gao et al. 2026

Seven claims reproduced (three on an assumption), five partially (two on an assumption), eight not reproduced (four on an assumption) and two blocked, one as methods underspecified and one for missing data. All 22 claims are on the dandiset. The first verification round agreed with 19 of the 22 outcomes as they stood and the second with all 22, and nothing was proposed after the second, so there was no third round. It pins version 0.260109.2104, the only published version; the paper cites none. The paper, Gao, Frake, Durand and He, "Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy" in IEEE Transactions on Neural Systems and Rehabilitation Engineering, applies tFUS to the corpus callosum of rats with seizures induced by 4-AP in right S1, 10 tFUS and 6 sham, and reports the seizure metrics of the sham group (Fig. 2) and of both groups (Fig. 3), band power and the asymmetry index (AI) of the EEG (Fig. 4, Figures S4 and S5), the evoked potentials and phase lag index (PLI) of all 23 rats before 4-AP (Fig. 5) and the PLI of the epileptic rats (Fig. 6, Figure S7). The claims were written from the NIH author manuscript in Europe PMC (PMC12848950) and its supplement, without a PDF of the main paper, so the significance marks inside Figs. 2 to 6 were not read; the paper links no code. The check made five changes and left three points open. Reproduced are `fig2d-seizures-under-two-minutes` (99.4% of 527 ipsilateral and 99.2% of 521 contralateral sham seizures under 120 s), `fig2e-sham-count-stable`, `fig2f-sham-percent-time-post3` (Bonferroni p = 0.040 in its family, 0.051 over all 25 comparisons, on three assumptions: BH635's files in time order, the repeated-measures reading of the ANOVA and one family per set of comparisons), `fig3a-count-reduction` (8.7, 36.4, 41.9 and 10.5, 41.4, 42.4%), `fig3b-percent-time-reduction`, `fig3c-interval-increase`, on the interval read as the gap from one seizure's end to the next one's start, which gives the paper's six percentages to within 0.4 point, and `figs5-seizures-lower-ai`, which rests on AI computed on band power and on a pre-4-AP state taken from the gaps between the pulses of the PLV recordings. Partial are `fig3a-count-sham-vs-tfus` (post 1 only), `fig3c-interval-sham-vs-tfus` (contralateral only), `fig4c-beta-decrease` (post 1 but not the condition block), `fig4ef-ai-increase`, which on band ratios would be not reproduced, and `figs7-seizure-pli-s1-vs-non-s1` (theta, and gamma under one reading). Not reproduced are `fig2c-sham-duration-stable` (mean durations fall from 49.6 to 53.0 s at baseline to 34.8 to 35.7 s at post 3, block p = 0.00145 and 0.00037 per rat), `fig3b-percent-time-sham-vs-tfus`, `fig3d-duration-decline`, `fig6-epileptic-pli-s1-decrease`, where the non-S1 PLI falls too, and `fig5ghi-low-band-pli-s1-only`, which rests on the PLV recordings standing for the target-confirmation EEG and would otherwise be blocked; the three claims of absence `fig3b-sham-percent-time-no-change`, `fig4-no-theta-alpha-gamma-power-change` and `figs4-sham-power-no-change` rest on taking the repeated-measures reading as the paper's test, and under the ordinary reading the first two would be reproduced and the third blocked. `fig5b-tfus-evoked-potentials` is blocked as methods underspecified, as 2 of 18 combinations of position, sham onsets and ANOVA find significant time points, and `fig5cdj-wild-type-gamma-pli-decrease` for missing data. The author's first run gave 8 reproduced, 3 partially, 7 not reproduced and 4 blocked. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 disagreed with three outcomes and found that the repeated-measures post hoc tests used a normal reference, that the per-trial PLI was biased by window length, so that the decrease in 100% of pairs was bias, that the EP intervals were not checked against the burst onsets, that pre-4-AP EEG exists for 13 of the 16 epileptic rats, that AI on band ratios was computed and never tested, and that an increase under division was read with the wrong sign; in reply t and F tests on Satterthwaite degrees of freedom, nine 20 ms sub-windows with trial-shuffled noise floors, an alignment check, the pre-4-AP analyses and the ratio tests were added, and five outcomes changed, three to the verifier's, `figs5` from blocked to reproduced and `figs7` from blocked to partially reproduced. Round 2 agreed with all 22, found the assumption flag missing on `fig4ef` and `fig5ghi`, and found sentences the outputs did not support (that the paper's within-group changes appear only under the repeated-measures reading, six cut-off seizures where the variant leaves out 14 against 6, 16 epileptic rats with a PLV recording where 13 have one, 0.70 for 0.6976, the scale of the raw EEG and the run times); in reply the flags were added, a question on which recordings the wild-type PLI used was added to the findings and the text was corrected, and nothing was filed in `questions/001683.yaml`. The author's run took about 1 h 40 min (08:14 to 09:56 UTC); the notebooks ran in 1, 13.5 and 7.7 min at first, 61, 849 and 438 s after the author-answers run, 61 s, 26 min and 12 min after round 1, whose first full run failed on a transient network error that a retry in the helper's range reads fixed, and the last two in 19.1 and 11.7 min at the end, while the eeg_blocks header still says about 22 minutes. Untracked files in the working tree (`.bashrc`, `.idea`, `scripts` and others) were left alone.

The seizure label table of all 70 labelled EEG blocks gives its times in minutes, while NWB prescribes seconds (the stops reach 62.7 in blocks of 3750 s); read as minutes the labels match the EEG, with 30 to 80 Hz power 2.5 to 50 times higher inside them in all 136 block-hemispheres. The EEG of the resting baseline of the target confirmation, the sham of Figs. 5E-F, is not in the dandiset, whose resting recordings hold only the intracranial LFP, and the first monitoring block after the first injection was not deposited. The EEG before the first 4-AP injection is there only as the PLV recordings, which carry tFUS pulses, end 64 to 176 min before the baseline block and are not described as pre-4-AP recordings; 13 of the 16 epileptic rats have one, and PLV files exist for 20 of the 23 wild-type rats (not BH638, BH642, BH644), while Fig. 5 gives N = 23. The five block files of sham rat BH635 are labelled BASELINE, SHAM, SHAM, BH636_post1 and BH635_post2, with no post3, and BH649's post 3 file has the session id None in its path. Every file gives the subject as "HSD:WI rat" of age P24W, while the paper used Sprague-Dawley rats of 3 to 6 months. The ElectricalSeries of the EP files is described as "EEG data" though it holds the 64 intracranial channels of left S1, and the PLV files are labelled 1Hz but 19 of 20 carry their pulses every 2 s. The files do not say which EEG channels were used to label the seizures (8 and 25 were read from the drawing of Fig. S1), which channels cover S1 (given only in the notes of the PLV files) or which transducer position was chosen, so the tFUS EPs of Fig. 5B cannot be selected. The baseline AI of the labelling channels on band power is strongly negative (sham -0.58 to -0.61, tFUS -0.24 to -0.29, and -0.17 to -0.26 before 4-AP), so the contralateral channel carries 1.7 to 4 times the ipsilateral power, while on band ratios the AI is near 0. The target-confirmation LFP shows no clear evoked potential at any lag of the 2 s cycle (mean RMS 5.2 uV from 0 to 200 ms against 6.8 uV later), although 1.4-1.5 kHz power marks the bursts at the interval starts in 13 of 23 CENTER recordings. Of the paper itself, Methods E gives the wild-type tFUS window as "20 ms of stimulation" of the target confirmation, whose bursts last 67 ms. Questions are put to the paper's authors: whether the two-way ANOVA was ordinary or repeated measures and which comparisons formed each Bonferroni family; which channels, recording, sham onsets and time resolution were tested for Fig. 5B; over which segment band power, AI and seizure PLI were computed, what total the band power was divided by, whether Eq. 1 was applied to band power or band ratio and how AI was normalized; and whether the wild-type PLI was computed on the target-confirmation bursts or on the recordings labelled for PLV analysis.

The author's points on the protocol: a criterion's partial clause can be too generous, as fig6's made it partially reproduced though the non-S1 condition fails, and it was applied literally; neither the protocol nor the criteria say what to do with a blocked claim that has a testable part, so the testable part's numbers went into the notes; the absence rule refers to "the paper's test" while the claims file leaves that test open, so one ANOVA reading was adopted by step 1.6 and used throughout; there is no single Bonferroni family for all claims, so claims of one figure pass under different families; the PLV files fit the Methods better than the claims file's reading of the data, and they were used as a deviation without asking a reader; and `entry.py` cannot run a single notebook, so a one-line fix cost a full 22-minute rerun.

## End of run

11 turns, 2 minutes, $1.00 at API prices, result: success.
