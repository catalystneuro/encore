I've finished steps 1 to 5 of the Author section and run the handover; the package is in `executed/001195-lee-2025/handover/`. The entry check passes with 0 errors, and the notebook runs from a clean environment in about 15 minutes (883 s on the final run).

I pinned version 0.250408.1733, the only published version. The paper cites none, and the draft has the same 230 assets and size.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig6df EPSPs and IPSPs at rest | reproduced, but the cell counts differ: 15/40/56 against 19/36/48 |
| fig6gi firing responses | partially reproduced: the pattern holds, but there are 3/13/13 firing cells against 5/20/17 |
| fig6j EPSP amplitude by region | reproduced, resting on an assumption |
| fig6k IPSP trough by region | not reproduced |
| fig6-s1de TTX/4AP | blocked: metadata_insufficient |
| fig6no CeA clusters | partially reproduced: 2–3 cells in the late-firing cluster are inhibited |
| fig6-s1h CeA cluster properties | reproduced |
| fig6pq BLP clusters | partially reproduced: 59–65% inhibited against 93%, 73% excited against 62% |
| fig6-s1i BLP cluster properties | reproduced |
| fig6-s1jk cluster voltage area | reproduced |
| fig6-s1ln combined clustering | not reproduced |
| fig7-s1ef red against blue light | reproduced |
| fig7-s1hi red light during blue | partially reproduced: amplitude is smaller, area is not significantly smaller |
| 8 in vivo imaging claims (Fig. 7) | blocked: data_missing |
| 17 claims from Figs. 1–5 and 8 | blocked: data_missing |

**(2) What the dataset holds, assumptions and questions**

- **Contents:** 148 patch-clamp cells (130 ChR2, 18 ChrimsonR) and 41 imaging sessions from 14 mice. There is no pose data, no cup interactions, no record of which cup held the juvenile and no session epochs, so none of the in vivo claims can be tested.
- **Light timing:** the light is not recorded anywhere; the stimulus series are all zeros. I took the first pulse as 5.468 s into each sweep, read from where the responses start; the later peaks are about 33 ms apart, as 30 Hz pulses would give. 19 ChR2 cells recorded only with other light protocols are left out.
- **Imaging rate:** the imaging is labelled 25 Hz, but its length matches the behaviour videos only at 20 Hz, the rate in the Methods. That holds in 40 of 41 sessions; one video lasts 800 s.
- **Cell counts:** the imaging files hold about twice as many ROIs as the paper's cell counts (869/913/854 against 429/441/484), and nothing marks which ones the paper kept.
- **Wrong descriptions:** the imaging files' virus, stimulus and experiment fields describe another experiment (GRIN lens in mPFC, Chrimson in BLA, 589 nm light).
- **Mislabelled patch-clamp data:**
  - The injected-current channel is stored with unit volts.
  - The seal test is stored as an IZeroClampSeries, but it is a voltage-clamp recording.
  - No sweep is marked as recorded in TTX/4AP.
  - Two cells named like BLP cells (P4x, P42) are labelled BNST.
  - One cell (P10) sits at −18 mV.
  - Subject IDs are inconsistent ("4484?", "235 cage").
- **Assumption:** for fig6j I included the "mix" cells (EPSP and IPSP together) among cells with an EPSP. Without them the region effect is not significant (p = 0.76 and 0.55).
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How was an EPSP or IPSP detected? The 2–3 SD rule calls most cells "mix" and finds 51–85 IPSP cells against the paper's 34.
  - Does Fig. 6J include the mix cells?
  - The capacitance code (Q-method) and its 250 ms step are not published or in the files. I estimated capacitance from the 5 mV seal-test pulses instead.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear**

1. It doesn't say how to handle a stimulus time missing from the files when it is data, not a method. I took it from the data, showed a check, and recorded it as a deviation and a finding, without `assumed: true`.
2. Some count claims have a criterion that judges "on the cells present" (fig6df) and others don't (fig6gi). Where the pattern held but the 0-tolerance counts failed, I recorded `partially_reproduced`.
3. Several criteria only define "reproduced" or "blocked if readings disagree". Where every reading failed in the same way (fig6no, fig7-s1hi), I used `partially_reproduced` when the effect held in part.
4. The protocol doesn't say how to quote the dataset id in YAML. I quoted `id: "001195"` so non-PyYAML parsers don't read it as a number.

**(4) Runtime and failures**

The run took about 1 h 50 min (07:32 to 09:19 UTC). Nothing failed. Loading the patch-clamp files takes about 13 minutes of the notebook's 15, over the protocol's 10-minute aim but within CI's 60. The untracked dotfiles at the repository root and `entries/001195-lee-2025/.claude/` were not created by my commands; I left them alone, so check them before the workflow commits.
