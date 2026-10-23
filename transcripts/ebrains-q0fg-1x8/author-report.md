I did steps 1 to 5 of the Author section and built the handover (step 6). The entry passes `check` and all six notebooks pass `entry.py all` in the clean locked environment. Nothing is committed.

Entry: `entries/ebrains-q0fg-1x8-nagelhus-2023/`. Record: `attempts/ebrains-q0fg-1x8-nagelhus-2023-01.yaml`. Questions: `questions/ebrains-q0fg-1x8.yaml`. Version: v1, the only published version; its DOI is the one the paper cites.

## 1. Outcomes (57 claims)

Totals: 25 reproduced, 2 partially reproduced, 7 not reproduced, 23 blocked (18 methods underspecified, 4 data missing, 1 other).

| Outcome | Claims |
|---|---|
| reproduced | cell-counts, fig2d-spatial-change-no-o, fig2d-o-om-change, fig2d-om-no-prime-change, fig2d-no-no-prime-change, fig3b, fig3c, fig3d, fig4b, fig4c, fig4h, figs5a, figs5b, figs5c, figs5f, figs6k, figs6l, tables1, fig5b-words, fig5bc, fig5e, figs7cd, figs7e, figs8, figs8eh |
| partially reproduced | figs4-object-traces, fig6ab |
| not reproduced | figs3a (CA3 fraction), figs5ghi, figs6 (occupancy decoder depends on distance), fig5b-counts, fig5-entropy, fig6ef (the lowest-tuned 20% reverse the decline), figs5jk (walls) |
| blocked, methods underspecified | fig1c, fig1d, fig1e, fig1f, figs2e, fig2d-rate-overlap, fig2-fraction, figs3f, figs2d, ovs, fig4e, figs5e, figs5l, figs5m, fig6c, fig6d, fig7, fig7-slope |
| blocked, data missing | fig1g, fig1h, figs2c, figs6hij |
| blocked, other | figs5d (only one control session has at least 25 cells) |

## 2. The dataset, and the questions asked

What I found in the dataset:
- **Main error:** in both Neuropixels population files the tracking y is a copy of x in every sample. The CA1 single-cell file holds the same two recordings with the same timestamps, x and spike trains, and a correct y. The decoding notebooks use that copy, and a variant shows the deposited tracking.
- **Missing:** no cell identities across days or day of exposure, no implant sites, no head direction.
- **Unlinkable units:** 283 of the 425 tetrode population units cannot be matched to the single-cell file.
- **CA3 count:** the CA3 file has 341 cells from 4 rats; the paper counts 313.
- **Object positions:** in one CA3 session the Object and Object Moved positions are the reverse of the protocol.
- **Spike times:** 3 CA1 units have spike times out of order.
- **Inclusion rules:** a few units break the paper's inclusion rules as computed from the trials.
- **Gaps between trials:** some last hours, against the 1 to 3 min in the Methods.
- **Unit field:** the tracking unit is a MATLAB string object that scipy cannot read; it says "centimeters" when decoded from the raw bytes.
- **Matches the paper:** 1,189 CA1 cells, 219 CA1 controls and 16 decoding sessions, which is the legends' count (the Methods say 15 tetrode sessions).

Questions asked (8):
1. How unvisited bins enter rate-map smoothing (readings `rm` a and b). This one decides several blocked claims, fig1c among them.
2. Whether a field's 1 Hz rule applies to its peak or to every bin.
3. The vector-map bins and smoothing for ovs-method-extra-cells, which the claims file leaves to two references.
4. Which occupancy and which testing samples figs6l uses.
5. How testing samples are formed under figs5f reading (b).
6. Which values the figs7cd rank-sum compares.
7. Which rate maps the population vector correlation uses.
8. Which mean rate the spatial information uses.

## 3. Where the protocol was unclear, wrong or missing something

1. **Do the author's own readings have to agree?** The protocol does not say whether readings the author adds for a detail the claims file leaves open must agree, the way the reader's do. I treated them as needing to agree. That is the main reason for the 18 methods-underspecified blocks.
2. **The block cascade.** "A claim that depends on a blocked claim is blocked" also blocks claims whose result is the same under every reading (fig1f is reproduced under all of them). I followed the rule and gave the results in the notes.
3. **How to combine readings.** When a criterion names readings but does not say "under one reading", the protocol does not say how to combine them. I required them to agree.
4. **Correcting one file from another.** The protocol does not cover fixing a data error in one file with another file of the same dataset. I did it, showed the deposited version as a variant, and recorded it as a finding.
5. **Seeds can change outcomes.** The protocol assumes a random seed cannot change an outcome, but figs5e's five t tests can flip. I blocked it under the readings rule and said so in the notes.
6. **Expected value against criterion.** For tables1 the criterion passes but H (28.4 to 32.8) is outside the expected 25.06 ± 2.5. I recorded it as reproduced and noted H.
7. **No partial rule.** Where a criterion defines no partial outcome, I used "partially" when some of its parts hold.
8. **Runtime.** The 10-minute aim does not fit 57 claims run under four reading combinations. I split the work into six notebooks of 4 to 19 minutes, each under CI's 30-minute limit.
9. **archives.md for EBRAINS.** It gives no way to list versions: the Knowledge Graph record shows only v1. It does not suggest recording file hashes, so I printed the data proxy's MD5s. It does not mention MATLAB string objects, which I decoded from the raw bytes.
10. **Clock check.** Here trial membership comes from the file structure, so the suggested check does not fit. I shifted spikes against positions instead: within-trial stability peaks at zero shift in 90 of 91 sessions.

## 4. Runtime and failures

- **Runtime:** the full clean run took 66 minutes: notebook 1 4 min, 2 19 min, 3 8 min, 4 19 min, 5 10 min, 6 6 min.
- **Fixed along the way:**
  - Notebook 2 first took 37 minutes and was cut to 19.
  - The first decoder runs used the broken Neuropixels tracking; all were re-run on the corrected copy.
  - Some conclusion text was changed after the final run. I copied it into the executed copies, after checking that every code cell is unchanged.
- **Nothing fails at the end.**
- **Sandbox artifacts:** the sandbox left untracked placeholder files in the repo root (`.bashrc`, `.gitconfig`, `.mcp.json`, `.idea`, `scripts` and others, all `/dev/null` character devices). I did not create them and left them alone; they should not be committed.
