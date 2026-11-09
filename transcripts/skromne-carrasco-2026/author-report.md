I've done steps 1 to 6 for DANDI:001676 (version 0.251205.2137, the version the paper cites and the only published one). Both notebooks pass `tools/entry.py all`, the entry check reports 0 errors, and the handover is in `executed/001676-skromne-carrasco-2026/handover/`. Of 32 claims, 15 are reproduced, 5 partially reproduced, 7 not reproduced and 5 blocked. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| edf1h-ring, fig1f-example-stable, fig1g-all-mice-stable, edf4ab-vtest-per-animal, edf4c-previous-session, edf4ef-not-diffusive, fig1h-drift-rate, edf4g-pairwise-offset-stable, fig1i-offset-drift, edf4ij-pv-decay, fig2e-offset-across-environments, edf5c-stable-within-environment, fig2g-environment-classifier, edf7-ephys-offsets, fig4e-decoder-single-visit | reproduced (15) |
| roi-counts, fig2i-random-remapping, fig4d-single-visit-memory, edf10c-environment-identity, edf8-same-vs-mixed | partially reproduced (5) |
| edf1e-hd-proportion, edf4f-change-below-shuffle, edf2ab-jaccard, edf2-no-registration-confound, fig2h-coherent-remapping, edf9-interference, edf10b-per-animal-change | not reproduced (7) |
| fig1k-decoding-across-days | blocked, too_large (1,883 fits × 3.2 s ≈ 101 min, over the 60-min limit) |
| edf7g-waveforms | blocked, data_missing |
| fig3de-probe-memory, fig3e-mvl-delay, fig3fg-probe-drift | blocked, metadata_insufficient |

**2. Dataset, assumptions, questions**

What the dataset holds and where it falls short:
- **Stored tuning curves:** the `tuning_curves` table repeats ROI 0's smoothed curve for every ROI, in 401 of 402 sessions.
- **No registration across protocols:** each protocol has its own CellReg table. The Fig. 3 probe week is the unlabelled first week of the random-order protocol, so its cells cannot be matched to the earlier visits. This blocks all of Fig. 3.
- **Ephys:** the files have no waveforms. They hold 254 PoSub units, the paper's n, plus cortex and CA1 units, and each environment was explored twice where the paper describes once.
- **Session counts:** 402 imaging sessions where the paper says 388, and random-order sessions exist for mouse 5, whose field of view the paper says was lost.
- **Durations:** sessions last 902 to 1799 s where the Methods say 20 min.
- **Related publication:** the metadata points to the bioRxiv preprint, not the Nature article.
- **What checks out:** the clock check passes (imaging and ephys), and the CellReg tables, dates and session numbers are consistent.

Assumptions, each run against the alternatives and recorded with `assumed: true` where the outcome depends on it:
- **Smoothing kernel:** 12° (4 bins). The stored curves match a 4-bin kernel best in 393 of 402 sessions.
- **HDI on the smoothed curve:** this gives the paper's session and pair counts (18, 85 vs 84, 25,441 vs 25,901). Raw HDI flips edf2ab, edf2 and edf4c.
- **Unsigned pairwise offsets:** only these give the paper's shuffle medians (about 52.7° expected, against 90° for signed).
- **Drift rate:** least-squares slope against day difference.
- **Decoder:** HD cells must meet the rule in both sessions, and activity is normalized by each cell's maximum.

Questions for the paper's authors are recorded as three `methods_unavailable` findings (HD rule, offsets and drift, decoders). I asked a reader no questions.

**3. Protocol gaps**
1. "Aim for under ten minutes" can't be met when streaming 402 files takes 16–23 min. I recorded 19 and 32 min.
2. Asset paths don't show the protocol, so the decoding notebook opens every file to select sessions (23 min). The protocol gives no guidance on this; I return a stub for skipped files.
3. Step 1.6 is written per claim, but here one open detail (the HD rule) underlies about 20 claims. I adopted one main reading for all of them, chosen because it reproduces the paper's reported sample sizes on the data. The protocol doesn't say whether that is a valid basis.
4. The chance-level rule says to block when my chance level is far from the paper's. For offsets, the signed reading's chance (90°) is far but the unsigned reading's matches, so I used the match to choose the reading and did not block.
5. Part of edf9's criterion needs a blocked claim (fig3de) that is not listed in `depends_on`. I tested the other parts; they failed, so the outcome is not_reproduced.
6. The line between partially and not reproduced for criteria with several parts is unclear. I used partially when the qualitative effect holds but a numeric part fails.
7. The suggested clock check (decoding with shifted labels) doesn't suit continuous imaging. I used head-direction tuning against time shift instead.
8. pycircstat does not import here (missing `decorator`, numpy 2), so I reimplemented its V-test, Rayleigh and correlation formulas.

**4. Runtime and failures**
The run took about 2 h of the 5 h budget (04:40 to 06:43 UTC). The executed notebooks took 19 min and 32 min. Nothing failed. The repository root has untracked character-device files (`.bashrc`, `scripts`, `.idea` and others, created at 04:39 before I started); they look like sandbox artifacts and should not be committed.
