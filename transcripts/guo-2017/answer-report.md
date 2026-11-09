I've answered all six questions in `questions/000009.yaml` and set `answered: 2026-10-20` on each. The answers are also written into the criteria of `claims/000009/10.1038-nature22324.yaml`. I changed no statement or expected value. `python tools/claims_check.py` reports 39 claims, 39 quotes and 0 problems. Nothing is committed.

One gap affects most of the answers: Supplementary Table 1, which lists the animals, coordinates and powers for each experiment, is not in the text I had. Answers 2, 3 and 5 rest on the main text without it.

1. **alm-unit-classes (computed widths P1 or file labels P2):** The paper gives the rule, not the label: widths are "computed as the trough-to-peak interval in the mean spike waveform", which is P1. It never mentions the deposited `cell_type` label, so P2 is only a reading. For the thalamic claims of Fig. 2 and 6 there is a third reading (P3, all units pooled), because the Methods say the conclusions "are valid if all the units were pooled". This is now convention C in the file's opening comment.

2. **fig3-alm-collapse (PV-Cre x Ai32 sessions):** No, by the text. Fig. 3 is "using VGAT-ChR2-EYFP mice" at 10 mW (Extended Data Fig. 2e, n = 314), and PV-Cre x Ai32 mice are listed only for ALM photoinhibition. Those sessions stay a variant and are not judged.

3. **fig6c-vmval-reduced (0.75 and 0.79 mW trials):** No. The Methods give only "1.5mW average power" for ALM photoinhibition, so lower-power trials are outside the condition and pooling all powers is a variant. This is added to convention P.

4. **wc-thalamus-hyperpolarization (where the photostimulus starts):** The paper puts the onset at the start of the delay: 1.3 s after the pole starts moving, which is 0.1 s after it starts to retract. It does not say what the files' `pole_in_time` and `pole_out_time` mark. So both E and M are readings it allows, and placing the onset from the Vm change itself is not one. The 7.9 ms latency cannot be fixed from the paper.

5. **vm1-photoinhibition-no-effect (is galvo (0.5, 0.5) vM1, and at what power):** The paper does not say which condition is vM1. Its only vM1 coordinate is an Allen tracer injection, and the galvo coordinate frame is not given. On power, the comparison is with ALM at 1.5 mW (the Methods' only cortical power); ALM at matched power is a variant.

6. **selectivity-time-course (do photoinhibition trials enter):** The paper does not say. Both readings stand: correct control trials only (t1) and all correct trials (t2).
