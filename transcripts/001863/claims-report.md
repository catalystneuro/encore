I wrote `claims/001863/10.1101-2025.07.09.663970.yaml`. The quote checker reports 35 claims, 35 quotes, 43 statistical values and 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, full text from its JATS XML: Results, figure legends, Discussion and Methods. There is no separate supplement file, but the legends of all the supplemental figures are in the text and I read them. No PDF was supplied and none was needed. Nothing the claims rest on is missing.

**Code read:** github.com/Smear-Lab/Olfactory-search-on-psychedelics at commit aa80af0a. The paper itself links only the rig documentation. This repository is the authors' code: the dandiset description names it, and its README names the paper. It holds R Markdown files with each figure's statistics (`fig1_cleaned.Rmd` to `fig5_cleaned.Rmd`), a MATLAB occupancy plotting script, the task software and the NWB conversion script. Some inputs those files read were made by code that is not in the repository: the reward-port durations, the sniff inhalation times and the DeepLabCut (pose-tracking) tracks. The code fixes the mouse and session list (22 mice, which session was DOI and which saline), the 40-trial minimum per session, the rolling accuracy measure, the speed pipeline (80 fps, 0.0237 cm/pixel, 160 cm/s cutoff) and the head-twitch (HTR) spatial permutation statistic.

**Claims:** 35, all with quotes. 33 have statistics, all 35 have criteria, and 4 have expected values.

**Where the paper disagrees with itself:**
- **Speed tests:** the Results name the Wilcoxon rank-sum test for the speed comparisons (Figure 3C, 3D and supplement). The Methods and the code use the paired signed-rank test. The Methods decide, and rank-sum is shown as a variant.
- **Sniff limits:** the Methods print them as "10 s" and "1000 s". I read them as milliseconds.
- **HTR scoring:** the Methods say HTRs were marked by hand. The code also reads HTR times from a folder it describes as automated detection.

**Details left open, with the readings named:**
- **Trials completed (1D, and 1D by sex):** the code counts odor trials only, the Methods count all trials. Both are named readings.
- **False odor reports in the ITI:** the code does not compute them. The measure is either a count per session or that count divided by the number of ITIs.
- **Which reward-port entry counts (Figure 2):** the first entry after the trial's response, or the first entry within the 5 s reward window.
- **Sex test for Figure 2A:** the test is not named. It is either the code's Kruskal-Wallis test or Bonferroni-corrected pairwise rank-sum tests. If they disagree, the claim is blocked as underspecified.
- **Sniff exclusions:** the 5th and 95th percentile cut is read per session, and the duration limits in milliseconds. If the dataset holds only the raw thermistor signal, the peak-detection settings are open. Which sessions count as usable: the code drops four by name, and the counts are checked against 14 DOI and 13 saline.
- **Occupancy "similar" (Figure 5A, B):** the paper gives no test. I took the measures from the prediction the paper says it tested: the entropy of each mouse's occupancy map, and the fraction of time in the corners. The corner size is not given, so 5 cm and 10 cm squares are named, and both sizes are my own choices. Each is compared with the paired signed-rank test. If the measures disagree, the claim is blocked.
- **HTR position during the ITI:** the paper gives no test and the code runs none. The within-trial permutation test is applied to ITI frames, which is what the paper's "Similarly" implies.
- **Figure 1C bins:** the 0 to 10 min and 25 to 30 min bins are not reported separately in the text. They are reported but not judged.

**Missing from the paper:** no claim lacks something it needs from the paper. The ITI false-report measure, the reward-port duration files and the sniff preprocessing are not in the code, so those claims rest on the Methods text alone.
