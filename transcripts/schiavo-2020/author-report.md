I've done steps 1 to 6 of the Author protocol for DANDI:000249. The entry is in `entries/000249-schiavo-2020/` and the record is `attempts/000249-schiavo-2020-01.yaml`. `entry.py all` passes with 0 errors (the notebook runs in 89 s), and the handover is built. Nothing is committed.

The main result is that the dandiset itself supports almost nothing. It holds raw, unaligned two-photon movies with no ROIs, no stimulus times and no record of the order in which the calls were played. So all 20 imaging claims are blocked, and only the link claim could be tested on the dandiset's own data. The other tested claims use the whole-cell, slice and operant recordings in the figshare collection the dandiset links, which the claims file marks `data: elsewhere`.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| subject-group-link | partially reproduced |
| fig1g-ipsc-depress-faster | not reproduced (rests on an assumption) |
| fig1i-operant-prototypes, ed5b-press-count-unchanged | blocked: methods underspecified (the readings the criterion names disagree) |
| ed6ef-epsc-tuning, fig2j-ie-ratio-tracks-isi, fig2k-ipsc-exceeds-epsc-575 | not reproduced |
| fig2h-epsc-enhanced-ev | partially reproduced |
| fig2i-ipsc-weaker-nv | blocked: methods underspecified (largest 5 trials vs largest 10 give different outcomes) |
| ed9b-oxytocin-enhances-spiking | reproduced (rests on an assumption) |
| ed6h-dams-evs-epsc-similar | blocked: metadata insufficient |
| 20 imaging claims, fig3-retrieval-onset-range | blocked: metadata insufficient |
| 11 behaviour claims, fig1a-isi-distribution, ed4d-response-tracks-isi-probability | blocked: data missing |

**2. What was found**
- **Dandiset contents:**
  - Every one of the 777 files is just a movie.
  - The movies show no usable peak at the 0.1 Hz call rate, so call onsets can't be recovered from them either.
  - The retrieval behaviour and vocalization recordings are in neither the dandiset nor the figshare collection.
  - The paper's own figshare DOI does not resolve.
- **Metadata errors:**
  - Three recordings are deposited under both NV58 and NV63, with identical frames and start times.
  - EV56 and EV62 are described as "NV56" and "NV62" in their own files.
  - Indicator and location are "unknown" in every file.
  - The start of cohousing is not recorded.
- **Figshare whole-cell data:**
  - The microphone channel shows the morph ISIs are 125, 175, 275 and 575 ms, as the figure legends say, not the Methods' 125, 225 and 575 ms. They are played in a fixed order, not pseudorandom.
  - File 19424013 is listed at -70 mV but carries about +560 pA throughout.
  - Two listed files are not deposited.
  - The spreadsheets don't say which cells come from dams, which is why ed6h is blocked.
- **Noise drives the in vivo result:**
  - The trial-averaged current follows the call in only 3 of 26 EPSC cells.
  - The experienced recordings are about twice as noisy as the naive ones.
  - The experienced-vs-naive difference in fig2h is just as large in a window before the call. So the partial result there shows no call-evoked enhancement.
- **Operant files:** touch times are printed to 5 significant digits, so after 1000 s of a session they step by 0.1 s.
- **Assumptions (each marked `assumed`):**
  - fig1g: how the slice peak is measured (2 to 30 ms after each pulse, against the 5 ms before it).
  - ed9b: that Dunn's comparisons are five planned baseline-vs-post tests. Over all 45 pairs the outcome changes.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which gap between touch samples ends a lever press, and which sessions were compared.
  - How many of the "largest 5-10 trials" were averaged per cell.
  - How a "significant PSC" was defined for the inclusion rule.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. The claims file says to block when readings disagree, while step 1.6 allows adopting the best-supported reading as an assumption. I followed the claims file for fig1i and ed5b. For fig2i (5 vs 10 trials) there was no basis to choose, so I blocked it.
2. The clock check ("decode a task variable around trial starts") doesn't fit files with no stimulus times. I used the recorded microphone channel to time the calls, and compared the call window with a window before the call.
3. The protocol has no rule for a measure, taken exactly as the Methods define it, that turns out to track noise. I let the criterion decide the fig2h outcome (partially reproduced) and put the noise control in the notes and findings.
4. `docs/archives.md` has no figshare section. Its ABF files can't be streamed with the usual tools, so I read them into memory through a small shim around pyabf.
5. The repository root has untracked dotfiles and folders I didn't create (`.bashrc`, `.gitconfig`, `.idea`, `scripts`, and others). I left them alone; they shouldn't be committed.

**4. Runtime and failures**
The run took about 33 minutes (03:32 to 04:05 UTC), so no claim was blocked for time. Nothing failed.
