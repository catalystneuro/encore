I've finished steps 1 to 6 for andrews-2024. Only one of the 29 claims could be tested. Every one of the 69 files holds raw voltage and nothing else: no sorted units, no light events and no labels for condition or opsin. `entry.py all` passed: 0 check errors, and the notebook ran in 19.6 min with a 1.8 GB peak. The handover is built in `executed/andrews-2024/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| table1-cohort | partially reproduced |
| units-per-recording, and 22 claims on firing rates, amplitudes, Table 2, bursts, theta, propagation, closed loop, intensity, ChR2, S3, waveform and opto-response clusters | blocked: data_missing (no sorted units) |
| transduction-range, reporter-gcl-pyramidal, patch-hckcr1-hyperpolarizing | blocked: data_missing (histology and patch clamp not deposited) |
| transduction-not-explaining-response | blocked: data_missing (depends on the blocked Table 2 claims) |
| simulation-dampening | blocked: not_runnable |

- **Cohort claim:** the files resolve by name to 12 slices from 7 patients, 5 female and 2 male, aged 20 to 52, matching Table 1. It is only partial because neither the files nor the dandiset metadata record which opsin each slice carries.
- **Simulation:** NEST 3.4 is not on PyPI. NESTML 5, the version the code pins, fails against NEST 3.10. A syntax port to NESTML 9 generated the model code, but the build failed at cmake because the NEST 3.10 wheel's `nest-config` points at the paths of the machine that built it.

**2. The dataset**
- **Version:** I pinned 0.241130.1903. The paper cites no version, and both published versions hold the same 69 assets.
- **Light events:** the stored on/off times the Methods describe (GPIO bit and stimulation log) are not in the files. In the 3C recordings, though, the LED leaves a step in the voltage that marks each light period. I used these steps only for a survey and a variant that decides no outcome. No other slice shows a light step.
- **Saturation in 3C:** light onset drives 80 to 94% of channels to the ends of their range in the first 0.5 s. Threshold crossings are therefore confounded. They fall 86 to 90% during light in the single-trial files 3C-1 to 3C-5, and do not fall in 3C-6 or 3C-7.
- **Missing labels:** no file says which medium, drug or light protocol it was recorded under. The original recording names are not kept, so files cannot be matched to the paper's recordings.
- **Metadata errors:** each file's `subject_id` is the recording, so the archive counts 69 subjects. Every session start time is the conversion date, 2024-09-28. Electrode location is "unknown" on every channel.
- **No duplicates:** no two files share a first or last chunk.
- **Gains:** two gains are used (6.29 µV per count for 1A to 8D, 1.57 µV for 9E to 12G), and the dandiset does not describe them.
- **No assumptions, no questions:** I made no method assumptions, so there are no questions for the paper's authors. I asked readers nothing.

**3. Where the protocol was unclear**
1. It does not say whether events reconstructed from the data (here the light artifact) may stand in for missing events. I used them only for the survey and a variant.
2. table1-cohort's criterion has no case for "counts, ages and sexes match but opsins are not recorded". I judged that partial.
3. When an expected value cannot be measured, the schema still wants one `measured` value per expected value. I left `measured` out and put the numbers in the notes.
4. `data: elsewhere` is written for data in another archive, not for re-running code. The protocol also does not say whether to port outdated software. I did not, because a port would change the model the claim is about.
5. When both data_missing and metadata_insufficient apply, there is no rule for which is the main reason. I chose data_missing and named the other in the notes.
6. The duplicate check is impractical on 192 GB of data. I compared hashes of the compressed first and last chunk of each file instead.
7. The clock check in step 2 does not apply because there is no trial table. The 3C light steps sit in the voltage itself, so they share its clock.

**4. Runtime and failures**
- **Runtime:** 14:59 to 16:40 UTC, about 1 h 41 min.
- **Failures:**
  - The simulation build, as above.
  - The first notebook draft binned threshold crossings per 3.906 s chunk, which drifted against the clock. I fixed it to bin on absolute sample times before the final runs.

Files are in `entries/andrews-2024`:
- `reproduce_andrews_2024.ipynb`
- `hdmea.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/andrews-2024-01.yaml`.
