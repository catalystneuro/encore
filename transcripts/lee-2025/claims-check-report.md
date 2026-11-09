The claims file for DANDI:001195 is fit for an attempt, and its new check entry says `ready: true`. The checker's last result is: `38 claims, 38 quotes, 80 statistical values, 0 problems`. The file had 71 statistical values before; I added 9.

**Changes, by claim**
- **fig6no-cea-clusters**: Figure 6L shows the max-min normalised features on a 0-100 scale. That explains why the dendrogram reaches 200, so I removed the made-up reading with no normalisation. Proportions now count every cell in a cluster, because the Figure 6O pie charts include cells with no response.
- **fig6pq-blp-clusters**: The file counted only cells with a response. The Figure 6Q pies include non-responding cells, and 93% and 62% only fit 13 of 14 and 8 of 13 cells (27 in all) when every cell in the cluster is counted. I corrected the denominators and removed the no-normalisation reading here too.
- **fig6-s1ln-combined-clusters**: The 80% agreement threshold was the writer's own choice. I replaced it with the response pattern per region and cluster that Figure 6 supplement 1N shows.
- **fig7e-no-behavioural-change**: The statement said the parameters were "tuned so that" preference did not change; the paper only says changes were "minimized". It now says no significant difference. I also added the Geisser-Greenhouse correction, which the paper's fractional degrees of freedom imply.
- **fig7j-proportions-unchanged**: The source now also cites Figures 7G and 7K-L. The paper names no test for the per-mouse proportions, so I added the test its statistics section prescribes for three or more groups (repeated-measures ANOVA, or a mixed-effects model when a mouse misses a session), next to Kruskal-Wallis. I also added a reading for the "response strength" part of the statement. That part conflicts with the paper's own significant Kruskal-Wallis test in Figure 7H, and the criterion now says so.
- **fig7i-little-overlap**: "recruits" became the paper's "may recruit".
- **fig7m** and **fig7-s1no**: In Figure 7 supplement 1N and 1O, the two GH off p-values are swapped between the panels. Every printed r and p fits 10, 9 and 10 mice, not the printed N of 9, 8 and 9. Also, r = 0.679 with p = 0.045 in Figure 7M fits 9 mice. Both criteria now record this.
- **fig7-s1ef-red-vs-blue**: I added the four post hoc results from the legend. The file had picked one way of giving a single amplitude to a mixed potential; I named this as open, with two readings.
- **fig3a-c-epm-no-effect** and **fig3-s1-oft-no-effect**: I added the CeA and BLP interaction tests for the elevated plus maze, and the three distance-travelled tests the statement already covered.
- **fig4k-cea-face-investigation**: Noted that t(22) on a paired test implies 23 mice, while the legend says 22.
- **fig8d-cea-inhibition-rank**: Added a criterion noting that r = -0.500 with N = 20 gives p = 0.025, not the printed 0.0414.

**Still open** (each stays as named readings in its claim)
- How large a deflection must be to count as an EPSP or IPSP (fig6df).
- The linkage method of the MATLAB clustering (fig7-s2).
- The CellReg parameters; the defaults are used and stated as a choice (fig7i).
- The cup-interaction geometry and the time base (fig7gh).
- The paper links no analysis code, and the Figure 7 legend for panels J to M is missing from the PDF itself.
- The null correlations with social dominance (Figures 2H-J, 3D-F, 3J-L and 4M-O) have no claims. I judged them secondary. Every other main finding has a claim, and all claims come from this paper.

The only tracked change is the claims file. Some untracked files in the repository root (dotfiles, `.idea`, `scripts`) were not created by me and are left alone. Nothing was committed or pushed.
