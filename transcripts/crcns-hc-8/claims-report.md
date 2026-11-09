I wrote `claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` with 27 claims, and all 27 quotes pass `tools/claims_check.py` with 0 problems.

**What I read**
- **Paper:** the version of record (PMC5037237), the Methods 2.1 to 2.11, the Results, the Discussion and all the figure legends.
- **Supplement:** Data_Sheet_1, Figures S1 to S9 with their text.
- **Equations:** the supplied text leaves out Equations 1 to 14. I took them from the MathML in the PMC XML (fetched through NCBI eutils) and copied the ones the criteria use into the opening comment.
- **Code:** the paper links code only as "http://www.nicholastimme.com". From that site I read NCC Toolbox Version 1 (June 2016); its sha256 is recorded in the file. It holds the toolbox functions but not the scripts the authors ran on the cultures, which are not published.

**Counts**
- 27 claims, all with quotes. 9 are simulations (chain model, Bethe lattice, cortical branching model) and 18 use the culture data.
- No statistics are recorded. The paper prints no p-values; Figures 10 and 11 give only a star key (rank sum test with false discovery rate control), and the stars themselves could not be read.
- 7 claims have expected values: the peak at p_trans 0.265, the all-time-bins peak at 0.28, the counts of 435 recordings and 39,529 neurons (tolerance 0, since they are exact properties of the data), about 100 neurons per recording, ISI about 7 ms, about 10,000 avalanches, and the correlations 0.23, 0.296 and 0.197.
- All 27 claims have a criterion.

**Where the code settled a choice**
- The occurrence cut drops each size or duration value seen fewer than 20 times, one by one (as the toolbox demo does).
- Power-law fit ranges are searched largest first; surrogate count 500, acceptance at p of 0.2 or more.
- The complexity correction subtracts data randomized by permuting each neuron's time bins, then cuts at the first peak.
- The shape collapse searches 1/σνz from 0 to 4 at 0.001 precision.

**Details the paper leaves open, with the readings named**
- **Model p_trans grid:** the Methods print "increments of 0.05", which gives three values and cannot place a peak at 0.265. Readings: steps of 0.005 or 0.01.
- **Sub-sampling layout:** either 30 sub-samples at evenly spaced sizes, or 30 at each size from 40% to 100%.
- **Excluded recordings:** the "too few avalanches" threshold is not stated. Readings: exclude recordings where the size, duration or shape-collapse cuts leave nothing, or keep all.
- **False discovery rate method:** the paper cites both Benjamini-Hochberg and Benjamini-Yekutieli.
- **Susceptibility:** Eq. 14 as printed, var(A/N), or N·var(A/N). The second fits the 0 to 5 axis of Figure S8.
- **Curvature sign:** the code's 2a is negative for arched profiles, but the paper reports positive values. I used the absolute value.
- **Basic branching ratio:** I followed the Methods, Eq. 11, the time average of A(t+1)/A(t). The code computes a regression slope instead, which is shown as a variant.
- **"Slightly below 1":** within 0.05 or within 0.1 of 1.
- **"Strong" correlation:** read as Pearson r ≥ 0.7, with Spearman as a variant. This threshold is my choice, and the criterion says so.
- **"Most ... around":** the median or the histogram mode.
- **Smaller choices:** rounding the ISI bin, the number of Bethe lattice runs, and how to measure the curvature of the Figure 6 distributions. These are marked as standard choices or as measures the paper does not define.

**Missing from what was supplied**
- There is no PDF of the main article. So the per-exponent means and SDs in Figure 8, the Figure 9 histograms, the significance stars of Figures 10 and 11, and the list of excluded recordings in Figure 2B are unread. The claims on those figures are judged by direction only, with no numeric targets. Supplying the main PDF would let a reader add those values.
- The equations are missing from the supplied text, as noted above.

Nothing is committed.
