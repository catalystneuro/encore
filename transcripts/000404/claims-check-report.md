I checked the claims file for DANDI:000404 against the paper and made ten corrections. Four points stay open, none of which blocks an attempt, so I marked the file ready. Nothing is committed.

**Checker result:** `29 claims, 29 quotes, 57 statistical values, 0 problems`. The count went from 55 to 57 statistical values because I added two to fig6g.

**Changes, by claim**
- **Sources for conditions-per-session, figs1b, fig4c, fig4f, fig4g, figs3, figs5b, figs5f, figs6cd:** each now names its Results paragraph by its opening words. Five of the numbers were off by one (fig4c, fig4f, fig4g, figs5b, figs6cd). Counting paragraphs is also unreliable where equations split them.
- **fig4f:** the statement said the result was "far above" the shuffle, which the paper does not say. It now says "significantly more than shuffle dynamics", as the Figure 4F legend does.
- **figs5b:** I removed the reading that paired by session and task. The paper's own p-values only work as paired t-tests over sessions (8 and 3 degrees of freedom: T = -7.182 gives p = 9.4e-05, T = -5.141 gives p = 0.0143). So the pairs are the 9 and 4 sessions, as the Methods say, and the paper's N of 18 and 8 counts R2 values.
- **fig4c:** leaving out the transitions to and from a left-out command is now cited to the Figure S4A legend, which states it, and not only to the code.
- **figs6cd:** the population distance is divided by the square root of the number of neurons (Methods), not of the null-space dimension. This does not change r or the slope.
- **fig6d:** this is a claim that something is absent. It is now also not reproduced when the Wilcoxon test finds a difference in any session, because the paper's test covers the sessions too.
- **fig6g:**
  - I added the Table S2 statistics for the decoder-null comparison's own No Dynamics model against shuffle (Figure 6H).
  - The criterion now requires that absence and the per-session Mann-Whitney absences.
  - The null now has two readings: the Methods' behavior-preserving shuffle and the code's subsampling.
- **figs1d:** the criterion now says why the Statistics Summary's "behavior-preserving shuffle" is not the test here. That shuffle leaves commands unchanged, so the Methods' subsampling of the matched pool is the test.
- **fig5e:** the "about" field of the condition left-out statistic now says "each session".

**Open**
- I could not re-read the paper's code in this check, so method details cited only to code line numbers are taken as the first reader wrote them.
- fig4g and fig5f read "vast majority" and "majority" as more than half. fig5d uses two readings of "more accurately than the rest" that the first reader chose. The paper gives no rule for any of these.
- The paper gives no unit for the single-neuron distances and errors (fig3b, fig4de) or for the next-command error (fig5f). Hz comes from the code.
- Most claims need the decoder parameters. Whether the dataset holds them is for the author to find.

**Ready:** yes (`ready: true`).
