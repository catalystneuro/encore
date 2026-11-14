I've finished steps 1 to 6: the entry is at `entries/martinez-conde-2019/`, the record at `attempts/martinez-conde-2019-02.yaml`, and the handover package is built. `python tools/entry.py all` passes with 0 errors and the notebook runs in 58 s with 0.48 GB peak memory. I did not come across any earlier attempt's results.

**1. Outcomes**

Every tested outcome except neuron-counts and fig7a rests on the baseline-placement assumption described in section 2.

| Claim | Outcome |
|---|---|
| neuron-counts | not reproduced: 53 neurons in the data against 58 in the paper |
| spikes-per-condition | blocked (data_missing) |
| s4-baseline-no-difference | not reproduced |
| fig4a-above-baseline | reproduced |
| fig4b-spike-rate-difference | reproduced: 26.32, 19.67, 8.84, 4.62 spikes/s, all within the paper's SEM |
| fig4b-pairwise-significance | reproduced |
| fig5-average-maps | reproduced |
| table1-s40 | reproduced |
| table1-edge, table1-p180, table1-s90, table1-s52 | partially reproduced: 4 of 5 values each |
| fig6-midpoint-representative | reproduced |
| fig7a-rms-contrast-fit | not reproduced |
| fig7c-fold-edge-equivalence | not reproduced |
| fig7c-fold-edge-significance | reproduced |
| fig7d-nonlinear | reproduced |
| fig7d-dog-similar | blocked (data_missing) |
| s3-latency-peak | blocked (data_missing) |

**2. Dataset, assumptions, questions**

What the data set holds:
- It is one zip of spike-rate maps and stimuli; it has no spike times or eye positions. It holds 53 neurons (22 Square and Edge, 27 Star, 26 Corners), against 25, 30 and 28 in the paper.
- The `image` field is spikes per ms, not the raw spike counts the descriptor says. Only one neuron has an eye time map, so spike counts cannot be recovered.
- The two `ABS` files in the Star folder hold Corners stimuli and Corners recordings.
- The maps the authors registered to the stimulus (`Standard`, including a stored `BaseActivity`) are not documented.
- 15 Star neurons have no registered map and cannot be placed on the stimulus, because their receptive-field offset and aligned diagonal are missing. The Star analysis therefore uses 12 neurons.
- Six Corners registered maps use a frame cropped by 8 DU on each side.
- I checked that every registered map is its screen map moved rigidly (correlation 0.984 to 1.000). There are no duplicate recordings.

Assumption: the paper gives the baseline-square placement only in Fig 2. For each stimulus I took the placement whose values are closest, neuron by neuron, to the authors' stored `BaseActivity`. I chose it after seeing the results under every placement; the record says so, and the notebook shows them all.

Questions for the paper's authors, recorded as `methods_unavailable` findings:
- Where exactly are the baseline squares?
- How was the RMS contrast of Fig 7A computed?

I asked no questions of a reader.

**3. Protocol gaps**
1. The clock check in step 2 does not fit a data set of precomputed maps with no time series. In its place I showed that each registered map is the screen map shifted (and rotated, for the Star), and checked the stimulus luminance at the fold points.
2. The protocol does not say how to choose a reading using evidence from the data, such as the authors' stored baselines, once the results under every reading have been seen. I did it and disclosed it.
3. CRCNS data sets are not versioned. I recorded `unversioned`, the zip's MD5 and its last-modified date.
4. It does not say what to record when each part of a claim holds only under a different reading (fig7c-equivalence). I recorded not_reproduced.
5. It does not say what `measured` should hold when no reading matches. I recorded the first reading the criterion lists (fig7a).
6. During development I cached derived arrays in `$TMPDIR` to save time. The entry itself streams the data, and the cache is deleted.

**4. Runtime and failures**
The work took about 1 h 20 min, starting 12:52 UTC. One exploratory search for a reflection in a Star map timed out after about 28 minutes. It was outside the entry and is not needed: a faster method later matched all 12 Star maps.
