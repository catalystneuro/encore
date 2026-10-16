I've finished steps 1 to 6 for dandiset 000044 (Grosmark & Buzsáki 2016). Locking, checking and running the entry from a clean environment passed (`0 error(s)`), and the handover package is in `executed/000044-grosmark-2016/handover/`. Nothing is committed. The files are the claims in `claims/000044/10.1126-science.aad1935.yaml`, the attempt in `attempts/000044-grosmark-2016-01.yaml`, and the entry in `entries/000044-grosmark-2016/` (notebook, `grosmark.py`, README, lock).

Paper text used: the full main text and the Figure 1 to 4 legends, from the NIH author manuscript (PMC4919122). The supplementary Materials and Methods and the figure images could not be downloaded: PMC and Science serve them only behind a browser check.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| sessions-and-tracks | reproduced |
| place-cell-count (491) | not reproduced: 417 at a 1 Hz threshold, 480 at 0.5 Hz |
| fig1c-post-gt-pre | not reproduced by the pooled test; POST is higher within all 8 sessions (sign test p = 0.0039) |
| fig1c-maze-gt-pre | reproduced |
| fig2b-strong-contributors, fig2-pre-post-overlap, fig2d, fig2e, figs2, fig3a, fig3b, fig4a-rigid-faster, fig4a-plastic-ripple-burst-coactivation | blocked, methods_underspecified (analyses still shown) |
| fig4c-pre-fast-coactivation | reproduced |
| fig4c-slow-coactivation-increase | not reproduced |
| fig4c-slow-replay | not reproduced |
| rate-split-medians | partially reproduced (0.435 and 1.091 Hz) |
| figs16-low-rate-info-gain | partially reproduced |
| fig4d-slow-sequences | not reproduced |
| fig4e-gain-sequences | not reproduced |

Totals: 3 reproduced, 2 partially reproduced, 6 not reproduced, 9 blocked.

The pooled replay test that the criteria fixed is swamped by the three circular-track sessions. They score low in every epoch and supply nearly half the POST events. With each session's PRE mean subtracted (a variant, which does not change outcomes), the paper's pattern appears for fig2d, fig2e and fig4e.

### 2. The dandiset

- **Contents:** 8 sessions from 4 rats: 562 pyramidal units and 128 interneurons, LFP at 1250 Hz, sleep states, epochs and positions. Spikes, LFP, sleep states and positions all share one clock; three contrast checks confirm it.
- **Version pinned:** 0.261005.2101, the latest. The paper cites no version, and the two earlier versions store the position sampling period (0.0256 s) as the rate.
- **Epoch error:** in Gatsby_08022013 the POST epoch ends at 30413.6 s, while the data run to about 32002 s.
- **Missing data:** the description lists EMG and accelerometer signals, but the files hold neither, and no raw wide-band data.
- **Missing derived data:** no events, place-cell lists, PCC values or rigid/plastic labels are deposited, so the paper's selections can't be checked.
- **No code:** neither the paper nor the dandiset links analysis code.
- **Sparse metadata:** electrode location is "unknown" on every channel and subject age is "/".
- **Running direction:** on the circular track the animals ran toward decreasing linearized position, which the metadata doesn't say.
- **No duplicate recordings found.**

### 3. Where the protocol was unclear, wrong or missing something

1. **Chance-level rule.** It applies "when the paper states a chance level". The main text only says "significant". I read that as a 5% false-positive rate. My pre-registered PCC test has a 58% false-positive rate (a calibrated variant has 30%), so I blocked fig2b as methods_underspecified.
2. **Blocking dependents.** fig2d uses dPCC, not the significance test, but it lists fig2b in `depends_on`. I applied "a dependent of a blocked claim is blocked" literally.
3. **Main text open, supplement not.** The protocol only distinguishes full text from abstract. I used the main text, said so, and treated every Methods detail as a common choice fixed in advance.
4. **A pre-registered test can be confounded.** The pooled test hides a within-session effect (Simpson's paradox), and the protocol gives no guidance. I judged outcomes on the pooled test and showed the within-session test as a variant.
5. **Code bugs found after running claim analyses.** The protocol is silent on this. I had assumed the circular track was run in the increasing direction. I fixed it because the criterion says templates come from running, and the fix is recorded in the notebook.
6. **Some criteria define no partial outcome.** For rate-split-medians, where one of two values falls in tolerance, I used the protocol's general definition of partially reproduced.
7. **Unreadable figures.** I couldn't see the figure images, and the text doesn't state Fig. 1D's result, so I made no claim for it.
8. **Thresholds.** "Show how the result changes with a threshold" covers many choices here. I varied the place-cell peak and the PCC alpha and split, but not the ripple or burst thresholds.

### 4. Runtime and failures

- **Notebook:** about 8.3 minutes from a clean environment (498 s), on 4 processes. About 2 minutes of that is streaming one LFP channel per session.
- **Failed downloads:** the supplement PDF and figure images, from PMC, Europe PMC and Science.
- **First draft:** took 18 minutes and had the circular-direction bug; both are fixed and re-run.
- **Untracked items:** `git status` lists dotfiles and `scripts` that I didn't create. They are sandbox `/dev/null` mounts; I left them alone.
