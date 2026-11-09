I've revised the attempt for every point in the round-1 report. One outcome changed, the record's `verifications` now holds round 1, and the entry ran twice from a clean environment with no errors (9 and 21 minutes) and passes its checks. Nothing is committed.

**Outcome changes**
- **table3-destabilizing: blocked → not_reproduced.** The verifier said I-Mutant and MuPRO could have tested 2 of the 5 tools, so I ran both on the web servers the paper names, from sequence as the criterion says.
  - I-Mutant 2.0 gives a positive (stabilizing) ΔΔG for 4 of 5 variants. For p.Cys1019Tyr and p.Leu249Phe the sizes are Table 3's (0.14, 0.55) with the sign reversed. Its sign classifier also calls p.Asp423Glu stabilizing.
  - So "every tool gives a negative value" fails on a tool the paper names. The other 15 values (mCSM, SDM, DUET) are not computed because the structural models are not deposited.
  - MuPRO matches Table 3 for 3 of 5. Table 3's p.Cys1019Tyr value is the one MuPRO gives for p.Leu249Phe.
- **The two residue-contact claims** stay blocked, with the reason changed from `not_runnable` to `data_missing` (models not deposited), as the verifier gave it.
- **m73-vmd-phenotype and m73-f57-similar-lesions** keep their outcome (partially reproduced) but are now marked `assumed`.

**What I fixed or added**
- **Autofluorescence threshold (problem 2, affects a conclusion):** the arrow pixels are now left out of every measure, and each eye is judged under five readings of "bright focus".
  - The one adopted compares the lesion with same-size discs of the panel's own background, which replaces my own 1.1 cut-off.
  - M73's right eye has only a small speck, no brighter than the background (64% of background discs are as bright). Two of the other four readings would count it as bright, so all readings are shown and the reason is recorded.
  - I added a question for the paper's authors on what counts as hyper-autofluorescent.
- **Domains (problem 5, affects a conclusion):** Pfam, SMART and the PROSITE profiles are now each run as a reading. None has a second IMPG2 EGF-like domain: PROSITE places 6 of 7 variants, Pfam and SMART 4. The outcome stays partially reproduced.
- **Table 2 (problem 3):** every value in dbNSFP's per-transcript lists is now shown and checked, and I ran the FATHMM-MKL web server. Neither matches the paper (0 of 5).
- **ClinVar (problem 9):** the notebook now prints the record's HGVS, condition and summary. The entry first appears on 15 March 2021 with condition "not provided", so ClinVar does not contradict the "first association with VMD" half of the claim.
- **Smaller points:**
  - The sex and age checks are now described as true by construction.
  - A pI comparison shows that Asp to Glu moves the pI by +0.003, against +0.02 in Table 4.
  - The notebook now shows the Word document's two images and full-resolution crops around every arrow in Figures 2 and 3. The crops support my earlier readings.
- **Findings:** the Word document finding is corrected (−1.2666 is MuPRO's real value for p.Leu249Phe), and a new finding records the reversed I-Mutant signs in Table 3.
- **Other files:** the helper, README, header and summary are updated, and scipy was added to the locked requirements.

**What I did not do**
- MutationTaster2021 could not be run: its API redirects to its home page even for its own example, as the notebook prints.
- I did not run mCSM, SDM, DUET, DynaMut or a rerun of I-TASSER.
- I did not run ExPASy's own pI code.
- The FATHMM-MKL, MuPRO and I-Mutant servers have no version that can be pinned. They are recorded as inputs with the date they were queried.
- No reader question was added: the verifier reported no place where the claims file misreads the paper.
