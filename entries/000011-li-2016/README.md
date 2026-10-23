# Li, Daie, Svoboda and Druckmann (2016) on dandiset 000011

Reproduction of the findings of "Robust neuronal dynamics in premotor cortex during motor
planning" (Nature 532, 459-464, doi:10.1038/nature17643) from
[DANDI:000011](https://dandiarchive.org/dandiset/000011/0.220126.1907), version 0.220126.1907.

- `reproduce_li_2016.ipynb`: the data check, one section per tested claim, and a summary.
- `li2016.py`: streaming loader (trials, units, and photostimulus conditions read from the laser
  traces), and the measures (selectivity tests, rate-change tests, selectivity recovery, the
  coding direction and the network models).

The claims are in `claims/000011/10.1038-nature17643.yaml`, the questions asked about them in
`questions/000011.yaml`, and the outcomes in `attempts/000011-li-2016-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.
