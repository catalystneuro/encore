No outcome changed in this round. All 33 claims stay blocked: 32 as `metadata_insufficient` and `wt-no-label` as `data_missing`. The verifier agreed with every one of them, and each agreement is recorded under `verifications` with its reason and my response. The re-run with `python tools/entry.py all` passed (0 check errors, notebook ran in 663 s, same numbers on the repeat run), and the handover is rebuilt.

**What I added for each point in the report:**

1. **Placing fields in their overviews (problem 1):** the notebook now lists every block of overviews and the fields that follow them, per mouse, in run order with acquisition times. Run order and time agree in all but 2 of 12,073 steps. It then tries to place 66 fields, drawn with a fixed seed, inside the overviews before them, by image matching, with another mouse's overviews as a control.
   - 26 of the 66 fields can be placed, and none of them at the magnification the dataset gives it.
   - Even where a field is placed, no overview is aligned to the brain atlas. Recovering regions would mean redoing the paper's hand alignment of hundreds of sections, so the block stands, and the notebook now shows why.
2. **Region-labelled Abeta42 images (problem 2):** I listed all 561 of them with mouse, age, sex and region, plus a count of bright spots at two thresholds, and showed one image per mouse for the six claim parts the verifier named. I did not score them for cells or plaques, for three reasons the outputs show:
   - **Scale:** 554 are classed 200X by rule, and the fields I could place are not at 200X.
   - **What is label:** a brightness count cannot separate cells, plaques, vessels and autofluorescence. The paper did that by eye against wild-type sections, which are not in the dataset.
   - **Coverage:** the fields are chosen spots inside a region, so they cannot show that something is absent or below a bound.

   This is recorded as "considered and not done", part by part, in the notebook and in the notes of the six claims.
3. **Coverage table (problem 3):** added a count of 200X Abeta42 images per region and age. A1 has none, since its 9 labelled images are all DAPI.
4. **Position check (problem 4):** `samples.json` ("individual sections are not tracked") is now printed and cited.
5. **Unchecked scales (problem 5):** a new `metadata_error` finding records that none of the 26 placed fields is at its stated scale. Three images classed 200X have at least twice the stated pixel size: the cochlear nucleus field of mouse 0136 and the PRNc fields of the p14 mice BrTNR and LTN. This matters for fig7b, whose ">40 µm" giant-cell test needs a known scale. I narrowed the older finding about magnification to what the nucleus check supports.
6. **The extra mouse (problem 6):** it cannot be identified, because the paper gives no mouse identifiers.
7. **Section C:** the 21 follow-up subfolders that name no region are listed by magnification and stain.

**Other changes:** the helper `amyloid.py` has new functions for the blocks, the matching and the spot count. `matplotlib` is added to the requirements and the lock file is regenerated. The notebook header, summary, entry `README.md` and `entry.yaml` are updated, and the runtime is now 11 minutes.

**Not done:**
- The verifier reported no place where the claims file misreads the paper, so I added no questions file.
- I did not commit or push, as instructed.

Saving the attempt record reformatted the whole file, so its diff is larger than the content change.
