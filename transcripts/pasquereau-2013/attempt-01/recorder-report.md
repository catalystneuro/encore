I ran `tools/readme_row.py 001636 --write`, which added the 001636 row to README.md (4 reproduced, 3 partially, 3 not reproduced, 18 blocked). I then added this subsection at the end of docs/pilot-notes.md. Nothing is committed.

### 001636, Pasquereau et al. 2013

Four claims reproduced, three partially, three not reproduced and eighteen
blocked, all on the dandiset. Round 1 called `false-positive-rate` not
reproduced where the author had it blocked; the author kept it blocked under
the protocol's rule for a computed false-positive rate far from the paper's,
and round 2 accepted that and agreed with all 28 outcomes, so there was no
third round. The paper reports how pyramidal tract and corticostriatal
neurons in the primary motor cortex of two monkeys respond to torque
perturbations before and after MPTP. Only monkey V can be tested. The cell
counts, resting rates, antidromic latencies, kinematics and EMG were tested;
17 claims are blocked as `methods_underspecified`, because the response
detection as described gives a false-positive rate of 0.22 against the 0.01
its threshold implies, which blocks that claim and the 15 that use the
detected responses, and because the paper does not define the single-trial
latencies of `trial-correlations`.

The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
No monkey L file marks a torque perturbation, the monkey L torque command is
NaN in every pre-MPTP file, and 15 of 51 post-MPTP monkey L files have no
analog data, so the monkey L half of the paper (115 and 73 cells) cannot be
tested. The torque command's 50 ms pulse has three sizes (about 46, 91 and
183 units above rest), the smallest in most pre-MPTP sessions (108 of 157)
and the largest in most post-MPTP sessions (129 of 141), where the paper
describes one 0.1 Nm impulse; the kinematic and EMG outcomes therefore
compare different stimuli and cannot be attributed to MPTP, and post-MPTP
movements are faster and larger, the opposite of the paper. The analog
streams are not on the clock of the trials and spikes and fall behind by up
to 365 ms within a session; moving each trial's segment to its start puts
the command step 4 to 7 ms after every labelled onset. Other findings: the
angle's reference frame says positive is extension where the data show
flexion; four monkey V files repeat a block of another file's trials, and in
two of them the same unit is stored twice with different projection types;
`unit_also_in_session_id` uses the wrong prefixes, 35 of its 43 references
name files not in the dandiset, and the others point to a different unit;
the dandiset description gives systemic MPTP, elbow movements for both
monkeys and 1993 for Leu, where the files and paper say intracarotid MPTP,
the wrist for monkey L and August 1992; monkey L analog is sampled at 100 Hz
against the paper's 200 Hz, and the EMG is stored in uncalibrated A/D units;
the torque onset comes 1.70 to 1.73 s after `center_target_appearance_time`
in 90% of monkey V perturbations, where the Methods put it 1 to 2 s after
center capture at random; and no analysis code is published. The paper
itself gives different pre-MPTP PTN and CSN resting rates in the text (16.3
and 3.6 spikes/s) and Table 1 (18.3 and 3.2), and Table 1 marks the CSN
change in the fraction of excitatory responses p < 0.01, where its own
counts give p = 0.54.

An earlier author run, cut short by the session limit, had left a draft
helper and its transcript on the branch; the author read the end of that
transcript, replaced the helper, and flagged it as possible contamination of
the protocol-alone test. The author's other points on the protocol: the
paper states a per-comparison threshold, not a false-positive rate, and the
block that follows from treating it as one spreads to latency results that
match the paper; no rule for how to compute a false-positive rate; "the
stated spread" for a mean and SD over cells; supplementary material and a
dandiset that holds one of two subjects; counting each recording once
against matching counts that include duplicated units; a stimulus that
differs between conditions, which fits no finding kind; absence claims with
many tests; and no field in the attempt schema for the code repository and
commit read.
