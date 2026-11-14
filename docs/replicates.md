# Replicates

A replicate is a paper's attempt run again, from the same claims and the same data, to measure how much separate
attempts agree. Replicates do not change the registry: they are never merged, and the site does not show them.

## How a replicate runs

A replicate is a whole attempt, made the same way as a repeat attempt:

- The author is blind to the earlier attempts, as in any repeat attempt (`tools/blind.sh`).
- The author tests the claims file on main, as it is. A replicate never reads the claims again.
- The author is asked for the dataset version the current attempt used, where the dataset has versions.
- Every verification round and revision runs, as in an attempt.
- The reconcile step and the finish do not run. Nothing is recorded or merged.

The author's prompt says that the paper is tested again from the same claims and data to measure how much
separate attempts agree. It does not say what the earlier attempts found.

Each replicate has a name, `r1`, `r2` and so on, and a branch of its own, `replicate/<paper>/<name>`. Its runs
are named `Agent run: <paper>/<name> <role>` in the Actions tab.

## Starting one

From the runner's clone of the repository:

```bash
REPLICATE=r1 RUNNER_ACCOUNT=verified RUNNER_FALLBACK=none tools/runner/chain.sh <paper> [<version>]
```

Give the version the current attempt used, for a dataset with versions. The chain's last line is
`<paper> REPLICATE r1 DONE` when it finishes.

## Comparing them

```bash
python tools/replicates.py <paper> [<paper> ...]
python tools/replicates.py --all
```

The report compares the current attempt on main with every finished replicate, claim by claim. Link claims are
left out, as on the site. For each paper it gives:

| Measure | Meaning |
|---|---|
| Unanimous | The claims every run gave the same outcome. |
| Pairwise agreement | Of every pair of runs and every claim, the share that agree. |
| Fleiss' kappa | Agreement corrected for chance, over the four outcomes. 1 is full agreement; 0 is what chance gives. |
| Score, mean ± SD | Each run's claims reproduced plus half the partially reproduced, of the claims tested; their mean and standard deviation. |

It then lists each run's outcome counts, and every claim whose outcome differs between runs.

When the current attempt was made under an older protocol, compare the replicates with each other first. The
current attempt's differences from them mix the protocol's changes with the variation between attempts.
