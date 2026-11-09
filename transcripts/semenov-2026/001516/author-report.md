I've finished steps 1 to 6 of the Author section. The entry passes `check` and runs from a clean environment in 78 s, and the handover is built. The headline: dandiset 001516 holds none of the recordings behind the paper's figures, so 31 of the 32 claims are blocked and only one can be tested.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig5b-conductivity-calibration | **not reproduced**. Eq. (2) with the Methods' constants gives 1.33% for a 10-fold rise (1.20% under the second reading), against 2 ± 0.2%. A 100-fold rise gives 11.87%, inside 12 ± 1.2%. |
| The other 31 claims (Figs. 1 to 4, Gd3+, Fig. 5C, Ca2+, Fig. 7) | blocked, `data_missing` |

The fig5b claim uses no recordings, so its outcome says nothing about the dataset.

## 2. The dataset, assumptions and questions

**Version.** I pinned 0.261006.1833, the only published version; the paper cites none.

**What it holds.** 72 files from 12 fields of view recorded on 2023-06-22:
- Every file names FluoVolt with a FITC filter cube and 1.00-mm electrodes. The paper's Fig. 7 used Di-8-ANEPPS, and its electrodes were 1.6 mm apart.
- Sets have 20 sham frames then 40 pulse frames. The paper's sets have 40 and 60.
- Fields are 150 to 1570 V/cm, and pulse pairs come at intervals of 1, 5, 25, 125 and 250 µs.
- Two fields of view per protocol; the 5-µs pairs have 4 cells in all.

The paper does not report this experiment. Its Discussion names varying the interval as future work.

**Checks against the description:**
- **Frame order:** the data confirm the 20/40 order. The pole contrast steps at frame 20 in 170 of 174 pulse cell-sets and not in sham sets.
- **Field direction:** it can be read from the data, image-up in every field of view.
- **Duplicates:** no file is deposited twice.

**Findings for the data owner:**
- The metadata names the paper as the publication of these data.
- The description lists four intervals; two fields of view are at 250 µs.
- `starting_time` holds a Unix time where NWB expects an offset from the session start.
- The pulse protocol is only in free text, and there is no pixel size, field direction, or record of which cell in a field was the experiment's (each field holds 1 to 4 cells).
- The listed field strengths are not proportional to voltage, and the files do not map amplitudes to fields.
- Cells dim 9 to 17% after the sham frames even with no pulse.
- A paper inconsistency: the ~2% in Results 3.5 does not follow from Eq. (2) and its stated constants.

**Variants.** The notebook measures the dataset's own sets with the paper's pole method, as a section that decides no claim. With the uniform dimming removed, the cathodic test-pulse response at 5 µs falls to 76% after 1270 V/cm and 65% after 1570 V/cm.

**Assumptions:** none affect an outcome. **Questions for the paper's authors:** none. **Questions to a reader:** none. The claims file reads the paper correctly; it assumed the dataset held the Fig. 7 data, which is a dataset issue.

## 3. Where the protocol was unclear or missing something

1. It has no case for a dataset that holds a different, unreported experiment. I blocked every recording-based claim as `data_missing` and showed the dataset's own sets as descriptive variants.
2. It does not say how a claim that needs no data counts toward the dataset. I tested fig5b and said in its notes that it is independent of the data.
3. Step 2 asks to align data streams with "the trial tables", but there are none here. I used the frame-split contrast between sham and pulse sets instead.
4. There is no prescribed place for analyses of data that are not the paper's. I put them in an untagged section after the claim sections.
5. It is unclear whether `elsewhere` covers sibling dandisets on the same archive. Dandisets 001517 and 001518 name the same paper and are separate targets; I kept `data_missing` and named them in the notes.
6. docs/archives.md says to read files with `pynwb`. I read them with `h5py`, which was enough for one ImageSeries.

## 4. Runtime and failures

About 30 minutes, 20:14 to 20:43 UTC. Nothing failed. Several dotfiles (`.bashrc`, `.gitconfig`, `.idea`, …) are untracked in the repository root; they were already there and not created by this run, so I left them alone.

Files are in `entries/001516-semenov-2026/`:
- reproduce_semenov_2026.ipynb
- pulsed_imp.py
- README.md

The attempt record is `attempts/001516-semenov-2026-01.yaml`.
