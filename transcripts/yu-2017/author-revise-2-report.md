I worked through every point in the round-2 report and re-ran the entry. The second full run passed in 1047 s with 6.2 GB of memory at peak, and `tools/entry.py check` reports 0 errors. I didn't commit anything.

**Outcomes.** None changed, since round 2 doesn't allow it.
- **fig2s1cd-theta-autocorrelation** stays `partially_reproduced`. I added a `proposed` change to `reproduced` for a third verification round. The verifier was right: under the claims file's reading O1 (b), where every immobility period counts as a well entry or exit, all four depth comparisons hold (for example MAP 0.00653 against 0.00140, IAP 0.00104 against 0.00043). The partial result came only from the "well visit" definition, which the claims file doesn't have.
- **fig4s1b-offset-matched-coactivity**: the verifier now agrees with `reproduced`, and round 2 records that.

**What I corrected**
- **Entry and exit definition** (fig2c, fig2s1cd, fig2s1ij, fig4s3): every immobility period, as O1 (b) is written, is now the main definition in the notebook, the helper docstring, the README, the summary and the record. Well visits (immobility periods of at least 0.5 s within 15 cm of a well) are shown only as a variant. I also rewrote the deviation that said two contradictory things about what an entry is, in all four outcomes.
- **Question for a reader**: added to `questions/crcns-hc-13.yaml`. It asks whether O1 (b) misreads the paper, whose "periods at wells" (Figure 1, supplement 1B–C) look like visits. It includes the verifier's point that the paper's 0 s peak suggests a 0.5 s minimum would leave out some real visits. The claim itself is unchanged.
- **Statements the outputs didn't support:**
  - The fig4s1b conclusion and notes now say that under O7 (b) the 3 to 4 s bin is significant only under O6 (a) (p = 0.014), and no bin is under O6 (b) (p = 0.066 at 3 to 4 s).
  - The data check now says each day has three sessions except one day of T1 with two (35 sessions over 12 days).
  - The header no longer gives a size for hc-6 (the "28 GB" figure).
  - The clock check now says the IAP rate falls by about half or more, and by two thirds in S2 (7.65 to 2.51 Hz).
  - The README run time had no printed output behind it. I added a last code cell that prints the run time and peak memory, and the README now quotes it: 776 s and 1047 s in two runs, because streaming speed varies, and 6.2 GB.
- **fig2c**: the conclusion now gives the "other side of zero lag" figures for both definitions.
- **Record**: round 2 is entered under `verifications` for all 32 claims, with the verifier's reasons as it gave them and my responses.

**Not done**: nothing the report asked for was left out. The long R1/N2 spike widths still can't be checked, as the verifier noted, because the data hold no waveforms.
