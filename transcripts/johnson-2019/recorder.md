# crcns-fcx-3 · recorder · run 42564140922

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/crcns-fcx-3/ claims/crcns-fcx-3/; python tools/readme_row.py crcns-fcx-3; cat attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
<persisted-output>
Output too large (56.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2b426017-efd4-4c8c-9b1e-d67914478657/tool-results/b30z657zu.txt

Preview (first 2KB):
docs/pilot-notes/crcns-apl-1-bruno-2017-01.md
docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
docs/pilot-notes/crcns-hc-28-jadhav-2016-01.md
docs/pilot-notes/crcns-hc-13-yu-2017-01.md
docs/pilot-notes/crcns-vim-3-mannion-2015-01.md
claims/crcns-fcx-3/:
10.3389-fnsys.2018.00065.yaml

transcripts/crcns-fcx-3/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/crcns-fcx-3-johnson-2019-01.yaml; grep -n "^|" README.md | head -3; for f in crcns-apl-1-bruno-2017-01 crcns-ssc-10-lemessurier-2019-01 crcns-hc-28-jadhav-2016-01 crcns-hc-13-yu-2017-01 crcns-vim-3-mannion-2015-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; ls summaries | head; python -c "
import json;d=json.load(open('targets/dandisets.json'));
import sys
for e in (d if isinstance(d,list) else d.values()):
  if 'fcx-3' in json.dumps(e): print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (97KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2b426017-efd4-4c8c-9b1e-d67914478657/tool-results/b48nf5yyc.txt

Preview (first 2KB):
schema_version: 2
id: crcns-fcx-3-johnson-2019-01
dataset:
  archive: crcns
  id: fcx-3
  version: unversioned
  doi: 10.6080/K06971S9
paper: doi:10.3389/fnsys.2018.00065
date: 2026-11-08
entry: crcns-fcx-3-johnson-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 40 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2b426017-efd4-4c8c-9b1e-d67914478657/tool-results/b48nf5yyc.txt"
}
```

```
1	schema_version: 2
2	id: crcns-fcx-3-johnson-2019-01
3	dataset:
4	  archive: crcns
5	  id: fcx-3
6	  version: unversioned
7	  doi: 10.6080/K06971S9
8	paper: doi:10.3389/fnsys.2018.00065
9	date: 2026-11-08
10	entry: crcns-fcx-3-johnson-2019
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 772 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2b426017-efd4-4c8c-9b1e-d67914478657/tool-results/b48nf5yyc.txt",
 "offset": 792,
 "limit": 651
}
```

```
792	  - claim: fig5b-alpha-beta-no-sustained
793	    agrees: true
794	    outcome: reproduced
795	    reason: Yes, by the letter. The significant points come only from reading (b)'s pair-level test (30
796	      and 35 points, smallest p 2e-18). The 74 pairs it selects are about the number the
797	      trial-shuffled data select (71), and S3 supplies 44 of them, all treated as independent. No
798	      subject-level test is shown. Under reading (a) the outcome is partial.
799	    response: Outcome kept as round 2 does not allow a change, and partially_reproduced proposed for
800	      a third round under reading (a), now adopted, which finds no FDR-significant point. A paired test
801	      on subject means at each time point is now printed; under reading (b) it finds no point after
802	      FDR either (smallest p 0.0029 and 0.0078).
803	- date: '2026-11-09'
804	  kind: agent
805	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
806	  reviewed: Round 3. The three proposed changes of outcome (fig4c-alpha-beta-shift,
807	    fig5a-spatiotemporal-bidirectional, fig5b-alpha-beta-no-sustained) and the analysis behind them in
808	    the re-executed notebook of the second revision (commit 5d5c03884d), without downloading the data
809	    or re-running. It agreed with all three, found the switch to PSI reading (a) supported by the
810	    calibration outputs and not steered by the outcomes (it lowers two and raises one), asked that
811	    assumed stay on all three, and found no new place where the claims file misreads the paper.
[... 631 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "fcx-3" -A12 targets/dandisets.json | head -40; grep -n "| Dataset\|^| ---" README.md | head; ls -la transcripts/crcns-fcx-3/; wc -l transcripts/crcns-fcx-3/*-report.md claims/crcns-fcx-3/*; cat summaries/crcns-hc-13-yu-2017-01.md summaries/crcns-apl-1-bruno-2017-01.md
```

```
total 904
drwxr-xr-x   2 runner runner   4096 Nov  9 04:53 .
drwxr-xr-x 268 runner runner  12288 Nov  9 04:53 ..
-rw-r--r--   1 runner runner   1117 Nov  9 04:53 answer-report.md
-rw-r--r--   1 runner runner   5211 Nov  9 04:53 answer.md
-rw-r--r--   1 runner runner   2862 Nov  9 04:53 author-answers-report.md
-rw-r--r--   1 runner runner  10472 Nov  9 04:53 author-answers.md
-rw-r--r--   1 runner runner   4627 Nov  9 04:53 author-report.md
-rw-r--r--   1 runner runner   4078 Nov  9 04:53 author-revise-1-report.md
-rw-r--r--   1 runner runner 189665 Nov  9 04:53 author-revise-1.md
-rw-r--r--   1 runner runner   4380 Nov  9 04:53 author-revise-2-report.md
-rw-r--r--   1 runner runner 160157 Nov  9 04:53 author-revise-2.md
-rw-r--r--   1 runner runner   2019 Nov  9 04:53 author-revise-3-report.md
-rw-r--r--   1 runner runner  43139 Nov  9 04:53 author-revise-3.md
-rw-r--r--   1 runner runner 256679 Nov  9 04:53 author.md
-rw-r--r--   1 runner runner   3226 Nov  9 04:53 claims-check-report.md
-rw-r--r--   1 runner runner  22345 Nov  9 04:53 claims-check.md
-rw-r--r--   1 runner runner   4021 Nov  9 04:53 claims-report.md
-rw-r--r--   1 runner runner  47189 Nov  9 04:53 claims.md
-rw-r--r--   1 runner runner  10069 Nov  9 04:53 verifier-1-report.md
[... 20 more lines not kept]
```

**Agent**

Read the sample notes and the attempt record; now reading the run reports and the target entry.

**Agent calls Bash**

```bash
grep -n "fcx" targets/dandisets.json | head; head -c 600 targets/dandisets.json; echo; grep -n "Reproduced\|reproduced |" README.md | head -5; cd transcripts/crcns-fcx-3; for f in claims-report claims-check-report author-report answer-report author-answers-report author-revise-1-report verifier-1-report; do echo "=== $f"; cat $f.md; done
```

```
<persisted-output>
Output too large (30KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2b426017-efd4-4c8c-9b1e-d67914478657/tool-results/bvwwgluf9.txt

Preview (first 2KB):
{
 "schema_version": 1,
 "generated": "2026-11-05T14:39:45+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 672,
  "with_a_paper": 295,
  "with_a_published_version": 254,
  "papers": 312,
  "converted_by_catalystneuro": 51
 },
 "targets": [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-fcx-3; for f in verifier-2-report author-revise-2-report verifier-3-report author-revise-3-report; do echo "=== $f"; cat $f.md; done
```

```
/bin/bash: line 1: cd: transcripts/crcns-fcx-3: No such file or directory
=== verifier-2-report
**Verifier report, round 2: Johnson et al. 2019 on CRCNS fcx-3**

Cell numbers are 0-based positions in the executed `.ipynb`; the layout has changed since round 1. The claims file has 17 claims and the attempt record has 17 outcomes. Outside the notebook I ran one check of my own: a synthetic test of the PSI null in `$TMPDIR`, using no dataset files. It is described under fig4c.

### 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| table1-electrodes | partial | Yes. 187 channels and 1135 pairs (cell 17). |
| trial-counts | reproduced | Yes. Cell 20. |
| fig1b-accuracy | reproduced | Yes. Range 0.625–0.975; p = 0.283 (cell 23). |
| fig1b-rt-identity-slower | reproduced | Yes. p = 0.024, 0.005, 0.010 and 0.254 (cell 26). |
| erp-no-condition-difference (assumed) | not reproduced | Yes. The assumption is stated and reasonable. The outcome hardly depends on it: in the main configuration, 5 of the 6 neighbour × alpha-per-tail combinations give a cluster with p < 0.05 (or < 0.025 where that is the threshold). Only adjacent neighbours at 0.025 per tail give none (cell 29). |
| fig2-spatial-power | partial | Yes. 5 and 1 subjects, within one of the paper's counts. The percentages are off: 37.7 and 11.8 (cell 32). |
| fig3-temporal-power | partial | Yes. 5 and 2 subjects (4 and 2 with assignment b); no reading gets the percentages within tolerance (cell 32). |
| power-difficulty-subjects | reproduced | Yes. Holds under reading (b)(i) in every configuration. S3 breaks the converse (cell 37). |
| power-low-frequencies (assumed) | reproduced | Yes, by the letter. The assumption is stated and defensible, but weak: a "maximum" at the 2-Hz end of the range only means the density keeps rising below 2 Hz. Without counting that edge, the identity > other effect fails in every combination (cell 40). |
| fig4-maintenance-parietal-led | not reproduced | Yes. No subject is below −1.96
[... 138 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2b426017-efd4-4c8c-9b1e-d67914478657/tool-results/bvwwgluf9.txt"
}
```

```
1	{
2	 "schema_version": 1,
3	 "generated": "2026-11-05T14:39:45+00:00",
4	 "source": "https://api.dandiarchive.org/api",
5	 "counts": {
6	  "public_dandisets": 672,
7	  "with_a_paper": 295,
8	  "with_a_published_version": 254,
9	  "papers": 312,
10	  "converted_by_catalystneuro": 51
11	 },
12	 "targets": [
13	  {
14	   "dandiset": "000003",
15	   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
16	   "published_version": "0.260218.2052",
17	   "asset_count": 101,
18	   "size_gb": 2448.74,
19	   "data_standards": [
20	    "Neurodata Without Borders (NWB)"
[... 253 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "fcx" targets/dandisets.json; grep -n "Reproduced" README.md | head -3; head -40 claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml; grep -n "statement:" claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml | head -20
```

```
0
# Claims for Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019), Front. Syst. Neurosci. 12,
# 65, "Spectral Imprints of Working Memory for Everyday Associations in the Frontoparietal Network",
# doi:10.3389/fnsys.2018.00065, on CRCNS data set fcx-3 (doi:10.6080/K06971S9).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, PMC6333050 (open access), full text from Europe PMC JATS XML as
# supplied under paper/: Introduction, Materials and Methods, Results, Discussion, Table 1 and the
# legends of Figures 1 to 5. The paper has no supplement. No PDF was supplied, so values shown only
# inside figures (per-subject accuracy and RT of Fig. 1B, per-subject PSI of Fig. 4A and 4C, the
# time courses of Fig. 5) were not read; claims on those figures rest on the Results and legends.
# The CRCNS data descriptor was read only to know which experiments the data set holds; no claim or
# method comes from it.
#
# Code. The paper's Data Availability says its custom MATLAB code is deposited at CRCNS with the
# data. By the data descriptor it is the analysis_scripts directory of data set fcx-3 itself. It is
# one of the data set's files, which this reader does not open, so it was not read and no commit is
# recorded. Every method below is from the paper's text. Where the scripts settle a detail named as
# open below, the author may follow them (protocol, Reader step 2) and should say so.
[... 38 more lines not kept]
```

**Agent**

Writing the two files now. There is no `fcx-3` entry in `targets/dandisets.json`, so the notes leave out the CatalystNeuro sentence, as the other CRCNS notes do.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md",
 "content": "# crcns-fcx-3, Johnson et al. 2019\n\nSix claims reproduced, four partially, seven not reproduced and none blocked;\nfive outcomes rest on an assumption, `erp-no-condition-difference`,\n`power-low-frequencies`, `fig4c-alpha-beta-shift`,\n`fig5a-spatiotemporal-bidirectional` and `fig5b-alpha-beta-no-sustained`. The\nfirst verification round agreed with all 17 outcomes as they stood, the second\nagreed with 16 and disagreed on fig4c, and a third round, on the three changes\nproposed after the second (fig4c to not reproduced, fig5a-spatiotemporal to\nreproduced, fig5b to partial), agreed with all three. CRCNS does not version\ndata sets, so the version is recorded as unversioned with the data set's DOI\n(10.6080/K06971S9) and the MD5 sums in the notebook header. The paper, Johnson,\nKing-Stephens, Weber, Laxer, Lin and Knight in Frontiers in Systems\nNeuroscience (12:65), records intracranial EEG over lateral prefrontal (PFC)\nand parietal cortex in seven adults with epilepsy during a visuospatial working\nmemory task of 120 trials split between identity, spatial and temporal\nconditions, and reports that accuracy does not differ by condition while\nidentity responses are slower, that ERPs do not differ between conditions,\nthat processing-interval power differs by condition in most subjects, mostly at\nlow frequencies and in the subjects who found identity trials hardest, that\nPFC-parietal phase slope index (PSI) is parietal-led during maintenance, that\nafter the test cue delta-theta directionality shifts towards the PFC while\nalpha-beta stays parietal-led, that 1008 and 984 pairs are directional, and\nthat time-resolved delta-theta PSI separates the conditions in sustained\nepochs; the data set holds, for the 7 subjects, the filtered continuous iEEG\nwith per-trial event tables, the preprocessed bipolar epochs, channel MNI\ncoordinates and the analysis scripts. The claims were written from the version\nof record (PMC6333050) as Europe PMC JATS text with the legends of Figures 1 to\n5 but without a PDF, so per-subject values shown only in figures were not read,\nand without the MATLAB scripts, which sit among the data set's files; the claims\ncheck made nine corrections, among them a reading for electrodes in clusters of\nboth signs and the per-trial PSI reading, for 17 claims. All 17 could be\ntested. Reproduced are `trial-counts`, `fig1b-accuracy` (0.625 to 0.975, logit\nmodel p = 0.283 against the paper's p > 0.50), `fig1b-rt-identity-slower`\n(identity slower in all 7 subjects, F values below the paper's bounds),\n`power-difficulty-subjects`, `power-low-frequencies`, which holds only if the\n2-Hz end of the range counts as a local maximum, and fig5a-spatiotemporal, by\nthe letter only, as the identity trials show no direction either. Partial are\n`table1-electrodes` (187 channels and 1135 pairs against 192 and 1129),\n`fig2-spatial-power` (5 and 1 subjects, 37.7% and 11.8% of electrodes against\n54% and 36%), `fig3-temporal-power` (5 and 2 subjects, 37.4% and 21.0%) and\nfig5b. Not reproduced are the ERP claim (S2 p = 0.041 under the adopted\nneighbour reading), every PSI claim of Figures 4 and 5 except those two, among\nthem `fig4-maintenance-parietal-led` (no subject below -1.96, paper -40.03),\n`fig4a-delta-theta-shift` (no subject above 0, paper 6 subjects) and\n`directional-pairs` (78 and 104 of 1135 pairs, near the trial-shuffled\nsurrogate's 68 and 78). The author's first run had 8 reproduced, 4 partially, 5\nnot reproduced and none blocked. The author asked no questions of a reader, so\nthe answer and author-answers runs changed nothing. Round 1 held that the PSI\nnull did not compute the same statistic as the observed PSI, so no z was\ncalibrated, that the deposited code's variants without the conjugate are not a\nreading, that the cluster settings, the ERP baseline and band-pass and the power\nwindows reaching outside the 900-ms segment were unresolved, and that the\nprocessing epochs of 1150-ms trials may be misaligned; in reply the null was\nrebuilt as the Methods describe, segments were zero padded as the Methods say,\nwith the scripts' whole-epoch windows as a variant, the scripts' lines were\nprinted (they hold no cluster test), the 900-ms-delay trials were run as a\nvariant, a question on \"sustained\" went to `questions/crcns-fcx-3.yaml`, and\nerp, fig4a and directional-pairs moved to not reproduced and fig4c to partial.\nRound 2 showed with a synthetic test that per-trial PSI (reading b) is offset\ntowards negative z on independent signals, so fig4c's 6 of 7 subjects came from\nthe null, and found sentences the outputs did not support, among them the run\ntime and the ERP threshold; in reply the trial-averaged reading (a), calibrated\nat 6.0% and 6.9% on shuffled trials, was adopted where the readings differ, a\nrandom-trial control showed the loss of power effects on the 900-ms trials comes\nfrom fewer trials, and the three changes went to round 3. The author's run took\nabout 2 h 5 min (19:11 to 21:13 UTC); the notebook ran in 19 min at first, with\nabout 7 GB peak memory, 1067 s after the author-answers run, 33.5 min after\nround 1, 2448 s after round 2 and 2420 s after round 3. The first loader failed\non S4's unequal trial lengths and on S3's labels file, which is in MATLAB 5\nformat, and both were fixed; a first timing check on low-frequency signals did\nnot work and was replaced.\n\nThe deposited psianalysis.m computes the cross-spectrum without the conjugate,\nso its PSI z depends essentially on one channel's phase and changes sign with\nthe channel order (+58.67 with the PFC channel first, -55.47 with the parietal\nchannel first, delta-theta maintenance), and its null is the slope of the\ntrial-mean spectrum with both factors shuffled, not the frequency shuffle of one\nsignal the Methods describe; even with the conjugate added that null gives |z| >\n1.96 in 90% (delta-theta) and 92% (alpha-beta) of trial-shuffled pairs, and it\nalone gives the paper's directional-pair counts (1014 and 1041), as it does on\ntrial-shuffled data (1022 and 1044). psi_compute.m does not run as written, and\nits subtracterp.m selects temporal trials by the delay column, which selects\nnone. The data set's channel list holds 187 analysed channels where Table 1\ngives 192, as S4 has 5 right parietal channels where Table 1 gives 10, and the\nlist yields 1135 same-hemisphere pairs where the paper reports 1129 and Table\n1's counts would give 1165. The description says summary_file_trial.csv holds\n120 trials per subject, but for S6 and S7 it holds only the kept trials (101 and\n90 rows), so single-trial accuracy over all 120 cannot be rebuilt for them. In\nS2, S3 and S4 the processing-epoch responses of 1150-ms trials come 0.21 to 0.26\ns later relative to the processing column than in 900-ms trials, consistent with\nthat column lying about 0.25 s before the event in those trials, which the test\ndoes not prove. The electrode position files do not say how contact numbers map\nto grid positions, S3's labels (RH1 to RH256) do not match its grid's name, and\nthe reference contact of each bipolar channel was found only from the data. S7's\nderived epochs record 431506 samples where its data_primary.mat has 445952,\nthough the traces still match, and S3's elec_labels.mat is a MATLAB 5 file, the\nothers MATLAB 7.3. Questions are put to the paper's authors: which electrodes\nwere neighbours in the cluster tests and whether clusters were judged at 0.05 or\n0.025 per tail, and whether PSI came from trial-averaged or per-trial\ncross-spectra, with which channel first and with which null.\n\nThe author's points on the protocol: the analysis scripts sit among the data\nset's files, so the reader never read them and it is unclear whether they count\nas an outside input, and details were taken from them by file name; the order\n\"Methods, then code\" does not say what to do when the code is also buggy, so the\nMethods' readings were run with the conjugate fixed and the deposited code as a\nvariant; absence is judged on the paper's test alone, which is itself\nunderspecified here, so one reading was adopted as an assumption; the decoding\nsuggestion for the clock check does not fit pre-epoched data, so the derived\nepochs were matched to the continuous data and a delay contrast on\nhigh-frequency amplitude was added; and tar.gz files cannot be opened in place\nas `docs/archives.md` describes for zip, so each was streamed in order.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/crcns-fcx-3-johnson-2019-01.md",
 "content": "In this intracranial dataset the paper's behavioural results held up: identity trials were slower than spatial and temporal ones, and accuracy did not differ by condition. Its per-subject power differences after the test cue held in part, with similar subject counts but smaller shares of electrodes, and sat at low frequencies. The frontoparietal phase-slope findings did not reproduce: with the null the Methods describe, 78 of 1135 pairs were directional in delta-theta, about what trial-shuffled data give, and the paper's counts appear only with the deposited code's null, which flags shuffled data as well. The absence of ERP differences failed in one subject, under a neighbour rule the paper does not state.\n"
}
```

```
File created successfully at: summaries/crcns-fcx-3-johnson-2019-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
wc -w summaries/crcns-fcx-3-johnson-2019-01.md; grep -nE "—|rather|\*\*" summaries/crcns-fcx-3-johnson-2019-01.md docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md; git status --short
```

```
112 summaries/crcns-fcx-3-johnson-2019-01.md
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
?? docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md
?? scripts
?? summaries/crcns-fcx-3-johnson-2019-01.md
```

**Agent**

I wrote both files and changed nothing else. The summary is 112 words in four sentences, and neither file uses em dashes, "rather" or bold. There is no `fcx-3` entry in `targets/dandisets.json`, so the notes have no CatalystNeuro sentence. The working tree also has untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others). They were already there, as the round-2 revision report also noted, and I left them alone. Nothing is committed.

`docs/pilot-notes/crcns-fcx-3-johnson-2019-01.md`:

# crcns-fcx-3, Johnson et al. 2019

Six claims reproduced, four partially, seven not reproduced and none blocked; five outcomes rest on an assumption, `erp-no-condition-difference`, `power-low-frequencies`, `fig4c-alpha-beta-shift`, `fig5a-spatiotemporal-bidirectional` and `fig5b-alpha-beta-no-sustained`. The first verification round agreed with all 17 outcomes as they stood, the second agreed with 16 and disagreed on fig4c, and a third round, on the three changes proposed after the second (fig4c to not reproduced, fig5a-spatiotemporal to reproduced, fig5b to partial), agreed with all three. CRCNS does not version data sets, so the version is recorded as unversioned with the data set's DOI (10.6080/K06971S9) and the MD5 sums in the notebook header. The paper, Johnson, King-Stephens, Weber, Laxer, Lin and Knight in Frontiers in Systems Neuroscience (12:65), records intracranial EEG over lateral prefrontal (PFC) and parietal cortex in seven adults with epilepsy during a visuospatial working memory task of 120 trials split between identity, spatial and temporal conditions, and reports that accuracy does not differ by condition while identity responses are slower, that ERPs do not differ between conditions, that processing-interval power differs by condition in most subjects, mostly at low frequencies and in the subjects who found identity trials hardest, that PFC-parietal phase slope index (PSI) is parietal-led during maintenance, that after the test cue delta-theta directionality shifts towards the PFC while alpha-beta stays parietal-led, that 1008 and 984 pairs are directional, and that time-resolved delta-theta PSI separates the conditions in sustained epochs; the data set holds, for the 7 subjects, the filtered continuous iEEG with per-trial event tables, the preprocessed bipolar epochs, channel MNI coordinates and the analysis scripts. The claims were written from the version of record (PMC6333050) as Europe PMC JATS text with the legends of Figures 1 to 5 but without a PDF, so per-subject values shown only in figures were not read, and without the MATLAB scripts, which sit among the data set's files; the claims check made nine corrections, among them a reading for electrodes in clusters of both signs and the per-trial PSI reading, for 17 claims. All 17 could be tested. Reproduced are `trial-counts`, `fig1b-accuracy` (0.625 to 0.975, logit model p = 0.283 against the paper's p > 0.50), `fig1b-rt-identity-slower` (identity slower in all 7 subjects, F values below the paper's bounds), `power-difficulty-subjects`, `power-low-frequencies`, which holds only if the 2-Hz end of the range counts as a local maximum, and fig5a-spatiotemporal, by the letter only, as the identity trials show no direction either. Partial are `table1-electrodes` (187 channels and 1135 pairs against 192 and 1129), `fig2-spatial-power` (5 and 1 subjects, 37.7% and 11.8% of electrodes against 54% and 36%), `fig3-temporal-power` (5 and 2 subjects, 37.4% and 21.0%) and fig5b. Not reproduced are the ERP claim (S2 p = 0.041 under the adopted neighbour reading), every PSI claim of Figures 4 and 5 except those two, among them `fig4-maintenance-parietal-led` (no subject below -1.96, paper -40.03), `fig4a-delta-theta-shift` (no subject above 0, paper 6 subjects) and `directional-pairs` (78 and 104 of 1135 pairs, near the trial-shuffled surrogate's 68 and 78). The author's first run had 8 reproduced, 4 partially, 5 not reproduced and none blocked. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 held that the PSI null did not compute the same statistic as the observed PSI, so no z was calibrated, that the deposited code's variants without the conjugate are not a reading, that the cluster settings, the ERP baseline and band-pass and the power windows reaching outside the 900-ms segment were unresolved, and that the processing epochs of 1150-ms trials may be misaligned; in reply the null was rebuilt as the Methods describe, segments were zero padded as the Methods say, with the scripts' whole-epoch windows as a variant, the scripts' lines were printed (they hold no cluster test), the 900-ms-delay trials were run as a variant, a question on "sustained" went to `questions/crcns-fcx-3.yaml`, and erp, fig4a and directional-pairs moved to not reproduced and fig4c to partial. Round 2 showed with a synthetic test that per-trial PSI (reading b) is offset towards negative z on independent signals, so fig4c's 6 of 7 subjects came from the null, and found sentences the outputs did not support, among them the run time and the ERP threshold; in reply the trial-averaged reading (a), calibrated at 6.0% and 6.9% on shuffled trials, was adopted where the readings differ, a random-trial control showed the loss of power effects on the 900-ms trials comes from fewer trials, and the three changes went to round 3. The author's run took about 2 h 5 min (19:11 to 21:13 UTC); the notebook ran in 19 min at first, with about 7 GB peak memory, 1067 s after the author-answers run, 33.5 min after round 1, 2448 s after round 2 and 2420 s after round 3. The first loader failed on S4's unequal trial lengths and on S3's labels file, which is in MATLAB 5 format, and both were fixed; a first timing check on low-frequency signals did not work and was replaced.

The deposited psianalysis.m computes the cross-spectrum without the conjugate, so its PSI z depends essentially on one channel's phase and changes sign with the channel order (+58.67 with the PFC channel first, -55.47 with the parietal channel first, delta-theta maintenance), and its null is the slope of the trial-mean spectrum with both factors shuffled, not the frequency shuffle of one signal the Methods describe; even with the conjugate added that null gives |z| > 1.96 in 90% (delta-theta) and 92% (alpha-beta) of trial-shuffled pairs, and it alone gives the paper's directional-pair counts (1014 and 1041), as it does on trial-shuffled data (1022 and 1044). psi_compute.m does not run as written, and its subtracterp.m selects temporal trials by the delay column, which selects none. The data set's channel list holds 187 analysed channels where Table 1 gives 192, as S4 has 5 right parietal channels where Table 1 gives 10, and the list yields 1135 same-hemisphere pairs where the paper reports 1129 and Table 1's counts would give 1165. The description says summary_file_trial.csv holds 120 trials per subject, but for S6 and S7 it holds only the kept trials (101 and 90 rows), so single-trial accuracy over all 120 cannot be rebuilt for them. In S2, S3 and S4 the processing-epoch responses of 1150-ms trials come 0.21 to 0.26 s later relative to the processing column than in 900-ms trials, consistent with that column lying about 0.25 s before the event in those trials, which the test does not prove. The electrode position files do not say how contact numbers map to grid positions, S3's labels (RH1 to RH256) do not match its grid's name, and the reference contact of each bipolar channel was found only from the data. S7's derived epochs record 431506 samples where its data_primary.mat has 445952, though the traces still match, and S3's elec_labels.mat is a MATLAB 5 file, the others MATLAB 7.3. Questions are put to the paper's authors: which electrodes were neighbours in the cluster tests and whether clusters were judged at 0.05 or 0.025 per tail, and whether PSI came from trial-averaged or per-trial cross-spectra, with which channel first and with which null.

The author's points on the protocol: the analysis scripts sit among the data set's files, so the reader never read them and it is unclear whether they count as an outside input, and details were taken from them by file name; the order "Methods, then code" does not say what to do when the code is also buggy, so the Methods' readings were run with the conjugate fixed and the deposited code as a variant; absence is judged on the paper's test alone, which is itself underspecified here, so one reading was adopted as an assumption; the decoding suggestion for the clock check does not fit pre-epoched data, so the derived epochs were matched to the continuous data and a delay contrast on high-frequency amplitude was added; and tar.gz files cannot be opened in place as `docs/archives.md` describes for zip, so each was streamed in order.

`summaries/crcns-fcx-3-johnson-2019-01.md`:

In this intracranial dataset the paper's behavioural results held up: identity trials were slower than spatial and temporal ones, and accuracy did not differ by condition. Its per-subject power differences after the test cue held in part, with similar subject counts but smaller shares of electrodes, and sat at low frequencies. The frontoparietal phase-slope findings did not reproduce: with the null the Methods describe, 78 of 1135 pairs were directional in delta-theta, about what trial-shuffled data give, and the paper's counts appear only with the deposited code's null, which flags shuffled data as well. The absence of ERP differences failed in one subject, under a neighbour rule the paper does not state.

## End of run

13 turns, 2 minutes, $1.06 at API prices, result: success.
