I checked the claims file for CRCNS hc-1 and made eight corrections. It is ready for an attempt. Nothing was committed or pushed.

**Checker result:** `claims/crcns-hc-1/10.1152-jn.2000.84.1.390.yaml: 21 claims, 21 quotes, 4 statistical values, 0 problems`. This was the result both before and after my edits.

The extracted text replaces some symbols with a placeholder character. I couldn't render the PDF, so I decoded its compressed text and read which font character prints each one. That gave two of the corrections below.

**Changes, by claim**
- **fig7-vertical-spread (and the opening comment):** the paper prints "≥ 100 um" above and below the soma, using the same character as "≥ 13" and "≥ 60 uV". The file had read it as "approx. 100". The statement now says "100 um or more". The criterion had required a spike 75 um (three sites) from the soma site, a number no passage gives; it now requires 100 um (four sites) on at least one side.
- **tetrode-cell-count-estimate:** "about 13" displaced neurons is now "at least 13", for the same reason.
- **fig3a-example-pair, fig3b-latency-vs-amplitude, fig3c-backprop-velocity:** the source said "paragraph 7". The passage is in the paragraph that begins "Nine other pyramidal cell recordings" (the 8th or 9th), and the source now names it by those words.
- **fig4bc-burst-attenuation, fig4d-amplitude-correlation:** both passages are in paragraph 1 of their section. The file had said "paragraphs 1 and 2" and "paragraph 2".
- **fig2-interneuron-narrow:** the Discussion passage is paragraph 4, not 5.
- **duration-correlation:** the paper names no test for R = 0.66, so the test is now recorded as "not named" instead of "linear regression".
- **ap-duration-match (and open detail O4 in the opening comment):** the paper defines the end of the intracellular spike as the "return to threshold potential". The summary sentence in the same paragraph says "return to baseline" instead. I added the return to baseline as a second accepted reading and listed the discrepancy.
- **silent-cells-inference:** one of the paper's stated main findings had no claim: a tetrode should separate about 100 neurons (60 to 100 in the abstract), against about six units usually detected. I added it to this claim's statement and source, because it is the starting point of the same argument.

All the other claims check out against the paper: statements, quotes, the statistics, expected values and tolerances. Everything in the file comes from this paper.

**Still open (recorded in the file)**
- Several thresholds aren't in the paper, and the file supplies them as standard choices that could change outcomes:
  - P < 0.05 for the Fig. 3B and Fig. 6 correlations.
  - A 2 SD rule for when a spike counts as present (Figs. 6 and 7).
  - The time windows used to find the notch and the afterhyperpolarization peak.
  - "Consistently" read as a majority of cells.
- I judged the paragraph numbers from line breaks in the extracted text. They aren't confirmed against a rendered page.

The file is ready for an attempt (`ready: true`).
