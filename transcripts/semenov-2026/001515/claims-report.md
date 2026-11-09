I wrote the claims file for 001515 and did not commit it. It is `claims/001515/10.1016-j.bioelechem.2026.109283.yaml`, and the quote checker reports 34 claims, 34 quotes and 0 problems.

**Text read:** the version of record, from the supplied PDF's text extraction: main text, Methods, Results, Discussion and the legends of Figs. 1 to 7. The paper names no supplement and links no code ("Data will be made available on request"). Its analysis used MetaMorph, an Excel macro, Grapher and Origin, none of them published, so there was no code to read.

**How the file was built:** I started from the checked 001516 file for the same paper. I checked every claim, quote, statistic and criterion against the paper and kept them where the paper supports them. I added two claims:
- `fig1-schwan-pattern` (Results 3.1): below threshold the cathode-facing pole depolarizes and the anode-facing pole hyperpolarizes, polarization falls toward the equator, and it scales with field strength.
- `fig4b-poles-alike-570-780` (Results 3.4): the two poles are about equally permeabilized at 570 and 780 V/cm.

**What the dataset matches:** its title and description (charging and discharging during 1-µs pulses, versus cell size and field strength) point at the single 1-µs pulse experiments: Figs. 1, 2A/B, 3, 4A to C, and perhaps the Fig. 5A controls. This paper images only at 900 ns into the pulse, and reports no time course and no finding about cell size. Cell size enters only through the calculated IMP (Eq. 1). The header says the claims use the 900-ns frames, and that other time points give no outcome here.

**Counts:**
- 34 claims, all 34 with quotes and none needing an `inferred` note.
- 34 criteria.
- 7 claims with statistics (9 statistical values in all).
- 19 claims with expected values.
- 9 claims marked `with_inputs`, because they need the calculated IMP.

**Details the paper leaves open, and the readings named:**
- **Background subtraction for laser images:** (a) none, (b) subtract a cell-free region, as the paper does for Ca2+ images.
- **Cell radius:** (a) perimeter length / 2π, (b) radius of the circle of equal area.
- **Student's t-test form** (Methods 2.5): paired or unpaired, 2-tailed. Applies to Figs. 4A, 4B, 4C, 5A and the new poles claim; the claim is blocked as `methods_underspecified` when the two disagree.
- **Start and end of a set:** (a) first and last image, (b) first 10 and last 10 images.
- **Fig. 2B bleaching shift:** (a) last-10 minus first-10 at each pole, (b) the offset common to both poles.
- **Fig. 2D reduction:** which pole, each set or pooled, and the reference (first set, or mean of the sets before 1000 V/cm).
- **Fig. 3 correlation coefficient:** (a) Pearson r, (b) square root of the uncentred R² of the fit through the origin.
- **Fig. 3 FluoVolt non-linearity:** LOESS span 0.3, 0.5 or 0.75, or 50-mV bin means.
- **Fig. 4C equator arcs:** ±15° or ±30°.
- **Fig. 5A:** which datapoints are compared (three readings), and whose calculated IMP places a datapoint against the bounds (Gd3+ group, control group, or their mean).
- **Fig. 5B:** reduction counted as 1 − f/1.5, or relative to the intact value.
- **Ca2+ analysis windows:** peak frame or last 30 s (Fig. 6A); last frame, last 10 s or last 30 s (Fig. 6B).
- **"Strong response" in Fig. 6B:** 3 s.d. above baseline, above 50%, or above 100%.
- **Fig. 7 normalization and test:** normalize per cell or the means, each pole or their mean; a one-sample test against 100% or a paired test against the 150/150 control.
- **Fig. 7C:** whether fully resealed datapoints count toward "most datapoints".
- **Fig. 1 pattern** (new claim): "proportionally" and the drop toward the equator have no test in the paper. I used a linear regression (Methods 2.5) and compared the pole arcs with ±5° arcs at the equator, at 150 V/cm and above.
- **Poles alike** (new claim): the paper names no test, so I used the Methods' Student's t-test, paired and unpaired.

**Missing from the paper, or not checkable here:**
- **Charging time constant:** the fit of the time constant against cell radius is only in reference [20] (Bioelectrochemistry 168, 109143). Every claim using the calculated IMP needs it as an outside input. I did not read [20].
- **Fig. 6B cell counts:** no PDF renderer is installed in this run, so I could not read them from the figure. The thresholds for a "strong" response and the 90% for "nearly all" do not come from the paper.
- **Eq. (2) mismatch:** with the Methods constants, Eq. (2) gives a 1.3% IMP reduction for a 10-fold conductivity rise, where the paper says about 2%, and 11.9% for a 100-fold rise, where it says 12%. I kept the paper's numbers in the claim, so its 2% value may not reproduce.
