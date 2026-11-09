I've revised the entry for every point in round 1, re-run it, and recorded the round. Three outcomes change, all to the verifier's verdict. The entry passes its checks with 0 errors, and the clean run took 1087 s (about 18 minutes, up from 12). Its outputs match my development run line for line. Nothing is committed.

## Outcome changes

| Claim | Was | Now | Why |
|---|---|---|---|
| fig1g-all-ten-sensors-respond | partially reproduced | not reproduced | As the criterion is written, a sensor's mean trace is highest in its own or partner's well for only 2 of 10 sensors (3 of 10 by the per-well mean), under both labelling readings. |
| fig1h-crosstalk-pairs | partially reproduced | not reproduced | AVP-OXT ranks 12th to 16th of 45 pairs across windows and readings; 10 to 14 other pairs lie above it. |
| table1-peak-dff-morse | partially reproduced | not reproduced | The criterion asks for each value within 10%; only 4 or 5 of 14 are (2 of 14 with the reading (a) labels). |

The other 44 outcomes are unchanged, including the 35 blocked claims.

## What I added or corrected

**fig1g-all-ten-sensors-respond.** Responses carry over into later wells, which is why the criterion fails. I measured how much each well's plateau rises over the previous well's: every sensor rises most in its own ligand's well (10 of 10, under both readings). I added a question for a reader in `questions/001074.yaml` asking whether "highest during the well" is the intended reading of Figure 1G. The claim itself is unchanged.

**Labelling assumptions.** The rule that a cluster keeps its ligand only when its mean trace also peaks in that ligand's well was my own choice. It is now stated as an assumption in the helper, the notebook and the deviations. So is the one-minute window used to match clusters to ligands. The notebook shows labels without the rule (606 and 402 cells) and with a whole-well window (539 and 372). No variant brings the fig1g-sensor-yield cell counts into range. A per-sensor table of the mean trace in each well, for both readings, now checks the labels.

**Reading (a) labels are now carried through every labelled claim.** Only figs3e-tau-on-under-one-minute is affected. With those labels the concentration fit gives 7 of 10 sensors under 60 s against 8 needed, so its two readings would disagree. I kept it as reproduced, marked as resting on the reading (b) labels, and the notes say so.

**figs3e: fitting the plateau as a free parameter.** The verifier noted that fixing the plateau, as the code does, shortens long time constants. I added that variant: 9 and 6 of 10 (reading b).

**Table 1 EC50s.** I flagged the Eq. 28 fits that sit on the 1 pM lower bound (3 of 14) and added a variant that subtracts each cell's lowest-well plateau first (0 of 10 within 10%). Both EC50 claims still fail under every variant.

**fig1j.** Added a comparison of per-probe EC50s against Table 1 as well as against my consensus fits (3 of 10 sensors). It still fails.

**fig1c.** Added depth from the dose-recording masks of all ten probes, not just five; every recording has cells in all three thirds.

**figs2f-cells-tracked.** The main result now uses the paper's own probe sets for Figure S2F, from the code: 26 of 39 probes in range (0.67), so it stays reproduced. Slice probes alone are 3 of 7. The code confirms that each `matched<k>` file holds one pair of recordings, and 70 of 71 pairs hold equal counts. It also shows the probe 20230922-PL28 file `matched1` being re-saved as `matched`, which likely explains that probe's mislabelled files.

**Blocked claims.** A new cell shows, by context, that no file holds acquisition or stimulus data. For fig3g-ten-sensor-yield I listed every mouse probe with a post hoc dipping recording. I labelled the two 2025 probes, which carry 7 and 6 sensors. It stays blocked: the two 2023 probes have no well order in the files or the code, and the code loads their labels from files outside its repository.

**Small points.**
- The off-target normalization and the artefact-jump residual are noted, with no change.
- Reading (a) now gives 384 labelled cells where the first run printed 382, with the same code. The numbers and the record are updated.

**Record and README.** `attempts/001074-kalugin-2026-01.yaml` has updated notes and deviations and a `verifications` round with all 47 claims, giving the verifier's reasons and my responses. The README and the notebook summary carry the new outcomes and runtime.

## Not done

- **Band-pass artefact variant for fig1h:** still not run.
- **Stability denominator:** the verifier's remark that only stable recordings may have been deposited is not checked or recorded.
- **`tools/build_site.py`:** it was already modified before this run started, and I left it alone.
