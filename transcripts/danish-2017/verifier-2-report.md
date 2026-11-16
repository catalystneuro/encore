**Verifier report, round 2: Danish, Aronov & Fee 2017 on CRCNS aa-3**

The claims file has 26 claims and the attempt record has 26 outcomes.

The main problem is that the record and README describe a notebook that no longer exists. The notebook I was given is the revised version, fully executed (execution counts 1–40 in order, and the new sections have outputs). The record's `verifications.reviewed` says the revision "did not finish executing" and that every number "rests on the round-1 executed notebook". The README says the same (line 44). Both statements are now false, and the record's numbers and three of its outcomes need to be redone from this notebook.

### 1. Outcomes

I agree with these outcomes, and where they rest on an assumption it is stated and reasonable:
- **Lesion song:** lesion-directed-song-abolished (blocked, metadata_insufficient), figs1 (data_missing), single-unit (metadata_insufficient), fig2f, fig2c, fig2d, fig2e-rhythmicity-drop, fig2e-residual-rhythm-peak (not_reproduced).
- **Electrophysiology:** fig4a, fig4b, fig4c, both fig5 claims, fig6-peak, fig6-dip, fig7a, fig7b, fig7d, bout-offset-suppression, no-motif-bout-signal.
- **fig8:** blocked (other, not attempted).

The channel assumption (`assumed: true` on all the electrophysiology outcomes) is stated and reasonable. Note that fig6-peak depends on it: on b871's channel 7 the peaks would be 18, 16 and 22 ms, a mean of 18.7, which is inside 20±2 (cell 21).

fig2g (`assumed: true`) is reasonable as partial. The adopted form ("log centred") was chosen after the fact, as the only one of 16 combinations that matches, and the record says so.

These need attention:
- **spectral-features-weak:** the record says blocked ("not executed"), but cells 42 and 43 executed it. Under the claims file's criterion it is not_reproduced: 9 of 18 bird-feature pairs are significant in single birds under reading (a) and 15 of 18 under (b). Pooled gravity center is 0.291 (a) and 0.082 (b) against 0.17±0.017, and pitch goodness and FM pass under every pooling. The record should read not_reproduced, `assumed: true`, because `uva.sap_features` only approximates SAP (Hann taper, its own FM and pitch-goodness definitions).
- **fig3-antidromic:** the record says "Not attempted". The notebook (cell 85) and the README instead say "no antidromic response identifiable". That finding is not supported, because cell 85 subtracts each file's median trace across stimuli before detecting spikes (`res = sn - np.median(sn, 0, ...)`). That removes any response that is time-locked in more than half the trials, which is exactly what an antidromic spike with jitter under 100 µs looks like. So "files with more than half of their stimuli followed by a spike: 1" is low by construction. The detection window of 1.5 to 5 ms also makes the latency part pass automatically. Blocked is still right under the claims file, which calls the claim untestable without stimulus times and identified units, but the stated reason should be that, not a negative finding.
- **lesion-undirected-rate-similar:** I agree with not_reproduced, but it rests on two measurement choices: selected segments, and the first-to-last-file span as recording time. With all segments, p = 0.078, 0.109 and 0.078 (cell 63). The notebook summary marks it "(assumption)", but the record has no `assumed: true` and its notes leave out the all-segment result.
- **fig9-long-syllable-gamma:** I agree with not_reproduced. The long-type fraction is 0.33, the fraction with a fast peak is 0.83, and the lowest peak is 10.7 Hz, all outside tolerance. The record's notes are out of date, though (see section 2). One minor point: the coherence is averaged over long types, where the criterion says "across-bird" average.

### 2. Sentences the numbers do not support

**Attempt record**, against the executed notebook:
- **fig9:** "exceeds its null only at 3.9, 5.9 to 12.7 and 40.0 to 43.0 Hz, not over 1.1 to 49.5 Hz". Cell 45 prints one unbroken range from 2.0 to 59.6 Hz above a threshold of 0.107, so the coherence part now holds (cell 46).
- **fig4b:** "leave the band 33 and 38 ms before onset (mean 35.5 …)", with measured 35.5. Cell 15 gives 36 and 38 ms, a mean of 37.0.
- **fig6-dip:** "drops below the band 40.3 ms … sits 0.3 ms inside the tolerance", with measured 40.3. Cell 23 gives 40.7 ms.
- **fig7b:** "The rectified amplitude gives 9.16 to 9.28 Hz. Over bouts the song amplitude peaks at 3.4 to 6.3 Hz." Cell 37 gives 9.28 Hz, and 6.10 to 6.23 Hz over bouts. The notes also leave out that the length normalization puts the MUA peak at 12.6 Hz (motifs) and 11.6 Hz (bouts).
- **fig2e-residual:** the deviation "200 synthetic null sets" is wrong; it is 1000 (cell 79). The notes also leave out the local-maximum test (7 of 7) and the prominence test (4 of 7, or 5 of 7) from cell 82.
- **fig3 and spectral-features:** "Not attempted" and "did not finish executing" are contradicted by cells 85 and 42.
- **Responses:** every response that says "(not executed in this run)" is now out of date.

**Result cells:**
- **Cell 83:** "local maxima 1.29 to 3.39". Cell 82 prints 1.286 to 3.342.
- **Cell 84 and Summary (cell 86):** "the multiunit signal shows no antidromic response that could be measured" and "blocked (other: no antidromic response identifiable)". These are not supported, for the median-subtraction reason in section 1.
- **Cell 43:** "pitch goodness, Wiener entropy and FM are significant under every reading". This holds for readings (a) and (b). Under the z-scored variant, Wiener entropy has p = 0.06 and is not significant.

Every other Result sentence matches its cell. I checked cells 13, 16, 19, 22, 24, 29, 31, 35, 38, 40, 46 (apart from the outdated record), 49, 54, 64, 67, 70, 74, 77 and 81.

**README:**
- Line 31: "Antidromic responses | Blocked: no antidromic response identifiable". This conflicts with the record and is unsupported (see section 1).
- Line 32: "Spectral features | Blocked: analysis added after round 1, not executed in time". The notebook executed it.
- Lines 43–44: "the revised version did not finish within 47 minutes". The notebook here is executed.
- The "(assumption)" tags in the README do not match the record. They are missing for fig4b/4c, fig5, fig6-peak, fig7b, fig9, bout-offset and no-motif, all of which have `assumed: true` in the record.

**My round-1 reasons:** the record states them faithfully in its own words. The fig4b reason correctly names the unshifted padding, my problem 8.

### 3. Round-1 points

Resolved in the notebook:
- **1 (fig9 nulls):** the scramble is now circular. The power threshold is about 0.015 and the coherence threshold 0.107.
- **4 (residual-peak test):** a local maximum is now required, a prominence test is added, and 1000 draws are used.
- **5 (small-syllable peaks):** the histograms are plotted and the noise bumps are acknowledged.
- **6 (singing rate):** all-segment rates and per-audio-hour rates are shown.
- **7 (nanmean):** the birds behind each mean are printed.
- **8 (shuffle padding):** the shuffle now wraps periodically.
- **9 (fig7b normalization):** the spectra are no longer renormalized.

Partly resolved:
- **2 (maturity index):** the form remains an assumption, and the author could not reach Aronov et al. 2008.
- **3 (channel):** `ChannelFiles` is printed and lists all three channels. Orange150's first-day file runs its detectors on channel 7. Latencies on every channel are shown. The choice is still an assumption, and fig6-peak depends on it.
- **10:** 1000 draws are now used. The 5-draw null mean and the 30 Hz bound remain.
- **12:** fig3 and spectral features were attempted in the notebook, but the record was not updated. fig8 is still not attempted.

Not addressed, and they do not bear on a conclusion: 11, 13, 14.

What remains that bears on a conclusion:
1. The record has to be regenerated from the executed notebook:
   - spectral-features-weak becomes not_reproduced, assumed.
   - fig3's blocked reason has to be fixed.
   - The fig9, fig4b, fig6-dip, fig7b and fig2e-residual notes and measured values have to be updated.
   - `assumed: true` should be added to the rate claim.
   - `verifications.reviewed` and the responses need correcting.
   - The README needs to match.
2. In fig3, the median-trace subtraction removes the very response the analysis looks for. Either redo the analysis without it, or drop the negative finding.
3. The channel assumption decides whether fig6-peak is partial or reproduced.
4. The maturity-index outcome depends on a form chosen after the fact.
