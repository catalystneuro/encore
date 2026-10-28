# openneuro-ds002778 · recorder · run 40606001635

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/openneuro-ds002778/ transcripts/openneuro-ds002778/; python tools/readme_row.py openneuro-ds002778; cat attempts/openneuro-ds002778-jackson-2019-01.yaml
```

```
<persisted-output>
Output too large (41.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6f1eed02-ee64-4384-a228-24f8ab7c10d1/tool-results/bk6epriio.txt

Preview (first 2KB):
docs/pilot-notes/figshare-24949470-mintal-2024-01.md
docs/pilot-notes/figshare-24639285-tarduno-2024-01.md
docs/pilot-notes/figshare-26877211-ocagli-2024-01.md
docs/pilot-notes/dryad-4j0zpc8hz-didion-gency-2024-01.md
docs/pilot-notes/dryad-tdz08kq5d-wang-2024-01.md
claims/openneuro-ds002778/:
10.1523-eneuro.0151-19.2019.yaml

transcripts/openneuro-ds002778/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6f1eed02-ee64-4384-a228-24f8ab7c10d1/tool-results/bk6epriio.txt"
}
```

```
1	docs/pilot-notes/figshare-24949470-mintal-2024-01.md
2	docs/pilot-notes/figshare-24639285-tarduno-2024-01.md
3	docs/pilot-notes/figshare-26877211-ocagli-2024-01.md
4	docs/pilot-notes/dryad-4j0zpc8hz-didion-gency-2024-01.md
5	docs/pilot-notes/dryad-tdz08kq5d-wang-2024-01.md
6	claims/openneuro-ds002778/:
7	10.1523-eneuro.0151-19.2019.yaml
8	
9	transcripts/openneuro-ds002778/:
10	answer-report.md
11	answer.md
12	author-answers-report.md
13	author-answers.md
14	author-report.md
15	author-revise-1-report.md
16	author-revise-1.md
17	author-revise-2-report.md
18	author-revise-2.md
19	author.md
20	claims-check-report.md
[... 773 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in figshare-24949470-mintal-2024-01 figshare-24639285-tarduno-2024-01 figshare-26877211-ocagli-2024-01 dryad-4j0zpc8hz-didion-gency-2024-01 dryad-tdz08kq5d-wang-2024-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; grep -n "readme_row\|^| Dataset\|^| ---" README.md | head; sed -n 1,60p tools/readme_row.py; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('targets',d)
for x in (it if isinstance(it,list) else it.values()):
  if 'ds002778' in json.dumps(x): print(json.dumps(x,indent=1))"
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6f1eed02-ee64-4384-a228-24f8ab7c10d1/tool-results/bw8y8nhs5.txt

Preview (first 2KB):
=== figshare-24949470-mintal-2024-01
# figshare-24949470, Mintal et al. 2024

Twelve claims reproduced and four partially, all on the dataset, with none
not reproduced; the two claims on data held elsewhere are blocked and not
counted. It pins version 1, the item's only version, which holds 8 files: the
user responses (data_without_email.csv), the party workbook, the recoded party
positions, Supplementary Table 1, a census CSV, a data dictionary, a README and
the paper's R code. The paper, in Scientific Data, describes
the Volebny Kompas voting advice application for the 2023 Slovak parliamentary
election: 134,699 responses to 39 statements gathered from 5 September 2023 to
election day, and the positions of 11 parties on those statements, coded by two
experts and self-placed by 4 parties. The claims were written from the version
of record in Europe PMC (PMC11374779) without its figures or the R code, so the
party placements of Figures 2 and 3 and the dendrogram of Figure 7 were read
from the publisher's images, by pixel position, by a separate agent that had
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6f1eed02-ee64-4384-a228-24f8ab7c10d1/tool-results/bw8y8nhs5.txt"
}
```

```
1	=== figshare-24949470-mintal-2024-01
2	# figshare-24949470, Mintal et al. 2024
3	
4	Twelve claims reproduced and four partially, all on the dataset, with none
5	not reproduced; the two claims on data held elsewhere are blocked and not
6	counted. It pins version 1, the item's only version, which holds 8 files: the
7	user responses (data_without_email.csv), the party workbook, the recoded party
8	positions, Supplementary Table 1, a census CSV, a data dictionary, a README and
9	the paper's R code. The paper, in Scientific Data, describes
10	the Volebny Kompas voting advice application for the 2023 Slovak parliamentary
11	election: 134,699 responses to 39 statements gathered from 5 September 2023 to
12	election day, and the positions of 11 parties on those statements, coded by two
13	experts and self-placed by 4 parties. The claims were written from the version
14	of record in Europe PMC (PMC11374779) without its figures or the R code, so the
15	party placements of Figures 2 and 3 and the dendrogram of Figure 7 were read
16	from the publisher's images, by pixel position, by a separate agent that had
17	not seen the computed values, and are listed under `inputs`. The response
18	count, the collection window, the party workbook, the parties and
19	self-placements, the coders' kappa, the uni-dimension and landscape
20	placements, the clustering, Table 2, the age and education inconsistencies,
[... 534 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "ds002778" targets/dandisets.json | head; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else d[0])
E
head -c 6000 claims/openneuro-ds002778/*.yaml; grep -c "^  - id:\|^- id:" claims/openneuro-ds002778/*.yaml; grep -n "data:\|kind:" claims/openneuro-ds002778/*.yaml | sort | uniq -c | head -40; ls -la transcripts/openneuro-ds002778/; ls questions/ | grep ds002778
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
# Claims for Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, on OpenNeuro ds002778.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol as stated in docs/protocol.md.
#
# Text read: the version of record, full text from Europe PMC PMC6553574 (main text, Methods, figure
# legends, Tables 1 to 3). The only supplement is Extended Data 1, the analysis code, which is the
# GitHub repository read below. Figures were not opened; no claim needs a value read off a figure.
#
# Code read: https://github.com/SwannLab/Jackson_2019 at commit a7c89f50106aa4ccec76ace18bbfa45a5440545e
# (2020-05-19). It holds utils.py (loading the preprocessed traces, shape and PAC per recording),
# shape.py (zero crossings, peaks and troughs, sharpness, steepness), pac.py (normalized modulation
# index, Ozkurt and Schnitzler 2011) and notebooks Figure_1, Figures_2,3 and Figure_4. The notebooks
# print the Wilcoxon, rank sum, Spearman and Cohen's d values of Tables 1 and 2 (beta) and Figure 3.
# The code starts from preprocessed MATLAB files (AVG_motor.mat, rejectscombined.mat) that are not in
# the repository: the MATLAB preprocessing, the manual artifact marks, the mu/alpha analysis, the
# bipolar and CSD analyses, the F7/F8 and T7/T8 tests, the power spectra, the topographies and the Q4
# effect sizes (Table 3) are not in the code.
#
# Data the paper used (Methods, Participants and Data collection): resting scalp EEG from a dataset
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git log --reverse --format='%s' -- transcripts/openneuro-ds002778 | cat; cd transcripts/openneuro-ds002778; for f in author-report answer-report author-answers-report verifier-1-report author-revise-1-report verifier-2-report author-revise-2-report; do echo "=== $f"; cat $f.md; done; cat ../../questions/openneuro-ds002778.yaml
```

```
<persisted-output>
Output too large (32.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6f1eed02-ee64-4384-a228-24f8ab7c10d1/tool-results/bs1njtbuk.txt

Preview (first 2KB):
Agent run on openneuro-ds002778: claims (success)
Agent run on openneuro-ds002778: claims-check (success)
Agent run on openneuro-ds002778: author (success)
Agent run on openneuro-ds002778: answer (success)
Agent run on openneuro-ds002778: author-answers (success)
Agent run on openneuro-ds002778: verifier-1 (success)
Agent run on openneuro-ds002778: author-revise-1 (success)
Agent run on openneuro-ds002778: verifier-2 (success)
Agent run on openneuro-ds002778: author-revise-2 (success)
=== author-report
All 25 claims were tested and none is blocked. The entry passes `tools/entry.py all` with 0 errors, and the notebook runs in 100 s. The handover package is built in `executed/openneuro-ds002778-jackson-2019/handover/`. Nothing was committed.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6f1eed02-ee64-4384-a228-24f8ab7c10d1/tool-results/bs1njtbuk.txt"
}
```

```
1	Agent run on openneuro-ds002778: claims (success)
2	Agent run on openneuro-ds002778: claims-check (success)
3	Agent run on openneuro-ds002778: author (success)
4	Agent run on openneuro-ds002778: answer (success)
5	Agent run on openneuro-ds002778: author-answers (success)
6	Agent run on openneuro-ds002778: verifier-1 (success)
7	Agent run on openneuro-ds002778: author-revise-1 (success)
8	Agent run on openneuro-ds002778: verifier-2 (success)
9	Agent run on openneuro-ds002778: author-revise-2 (success)
10	=== author-report
11	All 25 claims were tested and none is blocked. The entry passes `tools/entry.py all` with 0 errors, and the notebook runs in 100 s. The handover package is built in `executed/openneuro-ds002778-jackson-2019/handover/`. Nothing was committed.
12	
13	**1. Outcome per claim**
14	
15	| Claim | Outcome |
16	|---|---|
17	| fig2-sharpness-off-on | partially reproduced: W 13 matches; d 0.73 is below 0.86 ± 0.086 |
18	| fig2-steepness-off-on | partially reproduced: d 0.70 matches; W 16 is outside 9 ± 0.9 |
19	| fig2-pac-off-on | partially reproduced: d 0.85 matches; W 13 (Methods' filters) or 12 (code's) is outside 15 ± 1.5 |
20	| bipolar-off-on | reproduced |
[... 303 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'));t=d['targets'];print(type(t),len(t));print(d['source']);x=t[0] if isinstance(t,list) else next(iter(t.items()));print(x)"; grep -c openneuro targets/dandisets.json; grep -n "time\|minutes\|runtime\|took" transcripts/openneuro-ds002778/*-report.md | head
```

```
<class 'list'> 288
https://api.dandiarchive.org/api
{'dandiset': '000003', 'name': 'Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells', 'published_version': '0.260218.2052', 'asset_count': 101, 'size_gb': 2559.25, 'data_standards': ['Neurodata Without Borders (NWB)'], 'species': ['House mouse'], 'approaches': ['electrophysiological approach', 'behavioral approach'], 'papers': [{'doi': '10.1016/j.neuron.2016.12.011', 'title': 'Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells', 'relation': 'IsDescribedBy', 'resource_type': 'JournalArticle', 'preprint': False}], 'catalystneuro': ['contributor Baker, Cody of CatalystNeuro']}
1
transcripts/openneuro-ds002778/author-report.md:30:- The `on` session of sub-pd16 was exported from preprocessed EEGLAB files. After preprocessing it has about 6 times the amplitude of any other recording and no alpha peak, and the dataset does not say how it was processed. The `on` session of sub-pd6 came from the same kind of export; it is already average-referenced and lasts 289 s. Results without these two patients are shown as variants.
transcripts/openneuro-ds002778/author-report.md:44:**4. Runtime and failures**
transcripts/openneuro-ds002778/author-report.md:45:The run took about 26 minutes (22:23 to 22:49 UTC). The only failure was a YAML colon-space in the attempt record, which I fixed. `git status` also shows untracked dotfiles at the repository root (`.bashrc` and others); these are sandbox device mounts, not files I created.
transcripts/openneuro-ds002778/verifier-1-report.md:52:5. **[does not affect a conclusion]** Two on sessions, pd6 and pd16, were exported from preprocessed EEGLAB files. pd6 is already average-referenced; pd16 has electrode SDs about 6 times the others and a high cutoff of 256 Hz. Both stay in the main analysis. Exclusion variants appear only in cells 16, 18 and 38, not for PAC, the correlations or Q4. The ratio measures d
[... 1 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/openneuro-ds002778-jackson-2019-01.md",
 "content": "# openneuro-ds002778, Jackson et al. 2019\n\nNine claims reproduced, nine partially and six not reproduced, with none\nblocked, all on the dataset. It pins version 1.0.5, the latest snapshot, which\nholds 46 BDF files at 512 Hz from 15 patients with Parkinson's disease recorded\noff and on medication and 16 controls; the paper cites no snapshot, and the\nchange log shows no change to the EEG files across snapshots. The paper, in\neNeuro, measures the sharpness and steepness asymmetry of beta waveforms and\nbeta to gamma phase-amplitude coupling (PAC) in resting scalp EEG, and reports\nthat all three are higher off than on medication at C3 and C4, with mu/alpha\nresults in Tables 1 and 2 and the shape quadrants of Figure 4. The claims were\nwritten from the version of record in Europe PMC (PMC6553574) and from the\npaper's code at SwannLab/Jackson_2019 commit a7c89f50, which starts from\npreprocessed MATLAB files that are not public, so every measure was computed\nfrom the BDF files with the Methods' preprocessing. The off against on tests\nof shape and PAC, the bipolar and temporalis controls, the topographies, the\noff against control tests with the average reference and with CSD, the UPDRS\nchange, the spectral peaks of Figure 1C, the alpha tests of Tables 1 and 2,\nthe correlations of Figure 3, the Q4 counts and the effect sizes of Table 3\nwere tested. The three main off against on tests hold after FDR correction\nbut each has one value outside tolerance: sharpness d 0.73 against 0.86 +/-\n0.086, steepness W 16 against 9 +/- 0.9, and PAC W 13 or 12 against 15 +/- 1.5.\n`offctrl-steepness` and `table2-alpha-offctrl` are not reproduced, as z and d\nare within tolerance but the FDR corrected p is 0.0531 under every filter\nreading, and Holm, Bonferroni and Benjamini-Yekutieli are further from 0.05;\n`offctrl-pac-csd` is not reproduced (p = 0.075 against 0.022), and no spline\nvariant reaches 0.05; `fig1c-beta-alpha-peaks` is not reproduced, as only the\ncontrols' mean spectrum has both peaks; `table1-alpha-pac-null` is not\nreproduced, as the null holds under two of the three phase filter readings;\nand `q4-patient-counts` gives 10, 10, 7 and 13 against 9, 8, 8 and 9 (+/- 1).\n`updrs-improvement` gives the paper's W = 3.5, p = 0.0033 exactly. The author\nasked a reader no questions, so the answer run changed nothing. Round 1 gave\nits own outcome for each claim and agreed with 21 of 24; the author took its\noutcomes for `offctrl-steepness` and `table2-alpha-offctrl` (from partially\nreproduced to not reproduced) and `table1-alpha-pac-null` (from reproduced,\nresting on an assumed 192-tap filter, to not reproduced), and its points led\nto the correction procedure sensitivity, CSD spline variants, a PAC variant\nthat drops the filtered edges, per-patient Q4 values and variants without\nsub-pd6 and sub-pd16. Round 2 agreed with all 24, so there was no third round;\nit found statements the outputs did not support, among them a summary calling\nthe statistics close to the paper's, a 5% that is 5.1%, and pd9 listed among\nthe near-axis points that decide Q4 membership where pd5 and pd11 do, and\nthese were corrected. Two questions were put to a reader, on whether the\nexpected statistic counts in `fig2-pac-off-on`, whose criterion contradicts\nitself, and on the missing partial clause of `pac-beta-larger-than-alpha`;\nboth are unanswered, as they were added after the answer step. Some outcomes\nrest on weak ground: `fig2-pac-off-on` would be reproduced if the criterion's\nlast sentence governs; `offctrl-pac-csd` uses MNE's spherical spline on the\nBioSemi 32 template positions, not compared with the MATLAB CSD toolbox; and\nin `q4-patient-counts` 16 of 60 points lie within 0.01 of an axis. The\nauthor's run took about 26 minutes and its only failure was a YAML colon-space\nin the attempt record, which was fixed; the notebook ran in 100 s at first and\n133 s in the last run.\n\nThe manual artifact marks and the list of excluded noisy electrodes that the\npaper's preprocessing used are not in the dataset: every channels.tsv marks all\nchannels good, the events files hold only a start trigger, and the paper's code\nloads the marks from rejectscombined.mat, which is not public, so all analyses\nran without rejection, which the verifiers judged the likely cause of the\nout-of-tolerance W and d values and of the Q4 count gap. The sub-pd16 ses-on\nrecording, which participants.tsv says was exported from a preprocessed EEGLAB\nfile, has electrode standard deviations about six times those of every other\nrecording after the same preprocessing (median 62.6 uV), about 100 times their\npower, and no alpha peak; its channels are not average referenced, and the\ndataset does not say how it was processed or scaled. The sub-pd6 ses-on file,\nalso exported from EEGLAB, is average referenced and lasts 289 s. Without\nthese two patients the steepness and PAC correlation falls within tolerance\nboth off and on medication. The questionnaire fields of the beh JSON files\n(Total UPDRS, UPDRS 18-26 and others) have no description, so \"Total UPDRS\"\nwas taken as the motor examination from its values, which exceed \"UPDRS 18-26\"\nby 1 to 14. The events files hold one trigger (value 1) a few seconds into\nmost recordings, and other values in sub-pd16 ses-on (130817) and sub-pd17\nses-off (a second 65536), and what the trigger marks is not described. The\ndataset holds no digitized electrode positions. The paper gives no filter\nlength for the mu/alpha phase filter of PAC, and alpha PAC off against on is\nnot significant after FDR correction with 192 or 231 taps (0.061, 0.078) but\nis with 118 samples (0.036); this is put to the paper's authors. Table 2 gives\nFDR corrected p = 1 for three tests where Benjamini-Hochberg over its six\ntests gives about 0.36, and Table 3 gives d = 0.75 for PAC in all patients\nwhere Table 1 gives 0.83.\n\nThe author's points on the protocol: it gives no rule for a result that falls\nin a case the criterion does not name, as for the two Table 2 steepness claims\nwith z and d in tolerance and corrected p 0.053; it is unclear which governs\nwhen a criterion's last sentence names fewer values than its expected list;\nthe clock check does not apply to continuous rest data with no trial table, so\nthe Status channel was checked against events.tsv instead; it does not say\nwhat to do when a reading the claims file names has no data, as the dataset's\nown artifact marks here; and step 1.6 does not say how to choose among\nreadings when two of three agree.\n"
}
```

```
File created successfully at: docs/pilot-notes/openneuro-ds002778-jackson-2019-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/openneuro-ds002778-jackson-2019-01.md",
 "old_string": "ran without rejection, which the verifiers judged the likely cause of the\nout-of-tolerance W and d values and of the Q4 count gap.",
 "new_string": "ran without rejection; round 2 judged this the likely cause of the\nout-of-tolerance W and d values and of the Q4 count gap."
}
```

```
The file docs/pilot-notes/openneuro-ds002778-jackson-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -nP "—|rather|\*\*" docs/pilot-notes/openneuro-ds002778-jackson-2019-01.md; git status --short
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
?? docs/pilot-notes/openneuro-ds002778-jackson-2019-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/openneuro-ds002778-jackson-2019-01.md` and changed no other file. ds002778 has no entry in `targets/dandisets.json`, so the note has no CatalystNeuro sentence. One source disagrees with the rest: the author's report says "All 25 claims", while the claims file, the attempt record and both verifiers count 24. I used 24. The new file is:

# openneuro-ds002778, Jackson et al. 2019

Nine claims reproduced, nine partially and six not reproduced, with none
blocked, all on the dataset. It pins version 1.0.5, the latest snapshot, which
holds 46 BDF files at 512 Hz from 15 patients with Parkinson's disease recorded
off and on medication and 16 controls; the paper cites no snapshot, and the
change log shows no change to the EEG files across snapshots. The paper, in
eNeuro, measures the sharpness and steepness asymmetry of beta waveforms and
beta to gamma phase-amplitude coupling (PAC) in resting scalp EEG, and reports
that all three are higher off than on medication at C3 and C4, with mu/alpha
results in Tables 1 and 2 and the shape quadrants of Figure 4. The claims were
written from the version of record in Europe PMC (PMC6553574) and from the
paper's code at SwannLab/Jackson_2019 commit a7c89f50, which starts from
preprocessed MATLAB files that are not public, so every measure was computed
from the BDF files with the Methods' preprocessing. The off against on tests
of shape and PAC, the bipolar and temporalis controls, the topographies, the
off against control tests with the average reference and with CSD, the UPDRS
change, the spectral peaks of Figure 1C, the alpha tests of Tables 1 and 2,
the correlations of Figure 3, the Q4 counts and the effect sizes of Table 3
were tested. The three main off against on tests hold after FDR correction
but each has one value outside tolerance: sharpness d 0.73 against 0.86 +/-
0.086, steepness W 16 against 9 +/- 0.9, and PAC W 13 or 12 against 15 +/- 1.5.
`offctrl-steepness` and `table2-alpha-offctrl` are not reproduced, as z and d
are within tolerance but the FDR corrected p is 0.0531 under every filter
reading, and Holm, Bonferroni and Benjamini-Yekutieli are further from 0.05;
`offctrl-pac-csd` is not reproduced (p = 0.075 against 0.022), and no spline
variant reaches 0.05; `fig1c-beta-alpha-peaks` is not reproduced, as only the
controls' mean spectrum has both peaks; `table1-alpha-pac-null` is not
reproduced, as the null holds under two of the three phase filter readings;
and `q4-patient-counts` gives 10, 10, 7 and 13 against 9, 8, 8 and 9 (+/- 1).
`updrs-improvement` gives the paper's W = 3.5, p = 0.0033 exactly. The author
asked a reader no questions, so the answer run changed nothing. Round 1 gave
its own outcome for each claim and agreed with 21 of 24; the author took its
outcomes for `offctrl-steepness` and `table2-alpha-offctrl` (from partially
reproduced to not reproduced) and `table1-alpha-pac-null` (from reproduced,
resting on an assumed 192-tap filter, to not reproduced), and its points led
to the correction procedure sensitivity, CSD spline variants, a PAC variant
that drops the filtered edges, per-patient Q4 values and variants without
sub-pd6 and sub-pd16. Round 2 agreed with all 24, so there was no third round;
it found statements the outputs did not support, among them a summary calling
the statistics close to the paper's, a 5% that is 5.1%, and pd9 listed among
the near-axis points that decide Q4 membership where pd5 and pd11 do, and
these were corrected. Two questions were put to a reader, on whether the
expected statistic counts in `fig2-pac-off-on`, whose criterion contradicts
itself, and on the missing partial clause of `pac-beta-larger-than-alpha`;
both are unanswered, as they were added after the answer step. Some outcomes
rest on weak ground: `fig2-pac-off-on` would be reproduced if the criterion's
last sentence governs; `offctrl-pac-csd` uses MNE's spherical spline on the
BioSemi 32 template positions, not compared with the MATLAB CSD toolbox; and
in `q4-patient-counts` 16 of 60 points lie within 0.01 of an axis. The
author's run took about 26 minutes and its only failure was a YAML colon-space
in the attempt record, which was fixed; the notebook ran in 100 s at first and
133 s in the last run.

The manual artifact marks and the list of excluded noisy electrodes that the
paper's preprocessing used are not in the dataset: every channels.tsv marks all
channels good, the events files hold only a start trigger, and the paper's code
loads the marks from rejectscombined.mat, which is not public, so all analyses
ran without rejection; round 2 judged this the likely cause of the
out-of-tolerance W and d values and of the Q4 count gap. The sub-pd16 ses-on
recording, which participants.tsv says was exported from a preprocessed EEGLAB
file, has electrode standard deviations about six times those of every other
recording after the same preprocessing (median 62.6 uV), about 100 times their
power, and no alpha peak; its channels are not average referenced, and the
dataset does not say how it was processed or scaled. The sub-pd6 ses-on file,
also exported from EEGLAB, is average referenced and lasts 289 s. Without
these two patients the steepness and PAC correlation falls within tolerance
both off and on medication. The questionnaire fields of the beh JSON files
(Total UPDRS, UPDRS 18-26 and others) have no description, so "Total UPDRS"
was taken as the motor examination from its values, which exceed "UPDRS 18-26"
by 1 to 14. The events files hold one trigger (value 1) a few seconds into
most recordings, and other values in sub-pd16 ses-on (130817) and sub-pd17
ses-off (a second 65536), and what the trigger marks is not described. The
dataset holds no digitized electrode positions. The paper gives no filter
length for the mu/alpha phase filter of PAC, and alpha PAC off against on is
not significant after FDR correction with 192 or 231 taps (0.061, 0.078) but
is with 118 samples (0.036); this is put to the paper's authors. Table 2 gives
FDR corrected p = 1 for three tests where Benjamini-Hochberg over its six
tests gives about 0.36, and Table 3 gives d = 0.75 for PAC in all patients
where Table 1 gives 0.83.

The author's points on the protocol: it gives no rule for a result that falls
in a case the criterion does not name, as for the two Table 2 steepness claims
with z and d in tolerance and corrected p 0.053; it is unclear which governs
when a criterion's last sentence names fewer values than its expected list;
the clock check does not apply to continuous rest data with no trial table, so
the Status channel was checked against events.tsv instead; it does not say
what to do when a reading the claims file names has no data, as the dataset's
own artifact marks here; and step 1.6 does not say how to choose among
readings when two of three agree.

## End of run

12 turns, 1 minutes, result: success.
