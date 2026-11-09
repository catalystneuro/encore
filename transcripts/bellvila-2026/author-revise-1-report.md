I changed no outcomes. One claim is reproduced (efield-20min-median, resting on an assumed channel layout) and the other 44 stay blocked. The final `python tools/entry.py all` passed with 0 check errors and the notebook ran in 731 s. I rebuilt the handover. Nothing is committed.

**Point 1, the too_large block on the 20-minute neurons.** The verifier was right that the old reason was weak: the 5- and 15-minute extrapolation gave anywhere from 52 to 126 minutes depending on the machine. I replaced it with a timed sort of one rat (sub-2023-04-28) over its whole 49.3-minute window: 20 minutes of baseline, 20 of stimulation and 9.3 after.
- **Timing:** loading took 65 s and sorting 391 s, or 9.2 s per minute of recording. Scaled to the 13 rats' windows (45.6 to 50 minutes each), that is about 98 minutes, against the 60-minute notebook limit. Two earlier runs gave 98 and 100.
- **Artifact removal:** before sorting I added a comb filter (Methods 2.5). It brings the 40 Hz artifact in the spike band down from 11–22 µV to 0.8–1.6 µV, close to the 0.4–2.0 µV before stimulation.
- **The sorted rat:** 26 units (median 1.5 per channel, against the paper's 44 per rat and 4 per channel), all passing the 0.25 Hz rule.

Sorting only some rats does not test the claims, because their counts are pooled over all 13. So too_large stays; the verifier would have called it "other", and that disagreement is recorded. The 8 power and PAC claims stay blocked with these neurons. Their notes now say the stored stream is not notch-filtered.

**Point 2 and section C, the electric field.**
- **Channel map:** I searched for the maker's map (Methods 2.3 names Microprobes; I checked its catalogue and TDT's manuals). It is not published, and the helper and the deviation now say so.
- **Random layouts:** over 2000 random channel layouts, reading (a) falls within tolerance in 18% of them and (b) in 43%. Over the smoothest 5% of layouts, the figures are 29% and 65%.
- **Bootstrap intervals:** for (b) the 95% interval is 1.310 to 1.777 mV/mm, a half-width of 0.234 against the paper's ±0.21. Resampling rats instead gives half-widths of 0.313 for (b) and 0.522 for (a).
- **Onset and offset:** I added a per-minute plot of the artifact for every rat and a check of each detected onset and offset.

**Point 5:** I added a per-electrode variant that uses all 16 electrodes and all 24 neighbour pairs. It gives 1.748 for (a) and 1.650 for (b), both within 1.65 ± 0.21.

**Point 8:** 14 of 208 channels, in 4 rats, change their artifact by more than half between the two halves of stimulation; in two rats it is the whole first row. Dropping the cells that touch them gives 1.834 for (a) and 1.695 for (b), both still within tolerance.

**Point 4, the claims file contradicting itself.** I added a question for a reader in the new `questions/001678.yaml`. It asks whether reading (ii) is the paper's method; the phrase "maximal electric fields" fits it best, and (ii) gives 3.698, outside the tolerance. It also asks which rule decides when readings disagree: the header says block the claim, while the criterion says one matching reading is enough. I followed the criterion and did not change the claim.

**Points 3 and 6, wrong reasons.**
- **baseline-fr and baseline-ppc:** the notebook header and notes now say their 20-minute halves are blocked with the 20-minute neurons as too large. The claims stay blocked as data_missing because their 1-minute halves have no data.
- **fem-depth-falloff:** its reason is corrected. As a ratio of fields, it does not depend on the missing 1-minute fields; the model being unavailable is what blocks it.
- **Kept category:** I kept data_missing for the three finite-element claims because the protocol gives that reason for an outside input that is not public (the rat model is licensed). The verifier's "other" is recorded.

**Point 7** needed no change.

I recorded round 1 under `verifications` for all 45 claims. The verifier agreed with every outcome; where it differed on the reason for a block, that is noted.

**Not done:**
- The 20-minute spike claims and the LFP claims that depend on them were not run, because the sorting alone does not fit in a notebook.
- I tried three ways to make the sorter faster: a different matching method, skipping matching, and installing torch. None helped or worked in this spikeinterface version.

Sources for the channel-map search:
- [TDT ZIF-Clip arrays manual](https://www.tdt.com/files/manuals/hardware/ZIFArrays.pdf)
- [TDT Channel Mapping Guide](https://www.tdt.com/files/manuals/ChannelMappingGuide.pdf)
- [Microprobes multichannel array catalog](https://microprobes.com/files/pdf/catalogs/MLS-Multichannel_Array_catalog.pdf)
- [Microprobes NiCr16 design form](https://microprobes.com/support-and-download/online-design-forms/odf-mwa-nicr-16)
