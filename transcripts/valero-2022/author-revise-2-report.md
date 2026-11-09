No outcome changed. The verifier disagreed on one claim, fig3g-spatial-information, and I agree with its argument. Round 2 can't change an outcome, so fig3g stays `reproduced` and I added a proposed change to `partially_reproduced` for a third verification round.

I re-ran `tools/entry.py all` twice and it passed both times (424 s, 0 check errors). Every number from the earlier run came out the same.

**Proposed change for fig3g.** The paper's control epochs are random 20 ms intervals between pulses, and the time-matched variant follows that most closely. Under that variant both correlations hold, but the increase in spatial information is negative in both groups and does not differ between them (p = 0.3). So the first part of the claim holds and the second does not. The dark-window control maps that currently give `reproduced` were themselves a revision of the original criterion. The analysis behind the proposal is already in the notebook's fig3g cell; the conclusion, summary and README now say a change is proposed.

**New outputs the report asked for:**
- **fig1e:** a sham test for reading (b), with onsets across all stimulation epochs jittered by up to 200 ms. 0 of 364 tests pass. The earlier sham tests only covered reading (a).
- **fig3c:** a chance level for reading (a). Control maps were thinned to each cell's own light time (2.6% to 6.2% of lap time), with 20 draws per cell. They show a field in 31.7% of draws on average, against 77.8% of cells with a light field. This is stated in the conclusion and notes, and the outcome is kept.
- **Dark windows:** the data check now prints the share of offsets between deposited pulses that are under 20 ms (3.8% and 3.2%). The text in cell 12, the figs11 deviations and the summary now say the files don't follow the 20 ms protocol in every case.

**Text corrected:**
- **fig3e:** "70 field directions" and "14 field directions from 7 cells", where it previously said fields.
- **figs10:**
  - The text now names the three sessions where the correlation is not significant.
  - The clock-check variant is now described as leaving out two sessions (n = 1055), not three.
- **fig1e:** the conclusion now says which sham test covers which reading.
- **fig3f:** the variant using stimulated laps only is now described as unable to differ, since dark windows lie only next to deposited pulses.
- **README:** the fig4c row no longer says "only", since place/non-place pairs have the same coefficient as place pairs. The run time now reads about seven minutes, and `entry.yaml` says 7.

Round 2 is recorded under `verifications` in `attempts/000568-valero-2022-01.yaml`, with the verifier's reasons and my response for each claim.

**Not done:**
- The Methods point is still open: the supplement remains unavailable, so the response test, field rule and control rule can't be checked against the paper.
- The two-sessions-from-one-mouse point needs no change beyond what the notes already say.

I didn't commit or push. Untracked dotfiles and a `scripts` folder are in the working tree; I didn't create them and left them alone.
