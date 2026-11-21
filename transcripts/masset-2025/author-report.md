I finished steps 1 to 6: the entry, the claims-file additions, the attempt record and the handover. One thing is not clean. After the full run passed, I added the entry README. That changed the entry's hash and started a second full run, which my shell cut off at 60 minutes. The executed copies are complete and error-free: two notebooks were re-executed and gave the same outputs, and the third is from the passing run. But no clean-run stamp exists for the entry as it stands now.

**(1) Outcomes** (under the claim's seed; † means another of the five seeds gives a different outcome)

| Claim | Outcome |
|---|---|
| link-units-across-tasks (link claim I added) | reproduced |
| cued-delay-neurons | not reproduced (67 units deposited, 43 selected) |
| session-trial-counts, fig2b, fig2c, fig2f, fig2g, fig2k-reward-timing-decoded, ed6e, ed5 | reproduced |
| ed3f, fig2k-better-than-single-discount | partially reproduced |
| ed5g † | partially reproduced |
| ed6g | not reproduced |
| fig3b | partially reproduced |
| fig3-common-value-fit, ed7c, ed7de, ed8cd, fig4a (assumed) | reproduced |
| fig4b † (assumed) | reproduced |
| ed8b †, ed8ej †, ed10 † (assumed) | partially reproduced |
| ed9g | blocked, too_large (estimated 3.6 h for 200 constrained fits) |
| mixing-model-accuracy | blocked, methods_underspecified |
| fig1f, ed2e, ed2 (simulations) | blocked, other (not attempted for time) |

**(2) The dataset**
- **Version:** DANDI:000251 has no published version. I pinned the draft by its modification time (2023-06-20) and said so in each notebook header.
- **Missing cued delay data:** the dandiset has no cued delay recordings, although the paper's deposit says its raw data are there. The cued delay units are in the paper's Mendeley deposit (doi:10.17632/tc43t3s7c5.1), which holds 67 of the 78 units in the paper's own table. I tested those claims there as `data: elsewhere`. Mendeley is not an archive the registry reads, so the paper cannot be listed on it.
- **Duplicates (rated critical):** 78 open-loop units are deposited twice, as `SU-VR-OL` and `SU-VR-ALL-OL` files with identical spike trains under different session numbers. The verifier must review this rating.
- **Mislabelled file:** `sub-3015 SU-VR-OL-4` holds a teleport session.
- **No identification flag:** the single-unit files carry no optogenetic identification flag and no unit description.
- **Passed checks:** the spike, lick and trial clocks agree in both sources, and every unit matches a row of the paper's table.
- **Assumption:** the common value model fit is capped at 10,000 iterations. On a subset, 3,000 iterations give a different result and 30,000 about the same. The VR-fit claims are marked `assumed: true`.
- **Questions for the paper's authors:** how far the fits converged; how many singular components the decoder uses (the decoding function is not in the deposit); and the mixing model's sharing parameter, which is lost from the text.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or missing something**
1. **No published version:** the protocol covers a draft only for repeat attempts. I pinned the draft by its modification time.
2. **Who sets `data`/`where`:** step 4 says to use `elsewhere`, but not whether the author may write it on reader-written claims. I set only `data`, `where` and one `depends_on`.
3. **Claims needing both sources:** session counts and the cross-task claims use DANDI and the Mendeley deposit together. I used `with_inputs`.
4. **Findings about a deposit not in the record's datasets:** an `about: data` finding would land on the DANDI page. I recorded them as `other`, `about: paper`.
5. **Five seeds with expensive shared fits:** this was most of the 69 minutes. Shared fits use the seed of the claim that defines them. The cross-task claims use the VR fit at the claims' seeds only.
6. **README after the run:** step 5 adds the README after step 4's run, but editing any entry file forces a full re-run. That caused the cut-off second run. The README should be written before running.
7. **Link-claim schema:** a link claim cannot have `inferred`, so I put the authorship note in the criterion.
8. **Untested for lack of time:** there is no `blocked_by` for a claim not attempted for time rather than stopped by computation. I used `other`.
9. **No partial rule in the criterion:** for ed8b, fig2k-better-than-single-discount and ed10, I used the protocol's general definition of partially reproduced.

**(4) Runtime and failures**
- **Full run:** passed at 14:33, taking 25, 32 and 11 minutes for the three notebooks.
- **Second run:** started by the README edit and cut off at 60 minutes, as described at the top.
- **Leftover files:** stray dotfiles that I did not create (`.bashrc`, `.vscode` and others) appear untracked in the repository root. I left them alone.
