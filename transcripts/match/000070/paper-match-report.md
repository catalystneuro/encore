I gave all eight papers a verdict in `papers/match/000070.yaml`, and the file passes `python tools/paper_match.py validate`. The dandiset holds Utah array recordings only: 10 sessions from monkeys Jenkins and Nitschke, 2009 to 2010. Seven papers get `partial` and one gets `other_data`. None is `primary`, because I changed the Nature 2012 verdict the checks wrote.

| Paper | Verdict | Deciding evidence |
|---|---|---|
| 10.1038/nature11129 | **partial** (was primary `by: checks`; now `by: agent`) | It analyses 9 datasets. Only its two array datasets are in the dandiset ("monkey J-array, recorded 09-18-2009; monkey N-array, recorded 09-23-2010"), and both match session files there. Its seven single-electrode datasets from monkeys A, B, J and N are not. |
| 10.1016/j.neuron.2010.09.015 | partial | Only its J-array dataset (146 isolations, the same count as the Nature J array session) can be here. Its single-electrode datasets from monkeys A, B and J are not. |
| 10.1152/jn.00892.2011 | other_data | "recordings were made one at a time with moveable tungsten single electrodes", and the dandiset holds array data only. |
| 10.1038/nn.3643 | partial | Its array datasets JA and NA fit the dandiset. Its single-electrode datasets J and N and its EMG do not. Which array days it used is uncertain. |
| 10.1038/nn.4042 | partial | The networks are trained on EMG, which the dandiset does not hold. They are compared with neural data that pool single-electrode and array units from monkeys J and N, and only the array part can be here. |
| 10.7554/elife.04677 | partial (uncertain) | Same monkeys and the same M1/PMd arrays, but it uses a "novel decision task" that the archive metadata does not mention. Whether its five sessions are among the ten in the dandiset is unknown. |
| 10.1523/eneuro.0085-16.2016 | partial | "The array datasets... (datasets JAD1, JAD2, NAD, and NAC) from a single session" fit the dandiset. Its single-electrode datasets JC and NS do not. |
| 10.1038/s41592-018-0109-9 (LFADS) | partial | Its monkey J maze dataset (Utah arrays, about 2300 trials over 108 reach types) fits the J array session. Its monkey P, cursor-jump, center-out and human-participant data are elsewhere. |

None of the papers says where its other data are deposited, so I left `data_in` empty. Since no paper is primary, an attempt will use the first `partial` paper, Nature 2012.

The working tree also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.
