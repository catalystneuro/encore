I've worked through all of the verifier's round-1 points and re-ran the whole entry. `python tools/entry.py all entries/000773-hart-2024` passed in 30 min, and `check` reports 0 errors. The new outputs match my development run on a cached copy of the data number for number. Nothing is committed.

**Outcome changes**
- **figs3c-general-breadth-no-age-effect:** reproduced → blocked (methods underspecified), as the verifier gave. It uses the same automated ROI counts as fig2e, which is already blocked. That method misses the paper's effect, and its counts are implausible (17 to 173 ROIs per ant).
- **fig3d-pg-60-vs-90-days-same:** reproduced → blocked (methods underspecified), as the verifier gave. Only 1 of 8 of the 90-day PGa positions beats chance. Reading (b) compares two measuring pipelines, not two ages.
- **pg-opposite-modulation:** partially reproduced → not reproduced, as the verifier gave. Its criterion needs fig3d-pg-stronger-old, which fails.
- **fig4-general-odorants-decline:** not reproduced → partially reproduced. This follows from the new main measure below: 9 of 10 declines are significant. The verifier said not reproduced on the round-1 measure, and the record keeps that view. This result is fragile: two of the p-values are 0.0498 and 0.048, and none of the eight other variants reaches the partial level.
- **fig2b-gcamp-baseline-unchanged:** still blocked, but the reason is now `other` instead of `data_unreadable`, as the verifier gave. The data were never read because the server did not answer.

**What I added or corrected**
- **Chance level for each glomerulus placement:** I shuffled the Data S2 values 200 times, across trials and by odor. All 42 young placements beat chance; only 24 of 39 old ones do.
- **Held-out placement, now the main measure:** each odor's responses are read where the glomerulus was placed using the other odors only, so the values tested no longer chose the place. On those held-out trials the link agrees for 44 of 108 (41%), and for old ants 9 of 52. The link outcome stays partially reproduced under its written criterion; the notes say it would fail on held-out trials.
- **PGa result explained:** the one significant PGa result from round 1 (p = 0.044) disappears at every held-out placement (p 0.13 to 0.33). It came from choosing the place on the same trials.
- **Variants shown for every focal glomerulus claim:** placements above chance only, placement from the general odorants only, and the round-1 placement.
- **Reading (b) fix:** it now skips pixels whose baseline is at background level. The old-ant G1 means of 39 to 57 drop to 2.6 and -6.3.
- **Whole-AL offset:** with each ant's paraffin oil value subtracted, the ratios are 6.0 and 9.5, still short of 8.1 and 51.3. Without the minimum filter the map saturates near 4. So that claim stays partially reproduced either way.
- **Smaller fixes:**
  - The motion-exclusion reading now actually excludes trials (3 of them).
  - The notebook tries the Brain Image Library three times; all three failed.
  - I corrected the `roi_trace` docstring.
  - The record now says why G4 has 5 old ants and not 6: Data S2 holds only general-odorant trials for G4 of one old ant.
- **Paperwork:** the notebook conclusions, summary, README and attempt record are updated. The round is recorded under `verifications`, with the verifier's reasons and my response for each claim.
- **Two questions for a reader** in the new file `questions/000773.yaml`:
  - pg-opposite-modulation's criterion contradicts fig4-propionic-acid-g2-g3's.
  - Reading (b) of the 60-vs-90-day claim mixes two pipelines.

**Not done**
- I did not run the reverse cross-check (placing from the six alarm trials to test the general odorants). With six trials the best match is near 1 by chance anywhere.
- I could not try the Brain Image Library from another network; none was available to this run.
- I could not compare the whole-AL offset with the paper's Figure S3B scale, because its values are not in the text.
- The changes already in `tools/` were there before I started, and I left them alone.
