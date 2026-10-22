I wrote `claims/001262/10.1038-s41597-024-03259-3.yaml`. The quote checker passes: 22 claims, 22 quotes, 0 problems. Nothing is committed.

**Text read.** The version of record (PMC11035566, from Europe PMC), including Methods, Data Records, Technical Validation, Usage Notes, Table 1 and the figure legends. The paper is a Data Descriptor and has no supplement. I did not need the PDF.

**Code read.** The paper's toolbox on Zenodo (doi:10.5281/zenodo.10370064, record 10370064, the only version, 2024-04-15), all 21 MATLAB files. The code settles these details, and the criteria follow it:
- **Age groups:** split at 365 and 1095 days.
- **Values used:** each unit's stored analysed values, not recomputed ones.
- **Spontaneous rate:** taken from the SR recording, else PH, else RLF, else BF.
- **Bins:** the histogram and moving-average bins of Fig. 6a and 6b. The paper's "bin bordered by 2.5 and 3.0 kHz" is the code's bin from 2423 to 2936 Hz.
- **Click latency:** the 2-bin latency, only for units with exactly one CLICK recording.
- **Vector strength:** the largest value among levels with p < 0.001.

**Claims.**
- **Quotes:** all 22 have one, so none needed an `inferred` note.
- **Statistics:** none. The paper reports no statistical tests.
- **Expected values:** 8 claims have them, covering Table 1 counts, means and ranges, oxygen use, experiment and recording-type counts, the Fig. 5b example unit, the highest phase-locking frequency, and the spontaneous-rate modes.
- **Criteria:** all 22 have one. Counts of deposited records have zero tolerance, with that reason given. Other values use the default 10%.

**Details the paper leaves open, and the readings named:**
- **"Multiple" short inter-spike intervals (`isi-exclusion`):** two or more within one recording, two or more pooled over all of a unit's recordings, or the BF recording only.
- **"Highest thresholds at 3.5 kHz" (Fig. 6a):** the largest bin over all frequencies, or a local maximum between the two sensitive regions.
- **"Fewest fibres" (Fig. 6b):** the fewest of all bins between the lowest and highest non-empty bin, or a local minimum.
- **Modes of spontaneous rate (Fig. 6c):** one reading, the two largest local maxima of the code's 5 spikes/s histogram.
- **Highest vector strength (Fig. 6d):** for young adults and for all ages, either the single top unit or the highest group median.
- **Recording-type counts:** units with a non-NaN analysed value, or units with any recording of that type.
- **"Representative" BF sampling (Fig. 7a, 7b):** compared with young adults or with all units, by a KS test or by medians within 10%.
- **Correlations (Fig. 7a, 7b):** the paper gives no test or threshold for "strongly". Pearson on log BF is the main measure and Spearman a variant. "No systematic deviation" is judged as the median CF/BF ratio within 10% of 1.

**What a claim needed and the paper lacks:**
- **No prepotentials, and RLF nonmonotonicity below 80 dB:** both checks were visual and neither the paper nor the code gives a rule. Both claims are marked to be blocked as `methods_underspecified` unless a reader can supply one.
- **43% against 88% recording success:** this needs the animals that gave no units, which the dataset may not hold.
- **"Phase locking did not change" with age:** this cites ref. 17, so I left it unclaimed and say so in the file's opening comment.

The paper's data are on Dryad (doi:10.5061/dryad.qv9s4mwn4). The dandiset lists itself as a variant form of that deposit, in NWB files with one unit per file, so every claim is `data: dataset`.
