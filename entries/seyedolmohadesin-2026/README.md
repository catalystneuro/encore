# Seyedolmohadesin et al. (2026) from dandiset 000981

Tests the findings of [Seyedolmohadesin et al. (2026)](https://doi.org/10.1016/j.cub.2026.08.040)
on [DANDI:000981](https://dandiarchive.org/dandiset/000981/0.260910.1747), which holds whole-head
calcium imaging of 22 hermaphrodites and 25 males during three cycles of ten chemosensory stimuli.

| Claim | Outcome |
|---|---|
| 22 hermaphrodites and 25 males recorded | Reproduced |
| 84 of 89 classes responsive | Reproduced |
| 80 of 89 classes dimorphic | Reproduced |
| Responsive and dimorphic classes per layer | Reproduced |
| Every stimulus has dimorphic and monomorphic classes | Reproduced |
| Nearly every sensory class dimorphic to one cue and monomorphic to another | Not reproduced |
| Dimorphism less present in interneurons, least in motor neurons | Reproduced |
| Osmotic onset: ASER, ASH monomorphic; AWA, AWB dimorphic | Reproduced |
| AWA dimorphic to osmotic stress, BAG monomorphic to high odor | Reproduced |
| ASH monomorphic to osmotic and toxic stress, dimorphic to high salt | Reproduced |
| ASER dimorphic to low salt, monomorphic to high salt | Not reproduced |
| I2 dimorphic to pheromone, osmotic stress and salt | Reproduced |
| Pharyngeal neurons dimorphic to food, salt and pheromone | Reproduced |
| AWA and AWB respond to osmotic and toxic stress | Not reproduced |
| ADF and M2 switch between food and pheromone | Reproduced |
| CEM and MCM predominantly unresponsive | Reproduced |
| Left and right neurons more alike than other classes | Reproduced |
| Dimorphic pattern robust to cycle 1 and per-animal tests | Reproduced |
| AIB's dimorphism differs between motor states | Reproduced |
| Responses mostly insensitive to motor state | Reproduced |
| Functional connectivity similar between sexes (R2 = 0.8) | Reproduced |
| Stimuli correlate most with sensory neurons | Reproduced |
| Pharynx uncorrelated with the rest of the brain | Reproduced |
| Almost all functional dimorphisms below 0.4 | Reproduced |
| Connectome names match the dandiset's (link) | Reproduced |
| Connectome normalization cuts the mean SEM from 1.14 to 0.62 | Not reproduced |
| Functional and synaptic dimorphism uncorrelated | Reproduced |
| Top synaptic pairs show no functional dimorphism | Reproduced |
| Indirect connections do not match functional dimorphism | Reproduced |
| No dependence on stimulus order; state dependence highest in interneurons; top functional pairs not connected | Blocked: methods underspecified |
| Tail neurons unresponsive; behaviour (Figure S1) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Two files (20220403-h3 and 20220403-m3) carry the same trace table, which holds both animals'
traces; the notebook shows which rows belong to which. The connectome claims use the published
connectomes of Cook et al. (2019) and Witvliet et al. (2021), as the paper's merged table is not
public. The layer of each class is read from the column groups of the paper's Figure 3A. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/seyedolmohadesin-2026-01.yaml`](../../attempts/seyedolmohadesin-2026-01.yaml).

- `reproduce_seyedolmohadesin_2026.ipynb`: the analysis. It takes about seven minutes, nearly two of
  them streaming the trace tables.
- `chemo.py`: loading the traces and stimulus annotations, the responses, exclusion and class tests
  of the paper's methods and code, the band-passed correlations, and the connectomes. Other notebooks
  on this dandiset can import it.
