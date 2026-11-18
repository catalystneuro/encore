The entry and attempt record are written. `python tools/entry.py all` passes (0 check errors, notebook 15.5 min in a clean environment), and the handover is built in `executed/peron-2020/handover/`. Nothing is committed. Of the 30 claims, 19 are reproduced, 3 are not reproduced and 8 are blocked.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| 7 model claims (`model-*`) | Blocked (`other`): network simulations not built in this run |
| neurons-per-mouse | Reproduced (8,126 ± 2,436; all 16 counts equal Extended Data Table 1) |
| representation-sizes | Reproduced (reading a: 900.6 / 0.108, 864.6 / 0.106) |
| touch-ablation-size, whisking-ablation-size, silent-ablation-size | Reproduced |
| touch-ablation-reduces-touch | Reproduced (0.123 → 0.100, p = 0.004) |
| touch-ablation-touch-count, touch-ablation-whisking-unchanged | Reproduced |
| whisking-ablation-no-effect-touch / -whisking | Reproduced |
| silent-ablation-no-effect-touch / -whisking | Reproduced |
| ablation-type-specificity, ablation-size-correlation | Reproduced |
| distance-dependence-touch, distance-dependence-whisking-absent | Reproduced |
| behaviour-unchanged | Not reproduced (paired tests: silent fraction correct p = 0.008, whisking touches p = 0.047) |
| response-similarity-touch-ablation | Not reproduced (touch p = 0.180, whisking p = 0.039 under the Methods trial average) |
| response-similarity-example | Not reproduced (slope −0.393 against −0.44 ± 0.044) |
| response-similarity-whisking-ablation | Reproduced |
| ablation-no-off-target-event-rate, ablation-success-rate | Reproduced |
| glial-reaction-local | Blocked (`data_missing`: no histology in the data set) |
| per-mouse-table | Reproduced, marked as resting on an assumption (code's cylinder 24/24 rows; Methods cylinder 23/24) |

## 2. What was found

**About the dataset:**
- All 16 archives and all 24 ablations are present and read without errors.
- Session files are a mix of MATLAB v5 (94) and v7.3 (107), which nothing documents.
- The curation files that say which neurons were ablated aren't in the data descriptor; they can only be found through the paper's code.
- an278939's post-silent directory has no trial-averaged dF/F, so one whisking ablation is missing from the response-similarity analysis.
- an278937's pre-ablation data has a sixth subvolume (995 neurons) that its post-ablation data lacks.
- an250220 has no list of attempted neurons, and an257218's logs carry no target ids.
- Touch-triggered dF/F confirms that the touch times and imaging frames share a clock in all 201 files; there are no duplicate recordings.

**About the paper (code mismatches):**
- The grand medians given for whisking and silent ablations come from a row-indexing bug in `ablation_summ_stats.m`: one includes zero rows, the other is the median over all 24 ablations.
- The behaviour P values are rank-sum tests on histograms, not the paired signed-rank tests the legend names.
- The Fig. 3 values come from a trial-average bug that keeps only the right-trial average, and from fits to bin means, not to the neurons.
- The proximity exclusion in the code uses a signed depth rule, not the Methods' symmetric cylinder; the paper's numbers follow the code.
- The neuron counts printed with the medians are sums of score > 0.1 counts, not the number of neurons that enter the medians.

**Assumptions and questions for the paper's authors:** I used the code's cylinder for per-mouse-table and asked which rule is meant. The touch-burst merging method (`getBurstTimes`) isn't public, so I assumed a rule and asked how it works. **Questions to a reader:** none.

## 3. Protocol gaps

1. `archives.md` only covers zip files. The ssc-11 archives are tar.gz and can't be read at an offset, so I streamed each archive once with `requests` and a resume-on-drop reader. fsspec's stream mode had timed out, and its HTTP filesystem needs aiohttp, which wasn't in the locked environment.
2. "Develop on a subset" doesn't fit archives where reading one file means reading the whole archive. I timed one mouse, then did one full pass and kept the reduction in `$TMPDIR` for development only; the notebook streams the data fresh.
3. The protocol's block reasons have no entry for claims not attempted because of the run's time limit when no computation was started. I used `other` with a timing estimate (about 400 runs of about 20 s each).
4. It's unclear how a claims-file "variant" (here the code's cylinder) relates to a "reading". Where only the variant matched (per-mouse-table), I adopted it as an assumption and set `assumed: true`.
5. For claims of absence, the expected values sometimes fall outside tolerance while the test passes (whisking-ablation-no-effect-touch, post value 0.106 against 0.095). I followed the protocol: the test decides, and the gap is reported in the notes.
6. Reference values printed only in a PDF table (Extended Data Table 1) had to be typed into the notebook. I listed them under `inputs`.

## 4. Runtime and failures

- **Runtime:** one full pass over the data (128 GB) takes about 15 to 17 minutes with 4 parallel streams and peaks at about 4 GB per worker.
- **Failures along the way:**
  - The first full pass failed on a connection timeout; the resume-on-drop reader fixed this.
  - The second pass could not read the v7.3 files; I added an h5py reader.
  - The first `all` run failed on the missing aiohttp dependency; I replaced fsspec with `requests`.
- **Model claims:** I did not attempt them. A numpy timing prototype ran, but the network was not built.
