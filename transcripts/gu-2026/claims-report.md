I wrote the claims file at `claims/001836/10.64898-2026.05.26.727951.yaml`. The quote checker passes: 29 claims, 29 quotes, 82 statistical values, 0 problems. Nothing was committed.

**Text read.** The bioRxiv preprint, version 1 (posted May 27, 2026), main text and legends, with its supplement (media-4.pdf). The supplement holds the Materials and Methods and the legends of Figs S1 to S12. I opened the PDF once, for page 4, to read the trial-count table in the Figure 1E inset, which the text extraction scatters. Movies S1 to S3 and Table S1 were not supplied; no claim rests on them.

**Code read.** The paper links `shijiegu/Gu2026_docker` (commit 910c547), which points to the analysis package `shijiegu/Gu2026` (commit 0f0c9a7, the Zenodo record the paper cites). The notebooks that run the figures, with their printed outputs, exist only inside the Docker image, so I did not read them. The opening comment lists six choices the code settles and the claims follow:
- the COM threshold is 0.1 of an arm's length;
- sessions with fewer than 20 trials are left out;
- the "mixed" models are plain fixed-effect Logit or OLS fits with one indicator per rat;
- how correctness and initial-choice correctness are defined;
- which arm pairs count as same-side;
- how a nearby control trial is drawn.

**Claims.**
- **Quotes:** all 29 claims have one; none needed an `inferred` note.
- **Statistics:** 23 claims record them.
- **Criteria:** all 29 have one.
- **Expected values:** 15 claims have them, with tolerances from the paper's confidence intervals or 10%.
- **Coverage:** behaviour (learning, trial and COM counts, side bias, correction, multiple COMs); decoding before and after stopping (Fig 3B to D, S6); ripples and theta (S7B, S8, S10); correctness (Fig 4A, 4B, S11B); home coupling, number of remote arms and next-choice prediction (Fig 4C to E, S11A, S11C); arm-end bias (Fig 5A, S3); head angle (Fig 5B).
- **Data:** every claim uses the dataset.

**Details left open, and the readings named:**
- **COM threshold:** 10 cm (Methods) or 0.1 of arm length (code). Also whether sessions under 20 trials count toward the trial totals.
- **Sequence per rat:** the Results, Fig 1B and Fig S1E disagree on which rats had which sequence, so it is to be read from the reward log.
- **Day of peak performance:** read as the day of highest sequence conformity.
- **Intercept with all five rat indicators:** these are collinear, so the model is fit either without an intercept or with four indicators.
- **Fig 1D:** "initially" (first day, or first two days); the unspecified logistic model of the day effect; how the final ratio of about 1.5 is pooled.
- **Fig 3B:** the pre-stopping window (arm entry to stop, or 5 s); whether the 0.2 posterior filter applies; distance alone or distance plus speed in the COM-prediction model.
- **Fig 3D:** one-sided (code) or two-sided test.
- **Fig 4A and 4B:** correctness per COM event (Methods, used for the main result) or per trial (code, kept as a variant).
- **Fig 4C:** how the "number of remote outer arms" enters a Fisher test (three readings).
- **Fig S11A:** proportion of COM trials with remote content, or number of events per COM.
- **Fig S11C:** which time bins count, and whether a speed limit applies.
- **Fig 5A:** how the proportion is normalized; the pooled model is not in the code.
- **Fig 5B:** the angle per event (mean, onset, or every bin). The text says three rats had gyroscopes while the Methods list four; the claim tests M, J and K, the rats the figure shows.
- **Fig S7B:** the time windows and the reference level of the model.
- **Fig S3:** the reference bin.
- **Fig S10:** which theta source and which z-scoring.
- **Fig S8:** the paper gives no test, so a Rayleigh test is fixed here.

**Gaps and inconsistencies in the paper:**
- Fig 4A(b) and Fig 4B print the same estimate and interval (1.50, 1.18 to 1.90). This may be a copying slip; each is tested as printed.
- The event counts printed for Fig 4E do not match the remote counts of Fig 4A, and the paper does not explain why.
- The p-value for the Fig S3 animal bin is printed "p < 10e-24" and is recorded as 1e-23.
- The camera rate is given as both 23 Hz and 28 Hz.
- No figure's numbers were missing in a way that blocked a claim. The notebook outputs that would settle several of the open details above could not be read.
