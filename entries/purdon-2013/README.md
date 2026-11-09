# Purdon et al. (2013) from dandiset 001285

Checks [DANDI:001285](https://dandiarchive.org/dandiset/001285/0.250110.2125) against the findings of
[Purdon et al. (2013)](https://doi.org/10.1073/pnas.1221180110), on behaviour and EEG during gradual
induction of and emergence from propofol in 10 volunteers.

| Claim | Outcome |
|---|---|
| All 22 claims (behaviour, Figure 1; EEG, Figures 2 to 5, S2 and S3) | Blocked: data missing |
| Of these, the 16 EEG claims, which need channel identities | Second reason: metadata insufficient |

The dandiset holds the 64-channel EEG of one of the ten subjects. It holds no behavioural responses,
from which the paper defines loss and recovery of consciousness and aligns every EEG analysis, no
infusion levels or time markers, and no channel names or positions. The notebook lists what the file
holds and checks its values against the description. The attempt record, with the reasons and the
findings about the dataset, is
[`attempts/purdon-2013-01.yaml`](../../attempts/purdon-2013-01.yaml).

- `reproduce_purdon_2013.ipynb`: the data check. It takes one to two minutes, most of it streaming the
  file.
- `propofol_eeg.py`: streaming the file and the per-channel summaries, spectra and band-power time
  course used in the check.
