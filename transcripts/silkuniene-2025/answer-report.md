I answered both questions and changed the claims file for each. `python tools/claims_check.py` reports 28 claims, 28 quotes and 0 problems. Nothing is committed.

**1. fig3a-centre-enhanced (should the Figs. 3 and 4 packet-rate claims list DANDI:001276?)** Claims file changed. The answer is yes for four of the nine claims, because 001276's CT26 wells at 2 bursts (x4) and 0.2 MHz match the paper's own description of that condition. The question reports that 001276 also holds 1-Hz wells and controls.
- **Can be tested in full:** fig3bc-rate-suppresses-off-target and fig4b-40-fold-ratio now list 001276. The first compares 1 Hz with 0.2 MHz, and the second uses 0.2 MHz only.
- **Partly:** fig3a-centre-enhanced and fig3-lorentzian-profile also list it. The paper states both "for every rate", so their criteria now say that with only some rates held, a claim can be at most partially reproduced.
- **Cannot be tested:** the other five need a trend across the rates, a set of comparisons across them, or the 1-kHz and 10-kHz wells. They do not list 001276.
- **Header:** it now records the reported 3.8-mm, 3.2-kV array in 001047 and explains why 001276 is listed. 001047 stays listed, and the author blocks a claim as data_missing where it lacks the data.

**2. fig7-offtarget-40-50-fold (which electrode footprint holds the background ROIs?)** Claims file changed. The paper says only "within a footprint of an electrode", and the question shows the choice changes the ratios by a factor of 2 or more, so it cannot be treated as a standard choice. Assumption O1 now lists four readings, one per electrode footprint, at the same position in every well.
- fig4b-40-fold-ratio and fig7-offtarget-40-50-fold now run every footprint and show every combination. A claim holds if one combination falls in range, and that outcome is marked as resting on the footprint that gives it.
- Every other claim that cites O1 now also runs the four footprints.

Both questions are marked `answered: 2026-11-20`.
