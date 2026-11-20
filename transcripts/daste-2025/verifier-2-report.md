**Verifier report: daste-2025 on DANDI:000785 @ 0.260520.1603, round 2**

The claims file has 36 claims and the attempt record has 36 outcomes: 20 reproduced, 1 partially reproduced, 10 not reproduced and 5 blocked. Five outcomes rest on an assumption: fig2b, fig2e, fig4ij, figs10e and discussion-differences-grow. Passive notebook = `P`, Go/NoGo notebook = `G`; numbers after them are cell indices.

### 1. Outcomes and assumptions

I agree with 34 of the 36 outcomes. I disagree with one (fig4ij) and agree only partly with another (fig2b).

- **fig4ij-valence-correct-trials (reproduced, assumed): I disagree.** I would give blocked (methods_underspecified).
  - The assumption is stated: correct-trial tables balanced to 3 trials per CS. It is not well supported.
  - The Methods also decode "odor identity for correct trials: Decode the 4 CS on only correct trials" (paper line 513). The notebook says that cannot be cross-validated with 3 trials per CS (G20). So the paper's correct-trial table was probably not a 3-per-CS table.
  - The matched table is also not the paper's: its shuffled level is 65–69%, against the paper's 50%.
  - Under the balanced reading the claim passes only with the maximum aggregate; with the mean, act-early fails (p = 1).
  - The condition "mPFC-p odor not above 50%" is met by accuracies of 27.8% and 31.4%, about 20 points *below* that table's shuffled level of about 51% (G21, G32). A 12-trial decoder that systematically anti-predicts is misbehaving; this does not show mPFC-p at chance. The notes do not mention it.
  - Neither table is credibly the paper's procedure.
- **fig2b-lifetime-sparseness-similar (not reproduced, assumed): I agree only partly.**
  - The assumption (never-active neurons left out) is stated, but the criterion fixes n at 81/84/1978, i.e. every neuron. That argues for keeping them.
  - The two readings that keep every neuron disagree: set to 0, the claim is reproduced (smallest corrected p 0.061); set to 1, it is not (P17).
  - The data therefore do not settle the outcome. I would record methods_underspecified. If the outcome stays, it should stay marked as assumed.
- **figs10e-sparseness-slope-no-difference (reproduced, assumed):** I agree on the criterion's terms. The assumption is stated and is the standard treatment of an undefined value. The outcome is weak: 16 or 8 of 87 neurons are kept, and one fill variant gives p = 0.048.
- **fig2e-reliability (Bonferroni ×3) and discussion-differences-grow (sub-668 left out):** the assumptions are stated and reasonable.
- **fig5e-transferability:** I agree under reading (a). The leave-one-out statement is wrong under the maximum aggregate (see section 2).
- **fig2f-latency:** I agree on the criterion. New observation: projection is confounded with mouse (see section 3).
- **fig3de-concentration-decoding and fig5f-stability:** both are now not reproduced, as I gave them in round 1.
- **The claims file:** I found no new place where it misreads the paper. Point 8 from round 1 (the criterion of discussion-differences-grow) is with a reader.

### 2. Sentences the printed outputs do not support

**Passive notebook**
- **P70 (Summary):** "the counts match the paper's to within 2% for the identity and concentration experiments". Untagged neurons are 1937 against 1978 (−2.1%) and 2132 against 2232 (−4.5%) (P5).
- **P6 and the record's notes for dataset-neuron-counts:** neither says that the measured Go/NoGo untagged mean, 1623.3 (7 mice, days 1–3), is outside 1690 ± 35 (P5). The outcome is unchanged.

**Go/NoGo notebook**
- **G57 and the record's notes for fig5e:** "so the identity part holds in 5 of the 6 leave-one-out sets". This holds only for the mean aggregate. Under the maximum, removing sub-2456 also gives a distal identity difference (corrected p = 0.041, G56), so the identity part holds in 4 of 6. The round-1 response "fails only without sub-2400" is wrong for the same reason.
- **G18:** "Their mean traces still change from the onset frame on (sub-2457 rises from 0.80 to 0.89 by 0.9 s)". The sub-2457 trace starts rising before onset: 0.80 at frame −4, 0.84 at −1, 0.85 at frame 0. sub-2400 and sub-2401 also drift upward before onset (G17). The 0.80 is a pre-onset value.
- **G18 and the record's notes for fig4def:** "rises later and less than in the other mice on all three days: 34 to 51% … against 40 to 85%". The ranges overlap: sub-2456 day 2 reaches 51% and sub-2400 day 1 has 40%. Later in the trial sub-2456 reaches 73–74%, above any sub-2400 session (G17).
- **G18 and the record's notes:** "pre-onset decoding at the shuffled level". The shuffled levels come from the pseudo-population tables, not from per-session decoding. sub-664 day 3 sits at 34–37% and sub-2456 day 2 at 32–39% before onset, which is above the shuffled means of 26–29%.
- **G24:** "every mean above is higher than that". This is true against the shuffled means. Against the 95th percentiles it is not: mPFC-p odor is 36.4% (7 mice, mean aggregate) and 36.2% and 36.1% (8 mice), all below the mPFC-p shuffled 95th percentile of about 37.2% (G21, G23).

**Attempt record notes**
- **fig3bc:** "The mPFC-p fractions are near the 5% false positive level". This holds for concentration and interaction (6.9%), not for identity (15.7%) (P58). P59 says it correctly ("interaction fraction").
- **fig2j:** the sentence about a development run with mPFC-p peaking at 4.75 s has no printed output behind it. It is disclosed as such.

**README**
- The row "Neuron counts of the passive and 30 Hz experiments … | Reproduced" presents part of dataset-neuron-counts as reproduced, while that claim's outcome is partially reproduced. The other rows match the record.

**Round-1 reasons in the record**
- They state my round-1 reasons faithfully, mostly in my own words, close to verbatim.
- The fig4def reason says "about two-thirds" of the day-3 mPFC-p cells. The notebook now prints 61 of 93; my round-1 figure was 59.

All other Result sentences and Summary statements I checked match the outputs.

### 3. Round-1 points: status, and what remains

**Resolved**
- **6 (fig2e):** the ×2 correction is now labelled as the attempt's own reading.
- **7 (fig3de):** a cross-validated peak and a shuffled null were added. The pre-onset offset is still unexplained and is said so.
- **9 (tracked-neuron-counts):** the count over days 0 to 3 only is printed: 43 and 37.
- **10 (`np.clip`):** 0 trial windows are clipped in every experiment.
- **11 (helper tests):** no change was needed.
- **Section C:**
  - Sniff alignment: every onset falls 1–10 ms after a sniff edge (P48).
  - Lick time reference: confirmed (G3).
  - Effective chance: shuffled nulls are now printed (G21).
  - fig2b fill variants: run (P17).
- **8 (discussion-differences-grow):** handled as far as the attempt can. The difference by day is printed and the question is with a reader.

**Partly resolved**
- **1 (sub-2456 and sub-2457 clock).** There is no sign of an early shift, and the onset frames match the files. The per-session check cannot rule out a true onset that is *later* than recorded, since that would look the same as slow responses.
  - The 30 Hz data, which are aligned independently to sniffs, also show these two mice to be slow, in their untagged cells too: medians 4.82 and 4.12 s against 2.70–3.73 s in the OB mice (P50). That favours slow responses in these mice over a Go/NoGo clock error.
- **2 (chance level):** quantified (G21). It now decides fig4ij; see section 1.
- **3 (figs10e) and 4 (fig2b):** both are now disclosed and bounded. fig2b's outcome depends on an assumption that conflicts with the criterion's n.
- **5 (fig5e):** leave-one-out sets were added. Pooling correlated entries remains; the per-mouse reading gives p = 0.6; the 5-of-6 statement needs correcting.

**What remains that bears on a conclusion**
1. **fig4ij:** the outcome should be methods_underspecified. Failing that, the notes need the below-null mPFC-p odor accuracy and the identity-on-correct-trials evidence.
2. **fig2b:** the outcome is not settled under the readings that keep every neuron, which is what the criterion's n implies.
3. **Mouse confound (new):**
   - In the 30 Hz data, within each mouse OB-p is not faster than untagged (2.70/2.70, 3.51/2.97, 4.96/3.73 s). mPFC-p is about as slow as its own mouse's untagged cells (4.59/4.82, 4.79/4.12 s) (P50).
   - So the fig2f latency difference, and similarly fig2g, follows the mouse more than the projection. sub-2456 and sub-2457 are the only mPFC mice in that dataset, and they supply 61 of 93 day-3 Go/NoGo mPFC-p cells.
   - The criteria pool neurons, so the outcomes stand, but the notes should say this.
4. **fig5e:** correct the leave-one-out statement in G57 and in the record.
5. **Not checked:** I still saw only the printed value ranges of the plots, not the images.
