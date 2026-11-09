I did steps 1 to 5 of the Author section and ran the handover (step 6); `python tools/entry.py all` passes with 0 errors. Of the 22 claims, 1 is reproduced, 1 partially reproduced, 7 not reproduced and 13 blocked. The entry is `entries/000019-bouchard-2013/`, with `attempts/000019-bouchard-2013-01.yaml` and `questions/000019.yaml`; nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| data-composition | partially reproduced |
| active-electrodes | not reproduced (about 24 per subject, against 27 to 33) |
| fig1c-e-articulator-electrodes | blocked: metadata_insufficient (no subject has all six named electrodes on vSMC) |
| fig1f-h-phonetic-contrasts | not reproduced (largest /ju/ z is 1.19, below the threshold of 2) |
| fig2a, fig2b, suppfig3b, suppfig3d, suppfig3f, suppfig5, suppfig7 (spatial) | blocked: metadata_insufficient |
| suppfig6-mixed-tuning | reproduced |
| fig3d-timing-sequence | not reproduced (tongue correlations begin after the C-V transition) |
| pca-nine-components | blocked: methods_underspecified |
| fig4a-consonant-clusters | not reproduced |
| suppfig11-co-clustering | blocked: methods_underspecified |
| fig4c-d-hierarchy | blocked: methods_underspecified |
| fig4ef-feature-correlations | blocked: methods_underspecified |
| fig5c-separability-timing | not reproduced |
| fig5d-separability-coupling | blocked: methods_underspecified (the claims file's own readings disagree) |
| suppfig13-consonant-vowel-distance | blocked: methods_underspecified |
| suppfig9-pc-articulator-weights | not reproduced |

**2. The dataset and the questions asked**

- **Version:** I pinned 0.220126.2148, the only published version; the paper cites none.
- **What it holds:** raw 256-channel ECoG at 3051.76 Hz, trial tables with C-V transition times, bad-channel flags, anatomical labels and rest periods. There is no audio and no high gamma, so high gamma is computed from about 42 GB of raw data, streamed into memory.
- **Subjects:** four (EC2, EC9, GP31, GP33). I assumed GP31 and GP33 are the paper's EC31 and EC33; nothing in the files links them. EC9 is not in the paper and is left out.
- **Positions:** no electrode position relative to the central sulcus or Sylvian fissure. EC2 and GP31 have x, y, z coordinates with no unit or frame; GP33 has none. This blocks the seven spatial claims.
- **Syllable counts:** 2 to 107 renditions per syllable against the paper's 15 to 100, and 169 syllables against 168.
- **Units:** the conversion factor (0.001) looks wrong; the stored values look like volts already.
- **Labels and ids:** two syllable labels are misspelt, and electrode ids start at 0 in some subjects and at 1 in others.
- **Duplicates:** none found.

I asked five questions:
- How the state-space input is z-scored: over each electrode's whole series, or at each time across syllables.
- Whether syllables with fewer than 15 renditions are kept. Together with the z-scoring question, this decides most of the methods_underspecified outcomes.
- Whether the hand-marked syllable start can stand in for the acoustic onset, since the audio is missing.
- Whether the dataset's rest period counts as a baseline.
- Whether the paper gives any way to get the spatial coordinates it uses.

**3. Where the protocol was unclear, wrong or missing something**

1. A claim depending on a blocked claim is blocked, but fig1f-h, suppfig6 and suppfig9 only use fig2a's weights, which need no positions. I tested them and recorded why.
2. Readings I add through a question multiply every other reading. I ran all of them, so several claims are blocked only because those readings disagree.
3. Rest period as baseline: it comes from the dataset, not the paper's text, so I showed it as a variant, not a reading.
4. The protocol's notebook header template uses bold labels, which conflicts with your no-bold rule. I removed the bold.
5. The archives doc says to stream with remfile, which reads these files chunk by chunk too slowly. I fetched each whole file into memory with parallel range requests; nothing was written to disk.
6. The articulator and phonetic feature matrices exist only as figures in the supplement. I transcribed them from the PDF into the helper module and listed them under `inputs`.
7. The protocol has no format for a claims file that leaves "pre-epoch level" undefined (fig5c). I read it as the value at -500 ms and recorded that as a deviation.

**4. Runtime and failures**

- The notebook runs in about 14.5 minutes, 11 of them streaming and computing high gamma. That is over the 10-minute aim and under the 30-minute limit.
- I could not remove an empty `.claude/.cc-writes` directory the harness created inside the entry: the permission was denied. Git does not track empty directories, so it will not be committed.
- The `.bashrc`-style entries in `git status` are sandbox device mounts, not files.
