## Claims check for DANDI:000541 (NeuroPAL, Cell 2021)

**Checker result:** `27 claims, 27 quotes, 7 statistical values, 0 problems`. Before my edits it was the same with 9 statistical values; I removed two.

**Changes, by claim:**
- **fig6-sample-sizes:** The file justified the exact head and tail counts as "counts of files the paper lists", but the paper lists no files, so I reworded the reason. I also cited the Figure 6 and S2 legends ("between 189 neurons") as support for reading (a).
- **fig6-all-heads-responsive:** The statement said "all 21 head recordings" responded. The STAR Methods instead describe a selection ("21 heads responded to all three stimuli") and never say how many heads were recorded. The statement now says 21 heads were kept, and the criterion asks for 21 heads that pass.
- **fig6d-ase-nacl and fig6d-awc-asymmetric:** I removed the unpaired t-test entries (p < 0.05). The paper reports no result of an asymmetry test, so that number was the Methods significance threshold, not a finding. The tests in the criteria stay.
- **fig6-tail-responses:** The source now includes Table S6. The paper names all five classes (LUA, PVN, PVQ, PVR, PVW), but the criterion only needed "at least three". It now needs all five, and three or four count as partial.
- **fig6f-pharyngeal:** The paper gives only the count of 20 pharyngeal neurons. The criterion now says the list it uses comes from outside the paper.
- **figs1h-avf-cyclic:** Added that the Figure S1H legend shows traces from five worms.
- **fig6-connectome-variations:**
  - Named a conflict: the Figure S2 legend says "N > 5, 10, 15 neurons", while the STAR Methods say N counts worms.
  - Said that using Spearman for "ranked correlation" is a standard choice the paper does not specify.
  - Said that the 3.1% cut-off for "noticeably" comes from the file, not the paper.
- **fig2-positional-variability:** The source now points at the Figure 2 legend, which is where the OLLR sentence is.
- **fig4e-extrasynaptic:** Added a criterion with two readings. The paper's "respectively" sentence pairs GAR and MGL with the wrong transmitters, so one reading follows the expected pairing and one follows the text as printed.

**Still open (recorded in `checks`):**
- The paper's threshold is "p or q ≤ 0.05", but the schema has no "≤", so it is stored as p < 0.05. There are no per-neuron p or q values because Table S6 was not in the paper store.
- Three judgement rules come from the claims file, and the paper gives no test for any of them. Each is marked as open:
  - "noticeably" in fig6-connectome-variations
  - "distinguishable" in figs2a-pca-trajectories
  - "similar" and "distinct" in fig6gi-stimulus-specific-correlations
- In fig7bc-id-accuracy, "above 90% with eight manual annotations" appears in the statement but not as an expected value.

The paper's main findings each have a claim, and every claim comes from this paper.

**Ready:** yes. The `checks` entry is added with `ready: true`. Nothing is committed.
