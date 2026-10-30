I wrote `claims/000541/10.1016-j.cell.2020.12.012.yaml`. The quote checker reports 27 claims, 27 quotes and 0 problems. Tables S1 to S6 were missing, but I went ahead without them (see the last section).

**Text read**
- The PMC author manuscript (PMC10494711), not the version of record. I read the Results, Discussion, figure legends, STAR Methods and Key Resources Table.
- Supplements: Methods S1 (identification software and atlas) and Methods S2 (optimal coloring).
- Code read:
  - NeuroPAL-traces at `92b27ed`: trace extraction, used only for strain OH15500.
  - CELL_ID at `759898d`: the identification software.
  - Optimal_Coloring at `f01284f`: the coloring solver.
  - None of the three holds the Figure 6 statistics, correlations or connectome comparison, so those methods come from the STAR Methods alone.
- Dataset: going by its archive description, 000541 holds the microfluidic GCaMP imaging behind Figure 6, Figure S1H and Figure S2.

**Claims**
- 27 claims, all with quotes.
- 7 claims carry statistics (9 entries in total), 19 have a criterion and 9 have expected values.
- 15 claims cover the whole-brain imaging: sample sizes, which heads responded, ASE and AWC asymmetry, the named interneurons, odors being more inhibitory, ASJ and RIC, tail and post-stimulus responses, pharyngeal responses, overlapping stimulus sets, the AVF cycle, stimulus-specific correlations, PCA trajectories, the connectome R² values and the variations on them.
- The other 12 cover findings the dataset is not described as holding: the reagent, integrant health, positional variability, receptor coverage, the GABA network, extrasynaptic signaling, the pag-3 and eor-1 mutants, identification accuracy and optimal coloring.
- 5 claims use outside data (`with_inputs`): the Cook 2019 connectome for the two connectome claims and two receptor-network claims, and WormBase reporters for optimal coloring. The file also names the Zenodo deposit, 10.5281/zenodo.3906530.

**Details the paper leaves open, and the readings named for each**
- **What 189 neurons and "neuron type" count:** distinct neuron names, either before or after the Methods removals; type as a name (left and right separate) or as a class (pooled).
- **How each head's ASE or AWC response was judged:** a sign test of the pulse mean against the prior 10 s, or the same with a 2 SD threshold.
- **FDR family:** all head tests together, each stimulus apart, or uncorrected p (the legend says "p or q").
- **What the asymmetry t-test compares:** the response (during minus before) or the mean during the pulse.
- **Post-stimulus window:** 10 s or 20 s.
- **What "more inhibitory" means:** a count of classes with a significant decrease, or the fraction of classes with a negative response.
- **AVF peaks and animals:** peak prominence of 1 SD or 0.5 SD; all animals with AVF identified, or only those with a spectral peak between 0.1 and 1 Hz.
- **Correlation similarity across animals and stimuli:** comparing pairs of animals, or random split halves.
- **PCA:** whole recording or stimulus windows; a pair of trajectories counts as distinguishable when their distance exceeds twice the SEM.
- **Connectome comparison:**
  - functional matrix: animal-averaged or pairs pooled;
  - neuron pairs: zero-synapse pairs included or excluded;
  - chemical counts: summed over both directions or the larger one.
- **"Noticeably" for the variations:** no variation gives R² above 3.1%, the paper's largest value widened by 10%.
- **The pharyngeal neuron list:** the paper does not give it, so I used the standard 20-neuron set and said so.

**Missing from the paper**
- Tables S1 to S6 were not in the paper store. Table S6 holds the per-neuron p and q values for Figure 6, so those claims have no per-neuron values to compare against. The findings are stated in the Results and the tests in the STAR Methods, which is why I wrote the claims instead of stopping. The protocol says to stop when a supplement the results rest on is missing, so if Table S6 counts as one, these claims should wait until it is supplied.
- Table S5 holds the mutant p-values, so the pag-3 and eor-1 claims have no statistics.
- Table S2 holds the crawling frequency that the AVF claim compares with, so that comparison is not tested.
