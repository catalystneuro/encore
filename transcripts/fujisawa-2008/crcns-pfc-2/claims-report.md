I wrote the claims file `claims/crcns-pfc-2/10.1038-nn.2134.yaml`, and the quote checker passes it with no problems. The file has 30 claims. All 30 have quotes, 30 have criteria, and 1 has a statistics entry: the permutation test, p < 0.01, for where left and right running paths separate.

**Text read:** the version of record (main text, Methods, figure legends) and the supplement (Supplementary Note and the legends of Supplementary Figures 1 to 16). Nothing the results rest on is missing. The paper links no analysis code; its only link is to the KlustaKwik spike sorter. The data description was read only to see what the data set holds: three of the paper's four rats (EE, FF, GG), with session EE.188 named as the one used for Figures 2A and 3D.

**What the claims cover:**
- Counts: unit count, task performance.
- Population activity: firing synchrony and how widely each neuron fires along the maze, by layer.
- Behaviour: where running path and head direction differ between left and right trials.
- Left/right selectivity: in the side arms and central arm, odor selectivity and its independence from stem selectivity, coding of the previous trial's reward side.
- Connections: counts, cell-type fractions, pyramidal-to-pyramidal connections, the Figure 3b and 3d session counts, connection probability against distance, the 1 to 2% rate for nearby pyramidal-interneuron pairs, and the left/right selectivity of connected cells.
- No spatial clustering of left- and right-specific cells.
- Position-dependent transmission: 67 of 343 pairs, 15 of 36 in one session, the example pairs of Figures 4 and 5, and the thinning control.
- Figure 6 depression and facilitation (12.7%, 10.7%) and its examples.
- Figure 7 supralinear effect of coincident inputs.
- No correlation with running speed; population vector correlation widths.

**Details the paper leaves open, with the readings named:**
- **Cross-correlogram bin width:** 1 ms or 0.5 ms.
- **Narrow-peak rule (2 ms or less):** the global-band test alone, or also requiring the run of bins above the pointwise band to span 2 ms or less.
- **Which spikes are jittered:** the Methods jitter every spike of both neurons; jittering one neuron (as Supplementary Figures 9 and 12 say) is a variant.
- **Units with both a peak and a trough:** left unclassified, or excluded.
- **Error trials:** correct trials only, or all trials.
- **Number of label permutations:** not given; the 1,000 used for jitter is taken as the standard choice.
- **Sessions:** the two example sessions, or all sessions by layer. This applies to synchrony, connected-cell selectivity and population vectors.
- **Firing width:** which PSTH (all trials, left and right separately, or the condition with the higher peak), and whether the width is the run around the peak or the total length above 50%.
- **Path variable for left/right separation:** lateral coordinate, or distance from the mean path.
- **Side-arm counting:** a significant segment overlapping positions 0.5 to 1, or the global band broken within that range.
- **Odor test:** Student's or Welch t-test.
- **Denominators:** for reciprocal pairs, for pyramidal-to-pyramidal connections (all pairs or pyramidal pairs), for depression and facilitation (343 or 495 pairs), and for the pyramidal/interneuron ratio (per session or per rat).
- **Position dependence:** left and right trials separately or pooled, and any significant region or a significant region plus a non-significant one.
- **Depression/facilitation measure:** peak height as the largest bin or the sum over 1 to 4 ms, and whether later spikes must belong to a train that began after 200 ms of silence.
- **Supralinear effect:** above k times the single-spike probability, or above 1 − (1 − p1)^k.
- **Thinning region:** positions 0.2 to 0.5, or a region chosen per pair.

**Criteria with no basis in the paper:** where the paper gives no test or definition, I fixed a test or threshold myself and marked it as a standard choice, not the paper's. This covers "relatively constant", population uniformity, "small fraction" for previous-trial coding, odor/stem independence, no clustering on the probe, no speed correlation, "steady" rates, and "toward the end of the right arm".

**Missing from what was supplied:** the PDF pages could not be rendered here, so numbers and significance marks shown only inside figure panels were not read (Figures 2b, 2d, 2e, 3e, 3f, 7b and the supplementary panels). Figures 2d (firing rates, t-test marks) and 2e have no claim for that reason. The paper's counts cover four rats, while the data set holds three.
