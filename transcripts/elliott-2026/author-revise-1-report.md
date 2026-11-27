I worked through every point in the verifier's report. The entry passes `python tools/entry.py all entries/elliott-2026` (spike notebook 10.7 min, LFP notebook 24.9 min), and `check` reports 0 errors. The record also passes its schema. Nothing was committed.

## What changed in the outcomes
- **s4-ka-no-epileptiform: not reproduced → partially reproduced** (marked as resting on an assumption). The verifier was right that the test dropped "synchronized", even though the fig1g criterion defines it: a burst that raises the rate of most units. With that condition applied:
  - S3 to S6 have no synchronized burst under any reading.
  - S1 has 77 to 138 synchronized bursts and S2 has 89 to 134.
  - S2 has bursting epochs of 19 s, but S1's longest is only 8 to 10 s, below the 10 s the criterion needs.
  
  So the absence the claim states holds, and the positive control holds for S2 but not S1. Neither the criterion's "reproduced" clause nor its "not reproduced" clause fits.
- **ext3: kept as reproduced** (resting on an assumption). The verifier would give partial because the theta amplitude never doubles. The criterion accepts either theta or broadband amplitude, and broadband holds at all three electrodes. The disagreement is recorded, and the weak theta rise (at most 1.92 times) is stated in the notes.
- **table2-phase-locking-counts: kept as not reproduced.** The verifier would give partial using the code's spike selection. The claims file makes the Methods' selection the main reading and the code's a variant. Under the Methods' selection S1 gives 60 units against 70 ± 7. The disagreement is recorded.
- **Every other outcome is unchanged.** For ext12 I kept the block reason `not_runnable` (the verifier gave `other`) and added the missing explanation to the notebook.

## What I added or corrected
- **Values from the paper's code:** each one is now printed beside its source file, cell and line, and checked against the value used. This covers the sorting-file assignments, the seizure and non-seizure windows, the spans of the other recordings, the sub-burst times and the phase-cluster thresholds. All match.
  - The spans turn out to be the start and stop times in the names of the LFP files the code saved.
  - The code filters theta within each window, as the notebook does, which answers the edge-effect point.
- **S5 and S6:** the scan correlates over every offset, so it finds partial overlaps. The S3 sorting is found in a 40 s piece of its file, and every sub-3C file is at least 40 s long. So no sub-3C file holds part of the S5 recording, alone or joined to the others.
- **S2 initiation window:** windows of one theta cycle or longer (250 ms, 500 ms, 1 s) all pass the coherence test under all five seeds. ext4 stays partial because S5 and S6 cannot be tested.
- **Baselines for fig1j:** they are now stretches free of detected bursts just before initiation (S1 12.0 to 13.0 s, S2 34.45 to 35.2 s). I added the angle for the hilus on the other side and an S2 run with a full-cycle window. fig1j still fails.
- **ext3 onsets:** the criterion's onset falls at 0.73 to 0.90 s under all four burst readings, which leaves no 5 s baseline and lies inside the wavelet's edge region. I also ran the first epoch that has 5 s before it: the claim holds under burst reading (b) and not under (a).
- **Angle histograms:** 8 to 24% of the weight lies exactly on bin edges. With the bins shifted by half a bin or y flipped, S1 and S2 stay bipolar and no other slice becomes bipolar. I corrected the markdown that said the classes do not change with the flip.
- **Rolling-wave detector:** now run as the criterion defines it. It finds no rolling wave in 63 theta cycles, so the claim stays blocked.
- **ext12:** a notebook section now gives the reason for the block and prints the simulation's conda-only environment.
- **fig2a:** rerun with clusters from the full-cycle S2 window; theta still does not alternate.
- **Burst merge window:** a variant outside the criterion merges peaks closer than 500 ms. It gives 7.5 to 8.0 bursts per epoch under reading (b), inside the expected range, and 67 S1 bursts in one setting, which is the paper's count. It decides no outcome.
- **The record:** the round is recorded under `verifications`, and the affected notes and deviations are updated.
- **Questions to a reader:** I created `questions/elliott-2026.yaml` with five:
  - fig1g: whether the 50 ms merge counts sub-bursts as bursts.
  - ext3: whether the criterion's onset is the paper's initiation at 14.4 s.
  - fig2b: whether reading (b), which is significant by construction, is a reading of the paper.
  - table2-phase-locking-seizure-vs-not: the 4 ± 0.4 tolerance rejects the paper's own 8 of 180.
  - table1: whether the table's durations are the analysed spans or the file durations.

## Not done
- **Verifier problem 14** (readings b and c compare separately curated unit sets): no question added, as the notes already say this.
- **`runtime_minutes` in entry.yaml** still says 21 for the LFP notebook, which now takes 25. Editing it would have changed the entry after the final run.
- **Untracked files:** some dotfiles and folders I did not create appear in the checkout (`.bashrc`, `.idea`, `scripts` and others). I left them alone.
