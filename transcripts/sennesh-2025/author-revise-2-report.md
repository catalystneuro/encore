I've finished the round-2 revision. No recorded outcome changed. I propose changing two outcomes, fig3h and fig3i, from reproduced to not reproduced, for the third round to decide. The last full run (`python tools/entry.py all entries/sennesh-2025`) passed both notebooks, `check` reports 0 errors, and every conclusion matches the new outputs.

**What changed in the outcomes**
- **The CSD tie-break (verifier's point 2):** I revised it as the verifier asked. A layer's sink onset now counts only if the sink is displayed and lasts at least 1/8 of a cycle at the band's centre frequency. The notebook also shows the old single-sample rule and the new rule at 1/16 and 1/4 of a cycle.
- **fig3h and fig3i:** both fail under the new rule with the adopted Methods' bands. In fig3h the L1 onset that decided it was one sample that isn't displayed; L1's lasting sink starts at 28.0 ms, after L2/3 and L4. In fig3i, L2/3 and L4 are both sinks from the start of the window. Each now has a `proposed` change to not reproduced, with its reason.
- **The other seven CSD claims:** same outcomes as before. The notes and Result cells now give the new onset times. fig2h, fig3i and fig4h now hold under the code's bands but not the Methods' bands, and the record says so.
- **fig3d:** I kept it as reproduced and recorded the verifier's disagreement (it rates it partially reproduced). The notebook now prints the outcome for each reading for fig2e, fig3d and fig4def. fig3d reproduces under only one of its four readings, and the notes say that.

**Critical findings**
- **Finding 1** (the cited version's LFP timestamps): I lowered it from critical to major, as the verifier rated it. The notebook now prints the timestamps of all 42 probe files of the 7 mice, and all 42 run 0, 24, 48 …, so the finding's "every probe file" is now shown.
- **Finding 2** (the same recording filed under two mice): the verifier agreed it is critical, and it stays so.

**Text corrected**
- **trial-counts note:** the left-out main-block sequences can only explain the xxxX and xxxY differences; the cause of the others is not known.
- **fig2ab:** under the per-trial dB reading the gamma does last past 250 ms; what fails is the 2.25 dB level.
- **Finding 12:** "4 of 13" corrected to at most 3 of 13, against at most 2 under 30-90 Hz.
- **fig4h:** the sentence about margins was wrong, since only the L1 margin is under 1 ms. The Result cell is rewritten and no longer claims it.
- **fig5 note and areas notebook:** now give the one-point difference in the GO count (1307 against 1308).
- **README:** the probe description now mentions the missing AL probes and the unlabelled probe, and the run times now match the logs.
- **Other text:** `glo.py`, the CSD methods question and the notebook Summary describe the new tie-break.

Round 2 is recorded under `verifications`, using the verifier's own words for each of the 37 claims and the two critical findings.

**Not done**
- I kept the code's spectrogram fitting range as the adopted reading. The verifier called the reason arguable but not unreasonable. The range is applied the same way to fig2e (where it lowers the outcome) and fig3d (where it raises it), and the question to the paper's authors stays open.
- I added nothing to `questions/sennesh-2025.yaml`, because the report found no place where the claims file misreads the paper.
- The untracked dotfiles at the repository root were not created by me, and I left them alone.
