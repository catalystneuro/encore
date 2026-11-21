The claims file for rozsa-2023 is ready for an attempt: the checker is clean, and I made seven corrections, none of which changes a claim's id.

**Checker result:** `claims/rozsa-2023.yaml: 31 claims, 31 quotes, 18 statistical values, 0 problems` (same before and after my edits).

**Changes, by claim:**
- **fig1f-human-raf-ngfc:** The file said it was open whether the 15 rosehip cells are among the 90 non-NGFCs. The paper's counts settle it: 30 RAF-positive plus 104 RAF-negative classified cells is 134, which equals 44 NGFCs plus 90 non-NGFCs. So the rosehip cells are among the non-NGFCs. That is now the main reading; counting non-NGFCs without them is a variant.
- **fig1hk-bleb-initiation-order:** Reading (c), which sorts APs by whether they fall inside a current pulse, cannot be used here, because these RA-APs occur during somatic pulses (Figure 1H and 1I legends). Reading (b) sorts APs by threshold and slope, so under it those differences are reported and only the latency is judged.
- **fig3-human-ap-states:** The file placed each AP in an up, down or transition state by its threshold potential, without saying the paper does not specify this. That is partly circular, since AIS-APs have the higher threshold. It is now marked open, with two readings: the mean potential 0 to 50 ms before threshold (the Figure 3F window), and the threshold itself.
- **fig2h-bleb-sag-higher:** The Methods do not say which trace and step give the bleb sag value. This is now named as open, with the bleb trace during a somatic step as the variant.
- **fig3i-rat-lfp-rhythm and fig3k-rat-pre-ap-fluctuation:** Each statement had a part the criterion never tested (synchronization to up states; AIS-APs in up and RA-APs in down states in rat). The paper gives no measure for either, so the criteria now say these parts are reported, not judged.
- **fig1ab-raf-patterns:** The duration values (minimum, maximum, mean, median) sit in the persistent RAF clause but may cover all epochs. Both readings are now shown.
- **Header, phase method:** The Methods say only that power was "corrected ... with the frequency values". Multiplying power by frequency is now stated as a standard choice for a detail the paper leaves open.

Every quote, p-value, count, expected value and tolerance matches the paper, and each main finding, including Figures S1 to S5, has a claim.

**What remains open:**
- **Details the paper does not give:**
  - the boundary between AIS-APs and RA-APs
  - the sag fraction formula (ref. 28 is not in the text read)
  - how up, down and transition states are defined (ref. 38)
  - how the LFP rhythm frequency is measured
  - the correlation type in Figure S4I
  - the test for Figure S5

  The claims name the readings the paper allows for each, and the paper links no code that could settle them.
- **No measure or test in the paper:** fig4-invivo-up-down-balance and figs5-not-genotype-or-anesthesia have none. Their criteria rest on readings chosen in the claims file, so their outcomes will rest on assumptions.

I added the `checks` entry with `ready: true`. Nothing was committed or pushed.
