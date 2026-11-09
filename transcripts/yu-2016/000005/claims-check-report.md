The file is ready for an attempt. I marked it `ready: true` and recorded 18 entries under `checks` (14 changes, 4 open problems).

**Checker:** `claims/000005/10.1038-nn.4412.yaml: 33 claims, 33 quotes, 20 statistical values, 0 problems`. It was 31 claims before I added two.

**Changes, by claim**
- **behavior-touches:** The criterion said the touch and trial counts (4,147 and 4,173) come from the 111 cortical cells and count only principal-whisker touches. The paper says neither, so both are now open, each with readings.
- **vpm-whisking:** The text gives 13.5 spikes/s "after onset of whisker movement" but defines no window for it. The criterion now reads it as the whisking-epoch rate that Fig. 5d plots, and says so.
- **exc-vm-touch-whisking:** The paper does not say how the 1.2 mV whisking change was measured, but the criterion took the Supp. Fig. 4 windows as given. It now runs two readings: those windows, and mean Vm in whisking epochs minus mean Vm in nonwhisking periods. **ion-cut-exc-whisking** now uses both readings too.
- **exc-inhibition-timing:** I dropped the requirement that the delay be "positive in most neurons", which the paper does not state. The Discussion's range (-0.8 to 1.6 ms) is now reported against the result.
- **exc-thalamus-photoinhibition and pv-enphr-suppression:** I removed a latency reading (a 3 s.d. threshold on Vm itself) that appears nowhere in the paper. The Methods' touch-latency rule is now applied to laser onset, and the criterion says that is an assumption.
- **ion-cut-exc-no-touch:** The old measure took Vm at the peak of the average PSP, which is undefined when there is no PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms after onset) against the 0 to 5 ms pre-touch mean, with the peak-based measure as a variant.
- **fs-suppress-movement-spiking:** The paper does not say which groups its Kruskal-Wallis test compared. That test is now reported but does not decide the outcome.
- **auc-weak-strong:** The criterion compared baseline-subtracted rates (the Fig. 8g measure) but cited Fig. 8h's 3.4 and 7.3 spikes/s, which are post-touch rates without the baseline removed. I separated the two.
- **auc-groups:** I added the Fig. 8h group sizes (19 and 21 of 40 neurons) as expected values and put them in the criterion.
- **Added exc-inhibition-whisking (Fig. 3e-g)** and **ion-cut-behavior (48% correct after nerve cut):** both are main-text findings that had no claim. The header now notes them.

**Open**
- I could not check the readings taken from figures: the waveform boundary in Supp. Fig. 6, the 12 phase bins in Supp. Fig. 2d, and the 23 to 26 VPM units above r2 0.25 in Supp. Fig. 2e. No PDF renderer was available in this run.
- vpm-whisking-phase and fs-whisking-phase count a population as coupled when "more than half of the cells are above r2 0.25". The paper gives no count or test, and states that threshold only for VPM units and for the nerve-cut fits, not for control FS cells. The rule is the file's own reading.
- For values given as mean ± s.d., the tolerance is the larger of 10% and s.d./√n, not the s.d. itself. The header gives the reason, but the protocol's "stated spread" could also mean the s.d.
- Some secondary findings have no claim, because the paper gives no test and no frequency band for them. They are the whisking-related Vm fluctuations above 10 Hz in L4 excitatory neurons (Supp. Fig. 5) and the absence of a spectral difference between whisking and nonwhisking after the nerve cut (Supp. Fig. 11). Also without a claim: FS Vm fluctuations in some cells (Supp. Fig. 8) and the VPM touch-response duration (2.9 ± 1.7 ms).

Nothing is committed or pushed.
