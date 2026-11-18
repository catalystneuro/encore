I've finished the round-1 revision. The four notebooks ran from a clean environment with `tools/entry.py all` (main 20 min, LFP 51, Figure 7E 24, the new shanks notebook 14), and the entry checks pass with 0 errors. Nothing is committed.

**Outcomes changed**
- **fig5e-state-coupling:** not_reproduced → **partially_reproduced**, resting on an assumption. As the verifier suggested, I ran the inset test over all HFOs pooled: NREM 0.302 against WAKE 0.091, p = 3.1e-171. The CCG bins and the WAKE value still fail, so it is partial. Averaged over recordings it is still not reproduced (p = 0.0025). I adopted the pooled reading because the paper's NREM 0.3 matches the pooled 0.302 and not the per-recording mean of 0.213.
- **fig7e-content-independent and fig7e-coupled-only:** the block reason is now `other` instead of `metadata_insufficient`, as the verifier said. What blocks them is the content features, which were not attempted.

**Outcomes kept, with the disagreement recorded**
- **fig1c-post-burst-suppression:** stays not_reproduced; the verifier gave reproduced (fragile). I kept the window from each event's stop as the reading of "immediately following": it shows no suppression under any of the five seeds. The +20..50 ms window passes under 3 of 5 seeds.
- **ls-spikes-not-locked-to-ca1-ripples:** stays not_reproduced; the verifier gave partial. The criterion has no partial outcome, and the reading inside CA1 ripples finds 7.2% locked (p = 0.012).

**Added or corrected**
- **fig1h:** `peak_normed_power` (the lab's maximum NSS) is now the primary amplitude. Both tests are not significant, so the Pearson assumption is gone. The verifier asked whether that column really is the maximum NSS, so I recomputed it from the LFP. It ranks events the same way within each recording (median Spearman 0.877), but it gives a weak, significant correlation with frequency (r = 0.081). So the outcome is still reproduced but now rests on the deposited value.
- **Figure 7E:** the z reading the verifier described now runs beside the claims file's t-test, and both are tested on synthetic null data: the t-test calls 42.2% of neurons significant, the z reading 2.5%. Under the z reading 2 to 4 of 16 combinations are within tolerance, which would make these claims reproduced. The outcomes stay partial under the claims file, and I added the question to the new `questions/tingley-2019.yaml`.
- **fig1d own-shank locking:** a new notebook, `shanks_tingley_2019.ipynb`, reads the shanks outside the detection block. Together with the in-block shanks, 1615 of 1992 neurons are locked (81.1%), still below the 83.25% floor, so the outcome stays partial.
- **Figure 4 pair shortfall:** a new cell shows that the pairs are lost in the HFO epochs. Of 20182 candidate pairs, 795 pass inclusion in PRE and 954 in POST, against 10823 in BEHAV; the HFOs last 252 s and 355 s in all. DT8 has 3 and 10.
- **fig5f:** the "WAKE outside trials" reading is now run and gives the same result.
- **Site labels (fig2, medial septum):** the per-site profiles show that on the septal shank the labels ls, ms, acg and cc alternate along the channel order. With no site positions stored, I can't tell whether the labels or the channel order are wrong. This is now in the notes and recorded as a finding.
- **Data check:** it now lists every electrode and units column in one file per animal. There is no position column and one waveform per unit.
- **figs2c:** the notes now say the positive control is weak.
- **Record:** the round is under `verifications` for all 39 claims, and I added two `methods_unavailable` findings (Figure 1H amplitude, Figure 5E pooling) and one data finding (the site labels).

**Not done**
- The Figure 2 site ratios still use only two storage chunks per recording, and cingulate reading (b) is still not pooled across recordings.
- Replay, seqNMF and the Figure 8 model are still not attempted, for lack of time.
- To keep under the time limit, the shanks notebook reads only the out-of-block shanks. The 81.1% total therefore adds the counts from two notebooks, and the notes say so.
