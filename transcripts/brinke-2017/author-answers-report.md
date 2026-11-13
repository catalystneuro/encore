The reader's answer let three of the four depth claims be tested, and all three reproduced. The fourth stays blocked because the paper's file has no depths for the second dataset. The entry passes its checks, ran from a clean environment in 480 s, and the handover is built. Nothing is committed or pushed, and I did not verify my own work.

## The question and what the answer changed

There was one question, on `firing-rate-depth`, which also covered `fig4s1-cs-peak-suppression-not-different`, `fig5ej-cs-pause-cells-shallower` and `fig6g-us-response-depth`. It asked whether these claims could take recording depth from the paper's Source data 1, since CRCNS cb-1 has no depth field.

The reader agreed and changed the claims file. The opening comment now names Source data 1 (`elife-28132-data1-v2.mat` on eLife) as outside data for recording depth. The four claims are now `data: with_inputs`, and their criteria take depth from that file. Statements, quotes and expected values did not change. The answer left the link claim to me.

## What I did
- **Link claim:** I added `source-data-1-link` (kind: link) to the claims file and listed it under `depends_on` for the four claims.
- **Helper:** `ipn.load_source_data1()` streams the file and checks its MD5 (3ca8f91c…).
- **Record:** the file is listed under `inputs` with source doi:10.7554/eLife.28132.
- **Notebook:** it has a new link section, and the four claim sections are re-run with their criteria as the claims file now gives them. Each claim's notes in the record say what the answer changed.
- **Other claims:** I compared all other notebook outputs with the previous run. Only warning line numbers and load time differ.

## Outcomes

| Claim | Earlier | Now |
|---|---|---|
| source-data-1-link (new) | – | reproduced |
| firing-rate-depth | blocked (data_missing) | reproduced, under reading (a) |
| fig4s1-cs-peak-suppression-not-different | blocked (data_missing) | reproduced |
| fig5ej-cs-pause-cells-shallower | blocked (data_missing) | blocked (data_missing), second-dataset depth |
| fig6g-us-response-depth | blocked (data_missing) | reproduced |

- **source-data-1-link:** all 372 cells, matched by order, agree on trial counts, per-trial eyelid closure at US onset and per-trial baseline rate. Shifted by one cell, none agree on the last two.
- **firing-rate-depth:** under the 500 ms baseline reading, the mean rate is 68.3 Hz and Pearson r = 0.086, p = 0.16. The paper gives r = 0.085, p = 0.16. Under the whole-trial reading the correlation is significant (r = 0.146, p = 0.017), so the claim holds under one reading only.
- **fig4s1-cs-peak-suppression-not-different:** no comparison is significant under any reading. The smallest p values are 0.174 for minimum rate, 0.129 for velocity and 0.239 for depth.
- **fig6g-us-response-depth:** the mean depths are 1920, 2061 and 2186 µm, all within tolerance and in the paper's order, with Kruskal-Wallis p = 0.00067 (paper 0.0025). It still holds with depth taken relative to each mouse's mean.
- **fig5ej-cs-pause-cells-shallower:** this one stays blocked. Source data 1 gives `Depth` as NaN for all 102 second-dataset cells, so the second-dataset test cannot be run, and the criterion needs both tests.
  - In the first dataset, CS pause cells are shallower under every reading, and all mean depths are within tolerance.
  - The difference is significant only under the mean readings with class (b): 2 cells against 86, p = 0.048.
  - Under the drop readings, with 7 to 9 CS pause cells, p ranges from 0.11 to 0.34.

Counts over the paper's 55 claims went from 10 blocked, 18 partially reproduced, 22 reproduced and 5 not reproduced to 7 blocked, 18, 25 and 5. The link claim is counted separately.

## Findings
- I updated the existing data finding: the dataset still has no recording depth, and Source data 1 supplies it only for the 270 first-dataset cells.
- I added a finding about the paper: Source data 1 has no second-dataset depths, although Figure 5J reports them.
