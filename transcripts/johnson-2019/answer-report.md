I made no changes, because `questions/crcns-fcx-3.yaml` does not exist. It is not in the working tree and has no history on any branch.

I checked the likely places for questions sent somewhere else instead:

- **The attempt record** (`attempts/crcns-fcx-3-johnson-2019-01.yaml`, lines 361 to 372) has two entries marked "Question for the paper's authors". One asks which electrodes counted as neighbours in the ERP cluster tests. The other asks how the PSI cross-spectra were computed and which channel came first. Both are filed as `methods_unavailable` deviations. They ask about method details the paper doesn't fix, and neither says the claims file misreads the paper. Under step 6 they are not a reader's to settle, so I left them alone.
- **The rest of the repository** turned up no question addressed to a reader for this dataset.

The claims file and questions file are unchanged, and I committed nothing. If questions for this attempt were supposed to be written to `questions/crcns-fcx-3.yaml`, the step that writes them didn't run or didn't save its output. Once that file exists, this task can be rerun.
