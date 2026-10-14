No outcomes changed. The verifier agreed with all 20, and they stay at 7 reproduced, 1 partially reproduced, 2 not reproduced and 10 blocked. I re-ran the entry twice with `python tools/entry.py all`; it passed, and `check` reports 0 errors.

**Output added**
- **Angular acceleration while the fish is still, by species.** The verifier said this direct test was missing. I added a per-frame speed column to `acceleration_frames` in `omr.py` and a new notebook cell that splits angular acceleration by speed band.
  - When still (below 1 mm/s), DC are about twice ZF: per-fish medians of 72.4 against 34.9 deg/s² (p = 0.00014).
  - In both species the values rise with speed, and DC are higher in every band. At 5 mm/s or more it is 207 against 85.8.
  - So DC heading is noisier at rest. Whether the higher values in moving DC are noise or turning during continuous swimming is still unknown. The fig1h conclusion, notes and Summary now say this, include the ZF rest test (ratio 1.07, p = 0.00012), and no longer say "suggests a tracking-noise floor".

**Text corrected**
- **Fast trials (cell 17):** it now lists both long DC-sub-2 trials that are not short, where it named only one. It also says the 0 to 35 s window of the code's check is why these trials pass.
- **`dist` statements:** the Summary bullet and the `dist` finding now say that the speed check from positions passes the same trials, so `dist` is not the cause.
- **fig1d-dc-no-modulation:** "two at 0.0" now reads "near 0". The 106.5 mm/s static trial is called a likely tracking artefact. The text says the outcome is a property of the paper's test on this data, not evidence that DC modulate their speed.
- **"4-hour blank block":** it now gives the protocol's 4 hours and the 0.2 to 787.3 min actually in the files.
- **Round-1 record:** the fig1h reason now includes the verifier's figure for ZF (1.4 times the frame interval), which it had noted was left out.
- **Round 2 in the attempt record:** all 20 claims are recorded with the verifier's reasons and my responses.

**Not done**
- **figs1e-dc-respond-less-monocular:** I left it as reproduced. The verifier agrees with that outcome under the code assignment the claims file fixes. Their view that the data favour the other assignment, under which the claim would be partially reproduced, is now recorded in the round-2 entry.
- **Untracked files:** dotfiles such as `.bashrc`, plus `.idea`, `.vscode`, `.mcp.json` and `scripts`, are in the working tree. I did not create them and did not touch them, so check them before the workflow commits.
- **Blocked command:** a command to read a saved copy of the protocol output was denied, because this session cannot approve prompts. I read `docs/protocol.md` directly instead, so nothing was lost.
