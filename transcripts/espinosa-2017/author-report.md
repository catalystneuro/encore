The entry, attempt record and verifier handover are done. The entry ran from a clean environment in 11.7 min and `check` reports 0 errors. I asked a reader nothing; nothing in the claims file looked like a misreading of the paper.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1-bf-response-classes | Not reproduced |
| fig1d-excited-cells-fire-faster | Reproduced |
| fig1d-discharge-by-class | Reproduced |
| fig1e-excited-slower-kinetics | Not reproduced |
| supp4-tail-pinch-response-patterns | Not reproduced |
| supp1, supp2, supp3 (histology, in vitro) | Blocked: `data_missing` |
| 16 prefrontal claims (Figures 2–4, Supp. Figs 6–11, Supp. Table 2) | Blocked: `data_missing` |
| fig5c-light-path-needed | Blocked: `data_missing` |
| fig5d-nphr-locomotion, supp14-moving-no-difference | Blocked: `metadata_insufficient` |

- **fig1 classes:** none of the 12 readings gets the counts within tolerance. They give 36–70 inhibited and 68–118 excited units, against the paper's 29 and 56.
- **fig1e kinetics:** the rank-sum test gives p = 0.051 to 0.99 under all 24 readings, so excited units are not shown to be slower.
- **supp4 pinch:** no reading matches. Pinch-activated units number at most 62, against 149.

## 2. The dataset, assumptions and questions

- **What it holds:** the basal forebrain recordings behind Figure 1 (4 animals, 20 recordings, 330 units, as the paper says), medial septum recordings for a later paper, and open-field videos. It has no prefrontal data, so the paper's main findings cannot be tested here.
- **The unit table holds the authors' own response flags.** These give 56 excited, 30 inhibited and 244 unaffected units, which matches the paper. The method as the claims file reads it agrees with these flags for 191 to 286 of the 330 units. I show the flags only as a variant; they do not decide any outcome.
- **Pinch data is incomplete:** pinch timing exists for 2 animals (NE52, NE58), but the legend gives 4 animals for panels C and D. Units in the other two animals still carry pinch flags. Using those flags across all units gives 45 pinch-inhibited units (10/7/28 by light class), against the legend's 44 (10/7/27).
- **The data descriptor is wrong in places:**
  - Recordings last 900 s (600 s in NE69), not 10 min.
  - Light pulses come every 20, 25 or 30 s, not 5 s on and 15 s off.
  - NE52's pinch TTL row holds hundreds of 50-ms pulses instead of the pinch events.
  - Several columns of the unit table are not described.
- **In pinch recordings, light-alone pulses alternate with light-plus-pinch pulses.** The paper does not mention this. I ran both readings (light-alone only, and every light pulse); neither changes an outcome.
- **The control videos have no laser timing, movement trace or genotype,** and nothing says which 5 of the 9 controls are the paper's NpHR- mice. That is why fig5d and supp14 are blocked.
- **Assumptions:** none (no outcome is marked `assumed`). Every outcome holds under all readings. The pulse-bin edge and the 1 ms to 20 s bound on the fitted time constant are standard choices and are recorded as deviations.
- **Question for the paper's authors** (a `methods_unavailable` finding): which bins, statistic and threshold produced the per-unit flags, and were light-plus-pinch pulses included? The same question covers the Figure 1E fit window.

## 3. Where the protocol was unclear or did not fit

1. docs/archives.md says CRCNS data sets are zip files to open in place. bf-2 is all tar.gz, which cannot be read at random. I streamed each archive once, start to end, keeping only the small files needed. The four ephys archives plus the two behavior archives take about 9 min per run.
2. "List everything" in step 1.1 means streaming whole archives for tar.gz. Listing the 9.4 GB control archive took 10 min.
3. The protocol does not say what to do when the deposit holds the authors' own derived results that match the paper but the described method does not. I showed them as a variant, let the criterion decide, and recorded the gap as a finding and a question.
4. The clock check suggests decoding a task variable. I used a simpler contrast: the response to the true light onsets against onsets shifted 10 s. The true onsets give the larger response in 20 of 20 recordings.
5. When part of a claim's data is missing (pinch in 2 of 4 animals) and the part that can be tested (panel E) fails, the protocol does not say whether that is `blocked` or `not_reproduced`. I chose `not_reproduced` and explained the missing part in the notes.
6. For the videos, blocking could be `too_large` or `metadata_insufficient`. Decoding fits the time limit (about 790 frames/s), so I used `metadata_insufficient`: the laser timing would need a detection step nobody describes. The probes I ran outside the notebook are mentioned in the notes as deciding nothing.
7. "`measured`: the first reading the criterion lists" is unclear when the readings combine bins, normalizations and classification rules. I used 500 ms/n1/r1 for fig1 and supp4, and 250 ms/w1/n1/r1 for fig1e, the order the criterion lists them.
8. CRCNS data sets have no versions. I recorded `unversioned`, the MD5 sums from `checksums.md5`, and the descriptor's version (0.6).

## 4. Runtime and failures

- The session took about 1 h 10 min (20:12 to 21:21 UTC). The notebook runs in 11.7 min with peak memory 0.33 GB in the main process.
- Two early attempts failed and were fixed: the scratch environment was missing fsspec, and PyAV needed a non-seekable wrapper to read a streamed video.
- No final run failed.

Nothing was committed. The working tree also has files I did not create or touch: a modified `tools/build_site.py`, an untracked `scripts/` directory and several dotfiles.

Files are in `entries/espinosa-2017/`:
- `reproduce_espinosa_2017.ipynb`
- `bf2.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/espinosa-2017-01.yaml`, and the handover is in `executed/espinosa-2017/handover/`.
