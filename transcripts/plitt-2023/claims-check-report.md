The claims file for DANDI:001710 is ready for an attempt. I made seven changes to it and left four open problems on record; nothing is committed or pushed.

**Checker result:** `claims/001710/10.1101-2023.11.20.567978.yaml: 56 claims, 56 quotes, 84 statistical values, 4 problems`

All quotes match the text word for word. The 4 "problems" are p-values the checker could not find: 5.00×10⁻⁶ (Fig 2D), 2.60×10⁻⁵ (Fig 4E) and 2.40×10⁻⁷ (Fig 5D, used by two claims). I found each one printed in those legends, written as "×10−n", so they are not errors.

**Changes, by claim:**
- **figs2f-novelty-slowing-familiar:** the file fixed trial speed as the mean of the binned speeds, which the Methods don't say. The criterion now runs two readings: binned mean and time-averaged speed.
- **fig5h-extinction-group-difference:** the paper calls the extinction window both "the previous reward anticipatory zone" (legends) and "the old reward zone" (Results). Both are now readings: the 30 cm before the old zone, or the old 25 cm zone itself.
- **figs6e-familiar-activity-trials-since-novel:** removed the requirement that activity be highest right after a novel trial. The paper states no direction for this effect.
- **figs6b-block4-activity-no-difference:** the quote only described the panel. I replaced it with the Results sentence that states the finding and added that paragraph to the source.
- **fig6c-no-pv-shift-cre:** added Fig S8B to the source, since its recorded statistic (t=-1.93, p=.710) is printed there.
- **fig6e-width-speed-correlation:** the Fig 6E legend names no day, but the file fixed day 1. The readings are now day 1 novel trials, and novel trials of days 1 to 6 pooled.
- **New claim, fig4d-activity-increase-spread-across-cells:** the Fig 4D finding had no claim ("roughly half of the cells", not a small group of highly active cells). The paper gives no measure for it, so the decile rule in the criterion is my reading and is labelled as one.

**Open (recorded in `checks`, claims left as written):**
- **vr-reward-location-learning:** the rule (lick rate before the zone above every other bin, normalized speed below 1) is not from the paper. Licking to drink the reward just after the zone may break it.
- **figs5-ca3-dg-place-fields:** the binomial test against the 5% shuffle level was devised by the first reader; the paper reports no count or test.
- **fig6d and fig6e:** the paper does not give the random-effects structure of its mixed models. The criteria use a random intercept per mouse, and another choice could change the result.
- **fig2cd-decoding-improves-over-days:** the Fig 2D legend prints "day 1 vs day 2-control", which may mean that comparison used control mice only. The claim still pools both groups.

The inconsistencies in the paper's printed statistics that the header lists (Fig 1F, S3A, 2C-D, S6E, 7H, 6D, and 5D against the Discussion) are real. Apart from those above, the claims match the paper. All of the paper's main findings now have a claim, and none draws on another source.

**Ready:** yes (`ready: true`).
