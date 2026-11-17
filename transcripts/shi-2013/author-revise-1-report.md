I revised the attempt in reply to the round-1 verification. No outcome changed. The entry re-ran cleanly with `python tools/entry.py all entries/shi-2013` (passes, 325 s), and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes**
- **No outcome changed.** Every number in the conclusions matches the re-run.
- **Disagreements kept and recorded:**
  - `fig4-indx1-means` stays partially reproduced: the Position Only part holds in full and the Position/Vision part fails. The verifier says not reproduced.
  - `rate-variance-nv-higher` stays partially reproduced: NV is higher in the same direction and about the same 2× ratio, but both means are about 20% low. The verifier says not reproduced.
- **Four outcomes are now marked as resting on an assumption:** `hold-vision-main-effect`, `hold-subepochs`, `fig4-indx1-negative` and `decoding-subepochs`. The assumption is taking the first sorted unit from each session, and using all 483 units would change each of these outcomes. The paper supports one neuron per session (Table 1 legend, and "N = 343 sessions" for 343 neurons), but not which unit.

**Outputs the verifier asked for, now in the notebook**
- **Population (B1):**
  - All 359 sessions were recorded from October 2008 to November 2009, on 92 days, before the paper was submitted (14 March 2012).
  - Their target layout is monkey X's in every month.
  - Consecutive sessions on the same day have unrelated tuning (median correlation 0.04, against −0.01 across days), so they are different neurons.
  - Why there are about 140 more sessions than the paper's 219 is still unexplained.
- **Hold timing (B3):** on all 30,789 completed trials, the time from code 10 to code 12 is at least the trial's own field 11 plus 28 ms. The verifier's 0.832 s intervals all come from trials with field 11 = 800. So the 800 ms window sits inside the hold. In 11.6% of trials it starts less than 250 ms after code 10; starting it later leaves `hold-subepochs` and `decoding-subepochs` unchanged.
- **Hand position (B2):**
  - V and NV trials are interleaved: the median session has 39 runs of one condition, against 41 expected for a random order.
  - With the V/NV labels shuffled, the MANOVA rejects in 5.7% of pairs, so the test is calibrated and the 16% is real.
  - Within a session, the five trials at a target spread by a median SD of 0.29, 0.29 and 0.19 cm in x, y and z.
- **Analog files:** I read their layout from the files themselves (it is undocumented) and summarised the channels of three sessions. No channel differs between targets during the hold or follows the hand (|r| ≤ 0.25). One channel spans a range a 12-bit converter cannot give, so my reading of the layout is at least partly wrong; the notebook says so. The eye-position block stays. I also corrected its note: the small spread of record fields 22–23 does not rule out an averaged eye position.
- **Other checks:**
  - The per-session clock check holds in 153 of 359 sessions; the other 206 are named as not established.
  - The decoder's chance level on shuffled labels is 16.1% (V) and 11.2% (NV), near the 12.5% used.
  - A Fano-factor variant keeping only the 331 cells within Fig. 5's plotted range gives 1.03 against 1.21, P = 0.17: still not reproduced.
  - The non-monotonic abort rates for code 4 are now in the `aborted-trials-nv` notes.

**Other corrections**
- I added `questions/shi-2013.yaml`, asking a reader whether the Fano-factor outlier readings match Fig. 5's 0 to 80 axes. The claim itself is unchanged.
- I removed an unused branch from `ppc.decode`; results are identical.
- The `output` tags of three outcomes now point at the claim's own tag.
- New methods questions for the paper's authors: which unit per session they used, and whether the recorded hand position is a mean over the hold.
- The `verifications` block for round 1 is recorded in `attempts/shi-2013-01.yaml`.

**Not done**
- `longer-hold-no-difference` stays blocked as `data_missing`, not the verifier's `metadata_insufficient`, because the per-trial timing supports reading field 11 as the minimum hold.
- I could not settle whether the hand position in fields 19–21 is a hold mean or a single sample: no position trace was found to check it against.

Several untracked files appeared in the repo root during the run (`.bashrc`, `.profile`, `.idea`, `.vscode`, `.mcp.json`, and others) along with a `scripts` folder. I did not create them, and they should be left out of the commit. The `tools/` changes were already there when the run started.
