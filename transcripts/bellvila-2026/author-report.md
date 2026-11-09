One of the 45 claims was tested, and it reproduced, resting on an assumption about the channel layout. The other 44 are blocked. The entry passed `tools/entry.py all`, and the handover is built in `executed/001678-bellvila-2026/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| efield-20min-median | **Reproduced (assumed)**: 1.83 mV/mm (median of rat means) and 1.53 (median of all 117 estimates), expected 1.65 ± 0.21 |
| efield-1min-medians | Blocked, data_missing |
| fem-depth-falloff, fem-lognormal-fits, fem-ellipsoid-axes | Blocked, data_missing (they depend on efield-1min-medians; Sim4Life is commercial and the ViZOO model is licensed) |
| units-1min and the 25 claims on 1-min spikes or LFP | Blocked, data_missing |
| units-20min, 20min-during-percentages, 20min-post-percentages, 20min-magnitudes | Blocked, too_large (spike sorting estimated at 118 min against the 60-min notebook limit) |
| 4 power and 4 PAC claims | Blocked, too_large (their channels are chosen by the 20-min neurons) |
| sham-no-fr-change, sham-lfp-baseline | Blocked, data_missing |

For the field, the per-electrode pairing gives 1.65 (median of all estimates, within) and 1.89 (median of rat means, just outside). The "largest pair per axis" reading gives 3.70, outside. The criterion says one matching reading is enough. The spread between rats is wider than the paper's ±0.21 (standard deviation of rat means 0.73).

## 2. The dataset

I pinned 0.260227.1824, the only published version; the paper cites none, and the draft holds the same files.

- **1-min files:** each holds one channel per trial, "S1r 1". It is the stimulation command, a sinusoid whose peak equals the current in µA. There is no recording, no LFP and no stimulation monitor.
- **Trials:** 15 to 23 per rat where the paper says 20. Three rats lack some combinations, and one trial at 100 Hz and 20 µA is outside the paper's design.
- **20-min files:** they hold one 16-channel stream at 12207 Hz. It is not low-passed at 300 Hz or notch-filtered, and it carries spikes. There are no sorted units, epochs or electrode positions.
- **Units:** every series says volts with a conversion of 1e-6, which is wrong both ways: the 1-min values are µA and the 20-min values are already volts.
- **Sex:** the 20-min subjects are 6 male and 7 female; the paper says 7 male and 6 female.
- **Sham:** the sham rat is not in the dandiset. Science Data Bank, where the paper says its data are, refuses access without a login.

**Assumption:** channels aw_1 to aw_16 sit row by row in the 4 × 4 grid. The data support this: at most 1.35% of 2000 random orders are as smooth in any rat, and a serpentine order gives the same outcome.

**Questions for the paper's authors** (recorded as a methods_unavailable finding):
- What is the channel layout of the array?
- How are the differences along the two axes paired for the vector addition?
- Over which set is Grubbs' test applied?
- Is the 1.65 median taken over rats or over all estimates, and what is the ±?

I asked a reader nothing.

## 3. Protocol points

1. The claims file's opening comment says that when readings give different outcomes the claim is blocked as methods_underspecified, but the field criterion says one matching reading reproduces it. I followed the claim's own criterion, as the protocol does for readings of a reported number.
2. A too_large block needs a timing, but the protocol says numbers in the record must come from the notebook. I put the timing run (5 and 15 minutes of one rat) in the notebook, which adds about 4 minutes to it. Its estimate varied between 113 and 126 minutes across runs; the record uses the executed run's 118.
3. The protocol doesn't say whether a sorter may write working files. Mine writes only its own output, to a temporary directory; the data are streamed.
4. Results can't pass between notebooks, so splitting the sorting to fit the 60-minute limit isn't possible. I blocked as too_large and named not_runnable in the notes: the paper's SpyKING CIRCUS 1 installs, but finds no MPI library.
5. Whether a claim with a 1-min and a 20-min part is blocked for the 1-min reason alone isn't covered. For baseline-fr and baseline-ppc I gave data_missing as the main reason and put too_large in the notes.
6. The newest example record follows an older protocol version (pilot-5); I followed pilot-13's text.

## 4. Runtime and failures

The notebook takes 8 to 9 minutes, and I ran it in full three times. One early detection bug (stimulation onset read from a single channel, which shortened two rats' stimulation periods) was found and fixed before the final runs. Nothing else failed.

The repository root shows untracked items (`.bashrc`, `.gitconfig`, `scripts`, `.idea` and others). They are sandbox device mounts that existed before this run, not my files, and should not be committed.
