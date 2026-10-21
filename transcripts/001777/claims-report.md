I haven't written the claims file. The response that would have created `claims/001777/10.1126-sciadv.adq8840.yaml` was stopped by a safety classifier, so nothing exists under `claims/001777/` and the quote checker was never run. I'm not retrying that write. Someone needs to restart the run, or tell me how to go on.

**What I read**
- **Text:** the version of record (Science Advances 12, eadq8840, 9 September 2026), from the hand-supplied PDF text, plus its supplement (Figs. S1 to S9). I opened PDF pages 3, 4, 6 and 8 to get the direction of effects in Fig. 2C, 3, 5F and 7, which the legends don't say in words.
- **Code:** the Zenodo record linked from the paper (concept doi:10.5281/zenodo.10855006, record 17297995, `Code Sample.nb`, md5 dd662358eca78e5ebd6a69b1e270c228). It is a Mathematica notebook with placeholders where the values should be:
  - A cell's rate is the spike count per episode divided by episode length, then the median over a "stable" run of episodes picked by eye.
  - A PSTH is the spike count per bin divided by bin width times the number of episodes.
  - "Glitched" episodes are dropped by hand, and there are no statistics in the code.
- **Dataset:** from its archive description only, it holds slice electrophysiology as NWB voltage clamp recordings (90 subjects, 412 files).

**Planned claims:** about 36, all but one quoted from the text or a legend (Fig. 5F's direction would have been read from the figure and marked `inferred`), most with a paired t, Welch, Wilcoxon or Mann-Whitney result. They cover Figs. 1 to 7 and S1 to S4 and S6 to S9, and include about eight claims of absence. The number of statistics and criteria was not fixed before the stop.

**Details the paper leaves open, with the readings I had named**
- **Spike detection:** neither the Methods nor the code give a threshold. Readings were 5 and 8 times a noise level estimated from the median absolute deviation; this is a standard choice, flagged as one.
- **"Stable" episodes:** either all episodes of a condition, or the last half of them (Fig. 7G shows drug effects levelling off about 6 minutes after application).
- **Percent changes:** the mean of each cell's percent change, the percent change of the group mean, or the median of each cell's percent change.
- **Measurement windows:** the window for evoked IPSC amplitude, how the paired-pulse ratio is computed, and the "basal" window in Fig. 2C are not given.
- **Text and legends disagree:**
  - Fig. 3B: n = 10 in the text, 45 in the legend.
  - Fig. 3D: P = 0.13 against 0.06.
  - Fig. 4A: P = 0.02 against < 0.01.
  - Fig. 4B: P = 0.19 against 0.16.
  - Recording temperature: 32 to 33°C in the Methods, 30°C in the Fig. S4E legend.

**Missing from the paper**
- **No electrophysiology methods section:** recording solutions, how cell-attached recordings were made, drug wash-in times, spike detection and analysis windows are all absent. I judged that the code and the readings above cover the rate measure, but a checker may count this as a missing Methods.
- **Tests not named:** for Fig. 6C and S3.
- **ALDH1A1 deletion in Fig. S6:** how it was done isn't described, and the figure reports no test.
- **Dopabase query (Fig. 6D):** no method is given for it.
