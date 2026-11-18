I checked the claims file against the paper and fixed seven things. The file is ready for an attempt.

**Checker result:** `claims/gonzalez-cabrera-2026.yaml: 41 claims, 41 quotes, 34 statistical values, 0 problems`. I ran it before and after my edits and got the same line both times.

**Changes, by claim:**
- **Header, photometry controls:** the file described the control mice's viruses wrongly. I replaced it with the list the Methods give (the PnO retroAAV, Flp-dependent Chrimson and AAV-EF1a-DIO-HDM4-mCherry in VTA).
- **fig1a-gad2-long-range-projections:** the criterion required labelling above background in every animal, which the paper never says. It is now judged on the mean across animals, which is how the Methods summarise the data. The zero threshold is marked as the reader's choice, since the paper gives no test.
- **fig1e-spike-duration:** the criterion stated the post hoc test as pairwise t-tests. The legend only says "FDR-corrected post hoc tests", so that is now marked as a reading.
- **fig2e-somatic-backward:** the speed gate was given in pixels per frame. The Methods say "units·frame⁻¹", so pixels is now marked as a reading.
- **fig2f-somatic-bins:** the post hoc test had no source. It is now cited to the paired tests in Methods, "Open-field video", with Wilcoxon signed-rank as the variant those Methods name.
- **fig2h-terminal-backward:** the return to baseline was judged by a ±2 s.e.m. band the first reader made up. The paper has its own test for that bin (Fig. 2i, p = 0.33), so the claim now uses it.
- **fig3g-firing-rate-no-difference:** the statement said the two firing rates were "the same". The paper only reports a non-significant Mann-Whitney test, so it now says they do not differ and gives both means.

Everything else held up: all quotes, p-values, the confidence interval, every n and expected value, and the readings already given for details the paper leaves open. Each main finding has a claim, and every claim comes from this paper.

**What remains open** (recorded under `checks`):
- I did not reread the paper's GitHub code. The header's account of it, and the criterion details taken from it, are as the first reader wrote them.
- There is no PDF, so no figure panel was seen. The claims rest on the text and the figure legends.
- The Results say VTA-PnO units have low-jitter tagging latencies and DA units more variable ones. The paper gives no number for this, so it has no claim of its own.

Only the claims file was changed, and nothing was committed or pushed.
