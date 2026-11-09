I've done steps 1 to 6 of the Author section for CRCNS pfc-1 against Rodgers & DeWeese (2014). Of the 35 claims, 33 are reproduced, one is not reproduced and one is partially reproduced; none is blocked. `tools/entry.py all` passes: 0 check errors, and the notebook runs from a clean environment in 132 s. The handover package is in `executed/crcns-pfc-1-rodgers-2014/handover/`. I did not commit anything.

**Version.** CRCNS data sets have no versions, so I recorded `unversioned` with DOI 10.6080/K0W66HPJ. The zip is pinned by its MD5 (`a8bc7ed9…`) from the bucket's `checksums.md5`, and the notebook checks that the bucket still lists it. The header gives this reason.

### (1) Outcomes

| Claim | Outcome |
|---|---|
| unit-table-link (a link claim I added) | reproduced |
| fig2a, figs1a, fig2d, iti-median (behaviour) | reproduced |
| fig3c (76 = 36 + 40), fig4c (36 = 13 + 23), a1-rule-encoding-not-audresp-dependent, rule-encoding-effect-size (74.7%, 99.8%) | reproduced |
| fig3ab-pfc-example-units | reproduced |
| fig4ab-a1-example-units | **not reproduced**: tested as the claims file names the units; with the two units swapped, all four rates match exactly |
| fig3d (57 units), fig4d (16), figs2c-s3c, figs2f-s3f, figs2gh-s3gh | reproduced |
| fig5ab (0.550 s and 0.625 s), fig5c (2.725 s and 0.875 s), fig5d | reproduced |
| audresp-prevalence, figs5cd, figs5e, fig6cd (43 and 17 units, A1 slope 0.98), evoked-beyond-baseline-rare (6 of 43, 4 from Rat 1), fig6e, figs5fg, figs5hi | reproduced |
| figs2i, figs2kl, posture-equalized-sign (0.471 and 0.318), posture-equalized-magnitude | reproduced |
| fig7, fig7c, figs1bc-catch | reproduced |
| fig8-model | **partially reproduced**: at SNR 0.25, 99% or better holds for only 25 to 30% of positive task signals, not "most" |

### (2) Dataset, assumptions and questions

**What I found about the dataset:**
- The spike files hold 2977 clusters. Which 220 are the units the paper analysed, and their auditory response windows, are only in the code repository's `unit_db.csv`, not in the dataset.
- Recomputing auditory responsiveness as the Supplement describes gives 46 mPFC and 61 A1 units, not the paper's 31 and 49. The table applies rules the paper does not state.
- All files are Python 2 pandas 0.10 pickles that current pandas cannot open. I read them with a custom unpickler in `pfc1.py`.
- Two CR21A sessions carry an undocumented second spike file. The spike times are the same, but tetrode groups and unit numbers differ.
- The descriptor names the stimulus column `stimulus_name` (the files say `stim_name`) and gives a stimulus numbering the files do not follow.
- Three sessions have no spike file.
- The code's figure index swaps the Figure 4A and 4B units.
- The Figure 4B legend swaps the trial counts relative to 4A.

**Assumptions:** none. Every method detail came from the claims file or the code it names. Two results depend on code details the paper does not describe, and I show the alternative as a variant:
- **Figure 5A/B onsets:** they match only with the code's smoother, which snaps spikes to a 50 ms grid. With exact spike times the mPFC median is 0.75 s.
- **Posture PRE:** it matches with the median-centred MAD. The code's own comment says its version did not centre.

**Questions for the paper's authors:** none.

**Question to a reader:** one, on fig4ab: should the units be identified by the legends rather than the code's figure index? It is in `questions/crcns-pfc-1.yaml`.

### (3) Where the protocol was unclear or did not fit

1. **Link claims.** Step 1.4 says dependent claims list the link claim in `depends_on`, which edits claims the reader wrote. I added `unit-table-link` to the claims file and only appended to `depends_on` fields; the claims check passes.
2. **Version.** The prompt asks for a "pinned published version", but CRCNS has none. I followed `docs/archives.md`: `unversioned` plus the MD5.
3. **Which data label.** `unit_db.csv` supplies measured values (response windows), not just names, so it is arguably `with_inputs`. I kept the claims file's `with_labels`.
4. **Several readings.** Reader step 3 says a claim holds if it matches "under any reading". Author step 1.6 says "the outcome is the one they all give". I applied the claims file's criteria, which say "under one reading".
5. **Misreading the paper.** Testing the file as written forces "not reproduced" on fig4ab even though the data match the paper exactly. That outcome is misleading until a reader answers.
6. **Clock check.** The protocol suggests decoding a task variable. I used the evoked response at stimulus onset against shifted times, plus the hold-period rule encoding. Fourteen sessions have no auditory-responsive unit, and they are listed.

### (4) Runtime and failures

The work ran from 13:41 to about 14:26 UTC, roughly 45 minutes; the notebook itself takes about 2 to 3 minutes. Nothing failed. `git status` shows untracked root entries (`.bashrc`, `.gitconfig`, `scripts`, `.idea` and others). They are `/dev/null` device nodes the sandbox created at 13:39, before the run, not files I made. The commit step should not pick them up.

My files are in the repository root:
- `entries/crcns-pfc-1-rodgers-2014/`
- `attempts/crcns-pfc-1-rodgers-2014-01.yaml`
- `questions/crcns-pfc-1.yaml`
- `claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml` (additions only)
