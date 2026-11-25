I've revised the attempt for verifier round 1. The entry re-ran with `python tools/entry.py all entries/powell-2021` and passed with 0 errors, and the record, notebook, summary and README now match the new numbers. Nothing was committed.

**Outcome changes (3)**
- **fig3-evoked-7-to-21-in-9-of-10: not reproduced → reproduced, marked as resting on an assumption.** Read as the criterion is worded ("every bin the preparation was held at"), 9 of 10 preparations pass. If 21 C must also be reached, 8 of 10 pass, and both counts are now shown. The verifier asked about 901_062's last stimulation blocks, which are now printed: its last stimulation was at 19 C and it was then cooled to about 7 C, so 21 C was never tried. The outcome depends on counting only temperature bins held for at least 120 s; counting every bin crossed gives 3 of 10. I added a `methods_unavailable` finding asking the paper's authors which bins they counted, and corrected the finding that said the data hold 8 of 10.
- **fig3s1-spontaneous-and-evoked-similar: blocked → not reproduced.** I tested the three preparations that have spike times, using the files the paper's script selects. Under the Methods burst rule only 901_080 is similar, so at most 2 of the 4 can be, whatever 941_006 would show. Among the ten evoked preparations, 3 burst before their first stimulation at 11 C, not 4; the paper's fourth is 941_006, which is not one of the ten. The table for all ten preparations that the verifier asked for is added.
- **fig6b-lg-start-counts: not reproduced → partially reproduced**, as the verifier gave it. Two of the three quantities are within tolerance, and the DG total is 22 over.

**Added or corrected**
- **Q10:** a variant using the measured temperature in place of the bin centre. Counts are unchanged.
- **Odd-temperature filter:** the notebook now prints what it drops: no slowdown stretches, 220 of 4128 LG burst starts, and 3.6% of LG and 9.2% of DG spikes.
- **fig5e:** two variants, counting only bins with more than one preparation (1 of 6) and building the shuffle from independent draws (2 or 3 of 8). Neither changes the outcome. Under one of the five seeds, the six-bin count gives 4 of 6, a majority, which is noted.
- **fig6b counts:** the notebook now states which denominator the fraction uses and why.
- **Error fixed in the fig5d text:** p misses 1e-5 at 17 and 21 C only, not 17, 19 and 21. The verifier's quoted reason still says 17, 19 and 21, as it wrote it.
- **New file `questions/powell-2021.yaml`** with four questions for a reader:
  - fig4c-q10-about-2, fig6b-lg-start-counts and fig6b-lg-phase-locked: should the code's method be the main reading, since the paper's numbers match it exactly?
  - fig5d-lg-pd-integer-coupled: the criterion's reproduced and partially-reproduced clauses contradict each other.
- **`verifications`:** round 1 recorded for all 22 claims, with the verifier's reasons in its own words and my response to each.

**Not done**
- I did not change any claim in the claims file, as instructed.
- fig3s1 still has no test of 941_006, because the record holds only its raw files with no spike times.
- Untracked dotfiles such as `.bashrc`, `.idea` and `scripts/` are at the repo root; I left them alone, and you may want to exclude them before the workflow commits.
