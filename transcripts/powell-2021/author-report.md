I ran steps 1 to 5 of the Author section and the handover (step 6). The entry is `entries/powell-2021/` and the record is `attempts/powell-2021-01.yaml`. `tools/entry.py all` reports 0 errors, the notebook passes in a clean environment in 233 s, and the handover is in `executed/powell-2021/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2-spontaneous-11-to-30 | blocked, data_missing |
| fig2a-less-regular-at-high-temperature | blocked, data_missing |
| fig3-evoked-7-to-21-in-9-of-10 | not reproduced (8 of 10) |
| fig3s1-spontaneous-and-evoked-similar | blocked, data_missing |
| fig4b-periods-decrease-all-preps | reproduced |
| fig4c-q10-about-2 | not reproduced (the Methods' Q10 gives 1 to 3 of 10; the code's gives 8) |
| fig4c-q10-pd-lg-not-different | reproduced |
| fig4s1-slowdown-after-stimulation | reproduced |
| fig4s2-gastric-without-pyloric-pacemaker | blocked, data_missing |
| fig4s2-rhythm-counts | blocked, data_missing |
| fig5a-example-ratios | reproduced |
| fig5d-lg-pd-integer-coupled | reproduced |
| fig5d-dg-pd-not-coupled | reproduced |
| fig5e-lg-area-exceeds-dg | partially reproduced |
| fig5f-ratio-independent-of-temperature | reproduced |
| fig5f-ratio-range | not reproduced (central 95% runs 7 to 26) |
| fig6b-lg-phase-locked | partially reproduced |
| fig6b-lg-start-counts | not reproduced (DG count 22 over tolerance) |
| fig6b-lg-phase-constant | partially reproduced |
| fig6c-lg-spiking-drops-near-pd-end | not reproduced |
| fig6e-dg-not-phase-locked | reproduced |
| fig6f-dg-spiking-no-drop | reproduced |

No outcome rests on an assumption, and none changes with the random seed.

## 2. The dataset, assumptions and questions

**What the record holds.**
- `evoked_data.mat` holds sorted PD, LG and DG spike times, plus temperature and a stimulation mask sampled at 1 kHz, for the ten evoked preparations. Its MD5 matches the record.
- Its preparation and file names are MATLAB categorical objects. I decoded them from the file's MCOS subsystem.
- The mask, spikes and temperature share one clock, and no recording appears twice.
- With the code's burst rule and the code's computations, the paper's numbers come out exactly: t = 1.27, p = 0.235; 3799 cycles with Spearman p = 0.88; rho = -0.31, p = 0.46; 3816 LG burst starts. So the file holds the data the paper analysed.

**What is missing or does not match.**
- The spontaneous set and the PD-hyperpolarized set are not in the record, although the paper's data statement points only to it. I searched Zenodo and DANDI: Zenodo 5139650 (Haddad and Marder) holds six other recordings, not these.
- 941_003 and 941_006 are raw ABF files only, with no spike annotations. Their headers date them to June 2019, which fits none of the paper's three sets. 941_006 is one of the four preparations of Figure 3, figure supplement 1.
- There is no zip of raw data for 901_005.
- 932_151's ABF header gives 2 May 2019, while the Methods say the evoked preparations are from 2017.
- The 901_062 zip holds 101 files, but only 58 are stacked in `evoked_data.mat`.
- The record has no README and no description of its fields, and Zenodo types it as a journal article.

**Disagreements between the paper and its code.**
- The Methods keep bursts of at least n spikes; the code counts inter-spike intervals, so it keeps bursts of n+1 spikes.
- The reported Rayleigh ranges come from the later code's first 50 starts, not the Methods' first 40.
- The Methods' Q10 formula differs from the code's per-burst Q10, and the reported count of 8 of 10 follows the code.

**Assumptions.** I made none that an outcome rests on. For the open details I ran every reading and they gave the same outcome: which bins count as "held" (at least 120 s, or any time at all) and which bins enter the Methods' Q10 (all, or only the held steps).

**Questions.** None for the paper's authors in the sense of step 1.6, and none for a reader.

## 3. Where the protocol was unclear, wrong or missing something
1. The rule to stream data and never write it to disk has no exception for a survey. I kept one temporary copy of the 73 MB `.mat` in `$TMPDIR` while exploring; the notebook streams the file.
2. The burst-count mismatch between the Methods and the code affects every claim, but there is no guidance for a code variant that runs through all of them. I ran the Methods rule as the main analysis and the code rule as a variant in every section.
3. "Held" temperature bins and the Q10 temperatures are details the claims file leaves open. I ran both readings each time.
4. The examples in archives.md come from DANDI, and there was no Zenodo entry or record to copy. I used `zenodo:3924718/3924718` and set version to the record id, as archives.md says.
5. The `lock` step did not write the `python` field into `entry.yaml` until `all` ran.
6. Zenodo returned one transient HTTP 500 while reading a zip listing. The protocol says nothing on retries; I added a bounded retry in the helper.
7. The protocol says a mismatch between the files and the paper is about the data, which makes cases like the "9 of 10" count awkward to classify. I filed them as `other` about the data, rated minor.
8. Untracked character-device dotfiles (`.bashrc`, `.mcp.json` and others) were already at the repository root before I started. They come from the sandbox, I left them alone, and the workflow should not commit them.

## 4. Runtime and failures
The notebook takes about 4 minutes, most of it reading `evoked_data.mat` from Zenodo at about 0.7 MB/s; peak memory was about 1.4 GB. The whole author run took about 55 minutes, finishing at 15:57 UTC. During development, three runs failed: a wrong metadata field, a column named `T` (the DataFrame transpose) and the Zenodo 500. All are fixed, and nothing is failing now.
