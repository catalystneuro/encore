I've written the entry at `entries/peyrache-2015`, the record at `attempts/peyrache-2015-02.yaml`, and the verifier's package in `executed/peyrache-2015/handover/`. Of the 35 claims, 32 were tested: 21 reproduced, 5 partially reproduced, 6 not reproduced, and 3 blocked for time. The check passes with 0 errors and the notebook passes the clean run in 12.4 minutes. I did not verify my own work, and nothing is committed.

**Blind status.** I came across part of an earlier attempt's results by accident. The release notes of version 0.261106.1949, returned by the DANDI API when I listed versions, say the conversion "fixes problems found by a reproduction attempt (issue #77)". They also list known gaps, such as Mouse32-140820 lacking head direction and the 8 Mouse20 units on post-subiculum shanks. I did not open the issue, the registry's website or its repository. Every finding in the record was found again from the data in this run.

### 1. Outcomes

| claim | outcome |
|---|---|
| recording-sample | reproduced |
| supptable1-per-animal | partially reproduced |
| hd-cell-fraction | not reproduced |
| hd-fraction-hd-shanks | reproduced |
| ensemble-sizes | not reproduced |
| sleep-duration | reproduced |
| adn-pos-peak-rate | partially reproduced (ratio 3.5 to 4.3, not about 3) |
| adn-pos-hd-information | reproduced |
| supfig2a-unimodality | reproduced |
| fig2a-rates-preserved | reproduced |
| fig2b-pair-correlations-preserved | reproduced |
| fig2f-sws-tenfold-faster | partially reproduced (ratio 12.3 in ADn, 6.1 in PoS) |
| fig2e-decoded-speed | partially reproduced |
| fig2f-rem-similar-to-wake | reproduced |
| fig3a-packet-60-degrees | partially reproduced |
| fig3a-adn-stronger-than-pos | reproduced |
| supfig5-rate-independent | not reproduced |
| fig3b-packet-coherence | reproduced |
| fig4b-noise-correlations | reproduced |
| fig4c-noise-adn-vs-pos | reproduced |
| fig4d-ole-near-bayesian | not reproduced (rests on an assumption) |
| fig4e-ole-covariance | not reproduced (rests on an assumption) |
| decoding-tracks-hd | reproduced |
| fig5b-sleep-tuning-similar | reproduced |
| fig5b-adn-decoded-tuning | reproduced |
| fig5d-adn-predicts-pos-reliably | blocked, `too_large` |
| fig5e-readout-windows | blocked, `too_large` |
| fig5e-adn-predicts-pos | blocked, `too_large` |
| fig6a-fast-oscillation | reproduced (rests on an assumption) |
| fig6b-adn-synchrony | reproduced (rests on an assumption) |
| fig7-adn-pos-connections | not reproduced |
| fig7c-adn-triggered-pos-lfp | reproduced (rests on an assumption) |
| fig7d-same-preferred-direction | reproduced |
| fig7e-driven-pos-hd-information | reproduced |
| fig7e-interneurons-no-difference | reproduced |

### 2. Dataset, assumptions, questions

**Version.** I pinned 0.261106.1949, the latest published version. The paper cites none, and it is the only version whose units carry a brain region.

**What was found about the dataset:**
- **Missing data.** Mouse28-140314 and both Mouse32 sessions hold no head direction, so Mouse32's 35 HD cells cannot be classified. Mouse25-140131 and Mouse25-140204 lack the paper's sleep scoring.
- **Mislabelled units.** Mouse20 has 8 units labelled post-subiculum, though the paper lists no PoS probe in that mouse.
- **Undocumented selection.** In the three mice with both probes, the paper counted ADn cells from 2, 3 and 3 sessions. The files do not say which.
- **Smaller problems.** In Mouse17-130130, spikes run 1101 s past the last sub-recording. Mouse17-130201 has one more head-direction sample than position samples. The wake interval of Mouse12-120808 spans 130 × 97 cm, larger than the 53 × 46 cm arena.
- **What checks out.** Unit counts match Supplementary Table 1 in the thalamus-only mice and in PoS. Head direction equals the LED angle, and spike times are sorted. Spikes and head direction share a clock: the decoding error is smallest at zero shift in all 30 ensembles. The files' own HD classification agrees with reading hd-a for 1007 of 1064 cells.

**Assumptions**, each recorded as a deviation:
- **OLE estimator.** The paper defines no OLE, so I used the standard Salinas and Abbott estimator. For the "signal" version I used the tuning-curve covariance off the diagonal and the observed variances on it.
- **Jitter null.** For the fast synchrony, the null is the expected value of the jittered cross-correlogram, not 100 actual jitters.
- **LFP window.** The spike-triggered LFP uses one 14-minute window per session.
- **Sessions used.** The main analysis uses every session; the Methods' session rule, read from the probe depths, is shown as a variant.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): how the OLE was built; which sessions gave the ADn cells of Supplementary Table 1; how the decoded speed in Fig. 2e was computed.

**Questions to a reader:** none.

### 3. Protocol points
1. The claims file's opening comment says 37 claims; it holds 35. I counted from the file.
2. "Count each recording once" is unclear when the same thalamic cells may recur across sessions at one probe position. I used all sessions and showed the depth-based rule as a variant.
3. The protocol does not say how to handle a session with no sleep scoring. I used its open-field epoch as wake, for waking analyses only, and recorded that.
4. The archive's release notes can reveal an earlier attempt's findings. A blind run cannot read version metadata without seeing them.
5. Many claims list several readings, so some outcomes rest on the one reading that matches (for example HD information under hd-b with means). I followed the criteria and did not mark these as assumptions.

### 4. Runtime and failures
- The run took about 3 h 10 min (11:24 to 14:35 UTC); the final notebook runs in 12.4 minutes.
- Two exploratory runs were cut off and their time lost. A full run with the GLM did not finish in 58 minutes, partly because several processes competed for threads. A later GLM run used the old settings, because an edit had failed after a wrong working directory, and was stopped at 40 minutes after 14 of 21 sessions. That is why the three GLM claims are blocked as `too_large`.
- The executed notebook shows harmless pandas deprecation warnings.
