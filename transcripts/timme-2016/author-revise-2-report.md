Round 2 is done. The verifier agreed with all 14 outcomes, so none changed and none is proposed. I re-ran the entry with `python tools/entry.py all entries/timme-2016`: checks report 0 errors, and the notebook took 54.6 min. Every main-analysis number is the same as before, and the conclusions match the new outputs.

**What I added for the verifier's remaining point (the tie-counting test is too liberal)**
- **Connections expected by chance:** cell 12 now prints this for the five tested recordings. Under the tie rule it is 8% to 30% of the significant connections (15.8% pooled; for example 1885 of 6364 for DataSet16 at 3.5 to 14 ms). This is now in cell 16, the Summary, the README and the tie-rule deviation in the record.
- **A stricter-threshold variant, `calibrated`:** no count of the 5000 surrogates gets the false-positive rate down to the nominal 0.1%. The strictest possible (no surrogate at or above the real TE) gives 0.20%, with 13.2% of connections expected by chance. I ran this through every analysis to see which way the excess pushes the results:
  - Every grade stays the same except fig5a. There, (s, Pearson) gives 19 of 48 positive (p = 0.097), which would be reproduced.
  - For fig4ac, the (s) fits rise to R² of 0.92 to 0.97, but one (f) fit stays at 0.88, so the grade is still partial.
  - I kept fig5a as partially reproduced and did not propose a change. The stricter threshold is not the paper's procedure (fewer than 5 of 5000 surrogates), so it is a check, not a better-supported main reading. The record now says the partial grade rests on that threshold.
- **Degree tracks firing rate:** cell 16 and the notes for fig4bd and fig5b now say that a high-degree neuron here is mostly a high-rate neuron.

**Text corrections**
- README run time: "about 52 minutes" is now "55 to 65 minutes".
- Cell 45: the real-data reference has 49 correlations, not 50, because DataSet5 has none at 1.6 to 6.4 ms.
- Cells 14 and 16 (the [44] figures): I checked them against [44]'s full text and they are correct. Cell 14 now quotes the passages (Fig 12C and D legends, and the paragraph before Fig 3) with the DOI and PMC id, since [44] is not under `paper/`.
- fig5ab: the notes now say the criterion only defines "reproduced", and that "partial" records one panel of two.
- Round-1 fig7d reason: it now says the verifier reran only a few models at 50,000 runs.

**The PID redundancy misreading the verifier reported:** this question was already in `questions/timme-2016.yaml`. The record's deviations pointed to a file that doesn't exist (`questions/crcns-ssc-3.yaml`); they now point to the right one, and I fixed the claims path in that file's header.

**Recorded:** round 2 is under `verifications`, with the verifier's reasons in its own words and my responses.

**Not done:** I left the claims file unchanged, as instructed. Some dotfiles and folders I did not create (`.bashrc`, `.idea`, `scripts`, and others) are untracked at the repo root. I left them alone; they should probably be kept out of the workflow's commit.
