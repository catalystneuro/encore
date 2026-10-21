# 002010 · claims-check · run 39534268766

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/002010/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; ls claims | grep 2010; git show --stat HEAD | head -30
```

```
- `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/002010/claims-report.md; ls claims/ | head; git log --all --oneline -- 'claims/002010*' | head; ls transcripts/002010
```

```
I wrote no claims. The paper's text is here, but the supplement that its statistical results rest on is missing, so under the Reader section, step 1, I stopped.

**Text read:** `paper/10.1101-2023.04.19.537568.txt`, the bioRxiv preprint (version 1, from the JATS XML). It has the main text, the Methods, the figure legends and the figure supplement legends. There is no PDF and no supplement file (`papers/manifest.yaml` lists `supplements: 0`).

**What is missing:**
1. **Supplementary Tables S1 to S18.** The paper puts the statistical results of almost every finding in these tables. The text and legends only point to them ("Table S3 for statistical details", and so on). Examples:
   - Fig. 2b stride-velocity t-tests (S2).
   - Slomo, shuffle and fast signature F-tests (S3, S8, S12).
   - EMG tests (S4, S10, S13) and the Z-score correlations (S5).
   - Laterality tests (S7, S11) and motor tests (S6, S9, S14).
   - Bouton counts and sensory tests (S15 to S17) and optogenetics (S18).
   - Dose and time titration (S1).

   Without them, no claim could have the paper's statistics or reported values, beyond a few numbers in the text (such as p 0.016 for lamina III boutons).
2. **The Z-score equation in the Methods** (section "a) Group definition"). The text breaks off at "Z-scores of the change in gait metrics were then calculated as follows:" and the equation is gone, probably an image that the XML extraction dropped. Every subgroup in the paper (slomo, shuffle, fast, and their opposites) is defined by Z_SwT or Z_StrV thresholds, so no criterion could fix how mice are grouped.
3. **Figure 7-Figure supplement 3:** the legend is cut off after its title.

**To proceed:** someone needs to add the bioRxiv supplementary file with Tables S1 to S18, and the preprint PDF so the Z-score equation can be read. A reader run can then write the claims. Because I stopped, I did not read the linked code (the two SourceForge projects, gait-analysis-gui and gait-emg-step-trigger).

**Counts:*
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i "calculated as follows" -A4 *.txt; grep -o -i "table S[0-9]*" *.txt | sort | uniq -c | head -30; grep -n -i "supplementary table\|supplementary information" *.txt | head
```

```
408 10.1101-2023.04.19.537568.txt
279:a) Group definition based upon gait phenomenology: To define subgroups that represented mice with similar direction and degree of gait changes, we calculated gait metric Z scores based upon each animal’s difference in performance between baseline and CNO, with each animal serving as its own control. This approach is conservative and limits random effects of mouse line, size and age. Scores were based on swing duration in the VGaT and VGluT2 cohorts: Differences between conditions in the corresponding WT groups defined the population averages, and Z-scores of the change in gait metrics were then calculated as follows: In the SerT cohort, we used speed, rather than swing time as the primary metric to define subgroups as there were no obvious swing time changes in this group. In addition, we calculated Z-scores for each of the other motor tests to determine whether changes in gait and other motor tests correlated and came from the same manipulation site.
280-
281-b) Video gait analysis: We used a validated approach ( 36 , 38 ) to answer the question whether there is evidence that the CNO treatment shifted gait curves or signatures from saline baseline in the same mice. In other words: do the best-fit values of unshared baseline and CNO gait parameters differ between data sets? For each stride we measured swing and stance durations based on the number of video frames and stride length based upon spatial coordinates using MATLAB. We then visualized these metrics as a function of the velocity of the stride. We derived cadence (1/cycle duration; cycle duration being the sum of stance and swing durations) from these measures, which we then also plotted against stride velocity. We also plotted stride length against swing speed as relevant for the swing phase. This data was then fitted to a curve using the simplest best fit model that was established for the respective gait metric within the speed bin that covers walking and diagonal trot
[... 24 more lines not kept]
```

**Agent**

There's no claims file to check. `claims/002010/` doesn't exist, and nothing has ever been committed there on any branch. So I didn't run `tools/claims_check.py`, there was nothing to correct, and I wrote no `checks` entry.

**Why there's no file.** The earlier reader run (`transcripts/002010/claims-report.md`) stopped at Reader step 1 and wrote 0 claims. It said the supplement and part of the Methods were missing. I checked that against `paper/10.1101-2023.04.19.537568.txt` and it holds:
- **Supplementary Tables S1 to S18 aren't in `paper/`.** The text points to them about 60 times for its statistics ("Supplementary Table S18", "Table 15S", and so on). There's no supplement file and no PDF.
- **The Z-score equation is gone.** At line 279 the Methods say "Z-scores of the change in gait metrics were then calculated as follows:" and the next sentence starts straight after, with no equation. Every subgroup in the paper (slomo, shuffle, fast and their opposites) is defined by Z_SwT or Z_StrV thresholds, so no criterion could say how mice are grouped.
- **The legend of Figure 7-Figure supplement 3 is cut off after its title**, as the reader reported. I did not check this one.

**What remains open.** Someone needs to add the bioRxiv supplementary file (Tables S1 to S18) and the preprint PDF, so the equation can be read. After that, a new claims run can write the file and a claims-check run can check it. The paper's code (the two SourceForge projects, gait-analysis-gui and gait-emg-step-trigger) hasn't been read yet either.

**Ready:** no, since there's no file.

## End of run

5 turns, 0 minutes, result: success.
