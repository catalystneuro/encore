No outcome changed. Round 2 doesn't allow it, so I proposed three changes under `proposed` for a third round to review. The entry re-ran cleanly (`tools/entry.py all`: 0 errors, all three notebooks pass), and the final run's outputs match the previous run's. Nothing is committed.

**Proposed outcome changes**
- **fig2c-subclass-ephys-differences: partially reproduced → reproduced.** The verifier asked me to check the "rheobase + 40 pA" sweep. The index is correct: the 6 cells it flagged are IPFX's own fallback, which picks a lower sweep when no sweep passing QC lies 39 to 61 pA above rheobase. In 7 of the 9 fallback cells that disagree with the paper, the paper's value comes from an in-range sweep that fails only the Methods' 500 ms noise criterion (rms below 0.5 mV) as measured here.
  - I added a variant (a') that extracts the features without that criterion. It brings 38 of the 39 computed features closer to the paper's values. Under it the initial firing rate has FDR p = 3.9e-9, below the claim's 1e-7, against 4.7e-7 with the criterion.
  - The proposal would rest on that choice as an assumption. I added a finding that asks the authors how this noise was measured.
  - No other claim's outcome changes under (a').
- **fig2c-lamp5-gradient and fig6a-ephys-dprime-subclass-structure: partially reproduced → not reproduced.** I agree with the verifier: their criteria name no partial level, the rule already applied to three other claims. Both disagreements are recorded.

**Added**
- A table of the 16 fallback cells, showing values with and without the noise criterion, and a per-feature comparison with the paper's values.
- Variant (a') in every reading loop of the human and mouse notebooks.
- A variant using the adaptation ratios computed here, for figs3a, fig6d and fig3g. No outcome changes: figs3a gives R2 0.20, fig6d stays within tolerance, and fig3g still holds.
- A printed fig2c breakdown of the 28 disagreeing cells, and the session-id check behind figs8b.
- A question for a reader on fig5d, whose criterion compares against L1 VIP although the paper makes no such comparison. The claim itself is unchanged.
- The round-2 entry under `verifications`, with all 41 claims (39 agree, 2 disagree).

**Corrected**
- Agreement figures: the 39 features used agree for 53 to 98% of cells, the five ratios left out for 4 to 37%, and the Spearman range is 0.886 to 0.997.
- The strict set left out of the dandiset is 50 Amsterdam and Szeged cells plus 12 Seattle cells that failed feature extraction, not "62 Amsterdam and Szeged cells". I removed the unprinted "136".
- The figs3a description: reading (a) uses the paper's ratio with sag computed here.
- fig6d's figures on the paper's values alone, and "38 features" for the four mouse claims.
- PLACEHOLDER is in the paths of DANDI 000337, not 000228 (record and question both fixed).
- Morphology counts are now 78 and 71, matching the outputs. The voltage-clamp sentence in the notebook header is fixed.
- README run times are now about 20 and 10 minutes, and the table gains rows for fig3e, fig3f, fig1e, fig3b and fig6b.
- The fig2b round-1 wording is clarified. The round-1 reasons for 11 not-attempted claims are now in the verifier's words.

**Not done**
- I did not search other public mouse patch-seq metadata for fig1e, which the verifier noted as unchecked. Its outcome is kept.
- The 50% rule is not marked `assumed`, because the variants show no outcome depends on it.

There are untracked dotfiles in the repo root (`.bashrc`, `.idea` and others) that I did not create or touch.
