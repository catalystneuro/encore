I've done steps 1 to 6: the entry passes `tools/entry.py check` and `all` (notebook runs in 363 s), and the handover is built in `executed/seyedolmohadesin-2026/handover/`. Nothing is committed.

## 1. Outcomes (35 claims)

| Claim | Outcome |
|---|---|
| recordings-animals | reproduced (22 hermaphrodites, 25 males) |
| fig5b-responsive-classes | reproduced (86, or 85 under the code's filters, against 84 ± 8.4) |
| fig5b-dimorphic-classes | reproduced (82 to 86 against 80 ± 8) |
| fig5b-layer-counts | partially reproduced, rests on an assumption (7 of 8; motor dimorphic 15 against 13) |
| fig3-each-stimulus-mixed | reproduced |
| sensory-dimorphic-and-monomorphic | not reproduced, rests on an assumption (21 and 20 of 24, at least 22 needed) |
| layers-sensory-most-dimorphic | reproduced (holds under one of the three readings) |
| fig3a-osmotic-onset, fig2b-bag, fig3a-ash, fig2e-i2, pharynx-dimorphic | reproduced |
| fig3a-aser-salt-concentration | not reproduced (low salt p = 0.055; ASER does not respond to high salt) |
| fig2-awa-awb-nociceptive | partially reproduced (AWA does not respond to CuSO4) |
| fig2-adf-m2-switch, male-specific-unresponsive, figs2f-left-right, figs3e-pattern-robust | reproduced |
| figs2c-aib-state, figs8-state-insensitive | reproduced (all 24 readings agree) |
| fig4c (R2 0.806), fig4-stimuli-sensory, fig4-pharynx, fig4-dimorphism-small | reproduced |
| connectome-link (link claim I added) | reproduced |
| connectome-normalization-sem | not reproduced |
| fig4d, fig4f, figs20 | reproduced |
| figs2e-no-order-effect, figs3fg-state-interneurons, fig4g | blocked: the readings disagree (methods underspecified) |
| tail-unresponsive, figs1-behavior | blocked: data missing |

## 2. The dataset, assumptions, questions

**Dataset findings:**
- **Duplicated trace table.** sub-20220403-h3 and sub-20220403-m3 hold the same 382-row table: h3's traces followed by m3's. I told the two blocks apart from the stimulus orders and the male-specific labels, and counted each animal once.
- **Sex field.** It is "O" in every file; the sex is only in the subject description and the subject id. The strain field is empty.
- **Stimulus times.** They are labelled seconds but hold frame numbers, and lie 1 to 3 frames after the onset frames the paper's code uses.
- **Missing data.** No tail neuron has a trace. There are no identification confidences, which the paper's code uses to select neurons.
- **Blank frames.** Some blocks of frames are blank with no note of why.
- **Neuron count.** The traces cover 189 sex-shared neuron names; the paper says 196.
- **Unpublished code inputs.** The paper's code reads files that are not public: the connectome table, the class-to-layer file, and the spreadsheet of ignored frames and ganglia.

**Assumptions:**
- The layer of each class (24 sensory, 36 inter, 15 motor, 14 pharyngeal), chosen to give the paper's totals.
- How h3's and m3's traces are split.
- The connectomes rebuilt from Cook 2019 and Witvliet 2021, with both of Cook's forms (synapse counts and EM sections) run.

**Questions for the paper's authors** (recorded as findings): the layer assignment; the open details of the motor state from AVA; the test behind Figure S2E; which Cook connectome form was used and over which values the 95% quantile is taken.

**Questions to a reader:** none.

## 3. Protocol issues

1. The claims file says to block a claim when method readings disagree; protocol step 1.6 allows adopting the best-supported reading as an assumption. I followed the claims file and blocked figs2e, figs3fg and fig4g.
2. Readings that I added, such as Cook's two connectome forms, combine with the claims file's readings. The protocol doesn't say how; I required them all to agree.
3. The time limit gives `too_large` for claims stopped by computation, but there is no code for claims not yet attempted. I later found time and tested them, so this did not end up applying.
4. `tools/entry.py check` hung for an hour: a regular expression backtracks badly on a 30-number list literal. I worked around it by writing the list as a string. The hour was lost.
5. `tools/entry.py lock` writes a `python:` field into `entry.yaml` that the schema rejects. I deleted the field after each lock.
6. The handover drops whole markdown cells that start with "**Result:"; nothing says the conclusion must be in its own cell. I split those cells.
7. For a claim the criterion judges only as reproduced or not (fig2-awa-awb, 3 of 4 pairs), I used partially reproduced as the protocol defines it.

## 4. Runtime and failures

About 2 h 40 min of the 5 h. Besides the one-hour `check` hang, my first survey of a file timed out after 10 minutes. Nothing else failed.
