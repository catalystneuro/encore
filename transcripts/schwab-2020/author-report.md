I did steps 1 to 6 for dandiset 000947 and Schwab et al. 2020. The entry passes `check` and runs from a clean environment in 687 s, and the handover is built in `executed/000947-schwab-2020/handover/`. I did not verify my own work, commit, or push. I used the paper's full text: it is open access in PLOS Biology, and I saved the JATS XML and a text copy under `paper/`. I pinned 0.240510.2211 because the paper cites no DANDI version and this is the only published version.

**1. Outcomes**

Of the 18 tested claims, 6 are reproduced, 5 partially reproduced and 7 not reproduced; 3 are blocked.

| Claim | Data | Outcome |
|---|---|---|
| unit-link | with_inputs | reproduced |
| table1-unit-counts | dandiset | not reproduced |
| table1-rest-rate | dandiset | reproduced |
| table1-ap-width | dandiset | reproduced |
| hold-period-ramps | dandiset | partially reproduced |
| mvt-responsive-fraction | dandiset | reproduced |
| increases-most-common | dandiset | partially reproduced |
| monophasic-more-in-vla | dandiset | not reproduced |
| integrated-change-positive | dandiset | partially reproduced |
| fig3a-vla-leads-gpi | dandiset | not reproduced |
| fig3b-gpi-decr-lag-vla-incr | dandiset | reproduced |
| fig3c-vla-decr-lead-gpi-incr | dandiset | not reproduced |
| gating-conflict-fraction | dandiset | reproduced |
| directional-units | dandiset | partially reproduced |
| fig4-ccf-rare | dandiset | not reproduced |
| fig4-noise-corr-rare | dandiset | not reproduced |
| fig5-vla-decrease-after-gpi-bursts | dandiset | not reproduced |
| behavior-rt-mt | dandiset | partially reproduced |
| figs3-emg-onset | elsewhere | blocked: methods_underspecified |
| fig1-vla-localization | dandiset | blocked: data_missing |
| fig6-simulation | elsewhere | blocked: other |

Two outcomes depend on which units are selected. The claims are judged on units chosen from the dandiset's own labels. With the paper's own unit list, monophasic-more-in-vla and fig3a-vla-leads-gpi would meet their criteria.

**2. What the dandiset holds**
- It has the paper's data. 364 of the 394 units the paper analysed are among its curated units. For matched units, activity computed from the dandiset matches the paper's stored per-unit activity (median r = 0.9992).
- It does not say which units the paper used. Its own labels give 268 GPi and 279 VLa units, against 209 and 185 in the paper.
- No identifier follows a neuron across consecutive files. 97 of the paper's units span 2 to 5 files.
- Location labels are inconsistent: GPI/VLA appear alongside GPi/VLa, 54 Gaia units are labelled only "Thalamus", and 33 Isis units have no label and no channel.
- 30 of the paper's units are missing from the curated tables, and 21 pre-MPTP files have no curated units at all.
- In every file, `session_start_time` is two days after the date in `session_id`.
- Error trials are flagged in only 127 of the 253 files with trials, and 87 Gaia files lack movement ends.
- One pre-MPTP file is empty, and one M1 spike train is stored twice.
- The EMG and the stimulation mapping are not in the dandiset.
- The paper contradicts itself: it gives 218 VLa units in the text and 185 in Table 1, and its Fig 3C latencies differ from Table 1.

**3. Where the protocol was unclear, wrong or missing something**
1. **Paper's unit list as an outside input.** The Dryad files list the paper's units, which is a selection, not names for codes. I used it only in a `with_inputs` link claim and in variants. Every claim on the findings is judged on a unit selection rule built from the dandiset alone and fixed in the claims file.
2. **Dryad download blocked.** Dryad's API needs a token. I read the identical deposit from its Zenodo mirror (record 4000719) and recorded that.
3. **No clean null for the clock check.** The protocol does not say what control to use for spikes plus a trial table. Shifting labels by one trial is not a null, because the previous trial's target affects activity. A 1 s offset also fails, because activity while holding at the target depends on the target. I used permuted labels and reported the offset honestly.
4. **Simulation claim category.** The protocol has no data category for a simulation. I set Fig 6 to `data: elsewhere` (its output is on Dryad) and blocked it as `other`.
5. **No partial outcome defined.** For hold-period-ramps the criterion only defined "reproduced". One part holds and one fails, so I recorded it as partially reproduced and noted this as a deviation.
6. **Method error found after a first run.** The first run computed the burst surprise with log10. Bursts came out about ten times longer than the paper's, so I switched to the natural log (MATLAB's `log`). The outcome was not significant in both runs, and the switch is in the deviations.
7. **Control not as stated.** My first burst control did not keep the shifted events in rest periods, though the criterion said it would. I fixed it before writing the conclusions.
8. **Chance level for a reported fraction.** The protocol does not cover a number that matches chance. The paper's 96% gating-conflict figure equals what shuffled onsets give (95.1%). I recorded the claim as reproduced and said in the notes that the number does not tell the data from random onsets.

**4. Runtime and failures**
- The notebook takes about 11.5 min: 3.3 min streaming files, about 3 min reading filtered traces for spike widths.
- The session took about 2 hours.
- Nothing failed in the final run. A Zenodo search command was denied by the permission system; I reran it without the `rm` it included.
- Untracked entries now sit in the repository root (`.bashrc`, `.idea`, `scripts` and others). The three I checked are character devices created at 05:04, before my first command, so they look like sandbox mounts. I left them alone, but they should not be committed.

Files are in `entries/000947-schwab-2020/`:
- `reproduce_schwab_2020.ipynb`
- `gpivla.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

Also new:
- `claims/000947/10.1371-journal.pbio.3000829.yaml`
- `attempts/000947-schwab-2020-01.yaml`
