I finished steps 1 to 6 by 06:11 UTC. The entry, the attempt record and the handover package are written, and `tools/entry.py check` and `run` pass (0 errors, both notebooks pass). I did not commit anything.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| quiescent-window-link (a check I added) | partially reproduced (399 of 455 developmental rows and 56 of 96 DREADD rows match a file) |
| fig1d, fig1f, figs2f-pearson-decline-females, figs2f-pearson-l23-above-l4-p11 | reproduced |
| figs2g-mi-decline, figs2g-mi-male-above-female-p21, figs2g-mi-l4-below-l23, figs4b-mi-trajectory, figs4b-mi-sex-p21 | blocked, methods_underspecified (run, results shown) |
| fig2e* , fig2d, figs3c, figs3d*, figs3e*, fig3a, fig3b*, fig3c*, fig3ef*, fig3g | reproduced |
| fig2f-tcc-increase-l23* | not reproduced |
| fig4b, figs4a, fig4c*, fig4e-tcc-l4-below-l23-p15* | reproduced |
| fig4d | partially reproduced |
| fig4a, fig4e-tcc-maximum-earlier-l23, fig4fgh*, figs4-distance* | not reproduced |
| fig5cd, fig5e, figs6d | reproduced |
| figs6ab, figs6c, fig5fgh*, figs6efg* | not reproduced |
| figs7a-events-clustered | not reproduced (13.6%, 0.31% and 21.6%; the repository's own table gives 13.5%, 0.35% and 21.6%) |
| figs7-method-comparison and the three claims that depend on it (S7, S8) | blocked, `other` (not run within the time) |
| figs5e, figs5f | blocked, `other` (Mendeley deposit is not public) |
| figs9-no-sex-difference-gabaergic-input | reproduced (`histology_figs9.ipynb`) |
| figs9-layer-differences | partially reproduced |

\* The outcome rests on an assumption (`assumed: true`, 13 claims).

## 2. Dataset, assumptions, questions

**What I found in the dataset.**
- **Version.** I pinned 0.250604.1510, the newest published version and the one with more files (422 against 361).
- **Missing subjects.** It holds 32 subjects. Three mice of litter C57-C4-3 have no files, and C57-C6-2-AL has no P13 or P15 files.
- **No behaviour.** There is no behavioural video or quiescent window, although the keywords say there is. I took the windows from the paper's code repository tables at commit 28e1b6d. The check that those windows sit on the files' clock passes: shifting a window by 30 s drops the event-frequency agreement from r = 0.93 to about 0.8.
- **Wrong age.** One file gives the age as P190D; its session date is wrong, and it matches the paper's P11 row.
- **Unknown sex.** Twelve files of two subjects give sex as U.
- **Undescribed events.** `ca_events` matches the paper's Step2 event detection, but its stored values are not explained.

**Assumption.** The Methods and the code disagree on three details: the synchrony threshold, the number of k-means runs, and the participation test. Where these give different outcomes, I took the code's choices. The paper's own per-dataset tables match the code and not the Methods: for example 25.7% non-cluster cells with the code's test, 9.1% with the Methods', 25.0% in the table. Every reading is shown in the notebook.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How was the MI computed? The repository's MI code, run on the dataset, gives values about ten times the table's, uncorrelated with them (r = 0.09), and driven by window length (r = -0.84).
- Which of the three disputed readings were used for the published results?
- The Discussion says about 25% of events are clustered, but the repository's own table gives about 13.5%. Which is right? I recorded this as a `paper_inconsistency`.

**Questions asked of a reader:** none.

## 3. Where the protocol was unclear

1. Step 4 says to block a claim with `data_missing` when its outside input is not public. The rule for `elsewhere` claims, which the checker enforces, forbids `data_missing`. For figs5e and figs5f I used `other`.
2. The protocol has no category for outside data that only selects time windows (neither labels nor measurements). I added a link claim marked `with_inputs` and put it in `depends_on` of the imaging claims, but left their `data: dataset` unchanged.
3. The rule "blocked when your procedure is far from the paper's" is stated only for chance levels. I applied it to MI, whose per-dataset values do not match the paper's.
4. The claims file names the Methods' readings as main, as reader step 2 directs, while author step 1.6 allows adopting the best-supported reading. I adopted the code's readings as an assumption, with the table evidence above.
5. No `blocked_by` category fits "not run within the run's time" for claims stopped by the author's time rather than by computation. I used `other`.
6. "Aim for under ten minutes" cannot be met for 422 fields of k-means at 100 runs. The notebook runs in about 38 minutes, under the 60-minute CI limit.

## 4. Runtime and failures

- **Run time.** The run took about 2 h 50 min (03:22 to about 06:11). The full notebook ran twice (39 and 38 min) with identical numbers, and the histology notebook takes 6 s. The peak memory of a worker was 0.7 GB.
- **Failures during development.** None remain. Two were fixed: a multiprocessing spawn error in the development script, and mixed-model fits with singular matrices, which now fall back to a simpler random structure.
- **Not run:** the other clustering methods for Figures S7 and S8 (cosine and Jaccard k-means, Louvain, DBSCAN).

Files are in `entries/huang-2025/` (two notebooks, `subnet.py`, `README.md`), with the record at `attempts/huang-2025-01.yaml`. In `claims/huang-2025.yaml` I added only the link claim and the `depends_on` lines.
