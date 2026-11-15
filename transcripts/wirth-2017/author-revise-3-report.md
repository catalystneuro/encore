The verifier agreed with both proposals in round 3, so neither proposal is still open.

**Outcomes changed**
- **direction-center-vs-periphery**: changed from partially_reproduced to blocked (`metadata_insufficient`). Reading (a), the direction-selective cells, meets neither level. Reading (b) needs the paper's set of responsive cells, which needs the point-of-gaze space. The three-space cells and the full set of cells give different results, so the paper's set could land at any level.
- **direction-tuning-not-maintained**: changed from not_reproduced to blocked (`metadata_insufficient`). Reading (a) fails on the number of cells tested: 40 or 28, against 56 ± 5.6. Under reading (b), sets that meet the criterion and sets that fail it both exist between the two bounds.

On both claims I removed `proposed`. I also removed `assumed: true`, which goes beyond "change nothing else": the entry's check failed because the schema does not allow `assumed` on a blocked outcome. The deviations stay, and the round-3 responses say why `assumed` went. No other outcome changed.

**Other updates**
- I updated the notes, the notebook's two conclusion cells, the header table and the summary, and the README. The blocked row in the README now counts 13 claims, up from 11.
- Round 3 is recorded under `verifications`, with one result per claim. Each gives agrees: true, outcome blocked, the verifier's reason and my response.
- The verifier also said the claims file's reading of the 56 cells fits reading (a) better than reading (b). It said this changes neither verdict. Following the protocol, I added it as a question in `questions/wirth-2017.yaml` and did not change the claim.

`python tools/entry.py all entries/wirth-2017` passed with 0 errors, and the notebook ran in 1,589 s. The re-executed cells 42 and 45 give the same numbers the text cites. Nothing is committed. The changes to `tools/` and the untracked dotfiles were there before this run, and I did not touch them.
