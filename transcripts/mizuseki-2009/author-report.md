I tested 11 of the 37 claims on CA1 alone; the other 26 are blocked because hc-2 doesn't hold the data. The entry passes its checks and ran twice from a clean environment with identical numbers, and the handover is built. I did not verify the work myself, as the protocol requires.

## (1) Outcomes

| Claim | Outcome |
|---|---|
| fig3-interneurons-min-ascending | Reproduced on CA1 (assumed). Minimum firing at 335° for pyramidal cells and 315° for interneurons |
| figs9-phase-method | Reproduced (assumed). The three phase methods agree within 0.7° |
| figs12b-burst-single-phase | Reproduced (assumed). 64 of 226 cells differ by more than 90°, 177 of 226 by Watson-Williams test |
| figs19-fast-firing-minority | Reproduced (assumed). 0.546 of spikes at 4–12 Hz against 0.049 at ≥40 Hz |
| figs7-individual-rats | Reproduced (assumed). The three rats agree within 8.5° (pyramidal cells) and 31.9° (interneurons) |
| fig3d-hippocampal-modulation | Partially reproduced (assumed). Mean R 0.193 is inside tolerance; 93.0% modulated is just above the 92.4 bound |
| fig5-rate-phase-shift | Partially reproduced (assumed). CA1 advances 130.2° against the criterion's 135° |
| fig5b-burst-double-peak | Partially reproduced (assumed). Double peak present, but burst and ≥40 Hz spikes are 154° apart |
| figs11-phase-time-agreement | Partially reproduced (assumed). r = 0.614 for pyramidal cell–interneuron pairs, 0.146 for pyramidal pairs |
| figs13-interneuron-rate | Not reproduced (assumed). Interneuron phase shifts 59.6° against a bound of 33° |
| figs2-ripple-sequence | Not reproduced (assumed). Fold increases of 10.05 or 7.41 (pyramidal) and 4.41 or 2.12 (interneurons), against about 6 and 3 |
| tables1-cell-counts | Blocked, data missing. Every expected count includes other tasks or rat i01; the hc-2 counts are shown |
| 25 claims on EC, CA3, DG, other tasks, linear track, or the Montgomery et al. current-source-density phases | Blocked, data missing |

## (2) Dataset, assumptions, questions

**What hc-2 holds:**
- **Scope:** 21 open-field CA1 sessions from rats ec13, ec14 and ec16, 920 session units (672 distinct units). There are no EC, CA3 or dentate cells, no other tasks, and no data from rats ec12 or i01. hc-2 has no versions, so the 21 files read are pinned by their MD5 sums from `checksums.md5`, printed in the notebook.
- **Missing labels:** no unit carries a cell-type or layer label (the `.xml` unit fields are empty), nothing says which channel is in the pyramidal layer, and positions are in pixels with no scale.
- **Noisy channel:** in ec016.582 the channel with the most ripple-band power is noisy. Picking it at first broke the clock check, so the channel choice now skips channels that don't correlate with their shank.
- **Animal naming:** sessions ec015.041 and ec015.047 are listed under rat ec14.
- **Clocks:** spikes, LFP and positions share one clock in all 21 sessions, shown by three shifted-signal contrasts.
- **Duplicates:** no session was deposited twice.

**Assumptions, each varied in the notebook:**
- **Theta reference:** CA1 pyramidal-layer LFP replaces EC3, which hc-2 lacks.
- **Theta epochs:** theta-to-neighbouring-band power ratio above 2 and running speed above 3 cm/s.
- **Cell types:** a unit is an interneuron if its trough-to-peak latency is under 0.4 ms or its mean rate is over 10 Hz.
- **Ripples:** the bin width and the baseline for the fold increase.

**Questions for the paper's authors,** recorded as `methods_unavailable` findings:
- What thresholds defined the theta epochs?
- What thresholds separated hippocampal principal cells from interneurons?
- Which bin and baseline give the ripple fold increases?

**Questions to a reader:** none.

## (3) Where the protocol was unclear

1. `docs/archives.md` covers only CRCNS zips, but hc-2 is gzipped tarballs. I streamed each one once with `fsspec` and `tarfile` in stream mode.
2. Some claims have expected values that all involve missing rats or tasks (tables1), yet the dataset still gives related counts. I blocked the claim as `data_missing` and put the counts in the notes.
3. The protocol forbids downloading but doesn't say whether reduced data may be cached while developing. I cached reductions in `$TMPDIR` for development only; the notebook streams everything.
4. When several assumptions underlie nearly every outcome, the protocol doesn't say how to show this compactly. I marked every tested outcome `assumed: true` and listed shared deviations on each.
5. The criterion for fig5-rate-phase-shift failed narrowly (130° against 135°) while the effect is clearly present. I chose `partially_reproduced` ("present but weaker").

## (4) Runtime and failures

The notebook takes about 10 minutes, most of it streaming 22 GB, with peak memory of 3 GB plus three loader workers. Agent work ran from 20:49 to about 22:10 UTC.

Two things went wrong along the way, both fixed:
- **Empty conclusions:** a bug in my notebook builder left the conclusion cells as placeholders in the first full run; the second run corrected this.
- **Wrong reference channel:** the first channel choice picked noisy channels in ec013.844, ec016.397 and ec016.582. This was fixed before the final runs.

Nothing failed in the final run.
