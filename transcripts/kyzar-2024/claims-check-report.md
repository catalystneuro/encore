The claims file for 000469 is ready for an attempt. I made four small corrections, and two points stay open.

**Checker:** `claims/000469/10.1038-s41597-024-02943-8.yaml: 20 claims, 20 quotes, 2 statistical values, 0 problems`. It gives the same result after my edits.

I checked the method details against the paper's code (rutishauserlab/workingmem-release-NWB at f8594e0), and they hold. That covers the example unit lists, the analysis windows, the ISI filter, the correct-trials-only reaction time filter, the CV2 settings, the projection distance handling, the area groupings, and the three code defects the file describes. The commit's code is identical to tag v1.0.0. The unit denominators match the reported percentages (453 MFC units in the Sternberg task). Every main finding of the paper has a claim, and nothing comes from another source.

**Changes, by claim:**
- **waveform-snr:** I reworded the statement to the paper's wording (noise s.d. against the peak of the mean waveform). It said "peak SNR", which ruled out the mean-SNR reading the criterion keeps, since the sentence cites Fig. 3g and 3h.
- **behavior-rt-load:** The F statistic is an expected value, but the criterion only reported it. F within tolerance now decides the claim. It counts as partially reproduced when only p < 0.05 and the direction hold.
- **persistent-activity:** The criterion required only the two means, but the claim lists four expected values. It now requires all four, as the other mean ± s.d. claims do.
- **maintenance-cells-mfc:** The criterion credited the 0 to 500 ms baseline to the Methods. The Methods give only its length; the code puts it at fixation onset. The criterion now says so.

**Open:**
- **screening-unit-yield / screening-concept-mtl:** The text gives 449 screening MTL units, but the reported percentages imply about 421. The paper can't settle which is right, so both readings stay.
- **behavior-accuracy-load:** The paper reports no test for accuracy against load. The rule that mean accuracy must fall from load to load is a reading of "less accurate answers".

The check entry is appended under `checks`. Nothing is committed.
