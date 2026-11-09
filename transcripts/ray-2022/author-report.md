I've finished steps 1 to 6 for CRCNS nac-1. Of the 34 claims, 17 are reproduced, 8 partially reproduced, 8 not reproduced and 1 blocked. The run `tools/entry.py all` passes (0 errors, notebook 57 s), and the handover package is in `executed/crcns-nac-1-ray-2022/handover/`. Nothing is committed.

Most population claims rest on a cluster partition I had to reconstruct and adopt as an assumption, because the paper's own population labels are not deposited.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| units-recorded | partially reproduced (368 units, 7 rats, but 90 sessions, not 95) |
| cue-responsive-193 | reproduced (reading b: 211 units, 81 sessions; the authors' script gives exactly 193 from 82) |
| fig1c-acquisition | blocked: data_missing |
| fig1g-discrimination | reproduced under one reading (all sessions, 0/0 read as 0); one CI bound sits near zero |
| fig1h-poke-rate-unrelated | reproduced (assumed: how 0/0 suppression ratios are handled) |
| fig1h-discrimination-safety | reproduced |
| fig2-five-clusters | partially reproduced (the five patterns appear, the counts don't match) |
| populations-by-rat | not reproduced |
| most-units-threat | reproduced |
| fig3ab, fig3c | reproduced, reproduced |
| fig4ab, fig4b, fig4cd, fig4ef, fig4f | partial, reproduced, partial, partial, reproduced |
| fig5ab, fig5cd | not, not |
| fig6-anova, fig6d, fig6e, fig6f, fig6-greatest | reproduced, reproduced, not, reproduced, reproduced |
| fig7-tuning-curves | reproduced |
| fig8ab, fig8cd, fig8ef | reproduced, partial, partial |
| fig9a, fig9bcd, fig9efg, fig9hij | not, partial, partial, not |
| fig10a, fig10bcd, fig10efg | reproduced, reproduced, not |

From populations-by-rat onward, every outcome is marked `assumed: true` except most-units-threat and fig3ab, which hold under every partition.

## 2. The dataset, assumptions and questions

**Version.** CRCNS does not version data sets. I recorded `unversioned` and pinned `data.zip` by its MD5 (ab134070…). The bucket holds only `live/` for nac-1, and the description is its initial version 0.6.

**What the data set holds.**
- The authors' MATLAB scripts are inside the zip. My loader reproduces their `cube.mat` exactly for all 368 units (trial onsets, binned firing, suppression ratios).
- The description never says which event channel is which; only the script `cubeScriptPR25.m` does.
- Recording pauses between trials. The files hold data only from 20 s before each cue to about 33.5 s after it, which the description doesn't mention. This limits every ITI analysis.
- There are 90 sessions, against 95 in the paper.
- The pre-surgery sessions (needed for fig1c) and the paper's cluster labels are not deposited.
- The description calls `poke.base` a 2-s rate; the values are 20-s rates.

**Where the scripts differ from the paper.**
- Firing normalization: the script works per trial against a floored 2-s baseline; the Methods average each trial type against a 10-s baseline.
- Rates are floored to whole Hz.
- 0/0 suppression ratios are set to 1.
- The waveform measure is half the scale of Figure 3C.

**Bootstrap intervals.** The paper's printed Figure 1G intervals match bootstrap-t quantiles added to the mean without reflection. The means and the ANOVA (F = 57.41) match the paper exactly, so the data agree; only the interval form differs.

**Assumptions.**
- Cue-responsive set: I used the script's screen, the only procedure that gives 193 units.
- Population labels: the partition among the claims file's readings whose cluster centres best match the five patterns the paper describes (N4 normalization, most frequent partition over 100 starts). It gives 6, 28, 45, 89 and 25 units against the paper's 5, 26, 55, 91 and 16.
- 0/0 suppression ratios set to 1, following the script, for fig1h.
- ITI event windows and their normalization taken from `cubeScriptPR25.m`, since the Methods leave them open.
- Waveform measure not halved, so it matches the scale of Figure 3C.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which normalization and which k-means run produced the published populations, and can the labels be deposited?
- How were ITI events chosen, given the recording pauses?
- How were 0/0 suppression ratios handled?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **The data set ships the authors' analysis code, but the paper links none.** The protocol only covers "code the paper links". I treated the scripts as the paper's code: Methods first, scripts second. Where the scripts contradicted the Methods (normalization), I ran them as a variant only. Where they settled a detail the Methods leave open (ITI windows, 0/0 handling), I ran them as a reading.
2. **Downstream claims depend on an unstable reconstructed clustering.** The protocol says to adopt a reading, but not how to choose among partitions. I chose the one whose clusters best match the five described patterns, then reported each claim under all 12 partitions.
3. **A bootstrap bound that sits on zero with n = 7 flips with the seed.** The protocol has no rule for this. I judged on the median bounds over 50 seeds and recorded that as a deviation.
4. **The protocol doesn't say whether "run every reading" combines with a claims file's "reproduced under any reading" rule.** This matters when some readings come from the code and the claim is a claim of absence. I used the any-reading rule for readings the claims file lists. For absence claims I judged on the paper's own procedure.
5. **One claims-file reading can't apply to this data.** ITI reading (a) needs events more than 30 s after onset, which the files don't hold. I ran it, showed it, and called it unsupportable.
6. **Neither the CRCNS section of archives.md nor the protocol says how to pin an unversioned archive in the notebook.** I recorded `unversioned` and the MD5 in both the helper and the header.

## 4. Runtime and failures

The run went from 03:54 to about 04:26 UTC. The notebook takes 57 s from a clean environment. Nothing failed in the final run.

The repository root contains untracked device-file entries (`.bashrc`, `.gitconfig`, `scripts`, `.idea` and others), created at 03:52 by the sandbox. They are not mine, so I left them; the workflow should not commit them.

Files written:
- `entries/crcns-nac-1-ray-2022/` (`entry.yaml`, `requirements.in`, `requirements.lock.txt`, `nac.py`, `reproduce_ray_2022.ipynb`, `README.md`)
- `attempts/crcns-nac-1-ray-2022-01.yaml`
