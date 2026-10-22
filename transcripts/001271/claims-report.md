I wrote `claims/001271/10.1016-j.xcrp.2025.102660.yaml`, and the quote checker passes it: 20 claims, 18 quotes, 7 statistical values, 0 problems. Nothing is committed.

**Text read.** I read the NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC: main text, figure legends and STAR Methods. I also read the supplement (Figures S1 to S4 and Table S1). I did not read the version of record. There was no main-text PDF, so Figures 1 to 6 were never seen. I opened page 3 of the supplement PDF only to see how Figure S2 is laid out: one vehicle neuron and two TTX neurons, each tested at the same fields before and after the change. No claim rests on what I read there. The paper says it reports no original code, so no repository was read.

**This dandiset.** Its DANDI title and description match the tetrodotoxin experiment of Figure S2. The paper deposited its data in ten dandisets without saying which figure is in which, so the other dandisets were assigned from their titles only.

**Claims.**
- **Tested on this dandiset (7):** how many neurons were tested; firing and then sustained depolarization before the drug; the depolarization reversing when the stimulus ends; TTX abolishing the APs; TTX blocking the sustained depolarization; vehicle neurons keeping their response; AP height and duration (11.3% ΔF and 8 ms).
- **Tested elsewhere (13):** the main findings of Figures 1 to 4, 6 and S1, the heating calculation, and the threshold estimate of 6.8 mV, each pointing to the dandiset its title suggests. For the Figure S1, 4 and 6 claims, the criteria defer to the existing claims files for 001272, 001273 and 001274.
- **Quotes:** 18 of 20 have one. The other two carry a note saying they are read from the figure, because no sentence states them: the pre-drug firing and depolarization pattern in the Figure S2 neurons, and the vehicle result.
- **Statistics:** 3 claims carry the paper's tests (7 values in all). The paper reports no test for Figure S2.
- **Criteria:** all 20 have one.

**Details the paper leaves open, and the readings named:**
- **O1, soma outline:** use the dataset's ROI; if it has none, (a) an Otsu mask of the component nearest the image centre, or (b) that mask eroded by 2 pixels.
- **O2, baseline (F0) window:** (a) all frames before the stimulus, or (b) the last 20 ms before it.
- **O3, AP detection height:** (a) above 5% ΔF, or (b) above 5 SD of the pre-stimulus trace. After TTX, the level is taken from the same neuron's sessions before the drug. The width bounds (2 to 20 ms) are a standard choice.
- **O4, sustained depolarization:** no AP in the last 100 ms of the stimulus while the mean ΔF there is above (a) 5 SD of the baseline, or (b) half the neuron's median AP height.
- **O5, which sessions are compared before and after:** (a) every field tested both times, or (b) only the highest such field.
- **"Immediately reversible":** the ΔF window after the stimulus is (a) 10 to 40 ms after it ends, or (b) the last 40 ms of the recording.
- **Neuron count:** "at least 4 replications" counts (a) TTX neurons only, or (b) TTX and vehicle neurons together.
- **Which 22 neurons the AP height and duration come from:** the paper does not say. Readings: (a) all APs or (b) only each session's first AP; duration as (a) half-height width or (b) time from rise back to F0.
- **Heating formula:** the field is (a) peak or (b) RMS, with the heat capacity of water as a standard choice.
- **Fractions such as "more than half":** the paper gives none, so these thresholds are labelled as standard choices.

**Missing from the paper:**
- No count of TTX or vehicle neurons.
- No sentence stating the vehicle result.
- No mapping of figures to dandisets.
- No source for the 22 neurons behind the typical AP values.
- No formula for the temperature rise.
- No code.
