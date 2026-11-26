The author steps for garud-2026 are done. The entry is locked, `python tools/entry.py all` passes (0 errors, notebook runs in 246 s), and the handover package is built in `executed/garud-2026/handover/`. I did not verify my own work, commit or push.

**1. Outcomes**

| Claim | Data | Outcome |
|---|---|---|
| floeder-subjects-sessions | DANDI:001552 | reproduced (18 mice, 16 to 24 sessions each) |
| fig4a-lick-short-above-long | DANDI:001552 | reproduced (2.39 vs 1.60 Hz, t(17) = 4.15, p = 0.00067) |
| fig4b-long-iti-dip-below-baseline | DANDI:001552 | partially reproduced: the long-ITI dip holds under all 8 readings, but the short-ITI trace is below zero before the next cue |
| fig4d-dip-deepens-with-training | DANDI:001552 | partially reproduced: slope negative under 16/16 readings, p < 0.05 under 10; within-mouse r −0.283 at p = 0.0043; no reading gives both the paper's r and p < 0.001 |
| fig4c-lick-rate-rises-with-training | DANDI:001552 | reproduced (r 0.648, p 1.2e-05) |
| krausz-included-observations | Mendeley (elsewhere) | reproduced (264,042 rows exactly) |
| fig2a, 2b, 2c, 2d, 2e | Mendeley | reproduced |
| fig2f-coupling-grows-near-goal | Mendeley | reproduced (r = −0.494, df 18, p = 0.027) |
| fig2gh-stationary-dip | Mendeley | reproduced, resting on an assumption (t = −4.274) |
| fig3-recovered-value-increases | Mendeley | partially reproduced, resting on an assumption (7 of 10 rats) |
| fig3cd-gaussian-shape-wins | Mendeley | partially reproduced (Gaussian wins in 9 rats; mean R² is not above 0.8 for all four shapes) |
| fig5bc-gaussian-ct-td-best | Mendeley | reproduced (best summed, wins in 8 of 10) |
| fig5d-tonic-term-and-gaussian-contribute | Mendeley | reproduced (ΔBIC 1170 and 696) |
| figs2-no-velocity-coupling-without-goal | Brown et al. | blocked: methods_underspecified (the supplement is not available) |

**2. Dataset, assumptions and questions**

I pinned version 0.250828.1728 because the paper cites it. Version 0.250903.1802 holds identical assets.

What I found in the dandiset:
- **Duplicates (critical):** two recordings are deposited twice, `ramp2-F2` Day3/Day4 and `ramp2-F4` Day5/Day6. I counted each once.
- **Clocks (critical):** the photometry and the event log run on different clocks, and the files do not say so. The photometry starts 3.6 to 251 s before the event log's zero. The only link is the undescribed TTL2 channel, which steps at each cue; I aligned every session by fitting TTL2 edges to cue times.
- **Wrong rate (minor):** 64 of the 144 JF-FP series state 120481.9 Hz; the TTL2 fit gives about 120.3 to 120.5 Hz.
- **Photometry-only mice (major):** 9 JF-VR-FP mice (144 files) have photometry only, with no events or description.
- **Session order (no problem with the data):** sessions are in blocks, not "alternating across days" as the paper says.

Assumptions:
- **fig2gh:** "non-approach" observations are read as all rows off the ports. This reading gives the paper's t exactly; the other row sets do not.
- **fig3:** no minimum observation count per position. A minimum of 5 gives 6 of 10 rats.

Questions for the paper's authors are recorded as three `methods_unavailable` findings:
- the Figure 4 ΔF/F correction, ITI reference, observation rule, session numbering and how r is computed;
- which rows make up "non-approach" in Figure 2G-H, and the details of the value recovery and its four profile shapes;
- the supplement and the OSF code, which are not available (the OSF API returns 401).

I asked no reader questions.

**3. Protocol points**
1. Many claims here are `data: elsewhere`, on outside data that are not deposited by this paper's authors and need no link to the dandiset. The protocol's link-claim rules do not cover this case. I tested them on the pinned Mendeley DOI and listed it under `inputs`, with no link claim.
2. Some criteria leave the readings for a partial outcome unclear (fig4d: "under one reading" is stated for reproduced but not for partial). I applied "any reading".
3. The protocol is silent on whether a duplicate deposit should be dropped before session numbering. I dropped the later copy and numbered sessions without it.
4. The "Develop on a subset" timing rule fit poorly here because the whole run takes 4 minutes. I timed 3 sessions (about 1 s each) and then ran everything.
5. When a finding mixes the reusing paper's description with the data ("alternating" sessions), the protocol's `about: data` rule felt forced. I recorded it as about the data with severity none.

**4. Runtime and failures**

The work ran from 09:30 to 10:41 UTC. The notebook takes about 4 minutes and peaks around 0.4 GB of memory. Nothing failed in the final run. During development:
- Mendeley and the DANDI S3 redirect rejected `urllib` requests (403), so I switched to `requests`.
- One notebook build had a string-escape bug, which I fixed.

`git status` also shows untracked dotfiles in the repository root (`.bashrc`, `.profile`, `.idea`, `.mcp.json`, `scripts`, and others). They look like they come from the environment, not from my work. I did not touch them, but the workflow's commit should leave them out.
