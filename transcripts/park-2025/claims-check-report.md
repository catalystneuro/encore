The claims file for DANDI:001266 is ready for an attempt. I made 12 corrections, and three problems remain open. Nothing is committed.

**Checker result:** `55 claims, 55 quotes, 20 statistical values, 1 problems`. The one problem is figs24-drugs-selective, p = 0.0005, which the checker reports as not found. The Fig. S24 legend prints it as "5.0 x 10-4", a form the checker doesn't match, so the value is correct and I left it.

**Changes:**
- **Header:** added the protocol's rule for readings. Where a reported number can be read several ways, any matching reading is enough. Where an open method detail has several readings, they must all agree, or the claim is `methods_underspecified`.
- **fig5b-supralinear-auc, fig5d-timing-window, fig5ef-late-efs-no-plateau:** these passed if just one integration window or one fit form matched. Those are method details, so all readings must now agree.
- **fig5d-timing-window:** the statement says amplification was greatest when the stimuli overlapped, but nothing tested it. Added that check.
- **fig3-cheriff-current:** the criterion said the paper gives no method, but the Peer Review File does. The Fig. 3a distal stimulus gave ~69 eYFP counts, which the Fig. S3e calibration turns into ~130 pA. The criterion now follows that and adds the 69 counts as an expected value. How charge becomes current is named as open. Data is now `with_labels`, since it uses the Fig. 3a recording.
- **fig1-denoising-variance:** the statement applied the paper's "> 93%" to the PCA step, but the paper gives it for the whole 2D/3D reconstruction. The pass mark (93%) also didn't match the expected value less its tolerance. The claim now covers only the "> 96%" bound, read as five components (Fig. S7b) or three (Methods), and passes at 86.4%. The quote is now the Fig. S7b legend, and data is now `with_labels`.
- **figs14-low-rate-attenuation:** the criterion called a test of a ratio against 1 a paired t-test. It now compares the first and last spike with a paired t-test and says the test is not the paper's.
- **figs18e-ni-no-effect-on-dspikes:** "the highest concentration each cell received" was the writer's choice, not the paper's. Recordings are now matched to the Source Data values for Fig. S18e, with three readings only if matching fails.
- **figs4-stimulus-localization:** the statement now includes the somatic 20% offset (23 ± 7 µm) and the sample sizes.
- **figs5-focal-selectivity:** the plateau tolerance is now the paper's stated spread (4, from the IQR 7 to 24%) instead of 10%. Which offsets count as the plateau is named as open.
- **figs2-imaging-fidelity:** the paper doesn't define noise-equivalent voltage, so I added a second reading.
- **fig4ce-period-doubling, fig3i-distance-dependence:** the thresholds the criteria invented are now marked as readings, not the paper's numbers.

**Open:**
- **fig5a and figs23:** the plateau duration (fig5a-plateau-collision, ~120 ms) and the persistence (figs23-dendrite-drives-soma, ~300 ms) each use one standard measure. The paper names none, and another measure could change the outcome.
- **Paragraph numbers:** I couldn't check the paragraph numbers given as sources in the Plateau section. The main text is one unbroken line and the main PDF is not under `paper/`.
- **Invented thresholds:** five criteria use thresholds the paper doesn't give. They are marked as readings, but a different threshold could change the outcome. The five are fig2e-f, fig3-two-motifs, fig3-predepolarization, fig4b-few-late and figs15.
