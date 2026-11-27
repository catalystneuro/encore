I tested 31 of the 39 claims and blocked 8. Both notebooks run cleanly from a locked environment, the entry checks pass, and the verifier package is in `executed/russo-2025/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| source-data-link | partially reproduced (Figure 2B means match; the Figure 1C session count and medians do not) |
| fig1a, fig1b, figs2, figs2a, figs3b (human, on the Source Data file) | reproduced |
| fig5a-human-mouse-similar | blocked, data_missing |
| fig1c (EEG), fig1d (LFP), fig1e (CSD), figs1b (PLF) | reproduced (CSD parts rest on an assumption) |
| figs4-intensity-dependence | reproduced, with all channels; with the file's valid channels the LFP low-intensity test gives p = 0.055 |
| speed-threshold-robust | partially reproduced (EEG holds up to 5 cm/s, LFP up to 2, CSD only at 0.1) |
| figs5-early-component-mouse | reproduced, under reading (b) only |
| figs6-posterior-no-modulation | blocked, data_missing |
| triphasic-pattern | partially reproduced (pattern present; silence 171.5 ms against 127.8) |
| fig2b-thalamus-leads | not reproduced (measure factor p = 0.24) |
| figs7a, figs7b (latencies) | reproduced (rest on an assumption) |
| fig3a-thalamic-rate-higher-active | reproduced, under the per-trial reading only |
| figs9-mos-rate-no-modulation | not reproduced (p = 0.012) |
| figs10a-fs-trn-no-modulation | reproduced |
| fig3b-bimodal-isi | not reproduced (relay-unit ISIs are unimodal, dip test p = 0.73) |
| figs11d-hf-earlier-less-variable | not reproduced (HF units respond later, the reverse) |
| figs12-intensity-shifts-to-hf | reproduced (the medium-to-high HF increase is 0.001) |
| fig3e-baseline-rate-doubles, fig3e-hf-frequency-reduced | reproduced |
| fig3e-lf-synchrony-reduced | partially reproduced |
| figs13-thalamic-features-predict-eeg, figs13d-lf-crosscorrelation | not reproduced |
| discussion-orthodromic-initial-excitation | reproduced |
| fig2fg (opto, figshare) | partially reproduced (unit delays match; no LFP in the deposit) |
| figs8b (opto) | reproduced |
| fig2h (opto) | reproduced (rests on an assumption) |
| fig4e, fig4f, fig4hi, figs14a, figs14b (model) | blocked, not_runnable |

## 2. What was found

**The dataset.**
- I pinned 0.230317.0039. It is the version the paper cites and the only published one.
- It holds 24 sessions from 23 mice. Only 10 sessions (10 mice, 9 with units) have the deep MOs stimulation the paper analyses. The paper reports 26 sessions from 15 mice for the EEG and units from 21 mice.
- There are no posterior-stimulation control sessions, which is why figs6 is blocked.
- The units' `waveform_duration` is labelled seconds but holds milliseconds.
- The file's `is_running` flag uses a 0 cm/s speed threshold; the paper uses 0.1 cm/s.
- The EEG, LFP, units and trial table share a clock: the stimulation artifact sits within one sample of every trial onset.
- The figshare opto deposit (doi:10.6084/m9.figshare.28440311.v1) is the authors' own deposit for this paper, in an archive the registry reads, but the paper is not listed on it. It should be. It has no description, one mouse's unit tables lack the area column, and it holds no LFP.

**Paper inconsistency.** The stimulating electrode's depth is 1.06 mm below the surface in the Results and 1.4 mm in the Methods.

**Assumptions** (outcomes marked `assumed`):
- For the CSD, the two sites of each Neuropixels row are averaged, so the 26- and 4-channel smoothing windows become 13 and 2 rows.
- The GFP peak threshold for the latencies uses a baseline of -1 to -0.01 s.
- In the opto deposit, light-only spike times are taken as timed from the light onset.

**Deviations from the paper's method:**
- Responsive units are found with 10 ms bins in place of the paper's adaptive kernel.
- The dip test uses the `diptest` package, because the paper's `unidip` does not run with numpy 2.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How was the 127.8 ms silence measured?
- What is the unit of the rest-versus-running firing-rate tests (per trial, per unit or per mouse)? The outcomes of fig3a, figs9 and figs10a depend on it.
- Which baseline window sets the GFP threshold, and how is the CSD handled across the probe's two columns?
- The opto deposit's layout is undocumented.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. A claim only partly testable (fig2fg, where the LFP part has no data) fits no outcome cleanly. I used `partially_reproduced` and explained it in the notes.
2. `measured` must be numbers, so I left it out for fig2fg, where some expected values cannot be measured.
3. When no reading matches, the protocol does not say which reading to record under `measured`. I recorded the first one listed.
4. Some criteria define no partial outcome (speed-threshold, fig3e-lf). I used `partially_reproduced` from the general outcome definitions.
5. An authors' deposit in a readable archive counts as one of the paper's datasets, yet the claims mark it `data: elsewhere`. I listed it under `inputs` only, not under `datasets`.
6. A seeded result used by other claims (the k-means split of fig3b): only fig3b was run under the five seeds. Its dependents use the claim's own seed.
7. A method the paper names but that cannot be run here (the adaptive kernel, `unidip`) is not left open by the paper, so I recorded the substitutes as deviations, not assumptions.
8. For the model claims, `not_runnable` asks what was tried. I read the code and did not attempt to run it, and the notes say so.

## 4. Runtime and failures

- The run took about 1 h 35 min (19:53 to 21:28 UTC).
- The main notebook takes 14 min; the opto notebook 1.5 min.
- Development hit three problems, all solved:
  - remfile streamed at only about 2 MB/s, so `russo.py` fetches HDF5 chunks directly by HTTP range request.
  - The figshare download address expires, so the reader re-resolves it and retries.
  - `unidip` is incompatible with numpy 2, so the dip test uses `diptest`.
- Nothing failed in the final run.
- The working tree also has untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others) that this run did not create; they should not be committed.
