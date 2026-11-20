I've answered every point in the round-2 report. No outcome changed and nothing is proposed for round 3. The verifier agreed with all 35 outcomes, and the re-run gives the same numbers for every claim, so none of the conclusions needed new figures. `python tools/entry.py all entries/000552-huszar-2022` passes with 0 errors in about 8 minutes.

**Corrections and added outputs**
- **Sessions without units (fig7fg):** the count was wrong in cell 62 and the fig7fg notes. Of the paper's 96 sessions, 57 have units and 39 don't (not 31). Cell 63 now prints this.
- **Stimulation channels in raw files (B7):** the notebook now lists every dataset in all 13 raw files, not just one. None has a stimulation, TTL, event or pulse series, only the voltage series and the electrodes table. The general statement in cell 62, the Summary, the README and the ed2 notes now rests on all 13 files.
- **Cell 16 and ed2 notes:** these now give the paper's pulse protocol and clipping window. They say the paper states neither the gap between pulse blocks nor what the clipped samples contain. The conclusion that the stimulation period isn't in the recording is now conditional on clipped samples being flat or zero. Only one wideband file was scanned.
- **fig7fg connection test:** I added a version that tests the three bins around the cross-correlogram peak, as the Methods describe (`is_monosynaptic_peak` in `huszar.py`). It searches for the peak at lags up to 4.0 ms, a range the Methods don't give, and I chose it after seeing the first results. Both tests now pass a synthetic check in the notebook. I also added a second session from inside the Fig. 7f cohort, e13_26m1_211019.
  - The original test finds connections in 0.448 and 0.407 of pairs (old session, new session); the peak-centred one finds 0.405 and 0.394. The paper reports 0.173.
  - So the block stands. The notes now say the gap may come from this implementation as well as from what the Methods leave out.
- **Smaller fixes:**
  - Corrected a swapped column label in the fig6c output, which should read "(novel, familiar)".
  - The novel-explorations conclusion now states as an interpretation that the 164 cm T-maze is the paper's novel figure-eight.
  - The README run time now says about eight minutes.
- **Round 2 in the attempt record:** recorded under `verifications` for all 35 claims, with the verifier's reasons in its own words and my responses.
- **Paper text:** saved under `paper/` (PMC10807234, as BioC JSON and plain text). That folder is gitignored, so it won't be committed.

**Not done**
- **Earlier record entry:** the round-1 response for fig7fg also said "31 sessions". I left it as originally recorded, corrected the outcome notes, and said so in the round-2 summary.
- **fig5e rate rule (B4):** no change. The files hold no cell types or waveforms to check the 5 Hz rule against, and the dependence is already stated.
- **fig6d-rate:** no change. Its fragility is already stated in the notes, the conclusion and the summary.
- **Wideband scans:** the other 10 wideband files (54 to 184 GB each) were not scanned.
