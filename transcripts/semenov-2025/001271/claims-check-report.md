The claims file for DANDI:001271 is fit for an attempt. I made four corrections and left two problems open, and I've recorded all of it under `checks` with `ready: true`.

**Checker result:** `claims/001271/10.1016-j.xcrp.2025.102660.yaml: 20 claims, 18 quotes, 7 statistical values, 0 problems`. It gives the same line before and after my changes.

**Changes, by claim:**
- **ap-amplitude-duration:** The outcome rule broke the file's own rule for open method details. Before, if a mean missed the paper's error margin under only one reading, the claim counted as partially reproduced. Now it is reproduced only when every reading agrees, and blocked as methods_underspecified when the readings disagree.
- **fig3-not-heating:** I worked the temperature formula from the paper's own values (1.64 S/m, 63 V/cm, 0.25 s, water's heat capacity). Neither reading gives the paper's 2.5 °C: the peak field gives about 3.9 °C and the RMS field about 1.95 °C. The ratios between the paper's three temperatures do follow the formula. The paper doesn't give the heat capacity or which field it used, so the criterion now says: if the absolute values miss but the ratios are within 10%, the claim is blocked as methods_underspecified, not "not reproduced".
- **fig2d-modulated-thresholds-higher:** The paper calls 57.7 V/cm "the AP threshold" without saying 1 or 5 APs. The criterion now names reading it as the 1-AP threshold as a choice, and reports the 5-AP mean beside it.
- **figs2-neurons-tested:** The expected-value label said TTX neurons only, but the criterion allows two readings (TTX alone, or TTX plus vehicle). The label now names both. It also said the legend shows one vehicle neuron; the legend gives no count, so that is now credited to the figure.

**Open:**
- **figs2-vehicle-keeps-response:** The rule that every field with APs before the solution change must have APs after is the earlier writer's own choice, not the paper's. The run-down in excitability the paper reports (Figure 3A legend) could remove near-threshold APs in a vehicle neuron and fail the claim.
- **Figure S2 layout:** The header gives a layout (one vehicle neuron, two TTX neurons, the fields each was tested at), which I could not check because no PDF renderer is installed here. The legend text says only "three representative neurons". No claim's outcome depends on the layout.

Everything else held up against the paper: statements, sources, statistics (results, not counting thresholds) and tolerances. The cross-references to the 001272, 001273 and 001274 claims files point at ids that exist. Each main finding has a claim, and none comes from outside this paper. Nothing is committed.
