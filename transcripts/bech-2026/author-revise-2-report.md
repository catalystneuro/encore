The round-2 revision is finished. No outcome changed: I proposed two changes for a third round. The final run (`python tools/entry.py all entries/001847-bech-2026`) passed in 45 min, and `check` reports 0 errors. Every number in the notebook came out the same as before, except the timings.

**Proposed changes (written under `proposed`; the verified outcome stays)**
- **fig3h:** proposed blocked (`methods_underspecified`). I agree with the verifier. The criterion requires every baseline to give the same outcome. The 50 ms baseline gives reproduced, but the 250 ms baseline gives a tie between RSC and wM1 in the pixel version. The paper gives both baselines. The notebook's conclusion and summary now say this. The question for the paper's authors now says that the paper is inconsistent.
- **fig4b (3 claims):** proposed blocked, changing the reason from `too_large` to `other` (not run in this attempt). The final run estimates 33 min of reading, about 55% of the limit for a separate notebook. So the data are not shown to be too large. The analysis itself is not run here, because the protocol leaves an analysis not yet run to a new attempt.

**Corrections and added outputs**
- **fig4b:** the notes now use the final run's printed numbers: reads of 33 min at 184 MB/s, and 45 min of notebook before the fig4b cell, 78 min in total. The notebook now times itself, so the unsupported "42 min" figure is replaced by a printed one.
- **fig3h:** the read time is now the final run's 2.0 min. It varies between runs (1.8, 2.0 and the verifier's 3.0 min).
- **Figure 2 (7 claims) and their finding:** the false statement "no site reaches d' 0.5" is replaced. Under null (i), no named site reaches 0.8; the largest values are tjS1 0.57 and 0.56 and wS1 0.53 and 0.53.
- **fig3f:** the largest early value is now 0.97 (wS1, 250 ms baseline), not 0.94.
- **fig4e:** the conclusion now compares RSC and tjS1 only with the sites the criterion names. It notes that A1 and RSC (-0.5, 0.5) are lower still.
- **DLC length finding:** this now has a printed source. The DLC cell lists the sessions whose timestamps and data differ in length: 76 of 97, mostly by a few frames. In PB192_20241121_122848 the jaw series has 311,339 data points for 1,116,888 timestamps. The finding gives these numbers.
- **fig4d:** I added a variant that places each trajectory along the line from control-lick to no-lick. It does not decide the outcome. The five inhibited sites lie 3.8 to 6.9 times the lick-to-no-lick distance from the lick trajectory, mostly on the side away from no-lick. So they move away from lick but not toward no-lick under either measure. The outcome stays not reproduced.
- **New reader questions** in `questions/001847.yaml`:
  - fig3c: the claims file says the trial set is "open in the text", but the Methods name it.
  - fig4d: whether "toward no-lick" should be read as "away from control-lick".
- **Round 2 is recorded** under `verifications`: 40 claims, with the verifier agreeing on 36 and disagreeing on fig3h and the three fig4b claims. The README, the summary and `runtime_minutes` (now 45) are updated.

**Not done**
- I did not change any claim and did not run the fig4b seed-to-pixel analysis.
- fig1l was already with a reader, so nothing changed there.

Nothing was committed.
