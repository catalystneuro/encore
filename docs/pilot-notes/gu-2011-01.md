# crcns-stc-1, Gu et al. 2011

Ten claims reproduced (seven on an assumption), five partially (four on an
assumption), one not reproduced and 18 blocked, 17 for missing data and one for
insufficient metadata; the link claim the author added, `training-group-link`,
reproduced, is counted apart. The first verification round agreed with 33 of
the 35 outcomes as they stood and the second with all 35; nothing was proposed
after the second, so there was no third round. CRCNS does not version data
sets, so the version is recorded as unversioned with the data set's DOI
(10.6080/K07P8WKF); the author pinned `stc-1/live/`, the bucket's only copy of
the data, and the notebook checks the files against the data set's MD5 sums.
The paper, Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis and Angelaki,
"Perceptual Learning Reduces Interneuronal Correlations in Macaque Visual
Cortex" in Neuron (71:750-761), records pairs of MSTd single units in three
naive monkeys and five monkeys trained in a vestibular and visual heading
discrimination task, while they fixate and experience headings in two
interleaved conditions, and finds lower noise correlations after training, with
a regression of noise on signal correlation whose intercept falls while its
slope is unchanged, which simulations of population thresholds then use; the
data set holds the noise and signal correlations per condition and the
preferred headings of the 127 pairs under 1 mm, and the tuning curves, neurometric thresholds and choice
probabilities of 129 units of two trained monkeys from Gu et al. (2008). The
claims were written from the PyMuPDF text of the version of record and the
legends of its Supplemental Information, without rendering the PDF, and the
paper links no code; the claims check added readings for the preferred heading
of `fig4dh-lateral-more-sensitive`, widened the readings of
`fig8cd-noise-not-preference` to fit the legend's 328 points, and revised
others. The noise correlation, regression and simulation claims, the Figure 1
claims, the choice probability claim and the preference group effect of Figure
4 could be tested, the last two on the 129 units; the time courses, Fano
factors, distances, electrode types, training histories, the naive and trained
single-unit comparisons, the pair tuning curves, the task correlations and the
eye records could not. Most assumed outcomes rest on reading the pooled noise
correlation as the mean of the two per-condition values (trained 0.0241 and
naive 0.1190, p = 0.0056, against the paper's 0.023, 0.116 and p = 0.006), and
those of Figures 6 and 7 on the claims file's tuning amplitude of 30 and
baseline of 10 spikes/s over 1 s, which the paper does not give. Reproduced
are, among others, `fig2b-trained-lower-noise-correlation`, `fig1-example-pair`
(pair m2c338r1), `fig5-noise-signal-positive`, `fig5-slope-unchanged`
(interaction p = 0.830 and 0.962) and `fig6a-population-thresholds` (a ratio of
5.41, 4.32 to 5.90 over the amplitude and baseline variants). Partial are
`fig1f-modality-correlated` (Spearman R = 0.449 on 127 pairs, outside 0.342 to
0.418), `fig5-intercept-lower-trained` (the training effect holds, p = 0.0184
and 0.0074, but the intercept intervals overlap under every construction),
`fig5-regression-coefficients` (trained intercept 0.0034, outside 0.005 +-
0.0005, a tolerance the claims check noted no fit could meet),
`fig7a-pair-sign-of-effect` (92 of 93 pairs with negative rsignal) and
`fig7c-narrow-preferences` (best improvement 4.83%, below 8 +- 0.8%). Not
reproduced is `fig8ab-choice-probability-lateral`: on 258 values from 129
units, fore-aft units do not have smaller choice probabilities (p = 0.136 and
0.796 under the two preference readings). The author's first run had 9
reproduced, 5 partially, 2 not reproduced and 19 blocked, with fig7c not
reproduced and fig4dh blocked. The author asked no questions of a reader, so
the answer and author-answers runs changed nothing. Round 1 disagreed on fig7c
(partially reproduced) and fig4dh (testable within the trained units), and
found that the unweighted vector sum used for fig8ab, biased by the uneven
headings, gave the only significant result, in the opposite direction (p =
0.0006), and that the fig8cd variant over 127 pairs is nearer the legend's point
count and fails with vestibular preferences (p = 0.0009); in reply fig7c became
partially reproduced, fig4dh was tested and reproduced under one of its 8
readings (p = 1.9e-07), the vector sum was weighted by heading spacing, the
fig8cd conflict was stated with the outcome kept on the trained pairs, and
bootstrap intercept intervals and the fig7a crossover (rsignal = -0.0216) were
added. Round 2 agreed with all 35 outcomes, asked that the fig4dh record state
the missing tuning selection of the Figure 4 legend, the preference by
condition interaction (p = 0.026) and the double counting of units, and found
text the outputs did not support, among them a match "to the third decimal" for
0.0241 and 0.1190 and file_ids and shared cell ids that no cell printed; in
reply proxy selections (p = 1.2e-07 and 9.6e-08) and a mixed model (p =
2.7e-07) were added, the outputs were printed, the text was corrected, and two
questions went to a reader in `questions/crcns-stc-1.yaml` (the tuning
selection of fig4dh and raw choice probabilities against their distance from
0.5 for fig8ab), a file written after the answer run, so they are unanswered.
The author's run went from 16:53 to 17:13 UTC; the notebook ran in 99 s at
first, 93 s after the author-answers run and about 49 and 53 s after the two
revisions, and nothing failed. The untracked files in the repository root,
sandbox device mounts, were left alone.

The data set holds derived values only: for the paper's pairs there are no
spike times or trial responses, no interneuronal distances, none of the 52
pairs over 1 mm, no discrimination-task correlations and no eye records, the
single-electrode database of Figures 4, S4 and 8A is represented only by 129
units of two trained monkeys, and the training histories of Figure 2A by one
threshold for each of two monkeys, so 18 of the 35 claims cannot be tested. No
pair or monkey carries a naive or trained label, which every comparison in the
paper needs; the groups can be recovered only because the paper's per-animal
pair counts in the Figure S2B legend are all distinct and match the counts per
monkey in the file_ids, giving 89 trained and 38 naive pairs and 146 and 64
units. No pair carries an electrode or distance label, and ten pairs of monkey
17, in six recordings, have file_ids ending in "s" without explanation, so the
single-electrode and multi-electrode pairs cannot be told apart. The data
descriptor does not say how heading_pref was computed, how cp is signed, or the
units of resp_global (demo.m labels them spikes/s). The descriptor lists
monkeys 1, 2, 3, 5, 17, 18 and 19 for the 127 MSTd pairs, while the file_ids
name an eighth, monkey 24, with two pairs, the trained animal with two pairs of
Figure S2B. Recording m19c21r1 holds six pairs from four units, where the paper
states a maximum of five pairs in an experiment. Questions are put to the
paper's authors: whether the pooled rnoise of Figures 2B and 5 is the
correlation of z-scores pooled over both conditions and whether the stored
values include the renormalization in blocks of 20 trials; what tuning
amplitude, baseline and counting window the simulations of Figures 6 and 7 used
and whether the trace term of equation 3 was included (without it the ratio is
9.2 and the best improvement up to 11.8%); how the intercept intervals of
Figure 5D were computed; and, for Figures 8A and 8B, how each unit's preferred
heading was computed, which units entered the 311 values and how CP was signed.

The author's points on the protocol: link claims are framed around outside
data while here the labels came from the paper itself, so its DOI was listed
under `inputs` and the link marked `with_labels`; adding the link claim meant
adding `depends_on` to 7 claims in a file the author is otherwise told not to
change; the rule that every data stream share the trial clock does not apply to
a data set of summary values only; there is no category for a claim testable
only on a subset that may not be the paper's sample (fig8ab), so it was tested
with the subset named in the deviations; the criteria give no outcome for all
but one (fig7a) or for a mixed result without a partial rule, so partially
reproduced was chosen with the exact counts; fig8cd's preferred reading needs
pairs not in the data set, so the closest reading the data allow was judged;
and `docs/archives.md` describes CRCNS zips where these files are plain `.mat`,
which were streamed into memory with fsspec.
