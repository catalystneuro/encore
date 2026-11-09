I rewrote `claims/000691/10.1038-s41592-023-01806-1.yaml` from the full text. The quote checker reports 0 problems; nothing was committed.

**Text read:** the version of record (Nature Methods 20, 546–549), from a PDF someone supplied. The extracted text has the main text, figure legends, Methods, the legends of Extended Data Figs. 1–10 and the reporting summary. The supplement is two videos, and no result rests on them. I didn't open the PDF.

**Code read:** FeeLab/Feescope-Paper-Code at commit d596646. It has the position tracking, all the decoders, the NMF and coactive-footprint maps, the receptive fields, the bead PSF fits with their images, and the illumination profiles with their images. It doesn't have the shuffle tests, the significance and Benjamini–Hochberg step for the maps, the Mann–Whitney test, the motion correction, the USAF images or the ADC recordings.

**Claims:** 23. 22 have quotes and 1 is `inferred` (ed9c, the octant map). 3 have statistics (Fig. 2j, Fig. 2k, Extended Data Fig. 9b), 18 have criteria and 11 have expected values.

**What changed from the deprecated file** (also stated in the opening comment):
- **ed9c and ed9b:** they now use the paper's null. Each footprint's trace is circularly shifted by its own random offset, over 1,000 shuffled decoders. For the maps, the null decoders use 32 randomly chosen footprints.
- **abstract-kiloscope-fov:** the expected field of view is now 4.8 × 3.6 mm. The old file had 4.0 mm for the longer side.
- **fig2-quadrant-direction-decoding:** restored. The main text states it: at least three times chance, P < 0.001.
- **Added:** fig1e and fig1f (bead PSF), ed1cf (field curvature), ed7 (motion), fig2k (decoder size), fig2l (quadrant and direction map), birds-singing-rate, fig2d-lman-sparse-bursting.
- **Thresholds dropped:** criteria no longer rest on thresholds the earlier author chose. The old file's criteria were also written after its author had seen the data and a prototype decoder; this one was written without seeing the data.

**Details the paper leaves open, and the readings named:**
- **Object-plane pixel size:** 5.94 µm or 5.35 µm (both from the code). This sets the 270 µm map radius (45 or 50 pixels) and the field of view in mm.
- **Footprint set for decoding:** the Fig. 2 legend fixes the 2,382 curated footprints. The code may in fact use all 2,948, which is named as a variant.
- **Fig. 2j, which accuracy must reach three times chance:** the median of the diagonal, or every diagonal element, at 0.375 or more.
- **Fig. 2k, what the Mann–Whitney U compares:** original against shuffled at each size, or each size against the next.
- **Maps (Fig. 2l, Extended Data Fig. 9c):**
  - random null footprints drawn anew for each decoder, or once for all;
  - the empirical p with or without +1;
  - "substantially different" read as significant and non-significant points both present, and a value range of at least 0.108 (the 0.18–0.30 colour bar, less 10%).
- **Fig. 1e/f, which width is "resolution":** the median major-axis FWHM, the median minor-axis FWHM, or the mean of the two.
- **Extended Data Fig. 2, edge radius:** 0.5 or 0.45 mm (Featherscope), 1.8 or 2.0 mm (Kiloscope). "Flat" has no measure.
- **Extended Data Fig. 7:** how the root mean square of the displacement is formed (three readings).
- **Extended Data Fig. 8:**
  - event times: each component's largest weight, or the code's eight times matched to components;
  - "from across the FOV": active footprints in all four quarters of the field, or their spread compared with random sets.
- **Extended Data Fig. 10:** the footprints were selected by eye. "Localized" is read by entropy or by map peak, each against 100 circular shifts.
- **No method at all:** fig2d (sparse bursting) and ed1cf (field curvature) have no criterion the paper fixes, so they are marked methods_underspecified.

**Missing from the paper:** the pixel size, the event times assigned to components, and any measure for "flat", "substantially different", "across the FOV" or "localized". The curation of the 2,382 footprints was done by eye and can't be redone. One quote is partial: the Featherscope resolution sentence is split out of order in the extracted text, so the quote is its second half (with the 7 µm figure). The first half, with "approximately 4 μm", is given in the opening comment.
