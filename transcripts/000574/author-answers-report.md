The reader answered one question, on `neurons-recorded`. I re-ran every claim that groups neurons by region under the amended criterion; no outcome changed. The entry checks with 0 errors, all three notebooks pass from a clean environment (20, 13 and 14 minutes), and the handover is built in `executed/000574-boran-2019/handover/`. Nothing is committed.

**What the answer changed.** The claims file now takes a unit's region from the tip contact of its electrode, under two readings: (a) the anatomical label updated after visual inspection of MRI, and (b) the Brainnetome label. The electrode name becomes only a variant.

- **Which contact is the tip.** Contact 1, because it lies nearest the midline in every bundle.
- **Where the labels come from.** The dandiset holds one label per contact. The G-Node deposit of the data descriptor flags the labels that were entered by hand.
- **Reading (a)** is the dandiset's own label. Those flags show that the dandiset's labels are the updated ones, and they are what the previous run used. So the existing numbers stand as reading (a).
- **Reading (b)** cannot be fully computed. Four tip contacts were labelled by hand, and their original Brainnetome label is in neither deposit. Two of them carry units (19 in subject 7, 6 in subject 9), so reading (b) leaves those 25 units out.

**Changes to the claims file and entry**
- I added a link claim, `electrode-labels-gin`, which compares the dandiset's electrodes with the G-Node deposit. It is reproduced: all 502 contacts match, with identical labels and coordinates, and 4 are flagged as entered by hand.
- I marked the region claims `data: with_labels` and made the top-level ones depend on the link claim. I did not change any statement, expected value or criterion.
- I added a third notebook, `reproduce_boran_2019_regions_b.ipynb`, for the decoding and dPCA claims under reading (b); adding them to the main notebook would have taken it past the 30-minute limit.
- The helper now fetches the G-Node labels, and the attempt record lists the deposit under `inputs`, with a new finding that the dandiset lacks the hand-entry flags.

**Outcomes, before → after**

| Claim | Before | After | Note |
|---|---|---|---|
| electrode-labels-gin (new) | – | Reproduced | |
| neurons-recorded | Not reproduced | Not reproduced | Counts are now 640/421/398 under (a) and 615 hippocampal under (b), where before they were by electrode name (446/456/585); paper 676/449/401, and 1487 units against 1526 |
| fig2b maintenance neurons | Reproduced | Reproduced | (b): 20.5%, chi-square 47.93 |
| fig2c load-dependent | Reproduced | Reproduced | (b): 22 of 122 |
| fig3e probe neurons, entorhinal | Reproduced | Reproduced | (b): chi-square 14.11 |
| fig3 probe onset not movement | Reproduced | Reproduced | |
| fig3 few task-specific | Partially reproduced | Partially reproduced | |
| fig4a dPCA | Not reproduced | Not reproduced | (b): 32.7% |
| fig4b speed | Partially reproduced | Partially reproduced | |
| fig4c distance | Reproduced | Reproduced | (b): significant with both 200 and 2000 runs |
| fig4d encoding decodes correctness | Not reproduced | Not reproduced | |
| fig4e workload decoding, and its leave-one-subject-out, maintenance-neuron and 6-vs-8 claims | Reproduced | Reproduced | (b): 81.4% |
| fig4f retrieval decoding | Not reproduced | Not reproduced | See below |
| figs3d hippocampal loadings | Reproduced | Reproduced | |
| fig5 subject 1 neurons | Partially reproduced | Partially reproduced | Same neurons under (b) |
| sfc (spike-field coherence) | Partially reproduced | Partially reproduced | Same 73 neurons under (b) |

**One judgment call to review: fig4f.** Under reading (b), the main run puts all neurons at a corrected P of 0.048, the smallest the reduced run count allows. Taken alone, the criterion would count that as one significant population and make the claim partially reproduced. Re-running the same decoder with three other random seeds gives corrected P of 0.10 to 0.62 under both readings. So I treated that one significant run as resampling noise and kept not reproduced. The record states this as a deviation, so the verifier can disagree.

I also fixed some conclusion text that had been cut off mid-number in the notebook and the record.
