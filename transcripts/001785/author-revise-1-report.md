I've revised attempt `001785-fujimoto-2026-01` for each point in the verifier's round-1 report. The entry was re-run with `python tools/entry.py all`: the check gives 0 errors and the notebook passes (293 s). Nothing is committed.

**Outcome changes**
- **fig6c-sham-cc1-no-change:** reproduced (assumed) → blocked, `methods_underspecified`. This was the only claim where the verifier disagreed (B1). With a 10-pixel minimum object size p = 0.31; with 50 pixels p = 0.044. Neither size can be defended: in monkey D the counts match the paper's only at 50 pixels, in the N and T regions only at 10, and no single setting matches every region. Using a different size per region would not be the paper's procedure.
- **ed6b-uf-fm-no-change:** still reproduced, but no longer marked assumed (B2). The main test now uses only the fields of the paper's design. The Methods say "5 fields × 4 sections" and the claims file's n is 40 fields per hemisphere, so N122 RW6 (a sixth field with no row in the paper's sheet) is left out. All four counting readings then agree (smallest p = 0.0685). Adding N122 RW6 back is shown as a variant and gives p = 0.04997.
- **fig3f-gratio-decrease:** still blocked, but the reason is now `other` instead of `not_runnable` (B12). The per-axon sheet, now printed, gives image names and measurements but no axon positions.

**Corrections and added outputs**
- **link-if-counts (B3):** the record had said the counts matched in two of four regions; the correct figure is three of four (monkey D's region matches at 50 pixels). The notebook now has a table applying the criterion per reading and region, scatter plots of my counts against the paper's, and a check that the red channel is CC1 and the blue is DAPI. The notes say no single reading matches every region and that my counting only approximates the paper's FIJI counts.
- **ed6a-dacc-cb-no-change:** still not reproduced. The notes now say the difference may come from my counting method, since the paper's own counts give p = 0.09.
- **FA value matching (B5):** values that match within 1e-6 now count every voxel inside that window. 199 values match exactly and 6133 by nearest value; 641 have more than one candidate voxel, but the candidates differ by at most 1.6e-6, so no FA value used changes. Every repeated voxel in the paper's lists is the same value listed twice.
- **fig5a-control-group-no-reduction (B9):** reading (b) now runs, without the cluster-level correction because AFNI isn't available here. It finds no negative cluster larger than 3 voxels, though the mean change in PCC and vmFC is negative in all three control animals. The claim stays blocked because reading (a) still can't be run.
- **fig6d-sham-scc-little-change (B7):** a thresholded map can't be made for monkey D (one map per session), so the notebook reports the unthresholded change instead. The ten largest increases sit next to the sham-side area 25, six of them inside it.
- **Other points:**
  - The two DANDI:001773 FC matrix files are now named in the header and the fig4 notes, with why they can't be used (B8).
  - The behaviour sheet's column headers are printed (B10).
  - The paper's DAPI p = 0.9611 is recorded as a misprint for 0.9511 (`paper_inconsistency`, B11).
  - The FA and seed claims are now described as re-running the paper's statistics on its own data (B4).
  - The `methods_unavailable` finding (the question for the paper's authors about how cells were counted) is updated.
  - The README and the notebook summary are updated.
- **Round-1 record:** the `verifications` entry lists all 35 claims, with the verifier agreeing on 34 and disagreeing on fig6c.

**Not done**
- **Small Tukey p-values (B6):** values below about 1.4e-11 still print at scipy's floor. They are all far below 0.05 and the floor is stated, so no conclusion depends on them.
- **Questions file:** I added nothing to `questions/001785.yaml`, because the report found no place where the claims file misreads the paper.
- **Pre-existing changes:** `tools/build_site.py` and `tools/site_assets/app.css` were already modified before I started; I left them alone.
