**Verifier report, round 1: Burman et al. 2023 on DANDI:000458**

The claims file has 35 claims. Ten are tested: six in `reproduce_burman_2023.ipynb` and four in `network_model.ipynb`. The other 25 are marked "Not testable": 24 patch-clamp claims, plus figs4-intrinsic-properties.

### A. Outcomes

| Claim id | My outcome | Reason |
|---|---|---|
| dataset-sessions-link | reproduced | Cell 13: all 17 gist sessions are assets of 0.230317.0039, each has every units and trials field, and each has both epochs. Cell 4: 16 subjects. |
| fig4c-sample | partially_reproduced | Cell 15, A1F1 (the Methods reading): 721 kept (inside 662 ± 66.2), but 144 excluded (outside 203 ± 20.3). Per-recording minimum is 7 against 1; 17 recordings, 16 mice; the total of 865 matches. Under the variant A1F2 every number matches the paper exactly (662/203, median 34, 1 to 93), so this is a deviation, not a failure of the data. |
| fig4d-synchrony-lower-awake | partially_reproduced | Cell 18, A1F1: awake 0.3188 is just outside 0.320–0.330; isoflurane 0.3862 is inside. Awake is lower, p = 1.45e-32. A1F2 matches exactly (0.3253 / 0.3928). |
| fig4d-entropy-higher-awake | partially_reproduced | Cell 22, A1F1: awake 1.3887 and isoflurane 1.1502 are both outside tolerance. Awake is higher, p = 3.3e-30, n = 656. A1F2 matches exactly (1.3474 / 1.1106). |
| fig4-rate-higher-awake | reproduced | Cell 24, A1F1: 14.0 Hz awake against 7.59 Hz isoflurane, paired t = 12.4, p far below 0.05. Holds under every reading; 15 of 17 recordings go the same way. |
| figs6-rate-regressed | reproduced | Cell 26, A1F1: synchrony is negative and entropy positive under R1, R2 and R3, all p < 1e-10. Same under every variant. |
| fig4f-model-hyperpolarizing-less-activity | reproduced | Model cell 11: 8.785 Hz hyperpolarizing against 19.468 Hz shunting, paired p ≈ 0; lower in 20 of 20 runs. |
| fig4h-model-synchrony | partially_reproduced | Model cell 7: shunting 0.7833 is inside tolerance; hyperpolarizing 0.8789 is outside (0.880–0.882). Shunting is lower, p ≈ 0, in 20 of 20 runs. See B2. |
| fig4h-model-entropy | partially_reproduced | Model cell 9: shunting 0.4516 is inside tolerance; hyperpolarizing 0.2014 is outside (0.195–0.199). Shunting is higher, p ≈ 0, in 20 of 20 runs. See B2. |
| figs7-model-decoding | reproduced | Model cell 13: accuracy 0.985 shunting against 0.932 hyperpolarizing. D1: p = 1.1e-12. D2: higher in 20 of 20 runs. Chance is 0.01 (100 patterns). |
| 24 patch-clamp claims (fig1b-perforation-rs, fig1h-vu-egaba, fig1i-vu-rmp, fig1j-vu-df, figs2-ramp-equals-step, figs3-egaba-unrelated-amplitude-rs, rm-awake-lower, fig2c-vm-depolarized, fig2d-subthreshold-fluctuation, fig2f-response-polarity, fig2h-egaba-depolarized, fig2i-rmp-depolarized, fig2j-df-depolarized, fig2j-awake-df-zero, fig2k-conductance-same, figs5-within-anesthetized, rm-nbqx-higher, fig3c-nbqx-vm, fig3d-nbqx-fluctuation, fig3e-nbqx-polarity, fig3g-nbqx-egaba, fig3h-nbqx-rmp, fig3i-nbqx-df, fig3j-nbqx-conductance-same) | blocked: data_missing | I queried the archive. The version has 24 assets, all `*_behavior+ecephys.nwb`. The measured variables are Units, ElectricalSeries, LFP and behavior, with no intracellular recordings. A DANDI search for "Burman", "Akerman" and "gramicidin" returns 0 dandisets. No part can be tested. |
| figs4-intrinsic-properties | blocked: methods_underspecified | The measure and test are only in the Figure S4 legend, which was not supplied. The notebook gives the reason as "other"; methods_underspecified fits better. The NEURON model (commit a404c3e) is linked, so a qualitative partial test may have been possible (B3). |

### B. Problems

1. **[affects a conclusion]** Cells 15, 18 and 22: the A1F1 rule against an exact A1F2 match (a point about the claims file, not the code). The claims file (N7) judges every Neuropixels claim under F1. Under F2, the gist's `get_firing_rate`, every published number is reproduced exactly: 662/203, median 34, range 1 to 93, synchrony 0.3253/0.3928, entropy 1.3474/1.1106. That is strong evidence that the paper's numbers were made with the gist's summed-latency rate. The three partial outcomes therefore reflect a bug in the paper's own code, not the data. I am reporting this, not overriding the rule; the outcomes should be recorded as deviations.
2. **[affects a conclusion]** fig4h criteria: the tolerance is too tight for runs with different seeds (a point about the claims file). The tolerance is the paper's SEM over 16,000 pooled neurons (0.001 and 0.002). The run-to-run SE of a 20-run mean, which I computed from model cell 4's per-run means, is 0.0013 for synchrony and 0.0023 for entropy. The hyperpolarizing misses are 1.6 and 1.9 of these SEs. With seeds that differ from the paper's (the gist sets none), that is seed noise, so the partial outcomes come from the criterion, not the model.
3. **[does not affect a conclusion]** Notebook cell 0, figs4: the "other" reason does not mention that the NEURON model code is available. The notebook neither attempts nor argues against simulating ramp E_GABA estimates under anesthetized and awake membrane properties.
4. **[does not affect a conclusion]** Cells 19 and 24: p-values print as `0.00e+00` because they are rounded with `.round(4)` / `.round(3)` before formatting. The true values are tiny, so nothing changes.
5. **[does not affect a conclusion]** Cell 8: the clock check uses off-pulse windows on only 2 of 17 files. For the other 15 it relies on the evoked-count contrast.
6. **[does not affect a conclusion]** Readings collapse. Cells 6 and 7 show that A1 equals A2 (only SSp-ll and SSp-tr occur) and that ≥ 0.4 equals > 0.4 (no unit has exactly 0.4 ms). In effect only F1 against F2 matters. This is handled correctly.
7. **[does not affect a conclusion]** `network.simulate`: a neuron with one spike gets entropy 0, not NaN, as in the gist. This differs from N5 for the data, but no neuron is affected (0 dropped; every neuron spikes).
8. **[does not affect a conclusion]** `npx.measures` and `npx.histogram`: I tested them on a synthetic 2-unit, 3-trial session. F1, F2, entropy and synchrony (unit included in its own population; spikes at 12.0 and 1.9 ms excluded) all match hand calculation. `read_session` assigns each spike to the latest electrical stop, which is safe with inter-pulse intervals of 3.5–4.5 s.
9. **[does not affect a conclusion]** `npx.paired`: the t tests pool neurons across 17 recordings and ignore clustering, as the paper does. The per-recording breakdowns (15 of 17 recordings in the expected direction for synchrony, entropy and rate) support the direction.

### C. What I could not check

- **Data-analysis gist.** I could not see it, so I cannot confirm that npx's F2 denominator (trial position within the condition's valid trials, in table order) and its trial ordering match it. The exact A1F2 match makes this likely but does not prove it. A cell running the gist's own functions on one session and comparing per unit with npx would settle it.
- **Simulation gist.** `network.py` is checked only against its own whole-run-stimulus mode (model cell 3), not against the gist. One unmodified gist run at a fixed seed, compared spike for spike, would check the transcription.
- **Brian 2 learning rate.** Whether Brian 2 rereads `eta` from the mutated `syn_ns` dict is supported only indirectly: the summed weights do not change after balancing. That is good evidence, but it is not a direct printout of `eta` per run.
- **Supplement (Figures S4, S6, S7 legends).** Not available, so I could not see which regression and decoding test the paper used. Its text would show whether R1–R3 and D1/D2 include the paper's method.
