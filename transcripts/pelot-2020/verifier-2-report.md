**Round 2 verification: Pelot et al. (2020), attempt pelot-2020-01**

The claims file has 35 claims and the attempt record has 35 outcomes: 29 reproduced, 3 partially reproduced, 2 not reproduced and 1 blocked. Ten outcomes carry `assumed: true`.

## 1. Outcomes and their assumptions

I agree with 34 of the 35 outcomes. The exception is fascicles-larger-cervical, where I agree only with qualification.

**fascicles-larger-cervical** (reproduced, `assumed: true`). The record says Kenward-Roger is "JMP's test". The paper's own numbers do not support that. Solving each of the paper's reported (F, p) pairs for the denominator degrees of freedom gives:

| Effect | df implied by the paper | Notebook, Satterthwaite | Notebook, Kenward-Roger |
|---|---|---|---|
| Nerve diameter, level | 23.0 | 23.3 | 30.7 |
| Nerve diameter, interaction | 23.5 | 23.4 | 30.8 |
| Fascicle number, level | 19.4 | 19.3 | 17.1 |
| Fascicle number, interaction | 18.5 | 19.3 | 17.1 |
| Fascicle diameter, species | 21.1 | 20.6 | 35.8 |
| Fascicle diameter, interaction | 25.6 | 28.4 | 51.2 |

(Notebook values from cells 35, 47 and 50.)

- So whatever JMP did, its degrees of freedom sit at this notebook's Satterthwaite values, not its Kenward-Roger ones.
- Under Satterthwaite with the code's rat values, which round 1 found to be the paper's actual values, the pig p is 0.0526 and only two of three species hold (cell 59). That would be partially reproduced.
- No variant gives the paper's pig p of 0.0009. Kenward-Roger gives 0.012.
- The assumption is stated, but it is not shown to be reasonable. The outcome should stay explicitly fragile.

**The other nine outcomes resting on an assumption** are stated and reasonable:
- **nerve-diameter-anova:** unbounded variance components match the paper's F values.
- **nerve-cervical-larger, human-variability, perineurium-no-level-difference, rat-perineurium-near-3-percent, human-pig-perineurium-thicker and no-age-trend:** each uses the claims file's own reading.
- **literature-comparison-human-pig:** the outcome is the same under both readings.
- **rat-literature-comparison:** the all-rows reading rests on the Results' "including data published for both left/right and anterior/posterior VNs", which I checked in the paper.

**rat-carotid-sheath-bundles** (blocked). I agree. Cell 125's image shows other bundles in all nine cervical micrographs, so a count by eye is possible, but it would be the attempt's own judgement. The claims file's criterion contradicts itself here, which I am reporting, not correcting: it says "Testable only if the dataset holds the cervical micrographs", which it does, and also "Not testable when only the vagus is traced", which is also the case.

**Claims file versus the paper.** As in round 1, the fascicle-diameter criteria follow the Methods text ("largest fascicle"), while the paper's numbers come from the code's first-trace rule.

## 2. Sentences the printed numbers do not support

- **Cell 42, and the record's notes for rat-ten-times-smaller:** "2.1e-15 and below 1e-15 … (Satterthwaite 4.3e-14 …)". Cell 41 prints 5.22e-15 and 1.22e-15, and Satterthwaite 4.12e-14. This does not affect the conclusion.
- **Cell 128, Summary:** "gives the numbers of the code folder's output file exactly, and the paper's". The rat cervical nerve diameter is 0.2577 mm (cell 23) against the paper's 0.260. The rat subdiaphragmatic fascicle diameter matches the paper only under the code's rule (0.1211 against 0.1291, cell 32).
- **Cell 128:** "the published code would measure the image frame (3.57 mm) in place of the nerve (1.62 mm)". The value 3.57 appears in no output. Cell 12 shows the code's own output file has 1615 µm for C54-3, the nerve.
- **Cell 128:** "holds the 18 rat micrographs … and the traces drawn over them lie within each image". Only the nine cervical micrographs are drawn and checked (cell 125).

Every other "**Result:**" sentence, the rest of the Summary, the README (counts 29/3/2/1 and "Six rest on an assumption") and the record's notes agree with the printed outputs.

The record's verification entries state my round-1 reasons accurately and in my own terms.

## 3. Round-1 points

**Resolved:**
- **B3 (Supplement 6):** it is a figure with no test. A Holm-corrected variant was added and the question was put to a reader.
- **B4 (estimation choice):** the unbounded fit is kept, supported by the F values.
- **B5 (literature rows):** the notes column is read, the continuation rows are identified as conversions, a left-only variant is run, and the posterior-study part is dropped.
- **B7 (MT minimum):** the per-bound reading is shown, and the 5 µm fascicle is noted as absent from the deposited data.
- **B8 (multi-df Satterthwaite):** replaced by the Fai and Cornelius method.
- **B11 (checksums):** the SHA-256 cell is present (cell 127).
- **C items:** the pig df explanation (observed versus expected information), the Fazan and Lachat rows, Supplement 6, the micrographs and the per-sample pig peanut counts are all now printed.

**Accepted with reasons:**
- **B1:** the code's rule stays a variant, on the protocol's rule that the Methods come before the code.
- **B6:** the claim stays blocked, now as "other".

**Remaining, bearing on a conclusion:**
- **fascicles-larger-cervical (B1, B2):** the paper's implied degrees of freedom contradict the Kenward-Roger assumption (table above). Under the combination closest to the paper's procedure, Satterthwaite with the code's rat values, the outcome is partially reproduced. No variant reproduces the paper's pig p.
- **rat-literature-comparison:** the outcome flips to reproduced with left-side rows only. This is stated and assumed, but it remains a reading-dependent outcome.
- **no-age-trend:** not reproduced under the uncorrected test, reproduced under the Holm correction. This depends on the open question about the criterion.
