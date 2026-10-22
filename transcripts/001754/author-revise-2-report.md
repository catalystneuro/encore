No outcome changed. The round-2 verifier agreed with all 10 outcomes, and I agreed with it, so nothing is under `proposed`. I re-ran `python tools/entry.py all entries/001754-knierim-2000` after the final edits: 0 errors and the notebook passes. Every outcome printed by the criterion's rule matches the record.

**Corrected, for the four sentences the printed numbers did not support:**
- **si-comparable-to-preflight (cell 29, cell 30, record notes):** cell 29 now also prints every p unrounded. The M-b variant gives p 6.2e-07 and 2.5e-07, and the conclusion and notes now give those values in place of "p < 1e-6".
- **direction-selectivity (cell 51, cell 48, record notes):** cell 51 now counts, in each zip file of the NASA record (OSD-968), the entries with a position-like name, and prints their file extensions. None has such a name. The text now says that, and that the .cel spike files and the archives nested inside the processed-files zip were not opened, so whether the record holds continuous position is not known.
- **fig3-stability-across-sessions (cell 44, record notes):** the text now says that 17 of the 19 session 2 maps were tied to a unit, with all 11 active maps among them, and 23 of 23 in session 3. It had said every map was tied.
- **Cell 23:** it no longer says the position trace is not Rat 2's in Rat 2's flight-day-4 window. It now says the trace could not be attributed to either rat there (0 of 17 and 1 of 16 units).

**Added:**
- A round-2 entry under `verifications` in `attempts/001754-knierim-2000-03.yaml`, giving for each of the 10 claims whether the verifier agreed, its outcome, its reason in its own words, and my response.
- A header comment in the record describing this revision.

**Not done, and why:**
The verifier's remaining points don't decide any outcome under the criteria, so I recorded them and changed no analysis:
- Rat 2's flight-day-4 position trace may not be Rat 2's.
- fig3-stability-across-sessions and three-orthogonal-surfaces rest on M-b alone, the unsmoothed recomputed maps with few spikes per bin, a reading that is weak by construction.
- The cell counts differ from the paper's.
- Its earlier, non-deciding points (B4, B6 and the unknown smoothing kernel) stand as before.

The caveats were already stated in the notes, deviations and findings. Changing how these claims are tested would mean changing the claims file, which is not mine to change. Nothing is committed.
