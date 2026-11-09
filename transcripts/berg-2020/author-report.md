I've done steps 1 to 5 of the Author section and built the verifier's handover package. `python tools/entry.py all` passes with 0 errors, and the notebook runs from a clean environment in 23.5 minutes. Nothing is committed.

The entry is `entries/000023-berg-2020/`, with the attempt record `attempts/000023-berg-2020-01.yaml` and 7 questions in `questions/000023.yaml`. I pinned version 0.210914.1900 because it is the only published version, the paper cites none, and the draft holds the same files.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| features-and-labels-link | with labels | reproduced, under reading M2 (see 2) |
| cohort-cells | with labels | not reproduced (318 cells, 307 with features, against 385 and 283) |
| cohort-donors | with labels | not reproduced (56 donors, against 90) |
| cohort-type-counts | with labels | not reproduced (2 of 6 counts match) |
| fig3d-depth-by-type | with labels | partially reproduced (no FREM3 cell deeper than 1) |
| fig4e-human-ephys-anova | with labels | partially reproduced (reproduced on the code's 283 cells alone) |
| fig4-glp2r-sag, edfig6-classifier-human-ephys (0.632), fig6c-col22a1-rin-fi-sag | with labels | reproduced |
| fig5c-frem3-ephys-depth (10 and 7 features) | with labels | partially reproduced |
| fig6-deep-ephys-anova (15 and 5 features) | with labels | partially reproduced |
| fig6c-carm1p1-upstroke-rin | with labels | blocked: the two readings of "upstroke" give different outcomes |
| fig4e-mouse-ephys-anova, edtable1-species-ephys, edfig6-classifier-mouse-ephys | with inputs | reproduced |
| fig2ef-pathology-ephys | with inputs | partially reproduced (4.1 mV, against 5 ± 0.5) |
| fig2d, edfig1, fig4f, fig5b, fig6-deep-morph | elsewhere | reproduced |
| fig1b-density, fig1c-soma-area | elsewhere | partially reproduced (human part matches, mouse part does not) |
| fig1a, fig6a, edfig6-classifier-morphoelectric | elsewhere | blocked: methods underspecified |
| fig1c-soma-variation, fig5d, fig1f, fig1g, fig3a, fig6e, fig6f | elsewhere | blocked: other |

## 2. Dataset findings and questions

**Findings:**
- **Missing identifier.** The files carry no SpecimenID, t-type, depth or region. Each file's session id sits 13 to 685 below its cell's SpecimenID within the same donor. Matching on that (reading M2) links all 318 files to distinct cells, and the features confirm it: computed with IPFX, they have a median difference of 0 from the code's table for all 18 features, and matching on features alone picks the same cell in 282 of 282 cases.
- **Undocumented selection.** The dandiset holds 318 of the 385 cells in the paper's table. That includes all 283 cells that have features in the paper's code, plus 25 more that give features here but not in the code; the dandiset does not say why.
- **Metadata errors.** Donor H18.03.318 is female in the files but male in the paper's tables. Donor H18.06.005 is 56 in the files and 57 in the tables.
- **Code differs from the Methods.** The code's feature table computes adaptation, initial firing rate and tau differently from how the Methods describe them, and my recomputed values match the code.
- **Code repository files.** The mouse NeuN section files do not reproduce the values Code7 prints (the human files reproduce Code6 exactly). The gene-depth table comes from the revision, not the preprint.
- **Recordings are sound.** Spike times computed here equal those stored in the files, and no spikes occur in the second before any step.

**Questions asked (7):**
1. The link: match through a stored SpecimenID (matches nothing) or through the session id (M2).
2. Fig1c-soma-variation: which depth bins count as deep L3.
3. Fig1c-soma-area: quartiles pooled across sections or per section.
4. Fig1a: where the mouse whole-cortex thickness comes from.
5. Fig5b and fig6-deep-morph: which method and which morphological features (60, or 58 without the two location features).
6. Fig6a: no method given.
7. Edfig6-classifier-morphoelectric: no method given.

## 3. Where the protocol was unclear, wrong or missing something

1. **Link claim names an identifier the dataset lacks.** The protocol says the author chooses how a link is matched, but here the reader fixed it in a criterion I may not change. I ran both readings, asked, and recorded the outcome under M2, arguing that the feature match makes the choice irrelevant to any outcome.
2. **`elsewhere` claims whose criterion is only "Not tested on the dandiset".** The checker requires testing them or blocking for a reason other than `data_missing`. I tested where a common method from the claims file applied (and asked), and blocked where there was no method.
3. **Data that is public but cannot be pinned** (the Allen RNA-seq portal) has no `blocked_by` category. I used `other`.
4. **Fig6f's images are not public anywhere.** The protocol says such a claim should be `data_missing`, but it is marked `elsewhere`, and the checker forbids that combination. I used `other`.
5. **The only public data is the wrong version** (fig5d, the revision's gene table). No category fits; I used blocked/`other` and put the measured count in the notes.
6. **One of two expected values can't be measured** (fig1a, mouse thickness). The protocol doesn't say whether that is partial or blocked; I chose blocked, methods underspecified.
7. **An outside input proved inconsistent** (the mouse section files). I marked the claims partially reproduced where the human part holds, and blocked the claim that depends only on mouse data.
8. **Streaming.** IPFX only reads a file path or an in-memory buffer, and opening the 318 files with remfile took about 8 minutes just for metadata. I read each file whole into memory instead, never to disk.
9. **Runtime.** The protocol aims for 10 minutes, but the criterion requires 1000-split classifiers (about 14 minutes) on top of about 9 minutes of IPFX. The total is 23.5 minutes, under the 30-minute limit. I cut the shuffled-label reference to 100 splits and recorded that as a deviation.
10. **Which cells to analyse.** The link revealed 25 cells the paper's table lacks features for. The protocol doesn't say whether to restrict to the paper's cohort. I used all cells, as the claims file defines them, and showed the paper's 283 as a variant. Two outcomes (fig4e-human, fig6-deep-ephys) depend on this.
11. **Clock check.** The suggested check (decoding a task variable) doesn't fit intracellular recordings. I used spike counts during the step against the second before it, and compared with the spike times stored in the files.
12. **Labels from another modality.** The `with_labels` definition ("names for codes the dataset holds") doesn't fit t-types and depths measured by other methods. I complied with the checker's requirement for a finding anyway.

## 4. Runtime and failures

- **Final notebook:** 1407 s (about 23.5 minutes): 9.3 minutes of extraction and about 14 of classifiers.
- **Full runs:** two of `entry.py all`, plus two development extractions and one development pass with the full classifiers.
- **Failures:** none. IPFX gives no features for 11 of the 318 files (no spiking or subthreshold steps, or a failed f-I fit), which the notebook reports.
- **Untracked files:** some dotfiles and `scripts`, `.idea`, `.vscode` appear as untracked in the repo root. These are sandbox device placeholders that I did not create.
