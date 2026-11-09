No outcome changed and none is proposed, so the record still has 5 reproduced, 7 not reproduced and 9 blocked. The new analyses all agreed with the verified outcomes. I re-ran the entry with `python tools/entry.py all` (pass, 53.6 min), and `entry.py check` reports 0 errors. Nothing is committed.

**Added**
- **Edge-effect check** (the verifier's main open point). I joined each trial's three segments into one continuous trace by their `sampleinfo`; no samples were missing. Then I compared power filtered from each segment with power from the joined trace at the same samples.
  - Baseline power is unaffected: 0.999 to 1.000 of the joined trace's, in every band from 1.5 to 14 Hz.
  - Encoding theta power is 13% to 27% low, but only in its first 250 ms. Postcue power is at most 1.1% low.
  - With power taken from the joined trace, power-theta-sustained gives 1 of 10, 0 of 9 and 0 of 9 subjects, as before. The theta-peak-bands overlap is 3 of 10 (it was 4).
- **Code-window variant for theta-peak-bands**, shown again: overlap 4 of 10.
- **MTL-OFC equal-strength model on the 5 pairs that sliding windows select** (s9 and s10; not judged). It finds no frequency effect (p 0.36), no frequency × direction effect (p 0.44) and no direction effect (p 0.995). The direction test is a Welch t test, because two subjects can't support a subject random intercept. MTL-PFC has only 1 pair, too few for a model.

**Corrected**
- **Notebook cell 59 and the pac-mtl-ofc-direction notes:** they now say that under surrogate (a), on the code's selection, one part of condition (1) holds (p = 0.00018). The criterion counts that as partial. These results are not judged.
- **psi-theta-shift notes:** the code's single window is now called a variant the criterion does not judge. The intro, the windows deviation, the notes, the summary and the README now say that if the deposited scripts produced the paper's figures, the paper's numbers come from the code's windows, so the main reading does not recompute them.
- **crossspectral-equal-strength notes:** the unsupported "too few units under the claim's own rule" is replaced with the actual counts (0 MTL to PFC pairs, 1 PFC to MTL).
- **`fcx2.py` docstring:** it now names sliding windows as the reading the claims are judged on.
- **`entry.yaml`:** `runtime_minutes` raised from 50 to 55 to match the 53.6 min run.
- **Round 2 under `verifications`:** all 21 claims have the verifier's reasons and my responses.

**Not done, and why**
- **The 9 blocked claims keep the label `methods_underspecified`.** The verifier agreed they are blocked but questioned the label; I recorded that disagreement. The Methods' PSI, run as stated, selects 0% to 1% of units per system against the paper's 31% to 49%. The code's version of PSI selects 57% of units even with trials shuffled. So neither the paper nor its code establishes which procedure selected the paper's units.
- **behavior-no-difficulty-difference stays as verified, resting on `summary_file.csv`.** No new source for that file's response times was found.
- **Still not run:** frequency-resolved PSI and the other null reading (the verifier's B6). The verifier marked them as not affecting a conclusion.
- **No questions added to `questions/crcns-fcx-2.yaml`:** the report names no place where the claims file misreads the paper.
- **`tools/build_site.py`** was already modified before this run. I did not touch it, but it is in the working tree and the workflow may commit it.
- **The local executed copy's markdown was patched by hand.** After the final run I filled in one sentence (the code-window peak overlap) in the source notebook and made the same edit in `executed/`. No outputs changed.
