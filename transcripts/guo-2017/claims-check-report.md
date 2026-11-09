The file is fit for an attempt, and its last check says `ready: true`.

**Checker result:** `claims/000009/10.1038-nature22324.yaml: 39 claims, 39 quotes, 11 statistical values, 0 problems`. The first run gave the same with 37 claims; the two extra are claims I added. All quotes and statistics matched the text in both runs.

**Changes, by claim** (each is also listed under `checks`):
- **Header conventions:**
  - **S:** which trial outcomes enter the selectivity t-test is now named as open (correct trials only, or correct and incorrect).
  - **P:** the per-unit t-test now has the Student's and Welch's readings.
  - **L:** reading L2 is now marked as a stand-in. It uses the injection site from Extended Data Fig. 9, a different experiment from the Extended Data Fig. 1 labelling the Methods cite for the VM/VAL centre.
- **task-performance:** what the lick-early and no-response rates are counted over was stated as fact. The paper doesn't say, so it is now a reading.
- **muscimol-vmval-bias:**
  - The statement gave the legends' distances, but its own quote gives the Results' figures, and the legend's dorsal distance is measured from MD, not VM/VAL. It now gives both.
  - The legend doesn't say which panel carries the significance star; the criterion now allows contra or ipsi.
- **fig2e-alm-selectivity:** added the new outcome readings from convention S.
- **fig2e-alm-contra-ipsi-balance:** the binomial test was presented as the only reading the text suggests, but the paper gives no test. There are now two readings, and the claim is marked as underspecified if they disagree.
- **fig3d-all-layers:** removed two requirements the paper doesn't state: significantly inhibited neurons in every depth bin, and at least 5 neurons per bin. The readings now cover the bin size and what "modulated" means.
- **wc-near-threshold:** the paper doesn't define spike threshold, so using the "kink" rule for it is now marked as a reading.
- **fig5c-selectivity-reduced:** the 1300 ms window is now marked as read from Fig. 5b. Added a report for neurons whose rate did not change, which the statement mentions.
- **fig6c-unmodulated-less-selective:** the slope (-0.73) and r (-0.33) were listed as expected values but played no part in the outcome. They are now in the statement and required for "reproduced".
- **fig6d-localized:** which units enter and which window "first 100 ms" means are now open, with readings for each.
- **vm1-photoinhibition-no-effect:** the legend says vM1 photoinhibition produced "less reduction", which is weaker than the Results' "did not cause a reduction". The statement now includes this. The paired test was presented as the paper's, but it is a reading; absence and the comparison with ALM photoinhibition are now tested separately.
- **fig6e-onset-latencies:** the legend calls the SNr and VM/VAL values a "latency difference". Added the reading where they are measured from the ALM silencing onset.
- **Added claims:**
  - `selectivity-time-course` (Fig. 2e, f; Extended Data Fig. 4c, f).
  - `alm-gabaergic-no-thalamic-projection` (Extended Data Fig. 8h, i).

**Still open:**
- The Supplementary Information and Supplementary Tables are not in the text. `latency-model-t3` and `network-models` can't be specified, and the photostimulus powers and coordinates per experiment are unknown.
- The text gives no coordinate for the VM/VAL centre. Reading L2 can only be checked against the counts 313 and 295.
- `selectivity-time-course` uses standard choices for words the paper doesn't quantify.
- No PDF was supplied, so I couldn't read any figure (for example the Fig. 3d bins or which panel carries the Extended Data Fig. 3b star).

Nothing is committed or pushed.
