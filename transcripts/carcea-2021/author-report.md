I've done steps 1 to 6 for dandiset 000114 and run the handover. `tools/entry.py check` reports 0 errors and the notebook runs clean in 65 s. Nothing is committed.

The paper's full text is open access (CC BY, PMC8387235), so I used it, along with its Source Data spreadsheets for the reported numbers. All of it is saved under `paper/`. I pinned version 0.230602.1643. It is the only published version, and the paper cites the dandiset without a version.

**1. Outcomes (19 claims)**

| Claim | Outcome |
|---|---|
| label-link (behaviour labels named through the paper's code) | reproduced (73.3% of nest dwells last 40 s or less; paper 70.5%) |
| ed7a-nest-entry-fraction | partially reproduced (21.6% activated against 26.5%; Fisher p = 1.9e-14) |
| ed7a-shepherding-fraction | not reproduced (1.5%, p = 0.12, against 11.9%) |
| ed7a-dam-retrieval-fraction | partially reproduced (9.8%, p = 9e-05, against 17.4%) |
| fig2j-shepherded-entry | not reproduced (p = 0.182) |
| fig1j-shepherding-rate | partially reproduced (0.65 per h, above 0.2 with p = 0.029, but far below 3.5 ± 0.9) |
| ed8a-dam-retrieval-rate | not reproduced (0.21 per h against about 0.5) |
| ot-pvn-units, ed6, fig1cd, fig2a, fig3fg, fig3ij, fig4c, fig4f, fig4jk, ed9 | blocked: data_missing (10 claims) |
| fig2f-virgin-chasing, fig4i-projection-photometry | blocked: metadata_insufficient |

**2. What I found about the dandiset**
- **What it holds:** PVN units and video annotations for 4 of the paper's 17 recorded virgins (228 units in 8 sessions), raw voltage only for a fifth virgin and for several other sessions, and photometry from 6 non-co-housed virgins. There is no optical tagging and no oxytocin-neuron identity. The code reads that identity from a spreadsheet that is not public.
- **Labels:** none of the behaviour labels is described in the files. The paper's code names three of them (shepherding, nest entry, dam retrieval). One file carries both the code's labels and the paper's names, with identical intervals, which supports the mapping.
- **Unit quality:** in V110 and V111, a median 7 to 9% of inter-spike intervals are under 2 ms, and 79 to 90% of spikes fall within 0.1 ms of another unit's spike. The Methods say both kinds of spike were removed.
- **Same clusters across days:** V111's three days have spike counts correlated 0.93 to 0.97 unit by unit, so they are probably the same clusters. I counted them per day, as the paper does, and gave results per session and per mouse.
- **Clock:** I could not establish that spikes and annotations share a clock in any session.
- **Timing errors:** session start times disagree with the session-id dates (V116, V118). In V116 03102018, spikes and events run to 13.4 h while the raw voltage lasts 4.46 h.
- **Metadata errors:** the photometry animals are described as co-housed, which they were not. Locations and fluorophore are "unknown". The photometry trace is stated in watts with values near 1000, and `commanded_voltage` varies within each session, so it is not a command signal.
- **Learners:** whether each photometry animal learned to retrieve is known for 2 of 6, so the learner and non-learner groups of Fig. 4i cannot be formed.
- **Methods against code:** the Methods cap nest entries at 40 s; the code does not. On this data that changes the activated fraction from 1.0% to 21.6%.
- **Draft:** draft files are 240 B to 6 KB larger. One ecephys file (inside the notebook) and one ophys file (outside it) have the same content as the pinned version; the rest were not compared.

**3. Where the protocol was unclear or missing something**
1. The clock check failed to settle alignment and the protocol does not say what then. I named every session "not established" and recorded it as a finding.
2. The data check already showed counts and durations that decide some claims (the ED 7b fraction, both event rates) before I wrote criteria. I disclosed this in the claims file header.
3. The paper splits its fractions by a label the dandiset lacks (oxytocin identity). I listed two readings, pooled and PVN only, before running the analysis.
4. It is unclear whether reference-only sources belong under `inputs`. I listed the Source Data and said that no values from them enter the analysis.
5. Fig. 4i is blocked for two reasons (learner status, unstated response measure). I gave `metadata_insufficient` as the main one and named the other in the notes.
6. For the oxytocin identity, it was unclear whether to use `data_missing` (no tagging recordings) or `metadata_insufficient` (units present, label absent). I chose `data_missing`.
7. Units that are probably the same across days, without being identical, are not covered by the duplicate rule. I counted them per session and also broke results down by session and mouse.
8. Showing version differences in content is impractical at 387 GB. I compared one ecephys file in the notebook and one ophys file outside it, and said so in the header.

**4. Runtime and failures**
- The notebook takes about 65 s.
- In exploration, h5py's `visititems` hung on the large ecephys files. My first survey of all files hit the 1-hour timeout and a second batch timed out file by file before I found the cause. A plain group walk takes about 1.5 s per file, and `pvn.py` uses it.
- One shell `cd` failed and wrote the README outside the entry. I moved it into place and rewrote `entry.yaml`.
- The untracked dotfiles at the repo root (`.bashrc`, `scripts`, `.idea` and others) are sandbox device mounts, not files I created. There is also an empty `.claude/.cc-writes` directory inside the entry from the harness, which git will not pick up.

Files are in `entries/000114-carcea-2021/`, with the claims file at `claims/000114/10.1038-s41586-021-03814-7.yaml` and the attempt record at `attempts/000114-carcea-2021-01.yaml`.
