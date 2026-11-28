I wrote `claims/alonso-2020.yaml`. The quote checker passes it: 22 claims, 22 quotes, 0 problems. Nothing is committed.

**Text read:** the version of record, extracted from the eLife PDF under `paper/`. That covers the main text, figure legends and Materials and methods. No preprint was used.

**Missing from the paper:**
- **Figure supplements:** only their titles are in the text (Figure 1 supplements 1 to 3, Figure 2 supplement 1, Figure 6 supplement 1). Their legends and panels are missing. The four claims that rest on them (`fig1s1-three-models`, `figs2-ramp-largest-isi`, `figs3-duty-cycle-variable-across-models`, `fig8-up-down-ramps`) use the main-text sentences that describe them. I went ahead because the main findings rest on the main figures. If you count these supplements as ones the results rest on, they should be supplied.
- **PDF figures:** the PDF could not be rendered (pdftoppm is not installed), so no figure was read. The pie-chart counts of Figure 10B are not recorded.
- **Model name:** the extracted text garbles the second character of the model used in Figures 1, 3 and 10 (written as "4?6W66" in the file).

**Code:** the only code the paper links to is the dataset itself, a 99 kB zip of code and parameters on Dryad. I was not allowed to open the dataset, so I read no code. The claims tell the author to take any open detail from the deposited code where it settles it, with the Methods taking precedence where the two disagree.

**Claims:**
- 21 are findings and 1 is a link check that the deposited models match the paper's list and fitted targets.
- All 22 have quotes.
- None has statistics, because the paper reports no tests.
- 21 have criteria; the 22nd (`fig1c-frequency-q10-phase-constant`) is judged on its expected values.
- 9 have expected values.
- Every claim is `data: dataset`, meaning a new simulation of the deposited models.

**Details the paper leaves open, and the readings named:**
- **Shared to all claims:** the spike detection threshold, whether the initial transient is dropped, the synapses' starting state, and how "fired in the right order" is tested. All are left to the deposited code.
- **Q10 of burst frequency:** (a) a log-linear fit over temperature, (b) the 25 to 10 °C frequency ratio raised to 10/15, or (c) the 20 to 10 °C ratio.
- **"Approximately constant" duty cycle and phases:** within 0.1 of a cycle, or within 20% of the 10 °C value (borrowed from the Methods' 0.2 spread limit).
- **Spike amplitude and threshold (Fig. 2):** amplitude as peak minus trough or the top of the voltage distribution; threshold as a dV/dt crossing or where the distribution's spike region begins.
- **Peak current amplitude (Fig. 3):** the largest value in the window, or the mean of per-cycle peaks.
- **Start and end of a burst (Fig. 4):** the first and last third, or the first and last 20%.
- **Model mismatches between legends and Methods:**
  - Figure 5: FGFKQS (Methods) or J9U8SQ ("same model as Figure 7A" in the legend). Both are run.
  - Figure 9B: the same pair, FGFKQS or J9U8SQ. Both are run.
- **Deletion timing (Fig. 9):** 20 s of control then 20 s with the current removed (Results), or removal at 4 s (legend). Both are run.
- **Up and down ramps (34 of 36 models):** which ramp is compared, the 10 to 35 °C one in 30 min or the 10 to 25 °C one over 60 min; "similar" is set at a standard 10% bound.
- **Figure 10B:** whether leak counts among the removed currents; "same response" as all four classes (PD, LP, PY, network) equal or only the network class; and standard bounds for "about half" (0.3 to 0.7) and "most" (above 0.5).
- **Slow time scales (Fig. 7):** read as an interval of more than 2 s between bursts or spikes, or a slow-voltage period of more than 2 s.
- **Largest ISI over the ramp:** followed in 1 °C windows or 1 min windows.
- **Bounds the paper never gives:** I set standard ones and labelled them as such, for "smoothly" (Spearman correlation beyond 0.9), "all" (at least 90% of cases) and the 5 mV used for peak voltage trends.

**Internal inconsistencies, recorded in the claims:**
- The LP and PY duty-cycle target is 25% in the Methods and about 20% in the Results. The 20% is shown as a variant.
- The Figure 8A legend says the cell goes quiet "before 600 s", but on the stated ramp that is about 18 °C. The time is reported but not judged.
- The claim that 2 of 40 solutions failed between control temperatures can only be tested if the deposit holds all 40 solutions, including the 2 that were discarded.
