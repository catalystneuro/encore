I've finished steps 1 to 5 of the Author protocol on DANDI:000630, version 0.230915.2257, and built the handover package. Only 4 of the paper's 44 claims could be tested, plus one link claim I added; the other 40 are blocked. `python tools/entry.py all` reports 0 errors and the notebook runs in 243 s. I did not verify my own work, commit or push.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| chartrand-label-link (link claim I added) | reproduced |
| sample-size | not_reproduced: the dandiset has 210 cells from 53 donors, against 542 from 170 (the criterion expected this) |
| fig3eg-human-fres-sag-rin | partially_reproduced, rests on an assumption: the slopes have the paper's signs and p < 0.05 in LAMP5 and VIP cells; only the VIP sag slope is within tolerance; PV cannot be tested |
| fig3ik-human-q-sag-rin | not_reproduced, rests on an assumption: sag effect p = 0.0046 (needs p < 0.001); input resistance p = 0.24. Under chirp reading (b) it would be partially reproduced |
| figs1-region-pathology | reproduced, rests on an assumption |
| 16 claims needing mouse cells, 5 needing cells across cortical depth or morphology, 4 on cultured cells, 4 on gene expression, 4 model claims that need a rebuild, fig2d-pv-highest | blocked, `other` |
| fig5be and figs3 (ZD7288 recordings) | blocked, `data_missing` (the paper says "on request") |
| fig7-model-ca and the three fig8 claims | blocked, `methods_underspecified` (the calcium conductance density is not given) |

## 2. Dataset, assumptions, questions

- **What the dandiset holds:** 210 human layer 1 cells from 53 donors. 93 files have chirp sweeps; 85 cells have a usable 20 s chirp (67 LAMP5/PAX6/Other, 18 VIP). There are no PV, SST, mouse, cultured, ZD7288, transcriptome or morphology data.
- **Linking labels:** every file matches the Chartrand repository table (pinned commit 7777857) by session id. Sex and age agree.
- **Table S1:** all 53 donors appear in it, but 43 are listed under "AcuteLDPublished" and only 10 under "Chartrand". I recorded this as a finding about the paper.
- **Problems in the files:** many sweeps were stopped early and are zero-filled without a flag. The files carry no subclass, region, disease or depth labels. The species is spelled two ways. No recording is deposited twice within the dandiset.
- **Assumptions:** I adopted the IPFX computations (chirp reading O1(a), sag O2(a), input resistance O3(a)). The Methods name IPFX, and reading (a) gives resonant fractions (LAMP5 32.8%, VIP 22.2%) close to Table S3's (31.25%, 25.0%); reading (b) gives 20.9% and 16.7%. Every reading is shown in the notebook.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): which frequency range and Z0 they used, the LOWESS fraction, and how sag and input resistance were defined.
- **Questions to a reader:** none.
- **Datasets the registry may want to list:** these are leads, not verified. The mouse cells look like they are in DANDI:000020 (I checked one specimen id). The Lee, Dalley et al. 2023 human cells may be in DANDI:000636. Neither was deposited for this paper.

## 3. Where the protocol was unclear

1. **No good block reason for public data the run had no time to link.** None of the `blocked_by` reasons fits mouse data that are probably public but would need a specimen-to-file map and hours of work. I used `other` and said where the data seem to be.
2. **Table S1 is only in the supplement.** The notebook may not read local paths, so I copied the donor labels (no numbers) into `resonance.py`, cited them, and listed them under `inputs`.
3. **Adding a link claim edits other claims.** I had to add `depends_on: chartrand-label-link` to three paper claims. The protocol requires it, but it also says the claims file binds the author. Statements, expected values and criteria are unchanged.
4. **Criteria assume subclasses that are missing.** Several criteria assume four subclasses. With only LAMP5 and VIP, a two-level interaction is not the paper's test. I judged only the parts the dandiset can test, and said so in the notes.
5. **`measured` cannot record an untestable value.** It has no way to say "not measurable" (the PV slopes), so I left it out for fig3eg.
6. **One reading of a method could not be run.** O5(a), Satterthwaite F tests, needs SPSS or R, which are not in the entry's environment. I ran O5(b), statsmodels Wald tests, plus GEE, and recorded it as a deviation.
7. **The checker blocks `data_missing` for `elsewhere` claims**, even when what is missing is a parameter. I used `methods_underspecified` for the model claims.

## 4. Runtime and failures

- **Runtime:** the run took about 2 h of the 5 h budget. The notebook takes about 4 minutes, almost all of it streaming the files, and peaks at 0.4 GB of memory.
- **Lost time:** about 55 minutes went on two loader runs that timed out. h5py's global lock serialized the threaded streaming; I switched to separate processes.
- **Smaller failures:** HEAD requests to DANDI download URLs returned 403, so I used the asset's metadata URL instead. GEE gave no estimate for the per-subclass VIP model. The statsmodels mixed model without interactions did not converge under the main reading for fig3ik; GEE on the same terms is shown.

Files are in `entries/mansvelder-2026/`:
- reproduce_mansvelder_2026.ipynb
- resonance.py
- entry.yaml
- README.md
- requirements.in and the lock file

The record is `attempts/mansvelder-2026-01.yaml`, the link claim was added to `claims/mansvelder-2026.yaml`, and the verifier's package is in `executed/mansvelder-2026/handover/`.
