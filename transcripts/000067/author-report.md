I finished steps 1 to 5 and ran the handover (step 6). `entry.py check` reports 0 errors and the notebook passes `entry.py run` in 605 s. Nothing is committed.

**Paper and version.** I used the full text of the author manuscript in PubMed Central (PMC2562676), saved under `paper/`. The supplementary PDF could not be fetched: PubMed Central and the publisher returned a reCAPTCHA page. I pinned 0.250624.0419, the most recent published version. The paper cites no version, and both published versions and the draft hold the same 28 assets with the same blob ids.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| channel-region-link | partially reproduced |
| rats-and-units | not reproduced |
| task-performance | blocked: data missing |
| fig2c-active-fraction | not reproduced |
| fig2-field-size | partially reproduced |
| fig2b-trajectory-selective | partially reproduced |
| traj-diverge | blocked: data missing |
| odor-nosepoke | partially reproduced |
| fig3-connection-rates | partially reproduced |
| fig3-cell-classes | not reproduced |
| fig3f-distance | not reproduced |
| fig4-position-dependence | not reproduced |
| fig6-facilitation-depression | not reproduced |
| fig7-supralinear | not reproduced |
| fig3-trajectory-by-class | not reproduced |
| ee188-example-session | blocked: data missing |

## 2. What was found about the dandiset

- **Missing data:** it holds 3 of the paper's 4 rats. The paper's example session EE.188, and also EE.152 and EE.165, are absent. EE.210 has no trial table.
- **Units table:** it holds spike times only. It mixes mPFC units, CA1 units, multi-unit clusters and clusters of the nose-poke sensor signals, with no channel, shank, region or cell type.
  - I placed each unit on a probe from its mean waveform in the wideband signal.
  - That is impossible for EE.088 and the other sessions of its day, which have no wideband signal.
  - Electrode locations are "unknown", and the electrode groups are just cuts of 8 consecutive channels.
- **Rat GG channel map:** it differs from the CRCNS description of the same recordings. The sensors are on channels 65 and 66, CA1 is on 70 to 101, and the sensor order (or the side labels) is reversed relative to rats EE and FF.
- **Trial table:**
  - `stop_time` is the end of the nose poke, which is the paper's trial start.
  - `left_or_right` carries the description of `reward_time`.
  - Only correct trials are listed.
- **Position:** both position series are the x coordinates of the two head LEDs, in pixels though labelled metres; the second is all zeros. There is no y coordinate. The linearized position is labelled metres but runs from 0 to 2.
- **Spike order:** in six files, unit 1's spike times are not in ascending order.
- **Clocks:** spikes, trials and LFP share one clock. Shown with the sensor edges, the spike waveforms and side decoding; decoding is weak in GG.097.

## 3. Where the protocol was unclear, wrong or missing something

1. **Outside labels the paper does not rely on.** The only channel-to-region map is in the CRCNS documentation, not something the paper uses. I treated it as `with_labels`, listed it under inputs, and tested it with a link claim.
2. **"Stated spread" as tolerance.** The paper's ±0.17 is the spread across neurons, not the uncertainty of the mean. I followed the protocol literally for the mean and added the s.d. as a second expected value with a 10% tolerance, which is the part that actually tests the claim.
3. **Values given by layer, with no layer per subject.** The protocol has no rule for this. I matched rat by rat, allowing each rat either layer with at most one in layer 5.
4. **Criteria written after seeing some results.** A timing run of the connection test printed per-session connection counts before I wrote three of the criteria. The protocol only covers seeing the data check first. I disclosed this in the claims file and changed none of those method choices afterwards.
5. **The Methods' test cannot work here.** The rank-based global band can never reach a one-sided 1% with 1000 surrogates on 101 smooth points. I found this after a first run gave 1.0% significant pairs. I switched to a mean ± c·s.d. band, kept the rank version as a variant, and recorded when and why as a deviation. The protocol's tie-break rule does not cover a test that cannot fire.
6. **No paper code.** The protocol only asks about code the paper or dandiset links to. I read the conversion code and the spike-sorting reader it used, recorded both at their commits, and used them to interpret the files.
7. **Supplement unavailable.** There is no rule for when the supplement is what defines the methods. I fixed those measures in the criteria and recorded them as deviations.
8. **A label link that holds only after a correction.** There is no outcome rule for this. I wrote it into the criterion beforehand as partially reproduced.
9. **A "per rat" criterion one rat cannot meet.** Rat GG has no putative interneurons, so fig3-trajectory-by-class fails its criterion. The protocol's rule for blocks that depend on a selection might have allowed `blocked: other` instead; I applied the criterion as written.
10. **Units shared across sessions.** Rat EE's sessions of one day were spike-sorted together, so they may share units. I counted units per session and stated this as an assumption.

## 4. Runtime and failures

- The notebook takes about 10 minutes, most of it streaming. I made three full clean runs, and the conclusions were checked against the final executed copy.
- The PubMed Central XML endpoint and the supplement could not be downloaded. The Buzsáki lab mirror of the data is not open. The CRCNS data files need an account and were not used; only their public description PDF was.
- Bugs I found and fixed before the final run:
  - The rank band could not reach significance (point 5).
  - A data-check cell read the position on the frame where it had already dropped to 0.
- Some untracked files in the repo root (`.bashrc`, `.idea`, `scripts` and others) are sandbox placeholder devices, not my output; I left them in place.
