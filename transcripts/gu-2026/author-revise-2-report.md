No outcome changed in this round. I propose one change, for fig3d-distant-vs-inbound: from partially reproduced to not reproduced. It is written under `proposed` and needs a third verification round. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, 671 s), and every conclusion matches the new numbers.

**The proposed change (fig3d-distant-vs-inbound)**
- **Which decoder made which table can now be told.** All 353 pairs of arm-restricted tables that share samples have the same decodes. In 157 of the 162 whole-track pairs that can be compared, exactly one member agrees with those arm-restricted tables. I call that decoder A. The paper's code takes a figure's COM and control decodes from one decoder, so decoder A is the one to use here.
- **Under decoder A the claim misses the partial bar.**
  - In the first random draw of arm ranges, COM exceeds inbound at p < 0.05 in only 3 rats (rat E has p = 0.053).
  - Over 20 further draws, the partial bar (four rats at p < 0.05) is met in 13.
  - Adding the whole-track tables that my file-classification rule had left out, it is met in none of the 20.
  - Measuring within the arm on both sides, as the verifier suggested, it is met in 3 of 20.
- This rests on an assumption, stated as a deviation: decoder A is likely the paper's "run_time" decoder, but the files do not show it.

**The verifier's other remaining points, each answered with new output**
- **"Other" tables (fig3c):** 35 to 44% of their rows per rat fall within 20 ms of my COM times. Adding them gives rat J 47 or 52 events instead of 26, and J still fails. fig3c stays partially reproduced.
- **Single random draw (fig3b-distance):** over 20 further draws, no draw meets both the tolerance and p < 1e-20. Partially reproduced is stable.
- **Single random draw (fig3b-extended):** with only the tables classed as COM tables, all five rats pass in 11 of 20 draws. With the paper's remaining pre-stopping tables added, all five pass in only 3, so I kept partially reproduced and proposed no change.
- **Rat K (figs7b):** I fitted reading (iii) with each rat left out. Without the reference subtraction it holds in every fit. With the subtraction it fails when rat K is left out, and the notes now say so. The outcome stands on the unsubtracted reading.
- **The COM-time fix from round 1:** a new cell runs the old rule beside the new one. The COM trial and event counts are identical in every rat; 11 COM times move, by a median of 1.0 s.

**Corrections and record**
- I corrected all ten sentences the verifier quoted:
  - the control p-values (1.0 in all five rats);
  - rat K's p-value;
  - the conjecture about where the rat is (removed);
  - the comparison with the paper's coefficients;
  - rat L's trials per day;
  - the read rate (now 62 to 72 MB/s, about 2 days of streaming);
  - the 12.5 TB of raw files;
  - the README sentences on Figure 3, Figure 1H and run time.
- The two dataset findings about the triggered tables are updated to match.
- Round 2 is recorded under `verifications`: the verifier agreed with all 29 outcomes, and its reasons are quoted or closely paraphrased, with my responses kept separate.

**Not done**
- No questions file entry: the verifier found no new place where the claims file misreads the paper.
- I did not commit or push, as instructed.
- I also cloned the paper's code at the cited commit, to check how it picks a decoder for a figure and which tables Figure 3D reads.
