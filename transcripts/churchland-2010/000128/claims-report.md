I wrote `claims/000128/10.1016-j.neuron.2010.09.015.yaml`. The quote checker reports 0 problems: 21 claims, 21 quotes, 9 statistical values. Nothing is committed.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC2991102, NIHMS240235): Results, Methods, figure legends, and the one supplement file. That file holds Supplemental Figures 1 to 5, the Supplemental Text and the Supplemental Experimental Procedures. No PDF of the main text was supplied, so I saw only the figure legends, not the figures. The paper links no code (it only says the regressions were done in Matlab), so no code was read, and every method in the file is cited to the Methods, a legend or the supplement.

**Data.** The dataset's title on the archive points to the maze-task array recordings from monkey J ("J-array": 146 units, 108 conditions, no EMG). The claims on the speed task (monkeys A and B), the single-electrode J recordings and EMG are written as the paper reports them, and are blocked if the dataset does not hold those data.

**Counts.**
- **Claims:** 21, all with quotes; none needed `inferred`.
- **Criteria:** all 21 have one; 2 are simulations of the paper's model.
- **Expected numbers:** 8 claims have them.
- **Statistics:** 9 entries in 4 claims:
  - the mean tuning correlation per dataset (p = 0.01, 0.01, 0.12, 0.03);
  - the regression on anterior-posterior (AP) location (four r and p values);
  - the Figure 6E asterisks (p < 0.001).

**Details the paper leaves open, with the readings named:**
- **Trial selection:** the reference "proto-trial" and how the two velocity components are compared. Readings: the condition-mean velocity with each component at r > 0.9, or the components concatenated.
- **Movement onset:** the paper never says how it was detected. The file uses the onset marked in the dataset; if there is none, that step is open.
- **"Spikes/s of tuning" for neuron inclusion:** the range across conditions, or the SD across conditions.
- **Test of the mean correlation against zero:** a t-test, a t-test on Fisher z, or a Wilcoxon signed-rank test.
- **Highest PCA dimensionality tested:** 14 or 12.
- **Kinematic space:** the window end (800 or 600 ms after movement onset) and "each neuron contributed one kinematic variable" (the six variables once, or repeated once per neuron).
- **Task spaces:** peak velocity (each component's maximum, or the components at peak speed) and segments (equal path length, or equal time).
- **Figure 4E:** how the go-cue and movement-onset traces are spliced (movement-locked throughout, or a splice).
- **Supplemental Figure 1:** the two intermediate conditions (read as the one-third and two-thirds ranks). For "dramatically smaller" no threshold is given; readings: less than half, or less than a quarter.
- **Figure 7A:** "performed poorly" means either below the unshuffled peri-movement space, or below it and also below the kinematic space.
- **Figure 7B:** "monkey J" means either the single-electrode J dataset or both J datasets.
- **Figure 7C:** whether each anterior or posterior half gets its own space; readings: built from that half, or from all neurons.
- **Figure 8:** the distribution of initial states (uniform or normal) and the grey interval (360 or 180 steps).
- **Standard choices** that cannot change an outcome: the 20 ms Gaussian taken as SD, 10 ms sampling, the shuffle count, the number of consistency draws, and the end-of-reach rule.

**Thresholds I set myself.** Several qualitative claims have no test or threshold in the paper, so their criteria are my readings of the wording, and the file says so:
- "most did not" maintain tuning (the 0.72 example is used as the cutoff);
- "began to decline" and "near zero" (Figure 4E);
- "almost always" higher;
- the dimensionality peak.

**Missing from the paper:**
- The neuron counts behind each mean correlation.
- The test behind the four p-values and behind the Figure 6E asterisks.
- The identity of the Figure 2B neuron.
- How movement onset was detected.
- A per-unit AP location for the array units, which the AP claims need.

The trials-per-neuron figure for J-array differs between sections (2166 in the Results, 2155 in the Methods); both fall within the tolerance.
