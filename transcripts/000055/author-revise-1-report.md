I've answered all of the verifier's round-1 points and re-run the entry three times with `python tools/entry.py all`. The last run passed in 655 s and `check` reports 0 errors. Nothing is committed.

**Outcomes:** none changed. The verifier agreed with all 22 (16 reproduced, 4 partially reproduced, 1 not reproduced, 1 blocked), and each agreement is recorded in the round-1 `verifications` entry of the attempt record, with its reasons quoted and my responses.

**Output the verifier asked for, now in the notebook:**
- **ECoG reader:** it gives the same samples as h5py in 12 of 12 comparisons, including 8 windows that cross a chunk boundary. Every file is little-endian float32 with gzip as the only filter.
- **Stored angle before folding:** upward reaches outnumber downward ones in all 12 subjects, so the upward skew is in the dandiset's values, not caused by the folding.
- **Best stored R2 electrodes:** of the 20 with the largest R2 per band, 19 (LFB) and 16 (HFB) sit mainly in a frontoparietal region.
- **Forward selection inside each training split:** largest R2 is 0.140; a model's test R2 drops by about 0.033 on average. Angle and day still lead, the angle coefficient keeps its signs, and angle is still the feature retained most often (61.8%).
- **Day-to-day variability:** the LFB count of 9 of 12 is borderline. Under resampling it stays at 9 or more only 90% of the time, and the notes now say so. HFB holds in every resample.

**Other additions and corrections:**
- **Eight-region pattern:** with events resampled within subjects, the criterion holds in 99.5% of 1000 resamples.
- **Late-starting files:** without them, 20 of 24 means fall inside Table 1's intervals (19 medians).
- **Durations of 0.5 to 4 s only:** under the range the Methods keep, all six feature correlations are within tolerance. feature-correlations stays partially reproduced because the criterion was fixed on all events.
- **Clock check:** the text now says it has little power in any one subject with 15 to 25 events.
- **New deviations:** the `good` flag also marks electrodes without coordinates; subjects 02 and 06 have only 5 and 7 regression electrodes, where the criterion says eight; selection sees the test events; time-of-day bins include both ends, though no event falls on an edge.
- **Corrected:** all three late-starting files have a shorter ECoG chunk length (54412, 55031, 55820 samples), not only subject 01 day 7. I fixed this in the data check, the summary and the finding.
- **Helper module (`ajile.py`):** it now records each file's dtype and filters and has the in-split selection option. The docstring that claimed an h5py check is now true.

**What I left alone:**
- **Regression seeds:** my first re-run moved the main regression numbers, because the new variant shifted their seeds. I gave the variant its own seeds, and the final run reproduces the numbers the verifier checked (largest R2 0.141, r = 0.865 and 0.776).
- **Standardisation:** it still uses all events, as the paper's code does. It uses only the features, not the response, so I did not move it inside the split.
- **Missing electrodes for 02 and 06:** I did not fetch more ECoG to make up the eight, since the verifier said this affects no conclusion.
