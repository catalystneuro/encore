I've finished the attempt on CRCNS:ac-2 (DeWeese & Zador 2004): steps 1 to 5 are done and the handover is built. The paper's main population values come back closely: total variability 4.58 mV against the paper's 4.6, and the best private estimate 1.51 mV against 1.6. Of 23 claims, 12 are reproduced, 8 partially reproduced, 2 not reproduced and 1 blocked. The notebook passes `entry.py all` and runs in 67 s.

**(1) Outcomes** ("assumed" means the outcome would change under another reading of a detail the paper leaves open)

| Claim | Outcome |
|---|---|
| fig3a-reliable-neuron | reproduced (022801md01b: 0.876 mV over 26 tones, q = 0.229 mV at 31,118 Hz) |
| fig2-stereotyped-shape | partially reproduced (ranges and shape hold; only 19/33 neurons peak within the claims file's 50 ms bound) |
| fig3b-total-variability-distribution | reproduced (assumed) |
| total-variability-population | reproduced (assumed), 4.58 ± 0.47 mV |
| lfp-culling-reduction | reproduced (assumed), 4.80 to 3.19 mV |
| fig5b-residual-lfp-psp-correlation | reproduced |
| fig7a-lfp-culling-estimation | partially reproduced (assumed); largest reduction 80% against 71 ± 7 |
| psp-culling-reduction | partially reproduced; mean 2.19 mV, but 30/33 neurons at or below 3.3 mV, not 32 |
| fig4c-psp-culling-can-increase | partially reproduced (assumed); 16/33 against 18 ± 1.8; Figure 4 neuron not found |
| fig7b-private-best-estimate | reproduced, 1.51 mV over 28 neurons |
| culling-controls | not reproduced; random culling matched to LFP culling gives 3.82 mV, not 4.5 |
| fig7d-large-responses | reproduced; private values from 14 neurons, not 16 |
| large-responses-controls | not reproduced; 2.43 and 2.40 mV against 3.2 |
| cv-large-responses | partially reproduced; two private CVs miss by 0.001 and 0.005 |
| lfp-cv-not-different | reproduced (p = 0.67) |
| anesthesia-comparison | partially reproduced; pentobarbital private value 0.98 against 1.1 ± 0.1 |
| fig8-spontaneous-veto | reproduced |
| overfitting-correction-example | reproduced (0.759, 0.746, 0.525, 0.538 mV) |
| private-shared-ranges | partially reproduced; only 64% of private values fall in 1 to 3 mV, the criterion needs 80% |
| quantal-comparison | reproduced (14/33) |
| mepsp-size | blocked, `methods_underspecified`; every detector and threshold reading is shown |
| recording-properties | reproduced (assumed) |
| access-resistance-depth-no-effect | reproduced (assumed) |

**(2) Dataset, assumptions and questions**
- **Version:** CRCNS data sets are unversioned. I recorded "unversioned" with the dataset DOI, and the notebook computes the MD5 of both tar files as it streams them. Both match `checksums.md5`.
- **What the dataset holds:** the 33 neurons, the 29 LFP flags, the three anesthetic groups (13/3/17) and the six TTX recordings the paper describes. Each neuron's `cell_specific_parameters.m` gives a stable epoch, which reproduces the paper's repetition counts exactly (mean 18.1, range 10 to 63), and a spike threshold. Neither field is documented for these neurons.
- **Findings recorded:**
  - The docs give a junction potential of about 10 mV in the depolarizing direction. The paper subtracts 12 mV, and only that reproduces its rest potentials (median −70.0, range −58.4 to −92.0 mV).
  - The docs call the prepulse height a voltage in mV; the values are currents in pA.
  - Recording depth is missing for 8 of the 33 neurons.
  - The TTX recording 030401md02h sits near +2.6 mV after its documented division by 4, which is not a membrane potential.
- **Assumptions:**
  - Spike trials are removed with the dataset's per-neuron threshold. The claims file's −20 mV rule gives 4.05 mV in place of 4.58 and is shown for every claim.
  - Input resistance is the prepulse response minus the recorded access resistance. With that subtraction the range is 19.1 to 140.6 MΩ (median 65.1), matching the paper; without it the claim fails.
  - The other open details from the claims file are all run and shown.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): the spike rule, how input resistance was measured, how mEPSPs were detected and sized, and the open details of the culling procedures.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or wrong**
1. **Tar files, not zips.** `archives.md` describes zips opened in place. ac-2 is a single 265 MB tar.gz, which cannot be read by range, so I streamed it once into memory (about 30 s), with nothing written to disk.
2. **`entry.py check` hangs.** Its `LONG_LITERAL` regex took over an hour (killed at the 1-hour timeout) on a 32-number list of tone frequencies, apparently from catastrophic backtracking. I worked around it by reading the tone list from the dataset's docs. The tool itself needs fixing.
3. **Clock check.** The suggested contrast (decoding in windows around trial start) cannot separate an offset from a response here: tones play in a fixed order, so the pre-stimulus window always carries the same preceding tone. I used post-onset tuning against a permutation null plus response-onset latency instead, and said so in the notebook.
4. **Claims-file header was wrong about spikes.** It says the spike rule "can change only the few trials with spikes"; it moves several results across their tolerances. I ran both rules and adopted one under step 1.6 without asking a reader, since this is a method detail, not a misreading.
5. **Gaps in criteria.** Several criteria define only "reproduced" and "partially reproduced". Where values missed narrowly but the effect held (cv-large-responses, anesthesia-comparison) I used partially reproduced. I used not reproduced for the two control claims, where the misses are large.
6. **When to set `assumed`.** The protocol doesn't say whether it applies when an alternative reading gives the same outcome. I set it only where the outcome would differ, and the notes say when it would not.

**(4) Runtime and failures**
- The notebook runs in 67 s from a clean environment; the run so far is about 1 h 30 min, an hour of it lost to the hanging check.
- No analysis failed and no claim was blocked for time.
- The handover is in `executed/crcns-ac-2-deweese-2004/handover/`. Nothing is committed.
