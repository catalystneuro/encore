I ran `tools/readme_row.py 000041 --write`, which added the row (8, 9, 15, 7) to README.md, and added the subsection below at the end of docs/pilot-notes.md. Nothing is committed. The untracked dotfiles and `scripts` in the repository root are sandbox mounts, not real files; the author's reports say the same.

### 000041, Watson et al. 2016

Eight claims reproduced, nine partially, fifteen not reproduced and seven
blocked, all on the dandiset; both rounds agreed with all 39 outcomes and
nothing was proposed, so there was no third round. The paper reports how
the firing rates of putative pyramidal cells and interneurons in the
frontal cortex of rats change across waking, nonREM and REM sleep, and
within and between sleep episodes. The rate distributions, burst index,
autocorrelogram peaks, packet durations and the rate changes over sleep
were tested, the microarousal claims on microarousals derived from short
Awake epochs. Six claims are blocked as `methods_underspecified`, because
the UP/DOWN state and spindle detection and the autocorrelogram decay fit
are described only in the Supplemental Experimental Procedures, which could
not be retrieved (PubMed Central and the publisher answer with a browser
check), and one, on movement in WAKE, as `data_missing`. Some outcomes rest
on weak ground: the last-packet mean of `fig3-first-last-packet` is 0.9679
against a bound of 0.968, and it and the nonREM peak of `fig2c-acg-peaks`
would fail without the seven sessions whose LFP could not be checked
against the spikes; `fig3d-first-last-slope` is reproduced, but its reading
that fast cells slow down and slow cells speed up is weakly supported;
`fig5c-delta-change` does not hold per session (p = 0.43); and
`fig5b-ma-between-packets` would meet its partial condition under a looser
microarousal rule picked after seeing the counts.

The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
It holds 22 sessions from 10 rats and 945 units (826 excitatory, 96
inhibitory, 23 unknown), where the paper and the dandiset's own description
report 27 sessions from 11 rats and the paper analysed 995 putative
pyramidal cells and 126 interneurons; which sessions and units were left
out, and why, is not stated. Two sessions are corrupt: in Dino-072114 the
spike times are whole seconds divided by 20000, because the conversion read
them from a CellExplorer file with a hard-coded 20 kHz rate, so its spikes
cannot be used; and the LFP of Dino-061914 has 125 columns for 128
electrodes, lasts 331.7 min against 291.9 min of states and spikes, and its
samples are scrambled. The state table holds only Awake, Non-REM and REM,
without the paper's microarousals, WAKE-SLEEP episodes, packets, UP/DOWN
states or spindles, and microarousals derived from short Awake epochs are
fewer than the paper reports (391 in 21 sessions, against 790 in 27). The
dandiset does not say how the states were scored, and the table may not be
the paper's scoring: it yields 30 WAKE-SLEEP cycles in 21 sessions, 3 of
them with none, though the paper kept only sessions with a full cycle, and
only 49 of 534 REM epochs are followed directly by Non-REM. Other findings:
the description gives 11 animals, 27 sessions, 1360 units and an age of
4-7 months, where the files hold 10 animals, 22 sessions and 945 units aged
3-7 months; the LFP is stored as int16 with unit volts and conversion NaN;
every electrode's location is "unknown" and every unit's region "CTX" or
"unknown", though the paper records from medial prefrontal, orbitofrontal,
anterior cingulate and secondary motor cortex; 23 units of one session have
cell type and region "unknown" with no description of the label; there are
no movement, accelerometer or EMG data, though the paper uses EMG to score
states and movement to define WAKE; and in 14 sessions the state labels
agree best with the spikes when shifted 5 to 60 s earlier, while the LFP
agrees with the spikes to within 50 ms in 14 of 21 sessions, three others
have a clear extreme 56 to 64 ms from zero lag, and in three agreement is
not established.

The author's points on the protocol: "open access" is not defined, and a
free-to-read author manuscript was taken as full text; no rule for a main
text available without its supplement, whose claims were blocked as
`methods_underspecified` though that reason is defined for a procedure
neither the paper nor its code fixes; no guidance on looking for code when
none is linked (the author read the conversion code, which explained both
corrupt files); a clock check by decoding shifted labels that is coarse for
states lasting minutes and does not apply to LFP; no guidance on a label the
paper uses and the dandiset lacks, or on corruption of single sessions; the
10% tolerance for correlations that depend on binning the paper does not
give, and fixed p-value thresholds that become stricter with fewer cells;
`measured` when no reading matches; no way to act on a check that shows a
criterion is not diagnostic; and a corrupt stream found after the criteria
were written and some results seen.
