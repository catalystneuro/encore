I've written the `reconciliation` block in `attempts/sabatini-2024-02.yaml` and added `entries/sabatini-2024/earlier_findings.ipynb` to the entry. `python tools/entry.py check` reports 0 errors, and the full run passes: 49, 30 and 2 minutes for the three notebooks. The lock file did not change and nothing is committed.

The biggest fact behind everything else: every file in DANDI:000070 was rewritten for 0.261122.2046, but the spike counts the analyses use are the same in both versions, except for Jenkins units 0 and 1. The earlier attempt had also run its main analyses without those units and Nitschke unit 170, and only one outcome changed (fig6e). So the dataset change explains none of the outcome differences.

**(1) Blind.** Yes, `blind: true`. The audit printed four lines. One is the protocol's link to the pilot notes. One clones the paper's own code (kaufmanlab/LDR-public). Two are the README's site links and the author's own runner URL. None of them shows an earlier attempt's results.

**(2) Earlier findings**

| # | Earlier finding | Status | Now | Evidence |
|---|---|---|---|---|
| 1 | Nitschke file joins five segments with overlapping clocks | fixed | – | One clock now; nothing goes backwards, all spike times sorted |
| 2 | One unit per electrode, no sorting label | partly_fixed | 1 | The units table now says these are unsorted threshold crossings; the sorted units are still missing |
| 3 | Jenkins unit 1's row holds two spike trains | fixed | – | Unit 0 now has 257638 spikes (61030 + 196608); unit 1 has 264946 |
| 4 | Positions labelled meters with conversion NaN | partly_fixed | 7 | Hand and cursor now have 0.001; eye still has NaN |
| 5 | No EMG | still_present | 8 | No EMG anywhere in either file |
| 6 | Nitschke unit 170 fires above 100 spikes/s on a run of trials | still_present | 9 | 229 trials, block ratio 13.7 against at most 2.5, same as before |
| 7 | Questions for the paper's authors | still_present | 10 | About the paper, which has not changed; the open questions are carried over |
| 8 | Paper's code needs files available only on request | still_present | 6 | The blind attempt reports the same files |

Findings 7 to 10 were added to the record with `found: on_prompt`.

**(3) New findings:** 2, 3, 4 and 5. Finding 3 is a "checks that passed" item rated `none`, which the blind attempt's protocol version still allowed.

**(4) Outcomes that changed (10 claims)**

| Claim | Earlier → now | Cause | Confidence |
|---|---|---|---|
| data-composition | reproduced → partially | label: same numbers; the blind attempt read the new units description as ruling out the unit count. Evidence points to partially | medium |
| jpca-variance-explained | partially → reproduced | reading: raw vs de-mixed basis and one vs two soft normalisations; PMd-N 5.4 vs 6.8% against a 6.3% bound | low |
| fig3g-basis-frequencies | not → partially | reading: factorization fitted on -150 to +850 ms vs the whole window; k = 7, 5, 7, 7 vs 7, 7, 9, 9 | medium |
| tbf-shuffle-control | partially → reproduced | reading: same window choice; PMd-J 28.7 vs 35.4% | medium |
| fig3h-recoverability | partially → reproduced | reading: same window and basis; chance level 86.5 to 89.6% vs 84.8 to 87.8% | medium |
| fig4b-plane-alignment | reproduced → partially | reading: k = 9 adds a PMd-N 3.65 Hz rotation with AUC 0.545 | medium |
| fig5a-frequencies-segregated | reproduced → partially | reading: an extra PMd-J rotation from k = 7 gives the one failure of 36 | medium |
| fig6c-location-tracks-direction | partially → reproduced | reading: target angle from the target position vs the hand endpoint, plus a different factorization; PMd-N 0.065 vs 0.357 | low |
| suppfig7a-not-memorization | partially → reproduced | reading: sextants as fixed 60° arcs vs six equal blocks of conditions | low |
| fig7f-ldr-decoding | partially → reproduced | error in the earlier attempt: `kin_ve` uses the raw sum of squared residuals, not the residual variance of the cited `getVarExplainedKinematics.m`. Evidence points to reproduced | medium |

Six of the ten come down to one open choice the claims file itself names: whether the factorization is fitted on -150 to +850 ms or on the whole -350 to +850 ms window. The PMd-N cause in jpca-variance-explained and fig6c was not pinned to one factor, and the size of the fig7f formula effect was inferred from the code, not re-run. A subagent did the first pass on the ten diagnoses; I checked its key code and record evidence before using it.

**(5) What did not fit the protocol**
- **Pilot notes:** `docs/pilot-notes.md` has no section after pilot-14. I read the pilot-19 change from `docs/protocol.md` (findings now need their code and versions). It explains no outcome difference.
- **Protocol version:** the current protocol is pilot-20, not pilot-19.
- **Earlier entry:** the repository has a single commit, so the `git show $c:entries/...` recipe returns the new entry. I used `earlier-entry/` for the earlier attempt's code.
- **Paper-only findings:** a finding about the paper (7, 8) cannot be "checked directly on the version". I treated them as still present.
- **Sandbox placeholders:** the sandbox left untracked placeholder files (`.bashrc`, `.idea`, `scripts` and others) in the checkout. I left them alone; they should not be committed.
