No outcomes changed. The verifier agreed with all 8 recorded outcomes in round 2, and I found no reason to propose a change, so nothing is filed under `proposed`. I re-ran `python tools/entry.py all entries/000005-yu-2016` after the last edit: the check reports 0 errors and the notebook passes in 201 s. All the claim numbers are the same as before.

**Text corrected (report section 2):**
- **Other cells (cell 16):** 85, not 80.
- **Sampling rate (cell 8 and the record's finding):** 10 kHz up to March 2015, with 5.2 or 5.5 s trials; 20 kHz with 5.9 s trials.
- **Whole-cell cells without a touch input (cell 25):** the three mice hold 9 whole-cell cells. 8 were tested and lack a touch input; one in anm318532 was never tested.
- **Summary, `exc-mainly-touch`:** it now says the selectivity test passes without the flagged mice (p = 0.024 and 0.038) but the outcome stays not reproduced, because the flag comes from touch responses.
- **Summary, ION-transected cells:** cells from these mice "may be" in both groups, and the inferred-transected mice contribute 3 excitatory and 4 included FS cells. I softened the same overstatement in the README and in the record's ION finding.
- **Juxtacellular variant (cell 40 and the `fs-suppress-movement-spiking` notes):** both now repeat the claims file's caveat that this selection is biased toward a rise and does not decide the outcome.

**Outputs added for statements nothing printed:**
- **Draft versus pinned version (cell 3):** the pinned version is the only published one, and the draft has the same 148 asset paths and sizes.
- **Whisker trial length (cell 9):** the whisker samples cover 5.0 s per trial in all 140 files.
- **README run time:** I replaced "about four minutes" with the load time the first cell prints (121 s).

**Metadata search (report section 3):** the helper module now collects every text value in each file: the session and experiment descriptions, the keywords, the optogenetics sites and the rest of `general/`. Cell 5 searches these as whole words for ION, infraorbital, nerve, transection, lesion, cut, surgery, sham and control. No file matches any of them, and all 130 L4 files have the same keywords. The blocked reason stands.

**Record:** round 2 is under `verifications`. Each claim has the verifier's reason in its own words and my response. The text corrections that don't belong to one claim are listed in the response for `sensory-input-drives-fs`.

**Not done:**
- **ION-cut and L5 cells in the groups, and the possible untaggable whole-cell FS cell among the excitatory cells:** the files cannot settle either. The record already says so, and the 0.7 ms width variant keeps the outcome.
- **The selectivity index for cells with few spikes:** I left the measure as it is. Its weakness is already reported, and changing it would need a new analysis.
- **The supplement under `paper/`:** I downloaded no paper text, and there is no `paper/` directory in this checkout, even though the verifier says it saved the supplement there.

As instructed, nothing is committed.
