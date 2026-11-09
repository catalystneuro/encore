**Round 3 verification: Claar et al. 2023 (eLife 84630) on DANDI:000458 v0.230317.0039**

The claims file has 37 claims and the attempt record has 37 outcomes. Two outcomes have a `proposed` change; I reviewed only those two. Cell numbers are 0-based indices into `claar_lfp.ipynb` ("LFP").

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig3abc-decay-with-distance | partially_reproduced (from blocked, metadata_insufficient) | Yes | | LFP cell 9 prints 128 combinations of readings. MO exceeds VIS for all three signals in 112 of them, all six values are within tolerance in none, and at most three are within tolerance in any one. The criterion calls that a partial reproduction: the ordering holds but a value is out of tolerance. See the notes below. |
| fig3d-magnitudes | blocked, too_large (from blocked, metadata_insufficient) | Yes, with reservations | | LFP cell 13 prints the cost: 86 probe areas over 24 sites, 262 min with all readings, and 91 min just to read the LFP (76 min if each probe is read once). Even the cheapest figure is over 30 min. Layer 1 can be approximated as in fig3abc, so missing metadata no longer stops the test; its size does. See the reservations below. |

**fig3abc: what I checked**
- **Numbers come from the data.**
  - `claar.lfp_magnitudes` follows the Methods and the claims-file criterion: it rectifies, averages over channels, z-scores to the baseline, takes the AUC from 0 to 0.5 s, and normalises against 1000 onset shuffles.
  - The re-reference uses the median of the ACSF ("none") channels. The CSD is the second spatial difference after 8 ms and 26-then-4-channel smoothing.
  - LFP cell 3 confirms the channel sets: MOs on probe F (119 valid channels) and VISp on probe C (87 valid). Units are int16 with the stated conversion.
  - The artifact profile in cell 6 peaks at k+2 and k+3, inside the mask that runs from k−1 to k+4. At k+5 it is 40 µV against a baseline near 30 µV, a small residue.
- **The result does not hang on a chosen reading.**
  - All 16 combinations where the ordering fails are LFP readings at the high current, 1 Hz cutoff and −0.5 to 0 s baseline (cell 8: 8.49 against 9.76, among others).
  - The ordering holds for CSD in 32 of 32 readings and for spiking in 32 of 32 (cell 9).
  - It also holds with the Methods' signed spiking integral (MO 0.31 to 3.96, VIS negative) and with or without the layer-1 exclusion. So the outcome rests on neither the |z| variant nor the 100 µm assumption.
- **Criterion applied as written.** I recomputed the reversal count, the CSD shift of 2.84 from leaving out layer 1, and the |z| range of 28.31 to 31.37 from the cell 8 table. All match the notebook text (cell 11) and the record notes.
- **How weak the partial is.** The record says this, but it should be clear: the LFP in MO is never within tolerance (7.57 to 77.16). The signed spiking magnitude in MO is about a tenth of 30.9. Only the ordering is reproduced.

**fig3d: reservations**
- **Record numbers do not match the printout.** The record (proposed reason, notes, round-2 response) gives "about 265 min" and "92 min". Cell 13 prints 262 and 91. Cell 14 says the rate varies from run to run, so the record's numbers come from an earlier run and should be updated to the printed ones.
- **The estimate is rough.**
  - It scales total time by channels × samples, but the shuffle part scales with trials and channels, not samples.
  - It counts the ACSF channels once per area, which double-counts within a probe.
  - Neither issue changes the conclusion: even the 76 min read-once figure is more than double the limit.
- **Splitting the work is not addressed.** The analysis could be split across several notebooks of under 30 min each; the entry already has three. The record does not say why that is ruled out.
- **The limit and the category could not be checked.** The 30 min notebook limit and the `too_large` category are not in my materials (docs/protocol.md was not provided). I accept them as the record states them.

**Claims file: two possible misreadings of the paper (reported, not corrected)**
- **Signed versus |z| spiking magnitude.** For fig3d-magnitudes and fig3abc, the criterion fixes the spiking magnitude as the signed integral of z. It does not name the paper's Results remark as an open reading: "our magnitude metric accounts for both reductions as well as increases" (Results, Global ERPs…, paragraph 1).
  - The |z| reading reproduces the MO value: 28.31 to 31.37 against 30.9 (cell 8).
  - "Rectified" in the Methods does nothing to a non-negative spike density, so the paper's text is ambiguous here. A reader should decide which reading the criterion uses.
- **Shuffle over the recording.** The criterion's "uniform over the recording" shuffle is run here over the span of the awake pulses. The record lists this as a deviation, so it is not a claims-file issue, but it is a further approximation behind the shuffled values.
