I did steps 1 to 5 of the Author section and ran the handover (step 6). All 39 claims were tested: 32 are reproduced and 7 partially reproduced; none is blocked or not reproduced. `entry.py all` passes (0 errors, notebook runs in 95 s) and the verifier's package is in `executed/wright-2019/handover/`. Nothing is committed.

**(1) Outcome per claim** (A = the outcome rests on an assumed reading)

| Claim | Outcome |
|---|---|
| fig1c-total-suppression, fig1c-nonlinear-scaling, fig1s1b, fig1e, onset-population, ramping-population, fig1s5 | reproduced |
| fig1d-interval-suppression | reproduced (A) |
| fig1s1a-nose-poke-rates | partially (A): baseline rates differ across trial types with the 20 s window, p = 0.017 |
| fig2a, fig2b first and last, fig2c, fig2d first and last, fig2e-rate, fig2s2 | reproduced |
| fig2e-departure-times | partially: danger departure at the Bonferroni threshold is 4.5 to 4.7 s against 5.8 s |
| fig2s1-single-trial | partially: Ramping firing exceeds baseline on 6 of 10 safety trials, the criterion allows 5 |
| fig3-onset-ramping-independent | partially: 3 pairs against the paper's 4; no negative betas |
| fig4abc, fig4d, fig4h | reproduced (4d and 4h only with the within-neuron shuffle) |
| fig4efg | partially: the danger/uncertainty correlation in panel E has p = 0.11 |
| fig5a, fig5i | reproduced |
| fig5bc, fig5d, fig5s1 (Onset), fig5e, fig5s2, fig5f, fig5gh, fig5j | reproduced (A) |
| fig5s1-ramping-regressor-combinations | partially (A): total fear used alone also differs from zero |
| fig6ab, fig6c, fig6d | reproduced |
| fig6ef-beta-correlations | partially (A): 3/20 and 0/20 significant against the paper's 13/20 and 4/20 |

**(2) Dataset, assumptions and questions**
- **What it holds:** 245 units, 88 sessions, 6 rats, 32 trials each, with raw spike times, events and waveforms. The paper's methods reproduce most of its statistics to the printed digits, for example Fig 5D F = 7.16 against 7.16.
- **The example neuron:** one unit (rf03092316 SPK12a) reproduces the regression input printed in the Methods. It does so only with a 20 s poke baseline for total fear, a 2 s baseline for interval fear and 0/0 ratios set to 1. None of these is among the claims file's readings. I used it as the primary reading, ran every reading the claims file names beside it, and marked 12 outcomes as assumed where the readings disagree.
- **Findings recorded:**
  - The data description says `poke.base` is the 2 s baseline, but `cubeScript.m` computes it over 20 s.
  - The script rounds the firing baseline down and uses 20 s for interval suppression ratios, both against the paper.
  - Cue onsets are 132 to 195 s apart, so no ITI reaches the stated 3.5 min mean.
  - Five within-session unit pairs share 66 to 90% of their spikes; one of these units is an Onset neuron.
  - The data set does not mark which units the paper placed in each population.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): the baseline windows and the 0/0 rule, the Fig 4D/4H shuffle, and the Fig 2E departure measure.
- **Question for a reader:** one, in `questions/wright-2019.yaml` on fig1c-total-suppression. It asks whether details 1 and 2 of the claims file should name the windows the Methods table fixes.

**(3) Where the protocol was unclear**
1. The Methods table showed a reading the claims file does not list. The protocol does not say whether an author may add a reading the paper fixes. I ran it as a reading taken from the paper, marked outcomes as assumed where readings differ, and asked the reader.
2. "Record the first reading the criterion lists" in `measured` sits badly with a reading added from the paper. I recorded the table reading and gave the first listed reading's values in the notes.
3. Some criteria give no rule for a mixed result (fig3: count wrong, effect present; fig1s1a: one part fails). I recorded partially reproduced.
4. The data set ships the authors' own scripts. The protocol ranks "code the paper links" but says nothing about code deposited only in the data set. I used it as evidence beside the paper, which takes precedence.
5. The protocol asks to count each recording once, but the overlapping unit pairs are not identical duplicates. I kept all 245 units, as the paper does, and reported the pairs.

**(4) Runtime and failures**
The run went from 10:16 to about 10:54 UTC, well before the 14:31 cutoff. The notebook takes 1.5 min and 0.36 GB at peak. Nothing failed.
