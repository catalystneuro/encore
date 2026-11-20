I've revised the attempt for every point in the round-1 report and re-run the full entry with `python tools/entry.py all entries/jones-2021`. All three notebooks pass (rest 41.5 min, run 15.8 min, CSD 7.3 min), the key numbers came out the same in a second full run, and `entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes** (now 5 reproduced, 3 partially reproduced, 31 not reproduced, 3 blocked for missing data):
- **fig2ef-csd-sr**: blocked → not_reproduced. It is tested in a new notebook, `csd_cohort1.ipynb`, on all 62 cohort 1 sessions. PV-Cre source and sink increase; the SST-Cre increases are not significant (p = 0.0078 and 0.015), so two of four effects hold where the partial rule needs three.
- **fig4d-swr-sg-power-pv**: blocked → not_reproduced, resting on assumptions about tapers and z-scoring. The PV-Cre rise holds in CA1 and CA3, but the CA1 genotype test fails (p = 0.11). Empty vector mice also rise in CA1, and the code's own-session z-scoring shows no PV-Cre effect.
- **fig4e-swr-sg-coherence-pv** and **figs2cd-sg-predicts-sw-frequency**: blocked → not_reproduced.
- **figs5-theta-coherence-frequency**: not_reproduced → reproduced, resting on an assumption.
- **tables4-genotype-baseline**: partially_reproduced → reproduced, resting on an assumption.
  - Both changes come from fixing the `freq_sites` bug and pooling frequency peaks over all of a region's sites. Method M averages a region over its sites, and Table S3's counts point to pooling.
  - With one site per region (shown as a variant), both claims fail, so they are marked as resting on the pooled reading.
- fig6g-fg-frequency-sst stays partially reproduced under both readings (now CA3 and DG, all 7 SST-Cre mice). fig5f-sg-frequency-pv stays not reproduced.

**What I added or corrected:**
- **Track alignment:** the LFP `starting_time` is now read (0 s in every file). A lag scan from -60 to +60 s shows the theta/delta ratio against speed peaking at zero lag (mean r 0.134 against 0.009 beyond 30 s; 122 of 170 sessions within 2 s).
- **Track spike clock:** a check against SWRs in still periods finds a clear peak in only 24 of 170 sessions, so the sub-second spike offset is not established on the track. This is recorded as a finding.
- **SW amplitude:** I added the per-session median raw LFP (39 file units), a mean-removed reading (now the main one), a pre-event baseline reading, and vehicle group means against Table S4. The offset turns out to be small and every variant gives the same result. The amplitude is about 8 times Table S4's values, and I record that as unexplained.
- **Genotype tests:** p-values with 5 degrees of freedom and their Holm decisions are now printed.
- **Session order:** a check within the vehicle sessions finds that only one of the nine empty vector run changes drifts before CNO. Speed by session rank is also printed.
- **P/S sex interaction on the track:** it is skipped because that group has 6 female mice and 1 male, and the notes now say so.
- **Units:** the data check no longer calls the file units 0.195 µV ADC steps. The LFP-unit finding is restated as unresolved.
- **Speed-up:** model fits now run in parallel and the metadata scan uses processes, which keeps the rest notebook under the 60-minute limit.
- The round-1 verification is recorded for all 42 claims (the verifier agreed with every outcome), along with two added questions for the authors and an updated README.

**Not done:**
- No questions were added to `questions/jones-2021.yaml`, because the verifier reported no misreading of the claims file.
- The spike-shifted run MUA variant gives no test: too few track sessions have a clear lag under both treatments.
- I did not change the dentate spike detection; the verifier found it matches the paper's rate.
