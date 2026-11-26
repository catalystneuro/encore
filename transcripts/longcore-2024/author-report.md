I finished steps 1 to 5 of the Author section and ran the handover (step 6), and I did not verify my own work. `python tools/entry.py check` reports 0 errors, and `all` passed: the notebook runs in 9 s. Nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| table1-suppression-0p5-and-above | reproduced |
| table1-increase-0p01 | reproduced |
| tukey-illuminance-within-cct | not reproduced |
| cct-0p01-not-significant | reproduced |
| glm-illuminance-cct-interaction | partially reproduced (interaction p 0.0063 at best; the paper reports < 0.002) |
| effect-size-illuminance-over-cct | reproduced |
| cct-effect-grows-with-intensity | partially reproduced (the spread across CCTs is smallest at 0.5 lx, not 0.01 lx) |
| lower-cct-less-suppression | reproduced |
| aicc-individual-sex | reproduced |
| sex-males-less-suppressed | reproduced |
| sex-predicted-suppression | reproduced |
| individual-variation | reproduced (-27.86 and +21.46) |
| cfos-no-cct-difference | reproduced (t(10) = 0.9409, p = 0.3689, exactly the paper's values) |

No claim is blocked and no outcome rests on an assumption. Nothing draws random numbers, so no seeds were needed. The record is `attempts/longcore-2024-01.yaml`; the entry is `entries/longcore-2024/` (the notebook `reproduce_longcore_2024.ipynb` and the helper `alan.py`).

## 2. Dataset, assumptions, questions

**Version.** I pinned version id 300765, the only published version. The paper cites the DOI, which resolves to it.

**Data findings:**
- The README says suppression "ranges -1 to 1", but the values are percent, from -59.6 to 100 (minor).
- 9 of the 192 mouse-by-treatment values are missing: mouse 6FC1, P2 at 0.01 and 0.5 lx, and mouse 6FC2, P8 at 0.01 lx. Those treatments have 14 or 15 mice where the paper says 16, and nothing explains why (minor).
- Only derived values are deposited. The wheel counts behind suppression are not there, and the cFos file has one value per animal with no animal ID, sex, section or observer (minor).
- Checks that passed: no duplicate recordings, the sexes and counts match the Methods, and the means agree with the abstract.

**Paper findings:**
- The Methods say the GLM uses a log link, but the reported AICc differences, sex predictions (one of them negative) and mouse effects are matched only by an identity link with illuminance in lux.
- The 3000 K cFos "s.d." of 8.22 is actually the s.e.m.; the real s.d. is 20.13.
- The Tukey sentence matches no comparison on the data: it is 3000 K that differs from the other CCTs, at 5 and 50 lx.

**Questions for the paper's authors** (recorded in the findings):
- Which link and which illuminance scale did the JMP models use?
- Why are the 9 values missing?
- Which comparisons does the Tukey sentence describe?

**Assumptions:** none needed. Every outcome is decided by readings the claims file lists.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit
1. "Develop on a subset" and timing don't apply to a 5 KB table. I ran everything at once and noted it.
2. The clock-alignment check (step 2) doesn't apply to tables with one value per mouse and treatment. I said so in the notebook.
3. No finding kind covers "the paper's sentence does not match its own data, and the paper doesn't give the pairs". I used `methods_unavailable` with a question for the authors.
4. Some criteria say "16 mice" but the file has 14 or 15 for some treatments. I used the mice present and recorded it as a deviation.
5. cct-effect-grows-with-intensity has no partial rule. I applied the protocol's general definition ("holds only in part").
6. Two readings in the claims file can't be run on the deposited data: averaging over cFos observers, and handling mice with no prior-day activity. I recorded deviations.
7. JMP's default centering of illuminance in the interaction is fixed by neither the paper nor the claims file. I used it and showed the uncentered fit; it changes no outcome, so it isn't marked as an assumption.
8. The "checks that passed" finding has no cell tagged `finding-*` of its own. I pointed it at the `sanity` cell.

## 4. Runtime and failures
- The run took about 15 minutes of the 5 hours (18:10 to about 18:24 UTC).
- Nothing failed except a read-only array error during development, which I fixed.
- The working tree shows untracked character-device files from 18:05, before this run started (`.bashrc`, `.idea`, `scripts` and others). They are sandbox mounts, not mine, so I left them for the workflow.
