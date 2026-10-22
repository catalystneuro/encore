I wrote `claims/000009/10.1038-nature22324.yaml`, and the quote checker passes it with no problems.

**What I read.** The HHMI author manuscript in PMC (PMC6431254), as served by Europe PMC. It has the main text, Methods, and the legends of Figures 1 to 6 and Extended Data Figures 1 to 10. It is the accepted manuscript, not the version of record. There is no PDF, so I could not open any figure. The paper links no analysis code, only the CRCNS deposit (doi:10.6080/K03F4MH2), so there was no code to read. From the dataset I looked only at its DANDI title and description, and the summary of what it holds.

**Missing from the paper text.** The Supplementary Information and Supplementary Tables 1 and 2 (animals, coordinates, light powers, viruses) are not there. Following earlier files in the registry, I went ahead instead of stopping. Two claims depend on the Supplementary Information and cannot be specified from the text: `latency-model-t3` (a model latency of 1.8 ms) and `network-models` (linear against non-linear models). Their criteria say so. No other claim needs the supplement.

**Counts.** 37 claims, all 37 with quotes. 10 claims carry statistics, 11 entries in all. 37 have criteria and 26 have expected values. The claims cover behaviour, unit classes, selectivity in ALM and VM/VAL, strong and weak thalamus photoinhibition, whole-cell recordings, onset latencies, ALM photoinhibition of VM/VAL, the vM1 and SNr controls, and anatomy.

**Details the paper leaves open, and the readings named.** Shared conventions sit in the opening comment; claim-specific ones are in the criteria.
- **Response epoch length:** (R1) 1.3 s after the go cue, or (R2) 1.5 s, the response window.
- **t-test variance:** Student's or Welch's.
- **Trials in photoinhibition rates:** (T1) correct and incorrect, or (T2) correct only.
- **"To X% of control":** (Q1) ratio of population means, (Q2) mean of per-unit ratios, or (Q3) median of per-unit ratios.
- **Spike-onset baseline:** (O1) the control PSTH in the same bin, or (O2) the mean control rate over the delay epoch.
- **Membrane-potential onset:** (V1) onset of the mean trace across cells, or (V2) mean of per-cell onsets.
- **VM/VAL centre:** the text gives no coordinate. (L1) the dataset's own location label, or (L2) 0.4 mm around AP -1.5, ML 0.85, DV 4.0 mm, the tracer injection site "mainly in VM" (Extended Data Fig. 9).
- **Gad2 reduction window:** the whole photostimulus, or 20 to 120 ms after onset.
- **Distance from threshold to resting potential:** the resting window is 0 to 0.5 s before the trial in the Methods but "during the delay epoch" in the Results; both are named.
- **Fig. 5c trials:** correct trials only, or all outcomes under photoinhibition.
- **Fig. 6c selectivity:** absolute contra minus ipsi, or preferred minus non-preferred; and which axis the regression is fitted on.
- **Selectivity groups in Fig. 6b:** by type (preparatory, peri-movement, both), or by epoch.
- **Inhibition measure for "equally inhibited":** ratio or difference of rates.
- **Behaviour rates:** pooled over trials, averaged over sessions, or control trials only.
- **Selectivity counts:** whether photoinhibition trials enter.
- **Muscimol control:** buffer infusions, pauses without infusion, or both.
- **SNr:** whether the 5-trial minimum applies; whether activated neurons enter the onset estimate.
- **Bootstrap resampling unit** in Extended Data Fig. 5g: cells or cell-condition points.
- **Fig. 3d depth bins:** 100 µm or 200 µm.

**Choices with no basis in the paper, for the second reader to check.** Where the paper gives no test or threshold, I set one myself:
- **Comparisons with no test given:** "approximately equal" contra and ipsi preference is judged by a binomial test. The vM1 absence and the thalamus-stronger-than-cortex comparison use the paper's t-test, which it never applies to them.
- **Thresholds I set:** a minimum of 5 neurons per depth bin. Partial-reproduction bands for fig1c, fig3, fig6c, wc-loss-of-excitation and fig2f-vmval-selectivity.
- **Fixed readings:** the 295 VM/VAL units are read as passing both the spike-width and the location rule.

**Inconsistencies inside the paper.**
- Muscimol doses differ: 1.8 to 5.9 ng in the Results, 1.5 to 5 ng in the Extended Data Fig. 3b legend.
- The distances of the control infusion sites differ between the Results and the legends.
- The 15.9 ± 9.3% spread is called SEM in the Methods but standard deviation in the Extended Data Fig. 2d legend.
- The −18.7 mV is written as "control − photoinhibition" but given a negative sign.
- VM/VAL counts differ: 313 in the Methods, 295 in the Results.
- Extended Data Fig. 3b does not say which side, contra or ipsi, carries the significance star.

I made no commits.
