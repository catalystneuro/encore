I didn't write the claims file. My attempt to write `claims/000549/10.1016-j.bioelechem.2022.108319.yaml` was stopped by a safety classifier, so the tool call never ran. I have not tried again, and `claims/000549/` does not exist. That means no quotes were checked and `tools/claims_check.py` was not run.

**What I read.** The paper is complete enough to write claims from:
- **Text:** the accepted author manuscript in PubMed Central (PMC9729435, NIHMS1849847), as served by ncbi_pmc. It has the Methods (2.1 to 2.6), Results (3.1 to 3.5), Discussion and all figure legends. I did not read the version of record, and there is no PDF.
- **Supplement:** PMC lists none, and the text cites none.
- **Code:** the paper links none. Images were measured in MetaMorph and fits made in Grapher.
- **Dataset:** 000549's title is the legend title of Fig. 4 (pulse duration, unipolar and 50% bipolar pulses). Fig. 5 re-measures the same images along the other axis. Dandiset 000550 ("Pulse repetition rate") names the same paper.

**What the file would hold.** It is drafted but not written:
- **Claims:** about 22, covering Figs. 2 to 7 and the thermometry in Methods 2.4. All but one or two have quotes from the text.
- **Statistics:** each test is the paper's two-sided Student's t-test. The reported p-values are p<0.01 and p<0.05 for Figs. 2C, 4 and 5, and p<0.0001 for the Fig. 7 exponential fits.
- **Tolerances:** reported ranges such as "20–25%", "30–50%", "2–3 fold" and "3–4%" are widened by 10% of each bound; single values get 10%.

**Details the paper leaves open, with the readings I would name:**
- **Field strength of each ROI:** it comes from the paper's Sim4Life model, which the paper does not deposit. Readings are (a) field values held in the dataset, or (b) ROIs ordered by distance from the center. Under (b), claims stated at a kV/cm value cannot be tested.
- **ROI layout:** only the 200-µm size is given. Readings are contiguous squares centered on the midpoint or offset by half a square, with the two sides of the center averaged or kept apart.
- **Background area inside the electrode footprints:** not given.
- **Fit for the Fig. 4 and Fig. 6 ratio curves:** the legends say "either exponential or polynomial". Readings are exponential, 2nd degree polynomial, or the ratio of means at each ROI.
- **Field cutoff for microsecond pulses:** not given (for nanosecond pulses it is under 7 to 8 kV/cm).
- **t-test form:** paired or unpaired for anode against cathode within a dish, and how the per-dish "% of unipolar" is formed.
- **Tests behind the "no dependence" claims (Figs. 2B, 2C, 3D):** the paper names none, so the gap rule from Methods 2.5 is the only test it offers.

**Missing from the paper:** the simulated field map, which the field-dependent claims need.

The file still needs to be written and checked in a new run.
