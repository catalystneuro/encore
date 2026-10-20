I've done steps 1 to 6 for dandiset 000005: the entry ran cleanly from a fresh environment, the checks pass, and the verifier's handover package is built. The paper is closed access (no copy in PMC, Unpaywall, OpenAlex or Semantic Scholar), so I worked from its abstract plus the eight figure titles on the public landing page. That means no number from the paper is tested. I pinned 0.220126.1853, the only published version; the draft has the same 148 files and sizes.

**(1) Outcomes**

| Claim | Outcome | Basis |
|---|---|---|
| vpm-touch | reproduced | 20 of 24 VPM units respond to touch; 0 of 24 when spikes are moved to the wrong trial |
| vpm-whisking | reproduced | 21 of 24 units modulated by whisking; 0.12 of units under the shifted-spike null |
| fs-touch-and-whisking | reproduced | of 20 light-tagged FS cells, 0.65 respond to touch and 0.80 to whisking |
| exc-mainly-touch | not_reproduced | the pre-set test misses: excitatory cells more touch-selective than FS p = 0.074, than VPM p = 0.090. Other measures lean the claim's way (whisking-modulated: 0.28 of excitatory cells against 0.80 FS and 0.88 VPM) |
| fs-suppress-movement-spiking | reproduced | firing during whisking rises in 6 of 7 PV-Cre excitatory cells, p = 0.016 |
| fs-enhance-touch-selectivity | not_reproduced | selectivity is lower with light in only 2 of 6 cells; touch responses rise more than whisking responses |
| thalamus-drives-fs | reproduced | FS firing falls with light at the VPM site in 9 of 9 cells (2 mice), p = 0.002; not specific, as 18 of 21 cells fall |
| sensory-input-drives-fs | blocked (methods_underspecified) | the experiment is not described in the abstract, and the files don't say what each light condition does |

**(2) What was found about the dandiset**
- **No cell types:** none of the 130 L4 files says whether its neuron is excitatory or FS. I identified FS cells by their spikes to 5 ms light pulses in VGAT-ChR2 mice, and excitatory cells by broad action potentials in untagged whole-cell recordings.
- **Light conditions undocumented:**
  - `photo_stim_mode` has no description, and its labels mean different things in different files.
  - `photo_stim_power` is empty in every L4 file, and no file names the opsin.
  - Two of the recorded wavelengths look questionable.
- **Wrong recording mode:** the session description is wrong for 24 of 130 L4 files. 23 labelled whole-cell hold juxtacellular traces.
- **Unstated sampling rate:** the L4 trace is at 10 kHz up to March 2015 and 20 kHz from August 2015; only the timestamps show this.
- **Bad `first_touch_time`:** in the L4 files it is the trial start plus the true latency divided by 1000. It is correct in the VPM files.
- **Other:**
  - 8 files name no principal whisker.
  - No recording is deposited twice.
  - Neither the paper nor the dandiset links any analysis code.

**(3) Where the protocol was unclear, wrong or missing something**
1. **Abstract only:** the rules for expected values and tolerances have nothing to work on. I wrote threshold criteria and noted that no number is tested.
2. **Figure titles as a source:** the protocol says to use the abstract when the paper is closed. I also used the public figure titles and said so in the claims file.
3. **Cell types inferred from the data:** the protocol covers labels taken from outside sources, not labels derived from the data. I fixed the classification in the claims file before any analysis and recorded it as a deviation on each claim and as a finding.
4. **A pre-set test that fails its own null:** the Rayleigh test of whisking phase marked 88% of VPM units as modulated even with spikes moved to the wrong trial. The protocol covers tied criteria but not this. I replaced the test with one corrected for uneven phase occupancy, tested against a trial-shift null. The amendment in the claims file records what I had already seen; the notebook shows both versions, and the new one decides.
5. **Clock check for single-cell sessions:** decoding a task variable doesn't fit here. I compared each cell's touch and whisking responses with spikes moved to the next trial. For 3 of 124 cells or units the alignment is not established; they are listed.
6. **Undocumented optogenetics:** the protocol offers either blocking or testing. I tested where the data support the assumption (some PV-Cre cells are silenced by the light), stated the assumption in the deviations, and blocked the Figure 7 claim.
7. **Runtime advice:** "reduce the data as it loads" was not enough. Reading through h5py/remfile took 20 minutes. Single HTTP range requests on the contiguous datasets plus a process pool brought loading to about 2.5 minutes.

**(4) Runtime and failures**
- The notebook runs in about 205 s, of which about 155 s is streaming.
- The final `all` run passed with 0 check errors and 0 cell errors, and the handover is in `executed/000005-yu-2016/handover/`.
- No step failed in the end. The only problems along the way were the 20-minute first load and the invalid Rayleigh test, both handled as described above.
- Untracked dotfiles at the repo root (`.bashrc`, `.vscode`, and similar) and an empty `entries/000005-yu-2016/.claude/` folder look like harness artifacts. I left them alone.

Nothing is committed or pushed. The attempt record is `attempts/000005-yu-2016-01.yaml`, the claims are in `claims/000005/10.1038-nn.4412.yaml`, and the notebook is `entries/000005-yu-2016/reproduce_yu_2016.ipynb`.
