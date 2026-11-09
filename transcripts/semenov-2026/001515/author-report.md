I could test only one of the 34 claims, and it came out partially reproduced. The other 33 are blocked because dandiset 001515 does not hold this paper's experiments. Lock, check and run pass with 0 errors, and the handover package is in `executed/001515-semenov-2026/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig5b-conductivity-calibration | partially reproduced. Eq. (2) with the paper's Methods constants gives an IMP reduction of 1.33% (reading a) or 1.20% (reading b) for a 10-fold rise in membrane conductivity, against the paper's ~2 ± 0.2%. The 100-fold rise gives 11.87% (a) or 11.75% (b), inside 12 ± 1.2%. |
| The other 33 claims (Figs 1 to 7) | blocked, `data_missing` |

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.261006.1841. The paper cites no dataset version; this is the only published one, and the draft holds identical paths and sizes.

**What the dandiset holds.** There are 292 files from 37 subjects in four sessions. Each file is a 70-frame strobe-imaging series of CHO cells stained with FluoVolt. Each subject got single 1-µs pulses at one amplitude only (20 to 100 V, electrodes 1.00 mm apart), recorded "forward" or "backward". This is the time-course protocol the paper attributes to its reference [20], an earlier study. The paper's own recordings are absent:
- no sets of 40 baseline plus 60 pulse images at 900 ns;
- no field-strength escalation within a cell;
- no Di-8-ANEPPS dye, 0.3-µs pulses, Gd3+, two-pulse or Ca2+ recordings.

**Findings recorded about the data:**
- **Frame delays.** The delay of each frame relative to the pulse is not recorded. The data show the frames are successive delays: the response's half-peak frames are 16 to 34 in forward files and the mirror image in backward files. A step of about 50 ns fits this but is not proven.
- **Field strength.** Amplitudes are in volts across 1.00-mm electrodes; the paper used 1.6 mm and modelled V/cm. At the same 40 V the response varies between sessions (25.9% against 11.9%).
- **Anode side.** In 35 of 37 subjects the response sign flips with the stated anode side, but 9 files disagree with their subject. Across sessions, "anode above" gives opposite signs, so image orientation is not fixed.
- **Odd file.** One file of CHO-20230926-c1 shows a different field of view and was recorded on 2024-12-16, about 14 months after its subject's other files.
- **Indistinguishable files.** Each subject has two files per order and anode side with nothing to tell them apart; one subject has 4 files instead of 8; each image contains several cells.
- **Frame 0** is dimmer than the rest (below 0.8 of the median frame) in 220 of 292 files.
- **Metadata errors.** The archive summary names two species for one CHO cell line, every subject has age "P1D", and the description mentions sine-wave exposures that no file holds.
- **Paper inconsistency.** The ~2% for a 10-fold rise does not follow from Eq. (2) with the paper's own constants (also recorded as a finding).

There were no duplicate frames and no field of view filed under two subjects. I made no assumptions, asked the paper's authors no questions, and asked no reader any questions.

## 3. Protocol points

1. **Sibling dandisets.** Dandisets 001516, 001517 and 001518 name the same paper and may hold the missing data. The protocol only says data "not public anywhere else" are `data_missing`. I kept `data_missing` for this dandiset, as the claims file has `data: dataset`, noted the siblings in each blocked claim's notes, and did not read them.
2. **Claims that need no recordings.** fig5b is a pure computation but sits under the default `data: dataset`, and the protocol does not say how to count such a claim. I tested it and said in the notes that it uses no recordings.
3. **Two block reasons.** For the FluoVolt claims, both `data_missing` (the paper's image sets are absent) and `metadata_insufficient` (no frame delays or V/cm) apply. I gave `data_missing` as the main reason and named the other in the notes, as step 1.5 allows.
4. **Data check with no tested data.** Step 2 assumes trial tables and decoding. With no claim using the recordings, I used a membrane polarization index per frame, compared between forward and backward files, anode sides and amplitudes. Its parameters are standard choices, said to be so in the helper.

## 4. Runtime and failures

The notebook runs in about 3 minutes, most of it streaming all 292 files; the whole run took about 30 minutes (20:06 to 20:37 UTC). Nothing failed. Untracked dotfiles and a `scripts` folder at the repository root were not created by me and I left them in place.
