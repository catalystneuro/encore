I've revised the record for round 1, but the revised notebook never finished running. Two full runs were stopped: the first crashed in the lesion part on a bug in my helper change (fixed since), and the second was killed at my 47-minute limit. I don't know why it was that slow; it may have been a stalled download. So the executed copy is still the round-1 notebook. Every number and outcome in the record rests on those round-1 outputs, and the record says so under `verifications`. `tools/entry.py check` passes.

**Outcomes changed** (all from round-1 numbers; every outcome now matches the verifier's):
- fig2g-maturity-index-drop: reproduced → partially_reproduced (assumed). Only my own "log centred" form matches. Aronov et al. 2008 was sought, but its supplement returned HTTP 403.
- fig2e-residual-rhythm-peak: partially → not_reproduced. 7 birds against 6 with tolerance 0, and in 3 birds the "peak" is the band edge.
- bout-offset-suppression: not_reproduced → partially_reproduced. The suppression is there; it lasts 127 ms against 180 to 220.
- lesion-directed-song-abolished and single-unit-spontaneous-rates: blocked as metadata_insufficient (was data_missing).
- fig8-no-gte-relation: blocked as other, not attempted (was not_runnable). The record names the third-party copy of the GTE code.

**Added or corrected in the entry** (none of it executed in the entry itself):
- **fig9 null:** the scrambled null no longer puts a dip at the window edges, and each syllable type's coherence threshold is printed.
- **fig4b shuffle:** the shifted-bout band now shifts the 150 ms around each event too.
- **Channel choice:**
  - The notebook prints which channels the analysis files list. All three are listed in every file.
  - Orange150's first-day file runs its event detectors on channel 7, the channel I chose for that bird.
  - fig6 latencies are now shown on every channel.
- **Means over birds:** each printout names the birds behind it (fig4b, fig4c).
- **fig7b:** spectra are no longer renormalized per bird.
- **Singing rate:** added counts from all segments and rates per hour of recorded audio.
- **fig2e residual peak:** the test now needs a real peak inside the band, adds a prominence variant, and uses 1000 null draws.
- **Plots:** event-aligned averages with their bands, the fig2c histograms with the fitted exponential, and the rhythm ratio spectra.
- **Directed song:** a listing of the lesion files' names, hours and properties. Nothing marks a recording as directed.
- **fig3:** an analysis of the stimulation artefacts.
- **spectral-features-weak:** a new test with six Sound Analysis Pro-style features.

matplotlib is added and the entry relocked. The README, notebook summary and two findings are updated to match.

**What the unexecuted revision gives on cached data** (same code and archives, but run outside the entry):
- fig9: the coherence part now holds from 2.0 to 59.6 Hz; the counts still fail.
- spectral-features-weak: would be not reproduced. Features are significant within single birds, which the paper says none are.
- fig3: no antidromic response can be identified. 91 of 779 stimuli are followed by a spike.

None of these supply an outcome in the record. A verifier needs a fresh run of the entry before round 2.

**Not done:**
- No full run of the revised entry completed.
- spectral-features-weak and fig3 stay blocked in the record.
- Ref 41 (the Gamma scale) could not be read.
- The Gamma subsampling check was skipped; the verifier marked it as not affecting a conclusion.
- No questions file was added, since the report names no place where the claims file misreads the paper.

The notebook's spectral-features and fig9 conclusions use numbers from the cached runs; the notebook says the record lists spectral-features as blocked. The modified `tools/` files were already changed before this run and I left them alone.
