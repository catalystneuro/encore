# Kauvar, Richman, Liu et al. (2025) from dandisets 001347 and 001326

Tests the findings of [Kauvar, Richman, Liu et al. (2025)](https://doi.org/10.1126/science.adt3971),
"Conserved brain-wide emergence of emotional response from sensory experience in humans and mice", on
[DANDI:001347](https://dandiarchive.org/dandiset/001347/0.250528.0702) (version 0.250528.0702), which
holds the human eyepuff behaviour, the iEEG recordings of the seven included participants with
spectrogram products aggregated across them, and the head-fixed mouse eyepuff behaviour. The mouse
Neuropixels claims are tested on [DANDI:001326](https://dandiarchive.org/dandiset/001326/0.250528.1957)
(version 0.250528.1957), where the paper deposited those recordings.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The mouse behaviour files carry no condition labels, the non-iEEG files do not say which series is
saline, and the CADSS scores, per-channel network labels and bad-channel lists are not in the dataset.
These come from the paper's code record (Zenodo 10.5281/zenodo.14920570), and link claims check
each against the data. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/kauvar-2025-02.yaml`](../../attempts/kauvar-2025-02.yaml).

| Claim | Finding | Data | Outcome |
|---|---|---|---|
| fig1e-human-late-eye-closure-ketamine | In the non-iEEG human cohort, late eye closure normalised by early eye closure is lower during ketamine ... | with labels | Reproduced |
| figs1b-human-early-eye-closure-unchanged | In the non-iEEG cohort, early (reflexive) eye closure does not differ between saline and ketamine (0.84 ... | with labels | Reproduced |
| figs1c-human-late-eye-closure-decrease | In the non-iEEG cohort, late (affective) eye closure alone is lower during ketamine than during saline ... | with labels | Reproduced |
| figs1d-human-cadss-saline-ketamine | In the non-iEEG cohort, dissociation (CADSS) is higher with ketamine than with saline (9.75 against 0.50). | with inputs | Reproduced |
| fig1f-human-subjective-reports | Participants described the eyepuffs as unpleasant under saline, and under ketamine the aversive quality ... | dataset | Blocked: data missing |
| fig2c-ieeg-cohort-selective-affective-decrease | In the iEEG cohort, ketamine reduces the late (affective) phase of the eyepuff eye closure while the early ... | dataset | Reproduced |
| figs8a-ieeg-inclusion-per-participant | Seven iEEG participants met the behavioural inclusion criteria, each showing a significant decrease of ... | dataset | Reproduced |
| figs8b-ieeg-excluded-participants | The other seven iEEG eyepuff participants did not meet the inclusion criteria, each lacking a significant ... | dataset | Reproduced |
| fig2d-ieeg-cadss-reversible | In the 7 included iEEG participants, dissociation (CADSS) rises during ketamine and returns to baseline ... | with inputs | Reproduced |
| figs14g-cadss-correlates-with-affective-decrease | Across participants, the ketamine increase in CADSS correlates with the ketamine reduction of normalised ... | with inputs | Reproduced |
| figs12-erp-not-explained-by-eyelid-closure | Puff-triggered ERPs are much larger than the activity around spontaneous blinks, although eyelid closure ... | dataset | Blocked: data missing |
| figs13-auditory-control-no-response | The brain-wide eyepuff-evoked response is absent in the auditory control, where the device sounds but the ... | dataset | Reproduced |
| figs15-ketamine-spectral-changes-frontal | Ketamine changes spectral power across the brain, with the largest changes in frontal cortex, led by ... | dataset | Not reproduced (assumption) |
| fig2g-nmf-six-factors | Non-negative matrix factorisation of trial-averaged, puff-triggered channel spectrograms yields six shared ... | dataset | Reproduced (assumption) |
| fig2h-factor-network-loading | Factors 0 to 2 load mostly on attentional and somatomotor networks, and factors 3 to 5 mostly on limbic, ... | with labels | Partially reproduced |
| fig2i-ketamine-reduces-factors-1-2 | Factors 1 and 2 are reduced during ketamine and recover after infusion; in the comparison of infusion with ... | dataset | Reproduced |
| fig2j-factor-change-by-network | During ketamine, factor 1 is suppressed in limbic, dorsal attention and ventral attention networks, and ... | with labels | Reproduced |
| fig3b-cluster-test-yeo-networks | Permutation cluster tests find ketamine-altered spectrotemporal clusters in the limbic, ventral attention ... | dataset | Reproduced |
| fig3c-cluster-test-regions | Ketamine alters the eyepuff spectrotemporal response in insula, cingulate, orbitofrontal, posteromedial, ... | dataset | Reproduced |
| figs27-slow-oscillations-with-strong-dissociation | All participants with strong dissociation (CADSS above 10) show ketamine-induced oscillations below 10 Hz, ... | with inputs | Reproduced (assumption) |
| fig6c-human-persistent-activity-reduced | In humans, eyepuff-evoked activity along the persistent (beta band power) dimension falls during ketamine ... | dataset | Reproduced |
| fig6e-human-fast-activity-unchanged | In humans, activity along the fast dimension (0.05 to 0.10 s) is not changed by ketamine (4.12, 4.00, 3.86). | dataset | Reproduced (assumption) |
| figs37c-persistent-reduction-across-bands | The ketamine reduction of the persistent projection holds in every band except broadband LFP, and recovers ... | dataset | Reproduced (assumption) |
| figs37b-fast-unchanged-across-bands | Activity along the fast dimension does not differ across preinfusion, ketamine and postinfusion in any ... | dataset | Reproduced (assumption) |
| figs37a-beta-most-similar-to-mouse | Of the human frequency bands, the beta band power persistent projection is the most similar (highest ... | with inputs | Reproduced (assumption) |
| fig6g-human-timescale-shorter | In humans, the baseline intrinsic timescale of the persistent population is shorter during ketamine (0.09 ... | dataset | Reproduced |
| fig6i-human-coupling-reduced | In humans, beta phase locking among the most persistent sites at baseline is lower during ketamine than ... | dataset | Partially reproduced |
| figs38a-baseline-coupling-not-different | Before infusion, phase locking among high-persistence sites does not differ from that among ... | dataset | Not reproduced |
| figs38b-ketamine-coupling-loss-larger-at-persistent-sites | The ketamine decrease in phase locking is larger among high-persistence sites than among low-persistence ... | dataset | Partially reproduced |
| figs38h-prepuff-coupling-predicts-persistence | Before infusion, single-trial pre-puff beta phase locking predicts post-puff persistent activity (and ... | dataset | Reproduced (assumption) |
| figs35-persistent-dimension-distributed | Participation in the human persistent dimension is spread uniformly across Yeo7 networks, whereas the fast ... | with labels | Reproduced |
| fig1k-mouse-late-eye-closure-ketamine | In mice, late eye closure normalised by early eye closure on the first puff of each trial is lower with ... | with labels | Reproduced |
| fig1l-mouse-dissociatives-reduce-late | Ketamine (50 mg/kg) and PCP (20 mg/kg) reduce late/early eye closure on the first puff relative to ... | with labels | Reproduced |
| figs2bc-mouse-ketamine-early-present-late-abolished | With ketamine, early eye closure on the first puff decreases but remains (0.78 to 0.45), while late eye ... | with labels | Partially reproduced |
| fig1m-mouse-late-closure-accumulates-and-persists | In mice, late eye closure accumulates across a sequence of eight puffs and persists after the last puff, ... | with labels | Reproduced |
| figs2g-mouse-scaling-with-puff-number-not-pressure | Normalised late eye closure rises from the first to the eighth puff at 8, 18 and 28 PSI, but does not ... | with labels | Reproduced |
| figs2h-mouse-dose-threshold | The dissociative effect on normalised late eye closure (eighth puff) is significant from about 35 mg/kg ... | with labels | Reproduced |
| figs5c-mouse-other-drugs-no-disconnection | Buprenorphine and diazepam do not reduce normalised late eye closure, whereas ketamine and PCP do. | with labels | Reproduced |
| fig1p-mouse-anesthesia-abolishes-both | An anaesthetic dose of ketamine with xylazine abolishes both reflexive and affective eye closure. | with labels | Reproduced |
| fig1no-mouse-dissociatives-no-accumulation | Under ketamine and PCP, reflexive blinks remain but affective eye closure does not accumulate or persist; ... | with labels | Reproduced (assumption) |
| figs2l-mouse-repeatable-across-days | Preinfusion eye closure (reflexive, affective, normalised) on days 2 to 5 does not differ from day 1. | with labels | Reproduced |
| figs2n-mouse-no-sex-difference | Male and female mice do not differ in normalised late eye closure, and saline does not change it in either ... | with labels | Reproduced |
| figs2o-mouse-no-anticipation | When a puff in the sequence is skipped, mice do not blink at its expected time, while late eye closure ... | with labels | Reproduced |
| figs4-mouse-reward-seeking-reduced | Eyepuff sequences cause a persistent reduction in licking for a liquid reward that recovers slowly after ... | dataset | Blocked: data missing |
| figs6-mouse-vpm-inhibition-reduces-affective | Muscimol inhibition of VPM thalamus reduces normalised late eye closure (0.60 to 0.11) without changing ... | with labels | Reproduced |
| fig4b-mouse-recorded-affective-reduced | Mice recorded with Neuropixels also show affective eye closure that ketamine reduces. | dataset | Not reproduced |
| fig4hi-mouse-rise-unchanged-decay-shortened | Ketamine leaves the rise times of puff-evoked regional activity unchanged but shortens regional decay ... | elsewhere | Partially reproduced |
| fig4g-mouse-slow-clusters-altered | Ketamine leaves neuron clusters with rapid preinfusion puff responses little changed and substantially ... | elsewhere | Reproduced |
| fig5d-mouse-emotion-dimension-accumulates | In mice, activity along the emotion-like dimension rises and saturates across the eight-puff series and ... | elsewhere | Reproduced |
| fig5e-mouse-emotion-dimension-late-reduced | Along the mouse emotion-like dimension, ketamine leaves the rapid response to the first puff unchanged (0 ... | elsewhere | Not reproduced |
| fig5g-mouse-first-order-model | A two-phase first-order model in which only the persistence time constant differs between preinfusion and ... | elsewhere | Reproduced (assumption) |
| fig6d-mouse-persistent-activity-reduced | In mice, activity along the persistent dimension (1 to 2 s after the puff) falls during ketamine (0.86 to ... | elsewhere | Reproduced (assumption) |
| fig6f-mouse-fast-activity-unchanged | In mice, activity along the fast dimension (0 to 70 ms) is not changed by ketamine. | elsewhere | Not reproduced (assumption) |
| fig6h-mouse-timescale-shorter | In mice, the baseline intrinsic timescale of the persistent population is shorter during ketamine (0.14 s) ... | elsewhere | Reproduced (assumption) |
| fig6j-mouse-coupling-reduced | In mice, baseline pairwise correlation among the most persistent neurons halves during ketamine (0.49 of ... | elsewhere | Partially reproduced |
| figs34-mouse-tone-persistence-reduced | For a neutral tone, mice do not close their eyes; fast tone activity is unchanged by ketamine, while ... | elsewhere | Partially reproduced (assumption) |
| p50-condition-labels-link | The paper's code (analyze_airpuff_p50.py) names which of the two eye-closure series of each non-iEEG ... | dataset | Reproduced |
| cadss-scores-link | The CADSS scores of the paper's code record (data/cadss_across_pts.csv) cover every iEEG participant whose ... | dataset | Reproduced |
| mouse-session-labels-link | The experiment lists in the paper's mouse scripts (code record, mouse_eyepuff/scripts/fig1_*.py) name ... | dataset | Reproduced |
| link-ieeg-yeo-labels | The Yeo7 labels of the code record's anat/pts_ch_labels.pkl apply to the 458 channels of the dataset's NMF ... | dataset | Reproduced |
| ieeg-channel-atlas-link | The channel labels of the paper's code record (anat/pts_ch_labels.pkl) name the dataset's iEEG contacts ... | dataset | Reproduced |

Notebooks (each streams its data; about 40 minutes in all, from 1 min for 01 to 17 min for 04):

- `01_human_behavior.ipynb`: human eye closure (non-iEEG and iEEG cohorts) and CADSS.
- `02_mouse_behavior.ipynb`: head-fixed mouse eye closure under ketamine, PCP and other drugs.
- `03_ieeg_spectral.ipynb`: NMF factors of the iEEG spectrograms and the permutation cluster tests.
- `04_ieeg_cd.ipynb`: human coding dimensions, intrinsic timescale and phase locking.
- `05_mouse_npx.ipynb`: mouse Neuropixels coding dimensions, emotion-like dimension, timescale,
  coupling, clusters and the first-order model, on DANDI:001326.

Helpers: `dandi_io.py` (streaming, pinned versions), `human_eye.py`, `mouse_eye.py`,
`ieeg_spectral.py`, `ieeg_cd.py` and `mouse_npx.py`. Later notebooks on these dandisets can import
them; each docstring says where every parameter comes from.
