The file for DANDI:001474 is ready for an attempt. I made four changes, and two problems remain open but don't block it.

**Checker result:** `claims/001474/10.1038-s41598-025-19800-2.yaml: 37 claims, 37 quotes, 13 statistical values, 0 problems`. There were 14 statistical values before the fig2b change below.

**Changes, by claim**
- **fig2b-meal-size:** I removed the statistics entry `p < 0.05`. It was the paper's significance cutoff, not a reported result. The text never calls the difference significant, and the p-value appears only in the figure. The criterion now says this.
- **supp1e-hfd-less-locomotion:** The criterion used the whole 60-s trial as the running-speed window, which is not in the paper. It now runs two windows: the whole trial and the 10 s before the cue, which is the pre-cue period of Supp. Fig. 2g. If the two give different outcomes, the claim is blocked as `methods_underspecified`.
- **supp3c-ncd-hfd6w-dynamics-retained:** The statement said the early-to-late increase was significant both before and after the switch. The paper calls only the after-switch increase significant, and says the change before was "comparable". I reworded the statement to match. The criterion now says that testing the before-switch phase is one reading of "comparable".
- **supp3q-hfd-ncd-weight-loss-meal-length:** For "no correlation with neural responses", the text means correlation with weight change. But it cites Supp. Fig. 3p, whose legend correlates mid-meal response with meal size. The criterion now runs both.

**Open**
- I could not read significance marks that appear only in figures. The supplementary PDF does not render here because the PDF renderer (pdftoppm) is not installed, and the main figures are not available. So four criteria require p < 0.05 only because the legend names a test: fig1l, fig2c, fig2d and fig3h. The paper's text never gives those results.
- Three method details have no source in the paper or its code:
  - the rolling-SD window for supp2j, given as readings;
  - the rule for when licking starts to decline in fig2e, given as readings;
  - the cutoff |r| < 0.5 that supp2j uses for "weak", which is one fixed reading of that word.

Every main finding has a claim, and every claim comes from this paper. Under `claims/001474/` I edited only the claims file, and I did not commit. The repository root has untracked files I did not create, such as `.bashrc`, `.idea` and `scripts`. I left them alone.
