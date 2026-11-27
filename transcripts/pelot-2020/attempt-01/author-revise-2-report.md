No outcome changed. I've proposed one change for a third verification round: fascicles-larger-cervical from reproduced to partially reproduced. `python tools/entry.py all entries/pelot-2020` passes (0 check errors, notebook ran in 228 s), and the text matches the new outputs. Nothing is committed.

**The main finding.** The verifier was right that Kenward-Roger as I had it was not the paper's test. Its degrees of freedom were up to twice the ones implied by the paper's own F and p values. I added a variant of Kenward-Roger that uses the observed information in place of the expected information (in `vagus.py`). It gives the paper's numbers for all nine effects the paper reports:
- F within 0.4% and p to the digits printed. For example, nerve diameter gives 577.0, 11.01 (p = 0.0030) and 2.4455 (p = 0.1085), against the paper's 577.1, 11.01 (0.0030) and 2.445 (0.1085).
- Degrees of freedom within 1 of those the paper implies.
- For fascicle diameter, the exact match needs the rat values the paper's code takes. This confirms again that the paper's statistics used the code's rule, not the "largest fascicle" of its Methods.

I made this the main test for every mixed-model claim, still marked as an assumption. The old Kenward-Roger test and the other variants are still shown. A new notebook section, "Which test the paper's F and p come from", sets the paper's implied degrees of freedom beside each test.

**Effect on the outcomes.**
- **fascicles-larger-cervical:** under the new test the pig contrast has p = 0.055 (0.060 with the code's rat values), so only two of three species hold. The verified outcome (reproduced) stays, and `proposed` gives partially_reproduced with the reason. No variant gives the paper's pig p of 0.0009. With this contrast's t it would need about 25 degrees of freedom, and I added that question to the existing finding that asks the authors about JMP's settings.
- **The seven other mixed-model claims** keep their outcomes; their numbers in the notebook, record and README are updated.

**Text corrected, as the verifier asked:**
- **rat-ten-times-smaller:** the p values now match what the notebook prints, with a note that values this small are at the limit of numerical precision.
- **Summary, rat values:** they now say they match the code's output file exactly and the paper only to rounding (0.2577 against 0.260 mm). The rat subdiaphragmatic fascicle diameter matches the paper only under the code's rule.
- **Summary, C54-3:** the unsupported "3.57 mm image frame" sentence is gone. The mask is inverted, and measuring the nerve from its complement gives the code output file's 1615 µm.
- **Summary, micrographs:** it now says only the nine cervical micrographs were opened and checked.

**Questions for a reader** (claims not changed), added to `questions/pelot-2020.yaml`:
- Should the fascicle-diameter criteria use the Methods' "largest fascicle" or the code's first-trace rule? It changes no outcome here but does change the values reported against the paper.
- The rat-carotid-sheath-bundles criterion contradicts itself for this dataset, which has the cervical micrographs but traces only the vagus.

**Round 2 recorded** under `verifications`, with all 35 claims marked as agreed as the verifier gave them; fascicles-larger-cervical is noted as "only with qualification". Each entry has its reason taken from the report and my response.

**Not changed:**
- rat-literature-comparison and no-age-trend still depend on a reading. Both are already stated and assumed, and the verifier did not ask for a change.
- The main rat rule stays the Methods' "largest fascicle", as agreed in round 1, even though the new test confirms the paper used the code's values.
