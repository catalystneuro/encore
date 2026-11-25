I've revised the attempt for every point in the round-1 report. Re-ran the entry with `python tools/entry.py all entries/kim-2026-learning`: 0 check errors, and the notebook passes in 1369 s (about 23 min). A second clean run gave identical outputs. The conclusions, README and record now quote the numbers from that run. Nothing is committed.

**Outcome changes (4):**
- **figs3-modulation-all-cells: partially reproduced → reproduced, marked as resting on an assumption.** Problem 13: responses are now computed at every current given, so the at-threshold test uses the rounded threshold current, as the criterion's reference to fig2g says. Modulation at threshold is then stable (p = 0.484 and 0.461). Restricted to 4–6 µA it rises, which would make the claim partial; that is shown as a variant, with a question for the authors.
- **fig5e-pyramidal-in-pl: not reproduced → partially reproduced**, as the verifier proposed. Pyramidal cells are 73.4% of PL units and 57.1% of NPL units, p = 0.000475. The effect is significant but weaker, and the NPL fraction is outside tolerance under all five seeds, so it is no longer seed-sensitive.
- **figs5-pre-movement-window: reproduced → partially reproduced, assumed** (problem 4). I adopted the reading where responses are recomputed in the 120 ms windows, as the cited code does. NPL modulation then rises at 4 and 6 µA under every seed. The other reading, which would give reproduced, is shown as a variant.
- **fig4g-modulated-count-mouse1:** still not reproduced, but now marked as resting on the 700 ms pre-window. With 300 or 500 ms, Mouse 1 becomes significant and so does the group test, which would make it partial.

**Corrections:**
- **fig2a:** fixed the session-threshold rule; the old medians had counted sessions with infinite thresholds. Reading (a) now gives 5.70 and 3.91 µA at the paper's n of 43 and 80, so both readings reproduce. I also added psignifit's own threshold parameter as a variant.
- **figs1e:** the conclusion and record quoted numbers from an earlier run. They now give 192.3 against 179.2 ms, p = 2.83e-11.
- **figs5-movement-onset:** the text wrongly said the 148 ms all-currents median was outside tolerance; it is inside.
- **Seeds (problem 10):** each claim now draws its own pulse-locking classes. This makes fig5fg-pl-modulation-latency and fig6f-pl-coupling-increase seed-sensitive (the outcomes themselves are unchanged). The pulse-locking code was sped up; it gives the same values.
- **Cell type (problem 5):** the stored label is now the main cell type for every claim. The 97 units where it disagrees with the recomputed value are not borderline cases, so the label was not computed from the stored waveform.

**Outputs the verifier asked for:**
- **Pulse-locked share:** the PL curves peak at a median of 3.75 ms. No spikes fall in the blanked 0–1.5 ms. The test's false-positive rate on these data is 2.4%. So the 80% share is not a blanking artefact or false positives, but I did not find its cause.
- **Control trains:** most trial tables agree with the 3 tabled bursts, but the spikes follow 10 bursts at 0.5 s. One session's trial table says 100 pulses over 4.7 s. A 10-burst variant gives no significant test at 5 µA; I kept the tabled bursts, and figs7 stays not reproduced, resting on assumptions. I extended the finding on the control tables.
- **Contact mapping:** both tables use Ripple channel numbers, and units on a stimulation channel sit 5–24 µm from it, so the mapping holds.
- **Pre-window:** 300 and 500 ms variants added, with the 700 ms choice now cited from the Results' delta-spike definition.
- **Other additions:** per-mouse tests for figs2ef (the counts change in 3 of 5 mice, so it stays not reproduced); wheel-threshold scaling for figs5-movement-onset; an unsmoothed variant for fig6d; the full volumetric description and the segmentation columns.

Round 1 is recorded under `verifications`; the verifier disagreed only on fig5e. I added one finding at the end (the fig. S3D question) and updated four existing statements, keeping their order.

**Not done:**
- No question was added to `questions/kim-2026-learning.yaml`, because the verifier found no misreading of the paper.
- I did not partly test fig3i or figs6 on untracked ROIs. Both claims are about the same neurons followed over weeks, and figs6 depends on a blocked claim, so both stay blocked. The notes say why.
- figs9 part (C) is still untestable: the controls have one NPL value.
