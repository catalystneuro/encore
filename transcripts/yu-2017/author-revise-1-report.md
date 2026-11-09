I've revised the attempt for round 1 and re-ran the entry: `python tools/entry.py all` reports 0 check errors and the notebook ran from a clean environment in 808 s. Its outputs match my development run line for line. Nothing is committed.

## Outcome changes
Totals now: 11 reproduced, 7 partially reproduced, 11 not reproduced, 3 blocked (before: 12, 6, 11, 3).

- **fig2s1cd-theta-autocorrelation: reproduced → partially reproduced.** I now take entries and exits from well visits: immobility periods of at least 0.5 s within 15 cm of a well (radius and minimum length are my choices; the paper gives neither). On those visits, the IAP theta peak at entry is not deeper when moving than when still (0.00089 against 0.00093, nearly a tie). The other three cases hold.
- **fig1-iap-map-counts: still blocked, but `data_missing` instead of `not_runnable`, as the verifier gave it.** The paper does not say which W-track rats or days it used, and some come from Kay et al. 2016.
- **fig4s1b-offset-matched-coactivity: kept as reproduced, against the verifier's partially reproduced, and the disagreement is recorded.** The verifier suspected the 4 to 5 s bin was inflated by pairs whose peak sits at the edge of the ±5 s window. With those pairs left out the bin still passes (p = 0.0004). The criterion accepts a result under any one of its listed readings.

## What I added or corrected, by verifier point
1. **SWR threshold:**
   - The data check now prints the fraction of immobile time inside events (9 to 14%) and of immobile samples above the threshold (13 to 20%).
   - The same threshold rule on synthetic pure noise lets 13% of samples through.
   - A fixed 3 SD threshold (about 0.2 events per second) is run as a check on fig4a, fig3c, fig5 and fig5dg; none of their outcomes changes.
   - I kept the claims file's reading and added a question to the new `questions/crcns-hc-13.yaml`.
2. **Foraging rats only:** the header and summary now say the outcomes of claims that need the W-track data are those of the foraging-only test.
3. **Entry/exit windows:** windows around every immobility period cover 32 to 62% of task time (median 53%); around well visits 9 to 37% (median 25%). fig1s1d, fig2c, fig2s1ij and fig4s3 are run under both definitions, and their outcomes do not change. I also fixed a bug: the fig2c cell printed the criterion's own side of zero lag as "the other side".
4. **Peaks pinned at the window edge:** histograms of the peak offsets for all three windows are printed, with variants that leave the pinned pairs out (fig4s1b, fig2s1ij).
5. **fig5s1d:** now uses 100 shuffles and 100 duration-matched draws per unit. The averaged test gives p = 0.36 and 0.73, so it is still not reproduced. Single shuffles vary widely (median p = 0.11).
6. **fig4s3:** the direction of the comparison with IAP-IAP pairs is now printed and stated (MAP-IAP is higher, the wrong way).
7. **fig4a:** added a variant restricted to the 12 days that have both IAPs and MAPs.
8. **fig6e and fig5dg:** the conclusions now say the tests treat shared units as independent, which overstates the evidence.
9. **Maze paths:** an occupancy image is added. About a quarter of moving frames are on diagonal paths, so fig1f is also run with the diagonals and with a 0.1 s minimum occupancy. Both stay null.
10. **Data checks:**
    - The 11 unit-days with no recorded area are counted and recorded as a finding.
    - The note on how the LFP is referenced now cites the paper's Methods, not the data descriptor.
    - The timing check between spikes, LFP and position now uses all CA1 units, so it covers R1 and Q1.
    - I corrected an earlier false statement that Q1's fourth well sits nearer the maze centre.

The attempt record has the round-1 verification for all 32 claims, with the verifier's reasons and my responses. The README and the notebook runtime (14 min) are updated.

## Not done
- **Pooled tests with the W-track rats:** not run, because the paper's selection of them cannot be identified.
- **Why R1 and N2 spike widths run long:** cannot be checked, since the data set holds no spike waveforms.
- **Untracked files:** dotfiles such as `.bashrc` and `scripts` in the working tree predate this run. I left them alone.
