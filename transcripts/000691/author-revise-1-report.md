I answered every point in the round-1 report and re-ran all seven notebooks; all passed within the 30-minute limit. No outcome changed. The only change of status is the reason for one block: fig2d-lman-sparse-bursting is now blocked as `methods_underspecified`, which is what its criterion says, with the missing data recorded in the notes. Round 1 is recorded under `verifications` for the 22 claims the report covered. Nothing is committed.

**Where I kept an outcome the verifier disagreed with**
- **fig2-quadrant-direction-decoding and ed9b-octant-decoding:** the verifier would call these reproduced on the n1 null alone. I kept them blocked (`not_runnable`) and recorded the disagreement. The criterion judges p under both null readings, and the full n2 null needs about 34 hours. I ran 9 n2 null decoders per claim, and all lie far below the real decoders: 0.089 to 0.145 against 0.437 for quadrant, 0.109 to 0.149 against 0.326 for octant. But 9 cannot show p < 0.001, so calling it reproduced would rest on my own guess that the full n2 null would agree.
- **fig2k, fig2l, ed9c:** the verifier wanted the reason for these blocks to be `other`. I kept `not_runnable`: the full runs are measured at 4.5 to 12.8 hours on four cores, against 30 minutes per notebook, which is the protocol's case for `not_runnable`. That disagreement is recorded too.

**What I added**
- **Is the motion movie raw (ed7-motion-small)?** The values say it is. The histogram of its counts has the uneven raw-sensor pattern in every block (roughness 0.740 to 0.745). Shifting frames by 0.13 px and saving them back as integers, as a motion correction would, smooths that to 0.052. Its zero values are at most 2 isolated pixels per frame, not strips at the frame edges. I also added a known 0.13 px jitter to the first 1200 frames; the registration recovered it (correlation 0.996). The outcome stays not reproduced and is no longer tentative.
- **PSF fits:** I added readings that use, for each bead, whichever of the two fits has the lower error, plus a table of the Kiloscope's centre and edge beads with both fits. The Featherscope result is unchanged. The Kiloscope is still partially reproduced: no reading meets the criterion, and the width is larger at the edge than at the centre under every reading. The 27.77 µm edge bead keeps its main fit because that fit has the lower error.
- **ed2b/ed2c:** a cell prints the lines of each `analysis.m` that load the images; they are the same files used in the notebook, in the same roles.
- **ed8:** I added counts with the quarters split at the image midlines. The result is the same, 8 of 8 events under one reading of the event times and 7 of 8 under the other, so it stays `methods_underspecified`.
- **Decoding:** each real decoder's 200 single fits are now compared with the single-fit n1 null on equal terms. For quadrant, 2 of 200 real single fits are at or below the largest null value; for octant, 11.
- **Reduced runs** of fig2k, fig2l and ed9c are in a new notebook, `decoding_reduced.ipynb`. They use far fewer fits and grid points than the criteria and decide nothing.
- **Other changes:**
  - The Kiloscope's unconfirmed image order (72%) and the near-circular field-of-view test are now in the record.
  - The fig2d entry in the notebook table, summary and README now matches the record.
  - The PSF and illumination conclusion cells now begin "**Result:**", so the handover tool would remove them.
  - Run times and costs are updated from the new run, and the README and `entry.yaml` list the three new notebooks.

**Things to know**
- **The Kiloscope centre value moved.** Under reading (a) it is now 4.467 µm, against 4.422 µm in the run the verifier saw. The fits are repeatable on this machine but differ slightly between machines, which the record now says.
- **`entry.py all` stops at the check step** with 11 errors, all in the deprecated `-01` record, which I left unchanged; the previous run hit the same errors. I ran the notebooks with `entry.py run` instead.
- **The run was split in two.** The 2-hour command limit cut it during the seventh notebook, so I ran `decoding_reduced.ipynb` separately through the same `run` code.
- **Text-only edits to the executed copies.** After the run I copied the revised conclusion text into the executed notebooks; their code cells are identical to the committed ones.
- **ed3-adc has no round-1 result.** The verifier's report gave no outcome for it, so it is left out of the results and the `reviewed` text says why.
