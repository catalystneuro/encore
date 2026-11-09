I wrote `claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml`, and the quote checker passes on it with 0 problems. Nothing is committed.

**Text read:** the version of record (Neuron 82, 1157–1170) with its Supplemental Information: Figures S1 to S7 legends and the Supplemental Experimental Procedures. Nothing the claims needed was missing, so I never opened the PDF. I read the data descriptor only to see what the data set holds.

**Code read:** github.com/cxrodgers/Rodgers2014 at commit 390b608. It has one folder of scripts per figure, the helper modules, and `metadata/unit_db.csv`. That table holds each unit's include flag, region, auditory-response class and response window. The scripts that set those columns are not in the repository. So every single-unit claim takes its units from that table and is marked `data: with_labels`. Recomputing the auditory-response classification as the Supplement describes is named as a variant.

**Counts:**
- 32 claims, and all 32 have quotes (none needed `inferred`).
- 21 claims carry 27 statistics entries.
- All 32 have a criterion; 23 have expected values.
- 8 are claims of absence, each judged on the paper's own test.
- Areas covered: behaviour, rule encoding, error trials, time course, evoked responses, decoding, posture, mPFC disruption, catch trials and the model.

**Details the paper leaves open, with the readings named:**
- **Benjamini-Hochberg adjustment for rule encoding:** (a) pooled over both regions, as the code does; (b) per region.
- **Auditory-responsive units:** (a) the code table's classes and windows; (b) recomputed per the Supplement. For (b) the trials used, the per-bin threshold, any correction and how atypical units were judged are open.
- **Which 55 sessions the "4 of 55 failed" refers to:** (a) the code table's 55, all marked include; (b) a set before that cut. Also open is which trials count toward the median of 698 per session.
- **Intertrial interval:** between stimulus onsets, or between center-poke starts.
- **Single-unit onset window:** the Results say ±3 s and the code uses ±5 s. I took the Results as the main reading and the code as a variant.
- **Figure 5D (go/nogo after leaving the center port):** the paper gives no test or window. Readings are a 0–3 s mean, or per-bin t-tests as in Figure 5C.
- **"Slope close to 1" (Figure 6C):** no value is given. I judged it by whether the slope's 95% confidence interval contains 1, and the file marks this as my own choice.
- **Movement time:** choice-port entry minus stimulus onset (the code), or minus center-port exit (the legend).
- **Model signal-to-noise ratio:** gain over noise, or over the square root of noise. The Supplement and Figure S7 disagree on whether the noise figure is a strength or a variance.
- **Head-angle differences:** which of 26.9, 36.6 and 24.1° belongs to which session is not said, so they are compared as a set.
- **Disruption analysis:** the code keeps the trials flagged as non-random; dropping them is a variant.
- **Smaller points:** Figure 4A and 4B give the same session's trial counts with the blocks swapped, so the counts are compared as a pair. The paired t-tests in Figure 6E are adjusted only in the code.

**Missing from the paper:** nothing a claim needed. The only gaps are the unit-selection and response-classification steps, whose results exist only as the code's table.
