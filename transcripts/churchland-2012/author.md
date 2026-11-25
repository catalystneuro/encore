# churchland-2012 · author · run 45507913066

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries attempts claims paper; wc -l docs/*.md README.md
```

```
Tue Nov 24 23:18:33 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
protocol.lock
[... 1106 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 760 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/churchland-2012.yaml"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Foster, Nuyujukian, Ryu & Shenoy (2012) on
2	# dandiset 000070.
3	# Source: the NIH author manuscript in PubMed Central (PMC3393826), full text, read from its
4	# Results, Methods and figure legends, and the Supplementary Information PDF from the
5	# publisher's site. Values marked "read from the figure" are readings of Figure 6, which the
6	# text does not give in numbers.
7	#
8	# When these criteria were written, the author had seen the data check only: the file list,
9	# metadata, trial tables, unit counts and firing rates, trial counts per condition after the
10	# Methods' selection, hand speed around movement onset, and the faults of the files (the
11	# wrapped first entry of spike_times_index, and the clock resets of the 2010 file). No jPCA
12	# or other claim analysis had been run on any file.
13	#
14	# The dandiset holds the paper's two array datasets, J-array (sub-Jenkins ses-20090918) and
15	# N-array (sub-Nitschke ses-20100923), each with 108 maze conditions. It does not hold the
16	# seven single-electrode datasets (monkeys A, B, J1 to J4 and N), the EMG, the leech or the
17	# walking-monkey data. It also holds eight further array sessions the paper does not use,
18	# one of which (sub-Nitschke ses-20090910, 108 conditions) is consistent with the
19	# "N-9-10-2010" dataset of Supplementary Figure 5 (see the notebook).
20	#
[... 326 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; grep -n "^#" docs/design.md docs/archives.md; ls entries/fouke-2025 entries/churchland-2012 2>&1; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat papers/datasets/churchland-2012.yaml; ls papers/author-notes/ | grep church; ls questions | grep church
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,35p docs/archives.md; cat attempts/fouke-2025-01.yaml; cat entries/fouke-2025/README.md
```

```
<persisted-output>
Output too large (39.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9e4295f9-dbae-4f3e-bb14-85eae35b1c30/tool-results/b50tl2qs3.txt

Preview (first 2KB):
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

## DANDI
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150
```

```
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/fouke-2025-01.yaml | grep -v "^    " | head -80; grep -n "findings:" -A40 attempts/fouke-2025-01.yaml | head -60; ls schemas; python tools/entry.py --help 2>&1 | head -30
```

```
outcome: not_reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
  deviations:
  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion
- claim: fig1c-continuous-vs-bouts
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1c-continuous-vs-bouts
  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
  deviations:
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "methods\|jPCA\|normaliz\|soft\|Gaussian\|delay\|trials" paper/10.1038-nature11129.txt | head -100
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1038-nature11129.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt; grep -n "METHODS\|Methods\|Recordings and task\|Data preprocessing\|jPCA\b" $TMPDIR/paper.txt | head -40
```

```
1266 /tmp/claude-1001/paper.txt
37:relevant to dynamical structure. We therefore employed a novel method that finds an informative plane within the top PCs. To be conservative, this ‘jPCA’ method was applied only to the top six PCs, 
38:which contain the six response patterns most strongly present in the data. The mathematical underpinnings regarding jPCA are described below, but the following is critical. Application of jPCA 
60:responses? Each axis of the jPCA projection captures a time-varying pattern that resembles a single-neuron response ( supplementary fig. 1 ). Indeed, single neurons strongly reflect combinations of 
65:appear by accident or for trivial reasons? Multiple ‘shuffle’ controls demonstrate that jPCA does not find rotational structure when such structure is not present ( supplementary fig. 2,3 ; 
68:capture the second- and third-most data variance possible) together capture 29% of the total variance. Thus, the jPCA projection simply captures response patterns that were always present in the top 
74:and spiking noise were matched to the recorded data. For velocity-model populations, jPCA found no robust or consistent rotations ( fig. 4 a,d,h ). This was true for all datasets (summary analysis 
94:weak correlation between preparatory and movement-period ‘tuning’ 15 , 29 . Despite such surface complexity, jPCA projections of the simulated populations successfully reveal the simple underlying 
96:state in the jPCA plane ( x ) to its derivative ( ẋ ) for every condition and time ( fig. 6 a ). The first jPCA plane is oriented such that the average rotational tendency of the data – however weak 
98:the velocity-tuned model, the complex-kinematic model, and EMG all had distributions that peaked slightly above zero. Rotation strength was also quantified via the jPCA computation, in which the data 
110:angular velocity for fast and slow reaches ( fig. 6 c,d ). The same point can be made by separately applying jPCA for fast and slow reaches: the largest eige
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 20,
 "limit": 205
}
```

```
20	individual-neuron responses. pmc-status-qastatus 0 pmc-status-live yes pmc-status-embargo no pmc-status-released yes pmc-prop-open-access yes pmc-prop-olf no pmc-prop-manuscript yes 
21	pmc-prop-open-manuscript yes pmc-prop-legally-suppressed no pmc-prop-has-pdf yes pmc-prop-has-supplement yes pmc-prop-pdf-only no pmc-prop-suppress-copyright no pmc-prop-is-real-version no 
22	pmc-prop-is-scanned-article no pmc-prop-preprint no pmc-prop-in-epmc yes Motor and premotor cortex were among the first cortical areas to be extensively studied 1 . Yet their basic response 
23	properties are poorly understood, and it remains controversial whether neural activity relates to muscles or to abstract movement features 2 – 13 . At the heart of this debate is the complexity of 
24	individual-neural responses, which exhibit a great variety of multiphasic patterns 4 , 14 , 15 . One explanation is that responses represent many movement parameters: eqn.1 r n ( t ) = f n ( param 1 
25	( t ) , param 2 ( t ) , param 3 ( t ) ⇌ ) where r n ( t ) is the firing rate of neuron n at time t , f n is a tuning function, and param 1 ( t ), param 2 ( t )… are arguments such as hand velocity or 
26	target position. Alternatively, motor cortex may constitute a dynamical system that generates and controls movement 4 , 8 , 14 – 17 . In its simplest, deterministic form this can be expressed as: 
27	eqn.2 r . ( t ) = f ( r ( t ) ) + u ( t ) where r is a vector describing the firing rate of all neurons (the ‘population response’ or ‘neural state’), ṙ is its derivative, f is an unknown function, 
28	and u is an external input. In this conception, neural responses reflect underlying dynamics and display ‘tuning’ only incidentally 18 , 19 . If so, then dynamical features should be present in the 
29	population response. In looking for dynamical structure, we focused on a common principle for movement generation across the animal kingdom: the production of rhythmic, oscillatory activity 20 – 22 . 
30	Rhythmic
[... 194 more lines not kept]
```

**Agent**

Now the supplement sections (shuffles, Supp Fig 4, 5) and the figure legends.

**Agent calls Bash**

```bash
sed -n 260,300p $TMPDIR/paper.txt; sed -n 400,700p $TMPDIR/paper.txt
```

```
Transient and Continuous Loads During Posture Journal of Neurophysiology 101 150 163 10.1152/jn.90230.2008 2008 19005005 37 Sussillo D Abbott LF Generating coherent patterns of activity from chaotic 
neural networks Neuron 63 544 557 2009 19709635 10.1016/j.neuron.2009.07.018 PMC2756108 38 Scott SH Optimal feedback control and the neural basis of volitional motor control Nat Rev Neurosci 5 532 
546 10.1038/nrn1427 nrn1427 [pii] 2004 15208695 39 Gilja V Chestek CA Nuyujukian P Foster JD Shenoy KV Autonomous head-mounted electrophysiology systems for freely behaving primates Curr Opin 
Neurobiol 20 676 686 S0959-4388(10)00104-2 [pii] 10.1016/j.conb.2010.06.007 2010 20655733 PMC3401169 40 Foster JD Proc. of the 5th International IEEE EMBS Conference on Neural Engineering 613 615 
10.1109/NER.2011.5910623 PMC4442696 26019730 41 Miranda H Gilja V Chestek CA Shenoy KV Meng TH HermesD: A high-rate long-range wireless transmission system for simultaneous multichannel neural 
recording applications IEEE Transactions on Biomedical Circuits and Systems 4 181 191 2010 23853342 10.1109/TBCAS.2010.2044573 42 Churchland MM Yu BM Ryu SI Santhanam G Shenoy KV Neural variability 
in premotor cortex provides a signature of motor preparation J Neurosci 26 3697 3712 2006 16597724 10.1523/JNEUROSCI.3762-05.2006 PMC6674116 Figure 1 Oscillation of neural firing rates during three 
movement types. a. Response of one of 164 neurons (simultaneously recorded using voltage-sensitive dye) in the isolated leech central nervous system during a swimming motor pattern. Responses (not 
averaged across repetitions) were filtered with a 100 ms Gaussian kernel. b. Multi-unit response from one of 96 electrodes implanted in the arm representation of caudal premotor cortex. Data from 32 
such channels was wirelessly transmitted during walking. Responses (not averaged across repetitions) were filtered with a 100 ms Gaussian kernel. c. Response of one of 118 neurons recorded from motor 
cortex of a reaching 
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/0.261122.2046/" | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['name','version','doi','description','assetsSummary','dateModified','datePublished']},indent=1)[:4000])"; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/0.261122.2046/assets/?page_size=100" | python -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(a['asset_id'],a['path'],a['size']) for a in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import pynwb, remfile, h5py, numpy, scipy; print(pynwb.__version__, h5py.__version__, numpy.__version__)"; which uv python; python --version; nproc; free -g
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, numpy, scipy; print(pynwb.__version__, h5py.__version__, numpy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib dandi nbformat nbclient ipykernel 2>&1 | tail -3; python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, sys
V="0.261122.2046"
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url,allow_redirects=True); s3=r.url
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
    else:
        print(name+'/', {k:v for k,v in obj.attrs.items() if k not in ('namespace','object_id')})
f.visititems(show)
EOF
time python survey.py 75013796-4a2d-41dc-9eb6-db9d365b28b4 2>&1 | cut -c1-300
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/devices/ {}
general/devices/Utah Array(M1)/ {'description': '96 channel utah array', 'manufacturer': 'BlackRock Microsystems', 'neurodata_type': 'Device'}
general/devices/Utah Array(PMd)/ {'description': '96 channel utah array', 'manufacturer': 'BlackRock Microsystems', 'neurodata_type': 'Device'}
general/experiment_description () object {}
general/experimenter (2,) object {}
general/external_resources/ {'neurodata_type': 'HERD'}
general/external_resources/entities (3,) [('entity_id', 'O'), ('entity_uri', 'O')] {'neurodata_type': 'Data'}
general/external_resources/entity_keys (5,) [('entities_idx', '<u4'), ('keys_idx', '<u4')] {'neurodata_type': 'Data'}
general/external_resources/files (1,) [('file_object_id', 'O')] {'neurodata_type': 'Data'}
general/external_resources/keys (5,) [('key', 'O')] {'neurodata_type': 'Data'}
general/external_resources/object_keys (5,) [('objects_idx', '<u4'), ('keys_idx', '<u4')] {'neurodata_type': 'Data'}
general/external_resources/objects (4,) [('files_idx', '<u4'), ('object_id', 'O'), ('object_type', 'O'), ('relative_path', 'O'), ('field', 'O')] {'neurodata_type': 'Data'}
general/extracellular_ephys/ {}
general/extracellular_ephys/1/ {'description': 'array corresponding to device implanted at PMd', 'location': 'Caudal, dorsal Pre-motor cortex, Left hemisphere', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/2/ {'description': 'array corresponding to device implanted at M1', 'location': 'M1 in Motor Cortex, left hemisphere', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'colnames': array(['location', 'group', 'group_name', 'channel_name'], dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'ElectrodesTable'}
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > desc.py <<'EOF'
import h5py, remfile, requests, sys
aid=sys.argv[1]
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
for p in ['intervals/trials/correct_reach','intervals/trials/maze_condition','intervals/trials/discard_trial','intervals/trials/trial_type','intervals/trials/timeseries','processing/ecephys/Processed/A001','processing/ecephys/Processed/B001','processing/behavior/Position/Hand','processing/behavior/Position/Eye','units']:
    print('==',p, f[p].attrs.get('description'))
for p in ['general/experiment_description','general/related_publications','general/session_id','session_description','general/subject/subject_id','general/keywords','identifier','session_start_time','general/source_script']:
    print('==',p, f[p][()])
print(f['general/extracellular_ephys/electrodes/location'][:3], f['general/extracellular_ephys/electrodes/group_name'][[0,95,96,191]], f['general/extracellular_ephys/electrodes/channel_name'][[0,95,96,191]])
print(f['units/electrodes'][:5], f['units/electrodes'][-5:], f['units/electrodes_index'][:5])
eg=f['units/electrode_group'][:]; print(eg[0], eg[-1]); 
import collections; print(collections.Counter(f[r].name for r in eg))
print(f['units/spike_times_index'][:5], f['units/obs_intervals_index'][:5])
print(f['units/obs_intervals'][:5])
EOF
python desc.py 75013796-4a2d-41dc-9eb6-db9d365b28b4
```

```
== intervals/trials/correct_reach tells you the result of our algorithm for determining whether this reach looked like the other reaches for this condition. To get it, we correlated the hand velocity for every pair of trials with that condition, accepted the reach with the most high correlations as prototypical, then marked as “consistent” only reaches that had a high enough correlation with the prototypical reach.
== intervals/trials/maze_condition The set of 27 (or 108) mazes included was composed of 3 (or 12) “subsets”. Each subset contained 3 related mazes. Each maze had 3 “versions”: the 3-target with barrier, the 1-target with barriers, and the 1-target with no barriers. These 3 versions shared the same target positions. The 3-target and 1-target versions also shared the same barrier positions. In the 3-target version, exactly one target was accessible 
== intervals/trials/discard_trial flag that will usually be 0, but is set to 1 if there was a photo box problem (meaning RT can't be calculated accurately) or we had a hand tracking error during the movement. In general, throw those trials away.
== intervals/trials/trial_type trial type
== intervals/trials/timeseries index into a TimeSeries object
== processing/ecephys/Processed/A001 LFP signal for array A, segment 1. Array A shares a clock with the trials and spikes, and is placed at the offset applied to this segment's trials. Array B was recorded by a second system whose clock runs slightly slower; its timestamps map it onto array A's clock using the trial start times recorded by both systems.
== processing/ecephys/Processed/B001 LFP signal for array B, segment 1. Array A shares a clock with the trials and spikes, and is placed at the offset applied to this segment's trials. Array B was recorded by a second system whose clock runs slightly slower; its timestamps map it onto array A's clock using the trial start times recorded by both systems.
== processing/behavior/Position/Hand x,y position of the hand in m
[... 29 more lines not kept]
```

**Agent**

Key early finding: the Units table now holds unsorted threshold crossings, one per electrode (192 per session), not the paper's 146/218 sorted isolations. Next I time reading the spikes.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t.py <<'EOF'
import h5py, remfile, requests, sys, time, numpy as np, resource
aid=sys.argv[1]
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3),'r')
st=f['units/spike_times']; print(st.chunks, st.compression, st.shape)
x=st[:5_000_000]; print('5M', time.time()-t)
tr=f['intervals/trials']; 
cols={k:tr[k][:] for k in ['start_time','stop_time','go_cue_time','move_begins_time','offline_move_onset_time','target_presentation_time','task_success','correct_reach','discard_trial','maze_condition','trial_type','trial_version','novel_maze','unhittable']}
print('trials',time.time()-t)
ht=f['processing/behavior/Position/Hand/timestamps']; print(ht.chunks, ht.compression)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
import pandas as pd; d=pd.DataFrame(cols); print(d.describe().T.to_string())
EOF
python t.py 75013796-4a2d-41dc-9eb6-db9d365b28b4
```

```
(1250000,) gzip (66676824,)
5M 1.824275016784668
trials 1.8917510509490967
(1250000,) gzip
0.147352 GB
                           count         mean          std       min          25%          50%           75%           max
start_time                2636.0  7524.402877  4549.852863  4.707200  3575.819667  7340.342667  11527.854841  15703.318791
stop_time                 2636.0  7528.070366  4549.854687  8.567133  3579.533325  7344.217650  11531.381091  15707.218791
go_cue_time               2636.0  7525.848341  4549.860280  6.517200  3577.352667  7341.641167  11529.358091  15704.416791
move_begins_time          2636.0  7526.284156  4549.848927  6.819200  3577.752917  7342.467167  11529.660591  15704.970791
offline_move_onset_time   2636.0  7526.260711  4549.849814  6.793200  3577.726417  7342.443167  11529.637341  15704.941791
target_presentation_time  2636.0  7525.208073  4549.853830  5.570200  3576.609917  7341.093667  11528.623591  15704.003791
task_success              2636.0     0.974962     0.156270  0.000000     1.000000     1.000000      1.000000      1.000000
correct_reach             2636.0     0.871017     0.335245  0.000000     1.000000     1.000000      1.000000      1.000000
discard_trial             2636.0     0.000000     0.000000  0.000000     0.000000     0.000000      0.000000      0.000000
maze_condition            2636.0    49.811836    32.843639  0.000000    21.000000    49.000000     78.000000    108.000000
trial_type                2636.0    19.768209    11.112421  0.000000    10.000000    20.000000     29.000000     39.000000
trial_version             2636.0     1.004552     0.815399  0.000000     0.000000     1.000000      2.000000      2.000000
novel_maze                2636.0     0.000759     0.027540  0.000000     0.000000     0.000000      0.000000      1.000000
unhittable                2636.0     0.076252     0.265451  0.000000     0.000000     0.000000      0.000000      1.000000
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > all.py <<'EOF'
import h5py, remfile, requests, numpy as np, json, hashlib
V="0.261122.2046"
a=requests.get(f"https://api.dandiarchive.org/api/dandisets/000070/versions/{V}/assets/?page_size=100").json()['results']
for x in sorted(a,key=lambda x:x['path']):
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r'); tr=f['intervals/trials']
    st=tr['start_time'][:]; mc=tr['maze_condition'][:]; ok=(tr['task_success'][:]==1)&(tr['correct_reach'][:]==1)
    gc=tr['go_cue_time'][:]; tp=tr['target_presentation_time'][:]; d=gc-tp
    sel=ok&(d>0.4)&(mc>0)
    si=f['units/spike_times_index'][:]
    nsp=f['units/spike_times'].shape[0]
    eg=[f[r].name.split('/')[-1] for r in f['units/electrode_group'][:]]
    print(x['path'].split('/')[-1], 'trials',len(st),'mono',bool(np.all(np.diff(st)>0)),'conds',len(np.unique(mc[mc>0])),'sel',sel.sum(),'selconds',len(np.unique(mc[sel])),
      'units',len(si),'groups',{g:eg.count(g) for g in set(eg)},'spikes',nsp,'idx0',si[0],'idx_mono',bool(np.all(np.diff(si)>=0)),
      'delay[min,med,max]',np.round([d.min(),np.median(d),d.max()],3),'hash',hashlib.md5(st.tobytes()).hexdigest()[:8], hashlib.md5(si.tobytes()).hexdigest()[:8],
      'proc',list(f['processing/ecephys/Processed'].keys()) if 'processing/ecephys' in f else None, 'start',f['session_start_time'][()], flush=True)
EOF
time python all.py
```

```
Exit code 1
sub-Jenkins_ses-20090912_behavior+ecephys.nwb trials 1588 mono True conds 27 sel 563 selconds 27 units 192 groups {'2': 96, '1': 96} spikes 44869604 idx0 129133 idx_mono True delay[min,med,max] [-0.004  0.481  0.998] hash 226b0db0 4f5f9693 proc ['A001', 'A002', 'B001', 'B002'] start b'2009-09-12T00:00:00-07:00'
sub-Jenkins_ses-20090916_behavior+ecephys.nwb trials 2265 mono True conds 27 sel 790 selconds 27 units 192 groups {'2': 96, '1': 96} spikes 61693399 idx0 474959 idx_mono True delay[min,med,max] [-0.004  0.497  0.998] hash 25b77c8a 73e6ad8a proc ['A001', 'A002', 'B001', 'B002'] start b'2009-09-16T00:00:00-07:00'
sub-Jenkins_ses-20090918_behavior+ecephys.nwb trials 2636 mono True conds 108 sel 1980 selconds 108 units 192 groups {'2': 96, '1': 96} spikes 66676824 idx0 257638 idx_mono True delay[min,med,max] [-0.004  0.664  0.998] hash 7234a33c f5f7eacc proc ['A001', 'A002', 'B001', 'B002'] start b'2009-09-18T00:00:00-07:00'
sub-Jenkins_ses-20090923_behavior+ecephys.nwb trials 2327 mono True conds 27 sel 829 selconds 27 units 192 groups {'2': 96, '1': 96} spikes 50009289 idx0 263162 idx_mono True delay[min,med,max] [-0.004  0.498  0.999] hash 7f9d0d59 ea7af84d proc ['A001', 'A002', 'B001', 'B002'] start b'2009-09-23T00:00:00-07:00'
sub-Nitschke_ses-20100812_behavior+ecephys.nwb trials 3038 mono True conds 27 sel 1312 selconds 27 units 192 groups {'2': 96, '1': 96} spikes 89773340 idx0 353739 idx_mono True delay[min,med,max] [-0.003  0.581  0.998] hash b0761894 a07c7b4c proc ['A001', 'A002', 'A003', 'B001', 'B002', 'B003'] start b'2010-08-12T00:00:00-07:00'
sub-Nitschke_ses-20100819_behavior+ecephys.nwb trials 3126 mono True conds 27 sel 134 selconds 27 units 192 groups {'2': 96, '1': 96} spikes 77347550 idx0 286761 idx_mono True delay[min,med,max] [-0.003 -0.002  0.998] hash 6b2236ee a361c595 proc ['A001', 'A002', 'A003', 'B001', 'B002', 'B003'] start b'2010-08-19T00:00:00-07:00'
sub-Nitschke_ses-20100910_behavior+ecephys.nwb trials 2911 mono True con
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > rest.py <<'EOF'
import h5py, remfile, requests, numpy as np
for aid,p in [('3814a1df-0694-463d-b8b4-2c2e1d34c1d9','N20100920'),('67b74fce-dacd-4e10-8055-493ad041cea5','N20100922'),('1b8d9330-6052-4a43-854f-c63eaa826acd','N20100923')]:
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r'); tr=f['intervals/trials']
    print(p, list(tr.attrs['colnames']), tr['start_time'].shape, f['units/spike_times'].shape, f['units'].attrs['description'])
    for k in tr.keys():
        if k not in tr.attrs['colnames'] and not k.endswith('_index') and k!='id': print('  extra',k)
    st=tr['start_time'][:]; print(' mono', np.all(np.diff(st)>0), st.min(), st.max())
    if 'maze_condition' in tr:
        mc=tr['maze_condition'][:]; ok=(tr['task_success'][:]==1)&(tr['correct_reach'][:]==1); d=tr['go_cue_time'][:]-tr['target_presentation_time'][:]
        sel=ok&(d>0.4)&(mc>0); print(' conds',len(np.unique(mc[mc>0])),'sel',sel.sum(),len(np.unique(mc[sel])),'delay med',np.median(d))
    si=f['units/spike_times_index'][:]; print(' idx0',si[0],'mono',np.all(np.diff(si)>=0), 'proc', list(f['processing/ecephys/Processed'].keys()))
EOF
python rest.py
```

```
N20100920 ['start_time', 'stop_time', 'target_presentation_time', 'go_cue_time', 'reaction_time', 'move_begins_time', 'move_ends_time', 'offline_move_onset_time', 'offline_reaction_time', 'discard_trial', 'task_success', 'trial_type', 'maze_num_targets', 'maze_num_barriers', 'target_positions', 'frame_details', 'hit_target_position', 'target_size', 'cursor_offset', 'barrier_info', 'timeseries'] (4044,) (81387912,) Threshold crossings on each electrode, not sorted (Blackrock unit code 0), one unit per electrode. Spike times were saved for each trial only, so obs_intervals are the trials.
 mono True 3.7712000000000003 20295.019540756497
 idx0 342705 mono True proc ['A001', 'A002', 'A003', 'B001', 'B002', 'B003']
N20100922 ['start_time', 'stop_time', 'target_presentation_time', 'go_cue_time', 'reaction_time', 'move_begins_time', 'move_ends_time', 'offline_move_onset_time', 'offline_reaction_time', 'discard_trial', 'task_success', 'trial_type', 'maze_num_targets', 'maze_num_barriers', 'target_positions', 'frame_details', 'hit_target_position', 'target_size', 'cursor_offset', 'barrier_info', 'timeseries'] (2612,) (66829586,) Threshold crossings on each electrode, not sorted (Blackrock unit code 0), one unit per electrode. Spike times were saved for each trial only, so obs_intervals are the trials.
 mono True 2.517466666666667 14633.945614268123
 idx0 292306 mono True proc ['A001', 'A002', 'B001', 'B002']
N20100923 ['start_time', 'stop_time', 'target_presentation_time', 'go_cue_time', 'reaction_time', 'move_begins_time', 'move_ends_time', 'offline_move_onset_time', 'offline_reaction_time', 'discard_trial', 'task_success', 'trial_type', 'trial_version', 'active_target', 'unhittable', 'proto_trial', 'maze_condition', 'correct_reach', 'maze_num_targets', 'maze_num_barriers', 'novel_maze', 'target_positions', 'frame_details', 'hit_target_position', 'target_size', 'cursor_offset', 'barrier_info', 'timeseries'] (3694,) (111572823,) Threshold crossings on each electrode, not sor
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > hand.py <<'EOF'
import h5py, remfile, requests, numpy as np, time
s3=requests.head("https://api.dandiarchive.org/api/assets/75013796-4a2d-41dc-9eb6-db9d365b28b4/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r'); t=time.time()
ts=f['processing/behavior/Position/Hand/timestamps'][:]; print(time.time()-t, ts[:5], np.median(np.diff(ts)), np.all(np.diff(ts)>0))
h=f['processing/behavior/Position/Hand/data'][:2000000]; print(time.time()-t, np.nanmin(h,0), np.nanmax(h,0), np.isnan(h).mean())
tr=f['intervals/trials']; print(tr['hit_target_position'][:5], tr['cursor_offset'][:5], tr['target_positions'][:6])
mo=tr['offline_move_onset_time'][:]; mb=tr['move_begins_time'][:]; print(np.percentile(mo-mb,[1,25,50,75,99]))
print(tr['reaction_time'][:5], tr['offline_reaction_time'][:5], (mo-tr['go_cue_time'][:])[:5])
EOF
python hand.py
```

```
1.2224161624908447 [4.7072 4.7082 4.7092 4.7102 4.7112] 0.0010000000002037268 True
2.8907809257507324 [-138.82442309 -218.80537028] [155.73632394  97.88246293] 0.0
[[-130.  -57.]
 [ 120.   70.]
 [ -77.   82.]
 [ 132.   56.]
 [   2.   82.]] [[ 0. 35.]
 [ 0. 35.]
 [ 0. 35.]
 [ 0. 35.]
 [ 0. 35.]] [[-130  -57]
 [ 120   70]
 [ -77   82]
 [ 132   56]
 [   2   82]
 [-118  -83]]
[-0.041 -0.028 -0.025 -0.022  0.012]
[0.335 0.305 0.3   0.305 0.3  ] [0.276 0.25  0.24  0.246 0.243] [0.276 0.25  0.24  0.246 0.243]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/churchland-2012/reach.py",
 "content": "\"\"\"Loading and jPCA measures for Churchland et al. (2012) on dandiset 000070.\n\nSources of the parameters (paper = doi:10.1038/nature11129, text under paper/;\nclaims = claims/churchland-2012.yaml; codepack = the jPCA code the claims file\ncites, bantin/jPCA at commit 3f8be9f, a port of the authors' MATLAB codepack):\n\n- Trial selection: successful trials (`task_success`), consistent reaches\n  (`correct_reach`), delay above 400 ms, conditions 1 to 108 (claims, header;\n  Methods, \"Only trials with delays >400 ms were analyzed\"). Trials flagged\n  `discard_trial` are also left out, as the file's own description of that\n  column says to do (standard choice; no trial of the two main sessions is\n  flagged).\n- Rates: condition averages of the trials' spikes, aligned on movement onset,\n  smoothed with a Gaussian of 20 ms SD (claims, header; Methods, \"filtering\n  with a Gaussian (20 or 24 ms depending on the dataset)\"). The movement onset\n  column is open: `offline_move_onset_time` (\"calculated offline using a\n  robust algorithm\") is the main reading and `move_begins_time` the other.\n- Soft normalisation by range + 5 spikes/s, cross-condition mean subtracted,\n  PCA and jPCA on -50 to +150 ms every 10 ms, 6 PCs, derivative as the\n  difference of adjacent samples, R2 as one minus residual over total sum of\n  squares (claims, header; Methods, \"Projections that capture rotational\n  structure\"). The window over which the range is taken is open: the codepack\n  takes it over all the times it is given; here the main reading takes it over\n  the analysed window and the other over -1000 to +700 ms.\n- Plane orientation: jPC1 along the largest spread of the states at the first\n  analysed time, and jPC2 so that the plane's fitted rotation is\n  counter-clockwise (Methods: \"selected jPC1 and jPC2 so that any net rotation\n  was counter-clockwise ... and so that the spread of preparatory states was\n  strongest along jPC1\").\n- Shuffles: supplementary figure 2 legend (dividing point 50 ms after the go\n  cue; inversion around the dividing point per neuron; reassignment of\n  peri-movement activity, the same for all neurons, appended to the final\n  preparatory rate).\n- Simulated populations: Methods, \"Simulated neural data\". The lag of the\n  rates behind... ahead of the hand, the time course of the preparatory term\n  and the relative weights of the factors are not given; they are assumptions,\n  stated in `simulate_population`.\n- Spikes are binned at 1 ms (a standard choice that cannot change a result at\n  the 10 ms sampling used).\n\"\"\"\nimport numpy as np\nimport h5py\nimport remfile\nimport requests\nimport pandas as pd\n\nDANDISET = \"000070\"\nVERSION = \"0.261122.2046\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nSESSIONS = {\n    \"J-array\": \"sub-Jenkins/sub-Jenkins_ses-20090918_behavior+ecephys.nwb\",\n    \"N-array\": \"sub-Nitschke/sub-Nitschke_ses-20100923_behavior+ecephys.nwb\",\n    \"N-9-10-2010\": \"sub-Nitschke/sub-Nitschke_ses-20100910_behavior+ecephys.nwb\",\n}\n\n# Rates are kept from T0 to T1 ms around movement onset, at 1 ms.\nT0, T1 = -1000, 700\nPAD = 100            # ms of spikes kept on each side for smoothing\nSMOOTH_SD = 20.0     # ms (claims, header)\nANALYSIS = (-50, 150, 10)   # ms: start, stop (inclusive), step (claims, header)\nSOFT_NORM = 5.0      # spikes/s (claims, header)\n\n\ndef list_assets():\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        out += r[\"results\"]\n        url = r.get(\"next\")\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef version_metadata():\n    return requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/\", timeout=60).json()\n\n\ndef open_asset(path):\n    \"\"\"Stream one NWB file of the pinned version (no download to disk).\"\"\"\n    assets = {a[\"path\"]: a for a in list_assets()}\n    aid = assets[path][\"asset_id\"]\n    s3 = requests.head(f\"{API}/assets/{aid}/download/\", allow_redirects=True, timeout=60).url\n    return h5py.File(remfile.File(s3), \"r\")\n\n\nTRIAL_COLS = [\"start_time\", \"stop_time\", \"target_presentation_time\", \"go_cue_time\",\n              \"move_begins_time\", \"offline_move_onset_time\", \"move_ends_time\",\n              \"task_success\", \"correct_reach\", \"discard_trial\", \"maze_condition\",\n              \"trial_version\", \"maze_num_targets\", \"maze_num_barriers\"]\n\n\ndef load_trials(f):\n    tr = f[\"intervals/trials\"]\n    d = pd.DataFrame({c: tr[c][:] for c in TRIAL_COLS if c in tr})\n    d[\"hit_x\"], d[\"hit_y\"] = tr[\"hit_target_position\"][:].T\n    d[\"cursor_dx\"], d[\"cursor_dy\"] = tr[\"cursor_offset\"][:].T\n    d[\"delay\"] = d.go_cue_time - d.target_presentation_time\n    return d\n\n\ndef select_trials(d):\n    \"\"\"The Methods' selection (see module docstring).\"\"\"\n    return ((d.task_success == 1) & (d.correct_reach == 1) & (d.discard_trial == 0)\n            & (d.delay > 0.4) & (d.maze_condition >= 1) & (d.maze_condition <= 108))\n\n\ndef unit_groups(f):\n    \"\"\"Electrode group name of each unit ('1' PMd, '2' M1 in these files).\"\"\"\n    return np.array([f[r].name.split(\"/\")[-1] for r in f[\"units/electrode_group\"][:]])\n\n\ndef load_rates(f, trials, onset_cols=(\"offline_move_onset_time\", \"move_begins_time\"),\n               target_bins=(-500, 500, 50), move_bins=(-1000, 700, 50)):\n    \"\"\"Condition-mean spike counts at 1 ms, aligned on each movement onset column.\n\n    Returns a dict with, per onset column, `sum` (units x conditions x ms) of\n    spike counts summed over trials, `n` trials per condition, and per-trial\n    counts in 50 ms bins aligned on target onset and on movement onset (for\n    the clock check). Spikes are read one unit at a time.\n    \"\"\"\n    si = f[\"units/spike_times_index\"][:]\n    st = f[\"units/spike_times\"]\n    nu = len(si)\n    conds = trials.maze_condition.values.astype(int)\n    cidx = conds - 1\n    ncond = 108\n    nbin = (T1 - T0) + 2 * PAD\n    out = {\"units_unsorted\": 0, \"outside_trial\": {}}\n    for col in onset_cols:\n        out[col] = {\"sum\": np.zeros((nu, ncond, nbin), np.float32),\n                    \"n\": np.bincount(cidx, minlength=ncond)}\n    tb = np.arange(*target_bins) / 1000.0\n    mb = np.arange(*move_bins) / 1000.0\n    tgt = trials.target_presentation_time.values\n    mov = trials.offline_move_onset_time.values\n    out[\"target_counts\"] = np.zeros((len(trials), nu, len(tb)), np.uint16)\n    out[\"move_counts\"] = np.zeros((len(trials), nu, len(mb)), np.uint16)\n    for col in onset_cols:\n        a = trials[col].values\n        lo = a + (T0 - PAD) / 1000.0\n        hi = a + (T1 + PAD) / 1000.0\n        out[\"outside_trial\"][col] = int(np.sum((lo < trials.start_time.values) | (hi > trials.stop_time.values)))\n    start = 0\n    for u in range(nu):\n        s = st[start:si[u]]\n        start = si[u]\n        if np.any(np.diff(s) < 0):\n            out[\"units_unsorted\"] += 1\n            s = np.sort(s)\n        for col in onset_cols:\n            a = trials[col].values\n            lo = np.searchsorted(s, a + (T0 - PAD) / 1000.0)\n            hi = np.searchsorted(s, a + (T1 + PAD) / 1000.0)\n            cnt = hi - lo\n            if cnt.sum() == 0:\n                continue\n            tri = np.repeat(np.arange(len(a)), cnt)\n            idx = np.concatenate([np.arange(l, h) for l, h in zip(lo, hi)])\n            b = np.floor((s[idx] - a[tri]) * 1000.0 - (T0 - PAD)).astype(int)\n            b = np.clip(b, 0, nbin - 1)\n            np.add.at(out[col][\"sum\"][u], (cidx[tri], b), 1)\n        for key, ref, edges in ((\"target_counts\", tgt, tb), (\"move_counts\", mov, mb)):\n            w = edges[1] - edges[0]\n            l = np.searchsorted(s, ref + edges[0])\n            h = np.searchsorted(s, ref + edges[-1] + w)\n            cnt = h - l\n            tri = np.repeat(np.arange(len(ref)), cnt)\n            idx = np.concatenate([np.arange(x, y) for x, y in zip(l, h)]) if cnt.sum() else np.array([], int)\n            b = np.floor((s[idx] - ref[tri] - edges[0]) / w + 1e-9).astype(int)\n            ok = (b >= 0) & (b < len(edges))\n            np.add.at(out[key][:, u, :], (tri[ok], b[ok]), 1)\n    out[\"target_edges\"] = tb\n    out[\"move_edges\"] = mb\n    return out\n\n\ndef smooth_rates(sum_counts, n, sd=SMOOTH_SD):\n    \"\"\"Gaussian-smoothed condition-mean rates (spikes/s) from T0 to T1 at 1 ms.\"\"\"\n    from scipy.ndimage import gaussian_filter1d\n    mean = sum_counts / np.maximum(n, 1)[None, :, None] * 1000.0\n    sm = gaussian_filter1d(mean, sd, axis=2, mode=\"nearest\")\n    return sm[:, :, PAD:PAD + (T1 - T0)]\n\n\ndef ms_index(t_ms):\n    return np.asarray(t_ms) - T0\n\n\ndef load_hand(f, trials, col=\"offline_move_onset_time\", t0=-200, t1=700):\n    \"\"\"Hand position (mm) from t0 to t1 ms around movement onset, per trial, at 1 ms.\"\"\"\n    ts = f[\"processing/behavior/Position/Hand/timestamps\"][:]\n    a = trials[col].values\n    lo = np.searchsorted(ts, a + t0 / 1000.0 - 0.005)\n    hi = np.searchsorted(ts, a + t1 / 1000.0 + 0.005)\n    grid = np.arange(t0, t1) / 1000.0\n    out = np.full((len(a), len(grid), 2), np.nan)\n    hd = f[\"processing/behavior/Position/Hand/data\"]\n    for i in range(len(a)):\n        if hi[i] - lo[i] < 10:\n            continue\n        x = hd[lo[i]:hi[i]]\n        tt = ts[lo[i]:hi[i]] - a[i]\n        for k in range(2):\n            out[i, :, k] = np.interp(grid, tt, x[:, k], left=np.nan, right=np.nan)\n    return out, np.arange(t0, t1)\n\n\n# ----------------------------------------------------------------------------\n# jPCA\n\ndef analysis_times():\n    s, e, d = ANALYSIS\n    return np.arange(s, e + 1, d)\n\n\ndef preprocess(rates, norm_window=None, times=None):\n    \"\"\"Soft-normalise, subtract the cross-condition mean, cut the analysed times.\n\n    rates: units x conditions x ms (T0..T1). norm_window: (start, stop) in ms for\n    the firing-rate range; None for the analysed window. Returns units x\n    conditions x analysed times.\n    \"\"\"\n    times = analysis_times() if times is None else times\n    if norm_window is None:\n        rng_src = rates[:, :, ms_index(times)]\n    else:\n        rng_src = rates[:, :, ms_index(norm_window[0]):ms_index(norm_window[1])]\n    rng = rng_src.max(axis=(1, 2)) - rng_src.min(axis=(1, 2))\n    r = rates / (rng + SOFT_NORM)[:, None, None]\n    r = r - r.mean(axis=1, keepdims=True)\n    return r[:, :, ms_index(times)]\n\n\ndef pca(X, k):\n    \"\"\"X: units x conditions x times. Returns scores (k x c x t), loadings, total variance.\"\"\"\n    n, c, t = X.shape\n    A = X.reshape(n, c * t).T\n    A = A - A.mean(axis=0)\n    U, S, Vt = np.linalg.svd(A, full_matrices=False)\n    var = S ** 2 / (A.shape[0] - 1)\n    total = var.sum()\n    scores = (A @ Vt[:k].T).T.reshape(k, c, t)\n    return scores, Vt[:k], var, total\n\n\ndef state_and_derivative(Z):\n    \"\"\"Z: k x c x t. Returns states (k x N) without each condition's last time, and differences.\"\"\"\n    k = Z.shape[0]\n    Xs = Z[:, :, :-1].reshape(k, -1)\n    dX = np.diff(Z, axis=2).reshape(k, -1)\n    return Xs, dX\n\n\ndef fit_M(X, dX):\n    M, *_ = np.linalg.lstsq(X.T, dX.T, rcond=None)\n    return M.T\n\n\ndef fit_Mskew(X, dX):\n    k = X.shape[0]\n    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]\n    N = X.shape[1]\n    H = np.zeros((k * N, len(pairs)))\n    for p, (i, j) in enumerate(pairs):\n        # M[i, j] = +m, M[j, i] = -m ; dX[i] += m X[j], dX[j] -= m X[i]\n        H[i * N:(i + 1) * N, p] = X[j]\n        H[j * N:(j + 1) * N, p] = -X[i]\n    m, *_ = np.linalg.lstsq(H, dX.reshape(-1), rcond=None)\n    M = np.zeros((k, k))\n    for p, (i, j) in enumerate(pairs):\n        M[i, j] = m[p]\n        M[j, i] = -m[p]\n    return M\n\n\ndef r2(M, X, dX):\n    res = dX - M @ X\n    tot = dX - dX.mean(axis=1, keepdims=True)\n    return 1.0 - np.sum(res ** 2) / np.sum(tot ** 2)\n\n\ndef jpca(X, k=6, n_planes=1):\n    \"\"\"jPCA as in the Methods. X: units x conditions x analysed times (preprocessed).\n\n    Returns a dict: planes (list of 2 x c x t projections), the planes' basis in\n    PC space, the variance each plane captures (fraction of total), the PCs'\n    variance fractions, M, M_skew, R2 values, and eigenvalues of M_skew.\n    \"\"\"\n    scores, load, var, total = pca(X, k)\n    Xs, dX = state_and_derivative(scores)\n    M = fit_M(Xs, dX)\n    Mk = fit_Mskew(Xs, dX)\n    ev, V = np.linalg.eig(Mk)\n    order = np.argsort(-np.abs(ev.imag) - 1e-9 * ev.imag)   # +i w before -i w\n    planes, bases, pvar, freqs = [], [], [], []\n    used = []\n    for idx in order:\n        if len(planes) >= n_planes:\n            break\n        if any(np.isclose(ev[idx], np.conj(ev[u])) or np.isclose(ev[idx], ev[u]) for u in used):\n            continue\n        used.append(idx)\n        v1 = V[:, idx]\n        v2 = np.conj(v1)\n        if np.sign(v1.real.sum()) != np.sign(v2.real.sum()):\n            v2 = -v2\n        j1 = (v1 + v2).real\n        j2 = (1j * (v1 - v2)).real\n        j1 /= np.linalg.norm(j1)\n        j2 -= j1 * (j1 @ j2)\n        j2 /= np.linalg.norm(j2)\n        P = np.stack([j1, j2])                      # 2 x k\n        Z = np.tensordot(P, scores, axes=(1, 0))    # 2 x c x t\n        # jPC1 along the largest spread of the first-time states\n        z0 = Z[:, :, 0] - Z[:, :, 0].mean(axis=1, keepdims=True)\n        w, U = np.linalg.eigh(z0 @ z0.T)\n        u = U[:, np.argmax(w)]\n        th = np.arctan2(u[1], u[0])\n        R = np.array([[np.cos(th), np.sin(th)], [-np.sin(th), np.cos(th)]])\n        P = R @ P\n        # counter-clockwise: the plane's skew dynamics dx2/dt = +w x1\n        if (P @ Mk @ P.T)[1, 0] < 0:\n            P[1] = -P[1]\n        Z = np.tensordot(P, scores, axes=(1, 0))\n        planes.append(Z)\n        bases.append(P)\n        pvar.append(np.sum(np.var(Z.reshape(2, -1), axis=1, ddof=1)) / total)\n        freqs.append(abs(ev[idx].imag))\n    out = {\"planes\": planes, \"bases\": bases, \"plane_var\": np.array(pvar),\n           \"pc_var\": var[:k] / total, \"pc_var_all\": var / total, \"M\": M, \"Mskew\": Mk,\n           \"R2_M\": r2(M, Xs, dX), \"R2_skew\": r2(Mk, Xs, dX), \"eig\": ev, \"scores\": scores,\n           \"plane_eig\": np.array(freqs)}\n    # fits within the first plane\n    Z = planes[0]\n    Xp, dXp = state_and_derivative(Z)\n    out[\"R2_M_plane\"] = r2(fit_M(Xp, dXp), Xp, dXp)\n    out[\"R2_skew_plane\"] = r2(fit_Mskew(Xp, dXp), Xp, dXp)\n    return out\n\n\ndef freq_hz(eig_mag, step_ms=ANALYSIS[2]):\n    \"\"\"Eigenvalue magnitude per sample to rad/s and Hz.\"\"\"\n    rad_s = eig_mag * 1000.0 / step_ms\n    return rad_s, rad_s / (2 * np.pi)\n\n\ndef net_rotation(Z):\n    \"\"\"Net change of polar angle (rad) of each condition's state across the window.\"\"\"\n    ang = np.unwrap(np.arctan2(Z[1], Z[0]), axis=1)\n    return ang[:, -1] - ang[:, 0]\n\n\ndef state_derivative_angles(Z):\n    X, dX = state_and_derivative(Z)\n    return np.arctan2(X[0] * dX[1] - X[1] * dX[0], X[0] * dX[0] + X[1] * dX[1])\n\n\ndef angle_peak(angles, bins=36):\n    h, e = np.histogram(angles, bins=bins, range=(-np.pi, np.pi))\n    c = (e[:-1] + e[1:]) / 2\n    return c[np.argmax(h)], h, e\n\n\n# ----------------------------------------------------------------------------\n# Shuffle controls (supplementary figure 2 legend)\n\ndef shuffle_invert(rates, div_ms, conds_mask):\n    \"\"\"Invert the peri-movement pattern around the dividing point.\n\n    rates: units x conditions x ms; conds_mask: units x conditions boolean, the\n    (unit, condition) pairs to invert (per neuron for shuffle 1, all for 2).\n    \"\"\"\n    i = ms_index(div_ms)\n    r = rates.copy()\n    ref = r[:, :, i:i + 1]\n    inv = 2 * ref - r[:, :, i:]\n    r[:, :, i:] = np.where(conds_mask[:, :, None], inv, r[:, :, i:])\n    return r\n\n\ndef shuffle_reassign(rates, div_ms, perm):\n    \"\"\"Give condition c the peri-movement activity of condition perm[c], appended\n    to c's final preparatory rate; the same for all neurons.\"\"\"\n    i = ms_index(div_ms)\n    r = rates.copy()\n    mov = rates[:, perm, i:] - rates[:, perm, i:i + 1]\n    r[:, :, i:] = rates[:, :, i:i + 1] + mov\n    return r\n\n\n# ----------------------------------------------------------------------------\n# Simulated populations (Methods, \"Simulated neural data\")\n\ndef kinematics(hand_mean, t_ms, sd=20.0):\n    \"\"\"Position (m), velocity, acceleration and jerk of condition-mean hand paths.\n\n    hand_mean: conditions x ms x 2 in mm. The path is smoothed with a Gaussian of\n    20 ms SD before differentiating (standard choice).\n    \"\"\"\n    from scipy.ndimage import gaussian_filter1d\n    p = gaussian_filter1d(hand_mean / 1000.0, sd, axis=1, mode=\"nearest\")\n    p = p - p[:, :1, :]\n    v = np.gradient(p, axis=1) * 1000.0\n    a = np.gradient(v, axis=1) * 1000.0\n    j = np.gradient(a, axis=1) * 1000.0\n    return p, v, a, j\n\n\ndef simulate_population(model, kin, t_kin, rates, n_trials, rng, lag_ms=100,\n                        prep_end_ms=-50, prep_fall_ms=100):\n    \"\"\"Simulated spikes for a velocity or complex kinematic population.\n\n    Assumptions (the Methods do not give them): the movement term leads the\n    hand by `lag_ms` (100 ms), the preparatory term holds before movement and\n    falls to zero over `prep_fall_ms` after `prep_end_ms`; before movement the\n    hand kinematics are those at its start. Preferred directions are drawn\n    uniformly for the preparatory and the movement terms (Methods). Velocity\n    model: movement term = velocity along the PD + speed, each factor scaled to\n    unit SD over conditions and times and weighted by a uniform draw on 0 to 1;\n    preparatory term = endpoint along the preparatory PD + peak speed, likewise.\n    Complex kinematic model: the Methods' sensitivities (25, 10, 1, 0.05\n    spikes/s per m, m/s, m/s^2, m/s^3) on position, velocity, acceleration and\n    jerk along the PD; preparatory term 25 spikes/s per m of endpoint along the\n    preparatory PD. Each unit's noiseless rate is then scaled to the recorded\n    unit's mean and range over T0..T1 (Methods: \"matched the overall firing\n    rates ... of each simulated unit to those of the respective recorded\n    neuron\"), rectified, and spikes are drawn from a gamma-interval process of\n    order 2 (Methods) for the recorded number of trials of each condition.\n\n    kin: (p, v, a, j), each conditions x len(t_kin) x 2, t_kin in ms.\n    rates: recorded units x conditions x ms (T0..T1). Returns summed spike counts\n    (units x conditions x ms, padded as load_rates) for smooth_rates.\n    \"\"\"\n    p, v, a, j = kin\n    nu, nc, _ = rates.shape\n    t = np.arange(T0 - PAD, T1 + PAD)\n    # kinematics at time t + lag, held at the ends\n    tk = np.clip(t + lag_ms, t_kin[0], t_kin[-1]) - t_kin[0]\n    P, Vv, A, J = (x[:, tk, :] for x in (p, v, a, j))\n    endpoint = p[:, -1, :]\n    speed = np.linalg.norm(Vv, axis=2)\n    peak_speed = np.linalg.norm(v, axis=2).max(axis=1)\n    w_prep = np.clip(1 - (t - prep_end_ms) / prep_fall_ms, 0, 1)\n    th_m = rng.uniform(0, 2 * np.pi, nu)\n    th_p = rng.uniform(0, 2 * np.pi, nu)\n    um = np.stack([np.cos(th_m), np.sin(th_m)], 1)\n    up = np.stack([np.cos(th_p), np.sin(th_p)], 1)\n    rec_mean = rates.mean(axis=(1, 2))\n    rec_rng = rates.max(axis=(1, 2)) - rates.min(axis=(1, 2))\n    if model == \"velocity\":\n        wv, ws, we, wps = rng.uniform(0, 1, (4, nu))\n        sv = Vv.std()\n        ss = speed.std()\n        se = endpoint.std()\n        sps = peak_speed.std()\n    out = np.zeros((nu, nc, len(t)), np.float32)\n    for u in range(nu):\n        if model == \"velocity\":\n            mov = wv[u] * (Vv @ um[u]) / sv + ws[u] * speed / ss\n            prep = we[u] * (endpoint @ up[u]) / se + wps[u] * peak_speed / sps\n        elif model == \"complex\":\n            mov = 25 * (P @ um[u]) + 10 * (Vv @ um[u]) + 1 * (A @ um[u]) + 0.05 * (J @ um[u])\n            prep = 25 * (endpoint @ up[u])\n        else:\n            raise ValueError(model)\n        r = mov * (1 - w_prep)[None, :] + prep[:, None] * w_prep[None, :]\n        core = r[:, PAD:PAD + (T1 - T0)]\n        rr = core.max() - core.min()\n        r = (r - core.mean()) / (rr if rr > 0 else 1) * rec_rng[u] + rec_mean[u]\n        r = np.clip(r, 0, None)\n        out[u] = gamma_spikes(r, n_trials, rng)\n    return out\n\n\ndef gamma_spikes(r, n_trials, rng, order=2):\n    \"\"\"Summed spike counts (conditions x ms) of a gamma-interval process.\n\n    r: conditions x ms (spikes/s); n_trials: trials per condition. Spikes are\n    drawn by time rescaling: intervals Gamma(order, 1/order) in units of the\n    integrated rate, with a random phase at the start.\n    \"\"\"\n    nc, nt = r.shape\n    lam = np.cumsum(r, axis=1) / 1000.0\n    out = np.zeros((nc, nt), np.float32)\n    for c in range(nc):\n        n = int(n_trials[c])\n        if n == 0:\n            continue\n        L = lam[c, -1]\n        m = int(L + 6 * np.sqrt(L + 1) + 10)\n        isi = rng.gamma(order, 1.0 / order, size=(n, m))\n        isi[:, 0] *= rng.uniform(0, 1, n)\n        cs = np.cumsum(isi, axis=1)\n        cs = cs[cs < L]\n        b = np.searchsorted(lam[c], cs)\n        out[c] = np.bincount(b, minlength=nt)[:nt]\n    return out\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/churchland-2012/reach.py",
 "old_string": "  peri-movement activity, the same for all neurons, appended to the final\n  preparatory rate).\n- Simulated populations: Methods, \"Simulated neural data\". The lag of the\n  rates behind... ahead of the hand, the time course of the preparatory term\n  and the relative weights of the factors are not given; they are assumptions,\n  stated in `simulate_population`.",
 "new_string": "  peri-movement activity, the same for all neurons, appended to the final\n  preparatory rate).\n- Simulated populations: Methods, \"Simulated neural data\". How far the rates\n  lead the hand, the time course of the preparatory term and the relative\n  weights of the factors are not given; they are assumptions, stated in\n  `simulate_population`."
}
```

```
The file entries/churchland-2012/reach.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now a first test on J-array: load rates, time it, and run jPCA.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import sys, time, resource, numpy as np, pickle
sys.path.insert(0,'entries/churchland-2012')
import reach as R
t=time.time()
f=R.open_asset(R.SESSIONS['J-array'])
d=R.load_trials(f); sel=R.select_trials(d); tr=d[sel].reset_index(drop=True)
print(len(d), sel.sum(), time.time()-t)
L=R.load_rates(f, tr); print('rates', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, L['units_unsorted'], L['outside_trial'])
pickle.dump((tr,L),open('J.pkl','wb'))
EOF
python t1.py
```

```
2636 1980 1.7401213645935059
rates 28.97705388069153 0.79058 0 {'offline_move_onset_time': 0, 'move_begins_time': 0}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, time, numpy as np, pickle
sys.path.insert(0,'entries/churchland-2012')
import reach as R
tr,L=pickle.load(open('J.pkl','rb'))
for col in ['offline_move_onset_time','move_begins_time']:
  rates=R.smooth_rates(L[col]['sum'],L[col]['n'])
  print(col, rates.shape, rates.mean(), rates.max())
  for nw in [None,(-1000,700)]:
    X=R.preprocess(rates,nw)
    o=R.jpca(X,6)
    Z=o['planes'][0]; nr=R.net_rotation(Z)
    pk,_,_=R.angle_peak(R.state_derivative_angles(Z))
    print(nw, 'plane var %.3f pc2+3 %.3f'%(o['plane_var'][0], o['pc_var'][1:3].sum()), 'ccw %.3f'%(nr>0).mean(), 'R2 M %.3f skew %.3f ratio %.3f | plane %.3f %.3f ratio %.3f'%(o['R2_M'],o['R2_skew'],o['R2_skew']/o['R2_M'],o['R2_M_plane'],o['R2_skew_plane'],o['R2_skew_plane']/o['R2_M_plane']),
      'freq Hz %.2f'%R.freq_hz(np.abs(o['eig']).max())[1], 'peak/pi %.2f'%(pk/np.pi))
    o10=R.jpca(X,10,3); print('  10pc planes', np.round(o10['plane_var'],3), o10['plane_var'].sum(), 'top6', o10['pc_var_all'][:6].sum(), [ (R.net_rotation(z)>0).mean() for z in o10['planes']])
EOF
python t2.py
```

```
offline_move_onset_time (192, 108, 1700) 39.592384008699604 280.21664792619
None plane var 0.149 pc2+3 0.192 ccw 0.954 R2 M 0.415 skew 0.381 ratio 0.918 | plane 0.554 0.524 ratio 0.946 freq Hz 1.34 peak/pi 0.53
  10pc planes [0.133 0.133 0.122] 0.3881675543838219 top6 0.519391058618671 [np.float64(0.9814814814814815), np.float64(0.9722222222222222), np.float64(0.9166666666666666)]
(-1000, 700) plane var 0.150 pc2+3 0.195 ccw 0.954 R2 M 0.414 skew 0.378 ratio 0.914 | plane 0.542 0.515 ratio 0.950 freq Hz 1.33 peak/pi 0.53
  10pc planes [0.138 0.128 0.122] 0.38843882394248624 top6 0.5314152970634797 [np.float64(0.9907407407407407), np.float64(0.9166666666666666), np.float64(0.9351851851851852)]
move_begins_time (192, 108, 1700) 39.59686213214153 279.6779500910738
None plane var 0.187 pc2+3 0.199 ccw 0.963 R2 M 0.373 skew 0.345 ratio 0.925 | plane 0.496 0.480 ratio 0.967 freq Hz 1.10 peak/pi 0.58
  10pc planes [0.127 0.138 0.113] 0.37740182462007255 top6 0.5249007992879489 [np.float64(0.9907407407407407), np.float64(0.9814814814814815), np.float64(0.9166666666666666)]
(-1000, 700) plane var 0.190 pc2+3 0.201 ccw 0.944 R2 M 0.365 skew 0.340 ratio 0.931 | plane 0.470 0.458 ratio 0.975 freq Hz 1.06 peak/pi 0.58
  10pc planes [0.126 0.138 0.113] 0.3769517795023857 top6 0.539916383780881 [np.float64(1.0), np.float64(0.9814814814814815), np.float64(0.9074074074074074)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > t3.py <<'EOF'
import sys, time, numpy as np, pickle, zlib
sys.path.insert(0,'entries/churchland-2012')
import reach as R
tr,L=pickle.load(open('J.pkl','rb'))
t=time.time()
f=R.open_asset(R.SESSIONS['J-array'])
H,th=R.load_hand(f,tr); print('hand',time.time()-t, np.isnan(H).any(axis=(1,2)).sum())
pickle.dump((H,th),open('Jhand.pkl','wb'))
sp=np.linalg.norm(np.gradient(H,axis=1),axis=2)*1000
print('speed mm/s at', [ (tt, np.nanmedian(sp[:,th==tt])) for tt in [-150,-100,-50,0,50,100,200,300,500]])
EOF
python t3.py
```

```
Tue Nov 24 23:26:08 UTC 2026
hand 6.168582201004028 0
speed mm/s at [(-150, np.float64(1.9552369037906516)), (-100, np.float64(1.978543420410524)), (-50, np.float64(5.166325325509954)), (0, np.float64(43.32091414171764)), (50, np.float64(336.69433362384245)), (100, np.float64(667.7793035223184)), (200, np.float64(587.7580494398808)), (300, np.float64(333.88380353093055)), (500, np.float64(20.850201131340988))]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t4.py <<'EOF'
import sys, time, numpy as np, pickle, zlib
sys.path.insert(0,'entries/churchland-2012')
import reach as R
tr,L=pickle.load(open('J.pkl','rb')); H,th=pickle.load(open('Jhand.pkl','rb'))
col='offline_move_onset_time'
rates=R.smooth_rates(L[col]['sum'],L[col]['n'])
go=np.median((tr.go_cue_time-tr[col]).values)*1000; div=int(round(go+50)); print('go',go,'div',div)
base=R.jpca(R.preprocess(rates),6); print('orig skew',base['R2_skew'])
rng=np.random.default_rng(1)
t=time.time()
for s in range(3):
    m=rng.random((192,108))<0.5
    o=R.jpca(R.preprocess(R.shuffle_invert(rates,div,m)),6); print('s1',o['R2_skew'], (R.net_rotation(o['planes'][0])>0).mean(), o['R2_skew']/o['R2_M'])
o=R.jpca(R.preprocess(R.shuffle_invert(rates,div,np.ones((192,108),bool))),6); print('s2',o['R2_skew'], (R.net_rotation(o['planes'][0])>0).mean(),o['R2_skew']/o['R2_M'])
for s in range(3):
    o=R.jpca(R.preprocess(R.shuffle_reassign(rates,div,rng.permutation(108))),6); print('s3',o['R2_skew'], (R.net_rotation(o['planes'][0])>0).mean(),o['R2_skew']/o['R2_M'])
print('t',time.time()-t)
# phase
Z=base['planes'][0]; z=Z[0]+1j*Z[1]; a=z[:,0]; b=z[:,-1]
pred=np.empty_like(b)
for c in range(108):
    m=np.arange(108)!=c; g=np.sum(np.conj(a[m])*b[m])/np.sum(np.abs(a[m])**2); pred[c]=g*a[c]
print('phase R2', 1-np.sum(np.abs(b-pred)**2)/np.sum(np.abs(b-b.mean())**2))
# curvature
cm=tr.maze_condition.values
Hm=np.stack([np.nanmean(H[cm==c],0) for c in range(1,109)])
v=np.gradient(Hm,axis=1); spd=np.linalg.norm(v,axis=2)
w=(th>=0)&(th<500)
curv=[]
for c in range(108):
    ok=w&(spd[c]>0.1*spd[c][w].max())
    hd=np.unwrap(np.arctan2(v[c,ok,1],v[c,ok,0])); curv.append(np.degrees(hd[-1]-hd[0]))
curv=np.array(curv); print('curv', np.percentile(curv,[0,10,50,90,100]), (curv<-20).sum(), (curv>20).sum(), (abs(curv)<=20).sum())
# sim
t=time.time()
kin=R.kinematics(Hm[:, th>=-200], th[th>=-200])
rngs=np.random.default_rng(5)
for model in ['velocity','complex']:
  S=R.simulate_population(model,kin,th,rates,L[col]['n'],rngs)
  sr=R.smooth_rates(S,L[col]['n'])
  o=R.jpca(R.preprocess(sr),6); pk,_,_=R.angle_peak(R.state_derivative_angles(o['planes'][0]))
  print(model,'ratio',o['R2_skew']/o['R2_M'],'peak/pi',pk/np.pi,'ccw',(R.net_rotation(o['planes'][0])>0).mean(),'var',o['plane_var'], 'mean rate', sr.mean(), rates.mean(), time.time()-t)
EOF
python t4.py
```

```
go -326.99999999931606 div -277
orig skew 0.3811327310182594
s1 0.0037561605453295677 0.6296296296296297 0.14442439401357232
s1 0.002858020795471039 0.5740740740740741 0.17404299716054272
s1 0.0016886360863350713 0.5462962962962963 0.06293717532926454
s2 0.238873794089125 0.9629629629629629 0.8665805645692874
s3 0.26559425311172724 0.9351851851851852 0.9354037388868772
s3 0.24356747348137053 0.9444444444444444 0.9184006786155736
s3 0.2701037761660151 0.9629629629629629 0.9437878133015183
t 1.8798801898956299
phase R2 0.567959356289055
curv [-222.9092506  -180.2270352    56.26288149  208.77829838  229.47893552] 40 62 6
velocity ratio 0.40532727655366996 peak/pi 0.30555555555555547 ccw 0.7962962962962963 var [0.40873541] mean rate 40.77493864863201 39.592384008699604 7.495220184326172
complex ratio 0.3476662156812665 peak/pi 0.6388888888888888 ccw 0.9444444444444444 var [0.46128021] mean rate 39.613643451327675 39.592384008699604 15.165374040603638
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t5.py <<'EOF'
import sys, numpy as np, pickle
sys.path.insert(0,'entries/churchland-2012')
import reach as R
tr,L=pickle.load(open('J.pkl','rb')); H,th=pickle.load(open('Jhand.pkl','rb'))
cm=tr.maze_condition.values
Hm=np.stack([np.nanmean(H[cm==c],0) for c in range(1,109)])
from scipy.ndimage import gaussian_filter1d
Hs=gaussian_filter1d(Hm,10,axis=1)
v=np.gradient(Hs,axis=1); spd=np.linalg.norm(v,axis=2)
w=(th>=0)&(th<500)
print('end speed frac', np.percentile(spd[:,th==499][:,0]/spd[:,w].max(1),[10,50,90]))
for thr in [0.05,0.1,0.2,0.3]:
    curv=[];segs=[]
    for c in range(108):
        ok=w&(spd[c]>thr*spd[c][w].max())
        hd=np.unwrap(np.arctan2(v[c,ok,1],v[c,ok,0])); curv.append(np.degrees(hd[-1]-hd[0]))
        segs.append(np.sum(np.diff(ok.astype(int))==1))
    curv=np.array(curv); print(thr, np.round(np.percentile(curv,[0,10,25,50,75,90,100])), 'cw',(curv<-20).sum(), 'ccw',(curv>20).sum(), 'str',(abs(curv)<=20).sum(), 'multi-seg', np.sum(np.array(segs)>1))
# by maze version: num barriers
nb=tr.groupby('maze_condition').maze_num_barriers.first().values; nt=tr.groupby('maze_condition').maze_num_targets.first().values
print(np.unique(nb,return_counts=True), np.unique(nt,return_counts=True))
# chord-based: angle between initial displacement direction (to 30% path) and final
EOF
python t5.py
```

```
end speed frac [0.00642486 0.02211665 0.19267729]
0.05 [-232. -190. -138.   75.  170.  207.  250.] cw 42 ccw 63 str 3 multi-seg 5
0.1 [-220. -177.  -94.   56.  168.  208.  227.] cw 39 ccw 63 str 6 multi-seg 0
0.2 [-209. -151.  -82.   42.  158.  202.  226.] cw 38 ccw 62 str 8 multi-seg 0
0.3 [-204. -134.  -66.   33.  148.  195.  217.] cw 37 ccw 59 str 12 multi-seg 0
(array([0, 6, 7, 8, 9], dtype=uint8), array([36,  6, 18, 18, 30])) (array([1, 3], dtype=uint8), array([72, 36]))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat >> t5.py <<'EOF'
thr=0.1
curv=[];c50=[]
for c in range(108):
    ok=w&(spd[c]>thr*spd[c][w].max())
    hd=np.unwrap(np.arctan2(v[c,ok,1],v[c,ok,0])); curv.append(np.degrees(hd[-1]-hd[0]))
    # heading between 20% of path length and 80%
    p=Hs[c,w]; d=np.r_[0,np.cumsum(np.linalg.norm(np.diff(p,axis=0),axis=1))]; d/=d[-1]
    i1,i2,i3,i4=[np.searchsorted(d,q) for q in (0.05,0.2,0.8,0.95)]
    a1=np.arctan2(*(p[i2]-p[i1])[::-1]); a2=np.arctan2(*(p[i4]-p[i3])[::-1]); c50.append(np.degrees(np.angle(np.exp(1j*(a2-a1)))))
curv=np.array(curv); c50=np.array(c50)
print('no barrier', np.round(curv[nb==0])); print('chord', np.round(c50[nb==0]))
print('barrier chord', np.round(c50[nb>0]))
print('chord classes', (c50<-20).sum(), (c50>20).sum(), (abs(c50)<=20).sum())
EOF
python t5.py 2>&1 | tail -5
```

```
95.  105.  110.  105. -163. -163. -101.  -93. -107. -112.  163.  156.
   78.  104.   92.   88.  141.  146.  102.  112.  163.  164.  150.  147.
 -126. -132. -135. -139.  102.  104.  -90.  -98.  165.  165. -108. -115.
 -106. -109.  147.  147.  147.  147.  114.  116.  160.  156. -148. -144.]
chord classes 34 53 21
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python t5.py 2>&1 | tail -14 | head -9
```

```
(array([0, 6, 7, 8, 9], dtype=uint8), array([36,  6, 18, 18, 30])) (array([1, 3], dtype=uint8), array([72, 36]))
no barrier [ 13. -71.  41. -20.  55.  97.  51. -57. -25.  33.  24. -82.   3.  93.
  34. -60.  31.  93. -71.  20.  67.  51. -18. 104.  82. -52. -92. -55.
  74.  18.  -8.  62. -39. -61.  58.  93.]
chord [ -0. -22.  10.  -2.  19.  49.   8. -21.  -3.  33.  16. -24.   0.  33.
  28. -20.  12.  33. -17.   6.  17.  16.  -8.  39.  27. -22. -27. -19.
  43.  13.   1.  12. -10. -21.  38.  16.]
barrier chord [  92.   99.  -61.  -58.  152.  150.  155.  152. -103. -106.  -67.  -75.
  163.  161.  126.  133. -124. -122.  167.  162.   89.  115. -106. -113.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t6.py <<'EOF'
import sys, time, numpy as np, pickle
sys.path.insert(0,'entries/churchland-2012')
import reach as R
tr,L=pickle.load(open('J.pkl','rb')); H,th=pickle.load(open('Jhand.pkl','rb'))
col='offline_move_onset_time'
rates=R.smooth_rates(L[col]['sum'],L[col]['n'])
cm=tr.maze_condition.values
Hm=np.stack([np.nanmean(H[cm==c],0) for c in range(1,109)])
kin=R.kinematics(Hm, th)
for lag in [0,100]:
  for pe,pf in [(-50,100),(10000,1)]:
    for model in ['velocity','complex']:
      res=[]
      for seed in [1,2]:
        S=R.simulate_population(model,kin,th,rates,L[col]['n'],np.random.default_rng(seed),lag_ms=lag,prep_end_ms=pe,prep_fall_ms=pf)
        o=R.jpca(R.preprocess(R.smooth_rates(S,L[col]['n'])),6); pk,_,_=R.angle_peak(R.state_derivative_angles(o['planes'][0]))
        res.append((round(o['R2_skew']/o['R2_M'],2), round(pk/np.pi,2), round((R.net_rotation(o['planes'][0])>0).mean(),2)))
      print(lag,pe,model,res,flush=True)
EOF
time python t6.py
```

```
0 -50 velocity [(np.float64(0.06), np.float64(0.03), np.float64(0.6)), (np.float64(0.06), np.float64(0.08), np.float64(0.63))]
0 -50 complex [(np.float64(0.21), np.float64(0.19), np.float64(0.92)), (np.float64(0.2), np.float64(0.14), np.float64(0.92))]
0 10000 velocity [(np.float64(0.14), np.float64(0.86), np.float64(0.57)), (np.float64(0.23), np.float64(-0.75), np.float64(0.55))]
0 10000 complex [(np.float64(0.36), np.float64(-0.97), np.float64(0.57)), (np.float64(0.27), np.float64(0.36), np.float64(0.6))]
100 -50 velocity [(np.float64(0.41), np.float64(0.47), np.float64(0.78)), (np.float64(0.37), np.float64(0.47), np.float64(0.81))]
100 -50 complex [(np.float64(0.35), np.float64(0.47), np.float64(0.96)), (np.float64(0.35), np.float64(0.42), np.float64(0.95))]
100 10000 velocity [(np.float64(0.14), np.float64(0.86), np.float64(0.57)), (np.float64(0.23), np.float64(-0.75), np.float64(0.55))]
100 10000 complex [(np.float64(0.36), np.float64(-0.97), np.float64(0.57)), (np.float64(0.27), np.float64(0.36), np.float64(0.6))]

real	2m4.014s
user	2m9.702s
sys	0m1.789s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/churchland-2012 && python - <<'EOF'
s=open('reach.py').read()
old_sig="""def simulate_population(model, kin, t_kin, rates, n_trials, rng, lag_ms=100,
                        prep_end_ms=-50, prep_fall_ms=100):"""
new_sig="""def simulate_population(model, kin, t_kin, rates, n_trials, rng, lag_ms=100,
                        prep="switch"):"""
assert old_sig in s; s=s.replace(old_sig,new_sig)
old="""    hand by `lag_ms` (100 ms), the preparatory term holds before movement and
    falls to zero over `prep_fall_ms` after `prep_end_ms`; before movement the
    hand kinematics are those at its start."""
new="""    hand by `lag_ms` (100 ms; 0 is the other reading), the preparatory term
    holds before movement and falls linearly to zero from -50 to +50 ms around
    movement onset (`prep="switch"`; `"persist"`, the other reading, keeps it
    throughout), and the movement term is added to it; before movement the hand
    kinematics are those at its start."""
assert old in s; s=s.replace(old,new)
old="""    w_prep = np.clip(1 - (t - prep_end_ms) / prep_fall_ms, 0, 1)"""
new="""    if prep == "switch":
        w_prep = np.clip(0.5 - t / 100.0, 0, 1)
    elif prep == "persist":
        w_prep = np.ones(len(t))
    else:
        raise ValueError(prep)"""
assert old in s; s=s.replace(old,new)
old="""        r = mov * (1 - w_prep)[None, :] + prep[:, None] * w_prep[None, :]"""
new="""        r = mov + pr[:, None] * w_prep[None, :]"""
assert old in s; s=s.replace(old,new)
s=s.replace("""            prep = we[u] * (endpoint @ up[u]) / se + wps[u] * peak_speed / sps""","""            pr = we[u] * (endpoint @ up[u]) / se + wps[u] * peak_speed / sps""")
s=s.replace("""            prep = 25 * (endpoint @ up[u])""","""            pr = 25 * (endpoint @ up[u])""")
s+='''

# ----------------------------------------------------------------------------
# Checks of the data

def reach_direction_class(trials, n=8):
    """Sector (of n) of the direction of the hit target from the screen centre."""
    ang = np.arctan2(trials.hit_y.values, trials.hit_x.values)
    return np.floor((ang + np.pi) / (2 * np.pi / n)).astype(int) % n


def decode_accuracy(counts, labels, rng, folds=5):
    """Cross-validated nearest-centroid decoding (standard choice).

    counts: trials x features. Features are z-scored on the training trials.
    """
    n = len(labels)
    order = rng.permutation(n)
    fold = np.empty(n, int)
    fold[order] = np.arange(n) % folds
    correct = 0
    classes = np.unique(labels)
    for k in range(folds):
        tr, te = fold != k, fold == k
        mu = counts[tr].mean(0)
        sd = counts[tr].std(0) + 1e-6
        Xtr = (counts[tr] - mu) / sd
        Xte = (counts[te] - mu) / sd
        cen = np.stack([Xtr[labels[tr] == c].mean(0) for c in classes])
        d = ((Xte[:, None, :] - cen[None]) ** 2).sum(-1)
        correct += np.sum(classes[np.argmin(d, 1)] == labels[te])
    return correct / n
'''
open('reach.py','w').write(s)
EOF
grep -n "prep_end\|prep_fall\|prep\b" reach.py | head
```

```
411:                        prep="switch"):
417:    movement onset (`prep="switch"`; `"persist"`, the other reading, keeps it
446:    if prep == "switch":
447:        w_prep = np.clip(0.5 - t / 100.0, 0, 1)
448:    elif prep == "persist":
449:        w_prep = np.ones(len(t))
451:        raise ValueError(prep)
474:        r = mov + pr[:, None] * w_prep[None, :]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t7.py <<'EOF'
import sys, time, numpy as np, pickle
sys.path.insert(0,'entries/churchland-2012')
import importlib, reach as R
tr,L=pickle.load(open('J.pkl','rb')); H,th=pickle.load(open('Jhand.pkl','rb'))
f=R.open_asset(R.SESSIONS['J-array']); g=R.unit_groups(f)
lab=R.reach_direction_class(tr); print(np.bincount(lab))
rng=np.random.default_rng(0)
for arr in ['1','2']:
    m=g==arr
    tc=L['target_counts'][:,m,:]; mc=L['move_counts'][:,m,:]
    pre=tc[:,:,:10].sum(2); post=tc[:,:,12:18].sum(2)   # -500..0, +100..+400
    print(arr,'target pre',R.decode_accuracy(pre,lab,rng),'post',R.decode_accuracy(post,lab,rng),'shuffled post',R.decode_accuracy(post,rng.permutation(lab),rng))
    acc=[R.decode_accuracy(mc[:,:,b].astype(float),lab,rng) for b in range(mc.shape[2])]
    print(arr,'move bins', np.round(acc,2))
col='offline_move_onset_time'
rates=R.smooth_rates(L[col]['sum'],L[col]['n'])
t=np.arange(R.T0,R.T1)
for arr in ['1','2']:
    p=rates[g==arr].mean((0,1)); print(arr,'grand mean rate at',[ (x, round(p[t==x][0],1)) for x in [-400,-200,-100,-50,0,50,100,200,400]])
# xcorr of condition-differential signal: per array the across-condition SD averaged over units
sd={a:rates[g==a].std(1).mean(0) for a in '12'}
for a in '12':
    s=sd[a]; print(a, 'cond SD at',[ (x, round(s[t==x][0],2)) for x in [-400,-200,-100,-50,0,50,100,200,400]])
EOF
python t7.py
```

```
[380 108   0 574 366 163 106 283]
1 target pre 0.12575757575757576 post 0.5651515151515152 shuffled post 0.13434343434343435
1 move bins [0.28 0.3  0.32 0.33 0.38 0.39 0.45 0.44 0.45 0.44 0.47 0.43 0.45 0.46
 0.45 0.48 0.5  0.55 0.6  0.62 0.63 0.64 0.65 0.64 0.6  0.58 0.53 0.52
 0.51 0.47 0.44 0.43 0.41 0.41]
2 target pre 0.12121212121212122 post 0.3813131313131313 shuffled post 0.14898989898989898
2 move bins [0.17 0.16 0.16 0.2  0.23 0.24 0.24 0.24 0.26 0.26 0.26 0.23 0.21 0.23
 0.25 0.27 0.3  0.35 0.4  0.48 0.49 0.48 0.51 0.47 0.48 0.48 0.45 0.47
 0.47 0.49 0.49 0.43 0.46 0.45]
1 grand mean rate at [(-400, np.float64(30.7)), (-200, np.float64(34.7)), (-100, np.float64(49.0)), (-50, np.float64(52.6)), (0, np.float64(53.9)), (50, np.float64(54.9)), (100, np.float64(55.9)), (200, np.float64(55.8)), (400, np.float64(46.5))]
2 grand mean rate at [(-400, np.float64(31.5)), (-200, np.float64(35.8)), (-100, np.float64(62.9)), (-50, np.float64(66.7)), (0, np.float64(60.9)), (50, np.float64(55.3)), (100, np.float64(50.9)), (200, np.float64(47.2)), (400, np.float64(40.4))]
1 cond SD at [(-400, np.float64(8.16)), (-200, np.float64(9.54)), (-100, np.float64(13.84)), (-50, np.float64(14.51)), (0, np.float64(14.62)), (50, np.float64(14.7)), (100, np.float64(14.91)), (200, np.float64(14.82)), (400, np.float64(13.86))]
2 cond SD at [(-400, np.float64(6.49)), (-200, np.float64(7.7)), (-100, np.float64(14.35)), (-50, np.float64(14.05)), (0, np.float64(12.9)), (50, np.float64(12.98)), (100, np.float64(12.29)), (200, np.float64(11.43)), (400, np.float64(10.53))]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u
```

```
Tue Nov 24 23:31:13 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Churchland et al. (2012), \"Neural population dynamics during reaching\", from DANDI:000070\n\n- **Paper:** Churchland MM, Cunningham JP, Kaufman MT, Foster JD, Nuyujukian P, Ryu SI, Shenoy KV (2012). Neural population dynamics during reaching. *Nature* 487, 51-56. doi:10.1038/nature11129.\n- **Claims:** `claims/churchland-2012.yaml`, written from the NIH author manuscript in PubMed Central (PMC3393826), its Methods and figure legends, and the Supplementary Information PDF.\n- **Dataset:** DANDI:000070, version **0.261122.2046** (doi:10.48324/dandi.000070/0.261122.2046). This version was asked for in the prompt of this attempt, a blind repeat attempt made after the dataset changed. The paper cites no version; the version asked for is also the most recent published one. All files are streamed from the archive; nothing is downloaded to disk.\n- **Sessions used:** sub-Jenkins ses-20090918 (the paper's J-array, recorded 09-18-2009) and sub-Nitschke ses-20100923 (N-array, 09-23-2010), each with 108 maze conditions. sub-Nitschke ses-20100910 (108 conditions) is used as the \"N-9-10-2010\" dataset of Supplementary Figure 5, as a variant only.\n\nMethod choices are those of the claims file (its header) and, where it is silent, the paper, cited in the helper `reach.py` and below. Two details the paper leaves open are run under each reading: which movement-onset column of the trial table is used (`offline_move_onset_time`, main, or `move_begins_time`), and the window over which a unit's firing-rate range is taken for the soft normalisation (the analysed window, main, or -1000 to +700 ms). The outcome is the one all four readings give; where they differ, the main reading is adopted as an assumption.\n\n| Claim | Tested here |\n|---|---|\n| array-dataset-composition | tested |\n| fig3ef-same-direction | tested |\n| fig3-independent-of-curvature | tested |\n| fig3-phase-from-prep-state | tested |\n| var-captured-jpc-plane | tested |\n| pc23-variance | tested |\n| suppfig4-j-array-planes | tested |\n| suppfig4-planes-range | tested |\n| fig6a-angle-peak | tested |\n| fig6b-skew-fit | tested |\n| rotation-frequency | tested |\n| suppfig3-shuffle-controls | tested |\n| suppfig5-areas-variance | tested |\n| suppfig5-m1-faster | tested |\n| fig6-velocity-model | tested (simulation; rests on assumptions about the model) |\n| fig6-complex-kinematic-model | tested (simulation; rests on assumptions about the model) |\n| fig1-leech-and-walking | blocked: leech and walking-monkey data are not in the dandiset |\n| fig2-single-neuron-responses | blocked: single-electrode datasets are not in the dandiset |\n| fig3abcd-single-electrode-datasets | blocked: single-electrode datasets are not in the dandiset |\n| fig4-emg-no-rotation | blocked: no EMG in the dandiset |\n| fig5-generator-model | blocked: no EMG in the dandiset |\n| fig6cd-speed-independent-frequency | blocked: the speed-task datasets (monkeys A and B) are not in the dandiset |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"MKL_NUM_THREADS\", \"1\")\nimport time, zlib, hashlib, resource\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport statsmodels.api as sm\nimport reach as R\n\nKEY = \"churchland-2012\"\ndef seed(claim, extra=0):\n    return zlib.crc32(f\"{KEY}/{claim}\".encode()) + extra\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\nT_START = time.time()\nprint(\"dandiset\", R.DANDISET, \"version\", R.VERSION)\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nThe archive's metadata and every file of the version: trials, conditions, units and spikes. Duplicate deposits are looked for by hashing each file's trial start times and its spike counts per unit.\n\"\"\")\n\ncode(r\"\"\"\nmeta = R.version_metadata()\nprint(meta[\"name\"], \"|\", meta[\"version\"], \"|\", meta.get(\"doi\"))\nprint(\"description:\", meta.get(\"description\"))\nprint(\"subjects:\", meta[\"assetsSummary\"].get(\"numberOfSubjects\"), \"files:\", meta[\"assetsSummary\"].get(\"numberOfFiles\"))\nassets = R.list_assets()\nrows = []\nfor a in assets:\n    f = R.open_asset(a[\"path\"])\n    tr = f[\"intervals/trials\"]\n    st = tr[\"start_time\"][:]\n    si = f[\"units/spike_times_index\"][:]\n    row = {\"path\": a[\"path\"].split(\"/\")[-1], \"GB\": a[\"size\"] / 1e9, \"trials\": len(st),\n           \"has_maze_condition\": \"maze_condition\" in tr, \"units\": len(si),\n           \"spikes\": f[\"units/spike_times\"].shape[0],\n           \"start_hash\": hashlib.md5(np.round(np.diff(st), 4).tobytes()).hexdigest()[:10],\n           \"units_hash\": hashlib.md5(np.diff(np.r_[0, si]).tobytes()).hexdigest()[:10]}\n    if \"maze_condition\" in tr:\n        d = R.load_trials(f)\n        sel = R.select_trials(d)\n        row[\"conditions\"] = int(d.maze_condition[d.maze_condition > 0].nunique())\n        row[\"selected_trials\"] = int(sel.sum())\n        row[\"selected_conditions\"] = int(d.maze_condition[sel].nunique())\n    rows.append(row)\n    f.close()\nsurvey = pd.DataFrame(rows)\nprint(survey.to_string())\nprint(\"distinct trial-interval hashes:\", survey.start_hash.nunique(), \"of\", len(survey),\n      \"| distinct spike-count hashes:\", survey.units_hash.nunique(), \"of\", len(survey))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nLoad the three sessions used: trial table, condition-mean spike counts aligned on each movement-onset column, per-trial counts for the clock check, and hand position.\n\"\"\")\n\ncode(r\"\"\"\nDATA = {}\nfor name, path in R.SESSIONS.items():\n    t0 = time.time()\n    f = R.open_asset(path)\n    d = R.load_trials(f)\n    sel = R.select_trials(d)\n    tr = d[sel].reset_index(drop=True)\n    L = R.load_rates(f, tr)\n    groups = R.unit_groups(f)\n    gdesc = {g: f[f\"general/extracellular_ephys/{g}\"].attrs[\"description\"] for g in np.unique(groups)}\n    udesc = f[\"units\"].attrs[\"description\"]\n    rates = {col: R.smooth_rates(L[col][\"sum\"], L[col][\"n\"]).astype(np.float32)\n             for col in (\"offline_move_onset_time\", \"move_begins_time\")}\n    rates24 = R.smooth_rates(L[\"offline_move_onset_time\"][\"sum\"], L[\"offline_move_onset_time\"][\"n\"], sd=24.0).astype(np.float32)\n    hand = None\n    if name != \"N-9-10-2010\":\n        hand, th = R.load_hand(f, tr)\n    DATA[name] = dict(all_trials=d, trials=tr, n=L[\"offline_move_onset_time\"][\"n\"], rates=rates, rates24=rates24,\n                      sums=L[\"offline_move_onset_time\"][\"sum\"] if name != \"N-9-10-2010\" else None,\n                      groups=groups, gdesc=gdesc, udesc=udesc, hand=hand,\n                      target_counts=L[\"target_counts\"], move_counts=L[\"move_counts\"],\n                      target_edges=L[\"target_edges\"], move_edges=L[\"move_edges\"],\n                      unsorted=L[\"units_unsorted\"], outside=L[\"outside_trial\"])\n    f.close()\n    print(f\"{name}: loaded in {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nTH = th\n\"\"\")\n\ncode(r\"\"\"\nfor name, D in DATA.items():\n    d, tr = D[\"all_trials\"], D[\"trials\"]\n    print(f\"== {name}\")\n    print(\"units:\", D[\"udesc\"])\n    print(\"unit groups:\", {g: int((D[\"groups\"] == g).sum()) for g in np.unique(D[\"groups\"])}, D[\"gdesc\"])\n    print(f\"trials {len(d)}; successful {int((d.task_success == 1).sum())}; consistent {int((d.correct_reach == 1).sum())}; \"\n          f\"discarded {int((d.discard_trial == 1).sum())}; delay > 400 ms {int((d.delay > 0.4).sum())}; selected {len(tr)}\")\n    print(f\"delay range {d.delay.min() * 1000:.0f} to {d.delay.max() * 1000:.0f} ms; selected {tr.delay.min() * 1000:.0f} to {tr.delay.max() * 1000:.0f} ms\")\n    n = D[\"n\"]\n    print(f\"conditions with selected trials {int((n > 0).sum())}; trials per condition {n.min()} to {n.max()} (median {np.median(n):.0f})\")\n    go = (tr.go_cue_time - tr.offline_move_onset_time) * 1000\n    print(f\"go cue relative to offline movement onset: median {go.median():.0f} ms (5-95%: {go.quantile(.05):.0f} to {go.quantile(.95):.0f})\")\n    dd = (tr.offline_move_onset_time - tr.move_begins_time) * 1000\n    print(f\"offline_move_onset_time minus move_begins_time: median {dd.median():.1f} ms (5-95%: {dd.quantile(.05):.1f} to {dd.quantile(.95):.1f})\")\n    print(\"units with unsorted spike times:\", D[\"unsorted\"], \"| trials whose analysis window leaves the trial interval:\", D[\"outside\"])\n    r = D[\"rates\"][\"offline_move_onset_time\"]\n    print(f\"condition-mean rates (spikes/s): units' mean {r.mean(axis=(1, 2)).min():.1f} to {r.mean(axis=(1, 2)).max():.1f}; overall max {r.max():.0f}\")\n    if D[\"hand\"] is not None:\n        h = D[\"hand\"]\n        print(f\"hand position (mm): x {np.nanmin(h[..., 0]):.0f} to {np.nanmax(h[..., 0]):.0f}, y {np.nanmin(h[..., 1]):.0f} to {np.nanmax(h[..., 1]):.0f}; trials without hand samples {int(np.isnan(h).all(axis=(1, 2)).sum())}\")\n        spd = np.linalg.norm(np.gradient(h, axis=1), axis=2) * 1000\n        print(\"median hand speed (mm/s) at\", {int(t): round(float(np.nanmedian(spd[:, TH == t])), 1) for t in (-100, -50, 0, 50, 100, 200, 400)}, \"ms from offline onset\")\n        end = h[:, TH == 450, :][:, 0, :]\n        tgt = np.c_[tr.hit_x - tr.cursor_dx, tr.hit_y - tr.cursor_dy]\n        err = np.linalg.norm(end - tgt, axis=1)\n        print(f\"hand at +450 ms against hit target minus cursor offset: median distance {np.nanmedian(err):.1f} mm (target positions span {tr.hit_x.min():.0f} to {tr.hit_x.max():.0f} mm in x)\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n### Clock check\n\nThe spikes are saved per trial. Both arrays should share the clock of the trial table (the files say that the LFP of one array was recorded on a second, slower clock and mapped onto the first). The check decodes the reach direction (eight sectors of the hit target's direction) from each array's spike counts: in the 500 ms before target onset it should be at chance, and after target onset (100 to 400 ms) above it. Around movement onset, the time course of decoding and of the across-condition spread of rates is compared between arrays: an offset between the arrays would show as a shift.\n\"\"\")\n\ncode(r\"\"\"\nCLOCK = {}\nfor name in (\"J-array\", \"N-array\"):\n    D = DATA[name]\n    tr = D[\"trials\"]\n    lab = R.reach_direction_class(tr)\n    rng = np.random.default_rng(seed(\"clock-check\"))\n    tc, mc = D[\"target_counts\"], D[\"move_counts\"]\n    te, me = D[\"target_edges\"], D[\"move_edges\"]\n    pre = (te >= -0.5) & (te < 0)\n    post = (te >= 0.1) & (te < 0.4)\n    for g in np.unique(D[\"groups\"]):\n        m = D[\"groups\"] == g\n        a_pre = R.decode_accuracy(tc[:, m][:, :, pre].sum(2).astype(float), lab, rng)\n        a_post = R.decode_accuracy(tc[:, m][:, :, post].sum(2).astype(float), lab, rng)\n        a_null = R.decode_accuracy(tc[:, m][:, :, post].sum(2).astype(float), rng.permutation(lab), rng)\n        acc = np.array([R.decode_accuracy(mc[:, m, b].astype(float), lab, rng) for b in range(len(me))])\n        CLOCK[(name, g)] = acc\n        print(f\"{name} group {g}: before target {a_pre:.3f}, after target {a_post:.3f}, after target with shuffled labels {a_null:.3f} \"\n              f\"(class sizes {np.bincount(lab, minlength=8).tolist()})\")\n    t = np.arange(R.T0, R.T1)\n    r = D[\"rates\"][\"offline_move_onset_time\"]\n    spread = {g: r[D[\"groups\"] == g].std(axis=1).mean(axis=0) for g in np.unique(D[\"groups\"])}\n    w = (t >= -400) & (t <= 400)\n    a, b = np.diff(spread[\"1\"][w]), np.diff(spread[\"2\"][w])\n    a, b = (a - a.mean()) / a.std(), (b - b.mean()) / b.std()\n    lags = np.arange(-60, 61)\n    xc = [np.mean(a[max(0, -l):len(a) - max(0, l)] * b[max(0, l):len(b) - max(0, -l)]) for l in lags]\n    print(f\"{name}: lag of group 2 behind group 1 at the peak cross-correlation of the change of across-condition spread: {lags[int(np.argmax(xc))]} ms (peak r {max(xc):.2f})\")\n    half = {g: t[w][np.argmax(spread[g][w] >= spread[g][w].min() + 0.5 * (spread[g][w].max() - spread[g][w].min()))] for g in spread}\n    print(f\"{name}: time at which the across-condition spread reaches half its rise: group 1 {half['1']} ms, group 2 {half['2']} ms\")\nfig, ax = plt.subplots(1, 2, figsize=(9, 3), sharey=True)\nfor i, name in enumerate((\"J-array\", \"N-array\")):\n    for g in (\"1\", \"2\"):\n        ax[i].plot(DATA[name][\"move_edges\"] * 1000 + 25, CLOCK[(name, g)], label={\"1\": \"PMd (group 1)\", \"2\": \"M1 (group 2)\"}[g])\n    ax[i].axvline(0, color=\"k\", lw=0.5); ax[i].set_title(name); ax[i].set_xlabel(\"ms from movement onset\")\nax[0].set_ylabel(\"decoding accuracy (8 directions)\"); ax[0].legend()\nplt.show()\nprint(\"plotted accuracies range\", round(min(v.min() for v in CLOCK.values()), 3), \"to\", round(max(v.max() for v in CLOCK.values()), 3))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## The jPCA analysis\n\nEvery claim below uses the same pipeline (helper `reach.py`): condition-mean rates aligned on movement onset (Gaussian 20 ms SD), soft normalisation (range + 5 spikes/s), the cross-condition mean subtracted, PCA on -50 to +150 ms every 10 ms, and jPCA on the top 6 PCs (10 for Supplementary Figure 4). It is run under the four readings of the two open details.\n\"\"\")\n\ncode(r\"\"\"\nREADINGS = [(\"offline_move_onset_time\", None), (\"offline_move_onset_time\", (-1000, 700)),\n            (\"move_begins_time\", None), (\"move_begins_time\", (-1000, 700))]\ndef rlabel(rd):\n    return (\"offline onset\" if rd[0] == \"offline_move_onset_time\" else \"move_begins\") + \", range \" + (\"analysed window\" if rd[1] is None else \"-1000..+700 ms\")\nMAIN = READINGS[0]\n\ndef summarise(o):\n    Z = o[\"planes\"][0]\n    nr = R.net_rotation(Z)\n    pk, _, _ = R.angle_peak(R.state_derivative_angles(Z))\n    rad_s, hz = R.freq_hz(np.abs(o[\"eig\"]).max())\n    return {\"plane_var\": 100 * o[\"plane_var\"][0], \"pc23_var\": 100 * o[\"pc_var\"][1:3].sum(), \"top6_var\": 100 * o[\"pc_var\"].sum(),\n            \"ccw_frac\": (nr > 0).mean(), \"R2_M\": o[\"R2_M\"], \"R2_skew\": o[\"R2_skew\"], \"ratio_6d\": o[\"R2_skew\"] / o[\"R2_M\"],\n            \"R2_M_plane\": o[\"R2_M_plane\"], \"R2_skew_plane\": o[\"R2_skew_plane\"], \"ratio_plane\": o[\"R2_skew_plane\"] / o[\"R2_M_plane\"],\n            \"peak_over_pi\": pk / np.pi, \"max_eig_rad_s\": rad_s, \"freq_hz\": hz}\n\nRES = {}\nfor name in (\"J-array\", \"N-array\"):\n    for rd in READINGS:\n        X = R.preprocess(DATA[name][\"rates\"][rd[0]], rd[1])\n        RES[(name, rd)] = R.jpca(X, 6)\n    X = R.preprocess(DATA[name][\"rates24\"], None)\n    RES[(name, \"smooth24\")] = R.jpca(X, 6)\nTAB = pd.DataFrame({(n, rlabel(rd) if rd != \"smooth24\" else \"24 ms Gaussian (variant)\"): summarise(o) for (n, rd), o in RES.items()}).T\npd.set_option(\"display.width\", 250)\nprint(TAB.round(3).to_string())\n\"\"\")\n\ncode(r\"\"\"\nfig, ax = plt.subplots(1, 2, figsize=(10, 4.5))\nlims = []\nfor i, name in enumerate((\"J-array\", \"N-array\")):\n    Z = RES[(name, MAIN)][\"planes\"][0]\n    col = plt.cm.RdYlGn((Z[0, :, 0] - Z[0, :, 0].min()) / np.ptp(Z[0, :, 0]))\n    for c in range(Z.shape[1]):\n        ax[i].plot(Z[0, c], Z[1, c], color=col[c], lw=0.8)\n        ax[i].plot(Z[0, c, 0], Z[1, c, 0], \"o\", color=col[c], ms=3)\n    ax[i].set_title(f\"{name}: first jPCA plane, -50 to +150 ms\"); ax[i].set_xlabel(\"jPC1\"); ax[i].set_ylabel(\"jPC2\"); ax[i].set_aspect(\"equal\")\n    print(f\"{name}: jPC1 range {Z[0].min():.3f} to {Z[0].max():.3f}, jPC2 range {Z[1].min():.3f} to {Z[1].max():.3f} (all points shown)\")\nplt.show()\n\"\"\")\n\nmd(r\"\"\"\n## array-dataset-composition\n\n> The two array datasets, monkey J-array recorded 2009-09-18 and monkey N-array recorded 2010-09-23, each present 108 reach conditions and comprise 146 and 218 isolations (a mix of single and multi-unit isolations).\n\nCriterion: conditions are the distinct `maze_condition` values above 0 among the trials the Methods select; isolations are the rows of the Units table. Reproduced when both sessions are in the dandiset with all four values within tolerance (108, 108, 146 +- 14.6, 218 +- 21.8); partially reproduced when the sessions and condition counts match but a unit count does not.\n\"\"\")\n\ncode(r\"\"\"\nexp = {\"J-array\": (108, 146, 14.6), \"N-array\": (108, 218, 21.8)}\ncomp = {}\nfor name in (\"J-array\", \"N-array\"):\n    D = DATA[name]\n    nc = int(D[\"trials\"].maze_condition.nunique())\n    nu = len(D[\"groups\"])\n    comp[name] = (nc, nu)\n    print(f\"{name} ({R.SESSIONS[name]}): conditions {nc} (expected 108), units {nu} (expected {exp[name][1]} +- {exp[name][2]}; \"\n          f\"{'within' if abs(nu - exp[name][1]) <= exp[name][2] else 'outside'} tolerance)\")\nprint(\"Units table description:\", DATA[\"J-array\"][\"udesc\"])\nprint(\"conditions match:\", all(comp[n][0] == 108 for n in comp),\n      \"| unit counts within tolerance:\", [abs(comp[n][1] - exp[n][1]) <= exp[n][2] for n in comp])\n\"\"\", tags=[\"claim:array-dataset-composition\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** Both sessions are in the dandiset and each has 108 conditions among the selected trials, but each Units table has 192 rows, outside the tolerance of 146 and of 218. The files describe these rows as unsorted threshold crossings, one per electrode, not the paper's sorted isolations.\n\"\"\")\n\nmd(r\"\"\"\n## fig3ef-same-direction\n\n> In the first jPCA plane the neural state rotates in the same direction for all conditions of the J-array and N-array datasets, including reaches in opposite directions.\n\nCriterion: for each condition, the net change of the polar angle of its state in the oriented jPC plane from -50 to +150 ms. Reproduced when at least 90% of the 108 conditions rotate counter-clockwise in each dataset; partially reproduced when at least 75% do in each, or 90% in one only. The shuffle controls (claim suppfig3-shuffle-controls) are shown as reference there.\n\"\"\")\n\ncode(r\"\"\"\nfor name in (\"J-array\", \"N-array\"):\n    for rd in READINGS + [\"smooth24\"]:\n        o = RES[(name, rd)]\n        nr = R.net_rotation(o[\"planes\"][0])\n        lab = rlabel(rd) if rd != \"smooth24\" else \"24 ms Gaussian (variant)\"\n        print(f\"{name} | {lab}: {int((nr > 0).sum())} of {len(nr)} conditions counter-clockwise ({100 * (nr > 0).mean():.1f}%); \"\n              f\"median net rotation {np.degrees(np.median(nr)):.0f} deg (range {np.degrees(nr.min()):.0f} to {np.degrees(nr.max()):.0f})\")\ndef outcome_dir(fr):\n    if all(f >= 0.9 for f in fr): return \"reproduced\"\n    if all(f >= 0.75 for f in fr) or any(f >= 0.9 for f in fr): return \"partially_reproduced\"\n    return \"not_reproduced\"\nfor rd in READINGS:\n    fr = [(R.net_rotation(RES[(n, rd)][\"planes\"][0]) > 0).mean() for n in (\"J-array\", \"N-array\")]\n    print(rlabel(rd), \"->\", outcome_dir(fr))\n\"\"\", tags=[\"claim:fig3ef-same-direction\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under all four readings at least 90% of the 108 conditions rotate counter-clockwise in both J-array and N-array (the percentages are printed above).\n\"\"\")\n\nmd(r\"\"\"\n## fig3-independent-of-curvature\n\n> The rotations do not relate directly to reach curvature; the neural state rotates the same way for clockwise-curving, counter-clockwise-curving and straight reaches.\n\nCriterion: each condition's reach is classed by the net change of heading of its mean hand path from movement onset to +500 ms as clockwise (below -20 degrees), counter-clockwise (above +20 degrees) or straight. Reproduced when, in each dataset, at least 90% of the conditions in each class with at least five conditions rotate counter-clockwise; partially reproduced when this holds for every class at 75%. A logistic fit of rotation direction on curvature is reported as well.\n\nThe heading is undefined while the hand is at rest, at onset and at the end of the reach. The main measure takes the heading of the mean path over 5 to 20% of its length (from onset to +500 ms) and over 80 to 95% of it, and the net change between them. A variant takes the unwrapped heading of the velocity over the samples where speed exceeds 10% of its peak, from the first to the last of them. Both are choices made here (the claims file and the paper do not define the heading).\n\"\"\")\n\ncode(r\"\"\"\nfrom scipy.ndimage import gaussian_filter1d\ndef curvature(hand, tr, th):\n    cm = tr.maze_condition.values\n    Hm = np.stack([np.nanmean(hand[cm == c], 0) for c in range(1, 109)])\n    Hs = gaussian_filter1d(Hm, 10, axis=1)\n    w = (th >= 0) & (th < 500)\n    chord, vel = [], []\n    for c in range(108):\n        p = Hs[c, w]\n        d = np.r_[0, np.cumsum(np.linalg.norm(np.diff(p, axis=0), axis=1))]\n        d /= d[-1]\n        i1, i2, i3, i4 = [np.searchsorted(d, q) for q in (0.05, 0.2, 0.8, 0.95)]\n        a1 = np.arctan2(*(p[i2] - p[i1])[::-1]); a2 = np.arctan2(*(p[i4] - p[i3])[::-1])\n        chord.append(np.degrees(np.angle(np.exp(1j * (a2 - a1)))))\n        v = np.gradient(p, axis=0); s = np.linalg.norm(v, axis=1)\n        ok = s > 0.1 * s.max()\n        hd = np.unwrap(np.arctan2(v[ok, 1], v[ok, 0]))\n        vel.append(np.degrees(hd[-1] - hd[0]))\n    return np.array(chord), np.array(vel), Hm\n\nCURV = {}\nfor name in (\"J-array\", \"N-array\"):\n    chord, vel, Hm = curvature(DATA[name][\"hand\"], DATA[name][\"trials\"], TH)\n    DATA[name][\"hand_mean\"] = Hm\n    CURV[name] = (chord, vel)\n    nb = DATA[name][\"trials\"].groupby(\"maze_condition\").maze_num_barriers.first().values\n    print(f\"{name}: heading change (main) range {chord.min():.0f} to {chord.max():.0f} deg; conditions without barriers: median |change| {np.median(np.abs(chord[nb == 0])):.0f} deg (n = {(nb == 0).sum()})\")\n\ndef classes(curv):\n    return np.where(curv < -20, \"clockwise\", np.where(curv > 20, \"counter-clockwise\", \"straight\"))\n\ndef curv_outcome(per_ds):\n    ok90 = all(all(f >= 0.9 for (n, f) in d.values() if n >= 5) for d in per_ds)\n    ok75 = all(all(f >= 0.75 for (n, f) in d.values() if n >= 5) for d in per_ds)\n    return \"reproduced\" if ok90 else (\"partially_reproduced\" if ok75 else \"not_reproduced\")\n\nfor meas, k in ((\"main (path segments)\", 0), (\"variant (velocity heading)\", 1)):\n    for rd in READINGS:\n        per = []\n        for name in (\"J-array\", \"N-array\"):\n            cl = classes(CURV[name][k])\n            ccw = R.net_rotation(RES[(name, rd)][\"planes\"][0]) > 0\n            d = {c: (int((cl == c).sum()), float(ccw[cl == c].mean()) if (cl == c).any() else np.nan) for c in (\"clockwise\", \"straight\", \"counter-clockwise\")}\n            per.append(d)\n            if rd == MAIN or k == 0:\n                print(f\"{meas} | {rlabel(rd)} | {name}: \" + \"; \".join(f\"{c} n={n}, {100 * f:.1f}% CCW\" for c, (n, f) in d.items()))\n        print(f\"   -> {meas} | {rlabel(rd)}: {curv_outcome(per)}\")\n\nfor name in (\"J-array\", \"N-array\"):\n    ccw = (R.net_rotation(RES[(name, MAIN)][\"planes\"][0]) > 0).astype(float)\n    x = CURV[name][0] / 100.0\n    if ccw.min() == ccw.max():\n        print(f\"{name}: logistic fit not possible, all conditions rotate the same way\")\n        continue\n    try:\n        fit = sm.Logit(ccw, sm.add_constant(x)).fit(disp=0)\n        print(f\"{name}: logistic fit of CCW on curvature (per 100 deg): slope {fit.params[1]:.3f}, p = {fit.pvalues[1]:.3f}, n = {len(x)}, {int(ccw.sum())} CCW\")\n    except Exception as e:\n        print(f\"{name}: logistic fit failed ({type(e).__name__}: {e})\")\n\"\"\", tags=[\"claim:fig3-independent-of-curvature\"])\n\nmd(r\"\"\"\n**Result: see the printed classes.** The outcome is decided by the main heading measure under the four readings; the conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## fig3-phase-from-prep-state\n\n> The rotation phase follows from the preparatory state; knowing the initial state in the jPC plane, the subsequent states are reasonably predictable.\n\nCriterion: writing each condition's state in the plane as a complex number, the state at +150 ms is predicted from the state at -50 ms by one complex gain shared by all conditions, fitted leaving one condition out. Reproduced when the cross-validated R2 is at least 0.5 in each dataset and above the median R2 of shuffle 3 (movement activity reassigned); partially reproduced when this holds in one dataset.\n\nThe shuffle-3 runs here are this claim's own (20 runs from its seed), with the same dividing point as suppfig3-shuffle-controls: the median go-cue time relative to movement onset plus 50 ms (Supplementary Figure 2 legend). The R2 of a shuffle is that of its own jPCA plane.\n\"\"\")\n\ncode(r\"\"\"\ndef phase_r2(Z):\n    z = Z[0] + 1j * Z[1]\n    a, b = z[:, 0], z[:, -1]\n    pred = np.empty_like(b)\n    for c in range(len(a)):\n        m = np.arange(len(a)) != c\n        g = np.sum(np.conj(a[m]) * b[m]) / np.sum(np.abs(a[m]) ** 2)\n        pred[c] = g * a[c]\n    return 1 - np.sum(np.abs(b - pred) ** 2) / np.sum(np.abs(b - b.mean()) ** 2)\n\ndef dividing_ms(tr, col):\n    return int(round(np.median((tr.go_cue_time - tr[col]).values) * 1000 + 50))\n\nPH = {}\nfor name in (\"J-array\", \"N-array\"):\n    D = DATA[name]\n    for rd in READINGS:\n        div = dividing_ms(D[\"trials\"], rd[0])\n        r = D[\"rates\"][rd[0]]\n        orig = phase_r2(RES[(name, rd)][\"planes\"][0])\n        offs = SEED_OFFSETS if rd == MAIN else [0]\n        meds = []\n        for off in offs:\n            rng = np.random.default_rng(seed(\"fig3-phase-from-prep-state\", off))\n            vals = [phase_r2(R.jpca(R.preprocess(R.shuffle_reassign(r, div, rng.permutation(108)), rd[1]), 6)[\"planes\"][0]) for _ in range(20)]\n            meds.append(np.median(vals))\n        PH[(name, rd)] = (orig, meds)\n        print(f\"{name} | {rlabel(rd)}: dividing point {div} ms; cross-validated R2 {orig:.3f}; shuffle-3 median R2 {meds[0]:.3f}\"\n              + (f\" (five seeds: {', '.join(f'{m:.3f}' for m in meds)})\" if len(meds) > 1 else \"\"))\nfor rd in READINGS:\n    ok = [PH[(n, rd)][0] >= 0.5 and PH[(n, rd)][0] > PH[(n, rd)][1][0] for n in (\"J-array\", \"N-array\")]\n    print(rlabel(rd), \"->\", \"reproduced\" if all(ok) else (\"partially_reproduced\" if any(ok) else \"not_reproduced\"))\n\"\"\", tags=[\"claim:fig3-phase-from-prep-state\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## var-captured-jpc-plane\n\n> The first jPCA plane captures an average of 28% of the total data variance (typically 20 to 35%).\n\nCriterion: (a) the mean of J-array and N-array within 28 +- 2.8%, (b) each of the two within 18 to 38.5%. Reproduced when (a) or (b) holds.\n\"\"\")\n\ncode(r\"\"\"\nfor rd in READINGS + [\"smooth24\"]:\n    v = [100 * RES[(n, rd)][\"plane_var\"][0] for n in (\"J-array\", \"N-array\")]\n    a = abs(np.mean(v) - 28) <= 2.8\n    b = all(18 <= x <= 38.5 for x in v)\n    lab = rlabel(rd) if rd != \"smooth24\" else \"24 ms Gaussian (variant)\"\n    print(f\"{lab}: J-array {v[0]:.1f}%, N-array {v[1]:.1f}%, mean {np.mean(v):.1f}% | (a) {a} | (b) {b} -> {'reproduced' if (a or b) else 'not_reproduced'}\")\n\"\"\", tags=[\"claim:var-captured-jpc-plane\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## pc23-variance\n\n> The plane of PC2 and PC3 captures 29% of the total variance on average, about as much as the first jPCA plane, so the jPCA plane captures patterns already present in the top PCs.\n\nCriterion: readings (a) the mean of J-array and N-array within 29 +- 2.9%, (b) each dataset within it. Reproduced when (a) or (b) holds and, in each dataset, the jPCA plane captures at least 80% as much variance as PC2 and PC3 together; partially reproduced when only one of these two parts holds.\n\"\"\")\n\ncode(r\"\"\"\nfor rd in READINGS + [\"smooth24\"]:\n    v = [100 * RES[(n, rd)][\"pc_var\"][1:3].sum() for n in (\"J-array\", \"N-array\")]\n    j = [100 * RES[(n, rd)][\"plane_var\"][0] for n in (\"J-array\", \"N-array\")]\n    p1 = abs(np.mean(v) - 29) <= 2.9 or all(abs(x - 29) <= 2.9 for x in v)\n    p2 = all(jj >= 0.8 * vv for jj, vv in zip(j, v))\n    lab = rlabel(rd) if rd != \"smooth24\" else \"24 ms Gaussian (variant)\"\n    print(f\"{lab}: PC2+PC3 J {v[0]:.1f}%, N {v[1]:.1f}%, mean {np.mean(v):.1f}% | jPCA/PC2+3 J {j[0] / v[0]:.2f}, N {j[1] / v[1]:.2f} | \"\n          f\"values {p1}, ratio {p2} -> {'reproduced' if p1 and p2 else ('partially_reproduced' if p1 or p2 else 'not_reproduced')}\")\n\"\"\", tags=[\"claim:pc23-variance\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## suppfig4-j-array-planes and suppfig4-planes-range\n\n> suppfig4-j-array-planes: in J-array the first three jPCA planes found within the top 10 PCs capture 22%, 19% and 12% of the variance (54% together), against 64% for the top six PCs, and each plane holds rotations coherent across conditions.\n\n> suppfig4-planes-range: every dataset contains two, and usually three, planes with rotations, together capturing 50 to 70% of the variance.\n\nCriteria: J-array, reproduced when all five values are within tolerance (22 +- 2.2, 19 +- 1.9, 12 +- 1.2, 54 +- 5.4, 64 +- 6.4) and at least 75% of the conditions rotate in the plane's direction in each of the three planes; partially when the three-plane total and the top-six-PC value are within tolerance. Range: reproduced when in each dataset the first three planes together capture 45 to 77% and at least the first two planes have 75% or more of the conditions rotating in the plane's direction; partially when this holds in one dataset.\n\nThe planes are ordered by the magnitude of their M_skew eigenvalues (Methods: \"the largest two (complex-conjugate) imaginary eigenvalues\" define the first plane); each plane is oriented as the first.\n\"\"\")\n\ncode(r\"\"\"\nR10 = {}\nfor name in (\"J-array\", \"N-array\"):\n    for rd in READINGS:\n        R10[(name, rd)] = R.jpca(R.preprocess(DATA[name][\"rates\"][rd[0]], rd[1]), 10, 3)\ndef s4(o):\n    pv = 100 * o[\"plane_var\"]\n    fr = [(R.net_rotation(z) > 0).mean() for z in o[\"planes\"]]\n    hz = [R.freq_hz(e)[1] for e in o[\"plane_eig\"]]\n    return pv, pv.sum(), 100 * o[\"pc_var_all\"][:6].sum(), fr, hz\nfor rd in READINGS:\n    pv, tot, top6, fr, hz = s4(R10[(\"J-array\", rd)])\n    exp = [(22, 2.2), (19, 1.9), (12, 1.2)]\n    within = [abs(p - e) <= t for p, (e, t) in zip(pv, exp)] + [abs(tot - 54) <= 5.4, abs(top6 - 64) <= 6.4]\n    out = \"reproduced\" if all(within) and all(f >= 0.75 for f in fr) else (\"partially_reproduced\" if within[3] and within[4] else \"not_reproduced\")\n    print(f\"J-array | {rlabel(rd)}: planes {', '.join(f'{p:.1f}%' for p in pv)} (total {tot:.1f}%), top six PCs {top6:.1f}%, \"\n          f\"CCW {', '.join(f'{100 * f:.0f}%' for f in fr)}, frequencies {', '.join(f'{h:.2f}' for h in hz)} Hz | within {within} -> {out}\")\n\"\"\", tags=[\"claim:suppfig4-j-array-planes\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\ncode(r\"\"\"\nfor rd in READINGS:\n    ok = []\n    for name in (\"J-array\", \"N-array\"):\n        pv, tot, top6, fr, hz = s4(R10[(name, rd)])\n        good = 45 <= tot <= 77 and fr[0] >= 0.75 and fr[1] >= 0.75\n        ok.append(good)\n        print(f\"{name} | {rlabel(rd)}: three planes {tot:.1f}% ({', '.join(f'{p:.1f}' for p in pv)}), CCW {', '.join(f'{100 * f:.0f}%' for f in fr)} -> {good}\")\n    print(\"   ->\", \"reproduced\" if all(ok) else (\"partially_reproduced\" if any(ok) else \"not_reproduced\"))\n\"\"\", tags=[\"claim:suppfig4-planes-range\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## fig6a-angle-peak\n\n> The distribution of the angle between the neural state and its derivative in the first jPCA plane, over all conditions and times, peaks near pi/2 (rotation), not near 0.\n\nCriterion: peak of a 36-bin histogram over -pi to pi. Reproduced when the peak lies between 0.3 pi and 0.7 pi in each dataset; partially reproduced in one.\n\"\"\")\n\ncode(r\"\"\"\nfig, ax = plt.subplots(1, 2, figsize=(9, 3))\nfor i, name in enumerate((\"J-array\", \"N-array\")):\n    for rd in READINGS:\n        ang = R.state_derivative_angles(RES[(name, rd)][\"planes\"][0])\n        pk, h, e = R.angle_peak(ang)\n        print(f\"{name} | {rlabel(rd)}: peak at {pk / np.pi:.3f} pi ({h.max()} of {h.sum()} angles in the peak bin); \"\n              f\"share of angles within 0.25 pi of pi/2: {np.mean(np.abs(ang - np.pi / 2) < np.pi / 4):.2f}\")\n        if rd == MAIN:\n            ax[i].bar((e[:-1] + e[1:]) / 2 / np.pi, h, width=2 / 36); ax[i].set_title(name); ax[i].set_xlabel(\"angle / pi\")\nplt.show()\nfor rd in READINGS:\n    ok = [0.3 <= R.angle_peak(R.state_derivative_angles(RES[(n, rd)][\"planes\"][0]))[0] / np.pi <= 0.7 for n in (\"J-array\", \"N-array\")]\n    print(rlabel(rd), \"->\", \"reproduced\" if all(ok) else (\"partially_reproduced\" if any(ok) else \"not_reproduced\"))\n\"\"\", tags=[\"claim:fig6a-angle-peak\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## fig6b-skew-fit\n\n> For the neural data the rotational (skew-symmetric) dynamics matrix fits the data nearly as well as the best unconstrained linear dynamics matrix, both in the 6-D space and in the first jPCA plane.\n\nCriterion: the ratio R2(M_skew) / R2(M). Reproduced when the 6-D ratio is at least 0.7 and the plane ratio at least 0.75 in each dataset; partially when both hold in one dataset, or one of the two holds in both. In the plane, M and M_skew are 2 x 2 matrices fitted to the projection onto the first jPCA plane (Figure 6b legend: \"the rank 2 matrices that capture dynamics in the first jPCA plane\").\n\"\"\")\n\ncode(r\"\"\"\nfor rd in READINGS + [\"smooth24\"]:\n    res = []\n    for name in (\"J-array\", \"N-array\"):\n        s = summarise(RES[(name, rd)])\n        res.append((s[\"ratio_6d\"] >= 0.7, s[\"ratio_plane\"] >= 0.75))\n        lab = rlabel(rd) if rd != \"smooth24\" else \"24 ms Gaussian (variant)\"\n        print(f\"{name} | {lab}: 6-D R2 M {s['R2_M']:.3f}, M_skew {s['R2_skew']:.3f}, ratio {s['ratio_6d']:.3f}; \"\n              f\"plane R2 M {s['R2_M_plane']:.3f}, M_skew {s['R2_skew_plane']:.3f}, ratio {s['ratio_plane']:.3f}\")\n    both = [a and b for a, b in res]\n    out = \"reproduced\" if all(both) else (\"partially_reproduced\" if any(both) or all(a for a, b in res) or all(b for a, b in res) else \"not_reproduced\")\n    print(\"   ->\", out)\n\"\"\", tags=[\"claim:fig6b-skew-fit\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## rotation-frequency\n\n> The rotations are brief and fast, up to about 2.5 Hz; the largest eigenvalues of M_skew in the monkey A and B datasets are 8.8 to 13.5 radians/s.\n\nCriterion: frequency is the magnitude of the largest eigenvalue of M_skew (radians/s) over 2 pi. Reproduced when it lies within 1.26 to 2.75 Hz in each dataset; partially when in one. The derivative is the difference of samples 10 ms apart, so an eigenvalue per sample is multiplied by 100 to give radians/s.\n\"\"\")\n\ncode(r\"\"\"\nfor rd in READINGS + [\"smooth24\"]:\n    ok = []\n    for name in (\"J-array\", \"N-array\"):\n        s = summarise(RES[(name, rd)])\n        ok.append(1.26 <= s[\"freq_hz\"] <= 2.75)\n        lab = rlabel(rd) if rd != \"smooth24\" else \"24 ms Gaussian (variant)\"\n        print(f\"{name} | {lab}: largest |eigenvalue| {s['max_eig_rad_s']:.2f} rad/s = {s['freq_hz']:.3f} Hz\")\n    print(\"   ->\", \"reproduced\" if all(ok) else (\"partially_reproduced\" if any(ok) else \"not_reproduced\"))\n\"\"\", tags=[\"claim:rotation-frequency\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## suppfig3-shuffle-controls\n\n> Three shuffle controls that keep preparatory activity and invert or reassign the peri-movement activity largely remove the rotational structure found by jPCA, so jPCA does not find rotations that are not there.\n\nCriterion: the dividing point is the median go-cue time relative to movement onset plus 50 ms. Shuffle 1 (half the conditions inverted per unit) and 3 (movement activity reassigned) are run 20 times with fixed seeds, shuffle 2 once. Rotation strength is R2(M_skew) in 6-D. Reproduced when, in each dataset and for each shuffle, every run is below the original and the median is at most 75% of it; partially when this holds for at least two shuffles in each dataset or all three in one. The fraction of conditions rotating counter-clockwise and the R2 ratio are shown as well.\n\nShuffle 1 inverts exactly half of the conditions (54 of 108), drawn per unit (Supplementary Figure 2 legend: \"inverted for half of the conditions, selected at random ... performed separately for each neuron\"). Inversion reflects the rate after the dividing point about its value there; reassignment adds the other condition's change from its dividing-point rate to this condition's rate at that point.\n\"\"\")\n\ncode(r\"\"\"\ndef shuffle_runs(name, rd, off):\n    D = DATA[name]\n    r = D[\"rates\"][rd[0]]\n    div = dividing_ms(D[\"trials\"], rd[0])\n    rng = np.random.default_rng(seed(\"suppfig3-shuffle-controls\", off))\n    nu = r.shape[0]\n    out = {1: [], 2: [], 3: []}\n    for _ in range(20):\n        mask = np.zeros((nu, 108), bool)\n        for u in range(nu):\n            mask[u, rng.permutation(108)[:54]] = True\n        out[1].append(summarise(R.jpca(R.preprocess(R.shuffle_invert(r, div, mask), rd[1]), 6)))\n    out[2].append(summarise(R.jpca(R.preprocess(R.shuffle_invert(r, div, np.ones((nu, 108), bool)), rd[1]), 6)))\n    for _ in range(20):\n        out[3].append(summarise(R.jpca(R.preprocess(R.shuffle_reassign(r, div, rng.permutation(108)), rd[1]), 6)))\n    return div, out\n\ndef shuffle_verdict(orig, out):\n    res = {}\n    for k, runs in out.items():\n        v = np.array([s[\"R2_skew\"] for s in runs])\n        res[k] = bool(np.all(v < orig) and np.median(v) <= 0.75 * orig)\n    return res\n\nSH = {}\nfor name in (\"J-array\", \"N-array\"):\n    for rd in READINGS:\n        offs = SEED_OFFSETS if rd == MAIN else [0]\n        for off in offs:\n            SH[(name, rd, off)] = shuffle_runs(name, rd, off)\nfor name in (\"J-array\", \"N-array\"):\n    for rd in READINGS:\n        orig = summarise(RES[(name, rd)])\n        div, out = SH[(name, rd, 0)]\n        print(f\"{name} | {rlabel(rd)} | dividing point {div} ms | original R2_skew {orig['R2_skew']:.3f}, CCW {100 * orig['ccw_frac']:.0f}%, ratio {orig['ratio_6d']:.3f}\")\n        for k, runs in out.items():\n            v = np.array([s[\"R2_skew\"] for s in runs])\n            print(f\"   shuffle {k} ({len(v)} runs): R2_skew median {np.median(v):.3f} ({np.median(v) / orig['R2_skew']:.2f} of original), range {v.min():.3f} to {v.max():.3f}, \"\n                  f\"runs at or above original {int((v >= orig['R2_skew']).sum())}; CCW median {100 * np.median([s['ccw_frac'] for s in runs]):.0f}%; ratio median {np.median([s['ratio_6d'] for s in runs]):.3f}\")\n        print(\"   meets the criterion per shuffle:\", shuffle_verdict(orig[\"R2_skew\"], out))\nprint(\"Seed sensitivity, main reading: median R2_skew of shuffles 1 and 3 as a fraction of the original, per seed offset\")\nfor name in (\"J-array\", \"N-array\"):\n    orig = RES[(name, MAIN)][\"R2_skew\"]\n    for off in SEED_OFFSETS:\n        div, out = SH[(name, MAIN, off)]\n        print(f\"   {name} +{off}: shuffle 1 {np.median([s['R2_skew'] for s in out[1]]) / orig:.3f}, shuffle 3 {np.median([s['R2_skew'] for s in out[3]]) / orig:.3f}, verdict {shuffle_verdict(orig, out)}\")\ndef sh_outcome(rd, off=0):\n    per = [shuffle_verdict(RES[(n, rd)][\"R2_skew\"], SH[(n, rd, off)][1]) for n in (\"J-array\", \"N-array\")]\n    if all(all(p.values()) for p in per): return \"reproduced\"\n    if all(sum(p.values()) >= 2 for p in per) or any(all(p.values()) for p in per): return \"partially_reproduced\"\n    return \"not_reproduced\"\nfor rd in READINGS:\n    print(rlabel(rd), \"->\", sh_outcome(rd))\nprint(\"main reading under the five seeds ->\", [sh_outcome(MAIN, off) for off in SEED_OFFSETS])\n\"\"\", tags=[\"claim:suppfig3-shuffle-controls\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## suppfig5-areas-variance and suppfig5-m1-faster\n\n> suppfig5-areas-variance: analysed separately, the PMd and M1 arrays each show clear rotations; the jPCA plane captures 29% (PMd) and 29% (M1) in J-array and 32% and 28% in N-array.\n\n> suppfig5-m1-faster: the angular velocity of the rotations is slightly higher for M1 than for PMd in each dataset.\n\nCriteria: units split by the electrode group of their array (PMd group 1, M1 group 2). Areas: reproduced when all four values are within tolerance (29 +- 2.9, 29 +- 2.9, 32 +- 3.2, 28 +- 2.8) and at least 75% of conditions rotate counter-clockwise in each; partially when all four lie in 18 to 38.5% with 75% rotating. Faster: frequency of the first jPCA plane per array; reproduced when M1 is higher than PMd in both datasets; partially in one. The sub-Nitschke ses-20100910 session is shown against the N-9-10-2010 values (26% and 24%) as a variant.\n\"\"\")\n\ncode(r\"\"\"\nAREA = {}\nfor name in (\"J-array\", \"N-array\", \"N-9-10-2010\"):\n    D = DATA[name]\n    rds = READINGS if name != \"N-9-10-2010\" else [MAIN]\n    for rd in rds:\n        for g, area in ((\"1\", \"PMd\"), (\"2\", \"M1\")):\n            m = D[\"groups\"] == g\n            o = R.jpca(R.preprocess(D[\"rates\"][rd[0]][m], rd[1]), 6)\n            AREA[(name, rd, area)] = summarise(o)\nexpv = {(\"J-array\", \"PMd\"): (29, 2.9), (\"J-array\", \"M1\"): (29, 2.9), (\"N-array\", \"PMd\"): (32, 3.2), (\"N-array\", \"M1\"): (28, 2.8),\n        (\"N-9-10-2010\", \"PMd\"): (26, 2.6), (\"N-9-10-2010\", \"M1\"): (24, 2.4)}\nfor rd in READINGS:\n    w, rng_ok = [], []\n    for name in (\"J-array\", \"N-array\"):\n        for area in (\"PMd\", \"M1\"):\n            s = AREA[(name, rd, area)]\n            e, t = expv[(name, area)]\n            w.append(abs(s[\"plane_var\"] - e) <= t and s[\"ccw_frac\"] >= 0.75)\n            rng_ok.append(18 <= s[\"plane_var\"] <= 38.5 and s[\"ccw_frac\"] >= 0.75)\n            print(f\"{name} {area} | {rlabel(rd)}: plane variance {s['plane_var']:.1f}% (paper {e}%), CCW {100 * s['ccw_frac']:.0f}%, frequency {s['freq_hz']:.3f} Hz\")\n    print(\"   ->\", \"reproduced\" if all(w) else (\"partially_reproduced\" if all(rng_ok) else \"not_reproduced\"))\nfor area in (\"PMd\", \"M1\"):\n    s = AREA[(\"N-9-10-2010\", MAIN, area)]\n    print(f\"variant N-9-10-2010 {area}: plane variance {s['plane_var']:.1f}% (paper {expv[('N-9-10-2010', area)][0]}%), CCW {100 * s['ccw_frac']:.0f}%, frequency {s['freq_hz']:.3f} Hz\")\n\"\"\", tags=[\"claim:suppfig5-areas-variance\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\ncode(r\"\"\"\nfor rd in READINGS:\n    ok = []\n    for name in (\"J-array\", \"N-array\"):\n        p, m = AREA[(name, rd, \"PMd\")][\"freq_hz\"], AREA[(name, rd, \"M1\")][\"freq_hz\"]\n        ok.append(m > p)\n        print(f\"{name} | {rlabel(rd)}: PMd {p:.3f} Hz, M1 {m:.3f} Hz, M1 - PMd {m - p:+.3f} Hz\")\n    print(\"   ->\", \"reproduced\" if all(ok) else (\"partially_reproduced\" if any(ok) else \"not_reproduced\"))\np, m = AREA[(\"N-9-10-2010\", MAIN, \"PMd\")][\"freq_hz\"], AREA[(\"N-9-10-2010\", MAIN, \"M1\")][\"freq_hz\"]\nprint(f\"variant N-9-10-2010: PMd {p:.3f} Hz, M1 {m:.3f} Hz, M1 - PMd {m - p:+.3f} Hz\")\n\"\"\", tags=[\"claim:suppfig5-m1-faster\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## fig6-velocity-model and fig6-complex-kinematic-model\n\n> fig6-velocity-model: a simulated population of units tuned to hand velocity and speed, with preparatory activity tuned to reach endpoint, matched to the recorded data, shows no robust or consistent rotations; M_skew fits it poorly and its angle distribution peaks slightly above zero.\n\n> fig6-complex-kinematic-model: a simulated population tuned to hand position, velocity, acceleration and jerk (with the Methods' sensitivities) produces multiphasic responses but no consistent rotations; M_skew fits it poorly.\n\nCriterion: one simulated dataset per array dataset from that session's condition-mean hand kinematics, analysed as the data. Reproduced when, in each dataset, its 6-D R2 ratio is below 0.6 and below the neural ratio and its angle peak is below pi/4; partially when this holds in one dataset.\n\nThe Methods describe the factors and the sensitivities but not how far the simulated rates lead the hand, nor the time course of the preparatory term. The main reading uses a lead of 100 ms and a preparatory term that falls to zero across movement onset (`reach.simulate_population`, docstring); the other readings are a lead of 0 ms, and a preparatory term that persists. Each simulated unit is matched to one recorded unit's mean rate, range and trial counts, and spikes are drawn from a gamma-interval process of order 2 (Methods). Simulations are run under the main pipeline reading (offline onset, range over the analysed window).\n\"\"\")\n\nSIM_READINGS = [(100, \"switch\"), (0, \"switch\"), (100, \"persist\"), (0, \"persist\")]\ncode(r\"\"\"\nSIM_READINGS = [(100, \"switch\"), (0, \"switch\"), (100, \"persist\"), (0, \"persist\")]\nSIM = {}\nt_sim = time.time()\nfor model, claim in ((\"velocity\", \"fig6-velocity-model\"), (\"complex\", \"fig6-complex-kinematic-model\")):\n    for name in (\"J-array\", \"N-array\"):\n        D = DATA[name]\n        kin = R.kinematics(D[\"hand_mean\"], TH)\n        rates = D[\"rates\"][\"offline_move_onset_time\"]\n        for sr in SIM_READINGS:\n            offs = SEED_OFFSETS if sr == SIM_READINGS[0] else [0]\n            for off in offs:\n                rng = np.random.default_rng(seed(claim, off))\n                S = R.simulate_population(model, kin, TH, rates, D[\"n\"], rng, lag_ms=sr[0], prep=sr[1])\n                sim_rates = R.smooth_rates(S, D[\"n\"])\n                SIM[(model, name, sr, off)] = summarise(R.jpca(R.preprocess(sim_rates), 6))\nprint(f\"simulations took {time.time() - t_sim:.0f} s\")\n\ndef sim_ok(model, name, sr, off=0):\n    s = SIM[(model, name, sr, off)]\n    neural = summarise(RES[(name, MAIN)])[\"ratio_6d\"]\n    return s[\"ratio_6d\"] < 0.6 and s[\"ratio_6d\"] < neural and s[\"peak_over_pi\"] < 0.25\n\ndef sim_outcome(model, sr, off=0):\n    ok = [sim_ok(model, n, sr, off) for n in (\"J-array\", \"N-array\")]\n    return \"reproduced\" if all(ok) else (\"partially_reproduced\" if any(ok) else \"not_reproduced\")\n\ndef show_sim(model):\n    for sr in SIM_READINGS:\n        for name in (\"J-array\", \"N-array\"):\n            s = SIM[(model, name, sr, 0)]\n            neural = summarise(RES[(name, MAIN)])\n            print(f\"{model} | lead {sr[0]} ms, preparatory {sr[1]} | {name}: 6-D ratio {s['ratio_6d']:.3f} (neural {neural['ratio_6d']:.3f}), \"\n                  f\"plane ratio {s['ratio_plane']:.3f}, angle peak {s['peak_over_pi']:.3f} pi, CCW {100 * s['ccw_frac']:.0f}%, plane variance {s['plane_var']:.1f}% -> {sim_ok(model, name, sr)}\")\n        print(\"   ->\", sim_outcome(model, sr))\n    sr = SIM_READINGS[0]\n    for name in (\"J-array\", \"N-array\"):\n        vals = [(SIM[(model, name, sr, o)][\"ratio_6d\"], SIM[(model, name, sr, o)][\"peak_over_pi\"]) for o in SEED_OFFSETS]\n        print(f\"   five seeds, main reading, {name}: 6-D ratio {min(v[0] for v in vals):.3f} to {max(v[0] for v in vals):.3f}, angle peak {min(v[1] for v in vals):.3f} to {max(v[1] for v in vals):.3f} pi\")\n    print(\"   main reading under the five seeds ->\", [sim_outcome(model, sr, o) for o in SEED_OFFSETS])\nshow_sim(\"velocity\")\n\"\"\", tags=[\"claim:fig6-velocity-model\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\ncode(r\"\"\"\nshow_sim(\"complex\")\n\"\"\", tags=[\"claim:fig6-complex-kinematic-model\"])\n\nmd(r\"\"\"\n**Result: see the printed values.** The conclusion is written in the attempt record after the run.\n\"\"\", tags=[\"placeholder\"])\n\nmd(r\"\"\"\n## Summary\n\nWritten after the run.\n\"\"\", tags=[\"placeholder\"])\n\ncode(r\"\"\"\nprint(f\"notebook ran in {(time.time() - T_START) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\n# remove the stray module-level variable from cells list (SIM_READINGS defined above for builder only)\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/churchland-2012/reproduce_churchland_2012.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''                      sums=L["offline_move_onset_time"]["sum"] if name != "N-9-10-2010" else None,
''','')
s=s.replace('''    f.close()
    print(f"{name}: loaded''','''    f.close()
    del L
    print(f"{name}: loaded''')
open(p,'w').write(s)
EOF
uv pip install -q statsmodels && python build_nb.py && cd entries/churchland-2012 && time python -c "
import nbformat
from nbclient import NotebookClient
nb=nbformat.read('reproduce_churchland_2012.ipynb',4)
NotebookClient(nb,timeout=7200,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
nbformat.write(nb,'$TMPDIR/dev_run.ipynb')
" 2>&1 | tail -20
```

```
59 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	10m23.075s
user	8m29.696s
sys	0m13.704s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('dev_run.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='stream': print(f'--- cell {i} {c.metadata.get("tags")}'); print(o.text[:6000])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
```

```
<persisted-output>
Output too large (35.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9e4295f9-dbae-4f3e-bb14-85eae35b1c30/tool-results/bjzi28tye.txt

Preview (first 2KB):
--- cell 1 None
dandiset 000070 version 0.261122.2046

--- cell 3 ['sanity']
Neural population dynamics during reaching | 0.261122.2046 | 10.48324/dandi.000070/0.261122.2046
description: Monkeys recordings of Motor Cortex (M1) and dorsal Premotor Cortex (PMd) using two 96 channel high density Utah Arrays (Blackrock Microsystems) while performing reaching tasks with right hand.
subjects: 2 files: 10

--- cell 3 ['sanity']
                                             path        GB  trials  has_maze_condition  units     spikes  start_hash  units_hash  conditions  selected_trials  selected_conditions
0   sub-Jenkins_ses-20090912_behavior+ecephys.nwb  2.569613    1588                True    192   44869604  4c94b24f03  6baa6e8b85        27.0            563.0                 27.0
1   sub-Jenkins_ses-20090916_behavior+ecephys.nwb  3.502318    2265                True    192   61693399  cc4fd35567  335e1e519f        27.0            790.0                 27.0
2   sub-Jenkins_ses-20090918_behavior+ecephys.nwb  4.338493    2636                True    192   66676824  d04eb8fcf6  dc0cda248f       108.0           1980.0                108.0
3   sub-Jenkins_ses-20090923_behavior+ecephys.nwb  3.538460    2327                True    192   50009289  73fda1b282  be8775633b        27.0            829.0                 27.0
4  sub-Nitschke_ses-20100812_behavior+ecephys.nwb  6.850368    3038                True    192   89773340  798a5ba2f6  4d058586d3        27.0           1312.0                 27.0
5  sub-Nitschke_ses-20100819_behavior+ecephys.nwb  5.943966    3126                True    192   77347550  ca3f101c20  f98f36e002        27.0            134.0                 27.0
[... 4 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/9e4295f9-dbae-4f3e-bb14-85eae35b1c30/tool-results/bjzi28tye.txt"
}
```

```
1	--- cell 1 None
2	dandiset 000070 version 0.261122.2046
3	
4	--- cell 3 ['sanity']
5	Neural population dynamics during reaching | 0.261122.2046 | 10.48324/dandi.000070/0.261122.2046
6	description: Monkeys recordings of Motor Cortex (M1) and dorsal Premotor Cortex (PMd) using two 96 channel high density Utah Arrays (Blackrock Microsystems) while performing reaching tasks with right hand.
7	subjects: 2 files: 10
8	
9	--- cell 3 ['sanity']
10	                                             path        GB  trials  has_maze_condition  units     spikes  start_hash  units_hash  conditions  selected_trials  selected_conditions
11	0   sub-Jenkins_ses-20090912_behavior+ecephys.nwb  2.569613    1588                True    192   44869604  4c94b24f03  6baa6e8b85        27.0            563.0                 27.0
12	1   sub-Jenkins_ses-20090916_behavior+ecephys.nwb  3.502318    2265                True    192   61693399  cc4fd35567  335e1e519f        27.0            790.0                 27.0
13	2   sub-Jenkins_ses-20090918_behavior+ecephys.nwb  4.338493    2636                True    192   66676824  d04eb8fcf6  dc0cda248f       108.0           1980.0                108.0
14	3   sub-Jenkins_ses-20090923_behavior+ecephys.nwb  3.538460    2327                True    192   50009289  73fda1b282  be8775633b        27.0            829.0                 27.0
15	4  sub-Nitschke_ses-20100812_behavior+ecephys.nwb  6.850368    3038                True    192   89773340  798a5ba2f6  4d058586d3        27.0           1312.0                 27.0
16	5  sub-Nitschke_ses-20100819_behavior+ecephys.nwb  5.943966    3126                True    192   77347550  ca3f101c20  f98f36e002        27.0            134.0                 27.0
17	6  sub-Nitschke_ses-20100910_behavior+ecephys.nwb  5.922265    2911                True    192   94386885  887747d77f  974539965f       108.0           1795.0                108.0
18	7  sub-Nitschke_ses-20100920_behavior+ecephys.nwb  5.652540    4044               False   
[... 379 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > drift.py <<'EOF'
import sys, numpy as np
sys.path.insert(0,'entries/churchland-2012')
import reach as R
from scipy.ndimage import gaussian_filter1d
for name in ['J-array','N-array']:
    f=R.open_asset(R.SESSIONS[name]); d=R.load_trials(f)
    tr=d[(d.task_success==1)].reset_index(drop=True)   # all successful trials
    a=tr.offline_move_onset_time.values; nb=6
    blk=np.minimum((np.arange(len(a))*nb)//len(a),nb-1)
    g=R.unit_groups(f); si=f['units/spike_times_index'][:]; st=f['units/spike_times']
    H=np.zeros((2,nb,1000)); s0=0
    for u in range(len(si)):
        s=st[s0:si[u]]; s0=si[u]
        lo=np.searchsorted(s,a-0.6); hi=np.searchsorted(s,a+0.4)
        cnt=hi-lo; tri=np.repeat(np.arange(len(a)),cnt)
        idx=np.concatenate([np.arange(l,h) for l,h in zip(lo,hi)])
        b=np.clip(((s[idx]-a[tri]+0.6)*1000).astype(int),0,999)
        np.add.at(H[int(g[u])-1],(blk[tri],b),1)
    print(name,'block start times (s)',[round(a[blk==k].min()) for k in range(nb)])
    t=np.arange(-600,400)
    for k in range(nb):
        x=[gaussian_filter1d(H[i,k]/(blk==k).sum()/96*1000,10) for i in (0,1)]
        dx=[np.diff(v[(t>=-400)&(t<=300)]) for v in x]
        dx=[(v-v.mean())/v.std() for v in dx]
        lags=np.arange(-150,151)
        xc=[np.mean(dx[0][max(0,-l):len(dx[0])-max(0,l)]*dx[1][max(0,l):len(dx[1])-max(0,-l)]) for l in lags]
        half=[t[np.argmax(v>=v[t==-400]+0.5*(v[(t>=-400)&(t<=100)].max()-v[t==-400]))] for v in x]
        print(f'  block {k}: lag of group2 behind group1 {lags[np.argmax(xc)]} ms (r {max(xc):.2f}); half-rise of mean rate g1 {half[0]} g2 {half[1]} ms; rate at -50 g1 {x[0][t==-50][0]:.1f} g2 {x[1][t==-50][0]:.1f}')
EOF
python drift.py
```

```
J-array block start times (s) [7, 2320, 4730, 7340, 10009, 12889]
  block 0: lag of group2 behind group1 9 ms (r 0.84); half-rise of mean rate g1 -153 g2 -149 ms; rate at -50 g1 51.4 g2 61.8
  block 1: lag of group2 behind group1 6 ms (r 0.77); half-rise of mean rate g1 -148 g2 -152 ms; rate at -50 g1 49.5 g2 60.4
  block 2: lag of group2 behind group1 8 ms (r 0.80); half-rise of mean rate g1 -153 g2 -152 ms; rate at -50 g1 51.8 g2 63.9
  block 3: lag of group2 behind group1 12 ms (r 0.83); half-rise of mean rate g1 -156 g2 -148 ms; rate at -50 g1 54.2 g2 68.4
  block 4: lag of group2 behind group1 11 ms (r 0.82); half-rise of mean rate g1 -148 g2 -141 ms; rate at -50 g1 55.7 g2 72.2
  block 5: lag of group2 behind group1 6 ms (r 0.79); half-rise of mean rate g1 -145 g2 -136 ms; rate at -50 g1 60.2 g2 79.3
N-array block start times (s) [7, 4209, 7982, 12401, 16805, 21530]
  block 0: lag of group2 behind group1 27 ms (r 0.97); half-rise of mean rate g1 -154 g2 -129 ms; rate at -50 g1 64.8 g2 68.2
  block 1: lag of group2 behind group1 24 ms (r 0.95); half-rise of mean rate g1 -146 g2 -127 ms; rate at -50 g1 69.8 g2 72.1
  block 2: lag of group2 behind group1 26 ms (r 0.95); half-rise of mean rate g1 -153 g2 -132 ms; rate at -50 g1 68.7 g2 71.5
  block 3: lag of group2 behind group1 25 ms (r 0.95); half-rise of mean rate g1 -154 g2 -132 ms; rate at -50 g1 70.8 g2 72.2
  block 4: lag of group2 behind group1 26 ms (r 0.98); half-rise of mean rate g1 -158 g2 -132 ms; rate at -50 g1 69.5 g2 74.2
  block 5: lag of group2 behind group1 33 ms (r 0.99); half-rise of mean rate g1 -167 g2 -139 ms; rate at -50 g1 67.3 g2 70.8
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/churchland-2012 && python - <<'EOF'
s=open('reach.py').read()
old='''               target_bins=(-500, 500, 50), move_bins=(-1000, 700, 50)):'''
new='''               target_bins=(-500, 500, 50), move_bins=(-1000, 700, 50), n_blocks=6):'''
assert old in s; s=s.replace(old,new)
old='''    the clock check). Spikes are read one unit at a time.'''
new='''    the clock check), and `block_sum`: counts aligned on the first onset column
    summed over the trials of each of `n_blocks` consecutive blocks of the
    session (units x blocks x ms), to look for a drift between arrays. Spikes
    are read one unit at a time.'''
assert old in s; s=s.replace(old,new)
old='''    out["target_counts"] = np.zeros'''
new='''    block = np.minimum((np.arange(len(trials)) * n_blocks) // len(trials), n_blocks - 1)
    out["block"] = block
    out["block_sum"] = np.zeros((nu, n_blocks, nbin), np.float32)
    out["target_counts"] = np.zeros'''
assert old in s; s=s.replace(old,new)
old='''            np.add.at(out[col]["sum"][u], (cidx[tri], b), 1)'''
new='''            np.add.at(out[col]["sum"][u], (cidx[tri], b), 1)
            if col == onset_cols[0]:
                np.add.at(out["block_sum"][u], (block[tri], b), 1)'''
assert old in s; s=s.replace(old,new)
open('reach.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''                      target_counts=L["target_counts"],'''
new='''                      block_sum=L["block_sum"], block=L["block"],
                      target_counts=L["target_counts"],'''
assert old in s; s=s.replace(old,new)
old='''fig, ax = plt.subplots(1, 2, figsize=(9, 3), sharey=True)
for i, name in enumerate(("J-array", "N-array")):
    for g in ("1", "2"):'''
new='''from scipy.ndimage import gaussian_filter1d
print("Drift check: the lag of group 2 behind group 1 in six consecutive blocks of each session, from the change of the")
print("grand-mean rate (10 ms Gaussian) from -400 to +300 ms around movement onset. An unmapped clock running 9.4 ppm slow")
print("(the LFP's second system: 999.9906 against 1000 samples/s) would add about 9.4 ms per 1000 s of session.")
for name in ("J-array", "N-array"):
    D = DATA[name]
    t = np.arange(R.T0 - R.PAD, R.T1 + R.PAD)
    w = (t >= -400) & (t <= 300)
    lags = np.arange(-150, 151)
    out = []
    for k in range(D["block_sum"].shape[1]):
        nk = int((D["block"] == k).sum())
        sig = []
        for g in ("1", "2"):
            x = gaussian_filter1d(D["block_sum"][D["groups"] == g, k].mean(0) / nk * 1000, 10)
            dx = np.diff(x[w]); sig.append((dx - dx.mean()) / dx.std())
        xc = [np.mean(sig[0][max(0, -l):len(sig[0]) - max(0, l)] * sig[1][max(0, l):len(sig[1]) - max(0, -l)]) for l in lags]
        t_start = D["trials"].start_time.values[D["block"] == k].min()
        out.append((round(t_start), int(lags[int(np.argmax(xc))]), round(max(xc), 2)))
    print(f"{name}: (block start s, lag ms, peak r):", out)
fig, ax = plt.subplots(1, 2, figsize=(9, 3), sharey=True)
for i, name in enumerate(("J-array", "N-array")):
    for g in ("1", "2"):'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Now writing the conclusions into the notebook from the dev run (all random draws are seeded, so the final run gives the same numbers).

**Agent calls Bash**

```bash
cd $TMPDIR && cat > concl.py <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''**Result: reproduced.** Under all four readings at least 90% of the 108 conditions rotate counter-clockwise in both J-array and N-array (the percentages are printed above).''',
'''**Result: reproduced.** Under the main reading 103 of 108 J-array conditions (95.4%) and 107 of 108 N-array conditions (99.1%) rotate counter-clockwise; under the four readings the shares are 94.4 to 96.3% and 99.1 to 100%, all at least 90%.''')
C=[
"""**Result: partially reproduced, resting on the assumption about the onset column.** Under the main reading (offline onset) 88.2% of the 34 clockwise-curving J-array conditions rotate counter-clockwise, below 90% and above 75%; the straight and counter-clockwise classes of J-array and all three classes of N-array are at 98.1% or more. Under the two move_begins readings every class is at 92.5% or more, which would make the claim reproduced. The velocity-heading variant gives the same split by reading. In J-array the logistic fit finds that the more a reach curves clockwise, the less likely its state rotates counter-clockwise (slope 1.524 per 100 degrees, p = 0.029); in N-array it finds no relation (slope -0.175, p = 0.873).""",
"""**Result: partially reproduced.** The cross-validated R2 is 0.568 in J-array and 0.676 in N-array, both at least 0.5. In N-array it is above the shuffle-3 median (0.600); in J-array it is below it (0.686), so the criterion holds in one dataset. All four readings and the five seeds give the same outcome (J-array shuffle-3 medians 0.678 to 0.688 over the seeds).""",
"""**Result: not reproduced, resting on the assumption about the onset column.** Under the main reading the first plane captures 14.9% (J-array) and 22.9% (N-array), mean 18.9%: the mean is outside 28 +- 2.8% and J-array is below 18%. Under the move_begins readings J-array captures 18.7 to 19.0% and N-array 21.1 to 22.0%, all inside 18 to 38.5%, which would make it reproduced under reading (b). The 24 ms variant gives 15.6% and 23.3%.""",
"""**Result: not reproduced, resting on the assumption about the onset column.** Under the main reading PC2 and PC3 capture 19.2% (J-array) and 28.3% (N-array), mean 23.8%: the mean and the J-array value are outside 29 +- 2.9%. The jPCA plane captures 0.78 (J-array) and 0.81 (N-array) as much variance as PC2 and PC3, so the 80% part fails in J-array. Under the move_begins readings the ratio part holds (0.84 to 0.95) and the values part does not, which would make it partially reproduced.""",
"""**Result: not reproduced.** In J-array the three planes capture 13.3%, 13.3% and 12.2% (38.8% together) and the top six PCs 51.9%, against 22, 19, 12, 54 and 64%; only the third plane is within tolerance. The rotations are coherent in each plane (98%, 97% and 92% of conditions counter-clockwise). The four readings agree.""",
"""**Result: partially reproduced.** In N-array the three planes capture 47.7%, inside 45 to 77%, with 97% and 100% of conditions rotating in the first two planes; in J-array they capture 38.8%, below 45%, although 98% and 97% rotate. The four readings agree (J-array 37.7 to 38.8%, N-array 45.8 to 48.8%).""",
"""**Result: reproduced.** The histogram peaks at 0.528 pi in J-array and 0.639 pi in N-array under the main reading, and at 0.528 to 0.583 pi and 0.639 pi under all four readings, between 0.3 pi and 0.7 pi.""",
"""**Result: reproduced.** The 6-D ratio R2(M_skew)/R2(M) is 0.918 (J-array) and 0.909 (N-array), and the plane ratio 0.946 and 0.953. Under all four readings and the 24 ms variant the 6-D ratios are 0.870 or more and the plane ratios 0.908 or more.""",
"""**Result: reproduced, resting on the assumption about the onset column.** The largest eigenvalue of M_skew is 8.44 rad/s (1.344 Hz) in J-array and 8.81 rad/s (1.402 Hz) in N-array, inside 1.26 to 2.75 Hz. Under the move_begins readings J-array gives 1.063 to 1.098 Hz, below the range, which would make it partially reproduced. The 24 ms variant gives 1.290 and 1.372 Hz.""",
"""**Result: partially reproduced, resting on the assumption about the onset column.** Under the main reading, in J-array every run of every shuffle is below the original R2(M_skew) of 0.381, and the medians are 0.01 (shuffle 1), 0.63 (shuffle 2) and 0.75 (shuffle 3) of it, so all three shuffles meet the criterion. In N-array shuffle 1 removes the structure (0.01 of the original of 0.527) but shuffles 2 and 3 leave 0.76 and 0.87 of it. The criterion's partial outcome (all three shuffles in one dataset) holds under each of the five seeds (J-array shuffle-3 medians 0.725 to 0.745 of the original). The other range window also gives partially reproduced (two shuffles in each dataset); the two move_begins readings give not reproduced, as N-array then meets only shuffle 1. After shuffles 2 and 3 the median share of conditions rotating counter-clockwise stays at 93 to 98%.""",
"""**Result: not reproduced.** Split by array, the first plane captures 21.6% (PMd) and 20.2% (M1) in J-array and 17.7% and 27.1% in N-array, against 29, 29, 32 and 28%; only N-array M1 is within tolerance, and N-array PMd is below 18%. Each array rotates (91 to 99% of conditions counter-clockwise under the main reading). The four readings agree (N-array PMd 17.6 to 17.9%). The N-9-10-2010 variant gives 14.7% (PMd) and 20.8% (M1) against 26% and 24%.""",
"""**Result: reproduced.** The first-plane frequency is higher for M1 than for PMd in J-array (2.020 against 0.844 Hz) and in N-array (1.488 against 0.973 Hz) under the main reading, and in both datasets under all four readings; the N-9-10-2010 variant agrees (1.659 against 1.063 Hz).""",
"""**Result: not reproduced, resting on the assumptions about the simulated model.** Under the main reading (rates lead the hand by 100 ms, the preparatory term falls at onset), M_skew fits the simulated population poorly (6-D ratio 0.400 in J-array and 0.244 in N-array, below 0.6 and below the neural 0.918 and 0.909), but the angle distribution peaks at 0.417 pi and 0.639 pi, above pi/4, in both datasets. The five seeds give the same outcome (peaks 0.306 to 0.472 pi in J-array, 0.250 to 0.639 pi in N-array). With no lead and the falling preparatory term the criterion holds in both datasets (peaks -0.083 pi and 0.083 pi); with a persisting preparatory term it fails in both under either lead.""",
"""**Result: partially reproduced, resting on the assumptions about the simulated model, and sensitive to the seed.** Under the main reading M_skew fits poorly in both datasets (6-D ratio 0.095 in J-array and 0.144 in N-array). The J-array angle peak is at -0.972 pi, below pi/4 (the state and its derivative point in opposite directions, not a rotation), and the N-array peak is at 0.861 pi, above it. Under the five seeds the outcome is partially reproduced twice and not reproduced three times (J-array peaks -0.972 to 0.750 pi). The other readings give partially reproduced (no lead) or not reproduced (persisting preparatory term with a lead of 100 ms).""",
]
import re
ph1='''**Result: see the printed classes.** The outcome is decided by the main heading measure under the four readings; the conclusion is written in the attempt record after the run.'''
assert ph1 in s; s=s.replace(ph1, C[0])
ph='''**Result: see the printed values.** The conclusion is written in the attempt record after the run.'''
assert s.count(ph)==13, s.count(ph)
for c in C[1:]:
    s=s.replace(ph,c,1)
s=s.replace(', tags=["placeholder"])',')')
SUM='''## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| array-dataset-composition | partially reproduced |
| fig3ef-same-direction | reproduced |
| fig3-independent-of-curvature | partially reproduced (assumed onset column) |
| fig3-phase-from-prep-state | partially reproduced |
| var-captured-jpc-plane | not reproduced (assumed onset column) |
| pc23-variance | not reproduced (assumed onset column) |
| suppfig4-j-array-planes | not reproduced |
| suppfig4-planes-range | partially reproduced |
| fig6a-angle-peak | reproduced |
| fig6b-skew-fit | reproduced |
| rotation-frequency | reproduced (assumed onset column) |
| suppfig3-shuffle-controls | partially reproduced (assumed onset column) |
| suppfig5-areas-variance | not reproduced |
| suppfig5-m1-faster | reproduced |
| fig6-velocity-model | not reproduced (assumed model details) |
| fig6-complex-kinematic-model | partially reproduced (assumed model details; seed sensitive) |
| fig1-leech-and-walking | blocked, data missing |
| fig2-single-neuron-responses | blocked, data missing |
| fig3abcd-single-electrode-datasets | blocked, data missing |
| fig4-emg-no-rotation | blocked, data missing |
| fig5-generator-model | blocked, data missing |
| fig6cd-speed-independent-frequency | blocked, data missing |

**How the analysis differs from the paper's.** The Units tables hold unsorted threshold crossings, 192 per session (one per electrode), where the paper analysed 146 and 218 sorted single and multi-unit isolations; every jPCA claim is judged on these units, as the claims file says. The paper's custom smoothing step (Methods: it "had essentially no effect on any of the population-level analyses") is not applied. Rates are aligned on movement onset only, not also on target onset and the go cue. Which movement-onset column the paper's alignment corresponds to, and over which window the normalisation range is taken, are not stated; both are run under each reading, and the offline onset with the range over the analysed window is the main reading. The simulated velocity and complex kinematic populations are built here from the Methods' description, with a lead of the rates over the hand and a time course of the preparatory term that the Methods do not give.

**What was found about the dataset.** All ten files of the version were read. The paper's two array sessions are there with 108 conditions each; the Units tables are unsorted threshold crossings, which the files state. Two of the eight further sessions (sub-Nitschke ses-20100920 and ses-20100922) have no `maze_condition`, `correct_reach` or `trial_version` columns. No recording is deposited twice (all trial-interval and spike-count hashes differ). Hand position is in mm (with a conversion to metres), its speed rises at `offline_move_onset_time`, and the hand ends about 9 to 11 mm from the hit target minus the cursor offset. Reach direction decodes at chance from both arrays before target onset and above chance after it. The lag between the arrays' movement-related changes is constant over each session (about 6 to 12 ms in J-array and 24 to 33 ms in N-array, M1 later), so there is no drift of one array's spikes against the other; a constant offset of about 25 ms in N-array cannot be told apart from a later M1 response.'''
old_sum='''## Summary

Written after the run.'''
assert old_sum in s; s=s.replace(old_sum,SUM)
open(p,'w').write(s)
EOF
python concl.py && . dev/bin/activate && python build_nb.py && grep -c "placeholder" build_nb.py
```

```
Exit code 1
59 cells
0
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
p='build_nb.py'; s=open(p).read()
s=re.sub(r'\*\*(?!Result)([^*]+?)\*\*', r'\1', s)
open(p,'w').write(s)
print(re.findall(r'\*\*[^*]+\*\*', s)[:3], len(re.findall(r'\*\*Result', s)))
EOF
. dev/bin/activate && python build_nb.py; grep -n "—\|rather" build_nb.py entries/churchland-2012/reach.py | head
```

```
['**Result: partially reproduced.**', '**Result: reproduced.**', '**Result: partially reproduced, resting on the assumption about the onset column.**'] 11
59 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "Result:" build_nb.py | cut -c1-150
```

```
316:**Result: partially reproduced.** Both sessions are in the dandiset and each has 108 conditions among the selected trials, but each Units table ha
345:**Result: reproduced.** Under the main reading 103 of 108 J-array conditions (95.4%) and 107 of 108 N-array conditions (99.1%) rotate counter-cloc
421:**Result: partially reproduced, resting on the assumption about the onset column.** Under the main reading (offline onset) 88.2% of the 34 clockwi
470:**Result: partially reproduced.** The cross-validated R2 is 0.568 in J-array and 0.676 in N-array, both at least 0.5. In N-array it is above the s
491:**Result: not reproduced, resting on the assumption about the onset column.** Under the main reading the first plane captures 14.9% (J-array) and 
514:**Result: not reproduced, resting on the assumption about the onset column.** Under the main reading PC2 and PC3 capture 19.2% (J-array) and 28.3%
549:**Result: not reproduced.** In J-array the three planes capture 13.3%, 13.3% and 12.2% (38.8% together) and the top six PCs 51.9%, against 22, 19,
564:**Result: partially reproduced. In N-array the three planes capture 47.7%, inside 45 to 77%, with 97% and 100% of conditions rotating in the first
592:Result: reproduced. The histogram peaks at 0.528 pi in J-array and 0.639 pi in N-array under the main reading, and at 0.528 to 0.583 pi and 0.639 
618:Result: reproduced. The 6-D ratio R2(M_skew)/R2(M) is 0.918 (J-array) and 0.909 (N-array), and the plane ratio 0.946 and 0.953. Under all four rea
641:Result: reproduced, resting on the assumption about the onset column.** The largest eigenvalue of M_skew is 8.44 rad/s (1.344 Hz) in J-array and 8
712:**Result: partially reproduced, resting on the assumption about the onset column.** Under the main reading, in J-array every run of every shuffle 
753:**Result: not reproduced. Split by array, the first plane captures 21.6% (PMd) and 20.2% (M1) in J-array and 17.7% and 27.1% in N-array, against 2
769:Result: reproduced.** The first-p
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; L=open(p).read().split('\n')
for i,l in enumerate(L):
    if l.startswith('Result:') or l.startswith('**Result:'):
        l=l.replace('**','')
        k=l.index('. ')
        L[i]='**'+l[:k+1]+'**'+l[k+1:]
open(p,'w').write('\n'.join(L))
EOF
grep -n "Result:" build_nb.py | cut -c1-110; grep -c '\*\*' build_nb.py; . dev/bin/activate && python build_nb.py
```

```
316:**Result: partially reproduced.** Both sessions are in the dandiset and each has 108 conditions among the 
345:**Result: reproduced.** Under the main reading 103 of 108 J-array conditions (95.4%) and 107 of 108 N-arra
421:**Result: partially reproduced, resting on the assumption about the onset column.** Under the main reading
470:**Result: partially reproduced.** The cross-validated R2 is 0.568 in J-array and 0.676 in N-array, both at
491:**Result: not reproduced, resting on the assumption about the onset column.** Under the main reading the f
514:**Result: not reproduced, resting on the assumption about the onset column.** Under the main reading PC2 a
549:**Result: not reproduced.** In J-array the three planes capture 13.3%, 13.3% and 12.2% (38.8% together) an
564:**Result: partially reproduced.** In N-array the three planes capture 47.7%, inside 45 to 77%, with 97% an
592:**Result: reproduced.** The histogram peaks at 0.528 pi in J-array and 0.639 pi in N-array under the main 
618:**Result: reproduced.** The 6-D ratio R2(M_skew)/R2(M) is 0.918 (J-array) and 0.909 (N-array), and the pla
641:**Result: reproduced, resting on the assumption about the onset column.** The largest eigenvalue of M_skew
712:**Result: partially reproduced, resting on the assumption about the onset column.** Under the main reading
753:**Result: not reproduced.** Split by array, the first plane captures 21.6% (PMd) and 20.2% (M1) in J-array
769:**Result: reproduced.** The first-plane frequency is higher for M1 than for PMd in J-array (2.020 against 
829:**Result: not reproduced, resting on the assumptions about the simulated model.** Under the main reading (
837:**Result: partially reproduced, resting on the assumptions about the simulated model, and sensitive to the
18
59 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n '\*\*' build_nb.py | grep -v "Result:" | cut -c1-150
```

```
441:        g = np.sum(np.conj(a[m]) * b[m]) / np.sum(np.abs(a[m]) ** 2)
872:What was found about the dataset.** All ten files of the version were read. The paper's two array sessions are there with 108 conditions each; the
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat, difflib
a=nbformat.read('dev_run.ipynb',4); b=nbformat.read('entries/churchland-2012/reproduce_churchland_2012.ipynb',4)
ca=[c.source for c in a.cells if c.cell_type=='code']; cb=[c.source for c in b.cells if c.cell_type=='code']
for x,y in zip(ca,cb):
    if x!=y:
        for l in difflib.unified_diff(x.split('\n'),y.split('\n'),lineterm='',n=0): print(l)
EOF
```

```
--- 
+++ 
@@ -19,0 +20 @@
+                      block_sum=L["block_sum"], block=L["block"],
--- 
+++ 
@@ -30,0 +31,20 @@
+from scipy.ndimage import gaussian_filter1d
+print("Drift check: the lag of group 2 behind group 1 in six consecutive blocks of each session, from the change of the")
+print("grand-mean rate (10 ms Gaussian) from -400 to +300 ms around movement onset. An unmapped clock running 9.4 ppm slow")
+print("(the LFP's second system: 999.9906 against 1000 samples/s) would add about 9.4 ms per 1000 s of session.")
+for name in ("J-array", "N-array"):
+    D = DATA[name]
+    t = np.arange(R.T0 - R.PAD, R.T1 + R.PAD)
+    w = (t >= -400) & (t <= 300)
+    lags = np.arange(-150, 151)
+    out = []
+    for k in range(D["block_sum"].shape[1]):
+        nk = int((D["block"] == k).sum())
+        sig = []
[... 13 more lines not kept]
```

**Agent**

Caught one code line damaged by my bold-stripping regex; fixing it and the summary line.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace("np.sum(np.abs(b - pred)  2) / np.sum(np.abs(b - b.mean())  2)","np.sum(np.abs(b - pred) ** 2) / np.sum(np.abs(b - b.mean()) ** 2)")
s=s.replace("What was found about the dataset.** All ten","What was found about the dataset. All ten")
open(p,'w').write(s)
EOF
grep -n "How the analysis differs" build_nb.py | cut -c1-80; . dev/bin/activate && python build_nb.py
```

```
870:How the analysis differs from the paper's. The Units tables hold unsorted th
59 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cat entries/fouke-2025/README.md | head -40; grep -n "python" entries/fouke-2025/entry.yaml
```

```
Tue Nov 24 23:48:35 UTC 2026
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/churchland-2012 && cat > entry.yaml <<'EOF'
schema_version: 1
name: churchland-2012
type: reproduction
title: Rotational population dynamics during reaching (Churchland et al. 2012)
description: Tests the findings of Churchland, Cunningham, Kaufman, Foster, Nuyujukian, Ryu and Shenoy
  (2012) on dandiset 000070, which holds the paper's two Utah-array datasets (J-array and N-array, 108
  maze conditions each) as unsorted threshold crossings. It runs jPCA on the condition-averaged rates
  and tests the direction, phase, variance and frequency of the rotations, the fits of the skew-symmetric
  dynamics, the shuffle controls, the split by array and two simulated kinematic populations. The
  single-electrode, EMG, leech and walking-monkey data are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_churchland_2012.ipynb
  title: Reproducing Churchland et al. (2012) from dandiset 000070
  runtime_minutes: 11
helpers:
- reach.py
related:
- id: dandi:000070/0.261122.2046
  relation: uses_data
- id: doi:10.1038/nature11129
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
h5py
ipykernel
matplotlib
numpy
pandas
remfile
requests
scipy
statsmodels
EOF
cat > README.md <<'EOF'
# Churchland et al. (2012) from dandiset 000070

Tests the findings of [Churchland et al. (2012)](https://doi.org/10.1038/nature11129) that can be
tested on [DANDI:000070](https://dandiarchive.org/dandiset/000070/0.261122.2046), which holds the
paper's two Utah-array datasets, J-array (sub-Jenkins ses-20090918) and N-array (sub-Nitschke
ses-20100923), with 108 maze conditions each. Their Units tables hold unsorted threshold crossings,
one per electrode (192 per session), where the paper analysed 146 and 218 sorted isolations. The
single-electrode datasets, the EMG and the leech and walking-monkey recordings are not in it.

| Claim | Outcome |
|---|---|
| The array datasets have 108 conditions and 146 and 218 isolations | Partially reproduced |
| The state rotates the same way for all conditions | Reproduced |
| Rotations do not depend on reach curvature | Partially reproduced (assumed onset column) |
| The rotation phase follows from the preparatory state | Partially reproduced |
| The jPCA plane captures 28% of the variance | Not reproduced (assumed onset column) |
| PC2 and PC3 capture 29%, as much as the jPCA plane | Not reproduced (assumed onset column) |
| J-array: three planes capture 22, 19 and 12% (Supplementary Figure 4) | Not reproduced |
| Three planes capture 50 to 70% in every dataset | Partially reproduced |
| The state-derivative angle peaks near pi/2 | Reproduced |
| M_skew fits nearly as well as the unconstrained M | Reproduced |
| Rotations up to about 2.5 Hz | Reproduced (assumed onset column) |
| Shuffle controls remove the rotations | Partially reproduced (assumed onset column) |
| PMd and M1 each capture 28 to 32% in the jPCA plane | Not reproduced |
| Rotations are faster in M1 than in PMd | Reproduced |
| A velocity-tuned simulated population does not rotate | Not reproduced (assumed model) |
| A complex kinematic simulated population does not rotate | Partially reproduced (assumed model, seed sensitive) |
| Leech, walking monkey, single electrodes, EMG, generator model, speed task (six claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/churchland-2012-02.yaml`](../../attempts/churchland-2012-02.yaml).

- `reproduce_churchland_2012.ipynb`: the analysis. It takes about eleven minutes, most of it
  streaming the spikes and simulating the kinematic populations.
- `reach.py`: loading the files, condition-averaged rates aligned on movement onset, jPCA as in the
  paper's Methods, the shuffle controls of Supplementary Figure 2 and the simulated kinematic
  populations. Other notebooks on this dandiset can import it.
EOF
cd ../.. && date -u && time python tools/entry.py lock entries/churchland-2012 2>&1 | tail -5
```

```
Tue Nov 24 23:48:50 UTC 2026
wrote churchland-2012/requirements.lock.txt (Python 3.13, with hashes)

real	0m0.362s
user	0m0.250s
sys	0m0.088s
```

**Agent calls Bash**

```bash
sed -i '/ipykernel/d' entries/churchland-2012/requirements.in && python tools/entry.py lock entries/churchland-2012 2>&1 | tail -2 && date -u && time python tools/entry.py all entries/churchland-2012 2>&1 | tail -30
```

```
wrote churchland-2012/requirements.lock.txt (Python 3.13, with hashes)
Tue Nov 24 23:48:55 UTC 2026
Installed kernelspec registry-churchland-2012 in executed/churchland-2012/.venv/share/jupyter/kernels/registry-churchland-2012
0 error(s)
pass  reproduce_churchland_2012.ipynb  (593 s)

real	10m2.171s
user	8m39.132s
sys	0m34.229s
```

**Agent**

Entry check and run pass (593 s). Verifying the executed outputs match the conclusions.

**Agent calls Bash**

```bash
ls executed/churchland-2012/; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('executed/churchland-2012/reproduce_churchland_2012.ipynb',4)
a=nbformat.read('dev_run.ipynb',4)
def outs(nb):
    r=[]
    for c in nb.cells:
        if c.cell_type=='code':
            r.append(''.join(o.get('text','') for o in c.outputs if o.output_type=='stream'))
    return r
x,y=outs(a),outs(nb)
import difflib
for i,(p,q) in enumerate(zip(x,y)):
    if p!=q:
        print('== cell',i)
        for l in difflib.unified_diff(p.split('\n'),q.split('\n'),lineterm='',n=0): print(l[:250])
for c in nb.cells:
    for o in c.get('outputs',[]):
        if o.output_type=='error': print('ERR',o.ename)
EOF
```

```
reproduce_churchland_2012.ipynb
result.json
== cell 2
--- 
+++ 
@@ -1,3 +1,3 @@
-J-array: loaded in 43 s; peak memory 1.84 GB
-N-array: loaded in 53 s; peak memory 2.55 GB
-N-9-10-2010: loaded in 92 s; peak memory 3.00 GB
+J-array: loaded in 46 s; peak memory 1.85 GB
+N-array: loaded in 58 s; peak memory 2.57 GB
+N-9-10-2010: loaded in 43 s; peak memory 3.11 GB
== cell 4
--- 
+++ 
@@ -8,0 +9,5 @@
+Drift check: the lag of group 2 behind group 1 in six consecutive blocks of each session, from the change of the
+grand-mean rate (10 ms Gaussian) from -400 to +300 ms around movement onset. An unmapped clock running 9.4 ppm slow
+(the LFP's second system: 999.9906 against 1000 samples/s) would add about 9.4 ms per 1000 s of session.
+J-array: (block start s, lag ms, peak r): [(18, 9, np.float32(0.84)), (2410, 5, np.float32(0.78)), (4921, 11, np.float32(0.76)), (7450, 10, np.float32(0.79)), (10048, -4, np.float32(0.8)), (12908, 4, np.float32(0.78))]
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('executed/churchland-2012/reproduce_churchland_2012.ipynb',4)
for c in nb.cells:
    if 'claim:suppfig3-shuffle-controls' in c.metadata.get('tags',[]):
        t=''.join(o.get('text','') for o in c.outputs); print(t[-900:])
EOF
```

```
huffle 1 0.007, shuffle 3 0.725, verdict {1: True, 2: True, 3: True}
   N-array +0: shuffle 1 0.009, shuffle 3 0.866, verdict {1: True, 2: False, 3: False}
   N-array +1000: shuffle 1 0.007, shuffle 3 0.854, verdict {1: True, 2: False, 3: False}
   N-array +2000: shuffle 1 0.006, shuffle 3 0.850, verdict {1: True, 2: False, 3: False}
   N-array +3000: shuffle 1 0.006, shuffle 3 0.851, verdict {1: True, 2: False, 3: False}
   N-array +4000: shuffle 1 0.008, shuffle 3 0.861, verdict {1: True, 2: False, 3: False}
offline onset, range analysed window -> partially_reproduced
offline onset, range -1000..+700 ms -> partially_reproduced
move_begins, range analysed window -> not_reproduced
move_begins, range -1000..+700 ms -> not_reproduced
main reading under the five seeds -> ['partially_reproduced', 'partially_reproduced', 'partially_reproduced', 'partially_reproduced', 'partially_reproduced']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); 
for k,v in s['properties'].items(): print(k, json.dumps(v)[:300])
EOF
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version {"const": 3}
id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}
datasets {"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "a
missing_datasets {"description": "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["why"], "properties": {"archive": {"type": "string"}, "id": {"type":
paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}
date {"type": "string", "format": "date"}
entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}
deprecated {"description": "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", "type": "object", "additionalProperties": false, "required": ["date", "reason"], "properties": {"
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"
outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reprodu
verifications {"type": "array", "items": {"type": "object", "additio
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
P=s['properties']
print(json.dumps(P['outcomes']['items']['properties'],indent=0)[:3000])
print(json.dumps(P['findings']['items'],indent=0)[:2500])
print(json.dumps(P['provenance'],indent=0)[:2000])
print(json.dumps(P['datasets']['items'],indent=0)[:1200])
EOF
```

```
{
"claim": {
"description": "Claim id from the target's claims file.",
"type": "string"
},
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
],
"description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
},
"blocked_by": {
"description": "Required when outcome is blocked.",
"enum": [
"data_missing",
"metadata_insufficient",
"methods_underspecified",
[... 271 more lines not kept]
```

**Agent**

Writing the attempt record now.

**Agent calls Write**

```json
{
 "file_path": "attempts/churchland-2012-02.yaml",
 "content": "schema_version: 3\nid: churchland-2012-02\ndatasets:\n- archive: dandi\n  id: \"000070\"\n  version: 0.261122.2046\n  doi: 10.48324/dandi.000070/0.261122.2046\n  relation: primary\npaper: doi:10.1038/nature11129\ndate: 2026-11-24\nentry: churchland-2012\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/encorescience/encore-registry/actions/runs/45507913066\noutcomes:\n- claim: array-dataset-composition\n  outcome: partially_reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:array-dataset-composition\n  measured:\n  - 108\n  - 108\n  - 192\n  - 192\n  notes: Both sessions are in the dandiset (sub-Jenkins ses-20090918 and sub-Nitschke ses-20100923),\n    each with 108 conditions among the 1980 and 2791 trials the Methods select. Each Units table has\n    192 rows, outside 146 +- 14.6 and 218 +- 21.8. The files describe the rows as threshold crossings\n    on each electrode, not sorted (Blackrock unit code 0), one unit per electrode, so they are not\n    the paper's isolations.\n  deviations:\n  - Trials flagged discard_trial are also left out, as the column's description says to do; no\n    trial of the two sessions is flagged.\n- claim: fig3ef-same-direction\n  outcome: reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:fig3ef-same-direction\n  notes: Under the main reading 103 of 108 J-array conditions (95.4%) and 107 of 108 N-array\n    conditions (99.1%) rotate counter-clockwise from -50 to +150 ms; the median net rotation is 97\n    and 113 degrees. Under the four readings the shares are 94.4 to 96.3% (J-array) and 99.1 to 100%\n    (N-array), and 96.3% and 99.1% with 24 ms smoothing. After shuffles 2 and 3 the median share\n    stays at 93 to 98%, and after shuffle 1 it is 58 to 61% (see suppfig3-shuffle-controls). The\n    units are unsorted threshold crossings (192 per session).\n  deviations:\n  - Units are the dandiset's 192 unsorted threshold crossings per session, where the paper used 146\n    and 218 sorted isolations, as the claims file says.\n  - The paper's custom smoothing step that discards features not shared across conditions is not\n    applied; the Methods say it had essentially no effect on the population analyses\n    (Methods, \"Computing average firing rate as a function of time\").\n  - Rates are aligned on movement onset only; the paper also aligned on target onset and the go cue,\n    for presentation.\n  - The trial table has two movement-onset columns, offline_move_onset_time (\"calculated offline\n    using a robust algorithm\") and move_begins_time, 25 ms (J-array) and 52 ms (N-array) apart at\n    the median, and the paper does not say which onset it used (\"data are precisely aligned on\n    movement onset\", Results). The window over which a unit's range is taken for the soft\n    normalisation is not stated either; the codepack takes it over all the times it is given. Both\n    details are run under both readings (four in all); here all four give the same outcome.\n- claim: fig3-independent-of-curvature\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:fig3-independent-of-curvature\n  notes: Under the main reading (offline onset), J-array has 34 clockwise-curving, 21 straight and 53\n    counter-clockwise-curving conditions, of which 88.2%, 100% and 98.1% rotate counter-clockwise;\n    N-array has 36, 18 and 54, at 100%, 100% and 98.1%. The clockwise class of J-array is below 90%\n    and above 75%. Under the two move_begins readings every class is at 92.5% or more in both\n    datasets, which would make the claim reproduced. The velocity-heading variant gives the same\n    outcome as the main measure under each reading (J-array clockwise class 89.7% under the main\n    reading). In J-array a logistic fit finds that reaches curving more clockwise are less likely to\n    rotate counter-clockwise (slope 1.524 per 100 degrees of curvature, p = 0.029); in N-array it\n    finds no relation (slope -0.175, p = 0.873).\n  deviations:\n  - The heading is undefined while the hand is at rest, at onset and when it stops. The net change\n    of heading is taken between the mean path's direction over 5 to 20% of its length and over 80\n    to 95% of it, from movement onset to +500 ms (path smoothed with a 10 ms Gaussian). A variant\n    takes the unwrapped heading of the velocity where speed exceeds 10% of its peak. Both are\n    choices made here, and they agree on the outcome.\n  - Assumed, as the main reading, that the paper's movement onset is the trial table's\n    offline_move_onset_time, which the file describes as calculated offline with a robust algorithm\n    and at which the hand speed starts to rise (median 43 and 15 mm/s at it, under 6 mm/s 50 ms\n    before). The paper says only that the data were precisely aligned on movement onset. Under\n    move_begins_time the outcome would be reproduced.\n- claim: fig3-phase-from-prep-state\n  outcome: partially_reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:fig3-phase-from-prep-state\n  notes: The leave-one-condition-out R2 of the state at +150 ms predicted from the state at -50 ms by\n    one complex gain is 0.568 in J-array and 0.676 in N-array. The median over 20 shuffle-3 runs is\n    0.686 in J-array (0.678 to 0.688 over the five seeds) and 0.600 in N-array (0.586 to 0.600). The\n    criterion holds in N-array and not in J-array, where the shuffled data predict better. All four\n    readings give the same (J-array 0.568 to 0.634 against shuffle medians 0.680 to 0.686).\n  deviations:\n  - The shuffle-3 runs are this claim's own, drawn from its seed, with the dividing point of\n    suppfig3-shuffle-controls (median go cue relative to movement onset plus 50 ms, -277 ms in\n    J-array and -268 ms in N-array); each shuffle's R2 is computed in its own jPCA plane.\n- claim: var-captured-jpc-plane\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:var-captured-jpc-plane\n  measured: 18.9\n  notes: Under the main reading the first jPCA plane captures 14.9% (J-array) and 22.9% (N-array) of\n    the variance, mean 18.9%; the mean is outside 28 +- 2.8% (reading a) and J-array is below 18%\n    (reading b). With the range over -1000 to +700 ms, 15.0% and 23.9%. Under the move_begins\n    readings J-array captures 18.7 to 19.0% and N-array 21.1 to 22.0%, all inside 18 to 38.5%, which\n    would make the claim reproduced under reading (b). With 24 ms smoothing, 15.6% and 23.3%. The\n    units are unsorted threshold crossings, which may hold less of the structure than sorted units.\n  deviations:\n  - Assumed the offline_move_onset_time column as the movement onset (see\n    fig3-independent-of-curvature); under move_begins_time the outcome would be reproduced.\n- claim: pc23-variance\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:pc23-variance\n  measured: 23.8\n  notes: Under the main reading PC2 and PC3 capture 19.2% (J-array) and 28.3% (N-array), mean 23.8%;\n    the mean and the J-array value are outside 29 +- 2.9%. The jPCA plane captures 0.78 (J-array)\n    and 0.81 (N-array) as much variance as PC2 and PC3, so the 80% part fails in J-array. Under the\n    move_begins readings the ratios are 0.84 to 0.95, so the ratio part holds and the values part\n    does not (means 22.5 and 22.9%), which would make the claim partially reproduced.\n  deviations:\n  - Assumed the offline_move_onset_time column as the movement onset (see\n    fig3-independent-of-curvature).\n- claim: suppfig4-j-array-planes\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:suppfig4-j-array-planes\n  measured:\n  - 13.3\n  - 13.3\n  - 12.2\n  - 38.8\n  - 51.9\n  notes: With jPCA on the top 10 PCs of J-array, the first three planes capture 13.3%, 13.3% and\n    12.2% (38.8% together), and the top six PCs 51.9%; only the third plane is within tolerance. The\n    rotations are coherent in each plane, with 98%, 97% and 92% of conditions counter-clockwise, at\n    1.63, 1.24 and 0.79 Hz. The four readings agree (three planes 37.7 to 38.8%, top six PCs 51.9 to\n    54.0%).\n  deviations:\n  - Planes are ordered by the magnitude of their M_skew eigenvalues (Methods, \"the plane defined by\n    the eigenvectors associated with the largest two (complex-conjugate) imaginary eigenvalues\"),\n    and each is oriented as the first.\n- claim: suppfig4-planes-range\n  outcome: partially_reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:suppfig4-planes-range\n  notes: In N-array the three planes capture 47.7% (19.6, 16.2 and 11.9%), inside 45 to 77%, with 97%\n    and 100% of conditions rotating in the first two planes (94% in the third). In J-array they\n    capture 38.8%, below 45%, although 98% and 97% rotate. The four readings agree (J-array 37.7 to\n    38.8%, N-array 45.8 to 48.8%).\n- claim: fig6a-angle-peak\n  outcome: reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:fig6a-angle-peak\n  notes: The 36-bin histogram of the angle between the state and its derivative in the first plane\n    (2160 angles per dataset) peaks at 0.528 pi in J-array and 0.639 pi in N-array under the main\n    reading; under the four readings at 0.528 to 0.583 pi and 0.639 pi. 69% (J-array) and 82%\n    (N-array) of the angles lie within 0.25 pi of pi/2.\n- claim: fig6b-skew-fit\n  outcome: reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:fig6b-skew-fit\n  notes: In 6-D, R2 is 0.415 for M and 0.381 for M_skew in J-array (ratio 0.918), and 0.580 and 0.527\n    in N-array (ratio 0.909). In the first plane the ratios are 0.946 and 0.953. Under the four\n    readings and with 24 ms smoothing, the 6-D ratios are 0.870 to 0.931 and the plane ratios 0.908\n    to 0.975. The paper's figure shows 6-D ratios of about 0.75 to 0.9; the R2 values themselves are\n    not stated in the paper.\n  deviations:\n  - In the plane, M and M_skew are 2 x 2 matrices fitted to the projection onto the first plane\n    (Figure 6b legend, \"the rank 2 matrices that capture dynamics in the first jPCA plane\").\n- claim: rotation-frequency\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:rotation-frequency\n  measured: 1.40\n  notes: The largest eigenvalue of M_skew is 8.44 rad/s (1.344 Hz) in J-array and 8.81 rad/s (1.402\n    Hz) in N-array, inside 1.26 to 2.75 Hz; the measured value given is the larger. With the range\n    over -1000 to +700 ms, 1.333 and 1.416 Hz. Under the move_begins readings J-array gives 1.063\n    to 1.098 Hz, below the range, which would make the claim partially reproduced. With 24 ms\n    smoothing, 1.290 and 1.372 Hz. The paper's own values for the array datasets are not stated.\n  deviations:\n  - Assumed the offline_move_onset_time column as the movement onset (see\n    fig3-independent-of-curvature); under move_begins_time the outcome would be partially reproduced.\n  - The derivative is the difference of samples 10 ms apart (Methods), so eigenvalues per sample are\n    multiplied by 100 to give rad/s.\n- claim: suppfig3-shuffle-controls\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:suppfig3-shuffle-controls\n  notes: Dividing points -277 ms (J-array) and -268 ms (N-array) from movement onset. In J-array the\n    original R2(M_skew) is 0.381; no shuffled run reaches it, and the medians are 0.01 (shuffle 1),\n    0.63 (shuffle 2) and 0.75 (shuffle 3, 0.745) of it, so all three shuffles meet the criterion. In\n    N-array the original is 0.527, and the medians are 0.01, 0.76 and 0.87 of it, so only shuffle 1\n    meets it. The partial outcome (all three shuffles in one dataset) holds under each of the five\n    seeds (J-array shuffle-3 medians 0.725 to 0.745 of the original, N-array 0.850 to 0.866). With\n    the range over -1000 to +700 ms the outcome is also partial (J-array shuffle 3 at 0.77, N-array\n    shuffle 2 at 0.74); under the two move_begins readings it is not reproduced, as J-array shuffle 3\n    is at 0.77 to 0.79 and N-array meets only shuffle 1. After shuffles 2 and 3 the median share of\n    conditions rotating counter-clockwise stays at 93 to 98% and the R2 ratio at 0.86 to 0.94; after\n    shuffle 1 it is 58 to 61% and 0.09 to 0.16. The claim's statement that the shuffles largely\n    remove the rotational structure holds for shuffle 1 only in N-array.\n  deviations:\n  - Shuffle 1 inverts exactly half of the conditions (54 of 108) per unit, drawn at random\n    (Supplementary Figure 2 legend). Inversion reflects each rate after the dividing point about its\n    value there, and reassignment adds the other condition's change from its dividing-point rate to\n    this condition's rate at that point (legend, \"simply appended to the final firing rate during the\n    preparatory state, such that there was no discontinuity\").\n  - Assumed the offline_move_onset_time column as the movement onset (see\n    fig3-independent-of-curvature); under move_begins_time the outcome would be not reproduced.\n- claim: suppfig5-areas-variance\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:suppfig5-areas-variance\n  measured:\n  - 21.6\n  - 20.2\n  - 17.7\n  - 27.1\n  notes: With units split by electrode group (group 1 described as the PMd array, group 2 as M1, 96\n    units each), the first plane captures 21.6% (PMd) and 20.2% (M1) in J-array and 17.7% and 27.1%\n    in N-array; only N-array M1 is within tolerance, and N-array PMd is below 18%, so the partial\n    reading fails as well. Each array rotates (96%, 99%, 91% and 97% of conditions counter-clockwise).\n    The four readings agree (N-array PMd 17.6 to 17.9%). The N-9-10-2010 variant (sub-Nitschke\n    ses-20100910) gives 14.7% (PMd) and 20.8% (M1) against 26% and 24%, with 94% rotating in each.\n- claim: suppfig5-m1-faster\n  outcome: reproduced\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:suppfig5-m1-faster\n  notes: The first-plane frequency is 2.020 Hz for M1 against 0.844 Hz for PMd in J-array, and 1.488\n    against 0.973 Hz in N-array. Under the four readings M1 is higher by 1.059 to 1.176 Hz (J-array)\n    and 0.433 to 0.523 Hz (N-array). The N-9-10-2010 variant agrees (1.659 against 1.063 Hz). The\n    paper calls the difference slight; here M1 is 1.5 to 2.4 times faster.\n- claim: fig6-velocity-model\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:fig6-velocity-model\n  notes: Under the main reading (rates lead the hand by 100 ms, preparatory term falling at movement\n    onset), M_skew fits the simulated population poorly, with 6-D ratios of 0.400 (J-array) and\n    0.244 (N-array), below 0.6 and below the neural 0.918 and 0.909; but the angle distribution peaks\n    at 0.417 pi and 0.639 pi, above pi/4, in both datasets, and 76% and 87% of the simulated\n    conditions rotate counter-clockwise. All five seeds give not reproduced (6-D ratios 0.345 to\n    0.400 and 0.178 to 0.244, peaks 0.306 to 0.472 pi and 0.250 to 0.639 pi). With no lead the\n    criterion holds in both datasets (ratios 0.077 and 0.083, peaks -0.083 pi and 0.083 pi), which\n    would make the claim reproduced; with a persisting preparatory term it fails in both under\n    either lead. The part of the statement that M_skew fits poorly holds under every reading. The\n    simulated population is this attempt's construction from the Methods' description.\n  deviations:\n  - The Methods give the factors (velocity, speed; endpoint and peak speed for the preparatory\n    activity), uniform preferred directions, rates and trial counts matched to the recorded units,\n    and gamma-interval spiking of order 2. They do not give how far the rates lead the hand, the time\n    course of the preparatory term, or the factors' relative weights. Assumed a lead of 100 ms, the\n    usual lead of motor cortical activity over the hand in velocity-tuning models such as the one the\n    paper cites (ref. 27), a preparatory term that falls to zero from -50 to +50 ms around movement\n    onset, and uniform weights from 0 to 1 on unit-SD factors. A lead of 0 ms and a persisting\n    preparatory term were run as the other readings.\n  - Each simulated unit's noiseless rate is scaled to the recorded unit's mean and range over -1000 to\n    +700 ms and rectified; the paper says only that firing rates were matched.\n  - Simulated with the condition-mean hand paths of the session (smoothed with a 20 ms Gaussian\n    before differentiating), under the main pipeline reading only.\n- claim: fig6-complex-kinematic-model\n  outcome: partially_reproduced\n  assumed: true\n  seed_sensitive: true\n  notebook: reproduce_churchland_2012.ipynb\n  output: claim:fig6-complex-kinematic-model\n  notes: Under the main reading M_skew fits poorly in both datasets (6-D ratios 0.095 in J-array and\n    0.144 in N-array, against the neural 0.918 and 0.909). The J-array angle peak is at -0.972 pi,\n    below pi/4 as the criterion asks (the state and its derivative point in opposite directions,\n    not a rotation), and the N-array peak at 0.861 pi is above it. Under the five seeds the outcome\n    is partially reproduced twice and not reproduced three times (6-D ratios 0.089 to 0.096 and 0.129\n    to 0.144; J-array peaks -0.972 to 0.750 pi, N-array 0.528 to 0.861 pi). The other readings give\n    partially reproduced (no lead, either preparatory term) or not reproduced (persisting\n    preparatory term, 100 ms lead). The part of the statement that M_skew fits poorly holds under\n    every reading and seed.\n  deviations:\n  - Uses the Methods' sensitivities (25, 10, 1 and 0.05 spikes/s per m, m/s, m/s2 and m/s3 along the\n    preferred direction). The preparatory term, \"sensitive to target endpoint\", is given 25 spikes/s\n    per m of endpoint along a preparatory preferred direction, an assumption. The lead and the\n    preparatory time course are assumed as for fig6-velocity-model.\n- claim: fig1-leech-and-walking\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The leech optical recordings and the walking-monkey recordings are not in the dandiset,\n    which holds only delayed-reach Utah-array sessions (all ten files were read). The paper says the\n    leech data were recorded by K. Briggman and W. Kristan and gives no public location for either.\n- claim: fig2-single-neuron-responses\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The 469 single-electrode isolations of monkeys A, B, J and N are not in the dandiset, whose\n    ten files are array sessions with unsorted threshold crossings.\n- claim: fig3abcd-single-electrode-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The seven single-electrode datasets (A, B, J1 to J4 and N) are not in the dandiset.\n- claim: fig4-emg-no-rotation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds no EMG; the paper recorded EMG only for the single-electrode datasets.\n- claim: fig5-generator-model\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The generator model is fitted to deltoid EMG, which is not in the dandiset; the paper says it\n    could not be simulated for the array datasets.\n- claim: fig6cd-speed-independent-frequency\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The speed-task datasets of monkeys A and B are not in the dandiset.\nfindings:\n- kind: data_missing\n  severity: major\n  statement: The Units tables of all ten files hold unsorted threshold crossings, one unit per\n    electrode (192 per session), as their description says, where the paper analysed 146 (J-array)\n    and 218 (N-array) sorted single and multi-unit isolations. The sorted isolations are not in the\n    dandiset. On these units the first jPCA plane captures 14.9% and 22.9% of the variance, against\n    the paper's average of 28%.\n- kind: data_missing\n  severity: major\n  statement: The dandiset holds the paper's two array datasets (sub-Jenkins ses-20090918 and\n    sub-Nitschke ses-20100923) and eight further array sessions, one of which (sub-Nitschke\n    ses-20100910) matches the N-9-10-2010 session of Supplementary Figure 5. The seven\n    single-electrode datasets, the EMG, the leech and walking-monkey recordings and the J-11-06-2009\n    session of Supplementary Figure 5 are not in it. Six of the paper's 22 claims cannot be tested.\n- kind: metadata_insufficient\n  severity: major\n  statement: Two sessions, sub-Nitschke ses-20100920 and ses-20100922, have no maze_condition,\n    correct_reach, trial_version, active_target, proto_trial, novel_maze or unhittable columns, which\n    the other eight files have, so their trials cannot be grouped by condition or selected for\n    consistent reaches as in the paper. The paper does not use these sessions.\n- kind: metadata_insufficient\n  severity: minor\n  statement: The trial table has two movement-onset columns, move_begins_time (described as movement\n    onset time) and offline_move_onset_time (calculated offline using a robust algorithm), which\n    differ by a median of 25 ms in J-array and 52 ms in N-array. Nothing says which one is the onset\n    the paper aligned on, and several results change with it (the variance captured by the jPCA\n    plane, 14.9 against 18.7% in J-array, and its frequency, 1.344 against 1.098 Hz). The hand speed\n    starts to rise at offline_move_onset_time.\n- kind: other\n  about: data\n  severity: none\n  statement: The spikes of both arrays are consistent with the clock of the trial table. Reach\n    direction decodes at chance from each array before target onset (0.12 to 0.17 against 0.14 to\n    0.17 with shuffled labels) and above it after target onset (0.37 to 0.70). The lag between the\n    arrays' movement-related changes is constant across six blocks of each session (-4 to 11 ms in\n    J-array, 25 to 32 ms in N-array, M1 later), so there is no drift like that of the LFP's second,\n    slower clock. A constant offset of about 25 ms between the N-array arrays cannot be told apart\n    from a later M1 response.\n- kind: other\n  about: data\n  severity: none\n  statement: Checks that passed. No recording is deposited twice (the trial-interval and spike-count\n    hashes of the ten files all differ). Spike times are sorted within every unit and every analysis\n    window lies inside its trial. Hand position is in mm with a conversion to metres, its speed\n    rises at offline_move_onset_time, and the hand ends a median 9.1 mm (J-array) and 11.4 mm\n    (N-array) from the hit target minus the cursor offset. Electrode groups 1 and 2 are described as\n    the PMd and M1 arrays, 96 units each.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Which movement onset were the array datasets aligned\n    on, the rig's online detection (move_begins_time in the files) or the offline estimate\n    (offline_move_onset_time), and over which times was each neuron's firing-rate range taken for the\n    soft normalisation? The paper says the data were precisely aligned on movement onset. This\n    attempt assumed the offline estimate and the analysed window; with the online onset the\n    variance captured and the rotation frequency of J-array change enough to change four outcomes\n    (var-captured-jpc-plane, pc23-variance, rotation-frequency, suppfig3-shuffle-controls) and that\n    of fig3-independent-of-curvature.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. For the velocity and complex kinematic models, how far\n    did the simulated rates lead the hand, what was the time course of the preparatory term (did it\n    end at movement onset or persist), and how were the factors weighted? With a 100 ms lead and a\n    preparatory term ending at onset, the simulated velocity population here has an angle\n    distribution peaking at 0.42 and 0.64 pi; with no lead it peaks near 0 as in Figure 6a. M_skew\n    fits poorly under every choice.\n"
}
```

```
File created successfully at: attempts/churchland-2012-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/churchland-2012-02.yaml'; s=open(p).read()
old='''attempt assumed the offline estimate and the analysed window; with the online onset the
    variance captured and the rotation frequency of J-array change enough to change four outcomes
    (var-captured-jpc-plane, pc23-variance, rotation-frequency, suppfig3-shuffle-controls) and that
    of fig3-independent-of-curvature.'''
new='''attempt assumed the offline estimate and the analysed window; with the online onset the
    outcomes of five claims would change (fig3-independent-of-curvature, var-captured-jpc-plane,
    pc23-variance, rotation-frequency and suppfig3-shuffle-controls), while the range window
    changes none.'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
import yaml; d=yaml.safe_load(s)
# find ': ' inside values
import re
for i,l in enumerate(s.split('\n')):
    body=re.sub(r'^\s*(- )?[a-z_]+: ','',l)
    if ': ' in body: print(i+1,l)
print(len(d['outcomes']), 'outcomes')
EOF
grep -n "—\|rather\|\*\*" attempts/churchland-2012-02.yaml entries/churchland-2012/README.md entries/churchland-2012/entry.yaml | head
```

```
22 outcomes
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old="(about 6 to 12 ms in J-array and 24 to 33 ms in N-array, M1 later)"
assert old in s
s=s.replace(old,"(-4 to 11 ms in J-array and 25 to 32 ms in N-array over six blocks of the selected trials, M1 later)")
open(p,'w').write(s)
EOF
. dev/bin/activate && python build_nb.py && cd  && date -u && python tools/entry.py all entries/churchland-2012 2>&1 | tail -8
```

```
59 cells
Wed Nov 25 00:01:11 UTC 2026
Installed kernelspec registry-churchland-2012 in executed/churchland-2012/.venv/share/jupyter/kernels/registry-churchland-2012
0 error(s)
pass  reproduce_churchland_2012.ipynb  (594 s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('executed/churchland-2012/reproduce_churchland_2012.ipynb',4)
a=nbformat.read('dev_run.ipynb',4)
def outs(nb): return [''.join(o.get('text','') for o in c.outputs if o.output_type=='stream') for c in nb.cells if c.cell_type=='code']
import difflib
for i,(p,q) in enumerate(zip(outs(a),outs(nb))):
    if p!=q:
        for l in difflib.unified_diff(p.split('\n'),q.split('\n'),lineterm='',n=0): print(i,l[:200])
EOF
cd  && python tools/entry.py handover entries/churchland-2012 2>&1 | tail -5; ls executed/churchland-2012/handover/; date -u
```

```
2 --- 
2 +++ 
2 @@ -1,3 +1,3 @@
2 -J-array: loaded in 43 s; peak memory 1.84 GB
2 -N-array: loaded in 53 s; peak memory 2.55 GB
2 -N-9-10-2010: loaded in 92 s; peak memory 3.00 GB
2 +J-array: loaded in 45 s; peak memory 1.85 GB
2 +N-array: loaded in 57 s; peak memory 2.57 GB
2 +N-9-10-2010: loaded in 43 s; peak memory 3.18 GB
4 --- 
4 +++ 
4 @@ -8,0 +9,5 @@
4 +Drift check: the lag of group 2 behind group 1 in six consecutive blocks of each session, from the change of the
4 +grand-mean rate (10 ms Gaussian) from -400 to +300 ms around movement onset. An unmapped clock running 9.4 ppm slow
4 +(the LFP's second system: 999.9906 against 1000 samples/s) would add about 9.4 ms per 1000 s of session.
4 +J-array: (block start s, lag ms, peak r): [(18, 9, np.float32(0.84)), (2410, 5, np.float32(0.78)), (4921, 11, np.float32(0.76)), (7450, 10, np.float32(0.79)), (10048, -4, np.float32(0.8)), (12908, 4,
4 +N-array: (block start s, lag ms, peak r): [(5, 26, np.float32(0.96)), (4273, 25, np.float32(0.94)), (8145, 28, np.float32(0.94)), (12519, 26, np.float32(0.96)), (16982, 26, np.float32(0.97)), (21547,
21 --- 
21 +++ 
21 @@ -1 +1 @@
[... 12 more lines not kept]
```

**Agent**

I've finished the blind repeat attempt on churchland-2012: 16 claims tested, 6 blocked. The entry is in `entries/churchland-2012/`, the record is `attempts/churchland-2012-02.yaml`, and the handover is in `executed/churchland-2012/handover/`. `entry.py all` passes with 0 errors and the notebook runs in 594 s. I did not come across any earlier attempt.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| array-dataset-composition | partially reproduced (108 conditions each; 192 units each, against 146 and 218) |
| fig3ef-same-direction | reproduced (95.4% and 99.1% of conditions counter-clockwise) |
| fig3-independent-of-curvature | partially reproduced, assumed (J-array clockwise reaches 88.2%, threshold 90%) |
| fig3-phase-from-prep-state | partially reproduced (R2 0.568 and 0.676; J-array falls below its shuffle median of 0.686) |
| var-captured-jpc-plane | not reproduced, assumed (14.9% and 22.9%, against 28%) |
| pc23-variance | not reproduced, assumed (mean 23.8%, against 29%) |
| suppfig4-j-array-planes | not reproduced (13.3, 13.3 and 12.2%; 38.8% together; top six PCs 51.9%) |
| suppfig4-planes-range | partially reproduced (N-array 47.7%, J-array 38.8%) |
| fig6a-angle-peak | reproduced (peaks at 0.53 pi and 0.64 pi) |
| fig6b-skew-fit | reproduced (6-D ratios 0.918 and 0.909) |
| rotation-frequency | reproduced, assumed (1.34 and 1.40 Hz) |
| suppfig3-shuffle-controls | partially reproduced, assumed (all three shuffles pass in J-array, only shuffle 1 in N-array) |
| suppfig5-areas-variance | not reproduced (21.6, 20.2, 17.7 and 27.1%) |
| suppfig5-m1-faster | reproduced |
| fig6-velocity-model | not reproduced, assumed (fit is poor as claimed, but the angle peaks at 0.42 pi and 0.64 pi) |
| fig6-complex-kinematic-model | partially reproduced, assumed, seed sensitive |
| fig1, fig2, fig3abcd, fig4, fig5, fig6cd | blocked, data_missing |

**2. What was found**

The dataset:
- The Units tables hold unsorted threshold crossings, one per electrode (192 per session), not the paper's sorted isolations. The files say this. Rated major.
- Only the paper's two array sessions are in it, plus eight further array sessions. sub-Nitschke ses-20100910 matches the "N-9-10-2010" session of Supplementary Figure 5. Rated major.
- Two sessions not used by the paper, ses-20100920 and ses-20100922, have no `maze_condition` or `correct_reach` columns. Rated major.
- There are two movement-onset columns, 25 to 52 ms apart, with no note saying which one the paper used. Rated minor.
- Checks that passed: no recording is deposited twice. Hand units and alignment are consistent. Both arrays share the trial clock, with no drift over the session. A constant M1 lag of about 25 ms in N-array cannot be told apart from a genuinely later M1 response.

Assumptions:
- The movement onset is `offline_move_onset_time`. The other column would change five outcomes.
- The firing-rate range for normalisation is taken over the analysed window. This changes nothing.
- For the two simulated models, the rates lead the hand by 100 ms, the preparatory term ends at movement onset, and the factors have uniform weights. With no lead, the velocity model would be reproduced.

Questions for the paper's authors: two `methods_unavailable` findings, one on the onset column and range window, one on the simulated-model details. I asked a reader no questions.

**3. Protocol points**
1. The protocol has no rule for a criterion whose literal reading passes a case it was not meant for. The complex-model angle peak of -0.97 pi counts as "below pi/4" but is a contraction, not rotation. I applied the criterion as written and said so in the notes.
2. The claims file names `simulate_population`, a helper from an earlier attempt that the blind checkout does not have. I wrote my own model from the Methods and gave it the same name.
3. The claims file's header refers to "the notebook" and to "clock resets of the 2010 file", both from the earlier attempt. I could not check either against that attempt, so I tested the clock myself.
4. The protocol says nothing on whether a claim that depends on another claim's shuffle runs should reuse them. I gave the phase claim its own shuffle-3 runs from its own seed and recorded this as a deviation.
5. The protocol says "the directory is empty", but `entries/churchland-2012` did not exist. I created it.

**4. Runtime and failures**
The run took about 1 h, from 23:12 to 00:12 UTC. The notebook takes 9.7 min with a peak of 3.5 GB. Nothing failed. My script that stripped extra bold from the markdown also damaged one code line (`** 2`); a diff against the development run caught it before the final run.

## End of run

59 turns, 54 minutes, $5.88 at API prices, result: success.
