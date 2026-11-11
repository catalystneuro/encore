I've brought `claims/kim-2022.yaml` up to the current protocol (pilot-14). The quote checker passes with 0 problems, and nothing is committed.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC9729435, NIHMS1849847), not the version of record. It has the Methods 2.1 to 2.6, the Results 3.1 to 3.5, the Discussion and the legends of Figs. 1 to 7. The paper has no supplement, and none was supplied. There was no PDF, so I read no figures. The paper links no code and no data deposit, so I read no repository.

**Counts.** There are 24 claims. All 24 have quotes and criteria, 5 carry statistics (7 values), and 9 have expected values.
- **000489:** the 6 claims on Fig. 2 rest on it, since its title is the Fig. 2A legend.
- **000448:** the 5 claims on Fig. 7 rest on it, since its title is the Fig. 7 legend.
- **Figs. 3 to 6 and the Fig. 1E heating (13 claims):** neither dataset's title names these data. I listed them under 000489, the YO-PRO-1 dataset from the same cells and measure. The opening comment says the author must check whether 000489 holds them; if it does not, they are blocked as `data_missing`.

**What changed**
- The top-level `dataset: 000489` is gone, as the schema requires for a paper's own claims file, and every claim now has `datasets:`.
- I added two Fig. 7 claims: `fig7-unipolar-pole-polarization` and `fig7-later-pulses-same-tau-difference`. The second is a "data not shown" finding that 000448 can test.
- The claims of absence (fig2b slope, fig2c flat, fig3d, fig4ac field independence, fig5 symmetry, fig6 same efficiency, fig7 same initial polarization and no build-up) are now judged on a single test: the paper's unpaired two-sided Student's t-test at p < 0.05. The paired test is shown as a variant.
- Where readings are method choices and give different outcomes, the author now picks one or blocks the claim as `methods_underspecified`. Before, the file declared that outcome directly. Readings of what a reported number means still need only one match.
- fig4eg now has a stated rule for which ROI count as measurable uptake, and two readings of what the p < 0.01 covers. fig4d's statement no longer says "a tenth of unipolar".
- I removed the old `checks` block. Its last entry said `ready: true` about the previous version, so the new file needs a fresh check.

**Details the paper leaves open, and the readings named**
- **ROI spacing and count along bb' and aa':** ROIs tiled from the centre on both sides, or on one side only. A named field strength is taken from the ROI closest to it.
- **Paired or unpaired t-test for comparisons within the same dishes or cells:** both are run. For claims of absence the unpaired test decides.
- **Grapher fitting:** nonlinear least squares, or regression on log values. Fits to means, or to each dish.
- **Fig. 4 and Fig. 6 fit type** ("either exponential or polynomial"): exponential for all, polynomial for all, or the better fit per curve.
- **Background cutoffs:** Fig. 2B "6-8 kV/cm" uses 8, with 6 and 7 as variants. For Figs. 3, 4 and 6 the Fig. 3 cutoff is read as 7 or 8 kV/cm. Microsecond pulses have no cutoff, so the file uses ROIs where unipolar YP is above zero by more than its s.e.m.
- **Which "~20%" (fig2c):** the mean over 8.7 to 15.1 kV/cm, or the lowest value in that range. The p < 0.01 is read as against unipolar, or against 25% and 100%.
- **What "moderate" field means (fig4d):** the lowest value of the ratio curve, or the ratio mid-range.
- **What "high-frequency" means (fig6cf):** 833 kHz only, or every kHz rate.
- **"30-50%" and its p < 0.01 (fig4eg):** the mean over the range or the whole curve; tested at most ROIs or on summed dish values.
- **The 425 fitted points (Fig. 7):** per-cell points pooled, or the trace averaged over cells.
- **Fig. 7 sign:** which direction of emission change means depolarization is fixed from the data itself. "Mirroring" is given a tolerance of the file's own: anodic size within half to twice the cathodic.

**Missing from the paper.** These gaps affect claims:
- The paper gives no data location for Figs. 3 to 6 or the heating photographs, and neither dataset's title names them.
- The finite element field model behind each ROI's field strength is not deposited. Its geometry is in Methods 2.3, so the author can recompute it.
- The paper links no code.
- Several findings (fig2a, fig3d, fig4h, fig6cf trend, the fig7 sign tests) have no reported test. Their criteria apply the general Methods 2.5 t-test, and the file says so.
