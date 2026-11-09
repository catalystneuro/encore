I did steps 1 to 6 of the Author section. The entry passes `check` and `run` in 152 s, and the handover is built in `executed/000128-churchland-2010/handover/`. Nothing is committed.

**(1) Outcomes per claim**

| Claim | Outcome |
|---|---|
| recordings-jarray | partially reproduced: 108 conditions and 2295 trials match; 182 units against 146 |
| recordings-single-electrode | blocked, data_missing |
| fig2b-example-concordant-tuning | blocked, data_missing |
| fig2ce-example-opposing-tuning | blocked, data_missing |
| fig3-maze-most-not-maintained | blocked, methods_underspecified (holds under T2, not under T1) |
| fig4d-mean-correlation-jarray | not reproduced: mean r 0.025 to 0.051, p > 0.4 |
| fig4abc-mean-correlation-single-electrode | blocked, data_missing |
| fig4-no-separate-populations | reproduced |
| fig4e-correlation-time-course | reproduced |
| suppfig1-population-averages | reproduced |
| fig6-peri-movement-space-best | blocked, methods_underspecified (holds under T2, not under T1) |
| fig6-each-dimensionality | blocked, methods_underspecified (readings disagree) |
| fig6-performance-vs-dimensionality | blocked, methods_underspecified (holds under T1, not under T2) |
| prep-dimensionality | not reproduced: 15 to 20 components, not 7 to 10 |
| fig6e-summary-across-datasets | blocked, data_missing |
| fig7a-shuffled-space-poor | blocked, methods_underspecified (holds under T2, not under T1) |
| fig7b-window-start-slide | reproduced (J-array ratio 0.90 to 0.97) |
| ap-location-no-effect-on-correlation | blocked, metadata_insufficient |
| fig7c-anterior-posterior-performance | blocked, metadata_insufficient |
| fig7d-pd-consistency | reproduced |
| fig8-model-weak-correlation | reproduced (simulation) |
| fig8-model-pd-perfect | reproduced (simulation) |

**(2) The dataset and the questions asked**

I pinned 0.220113.0400, the only published version. The draft holds the same two files with identical contents.

The dataset holds only the paper's J-array session (monkey Jenkins, 2009-09-25). There is no speed task, no single-electrode recording and no EMG.

What I found, all recorded under `findings`:
- **Array labels are wrong.** Every unit's electrode reference points into the 96 PMd rows, so by the file all 182 units are in PMd. The reference equals the unit id's channel minus one, so the array offset looks lost in conversion.
- **No locations.** The electrodes have no coordinates. The unit ids' leading digit (92 and 90 units) may be the array number, but nothing documents it.
- **Unit and trial selection.** There are 182 units against the paper's 146, with no record of which units or trials the paper used.
- **Test file.** 574 more trials sit in a test file as 0.7 s segments, with no labels or behaviour and only the 137 held-in units. None is a duplicate of a train trial.
- **Negative delays.** 14 trials have a delay below zero (down to -3 ms).
- **Clocks.** Hand speed rises at the marked movement onset. Reach direction can be decoded from spikes after target onset (accuracy 0.66) but not before (0.17).

Three questions are in `questions/000128.yaml`:
1. **T1 or T2 for the proto-trial selection.** This decides five of the blocked claims. T1 keeps 74% of trials and leaves two conditions empty; T2 keeps 91%. The question cites the supplement's "typically ~90% of all trials".
2. **Whether reading S2 can stand.** It selects 6 units, and none for the correlation claims.
3. **What "maximum rate" means in suppfig1.** The outcome does not change at present.

**(3) Where the protocol was unclear or missing something**

1. A reading that selects no units (S2 for the correlation claims) gives no outcome. The protocol says the outcome is "the one they all give" but does not cover a reading that yields nothing. I decided those claims on the readings that gave a result and recorded the gap.
2. A trial reading can leave a condition with no trials (T1 empties two). Nothing says what to do. I dropped those conditions for that reading and recorded it as a deviation.
3. The claims file allows the array as a fallback for anterior-posterior location, but the dataset's array labels are wrong. The protocol has no rule for an undocumented substitute such as the unit-id digit. I blocked both claims as metadata_insufficient and showed the digit regression only as a variant that decides nothing.
4. The paper's own "~90% kept" works like the protocol's chance-level check for a selection, but that check is written only for chance levels and false-positive rates. I did not use it to drop T1 and asked instead.
5. recordings-jarray: the criterion only says when the claim is reproduced, not when it is partial. Two of three counts match, so I called it partially reproduced.
6. Some details the criteria leave open below their stated readings. I ran both versions of each and recorded them as deviations, not questions, since neither changes an outcome:
   - V1 "maximum absolute value": run as the magnitude and as the signed component.
   - How the go- and movement-locked rates are joined under A2.
   - Acceleration: taken as the time derivative of the dataset's hand velocity.

**(4) Runtime and failures**

The notebook runs in about 2.5 minutes (152 s under `tools/entry.py run`; `all` took 2 min 54 s). Nothing failed.

One bug turned up during development and is fixed: an empty condition was averaged as zero rates. That had made fig4d look reproduced (mean r 0.117); with the fix it is not reproduced.

Some untracked dotfiles (`.bashrc`, `.idea` and others) are in the repository root. I did not create them and left them alone.
