I've finished the author steps (1 to 5) and the handover (step 6) for DANDI:001474. `tools/entry.py check` reports 0 errors and the notebook runs clean in 103 s. Of the 37 claims, 24 are reproduced, 6 partially reproduced, 5 not reproduced and 2 blocked. Nothing is committed and I did not verify my own work.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| supp1i, supp1h, fig1gh, supp1e | Reproduced |
| fig2b, fig2c, fig2d, fig2fj, fig2p, fig2km, fig2q, fig2r, fig2s | Reproduced |
| supp2a, supp2fg, supp2j, supp2k | Reproduced |
| fig3i, fig3k, fig3c, supp3c, supp3j, supp3l | Reproduced |
| supp3q | Reproduced (assumed) |
| fig1k-early-late-recordings, fig1l, fig1c, fig2e, fig3h | Partially reproduced |
| supp3m | Partially reproduced (assumed) |
| fig1k-lme, supp2h, supp2lp, fig3j, fig3-hfd-hfd-short-meals | Not reproduced |
| supp1cd | Blocked: methods_underspecified (its criterion's readings disagree) |
| supp2q | Blocked: data_missing (no training sessions in the dataset) |

## 2. The dataset, assumptions and questions

**Version.** I pinned 0.251031.1725, the only published version. The paper cites none, and the draft has the same 349 assets and size.

**What is in it.** Each file holds per-trial matrices (Ensure pump, licks, signed running, a Z-score computed by the depositors), the raw 465 nm trace, and notes with diet, fasting, Ensure volume and body weights. There is no 405 nm control, no trial table or tone times, and no training sessions.

**Findings about the data:**
- **Duplicates.** Four `ses-None` files are byte-identical copies of dated files.
- **Missing mouse.** Cohort 2 has 6 of the paper's 7 HFD mice (a male is missing). Other groups are 1 to 5 recordings short of the paper's counts.
- **Z-score mismatch.** In 32 files the deposited Z-score does not match that file's own raw trace.
- **Column counts.** In 27 files the series have different numbers of trial columns.
- **Rate.** The stored rate is 1 Hz in about half the files; the data are at 50 Hz.
- **Sex.** MPK173 and MPK182 have different sex labels in their first- and second-phase files.
- **Age and dates.** Every file gives age "P12W/", and one MPK191 file is dated 2024-01-02, before that mouse's first recordings.
- **Undocumented fields.** The notes fields have no units or definitions, and the running signal's sign is not described.
- **Lost signal.** 12 trials in two MPK120 recordings lose the signal; I left them out of the raw-trace measures.

**How I computed the Z-scores.** I computed the claims file's two Z-scorings (Z1, Z2) from the raw trace. I located trial onsets by correlating it with the deposited Z-score, or used the modal onset in 58 files where that was not possible. The deposited Z-score (Z0) is shown only as a variant. This matters for fig1k-lme: under Z1/Z2 the HFD-above-NCD early effect has p 0.09 to 0.35, while under Z0 it holds at p < 0.001.

**Assumptions:**
- **supp3m.** I used recordings with ≥30 triggered trials, the Methods' default. With ≥15 the claim would be reproduced.
- **supp3q.** I read the notes' `ad lib bw` and `before ad lib bw` fields as weights B and A of Supp. Fig. 3k; the files do not define them.
- **Running speed.** I used the absolute value of the signed running signal; the signed mean is shown as a variant.
- **Per-mouse SD.** "A single Z-score per animal" could mean all of a mouse's recordings or only one diet phase, so I ran both readings (Z1/Z2 and Z1p/Z2p).

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
1. How was the Z-score computed?
2. How was the Supp. Fig. 1d lick AUC normalized?
3. Which recordings enter Supp. Fig. 3l–q, and what do the weight fields mean?

I asked no questions of a reader.

## 3. Where the protocol was unclear

1. **Streaming.** archives.md says to use `remfile`, but it took about 30 s per file here. I read each file whole into memory with one HTTPS GET (about 1 s per file, nothing on disk) and said so in the helper.
2. **Deposited derived values.** The protocol does not say whether a quantity the depositors computed, here their Z-score, can count as a reading. I kept it as a variant; this changes how fig1k-lme reads.
3. **Criterion versus step 1.6.** supp1cd's criterion says to block when its readings disagree, while step 1.6 would let me adopt the best-supported reading. I followed the criterion.
4. **`measured` when no reading matches.** "Record the first reading the criterion lists" doesn't cover this case. I recorded the first-listed combination for most claims, but the closest one (Z2) for fig1k and fig1l, so the choice is not uniform across claims.
5. **Unstated recording sets.** Where a criterion leaves the set open (supp2fg, supp3l, supp3m), the protocol's rule for absence claims does not cover a choice of selection. I ran both sets, and recorded it as an assumption where they disagree.
6. **Repo root.** Device files created by the sandbox (`.bashrc`, `.mcp.json`, `scripts` and others) show as untracked there. I left them alone; the commit step should not pick them up.

## 4. Runtime and failures

The session took about 50 minutes (17:18 to about 18:07 UTC). The notebook runs in 103 s, of which 79 s is reading the files.

The first metadata survey with `remfile` took 10 minutes. During development I found and fixed four bugs:
- The Tukey p-values were rounded to 0, and the sign of the differences was reversed.
- Z2 exploded in the trials with a lost signal.
- Some files have mismatched column counts, which broke indexing.
- The alignment table showed the wrong offset for the unmatched files.

Nothing failed in the final run, and its outputs match the development run line for line.
