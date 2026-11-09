The claims file for DANDI:001444 is ready for an attempt. I corrected eight things against the paper; a few method details stay open because the paper doesn't give them.

**Checker:** `claims/001444/10.1038-s41531-025-01070-4.yaml: 40 claims, 40 quotes, 10 statistical values, 0 problems`. It counted 12 statistical values before my edits; two statistics entries were removed (see the unitary-event claims below).

**Changes, by claim:**
- **fig1-network-size:** the statement said "15 populations", a number from the code (`cfg.py`), not the paper. It now says seven excitatory pyramidal and two interneuron cell types, as the Methods do.
- **fig4-control-unitary-events, fig7-pd-unitary-events:** I removed the statistics entries. The joint-surprise p < 0.05 decides which time windows count as significant, so it is a threshold used for counting, not a result.
- **fig3b-control-activated-spectrogram:** the statement includes the ~50 ms length of the 25 to 35 Hz bursts, but the criterion never tested it. I added it as an expected value with a 5 ms tolerance. The 14 to 16 Hz band used for the "15 Hz bursts" is now marked as the first reader's choice, since the paper gives no band width.
- **fig5-pd-activated-gamma:** added a note that the Results say ~44 Hz while the legend says ~43 Hz. The tolerance covers both.
- **rest-beta-power-order-of-magnitude:** the 14 to 16 Hz band was justified by a periodicity the paper actually gives as 14 to 15 Hz. It is now stated as a band the paper does not give.
- **control-duty-cycle** (and pd-duty-cycle, which uses it): averaging over periods was a choice the paper doesn't make. I added a second reading: total time above half-height divided by total time.
- **control-coincident-spikes** (and pd-coincident-spikes): the readings now say a spike of another PT5B *neuron*, matching the Results.
- **pt5b-highest-rate:** the "excitatory cell types only" reading now cites the Methods for the seven excitatory cell types.

**Open:**
- **Spectrogram claims (fig3a, fig3b, fig6a, fig6b):** the paper never defines a burst or the band widths. The reading the claims use borrows the paper's half-height rule for duty cycle, so these claims may end up blocked as `methods_underspecified`.
- **pd-it6-rate-unchanged:** this claims there is no change, but the paper names no test or threshold for it. The criterion's p < 0.05 is inferred from the bounds the paper uses elsewhere.
- **Supplement not supplied:** Supplementary Tables 2 and 3 and Supplementary Figs. 1 to 5 were not in the text. So model-pt5b-excitability-decrease and robustness-four-sets can't be completed.
- **Subthreshold oscillation claims:** neither the paper nor its code gives a rule for detecting a subthreshold oscillation.
- **Not covered:** the timing of IT5A and IT5B firing relative to the PT5B spike histogram, and the LFP–spike-histogram antiphase, are described only in words. I judged them minor and added no claim.

**Ready:** yes. The entry is recorded under `checks` with `ready: true`. Nothing was committed or pushed.
