I checked the claims file against the paper and fixed seven claims. It is ready for an attempt.

**Checker:** `23 claims, 23 quotes, 3 statistical values, 0 problems`, both before and after my edits.

All quotes, sources, statements and expected values match the paper. The three p-values (all p < 1e-5, Figure 4B) are results, not thresholds used to count units. Every main finding has a claim (Figures 3 to 8, Figure 10, Table 1, the methods facts), and none comes from outside this paper. I cloned the paper's code at the commit the file cites (24e8e61) to check what the criteria say about it. Two of those statements were wrong (fig78b, fig10).

**Changes, by claim:**
- **mea-electrodes-and-rates:** Methods 5.2 say APWaveform was recorded at "typically 200 kHz", so the patch-rate check now accepts 20 or 200 kHz for APWaveform.
- **fig3b-ap-initiates-distal-ais:** the protocol (IDrest 300%, averaged spike cutouts) now comes from the code. Timing the spike start by the −20 mV crossing was not in the paper; it is now one of two readings, with the AP peak time as the other.
- **fig4b-extra-better-than-soma:** the paper does not say which pairs the Holm correction covers. The two readings are the three soma comparisons, or all six pairs as the code does.
- **fig4d-templates-better-than-soma:** the code normalizes each channel differently from the legend's peak-to-peak (it uses the range of the absolute values). Added as a variant.
- **fig78a-soma-intra-all-extra:** the criterion used the code's rheobase settings (fractions 0.4 and 0.2, tolerance 30) as the method. The main result now follows the Methods (majority of recordings, 10% tolerance), with the code's settings as a variant.
- **fig78b-validation-spiking:** the file said the code plots the best extracellular seed. The notebooks that make Figures 7 and 8 use the best intracellular seed, as the legends say. Corrected.
- **fig10-cell2-soma-underestimated:** added the code's recording positions, protocol (IDrest 250%) and electrode choice. The code passes the soma model's parameters while the paper names the all model; the all model is the main result and the soma model a variant.

**Still open (recorded in the check entry):**
- In fig4d and fig78b, "almost all" and "main features" have no definition in the paper. The criteria use two readings each, and the outcome needs them to agree.
- For fig10, neither the paper nor the code says how the model and recorded time axes are aligned. The criterion lines both up at 2 ms before the peak.
- For fig4b, the paper names post hoc Mann-Whitney tests but gives no omnibus test and does not say one- or two-sided. Two-sided is used.

The check entry is at the end of the file with `ready: true`. Nothing was committed or pushed.
