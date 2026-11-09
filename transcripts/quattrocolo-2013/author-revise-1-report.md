No outcomes changed. fig7a-olm-sag is still reproduced, resting on an assumed measure of sag, and the other 25 claims are still blocked as `data_missing`; the verifier agreed with all 26. I re-ran the entry with `python tools/entry.py all`: 0 check errors, and the notebook passes in about 10 s. The attempt record validates against the schema.

One new result matters for the reader. Reading (a)'s test (sag larger than twice the pre-step SD) also passes on each cell's 0 pA sweep, where no current is injected: 2.8 to 20.1 SDs. The 75 ms pre-step baseline misses slow drift in the voltage over the 1 s step (SD 0.59 to 1.03 mV). So reading (a) alone cannot tell a sag from noise in these recordings. The outcome still holds on measures that can:
- The -100 pA sags are 4.5 to 7.3 times the same measure on the 0 pA sweep.
- They are 4.2 to 10.8 times twice the SD of the 0 pA step window.
- Reading (b), the sag ratio, gives 3 of 3 cells, and no synthetic trace without a sag passes it.

The notes, conclusion, summary and a new deviation say this.

**Changes in reply to the report:**
1. **Raw minimum (point B1):** V_min is now taken from a 1 ms running mean in `hc9.py`, with the raw minimum as a variant. The new numbers are 17.5, 7.9 and 8.7 mV, with sag ratios 0.448, 0.224 and 0.208. A new cell repeats the verifier's synthetic test: the raw minimum passes reading (a) in 100 of 100 traces without a sag, the running mean in none.
2. **Noise floor (point C2):** the same cell runs the sag measure on each cell's 0 pA sweep, which gave the result above.
3. **Zoomed plot (point C1):** added a plot of the first 300 ms of each cell's -100 pA step.
4. **Error the verifier missed:** the old conclusion and notes said the Figure 7D cell's sag ratio lay between those of the two 7A cells. It is below both; I corrected it.
5. **Record:** round 1 is under `verifications`, with the verifier's reasons and my response for each claim.

**Not done, and why:**
- **Plot against Figure 7 (point C1):** I did not set the plot next to a crop of Figure 7. Entries may not embed images or copy figures, and the PDF cannot be rendered here because `pdftoppm` is not installed. So I could not compare the traces with the printed figure myself either; the notes say so.
- **"30 pA" in the claims-file header (point B4):** no question added for a reader. It repeats the data description, not the paper, and no claim rests on it. The description's error is already recorded as a `metadata_error` finding.
- **Panel mapping and +50 pA firing table (points B2 and B3):** left as they were, since the verifier found both consistent with the criterion.

Nothing is committed, as instructed.
