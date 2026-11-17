No outcome changed. Every outcome the verifier gave is kept except one: figs4-intrinsic-properties stays blocked, but its reason changes from `other` to `methods_underspecified`, as the verifier suggested. The entry re-ran cleanly with `tools/entry.py all`: check 0 errors, the Neuropixels notebook passed in 142 s and the model notebook in 949 s. The printed numbers match the conclusions and the attempt record.

**What I changed, point by point**
- **B1 (partial outcomes come from the paper's own rate code):** this is a point about the claims file, so I added it as a question for a reader in the new `questions/burman-2023.yaml`. The three claims stay partially reproduced. I also settled the verifier's first open check: the paper's analysis gist now runs unmodified on the loaded data. It agrees with `npx` for all 865 units (0 values differ), and with the Methods' exclusion applied to its rate it gives the paper's numbers exactly: 662 kept, 203 excluded, synchrony 0.3253 and 0.3928, entropy 1.3474 and 1.1106.
- **B2 (model tolerances too tight for different seeds):** added as a second question for a reader. The model notebook now prints the run-to-run standard error of the 20-run mean: 0.0013 for synchrony and 0.0023 for entropy in the hyperpolarizing condition. The misses are 1.6 and 1.9 of these. Both claims stay partially reproduced.
- **B3 (figs4):** the notebook header and the notes now say the NEURON model and its parameters are public. They also say why I did not simulate it: what the result would be judged against is only in the Figure S4 legend, which wasn't in the text read, and the claims file gives no criterion. I added a `methods_unavailable` finding asking the paper's authors.
- **B4 (p-values printing as 0):** p is now formatted before rounding. The rate test shows p = 5.75e-32.
- **B5 (clock check on only 2 of 17 files):** it now covers all 17 files, with a Wilcoxon test for each file and condition. 33 of 34 pairs pass at p < 0.001. The exception is the awake trials of sub-569069_ses-20210312 (p = 0.59), where the units barely respond while awake; that file's isoflurane trials pass. This is now in the notes.
- **Simulation gist:** the gist, run unmodified on a small network with the same seed, gives the same 19,093 spikes as `network.py`. It also gives the same rate, entropy and synchrony for all 800 neurons.
- **Brian 2 learning rate:** each run now prints the value used in the compiled synapse code. In all 20 runs it is 0.1 during balancing and 0 during the test.

**Corrected**
- The decoding claim's notes said t = 16.92, p = 6.52e-13, which did not match the notebook's output. They now give the printed t = 16.42, p = 1.11e-12.
- The model notebook's runtime in `entry.yaml` and the README is updated to about 20 minutes.

The round is recorded under `verifications` for all 35 claims, with the verifier's reasons and my response to each.

**Not done**
- I did not simulate the Figure S4 model, for the reason above.
- I did not change the claims file, which the instructions forbid; B1 and B2 wait for a reader's answer.
- Nothing is committed.
