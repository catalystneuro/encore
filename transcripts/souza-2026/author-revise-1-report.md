I've worked through all eleven points in the round-1 report. One outcome changed. I re-ran the entry with `python tools/entry.py all entries/souza-2026`: it passed in 53 minutes, every number matched the run before it, and `check` reports 0 errors. Nothing is committed.

## What changed in the outcomes

- **layer4-controls** is now not reproduced (it was partially reproduced). I took the verifier's reading: the "50 µm count" is the paper's "63 of 72 sessions", and our 80 sessions are outside 72 ± 7.
- **Kept, disagreement recorded** for four claims where the verifier would give not reproduced:
  - **data-sessions-units** (partially reproduced): the criterion has the selection recorded as an assumption, and the verifier called that assumption reasonable.
  - **latency-change-to-reward**, **m-baseline-sensitivity** and **layer4-within-waveform** (partially reproduced): their criteria have no partial clause, so I applied the protocol's general definition (the effect holds only in part or is weaker).
- **New tally:** 17 reproduced, 14 partially reproduced, 7 not reproduced. Round 1 is recorded under `verifications` for all 38 claims, with the verifier's reasons in its own words.

## What I added or corrected

- **Waveform rows (B1, B2):** the layout is as assumed. Every unit has 384 rows, and in 230 of 300 units checked the largest-amplitude row is the peak channel's (299 within 4 channels). So the layout does not explain why reading (a) fails to split narrow from broad. The cause is a long tail of durations, which a variant on waveforms upsampled to 200 points also shows. The notebook now prints a duration histogram and each seed's log-likelihood; the claim's seed gives the better fit. The class labels now default to the stored duration, which the outcomes rest on.
- **Whole-recording ISI null (B3):** running it on all 104 sessions pushed the first revision run past the 60-minute cell limit. It now runs on 12 sessions, where it changes the cohort by 4 of 1,272 units.
- **1,000 permutations (B4):** the check now covers 300 units in three sessions: 225 units pass with 100 permutations and 229 with 1,000.
- **Detection-rate denominator (B7):** it now uses the cohort claim's readings (b) and (c), giving 91.1% against 92.5%, and 83.9% against 85.8%.
- **CA1 read as layer 1 (B8):** fixed; no analysed unit lies in such a structure, so nothing changes.
- **Stricter layer rule (B9):** assigning layers only in visual-area structures gives 87.0%, 84.3%, 96.5% in VISam and 45.5% in VISrl, all within the paper's tolerance. The Methods don't state this rule, so I kept the outcome on the criterion's rule and added a `methods_unavailable` finding asking the paper's authors.
- **False-alarm clock (B10):** I removed the fallback to the other clock; it was used 0 times, so the numbers are unchanged.
- **Averaged RW- series (B11):** with a single RW- draw instead of the mean of 20, the within-RW- correlation falls below RW+ (0.300 against 0.354), and the block excess turns negative (-0.050). The outcomes stay as tested, but the notes and summary now say the excess depends on averaging the draws.
- **Other outputs the verifier asked for:** a per-session table with dates, unit counts, areas and hits, and a hit accounting. All 15,592 hit trials are used and no filter drops any.
- **Atlas source:** GIN now answers 403 to this runner. The notebook falls back to the Allen Institute's own CCF 2017 files, each checked by SHA-256 and listed under `inputs`. Layer counts are identical to the first run, which used BrainGlobe's copy.

## What I did not do

- **1,000 permutations for all 54,045 units:** about nine CPU hours, too long for the notebook.
- **The paper's 103rd session:** I could not identify it. The smallest session holds 262 units, so dropping any one session cannot give the paper's 54,039 units.
- **The stricter layer rule in the other layer claims:** I show it as a variant only in layer4-suppression and layer4-controls.
- **Questions for a reader:** none added; the verifier reported no place where the claims file misreads the paper.
- **Runtime:** the notebook now takes about 53 minutes, inside the 60-minute limit but with little margin.
