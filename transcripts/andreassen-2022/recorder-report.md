I wrote two new files, `docs/pilot-notes/andreassen-2022-01.md` and `summaries/andreassen-2022-01.md`, and changed no other file. The summary is 119 words. This Figshare item has no entry in `targets/dandisets.json`, which lists only DANDI datasets, so there is no `catalystneuro` field and the dataset paragraph does not open with the conversion sentence. The dotfiles, `.idea`, `.vscode`, `.mcp.json` and `scripts/` at the repository root are untracked and were not created by me. The author's reports already warned that a workflow committing everything would pick them up.

# andreassen-2022, Andreassen et al. 2022

Seventeen claims reproduced, two partially, none not reproduced and nine
blocked, all nine for missing data. One outcome,
`figs3d-medulla-drops-before-depolarization`, rests on an assumption. The first
verification round agreed with all 28 outcomes, and so did the second, which
also corrected its own round-1 reason for `fig5a-ctmax-oxygen` (the
overall-quartile variant does not pass); nothing was proposed after it, so there
was no third round. It pins version 4 of the Figshare item, the latest; the
paper cites the item without a version, and version 3 has the same files with
the same MD5s. The paper, Andreassen, Hall, Khatibzadeh, Jutfelt and Kermen,
"Brain dysfunction during warming is linked to oxygen limitation in larval
zebrafish" (PNAS 119, e2207052119), warms Tg(elavl3:GCaMP6s) larvae at 0.3
°C/min in five experiments and reports that CTmax is similar in larvae and
adults, that medulla activity rises with warming and then falls before a
brain-wide depolarization that follows CTmax, that heart rate falls above 34
°C, and that hypoxia lowers and hyperoxia raises CTmax, the depolarization
onset and the resilience of medulla activity and optic tectum light responses.
The item holds ten CSV tables of per-fish values, a Readme and the paper's R
script, which settled the outlier rule, the model formulas, the temperature
binning and the centering of the light model. The CTmax, depolarization, heart
rate, oxygen and light-response model claims reproduce, with the estimates the
claims file quotes from Tables S1 and S3 to S10; the age comparison of
`fig1c-ctmax-similar-across-ages` and the oxygen effect of `fig5a-ctmax-oxygen`
hold only after the paper's outlier removal (with all 16 adults the 5 dpf
against adult contrast has p = 0.038, and with all 76 fish neither oxygen
contrast is significant). `fig2f-medulla-heat-rise-then-fall` reproduces on the
group mean curve (3.59 peaks/min) and not on per-fish maxima (4.30).
`fig5d-medulla-hypoxia` is partial because the Q10 from 28 to 34 °C is 0.883
against 0.8 ± 0.08, and no reading tried gives 0.8; `fig6c-light-responsiveness-by-oxygen`
is partial because, by the claims file's decline rule, hyperoxia keeps its level
only to 29 °C, not 36 °C. The figs3d drop is below half the maximum over the
last 2 min in every treatment but not over the last 5 min, and it fails if the
onset bin is rescaled as a rate over the whole bin, so it is called fragile.
Blocked are the spiral swimming and loss of response of Fig. S1, the
experiment-2 medulla activity by temperature, onset temperature, spread and
recovery, the experiment-4 medulla counts, the light response amplitudes and
the depolarization magnitude. Mixed models were reimplemented in Python with
Satterthwaite degrees of freedom, as there is no R in the locked environment,
where the script uses Kenward-Roger; no p-value is near a threshold. The author
asked a reader no questions. Round 1 found that the `Response` column of
LOEData.csv was never explained, that the spiral-swimming test could have been
run on the caption's counts, that the figs3d result was fragile, that the 27
°C bin and the R script's Q10 code were not shown, and that the Readme was never
printed; in reply the column was shown to record loss of equilibrium, the test
was run as a check of the paper's arithmetic, variants and a question on the
onset bin were added, the R script was shown to compute no Q10, and printing
the Readme found the Recovery unit error. Round 2 found sentences the outputs
did not support, on Fish33, the ramp rate, the partial onset bin in hyperoxia
and the summary's claim that every model reproduces Tables S1 and S3 to S10,
which were corrected. The author's run took about 25 minutes (08:17 to 08:41
UTC), and the notebook ran in about 24 s, 23 s after round 1 and 27 s at the
end; two patsy formula errors, a pandas index error and a check run from the
wrong Python environment were fixed before the final run.

The item holds only part of the paper's data (major): the experiment-2
temperatures and onset temperatures, the experiment-4 medulla counts, the
spiral-swimming and loss-of-response scores of Fig. S1B, C and E, the
amplitudes of the light responses, the medulla peak amplitudes and any imaging
time series are not deposited, and nine of the 28 claims cannot be tested. The
R script types the spiral-swimming counts into a matrix, so they are not
deposited data. The Readme gives Recovery in minutes, but its 39 values run
from 60 to 464 and are seconds. It says FishID corresponds across the
depolarization, medulla and light tables, but LightResponse.csv names three
fish Fish3, Fish4 and Fish5 where the depolarization table has Fish03, Fish04
and Fish05, and Fish33 has medulla and light values but no depolarization row.
In 30 of 32 embedded fish of experiment 5 the medulla series ends in the bin
that holds the onset, but in Fish03 it ends one bin earlier and in Fish35 two;
the light recordings of Fish27 and Fish29 end about 10 °C below their onsets;
and CTmaxData_Total.csv has 90 rows, 2 without a treatment or temperature and
12 more without a temperature, with nothing to explain any of these. Two
questions are put to the paper's authors: over what window the drop of Fig. S3D
was judged and how the frequency of the bin that holds the onset was
normalised, and how the Q10 values of Fig. 5D were computed.

The author's points on the protocol: its clock check assumes time streams and
trial tables, and the nearest check on derived tables was whether each fish's
last medulla bin falls in its onset bin; the claims file names Satterthwaite
where the paper's script uses Kenward-Roger, which was recorded as a deviation;
it says nothing about papers whose code is in R, and the models were
reimplemented in Python; it does not say whether a reading the paper's code
rules out still counts; it only partly covers outcomes that rest on thresholds
the reader set; it has no rule for numbers typed into the paper's own code,
which were blocked as missing data; and untracked files the author did not
create were left in the repository root.

---

Most of the paper's main findings hold up in the per-fish tables: larvae and adults reach a similar thermal limit (CTmax), the brain-wide depolarization follows CTmax, medulla activity rises with warming then falls before it, heart rate falls late in warming, and hypoxia lowers and hyperoxia raises both CTmax and the depolarization temperature. The age comparison and the oxygen effect on CTmax need the paper's outlier removal. Two oxygen results hold in part: hypoxic medulla activity declines more slowly early on than reported, and hyperoxia keeps light responsiveness to 29 °C, not 36 °C. The depolarization's onset, spread and recovery in the first imaging experiment and light response amplitudes could not be tested, as those data are not deposited.
