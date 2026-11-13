I've answered every point in the round-2 report. No outcome changed and nothing is under `proposed`. I re-ran the entry with `python tools/entry.py all entries/niknam-2019`: the notebook passes in 71 s, the entry check reports 0 errors, and the Figure 1 numbers are the same as before. Nothing is committed.

**Outcomes (unchanged):** 5 reproduced, 1 partially reproduced, 3 not reproduced, 25 blocked (24 too large, 1 methods underspecified, 1 metadata insufficient). The verifier agreed with every outcome, and round 2 is now recorded under `verifications`.

**Corrections:**
- **Cost of the S-model (24 too-large claims):** the old text in cell 37, cell 0 and the 24 notes gave timings from one run that did not match the next. They now give the range across this attempt's runs:
  - as ported: 2.2 to 6.7 ms per fit, 345 to 1,040 hours on 4 CPUs;
  - a fully batched port, which nobody has written: at least 11.5 to 27.5 CPU hours (2.9 to 6.9 hours on 4 CPUs).

  The argument now rests on the cost of the port as it exists, plus the steps that come after the selection. The notebook also prints a new figure: the A-model fits the S-model ten times (Methods, A-model), which puts the batched figure at 29 to 69 hours on 4 CPUs for the A-model claims. This run's values (6.7 ms, 1,037 h, 6.8 h, 68 h) fall inside those ranges.
- **Probe timing:** the summary and the data finding now include the rare runs of 8 to 28 ms and the gaps of 7 to 28 ms that cell 4 prints.

**Questions added for a reader:**
- **fig1c, fig1d, fig1e:** the existing pairing question now says that the smoothed-bin variant is anti-conservative. It treats 71 smoothed, autocorrelated bins as independent pairs, which gives p values of about 1e-13.
- **fig1-example-neurons:** a new question asks whether each example should meet the paper's p < 0.001 rather than the criterion's p < 0.05, citing the Results passage. Under the stricter threshold only 1 of 4 examples would match, and the outcome would go from partially reproduced to not reproduced. The README now mentions it.

**Ref [48], beyond what the verifier asked:** I identified it from the paper's published reference list as Akbarian et al. (2018), IEEE Trans Biomed Eng 65(2):241-253, doi:10.1109/TBME.2017.2762687. It is freely available as PMC5796416. It describes the N-model but publishes no code. The claims file says to take the N-model from ref [48] once it is identified, so the original reason for blocking the N-model claim no longer holds. I still kept that claim blocked as methods underspecified, with no proposed change, because this attempt did not implement the N-model and testing it would need a new analysis. A later attempt can take it up. I updated the notes, the finding, cell 0, cell 37 and the summary to say this.

**Not done:**
- I did not investigate the fixation set of the RF example further, and I did not compare the docx version of the data descriptor; the verifier said neither bears on any conclusion.
- I left the round-1 responses in the record as written, including the old "28 CPU hours" figure, since they record what was said at the time.
- The working tree has stray untracked dotfiles and a `scripts` folder at the repo root. I didn't create them and left them alone.
