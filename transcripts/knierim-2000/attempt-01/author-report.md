I finished steps 1 to 6 for dandiset 001754. The entry passes `check` and runs from a clean environment in 70 s. Of seven claims, two are reproduced, one partially reproduced, one not reproduced and three blocked. The paper (doi:10.1038/72910) is not open access, so I used only its abstract and the titles of its three figures, saved in `paper/abstract.txt`. I pinned 0.260728.1352: the paper cites no DANDI version, and all three published versions hold identical files, differing only in metadata.

## 1. Outcomes

| Claim | Source | Outcome |
|---|---|---|
| `flight-spatial-code` | Abstract | Partially reproduced. On flight day 9, 13 of 25 Rat1 units are significant against shuffles, but only 3 of 28 Rat2 units, which is chance level. |
| `three-orthogonal-surfaces` | Abstract | Blocked: metadata insufficient. Nothing maps pixel positions to the track's three surfaces. |
| `si-comparable-to-preflight` | Dandiset description | Reproduced. Spatial information 1.385 in flight against 1.448 bits/spike preflight, p = 0.45. |
| `fd4-abnormal-selectivity` | Dandiset description | Not reproduced. Flight day 4 is lower (1.214 against 1.441 bits/spike) but p = 0.055, just above the 0.05 threshold. |
| `fig3-stability-across-sessions` | Figure 3 title only | Reproduced. Median correlation 0.538 between Rat3's two Escher staircase sessions, against a null 95th percentile of 0.091. It drops below the 0.5 threshold with lighter smoothing. |
| `theta-normal` | Dandiset description | Blocked: data missing (no EEG). |
| `ripples-normal` | Dandiset description | Blocked: data missing (no EEG). |

## 2. What I found about the dandiset

- **Shared position trace:** the Rat1 and Rat2 files from the same flight day contain the same position trace (99% of matching samples agree within 2 px).
  - Rat1's units are spatially selective with it. Rat2's are not, in any window.
  - In Rat2's flight day 4 staircase session the trace behaves like Rat1's position, so whose position it is during Rat2's sessions can't be established. This probably explains Rat2's poor result in the first claim.
- **Position only at spike times:** position is stored only when a unit fires, so occupancy can't be rebuilt from it. The preflight files have no position at all.
- **Rate maps can't be linked to units:** the rate-map file names are old Windows short names (`ESCELL~1`, `ES2BC0~1`). The `cell_number` column is read from the `~N` suffix and is not a cell number. It matches the best-fitting unit in only 84 of 211 cases.
- **Undocumented values in the maps:** `-999` marks unvisited bins, which the column description doesn't say. The tracker's "position lost" value (0, 255) was counted in the original occupancy, up to 19% of a map.
- **Duplicate maps:** 8 rate maps are identical copies of another map in the same file, some filed under a different tetrode.
- **Units across epochs:** each unit merges per-epoch spike files with the same tetrode and cluster id. Nothing says these are the same neuron. The unit table also lacks the `session_type` and `source_file` columns that the conversion README lists.
- **Spike times** are rounded to 10 ms in five files, and 2 to 15% of the intervals within a unit are zero.
- **No EEG**, although the dandiset description reports theta and ripples.

## 3. Where the protocol was unclear or didn't fit

1. With only a three-sentence abstract, the protocol doesn't say whether other summaries of the paper can be claim sources. I used the dandiset description and one figure title, labelled as such in each claim.
2. For "no difference" claims the protocol says to use the paper's own test, which can't be known without the text. I fixed a Mann-Whitney test in advance and recorded it as a deviation.
3. The check that spikes and position share a clock assumes trial tables or continuous annotations; here there are neither. I used occupancy-map matching plus a test of each rat's units in the other rat's sessions. It doesn't say what to do with a session that fails the check; I tested Rat2 anyway and noted it.
4. The protocol only covers linking outside data; a broken identifier inside the dandiset (rate maps to units) has no rule. I reported it in the data check and as a finding, not as a claim.
5. The duplicate check is about recordings deposited twice; it doesn't cover one trace shared by two subjects, or copied maps. I reported each pair.
6. "Read the code the paper links" didn't apply, since the paper links none. I read the dandiset's conversion code (catalystneuro/mcnaughton2000-to-nwb at b538d9e).
7. I correlated unit spike maps with the rate maps (same binning) before writing the criteria. The claims file's opening comment says so.

## 4. Runtime and failures

The notebook runs in 70 s; loading the eight files takes about 13 s. My first execution failed on a comparison of epoch lists with different lengths, and I fixed it. I did not open NASA's 272 MB processed archive, so "no EEG there" rests on its file listing. Files are written but not committed, and the verifier package is built in `executed/001754-knierim-2000/handover/`. The untracked dotfiles in the repo root were created by the sandbox, not by me, and I left them alone.
