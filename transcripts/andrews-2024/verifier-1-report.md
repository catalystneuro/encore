**Verifier report, round 1: Andrews et al. 2024 on DANDI:001132 version 0.241130.1903**

The claims file has 29 claims. The notebook tests one (`table1-cohort`) and treats 28 as blocked. I queried the archive API myself. The version has 69 assets, all `.nwb`, with `variableMeasured` = ElectricalSeries and ElectrodeGroup only. Each asset's participant entry holds only age, sex and species, with no genotype or strain, and each session description is empty. The dandiset's `relatedResource` lists the GitHub repository as "Supplementary code and other data" (HasPart). Table 1 in `paper/` (A 20 M, B 44 F, C 40 F, D 46 F, E 46 F, F 52 F, G 35 M; slices 1A to 12G) matches cell 16's output.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| table1-cohort | partially_reproduced | Cells 5 and 16: 12 slices and 7 patients (patient read from the slice-name letter), 5 F and 2 M, ages 20 to 52, and every patient's age and sex match Table 1. All 8 HcKCR1 slice names are present. No opsin is recorded in the asset metadata or the inspected objects, so "8 HcKCR1 / 2 ChR2 / 2 none" cannot be derived from the data. That meets the criterion's partial clause. See B1. |
| units-per-recording | blocked: data_missing | No units table in any of the 69 files (cell 5; confirmed on the archive). The claims file makes a re-sort a variant that gets no verdict. |
| transduction-range | blocked: data_missing | Histology is not deposited; the archive holds ecephys NWB only. |
| reporter-gcl-pyramidal | blocked: data_missing | Same as above. |
| patch-hckcr1-hyperpolarizing | blocked: data_missing | No icephys data on the archive. |
| simulation-dampening | blocked: other | Data are "elsewhere" (GitHub code). The notebook says NEST 3.4 and NESTML cannot be installed together but shows no attempt or error. "not_runnable" is not an allowed reason code. See B2. |
| fig3a-spontaneous-reduction | blocked: data_missing | The light events can be recovered for 3C (cell 13: 3C-6 has 5 trials with a full pre window), but there are no curated units. The cell 18 threshold-crossing variant decides nothing. |
| physio-bic-reduction-all-slices | blocked: data_missing | No units. No light steps in 5C, 7D or 8D (cell 13). |
| physio-bic-amplitude-unchanged | blocked: data_missing | No units, so no per-spike amplitudes. |
| table2-fr-decrease-physio-bic | blocked: data_missing | No units. Light events exist for 3C only. |
| table2-fr-decrease-0mg | blocked: data_missing | No units, no light events and no condition labels for 9E to 12G. |
| zero-mg-reduction | blocked: data_missing | Same as above. |
| zero-mg-isolated-bursts | blocked: data_missing | The detector is defined on unit population rate. Which file is the 0-mg recording is also not recorded (metadata_insufficient as well). |
| ka-rhythmic-bursts | blocked: data_missing | Same as above, for 0-mg against 0-mg+KA. |
| ka-light-reduction | blocked: data_missing | No units, light events or condition labels. |
| ka-bursts-during-light | blocked: data_missing | Needs unit bursts and light trials; no light steps found in 10F or 11G. |
| ka-theta-coherence | blocked: data_missing | The LFP is in the raw voltage, but the bursts depend on ka-rhythmic-bursts (units), and the 0-mg+KA file of 10F cannot be identified. |
| fig4-firing-propagation | blocked: data_missing | No units. The recording is unidentifiable and the hilar axis needs histology. |
| fig4-theta-propagation | blocked: data_missing | Bursts come from units, the condition file is unidentifiable, and the axis needs histology. |
| closed-loop-bicuculline | blocked: data_missing | No GPIO bit and no units. No light steps in 5C, 7D or 8D. |
| intensity-threshold | blocked: data_missing | No stimulation log, so no intensities, and no units. 3C-1 to 3C-5 look like a sweep (cell 14), but the intensity of each step is not recorded. |
| chr2-increase | blocked: data_missing | No units. No light steps in 4C (cell 13). |
| transduction-not-explaining-response | blocked: data_missing | Depends on the two Table 2 claims, which are blocked. |
| s3-reduction-by-condition | blocked: data_missing | No units, light events or condition labels outside 3C. |
| waveform-clusters | blocked: data_missing | No curated units. |
| waveform-gcl-association | blocked: data_missing | Depends on waveform-clusters. |
| opto-response-clusters | blocked: data_missing | No units, and light trials only for 3C. |
| opto-waveform-association | blocked: data_missing | Depends on the two clusterings. |
| opto-cluster3-profile | blocked: data_missing | Depends on opto-response-clusters. |

Count: 1 partially_reproduced and 28 blocked (27 data_missing, 1 other). No claim states a chance level, so there was nothing to compare.

I checked every blocked claim against the archive. No part of any can be tested on the dandiset under the claims file's main method, because all of them need deposited curated units, histology, patch clamp or external code.

Two partial routes exist outside the dandiset, and the claims file does not adopt either:
- The light-ON statistics could be tested from the per-unit, per-trial rate CSVs that the claims file lists in the GitHub repository (`data/statistics/*.csv`). The archive declares that repository HasPart.
- The waveform clustering could be tested from the saved waveforms and labels in the same repository.

Either would be a test of the authors' derived data, not of the deposit.

### B. Problems

1. [affects a conclusion] `hdmea.metadata` (`paths`) and cell 16 (`opsin_fields`): the search for opsin, virus, genotype or condition fields skips every object under `general/`. That is where NWB stores `virus`, `subject/genotype`, `experiment_description`, `notes`, `pharmacology`, `protocol`, `optogenetics` and `stimulus`. Only `session_description` and four subject fields are read. The archive's participant metadata rules out `subject/genotype` and `strain`, but the other `general/` fields were never checked. If any of them holds the opsin, `table1-cohort` would be reproduced. If they hold medium or drug labels, the reason "conditions not labelled" would be wrong for six claims.
2. [affects a conclusion] Cell 0 (simulation-dampening): the block rests on an install failure that the notebook neither shows nor logs. "not_runnable" is not one of the allowed reasons; it should be `other`. Whether the published `Simulation/simulation.py` can run with some compatible NEST and NESTML pair was not checked.
3. [does not affect a conclusion] Cell 8 (`hdmea.scan`) scans only the first 64-channel group of each file. The finding that light steps exist only in 3C rests on that group. A local artifact elsewhere on the array, for example in 10F, which the paper illuminated for 10 trials, would be missed. No outcome changes, because units are missing anyway.
4. [does not affect a conclusion] `hdmea.light_steps`: a step that splits across two 10 ms bins is missed when neither half exceeds `STEP_MIN`. My synthetic test confirmed this: a 100-count step split 50/50 gave no detection. The 3C steps of 67 to 168 counts, stable across thresholds of 20 to 60, are fine, but the null result for other slices is weaker than stated.
5. [does not affect a conclusion] Cell 18 variant (`hdmea.window_rates`, `compare`):
   - The ON window starts at the onset transient, when about 85% of channels sit at the rail for the first 0.5 s (`rail_on_first_0.5s`).
   - The OFF window starts on the offset artifact.
   - The 5×MAD threshold is estimated per chunk, including those artifacts.
   - So the −88% drops in 3C-1 to 3C-5 and the null results in 3C-6 (−16%, adj p 0.82) and 3C-7 (+6%, adj p 0.87) are artifact-contaminated in both directions. The cell rightly does not use them for an outcome.
6. [does not affect a conclusion] Cell 19: the ON label runs from floor(onset) to ceil(offset). Second 80 of 3C-7, which holds the offset artifact of 7466 crossings, is therefore counted as ON.
7. [does not affect a conclusion] Cell 0: transduction-not-explaining-response is given as blocked "on histology". In the claims file, transduction is an input from Table 2 (`data: with_inputs`). It is blocked only through its dependence on the Table 2 claims.
8. [does not affect a conclusion] Cell 16 compares Table 1 ages and sexes only by printing them next to markdown values, with no programmatic check. I checked them by hand and they match the paper.

The helper functions work on synthetic inputs:
- `light_steps` recovered an onset at 10.00 s and an offset at 20.00 s with the correct amplitudes.
- `window_rates` gave the planted 10, 0 and 5 Hz rates and dropped a trial whose pre window was incomplete.
- `reduce_chunk` detected 39 of 39 planted spikes with no false crossings on noise channels.

### C. What I could not check

- The contents of `general/` in any file: `virus`, `experiment_description`, `notes`, `pharmacology`, `optogenetics`, `protocol`. A cell printing these fields for one file per slice would settle problem 1 and the opsin part of `table1-cohort`.
- The simulation block. Outputs that would settle it: the attempted environment spec and the resolver or build error, or a run of `simulation.py` under the nearest installable NEST and NESTML versions, reported as a variant.
- Light artifacts outside channel group 0. A `light_steps` table over all channel groups for at least 4C, 5C, 7D, 8D, 10F and 11G would show whether light events are recoverable beyond 3C.
- Whether 3C-6 or 3C-7 is the paper's 5-trial 3C recording. Neither the unit count nor the code's file name can be mapped to a file. The channel or electrode configuration of each file compared against the code's recording index (`new_rec_info_index.json`), if the repository records it, would help.
- Whether the step sizes of 3C-1 to 3C-5 (90 to 153 counts) track LED intensity. Plotting step size against the Extended Data Fig. 7 sweep order would show it, though without calibration it could not give mW/mm².
