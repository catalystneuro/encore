I corrected 9 of the 29 claims in `claims/wang-2025.yaml` against the paper and added a check entry. The file is ready for an attempt.

**Checker result:** `claims/wang-2025.yaml: 29 claims, 29 quotes, 44 statistical values, 1 problems`. The one flag is `fig2b-area-ordering 2.8e-08`. The checker writes the number as 2.8e-08 and never tries the paper's printed form "2.80e-08". That value is in the Extended Data Fig. 3 legend. Before my changes the checker also reported one problem, the striatum p in edfig6, which is now fixed.

**Changes, by claim:**
- **fig2b-area-ordering:** the thalamus entry claimed 8.26e-09 was the largest of its three p-values. The largest is ALM against thalamus, 2.80e-08. I split the two grouped entries into the seven pairs, each with its printed p.
- **fig2e-method-improvement:** the criterion used the code's explained-variance threshold (0.005) as the main reading and the Methods' 0.01 as the variant. The protocol puts the Methods first, so I swapped them.
- **fig3f-thalamic-nuclei:** I removed a statistic, "p < 0.1", which is only the cutoff for which pairs Extended Data Fig. 4 displays, not a result. I also removed the requirement that VAL be lower than PO, VM and VP, because no text or legend states it.
- **thalamus-ev-not-rate:** "VAL lowest of the four" became "VAL highest or lowest", with the direction reported. The text says only that VAL differed from PO, VM and VP.
- **fig4b-medulla-leads:** area curves are now averaged within each session, then over sessions, as the Fig. 4b legend and Methods (Data pooling) say. Averaging over all pooled neurons is kept as a variant.
- **edfig6-offset-ev-correlation:** the striatum p is printed in the legend as "3e7", a misprint. I recorded the main text's P < 0.001 in its place. I removed a made-up rule that an R within 0.03 counts as a match. R values and counts outside tolerance now give "partially reproduced".
- **fig5a-somatosensory-vs-alm:** I added the Bonferroni correction, which the Fig. 5 legend states.
- **fig7d-alm-midbrain-vs-medulla:** the threshold now reads "exceeds 0.65", as in the Methods, not "at least 0.65". Counting every neuron above threshold, including those above it for both AUCs, is named as a variant.
- **supp-session-independent-autoencoder:** the quote's "..." joined the training-session clause to the held-out number (12.8%, n=192). It now gives both: training 3.6%, n=122, and held-out 12.8%, n=192.

**Still open:**
- **Choice decoder (Figs. 6 and 7):** the paper does not describe it and its code is not public, so the criteria list possible readings.
- **Direction of the VAL difference in Fig. 3f:** only the supplement PDF was supplied, not the main-text figures, so I could not see it.
- **Rules not from the paper:** a few criteria set thresholds of the file's own where the paper gives none (fig5-significant-offsets, edfig10-subtraction-consistent, fig4b-medulla-leads). Each criterion says so.

Every main finding has a claim, and every claim comes from this paper or its supplement. Nothing was committed.
