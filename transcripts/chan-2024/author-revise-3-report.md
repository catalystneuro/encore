Round 3 is applied and recorded. `python tools/entry.py all entries/chan-2024` re-ran the notebook (it passed in 484 s) and reported 0 errors.

**Outcome changed:** `fig4ab-no3-shortens-recognition` went from reproduced (assumed) to partially reproduced (assumed). The verifier agreed with the proposal, so I removed the `proposed` block.
- The "more severe" part holds under every reading and needs no wind.
- The cities below 400 m match the paper's nine only under the wind reading that takes the speed of the mean wind vector. Under that reading, the Table S13 distances that this claim depends on are not matched (0 or 1 of 8 values). Only 5 or 6 of the cities counted are among the paper's nine.
- I kept `assumed`, because the 400 m part is still worked out on the assumed MERRA-2 wind and city coordinates.

**Proposals that stand:** none. This was the only proposed change, and no other outcome changed.

**Other edits that follow from the round:**
- **Wording:** the verifier called one part of the proposed reason weak: that the paper's "mean horizontal wind speed" reads more naturally as the monthly mean speed. I dropped that wording from the outcome's notes and the notebook's conclusion. They now say both wind readings are plausible, that the outcome rests on the failed Table S13 match and the different cities, and that the criterion defines no partial outcome.
- **Deviation:** one deviation said "the cities themselves are not compared". It now says they are compared with the nine cities below 400 m in the paper's table.
- **Summary and README:** the notebook summary table and the README row now show the new outcome.
- **Round 3 record:** added under `verifications` with one result for this claim (agrees, partially_reproduced). It gives the verifier's reasons, including the two places where it found the claims file underspecified, and my response.

Nothing is committed. The working tree also has edits I did not make, to `tools/build_site.py`, `tools/runner/chain.sh` and `tools/site_assets/list.js`, and some untracked files such as `.bashrc`, `.idea` and `scripts`. I did not touch any of these.
