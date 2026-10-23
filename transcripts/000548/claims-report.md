I didn't write a claims file. The write was stopped by a safety classifier, so `claims/000548/` is empty, no quotes were checked with `tools/claims_check.py`, and I'm not retrying the write in another form. Nothing was committed.

**Text read.** The accepted author manuscript from PubMed Central (PMC9729435, NIHMS1849847). It includes the main text, Materials and methods, Results, Discussion and figure legends. PMC lists no supplement and the text cites none. I did not read the version of record. The paper links no code and names no deposited data, so there was no code to read.

**What the dataset holds.** Its DANDI title and description name only the Fig. 3 experiment: trains of 5, 10 or 15 pulses at 1 Hz on bovine endothelial (BPAE) cells, either single 600-ns pulses or 600+600-ns pulses whose second, opposite phase is at 50% of the first.

**Findings to cover.** About 19 claims, roughly one per finding:
- **Fig. 2:** dependence on the second phase's amplitude.
- **Fig. 3:** dependence on pulse number.
- **Figs. 4 and 5:** dependence on pulse duration, and stronger dye uptake near the anode with microsecond pulses.
- **Fig. 6:** dependence on repetition rate.
- **Fig. 7:** membrane-charging time constants.
- **Fig. 1E:** heating.

**Details the paper leaves open for Fig. 3**, the part this dataset can test:
- The applied voltage. 5.75 kV is stated only for the 600-ns pulses of the other experiments (sections 3.1 and 3.3).
- The spacing and number of the measurement regions along the line between the electrodes.
- Whether the 2nd-degree polynomial fits use the per-region means or all replicate values, and how they are weighted.
- The field cutoff for the ratio. The paper says "<7–8 kV/cm", so the readings are 7 and 8 kV/cm.
- How the paper judges that the curves "nearly overlapped". The paper reports no test for this; the only test it names is the two-sided Student's t-test at p < 0.05 from its Methods.

**Missing from the paper.** Nothing the claims would need is missing. The full text and Methods are present and there is no supplement. The run needs to be re-launched to produce the file.
