No outcome changed in this round. The verifier agreed with all 19 outcomes in round 1, and the fixes and new outputs did not move any of them. The clean run of `python tools/entry.py all entries/yang-2025` passes with 0 errors in 589 s, and its numbers match the conclusions and the attempt record. Nothing is committed.

**Fixes, by report point**
1. **Onset and end rule:** the notebook now checks it further and plots LFP, line-length score, onset, end and trains for four example clips.
   - The idea that clips were cut around the authors' onset at 300 s does not hold. In stimulation clips the first train falls at a median 309 s (middle half 292 to 328 s), and only 21 of 250 fall between 300 and 305 s, so I did not run 300 s as an onset.
   - The detected end comes a median 8 to 10 s after the last train, and within 2 s of it in only 24 of 248 seizures. A "device end" variant (a seizure ends no earlier than its last train) is now shown for every duration claim and for the interictal spike (IIS) claim.
2. **Unstable readings:** AIC model order was re-run with the cap raised from 20 to 30. For figs2 this gives 21 of 28 groups, and counts of 8 target and 20 non-target, as in Figure S2. That is still partial, because only 22 of the 28 labels agree. The record and conclusions now say that tables1 rests on counting self-pairs and that fig2 and figs2 rest on AIC order.
3. **HFO detector:** it is now the HFO App's short line length detector at its own defaults, which I read from the app's source on GitHub (zelanolab/hfoapp, commit 1ccff19). Events near stimulation trains are removed in place of the paper's manual review. I added a variant that sets the threshold outside the trains, and a pooled normalization that drops no seizure.
4. **IIS artefact:** spikes within 0.5 s of a train are now dropped and that time left out. Hardly anything moves (7 of 249 seizures lose any time), so artefact does not make the difference. fig5b depends on rat R7 alone: without it the time-bin test gives p = 0.16. It stays reproduced on the criterion, and the record says this.
5. **PSD and HFO windows:** the main windows now stay 0.25 s clear of every train and stop where the next train starts. The windows as worded in the paper and a 5 s pre window are shown as variants.
6. **Group order:** the Figure S2 order is now a variant of the duration claims.
7. **Dunn pairs:** the pairs found under each Dunn reading are printed.
8. **One-sided tests:** two-sided tests are added; the count stays at 3.
9. **Mixed units:** under the stimulated-channel reading, a baseline seizure now gives one channel, the site stimulated next.
10. **Tolerance scale:** tolerances are judged only for the relative change.

**Other additions**
- `verifications` round 1 in `attempts/yang-2025-01.yaml`, with the verifier's reasons in its own words and my response for each claim. The figs2 measured values are now 8 and 20, from AIC order capped at 30.
- `questions/yang-2025.yaml`: the partial clause of fig3a-per-rat-site-differences does not require R1 and R6 to have no significant pairs. If it did, that outcome would be not reproduced. The claim itself is unchanged.
- I updated the question to the paper's authors about the HFO App settings.

**Other changes**
- The first clean run took 45 min. Worker processes forked after numpy had loaded ignored the one-thread setting, so their VAR fits competed for the CPUs. The helper now starts its 4 workers with spawn, and the run takes about 10 min.
- matplotlib is added to the requirements for the new figure, and the lock file was regenerated.
- As in earlier runs, `lock` wrote a `python: "3.13"` line into `entry.yaml` that the schema rejects, so I removed it.

**Not done**
- The five blocked claims are unchanged; the verifier agreed they are blocked.
- I did not adopt any proxy for seizure rate.
- The onset rule is still an assumption: nothing in the dandiset can validate it beyond the train-timing checks above.

Sources:
- [HFOApp (eNeuro)](https://www.eneuro.org/content/8/5/ENEURO.0509-20.2021)
- [zelanolab/hfoapp](https://github.com/zelanolab/hfoapp)
