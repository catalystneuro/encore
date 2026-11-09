I finished steps 1 to 5 of the Author section and ran the handover (step 6). The entry is `entries/crcns-pag-2-moaddab-2020/` and the record is `attempts/crcns-pag-2-moaddab-2020-01.yaml`. `entry.py all` passed with 0 errors and the notebook runs in about 60 s. I did not verify my own work and committed nothing.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig1bc-adversity-slows-weight-gain | blocked, data_missing |
| fig1ef-acquisition-equivalent-final | blocked, data_missing |
| fig2b-baseline-poke-equivalent | reproduced |
| fig2c-recording-discrimination | reproduced |
| fig2d-cue-responsive-counts | reproduced (32/49/48/84, the paper's counts exactly) |
| fig2d-higher-proportion-responsive | reproduced (χ² = 5.68) |
| fig2ef-baseline-firing | reproduced |
| fig4ab-excited-temporal-pattern | partially reproduced (the bregma part could not be tested) |
| fig4c-excited-inflated-onset | reproduced |
| fig4de-inhibited-temporal-pattern | partially reproduced (the bregma part could not be tested) |
| fig4f-inhibited-danger-decrease | reproduced |
| fig4f-inhibited-danger-uncertainty-discrimination | reproduced |
| fig5abc-excited-reduced-threat-probability | partially reproduced, rests on an assumption |
| fig5d-threat-tuning-curve | reproduced, rests on an assumption |
| figs4-peak-assignment-same-pattern | reproduced, rests on an assumption |
| fig5efg-inhibited-fear-output | reproduced |
| fig6-excited-firing-threat-decoupled | partially reproduced |
| figs5-excited-firing-fear-output-unrelated | reproduced |
| fig7-inhibited-firing-fear-output | not reproduced |
| figs6-inhibited-firing-threat-probability | reproduced |

**2. The dataset**

There is one zip, streamed in place. CRCNS has no versions, so the record says `unversioned`. The header explains that `live/` holds the only published copy, and the zip's ETag matches `checksums.md5` (`7d1686e3…`).

What I found:
- **Session count:** the units come from 182 sessions (74 Control, 108 EAA), not the stated 72 and 107.
- **Group labels:** which rats are Control or EAA is given only by lists in the authors' script, `vlpagAnalysis.m`, which is inside the zip.
- **Event codes:** they are undocumented. Which code means danger, uncertainty or safety changes with the behaviour program (epr38a/b/c). I assigned them by shock contingency, and they match the cube's trial table in 354 of 354 units.
- **Truncated rates:** the cube stores firing rates truncated to whole Hz. The paper's neuron counts come out exactly only from these truncated rates. With exact rates from the spike times, the Control inhibited count is 54, not 48.
- **Baseline poke field:** `poke.base` is the 20 s baseline in pokes per minute, not "2 s" as the description says.
- **0/0 trials:** trials with no pokes, where the ratio is 0/0, are stored as 1.
- **Typo:** the description gives the uncertainty shock probability as 0.25; it is 0.375.
- **Not in the data:** there is no bregma level per rat, no body weight and no pre-surgery session.
- **Partial recordings:** spikes and pokes are stored only from about 20 s before to about 33 s after each cue onset, not over the whole session.
- **Code differs from Methods:** the paper's numbers for Figs. 4C, 4F and 6 match the authors' script to the second digit. The script averages the cube's trial-wise Z scores, which is not the normalization the Methods describe. The claims file fixes the Methods' version, so under it the uncertainty part of Fig. 6 fails. I show the script's version as a variant.

The assumption: for the regressions I used the script's own inputs, the cube's trial-wise Z score `fire.z.s1` regressed on `cer.cue`. I ran all twelve combinations of the claims file's readings and the script's.

Three questions for the paper's authors are recorded as `methods_unavailable` findings:
- Which trial-wise firing and which treatment of 0/0 trials did the regressions use?
- Which neurons were left out, given that several reported degrees of freedom are smaller than the neuron counts give?
- Why does Fig. 7 not match the computation that reproduces Fig. 6?

I asked no reader anything: I found no place where the claims file misreads the paper.

**3. Where the protocol was unclear**
1. **Code in the dataset:** the protocol only names code the paper links. This zip contains the authors' own script. I used it, as the code source, to settle details the paper leaves open, and cited line numbers.
2. **Part of a criterion untestable:** for the bregma ANOVAs no outcome fits. I recorded partially reproduced, and the notes say why.
3. **Claims file method vs the paper's actual computation:** the claims file's method follows the Methods, but the data show the paper's numbers came from the script. The protocol says Methods come first and gives no route for this. I kept the claims file's method and recorded a `code_mismatch` finding.
4. **Many readings at once:** with twelve combinations, "reproduced under one reading" invites fishing. I adopted the script's own combination as the assumption, with no reading-by-reading choice per claim.
5. **Clock check:** a time shift into the inter-trial interval was impossible because the streams are stored only around trials. I shifted onsets 10 s earlier for the spikes (221 responsive units drop to 15) and permuted the cue labels for the pokes.
6. **Rate source:** truncated cube rates against exact spike rates is a data variant that the "readings" concept does not cover. I followed the script and showed both.
7. **Develop on a subset:** this did not apply, since the whole dataset loads in 35 s.

**4. Runtime and failures**

The work took about 31 minutes (19:53 to 20:24 UTC) and the notebook runs in about 60 s. Nothing failed. Two clean-up commands were denied by permissions and nothing was lost by it:
- An empty harness folder, `entries/crcns-pag-2-moaddab-2020/.claude/.cc-writes`, is still in the entry. Git does not track empty folders.
- I first tried to delete my temporary cache files with a wildcard path. That was denied, and the same deletion with full paths worked.

The untracked dotfiles in the repository root are device mounts from the sandbox, not files I created.
