I've revised the attempt for every point in the round-1 report and re-run the entry with `python tools/entry.py all`: it passes in 17 minutes and `check` reports 0 errors. Every conclusion, the record, the README and the summary now match the new numbers. Nothing is committed.

The outcomes are now 12 reproduced, 6 partially reproduced, 4 not reproduced and 18 blocked (11 because the method is underspecified, 7 too large). Many outcomes changed because the fix to the sleep-like detector changes which epochs and units enter the self-organizing map (SOM), so the retrained clusters and their category numbers change too. The four outcomes that moved this way are marked as resting on that assumption, and their notes give the round-1 result.

**What I changed in reply to the report**
- **Sleep-like detector (problem 1).** Detection now pools the cortical units of all probes in a session; the Methods say "detected per recording session". A session gets no detection if the detector marks 1% or more of the time in a random-firing (Poisson) population at the same rate. I added the per-probe table the verifier asked for: unit count, rate, that null rate, an EMG check, and the paper's own result.
  - The paper's Zenodo files hold its own detection. They mark 19 recordings as not using it, a step the Methods don't describe; I added this as a finding and a question to the authors.
  - Median sleep-like time is now 9.9% per recording (it was 20.2%; the paper reports 6%). `extfig1-epoch-counts` stays not reproduced. Even the paper's own sleep-like periods give 1.5%, 248 and 21.5 on these recordings.
- **12-epoch rule (problem 2).** The unit counts now follow the Unit quality control passage: at least 6 spikes in 12 spontaneous epochs. `dataset-ki-counts` becomes reproduced (24,898 units, 52.4% in the PFC, 99 recordings, 13,040 PFC units). `fig1h-waveform-classes` becomes reproduced (19,731 / 4,247 / 920); the other epoch rules each miss one count narrowly. I also added counts with the paper's Zenodo quality flags.
- **Using 000473 more widely (problem 3).** The main analyses stay on 001260, since the protocol has the analysis run on the dataset's own data. I added variants on the paper's 42 dataROI polygons (fig4e, fig5cd, fig5e, fig5i) and on all of dataset KI (fig4e).
- **Category numbering (problem 4).** I quoted the `relabel_clusters.py` lines; they confirm the helper applies the code's permutation in the right direction. As a variant, I projected the units onto the paper's own trained SOM from Zenodo. There the categories match the text's descriptions, and 4 of the 8 claims blocked on numbering hold. The claims file's rule keeps those 8 blocked.
- **Problems 5 to 9.** The notebook now says an E-score is significant at a 10% two-sided level, and fixes the fig5e wording to one reference. I noted the 425-node grid; the 8 PCs now explain 95.1%. I noted the forced complement in extfig5g.
- **Other outputs asked for.** fig2j now also runs on the 9 regions with the most narrow-waveform units. For fig4g I added the ranks of GaoROIs 19, 20, 41 and 23 (6th, 8th, 11th and last of 29) and their unit counts.

**Outcome changes**
| Claim | Round 1 | Now |
|---|---|---|
| dataset-ki-counts | partially reproduced | reproduced |
| fig1h-waveform-classes | partially reproduced | reproduced |
| extfig1d-sleep-like-differ | reproduced | partially reproduced (firing rate no longer differs, p = 0.14) |
| fig2g-pfc-regular-enrichment | blocked | reproduced |
| fig2f-low-rate-less-stable | blocked | partially reproduced |
| extfig3f-layer-enrichment | blocked | partially reproduced |
| extfig5g-nw-enrichment | not reproduced | partially reproduced |
| fig2j-nw-ww-correspondence | partially reproduced | not reproduced (as the verifier gave) |
| fig4e-activity-modules | partially reproduced | blocked (the claim's two readings of "ILA-specific" disagree) |
| fig4g-gao-category1 | not reproduced | blocked (the category numbering now changes the outcome) |

**Disagreements I kept and recorded under `verifications`**
- **fig3a, fig5i, fig4g-pl-orbl-extremes:** still blocked. fig3a is now blocked by the numbering rule and fig5i by its dependency on an IBL claim. fig4g-pl-orbl-extremes is blocked because its readings disagree.
- **supptable5:** still blocked, because it depends on fig3a.
- **fig5cd:** kept as partially reproduced; the verifier gave not reproduced.
- **IBL claims:** kept as too large, where the verifier gave data missing. The IBL data are public, so the protocol doesn't allow data missing.

**Added**
- `questions/001260.yaml`, a question for a reader: does Fig. 4g number the GaoROIs as the Zenodo table does?
- Two new methods-unavailable findings, a new set of inputs, and the round-1 verification block.

**Not done**
- The IBL claims were not attempted.
- Tone responses were not computed for 000473, so fig5cd and fig5i use 001260 units only.
- After the run I changed only docstrings in `pfcki.py` and one markdown sentence, which I updated in the executed copy too.
