There was one question, and I changed the claims file to answer it.

**fig4ab-a1-example-units: changed.** The Figure 4 legends define the two panels by preference: 4A is the unit that prefers localization (8.0 vs 4.8 Hz) and 4B is the unit that prefers pitch discrimination (10.1 vs 2.0 Hz). The protocol ranks the legends above the code's index. The criterion still takes the pair of units from `metadata/figures_generated_by_each_script.csv` (CR20B_120602_001_behaving-612 and -712). Unit A is now whichever of the two prefers localization, and unit B is the other. The criterion also says the csv's panel assignment is not binding and asks for the assignment found to be reported. The statement, quote and expected values stay as they were.

`python tools/claims_check.py` reports 0 problems across 35 claims. Only `claims/crcns-pfc-1/` and `questions/crcns-pfc-1.yaml` were modified, and nothing is committed or pushed.
