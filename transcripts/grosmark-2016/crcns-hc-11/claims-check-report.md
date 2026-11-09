I've checked the claims file and corrected it; it is ready for an attempt (`ready: true`). Nothing is committed.

**Checker result:** `31 claims, 30 quotes, 21 statistical values, 9 problems`. The 9 are values the checker could not find in the text. Eight are printed only in the supplementary figure panels (S14 for fig4a, figs14-plastic-ripple-gain and figs14-plastic-ripple-bursting). I rendered those pages and they match. The ninth, 3.94e-06, is in the Figure S16 legend written as "3.94 x10-06", a form the checker doesn't read. All the other values the previous agent read from figures (S9B, S16D-E, S17, S18, S19A) also match the rendered pages.

**Changes, by claim**
- **fig1c-sequence-content:** added Figure S6 to the source and criterion. It is the only place the paper shows "MAZE highest" (true in all four animals); POST is above PRE in three of the four.
- **fig2d-high-dpcc-shuffle-abolishes-replay:** changed the expected value from 15 ± 7 to 15.5 ± 6.5. The old value covered 8 to 22%, but the criterion says 9 to 22% (the paper's 10 to 20% widened by 10% at each end).
- **fig3a-plastic-more-specific:**
  - Removed the statistic "p < 0.05". The paper prints no p-value for Fig. 3A.
  - Replaced the made-up rule "at least four of five measures" with all five. Figure S19E marks all six measures significant.
- **figs13-outfield-rate-falls:** the statement said within-field rate did not "change". The legend only says it did not significantly increase, so the statement and criterion now say "increase".
- **fig4a-rigid-fire-faster:** the statement says there is no difference during maze running, but the criterion never tested it. Added that test as a condition.
- **figs16ab-plastic-synchrony-increase:** the test comparing rigid and plastic coactivity change had no source. Now cites Fig. 4A and S19G, which compare each cell's change in coactivity by rank-sum test. The definition of that per-cell change isn't given, so the criterion lists two readings. Also noted that S16B shows significant increases in both groups.
- **fig4c-coactivation-by-rate:** now states that the paper names no test for Fig. 4B and 4C, and the tests in the criterion are standard choices.
- **New claim fig2e-plastic-removal:** the Fig. 2E finding (the PRE to POST increase depends on plastic cells) had no claim.
- **New claim figs19c-pcc-change-per-cell:** the reported 2.2% (PRE higher than POST) and 21.4% (POST higher than PRE) had no claim.

**What remains open** (recorded in the checks entry)
- The main-text figure images (Figs. 1 to 4) are not under `paper/`, so numbers printed only in those panels are missing. Criteria rely on the legends and the matching supplementary figures.
- Figure S17B is internally inconsistent: the legend gives a difference of -0.035, while its panels give r = -0.037 and -0.065 (difference -0.028). I left it out, along with other secondary panels (S5C, S7, S8, S15, S17E-F). Fig. 1D has no claim because the paper never states its result.
- The paper refers to the Methods for how cells were split into low and high firing rate, but the Methods don't give it. The readings in low-high-rate-split stand.
- The colour key in Figure S14 swaps the rigid and plastic labels compared with the legend text; the claims follow the text.

`git status` shows untracked files outside `claims/` (including `uv.lock`, possibly created when I ran `uv run` to render the PDF). I left them alone; per your instructions only files under `claims/crcns-hc-11/` are kept.
