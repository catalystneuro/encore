I finished steps 1 to 6 for fedele-2017: the notebook ran clean from a fresh environment in 37.8 minutes, `entry.py check` gives 0 errors, and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| table-s1-link (link claim I added) | reproduced |
| cohort | partially reproduced |
| table1-nights-intervals | reproduced |
| hfo-amplitudes | reproduced |
| followup-not-different | reproduced (only on Table 1's values) |
| table-s1-rates | reproduced |
| fig1-patient4 | reproduced |
| frandr-area-resection-per-patient | reproduced |
| ripple-fr-area-resection-per-patient | partially reproduced |
| table2-frandr-prediction | reproduced |
| table2-ripple-fr-prediction | partially reproduced |
| frandr-more-specific | reproduced |
| engel-prediction | reproduced |
| ete-soz-not-resected | blocked, data_missing |
| fig2-patient17 | partially reproduced |
| fig3-patient1 | reproduced |
| test-retest-group | partially reproduced (assumed) |
| test-retest-by-group | reproduced (assumed) |
| spectral-classes | partially reproduced (assumed) |
| spectral-tle-ete-no-difference | not reproduced (assumed) |
| tp-patients-hfo-area-location | blocked, metadata_insufficient |

The main numbers behind these:
- **Rates and areas:** 98.1% of Table 1S's channel rates match. All 60 Table 1S HFO areas match exactly. The FRandR resection agrees with Table 1 for all 20 patients, and every Table 2 FRandR measure is the paper's.
- **Ripple and FR misses:** they all come from the paper's own Table 1S and Table 1 disagreeing for patients 1, 7, 11 and 15.
- **Test-retest:** the lower quartile over interval pairs is 55% against the paper's 67%.
- **Spectral:** the selected channels hold 20,421 FRandR events, not 6,182, and no reading gives the paper's class shares.

## 2. Dataset, assumptions, questions

**Pinned version:** "unversioned" (CRCNS data sets have no versions), with the DOI 10.6080/K06Q1VD5. All 20 file MD5s are in the notebook header and match `checksums.md5`.

**What the data set holds:** 92.5 GB of MATLAB v5 files inside tar.gz, streamed once; nothing was written to disk. It has 20 patients, with nights and intervals exactly as in Table 1. Event timing matches the signal in every patient: 94% of ripples and 98.5% of FR have more band power at the marked time than 1 s later.

**Findings about the data set:**
- It holds no outcome, follow-up, epilepsy type, resected channels or seizure onset zone, although its title names the surgical outcome.
- 93 of 385 intervals are not 5 minutes long (204 to 720 s), contrary to the data description.
- The unit of the signal is not stated; the values fit microvolts.
- 745 events end after the last sample of their interval.
- Every FRandR event is also listed as an R and an FR event with the same start and end. The description does not say so.
- The electrode schemes do not give the brain region of each contact.

**Inconsistencies in the paper:**
- Table 1S lists patient 14's 15 excluded channels under patient 11.
- Table 1S and Table 1 disagree on whether the area was resected for patients 1, 7, 11 and 15.
- The Methods cap intervals at six per night, but 14 patients have more, up to 16.

**Assumptions:**
- I pooled rates as all events over the total recorded time. Of the three pooling readings this matches Table 1S best.
- For test-retest I used FRandR rates with a separate permutation null for each interval pair. This puts 17 of 18 patients within 0.1 of Table 1.
- The spectral fit settings are my choices. All ten readings are shown in the notebook.

**Questions for the paper's authors** (filed as `methods_unavailable` findings): which HFO type and which null produce Table 1's test-retest values; and how the 6,182 spectral events were selected and how the spectrum was fitted.

**Questions to a reader:** none.

## 3. Protocol gaps

1. The data are tar.gz, not zip, so they cannot be opened in place as docs/archives.md describes. I streamed each file once, in parallel, using Python's tarfile in stream mode.
2. The protocol does not say how to label claims that need non-measurement data from the paper itself (resected channels, outcomes). I added a `kind: link` claim, `table-s1-link`, and added it to the `depends_on` of five claims. I also listed Table 1 and Table 1S, fetched at run time and checked by MD5, under `inputs`.
3. The rule against embedded data conflicts with needing about 600 reference values from the paper. The notebook fetches the supplement and the Europe PMC full text at run time and parses them.
4. Some claims can only be tested on the paper's own table (follow-up) or are partly about the patients (cohort), and the protocol does not say how to count these against the dataset. I followed the criteria and said in the notes that these test the paper's table, not the data set.
5. For several claims the criterion only defines "reproduced". Where part of the result held, I used "partially reproduced", following the protocol's general definition.
6. The time rule assumes analysis is the bottleneck. A single full pass over the data already takes about 20 minutes, which constrains how much can be developed on the whole data set.

## 4. Runtime and failures

- **Runtime:** the full scan took 15 minutes in development and 20.5 minutes in the CI run; the whole notebook took 37.8 minutes.
- **Lost hour:** a local development script hung for an hour because it lacked the `__main__` guard that spawned worker processes need. The notebook itself is not affected.
- **Formatting slip, fixed:** a bold-removal edit briefly stripped the "**Result:**" openers. I restored them.
- **Executed copy:** after the run I edited only markdown cells, and patched the same text into the executed copy, so its outputs come from that one run.
- **Spectral fits:** 180 to 470 fits per reading did not converge. They are classified from their last estimate.
