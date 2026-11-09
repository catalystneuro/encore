# 001676 · recorder · run 41660467386

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  for f in $(git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5); do echo "== $f"; cat $f; done; python tools/readme_row.py 001676; ls claims/001676 transcripts/001676; cat attempts/001676-skromne-carrasco-2026-01.yaml
```

```
<persisted-output>
Output too large (106.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/cf044e14-0420-492b-95aa-87cd817ec998/tool-results/bvpvppksi.txt

Preview (first 2KB):
== docs/pilot-notes/001702-chaunsali-2025-01.md
# 001702, Chaunsali et al. 2025

No claim reproduced, none partially, none not reproduced and 42 blocked, 23 for
missing data and 19 for insufficient metadata; no outcome rests on an
assumption. Of the 51 claims, 42 are on the dandiset and nine, on the bulk
RNA-seq counts, use data in GEO (GSE317499) and are counted apart: five
reproduced, one partially and three blocked as methods underspecified. The
first verification round agreed with 49 of the 51 outcomes as they stood and
the second with all 51, and nothing was proposed after the second, so there was
no third round. It pins version 0.260216.2323, the only published version; the
paper cites none, and the draft has the same 656 assets. The paper, Chaunsali
et al., "Degradation of perineuronal nets in hippocampal CA2 explains the loss
of social cognition memory in Alzheimer's disease", reports the loss of
perineuronal nets (PNNs) in CA2 of 5XFAD mice from immunohistochemistry
(Figures 1, 3B, 3G, 5I, S1 to S6 and S9), social memory and object recognition
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/cf044e14-0420-492b-95aa-87cd817ec998/tool-results/bvpvppksi.txt"
}
```

```
1	== docs/pilot-notes/001702-chaunsali-2025-01.md
2	# 001702, Chaunsali et al. 2025
3	
4	No claim reproduced, none partially, none not reproduced and 42 blocked, 23 for
5	missing data and 19 for insufficient metadata; no outcome rests on an
6	assumption. Of the 51 claims, 42 are on the dandiset and nine, on the bulk
7	RNA-seq counts, use data in GEO (GSE317499) and are counted apart: five
8	reproduced, one partially and three blocked as methods underspecified. The
9	first verification round agreed with 49 of the 51 outcomes as they stood and
10	the second with all 51, and nothing was proposed after the second, so there was
11	no third round. It pins version 0.260216.2323, the only published version; the
12	paper cites none, and the draft has the same 656 assets. The paper, Chaunsali
13	et al., "Degradation of perineuronal nets in hippocampal CA2 explains the loss
14	of social cognition memory in Alzheimer's disease", reports the loss of
15	perineuronal nets (PNNs) in CA2 of 5XFAD mice from immunohistochemistry
16	(Figures 1, 3B, 3G, 5I, S1 to S6 and S9), social memory and object recognition
17	in these mice and after aggrecan knockout, chondroitinase ABC and GM6001
18	(Figures 2, 3, 5, S7 and S8), and the bulk RNA-seq of CA2 at 3 and 7 months
19	(Figure 4). The claims were written from the version of record in Europe PMC
20	(PMC12541281) without a PDF, so the figures were not seen, and without the
[... 859 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/cf044e14-0420-492b-95aa-87cd817ec998/tool-results/bvpvppksi.txt",
 "offset": 879,
 "limit": 890
}
```

```
879	  outcome: reproduced
880	  notebook: reproduce_skromne_carrasco_2026.ipynb
881	  output: claim:edf4ef-not-diffusive
882	  assumed: true
883	  notes: With changes relative to the last day (reading a), the variance over all recordings is
884	    below half the value of a line through the origin fitted to the first five points in 4 of 5 mice
885	    (mouse 2, 421 against 127, is the exception). Relative to the first day (reading b) it holds in
886	    2 of 5. Under raw HDI reading (a) holds in 3 of 5. The readings differ only in the reference
887	    session and in which cells enter each session's change, so the pass rests on noisy session values
888	    and is fragile.
889	  deviations:
890	  - The test and its threshold are the reader's; the paper shows the curve without a test.
891	  - Main HD reading as for fig1f-example-stable (assumption).
892	- claim: edf4f-change-below-shuffle
893	  outcome: partially_reproduced
894	  notebook: reproduce_skromne_carrasco_2026.ipynb
895	  output: claim:edf4f-change-below-shuffle
896	  measured:
897	  - 16.45
898	  - 4.63
[... 870 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml,collections
d=yaml.safe_load(open('attempts/001676-skromne-carrasco-2026-01.yaml'))
c=collections.Counter((o['outcome'],o.get('assumed',False),o.get('blocked_by')) for o in d['outcomes']);print(c)
E
python -c "
import json;d=json.load(open('targets/dandisets.json'));
x=[e for e in (d if isinstance(d,list) else d.values()) if '001676' in json.dumps(e)][:1];print(json.dumps(x,indent=1)[:3000])"
head -c 3000 claims/001676/*.yaml; grep -c "^- id:\|^  - id:" claims/001676/*.yaml; wc -w transcripts/001676/*report.md; git log --format='%h %s' -- transcripts/001676 attempts | head -20
```

```
Counter({('reproduced', True, None): 14, ('partially_reproduced', False, None): 4, ('reproduced', False, None): 4, ('blocked', False, 'metadata_insufficient'): 3, ('not_reproduced', True, None): 2, ('partially_reproduced', True, None): 2, ('not_reproduced', False, None): 1, ('blocked', False, 'too_large'): 1, ('blocked', False, 'data_missing'): 1})
[
 [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 2559.25,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "House mouse"
   ],
   "approaches": [
    "electrophysiological approach",
    "behavioral approach"
   ],
   "papers": [
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d[0] if isinstance(d[0],list) else d):
  if e.get('dandiset')=='001676': print(json.dumps(e,indent=1))"; cd transcripts/001676; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (34KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/cf044e14-0420-492b-95aa-87cd817ec998/tool-results/bd9rxj7si.txt

Preview (first 2KB):
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    for e in (d[0] if isinstance(d[0],list) else d):
                                 ~^^^
KeyError: 0
=== author-report.md
I've done steps 1 to 6 for DANDI:001676 (version 0.251205.2137, the version the paper cites and the only published one). Both notebooks pass `tools/entry.py all`, the entry check reports 0 errors, and the handover is in `executed/001676-skromne-carrasco-2026/handover/`. Of 32 claims, 15 are reproduced, 5 partially reproduced, 7 not reproduced and 5 blocked. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| edf1h-ring, fig1f-example-stable, fig1g-all-mice-stable, edf4ab-vtest-per-animal, edf4c-previous-session, edf4ef-not-diffusive, fig1h-drift-rate, edf4g-pairwise-offset-stable, fig1i-offset-drift, edf4ij-pv-decay, fig2e-offset-across-environments, edf5c-stable-within-environment, fig2g-environment-classifier, edf7-ephys-offsets, fig4e-decoder-single-visit | reproduced (15) |
| roi-counts, fig2i-random-remapping, fig4d-single-visit-memory, edf10c-environment-identity, edf8-same-vs-mixed | partially reproduced (5) |
| edf1e-hd-proportion, edf4f-change-below-shuffle, edf2ab-jaccard, edf2-no-registration-confound, fig2h-coherent-remapping, edf9-interference, edf10b-per-animal-change | not reproduced (7) |
| fig1k-decoding-across-days | blocked, too_large (1,883 fits × 3.2 s ≈ 101 min, over the 60-min limit) |
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/cf044e14-0420-492b-95aa-87cd817ec998/tool-results/bd9rxj7si.txt"
}
```

```
1	Traceback (most recent call last):
2	  File "<string>", line 4, in <module>
3	    for e in (d[0] if isinstance(d[0],list) else d):
4	                                 ~^^^
5	KeyError: 0
6	=== author-report.md
7	I've done steps 1 to 6 for DANDI:001676 (version 0.251205.2137, the version the paper cites and the only published one). Both notebooks pass `tools/entry.py all`, the entry check reports 0 errors, and the handover is in `executed/001676-skromne-carrasco-2026/handover/`. Of 32 claims, 15 are reproduced, 5 partially reproduced, 7 not reproduced and 5 blocked. Nothing is committed.
8	
9	**1. Outcomes**
10	
11	| Claim | Outcome |
12	|---|---|
13	| edf1h-ring, fig1f-example-stable, fig1g-all-mice-stable, edf4ab-vtest-per-animal, edf4c-previous-session, edf4ef-not-diffusive, fig1h-drift-rate, edf4g-pairwise-offset-stable, fig1i-offset-drift, edf4ij-pv-decay, fig2e-offset-across-environments, edf5c-stable-within-environment, fig2g-environment-classifier, edf7-ephys-offsets, fig4e-decoder-single-visit | reproduced (15) |
14	| roi-counts, fig2i-random-remapping, fig4d-single-visit-memory, edf10c-environment-identity, edf8-same-vs-mixed | partially reproduced (5) |
15	| edf1e-hd-proportion, edf4f-change-below-shuffle, edf2ab-jaccard, edf2-no-registration-confound, fig2h-coherent-remapping, edf9-interference, edf10b-per-animal-change | not reproduced (7) |
16	| fig1k-decoding-across-days | blocked, too_large (1,883 fits × 3.2 s ≈ 101 min, over the 60-min limit) |
17	| edf7g-waveforms | blocked, data_missing |
18	| fig3de-probe-memory, fig3e-mvl-delay, fig3fg-probe-drift | blocked, metadata_insufficient |
19	
20	**2. Dataset, assumptions, questions**
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else '')
s=json.dumps(d); i=s.find('\"001676\"'); print(s[i-50:i+1500])"; grep -n "^#" claims/001676/*.yaml | sed -n '30,120p'
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
escription"}], "catalystneuro": []}, {"dandiset": "001676", "name": "Months-long stability of the head-direction system", "published_version": "0.251205.2137", "asset_count": 406, "size_gb": 50.94, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Mus musculus - House mouse"], "approaches": ["microscopy approach; cell population imaging", "behavioral approach", "electrophysiological approach"], "papers": [{"doi": "10.1101/2024.06.13.598909v1", "title": "Months-long stability of the head-direction system", "relation": "IsPublishedIn", "resource_type": "Preprint", "preprint": true}], "catalystneuro": []}, {"dandiset": "001678", "name": "Data for parametrizing alternating current stimulation for neuromodulation (Bell Vila, M., et al, 2026)", "published_version": "0.260227.1824", "asset_count": 22, "size_gb": 55.25, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Rattus norvegicus - Norway rat"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1162/imag.a.1066", "title": "Parametrizing alternating current stimulation for neuromodulation", "relation": "IsCitedBy", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": []}, {"dandiset": "001683", "name": "Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy", "published_version": "0.260109.2104", "asset_count": 318, "size_gb": 355.74, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Rattus norvegicus - Norway rat"], "approach
30:#   and third environment; for mouse 5 the field of view was lost before the probe trials.
31:# - Imaging, mice 6 to 10 (Fig. 4, Extended Data Fig. 10). Two novel environments (square and
32:#   circular in the figure) visited on one day 8 h apart, one of them then visited weekly for
33:#   three weeks, both revisited on week 5 (7 sessions over 5 weeks). The groups 
[... 58 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001676-skromne-carrasco-2026-01.md",
 "content": "# 001676, Skromne Carrasco et al. 2026\n\nEighteen claims reproduced (14 on an assumption), six partially (two on an\nassumption), three not reproduced (two on an assumption) and five blocked,\nthree for insufficient metadata, one for missing data and one as too large.\nAll 32 claims are on the dandiset. The first verification round agreed with 26\nof the 32 outcomes as they stood and the second with all 32, and nothing was\nproposed after the second, so there was no third round. It pins version\n0.251205.2137, the version the paper cites and the only published one. The\npaper, Skromne Carrasco, Viejo and Peyrache, \"Months-long stability of the\nhead-direction system\" in Nature, images head-direction (HD) cells of the\npost-subiculum with a Miniscope in mice 1 to 5 over a month in one environment\n(Fig. 1), over two weeks in each of four environments (Fig. 2), in a week of\nprobe trials (Fig. 3) and in visits in random order (Extended Data Fig. 9), and\nin mice 6 to 10 over weekly and single visits (Fig. 4, Extended Data Fig. 10),\nwith silicon-probe recordings in four mice (Extended Data Fig. 7). The claims\nwere written from the version of record without the Supplementary Information\nor the Source Data, and no figure was read from the PDF; the paper's code is\navailable on request, so no code was read. Twenty-seven claims were tested.\nMost rest on one open detail of the HD cell rule, whether the head-direction\ninformation (HDI) is computed on the smoothed or the raw tuning curve; the\nsmoothed curve with a 12 degree kernel was adopted for every claim as the main\nreading because it gives the paper's numbers of compared sessions (18 in Fig.\n1f; 85 pooled against 84) and of offset values (25,441 against 25,901), where\nraw HDI gives 92 sessions and 92,537 values, and raw HDI is shown alongside.\nReproduced are the stability of preferred directions in Fig. 1f and 1g and\nExtended Data Fig. 4a to c (pooled V 75.58 over 85 sessions against 75.21 over\n84), the drift rates of Fig. 1h and 1i (6.71 and 5.32 degrees per week), the\npairwise offsets of Extended Data Fig. 4g, Fig. 2e and the electrophysiology\nof Extended Data Fig. 7, `edf1h-ring`, `edf4ef-not-diffusive`, `edf4ij-pv-decay`,\n`edf5c-stable-within-environment`, `fig2g-environment-classifier`,\n`fig4e-decoder-single-visit`, `edf2-no-registration-confound` and the two\nExtended Data Fig. 10 claims. The classifier of Fig. 2g reaches 0.64 against\n0.28 for shuffles, but given only which cell pairs are present it reaches 0.70,\nand with the correlations permuted among the pairs present 0.59, so the\ncorrelations add a little to the presence pattern. The two Extended Data Fig.\n10 claims rest on taking a change in preferred direction as the earlier session\nminus the later one, the convention under which the Fig. 1g means have the\npaper's sign in 5 of 5 mice. Partial are `roi-counts` (402 sessions, 367 for\nmice 1 to 5, against 388), `edf4f-change-below-shuffle`, `edf8-same-vs-mixed`,\n`fig2i-random-remapping` (Rayleigh p 0.069 where the paper reports 0.032),\n`edf9-interference` and `fig4d-single-visit-memory` (single-visit mean 21.9\nagainst 6.6 +- 4.1). Not reproduced are `edf1e-hd-proportion` (main reading\n0.116, 0.400, 0.035, 0.292, 0.072, at most 1 of 5 within tolerance under any\nreading), `edf2ab-jaccard` (2 of 5 mice) and `fig2h-coherent-remapping` (10 of\n15 pairs, 67% against 80%); with raw HDI the last two would be reproduced, and\nraw HDI would also change `edf4c-previous-session` and fail parts of\n`fig1f-example-stable` and `edf4ij-pv-decay`. `fig1k-decoding-across-days` is\nblocked as too large: its 1,883 XGBoost fits at 2.56 s each, four at a time,\ntake an estimated 80 minutes (51 for the pairs up to 10 days apart), plus\nloading, against the 60-minute limit; the data it needs are in the dataset.\nThe author asked no questions of a reader, so the answer and author-answers\nruns changed nothing. Round 1 disagreed with six outcomes and found that the\nsign of the change in preferred direction was run one way only, that most HD\ncell claims were run only under the main reading, that `edf2` kept only cells\nwith CellReg score above 0.8 and corrected over 3 tests where the claims file\nlists 4, that the Fig. 2g classifier may read which cells are present, and\nthat the decoders were run only with test cells passing the HD rule in the test\nsession; in reply both signs and raw HDI were run, `edf2` was rerun over all\nscores, controls and a looser decoder rule were added, five outcomes changed\nto the verifier's, and `edf2ab-jaccard` was kept not reproduced with the\ndisagreement recorded, as choosing raw HDI for that claim alone would pick the\nreading that passes. Round 2 agreed with all 32, asked that `edf2`,\n`edf4ij-pv-decay` and `edf1h-ring` be marked as resting on an assumption, found\nCellReg scores below 0 in the raw-HDI `edf2` set and stale sentences (fit times\nof 2.39 s, 75 and 47 minutes where 2.57 s, 81 and 51 were printed, and run\ntimes), all corrected, and asked for the presence-keeping shuffle of Fig. 2g,\nwhich was added. The author's run took about 2 h (04:40 to 06:43 UTC); pycircstat\ndoes not import under numpy 2, so its formulas were reimplemented, and a helper\nbug crashed the decoding notebook on the first full run after round 1 and was\nfixed. The main and decoding notebooks ran in 19 and 32 minutes at first, 2038\ns and 1740 s after the author-answers run, 25 and 34 minutes after round 1 and\n35.3 and 40 minutes at the end. Untracked items at the repository root\n(`.bashrc`, `scripts`, `.idea` and others), which predate the run, were left\nalone.\n\nThe tuning_curves table of every imaging file holds one curve repeated for\nevery ROI, in 401 of 402 sessions the curve of ROI 0, smoothed with a kernel of\nabout 4 bins, while its description says it holds the tuning curve of each\nROI. Each protocol's files carry a CellReg table for that protocol only, and\nnothing links ROIs across protocols, so the probe trials of Fig. 3 cannot be\nmatched to the last visits of the two-week protocol and all of Fig. 3 is\nblocked; the probe week is also not labelled, and is found as the first week of\nthe random-order protocol, which starts 3 days after the last two-week session\nfor mice 1 to 4 and 81 days after it for mouse 5. The electrophysiology files\nhold spike times and electrode groups only, with no waveforms, so the waveform\nfeatures of Extended Data Fig. 7f-h cannot be computed; they hold 347 units,\n254 of them on PoSub shanks (the paper's n of 254 cells), and two explorations\nof each of the three environments separated by sleep where the paper describes\none. The dandiset holds 402 imaging sessions (367 for mice 1 to 5) where the\npaper reports 388, including random-order sessions of mouse 5, whose field of\nview the paper says was lost before the probe trials, and sessions last 902 to\n1799 s where the Methods state 20 min; the circular protocol has 19, 20, 19, 19\nand 20 sessions, as Extended Data Fig. 1e states. The CellReg scores include\nvalues below 0, 102 of 5,190 rows, down to -1.24, which a CellReg confidence\nscore cannot take, and the files do not describe the score. The dandiset's\nrelated publication and each file's related_publications point to the bioRxiv\npreprint, not the Nature article. Questions are put to the paper's authors:\nwhether the HDI is computed on the raw or the smoothed tuning curve and whether\nthe kernel is 12 degrees or 12 bins, what \"detected in at least six sessions\"\nmeans and which sessions enter the average HDI; whether pairwise offsets are\nunsigned, how the drift rate per week is computed and what the sign of a\nchange in preferred direction is; and the XGBoost hyperparameters, the dF/F\nnormalization, how population activity is summed, whether test cells must be\nHD cells in the test session and whether the error variance of Extended Data\nFig. 8c is circular or linear.\n\nThe author's points on the protocol: the aim of under ten minutes cannot be met\nwhen streaming the 402 files takes 16 to 23 minutes; asset paths do not show\nthe protocol, so the decoding notebook opens every file to select sessions;\nstep 1.6 is written per claim while one open detail, the HD rule, underlies\nabout 20 claims, and one main reading was adopted for all of them because it\nreproduces the paper's sample sizes, which the protocol does not say is a valid\nbasis; the chance-level rule would block where the signed offsets' chance (90\ndegrees) is far from the paper's, but the unsigned reading's matches, so the\nmatch chose the reading; part of edf9's criterion needs a blocked claim not\nlisted in `depends_on`; the line between partially and not reproduced for\ncriteria with several parts is unclear, and partially was used when the\nqualitative effect holds but a numeric part fails; the suggested clock check\ndoes not suit continuous imaging, and HD tuning against time shift was used;\nand pycircstat does not import, so its formulas were reimplemented.\n"
}
```

```
File created successfully at: docs/pilot-notes/001676-skromne-carrasco-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -nE "—|rather|\*\*" docs/pilot-notes/001676-skromne-carrasco-2026-01.md; wc -w docs/pilot-notes/001676-skromne-carrasco-2026-01.md docs/pilot-notes/001641-ito-2009-01.md; git status --short
```

```
1508 docs/pilot-notes/001676-skromne-carrasco-2026-01.md
 1646 docs/pilot-notes/001641-ito-2009-01.md
 3154 total
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
?? docs/pilot-notes/001676-skromne-carrasco-2026-01.md
?? scripts
```

**Agent**

I wrote the notes in `docs/pilot-notes/001676-skromne-carrasco-2026-01.md` and changed no other file. The only new item in `git status` is that file; the other untracked items at the repository root were there before I started. Nothing is committed or pushed. The `catalystneuro` field for 001676 is empty, so the second paragraph does not open with the conversion sentence.

# 001676, Skromne Carrasco et al. 2026

Eighteen claims reproduced (14 on an assumption), six partially (two on an assumption), three not reproduced (two on an assumption) and five blocked, three for insufficient metadata, one for missing data and one as too large. All 32 claims are on the dandiset. The first verification round agreed with 26 of the 32 outcomes as they stood and the second with all 32, and nothing was proposed after the second, so there was no third round. It pins version 0.251205.2137, the version the paper cites and the only published one. The paper, Skromne Carrasco, Viejo and Peyrache, "Months-long stability of the head-direction system" in Nature, images head-direction (HD) cells of the post-subiculum with a Miniscope in mice 1 to 5 over a month in one environment (Fig. 1), over two weeks in each of four environments (Fig. 2), in a week of probe trials (Fig. 3) and in visits in random order (Extended Data Fig. 9), and in mice 6 to 10 over weekly and single visits (Fig. 4, Extended Data Fig. 10), with silicon-probe recordings in four mice (Extended Data Fig. 7). The claims were written from the version of record without the Supplementary Information or the Source Data, and no figure was read from the PDF; the paper's code is available on request, so no code was read. Twenty-seven claims were tested. Most rest on one open detail of the HD cell rule, whether the head-direction information (HDI) is computed on the smoothed or the raw tuning curve; the smoothed curve with a 12 degree kernel was adopted for every claim as the main reading because it gives the paper's numbers of compared sessions (18 in Fig. 1f; 85 pooled against 84) and of offset values (25,441 against 25,901), where raw HDI gives 92 sessions and 92,537 values, and raw HDI is shown alongside. Reproduced are the stability of preferred directions in Fig. 1f and 1g and Extended Data Fig. 4a to c (pooled V 75.58 over 85 sessions against 75.21 over 84), the drift rates of Fig. 1h and 1i (6.71 and 5.32 degrees per week), the pairwise offsets of Extended Data Fig. 4g, Fig. 2e and the electrophysiology of Extended Data Fig. 7, `edf1h-ring`, `edf4ef-not-diffusive`, `edf4ij-pv-decay`, `edf5c-stable-within-environment`, `fig2g-environment-classifier`, `fig4e-decoder-single-visit`, `edf2-no-registration-confound` and the two Extended Data Fig. 10 claims. The classifier of Fig. 2g reaches 0.64 against 0.28 for shuffles, but given only which cell pairs are present it reaches 0.70, and with the correlations permuted among the pairs present 0.59, so the correlations add a little to the presence pattern. The two Extended Data Fig. 10 claims rest on taking a change in preferred direction as the earlier session minus the later one, the convention under which the Fig. 1g means have the paper's sign in 5 of 5 mice. Partial are `roi-counts` (402 sessions, 367 for mice 1 to 5, against 388), `edf4f-change-below-shuffle`, `edf8-same-vs-mixed`, `fig2i-random-remapping` (Rayleigh p 0.069 where the paper reports 0.032), `edf9-interference` and `fig4d-single-visit-memory` (single-visit mean 21.9 against 6.6 +- 4.1). Not reproduced are `edf1e-hd-proportion` (main reading 0.116, 0.400, 0.035, 0.292, 0.072, at most 1 of 5 within tolerance under any reading), `edf2ab-jaccard` (2 of 5 mice) and `fig2h-coherent-remapping` (10 of 15 pairs, 67% against 80%); with raw HDI the last two would be reproduced, and raw HDI would also change `edf4c-previous-session` and fail parts of `fig1f-example-stable` and `edf4ij-pv-decay`. `fig1k-decoding-across-days` is blocked as too large: its 1,883 XGBoost fits at 2.56 s each, four at a time, take an estimated 80 minutes (51 for the pairs up to 10 days apart), plus loading, against the 60-minute limit; the data it needs are in the dataset. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 disagreed with six outcomes and found that the sign of the change in preferred direction was run one way only, that most HD cell claims were run only under the main reading, that `edf2` kept only cells with CellReg score above 0.8 and corrected over 3 tests where the claims file lists 4, that the Fig. 2g classifier may read which cells are present, and that the decoders were run only with test cells passing the HD rule in the test session; in reply both signs and raw HDI were run, `edf2` was rerun over all scores, controls and a looser decoder rule were added, five outcomes changed to the verifier's, and `edf2ab-jaccard` was kept not reproduced with the disagreement recorded, as choosing raw HDI for that claim alone would pick the reading that passes. Round 2 agreed with all 32, asked that `edf2`, `edf4ij-pv-decay` and `edf1h-ring` be marked as resting on an assumption, found CellReg scores below 0 in the raw-HDI `edf2` set and stale sentences (fit times of 2.39 s, 75 and 47 minutes where 2.57 s, 81 and 51 were printed, and run times), all corrected, and asked for the presence-keeping shuffle of Fig. 2g, which was added. The author's run took about 2 h (04:40 to 06:43 UTC); pycircstat does not import under numpy 2, so its formulas were reimplemented, and a helper bug crashed the decoding notebook on the first full run after round 1 and was fixed. The main and decoding notebooks ran in 19 and 32 minutes at first, 2038 s and 1740 s after the author-answers run, 25 and 34 minutes after round 1 and 35.3 and 40 minutes at the end. Untracked items at the repository root (`.bashrc`, `scripts`, `.idea` and others), which predate the run, were left alone.

The tuning_curves table of every imaging file holds one curve repeated for every ROI, in 401 of 402 sessions the curve of ROI 0, smoothed with a kernel of about 4 bins, while its description says it holds the tuning curve of each ROI. Each protocol's files carry a CellReg table for that protocol only, and nothing links ROIs across protocols, so the probe trials of Fig. 3 cannot be matched to the last visits of the two-week protocol and all of Fig. 3 is blocked; the probe week is also not labelled, and is found as the first week of the random-order protocol, which starts 3 days after the last two-week session for mice 1 to 4 and 81 days after it for mouse 5. The electrophysiology files hold spike times and electrode groups only, with no waveforms, so the waveform features of Extended Data Fig. 7f-h cannot be computed; they hold 347 units, 254 of them on PoSub shanks (the paper's n of 254 cells), and two explorations of each of the three environments separated by sleep where the paper describes one. The dandiset holds 402 imaging sessions (367 for mice 1 to 5) where the paper reports 388, including random-order sessions of mouse 5, whose field of view the paper says was lost before the probe trials, and sessions last 902 to 1799 s where the Methods state 20 min; the circular protocol has 19, 20, 19, 19 and 20 sessions, as Extended Data Fig. 1e states. The CellReg scores include values below 0, 102 of 5,190 rows, down to -1.24, which a CellReg confidence score cannot take, and the files do not describe the score. The dandiset's related publication and each file's related_publications point to the bioRxiv preprint, not the Nature article. Questions are put to the paper's authors: whether the HDI is computed on the raw or the smoothed tuning curve and whether the kernel is 12 degrees or 12 bins, what "detected in at least six sessions" means and which sessions enter the average HDI; whether pairwise offsets are unsigned, how the drift rate per week is computed and what the sign of a change in preferred direction is; and the XGBoost hyperparameters, the dF/F normalization, how population activity is summed, whether test cells must be HD cells in the test session and whether the error variance of Extended Data Fig. 8c is circular or linear.

The author's points on the protocol: the aim of under ten minutes cannot be met when streaming the 402 files takes 16 to 23 minutes; asset paths do not show the protocol, so the decoding notebook opens every file to select sessions; step 1.6 is written per claim while one open detail, the HD rule, underlies about 20 claims, and one main reading was adopted for all of them because it reproduces the paper's sample sizes, which the protocol does not say is a valid basis; the chance-level rule would block where the signed offsets' chance (90 degrees) is far from the paper's, but the unsigned reading's matches, so the match chose the reading; part of edf9's criterion needs a blocked claim not listed in `depends_on`; the line between partially and not reproduced for criteria with several parts is unclear, and partially was used when the qualitative effect holds but a numeric part fails; the suggested clock check does not suit continuous imaging, and HD tuning against time shift was used; and pycircstat does not import, so its formulas were reimplemented.

## End of run

10 turns, 1 minutes, $0.97 at API prices, result: success.
