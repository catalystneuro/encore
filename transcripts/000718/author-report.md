The attempt on dandiset 000718 is done through step 6 (protocol `pilot-7`). `tools/entry.py check` reports 0 errors, the notebook passes `all` in a clean environment in 81 s, and the handover is built in `executed/000718-zaki-2024/handover/`. I used the full text of the paper, which is open access (PMC11666460, CC BY), saved under `paper/`. Nothing is committed.

## 1. Outcomes (26 claims)

| Claim | Outcome |
|---|---|
| `source-data-link` (uses outside data): the two mice match the paper's per-mouse freezing | reproduced (4 of 4 values within 10%) |
| `ed9b-aversive-freezing-high-vs-low` | reproduced (64.1% against 8.8%, one mouse per group) |
| `offline-bursts-above-shuffle` | blocked, `methods_underspecified` |
| `offline-skew-above-shuffle` | reproduced (3 of 3 recordings above all 1000 surrogates) |
| `burst-locomotion-pause` | not reproduced (telemetry movement proxy) |
| `fig5c-wake-overlap-neutral-coburst` | partially reproduced (holds only with wake as the `wake` label alone; 2 against 1 discordant bursts) |
| 20 other claims (behaviour-only, one-hour offline and single-experience, inhibitory tagging, no-shock, EEG sleep and low-shock) | blocked, `data_missing` |

On the burst claim: under the procedure the criterion fixed, the true burst rate is below the surrogates, which would be "not reproduced". But the paper's own chance level (surrogate/true 0.72 to 0.96, from its source data) is far from mine (1.26 to 1.60), so the protocol's chance-level rule makes it blocked.

## 2. What was found about the dandiset

- **Coverage:** it holds 2 of the 9 mice of the EEG/EMG experiment: Ca_EEG2-1 (1.5 mA, high shock) and Ca_EEG3-4 (0.25 mA, low shock). Of each offline period only the first 10 min recording of 24 is there. Ca_EEG2-1 has no neutral or novel recall session and no offline-day-1 recording.
- **Missing cohorts:** none of the mice behind Figures 2 to 4 and 6 or the behaviour-only experiments are deposited.
- **Registration:** only Ca_EEG2-1 has cell registration. Its 19 tables cover recordings of which one is deposited. The tables agree with the ROI centroids (2 to 3 px against about 190 px for random pairs).
- **Session times, Ca_EEG2-1:** behaviour-session start times (and the Week epochs built from them) are about 1 h later than the telemetry and Miniscope clock. As deposited, the offline recording after FC starts 47 min before FC. Telemetry dropouts while the mouse is out of its cage show the true order.
- **Timestamps:** the OnePhotonSeries timestamps of three files are halved.
- **Sleep labels:** the labels include `quiet wake`, which the paper never defines. The deposited offline recordings hold no NREM or REM.
- **Offline session description:** it says "an hour" and "webcam"; the deposited recordings are 10 min of telemetry with no video.
- **Paper's code:** the analysis repository the paper names returns 404.
- **No duplicates:** no recording is deposited twice.
- **Clock checks:** calcium, behaviour and telemetry are consistent with a shared clock, except Ca_EEG3-4 offline day 1, where it could not be established.

## 3. Where the protocol was unclear, wrong or missing something

1. **General claims shown only in an undeposited cohort.** The protocol doesn't say whether these may be tested on the cohort that is deposited. I tested three (bursts, skew, movement pause), because the paper relies on them for its Figure 5 argument, and recorded the cohort difference as a deviation. Claims specific to the undeposited cohorts are blocked.
2. **Chance-level rule.** The paper states its chance level only in its source data, and for another cohort at another frame rate. I applied the rule anyway (blocked), and the notes give the result under the fixed criterion.
3. **Source-data repository.** The lab's repository of per-mouse figure values isn't covered: it could count as data deposited elsewhere (`elsewhere`) for the behaviour claims. I kept those claims `data_missing` and did not re-run statistics on figure values. I used the repository only for the link claim and for the reference chance levels.
4. **Link claim with nothing depending on it.** The protocol describes link claims as gates for dependent claims. Here no claim needs the outside data, so `source-data-link` is a standalone check of the dandiset with no `depends_on`.
5. **One mouse per group.** The protocol is silent on how to judge an across-mouse claim with one mouse. I fixed within-session tests in the criteria (30 s bins, McNemar over bursts) and said the paper's statistic was not tested. For the absence claim with one low-shock mouse, I blocked it.
6. **Clock between sessions.** The clock check covers streams within a session only, not start times across sessions. I added a cross-session check using telemetry dropouts.
7. **Data seen before criteria.** During the data check I saw one value the link claim compares (Recall2 freezing, 15.1%). I stated this in the claims file's opening comment, as the protocol allows.
8. **Paper year for the entry name.** It's ambiguous (online 2024, issue 2025). I used 2024: `entries/000718-zaki-2024`.

## 4. Runtime and failures

- **Runtime:** the notebook takes 81 to 82 s; `entry.py all` takes about 92 s.
- **Cloning:** `git clone` from GitHub failed (it asked for credentials), so I fetched both repositories as tarballs at pinned commits.
- **Cleanup denied:** removing `entries/000718-zaki-2024/__pycache__` and an empty harness directory `entries/000718-zaki-2024/.claude/.cc-writes` needed approval and was denied. `__pycache__` is gitignored, and git does not commit an empty directory, so neither should end up in the commit, but a check before the workflow commits would confirm it.
- **Stray files:** the sandbox's `/dev/null` placeholders (`.bashrc`, `.idea` and others at the repo root) appear as untracked; I left them alone.
