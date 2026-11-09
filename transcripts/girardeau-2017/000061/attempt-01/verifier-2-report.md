**Round 2 verification: Girardeau et al. 2017 (doi:10.1038/nn.4637) on DANDI 000061, version 0.250624.0426**

Counts come from the claims file and the attempt record: 6 claims, of which 4 are reproduced, 1 is not reproduced and 1 is blocked. I worked only from the printed outputs of the re-executed notebook and from the helper code. I did not download the data or the paper again, because the claims and criteria have not changed since round 1. `paper/` is no longer in the working directory. I recomputed the three session-level Wilcoxon tests in cell 35 from the printed values (exact test) and got the same results: 13/15 with p = 0.00031, 10/15 with p = 0.030, and 10/15 with p = 0.030.

**1. Stated outcomes**

| Claim | Record | Agree? |
|---|---|---|
| hpc-bla-reactivation-post-sleep | reproduced | Yes. Cell 28: 36 patterns, median 0.0119, 28/36 positive, p = 3.6e-05. The median is above zero in all three rats. Session level: 14/15, p = 0.00012. |
| reactivation-peaks-at-ripples | reproduced | Yes. Both readings hold for patterns (cells 33, 34) and for sessions (cell 35). |
| bla-ripple-up-subgroup | reproduced | Yes. Cell 38: 103/822 units against a chance level of 0.007, p = 9.8e-90. Each rat passes against both the pooled chance level and its own. |
| reactivation-involves-ripple-up-cells | reproduced | Yes, under the pooled per-pattern criterion (cell 42: 24/31, p = 0.0013). The support is weaker than this suggests: rate-matched at session level gives p = 0.22 (cell 43). |
| aversive-direction-stronger | not_reproduced | Yes. Cell 46/48: p = 0.107, and no variant changes it. |
| rats-learn-puff-location | blocked (too_large) | Yes. Cell 11: 1,920,573 run frames, about 212 h to stream. |

**2. Text not supported by the printed outputs**

- Attempt record, rats-learn-puff-location notes and response: "streaming 20 frames took 8.1 s, about 217 hours". Cell 11 prints "8.0 s" and "about 212 hours". These numbers look left over from an earlier run.
- Cell 52: "in the pre-run and the post-run, when no puffs are given". No output shows how many puffs fall in each epoch. Cell 19 counts puffs only by lap direction within the run.
- Attempt record, aversive-direction-stronger deviation: "927 of 957 puffs fall in it" (also cell 20: "Nearly all puffs (927 of 957)"). Cell 19 counts only the 31 files that have units and at least 5 puffs. Cell 3 lists 1197 puffs in total. For the 13 analysed sessions in cell 19 the count is 290 of 299 (my sum), and the two sessions with 2 and 3 puffs are not covered. The scope should be stated.
- Cell 40: "It is a subgroup: as many units (104, 12.7%) fire less in ripples." The numbers are correct. What makes the 12.5% a subgroup is that the fraction is below 1. The count of negatively modulated units does not bear on that.
- README: "It takes about eleven minutes, six of them streaming the files." Only the 361 s load time is printed (cell 1). The total run time is not shown.

Every other sentence I checked matches the printed numbers. That covers the "**Result:" cells 31, 36, 40, 44 and 49, the Summary (cell 53), the rest of the README, and the notes and findings in the record.

The record states my round-1 reasons accurately and in my own words for all six claims. That includes the "other or too_large" reason for the block and the points I listed under C.

**3. Round-1 points**

All resolved:
- B1 (laps include waiting time): lap table and travel-part variant added, cell 48, p = 0.19.
- B2 (no puff minimum): variant added, p = 0.146, and recorded as a deviation.
- B3 (equal-bins variant took the first bins): now a random subset, cell 47, p = 0.33.
- B4 (firing rate): rate data, correlation and a rate-matched test added, cell 43.
- B5 (pre-sleep peak): conclusion reworded to rest on the post minus pre contrasts, cell 36.
- B6 (patterns treated as independent): session-level tests added, cells 35 and 43.
- B7 (pooled chance level per rat): each rat's own chance level added, cell 38.
- B8 (reason for the block): changed to too_large and supported by cell 11.
- C (missing outputs): the lap table by epoch (cell 51), the epoch boundaries (cell 25), and the fraction of shifted ripple peaks outside Non-REM (cell 39) were all added.

What still bears on a conclusion (none of it changes an outcome):
- reactivation-involves-ripple-up-cells rests on a per-pattern test of patterns that are not independent. Up units fire faster (1.66 against 0.41 Hz), and once rate is controlled the session-level effect is not significant (9/13, p = 0.22). The conclusion says this. The claim is reproduced only under the criterion as written.
- hpc-bla-reactivation-post-sleep: Rat10 passes the "median above zero" test by a small margin (5/8, p = 0.74). One of its three sessions has a negative median (cell 28).
- Cell 51, which only describes the blocked claim, assigns laps to epochs by their midpoint. Its "run" for Rat08-20130708 therefore includes the second run, and its lap counts differ from those of `run_laps` in cell 48 (for example 4/3 against 2/2 for that session). It is descriptive only.
