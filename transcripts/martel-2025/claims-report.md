I've written `claims/001174/10.1016-j.isci.2025.112767.yaml`. The quote checker passes: 23 claims, 22 quotes, 6 statistical values, 0 problems. Nothing is committed.

**Text read.** I read the version of record from Europe PMC (PMC12192352): main text, figure legends and STAR Methods. The bioRxiv preprint (v1) was used only to look up method details; its analyses differ and none of its numbers are used. No PDF was supplied, so no figure was viewed.

**Missing.** The supplement (Document S1: Figures S1–S3, Tables S1–S3) is not in the text. I still wrote claims, because every result the claims rest on is stated in the main text. Each claim that touches the supplement says so:
- Table S2 would give the cell counts per session; `cell-counts` has to choose between two readings without it.
- The Figure S1 legend would say which monkey U session and how many trials; the three monkey U alignment claims can't confirm it.
- The Figure S2 legend would fix what the sequence-distance comparison is.

**Code read.** Four Zenodo records: event-based MATLAB 14963213, Jaccard R 14977106, sequence MATLAB 14963234, and MonkeyLogic task files 15346239. The opening comment records the md5 sums. There is no code for the Fig. 1D–F statistics. The code reads which cells are the same across sessions from a spreadsheet (`Metadata_all_monkeys.xlsx`) that was never deposited.

**Claims.**
- **Counts:** 22 findings plus 1 link claim, which checks the dandiset against the paper's Zenodo per-cell table.
- **Quotes:** 22 have quotes; the link claim needs none, so no claim uses `inferred`.
- **Statistics:** 4 claims carry 6 entries: the monkey U SMA amplitude test (p = 0.032), the M1-versus-SMA event rate tests (p < 0.001, twice), the task amplitude test (p = 0.03), and the synchrony tests (p = 0.07 and 0.22).
- **Criteria:** all 23 have one.
- **Outside data:** two histology claims use data on Zenodo 15328390 (`elsewhere`).

**Details left open, and the readings named:**
- **Fig. 1 tests:** the grouping is either per region with monkeys pooled, or per monkey and region. The false-discovery-rate correction family is either all three measures together or each measure alone. Whether monkey V's second recording counts as task is also open: the text says only Q and U did the task, but the code treats it as task.
- **Fig. 1 per-cell value:** the cell's value in its first session (as the Methods say), or its median over sessions (as the legend says).
- **Cell counts:** unique cells, or the sum over sessions.
- **M1-versus-SMA tests:** uncorrected, or corrected.
- **Fig. 2, which cells enter the magnitude tests:** one value per significant condition, or one per cell.
- **Fig. 2, where the code and Methods disagree:** I followed the Methods and kept the code's choice as a variant:
  - the code corrects each condition separately, the Methods correct each chamber as a whole;
  - the code's example call aligns Q's trials on the touch;
  - the code skips the last trial of each condition.
- **Fig. 3A,B, synchrony against distance:** the paper reports no test. The test is either Pearson or Spearman correlation, and the example session (not named) can be any monkey U session.
- **Fig. 3C:** the Methods use 1,000 random shifts per pair; the code's SMA loop uses 10, kept as a variant.
- **Sequences:**
  - The paper gives 0.05 s to two different settings in two places. Readings: it applies to both, to the gap between events only, or to the gap between repetitions only.
  - Which 10 minutes are analysed: the first 10 min of each part, or the last 10 min of the task.
  - Minimum repeats: at least 4 (Methods), or more than 4 (the code's rule) as a variant.
  - Single-cell repeats: left out, as the Methods require two or more cells; the code includes them, kept as a variant.
  - The example sessions of Fig. 4A and 4B are not named; any Q session with 40 or 18 cells counts.
- **Fig. 4C:** what is compared is either centroid positions or distances within a sequence. The paper reports no test, so the readings are a Kolmogorov–Smirnov test or a Mann–Whitney test.

**Other discrepancies, recorded in the file:** the two-target task script holds the centre target for 600 ms and allows 500 ms to release, where the Methods say 1 s and 1 s. The paper says cells per session ranged from 23 to 129, which are the same numbers as the per-site totals.
