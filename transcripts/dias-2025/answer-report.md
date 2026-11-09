I answered the one open question. `tools/claims_check.py` reports 32 claims, 32 quotes, 58 statistical values and 0 problems, and both YAML files parse. Nothing is committed.

**Question (`s4-s6-spring-migration-temperature-none`, also `s6-autumn-ahy-recent-wintering-prebreeding-precipitation-none`): how should a 95% bound that lies within Monte Carlo error of 0 be judged?**

- **Answer:** The paper does not give it. Neither the paper nor Script02 sets a seed or gives a rule for Monte Carlo error. The supplement reports one run of four chains of 15,000 iterations.
- **How the paper treats bounds near 0:** its tables go by the sign of the unrounded bound.
  - Table S5 prints the spring migration temperature interval as "-0.03 – 0.00" and counts it as not significant.
  - It prints wintering precipitation as "-0.04 – -0.00" and counts it as significant.
  - So the attempt's upper bound of -0.0002 would count as excluding 0 under the paper's own convention. The paper's own run just happened to land on the other side of 0.
- **Change to the criteria:** both now name two readings: one run with a recorded seed, and the majority over a set of seeds. The seed is a choice made by the attempt, so a claim whose two readings give different outcomes is blocked as `methods_underspecified`. That follows the protocol rule that an agent's choice is never the basis of an outcome.
- **Unchanged:** the statements and the expected intervals.

I set `answered: 2026-10-27` on the question.
