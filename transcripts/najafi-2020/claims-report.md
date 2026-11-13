I've written the claims file, `claims/000016/10.1016-j.neuron.2019.09.045.yaml`. The quote checker reports 38 claims, 38 quotes, 10 statistical values and 0 problems. Nothing is committed.

**Text read**
- **Paper:** the accepted author manuscript in PubMed Central (PMC6952547, NIHMS1545193). It has the full Results, the figure legends and the STAR Methods.
- **Supplement:** the one file, NIHMS1545193-supplement-1.pdf, with the legends of Figures S1 to S15.
- **Not used:** the bioRxiv preprint, which is an earlier version. The main figures were read only through their legends, because there is no PDF of the main paper.
- **Dataset:** only its title and description on DANDI were read. They say 4 mice with one NWB file per session.
- **Code:** github.com/farznaj/imaging_decisionMaking_exc_inh at commit b7352ac. The batch scripts that set the parameters of the published runs are not in the repository, and some settings differ between its scripts.

**Contents**
- 38 claims, every one with a quote and a criterion.
- 7 claims carry 10 statistics entries; 13 claims carry expected values.
- 5 claims are model simulations or need material other than the activity recordings (the raw movies for S14, the stained sections for S15).

**Open details, with the readings named for each**
- **Shuffle significance test:** the Methods say only that the probability of the real value under the shuffles must be below 0.05. The code fits a normal distribution, which comes to about |z| ≥ 2.45; I followed it. An empirical p from the 50 shuffles is a variant.
- **Stability (Fig 4):** the Methods say "2 standard deviations" but the code uses 2 standard errors. The Methods are the main reading and the code a variant. Whether stable bins must be contiguous, and a significance level of 0.001 (code) against 0.05 (Methods), are also named.
- **Choice-signal onset (Fig 8C):** the Methods give p < 0.05 and the code uses 0.001, so the code's value is a variant. The code also has an apparent bug at line 600, where it tests excitatory data against the inhibitory shuffle; the criterion uses the excitatory shuffle, as the Methods describe.
- **Trials for the learning decoders:** the code uses all outcomes. Readings are (a) balanced only by choice and (b) equal correct and incorrect trials within each choice.
- **Early and late days:** (a) every day below the 20th or above the 80th performance percentile (code) or (b) only the runs of days at the start or end of training (Methods' wording).
- **Mouse labels in the Fig 8 legend:** "mouse 2" and "mouse 3" can mean the paper's mice 2 and 4 or mice 2 and 3. By Figure S1C the learning mice are 1, 2 and 4.
- **Test unit:** for the inferred-spiking test, the correlation tests and Fig 7, whether the test runs across sessions or on neurons pooled over sessions. For Fig 7, also a one-sample test of the changes against an unpaired comparison.
- **Windows:**
  - Fig S3C: the code's −194 to +291 ms or the stated −200 to +300 ms.
  - "Just after the choice": the first bin or within 300 ms.
  - Previous-choice and stimulus-category decoding: which bin and alignment.
  - Outcome decoding: the end of the "after reward" window.
- **Other:**
  - Fig S5: denoised traces or ΔF/F.
  - The fraction of inhibitory neurons and trials per session: which denominator.
  - The ×3 increase in Fig 8G: per mouse or pooled.
  - S2 and S7C have no test, so the Methods' t-test is used, with and without correction over windows or two summaries.
  - The model's range of connection-strength ratios is not in the text, and the Fig S8 formula is garbled.

**Missing from the paper that some claims need**
- **Test thresholds:** no test or threshold is given for "similar", "matched" or "peaked", so the Methods' generic two-tailed t-test is used.
- **Fig 3F:** the star marks a significant difference in mice the text does not name.
- **Example sessions and mice:** those in Figs 2A, 3, 6B and 8 are not identified.
- **Mouse identifiers:** none link the paper's mouse 1 to 4 to the dataset. Mice are matched by session counts (45, 48, 7, 35).
- **Figure 1B:** it uses 10 mice, and the dataset holds the 4 imaged mice.
- **S14 and S15:** they need the raw movies and the histology sections.
