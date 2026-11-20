No outcome changed. I kept fig5d-lag at partially reproduced, and the verifier would give not reproduced; that disagreement is now in the record. The entry passes `check` and ran cleanly twice in about 22.5 minutes, and both runs gave identical numbers.

**What changed in the outcomes**
- **fig5d-lag:** kept partially reproduced. The criterion defines no partial case, but the claim has two parts. The coupling holds and the lag does not, which is partial under the protocol's general definition.
- **fig7e-content-independent:** the verifier gave blocked for reason "other". I kept `methods_underspecified`, because the protocol says a claim that depends on blocked claims takes their reason, and both claims it depends on are blocked that way.
- **Totals in the record:** 5 reproduced, 9 partially reproduced, 9 not reproduced, 8 blocked.

**What I added or corrected**
- **Re-referenced LS channel (problem 1):** I re-detected events on the LS channel minus another LS channel on the same shank. It shows how far each HFO result depends on a signal shared with the hippocampal channel.
  - Coupled events landing on the same sample as the CA1 ripple fall from 35% to 4.1%.
  - Nothing else moves towards the paper. The lag is 0 to 0.8 ms (paper 6.4). No animal shows raised LS firing at the events. Coherence at ripples is 0.164 against 0.074 jittered, still 24 SD above chance. NREM rates are not above WAKE.
  - fig2 gets a shank-referenced variant: LS is highest in 2 of 4 recordings.
- **Phase locking from another shank (problem 5):** taking each unit's phase on another shank, 52.3% of 2003 units still lock, centred near the trough (190°). So the trough preference does not come from the units' own spikes.
- **Outputs the verifier asked for:**
  - units-table columns (only `clu_id`, `group_id`, `location`)
  - electrode groups and devices
  - LFP start time (0 s in every file)
  - ripple counts and the random-phase baseline for the coherence
  - which files hold position data (74) and how much of the trials they cover
  - fig2ef depth profiles (fig2ef stays blocked)
- **Corrections:**
  - The fig1c spike window was −10 to +11 ms and is now −10 to +10 ms; its numbers moved slightly.
  - The clock check now names the 10 recordings that peak off zero. The 7 hippocampal ones are all DT5.
  - The fig7e conclusions now explain how the start-to-stop counting window inflates the duration and CA1-spike results, and say reading (b) is unusable (about 41% by chance).
  - The fig4 blocks now say the shortfall comes from this attempt's detection, not from the archive.
- The shared-signal finding is updated with the re-referencing result. Some files list a device described as "reference sites a few millimeters dorsal" without saying which channels use it.
- `verifications` round 1 is recorded for all 31 claims. The README, the runtime (23 min) and the conclusions match the new outputs.

**What I did not do**
- I did not test replay score 1 alone (fig7e-replay). It would need a criterion written before running it, so it belongs in a new attempt.
- I did not repeat the verifier's synthetic test of the frequency estimator. Its finding is recorded as a deviation on fig1g, credited to the verifier.
- I downloaded no paper text, so `paper/` is empty in this checkout.
- `git status` lists sandbox placeholder files (`.bashrc`, `.idea`, `scripts` and others) that I did not create. They should not be committed.
