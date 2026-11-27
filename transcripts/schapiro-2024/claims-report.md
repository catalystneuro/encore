I wrote `claims/schapiro-2024.yaml`, and the quote checker passes it: 25 claims, 25 quotes, 27 statistical values, 0 problems.

**Text read.** The eLife version of record, from Europe PMC (PMC11479588, open-access JATS). It has the Results, Discussion, Methods, the Figure 1 to 6 legends, Table 1, and Figure 1–figure supplement 1, which is the paper's only supplement. Nothing the claims needed was missing, and I didn't open the PDF.

**Code.** The paper says its analysis code is deposited inside the Dryad dataset. That makes it one of the dataset's files, so I didn't read it and no commit is recorded. The paper also links Crabsort, its spike-sorting software; I read it at commit ee237ea, and it fixes none of the measures.

**Claims.** All 25 have quotes, none is inferred, 25 have criteria and 24 have statistics. They cover:
- Ih reduction at 11 and 21 °C.
- Frequency at 11 °C, the saline minus Cs+ difference growing with temperature, and the lower Q10 in Cs+.
- Three controls with two saline runs, which are absence claims.
- The example where the depolarizing phase lengthens.
- The percentages of frequency falling during warming and rising during stable temperature.
- The three picrotoxin ANOVAs.
- PD burst duration and the Table 1 phases (PY unchanged is an absence claim).
- The delay from PD OFF to LP ON, and LP duty cycle (an absence claim).
- Period-matched latencies with their correlation.
- Phase slopes with temperature.

**Details the paper leaves open, with the readings named:**
- **Q10:** the paper only says "as described previously". Readings are (a) a nonlinear exponential fit, (b) a straight line through log frequency, or (c) the ratio of frequencies at 21 and 11 °C.
- **Which 11 °C hold:** the first hold of each condition is the main reading; the return to 11 °C after 21 °C is a variant.
- **Smoothing for the frequency "jag" measure:** a centred moving average is the main reading and a trailing one a variant. The span is either the step protocol only or the whole recording with cooling counted as stable.
- **Which cycles make up a phase at a temperature:** either cycles within 0.3 °C of the target or the whole holding period. The slope is either a line through the per-temperature means or through all cycles.
- **Tukey's test after the repeated-measures ANOVA:** MATLAB's `multcompare` on the repeated-measures model, or the classic Tukey test on the ANOVA's error term.
- **LP and PY onset and offset:** first and last spike within each PD cycle, used as a standard choice.
- **Ih windows:** the paper doesn't say over which times the initial and steady-state currents are taken; two readings are named.
- **Period matching:** either the Cs+ hold nearest in period, or cycles within 2% of the period (the 2% is my standard choice).
- **Depolarizing-phase claim (Figure 2C):** the paper shows only an example and defines no measure, so I set one from the phases the legend names.

**Inconsistencies in the paper, recorded in the criteria:**
- Figure 1D reports F(5,85) with N=21, but those degrees of freedom imply 18 experiments. Both readings are named.
- The period-matched correlation, r(21)=0.26 with p=0.2928, doesn't match the stated number of pairs. The author is to report how many pairs were used.

**Also unstated:** whether the 6 picrotoxin experiments are among the 21.

Tolerances are the paper's stated SDs, as the protocol directs, which makes them loose for some means; counts use 10%.
