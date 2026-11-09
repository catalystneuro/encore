I've finished steps 1 to 5 of the Author section and run the handover (step 6). The entry is `entries/okubo-2015/`, the record is `attempts/okubo-2015-01.yaml`, and the verifier's package is in `executed/okubo-2015/handover/`. `tools/entry.py all` reports 0 errors and the notebook passes in 925 s; a second clean run gave the same numbers. Nothing is committed.

## 1. Outcomes (42 claims: 19 reproduced, 15 partially reproduced, 4 not reproduced, 4 blocked)

| Claim | Outcome |
|---|---|
| counts-neurons-birds | reproduced (juvenile part: 1,116 neurons, 32 birds, 210 HVCp) |
| ed1a-stage-age | reproduced (rho 0.615; median ages 48, 58, 62, 73 dph) |
| fig1-subsong-locking | not reproduced (25 or 27 of 39 locked, paper 19) |
| fig1f-locking-increases | partially (juvenile stages only; r 0.196, fraction rises) |
| fig1f-rhythmic-protosyllable | partially (87 rhythmic against 70; period 161.6 or 174.9 ms) |
| fig1fg-rhythm-increases | partially (juvenile only; r 0.29 and 0.47) |
| ed1c-burst-width-rate | blocked, data_missing (needs the adult neurons) |
| fig1de-bout-related | not reproduced (342 bout-related against 285; too many post-bout neurons) |
| fig2b-protosequence | partially (55 neurons against 54; latencies span the protosyllable only in bird 2) |
| ed2st-coverage | partially, assumed (17 of 19 syllables over 90%; lowest 79.8%; 18 of 19 within their interval) |
| ed2p-probabilistic | reproduced (52.3% against 53%) |
| ed2qr-pairs-independent | partially (10 pairs; median r² 0.119, MI 0.083 bits) |
| fig2c-latency-subsong-earlier | reproduced (64% against 44% before onset, P = 0.038) |
| fig2c-latency-broadens-later | reproduced |
| bird1-protosequence | reproduced (14 of 16) |
| fig3g-bird1-shared-specific | reproduced, assumed (37 / 39 / 20) |
| ed4a-shared-latency-bird1 | partially, assumed (early r 0.852; late 0.700) |
| ed3j-shared-ibi-specific-doubled | reproduced (ratios 2.19 and 1.03 with 10 ms bins) |
| fig3h-bird1-shared-decrease | partially, assumed (8 shared late, against 10) |
| all-birds-shared-specific | partially, assumed (bird 3 has no labels; totals outside tolerance) |
| all-birds-shared-decrease | reproduced, assumed (CMH P = 1.3e-4 to 1.7e-6) |
| skipping-cycles | partially (found in birds 1, 3 and 4, not 6) |
| fig4-bird2-before-beta | partially (12 pre-bout neurons against 4) |
| fig4h-bird2-shared-early | partially, assumed (counts match; r 0.787, below 0.891) |
| fig4i-bird2-shared-decrease | partially, assumed (decrease P = 0.016; late counts off) |
| ed4bd-shared-latency-other | not reproduced, assumed (bird 2 late r = -0.41) |
| ed7-bird1-bd-shared-persist | reproduced, assumed (0.77 against 0.09) |
| ed8-bird3-phase | blocked, metadata_insufficient |
| motif-strategy-shared | blocked, metadata_insufficient (depends on ed8) |
| ed9-bird4-rhythms | not reproduced (8 rhythmic against 11) |
| ed4j-bias | partially, assumed |
| ed5-shared-acoustic-difference | blocked, not_runnable (needs Sound Analysis Pro) |
| ed5-shared-ra-x-proportion | reproduced, assumed (no difference, P = 0.116 and 0.085) |
| ed2mo-ra-x-similar | reproduced (juvenile only; only the motif-stage period differs) |
| model claims (8, run on a Python port of the paper's code) | 7 reproduced; model-ed10eh-motif partially (13 neurons still shared between two groups) |

## 2. Dataset, assumptions, questions

**What the dataset holds.**
- The spike times and syllables are in one 7.9 MB `Analysis_files.tar.gz`, with one MATLAB structure per neuron. I streamed it into memory.
- There are 1,125 neuron files. After the 5 s singing rule, 1,116 neurons remain, and the per-stage counts (39, 135, 564, 378) match the paper's to within one neuron.

**Findings recorded in the attempt:**
- The neuron list has a "young adult" stage the paper doesn't define: 66 neurons of bird 1, at 90 to 112 dph. The paper evidently counts them as motif.
- Two rows of the list share one name (`to3563_2013-02-25_HVCp-1`) but only one file exists for them.
- Bird 3's syllables are unlabelled except in 1 of its 19 neurons.
- The labels are Latin letters (a to e for alpha to epsilon), which the data descriptor doesn't say.
- The two rows of spike times per file are not documented.
- The 32 adult neurons are not in am-3, and I didn't find them elsewhere on CRCNS.

**Main assumption.** The paper adjusted the shared/specific test window by eye, which can't be repeated. I replaced it with a fixed rule: when a peak falls in the margin before onset or after offset, it is searched again inside the syllable. Without that rule, bursts in the gap between two syllables count for both. Bird 1 then has 32 shared neurons against the paper's 22, and the latency correlations vanish (r = -0.21). The notebook shows both versions.

**Other assumptions:**
- The syllable pairs for birds 5 and 6.
- The 19 syllables used for coverage (the paper's 20 are not listed).
- The early/late age boundaries for bird 1's B/D pair and bird 4's pairs.
- Iteration counts for the motif model.
- Bird 4's protosyllables are taken from the dataset's `a` labels.

**Questions for the paper's authors** (three `methods_unavailable` findings):
- The adjusted windows.
- The 8 pairs, the 20 syllables and the age boundaries.
- How the shift surrogates handle spikes past ±0.5 s, and the histogram bins. With every reading I tried, more neurons come out locked, rhythmic and post-bout than the paper reports.

**Questions to a reader:** none.

## 3. Where the protocol or tools didn't fit
1. `docs/archives.md` describes CRCNS data as zip files; am-3 uses `.tar.gz`. I streamed the archive into memory with `tarfile`, not on disk.
2. `entry.py lock` writes `python: "3.13"` into `entry.yaml`, and the entry schema then rejects that field. I removed the line. (`tools/entry.py` already had uncommitted changes in the checkout.)
3. `check` requires the word "unversioned" to appear in the notebook or a helper, which the docs don't mention. I added a `DATASET_VERSION` constant.
4. Blocked outcomes that name a notebook must have a tagged cell. I tagged three cells and dropped the notebook fields for the claim that has no code.
5. The protocol has no rule for a method the paper performed by eye. I treated it as an assumption under step 1.6 and showed both readings.
6. Where to draw the line between partially and not reproduced is left to judgement. I used "partially" when the effect held and some expected values matched.
7. Some criteria judge only a subset of the expected values (fig2c, ed2p, ed3j). I followed the criterion and gave the out-of-tolerance values in the notes.
8. For development only, I kept a pickle of per-neuron derived results in `$TMPDIR`, never raw data. The notebook computes everything from the streamed files.

## 4. Runtime and failures
- The run took about 1 h 30 min (19:35 to 21:04 UTC). The notebook takes about 15.4 minutes on 4 processes; memory peaked at about 1 GB per process.
- The model port (`hvcmodel.py`) was written by a subagent, and I checked HVCIter against the MATLAB line by line. MATLAB's random numbers can't be reproduced, so no model run matches the published figures exactly.
- No run failed. Only the entry check failed at first (items 2 to 4 above); it passes now.
