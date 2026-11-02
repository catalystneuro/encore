I've finished steps 1 to 5 of the Author section and run the handover (step 6). The entry passes `tools/entry.py all` and runs in 201 s from a clean environment. I did not verify my own work, and nothing is committed.

The files are `entries/001262-heeringa-2024/` (notebook, `gerbil_an.py`, README, lock files) and `attempts/001262-heeringa-2024-01.yaml`. I pinned version 0.241205.0959, the newer of the two published versions. The paper cites only the Dryad deposit, and both versions hold the same 1160 files, so the choice changes no number.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| table1-animals-units | reproduced (all 11 counts) |
| table1-age-abr-weight | reproduced, assumed (ABR decoding) |
| table1-bf-range | reproduced (exact) |
| fig3-abr-age | reproduced, assumed (ABR decoding) |
| females-fewer-in-old | reproduced |
| oxygen-78 | reproduced |
| complex-stimuli-experiments | reproduced (21, 5, 17) |
| recording-type-counts | partially reproduced (5 of 6 match; CLICK is 271 or 275, paper says 261) |
| fig7-sampling-by-age | reproduced |
| isi-exclusion | not reproduced (370, 391 and 148 units fail under readings a, b, c) |
| no-prepotentials | blocked, methods_underspecified |
| rlf-monotonic | blocked, methods_underspecified (description shown) |
| fig5b-example | reproduced (7620 Hz, 19 dB) |
| fig6a-young-two-sensitive-regions | reproduced (holds under reading b only) |
| fig6b-young-bf-gap | not reproduced (the named bin holds 34 units; its neighbours hold 34 and 35) |
| fig6c-sr-distributions | reproduced |
| fig6d-max-phase-locking-bf | reproduced (4598 Hz; recomputed vector strength) |
| fig6d-highest-vs-low-bf-low-sr | reproduced |
| fig7a-cf-matches-bf | reproduced (r = 0.973, median CF/BF 1.003; recomputed CF) |
| fig7b-click-latency-bf | reproduced, assumed (r = -0.88; click delay assumed) |
| fig7ab-representative-sampling | not reproduced (the CF units' BFs differ from the full set under every reading) |
| old-success-rate | blocked, data_missing |
| psth-primary-like | blocked, methods_underspecified |

**2. What was found about the dataset**
- **ABR threshold.** It is stored as a single character in `general/notes`, and the character's code point is the threshold ("#" is 35). Decoded this way, the values reproduce Table 1's means and SDs exactly. I recorded it as a format error.
- **Missing analysed values.** The NWB files keep only the best frequency, spontaneous rate and threshold per recording. The characteristic frequency, vector strength and its p-value, and the click latencies are missing, so I recomputed them from the spike times with the paper's own MATLAB functions (Zenodo 10370064). The CF uses only the code's automatic pass; the manual corrections it allows are not in the data.
- **Click delay.** The CLICK trials have no delay in the files.
- **Short inter-spike intervals.** Many units have intervals below 0.6 ms, though the paper says such units were excluded.
- **Recording technique.** The extracellular recordings are stored as intracellular voltage-clamp series, and the archive summary lists the technique as "voltage clamp".
- **Unsuccessful experiments.** Animals operated on without a successful recording are not listed anywhere, so the success rates can't be checked.
- **Assumptions** (marked `assumed: true` on those three claims):
  - The ABR character is read as its code point.
  - The click delay is 7.75 ms, the delay of every tone recording. The result is the same with 5 ms.
- **Question for the paper's author:** what was the click delay in the CLICK recordings, and was it the same in all of them? It is recorded as a `methods_unavailable` finding.
- **Questions to a reader:** none.

**3. Points where the protocol was unclear or missing something**
1. Neither the protocol nor the claims file says what to do when the criteria name stored values the dataset lacks but which the paper's code can recompute from the raw data. I recomputed them, cited the functions, and recorded deviations.
2. `assumed` is defined for methods the paper leaves open. The ABR decoding is a reading of the data, not a method, but I marked the outcomes `assumed` so it is visible.
3. The fig7ab criterion ("not reproduced when none does") is ambiguous when the CF and CLICK subsets give different results. I took "a reading holds" to mean it holds for both subsets, and the notes give the other reading, under which the claim would be blocked.
4. The protocol does not say whether a blocked claim may have outputs. For rlf-monotonic and old-success-rate I added tagged cells with the description the criterion asks for.
5. The protocol does not say whether code read only for method details goes under `inputs`. I left `inputs` empty and cited the Zenodo code in the helper and the deviations.
6. Step 2's clock check is phrased as decoding a task variable. I used a contrast instead: rate in tone trials minus rate in silent trials, in 5 ms windows from trial start.

**4. Runtime and failures**
The run took from 13:32 to about 14:07 UTC. The notebook takes 3.3 min, mostly reading the 1160 files in parallel with processes; threads were slow because h5py holds a global lock. Nothing failed. The only error on the way was a text substitution in my notebook build script, which I fixed and re-ran.
