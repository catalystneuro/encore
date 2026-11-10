There was one question, and I changed the claims file to answer it.

**imaging-cell-counts: claims file changed.** The question was right: 187.3 ± 8.1 is the number of cells imaged each day summed over the five mice, not per mouse. The paper's own counts show this, without using the dataset's numbers:
- Fig 2j gives 202 rat-responsive cells "from 5 mice across 3 days", and Fig 3e gives 133 USS-responsive cells.
- The text says 74.4% of neurons respond to at least one stimulus.
- At 187.3 cells per mouse per day there would be about 2,810 cell-days, and about 2,090 of them would have to respond. That is far more than those counts allow.
- Summed over the mice there are about 562 cell-days and 418 responders, which fits.

So the 78 tracked cells are also a total over the five mice: 42% of 187.3, the Methods' "Roughly half of all cells could be registered". I updated the statement, both units and the criterion, and removed the two readings of the tracked count. The claim is now reproduced when both counts are within tolerance. I set `answered: 2026-11-10`.

`python tools/claims_check.py` passes all quotes. It still reports two p-values it cannot find (1.8e-05 and 5.2e-05). The earlier check already confirmed both in Supplementary Table 1, where they are printed with a non-ASCII hyphen. Only `claims/kennedy-2020.yaml` and `questions/kennedy-2020.yaml` are modified, and nothing is committed or pushed.
