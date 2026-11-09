I've worked through the round-2 report. No outcome changed and nothing is proposed for round 3: the verifier agreed with all 20 outcomes, and nothing I found argues for a change. `python tools/entry.py all entries/crcns-pag-2-moaddab-2020` passes (0 check errors, notebook runs in 68 s), and the round-2 results are recorded under `verifications`. Nothing is committed.

**Assumption flags**
- I removed `assumed: true` from fig5abc and figs4. The claims file's own readings give the same outcome for both, so neither rests on the adopted reading. The README rows, the summary table and the false summary sentence about S4 are corrected.
- fig5d keeps its flag. Its justification is now printed: the data check shows the script's regression lines (2149, 2150, 2162 to 2171), where `fire.z.s1.interval` is regressed on `cer.cue`. The earlier citation "lines 2161 to 2170" was off by one and is corrected.

**Text the outputs did not support**
- **fig6 notes:** the EAA safety p range is now 0.0084 to 0.040.
- **fig7:** "strongly" is replaced by the actual range, r = 0.35 to 0.73, p ≤ 0.015.
- **fig7, first 5 s:** the statement now says it was tested under the adopted reading. I also ran the first-5 s window under all twelve readings and both normalizations. Every part holds with firing (b) or (d), with one exception: (b) with empty trials set to 1 fails the safety part under the Methods' normalization. It fails with (a) and (c). The notebook, notes and summary say this.
- **fig7, script windows:** the claim that the script computes cue-inhibited firing only over the first 5 s and the whole cue now cites printed lines 2796 to 2817.
- **Storage windows:** the data check now prints how far around each cue onset spikes and nose pokes are stored. 99.98% of spikes and 99.99% of pokes fall between 20.5 s before and 33.5 s after an onset. The notebook text and the finding are corrected to match.
- **"Fixed before the outcomes were seen":** removed from the notebook and the record, since no output can confirm it.

**New check on the design that is not of full rank**
- One cue-inhibited neuron (mh38101617epr38bSPK05a) comes from a session where the rat never poked during any cue. That makes its design rank-deficient, so the Python fit and Matlab `regress` give it different betas.
- I added a Matlab-style fit to `pag2.py` and re-ran Figs. 5E to G, S4, 7 and S6 under the adopted reading in a new notebook section. That neuron's fear output betas become 0, Fig. 5E to G gives F = 2.14, p = 0.024 and t = 2.30, p = 0.023, and no outcome changes. It is recorded as a deviation.

**Not done**
- The paper's smaller degrees of freedom (about 13 cue-excited neurons unaccounted for) stay an open question for the authors. No exclusion rule was found; the script's `deleteThisSlice` steps only drop the empty slices of the per-class arrays.
- No question was added to `questions/crcns-pag-2.yaml`, because the verifier found no place where the claims file misreads the paper.
- The verifier's own round-1 r range for fig7 (0.56 to 0.73) is left as it gave it; the round-2 entry records its correction.
- The working tree has untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others) that I did not create; I left them alone.
