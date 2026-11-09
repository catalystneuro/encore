All 22 claims are blocked, every one for `data_missing`. The dataset holds the EEG of only one of the paper's ten subjects, with none of the behavioural data the paper builds its analyses on. The entry passed `tools/entry.py all` with 0 errors, the notebook runs in 76 s, and the verifier's package is in `executed/001285-purdon-2013/handover/`. I did not verify my own work, and nothing was committed.

**1. Outcome per claim**

| Claim | Outcome | What it needs that the dataset lacks |
|---|---|---|
| fig1c-clicks-lost-before-verbal, eon-loc-duration, fig1e-group-induction, fig1e-group-emergence, eoff-not-reached, roc-eoff-duration | blocked: data_missing | the button-press responses and stimulus times; 9 of 10 subjects |
| fig2bc-gamma-beta-before-loc, fig2bc-alpha-slow-at-loc, fig2-emergence-reverse, slow-power-tenfold, fig3a (induction and emergence), fig5 (all three), figs3-broadband-modulation | blocked: data_missing | LOC, ROC, EON and EOFF, which the paper derives from the responses; the 10-subject group and sign tests; which channel is Fz |
| fig2d-spatial-loc15, fig3b, figs2-band-spatial-shift, fig4ab, fig4cd, fig4-no-low-frequency-mode | blocked: data_missing | the same, plus channel names or positions for the spatial groups (recorded in the notes as metadata_insufficient) |

**2. What the dataset holds**
- **Version:** `0.250110.2125`, pinned because the paper cites none and it is the only published version. The draft holds the same file (same blob).
- **Contents:** one NWB file with one generic TimeSeries (`example_timeseries`): 64 channels at 250 Hz for 154.5 min. There is no electrode table, so no channel names, positions or bad-channel marks. There are no trials, events, stimuli, infusion levels or behavioural markers.
- **Elsewhere on DANDI:** dandisets 001286 and 001287 carry the same description of the study and hold no files.
- **Format:** the data are stored channels first, so pynwb reads the series as 64 samples.
- **Metadata errors:** the subject's age is 30 days, for a volunteer aged 18 to 36. The session start time is the 2025 conversion date. The identifier (`NWB123`) and session description ("EEG Session Example") are placeholders, and the ORCID in the file's notes differs from the contact's ORCID on DANDI. Subject001 is not mapped to the paper's subject numbering.
- **The values themselves fit the description:**
  - The 60 Hz mains peak and the roll-off above 100 Hz fit the stated 250 Hz rate.
  - The amplitudes fit microvolts.
  - No channel duplicates another, and there are no gaps.
  - The band-power time course looks like a gradual propofol induction and emergence. Beta steps up at minutes 17 and 33, and low-frequency power is 6.5 to 34 times its opening level from minute 49 to 97. This is shown as a description of the file only and decides no outcome.
- **Assumptions and questions for the paper's authors:** none, since no analysis was run. I asked a reader no questions, because I found no misreading in the claims file.

**3. Where the protocol was unclear or did not fit**
1. The protocol does not cover an entry where every claim is blocked. I made a notebook with the header, the data check, a section showing what each claim needs, and the summary. It has no `claim:` cells and no "**Result:**" openers, and the outcomes have no `notebook` or `output` fields.
2. When a claim lacks several things at once (behaviour, the other subjects, channel labels), `blocked_by` takes only one reason. I gave `data_missing` as the main reason and named metadata_insufficient in the notes.
3. The clock check (step 2) assumes a trial table exists. With none in the file, I said so, as the protocol asks for any session where the check cannot be made.
4. The protocol does not say whether the data check may describe a file in terms close to a blocked claim, such as the time course of low-frequency power. I showed it, labelled it as a description that tests nothing, and kept it out of every outcome.

**4. Runtime and failures**
- The run took about 15 minutes (01:01 to 01:16 UTC). The notebook takes 76 s in the clean environment.
- One command failed because it ran from the wrong working directory; I reran it from the repository root. Nothing else failed.
- Untracked dotfiles (`.bashrc`, `.gitconfig`, `.idea`, `.mcp.json` and others) appeared in the repository root; the gitStatus snapshot at the start showed a clean tree. I don't believe I created them, and I left them alone, so check them before the workflow commits.

Files are in `entries/001285-purdon-2013/`:
- `reproduce_purdon_2013.ipynb`
- `propofol_eeg.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/001285-purdon-2013-01.yaml`.
