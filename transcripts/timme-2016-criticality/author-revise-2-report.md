I've addressed every point in the round-2 report. No outcome changed. I propose one change, on fig8-exponents-match-literature, for round 3 to review. The entry is re-run and its checks pass with 0 errors, and nothing is committed.

**How the re-run was done.** The four notebooks together take about 2 h 20 min, which is longer than one foreground command can run (2 h). So instead of a single `entry.py all`, I ran `entry.py run` twice. Each time I trimmed `entry.yaml` to two notebooks, then put the full file back and ran `entry.py check` on it. All four notebooks pass:

| Notebook | Runtime |
|---|---|
| culture_criticality | 38 min |
| models | 9 min |
| complexity_culture | 31 min |
| complexity_swap | 40 min |

I merged the two `result.json` files and copied the text corrections into the executed notebooks. The code cells are identical to what ran.

**Outcomes**
- **fig8-exponents-match-literature:** stays blocked, with `proposed: reproduced`. I read the reference values from Mazzoni et al. (2007) and Friedman et al. (2012) and added them as inputs. For both papers, for tau and for alpha, and under every variant, the sub-sampled mean is closer to the cited value than the full-system mean. I found no open full text for Pasquale et al. (2008). The third paper could not reverse a two-of-two result.
- **fig12a-swap-preserves-complexity:** stays reproduced. A new notebook, `complexity_swap.ipynb`, runs only the real and swapped data on 200 recordings. The original 40 give exactly the same values there. The rank-sum test still finds no change (p 0.933), and that test is what decides the outcome. However, Pearson r falls to 0.658, below the 0.7 reading of "strongly correlated". The notes and the round-3 record say this; whether it deserves more weight is for the verifier.
- **Jitter now matches the toolbox:** it moves one spike at a time, as `randomizeasdf2.m` does. The data check prints the share of spikes that stay in place: 0.449, 0.135 and 0.054 for 1-, 10- and 100-bin jitter. Every jitter claim keeps its outcome. In fig10a, 10-bin jitter is no longer significant (corrected p 0.0955), which still leaves the claim not reproduced. All affected numbers are updated.

**Corrections**
- The complexity runtime now quotes the printed value (28.1 min).
- The "78-fold" wording is now a relative change of 77.7, or 78.7 times the real median.
- The README timings are fixed, and its sentence about exceptions now names the 1-bin and 10-bin jitter cases and the fact that fig10b passes under only one susceptibility reading.
- Cell 14 now says one recording, not four.
- The summary no longer lists the old jitter deviation.
- The 134 s per complexity call is now marked as a development timing not printed in any notebook.

**Questions for a reader.** I created `questions/timme-2016-criticality.yaml` with five questions:
- fig5f: the 5% bound is smaller than the estimator's own spread.
- figs8 and figs9: the 10% tolerance is narrower than the sampling error of r.
- eq4-relation-randomized: it cites a claim id that is not in the file.
- fig10c: the criterion defines no partial outcome.

**Round 2 is recorded** under `verifications`, with all 28 claims.

**Not fully done**
- **Toolbox comparison:** I ran the toolbox in GNU Octave, outside the notebooks, so it supplies no numbers to the record.
  - `cbmodel.m` agrees with the port within the spread between runs. It has no refractory period either, so the one-step ratio below 1 where 4·p_trans = 1 comes from the model itself, not the port.
  - The uncorrected `complexity.m` integration curve matches the port to 1e-12.
  - I could not run the cut step, because Octave's `findpeaks` package would not install.
- **Recording counts:**
  - fig12a: all 435 recordings would take about 85 min, over the 60 min notebook limit.
  - figs9: I did not re-run it on more recordings.
- **Untracked dotfiles:** files such as `.bashrc` and `.idea` appeared at the repo root. I did not create them and left them alone.
