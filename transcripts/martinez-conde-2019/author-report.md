I've finished steps 1 to 6 of the Author section. The entry is at `entries/martinez-conde-2019/`, with the notebook `reproduce_martinez_conde_2019.ipynb` and the helper `vasarely.py`, and the record is `attempts/martinez-conde-2019-02.yaml`. Lock, check and the clean run all pass with 0 errors, and the handover package is built. I did not come across any earlier attempt's results.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| neuron-counts | not reproduced: 53 neurons, 22/29/26 per condition, against 58, 25/30/28; only the 7 tested in all three conditions match |
| spikes-per-condition | blocked, data_missing |
| s4-baseline-no-difference | not reproduced: all three readings find a difference (Kruskal-Wallis p = 0.005) |
| fig4a-above-baseline | reproduced |
| fig4b-spike-rate-difference | partially reproduced: the order holds, but S90 is 8.09 against 10.69 ± 1.94 |
| fig4b-pairwise-significance | reproduced |
| fig5-average-maps | reproduced |
| table1-edge, table1-p180, table1-s90 | not reproduced: values about 15 to 20% low |
| table1-s52 | reproduced (under reading a ii) |
| table1-s40 | reproduced |
| fig6-midpoint-representative | reproduced |
| fig7a-rms-contrast-fit | not reproduced: neither reading gives 0.61 to 0.943 |
| fig7c-fold-edge-equivalence | not reproduced: each reading misses one condition |
| fig7c-fold-edge-significance | reproduced under all four corrections |
| fig7d-nonlinear | reproduced |
| fig7d-dog-similar | blocked, data_missing |
| s3-latency-peak | blocked, data_missing |

No claim rests on an assumption, and nothing uses random draws.

**2. Dataset, assumptions and questions**

- **Counts:** the data set holds 77 recordings of 53 neurons (49 from monkey J, 4 from A). The spreadsheet lists 58 cell codes, but 5 have no condition and no files.
- **Units:** the descriptor is wrong about `image`. It is spikes per ms of eye time, not raw counts; multiplying by `eyetime` gives exact integers in the one recording that has it. `smoothed_image_norm` is the map minus `BaseActivity`, scaled to its maximum.
- **Undocumented fields:** the analyses rest on the `Standard` struct, the ROI rotated to the preferred orientation, with polygon vertices that tie it exactly to the stimulus (residual 1e-12). It, `BaseActivity` and `eyetime` are undocumented. `BaseActivity` is present in 38 of 60 aligned recordings, and no placement of 16 DU baseline squares reproduces it.
- **Star:** 17 of 29 recordings cannot be placed on the stimulus. 15 lack `Standard`, and the RF offset needed to build it is not stored. The other 2 (ABS) also lack it and have MATLAB 7.3 stimulus files of a different star. So Star rests on 12 of the paper's 30 neurons.
- **Missing raw data:** no spike times or eye traces are deposited.
- **Choices I made:** off-display pixels are left out of every measure; keeping them changes no outcome. The text gives no position for the Corners baseline squares, so I placed them where the paper's Fig 2C draws them, reading the figure from the journal page.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How was local RMS contrast along the Edge computed (Fig 7A)?
  - Which test and which baseline computation lie behind S4 Fig, and where were the Corners baseline squares?
- **Questions to a reader:** none.

**3. Protocol points**

1. CRCNS has no versions. I recorded `unversioned` with the MD5 sums from `checksums.md5`; the bucket holds only `live/`.
2. `paper/` has no figures or PDF. I fetched Fig 2 from journals.plos.org to place the Corners baseline squares and cited it as the paper's figure.
3. The "shared clock" check does not apply to maps without time. I used a contrast instead: the bright S40 fold beats the dark one in 23 of 26 recordings (p = 2e-6).
4. The "record the first reading listed" rule for `measured` is unclear when only a later reading matches (table1-s52). I recorded the matching reading's values and gave the first reading's in the notes.
5. The protocol does not say whether a heavily reduced subset (Star 12 of 30) should change an outcome label. I applied the criteria as written and flagged the subset in the notes.
6. One check made while preparing (re-registering the full-screen maps) is mentioned in a finding as not run in the notebook, with no number from it.

**4. Runtime and failures**

The notebook runs in 35 s with 0.37 GB peak memory; the whole session took about 40 minutes. Nothing failed in the final run.
