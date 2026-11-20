I've revised the attempt for every point in the round-2 report. No verified outcome changed, and I propose one change for a third round. The final run of `python tools/entry.py all entries/prakash-2022` passed with 0 errors and took 46 minutes. Its numbers match the conclusions.

**Proposed outcome change (for round 3)**
- **fig7d-contacts-exceeding-baseline** stays not reproduced. Under `proposed` I suggest blocked as `methods_underspecified`. A new notebook cell runs the claim's own rule on the paper's Fig. 7d data (Supplementary Data 7). It counts 20 of 25 Opsin (-) contacts above baseline (19 with the 10 s block variant), and the paper reports 2.7 per mouse. Those sheets hold averages over mice, not single mice, and the reason says so. Still, the rule as the Methods describe it cannot produce the paper's numbers from the paper's own data. So the result says more about the rule than about the recordings. The notes, the README and the summary now say this.

**Output added**
- **fig7d-superficial-layers:** a new cell prints the paper's per-contact Fig. 7d profiles next to this attempt's, as the verifier asked. In both, the gamma rise is largest at one end of the numbering and falls along it: from contact 1 in the paper, and from electrode 1 (z = 775) here. So the paper's contact 1 is most likely the same end of the probe as the files' electrode 1. Neither source says whether that end is near the surface, so the claim stays blocked.
- **New finding (`paper_inconsistency`):** the notes on the Fig. 7d sheets give the band as 30 to 100 Hz, but the figure legend says 80 to 100 Hz.

**Text corrected**
- **Run time and size (README and notebook intro):** they now give the measured figures. The six files are 49.1 GB including images. The main pipeline step took 38 to 50 minutes over three runs, and the whole notebook about 46 minutes.
- **fig6c:** the SB + CTZ test is the same under both readings, and green light lowers the counts under both. The claim therefore holds under both readings.
- **Bootstrap finding:** the per-mouse count is now 22 to 31, not 25 to 29.
- **"Asked of the authors":** replaced with "raised as methods_unavailable findings", since the authors were not contacted.
- **Supplementary Data 7 entry under inputs:** it no longer says "No outcome uses it". It now says no outcome depends on it, and that the fig7f-mua-electrodes notes and the two fig7d claims cite it.
- **Round 2 under `verifications`:** recorded for all 26 claims. The verifier agreed with every outcome; each claim has its reason in the verifier's words and a response.

**Not done**
- The onset of interlum_ctrl_4 is unchanged. As the verifier says, the files cannot show which onset is right, and the notes already say so.
- No questions file was written, because the verifier reported no place where the claims file misreads the paper.
