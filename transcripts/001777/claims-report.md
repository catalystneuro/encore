I didn't write the claims file. A safety classifier stopped my response while I was writing `claims/001777/10.1126-sciadv.adq8840.yaml`, so nothing was saved and `claims/001777/` doesn't exist. No quotes were checked and nothing is committed.

What I read before the stop:

- **Text**: the version of record (Science Advances, 9 September 2026, CC BY) in `paper/10.1126-sciadv.adq8840.txt`, with the full main text, Methods and figure legends. The supplement (Figs. S1 to S9) is present too. I opened PDF pages 3, 4, 6 and 8 for Fig. 2B's time axis (the train runs from 2 to 4 s of a 6-s sweep), Fig. 3B's cell count (about 45 cells) and the direction of Fig. 5F (the inhibitor-treated group fires faster). Nothing the claims need is missing from the paper.
- **Code**: `doi:10.5281/zenodo.10855006`, which resolves to version `doi:10.5281/zenodo.17297995` and holds one Mathematica notebook, "Code Sample.nb". It computes the spike rate per episode as spike count divided by episode length, takes the median over a stable window chosen by eye, and builds the PSTH. The window limits, bin width, trigger time and dropped episodes are placeholders in the code. Spike detection was done in Clampfit, with no settings given.
- **Outside data**: per-figure raw data and analyses are on Zenodo (`doi:10.5281/zenodo.15881780`). There are no folders for Figs. S1, S5, S6 or S8. Fig. 6D draws on Dopabase and GEO GSE271781. Fig. S5 comes from Gonzalez-Rodriguez et al. 2021.
- **Not read**: the protocols on protocols.io, because their API needs a login.

**Details the paper leaves open, for whoever writes the file:**

- **Fig. 3B**: the text gives n = 10 and the legend n = 45.
- **Fig. 3D**: the text gives P = 0.13 and the legend P = 0.06.
- **Fig. 4A and 4B**: the text gives P = 0.02 and P = 0.19; the legends give P < 0.01 and P = 0.16.
- **Unnamed tests**: Figs. 6C, 7D, 7E, 7H, S3 and S4D don't name their test.
- **Stable window**: the code chooses it by eye. Possible readings are all episodes, or the episodes after wash-in.
- **Percent changes**: these could be the mean of per-cell changes, the change in group means, or the median of per-cell changes (the Discussion calls them "modal").
- **Fig. 2C**: the baseline and stimulation windows for "percent inhibition" are not defined.
- **IPSC amplitude and paired-pulse ratio**: how they were measured is not given.
- **Sidedness of tests**: not stated.
- **Fig. S6**: no test is reported, and the "deletion" groups are not described in the Methods.

Re-running the reader would produce the file.
