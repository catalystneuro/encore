I didn't write the claims file. A safety classifier stopped my write of `claims/000550/10.1016-j.bioelechem.2022.108319.yaml` partway through, so the file doesn't exist and the quote check never ran. I won't regenerate that content, so it needs a fresh reader run, or you can tell me how to proceed.

**Text read:**
- `paper/10.1016-j.bioelechem.2022.108319.txt` is the NIH author manuscript from PubMed Central (PMC9729435), not the version of record. It has the full main text, Methods 2.1 to 2.6, Results 3.1 to 3.5, Discussion and the legends for Figs. 1 to 7.
- There is no supplement: PMC marks the paper as having none and the text cites none. There is no PDF.
- The paper links no analysis code. It only names commercial software (Grapher 16 for fitting, MetaMorph 7.8.13 for measuring regions of interest), so no code was read.
- Nothing a claim needs is missing from the paper, so it would not have been a reason to stop.

**Dataset:** DANDI lists 000550 as "Pulse repetition rate" (cattle cells, 17 assets). That points to the Fig. 6 experiment. The archive lists the paper's other experiments as separate dandisets: 000489 (Fig. 2), 000548 (Fig. 3), 000549 (Figs. 4 and 5) and 000448 (Fig. 7).

**Planned claims:** about 23, every one with a quote and none from the abstract. Six were on Fig. 6, and the rest covered Figs. 1E, 2, 3, 4, 5 and 7. The p-values the paper reports were all bounds (p<0.01, p<0.05, p<0.0001), recorded as such.

**Details the paper leaves open, with the readings I had planned:**
1. **Where the measurement squares go:** they are 200 µm, but their spacing isn't given. Readings were the positions the dataset records, or squares laid edge to edge; squares on either side of the centre either averaged or kept apart.
2. **Background area under the electrodes:** either the whole of both footprints, or one 200-µm square in each.
3. **Applied voltage for Fig. 6:** not stated. Readings were the value the dataset records, or 5.75 kV as in the other 600-ns experiments.
4. **Curve fits behind the bipolar/unipolar ratios:** the legends say "either exponential or polynomial" without saying which curve got which. Readings were exponential, second-degree polynomial, whichever fits better, or no fit (a ratio of means).
5. **Field range included:** either everything, or only 8 kV/cm and above.
6. **Statistics:** the test is the two-sided Student's t-test with one dish as one sample, uncorrected.
7. **Field strength per square:** this comes from the paper's own simulation (Fig. 1B, C), which wasn't deposited. Claims needing values in kV/cm would therefore use data from outside the dataset.
