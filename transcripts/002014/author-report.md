I finished steps 1 to 6 for dandiset 002014. Five claims were tested and eight are blocked. The entry passes `check`, and `all` ran it from a clean environment in 85 s. The handover is in `executed/002014-choi-2025/handover/`. Nothing is committed.

I used the full text: the paper is open access as an NIH author manuscript in PubMed Central (PMC13250822, CC BY). I pinned 0.261012.0921, the only published version. The paper cites a Zenodo record, not a DANDI version, and the draft holds the same file and metadata.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig8a-single-trial-dopamine | reproduced (weak test: the SD ratio after/before the value cue is 2.02 for trial 133, but 60% of all trials are above 1) |
| fig8b-dopamine-large-vs-small | reproduced (difference 0.76, p = 0.0037, Cohen's d 0.18) |
| fig9a-spikes-task-aligned | reproduced, but only after moving the spike times to the trial clock; with the times as stored it fails |
| fig9bc-unit-waveform-isi | reproduced (the interval half is guaranteed by the detector's 1.56 ms dead time) |
| fig9d-beta-suppression-large | partially reproduced (both conditions suppressed; large lower but p = 0.108) |
| recordings-two-monkeys, scfe-functional-yield, scfe-background-yield, mcfe-functional-yield, dopamine-signal-yield, asepsis-cultures, fig6-drainage-volume, fig7-bone-growth-margins | blocked: data_missing |

**2. What I found about the dandiset**

- **Spike clock:** The raw ephys and the spike times are not on the clock of the trials, events, LFP and FSCV table. The raw ephys is stored from 0 s with no timestamps. Locating it in the stored LFP puts it 11,812.11 s later (r 0.98 to 1.00 at eight points, drift about 4 ms per hour).
- **Spike lag:** The stored spike times sit about 7.1 ms after the spike troughs in raw c5d.
- **Absolute times:** On the trial clock the raw samples end at 17:12:20, two hours after the "recording closed" time in the Neuralynx header (15:12:24).
- **Units and labels:**
  - The "beta-band LFP" is broadband. Its values are already in volts, yet it carries the raw conversion factor, which would make them about 3e7 times too small.
  - The spike waveforms are labelled volts but hold µV.
  - The raw FSCV current is labelled amperes but holds nA.
  - The FSCV table columns state no units, and the `good` column is true for every trial.
- **Wrong descriptions:** The subject, session and experiment descriptions and one keyword describe the lab's micro-invasive probe study, not this paper.
- **Event table:** Each event is stored about five times over, unsorted. The trial tags carry no trial type.
- **Unsorted spikes:** The Plexon unit's spike times are not sorted.
- **Trial selection:** Reward size and outcome rebuilt from the events match the paper's Zenodo trial lists, except the last trial (1411).
- **Reward location:** The paper says reward size depends on a top or bottom target. The events code left and right, and these do not predict reward size.
- **Raw FSCV:** The minute files are joined without their gaps (328 min of scans against 302 min of trials). I could not find the trial-aligned oxidation current in it, so its clock is not established. No claim uses it.
- **Missing data:** Only one session of monkey T is deposited. Monkey J and the yield, culture, drainage and bone-growth data are absent.

**3. Where the protocol was unclear or did not fit**

1. A stream offset by a constant that the data reveal. The protocol says to trust the data, but not whether a claim that passes only after a correction derived from the data counts as reproduced. I recorded it as reproduced, with a deviation, and the notes say it fails on the file as published.
2. The suggested clock check, decoding a task variable from spikes, assumes the spikes share some clock with the trials. Here it needed the raw ephys: cross-correlating raw with the stored LFP, plus a spike-triggered average. The task contrast I could run only places the spikes to within a few seconds, because the response is broad.
3. This is a methods paper. Most of its findings are surgical and culture outcomes that no dataset holds. Its data figures (8A, 9A to 9C) are demonstrations without a stated effect. I wrote criteria for them, and they are weak; I said so in the notes.
4. Outside data used only as a check (the Zenodo trial lists) fits neither `inputs` nor a link claim cleanly. I listed it under `inputs`, wrote no link claim, and kept all claims `data: dandiset`.
5. "Deposited more than once" does not cover two sortings of the same channel (thresholded and Plexon). I treated them as one recording: thresholded as the main analysis, Plexon as a variant.
6. While checking the array layout, before writing criteria, I printed stored dopamine values that include trial 133. The protocol asks for disclosure but not whether that taints the claim. I disclosed it in the claims file header.
7. "Every data stream shares the clock" includes streams no claim uses. I tried the raw FSCV and reported its clock as not established.
8. The 10% tolerance rule applied to proportions: I used 10% relative. All those claims are blocked, so it does not matter here.

**4. Runtime and failures**

- The notebook runs in about 1.3 minutes.
- During development my first clock locator was numerically broken and gave a wrong offset. Under that offset fig9a looked like it failed. I fixed the locator, and the final offset matches at eight points across the session.
- Deleting an empty `.claude/.cc-writes` folder that the harness created inside `entries/002014-choi-2025/` was denied (no approval surface). Please leave it out of the commit.
- Untracked dotfiles (`.bashrc` and others) and a `scripts` folder in the repo root are not mine; `scripts` was there when I started.
