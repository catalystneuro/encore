I ran author steps 1 to 6 for wang-2025. Of 30 claims, 2 reproduced, 1 partially reproduced and 25 are blocked; the entry passes its checks and its clean run (1,102 s). I did not commit anything.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| link-authors-deposit (link claim I added) | reproduced: all 16 areas in the authors' area grouping match the dataset's annotations; all 106 of the authors' Fig. 6/7 sessions match dataset sessions (21 mice) |
| data-scale | reproduced: 272,227 units (154,948 `unit_quality` good, 69,453 `classification` good), in 17 areas |
| fig6e-marker-clustering | partially reproduced: Calinski-Harabasz score 5.92 against a null of 1.02 ± 0.33, p < 0.001. Both nose-dominant (3) and jaw-dominant (11) mice occur. The score is outside the paper's 12.57 ± 1.26; it is 7.63 on the authors' 106 sessions and 3.61 to 7.90 across all variants. The outcome is the same under all five seeds. |
| 25 other claims (Figs. 2 to 7, Extended Data, Supplementary autoencoder) | blocked, `too_large` |

## 2. Dataset, assumptions, questions

- **Version.** I pinned 0.230822.0128, the version the paper cites. It holds spikes, trials and the jaw, nose and tongue markers, but no video and no autoencoder embedding.
  - The later version 0.231012.2129 (65.7 TB) adds the raw video. Reading it would take about 1 h per session, about 100 h for the paper's 106 sessions, before training any network. That is why the 25 claims are blocked.
  - Units, trials and markers are identical in both versions for 4 sessions drawn at random.
- **Authors' deposit.** Their Zenodo deposit has no per-frame embeddings. Their Google Drive folder is not pinned, so it cannot be used.
- **Critical finding.** In 5 sessions (SC011 on three days, SC022 on two, February 2019) the marker timestamps step 3.4 ms but the frames are 6.8 ms apart.
  - As deposited, the tongue is visible at 6 to 13% of lick events. With the timestamps stretched by 2 it is visible at 99.9 to 100%.
  - Nothing in the files shows this.
- **Major findings.**
  - In SC026_080719, 117 trial videos do not match the lick events; the cause was not established.
  - SC066_041321 has markers for only 7 trial videos.
  - SC065_050521 has no markers for 140 of its 354 correct trials.
- **Minor findings.**
  - The frame step is a nominal 3.4 ms (294 Hz), where the paper says 300 Hz.
  - Only units with `classification` good carry a brain-area annotation.
- **Session selection.** The paper's 106 sessions come from 21 of the 28 mice, and the paper does not say how they were chosen.
- **Assumptions.** None needed: both decoder readings in the claims file, both epoch windows and all three session sets give the same outcome.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): what is the Fig. 6 choice decoder? It is not described and its code is not public.
- **Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Fields of a link claim.** The protocol does not say which fields a link claim takes; the schema rejects `inferred`. I left out both quote and inferred.
2. **Editing a reader's claim.** The protocol is silent on whether the author may change a claim's `data` or `depends_on` fields. When I used the deposit's area grouping for data-scale, I set it to `with_labels` and made it depend on the link claim.
3. **An outside list used only to select sessions.** It is neither a label nor a measurement, so it fits no data category cleanly. I kept the main analysis on the dataset alone and used the authors' 106 sessions only as a variant, covered by the link claim.
4. **Version choice.** The cited version lacks the input most claims need, and only an unpinned later version has it. The protocol does not say how to block such claims. I used `too_large`, with the read-time estimate printed in the notebook.
5. **Sessions that fail the clock check.** The protocol does not say whether to leave them out of an analysis. I left the 7 sessions that fail it out of the main fig6e analysis and showed them as a variant.
6. **No partial rule.** The fig6e criterion gives only a rule for "reproduced". I applied the protocol's general definition ("present but weaker").
7. **Severity of clock problems.** "Events on different clocks" is critical, but "a clock that could not be established" is at most major. I rated the factor-2 sessions critical, since the stretch proves the mismatch, and SC026_080719 major.
8. **Repeated full runs.** The protocol asks for one run on the whole dataset, but the conclusions must sit in the notebook and any edit forces a full run. I did five full runs of about 18 min each.

## 4. Runtime and failures

- About 2 h 10 min, from 17:38 to about 19:46 UTC. The notebook runs in about 18 min, at most 0.5 GB of memory.
- One known flaw remains: the notebook labels SC066_041321 as having fewer than 20 correct trials of a side. In fact it was not decoded because its marker frames are missing; the attempt record says so.
- To make decoding fit the time, the delay-epoch AUC is computed every 68 ms (17 bins). The decoder fits all folds and penalties at once with Newton's method; it matches sklearn to within 0.01 AUC on a test session.

Files are in `entries/wang-2025/`, `attempts/wang-2025-01.yaml` and `claims/wang-2025.yaml` (link claim added). The verifier package is in `executed/wang-2025/handover/`.
