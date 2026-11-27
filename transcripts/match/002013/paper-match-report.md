I judged the one paper `primary`. `papers/match/002013.yaml` passes `python tools/paper_match.py validate`.

**doi:10.1021/acschemneuro.5c00071**, "Microinvasive Probes for Monitoring Electrical and Chemical Neural Activity in Nonhuman Primates": **primary** (`by: agent`).
- **Deciding evidence:** the paper's data statement says "Data used in this study are available at zenodo (https://doi.org/10.5281/zenodo.14826579)". The dataset's description says it "includes the processed data published on Zenodo (https://doi.org/10.5281/zenodo.14826579) together with the raw recordings from which they were derived."
- **Why the checks left it open:** they flagged three other Zenodo records. The first, 14826579, is this same data. The other two, 10955583 and 10397773, are the paper's MATLAB analysis code, not data.
- **Supporting evidence:** the monkeys, sites and sessions match. The paper's figures use monkey T sites c8dg (483 days after implant) and c3bs-c3a (496 days after implant), plus monkey P. The dataset has monkeys P and T, with FSCV from c8dg on 09/13/2024 and electrophysiology and beta-band LFP from c3bs/c3a on 09/26/2024.
- **Gaps:**
  - Results on how the probes were built and tested in saline are not in the dataset.
  - One figure also shows a neighbouring site, c8ds, which the dataset description does not mention.

  Neither changes the verdict, since the in-animal findings rest on the data the paper names.
