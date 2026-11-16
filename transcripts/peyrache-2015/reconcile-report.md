I wrote the `reconciliation` block in `attempts/peyrache-2015-02.yaml`, added `earlier_findings.ipynb` to the entry, and locked, checked and ran the whole entry. All four notebooks pass (the new one in 158 s), the lock file came out unchanged, and `python tools/entry.py check entries/peyrache-2015` gives 0 errors. Nothing is committed.

**(1) Blind: yes.** The audit printed one line, in `transcripts/peyrache-2015/author.md:3584`. It is the author's own provenance runner URL (`github.com/catalystneuro/encore/actions/...`), not a sight of an earlier attempt. `blind: true`.

**(2) Earlier findings.** The new dataset version is a full reconversion, which fixed most of them.

| # | Earlier finding | Status | now |
|---|---|---|---|
| 1 | Units have no region, electrode, shank or quality measure | fixed (every unit labelled: 853 ADn, 365 PoS, ...) | |
| 2 | 1959 unit rows; the paper's 1077 cells can't be recovered | partly_fixed (1682 rows, shank, cluster_id, lratio, `in_lab_cell_list` 1351; the paper's selection is still unrecorded) | 4 |
| 3 | Open-field epoch not marked | fixed (41 of 42 sessions; the wake state lies wholly inside it) | |
| 4 | Unsorted spike times in 36 files | fixed (0 of 1682 units) | |
| 5 | Mouse12-120808 clock offset | fixed (best shift −0.1 to +0.1 s in each quarter) | |
| 6 | Raw LED positions stated in meters, hold pixels | fixed (unit pixels, conversion 1.0) | |
| 7 | Mouse32-140820 and Mouse17-130201 lack position or states; three Mouse20 position series end early | partly_fixed (Mouse17 fixed; Mouse32 still missing; Mouse20 still ends early, added as 11) | 1 |
| 8 | `dow`, `hdD` and `rip` have no description | fixed (now described TimeIntervals tables) | |
| 9 | Related resource name and identifier wrong | fixed | |
| 10 | No analysis code linked | still_present (added as 12) | 12 |

The two added findings are 11 (Mouse20 position ends 665, 4905 and 6538 s before the recording) and 12 (no code linked). Both carry `found: on_prompt`. I left `found` unset on the blind attempt's ten.

**(3) New findings:** 2, 3, 5, 6, 7, 8, 9 and 10 of `peyrache-2015-02`.

**(4) Outcomes that changed (15):**
- **`hd-cell-fraction`** went from partially reproduced to not reproduced. The new files label regions, and the rewritten claims file tests per-region counts. The thalamic HD count of 293 is above 242 ± 24.2 because the files include sessions of the dual-site mice that the paper discarded.
- **`fig3a-packet-60-degrees`** went from reproduced to partially reproduced. The earlier attempt pooled all pairs. The new claims file asks for each pair type, and PoS-PoS in SWS crosses at 54 and 108 degrees.
- **The 13 claims blocked earlier** (`metadata_insufficient`) were blocked because the earlier files had no regions; the new region labels let all of them be tested. Their new outcomes are 9 reproduced, 2 partially reproduced (`ensemble-sizes`, `adn-pos-peak-rate`) and 2 not reproduced:
  - `fig4e-ole-covariance` rests on an estimator the paper does not define.
  - `fig7-adn-pos-connections` fails partly because the files hold only 4765 ADn by PoS pairs against the paper's 6960.
- **Claims file:** for `fig5e-adn-predicts-pos`, the readout windows of the earlier statement moved to a claim of their own.

**(5) What did not fit the protocol:**
- **Earlier entry:** the checkout was a one-commit shallow clone, so `git log -1 -- attempts/peyrache-2015-01.yaml` returned the current HEAD, and that holds the new entry. I ran `git fetch --deepen=200` to reach commit `72c9fcd`, the earlier entry.
- **Pilot notes:** `docs/pilot-notes.md` has no headings for pilot-11 or pilot-15. The `protocol` note covers pilot-8, 9, 10, 12, 13 and 14 only.
- **One pointer per finding:** earlier finding 7 is partly in new finding 1 and partly still present outside it. A single `now` can name only one, so it points at 1 and the note names finding 11.
- **Stray files:** `scripts/` and several dotfiles appear untracked in the repo root, and `tools/backfill_summaries.py` and `tools/build_site.py` were already modified at the start. I didn't create or touch any of them, and the workflow's commit may pick them up.
