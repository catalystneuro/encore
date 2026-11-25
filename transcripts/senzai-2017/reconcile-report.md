I've written the `reconciliation` block in `attempts/senzai-2017-02.yaml` and added `entries/senzai-2017/earlier_findings.ipynb`, which is listed in `entry.yaml` and the README. Lock, check and run all succeed: lock left the lock file unchanged, check gives 0 errors, and both notebooks pass (the main one in 1313 s, the new one in 616 s). Nothing is committed.

**(1) Blind: yes.** The audit printed five lines. Four are links in `docs/protocol.md` and `README.md` (the pilot notes and the website). The fifth is the author writing its own `senzai-2017-02.yaml`. The author used no web tools and read no earlier record, transcript or git history. The only questions file it touched was the one it wrote itself.

**(2) Earlier findings (senzai-2017-01)**

| # | Earlier finding | Status | Now | Evidence on 0.261122.2143 |
|---|---|---|---|---|
| 1 | Spike-index overflow in 24 files | fixed | | No unit's spike times decrease (0 of 4216 units) |
| 2 | Genotypes don't match the paper | fixed | | 6 SST-Cre, 5 DRD2, 4 POMC-Ai35 (one is YutaMouse57), 1 wild type; the paper's YM21 is not in the dandiset |
| 3 | Shank given in only 18 files; no site coordinates | partly_fixed | 1 | Every unit now has a shank; sites still have no position |
| 4 | T-maze series not described | fixed | | Both series described in all 45 files |
| 5 | Brain states not described | fixed | | awake = wake; quiet and transit stated as not defined by the paper |
| 6 | No region for interneurons | fixed | | `region` column; 248 dentate narrow-waveform interneurons |
| 7 | Monosynaptic table not converted | partly_fixed | 4 | In 88 of 101 files; 13 lack it with no reason given |
| 8 | 609 GC / 568 MC; 237 units labelled `missing` | fixed | | YutaMouse57 is documented as not in the paper; without it 583 / 503; 245 units labelled "not in unit summary" |
| 9 | Duplicate light pulses in YutaMouse57-161006 | fixed | | No duplicates or decreasing times in any of the 1485 series |
| 10 | Two units-table layouts | fixed | | One layout; only YutaMouse33-150218 lacks waveforms |
| 11 | 'b' files: second probe or second session? | partly_fixed | 11 | Now "second recording session of the day … same probe"; whether they hold the same neurons is still not said |
| 12 | Burst-index threshold 1.2 vs 1.8 | still_present | 12 (added, `found: on_prompt`) | The labels don't settle it: 12 of 1654 excitatory units and 8 of 320 wide-waveform interneurons lie between 1.2 and 1.8 |
| 13 | Electrodes-table channel map wrong | fixed | | Largest wide-band spike is on the unit's shank for 356 of 356 units (earlier 45%) and at the table's site for 0.935 (earlier 9%) |
| 14 | Stored waveforms about 5× too large; filtering not stated; 1.6 ms window | partly_fixed | 3 | Scale fixed (ratio 1.05, unit documented); the cut-off window and unstated filtering remain |

**(3) New findings of senzai-2017-02:** 2, 5, 6, 7, 8, 9, 10.

**(4) Outcomes that differ** (all three: cause `dataset_changed`, confidence high)

| Claim | senzai-2017-01 | senzai-2017-02 | Why | Supports |
|---|---|---|---|---|
| unit-counts | partially_reproduced | reproduced | Same labels (609 / 568 over all 16 mice). The new version says YutaMouse57 is not in the paper, so leaving it out gives 583 / 503 | reproduced |
| interneuron-rates | partially_reproduced | reproduced | The new `region` column allows dentate-only interneurons: 7.65 / 2.053 Hz, against 5.96 / 2.57 Hz when CA3 was pooled in | reproduced |
| gamma-rate-correlation | partially_reproduced | not_reproduced | Excluding YutaMouse57 moves MC under reading (b) from -0.253 (P below 0.0001) to -0.182 (P = 0.00019) | not_reproduced |

For gamma-rate-correlation I ran a small check outside the entry, using the blind attempt's phase code on all files. Without YutaMouse57 it gives the blind numbers exactly. With YutaMouse57 it gives MC r = -0.245 (472 units, P = 7.1e-08). Applying the earlier attempt's other rules (at least 10 spikes, awake periods of at least 10 s, uncorrected kappa) changes nothing on the 15 mice. The check is not saved in any notebook.

**(5) Protocol things that did not fit**
- **Missing pilot notes:** `docs/pilot-notes.md` stops at pilot-14, and there is no section for pilot-11. The changes in pilot-15 to pilot-18 (the `about` field, author notes, severity ratings) appear only in `tools/entry.py` and `docs/protocol.md`, so the `protocol` note describes them from there.
- **No git history:** the repository has a single commit, so `git show $c:entries/...` gives the new entry, not the earlier one. I used `earlier-entry/` for the earlier attempt's code.
- **Paper-level finding:** earlier finding 12 is about the paper, so a new dataset version cannot fix it. I marked it `still_present` and added it with `found: on_prompt`, with a data section that shows the labels can't settle which threshold was used.
- **'b' file count:** both records say seven 'b' files, but there are eight. YutaMouse51b160514 has no same-day partner, so there are seven same-day pairs.
- **Stray files:** untracked dotfiles, `.idea`, `.vscode` and `scripts/` appeared in the checkout during the run. I didn't create them and left them alone.
