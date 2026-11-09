I've addressed every point in the round-1 report and re-run the entry. `python tools/entry.py all` passes in 219 s. No outcome changed; the blocked claim now has a different reason. Nothing is committed.

**Outcomes**
- The verifier agreed with all eight outcomes, and they all stand.
- `sensory-input-drives-fs` is still blocked, but the reason is now `metadata_insufficient` instead of `methods_underspecified`. The verifier was right that the paper's supplement describes the test: Figure 7 compares FS cells in control mice and mice with the infraorbital nerve cut (ION transection). The notebook now prints every metadata field of the 130 L4 files. None records a surgery, a lesion or notes, so the cut mice cannot be identified from the files.
- `exc-mainly-touch` stays not reproduced (p = 0.074 against FS cells, 0.090 against VPM units), but the result is fragile:
  - Leaving out the four mice flagged as lacking touch input gives p = 0.024 and 0.038.
  - Keeping only the 12 excitatory cells with at least 20 spikes near touches gives p = 0.003 and 0.005.
  - Neither variant decides the outcome. The flag is inferred from touch responses, so both selections favour the claim by construction. The conclusion and notes say this, and round 2 may disagree.

**What I added or corrected**
- **Paper:** the supplement PDF is public. Its legends and Supplementary Tables 1 and 2 are saved under `paper/`.
- **Cut mice:** I added a membrane-potential touch response. Whole-cell cells in anm318530, anm318531 and anm318532 show no touch response (below 0.35 mV), against a median of 2.8 mV elsewhere. Those three mice hold 9 whole-cell cells, the number the paper gives for cut mice. Four mice are flagged as probably cut, by a threshold I chose after seeing these values. I use the flag only in variants and in an exploratory comparison of FS cells, which is not a test of the claim.
- **Mouse lines:** Supplementary Table 1 is now read at run time, which adds `pypdf` to the lock file and is recorded under `inputs`. Cell counts per mouse line and recording mode match Supplementary Table 2 for every line except PV-Cre (48 files against 47 cells).
- **Outputs the verifier asked for:**
  - tag site, tag p and latency for each tagged cell;
  - spike width by sampling rate;
  - a light-artifact check and example traces with detected spikes;
  - spike and trial counts per condition, and whisking and touch behaviour with and without light, for the PV-Cre and VPM-light tests;
  - a trial-shift null for the L4 cells;
  - the paper's sinusoid-fit r² measure, as a variant (it marks 0.33 to 0.40 of cells on the null, so it does not decide anything);
  - the PV-Cre test without anm266945 (3 of 3, p = 0.125).
- **Code fix:** touch windows that crossed a trial boundary are now dropped. This affected 7 of 66,206 touches.
- **New findings:**
  - no file marks the cut mice;
  - the genotype is missing for 9 mice, and the SOM-IRES-Cre x Ai32 mice are labelled `Ai32`;
  - every cell is labelled layer 4, though the paper includes some L5 cells;
  - all 24 files with the wrong recording mode in their session description are PV-Cre files.
- **Other files:** the claims file has a second amendment that records the supplement without changing any criterion. Round 1 is recorded under `verifications`, and the conclusions, summary, README and attempt notes match the new numbers.

**Not done**
- I kept the main tests as the criteria fixed them, because I had seen every outcome before reading the supplement. The paper's FS waveform rule, its r² rule and the PV-Cre juxtacellular population are shown only as variants.
- The spike detector was not checked against any ground truth.
