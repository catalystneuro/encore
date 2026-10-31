# Rouse & Schieber (2015) from dandiset 000941

Tests the findings of [Rouse and Schieber (2015)](https://doi.org/10.1152/jn.00686.2015) on
[DANDI:000941](https://dandiarchive.org/dandiset/000941/0.241029.1405), the FALCON M1-A benchmark.
The dandiset holds trial tables, EMG and multiunit spikes of monkey L, including the first 53
minutes of the paper's session L20120928 (412 successful trials, no failed ones). It holds no marker
positions or joint angles, which every kinematic finding of the paper uses, and no data of monkeys
X and Y.

| Claim | Outcome |
|---|---|
| Trial counts of Table 2 | Blocked: data missing |
| Median movement time 255 ms in monkey L, differing among monkeys | Not reproduced (200 ms; monkey L only) |
| 28 trials to the coaxial cylinder at 45 degrees (Fig. 2) | Blocked: data missing |
| The 23 claims on joint angles and marker positions (Figs. 2 to 10) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files' `tgt_obj` does not name the grasped object; `obj_id` does, and its codes are named here
from the apparatus order in the paper's Fig. 1 legend. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000941-rouse-2015-01.yaml`](../../attempts/000941-rouse-2015-01.yaml).
