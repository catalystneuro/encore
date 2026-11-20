I've finished the round-1 revision. Two outcomes changed, the final run passed (`tools/entry.py all`, 49.7 min) and `check` reports 0 errors. Nothing is committed. The record now has 17 reproduced, 10 partially reproduced, 7 not reproduced and 10 blocked.

**What changed in the outcomes**
- **fig2c-theta-cofiring: reproduced → partially reproduced (assumed).** I redid the theta channel choice (verifier point 1). The sharp wave is now measured against a pre-ripple baseline and in µV; the conversion factor was missing before. 76 of 104 sessions now follow the Methods' rule, against 42 before. On these channels both medians fall just below tolerance (0.0169 and 0.0071). On the layer-centre channel they fall within it.
- **ed3-depth-control: blocked → not reproduced (assumed).** It is now tested. The depth matching holds, but the burst, spatial-information and coverage fractions (0.976, 0.980, 0.992) are above the paper's (0.71 to 0.74) by more than the tolerance. The criterion's partial case needs the burst fraction within tolerance. In plain terms, the birthdate differences survive depth matching more often than the paper found.
- **Not changed:** fig1f is still not reproduced. No channel reading gives a significant slope.

**What I added or corrected**
- **Open fields (point 2):** they are now in the novel-environment analyses, binned on the assumption that one lab unit is 1 cm, with 2 and 0.5 cm per unit as variants. fig6c-novel stays not reproduced (p = 0.78), but the result rests on that scale: at 2 or 0.5 cm per unit it would be partially reproduced. The notebook now explains why the e16_3m2_211211 linear track is left out.
- **Connection detector (point 3):** each assumed detail is now varied in turn. Every variant still finds 38,402 to 50,756 connections, against the paper's 31,932, and the transmission peak stays in the same bin.
- **Front/Back electrodes:** I first read these as two separate probes. Counting both faces as one shank is the only reading that gives the paper's pair counts exactly (2,561; 1,205; 1,743/15,996; 347/3,588), so fig5d keeps its earlier numbers. This is a new finding about the data.
- **Partly testable blocked claims (point 4):** ed5's rate-matched half, ed7's part (e) and all of ed10's own parts are now computed and in the notes. They stay blocked: ed5 needs the L-ratio, which the files lack; ed7 and ed10 depend on blocked claims.
- **Smaller points:** the trials-table counts per session confirm maze-task. The ACG binning is fixed. fig6f's tercile edges now count each pair once, with a one-value-per-pair variant. I showed that Tukey over the six groups is the same test as the post hoc on the two-way model. All the outputs the verifier asked for are printed.
- **Questions and findings:** `questions/huszar-2022.yaml` asks a reader about the sessions-durations criterion's missing case and the Fig. 1f legend's n. I added a paper-inconsistency finding for the latter.
- The record's `verifications` holds round 1 for all 44 claims, with the verifier's reasons and my responses.

**What I did not do**
- **sessions-durations:** I kept not reproduced, as the criterion reads literally, and recorded the verifier's disagreement (it would give partially reproduced).
- **fig4d and the assembly claims (fig3c, fig3e, ed6):** not run. They are a heavy computation not attempted in this revision.
- **entry.yaml:** it still says the notebook takes 35 minutes; it now takes about 50. Editing it would have forced another 50-minute run, and no tool reads that field. The README and notebook header give the correct time.
