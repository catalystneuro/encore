# Shukla, Rivera, Bladon & Jadhav (2026) from dandiset 001845

Tests the findings of [Shukla et al. (2026)](https://doi.org/10.1523/jneurosci.0143-26.2026) that can be
tested on [DANDI:001845](https://dandiarchive.org/dandiset/001845/0.260526.1807). The dandiset holds the
cooperative W-maze sessions of 5 WT and 5 Fmr1 rat pairs under 100% and 50% reward: poke events of both
rats, the matched and rewarded pokes, and DeepLabCut positions. The mixed pairs, the visual-cue task and
the virtual-agent task are not in it, and no session is labelled as sensory deprived.

| Claim | Outcome |
|---|---|
| WT pairs have higher match rates (Fig. 1E) | Blocked: methods underspecified |
| Fmr1 rats make fewer transitions (Fig. 1F) | Blocked: methods underspecified |
| Match rate rises with transition rate, steeper in WT (Fig. 1G) | Partially reproduced |
| Pairs coordinate above chance late in training (Fig. 1H) | Partially reproduced |
| Performance lower in Fmr1 pairs (Fig. 1I) | Blocked: methods underspecified |
| Partner location predicts choice, better in WT (Fig. 1J) | Not reproduced |
| Choice triplets by contingency (Fig. 3C) | Not reproduced |
| Entropy lower in WT rats (Fig. 3D) | Partially reproduced |
| Exploration efficiency higher in WT rats (Fig. 3E) | Not reproduced |
| Choice similarity within pairs higher in WT at 50% (Fig. S2) | Not reproduced |
| Arrival lag shorter in WT pairs (Fig. 4B) | Not reproduced |
| Departure lag shorter in WT pairs (Fig. 4C) | Not reproduced |
| Dwell time, Fmr1 longer but not significant (Fig. 4D) | Reproduced |
| Cross-correlation of arrivals higher in WT pairs (Fig. 4E to 4G) | Not reproduced |
| Peak-lag distributions differ at 50% (Fig. 4H) | Not reproduced |
| Peak correlation higher in WT pairs (Fig. 4I) | Blocked: methods underspecified |
| Rats lead about half the matches (Fig. 5D) | Reproduced |
| Leading difference by genotype at 50% (Fig. 5E) | Not reproduced |
| Leadership depends on history (Fig. S3) | Blocked: methods underspecified |
| Reinforcement learning model (Fig. 6) | Blocked: methods underspecified |
| More asynchronous matches in Fmr1 pairs at 50% (Fig. 7B) | Not reproduced |
| Trial duration correlates negatively with performance (Fig. 7C) | Partially reproduced |
| Follower-only gaze highest late in the trial (Fig. 7E) | Reproduced |
| Gaze GLMM contrasts at 100% and 50% (Fig. 7G, 7H) | Not reproduced |
| Partner history shapes cooperation (Fig. 8B, 8E) | Blocked: the test is decided by how follower trials are built |
| Δt longer in Fmr1 rats (Fig. 8D) | Blocked: depends on Fig. 8B |
| Sensory-deprived sessions (Fig. 2B) | Blocked: metadata insufficient |
| Mixed pairs, visual-cue and virtual-agent tasks (six claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's analysis code is not published, so the event definitions (visits, matches under a time
shift, synchronous matches, gaze trials, follower trials) are this attempt's readings of the Methods.
Several genotype effects are significant only when sessions are treated as replicates, as the paper's
printed df suggest, and not with pairs or rats as subjects; the claims file blocks those claims. About
5% of pokes are near-simultaneous pokes at two wells, removed here as sensor crosstalk. In 6 of 10 pairs
the head positions agree poorly with the pokes, which bears on the position-based measures. Follower
trials built from the sequence of arrivals show a partner-history effect even when one rat is shifted
in time, so the Figure 8 claims are blocked. The arrival and departure lags of Figure 4B and 4C fail
under both readings with every session; they were blocked until the third verification round, when the
verifier agreed that the removal of four sessions with head-position lags over 100 s, a threshold chosen
after seeing one of them, should not decide the outcome. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/shukla-2026-01.yaml`](../../attempts/shukla-2026-01.yaml).

- `reproduce_shukla_2026.ipynb`: the analysis. It takes 10 to 13 minutes (the run time is printed at the end), most of it streaming
  the 1,120 analysed NWB files and reading the 646 others.
- `coop.py`: streaming and reduction of the files, choice sequences, the match rule rebuilt from pokes,
  well occupancy and cross-correlation, the bearing angle, the state-space model and the ANOVA readings.
  Other notebooks on this dandiset can import it.
