I wrote `claims/grosmark-2016.yaml`. All quotes pass the checker; it still exits with 9 problems, all numbers printed only in supplementary figures, which I confirmed by reading the rendered pages.

**Text read:** the NIH author manuscript in PubMed Central (PMC4919122), not the version of record: the main text, the Figure 1–4 legends, and the full supplement (Methods, Figs. S1–S22 with legends). The paper links no analysis code; it only says the data are on CRCNS.org. Both datasets' archive descriptions describe the same eight sessions in four rats, so every claim lists both `000044` and `crcns-hc-11`.

**Claims:** 36. 35 have quotes; one (`figs14-plastic-ripple-bursting`) is marked `inferred`, because its numbers appear only in the Fig. S14 panel titles. 8 claims carry statistics (21 p-values), and all 36 have a criterion.
- Where the two earlier files named the same finding differently, I kept the 000044 id and listed the crcns-hc-11 alias in the opening comment.
- Composite claims are split: Fig. 1C into above-chance, POST > PRE and MAZE > PRE; Fig. 4C into three; the 000044 ripple/burst/coactivation claim into three.
- The 000044 file's method choices were made before the supplement was available. They are replaced by the supplement's methods.
- The 9 checker problems:
  - 8 p-values printed only in the Fig. S14 panel titles.
  - The Fig. S16 legend's "3.94 x10-06", a number format the checker doesn't parse.

  To read these I installed PyMuPDF into a temp directory and rendered the pages. The Fig. S5, S6, S9 and S16–S19 values match too.

**Details the paper leaves open, with the readings named:**
- **Sleep scoring (S):** the lab's own state epochs, or a recomputed theta/delta + EMG scoring.
- **PRE/POST yoking to the shorter epoch (Y):** the parts nearest the maze, the first part of each epoch, or counted in offline time.
- **LFP ripple threshold (L):** mean + 3 SD, or mean + 5 SD.
- **Linear-maze direction handling (D):** both direction templates scored, or one direction assigned by the direction decoder.
- **Test for "strongly contributing" (P):** the Methods say rank-sum, the Fig. S19B legend says signed-rank.
- **Denominator of the 54% place cells:** per running direction, or all 562 pyramidal cells.
- **Duration test events:** all ripple events, or only the replay-eligible ones.
- **What "eliminated" means in Fig. 2D:** mean change at or below zero, or a bootstrap interval that includes zero. Steps of 5% are a standard choice.
- **Fig. S5B bootstrap comparison:** two forms named.
- **Fig. S2 track distribution:** no test given; KS test, or rank-sum on distance from the track end.
- **Place-field stability split:** halves, or odd/even laps.
- **Firing rates:** what "session-wide" covers (three readings) and the MAZE rate (two).
- **Within-ripple ISIs:** within one event, or across concatenated ripples.
- **Ripple-triggered rate test and per-cell coactivity change:** two readings each.
- **Low/high rate split** (Methods referenced but absent): per session and direction, per session, or pooled; rate from PRE + POST or PRE only.
- **Fig. 4C ranking:** within session or pooled. No test is named, so Spearman and signed-rank are flagged as standard choices, not the paper's.
- **Fig. 4D/E test:** rank-sum, or bootstrap interval.
- **Fisher Z form:** independent or dependent correlations.

**Missing from the paper:** the images of main Figures 1–4 are not under `paper/`, so values printed only in those panels are not recorded. Criteria for those claims rely on the legends and the supplementary counterparts. There are also inconsistencies the claims work around:
- The main text's supplementary figure numbers are off by one in places; the claims use the supplement's own numbering.
- The Fig. S14 colour key is reversed relative to its legend; the legend text is followed.
