I judged the one paper the archive names. The match file validates with `python tools/paper_match.py validate papers/match/000235.yaml`, which printed no errors.

**doi:10.7554/elife.83289**, "Model discovery to link neural activity to behavioral tasks" (Costabile, Balakrishnan et al., 2023): **partial**, `by: agent`.

- **Deciding evidence:** the paper's Data availability section lists four dandisets as its raw data (000235, 000236, 000237 and 000238). Its zebrafish results rest on 25 larval fish ("We imaged a total of 750 planes across 25 larval zebrafish"). This dandiset holds only 8 of them, all forebrain imaging sessions under the random wave heat stimulus.
- **Not in this dataset:** the other zebrafish sessions are in DANDI:000236, 000237 and 000238. The mouse cortex analyses use the published widefield dataset from Musall et al. 2019, and the processed data are on Zenodo (7737788). All of these are in `data_in`.
- **What can be tested here:** some zebrafish findings on forebrain neurons. Any finding that pools fish across the whole brain also needs the other three dandisets.

The checks had left this paper without a verdict, so there was no checks verdict to correct.
