I worked through every point in the verifier's report. No outcome changed: the verifier agreed with all 22, and none of the new numbers moves one. The entry passed `python tools/entry.py all` (0 errors, 21 minutes), and the claim results match the run before. Round 1 is recorded under `verifications` in the attempt record, one entry per claim with the verifier's reason and my response. Nothing is committed.

**Errors I corrected**
- **fig1c-e:** the conclusion said at most 4 of the 6 named electrodes are on vSMC. The verifier was right that it is 5 of 6, in EC2 counted from 0 (e129 is labelled middle temporal). The header table also no longer lists this claim as simply "tested".
- **Artifact trials:** the earlier count of 177 counted some trials twice. 162 trials overlap intervals marked as ECoG artifacts. The finding and the summary are fixed.
- **suppfig11:** the three tests were combined, so one label reading's outcome depended on the other's test. Each label reading is now judged on its own consonant test plus the vowel test. The counts stay 38 partial and 10 not reproduced. The consonant median range is now given per label reading.
- **Bootstrap (`bouchard.py`):** a token could be paired with its own copies, adding distance-zero pairs. I fixed this and checked it against a direct computation on synthetic data. Only the s.e. for one onset reading of fig5c moves: the consonant onsets now run to -180 ms, and the recorded vowel onset goes from 100 to 105 ms.
- **File contents:** the hard-coded "only ElectricalSeries" line is replaced by a listing read from the files. One file (EC2 block 1) holds a power spectrum in a processing module; no file has audio.

**What I added that the verifier asked for**
- **Subject identity:** the subject fields hold only species and id. EC2 and GP31 have an electrode group named `L256Grid electrodes`, which fits a left hemisphere; GP33's is `auto_group`. Nothing links GP31 and GP33 to the paper's EC31 and EC33. GP31 is the subject with 18 consonants that have all three vowels, which fits the paper's 54-syllable subject.
- **active-electrodes:** every electrode that counts with all syllables but not with the 15+ set comes from GP31's /thi/, which has 2 renditions. In a variant that leaves out the artifact trials, no reading reaches 27 to 33. The one reading inside the range (`rest` baseline, 15+ syllables) drops from 31 to 2 GP31 electrodes, so it depends on trials the files mark as artifacts. This is recorded in the notes, but the outcome stays blocked because the variant is not one of the claims file's readings.
- **suppfig6:** run on weights shuffled across electrodes, the same test still holds in 94 of 96 readings. That confirms the verifier's point that it barely discriminates. The outcome stays reproduced because the criterion decides it, and the notes say what the test cannot show.
- **Other outputs:**
  - Outcome counts per reading factor for all seven methods_underspecified claims the verifier listed.
  - All-vSMC counts for fig1f-h.
  - fig3d with artifact trials left out: same outcome.
  - Tongue electrode counts for fig3d (2 to 7 under the "all six" readings).
  - suppfig9 electrodes dropped for lack of a window (none in 168 readings, up to 83 in the others).
  - The Supplementary Figure 12 and 1d matrices printed and drawn for checking against the supplement.

**What I did not do, and why**
- **suppfig13:** the verifier noted that labelling readings "partially reproduced" when only the pair count differs is my own category. I kept the label and the blocked outcome, which the verifier also gave. The notebook now prints that no reading meets the criterion as written (0 of 48), and the notes say that read strictly, every reading is not reproduced.
- **Position substitutes for suppfig7 and suppfig5:** not run. The claims file names no such substitute, and its answer of 2026-10-22 rules out deriving positions from unlabelled coordinates or labels.
- **fig5c pre-epoch level:** I asked no question about it. It decides only the onsets, and the outcome rests on the peaks, which fail in every reading.
