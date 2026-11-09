The claims file for DANDI:001642 is now ready for an attempt. I made 15 corrections, listed below. A few points the paper doesn't settle remain open. Nothing is committed or pushed.

**Checker result** (after my edits): `32 claims, 32 quotes, 40 statistical values, 0 problems`

**Changes, by claim**
- **File-wide:** every criterion from the fig. 2 extinction test (`fig2c-extinction-differs`) onward said "Reproduced when, under one reading" where the readings are method choices. The protocol requires every method reading to give the same outcome, or the claim is blocked as `methods_underspecified`. I changed these to "under every reading" and stated the rule in the opening comment. `trial-counts` and `trials-per-block` keep "any reading", because their readings are about what a number counts.
- **Opening note O6:** the Fig. 8 legend says "seven trial events" without naming them. I added two readings: E1 to E7, and E0 to E6.
- **fig2b-extinction-time-course:** the paper doesn't give the interval method. Wilson and Clopper-Pearson are now both readings; before, Wilson alone decided.
- **fig2d-f-decision-trees:** the 10-trial floor was the writing agent's own choice and decided the outcome. With and without the floor are now both readings.
- **fig2g-fq-variable-best:** the statistics said every other model differs from FQ (variable). Which models carry the Fig. 2G marks can't be read, and the entry now says so.
- **actor-critic-near-chance:** the criterion let the author pick the model and judge whether it was acceptable. It now names readings of a regular actor-critic (shared or separate learning rates), fitted and tested as in Fig. 2G, and all readings must agree.
- **neuron-counts:** added that the Results also cite waveforms for classing a neuron as phasically active, but the Methods give no waveform rule.
- **fig4c-activation-duration:** the criterion ordered regions by medians. Fig. 4C and the Discussion use averages, so it now uses means, and it names opening note O3 (which trials are used) alongside O2.
- **fig5g-reward-info:** the statement's "rises in all regions after L/R-hole entry" wasn't tested. Added a test that each region first crosses its shuffle threshold in Phase 6.
- **fig6-event-coding-proportions:** the χ2 entry now says which region pairs carry the significance marks can't be read.
- **fig9-temporal-order-all-blocks:**
  - Any VS crossing before Phase 5 failed the claim, but Fig. 10C reports a brief VS peak during the cue that the paper doesn't count as the rise. The rise is now the start of the sustained rise.
  - Free-choice blocks were held to the fixed-block phases, but the text claims only "this temporal pattern" there. They are now held to the order DLS, then DMS, then VS.
- **fig9-dms-never-above-dls:** it cited a Fig. 10 test "between regions", but the Fig. 10 tests compare block types within one region. It now cites the paper's between-region Mann-Whitney U test from the Fig. 5 results.
- **fig10c-vs-no-fixed-free-difference:** the absence test was tied to "the reading used for fig10a". Every reading of the test must now agree.
- **fig10d-dls-stay-above-switch:** it said the Fig. 10 legend gives "last 20 trials", but only the Fig. 9 legend and Results do. Corrected.
- **no-policy-coding:** applied the every-reading rule.

**Still open** (recorded in `checks`)
- The chance level for the Fig. 8 binomial tests isn't given. Reading it as 0.01 is conservative for the policy-coding test, which needs both QL and QR coded, so it is harder for that test to find an effect.
- The model comparison used 202 sessions (101 training, 101 test), but only 86 recording sessions are reported, and the paper doesn't say where the others come from. The equations are images missing from the text, so those criteria rest on readings of the surrounding words.
- The paper doesn't say whether its Mann-Whitney U tests are one- or two-sided. Two-sided is used, but the results near p = 0.04 (fig4c DLS against DMS, fig10b Phase 3) could depend on it.

All of the paper's main findings have a claim, and every claim comes from this paper.
