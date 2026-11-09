I've finished steps 1 to 6 of the Author section for DANDI:001193 / doi:10.1038/s41562-022-01334-6. The entry passes its checks and runs from a clean environment in 52 s, and the handover package is built. Almost nothing could be tested: the dataset holds only one z-scored high-gamma matrix per block, and every analysis in the paper needs things it doesn't have. Nothing is committed.

The pinned version is 0.240921.1006. The paper cites no version, and this is the only published one. The draft has the same 40 files with the same checksums and differs only in version-naming fields, as the notebook shows.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| participants | partially_reproduced |
| task-structure, behaviour-response-time, fig1b-high-gamma-best-band, fig1c-responsive-in-ifg, fig1d-only-after-keyword, fig2b-violation-electrodes, fig2b-single-type, suppfig6a-half-split, suppfig6b-duration-metric, fig2c-euclidean-similarity, suppfig7a-com-overlap, suppfig7b-not-nonlinguistic, fig2de-no-spatial-separation, suppfig8b-individual-no-separation, fig2f-circuit-diameter, suppfig9-predict-from-corr, fig3-latency-values, fig3d-latency-differences, fig3-sync-latency-variability, fig3e-latency-not-location, suppfig10a-separable-400-700, suppfig10b-duration-differs, nl-low-frequency (23 claims) | blocked, data_missing |
| stimuli-word-frequency | blocked, other |

For participants: the 10 subjects and the 256 electrodes each (two groups of 128) match. Sex is "U" for every subject, and "4 males and 6 females" appears only as free text copied into every file. Age is only the group range, P19Y/P50Y. Nothing says who did COM or NL.

**2. The dataset**
- The files have no trial, word or keyword event times, no condition labels, no responses and no photodiode signal. The stimulus, analysis and processing groups are empty.
- There are no electrode coordinates or anatomical labels: every location is "unknown", and neither grid says whether it covers the IFG or the MFG/STG.
- Only high gamma is deposited, so there is no broadband signal or other frequency band.
- Nothing maps the subject ids (TC5 to TC20) to participants 1 to 10 of Supplementary Table 1.
- The unit "volts" is wrong. Every channel of every file has mean 0 and standard deviation 1, which fits the paper's z-scoring within each block.
- The stated rate of 400 Hz doesn't fit the data. At 400 Hz every block lasts 70 to 95 s, but a block needs at least 138 s for its trials. At the paper's 100 Hz high-gamma rate blocks last 282 to 381 s. A weak spectral check at the 2 Hz word rate points the same way. This is consistent with 100 Hz but not shown, since there are no events to check against.
- The bad channels and time intervals the Methods exclude are not marked anywhere.
- No block was deposited twice: the largest match between different files is a correlation of 0.72, and all 40 lengths differ.
- I made no assumptions, so there are no questions for the paper's authors. I asked a reader nothing, as the claims file doesn't misread the paper.

**3. Where the protocol was unclear**
1. Outside data must be "pinned: a DOI, or a repository at a commit". The word-frequency site is public and reachable but can't be pinned, and the protocol only covers inputs that are not public. I blocked stimuli-word-frequency as `other` and said why. It also uses no data from the dataset, and the protocol doesn't say how to handle a claim like that.
2. The protocol has no guidance for a criterion where some expected values can't be measured. `measured` must be all numbers, one per expected value. I gave participants partially_reproduced (2 of 6 counts measurable and matching), left `measured` out and put the values in the notes.
3. It isn't clear whether missing event times or labels are `data_missing` or `metadata_insufficient`. I used `data_missing`, since the events are absent, not undescribed.
4. The clock check ("share the clock of the trial tables") assumes trial tables exist. I tested the sampling rate against the task timing and stated that the clock could not be established for any session.

**4. Runtime and failures**
- The run took about 15 minutes (07:28 to 07:43 UTC) and the notebook runs in 52 s.
- My first duplicate check falsely matched many files, because they all start with the same kind of large transient. I fixed it by comparing differenced stretches from the middle of each file.
- Nothing else failed.
- `git status` shows untracked dotfiles and folders at the repository root (`.bashrc`, `.idea`, `scripts` and others) that I did not create; I left them alone.

My new files are `attempts/001193-zhu-2022-01.yaml` and `entries/001193-zhu-2022/` (notebook, `ifg_hga.py` helper, README, `entry.yaml`, requirements and lock file); the verifier's package is in `executed/001193-zhu-2022/handover/`.
