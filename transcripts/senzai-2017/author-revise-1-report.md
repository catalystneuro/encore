I've revised the attempt for verifier round 1. No outcome changed. I re-ran the entry with `python tools/entry.py all entries/senzai-2017`; it passed (1285 s, 0 errors), the record validates against the schema, and every conclusion matches the new outputs. I added three questions for a reader and recorded the round under `verifications`, with each claim's reason in the verifier's words and my response. Nothing is committed.

**Outcomes.** The verifier agreed with 28 of 31 claims. I kept the three disagreements and recorded why:
- **pv-remap:** kept as reproduced, seed sensitive (the verifier said partially reproduced). The protocol takes the outcome under the claim's own seed, and the test over 1000 draws is the paper's own. I added a measure that doesn't shrink with more draws: the chance a granule-cell draw is below a mossy-cell draw is only 0.514 to 0.537 at n = 20, which supports the verifier's concern. That number is in the notes.
- **gc-mc-distance and gc-backpropagation:** kept as blocked for missing metadata (the verifier said the real block is the missing criterion). I ran the depth check it proposed, and it does not establish the depth order. On the 261 shanks where the DS2 reverses, its amplitude rises with the site's list position on 46% and falls on 43%. The sign also flips between days in the same mouse, and some shanks have 10 sites where the probe description says 8. The missing criterion is given as a second reason.

**Added or corrected:**
- **gc-mc-classification:** now uses the unfiltered wide-band waveform, as the criterion says: 94.4% agreement under all five seeds. The filtered version (94.9%) is a variant.
- **optotag-drd2:** Reading the Methods' rule per 1 ms bin gives 28 of 106 mossy cells (0.264, within tolerance). It also gives 0 granule cells, 7 wide- and 0 narrow-waveform interneurons, and includes 28 of the authors' 29 tagged cells. The criterion fixes the mean rate over the window, so the outcome stays partially reproduced. I added a question asking whether the claims file misreads the Methods; under the per-bin reading the claim would be reproduced. Adding a significance test changes nothing, and the pre-pulse baseline is not inflated.
- **Waveform source:** The files don't say whether the stored waveforms were filtered, and the paper measures the unfiltered waveform. I added a question on first-stage-labels and gc-narrower-waveform. In the unfiltered wide-band, the granule-versus-mossy result depends on how the peak is defined: P = 0.175 one way, 7.9e-10 the other.
- **Other outputs the verifier asked for:**
  - a circular phase test: P = 0.0001 for theta and gamma
  - a spike-count-matched gamma control: the rate correlations mostly vanish
  - a per-pair state-transmission table
  - the T-maze linearisation table
  - the hilus reference channel check: positive DS2 in all 91 files
- **Splitters:** fixed the bug that kept a NaN result. Only 1 of 901 field fits failed and no counts changed. An exact test gives P = 0.835.
- **Findings:** I revised findings 1, 3, 6 and 8 in place. I added a new minor finding 11: in one mouse, 5 of 9 units in the second file of a day have a near-identical waveform in the other file of that day, against none on another day. The other six pairs are inconclusive, so whether the same neurons are counted twice is not settled.

**Not done:**
- No question for zero-lag-synchrony's wrong statement that unit shanks are unknown. It is about the data, not a misreading of the paper; it is in the notes.
- I couldn't read the supplement PDF, as no PDF tools are installed, so I worked from the main text.
- No finding is rated critical, so there was nothing for round 2 to review there.
