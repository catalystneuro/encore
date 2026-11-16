No outcome changed in this round. The verifier agreed with all 26 outcomes, and I found nothing that calls for a `proposed` change. That leaves 20 claims blocked as methods_underspecified, 5 blocked as data_missing and fig1-model-neurons partially reproduced. I re-ran with `python tools/entry.py all entries/elie-2019`: it passed (1666 s) and the checks report 0 errors.

**Output added**
- **Anatomy gap:** the verifier noted that the notebook did not list the attributes under `class_info` and `extra_info`, and read only some attributes of the stimulus groups. `elie.py` now collects the attribute names of every group and dataset in each file, and cell 16 prints them across all files. Nothing under `class_info` or `extra_info` carries an attribute, and no attribute anywhere is an area or a coordinate; only site, electrode and depths are stored. The cell 17 conclusion and the five anatomy notes now say this.
- **Clock check:** cell 9 now prints the ranges before and after onset.
- **Model neuron (cell 27):** it now prints the model rate's largest cumulative information next to its last bin. It also prints the model's spikes per trial next to the observed ones.

**Text corrected**
- **README:** the row for the claims on the 404 and 337 units said 19 claims; it is 18, so the rows now add up to 26.
- **Cell 10:** it now matches cell 9's output: 0.5% to 1.3% of units before onset, 6.33 to 6.41 spikes/s, 42.2% to 65.3% after onset, peak 23.30 spikes/s.
- **Model rate figure:** cell 29 and the fig1 notes quoted 1.956 bits as the model rate's cumulative information. That is the last bin; they now also give the largest value, 1.990 bits.
- **fig1 deviation:** "11.8 against 12.1" was wrong. The printed values are 12.0, 11.0, 9.0 and 10.5 spikes per trial against 12.1, 8.3, 8.5 and 11.4 observed, and the deviation now gives these.
- **Cost estimate:** the 13 notes that said "118 to 120 h in three runs" now give this run's printed estimate, 128 h on one core. The verifier saw 117 h; the time per estimate varies between runs, and "more than 100 hours" still holds.
- **Round 2 record:** added under `verifications` in `attempts/elie-2019-01.yaml`, with the verifier's reason and my response for each of the 26 claims.

**Not done**
- **Questions file:** I added nothing to `questions/elie-2019.yaml`, because the verifier found no place where the claims file misreads the paper.
- **Round-1 reason for fig1:** I left it as recorded. The verifier said the omission of its MATLAB remark does not misrepresent it.
- **General points:** the record has no field for points that apply to the whole round. So I attached the cell 10 point to units-404 and the README point to the 18 claims it concerns.
- **Other changes:** the working tree also has edits under `tools/` that were there before this run. I did not touch them. Nothing was committed.
