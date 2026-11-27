I've finished the round-1 revision. The entry was re-run with `python tools/entry.py all entries/gillespie-2024`; it passes in 627 s and `check` reports 0 errors. The record's numbers and conclusions match that run. Nothing is committed.

**Outcome changes**
- **fig2s1h-control-dwell-increases** changed from reproduced (resting on an assumption) to partially_reproduced, as the verifier argued. r is positive in all four rats under one leaving reading and in three under the other, and neither the paper nor its code chooses between them. The outcome is now the one both readings give, and the question to the paper's authors stays (finding 8).
- All other outcomes are unchanged. I kept two and recorded the verifier's disagreement:
  - **fig1s1c-prereward-dwell-matched** stays partially_reproduced; the verifier would say not_reproduced. Two of three rats are within the criterion's 10% (three of three under the final 7 days).
  - **fig5b-redundant-search-balanced** stays not_reproduced; the verifier would say partially_reproduced. The criterion has no partial level, and one rat has p < 0.05 under the adopted plateau reading.

**Added or corrected, by point in the report**
- **Data-elsewhere claims (point 1):** docs/protocol.md (Author, step 1.4) says to test them on the data the paper deposited, listed under inputs and counted apart. They stay tested, and the notebook header now says why.
- **Pre-reward start (point 2):** the Methods passage that supports starting at the first entry ("from initial center port nosepoke") is now cited. The sanity cells count withdrawals per rat: the beam flickers within most nosepokes, but only 3 control trials and 124 neurofeedback trials have a withdrawal longer than the 200 ms the task script allows. The other reading (start after the last such withdrawal) now runs for fig1s1c and both speed claims:
  - fig1s1c: bernard goes from 10.2% to 16.1%, still two of three rats within 10%.
  - Both speed claims are unchanged.
- **Mixed models (point 6):** they are now fit by maximum likelihood, MATLAB fitlme's default. The p-values moved and every conclusion and note was updated, for example fig5a's delay-against-control p is now 0.062 to 0.14 under reading (b). No outcome changed.
- **000629 position scale (point 5):** I corrected the sentence that said the head positions span the same range as in 000115. The notebook now prints both per-epoch distributions, and the deviation says the data do not confirm the scale. The largest neurofeedback median would stay below 4 cm/s under a scale up to 80% larger.
- **Goal carry-over (asked for under C):** 8 of 59 epochs start with the previous epoch's last goal, holding 39 of 3201 search trials, too few to matter.
- **Rat 1's port events (asked for under C):** a raw excerpt of remy's pump events now prints next to a normal rat's. It shows the same timestamp repeated with toggling values.
- **Finding 1:** I had said no tetrode location is recorded. The verifier found that the electrode groups are labelled `ca1`, `bad_ca1`, reference, `dead` or `lost`. The statement is corrected (they still don't say which tetrodes are in the cell layer) and the severity lowered from major to minor. No finding is rated critical.
- **Stale text:** I fixed notebook text that still said every neurofeedback claim was blocked.
- **Verifications:** round 1 is recorded under `verifications`, with the verifier's reasons and my responses, for the 17 claims it gave outcomes for.

**Not done**
- **fig2s1f-control-rate-increase and fig2b-control-timecourse (point 9) stay blocked as too_large.** The verifier thought a subset of epochs would be feasible. I tried and found it is not, within the 60-minute notebook limit:
  - h5py reads the raw data at under 2 MB/s in total, however many threads read at once.
  - With parallel direct range requests, 180 s of 10 `ca1` tetrodes took about 2 minutes to read.
  - The smallest subset the Figure 2B criterion allows (two epochs per rat) is therefore about 2 h in four processes, before any SWR detection.
  - A one-session trial run outside the notebook did not finish within an hour.
  
  The timing is now in the cell tagged `too-large-estimate`, and the reading code is kept in the helper.
- **No question was added to `questions/gillespie-2024.yaml`**, because the verifier reported no place where the claims file misreads the paper.

The paper should be listed on DANDI:000629, the neurofeedback cohort it deposited. The record still uses it as an input.
