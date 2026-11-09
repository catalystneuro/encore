# crcns-pfc-1, Rodgers et al. 2014

Thirty-four claims reproduced (two on an assumption), none partially, none not
reproduced and none blocked; the link claim the author added, `unit-table-link`,
reproduced, is counted apart. The first verification round agreed with 34 of
the 35 outcomes as they stood and the second with all 35; nothing was proposed
after the second, so there was no third round. CRCNS does not version data
sets, so the version is recorded as unversioned with the data set's DOI
(10.6080/K0W66HPJ), and the zip is pinned by its MD5 from the bucket's
`checksums.md5`. The paper, Rodgers and DeWeese, "Neural correlates of task
switching in prefrontal cortex and primary auditory cortex in a novel stimulus
selection task for rodents" in Neuron (82:1157-1170), records 121 prelimbic
mPFC and 99 A1 single units from six male Long-Evans rats that switch between
localization and pitch discrimination blocks of 80 trials, studies how hold
period activity encodes the selection rule, its time course, auditory evoked
responses and posture, and adds electrical disruption of mPFC in three further
rats, a catch-trial task and a network model. The claims were written from the
PyMuPDF text of the version of record and its Supplemental Information, without
opening the PDF pages, and from the paper's code (cxrodgers/Rodgers2014 at
commit 390b608), whose `metadata/unit_db.csv` gives the units, their region and
their auditory response class and window; the claims check added
`fig2d-block-switch` and `figs2c-s3c-hold-by-trial-type` and revised two others.
Every claim could be tested, the single-unit claims on the code's unit table
(`with_labels`). Reproduced are, among others, `fig3c-pfc-rule-encoding` (76 of
121 mPFC units, 36 and 40 by preference, under both readings of the
Benjamini-Hochberg adjustment), `fig4c-a1-rule-encoding` (36, 13 and 23),
`fig5c-population-onset` (2.725 s before onset in mPFC, 0.875 s in A1),
`posture-equalized-sign` (PRE 0.471 and 0.318) and `fig7-disruption-by-block`.
Two outcomes rest on an assumption: `fig5ab-single-unit-onset` (0.550 s in A1
and 0.625 s in mPFC with the code's smoother, kept only when the 7 mPFC and 2
A1 units with no significant interval containing the bin just before onset
count in the median; left out, 0.650 s in both regions) and `fig8-model`, where
"most positive task signals" is read over Figure 8B's plotted range (90% of the
symlog axis, 38 of 40 positive gains of the code's linear sweep) while counted
per log-spaced gain only 25% reach 99%. Several other outcomes rest on the
code's own choices: `audresp-prevalence` and `figs5e-latency` on the unit
table's response windows (recomputed from the spikes, 46 and 61 responsive
units and latencies of 16.38 and 16.25 ms with p = 0.41), and
`evoked-beyond-baseline-rare` on the code's BH correction (unadjusted, 12 of
43, which fails). The author's first run had 33 reproduced, one not reproduced
and one partially, with `fig4ab-a1-example-units` not reproduced because the
claims file named the units by the code's figure index, under which none of
the four rates is within tolerance, and fig8 partially reproduced. The author
asked a reader whether the units should be identified by preference as the
Figure 4 legends do; the reader changed the criterion, and in the
author-answers run fig4ab became reproduced (8.01 and 4.76 Hz for unit 712,
10.07 and 2.00 Hz for unit 612). Round 1 disagreed on fig8-model (reproduced),
and asked for the fold to be checked against the blocks, the bootstrap p values
of `evoked-beyond-baseline-rare` under more seeds, a chance level for the
decoding scores, the fig5ab medians without the nine units, power and
intervals for the small-sample claims of absence, and for the recomputed
auditory responsiveness to be reported; in reply these were added, fig8 was
changed to reproduced on an assumption, four conclusions left in section
headers were moved and the notebook header was added. Round 2 agreed with all
35 outcomes, fig5ab only under a reading it asked to be marked assumed, and
found text the outputs did not support, among them a claim that reading (b) of
fig3c fails where 81, 37 and 44 are all within tolerance, and "55 sessions, all
of which pass" where 54 were tested; in reply fig5ab was marked assumed, a
second question went to a reader in `questions/crcns-pfc-1.yaml`, written after
the answer run, so it is unanswered, and the text was corrected. The author's
run went from 13:41 to about 14:26 UTC; the notebook ran in 132 s at first, 160
s after the author-answers run, 233 s after round 1 and about 190 s after round
2, and nothing failed. The untracked entries in the repository root, device
nodes the sandbox created before the run, were left alone.

The data set does not say which of the 2977 sorted clusters in its spike files
are the 220 well-sorted units the paper analysed, or give their auditory
response class and window; these come only from `metadata/unit_db.csv` in the
paper's code repository, and the scripts that made the table are not
published. That table's auditory response classes apply rules the paper does
not state (too brief, lasts to end, lasts too long): recomputing responsiveness
as the Supplement describes gives 46 mPFC and 61 A1 responsive units in place
of the paper's 31 and 49, and, of 67 units responsive under both, 17 whose
window starts at a different time, the difference coming partly from the
table's unstated classes and partly from the threshold and trial choices of the
recomputation (6 units classed nothing become responsive, 13 classed responsive
do not). The spike files and the miscellaneous pickles are pandas 0.10 pickles
written under Python 2, which current pandas cannot open and the descriptor's
`pandas.load` no longer reads; they can be read with a custom unpickler. Two
sessions, CR21A_120503_004 and CR21A_120504_004, hold a second spike file
besides `klusters0/` that the descriptor does not mention, with the same spike
times but a column named spike_time, tetrode groups 0 to 7 in place of 1 to 8
and different unit numbers. The descriptor names the stimulus column
stimulus_name where the files call it stim_name, and numbers le_lc_go as 1
where the files give it 3 (ri_lc_no 4, lo_pc_go 1, hi_pc_no 2). Three sessions
(CR20B_120613, CR21A_120502, CR21A_120506) have no spike file, their
`klusters0/` holding a README.txt where the descriptor says the directory is
empty; the data set holds the 55 sessions the paper reports, and its four
discarded sessions are not in it. The code's figure index names unit 612 as
Figure 4A and 712 as 4B, while the legends fit the reverse, and the Figure 4B
legend gives the pair's trial counts with the blocks swapped relative to 4A;
the data have 312 localization and 253 pitch discrimination trials for both
units. A comment in `3-5-vidtrack/main5.py` says statsmodels' stand_mad does not
subtract the median, but the paper's PRE values (0.471 and 0.318) are
reproduced exactly by the MAD about the median, and the uncentered MAD gives
0.327 and 0.343. A question is put to the paper's authors: whether the 7 mPFC
and 2 A1 rule-encoding units with no significant interval containing the bin
just before onset were included in "the median rule-encoding unit" of Figures
5A and 5B, and with what onset.

The author's points on the protocol: step 1.4 has dependent claims list a link
claim in `depends_on`, which edits claims the reader wrote, so `unit-table-link`
was added and only `depends_on` fields were appended to; the prompt asks for a
pinned published version that CRCNS does not have, so `docs/archives.md` was
followed with `unversioned` and the MD5; `unit_db.csv` supplies measured values
(response windows) and not only names, so it is arguably `with_inputs`, while
the claims file's `with_labels` was kept; reader step 3 accepts a claim "under
any reading" while author step 1.6 takes the outcome all readings give, so the
claims file's criteria were applied; testing the file as written forced not
reproduced on fig4ab although the data match the paper, an outcome misleading
until a reader answers; and in place of decoding a task variable for the clock
check, the evoked response at stimulus onset against shifted times and the hold
period rule encoding were used, with the fourteen sessions that have no
auditory-responsive unit listed.
