I've done steps 1 to 5 and the handover (step 6). The entry is `entries/000294-buccino-2024/` and the record is `attempts/000294-buccino-2024-01.yaml`. `entry.py all` passes with 0 check errors, and the notebook ran from a clean environment in 382 s. I pinned version 0.260528.0854: it is the only published version, the paper cites none, and the draft holds the same two files.

**1. Outcomes (23 claims)**

| Claim | Data | Outcome |
|---|---|---|
| recordings-two-cells-runs | dandiset | reproduced (2 cells, 5 and 4 runs, median run 195.8 s) |
| ecode-protocol-structure | dandiset | reproduced (all 8 protocols in all 9 runs; IV is reading a, -140 to 60%) |
| holding-potential | dandiset | reproduced (-69.54 and -69.12 mV, not corrected for the junction potential) |
| extracellular-spikes-above-50uv | dandiset | reproduced (negative peaks 159 to 218 µV) |
| mea-electrodes-and-rates | dandiset | partially reproduced: 678/675 electrodes at 20 kHz as stated, but the patch is 20.41 kHz for most protocols and 125 kHz for APWaveform |
| culture-age | dandiset | blocked: metadata_insufficient |
| fig6-ais-from-dendrite | elsewhere | reproduced |
| gt-rheobase | elsewhere | reproduced (150 pA with the notebook's series, 140 pA starting lower) |
| fig3b-ap-initiates-distal-ais | elsewhere | reproduced, by a narrow margin (distal AIS leads the middle by 0.005 ms at the -20 mV crossing) |
| fig3a-largest-channel-at-ais | elsewhere | reproduced, by a small margin (nearest electrode 23.3 µm away against 26.8 µm for the next) |
| table1-feature-counts | elsewhere | reproduced (76, 87, 109, 153) |
| fig4a, gt-intracellular-scores, fig4c, both fig4b claims, fig4d, fig5 | elsewhere | blocked: too_large |
| fig78a, experimental-intracellular-scores, fig78b, fig78c, fig10 | with_inputs | blocked: too_large (the last three because they depend on fig78a) |

The fits are blocked because one evaluation of the training protocols takes 8.3 s even without the extracellular part. That puts each set of fits at 1108 CPU hours or more, about 277 hours on this runner.

**2. What was found about the dataset**
- The archive metadata link the paper to doi:10.1162/neco_a_01676. Crossref gives that DOI as a different article ("Energy Complexity of Convolutional Neural Networks").
- The patch voltages are stored in mV but labelled volts; the currents are in pA but labelled amperes.
- The patch sampling rates (20.41 kHz and 125 kHz) differ from the paper's 20 kHz and "typically 200 kHz".
- The icephys sequential-recordings table leaves out 35 and 28 recordings (the first sweep of most protocols, and every PosCheops sweep).
- There is no culture age, plating date or DIV anywhere in the files or metadata.
- The electrode x, y and z are empty; positions are only in the custom columns `rel_x` and `rel_y`.
- Cell 2 holds runs 3 to 6, renamed run1 to run4, with nothing saying why runs 1 and 2 are absent.
- 117 to 132 MEA channels per run are constant for part of the run.
- In the files the stimulus starts 50 ms earlier than the timings in the paper's code.
- The paper contradicts itself twice: the IV step range (the data have 11 steps to 60%), and 79 against 76 features (79 is the count before the code drops three sag features).
- Positive checks: no duplicate recordings, and the patch and MEA share a clock. With the spike times shifted by 100 ms, the largest channel falls from 159–189 µV to about 20 µV.
- No outcome rests on an assumption, there are no questions for the paper's authors, and I asked no reader anything.

**3. Where the protocol was unclear, and what I did**
1. **Simulator versions:** the entry's Python is fixed at 3.13, and the paper's simulator stack (BluePyOpt 1.13.88 with LFPy) won't run there. I used BluePyOpt's NEURON simulator on the repository's own model definition and recorded it as a deviation.
2. **One expected value, two cells:** `measured` takes one number, so I gave cell 1's holding potential and the smaller cell's spike amplitude, and said which in the notes.
3. **Tolerance at 0%:** a 10% relative tolerance is undefined for the IV 0% step. I used 10% of the IV increment and recorded it as a deviation.
4. **Clock check:** the protocol's examples don't fit patch-plus-MEA data. I used spike-triggered templates against spike times shifted by 100 ms.
5. **too_large or not_runnable:** the fits are blocked by cost and also by the simulator not running in the locked environment. I chose too_large as the main reason and put the other in the notes.
6. **Outside code on disk:** the rule against writing to disk covers dataset files only. I fetch the repository tarball and compile its mechanisms in a temporary directory.
7. **Result cell for blocked claims:** the protocol doesn't say how to present a shared cost estimate. I gave it its own section, tagged `fits-cost`, with a "Result:" conclusion.

**4. Runtime and failures**
The run took about 56 minutes, from 23:05 to 00:01 UTC; the notebook takes about 6.5 minutes. Nothing failed in the final run. During preparation, getting the simulator to work took several tries, ending with NEURON 9 and its NEURON-only simulator.

The repository root has untracked entries I didn't create (`.bashrc`, `scripts` and others, which are sandbox device nodes); I left them alone. Nothing is committed.
