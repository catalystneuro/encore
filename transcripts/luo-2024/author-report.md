I finished steps 1 to 5 and ran the handover. Of the 29 claims, 4 are reproduced, 11 partially reproduced and 3 not reproduced; 11 are blocked because the morphology is not in the dataset and 1 because the paper does not say how its UMAP separation was judged. The verifier package is in `executed/001261-luo-2024/handover/`. Nothing is committed.

The entry is `entries/001261-luo-2024/`: the notebook, the helper `nbmsi.py`, the README, `entry.yaml` and the lock files. The record is `attempts/001261-luo-2024-01.yaml`. I pinned 0.250917.2023, the only published version: the paper cites no version, and the draft has the same 152 files.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| sample-sizes | partially reproduced (mouse noncholinergic: 45 distinct recordings, paper says 46) |
| fig2-mouse-c-nc-15-of-18 | not reproduced (11 or 12 of 17 differ; 13 to 15 needed) |
| fig2d-mouse-max-firing-rate | partially reproduced (p = 1e-12; both means just below tolerance) |
| fig2d-mouse-threshold-rheobase | partially reproduced (rheobase p = 0.0023, paper says < 0.001) |
| fig2d-mouse-ahp | partially reproduced (amplitude holds; width reversed under the Methods' window) |
| fig2d-mouse-adaptation | reproduced (only when measured on the step with the most spikes) |
| fig2d-mouse-passive | partially reproduced (tau effect present, means far above the paper's; resting potential not recorded) |
| figs2-2-mouse-amplitude-cv-sag | partially reproduced (sag does not differ) |
| fig2c-mouse-umap-separation | not reproduced (6 to 9.5 neurons on the wrong side, paper says 2) |
| fig5a-mouse-lda-electrophysiology | reproduced |
| fig5b-mouse-lda-ahp-amplitude-top | reproduced |
| fig7d-macaque-more-excitable | partially reproduced (macaque max rate 21.2 Hz, paper 26.3) |
| fig7d-macaque-threshold-ahp | partially reproduced (AHP width does not differ) |
| fig7-macaque-spike-width | partially reproduced (p = 0.025, paper says < 0.01) |
| figs7-1-macaque-amplitude-cv-sag-upstroke | partially reproduced |
| fig7-macaque-mouse-feature-count | not reproduced (12 or 13 of 17) |
| fig7d-macaque-input-resistance | reproduced |
| fig7c-macaque-mouse-umap-separation | blocked, methods underspecified |
| 11 morphology claims (Figs. 4, 5C, 9, 10, S4-1, S9-1) | blocked, data missing |

**2. The dataset, assumptions and questions**

- **Groups:** each file holds one neuron, and its group is in `session_description`. The file counts are 48/46/46/12, from 27 mice and 9 macaques, with the paper's sexes.
- **Duplicates:** one mouse recording is deposited twice, once as cholinergic and once as noncholinergic. I counted it once, as cholinergic, because its name says G+. One macaque noncholinergic recording is also deposited twice.
- **Wrong scale:** one macaque file's voltage is 20 times too large. I left it out.
- **Non-responding neurons:** eight neurons (six mouse cholinergic) do not depolarise with positive steps and fire no spikes. I kept them; results without them are shown as a variant.
- **Metadata:**
  - The stimulus is labelled amperes but holds pA.
  - The amplifier fields hold one placeholder value in every file.
  - The step amplitudes and durations differ from the paper's 10 pA increments and 500 ms.
  - Two files in mouse CG608's folder are named for CG609.
  - The 46 macaque cholinergic neurons come from 6 of the 9 macaques.
- **Missing:** the resting potential is not recorded, except in 63 of the 152 file names, so the counts are out of 17 features. Quality-control measures, slices and morphology are not in the dataset.
- **AHP:** the paper's code gives all four mouse AHP means within 10% of the paper's values; the Methods' window, which the claims file makes decide, does not. I recorded this as a code mismatch.
- **Assumptions:** for the AHP width under the Methods' window I searched to the end of the step and also ran the other reading; both give the same outcomes, so no outcome is marked as resting on an assumption. Where an amplitude was recorded more than once I used the first sweep; the last sweep changes nothing.
- **Questions for the paper's authors** (in the record):
  - Which AHP window produced the reported values?
  - What is "the maximal current step" for adaptation and CV?
  - How was UMAP separation judged?
  - Where was the resting potential measured?
- I asked a reader no questions.

**3. Where the protocol was unclear**

1. Several criteria do not cover a test that holds only at a weaker p, or one test holding while another reverses (spike width, AHP, passive). I applied the protocol's definition of partially reproduced and said so in the notes.
2. `archives.md` says to stream with `remfile`, which took 11 minutes just for metadata. I read each file whole into memory over HTTP instead (22 s, nothing written to disk).
3. Step 1.2 says to count a duplicate once, but not which label to keep when the copies disagree. I used the label in the file's name.
4. `measured` needs one number per expected value, but the resting potential cannot be computed for the paper's neurons. I gave the values from the file-name subset and said in the notes that they do not decide.
5. The protocol says nothing about excluding recordings that are clearly broken. I left out the wrongly scaled file and kept the non-responding neurons, with a variant without them.
6. The clock check has no recipe for current clamp without a trial table. I compared the voltage change at the stimulus onset with the same windows shifted 50 ms earlier.
7. The Methods-before-code rule decides outcomes even where the code clearly matches the paper's numbers (the AHP). The protocol's only route is a finding, so I recorded one plus a question for the authors.
8. The UMAP and LDA criteria say "F1 to F18" while F1 is missing. I used 17 features.
9. Provenance: I wrote the harness as "Claude Code", as the prompt says, not the "Claude Code (GitHub Actions)" of the example record.

**4. Runtime and failures**

The run took about 50 minutes, 12:50 to 13:38 UTC. The notebook runs in about 2 minutes, and `entry.py all` reported 0 errors and a pass. Two sandbox artefacts were left: an empty harness folder `entries/001261-luo-2024/.claude/.cc-writes`, which I could not delete because the command needed approval, and some untracked placeholder files at the repository root (`.idea`, `scripts`, dotfiles) that I did not create. Neither should be committed.
