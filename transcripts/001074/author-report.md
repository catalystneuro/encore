I did steps 1 to 5 and the handover (step 6). The entry runs from a clean environment and passes its checks, and the claims file still passes the quote checker (47 claims, 0 problems). Nothing was committed.

## 1. Outcomes

12 claims tested (11 of the paper's plus one link claim I added); 35 blocked.

| Claim | Outcome |
|---|---|
| link-revision-well-order (link, added by me) | reproduced |
| fig1c-cells-per-gel | reproduced (reading b only; assumed) |
| fig1g-sensor-yield | partially reproduced (assumed) |
| fig1g-all-ten-sensors-respond | partially reproduced (assumed) |
| fig1h-crosstalk-pairs | partially reproduced (assumed) |
| table1-ec50-on-target | not reproduced (assumed) |
| table1-ec50-off-target | not reproduced (assumed) |
| table1-peak-dff-morse | partially reproduced (assumed) |
| fig1j-ec50-consistent-across-probes | not reproduced (assumed) |
| figs3e-tau-on-under-one-minute | reproduced (assumed) |
| figs3f-depth-delay | not reproduced (assumed) |
| figs2f-cells-tracked | reproduced |
| fig1d, fig1f, methods-revision-probe-stability, figs2c, slices-probe-stability, figs6ef, fig4-ex-vivo-elevations, fig4-ex-vivo-two-orders-lower, figs6j, fig5gh, fig6, fig6c, figs6a (13) | blocked, data_missing |
| 16 slice claims, fig3df, fig3g, fig3h, fig4-ip-csf-concentrations, fig5ab, fig5cd (22) | blocked, metadata_insufficient |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.260928.0807, the most recent. The paper cites no version, and all three published versions hold the same 713 assets with the same blobs.

**What the dataset holds.** Only CaImAn traces and 3D masks. It has no sensor labels and no well, wash-on, injection or stimulation times. That is why the slice and in vivo claims are blocked.

**Findings about the dataset:**
- The timing metadata are placeholders: 30 Hz, every file starting at 0, the same session start (2023-01-01). The indicator is given as "OGB-1". The paper's code uses 31 frames per minute (52 for some 2023 recordings).
- The image masks are stored scrambled: Fortran-order data written into a C-order array. I reordered them for every depth measure.
- 67 files belong to an unnamed subject "0"; 16 of them repeat named files.
- The 250918-SL1ZS5 slice and wells001 files are identical.
- The matched-file suffixes of probe 20230922-PL28 do not fit their pairs.
- The 251119-ZS16 matched pair has 143 cells against 142.
- The accepted and rejected flags are all false.
- Masks have 15 to 26 planes, where the Methods describe 30.

**Outside input.** The well order and mixture concentrations come from the paper's code (pkalugin/kalugin-et-al-morse at commit fa4526a). I marked the nine dependent claims `data: with_labels` and added the link claim to their `depends_on`. I did not change any statement, expected value or criterion.

**Assumptions:**
- The sensor labels come from the Methods' clustering without the code's hand corrections, so the labelled cells are not the paper's 506.
- The dose-response normalization follows the code's baseline and peak wells.
- tau-on uses the claims file's Table 1 constants.
- Depth orientation is taken from the code.
- Gel thickness is read as the imaged z range.

**Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
1. Which hand corrections were made to the sensor clusters, and why?
2. Which background windows and wells were used for the dose-response fits, and is the code's noise cut part of the published fits?
3. Is the deposited plane index the code's z?
4. How were the 30 s artefact decay and the background-fit windows chosen?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Outside data the claims file does not name as data.** The protocol allows outside data only when the claims file says the paper relies on it. The claims file cites the code only for methods, but the well order is needed to label the frames. I treated it as `with_labels`, following an earlier claims file (000351) that does the same.
2. **Link claims and `depends_on`.** The protocol says the author writes link claims and that dependent claims list them, but changing another claim's `data` field is not addressed. I set `data` and `depends_on` on the dependent claims and left their statements and criteria alone.
3. **When a link criterion is written.** Criteria are meant to be fixed before the analysis, but the protocol does not say when an author-written link claim's criterion is fixed. I wrote it after seeing the frame counts and recorded that as a deviation.
4. **Readings the author makes.** The claims file's SENSOR IDENTITY procedure needs choices the Methods leave open. I ran two labelling readings (pooled, and pooled plus per probe) and reported both. The rule "record the first reading the criterion lists" does not cover readings the author constructs, so I recorded reading (b), the one closest to the code.
5. **Time budget.** Surveying all files by metadata only took about 9 minutes. That makes the notebook 12 minutes, over the 10-minute aim, with no way around it for a full survey.

## 4. Runtime and failures

The notebook takes about 12 minutes: 692 s and 701 s in the two clean runs, 9 of those minutes for the 713-file survey. The run finished at 07:20 UTC, well before the 10:11 deadline. Nothing failed.

I did not attempt the LC slice claims using the code's hand-set frames, or the ten-sensor in vivo yield, whose code mixes recordings at two frame rates and hand corrections. Both are recorded as blocked, metadata_insufficient.

Files are in `entries/001074-kalugin-2026/`:
- reproduce_kalugin_2026.ipynb
- morse.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

Elsewhere:
- `attempts/001074-kalugin-2026-01.yaml`
- `claims/001074/10.1016-j.neuron.2026.07.008.yaml` (edited)
- `executed/001074-kalugin-2026/handover/` (the verifier's package)
