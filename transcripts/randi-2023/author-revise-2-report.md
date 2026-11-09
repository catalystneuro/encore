I worked through every point in the round-2 report. No outcome changed and nothing is under `proposed`. The verifier agreed with all 19 outcomes, and I found no reason to propose a change. `python tools/entry.py all entries/001075-randi-2023` passes: the check reports 0 errors and the notebook ran in 634 s.

**Text the printed numbers did not support**
- **Cell 38, sourcedata-link:** "Every variant falls in the partial band" was false. It now says the filter and exported-assignment variants are in the partial band, and the variant that keeps only detected responses (36.0%, 0.471, 0.458) falls below it.
- **edfig2ij deviation in the record:** now says readings (a) and (c) are within tolerance and (b) is not.
- **0.616/0.617, 0.675/0.676, 3,172/3,173, 59/58, 54/53, 10,161/10,160:** the re-run prints exactly the numbers the text already gave, so I kept the text. The verifier's copy came from an earlier run whose counts differ by one and whose correlations differ by 0.001. My guess is floating-point differences in the photobleaching fits; I did not confirm that. The Summary now states this difference, and I added that no conclusion depends on it.
- **osf-link link to subjects 20, 23, 33:** cell 32 now prints the session ids of the three subjects that have only imaging files. They are exactly the three unmatched export keys, so the notes are now backed by output.
- **Subject 11, 200 vs 201:** the side-by-side line now drops the export's trailing empty label entry, as the other line does, and prints 200.
- **README:** the run time now reads "10 to 15 minutes" (this run took 627 s, the verifier's 919 s). The blocked row now names Extended Data Fig. 7b, so it no longer clashes with the reproduced fig4-rid-unc31 row.
- **Cell 12:** now matches the new output, so I left it as it was.

**Output added for edfig6-kernel-stereotypy**
The verifier noted that no cell showed the failed install. A new section before the Summary now tries to build the paper's `pumpprobe` package and the three packages it imports, at fixed commits, in a temporary environment. The result:
- As published, pumpprobe does not build because the compiler cannot find the numpy headers.
- With the headers added by hand it does build, which the old notes did not say. It still cannot be imported, because none of the three packages it imports builds:
  - mistofrutta fails on its version string;
  - wormbrain needs the Eigen library;
  - wormdatamodel uses numpy C API names that numpy 2 removed.

I rewrote the edfig6 notes to match this output. The cell needs `uv` and access to GitHub when the notebook runs.

**Recorded in the attempt record**
The round-2 entry under `verifications` covers all 19 claims, with the verifier's reasons in its own words and my responses.

**Not done**
- I did not reimplement the kernel fits without the paper's package. The verifier pointed this out, and the edfig6 notes say it. It would be a new analysis, so it belongs in a later attempt.
- I made no change for fig4-rid-unc31 being met only barely. The notes and conclusion already give the single WT trial, the p values and the comparison with the WT export.
- There are untracked dotfiles in the repo root (`.bashrc`, `.idea` and others) that I did not create; I left them alone.
