I made 10 changes to the claims file, including one new claim, and marked it ready. Five open problems remain, listed below. Nothing is committed or pushed.

**Checker result:** `claims/001847/10.7554-elife.109717.yaml: 39 claims, 39 quotes, 13 statistical values, 2 problems`. Both problems are the checker missing values the paper prints as "2.0 x 10-4" (supp1c-wplus-blocks-longer) and "6.0 x 10-4" (supp1d-faster-response-wplus). I read both in the supplement legends and they are correct. All 39 quotes pass.

**Changes, by claim:**
- **fig1e-context-off-no-discrimination:** For a claim of absence, the protocol judges on the paper's test alone. The only test in the paper or its code is the code's supplement 1E test, so it now decides, per transition direction. The W+ against W- t-test, which neither the paper nor the code runs, is now a variant.
- **fig1k-model-accuracy:** Added that the Methods say "all expert sessions", but the orofacial features exist only for sessions with face video. The code's list of 60 sessions settles the set.
- **fig2d, fig2e-whisker, fig2f, fig3e, fig4b-wminus:** These said "reproduced under a reading", so any single threshold, null, order or test reading could decide. These details can change the outcome, so all readings must now give the same outcome, otherwise the claim is blocked as `methods_underspecified`.
- **fig3h:** Both readings of the 20 ms exclusion, and every baseline reading, must agree.
- **fig2e-rsc-tjs1-increase-wminus, fig2f:** The file treated the RSC site as open. The Methods fix it at 1.5 mm posterior and 0.5 mm lateral, and the tracing used the same coordinates, so the site is (-1.5, 0.5) and (-0.5, 0.5) is a variant.
- **fig3c-jaw-onset:** Either onset rule could decide. The Methods' rule (d' ≥ 1) now decides and the code's rule (3 SD) is a variant, since the Methods come first.
- **New claim, fig2cd-rsc-no-effect-catch-auditory:** The Results say RSC inhibition in catch and auditory trials did not change performance, and no claim covered this. It is judged as a claim of absence on the opto-map d'.

**Still open** (the paper gives no measure, so these cuts are the first reader's, not the paper's):
- **fig2c:** "little effect" is counted as at most 3 of 39 sites.
- **fig4c and supp4d:** a decrease is a drop below control by more than the control SD over mice.
- **fig4d:** closeness is measured as mean squared distance on PC3.
- **supp2-muscimol:** the "non-significant positive trend" is read as 0.05 ≤ p < 0.1; the 0.1 bound is not the paper's.
- **fig1f and fig1h:** the gradual-adaptation rule and the anticipation tests are readings of statements the paper never tests.

**Ready:** yes, `ready: true` in a new `checks` entry dated 2026-10-21, with one line per change and per open problem. The attempt should record the open items as deviations.
