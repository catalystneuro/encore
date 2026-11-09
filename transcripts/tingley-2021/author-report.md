I've completed steps 1 to 6 of the Author section: the entry, the attempt record and the verifier's package are written. Of the 35 claims, 14 were tested: 7 reproduced, 4 partially reproduced and 3 not reproduced. The other 21 are blocked. The entry passes its checks, and the notebook runs from a clean environment in about 3 minutes, with the same output on every run. I did not commit anything.

I pinned DANDI:000233 at version 0.250624.0414. The paper cites no version; this is the latest published one, and the earlier version 0.230223.0815 has the same 345 files with the same sizes.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig2-ripple-rate-predicts-glucose | reproduced (rests on an assumption): 18 rats; matches under 3 of 16 combinations of readings, e.g. R −0.176 at a mean lag of 14.2 min |
| fig2ef-correlation-beyond-shuffle | reproduced (KS test p = 4e-6) |
| fig2g-clustered-ripples | reproduced under reading (a): −0.191 nA after clustered epochs against +0.050 nA after isolated ones |
| edfig4-ripple-features | partially reproduced: inter-SPW-R interval has the largest effect, but the rest of the order differs |
| fig2h-phase-reset | not reproduced |
| edfig5-cross-frequency-coupling | partially reproduced: both coupling tests pass, but the comodulogram peak is not shifted off the diagonal |
| edfig1-glucose-rhythm | partially reproduced: the peak is at 51.4 min, outside 60 ± 6 |
| edfig1-sensor-decay | reproduced |
| supp-ripple-rate | reproduced (10.19 per minute, 14,671 per day) |
| supp-ripples-stable-across-days | reproduced |
| edfig3-ripple-rate-rhythms | partially reproduced: peaks at 24.0 h and 3.8 h, but 1,890 recording hours where the paper has 1,568.5 |
| edfig2-refractory-period | not reproduced: no interval between stored ripples is shorter than 25.6 ms |
| edfig4-nrem-wake | reproduced, on 3 rats where the paper has 8 |
| edfig4-no-hour-differs | not reproduced: 10 of 276 hour pairs have p < 0.05 |
| edfig1-glucose-circadian-meals | blocked, data missing (no meal times; the circadian part was run and found no effect, p = 0.99) |
| edfig9-dorsal-ventral | blocked, other: only one rat, with two days, has dorsal and ventral ripples and glucose recorded together |
| edfig6 (3 claims) | blocked, too large: about 6.4 h of LFP and 2.4 h of accelerometer reading, timed in the notebook |
| fig3 and edfig7 (7 claims) | blocked, data missing: no stimulation times |
| edfig3e, edfig8, edfig4-fasting-fed | blocked, data missing: no spike units, no meal times |
| fig4 and edfig10 (6 claims) | blocked, metadata insufficient: no cohort labels, no CNO or vehicle days |

**2. Dataset findings, assumptions and questions**

- **Swapped glucose dates.** In 12 subjects, glucose readings dated on day 12 or earlier were stored with day and month swapped (4 March appears as 3 April). I repaired this per subject only where it joins the series into continuous 5-minute steps. The repair raises the hours with both glucose and ripples from 1,139 to 1,717.
- **Duplicate files.** 27 recordings are deposited twice, once with dashes and once with underscores in the file name. Each is counted once.
- **Ripple time columns.** In the ripple tables, `peak` is measured from the start of the file, while `start_time` is on the session clock. The column descriptions don't say this.
- **Ripple threshold.** Nine subjects' ripple tables include events down to 4 s.d., where the Methods give 5 s.d. I applied the Methods' threshold and show the unfiltered events as a variant. The ripple-rate claim only matches with the threshold applied.
- **Clocks.** Session start times are local wall-clock time labelled UTC. In CGM2 and CGM3, files of the same rat use two different reference times, so I put each rat's files on one clock.
- **Missing links and data.** Nothing maps the dandiset's subjects to the paper's rats 1–45 or to its experimental groups. There are no units, stimulation times, injection times or labels, or meal times. Four subjects have glucose and electrophysiology on different days, and Vanessa's glucose sensor reads a median of 0.25 nA, against about 30 nA in the other rats.
- **Assumption, main claim only.** The SPW-R count and the glucose change are paired over the same 5-minute interval. Counting ripples over the 5 minutes after each reading leaves no per-rat combination matching, so the outcome depends on this choice. It is recorded as a question for the paper's authors (`methods_unavailable`), together with which correlation type was used and which lags were searched.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**

1. It doesn't say what to do when the data's own processing contradicts the Methods (the 4 s.d. threshold) while the claims file says to use the stored events. I applied the Methods' threshold, cited it as a method detail taken from the paper, and showed the stored events as a variant.
2. Repairing data, such as the swapped dates, isn't covered. I repaired them, recorded the repair as a finding, showed the results with the stored timestamps, and listed the repair as a deviation.
3. It doesn't say how to record a claim where only part can be tested (circadian testable, meals not). I blocked it as `data_missing` and put the circadian result in the notes.
4. Neither the protocol nor the claims files say whether a partial outcome is allowed when a claim's criterion has no "partial" case. I used `partially_reproduced` where the effect holds only in part, for the glucose rhythm and the ripple-rate rhythms.
5. Showing that the glucose and electrophysiology clocks agree has no contrast independent of the claims. I said so in the notebook and used the date repair as supporting evidence.

**4. Runtime and failures**

The run took about 1 h 25 min (17:40 to 19:04 UTC). The final notebook runs in 3.1 minutes. Nothing failed in the end. Two problems turned up along the way and were fixed:
- Reading the files in parallel threads gave no speedup, so I switched to separate processes.
- One file per rat in CGM1 to CGM3 stores the glucose series in a different order or against a different reference time. I found this during the clean run and fixed it by putting each rat's files on one clock. This moved the main claim's lags, which is why it now matches under 3 combinations of readings and rests on the alignment assumption.

Files are in `entries/000233-tingley-2021`:
- `reproduce_tingley_2021.ipynb`
- `sprglu.py`

The attempt record is `attempts/000233-tingley-2021-01.yaml`, and the verifier's package is in `executed/000233-tingley-2021/handover/`.
