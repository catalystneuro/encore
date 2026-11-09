**Round 2 verification: doi:10.1038/s41586-025-09235-0 on DANDI 000409 (0.260309.1324)**

Counts come from the files. The claims file has 30 claims. The attempt record now gives 17 reproduced, 4 partially reproduced, 2 not reproduced and 7 blocked. Since round 1, traj-stim-regions has moved from blocked to not reproduced. Cell indices below refer to the re-executed notebook, which has been renumbered since round 1. I did not download the paper this round: every check here is against the notebook's printed outputs and the criteria in the claims file.

**1. Outcomes**

I agree with 29 of the 30 stated outcomes. I disagree with one:

- **behav-zero-contrast** (record: partially reproduced; mine: not reproduced). The criterion defines only the reproduced case: both values within tolerance under one reading. Every other criterion in the file with two parts defines a partial case explicitly, and this one does not. Neither reading meets it (cell 48). With the 454 canonical sessions the mean is still 58.27%, so the miss of 0.04 points beyond the tolerance stands.

Notes on outcomes I agree with:

- **traj-stim-regions** (not reproduced): I agree. The criterion was written after round 1, but the counts are far from the target whichever choice is made: 46 under reading (a), 62 under (b), 46 to 53 in the variants, against 104 ± 10.4 (cell 99).
- **fig1g-block-switch** and **behav-performance** (reproduced) each pass under only one of the readings the criterion allows:
  - fig1g-block-switch: 75.9% of bootstrap resamples fall within 4.5 to 11 (cell 60).
  - behav-performance: the reading that passes, the mean over sessions, is not the reading whose s.e.m. matches the paper's ± 0.4 (cell 45).

**2. Sentences the outputs do not support**

- **README, run time:** "It takes about 26 minutes: 2 to scan … 1 to stream the spikes of the 14 regions … 12 to stream every canonical unit". The outputs show:
  - Cell 105: 29.4 min in total.
  - Cell 1: the scan took 224 s, about 3.7 min.
  - Cell 66: the 14-region stream took 115 s, about 1.9 min.
  - Cell 67: the full stream took 814 s, 13.6 min.
- **Attempt record, wheel-speed-decoding notes:** "the notebook estimates about 29 minutes to decode one binary variable". Cell 105 prints about 41 min. The record's own response to round 1 also says 41.
- **Cell 97 and the traj-latency-late notes:** "so they do not depend on where the window ends here". This holds only between 150 and 200 ms. In the 0 to 100 ms window, which is the paper's, IRN has no latency and GRN gives 100.0 ms (cell 96). The next sentence of cell 97 says this itself. The IRN distance is also still rising at 189.5 ms (cell 91).
- **Cell 103:** "The power difference does not rest on the larger evoked response after reward alone". Neither variant removes the evoked difference:
  - The z-score is computed per unit over both conditions together (`z.mean((1, 2))` on units × condition × bins), so the gap between correct and incorrect amplitude remains.
  - The fractional variant measures power in a band centred on the correct-trial peak. The incorrect trials are measured at that same frequency, which favours the correct trials by selection.
- **Attempt record, dec-feedback-nearly-all notes:** "The partial outcome comes in part from … the smaller null". No output shows this. HATA (5 sessions, p = 0.0255) and TR (3 sessions, p = 0.0227) are not at the resolution floor of 1/101 (cell 78).
- **Cell 106, Summary:** "It holds the released dataset completely". The next bullets say the receptive-field mapping phase is absent, and cell 0 says the saturation intervals are not in the dandiset.

Everything else checks against the outputs, including:

- every decoding count, effect, Spearman correlation and nested-null figure (cells 70 to 81);
- the "6 of 9" comparisons of the null's 95th percentiles;
- the single-cell rates, the "about 3.5 times" ratio and the 2.1% to 3.8% visual range (cells 85 and 88);
- the latencies, the comparisons with `stim.pkl` and the "16 region-sessions" (cells 91 and 93);
- the traj-stim-regions counts and agreement figures (cell 99);
- the oscillation numbers, including 4 sessions at 4.00 Hz and one at 4.25 Hz (cell 102);
- the behaviour and dataset cells and the README outcome table.

**My round-1 reasons in the attempt record:** they are stated faithfully and in my own words. Problems from section B are merged into the per-claim reasons. B9 (the two truncated sessions) is not carried over; it did not bear on a conclusion.

**3. Round-1 points**

Resolved:

- **B1, L1 penalty:** scikit-learn 1.9.1 is printed. At C = 0.01 the L1 fit has 0 of 13 coefficients nonzero, against 12 with L2 (cell 70).
- **B2, nested null for VISp stimulus:** VISp stays significant, Fisher p = 1.8e-05 (cell 81).
- **B3, single-cell null rate:** a null with the labels shuffled over the tested trials was added. Its rate is 7.7e-4, against a product of the two single rates of 4.7e-5 (cell 85).
- **B6, 454 sessions:** the values do not change (cells 45 and 48).
- **B7, block-switch fit:** a bootstrap over mice was added (cell 60).
- **B8, canonical-window baseline:** fixed.
- **B9, truncated sessions:** kept at 457 and 460 trials, both above the 400-trial floor (cell 8).
- **B10, dropped sessions:** with the 64 sessions included, the latencies are unchanged.
- **B11, traj-stim-regions:** now tested.
- **Window end for IRN and GRN:** the distance curves and the 0 to 200 ms latencies are now shown.
- **B4, B12, B13:** recorded or not needing a change.

One correction to my own round 1: I said six sessions peak at the 4 Hz band edge. The table shows 4 at 4.00 Hz and 1 at 4.25 Hz.

Remaining points that bear on a conclusion:

- **B5, fback-oscillation-licking test (ii):** only partly resolved, as described in section 2. A test that subtracts each condition's mean evoked response, or picks the frequency band without using the correct trials, is still missing. The partial outcome rests on (ii) and (iii).
- **Stimulus against choice margin (dec-stim-restricted, dec-choice-widespread):** the margin is one region, 4 against 5. The nested null was run only for VISp stimulus. CL's choice result sits at the 2-session Fisher floor of 0.0010, and losing one choice region would fail both criteria.
- **traj-latency-late:** the outcome depends on the criterion's 0 to 150 ms window. In the paper's 0 to 100 ms window IRN has no latency and GRN is at 100.0 ms, and the paper's table gives 89.4 ms for both.
- **behav-zero-contrast:** the disagreement stands.
