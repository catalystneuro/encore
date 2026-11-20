I wrote `claims/mohebi-2019.yaml` and the quote checker passes it: 37 claims, 36 quotes, 7 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC6555489). It has the main text, the Methods, the legends of Extended Data Figs. 1 to 8, and the Supplementary Information PDF. That PDF is only the Supplementary Figure, one page per dopamine cell, with no text beyond its legend.

**What is missing:**
- **Main figure legends:** the legends of Figures 1 to 5 are not in the text, and there is no PDF of the article. They would give the tests, sample sizes and windows for Fig. 2f,h,i, Fig. 3c,d,f–h, Fig. 4c,e,f and Fig. 5a–d. I went ahead because the Methods and the Extended Data legends are there, as the repo did for goncalves-2013. Every claim that rests on those panels names the missing detail as open.
- **Code:** none was read. The paper says its MATLAB code is "available upon request" and links no repository.
- **Model:** the semi-Markov model is "exactly as previously described" in the paper's ref. 5 (Hamid et al. 2016), which was not supplied.

**Counts:** 37 claims, 36 with quotes. One is marked `inferred`: the Pavlovian cue responses, which are read from the Extended Data Fig. 5 legend. Statistics are recorded for 5 claims (7 entries), expected values for 15, and every claim has a criterion. All claims use the paper's own recordings. Many of them need microdialysis, dLight, voltammetry, histology or non-dopamine cells, which the data set description does not mention.

**Details left open, with the readings named:**
- **Reward rate:** the increment size and time step cannot change the outcome, so standard choices are used. It is read at the aligned event.
- **Time to cue response:** the multiple-comparison correction is read as Bonferroni over bins. The post-cue window is 0.5 s or 1 s.
- **Tagging test:** the test's own window and bin are read as its published defaults (10 ms, 1 ms).
- **Firing rates:** the cell set is 27 or 29. The session-wide rate is from the bandit task or the whole recording.
- **Waveform width:** taken from the largest-amplitude wire.
- **Microdialysis Bonferroni divisor:** 21×7×9 (Methods) or 21×7×12 (Extended Data Fig. 2 legend). Sessions are pooled or fitted one by one.
- **Number of past trials** in the Extended Data Fig. 1b latency regression: 5 or 10.
- **Fig. 2 tonic firing test:** rank-sum on 1-min bins, or on block means, at p < 0.05.
- **Burst rate and inactive-time tests:** signed-rank or paired t-test.
- **"Long" inter-spike interval:** 0.5, 1 or 2 s. "Very low" is judged as a median below 5% of time.
- **Ramp angle test** (Fig. 4f): signed-rank or sign test. The angle's axis scaling does not change its sign.
- **"Better aligned"** (Fig. 4e): peak height, or trial-to-trial timing spread.
- **Early-trial window** (Fig. 5a): after Light-On or before Center-In. The test is a per-cell correlation or a Friedman test.
- **Valley window** after unrewarded Side-In: the Methods say 1–3 s after it, the Extended Data Fig. 8 legend says 0–2 s.
- **The 2/29 pause count:** significant before or after correction.
- **Actor-critic and Q-learning models:** how alpha is fitted, and the starting values (0.5).
- **dLight windows and tests** for Fig. 3c,d, Fig. 4c and Fig. 5c,d.
- **Standard choices:** "great majority" is judged as at least 75% of cells, with p < 0.05 where the paper gives no threshold.
