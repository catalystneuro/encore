I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all entries/keles-2024`. Both notebooks pass (reproduce 294 s, hfb 2518 s) and `check` reports 0 errors. No outcome changed: 27 claims are reproduced and the three fMRI claims stay blocked. I committed nothing.

**Outcomes the verifier disagreed with (kept, disagreement recorded)**
- **scanner-questions:** the verifier would block it; I kept it as reproduced. The protocol (Author, step 1.4) says a `data: elsewhere` claim is tested on the data where the paper deposited them and counted apart from the dandiset's claims. The notebooks, README and notes now say plainly that the result comes from the code repository's file, not the dandiset.
- **fmri-motion, fmri-tsnr, fmri-isc:** the verifier agrees they are blocked but gives `data_missing`. I kept `not_runnable`, since the protocol never uses `data_missing` for an `elsewhere` claim: the raw BIDS data are public, and what stops the test is that fMRIPrep cannot run here. I also corrected the old "30-minute limit" in their notes to the real 60-minute limit.

**Corrected**
- **LFP clock (B1):** the verifier was right. The stored `starting_time` matches the Usage Notes; it only breaks the NWB rule that `starting_time` is the time of the first sample. I rewrote the text in both notebooks, the README and the finding, which is now `format_error`. I also replaced the check that tested the wrong thing and the column that was true by construction.
- **Seeds (B4):** every permutation test now uses seed 0, as open detail 8 says. P-values moved slightly; no decision changed.
- **Bootstrap port (section C):** I added a cell-by-cell literal port of the original code's `ms_test`, `scenechange_test` and `get_bootstrappval`. At first it disagreed with the helper on 1128 of 1266 memory cells, by up to 0.068 in p. The cause was that the helper worked on spike counts, while the original code uses rates (count / 1.5 s), whose floating-point near-ties fall differently. The helper now uses the code's rates, and the two agree exactly on all 1266 memory and 1450 event cells. As a result ACC memory cells are 22/186, the paper's count (it was 21).
- **Projection distances (B5):** the gap is explained, 1266 − 26 + 2 = 1242. The 7 units with no waveform metrics are the same 7 units outside the 1450, and their pairs are left out (26). Two P58CS_R1 wires with no unit hold one distance each (2).
- **README and `entry.yaml`:** the hfb notebook now takes about 45 minutes, not 25.

**Outputs added (section C)**
- **Clock offset:** a sweep from 9 to 11 s and the HFB time course after image onset, shown next to the spikes'. With the 10-s offset the response reaches half its peak at 200 ms (macro) and 350 ms (micro), against 300 ms for spikes, with no response before onset. So the offset is right to within about 100 ms.
- **HFB intermediate steps:** line-noise power at 60/120/180 Hz before and after the filters, and per-channel HFB statistics.
- **Confidence-accuracy:** a table of every session's responses per confidence level, with why each of the seven excluded sessions is dropped.
- **Gaze sigma (B6):** I cited the code lines (sigma is taken at line 120, before the exclusion at line 130). With sigma from the 27 kept sessions, r = 0.754 ± 0.123, still within tolerance.

**Question for a reader:** the "higher" against "different" wording in confidence-accuracy (B7) is now in a new `questions/keles-2024.yaml`. The claim is unchanged, and the outcome holds either way because high confidence is above low.

**Record:** round 1 is under `verifications` in `attempts/keles-2024-01.yaml`, with the verifier's reasons and my responses. I also moved the provenance protocol from pilot-12 to pilot-14, the version this revision followed.

**Not done:** I didn't run `handover`, because the workflow prepares round 2. Nothing needed a new lock: the requirements are unchanged.
