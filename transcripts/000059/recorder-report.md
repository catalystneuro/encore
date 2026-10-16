I added the README row for 000059 with `tools/readme_row.py --write`. It gives 12 reproduced, 15 partially, 10 not reproduced and 1 blocked. I also added the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed. `git status` also lists untracked dotfiles and a `scripts` directory. I didn't create them, and the author's report says the sandbox mounts them over masked paths, so the commit should leave them out.

### 000059, Petersen et al. 2020

Twelve claims reproduced, fifteen partially, ten not reproduced and one
blocked, all on the dandiset. Round 1 disagreed on one outcome,
`fig5-speed-control-cooling`, whose criterion needs both speeds within
tolerance under one reading and states no partial case; the author changed it
from partially reproduced to not reproduced, round 2 agreed with all 38
outcomes and nothing was proposed, so there was no third round. The paper
reports that cooling the medial septum (MS) of rats slows hippocampal theta
and raises choice errors, while the theta phase lags between place cells are
kept. The cooling time course, theta frequency and power against temperature,
choice errors and speed, place cell and interneuron rates and oscillation
frequencies, waveforms, field size and information, phase precession and the
pair correlogram, compression and lag claims were tested, on session lists
and parameters taken from the paper's MATLAB code, read and not run.
`suppl1-hippocampal-temperature` is blocked as `data_missing`, because the
control experiment that measured temperature in the MS and both hippocampi is
not in the dandiset. The supplement could not be obtained, so supplementary
figures were tested only where the main text states their result. Some
outcomes rest on weak ground: `fig3c-field-size-correlated` has R = 0.8197
against a bound of 0.819; the error peak of `fig6c-worst-trials-4-to-8` at
trial 7 is narrow, and within single rats the mean peaks at trials 14 to 26;
and in `fig5d-ccg-period` the criterion's estimator often takes the second
neighbouring peak, so its 109.2 ms is biased upward, while the nearest-peak
variant gives 91.0 ms but is biased downward.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The temperature series of the nine MS10 sessions and of the
two control sessions of 2018-07-19 is not a recording: the paper's code lists
no temperature channel for them, ten run from 17.0 to 37.0 C (exactly in
nine; MS10-170313 reaches 16.98 C) and sit at exactly 37.0 C for 16% to 35%
of samples, MS10-170307 is a constant 37.0 C, and nothing in the files says
the series is modelled. The two 2018-07-19 sessions, which the code lists as
controls without cooling, have trials labelled with the cooling states and a
temperature dip, and their theta frequency during 'Cooling on' differs from
pre by -0.20 and +0.44 Hz, against a median of -0.82 Hz in the cooled
sessions. Six of the paper's 53 behavioural sessions are not in the dandiset,
four of them were in version 0.210812.1514 as files without behaviour, and
MS21-180627 has trials without the cooling state and MS21-180712 has no
trials. Other findings: the files hold no cell types, no place field
definitions and no electrode locations (every location is 'unknown'); the
trial state 'Cooling off' (a median 14 trials per session) is not described
in the files or the paper; in seven sessions every unit has quality
'unsorted', so MS10 has no usable units; in MS21-180621 and MS22-180621 the
units carry no spatial information (0.23 and 0.12 bits/spike), so the clock
of spikes and position could not be established there; the dandiset holds
three sessions that are not in the paper's behavioural analysis without
saying so; the first published version (0.210812.1514) has no trials table;
the Methods give position tracking at 120 Hz, while the MS10 sessions are
sampled at 40 Hz (six), 30 Hz (one) and 120 Hz (two); the Figure 5H legend
gives P = 8.0e-5 by a sign rank test with N = 10 sessions, which an exact
test over 10 sessions cannot give; and the Discussion's 12% decrease of theta
frequency does not match the Results' 8.4 and 7.7 Hz, about 8%.

The `fig5d-ccg-period` criterion was revised after a pilot session and before
any analysis across sessions, as the summed correlogram's spectrum followed
its envelope, and the two 2018-06-21 sessions were left out of the unit
claims at the data check. The author's points on the protocol: a criterion
revised after a pilot; no rule on using sessions the paper's code leaves out,
or modelled data; no rule on excluding sessions that fail the clock check
after the claims are written; no input kind for outside code that only
selects sessions and parameters; tolerances from a stated spread across
fields, which are very loose on a mean; criteria with no partial rule;
absence claims with no named test, where rank-sum tests over about 10,000
theta cycles are nearly always significant; per-rat tests that cannot reach
0.05 with 5 sessions; a continuous value on the tolerance edge; full text
available without its supplement; `measured` when no reading matches; and
bold labels in the example entry and notebook outline that conflict with the
instructions.
