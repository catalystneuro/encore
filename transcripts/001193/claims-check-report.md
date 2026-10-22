I checked the claims file for DANDI:001193 against the paper, corrected 11 claims, added one, and recorded everything under `checks`. The file is ready for an attempt, with four open problems listed below.

**Checker result:** `claims/001193/10.1038-s41562-022-01334-6.yaml: 25 claims, 25 quotes, 9 statistical values, 0 problems`. The first run, before my edits, gave 24 claims and 0 problems.

**Changes, by claim:**
- **Shared rule for "more than 50 ms" (V1):** added a third reading the words allow, a run of at least 7 consecutive 10 ms samples (spanning more than 50 ms from first to last).
- **behaviour-response-time:** the statement said participants responded fast and accurately; the paper says "most participants" did.
- **fig1b-high-gamma-best-band:** the criterion required high gamma to win under every classifier, kNN included. The paper reports band accuracies only for the SVM (Fig. 1b) and logistic regression (Supp. Fig. 3a), so kNN is now a variant. I also added a test for the ERP part of the statement, using the Supp. Fig. 3d measure.
- **fig1d-only-after-keyword:** the 5% threshold was not from the paper. It is now a claim of absence on the paper's own test: no electrode and condition pair may pass before the keyword. Leaving out the SEM verb period is a variant.
- **fig2c-euclidean-similarity:** reading (b) dropped time, which the Methods' "time-course similarities" does not allow; it is now the time course averaged over electrodes. The criterion judged on the order of distances alone; the expected values must now match under at least one reading.
- **suppfig7a-com-overlap:** noted that 78.3% and 26.1% fit 18 and 6 of 23 electrodes at the smallest, so the tolerance on 26.1% is below one electrode.
- **suppfig8b-individual-no-separation:** removed the "partially reproduced" outcome, which a claim of absence cannot have. The three-electrode minimum is now marked as a standard choice, not the paper's.
- **suppfig9-predict-from-corr:** noted that the kNN settings come from the Methods' frequency-decoding section. Added a second reading of "non-responding electrodes": IFG electrodes outside the responsive set.
- **fig3e-latency-not-location:** named the two readings of the legend's coordinates: MNI y and z, or MNI x and y as printed.
- **suppfig10a-separable-400-700:** added the reading of each violation classified against CORR. Marked the cross-validation as a standard choice, and added the "not reproduced" and "blocked" outcomes.
- **nl-low-frequency:** added the Supp. Fig. 4a measure to the criterion.
- **New claim, fig3-sync-latency-variability:** the main text reports greater variation in SYN-C onsets and peaks than in SYN-P's, and no claim covered it.

**Still open:**
- I could not read the counts in the Venn diagrams (Fig. 2b, Supp. Figs. 6 and 7) because no PDF renderer is available here. The text layer of Fig. 2b holds 21, 6, 20, 2, 1 and 8, which add up to 58 and split into 49 single-type and 9 co-activated, but I can't tell which region each belongs to.
- suppfig7b-not-nonlinguistic still uses a 5% ceiling for "almost completely not", which the paper never puts a number on. Once read, the Supp. Fig. 7b Venn count should replace it.
- fig2b-violation-electrodes and the claims built on it let any reading of the electrode selection and violation tests match, instead of requiring all readings to agree. The protocol allows this when the question is which subset a reported number means. The attempt should report every combination.
- The circuit-size formula in the Methods is garbled in the text layer, and I could not check it against the PDF. r = 0.5 mm / p is the only reading that gives the paper's ~3.25 mm from 9 of 58.

Nothing was committed or pushed.
