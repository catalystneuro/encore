**A. Outcomes**

The claims file has 24 claims: 1 link claim and 23 findings. The attempt record was not among my materials, so these counts come from the claims file alone.

| Claim | My outcome | Reason |
|---|---|---|
| recordings-as-described | reproduced | Cell 16: all 15 checks hold. The five named files are present. `sub-mouse412804_ecephys.nwb` has 248 channels, 30 kHz and 27,000,000 frames. MEArec is 600.00 s with 250 ground-truth units, rat is 384 channels at 30 kHz, and the retina is 1024 channels at 23199.09 Hz. I confirmed the 6 assets with the archive API myself. |
| fig1b-unit-counts | blocked (other) | Needs all six sorters. Cell 9/18: no MATLAB, GPU or MPI, so Kilosort2, IronClust and HDSort cannot run. The archive holds no sorter output: I checked that the asset metadata of the mouse recording lists only ElectrodeGroup and ElectricalSeries, with no Units. |
| fig1c-low-agreement | blocked (other) | Same: depends on all six sorter runs. |
| fig1d-most-units-unmatched | blocked (other) | Same. |
| fig1s2-agreement-scores-high | blocked (other) | Same, under both readings of the recording. |
| fig1s3-s4-other-recordings-disagree | blocked (other) | Needs six sorters on the rat recording and four on the retina, three of which need MATLAB. |
| fig2c-sim-unit-counts | blocked (other) | Needs six sorters on MEArec. |
| fig2s1a-precision-recall-bias | blocked (other) | Needs sorter outputs, although the ground truth is present (cell 7). |
| fig2s1b-accuracy-snr | blocked (other) | Needs sorter outputs. Ground-truth SNR alone could be computed, but it decides nothing. |
| fig2d-ks2-highest-scores | blocked (other) | Needs Kilosort2 and the five other sorters. |
| fig2e-ks2-unit-types | blocked (other) | Needs a Kilosort2 run. |
| fig2e-ks2-curated-unit-types | blocked (other) | Needs a Kilosort2 run. |
| fig2e-tdc-few-fp-hds-many-fp | blocked (other) | Both parts compare against all six sorters. Tridesclous alone (pip-installable, cell 19) decides neither part. |
| fig3a-sim-low-agreement | blocked (other) | Needs six sorters. |
| fig3b-sorters-prone-to-low-agreement | blocked (other) | Same. |
| fig3c-fp-found-by-one-sorter | blocked (other) | Same. |
| fig3s1-ks2-ic-best-pair | blocked (other) | Same. |
| fig3s1-pairs-remove-fp-four-keep-tp | blocked (other) | Same. |
| fig3d-snr-rises-with-agreement | blocked (other) | Same. |
| fig3s2-snr-does-not-separate-ks2-fp | blocked (other) | Needs Kilosort2 units. |
| fig4a-curators-agree | partially_reproduced (lower bound) | Cell 21: pairwise `compare_two_sorters(C1, C2)` with defaults gives 226 (expected 226 ± 22.6), 351 (351 ± 35.1) and 64.39% (64.2 ± 6.42). The 174 needs the Kilosort2 run and is untested. The criterion gives reproduced if 174 holds and partially reproduced if not, so the claim is at least partially reproduced either way. The notebook calls the whole claim blocked. |
| fig4b-single-sorter-match-curated | blocked (other) | Needs all six sorter runs. |
| fig4c-consensus-match-curated | blocked (other) | Same. |
| fig4d-nonconsensus-rarely-curated | blocked (other) | Same. |

No claim states a chance level, so there was none to compare.

**B. Problems**

1. **[affects a conclusion] Cell 0 table and cell 20 (fig4a-curators-agree).** The notebook files the claim as blocked because it "depends on fig1b". Yet its own output puts all three curator-only values within tolerance, and under the claim's criterion that fixes the outcome at no worse than partially_reproduced. The dependency on fig1b only touches the 174.
2. **[does not affect a conclusion] Cell 0 table.** The blocking reason `not_runnable` is not one of the allowed reasons. The actual cause is software and hardware (MATLAB, a CUDA GPU, MPI), which is `other`. It is not `too_large` and not `data_missing`.
3. **[does not affect a conclusion] Cells 18–19.** The claim that streaming takes "6.8 h, over the 0.5 h limit" assumes serial remfile reads of single-channel chunks, at about 0.5 MB/s. A bulk S3 download of the 13.4 GB mouse file at ordinary bandwidth takes minutes. So "even the three Python sorters would first need … hours" is overstated, and it is not a valid argument for too_large. The block still stands on the missing MATLAB and GPU.
4. **[does not affect a conclusion] Cell 14.** It says the mouse data in µV "have plausible ranges". But the band-passed noise SD is 49.9 "µV" and the median trough 455 µV (cell 11). That is about 5× typical Neuropixels levels, and fits raw int16 counts, which need a gain of about 0.195 µV/bit, mislabelled with conversion 1e-6. This was not flagged. The same unchecked-units issue the notebook does flag for the retina applies here. No tested claim uses amplitudes.
5. **[does not affect a conclusion] Cell 12.** MEArec noise is 15.9 µV by MAD, against the paper's 10 µV, and only 63% of ground-truth units have their trough within 3 frames. The notebook leaves the noise question open, which is fair, but it never checked whether the stored traces are filtered.
6. **[does not affect a conclusion] `to_frames`.** It drops frame 0, which matches spikeextractors 0.8.4. I tested it on synthetic input (`[0, 1e-5, 1/30000, 0.5]` → `[1, 15000]`). `lag_scan` recovers an injected +3-frame lag correctly. The helpers are sound.
7. **[does not affect a conclusion] Claims file, reported not corrected.** I found no misreading of the paper. "64.2%" in the paper is 226/351 = 64.39%, a rounding in the paper itself.

**C. What I could not check**

- I could not confirm that the curated Units tables carry no Kilosort2 labels or links. Asset metadata lists only "Units", and I did not open the files. Printing the full HDF5 tree of both curated files, plus that of `sub-mouse412804_ecephys.nwb`, would settle whether the 174 can be got without a Kilosort2 run.
- To make the too_large argument fair, the notebook should add the measured time of one bulk download (for example, `dandi download` or a ranged S3 GET of 1 GB).
- For the mouse units issue (problem 4), the notebook should print the electrode table's gain or `channel_conversion` columns, if present.
- I had no attempt record, so I could not check the author's stated outcomes or counts against it.
