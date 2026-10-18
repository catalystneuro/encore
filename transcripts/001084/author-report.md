I finished steps 1 to 6 for dandiset 001084. The entry was locked and passes `check`; the clean run passed in 827 s; the handover was built in `executed/001084-vu-2024/handover/`. Nothing is committed.

I used the full text of the NIH author manuscript in PubMed Central (PMC10957316), saved under `paper/`. The supplement PDF was blocked by a captcha, so I did not read the supplementary figure legends. I pinned version 0.241023.2011, the only published version; the paper cites no DANDI version.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1c-isosbestic-control | reproduced |
| figs2d-correlation-distance | reproduced |
| figs2ef-no-bundle-crosstalk | reproduced |
| fig1d-chronic-reward-stability | partially (only weeks 5 to 8 can be tested) |
| fig4-link-published-results (with Zenodo inputs) | reproduced |
| fig4e-light-increases-widespread | reproduced |
| fig4e-light-anterior-posterior-gradient | partially |
| fig4f-tone-tail-increase-anterior-decrease | reproduced |
| fig4f-decreases-lateral-ventral | partially |
| figs4ac-patterns-consistent-across-mice | partially |
| figs4eh-patterns-not-movement | partially |
| figs5-isosbestic-no-pattern | partially |
| fig5ab-response-latencies | partially (the paper's code counts one frame later; with its count the means match within 2 ms) |
| fig5g-light-latency-gradient | reproduced |
| fig5h-tone-latency-gradient | reproduced |
| figs6cd-gradients-individual-mice | partially |
| fig6-inclusion-counts | partially |
| fig6gh-release-decays-with-distance | reproduced |
| fig6g-dorsal-spread | partially |
| fig6-tdtomato-control-no-response | reproduced |
| figs7a-photoswitch-confined | reproduced |
| figs1, figs3, fig3, fig7d, fig7ef (data only on Zenodo) | blocked: other, not attempted |

Totals: 10 reproduced and 10 partially reproduced on the dandiset alone, 1 reproduced with Zenodo inputs, and 5 blocked.

## 2. The dandiset

- **Matches the paper:** the 280 fibers from 7 mice (4 F, 3 M) are exactly the paper's. The raw stimulus-triggered averages equal the paper's published per-fiber values (difference 0.0).
- **Missing data:**
  - stimulation times and the identity of the stimulated fiber in every optogenetic session; I recovered them from the laser artefact in the ΔF/F;
  - the tone frequency for DL18, which has 44 tones where the paper used its 14 tones at 12 kHz;
  - the task variables that separate unpredicted rewards in DL15's later sessions;
  - one of the 26 tdTomato control sessions;
  - the data for Figures 2, 3, 7, S1, S3 and S5A to D (on Zenodo).
- **Metadata errors:**
  - the `included` column is described as "successfully implanted" but marks fibers within the striatum, leaving out fibers on its border;
  - UG21's indicator says tdTomato, but its sessions match the paper's rDAm3.0 mouse without opsin;
  - DL31 and DL32 store a regular frame rate whose times drift up to 0.5 s from the actual frame timestamps;
  - the archive summary describes the approach as "cell population imaging".
- **Paper code against the Methods:** latencies are counted one frame late, negative cross-correlation lags are not shifted, and the Figure 1C legend does not match the plotting code.

## 3. Protocol gaps

1. There is no blocking reason for an `elsewhere` claim that could be tested but was not attempted. I used `other` with "Not attempted" for the five Zenodo-only claims.
2. A reported number can come from code that disagrees with the Methods: the latencies are off by exactly one frame. The rule for several readings says any matching reading counts; the Methods-versus-code rule says judge on the Methods. I followed the Methods-versus-code rule, so the claim is partially reproduced even though the code's count matches the paper.
3. The supplementary legends were unavailable. The protocol does not say how to write criteria for supplementary figures without them; I based them on the Results text and the code, and recorded that.
4. The protocol does not say whether "the stated spread" in the tolerance rule includes a standard deviation across fibers. I used 10% of each value and recorded why.
5. Facts seen only while preparing must not supply numbers to the record, but they can matter. The paper's folder names show the largest-artefact rule picks the wrong fiber in some tdTomato sessions. I mention this only qualitatively.
6. Checking for duplicate recordings means reading data from every file. I compared the sessions the analysis loads anyway; Grid-9 was skipped, as it is that mouse's only session.
7. The notebook takes 14 minutes, over the 10-minute aim, because the Methods' 10,000 null refits run for each of 11 fits. I kept the Methods' number.

## 4. Runtime and failures

- The session ran about 2 hours. The final notebook run took 827 s (13.8 min).
- During preparation Zenodo returned "429 Too Many Requests" errors; I handled them with retrying range requests, which the notebook also uses for its one Zenodo file.
- Early runs failed on bugs that are now fixed: a column named `tail` clashing with a pandas method, windows running past the end of the recording, and event placement in the 18 Hz sessions.
- The final run had no errors.
