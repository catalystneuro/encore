I've revised the attempt after the round-1 report and re-run the entry. It passes `check` and runs in 15 minutes. The final run gives the same numbers as the run the conclusions were written from, and nothing is committed.

## What changed in the outcomes
- **fig8d-error-outnumber-correct: partially reproduced → not reproduced.** The verifier's call was right. Reading (a) holds (2,825 error-preferring against 2,004 correct-preferring). Reading (b) only reaches 1.81 bootstrap SD under V1, the reading that decides, and the bound is 2. The criterion needs both readings and has no partial outcome. This also matches the two other claims that point the right way but miss their 2 SD bound, which were already not reproduced.
- No other outcome changed. The record now has 13 reproduced, 3 partially reproduced, 7 not reproduced and 10 blocked, and the verifier's outcome matches all 33.

## What I added or corrected
- **Depth and lick times:** the data check now prints every object in a file and every text value of all 105 planes, and searches them for depth, coordinate or layer words. None names a depth or a layer; the only hit is the area names in the keywords. The behavioural events are sample, delay and go in every plane, so there are no lick times. The depth-based blocks stand.
- **Duplicate files:** three pairs (17, 78 and 182 MB) are now compared in full during the run. Every dataset is identical except the identifier and creation date. All pairs are now matched on the first and last 200 frames.
- **figs5-single-coefficient:** with shuffled trial labels, the pure/selective ratio is 0.845 to 0.911 and above one half in all 59 bins. So the criterion is met at chance too, and the notes and conclusion now say so. I also noted that the shuffled labels meet the fig4a and fig4b existence tests, and that fig6-outcome part (a) ignores the 1% false-positive rate.
- **figs4-peak-shift:** I added the peak taken only before the go cue, and only within the delay, under V1 and V2. Before the go cue, MM peaks before ALM in every combination (V1: 2.08 against 4.16 s with T1 bins). That would pass, so the outcome depends on which window the peak is taken over. I added a question to `questions/000015.yaml` and kept the outcome on the whole window until a reader answers.
- **fig8d-mm-object-location (still blocked):** I ran the PT part of (a), which assumes PT neurons are deep as the paper says. MM PT is 0.623 against 0.033 for ALM PT, larger in 0.977 of the bootstrap resamples. But the MM bootstrap SD is as large as the mean, and 280 of the 334 MM PT cells are in 7 planes of one mouse.
- **fig8ef-area-explains-variance (still blocked):** projection type explains more variance than area in every reading (0.0013 against 0.0005), but the bootstrap does not separate them. One correction to the verifier: area below projection type rules out "reproduced", but depth could still make the claim partially reproduced.
- **CRCNS DOI:** the notebook now prints the DOI's DataCite record. It is a placeholder (alternative title "CRCNS.org ssc-8TBD", "not yet available", size "TBD").
- **Notes added:**
  - fig8d-pt-earlier-than-it: the two passing combinations use T2 bins interpolated from frames, so neighbouring bins are correlated.
  - ephys-pt-it-onset-not-detected: the IT baseline SD is only 0.0004, and the PT onset under rule S1 falls in the sample epoch, so the test carries little information.
- The round is recorded under `verifications` in `attempts/000015-chen-2017-01.yaml`, with the verifier's reasons and my responses. The notebook summary, the README and the runtime are updated.

## What I did not do
- **ephys-selective-counts:** I kept the block reason as `other`, not the `data_missing` the verifier gives. The registry check rejects `data_missing` for a claim whose data are placed in another archive; the response in the record explains this.
- **V1 against V2 sensitivity (problem 1):** no change. V1 is the reading the claims file says decides, and V2 is already reported for every claim it touches.
- **fig8ef and fig8d-mm-object-location:** both stay blocked. Their deciding parts need plane depth, which the files don't hold.
