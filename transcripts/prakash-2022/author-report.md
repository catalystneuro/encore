I finished steps 1 to 5 of the Author section and built the handover package (step 6) in `executed/prakash-2022/handover/`. The final `entry.py all` run passed with 0 check errors; the notebook took 38 minutes and gave the same numbers as the development runs. Nothing is committed.

**(1) Outcomes per claim**

| Claim | Outcome |
|---|---|
| fig2d-chr2-ctz-excites, fig2d-gtacr2-ctz-inhibits, fig3c-uncut-responses, fig3c-cut-abolishes-ctz, figs4c-blockers-silence, fig4c-sb-ctz-activates, fig4e-late-ctz-no-effect, fig4e-stim-then-ctz-activates, fig4e-stim-alone-no-effect, fig5c-bont-blocks, fig6c-green-light-abolishes | reproduced (tested on the article's Supplementary Data 1 to 6) |
| fig6f-nonfunctional-opsin-no-response | not reproduced: p = 3.6e-10, where the paper reports 0.787; the published "SB alone" column looks misplaced |
| figs5-bont-reduces-release, figs6-luciferase-in-dcvs, figs3-ctz-acts-postsynaptically, figs2-cut-disrupts-synchrony | blocked: data missing |
| fig7b-bioluminescence-both-groups, fig7c-gamma-emerges-opsin-plus | reproduced |
| fig7d-contacts-exceeding-baseline | not reproduced |
| fig7d-superficial-layers | blocked: metadata insufficient |
| fig7e-gamma-power-electrodes, fig7e-gamma-events-electrodes, fig7e-gamma-power-mice | partially reproduced |
| fig7e-gamma-events-mice, fig7f-mua-mice-not-significant | blocked: methods underspecified |
| fig7f-mua-electrodes | not reproduced |

**(2) The dataset, assumptions and questions**

What the dataset holds and how it differs from the paper:
- It holds only the in vivo experiment of Fig. 7: six mice in two groups of three, and one Opsin (+) mouse has no imaging.
- The ephys is at 10 kHz. The file says it was acquired at 20 kHz; the Methods say 30 kHz.
- Two image series are not 512 x 512 as the Methods say: interlum_4 is 1024 x 1024 and interlum_ctrl_2 is 684 x 697.
- interlum_4 has 58 blank (all-zero) frames, and its imaging ends 866 s after onset, where the paper's series run to 1200 s.
- In interlum_ctrl_4 the bioluminescence onset comes 8 s before the recorded start of the CTZ infusion.
- The ROI position is not recorded, and the electrode positions don't say which end of the probe is the surface.
- Signal amplitudes are low for raw recordings stored in volts (median contact RMS 1.9 to 6.7 µV).
- The paper's errant-contact rule flags 4 contacts here, not the paper's 7.
- I matched the bioluminescence series against the article's Supplementary Data 7, as a check only. The three Opsin (-) mice match the paper's controls (r 0.975 to 0.990). Neither imaged Opsin (+) mouse matches the paper's "exp 1" series (r at most 0.68).

The draft and the published version contain the same files. I pinned the published version 0.240319.2026; the reason is in the notebook header.

Assumptions: I flagged no outcome as resting on an assumption. Two choices could change results; both are recorded as deviations:
- Blank frames are treated as missing. Otherwise the onset of interlum_4 falls on a blank frame.
- Bioluminescence is the whole-frame mean, because the paper's ROI reading cannot be run.

Questions for the paper's authors are recorded as `methods_unavailable` findings:
- Which 7 contacts were excluded.
- Which percentile rule gives each mouse's 85th percentile.
- How gamma events were detected: the counts here are about 30 per contact against the paper's 214.
- Which baseline values the "contact exceeds baseline" bootstrap used.

I asked a reader nothing.

**(3) Where the protocol was unclear or did not fit**
1. The claims file's criteria block a claim when its readings give different outcomes. Step 1.6 lets the author adopt the best-supported reading instead. I followed the claims file and blocked the two mouse-level claims. I noted that MATLAB's prctile would be the best-supported choice.
2. The protocol's readings cover methods the paper leaves open, not an undocumented layout in the data (here, the probe orientation). When the two orientations gave opposite outcomes, I blocked the claim as `metadata_insufficient`.
3. Step 2 asks for a contrast showing that the data streams share a clock. In this design (one session per mouse with a drug), the only contrast on the ephys is the effect being tested. I said so in the notebook, and the clock is recorded as not established.
4. The 10-minute runtime target cannot be met here: about 40 GB has to be streamed three times, once to find errant contacts and once per kept-contact set the claims file asks for. The run took 38 minutes.
5. There is no slot for outside data used only in the data check (Supplementary Data 7). I listed it under `inputs` and stated that no outcome uses it.
6. The supplementary spreadsheets are pinned only by the article's DOI. I recorded the publisher's file URLs alongside it.
7. The protocol doesn't say which value goes in `measured` when no reading matches. I recorded the first reading the criterion lists.

**(4) Runtime and failures**
- The session took about 2 h 45 min (11:03 to about 13:47 UTC).
- The full notebook was executed twice by `entry.py all`, about 38 minutes each. The second run only added a markdown note on clocks, and its outputs are identical to the first.
- Peak memory was about 8.6 GB.
- Nothing failed.
