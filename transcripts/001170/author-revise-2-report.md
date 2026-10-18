No outcomes changed. The round-2 verifier agreed with all 19, including figs7e-ibi-chance, which it now accepts as blocked (methods underspecified). That leaves 6 reproduced, 6 partially reproduced, 4 not reproduced and 3 blocked. Nothing went under `proposed`.

I re-ran `python tools/entry.py all entries/001170-ling-2023` and it passed (183 s), as did `tools/entry.py check`. The numbers are the same as before, and the corrected text matches the new outputs.

**What I corrected, one item per point in the report:**
- **fig2f and the whole-window z-score:** the README, the Summary and the first `metadata_insufficient` finding said the ON/OFF anticorrelation appears with that z-score. They now say only the fig6e contrast and the fig7d negative correlations from 5 s on appear with it. The time-averaged ON and OFF vectors are not anticorrelated with any normalisation tried (median r 0.068, 12 of 28 below 0).
- **Window drift:** the Summary said up to about 2 s. It now says 912 frames last 51.2 to 66.4 s, a drift of 6 to 9 s at the extremes and about 1.8 s in sub-141 ses-8. The `code_mismatch` finding gives the same range.
- **"Only because of the centring":** the README now limits this to the mouse (uncentred mean 71.8). It gives the locust figure without centring, after subtracting the pre-odor baseline: 91.9, with 9 of 11 odors above 90. The Summary says the same.
- **fig7h null mean:** corrected from 17.1% to 16.7% in the cell 51 conclusion and in the notes.
- **fig7j block-relabelling null:** I removed it from the code (cell 53), from the cell 55 conclusion and from the notes, and dropped the `itertools` import it alone used. The text now says why no permutation that keeps whole blocks can serve as a null.
- **fig7j pseudo-trials:** these now read "nearly as high as" the ITIs, "within the 15 min after each block". I checked against the new outputs that the pseudo-trial maximum is below the ITI minimum in 4 of 7 sessions.
- **fig7d synthetic check:** cell 48 and the notes now say the synthetic values (−0.90 and −0.93) have the same sign as the data but a larger size.

**Record:** round 2 is under `verifications`, with the verifier's reasons taken from the report and my reply to each under `response`.

**Not done:**
- I downloaded no paper text, so there was nothing to save under `paper/`. The verifier's saved v2 text is not in this checkout.
- Table S1 of the preprint is still unchecked, as the verifier noted. It is an image.
- Several untracked files at the repo root (shell dotfiles, `.idea`, `.vscode`, `.mcp.json`, `scripts`) were not created by this edit. I left them alone; whoever commits should leave them out.

Nothing is committed.
