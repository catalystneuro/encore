The file is ready for an attempt. I made seven corrections and noted three open problems in the new `checks` entry, and the checker still passes.

**Checker result line** (same before and after my edits): `claims/001272/10.1016-j.xcrp.2025.102660.yaml: 19 claims, 19 quotes, 7 statistical values, 0 problems`

**Changes, by claim**
- **figs1-effects-same-as-fluovolt**
  - I removed the expected value of 57.7 V/cm. The paper does not base the Di-8-ANEPPS comparison on that number. It is now a reported check on the FluoVolt reference group and is not judged.
  - The claim now fails on a difference in either direction. Before, only a higher Di-8-ANEPPS threshold failed it, but the paper says only "not different".
  - The criterion now says that comparing thresholds is the reader's reading of "not different". The paper names no measure or test for it.
- **fig2-modulated-locks-to-beats:** the 12.5 to 37.5 ms window assumed each beat peaks 25 ms in. That is now sourced:
  - the Results describe five 50-ms beats;
  - the Methods say the modulated waves begin and end at minimal amplitude;
  - the dataset's stimulus record takes precedence when it gives the envelope.
- **fig4-orientation-and-poles:** I noted that the Figure 4 legend gives different p bounds and test types (both p < 0.01, one paired, one unpaired) from the Results' p < 0.001 and p < 0.01 for the same comparisons.
- **fig6-sine-less-than-pulse:** I named the DANDI:001274 claim ids that its criterion defers to.
- **Header F1:** the Methods say the inverted scale is in "Figure S2", but that is the Di-8-ANEPPS figure, S1. I noted that it is read as S1.

Everything else matched the paper: the statements, sources, statistics (all results, none of them thresholds used to count units), expected values and tolerances. Every main finding has a claim, and all of them come from this paper only.

**Open**
- **figs1-effects-same-as-fluovolt:**
  - It still rests on a threshold comparison the paper does not name.
  - The FluoVolt neurons it compares against come from dandisets matched to figures by title only.
  - The Di-8-ANEPPS fields were tested in a random order, not searched for a threshold, so the measured threshold is only an upper bound.
- **fig1-pure-sine-excites-all:** the statement includes an excitation block at the highest fields, but the criterion only reports it. The paper gives no fraction of neurons that would let it be judged.
- **Figure S1 claims:** the paper describes Figure S1 only in words, so these criteria use standard choices (majority rules, the 75% cutoff, Spearman correlation, time windows, AP width limits). Each one is labelled as a standard choice.

**Ready:** yes (`ready: true`). Nothing is committed or pushed.
