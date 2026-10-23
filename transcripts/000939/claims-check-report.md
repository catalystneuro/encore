The claims file for 000939 is ready for an attempt. I corrected eight things across seven claims and the opening comment, and four problems stay open.

**Checker:** `claims/000939/10.1038-s41593-024-01588-5.yaml: 34 claims, 34 quotes, 9 statistical values, 0 problems`. I got the same result before and after my edits.

**How I checked:** I read the whole paper text, including the Extended Data legends and the Supplementary Methods. I also downloaded the paper's MATLAB code and session lists from figshare to check what the file says about the code. Their md5 sums match the ones the file records. All seven code-versus-Methods disagreements the opening comment lists are real.

**Changes, by claim**
- **fig3e-fourier-signatures-differ:**
  - The file called cell type a between factor. The code enters it as a number (1, 2, 3), and only that gives the paper's F(9,19116). A categorical factor would give (18, 19107). The numeric coding is now the main reading and the categorical factor a variant.
  - Which components count as "low" and "high" was the first reader's own choice. It is now one named reading. A second reading comes from the cumulative signatures in the Fig. 3e inset, and the direction must hold under both.
- **ed4a-autocorrelogram-symmetries:** The "mean of 120° and 240°" was made up. The code tests the value at 120° for threefold cells (and 180° for twofold cells), so that is now used. The code runs a rank-sum test where the legend names a signed-rank test; the rank-sum is now a variant.
- **fig2f-cue-rotation:** The criterion cited the code for an exclusion rule the code does not use. The code excludes an epoch if any of three conditions holds: mean decoder error changes by less than 45°, error variance is above 10, or angular head velocity is below 10. It has no speed condition. This is now named as a variant.
- **fig1ac-posub-border:** The Mann-Whitney test and the "border placed by the code" were made up. The paper gives no test and the code draws no border. The criterion now uses the code's running average, and the step is judged by eye and reported as such.
- **fig5b-posub-rates-increase:** The statement said PoSub-HD rates rose compared with control mice, but that test is not significant in the paper (z = 1.69). It now says both cell types' rates rose and only the FS rise exceeds control.
- **ed7gj-tuning-preserved:** The reading of the legend's n = 52 as the 83 ArchT PoSub-HD cells, and the unsmoothed FS correlation over all 47 cells, are now tied to the code. The code's rank-sum test for tuning widths is named as a variant.
- **Opening comment:** I added two disagreements to its list: the cue-rotation exclusion rule and the Extended Data Fig. 4a test.

**Open**
- **fig1ac-posub-border:** The paper gives no test, so the outcome rests on judging the plotted profile by eye.
- **fig4-random-connectivity-simulation and fig4h-model-fit:** These depend on Python code the authors did not deposit, so they stay untestable.
- **ed6-trn-innervates-adn:** The anatomy images are not deposited, so it stays untestable.
- **fig3h-dominant-component:** "Similar" is judged with the protocol's default 10% tolerance, not a number from the paper.
- **fig5e:** The legend gives n = (83, 52). The criterion reads the FS count as 46, from the Methods' exclusion of 1 of 47 FS cells, but the text cannot confirm that reading.

Every main finding has a claim, and none comes from outside the paper. The `checks` entry is appended with 13 lines and `ready: true`. Nothing is committed.
