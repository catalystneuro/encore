**Checker result:** `claims/bittner-2017.yaml: 28 claims, 28 quotes, 0 statistical values, 0 problems`. Before my edits it was 26 claims, also with 0 problems.

**Changes, by claim**
- **fig1cd-spike-count-correlations:** Added Results (Excitatory and inhibitory populations section), paragraph 4 to the source. That paragraph is where the paper says inhibitory-inhibitory pairs have a wider correlation spread than excitatory-excitatory pairs.
- **fig3ab-psv-type-order:** The criterion skipped 10 neurons for no reason the paper gives. It now judges every count from 10 to 150 and says these counts are set here.
- **fig3cd-trial-saturation:** The statement says all four curves saturate. But the paper also says the non-clustered excitatory curves had not saturated by 10,000 trials (Ratio section, paragraph 4). The criterion now says that part is not judged, and why.
- **s2-psv-vs-correlation-width:** The name given for ref 44 ("Macke et al. 2009") is not in the text read, which has no reference list, so I replaced it with a note that the attempt must identify ref 44. I also added that each 20,000-trial set is an independent draw (S2 Fig legend).
- **fig5b-dim-rises-with-inhibitory-fraction:** The Spearman rule is now labelled as set here.
- **fig5ac-trial-dependence:** Added two findings the claim left out of its cited paragraphs, in the statement, quote and criterion:
  - at 20,000 trials, the non-clustered network's percent shared variance trends still hold;
  - at 1,200 trials, the clustered network's percent shared variance slightly decreases.
- **v1-classification-counts:**
  - The Methods are now the main reading and the code a variant, as the protocol requires: training on the top 75% by SNR pooled over all sessions, and excluding four units by waveform.
  - The made-up 0.2 amplitude threshold is replaced by "the four units with the largest rise before depolarization", since the Methods give the count of four.
- **v1-no-excitatory-psv-advantage:** Removed "as the paper's figure implies" (no figure was read). The rule now rests on the Fig 7 legend's standard errors and is labelled as set here. "At most counts" now reads "more than half of the sweep counts", and I named a partial outcome for the case the old rule left undecided.
- **v1-resembles-clustered-network:** The criterion only tested the networks. It now also requires the V1 trend claims it depends on.
- **New claim s4-100ms-window-mixed:** The paper says the Fig 5 trends also hold with 100 ms windows (S4 Fig), and nothing covered this.
- **New claim disc-small-sample-shrinks-ei-difference:** The Discussion (paragraph 8) says the clustered network's difference between excitatory and inhibitory neurons is much smaller with 23 neurons and 1,200 trials. Nothing covered this; "much smaller" is read as less than half, set here.

**Still open**
- **No figures:** There is no PDF, so no figure was read. The neuron and trial count grids, whether Fig 3C and 3D go to 10,000 or 20,000 trials, and every trend the paper judges by eye rest on readings set in the file.
- **Waveforms:** Waveform classification needs average waveforms, and every V1 claim depends on it. Whether the dataset has them is for the author to find.
- **Conflicting value:** The non-clustered excitatory-excitatory correlation spread is printed as 0.11 in the Fig 1D legend and 0.011 in the S2 Fig legend. Both stay as readings.

**Ready:** yes. The `checks` entry is appended with `ready: true`. Nothing was committed or pushed.
