# Clark and Nolan (2024) from dandiset 000943

Attempts the findings of [Clark and Nolan (2024)](https://doi.org/10.7554/eLife.89356) on
[DANDI:000943](https://dandiarchive.org/dandiset/000943/0.240614.0754), version 0.240614.0754, which
holds the raw tetrode signal and the position series of 734 open arena and virtual track sessions from
12 mice.

| Claim | Outcome |
|---|---|
| All 31 claims (grid cell counts, session-level and trial-level task anchoring, agreement between cells, behaviour by grid firing mode) | Blocked: too large |

Every claim rests on single units, and the dandiset holds none: no file has a units table or any
processed data. The paper sorted its units from the raw signal with MountainSort. Streaming the raw
signal of the sessions the paper used (638 GB) takes about 2.5 h at the rate measured here, more than
the one-hour limit for a notebook, before any sorting, so no claim could be tested. The paper's sorted
units are deposited at Edinburgh DataShare (doi:10.7488/ds/7684) in a single 26.5 GB pickle.

The notebook surveys every file, checks the description against the values (session and trial counts
against the paper's summary table, the position series, duplicate recordings, and whether the raw signal
and the position series share a clock), and measures the streaming rate. The attempt record, with the
findings about the dandiset, is
[`attempts/000943-clark-2024-01.yaml`](../../attempts/000943-clark-2024-01.yaml).
