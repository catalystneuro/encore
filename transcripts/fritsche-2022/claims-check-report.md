The checker passed and the file is ready for an attempt. The only change on disk is to `claims/fritsche-2022.yaml`; nothing is committed.

**Checker result:** `claims/fritsche-2022.yaml: 31 claims, 31 quotes, 81 statistical values, 0 problems`. Before my changes it was 29 claims, 29 quotes, 80 values, 0 problems. I ran it against `paper/10.1523-jneurosci.1350-21.2021.txt`; there is no `paper/fritsche-2022.txt`.

**What held up:** I checked every expected value and tolerance against the text, Table 1 and Table 2. Each tolerance is the larger distance from the value to a CI bound, or 10% where the paper gives no interval. Ranges are widened by 10% of each bound. No statistic is a threshold used to count units, and no claim comes from outside this paper.

**Changes, by claim:**
- **Header, open detail O4:** how the preferred orientation is chosen is now named as open, with two readings: the best orientation pooled over directions and temporal frequencies, or the orientation of the single best condition. The Methods say only "eliciting the highest firing rate", and the file had silently picked the first.
- **fig3a-v1-half-life:** the statement no longer says the ~14 s half-life belongs to the slow V1 component. The Discussion doesn't say which component or area it is; that is now marked as a reading.
- **table1-extrastriate-tau-slow:** the statement now uses the paper's words, "slowest in V1" and "relatively similar", in place of "close to V1's". The criterion also reports whether V1 has the largest slow time constant.
- **fig2-v1-adaptation-at-all-orientations:** which tests the multiple-comparison correction covers is now open, with two readings: the nine V1 cells, or every cell in Figure 2D to 2F.
- **fig8-no-spurious-long-term:** the range of n-back positions is now open (2 to 10, or 2 to 50); the old criterion had no upper bound. The simulated neuron's 1-back ratio is now that stimulus set's own V1 ratio.
- **New, fig7b-static-areas-long-term:** after static gratings, cortical areas adapt up to 20 trials back and the thalamus less so (Fig. 7B). This finding had no claim.
- **New, fig7c-static-long-term-across-mice:** long-term static adaptation is consistent across mice (Fig. 7C). This was missing, while the matching Figures 1E, 3C and 6D each have a claim.

**Still open (recorded under `checks`):**
- The model equations, including the sign of the double exponential's second term, are not in the text under `paper/`. The writer read them from the PubMed Central page, so I couldn't check them. The criteria run both sign readings, so no outcome depends on this.
- The paper's analysis code is reported as access-restricted and was never read. The open details O1 to O6 therefore stay open.
- In the static-grating results, the LGN and LP ratios (0.93, 0.85) sit exactly on the lower edges of their printed confidence intervals. The writer's rule for this, which widens each interval down to the value minus 10%, is not from the paper. I kept it with its stated reason.

`git status` also lists untracked files I didn't create (`.bashrc`, `.idea`, `scripts`, and others). I left them alone.
