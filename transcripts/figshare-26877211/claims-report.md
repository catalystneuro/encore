I wrote `claims/figshare-26877211/10.1038-s41597-024-04294-w.yaml`, and the quote checker passes it (9 claims, 9 quotes, 0 problems). Nothing was committed.

**Text read:** the version of record from Europe PMC (PMC11682307): Methods, Data Records, Technical Validation, Usage Notes, and Tables 1 and 2, which come through flattened but readable. The paper is a Data Descriptor and has no supplement. There was no PDF, but Figures 1 and 2 are a flow chart and a screenshot with no results in them. The text gives the authors as initials only, so the opening comment names the paper by title.

**Code read:** https://github.com/UBESP-DCTV/jecfa at commit 2d8a534. It is an R `{targets}` pipeline that scrapes the pages, builds the table and text-mines the PDFs. It has no code for the paper's Table 1 percentages, its Table 2, the FAS count or the validation. It differs from the Methods in two places, both noted in the file:
- It scrapes ids 1 to 10000; the Methods say 1 to 7000.
- It never removes duplicates, although the Methods say the table is cleaned of them.

**Claims:** 9, all with quotes; 1 is a link claim and 8 are findings. None has statistics, because the paper reports no tests. All 9 have criteria:
1. The deposit has 6552 rows and the Table 1 fields (the link claim).
2. 6549 unique pages after cleaning.
3. Table 1: the share of pages carrying each of 17 fields.
4. Table 2: counts and shares by evaluation year.
5. Table 2: counts and shares by functional class.
6. The unknown rows carry only the JECFA name.
7. FAS codes: almost all 85 referenced, and seven of them hold 50% of records.
8. Validation discrepancy rates from 700 manually checked pages.
9. The portal search count of 6547 against the pages with a JECFA name.

Claims 8 and 9 need outside data the paper does not deposit: the manual REDCap extraction and the live portal, which has changed since May 2024. Only the dataset's side of claim 9 can be tested.

**Details left open, with the readings named:**
- **What a row is:** every row of the table, or one row per distinct URL. Fields with several values could give a page more than one row.
- **Missing values:** the reading is that a field counts as absent when it is NA or an empty string.
- **How duplicates are found:** by distinct URL, by distinct JECFA name, or by removing page 5883 and the extra copies of page 6316's chemical.
- **Which evaluation year counts:** the code takes the first one listed on each page, and the criterion follows the code. Table 2's year bins and its denominator of known values are read from the paper's own numbers. The text says 2,356 for 1958 to 2000 where the table says 2,357; both are within tolerance.
- **Functional class mapping:** the strings run the class into the sub-class, so the reading is a match on the leading class name.
- **FAS 50% denominator:** all rows, or only rows with a FAS code. The "almost all 85" threshold (at least 77 codes) is my choice and is flagged as one.
- **Validation denominator:** all 700 sampled ids, the ids that resolve to a page, or the pages where the field is present. 0.2% is not a whole number of pages out of 700, which argues against the first reading.
- **Unknown rows (claim 6):** the 90% threshold is my choice and is flagged as one.
- **Tolerances:** claims 1 and 2 use the paper's own spread of 6549/6551/6552 in place of the default 10%.

**Missing from the paper:** the reference list is not in the text, so references 12, 17 and 18 could not be identified. Reference 18 is the one cited for the validation results in claim 8.
