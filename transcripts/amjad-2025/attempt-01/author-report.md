I did steps 1 to 6 for dandiset 002013. The entry `entries/002013-amjad-2025/` passes `check`, runs from a clean environment in 2.0 min (130 s under the tool), and the handover package is in `executed/002013-amjad-2025/handover/`. I did not verify my own work, commit or push.

The paper's full text is open access (PMC12183687, CC-BY) and was used; it is saved under `paper/`. I pinned 0.261012.0921, the only published version, because the paper cites no DANDI version.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| insertion-yield | Blocked: data_missing |
| chronic-duration | Blocked: metadata_insufficient (no implant dates) |
| fscv-waveform | Partially reproduced: lowest potential is -0.347 V, the paper says -0.4 V |
| ephys-acquisition | Reproduced (high cut is 8000 Hz, inside the 10% tolerance of 7500) |
| shape-task-structure | Reproduced (24.4% forced trials; complete blocks of 71 to 273 trials) |
| zenodo-link (with outside data) | Reproduced (trial lists agree for 99.8 to 100% of trials; beta trace r = 0.943) |
| fig3a-dual-channel | Blocked: data_missing (site c8ds is not in the dandiset) |
| fig3a-redox-peaks | Blocked: metadata_insufficient (raw FSCV cannot be placed on the trial clock) |
| fig3b-beta-bursts | Reproduced (p = 9.5e-10; the direction of the change depends on the threshold) |
| fig4a-dopamine-reward | Reproduced, weakly (p = 0.023; not in the stored `da`, nor in the second half of the trials) |
| fig4b-beta-reward | Reproduced (p = 1e-08, only in the 0 to 0.5 s window) |
| fig4c-beta-side | Reproduced (p = 1.6e-06) |
| fig5a-spike-reward | Blocked: data_missing (no events for Monkey P) |
| fig5bc-unit-isolation | Reproduced (0.003% of intervals under 1 ms; trough 5.7 times the noise) |

**2. What was found about the dandiset**
- **Events and trials:** each event is stored about five times, once per overlapping 60 s trial window. The trials tables hold no conditions, so I decoded them from the event codes. The 09/13 session has no small-reward code; codes 35 and 36 turn out to code reward size, which their labels do not say.
- **Trial-aligned FSCV:** it covers only the first 734 of 1468 trials, its columns have no units, and `da` is not referenced at the value cue as the Methods say.
- **Raw FSCV:** it is labelled amperes but holds values of about ±1500. Its scan times are an exact 0.1 s grid starting at the first trial. It matches the stored traces at no offset anywhere in the record and shows no reward contrast at the stored times.
- **09/26 ephys:**
  - The bipolar LFP's conversion factor is wrong; the values are already in volts.
  - The raw series starts at 0 s but lines up with the LFP only 9831.35 s later on the trial clock, consistently across trials (r 0.92 to 0.98).
- **Monkey P:**
  - Its spike times are 6800.666 s ahead of its raw signal's clock.
  - Its units table merges the unsorted and poor-quality spikes into "unit 0", and the poor-quality spikes are not in time order.
  - It has no trials or events.
- **Metadata:** the site is `cl3` in the file and `c33` in the paper, and the files cite the preprint instead of the article.
- **Match with the paper's Zenodo files:** the trial selections decoded from the events match the paper's own lists exactly, except the last trial (1501).

**3. Protocol gaps** (numbered; each with what I did)
1. There is no `blocked_by` reason for "the data are there but the stated timing is wrong". I used `metadata_insufficient` for fig3a-redox-peaks and also recorded a `metadata_error` finding.
2. The protocol does not say which `data` class a link claim uses when the outside source holds both labels (trial lists) and measurements (a beta trace). I marked zenodo-link as `with_inputs`, and made no other claim depend on it.
3. Clock checks: they ask for a contrast between conditions, but here that contrast is the claim itself. I showed responses locked to the cue against shifted times in the data check, and pre-cue checks inside each claim's section.
4. The protocol does not cover a criterion written after its result was already seen while checking the data. That happened for zenodo-link (r = 0.94); I wrote the criterion anyway and said so in the claims file's opening comment.
5. The required sentence about failure to reproduce is triggered by a partial outcome on a recording-parameter claim. I included it.
6. The protocol says to read the linked code but does not cover linked code that holds none of the analysis. The paper's code covers only artifact removal and the ISI and waveform plots, so I used common choices and stated them in the helper's docstring.

**4. Runtime and failures**
- The notebook runs in about 2 minutes, most of it streaming the full 09/26 raw ephys.
- My first search for the 09/26 raw offset used too short a window and found a false peak (2220.9 s). I caught this by checking a late trial; the full-length search gives the consistent 9831.35 s, and that is what the notebook shows. Nothing else failed.
- The repo root contains untracked dotfiles (`.bashrc`, `scripts`, `.idea` and others). They are sandbox mounts of `/dev/null` that I did not create and left alone. They should not go into the commit.
