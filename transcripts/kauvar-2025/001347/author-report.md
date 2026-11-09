The author run is finished: steps 1 to 5 are done and `python tools/entry.py handover` built the verifier package. Analysis was split across five notebooks; I wrote the human-behaviour one and four sub-agents wrote the others under a shared brief, and I merged and checked their results. The entry passes `tools/entry.py check` and ran twice from a clean environment in 22.5 min, with identical numbers apart from timings and float noise. I did not commit anything.

**(1) Outcomes** (61 claims, 5 of them link claims I added: 45 reproduced, 7 partially, 4 not reproduced, 5 blocked; "assumed" = rests on an assumption)

| Claim | Outcome |
|---|---|
| p50-condition-labels-link, cadss-scores-link, mouse-session-labels-link, link-ieeg-yeo-labels, ieeg-channel-atlas-link | reproduced (link claims) |
| fig1e, figs1b, figs1c, figs1d | reproduced (exact Table S3 statistics) |
| fig1f (verbal reports) | blocked, data_missing |
| figs8a, figs8b, fig2c, fig2d, figs14g | reproduced (figs14g under the code's reading only) |
| figs12, figs15, figs27 | blocked, data_missing |
| fig2g | reproduced, assumed |
| fig2h | partially reproduced (4 of 6 networks) |
| fig2i, fig2j, figs13, fig3b, fig3c | reproduced |
| fig6c, fig6g, figs35 | reproduced |
| fig6e, figs37c, figs37b, figs38h, figs37a | reproduced, assumed |
| fig6i, figs38b | partially reproduced |
| figs38a | not reproduced |
| fig1k, fig1l, fig1m, figs2g, figs2h, figs5c, fig1p, figs2l, figs2n, figs2o, figs6 | reproduced |
| figs2bc, fig1no | partially reproduced |
| figs4 (licking) | blocked, data_missing |
| fig4b | reproduced, assumed (10 of 13 sessions) |
| fig6d, fig6h, fig5g | reproduced, assumed |
| fig5d, fig4g | reproduced |
| fig6f, fig5e, fig6j | not reproduced |
| figs34, fig4hi | partially reproduced |

The four not-reproduced claims:
- **fig6f:** a claim of absence (fast mouse activity unchanged). The ketamine-against-post test is significant (corrected p = 0.0045), so it fails the paper's own test.
- **fig5e and fig6j:** these follow the Methods, as the criterion says. The code's choices (target window 3 to 4 s after the last puff instead of 5 to 6 s; one pooled variance instead of per-neuron) give back the paper's values.
- **figs38a:** phase locking differs at baseline in theta and alpha in every channel selection. None of the selections gives the paper's 716 edges.

**(2) Dataset**
- **Version:** the only published version, 0.250528.0702, is pinned; the paper cites none. The mouse Neuropixels data are in DANDI:001326 (0.250528.1957).
- **Labels and scores that are only in the paper's code record** (Zenodo 14920570, which notebooks fetch at run time and md5-check):
  - None of the 142 mouse behaviour files says which drug, dose, mouse, sex or day it is.
  - The non-iEEG files do not say which series is saline.
  - There are no CADSS scores, verbal reports, lick data, Yeo network labels, bad-channel marks, infusion timing, or sleep and seizure annotations.
- **Format problems:**
  - Every spike train in 001326 is stored unsorted.
  - The LFP unit says "volts" but the values are digitiser units.
  - The puff sync channel is unnamed (called "CCEP" in some files, "DC03" in others).
  - Electrode coordinates are all NaN.
  - 001326 has no identifiers linking its mice to the paper's, and behaviour for 3 of the 13 recorded sessions is missing.
- **Paper and code problems:** Table S3's saline late value 0.34 contradicts its own t-test; the iEEG coding-dimension path swaps SD245's sessions; the code keeps per-trial epoch ranges that differ from the Methods; the stressed mouse that was excluded is never named.
- **Duplicates:** no recording is deposited twice.
- **Assumptions:** each is a deviation with `assumed: true` and a `methods_unavailable` question for the authors:
  - fig2g: the elbow rule for picking six NMF components.
  - Human projection z-scoring (Open C) and whether white matter is excluded (Open D).
  - figs38h: per-trial pre-puff subtraction.
  - The mouse epochs and which mouse was excluded (taken as mouse 5).
  - fig4b: dividing each trace by its maximum.
  - figs37a: which data enter the human-mouse comparison; fig5g: which doses enter the fits.
- **Reader questions:** none filed. Every point the sub-agents raised was a paper or code inconsistency, or a method left open, not a misreading by the claims file.

**(3) Where the protocol was unclear**
1. The author may add only link claims, but step 1.4 says each claim states its `data`. I set `data` and `depends_on` on 23 existing claims and changed no statement, expected value or criterion.
2. An absence claim tested with two tests, one of which finds the effect, has no partial outcome. I applied the binary rule, so fig6f is not reproduced.
3. When the criterion itself names the readings (fig6d epochs), it is unclear whether `assumed` is needed. I kept it only where an unstated choice also matters (the excluded mouse).
4. Outside selections such as bad-channel lists are neither labels nor inputs. I left those claims as `data: dataset`, since every outcome holds without the lists.
5. The dataset deposits the paper's own derived products (NMF factors, cluster contours). I refit from the deposited spectrograms and report agreement with the deposited outputs, which is exact.
6. A link claim cannot test a label the data cannot show (which series is saline). I recorded identity and counts as holding and said the label itself rests on the code.
7. "The notebook's summary" carries the failure sentence: with five notebooks, I put it in each one that has a failure.
8. The protocol assumes a single author context. I used parallel sub-agents, each with its own notebook and helper; the author stays accountable for the merged record.
9. 04_ieeg_cd.ipynb runs 11 min, above the 10-min aim but within the 60-min limit.

**(4) Runtime:** 05:36 to about 07:50 UTC, roughly 2 h 15 min; the entry itself runs in 22.5 min. Nothing failed. The claims checker flags one known item (p = 1.8e-09 printed as 1.80e-09).

Files are in `entries/001347-kauvar-2025/` (`README.md` first) and `attempts/001347-kauvar-2025-01.yaml`; the handover is in `executed/001347-kauvar-2025/handover/`.
