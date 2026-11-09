The checker passes, before and after my edits: `26 claims, 26 quotes, 37 statistical values, 0 problems`. I edited only the claims file and did not commit.

**Changes, by claim**
- **Six Fig. 7 claims** (`fig7e-gamma-power-electrodes`, `fig7e-gamma-events-electrodes`, `fig7e-gamma-power-mice`, `fig7e-gamma-events-mice`, `fig7f-mua-electrodes`, `fig7f-mua-mice-not-significant`): the criteria counted a claim as reproduced if the values matched under any one combination of the open method readings (o1) to (o6). That contradicts the file's own opening comment and the protocol, because these readings are method details that could change the outcome. Now every combination must agree; if they disagree, the claim is blocked as `methods_underspecified`. `fig7e-gamma-events-mice` gets the new rule through its "As fig7e-gamma-power-mice" wording; I did not edit its text.
- **`fig7c-gamma-emerges-opsin-plus` and `fig7d-contacts-exceeding-baseline`**: these criteria did not state the rule for how the readings combine, so I added the same all-readings rule. I also removed a repeated condition from fig7c.
- **`fig7b-bioluminescence-both-groups`**: the criterion described its bootstrap test as the Methods' rule. The Methods give that rule for electrode contacts, not for the bioluminescence signal. The criterion now says the test is a choice of this file, and the before and after means are shown for each mouse.
- **No changes needed:** all in vitro claims (Figs. 2 to 6, Supplementary Figs. 2 to 6). Their statements, sources, statistics, sample sizes and p-values match the Results and legends. Each of the paper's main findings has a claim, and nothing comes from outside the paper.

**Still open** (recorded in `checks`)
- **`fig7d-superficial-layers`**: the paper gives no layer boundaries. Both depth splits in the criterion (upper half, and upper two thirds) were chosen by the claims writer, not taken from the paper. I left both in, and both are run.
- **`fig7d-contacts-exceeding-baseline`**: the Methods count contacts above baseline for three measures, and the Results link the 15.7 and 2.7 to "the gamma increase". The file reads this as gamma power. That is the likely reading, but the paper does not say so outright.

**Ready:** yes. The `checks` entry is marked `ready: true`.
