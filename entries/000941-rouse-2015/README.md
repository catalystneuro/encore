# Rouse & Schieber (2015) from dandiset 000941

Tests the findings of [Rouse and Schieber (2015)](https://doi.org/10.1152/jn.00686.2015) on
[DANDI:000941](https://dandiarchive.org/dandiset/000941/0.241029.1405), the FALCON M1-A benchmark.
The dandiset holds trial tables, EMG and multiunit spikes of monkey L, including a 53-minute
stretch of the paper's session L20120928 (trials 201 to 673) (412 successful trials, no failed ones). It holds no marker
positions or joint angles, which every kinematic finding of the paper uses, and no data of monkeys
X and Y.

| Claim | Outcome |
|---|---|
| Trial counts of Table 2 | Blocked: data missing |
| Median movement time 255 ms in monkey L, differing among monkeys | Blocked: metadata insufficient (the dataset's onset is about 55 ms later than the paper's; monkey L only) |
| 28 trials to the coaxial cylinder at 45 degrees (Fig. 2) | Blocked: data missing |
| The 23 claims on joint angles and marker positions (Figs. 2 to 10) | Blocked: data missing |

The dataset's `move_onset_time` is very likely not the paper's movement onset: in each of the four monkey L
sessions it gives movement times 52 to 58 ms shorter than the authors' own medians for the session
(Rouse and Schieber 2016, J Neurophysiol, Table 2), while cue to contact agrees.

The files' `tgt_obj` does not name the grasped object; `obj_id` does, and its codes are named here
from the apparatus order in the paper's Fig. 1 legend. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000941-rouse-2015-01.yaml`](../../attempts/000941-rouse-2015-01.yaml).
