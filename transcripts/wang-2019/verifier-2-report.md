**Verifier report, round 2: wang-2019-01 (doi:10.1113/jp278016, SPARC:212 v1)**

The claims file has 25 claims and the attempt record has 25 outcomes: 11 reproduced, 1 partially_reproduced, 1 not_reproduced and 12 blocked (8 data_missing, 4 not_runnable). Three outcomes are marked `assumed: true`: fig1bc, fig1ef and fig3f.

**1. Outcomes**

| Claim | Agree? | Note |
|---|---|---|
| fig1a, fig1d | Yes | |
| fig1bc (assumed) | Yes | The assumption, that the first 20 s of the Fig. 2 series stand in for the Fig. 1 hearts, is stated and reasonable. The notes now say that rabbit APD80 passes only on the majority reading (cell 18, p=0.13). |
| fig1ef (assumed) | Yes | Same assumption, stated. |
| fig2a partially_reproduced | No, I'd give not_reproduced | The criterion is "reproduced when … all three monotonic … and significant at 60 s" and has no partial rule, unlike fig2d, fig2cf and fig3abc. Partial is arguable under the protocol's general definition. But the reason given for it is false (see §2). |
| fig2d, fig2cf, fig3e, fig4g-5f, fig7f | Yes | fig4g-5f is borderline (p=0.0482, cell 47). |
| fig3abc reproduced | Yes | The criterion asks for "HR rising", which noradrenaline meets: HR stays above time 0 throughout (cell 34, 82.5 bpm at 59.75 s, p=0.023). The record's general rule ("counts a claim reproduced when it holds under any reading") is not in this criterion's text. The outcome stands anyway. |
| fig3d not_reproduced | Yes, by the criterion's rule | It rests on reading (i), APD80 at 10 s p=0.0101 (cell 38). See §2 on the pooled-error support. |
| fig3f reproduced (assumed) | Yes on the letter of reading (a) | The column pairing is stated and is the more plausible choice (4th of 120 assignments, cell 44). The whole effect is present at time 0 (+2.69 ms, p=0.036), and the change from time 0 does not differ at any time (p 0.18 to 0.94). The notes and cell 45 say this plainly. |
| 8 × data_missing | Yes | |
| fig8e, fig8f, fig8ij, fig9 not_runnable | Blocked yes; the reason is not established | "Octave cannot be installed without root" is untested. conda-forge ships Octave as a user-space install, and Octave has `ode15s`. "A Python lock file cannot hold it" describes a choice about the environment, not a property of the code. |

**2. Text checked against the printed outputs**

- **Cell 29:** "The 60 s SD (4.89 ms) is about half of the Abstract's 9.1." Cells 12, 27 and 28 print 4.94. The record has the correct value.
- **Cell 25, and the record's fig2a notes:** "heart rate rises and APD80 and CaTD80 shorten significantly from time 0 at 60 s under every significance reading". The record words it as "hold under every significance reading", and its verifications response says "for all three variables under every significance reading".
  - Cells 23 and 24 contradict this: APD80 at 60 s has Holm-Sidak p=0.1766 and "60 s sig (ii)" is False.
  - The first sentence of cell 25, and the record's own line "APD80 does not (p = 0.18)", also contradict it.
  - This sentence is the stated basis for the partial outcome.
- **Cell 25:** contains the typo "APD80 APD80 falls".
- **Cells 39 and 52 (Summary), and the record's fig3d notes and findings:** they count "APD80 at 25 s (p = 0.036)" as a pooled-error post hoc result.
  - The APD80 repeated measures ANOVA is not significant (p=0.109, cell 38), so under reading (ii) no post hoc comparison follows. Cell 24 gates the same comparison on ANOVA p<0.05 for fig2a.
  - Only the heart-rate comparisons (ANOVA p=0.031) qualify. They rise in 2 of 3 hearts: heart 1 goes from 226 to 224 bpm (cell 7). The paired p at 60 s is 0.24.
  - "The result does not rest on the one unadjusted test" therefore leans on a pooled error with n=3 and no sphericity correction.
- **"SigmaPlot's pooled-error Holm-Sidak" (cells 25 and 39):** the paper names no software (Methods, "Data analysis and statistics"). The phrase should read as a variant, not as the paper's method. My round-1 wording invited this.
- **Record fig2a notes, "APD80 p = 6e-5":** not visible in the outputs, which print 0.0001 at 4 dp. The two are consistent.
- **README:** the fig1bc/fig1ef row ("Reproduced, on the first 20 s…") leaves out that rabbit APD80 holds only on the majority reading. The rest of the README matches.
- **Cell 13, a supporting sentence, not a conclusion:** "In both species the whole-field change … lies in the range spanned by the base and apex changes". One rabbit heart, at −6.6 ms, lies outside both the base and the apex ranges (cell 12).
- **Everything else checks:** the other Result cells, the Summary, the README and the record's notes match the printed numbers. This includes fig3abc, fig3e, fig3f, fig2cf, fig2d (apart from the SD in cell 29), fig4g/fig7f, the 0.75 chance figure, 1.65 to 4.84 ms, and 400.9 against 380.3.
- **My round-1 reasons in the record:** they are restated faithfully, close to verbatim. Two small gaps:
  - My B6 example (rabbit APD80 at 60 s: paired p=0.021 against Holm-Sidak 0.18) is missing.
  - The simulation claims lost my blocked_by "other". They are now recorded as blocked, with "questionable" in the reason.

**3. Round-1 points**

Resolved:
- B3: the pairing evidence and the change-from-time-0 variant were added.
- B4: the notes now carry the substitution and the majority reading.
- B5: the weakness of reading (b) is now in the notes.
- B7, B8, B9, B10: now in the notes.
- C items resolved: raw Fig3 blocks and column B printed; Fig1 sheet printed (no window stated); `revisions/` listed (banner, manifest, readme, no data); instructions printed (Figure 8 only).

Partly resolved:
- B2 / fig3d: there is more evidence now, but the added pooled support is weaker than the record states (see §2).
- B6: the pooled-error variant was added, with no sphericity correction.

Remaining, bearing on a conclusion:
1. fig2a: the partial label rests on a false sentence about APD80 under reading (ii). I still give not_reproduced.
2. fig3d: drop the APD80 25 s pooled result, which follows a non-significant ANOVA. Restate the HR pooled result as 2 of 3 hearts with no sphericity correction. The outcome itself stands on reading (i).
3. fig8e, fig8f, fig8ij, fig9: not_runnable rests on an untested claim that Octave can't be installed. The claims file's "data elsewhere / registration form" still misreads the dataset; the record has passed this to a reader.
4. fig3f: the outcome stays on the letter of reading (a). The criterion does not exclude a difference already present at time 0, which is the only difference the data show.

Minor fixes: the SD in cell 29 (4.89 should be 4.94), the doubled "APD80" in cell 25, and the range sentence in cell 13.
