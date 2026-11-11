I've added the reconciliation block to `attempts/kim-2022-02.yaml`, along with two findings marked `found: on_prompt` and a new notebook, `entries/kim-2022/earlier_findings.ipynb`, which is listed in `entry.yaml`. Both notebooks ran cleanly, `reproduce_kim_2022.ipynb` in 514 s and `earlier_findings.ipynb` in 169 s. Locking left the pins unchanged. `python tools/entry.py check entries/kim-2022` still reports 3 errors (see point 5); they were there before I started. Nothing is committed.

**1. Blind: yes (`blind: true`).** The audit flagged one line, `transcripts/kim-2022/author.md:1988`. It is the author writing its own record, `kim-2022-02`, so it shows nothing from the earlier attempt.

**2. Earlier findings**

| Earlier finding | Kind | Status | Now |
|---|---|---|---|
| 1 | data_missing (no Figs. 3–6 or Fig. 1E data; nothing points to 000548–000550) | still_present | 1 |
| 2 | Same YP image in sub-Fig2-0-03 and sub-Fig2-25-04 | still_present | 3 |
| 3 | Both channels of sub-Fig1F are the same image | still_present | 4 |
| 4 | ImageSeries of shape (22323, 22323, 2), 2 Hz, unit n.a. | still_present (checked in the new notebook, added as on_prompt) | 12 |
| 5 | No pixel size, electrode positions, ROI or field | still_present | 5 |
| 6 | Description says 144 images of a six-well plate | still_present | 6 |
| 7 | Dish numbers up to 18 with no selection described; 100% dishes take up more than unipolar | still_present (checked in the new notebook, added as on_prompt) | 13 |
| 8 | Questions for the authors | still_present (2 of the 5 questions asked again) | 10 |

For finding 7, the 100% dishes still take up more YP than the unipolar ones: largest mean 750.5 against 650.8 a.u. with this entry's ROI. The earlier attempt measured 761.0 against 571.1.

**3. New findings in `kim-2022-02`:** 2, 7, 8, 9 and 11. All are about 000448, which the earlier attempt did not use.

**4. Outcomes that changed**
- **fig2a-uptake-rises-with-field** (was partially_reproduced, now reproduced): the claims file now judges the unpaired test only. On top of that, the method differs in the footprint disc (0.2 mm against 0.5 mm), the 25% group (2 dishes against 3) and the field scaling. The paired test passes for 3 of 5 amplitudes in both attempts.
- **fig2b-exponential-same-slope** (was not_reproduced, now partially_reproduced): the claims file now fixes one reading where it used to run 12. The two attempts also label "slopes agree but the exponential fits only 3 of 5" differently.
- **fig2c-inhibition-flat-above-8-7** (was not_reproduced, now reproduced): a difference in method. The high-field ROI differs, and the smaller footprint discs raise the unipolar mean at 1.8 mm (87.9 against 47.7 a.u.).
- **fig2c-weaker-at-6-7** (was blocked, now partially_reproduced): a difference in method. The unipolar mean at about 6.7 kV/cm is 19 a.u. now against -8.6 a.u. earlier, and the earlier attempt's own background rule blocked it.
- **fig7-charging-time-constant, fig7-bipolar-overshoot, fig7-summation-without-buildup** (were blocked): a change in the protocol. Under pilot-14, 000448 counts as one of the paper's datasets, so the blind attempt used it.

**5. What did not fit**
- **Failing check:** the claims file was rewritten after the earlier attempt and now has three more Fig. 7 claims, which `attempts/kim-2022-01.yaml` has no outcomes for. I left that record alone because the protocol says it stays as it was. Someone needs to decide how `check` should treat a superseded record like this.
- **Figs. 3–6 claims:** both attempts record them as blocked, so I did not list them under `outcomes`. Only the reason changed (`other` became `dataset_missing`), and I note that under `protocol`.
- **Finding 1:** I marked it `still_present`, not `partly_fixed`. Fig. 7 became testable because the registry's list of the paper's datasets changed; the dataset itself is the same version.
- **Pilot-13:** raising the notebook time limit to 60 minutes had no effect here, since neither attempt came near the old limit.
