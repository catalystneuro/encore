I wrote `claims/jones-2019.yaml`. The quote checker passes it: 65 claims, 65 quotes, 110 statistical values, 0 problems. Nothing was committed.

**Text read:** the version of record, with its supplement (Figures S1 to S4, Tables S1, S3 and S4) and Table S2 from the xlsx. I opened the PDF only to read R and p values printed inside figure panels, and the directions in Figures S3 and S4. Those values are marked "read from the panel". I also read the paper's code, emilyasterjones/SWR-predictions at commit ca056a8. Nothing a claim needed was missing.

**Counts:** all 65 claims have quotes, so none needed an `inferred` note. 56 have statistics and every claim has a criterion. 12 are claims of absence, each judged on the paper's own test.

**Details the paper leaves open, and the readings named:**
- **Ripple threshold:** the Methods say above 5 SD for 15 ms. The code detects above 3 SD for 15 ms and keeps events peaking at 5 SD. The Methods are the main reading and the code is the variant.
- **Slow gamma (SG) power:**
  - The code triggers on all events above 3 SD; the Methods and Table S2 use the 5 SD events.
  - The code's frequency bins include 54.7 Hz; the Methods' 30 to 50 Hz does not.
  - The Methods average per session and then over sessions; the code pools all events.
- **Z-score population for the performance scores:** either the apoE4-KI mice in the correlation, or all mice of the cohort.
- **Metrics in the APA learning score (Fig 3F):** two metrics in the text, three in the Methods.
- **MUA baseline:** either the whole 400 ms before detection, or the bin from -400 to -300 ms.
- **Cohort comparison (0.12 vs 0.20 Hz, 16.2 vs 11.5 µV):** the text doesn't say which cohort is which, or which mice the baseline t(25) covers.
- **Day 1 vs day 2 variance in APA shock-zone entrances:** which mice are included.
- **"This cohort" in the age claim:** the screen or the replication cohort.
- **Fig S3G test:** the df of 44 suggests ANOVA post hoc tests, but separate t tests per day are also possible.
- **Holm-Sidak families:** these are not stated. I found the family that reproduces every printed adjusted p from the printed F values (one per SWR property's planned metrics) and fixed that in the file.
- **Significance in the replication cohort:** read on unadjusted p. The paper calls every replication significant, but several adjusted p are above 0.05.

**Inconsistencies in the paper, recorded in the criteria:**
- The 9-of-88 binomial test prints p < 0.00032, but the test that reproduces the other two binomial values gives 0.032.
- Fig 2I says 77% of variance, but its R and F both give 71%.
- The panel R values in Fig 2M and S1G don't fit their F and p, so I used the R implied by F.
- Fig 4I prints F(1,8) for n = 11.
- The Fig S1J legend gives F = 0.80 where Table S2 implies about 0.08.
- In the text "R = 0.2, F(1,12)" for apoE3-KI mice, F(1,12) needs 14 mice but only 9 have the measure.
- The Results say young CA3 SG power predicts "entries" into the shock zone, but Figure 4J and Table S4 show latency to first entrance; I followed the figure.

Untracked dotfiles such as `.bashrc` and `.mcp.json`, plus `scripts/`, have appeared in the repo root. I didn't create them and left them alone.
