I've finished steps 1 to 5 for dvali-2025, run the handover, and the entry passes `tools/entry.py all`. Of the 39 claims (38 from the reader plus one link claim I added), 15 were tested: 10 reproduced and 5 partially reproduced, none not reproduced. The other 24 are blocked, almost all because graph-tool can't be installed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| atlas-dataset-link (link claim I added) | partially reproduced |
| signaling-network-size | reproduced, reading (b): 1154 edges, density 0.0328 |
| signaling-clustering-small-world | reproduced: C 0.135, sigma 4.62 |
| anatomy-network-properties (elsewhere) | reproduced, assumed: 3223 edges, density 0.092, C 0.306, sigma 2.52 |
| triad-distribution | reproduced |
| ed6-signaling-not-feedforward | reproduced |
| ed6-anatomy-feedforward (elsewhere) | partially reproduced |
| fig4c-broadcaster-integrator | partially reproduced: amphid p = 0.0046; pharynx p = 0.073 |
| ed9-sampling-not-confound | reproduced: KS p = 0.994 and 0.518 |
| fig5a-signaling-rich-club | partially reproduced: 16 and 5 neurons, maxima at 25 and 42; the one-SD rule fails at k = 4 |
| fig5c-rich-clubs-disjoint | reproduced: only AVEL and AVER are in both |
| fig5b-degree-correlation | reproduced, assumed: r = 0.219 |
| ed10-rich-club-cell-classes | reproduced |
| ed9e-degree-observations | partially reproduced: r = 0.702; 10 of 16 rich club neurons well above the line |
| ave-most-connected-both | reproduced under reading (b), assumed |
| signaling-threshold-controls, bilateral-controls-signaling, rich-club-controls | blocked, data_missing |
| 21 claims on the community model and what depends on it | blocked, not_runnable |

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.240920.1434, the version the paper cites. Only the next version, 0.240930.1859, says which ROI each stimulation targeted, so that one column comes from it, listed under `inputs`.

**Findings about the dataset:**
- **No stimulated-neuron identities in the cited version** (major). The later version adds them, but only for 2815 of the 5614 stimulations.
- **Unmarked interpolation** (major). In the cited version, the green and red signals contain interpolated values for 17% to 68% of frames and ROIs per file (mean 42%), with nothing marking them.
- **Control recordings missing** (major). The q-values that define the network are computed against recordings without stimulation, and those are not in the dandiset. So the network can't be rebuilt from the data.
- **Network taken from the released atlas** (reading (b) in the claims file). The atlas has 1154 edges against the paper's 1151.
- **Atlas only partly matches the recordings.** Its amplitudes agree with the recordings (Spearman rho 0.52). But only 88% of its edges were measured in the dandiset, and 23 neurons it gives out-edges never appear as a labeled stimulation target.
- **Minor issues:**
  - Three recordings have raw imaging but no segmentation file.
  - Labels include sideless class names, numbers and free text, none described.
  - Two subjects give the strain "none".
  - pynwb 4.2.0 cannot read the files; I read them with h5py.
- **Checks that passed.** Stimulation times share the clock of the signals (108 of 108 recordings), and no recording is deposited twice.

**Assumption:** the paper doesn't name its four electron-microscopy connectomes or say how gap junctions get a direction. I used the four that Randi et al.'s code combines, with gap junctions in both directions. That choice matches every reported number, including the control densities; the alternatives change several of them, which is why three claims are marked assumed.

**Questions for the paper's authors** (recorded as findings):
- Which q-values or atlas file did the analysis use, and can the q-values be published so the q < 0.01 and q <= 0.18 controls can be built?
- Which four connectome datasets, and which gap-junction direction?

Also recorded is a paper inconsistency: the Results say "degree 25 or higher" and "40 or higher", but the counts of 16 and 5 only come out with "above 25" and "above 40".

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **The `data` field.** signaling-network-size is marked `data: dataset`, but reading (b) rests on an outside atlas. The protocol doesn't say whether the author may change `data`. I left it as is and recorded a deviation.
2. **Cited version lacks a needed variable.** The protocol says to pin the cited version but not whether a column may be taken from a later one. I took only the stimulation-target column from 0.240930.1859, listed it under `inputs`, and showed in the notebook how the versions differ.
3. **Link claim when outside data replaces the measurement.** The protocol describes link claims for labels and matching, not for an outside network that stands in for the analysis itself. I wrote the link claim, its criterion, and added it to `depends_on` of signaling-network-size.
4. **A claim with no criterion.** ed6-anatomy-feedforward has none. I applied the paper's test from the signaling version of the claim and defined what full and partial mean.
5. **Software that can't be installed with uv.** Not runnable fits the community model, but the protocol doesn't say whether a substitute is allowed. I wrote a substitute only for the rich-club rewiring, recorded as a deviation, and none for the community model.
6. **A criterion with no partial clause.** fig5a meets every condition except one, at k = 4. I recorded it as partially reproduced.
7. **Severity of unmarked interpolated values.** It sits between critical and major; I chose major, since the later version fixes it.

## 4. Runtime and failures

The session took about 50 minutes (08:08 to about 08:57 UTC). The notebook runs in 6.2 minutes with 1.2 GB peak memory, most of it streaming the 110 files. The only failures were graph-tool, which has no PyPI distribution, and pynwb reading the files. Nothing timed out.

Files are in `entries/dvali-2025/`:
- `reproduce_dvali_2025.ipynb`
- `networks.py`
- `README.md`

Outside the entry: `attempts/dvali-2025-01.yaml` and `claims/dvali-2025.yaml` (the added link claim and its dependency). The verifier package is in `executed/dvali-2025/handover/`.
