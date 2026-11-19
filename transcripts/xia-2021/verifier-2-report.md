**Verifier report: Xia et al. 2021, attempt xia-2021-01, round 2**

The claims file has 29 claims. The attempt record gives 4 reproduced, 5 partially reproduced, 3 not reproduced and 17 blocked: 15 for missing data, 1 for insufficient metadata and 1 as not runnable. The notebook tests 12 claims (cell 0).

### 1. Outcomes

| Claim | Agree? | Notes |
|---|---|---|
| fig2d-hplc-yield (partial, assumed) | Yes, by the letter of the criterion | Reading (b), a straight line under each peak, gives 77.5–83.1% (4 of 18 readings; cell 21). The volumes cannot be tested without a flow rate, so partial is the most the attempt can give. The assumption (the second peak ends where its descent ends) is stated and reasonable. **But** the passing reading's line runs from the valley and cuts away 46% of the main peak (area 27.25 → 14.61) and 70% of the second peak (12.71 → 3.86). Cell 20 says itself that this line "cuts through the second peak". Every reading that splits the overlap the usual way gives 65.8–69.1%, just below the 69.3% floor. The conclusion should say this. |
| fig2e-page-bands (reproduced) | Yes | Cell 24 bears it out. |
| figs5-btx-staining (reproduced) | Yes | The judgement is by eye. Nearness to GFP beats chance in 3 of 4 images (0.82 vs 0.37 in the low-magnification projection). |
| fig3d-sensor-on-soma (partial, assumed) | Yes | Coincidence beats the shifted null in 4 of 5 images. The soma localisation is at chance, and (b) is 0.09–0.35. The assumption is stated and reasonable. |
| fig4b-michaelis-menten (not reproduced, assumed) | Yes | 0 of 80 readings. The onset assumption is stated, and a single common onset still gives Km 0.545 µM. |
| fig4b-lod (not reproduced, assumed) | Yes | 0 of 160 crossings. Reading (c) is still not run, and the record says so. |
| fig5b-in-vivo-response (not reproduced, assumed) | Yes | dF/F is 17.1–40.1%, and 0 of 144 readings fit. The assumption about which recordings stand for the three mice is stated. |
| fig6-vesamicol (partial, assumed) | Yes | One experiment of four. The reduction is within tolerance in 44 of 48 readings, and the 17% example depends on the ROI. Note that the main reading's bin test gives p = 0.0103, which is not below 0.01. |
| figs16-af647-stable (reproduced, assumed) | Yes | The channel assignment is stated as an assumption. |
| fig7-rostral-caudal (partial, assumed) | Yes, with a caveat | The order holds in 18 of 18 variants, and no time is within tolerance in any of the 36. Both the substitute for AQuA and the orientation are stated. However, the order would reverse if the frame were flipped. Rostral-up rests on a comparison with Fig. 7A made outside the notebook, and the notebook says that comparison "decides nothing" (cells 47, 11). In fact it decides the outcome. |
| fig7-peak-timing (reproduced, assumed) | **No.** I would call it partially reproduced at most | It passes only under reading (ii), timed from each region's onset (30 of 36 variants). Those onsets come 2.75–3.3 s after the paper's for the rostral region, and the parent claim matches 0 of 6 times. Timed from the stimulus, reading (i), it fits in 0 of 36 variants and 0 of 157 blocks. Reading (ii) applied to the paper's own Fig. 7B times gives 8.8 s for the rostral region (22.0 − 13.20), outside 9–16.5 s. The claims file flags the paper's contradiction only for the caudal region. |
| figs12-3v-propagation (partial, assumed) | **No** | The criterion grants partial "when two of three show the order". Only one mouse is deposited, so that threshold cannot be reached. The amplitude part holds (6 of 6 readings), and the order holds in 12 of 18 variants on the median onset and 11 of 18 on the earliest block. These results should be reported without the label "partial", or the claim should be blocked for the two missing mice. |
| 17 blocked claims | Yes | sub-4 is now shown to hold a single response (cell 10), so fig5e is blocked. For figs9, I accept "not_runnable" on the author's citation of docs/protocol.md, which I cannot see here. |

### 2. Sentences the printed numbers do not support

- **Cell 22:** "From 21 to 30 min the signal is 0.09 to 0.25, two to six times the pre-injection level". Cell 21 prints a minimum of 0.055 for 27–30 min, about 1.3 times the pre-injection level. "the 5.2-high valley" is not printed anywhere in this run.
- **Cell 28:** "(11.4 to 64.4 with the first rule…)". The first-rule densities printed in cell 27 are 17.79–64.41. The attempt record correctly says 17.8–64.4.
- **Cell 46 and the figs16 notes in the attempt record:** AF647 "recovers by 11.1 to 16.5% from that minimum without passing its pre-stimulus level". In 4 of 6 readings the rise from the minimum exceeds the drop: for the own tissue mask with fit a, 15.76 against −13.00; for the whole half with fit a, 16.50 against −15.16. The trace therefore passes its pre-stimulus mean, though not the mean + 3 SD.
- **Attempt record, methods_unavailable finding, question (2):** "giving 17 to 37% against 3.7%". This is stale; the current range is 17.1–40.1% (cell 39).
- **README:** "It takes about two to three minutes". Cell 56 prints a total of 98 s. This is minor.
- Everything else checks out against the notebook's printed outputs. That covers every other Result sentence, the Summary, the rest of the README table (including the "(16 claims)" row) and the other notes in the attempt record.
- The attempt record's verification entries state my round-1 reasons accurately and in substance, including problems 3–8, 10, 11 and 13 folded into the claim reasons. Problem 12 (the docstring) is not restated, but it bore on no conclusion and is now fixed (`xia2021.py:35`).

### 3. Round-1 points

**Resolved:**
1. Circular flow rate: the volumes are no longer tested.
2. Peak limits: the ends of the second peak are varied. My estimate of about 69–70% is confirmed at 68.2–69.1%.
3. k-frame rates: they now start at each trace's departure from baseline.
4. Bleaching fit absorbing the response: a 180 s variant was added; sub-2 is still above baseline at 120 s.
5. Dark level: shown as a variant.
6. fig3d threshold: a new rule plus a shifted null for both masks.
7. Noise puncta in figs5: much reduced.
8. fig4b onset: now plotted, with a common-onset variant.
10. fig7 and figs12: now tested; the not_runnable question is addressed by citation.
11. Paired t test over frames: a test over 10 s bins was added.
12. Docstring: fixed.
13. Dependence of the fig6 ratio on the ROI: stated.
14. Channel assignment: stated.
- All section C requests were met.

**Remaining, bearing on a conclusion:**
- **fig2d:** the share passes only under a baseline line that the notebook itself says cuts through the peaks. The conclusion should say so.
- **fig7-peak-timing:** "reproduced" rests on late substitute onsets and on reading (ii), which the paper's own Fig. 7B times fail. Partial at most.
- **figs12:** partial does not meet the criterion's threshold of two of three mice.
- **fig7 and figs12:** the direction of propagation depends wholly on an orientation checked outside the notebook.
- **Item 9 (does not change an outcome):** LLOD reading (c) is still not run.

**Claims file:** I found no misreading of the paper beyond the fig7-peak-timing point in section 1. Reading (ii) does not fit the paper's own rostral times, and the file flags the contradiction only for the caudal region.
