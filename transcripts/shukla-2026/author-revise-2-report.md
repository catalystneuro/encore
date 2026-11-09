I've worked through the round-2 report. No verified outcome changed. I propose two changes for a third round: fig4b and fig4c, from blocked to not_reproduced. The entry re-ran cleanly with `tools/entry.py all` (0 errors, 10.5 min), and the numbers matched the run before it.

**Proposed changes (fig4b, fig4c).** The verifier asked for a per-session median lag, a measure that needs no sessions dropped. With it, the head-position arrival lag still fails at 100% (p = 0.39), and so does the head-position departure lag (p = 0.69). The blocked outcomes therefore depend entirely on removing four sessions, using a 100 s cut-off I chose after seeing an outlier. My justification for it ("longer than any plausible wait") was wrong: poke-based session mean lags reach 208.6 s. With every session included, as the claims file measures the lag, both readings fail for both claims. Preferring pokes, as fig4d does, gives the same result. The record keeps blocked and puts not_reproduced under `proposed` with the reason. The fig4d notes now explain why it treats the readings differently: only the 4b and 4c criteria say to block when readings disagree.

**Outputs added, as the verifier asked:**
- **fig1g:** fits with the raw, uncleaned sequences. They are much weaker (R² 0.03 to 0.12), which backs the note that previously had no output behind it.
- **fig1j, fig7g, fig7h:** the same tests on the "aligned" sessions only, i.e. the four pairs whose head positions match their pokes. Each outcome holds there.
- **fig7e:** the quartile ANOVA on the aligned sessions (8 rats). The follower-only gaze effect holds. Two parts of the criterion fail there: quartile 3 is highest for WT rats, and mutual gaze also rises over the quartiles (p = 0.0004). I kept the outcome as reproduced and proposed no change, because the criterion is defined on all sessions and this subset has 8 of the 20 rats. The notes and the round-2 record say the outcome rests on the six pairs whose positions disagree with the pokes. Round 3 will only see this in the record, not as a proposal.

**Corrections:**
- **fig1i:** the notes now say the blocked outcome depends on removing sensor crosstalk, and that with the raw sequences both ANOVA readings fail, which would give not_reproduced.
- **fig1h:** the notes now say the variant from round 1 cannot test the early sessions, because it is at chance there by construction. I count 5 such sessions in the table, where the verifier counted 6; the record states my count.
- **Wording:** fixed the fig1f p range, the fig4eg interaction sentence ("over all sessions"), the Summary sentence on the clock check (it used every 7th session), the run time in the README and cell 0, and the missing "(assumption)" on fig3e in the Summary table.
- **Findings:** added the verifier's question for the authors: were the unlabelled sensory-deprived sessions numbered as 50% sessions, possibly inside the first 35 analysed?
- **Record:** added round 2 under `verifications` for all 35 claims.

**Not done:**
- `assumed: true` on fig1i, fig4b and fig4c: the attempt schema forbids it on a blocked outcome, so the deviations and notes state the dependence instead.
- A Laplace-fitted GLMM check for the gaze models: R is not in the environment.
- `questions/001845.yaml`: the verifier reported no place where the claims file misreads the paper, so nothing was added.

The pre-existing changes to `tools/build_site.py` and `tools/site_assets/app.css` are not mine and I left them alone. Nothing is committed.
