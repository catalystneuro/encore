No outcome changed and none is proposed. The round-2 verifier agreed with all 29 outcomes (19 reproduced, 7 partially reproduced, 2 not reproduced, 1 blocked). I re-ran the entry twice with `tools/entry.py all`. Both runs passed in 8.7 minutes, every number from the earlier run came out the same, and `entry.py check` reports 0 errors.

**New outputs:**
- **figs4h:** the notebook now prints how many sessions meet the first reading of "needed condition": S1 1 of 10, S2 0 of 8, MM 0 of 9, ALM 1 of 13. Cell 56 and the deviation in the record used to leave out ALM; they now name it.
- **fig6ij:** a new cell runs the twelve laser-only CIs with ten other seeds. The failing detection-task MM interval (short laser) excludes 0 in all ten seeds, with its lower bound between 0.040 and 0.053. The other eleven include 0 in every seed. The result cell and the record notes now say this.

**Text I corrected:**
- **"No other optogenetic call changes"** (fig6c notes and Summary): this now applies only to the bootstrap that resamples false alarms too, as the Methods describe, and only to the CIs checked over seeds. It also names the one exception: the figs6b ALM interval under the code's resampling includes 0 on the main draw (+0.002) and is below 0 in 9 of 10 other seeds.
- **Summary seed counts:** these now say "over the main seed and four others". I added that fig2c S1 is within tolerance in 0 of 5 seeds, and that on the five-seed means all areas of fig1h and fig2c are within tolerance.
- **Cell 24:** I removed the clause that claimed the gap rates tell the two readings apart.
- **Cell 39 and fig3b notes:** the shuffled medians are now described as about equal to the larger block's share of correct trials, and the remark about class priors is gone.
- **Cell 61:** now reads "S2 is 0.422 against 0.32, more than 0.1 above it", which no longer hides the failure by rounding.
- **Cell 0:** 141 optogenetic sessions corrected to 130.
- **README:** run time is now "about 9 minutes, close to 3 of them streaming". The new run streamed for 162 s of 8.7 min.
- **New finding:** the three sessions whose shared clock the stimulus-decoding check could not establish, including YT086 2020-03-20 (MM), are now listed in the record. Before, only the notebook named them.
- **Round 2 under `verifications`:** all 29 claims are recorded, with the verifier's reasons and my responses.

**What I left alone, and why:**
- **fig1h and fig2c:** both would be reproduced on the five-seed means. I kept them as verified and did not propose a change, because every bootstrap claim is judged on the main seed, a rule set before the seeds were run. This is recorded in the responses.
- **fig4c and fig4e:** these depend on the units of the soft-normalization offset. Neither the paper nor its code states those units, so I have nothing further to check.
- **The last 20 trials (fig1d):** the data cannot settle whether they are missing. The criterion allows either reading.

I did not commit or push.
