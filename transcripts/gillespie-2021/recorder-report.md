I wrote `docs/pilot-notes/000115-gillespie-2021-01.md` and changed no other file. It has no em dashes, bold or bullets, and does not use the word "rather". That meant I couldn't quote the paper's title, which contains that word, so the note describes the paper instead. The `catalystneuro` field for this dataset is empty, so the second paragraph doesn't open with the conversion sentence. Some untracked dotfiles, `.idea` and `scripts` were already in the repository root; I left them alone. Nothing is committed.

# 000115, Gillespie et al. 2021

Two claims reproduced and 31 blocked, all on the dandiset, with none partially
or not reproduced. It pins version 0.210914.1732, the only published version,
though the README of the paper's code links the draft. The paper, in Neuron,
records CA1 tetrodes in four male Long-Evans rats (jaq, roquefort, despereaux
and montague) on an eight-arm win-stay lose-switch task whose goal arm changes
after 4 to 15 rewards, and reports that replay during sharp-wave ripples
(SWRs) favours the previous goal arm, stays enriched long after that arm stops
being rewarded, and does not consistently favour the upcoming choice. The
claims were written from the accepted author manuscript in PubMed Central with
its supplement, and from the paper's code at commit 1be6a6a7. Only the two
behavioural claims could be tested, on trials rebuilt from the StateScript
logs in the files: `fig1d-sessions-blocks` gives 25, 32, 24 and 33 sessions
against 24, 32, 23 and 33 and 88, 85, 109 and 166 blocks against 89, 85, 105
and 166, and `fig1ef-reward-rate` gives a trial 1 rate of 0.065 to 0.133
rising to 0.584 to 0.710 by trial 15, with jaq (0.068) and roquefort (0.094)
starting below chance, which the criterion allows. The other 31 claims, on
ripples, decoding, replay content, the GLMs and the controls, are blocked as
`too_large`, as they need ripples or clusterless decoding recomputed from the
raw broadband. The author put two questions to a reader; the answers fixed
reading (a) and (b) of which jaq sessions are "sessions 1 and 3", so that
under (b) each of the other 26 jaq sessions was tried as the poorly decoded
one (88 to 93 jaq blocks, all within tolerance), and the code's rule that the
first valid trial after a goal change closes the old block, which moved
montague from 167 blocks to 166; no outcome changed. Round 1 agreed with all
33 outcomes and led to a per-session table, trial counts against the legends
and the behavioural half of `fig6b-visits-decay`, which stays blocked with the
replay half. Round 2 also agreed with all 33, so there was no third round; it
found statements the outputs did not support, among them a streaming rate of
8.4 MB/s against 9.5 printed, a 226 s gap and 55 rewritten files that no
output showed, and these were corrected. Some outcomes rest on weak ground:
the behavioural half of `fig6b-visits-decay` holds in jaq, despereaux and
montague but fails in roquefort at a single trial +29 with the tie-corrected
rank-sum test (p = 1.6e-4), not without the tie correction (p = 0.074), and
the question on which form applies is open; and error trials are 11 to 24%
more than Figure 5B's, though no tested claim uses them. The notebook ran in
about 7.7 minutes at first, 282 s after the answers and 328 s after round 1.

The dandiset holds the raw 30 kHz broadband of 128 channels, port events,
position and task logs, about 9.1 TB over 57 files stored one channel per
chunk, but none of the derived data the paper's findings rest on: no spike
times or waveform features, LFP, ripple or multiunit event times, linearised
position or decoder output. Streaming measured about 5 MB/s in the first run
and 8.8 MB/s in the run recorded, at which one 90-minute run epoch takes 79
minutes and the whole dandiset 288 hours. The electrode table gives the
location of all 128 channels as None in every file, so the CA1 cell-layer
tetrodes used for ripple detection and decoding and the corpus callosum
reference tetrode cannot be identified. The files do not mark which run
sessions the paper analysed: they hold 27, 32, 24 and 33 run epochs, where the
paper used 26 (24 after excluding sessions 1 and 3 of subject 1), 32, 23 and
33, the excluded sessions are named only by number, and which jaq and
despereaux epoch the paper did not count cannot be told; possible ones are jaq
day 7 epoch 2 (6 rewards in 74 valid trials) and the epochs shorter than the
Methods' 45 minutes (jaq day 6 epoch 4 and day 9 epoch 6, despereaux day 4
epoch 4), and leaving out any one more keeps all counts within tolerance. The
paper's code repository holds a saved filter output with per-animal epoch
lists that may identify them, which was not used. The task logs, embedded as
text, are the only record of the goal arm, trial structure and timeouts, as
there is no trials table, and five run epochs carry the log without the header
that states the task parameters, so forage assist can be ruled out for them
only from the log lines. Logged rewards match the DIO pump onsets in 115 of
116 epochs. 55 of the draft version's 57 files differ in content from the
published version's, and in the file compared (montague day 4) the draft's
position timestamps are shifted by about -1.59e9 s and no longer share the DIO
clock, while in the published version they do. Other findings: position is
sampled at 32.9 to 33.0 Hz, where the Methods state 30 Hz, and 110 of 116 run
epochs end with 1 to 4 NaN position timestamps, all the last samples of the
series, while two epochs have non-increasing timestamps (up to 200); in
montague day 16 epoch 2 the log's clock steps by about 3.4 s twice against the
DIO pump times; and in jaq day 6 epoch 4 the DIO holds one more reward pump
(arm 8) 226 s after the last logged reward and 40 s after the last logged
trial, so that log appears to end before the epoch, though the DIO confirms
arm 6 was never entered in that session.

The author's points on the protocol: a variant the criterion rules out,
excluding no session, was shown labelled as a variant; the paper's saved epoch
lists are an outside input the claims file does not list, so they decide
nothing; step 1.6 asks for questions even when every reading gives the same
outcome; the paper's code links a draft that differs from the published
version in content the analysis would use; no category covers a dataset too
large to stream, so `too_large` was used with a measured throughput; the
criterion gives no test for "rises" in `fig1ef-reward-rate`; and a claim
depending on a blocked claim is blocked even when part of it, here the visit
curves of `fig6b-visits-decay`, can be computed.
