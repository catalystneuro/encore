I've finished steps 1 to 6 for yang-2025. `entry.py check` reports 0 errors, the clean run passed in 661 s (about 11 minutes), and the handover package is in `executed/yang-2025/handover/` with the conclusions removed. I did not verify my own work, commit or push.

The dandiset has one published version, 0.241023.0931, which I pinned. It holds 56 files, one per rat and group, each a set of 600 s seizure clips (519 in all) at 1 kHz on 4 channels. It has no seizure onset or end times, no stimulation times, no interictal recordings and no recording durations. I therefore marked seizure onset and end with a line-length rule, which is an assumption, and found the stimulation trains from the artefact they leave in the recording. Every tested outcome rests on that onset rule and is marked `assumed: true`.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| tables1-network-stable-short-term | reproduced (only when self-pairs, r = 1, are counted as intra-group) |
| fig2-r1-target-shifts | partially reproduced (3 of 4) |
| figs2-target-assignment | partially reproduced (20 of 28 baseline groups; 9 target / 19 non-target groups) |
| fig3a-target-reduces-each-rat | not reproduced (3 of 8) |
| fig3a-nontarget-can-lengthen | reproduced (11 of 20) |
| fig3a-per-rat-site-differences | partially reproduced (5 of 11 pairs, but R1 and R6 also show pairs) |
| fig3a-target-vs-nontarget-total | not reproduced (-0.037 vs 0.003, p = 0.93) |
| fig3a-some-nontarget-shorten | partially reproduced |
| fig3b-same-site-target-vs-nontarget | not reproduced |
| seizure-duration-proportion, fig3c-frequency-no-difference | blocked, data_missing (no recording time) |
| fig4b-psd-target-bands, fig4b-psd-other-bands-unchanged | not reproduced |
| fig5b-iis-post-seizure | reproduced (time-bin reading, p = 7.8e-10; mixed across rats) |
| fig5c-interictal-iis, fig5d-iis-seizure-correlation, fig6cd-interictal-hfo | blocked, data_missing (no interictal data) |
| fig6e-ictal-ripples-no-difference | reproduced (p = 0.73, but my HFO detector gives values far from the paper's) |
| fig6f-ictal-fast-ripples-reduced | not reproduced |

**(2) Dataset, assumptions and questions**
- **Baseline groups hold stimulated seizures.** At least 7 baseline clips (R1 base2, R4 base0, R5 base0, R6 base1) carry 5 s stimulation trains like those of the stimulation groups.
- **Clip names collide.** 16 clip names occur in two groups of the same rat with different contents. Some clip dates also fall outside their group's place in the order (for example, R3's CA1 group predates its base3 group).
- **Stimulation order.** For R5 and R6 the order in the dandiset differs from the paper's Figure S2.
- **Smaller points:** no duplicate recordings were found. Two groups hold fewer than the 6 seizures the paper states. The `-small` and `-large` clip names are not explained. The ANT depth is -5.6 mm in the files against -6.0 mm in the paper. Age and weight are the same in every session.
- **Assumptions:**
  - The onset rule: 1-40 Hz line length with thresholds 3 and 2, shown also at (2, 1.5) and (4, 2.5). I chose the thresholds on stimulation timing in 42 clips, before computing any claim.
  - The post-stimulation window is the 5 s after the first train ends.
  - HFOs are counted with detector settings I chose, since the paper's are not given.
- **cf_w sign:** the data favour out-strength minus in-strength, against the wording of Methods B: it recovers 20 of 28 Figure S2 targets, the other sign 0 or 1.
- **Questions for the authors:** eight, in one `methods_unavailable` finding. They cover the onset rule, the cf_w sign, the VAR order and significance test, the normalization, the post hoc tests and PSD settings, the post window, the HFO App settings and the pairing in Figure 6.
- **Questions to a reader:** none.

**(3) Protocol points**
1. `tools/entry.py lock` writes a `python: "3.13"` line into entry.yaml, but the schema rejects it, so `check` failed. I deleted the line, after which the check passed. The modified `tools/entry.py` was already uncommitted in the checkout.
2. The protocol does not say what to do when one assumption (here, seizure onset and end) underlies every tested claim. I marked every outcome `assumed: true` and said so in the summary.
3. "Reproduced under any reading" lets a reading that is built to favour the claim decide it (self-pairs of r = 1 in tables1). I followed the rule and flagged it in the notes.
4. The partial clause of fig3a-per-rat-site-differences does not say whether R1 and R6 must show no pairs. I read it literally (5 of 11 pairs is enough) and recorded that R1 and R6 do show pairs.
5. The protocol gives no guidance on tuning a detector on the data when no annotations exist. I tuned only against the stimulation timing, not the claims, and recorded it.

**(4) Runtime and failures**
- About 1 h of the 5 h budget, finishing around 00:25 UTC. The entry run takes 661 s.
- The only failure was the schema error in point 1.
- Untracked dotfiles (`.bashrc`, `.profile`, `.idea` and others) appeared in the repository root. I did not create them and left them in place.

Files are in `entries/yang-2025/`:
- reproduce_yang_2025.ipynb
- yang2025.py
- README.md

The attempt record is `attempts/yang-2025-01.yaml`.
