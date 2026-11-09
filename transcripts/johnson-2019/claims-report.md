I wrote `claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml`. The quote checker reports 17 claims, 17 quotes, 17 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the version of record (PMC6333050, Europe PMC full text): Methods, Results, Discussion, Table 1 and the legends of Figures 1 to 5. The paper has no supplement and no PDF was supplied, so I did not read values shown only inside figures (Fig. 1B per subject, Fig. 4A/4C per subject, Fig. 5 time courses). The claims on those figures rest on the Results and the legends. I read the data descriptor only to see what the dataset holds.

**Code.** The paper's MATLAB scripts are deposited inside the dataset itself, in its `analysis_scripts` folder. Since readers do not open the dataset's files, I did not read them and recorded no commit. The opening comment says the author may use them to settle any detail named as open below.

**Claims.** There are 17, all with quotes and all with criteria. 11 carry statistics (17 entries) and 11 carry expected values. All use the dataset alone; the paper uses no outside data. They cover:
- Electrode and pair counts (192 electrodes, 1129 pairs) and trial counts.
- Behaviour: accuracy range with no condition effect, and identity RTs longer than spatial and temporal.
- No ERP difference between conditions.
- Per-subject power effects for spatial (5/7 and 2/7 subjects) and temporal (4/7 and 2/7).
- The same subjects being slower and less accurate on identity trials.
- Power effects concentrated at low frequencies.
- Phase slope index (PSI) results: parietal-led during maintenance; the delta-theta shift after the cue (6/7 subjects net PFC-led); the alpha-beta shift that stays parietal-led; and the counts of directional pairs (1008 and 984).
- Time-resolved delta-theta effects: the sustained epochs, identity trials PFC-led early and parietal-led late, and spatial and temporal trials staying bidirectional.
- No sustained alpha-beta effects.

**Details the paper leaves open, with the readings named:**
- **Behaviour models:** the reported degrees of freedom imply one value per subject and condition (a); fitting single trials is (b). Accuracy is either over all 120 trials or over the trials kept after rejection. How Cohen's d was computed is not stated, so d is recorded but not judged.
- **Accuracy range:** per subject, or per subject and condition.
- **Power windows longer than the 900 ms segment:** zero-embedded so every window is computed (a), which is the only reading that yields the reported 2 Hz effects; or left unestimated (b).
- **Baseline bootstrap:** r is either all correct trials or the condition's trials.
- **Cluster test:** spatial neighbours are adjacent channels on the same strip or shaft, channels within the contact spacing, or no spatial clustering; alpha is 0.05 per tail or split between tails.
- **"Difficulty" comparison:** identity against the contrast's own condition, or against the mean of spatial and temporal.
- **Spectral density:** masked points only, or all points with unmasked points as zero.
- **PSI computation:**
  - Mean subtraction is over all correct trials or per condition.
  - The spectrum is one FFT of the whole segment or time-averaged sliding windows.
  - Band PSI is a single slope across the band's bins, or per-frequency PSI averaged over the band.
  - The frequency shuffle uses one permutation for all trials or one per trial.
- **What a group mean or SD is taken over:** subjects or pooled pairs; for the processing z of 6.01, all 7 subjects or the 6 with positive values.
- **Epoch z values:** the epoch mean, the pooled-pair mean, or the least extreme time point (reading the printed "z >" as a bound).
- **"All |z| < 1.60":** every time point, or every reported epoch.
- **FDR method:** read as Benjamini-Hochberg over time points, a standard choice the paper does not name.

**Missing from the paper.** No claim was blocked. Only the per-subject figure values (Fig. 1B, 4A and 4C) could not be read without a PDF.
