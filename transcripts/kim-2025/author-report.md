I've finished steps 1 to 6: the entry and the attempt record are written, both notebooks pass `entry.py all`, and the handover is built. Nothing is committed.

## 1. Outcome per claim

| Claim | Data | Outcome |
|---|---|---|
| illusion-data-link | 000248 (with_labels) | reproduced |
| illusion-fig1c-isomap-geometry | 000248 | reproduced (every reading) |
| illusion-fig3a-orthogonal-variance-example | 000248 | reproduced |
| illusion-geometry-similar-across-datasets | 000248 | reproduced |
| data-v1-units | elsewhere (000021) | reproduced, rests on an assumption |
| fig1b-across-neuron-slope-near-1 | elsewhere | reproduced, rests on an assumption |
| fig1b-across-stimulus-slope, figs2, figs3, figs4ab, fig1d, figs5c, fig2a, fig2c, fig3bc, fig3d, fig3e, fig3f, fig4a, fig4c, fig4d, fig4e | elsewhere | reproduced |
| figs6-higher-areas-consistency | elsewhere | reproduced under reading (a); reading (b) holds in only 2 of 4 panels |
| figs5a-movie-slope-near-1 | elsewhere (000022) | partially reproduced: 24 sessions where the paper has 23; median slope 1.131 |
| fig2b-decoding-falls-with-slope | elsewhere | blocked, too_large (about 30 to 300 min on 4 CPUs, timed in the notebook) |
| figs4c-shuffling-alters-dependence | elsewhere | blocked, too_large (depends on fig2b) |
| figs1-gain-variance, fig2d-tangent-angle-rises-below-1 | elsewhere | blocked, not_runnable (not ported within the time limit) |

## 2. Dataset, assumptions, questions

**Dataset 000248**, pinned at 0.240502.2344, the only published version:
- The ICwcfg1 table lists every 400 ms frame, including the gray frames between trials. Those gray frames show the same image as the Blank stimulus, and nothing marks which of them are Blank trials. The image codes have no names; I took them from the paper's code (finding rated major).
- The trials can be recovered from the sequence: 60 leading gray frames, then trial and gray frame alternate. Every session then has 400 Blank trials and the 12 stimuli with 400 repeats that the code expects.
- The spikes share the clock of the table: the V1 response rises at 75 ms after image onsets, and decoding gives 0.576 after onset against 0.089 before it.
- The units table columns have no descriptions (minor).
- No session is deposited twice. All 11 subjects the code lists are present, plus a twelfth, sub-619293, that the code does not use.

**Allen data**: I used the DANDI copies, 000021 at 0.251116.2246 and 000022 at 0.251116.2247, as inputs. The exclusion rule drops the same two sessions as the paper's code.

**Assumption**: the paper's V1 units are AllenSDK's default units. That means the three quality criteria the Methods name, plus the "good" label AllenSDK requires by default (checked in `probes.py` at commit a56bd8e). With the label the counts match the paper (66.9 ± 25.5, 2008 units, slope 1.0489). Without it they do not (71.1, 2133 units, slope 1.0552). The other Allen claims use the three criteria alone, which is stated in the record.

**Questions for the paper's authors**, recorded as findings: whether the units are AllenSDK's default set, and which third movie session was excluded.

**Questions to a reader**: none.

## 3. Where the protocol was unclear or did not fit

1. Claims marked "elsewhere" make up most of the paper. Testing 24 of them took most of the run, and the protocol gives no priority between them and the dataset's own claims. I tested all I could and blocked the rest.
2. The rule of five seeds is too costly for fig4a's overlap halves and for the decoding. For fig4a I ran only the claim's seed and recorded it as a deviation; the RSM-based claims ran all five seeds.
3. There is no block reason for "not attempted within the time limit" that is not about the computation's size. I used `not_runnable` for figs1 and fig2d.
4. A finding about an input dataset (000021 pupil area labelled "Pixels ^ 2" but holding values from 0.0002 to 0.012) has no place in the record, since it is not the attempt's dataset. I put it in the claim's notes.
5. The protocol says nothing on whether to apply defaults of the software the paper used to read the data (AllenSDK's "good" filter). I treated it like the paper's code: run both readings, adopt the best-supported one as an assumption.
6. Timings printed in the notebook change from run to run, so a conclusion that quotes them exactly breaks on re-run. I wrote them as approximate values.

## 4. Runtime and failures

- The run took about 3 h 32 min (23:36 to 03:08 UTC).
- Final executed run: Illusion notebook 515 s, Allen notebook 2698 s (about 45 min), peak memory under 2 GB.
- One bug was caught and fixed before the final run. Three sessions start with a Blank trial, and my first trial-slot rule missed it.
- No command failed in the final run.
- Untracked dotfiles (`.bashrc`, `.idea`, and others) show up in the repository root. I did not create them and left them alone.
