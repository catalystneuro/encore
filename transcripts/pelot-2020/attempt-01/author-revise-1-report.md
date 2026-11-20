I've addressed all twelve points of the round-1 report. The entry passes `check` and the clean run (240 s), and every conclusion in the notebook and the record matches the new numbers. No outcome changed; the only status change is that `rat-carotid-sheath-bundles` is now blocked for `other` instead of `data_missing`.

**Mixed-model tests (points 2, 4 and 8).** All the mixed models are now tested with Kenward-Roger F tests and degrees of freedom, which is what JMP reports for these fits. I wrote it in `vagus.py` and checked it on a balanced test design, where it gives the exact F tests.
- It brings the nerve-diameter F values closer to the paper: 587.3, 11.03 and 2.450, against the paper's 577.1, 11.01 and 2.445.
- The pig df of 3.74 the verifier flagged comes from the observed information that the Satterthwaite method uses. Kenward-Roger uses the expected information and gives 7.55. The notebook prints both.
- With Kenward-Roger, `fascicles-larger-cervical` holds for all three species under both rat fascicle rules: pig p = 0.012, rat p = 0.044 (0.0089 with the paper code's rat values). Of the eight combinations printed, six give all three species and two give two, so the outcome stays marked as resting on an assumption.
- I dropped the degenerate rat-only fit (p = 1e-64). In its place is a rat-only Kenward-Roger model (p = 1.7e-07) and a paired t test (p = 8.0e-07).
- Satterthwaite for effects with more than one degree of freedom now uses the standard method lmerTest uses, not the mean of per-coefficient df.

**Added or corrected:**
- **`no-age-trend`:** the notebook now opens the supplement. Supplement 6 is only a figure of the metrics against age, with no test, so it doesn't settle the method. With a Holm correction no test is below 0.05, which would make the claim reproduced. I kept not reproduced, because the claims file fixes the uncorrected test.
- **Literature claims:**
  - The odd Fazan and Lachat rows are that study's own means converted between area and diameter; the notebook now prints Supplement 4's notes.
  - I added a left-side-only reading and stopped counting the "posterior study" part, which isn't in the claim. Human-pig is now 8 of 10 parts, still partially reproduced under both readings.
  - For the rat claim the readings disagree: left-only would make it reproduced. I kept every published row as the main reading, because the paper says it compares left and right nerves and Figure 7 plots both. The record marks this as an assumption.
- **`pig-if-mt-consistent`:** the bound-by-bound reading is shown. The MT minimum fails it (23.7 µm against 5 µm), and no fascicle under 23.7 µm exists in the deposited file. The outcome stays reproduced because the criterion only tests containment.
- **`peanut-fascicle-counts`:** per-sample pig counts are shown. The 25th cervical peanut fascicle isn't in any sample, and the code never saves its own count, so that can't be compared.
- **`rat-carotid-sheath-bundles`:** the nine cervical micrographs are now shown with the trace drawn over each. The claim stays blocked: no other bundle is traced or labelled, and a count by eye would be my judgement, not a measurement. This partly keeps the verifier's disagreement, and the record says so.
- **Checksum cell:** it now comes before the summary, so the handover no longer cuts it.
- The round is recorded under `verifications` for all 35 claims. `pypdf` was added to the requirements and the environment relocked.

**Not done, and why:**
- **Point 1:** I kept the largest rat fascicle as the main run, not the code's first-trace rule. The claims file and the paper's Methods both say "largest", and the protocol puts the Methods before the code. The code's rule runs as a variant on every claim it affects. Because the claims file reads the paper correctly here, I asked no question about it.
- **Point 9:** no change; both tests belong to the claims file.
- **Kenward-Roger check against R:** I couldn't run the R cross-check (lme4/pbkrtest) the verifier suggested, because R isn't installed.

**Question for a reader.** I added one to the new `questions/pelot-2020.yaml`. It asks whether `no-age-trend` should correct for the 26 tests, now that Supplement 6 turns out to be plots only.

Nothing was committed.
