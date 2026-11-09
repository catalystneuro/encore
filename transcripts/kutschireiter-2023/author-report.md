I've finished steps 1 to 5 and the handover (step 6), in about 1 h 20 min (22:52 to 00:10 UTC). The entry passes `python tools/entry.py all` with 0 errors and the notebook runs in about 9 minutes.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1-conflict-decreases-certainty | reproduced |
| fig2h-bump-tracks-circkf | reproduced |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced |
| fig3b-bayesian-beats-conventional | reproduced |
| fig3c-update-weights | reproduced |
| fig3d-best-network-slow-decay | partially reproduced: condition (4) fails, with two small rises (0.0008 and 0.0014) |
| fig3f-noise-drop-below-70 | reproduced (63.1% at noise SD 10) |
| fig3f-retuning-reduces-drop | reproduced: measured 34.64% (expected 35 ± 3.5) |
| noise-effects-on-mu-and-kappa | partially reproduced: bump amplitude falls under noise instead of drifting up |
| fig4b-connectome-motifs | reproduced, resting on an assumption (`assumed: true`) |
| fig4gh-drosophila-network-matches | partially reproduced: holds within 0.02, not within 0.01 |
| figs2-performance-independent-of-n | partially reproduced: one value (N 16 at 0.1/s) is 0.041 off |
| prediction-bump-amplitude-cue-reliability | blocked, `methods_underspecified` (the claim's readings disagree) |

### 2. The dataset, assumptions and questions

**What the dataset is.** The paper is a theory paper. The dandiset holds imaging of EPG neurons from a separate study by the same lab (Basnak et al.), and the paper uses none of it. Twelve claims are tested on the paper's Zenodo code and outputs (doi:10.5281/zenodo.7615975) and on the public hemibrain v1.2 export. The prediction claim is tested on the dandiset's cue-contrast experiment (subjects 1 to 15).

**Version.** I pinned 0.240801.1040. It is the only published version, and the draft is identical in assets and size.

**Findings recorded:**
- **Wrong paper link.** The dandiset links this paper's preprint, which uses none of its data.
- **Wrong imaging rate.** `imaging_rate` says 9.18 Hz for every file, but sub-4 and sub-10 are imaged at 7.87 Hz.
- **Odd trial table.** sub-2 has one high-contrast block where every other fly has two, and a 405 s final block labelled low.
- **dF/F not described.** The stored dF/F matches the raw imaging only after spatial smoothing (correlation 0.66 without, 0.93 with), and the files don't say how it was made.
- **Paper's code issues.** Two code issues block running it as released (a missing `z` argument, a `kappa_y`/`kappa_v` keyword mismatch). Its network's amplitude falls under noise, against what the SI predicts.
- **Clock check.** The bump phase follows the cue position with peak coupling at lag 0 to 5 frames, so the dF/F and the cue share a clock.

**Assumptions (fig4b):**
- I sorted neurons by protocerebral bridge glomerulus only. The other sort the criterion names can't be formed because hemibrain names carry no ellipsoid body position.
- Any synapse counts as a connection.
- I defined the PEN1 offset as a synapse-weighted circular mean, since the paper gives no measure.

**Questions for the paper's authors (recorded as `methods_unavailable` findings):**
- Which signal, comparison and test should test the bump-amplitude prediction? Here the answer changes with the choice: raw fluorescence gives p 0.021, dF/F gives p 0.138.
- Which spatial position was used to sort neurons in Fig. 4B?

**Questions to a reader:** none.

### 3. Where the protocol was unclear

1. **Theory paper.** The protocol assumes the dataset holds the paper's data; here it doesn't. I tested the twelve `elsewhere` claims on the paper's Zenodo deposit, held in memory and pinned by DOI and md5.
2. **A named reading that can't be run.** The protocol doesn't cover the case where one of the criterion's readings can't be formed from the data (fig4b's second sort). I judged on the reading that can be run and marked the outcome as resting on an assumption.
3. **"All readings" versus "any reading".** The claims file requires every reading to hold for unquantified words (fig4gh, figs2), while the protocol lets a number be reproduced under any reading. I followed the claims file, so both are partially reproduced.
4. **Block versus adopt an assumption.** The prediction's criterion says to block when the readings differ, while step 1.6 allows adopting the best-supported reading. I followed the claims file and blocked.
5. **What counts as public.** neuPrint, which serves the v1.2.1 connectome the paper used, now needs a personal token. I used the public v1.2 export and recorded the difference as a deviation.
6. **Scope of the duplicate check.** I compared traces only among the 15 sessions the analysis uses. The other 206 files were surveyed by metadata only.
7. **Streaming outside inputs.** The streaming rule is written for the dataset; I read the 0.8 MB zip and the 46 MB tar whole into memory, never to disk.
8. **Partial versus not reproduced.** When one condition of a multi-condition criterion fails but the effect is present (fig3d, the noise claim), I recorded `partially_reproduced`.

### 4. Runtime and failures

- The notebook runs in about 8.5 to 9 minutes, most of it streaming 10% of the raw imaging for the 15 sessions.
- Nothing failed. The paper's large simulation scans (10,000 trajectories per setting) were not re-run; the claims are judged on the stored outputs, as the claims file says.
- I left untracked files I didn't create (`.bashrc`, `.idea`, `scripts`, and others) in the repository root untouched.

Files are in `entries/000289-kutschireiter-2023/`:
- `reproduce_kutschireiter_2023.ipynb`
- `bra.py`
- `README.md`
- `entry.yaml`

The attempt record is `attempts/000289-kutschireiter-2023-01.yaml`, and the verifier package is in `executed/000289-kutschireiter-2023/handover/`.
