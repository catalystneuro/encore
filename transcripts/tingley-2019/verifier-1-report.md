**Verifier report, round 1: Tingley & Buzsáki 2019 on DANDI:000218 (0.261110.1911)**

There are 39 claims in the claims file. The notebooks test 30 of them and treat 9 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| dataset-composition | partially_reproduced | Within tolerance: 6 animals, 1996 LS neurons with more than 50 spikes (reading a, LFP nb cell 13), 38 CA1+LS recordings (by unit label), 55 CA1-rate recordings (with the ripplesALL fallback), mean 31.1 neurons per recording. Out: CA3+LS is 10 or 19 (expected 25 ± 2.5) and LS-HFO-rate recordings 77 or 80 (expected 89, lower bound 80.1). That is 4 of 6 counts. |
| fig1c-hfo-each-animal | partially_reproduced | Median frequency is in 120–180 Hz in 6 of 6 animals. Firing at the event exceeds random by more than 3 SEM in 4 of 6 animals at the event bin and 5 of 6 at ±5 ms (cell 17). |
| fig1c-post-burst-suppression | reproduced (fragile) | Pooled over neurons at +20..50 ms, random minus HFO is 0.000200 against 3 SEM of 0.000178. It fails with stop..+50 ms, fails at 2 of 5 seeds (cell 19), and holds in only 1 of 6 animals. |
| fig1c-event-count | reproduced | 27,014 deposited LSRipples events against 29,955 ± 2,995 (cell 11). |
| figs1-participation | not_reproduced | Fraction is 0.057–0.107 against 0.16; spikes per event 0.079–0.155 against 0.23, under every window and averaging (cell 21). |
| fig1d-phase-locking | partially_reproduced | Trough preference holds: circular mean −167°, Rayleigh p ≈ 0. The locked fraction is 0.606 (detection channel) or 0.782 (own shank), below the 0.8325 floor under every reading (LFP cell 13). |
| fig1f-shorter-than-ripples | reproduced | 27.8 ± 9.5 against 31.2 ± 13.7 ms, rank-sum p = 1e-199 (cell 13). |
| fig1g-slower-than-ripples | reproduced | 147.6 against 158.3 Hz, both within tolerance, p ≈ 0 (cell 13). |
| fig1h-no-amplitude-frequency-correlation | reproduced | Under the Methods' amplitude (maximum NSS, i.e. `peak_normed_power`): Pearson p = 0.96, Spearman p = 0.36, r ≈ 0. The notebook's primary column `peak_amplitude` gives Spearman p = 0.00095 with rho = 0.02 (see B3). |
| fig2-confined-to-ls | not_reproduced | The criterion holds in 0 of 8 recordings. Medial-septum medians exceed LS in 3 recordings, and sites in every other structure have ratios above 1.5 (LFP cell 21). |
| fig2ef-intermediate-ls | blocked (metadata_insufficient) | Confirmed on the archive (see the paragraph after this table). |
| fig3-travelling-waves | blocked (metadata_insufficient) | Confirmed on the archive (see the paragraph after this table). |
| fig4b-pre-post-unchanged | partially_reproduced | PRE and POST differ at p < 0.05 in all 8 raw-count readings (p ≈ 0.004–0.007) and in none of the 8 normalized readings. There are 361–503 pairs against 7,172 ± 717 and 21–23 sessions against 53 (cell 33). |
| fig4b-hfo-above-behav | reproduced | Both parts hold in 12 of 16 readings; the jitter part holds in 16 of 16 at all 5 seeds (cells 35–36). This rests on about 6% of the paper's pairs. |
| fig4-sessions-few-change | not_reproduced | 21–23 sessions against 53; fraction 0–0.048 against 0.132; both directions never occur together (cell 38). |
| fig4c-temporal-bias | reproduced | No difference in any of 16 readings (smallest p = 0.06). This uses 16–19 recordings against 53, and PRE–BEHAV r ≈ 0 (cell 40). |
| fig4d-compression | partially_reproduced | PRE and POST exceed chance at factor 1, and PRE and POST never differ at p < 0.01. The largest factor is 5–12, against 20 ± 2 (cells 42–43). |
| figs3d-hpc-compression-post | partially_reproduced | POST exceeds PRE at p < 0.01 at only 1–3 of factors 1–7 (cell 45). |
| figs2-post-rate-increase | partially_reproduced | LS POST > PRE (p = 0.032). CA1 is significantly lower in POST (t = −2.0), and CA3 is not significant. Neuron counts are 1570, 2597 (or 2254) and 466 (or 809), mostly out of tolerance (cell 47). |
| figs2c-no-ls-reactivation | reproduced | At 25 ms after rate matching, EV does not exceed REV for any pair set at any seed (cells 49–50). The positive control fails, though (see B9). |
| fig5b-nrem-and-rates | reproduced | 72.9% of HFOs fall in NREM; NREM rate exceeds WAKE in 66 of 73 recordings (p = 3e-12); LS rates are below CA1 under both tests (p ≤ 1e-10) (cell 23). |
| fig5d-lag | reproduced | Median lag 6.2–6.4 ms with deposited peak times and 6.0–6.4 ms with maximum-NSS times; CCG peak is 37 SD above the flanks (cell 25; LFP cell 17). |
| fig5e-state-coupling | not_reproduced | 0 bins pass (smallest corrected p = 0.026). The NREM > WAKE fraction test gives p = 0.0025, not below 0.001. Pooled NREM 0.302 is within tolerance; WAKE 0.091 is not (cell 27). |
| fig5f-ripple-triggered-firing | not_reproduced | No bin within ±25 ms shows NREM higher (smallest corrected p = 0.18–1). There are 1,266 neurons against 1,313 (cell 29). |
| fig5f-no-phase-coherence | not_reproduced | PLV at the ripple time is 0.186, against a jittered mean of 0.104 and an upper bound of 0.126; 14 lags lie above +3 SD (LFP cell 19). |
| ls-spikes-not-locked-to-ca1-ripples | partially_reproduced | Inside CA1 ripples, 7.2% are locked (binomial p = 0.012), so locking is present. In the CA1 high-power epochs, 5.0% (p = 0.51), so it is absent. The two readings disagree (LFP cell 15). |
| fig6-optogenetic-hfos | blocked (data_missing) | Confirmed: the archive has 6 subjects (DT1, 2, 5, 7, 8, 9), all LS/HPC rats, and no optogenetic sessions. |
| fig7e-ca1-spikes | partially_reproduced (unreliable) | 47–80% against 38 ± 3.8; above the notebook's chance in every combination. The chance level used is 25–44% (see B1). |
| fig7e-state | partially_reproduced (unreliable) | 44–64% against 26; same problem as fig7e-ca1-spikes. |
| fig7e-duration | partially_reproduced (unreliable) | 41–89% against 20; same problem as fig7e-ca1-spikes. |
| fig7e-ca1-depth | blocked (metadata_insufficient) | Confirmed: the dataset description says electrode positions are not stored, and each unit has only its largest-waveform channel and waveform. |
| fig7e-replay | blocked (other) | Not data-blocked: position is present in 74 files (`SpatialSeries`/`Position`) along with trials and spikes. It was simply not attempted. |
| fig7e-seqnmf | blocked (other) | Not data-blocked: it needs only hippocampal spikes and CA1Ripples, which are loaded. Not attempted. |
| figs5-seqnmf-variance | blocked (other) | Not data-blocked, same as fig7e-seqnmf. Not attempted. |
| fig7e-content-independent | blocked (other) | The notebook's reason (it depends on fig7e-ca1-depth) is wrong. The partial criterion needs only 4 of 6 content-independent features, and 5 are computable; the real blocker is the unattempted content features. |
| fig7e-coupled-only | blocked (other) | Same as fig7e-content-independent. |
| discussion-medial-septum | not_reproduced | (a) The MS site ratio is below LS in only 3 of 6 recordings. (b) MS rate around ripples is *above* the mean (median ratio 1.43; below the mean in only 6 of 25 units) (cell 31; LFP cell 21). |
| discussion-cingulate-down-state | not_reproduced | (a) The minimum is at 105 ms. (b) The LFP extremum is at 2–82 ms per recording; none falls in 45–55 ms (cell 31; LFP cell 23). |
| fig8-model | blocked (other) | Testable: the model notebook is on GitHub (DavidTingley/papers 9f4cd48). Not attempted. |

On the two depth/geometry blocks (fig2ef, fig3): the dataset description says it does not store electrode positions or each recording's relative depth in LS. It also says it does not record which probe each depth in a session name belongs to. A rough check of fig2ef inside DT1 alone (one tetrode drive, single depth in each session name, 12 recordings) is the only part that could be tried, and only without LS borders.

### B. Problems

1. **[affects a conclusion]** Figure 7E notebook, `sig_from_mse`. The test is a one-sample t-test of 99–100 shuffled MSEs against the actual MSE, so it uses the standard error of the shuffle mean. Any value about 0.2 SD below the shuffle mean passes.
   - On synthetic normal draws this gives a 41% chance rate; a z-score against the shuffle SD gives 3%.
   - The notebook's own chance column is 22–44%. The paper's content features (6.6–8.1%) are "not different from chance", which implies a chance level of a few percent.
   - The Figure 7E y-axis is "number of standard deviations … from a distribution of MSE", which supports the z reading. That reading was not run.
   - This is the claims file's literal reading; I report its misreading here rather than correcting it. The percentages for fig7e-ca1-spikes, fig7e-state and fig7e-duration are not comparable to the paper's.
2. **[affects a conclusion]** Main notebook cell 33 (Figure 4 pairs). There are 361–503 pairs and 21–23 sessions against 7,172 and 53, and DT8 contributes 0 pairs from 17 recordings. Pairs before inclusion, and which epoch excludes them, are never shown. Every Figure 4 claim rests on about 6% of the paper's population. The PRE-vs-POST result flips with normalization: raw counts carry a confound from differing HFO time in PRE and POST.
3. **[does not affect a conclusion]** Cell 15 (fig1h). The Methods define amplitude as the maximum NSS, which is `peak_normed_power` (buzcode's `peakNormedPower`). The notebook takes `peak_amplitude` as primary and `peak_normed_power` as the variant. Under the correct column, both tests are not significant.
4. **[affects a conclusion]** Cell 27 (fig5e). The inset fraction test is run only over recordings. A test over pooled HFOs (pooled fractions 0.302 against 0.091, about 20,000 HFOs) was not run. It could move the outcome to partially_reproduced.
5. **[could affect a conclusion]** LFP cell 11, `lock_near`. The own-shank reading covers only shanks inside the detection channel's 16-channel block: 1,299 of 2,327 neurons. That reading's 0.782 is the one nearest tolerance.
6. **[does not affect a conclusion]** LFP cells 21 and 23 (fig2, cingulate b). Only the 2 storage chunks with the most HFOs are read (17–113 HFOs and 8–591 ripples per recording). Cingulate reading (b) is not pooled across recordings. In one recording the LS sites show no HFO power at their own HFO times (median ratio 0.97), which suggests label or channel problems; this was not investigated.
7. **[does not affect a conclusion]** Cell 29 (fig5f). The "WAKE outside trials" reading from the opening comment was not run here (it was run for fig5e). With WAKE already higher after normalization, it is unlikely to flip the result.
8. **[does not affect a conclusion]** Cells 17 and 19 (fig1c suppression). The outcome depends on the seed of the random-time baseline. The more stable comparison, against the pre-event baseline (0.00166 against 0.00140), is not the criterion.
9. **[affects interpretation]** Cell 49 (figs2c). The positive control fails. Without rate matching, HPC–HPC EV > REV does not reach p < 0.05 at 25 ms (paired p = 0.055), and reaches it at 1 s only by the paired test (p = 0.049; two-sample p = 0.055) and not after rate matching. The Methods report EV > REV at 1 s for every pair set; here it holds for none. So the absence for LS–LS has weak sensitivity.
10. **[does not affect a conclusion]** Helper module, `Session.epochs`. PRE, BEHAV and POST are taken from the first and last trial. The dataset description confirms the epochs are not marked, so this is a reasonable, stated assumption.
11. **[does not affect a conclusion]** Blocked rows. fig7e-content-independent and fig7e-coupled-only are attributed to fig7e-ca1-depth, but the actual blocker is the unattempted content features. fig7e-replay, fig7e-seqnmf, figs5-seqnmf-variance and fig8-model are "not attempted", not unavailable data.

The helpers I tested on synthetic inputs all behave correctly: `rayleigh` (null rate 0.048 at p < 0.05, correct mean angle), `ccg_all` (matches a brute-force count), `gauss_smooth` (edge normalisation), `in_intervals`/`intersect` and `triggered_counts`.

### C. What I could not check, and the output that would settle it

- **Figure 4 pair shortfall:** I could not find its cause. Needed: per session, candidate cross-shank pairs, the pairs failing inclusion in each epoch, and the PRE and POST HFO counts and durations.
- **Figure 7E under the z reading:** Needed: the percentage with z = (actual − shuffle mean) / shuffle SD below −1.96, with its chance rate.
- **fig5e with pooled events:** Needed: the pooled-HFO test of the NREM against WAKE fraction.
- **Own-shank phase locking for all neurons:** Needed: that reading for every shank, not only those inside the detection block.
- **Electrode-table and units columns:** whether any per-site waveform or position field exists. I used only the archive's API metadata, as allowed.
- **Whether `peak_normed_power` really is the per-event maximum NSS:** Needed: its range or a check against `T.nss` on one recording.
- **Region-label sanity for the fig2 and MS recordings:** Needed: per-site HFO ratio plotted against channel order on each shank.
