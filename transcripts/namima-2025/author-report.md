All 27 claims have an outcome: 18 were tested on the data and 9 are blocked. The entry is written, `tools/entry.py all` passes (0 errors; the notebook runs in 457 s) and the handover package is built. Nothing is committed.

The dataset is pinned at version 0.261006.2007, its only published version; the paper cites no version. The notebook header records this.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-sessions-and-neurons | reproduced |
| ex-m2p6-cluster | partially reproduced (13 neurons with significant Isimilarity, expected 11; 17 missing, 12, 21 and 22 added) |
| ex-m2p6-pairs | partially reproduced (only the bright similarity of neurons 18 and 19 misses: −0.144, expected −0.25) |
| ex-m2p6-invariance | reproduced |
| ex-csd-sinks | blocked, data_missing (no LF signal in the files) |
| ex-m1p12-no-cluster | reproduced |
| ex-m1p12-strong-responses | reproduced (28 and 26, exactly the paper's numbers) |
| pop-significant-isimilarity | partially reproduced (always a minority, but 381–625 neurons, expected 344) |
| pop-intercept-slope-correlation | reproduced (r = −0.768) |
| pop-dark-bright-consistent | not reproduced (r = 0.48–0.52, expected 0.435; the consistency is stronger than reported) |
| pop-contrast-invariance | reproduced (0.632, reliability reading b) |
| pop-sparse-across-penetrations | reproduced |
| pop-asymptote-20-percent | reproduced |
| pop-mean-isimilarity-yield | reproduced |
| pop-recording-density | reproduced (r = 0.257) |
| pop-within-vs-across-sessions | partially reproduced (direction and p hold under every reading; no reading matches the means) |
| orientation-sf-isimilarity | blocked, data_missing (shape images not public) |
| orientation-auc-coarse-clusters | not reproduced (M2p6 and M1p5 are of neither kind, whichever stim_ID is taken as the spindle) |
| apc-peaks-sparse-clustering, apc-example-m2p51 | blocked, data_missing (the shapes' curvature descriptions are not public) |
| gyrus-penetrations-consistent | blocked, metadata_insufficient (no grid coordinates in the files) |
| texture-sparse-clusters | not reproduced |
| texture-original-reversed-consistent | not reproduced (r = 0.64–0.71, expected 0.464) |
| texture-asymptote-20-percent | not reproduced (26–52%, expected 20%) |
| position-optimal-consistent | reproduced (r = 0.325, 721 neurons; expected 723) |
| position-examples-invariant | not reproduced |
| simulation-random-with-domains | blocked, methods_underspecified |

No outcome rests on an assumption (`assumed` is never set).

## 2. The dataset, assumptions and questions

**What the dataset holds.** Only spike times of good units, with a `pen_ID` label on every file. The labels identify the example penetrations: the labelled sessions give the paper's neuron counts for M2p6 (24), M1p12 (42) and M2p28 (55). Session counts and responsive-neuron counts match the paper. The texture files' good units sum to exactly 1,345, the paper's 979 + 366.

**Findings recorded in the attempt:**
- **Missing:** the LF signal, the stimulus images, the RF-mapping data and the grid coordinates are not in the files.
- **Unlabelled codes:** shape `stim_ID` 0–14 and position codes 0–4 have no names. The data do not reveal which position is the center either: the largest population response falls on different positions in different files.
- **Mislabelled sessions:** the trial tables of all 34 position-test files name their session "…SL".
- **Undescribed conditions:** a third luminance level of 8 cd/m2 (the background) appears in 73 of 74 shape files, and the texture files hold the spectral-noise version.
- **Depth:** unit depth is the best channel in 20 µm steps, not the template center of mass the Methods describe.
- **Session mismatch:** 5 of the 34 M2 texture sessions are texture-only days, where the paper says shape and texture were both run in 34 sessions. There is also a 34th position-test file holding a single unit; the paper reports 33.
- **Clock check:** spikes and presentations share a clock in 152 of 159 files. It could not be established in five M1 texture files and the two single-unit files.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): does "confidence limit > 0.5" mean the width or the half-width of the bootstrap interval, and at what level? The two readings change the significant-Isimilarity counts by 10–60%. The texture counts point to the half-width reading.

**Question to a reader** (`questions/001357.yaml`): position-examples-invariant accepts a session only if its neuron count is within 10% of Figure 11's n. But the legend defines that n as neurons with quantified RF centers, not the neurons in the matrices. Under the rule as written, M2p9 is matched to the session labelled p12, where the claim fails. Under the dataset's p09 label, the M2p9 half of the claim holds. The claim's outcome is not reproduced either way, because M2p28 fails.

## 3. Where the protocol was unclear

1. **No partial rule in a criterion.** pop-significant-isimilarity's criterion defines only "reproduced". I recorded partially reproduced, because the minority the statement describes holds and the counts do not, and gave that reasoning in the notes.
2. **The clock check for this dataset.** A stimulus-against-blank rate contrast did not work: stimuli suppress some units, so it failed in many files. I used per-unit ANOVA over stimuli at true onsets against onsets shifted by −1.3 s, and named the files where the check fails.
3. **A misreading that cannot change the outcome.** The protocol says to ask a reader only when a misreading "could change the outcome". In the Figure 11 case it changes half of the claim but not the outcome; I asked anyway and said so in the question.
4. **Bootstrap bias.** The bootstrap of a noise-corrected estimator sits below the point estimate, which the paper does not mention. I used only the interval's width and recorded this as a deviation.
5. **Outside data.** No pinned public copy of the Pasupathy and Connor (2001) shapes turned up; I searched the shape lab's publication pages, Pospisil et al. 2018, github.com/deanpospisil/er_est and the SparseShape OSF project. Those claims are blocked as data_missing, as the protocol requires for an outside input that is not public.

## 4. Runtime and failures

The run took about 1 h 20 min (06:52 to 08:10 UTC); the notebook runs in about 8 minutes, half of it streaming the files. Nothing failed.

Untracked dotfiles (`.bashrc`, `.profile`, `.idea`, `scripts` and others) appeared in the repository root; I did not create them and left them alone. Exclude them when committing.

Sources (web search for the shape set):
- [Pospisil et al. 2018, eLife](https://elifesciences.org/articles/38242)
- [SparseShape, J Neurosci 2023](https://www.jneurosci.org/content/43/22/4129)
- [Pasupathy & Connor 2001 PDF](https://depts.washington.edu/shapelab/publications/ShapeRepV4JNeurophys.pdf)
