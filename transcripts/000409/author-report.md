I've done protocol steps 1 to 6 for dandiset 000409: the entry is `entries/000409-ibl-2025/`, the attempt record is `attempts/000409-ibl-2025-01.yaml`, and the handover package is in `executed/000409-ibl-2025/handover/`. I used the paper's full text, which is open access (CC BY 4.0); it is saved under `paper/`. I pinned 0.260309.1324, the only published version. The paper cites no DANDI version, and the draft holds the same 2,048 files. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| dataset-sessions-mice-labs (459 / 139 / 12) | reproduced |
| dataset-probes-units (699 insertions, 621,733 units) | reproduced |
| well-isolated-neurons (75,708) | reproduced |
| canonical-regions (201 regions, 62,857 neurons; every inclusion step matches) | reproduced |
| brain-areas-279 | reproduced |
| mice-sex (94 male / 45 female) | reproduced |
| mice-age-weight | partially reproduced: weight matches; age at recording is 13 to 66 weeks, the paper says up to 178 |
| probe-versions (109 / 586 / 4) | reproduced |
| trials-per-session | reproduced |
| rf-mapping | blocked, data_missing |
| behav-performance (81.4% correct) | reproduced (mean over sessions, 81.58%) |
| behav-zero-contrast (58.7%, t = 20.18) | partially reproduced (58.26%, t138 = 19.68) |
| behav-early-movements (22.8% under 80 ms) | reproduced (22.75%) |
| fig1d, fig1ef, fig1g, fig1h | reproduced (fig1g only under reading b, 9.9 trials) |
| dec-stim-restricted | reproduced |
| dec-choice-widespread | reproduced (5 regions against 4 for stimulus, a margin of one) |
| dec-feedback-nearly-all | partially reproduced (7 of 10 regions significant) |
| sc-stim-fraction, sc-choice-fraction | blocked, methods_underspecified (false-positive check failed) |
| traj-latency-visual | not reproduced (VISam 59 ms is not later than VISpm 61 ms) |
| traj-latency-late | reproduced (IRN 118 ms, GRN 110 ms) |
| fback-oscillation-licking | partially reproduced (peak at 7.1 Hz, not about 10 Hz; tied to licking) |
| traj-stim-regions, wheel-speed-decoding, encoding-feedback-largest, video-correlates, granger-interactions | blocked, other (not attempted) |

In total: 17 reproduced, 4 partially reproduced, 1 not reproduced, 8 blocked.

For the decoding claims, the per-region effects here track the paper's own region table closely (Spearman 0.91 to 0.98). The two single-cell claims are blocked only by the protocol's false-positive rule. Without that rule, all 14 regional stimulus fractions are within 0.02 of the paper's table.

## 2. What was found about the dandiset

- **Complete release.** It holds every session, mouse, probe and unit the paper reports, and every count of the paper's inclusion table. No recording is deposited twice.
- **Wrong block column in 64 sessions.** These are all the sessions with the protocol name `_iblrig_tasks_ephysChoiceWorld` without a version. In them, `probability_left` (and so `block_index` and `block_type`) flips between 0.2 and 0.8 on every trial after the first 90. The stimulus falls on the stated likely side in only 47.5% to 57% of trials, against 76% to 83% in the other 395 sessions. I left these sessions out of every analysis that uses blocks.
- **No receptive-field mapping.** No session contains the mapping phase or its stimulus.
- **Quality threshold differs from the Methods.** The quality score matches a noise cutoff below 5 for every unit; the Methods say below 20 µV, which would give 95,430 well-isolated units instead of 75,708.
- **Descriptions that disagree with the data:**
  - The first-movement time is described as after the go cue, but it comes before the go cue in 12% of trials.
  - The reward is 1.5 µL on every rewarded trial; the Methods say 3 µL.
  - The units description mentions a `label` column that does not exist and calls all probes Neuropixels 1.0, though four are NP2010.
  - Weight is a single value per mouse, the same in all its sessions.
- **Inconsistencies in the paper and its code:**
  - The "± 0.4 s.d." on 81.4% correct is an s.e.m.; the s.d. across mice is 5.1.
  - The paper's code takes age from the IBL database, not the recording day, and swaps the mean and median labels for weight.
  - The paper's region table marks 210 regions canonical, not 201.
  - The paper's own results table gives different visual latencies from those in the text.
  - The single-cell null rate here is about 2.5e-3, roughly 50 times the paper's stated 5e-5, because the two tests are not independent.

## 3. Where the protocol was unclear, wrong or missing something

1. **Scale.** Nothing covers a dataset where the paper's own analysis (459 sessions, 10 cross-validation runs, 200 null sessions) cannot fit in 30 minutes. I tested a fixed set of regions, chosen in advance in the claims file, and reduced the repeats and nulls. Every reduction is recorded as a deviation.
2. **`not_runnable` versus not attempted.** `not_runnable` asks the notebook to show the analysis does not fit, but some whole-brain analyses could fit in a separate notebook. I used `other`, said "not attempted", and gave the measured cost.
3. **Claims not covered by the criterion.** fig1g had no measure in the paper, so I fixed two readings beforehand. behav-zero-contrast's criterion defined only "reproduced"; I chose partially reproduced and recorded why.
4. **What "far from the paper's rate" means.** The false-positive rule doesn't say. I fixed it in advance as the 95% interval excluding a band of one third to three times the paper's rate. The rule then blocks claims whose regional values match the paper, and the cause looks like the paper's own assumption, not a different procedure. I followed the rule and recorded a finding.
5. **The paper's per-region results tables.** It's unclear whether the tables in its repository count as outside inputs, since they are reported values, not measurements. I listed them under `inputs` and kept the claims as `data: dandiset`.
6. **Bad data found mid-way.** The protocol doesn't say what to do with data found wrong before the analysis but after the criteria were written. I amended the claims file's opening comment before running those analyses and left the 64 sessions out.
7. **Clock check with few units.** Some sessions have too few loaded units to show the shared clock; I listed the 16 such sessions, as the protocol asks.
8. **First author is a consortium.** I named the entry `000409-ibl-2025`.

## 4. Runtime and failures

The notebook runs in about 10.5 minutes (624 s in the last clean run): about 3.5 to scan the 459 processed files, 2 to stream the spikes of 168 sessions, 4 to decode. The last three clean runs gave identical numbers.

Failures during development, all fixed:
- Some files have no `epochs` group, which crashed the first run.
- Mixed time zones broke a date column under pandas 3.
- Decoding was not reproducible until I fixed the liblinear seed.

Six of 226,440 logistic fits did not converge; the notebook reports this. Nothing failed in the final run.
