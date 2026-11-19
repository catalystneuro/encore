# asari-2009 · author-revise-1 · run 44456522978

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/asari-2009/verifier-1-report.md; ls entries/asari-2009 entries/asari-2009/*; ls paper questions
```

```
Thu Nov 19 04:17:43 UTC 2026
**Verifier report, round 1: Asari & Zador (2009) on CRCNS ac-1. The claims file has 21 claims.**

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| methods-recording-counts | partially_reproduced | Cell 10 matches 305 natural probes in 39 cells and 93 MGB probes in 14 cells, under both silence readings. It finds 133 A1 cells meeting the criterion, not 123, and the synthetic counts don't match (MHT 26 cells vs 39, DMR 15 vs 6; Table 1 rows differ, see B1–B2). The voltage-clamp counts can't be tested because those recordings aren't in the data set. |
| a1-mgb-firing-rates | partially_reproduced | Cell 12: no reading puts all four means within tolerance, because MGB evoked is at most 7.07 Hz against 11.4 ± 1.14. The A1 15-mV reading (0.481 / 0.547 Hz) and the half-threshold MGB reading (spontaneous 0.768, evoked 7.07 > 5 Hz) meet the partial rule. |
| fig2-example-reliability | reproduced | Cell 14: mean over pairs of trials, averaged over cells, is 0.310 ± 0.092 (paper 0.31 ± 0.09). The matched cell gives 0.611 and its probe 0.737. |
| fig2-example-long-context | reproduced | Cell 16, matched probe (20051222-ha1-001-002, probe 4, contexts [0,2,3], 6 repeats): significant periods up to 1.60 s, none in 2.2–3.6 s, then periods from 3.97 s. |
| fig3a-proportion-significant | reproduced | Cell 18, silence counted, all-probes reading: 186 of 305 (within 204 ± 20.4), 0.610 (within 0.669 ± 0.067), late fraction 0.255 (within 0.237 ± 0.024). Noise floor 0.00281 matches the paper's chance level of 2.8×10⁻³. This holds narrowly; the probes-running reading gives 0.270, which is out. |
| fig3a-significance-decay | partially_reproduced | Cell 20: no reading has all four values within tolerance. Two exponentials with the slow constant between 0.5 and 2 s are selected in many readings (e.g. 0.159/0.26 s and 0.072/1.05 s). |
| fig3b-fractional-power-decay | not_reproduced | Cell 22: α is 0.45–0.47 but τ is 1.29–1.78 s in every reading (toler
[... 239 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
713 docs/protocol.md
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
345:### 2. Check the data against its description
360:### 3. Write the entry
443:### 4. Lock, check and run
463:### 5. Record the attempt
538:### 6. Hand over for verification
576:## Repeat attempts
641:## Local and remote datasets
664:## Verifier
668:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,713p docs/protocol.md
```

```
<persisted-output>
Output too large (32.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/bqmndeukg.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-16`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/bqmndeukg.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-16`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
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
[... 538 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep asari; wc -l entries/asari-2009/* attempts/asari-2009*.yaml claims/asari-2009* 2>/dev/null; ls claims | grep asari; cat entries/asari-2009/entry.yaml; ls executed/asari-2009 2>/dev/null; ls questions/ | grep asari
```

```
asari-2009-03.yaml
    44 entries/asari-2009/README.md
   980 entries/asari-2009/asari.py
    24 entries/asari-2009/entry.yaml
  1429 entries/asari-2009/reproduce_asari_2009.ipynb
     6 entries/asari-2009/requirements.in
  1521 entries/asari-2009/requirements.lock.txt
   418 attempts/asari-2009-03.yaml
   720 claims/asari-2009.yaml
  5142 total
asari-2009.yaml
schema_version: 1
name: asari-2009
type: reproduction
title: Long-lasting context dependence in rat auditory cortex (Asari & Zador 2009)
description: Tests the findings of Asari and Zador (2009) on CRCNS ac-1, which holds Hiroki
  Asari's whole-cell recordings from rat A1 (natural and synthetic sound ensembles) and
  cell-attached recordings from the auditory thalamus, with the authors' analysis code. It measures
  how long the response to a sound depends on the sound before it, by a pointwise Kruskal-Wallis
  test and a fractional power measure, how this depends on the property that varies among
[... 17 more lines not kept]
```

**Agent**

Starting with the attempt record, the helper and the notebook, so I can plan fixes around the 35-minute full run.

**Agent calls Read**

```json
{
 "file_path": "attempts/asari-2009-03.yaml"
}
```

```
1	schema_version: 3
2	id: asari-2009-03
3	datasets:
4	- archive: crcns
5	  id: ac-1
6	  version: unversioned
7	  doi: 10.6080/K0KW5CXR
8	  relation: primary
9	paper: doi:10.1152/jn.00577.2009
10	date: 2026-11-19
11	entry: asari-2009
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-16
20	  runner:
[... 399 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60; grep -n "verification\|proposed" schemas/*attempt* 2>/dev/null | head -40; ls schemas 2>/dev/null
```

```
attempts/amjad-2025-01.yaml
attempts/andrews-2024-01.yaml
attempts/armstrong-2026-01.yaml
verifications:
- date: '2026-10-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
    reward_blocks). It had no attempt record and took the claims from the claims file.
  results:
  - claim: insertion-yield
    agrees: true
    outcome: blocked
    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
      not in the archive.
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 380,470p schemas/attempt.schema.json
```

```
"not": {
                    "const": "blocked"
                  }
                }
              }
            }
          }
        ]
      }
    },
    "verifications": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "date",
          "kind",
          "by",
          "results"
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,140p entries/asari-2009/asari.py
```

```
"""Loading and context-dependence measures for CRCNS ac-1 (Asari & Zador 2009).

The data set is read in place from the public S3 bucket ``crcnsarchive``
(docs/archives.md, "CRCNS"): each zip is opened over range requests with
fsspec and ``zipfile``, and each MATLAB file is read into memory, reduced to
what the analysis needs, and dropped.

Where a parameter comes from:

- Paper, Methods, Analysis: the 10-ms median filter that clips spikes; the
  Kruskal-Wallis test at each 0.1-ms point, P < 0.01 held for 5 ms (50
  points); the shuffle noise floor (1000 shuffles of trials across contexts
  per probe); the power estimates of Eqs. 17 to 19 and the running mean over
  [0, 2t] of the denominator of Eqs. 20 and 43; Eq. 44 for the exponential
  fits and its rule that each exponential carry at least a tenth of the total;
  the 100-ms PSTH bins and Eq. 42 for the thalamus; Eq. 45 for the noise
  autocorrelation. MGB spikes by a high-pass filter and a threshold, with the
  spike at the peak (Methods, Analysis, paragraph 3).
- The authors' own analysis code, shipped with the data set
  (``asari/Tools/CxtDep.m``, ``GetEvoked.m``, ``ViewResp.m``, ``GetSpikes.m``
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,560p entries/asari-2009/asari.py
```

```
"""
    zname, member = member_index()[path]
    b = open_zip(zname).read(member)
    names = ["triggers", "param"] + (["response"] if trace else [])
    m = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False,
                    variable_names=names)
    del b
    p = m["param"]
    notes = [str(s) for s in _lst(p.notes)] if "notes" in p._fieldnames else []
    seqs, rep = parse_notes(notes)
    stim = []
    if "stimulus" in p._fieldnames:
        for s in _lst(p.stimulus):
            stim.append(dict(name=_s(s.name), description=_s(s.description),
                             file=_s(getattr(s, "file", "")),
                             param={k: getattr(s.param, k) for k in s.param._fieldnames}))
    trig = []
    for t in _lst(m.get("triggers", [])):
        trig.append(dict(type=str(t.type), time=int(t.time),
                         param={k: getattr(t.param, k) for k in t.param._fieldnames}))
[... 401 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 560,980p entries/asari-2009/asari.py
```

```
reversal): anything that is not a TORC, DMR, MHT or modulated coloured
    noise, nor silence."""
    desc = s["description"]
    return bool(desc) and desc != "[]" and not any(
        k in desc for k in ("TORC", "DMR", "Modulated Harmonic", "pink noise"))


def property_classes(d: dict) -> dict:
    """Sets of fragments (1-based) that differ from each other in one property
    only. TORC and DMR ensembles are labelled in their descriptions ("amplitude
    variants", "bandwidth variants", "frequency variants"); MHT and
    natural-sound variants are told apart by their parameters; a natural sound
    and the modulated coloured noise made from it (same stimulus file) form a
    higher-order class (Table 1 legend)."""
    st = d["stim"]
    out = {p: [] for p in PROPERTIES}
    typ = d["triggers"][0]["type"] if d["triggers"] else ""
    syl = lambda s: _norm(s["param"].get("syllables"))
    if typ in ("torc", "dmr"):
        groups = {}
[... 401 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python - <<'EOF'
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== cell {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')}")
    print(src)
EOF
```

```
<persisted-output>
Output too large (51.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/bikvw84w0.txt

Preview (first 2KB):
=== cell 0 [markdown] tags=None
# Reproducing Asari & Zador (2009) on CRCNS ac-1

Paper: H. Asari and A. M. Zador (2009), "Long-Lasting Context Dependence Constrains Neural
Encoding Models in Rodent Auditory Cortex", J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.
The claims file (`claims/asari-2009.yaml`) was written from the version of record (a text
extraction of the publisher's PDF); the online supplement was not read.

Dataset: CRCNS ac-1 (doi:10.6080/K0KW5CXR), read in place from the public S3 bucket
`crcnsarchive` (`ac-1/crcns-ac1.zip`, `crcns-ac1-asari-results-1.zip`,
`crcns-ac1-asari-results-2.zip`). CRCNS data sets are not versioned, so the version is
`unversioned`; it is pinned by the MD5 sums of the three zips, printed below from the data set's
`checksums.md5` (docs/archives.md, "CRCNS"). This is the only published version, so it is the one
used. Of the data set, this notebook uses Hiroki Asari's recordings (`asari/` and the two results
zips). Michael Wehr's recordings (`wehr/`), which the paper reanalyses for its STRF models
(Figure 4), are not used: that claim was not run in the time of this attempt.
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/bikvw84w0.txt"
}
```

```
1	=== cell 0 [markdown] tags=None
2	# Reproducing Asari & Zador (2009) on CRCNS ac-1
3	
4	Paper: H. Asari and A. M. Zador (2009), "Long-Lasting Context Dependence Constrains Neural
5	Encoding Models in Rodent Auditory Cortex", J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.
6	The claims file (`claims/asari-2009.yaml`) was written from the version of record (a text
7	extraction of the publisher's PDF); the online supplement was not read.
8	
9	Dataset: CRCNS ac-1 (doi:10.6080/K0KW5CXR), read in place from the public S3 bucket
10	`crcnsarchive` (`ac-1/crcns-ac1.zip`, `crcns-ac1-asari-results-1.zip`,
11	`crcns-ac1-asari-results-2.zip`). CRCNS data sets are not versioned, so the version is
12	`unversioned`; it is pinned by the MD5 sums of the three zips, printed below from the data set's
13	`checksums.md5` (docs/archives.md, "CRCNS"). This is the only published version, so it is the one
14	used. Of the data set, this notebook uses Hiroki Asari's recordings (`asari/` and the two results
15	zips). Michael Wehr's recordings (`wehr/`), which the paper reanalyses for its STRF models
16	(Figure 4), are not used: that claim was not run in the time of this attempt.
17	
18	This is a repeat attempt, made blind to earlier attempts.
19	
20	| Claim | Tested here |
[... 827 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/asari-2009/reproduce_asari_2009.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''
    for o in c.get('outputs',[]):
        out+=o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o.get('text',''))
        if 'data' in o and 'text/plain' in o['data']: out+=''.join(o['data']['text/plain'])
    print(f"=== cell {i}"); print(out[:3000])
EOF
```

```
<persisted-output>
Output too large (30.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/b51i2rtxr.txt

Preview (first 2KB):
=== cell 1

=== cell 3
18537da81d98e311c0274f62aea04daa  crcns-ac1-asari-results-1.zip
2f7ab955cc778fc6839ce59ed51bce89  crcns-ac1-asari-results-2.zip
2300ee76d93383ab8c808ddf16761a23  crcns-ac1.zip
bd87f2663a3b383dc33de4841d601d54  filelist.txt

%==========================================================================
% DATA
%
%   The data sets contain neural responses to various sound stimuli in 
%   anesthetized rat primary auditory cortex (in vivo whole-cell 
%   recordings) and auditory thalamus (in vivo cell-attached recordings), 
%   obtained by Hiroki Asari (Zador Lab, CSHL; 2005 - 2007).
%   The main analysis results were shown in:
[... 42 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/b51i2rtxr.txt"
}
```

```
1	=== cell 1
2	
3	=== cell 3
4	18537da81d98e311c0274f62aea04daa  crcns-ac1-asari-results-1.zip
5	2f7ab955cc778fc6839ce59ed51bce89  crcns-ac1-asari-results-2.zip
6	2300ee76d93383ab8c808ddf16761a23  crcns-ac1.zip
7	bd87f2663a3b383dc33de4841d601d54  filelist.txt
8	
9	%==========================================================================
10	% DATA
11	%
12	%   The data sets contain neural responses to various sound stimuli in 
13	%   anesthetized rat primary auditory cortex (in vivo whole-cell 
14	%   recordings) and auditory thalamus (in vivo cell-attached recordings), 
15	%   obtained by Hiroki Asari (Zador Lab, CSHL; 2005 - 2007).
16	%   The main analysis results were shown in:
17	%
18	%       H. Asari and A. M. Zador (submitted) 
19	%       "Long-lasting context dependence constrains neural encoding models 
20	%       in rodent auditory cortex."
[... 320 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/asari-2009.yaml'))
print([k for k in c if k!='claims'])
for cl in c['claims']:
    if cl['id'] in ('methods-recording-counts','fig4-strf-performance-low','fig8a-proportion-by-property','fig8c-relative-effects','fig8-natural-synthetic-probes-alike','fig9-mgb-fast-decay','fig7-example-frequency-context','fig8b-decay-by-property'):
        print(yaml.safe_dump(cl, width=110, sort_keys=False))
EOF
```

```
['schema_version', 'paper', 'checks']
id: methods-recording-counts
statement: Of 194 A1 cells recorded in current clamp, 123 met the analysis criterion (39 tested with natural sounds,
  14 with TORCs, 6 with DMRs, 39 with modulated harmonic tones, 27 with modulated colored noise); 14 of 42 voltage-clamped
  cells and 14 of 16 MGB cells were analysed.
source: Methods, Electrophysiology, paragraphs 2 and 3; Table 1
quote: All together, we recorded from 194 cells in 139 animals in current-clamp mode, of which 123 cells met our
  criterion for the analysis ... Of these, 39 cells were examined with natural sound ensembles, 14 cells with ensembles
  of temporally orthogonal ripple combinations, 6 cells with ensembles of dynamic moving ripples, 39 cells with
  ensembles of modulated harmonic tones, and 27 cells with ensembles of modulated colored noise ensembles
expected:
- quantity: A1 current-clamp cells meeting the criterion
  value: 123
  tolerance: 0
- quantity: A1 cells with natural sound ensembles (current clamp)
  value: 39
  tolerance: 0
- quantity: natural sound probes in A1 current clamp (Table 1, all properties)
  value: 305
  tolerance: 0
[... 209 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; timeout 600 python - <<'EOF'
import asari as A
z=A.open_zip(A.ZIPS['main'])
names=[i.filename for i in z.infolist()]
print(len(names))
print([n for n in names if n.startswith('asari/') and not n.startswith('asari/Stimuli')][:200])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "entries/asari-2009/asari.py", line 49, in <module>
    import fsspec
ModuleNotFoundError: No module named 'fsspec'
```

**Agent calls Bash**

```bash
cd  ls -a; ls .venv* envs 2>/dev/null | head; grep -n "venv\|def cmd_run\|def run" tools/entry.py | head -30
```

```
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -a executed/asari-2009/; ls executed/asari-2009/.venv/bin 2>/dev/null | head
```

```
.
..
.clean-run.json
.venv
reproduce_asari_2009.ipynb
result.json
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
deactivate.bat
debugpy
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; timeout 600 $PY - <<'EOF'
import asari as A
z=A.open_zip(A.ZIPS['main'])
names=[i.filename for i in z.infolist()]
print(len(names))
print([n for n in names if n.startswith('asari/') and 'Stimuli' not in n][:300])
EOF
```

```
1823
['asari/', 'asari/Summary.mat', 'asari/Contents.m', 'asari/Tools/', 'asari/Tools/ViewResp.m', 'asari/Tools/ViewCxtDep.m', 'asari/Tools/SoundTrans.m', 'asari/Tools/TuningCurve.m', 'asari/Tools/PinkNoise.m', 'asari/Tools/MovingRipple4.m', 'asari/Tools/MHTones.m', 'asari/Tools/MakeWhiteNoise.m', 'asari/Tools/MakeTone.m', 'asari/Tools/MakeRandomChords.m', 'asari/Tools/MakeRamp.m', 'asari/Tools/logspectrogram.m', 'asari/Tools/GetSpikes.m', 'asari/Tools/GetEvoked.m', 'asari/Tools/GetData.m', 'asari/Tools/DMRipple2.m', 'asari/Tools/CxtDep.m', 'asari/Results/', 'asari/Results/README-Results.txt']
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; mkdir -p $TMPDIR/tools; timeout 600 $PY - <<'EOF'
import asari as A, os
z=A.open_zip(A.ZIPS['main'])
for n in ['CxtDep.m','ViewCxtDep.m','GetSpikes.m','GetEvoked.m','ViewResp.m','MHTones.m','SoundTrans.m','PinkNoise.m']:
    open(os.environ['TMPDIR']+'/tools/'+n,'wb').write(z.read('asari/Tools/'+n))
print(z.read('asari/Results/README-Results.txt').decode('latin-1')[:6000])
EOF
wc -l $TMPDIR/tools/*; grep -n -i "synth\|property\|varian\|mht\|pink\|torc\|dmr" $TMPDIR/tools/CxtDep.m | head -50
```

```
Result files (which originally were in this directory) are now in
two separate zip files:
crcns-ac1-asari-results-1.zip, and
crcns-ac1-asari-resluts-2.zip.

  398 /tmp/claude-1001/tools/CxtDep.m
  166 /tmp/claude-1001/tools/GetEvoked.m
  318 /tmp/claude-1001/tools/GetSpikes.m
  294 /tmp/claude-1001/tools/MHTones.m
   64 /tmp/claude-1001/tools/PinkNoise.m
  158 /tmp/claude-1001/tools/SoundTrans.m
  266 /tmp/claude-1001/tools/ViewCxtDep.m
  237 /tmp/claude-1001/tools/ViewResp.m
 1901 total
46:%       .invariant : context-invariant (model predictive) power
215:        [PARAM(i).total,PARAM(i).predictable,PARAM(i).invariant] = FracPow(PARAM(i)); % fractional power measure
253:        if strcmpi(stimtype,'pinknoise') && isfield(stim(i).param,'iter')
254:            tmp = PinkNoise(tmp.stimulus.sample(:),stim(i).param);
261:            case 'dmr',         tmp = DMRipple2(stim(i).param);
262:            case 'synthetic',   tmp = MHTones(stim(i).param);
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; cat > $TMPDIR/survey.py <<'EOF'
import asari as A, pickle, os, time
def meta(p):
    d=A.load(p, trace=False)
    return d
if __name__=='__main__':
    t=time.time()
    F=A.file_lists()
    pickle.dump(F, open(os.environ['TMPDIR']+'/F.pkl','wb'))
    M=A.run_many(meta,[(p,) for p in F['synthetic']+F['other']])
    pickle.dump(M, open(os.environ['TMPDIR']+'/synmeta.pkl','wb'))
    print(time.time()-t)
EOF
cp $TMPDIR/survey.py .; time timeout 1200 $PY survey.py; rm survey.py
```

```
18.657521963119507

real	0m19.592s
user	0m13.200s
sys	0m3.676s
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import pickle, os, collections
M=pickle.load(open(os.environ['TMPDIR']+'/synmeta.pkl','rb'))
F=pickle.load(open(os.environ['TMPDIR']+'/F.pkl','rb'))
nsyn=len(F['synthetic'])
for d in M[:nsyn]:
    typ=d['triggers'][0]['type'] if d['triggers'] else ''
    if typ!='naturalistic' and typ!='synthetic': continue
    print('---',d['path'].split('/')[-1], typ, 'rep',d['rep'], d['description'][:80], 'nseq',len(d['seqs']))
    for i,s in enumerate(d['stim'],1):
        print('  ',i, s['description'][:70],'|',s['file'][-30:],'|',sorted(s['param'].keys())[:20])
EOF
```

```
<persisted-output>
Output too large (86.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/b41vkj5sh.txt

Preview (first 2KB):
--- 20061022-ha4-001-002.mat synthetic rep 5 Natural sound probe following synthetic sound variants (amplitude, frequency, am nseq 18
   1 neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to  | class6/6l.mat | ['duration', 'ramp', 'sf']
   2 Modulated Harmonic Tone 1 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   3 Modulated Harmonic Tone 2 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   4 Modulated Harmonic Tone 3 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   5 Modulated Harmonic Tone 4 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   6 Modulated Harmonic Tone 5 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   7 Modulated Harmonic Tone 6 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   8 Modulated Harmonic Tone 7 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   9 Modulated Harmonic Tone 8 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   10 Modulated Harmonic Tone 9 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   11 Modulated Harmonic Tone 10 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration', 'f0', 'iniphase', 'm', 'ramp', 'sf']
   12 Modulated Harmonic Tone 11 |  | ['AMmean', 'AMrange', 'AMstd', 'FMrange', 'FMstd', 'df', 'duration',
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import pickle, os, collections, re
M=pickle.load(open(os.environ['TMPDIR']+'/synmeta.pkl','rb'))
F=pickle.load(open(os.environ['TMPDIR']+'/F.pkl','rb'))
nsyn=len(F['synthetic'])
agg=collections.Counter()
for d in M[:nsyn]:
    typ=d['triggers'][0]['type'] if d['triggers'] else ''
    kinds=collections.Counter(re.sub(r'[\d\.]+.*','',s['description'])[:30] for s in d['stim'])
    key=(typ, d['description'][:90], tuple(sorted(kinds.items())))
    agg[key]+=1
for k,v in sorted(agg.items()):
    print(v, k)
EOF
```

```
5 ('dmr', 'Combinations of 4 synthetic sounds', (('DMR', 4),))
2 ('dmr', 'Combinations of 4 synthetic sounds', (('DMR; amplitude variants', 4),))
5 ('dmr', 'Combinations of 4 synthetic sounds', (('DMR; amplitude variants', 16), ('neotropical-mammals-', 1)))
1 ('dmr', 'Combinations of 4 synthetic sounds', (('DMR; frequency variants', 12), ('diversity Track ', 1)))
4 ('dmr', 'Combinations of 4 synthetic sounds', (('DMR; frequency variants', 12), ('neotropical-mammals-', 1)))
1 ('naturalistic', 'Combinations of 4 synthetic sounds', (('diversity Track ', 16),))
8 ('naturalistic', 'Combinations of 4 synthetic sounds', (('neotropical-mammals-', 16),))
1 ('naturalistic', 'Combinations of 6 naturalistic sounds', (('amplitude variant', 1), ('diversity Track ', 1), ('frequency variant ', 2), ('randomized syllables', 1), ('reversed stimulus in time', 1)))
4 ('naturalistic', 'Combinations of 6 naturalistic sounds', (('amplitude variant', 1), ('frequency variant ', 2), ('neotropical-mammals-', 1), ('randomized syllables', 1), ('reversed stimulus in time', 1)))
6 ('pinknoise', 'Combinations of 4 sounds (2 natural sounds, each with corresponding pink noise)', (('diversity Track ', 1), ('neotropical-mammals-', 1), ('pink noise corresponding to na', 2)))
7 ('pinknoise', 'Combinations of 6 sounds (2 natural sounds, each with 2 corresponding pink noise)', (('diversity Track ', 1), ('neotropical-mammals-', 1), ('pink noise corresponding to na', 4)))
1 ('pinknoise', 'Combinations of 6 sounds (2 natural sounds, each with 2 corresponding pink noise)', (('diversity Track ', 2), ('pink noise corresponding to na', 4)))
3 ('pinknoise', 'Combinations of 6 sounds (3 natural sounds, each with corresponding pink noise)', (('diversity Track ', 1), ('neotropical-mammals-', 2), ('pink noise corresponding to na', 3)))
7 ('pinknoise', 'Combinations of 6 sounds (3 natural sounds, each with corresponding pink noise)', (('diversity Track ', 2), ('neotropical-mammals-', 1), ('pink noise corresponding to n
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import pickle, os, collections, re
import numpy as np
M=pickle.load(open(os.environ['TMPDIR']+'/synmeta.pkl','rb'))
F=pickle.load(open(os.environ['TMPDIR']+'/F.pkl','rb'))
nsyn=len(F['synthetic'])
shown=0
for d in M[:nsyn]:
    typ=d['triggers'][0]['type'] if d['triggers'] else ''
    if typ=='naturalistic' and d['description'].startswith('Combinations of 4'):
        print('---',d['path'], d['rep'], d['seqs'][:6], len(d['seqs']))
        print('\n'.join(d['notes'][:30]))
        for i,s in enumerate(d['stim'],1):
            p={k:(np.round(np.asarray(v,float),3).tolist() if not hasattr(v,'_fieldnames') and np.asarray(v).dtype.kind in 'fiu' else str(v)[:40]) for k,v in s['param'].items()}
            print(' ',i,s['description'][:60],'|',s['file'],'|',p)
        shown+=1
        if shown==2: break
EOF
```

```
--- Results/20060904-ha1-001/20060904-ha1-001-002.mat 4 [[15, 2, 16, 2], [3, 2, 7, 2], [8, 2, 4, 2], [9, 2, 11, 2], [12, 2, 14, 2], [6, 2, 5, 2]] 8
Stimulus sequences are given as follows.          
Seq.1:  15   2  16   2                            
Seq.2:  3  2  7  2                                
Seq.3:  8  2  4  2                                
Seq.4:  9   2  11   2                             
Seq.5:  12   2  14   2                            
Seq.6:  6  2  5  2                                
Seq.7:  13   2   1   2                            
Seq.8:  2   2  10   2                             
                                                  
Effective repeats:  4                             
                                                  
See also SoundTrans.m, DMRipple2.m, and MHTones.m.
                                                  
Forgot to save the state of RANDN function.       
  1 neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From  | class6/6l.mat | {'ramp': 5.0, 'duration': 5475.014, 'sf': 97656.0, 'attenuation': 3.162}
  2 neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From  | class6/6l.mat | {'ramp': 5.0, 'duration': 5475.014, 'sf': 97656.0, 'attenuation': 1.0}
  3 neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From  | class6/6l.mat | {'ramp': 5.0, 'duration': 5475.014, 'sf': 97656.0, 'attenuation': 0.316}
  4 neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From  | class6/6l.mat | {'ramp': 5.0, 'duration': 5475.014, 'sf': 97656.0, 'attenuation': 0.1}
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import pickle, os, collections, re
import numpy as np, asari as A
M=pickle.load(open(os.environ['TMPDIR']+'/synmeta.pkl','rb'))
F=pickle.load(open(os.environ['TMPDIR']+'/F.pkl','rb'))
nsyn=len(F['synthetic'])
for d in M[:nsyn]:
    typ=d['triggers'][0]['type'] if d['triggers'] else ''
    if typ not in ('synthetic',): continue
    T=A.synthetic_tests(d)
    c=collections.Counter((t['prop'],'N' if t['natural'] else 'S') for t in T)
    print(d['path'].split('/')[-1], d['description'][:40], 'rep',d['rep'],'nseq',len(d['seqs']), dict(c))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
  File "entries/asari-2009/asari.py", line 638, in synthetic_tests
    P = pairs(d, silence=False)
  File "entries/asari-2009/asari.py", line 217, in pairs
    lens = fragment_samples(d)
  File "entries/asari-2009/asari.py", line 183, in fragment_samples
    return np.array([int(round(float(s["param"]["duration"]) / 1000 * d["sf"]))
                                                                      ~^^^^^^
KeyError: 'sf'
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; cat > $TMPDIR/tab.py <<'EOF'
import pickle, os, collections, re, sys
import numpy as np, asari as A
M=pickle.load(open(os.environ['TMPDIR']+'/synmeta.pkl','rb'))
F=pickle.load(open(os.environ['TMPDIR']+'/F.pkl','rb'))
nsyn=len(F['synthetic'])
for d in M: d['sf']=10000
def tabulate(fn=A.synthetic_tests, show=None):
    tot=collections.Counter(); cells=collections.defaultdict(set)
    for d in M[:nsyn]:
        if (d['rep'] or 0)<4: continue
        typ=d['triggers'][0]['type'] if d['triggers'] else ''
        T=fn(d)
        c=collections.Counter((t['prop'],'N' if t['natural'] else 'S') for t in T)
        if show and typ in show:
            print(typ, d['path'].split('/')[-1], d['description'][:40], 'rep',d['rep'],'nseq',len(d['seqs']), dict(c))
        for t in T:
            row = 'NS' if t['natural'] else typ
            tot[(t['prop'],row)]+=1; cells[(t['prop'],row)].add(d['cell'])
    for k in sorted(tot): print(k, tot[k], len(cells[k]))
EOF
$PY -c "
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from tab import *
tabulate(show=('synthetic','naturalistic'))"
```

```
synthetic 20061022-ha4-001-002.mat Natural sound probe following synthetic  rep 5 nseq 18 {('amplitude', 'N'): 1, ('frequency', 'N'): 1, ('AM', 'N'): 1, ('FM', 'N'): 1}
synthetic 20061022-ha6-001-002.mat Natural sound probe following synthetic  rep 6 nseq 18 {('amplitude', 'N'): 1, ('frequency', 'N'): 1, ('AM', 'N'): 1, ('FM', 'N'): 1}
synthetic 20061022-ha6-001-003.mat Natural sound probe following synthetic  rep 7 nseq 18 {('amplitude', 'N'): 1, ('frequency', 'N'): 1, ('AM', 'N'): 1, ('FM', 'N'): 1}
synthetic 20061022-ha6-002-002.mat Natural sound probe following synthetic  rep 6 nseq 18 {('amplitude', 'N'): 1, ('frequency', 'N'): 1, ('AM', 'N'): 1, ('FM', 'N'): 1}
synthetic 20061022-ha7-001-002.mat Natural sound probe following synthetic  rep 4 nseq 18 {('amplitude', 'N'): 1, ('frequency', 'N'): 1, ('AM', 'N'): 1, ('FM', 'N'): 1}
synthetic 20061022-ha7-003-003.mat Natural sound probe following synthetic  rep 4 nseq 18 {('amplitude', 'N'): 1, ('frequency', 'N'): 1, ('AM', 'N'): 1, ('FM', 'N'): 1}
naturalistic 20061125-ha1-001-002.mat Combinations of 6 naturalistic sounds rep 5 nseq 6 {('amplitude', 'N'): 6, ('frequency', 'N'): 6}
naturalistic 20061125-ha2-003-002.mat Combinations of 6 naturalistic sounds rep 6 nseq 6 {('amplitude', 'N'): 6, ('frequency', 'N'): 6}
naturalistic 20061126-ha1-002-002.mat Combinations of 6 naturalistic sounds rep 4 nseq 6 {('amplitude', 'N'): 6, ('frequency', 'N'): 6}
naturalistic 20061126-ha1-003-002.mat Combinations of 6 naturalistic sounds rep 4 nseq 6 {('amplitude', 'N'): 6, ('frequency', 'N'): 6}
naturalistic 20061201-ha2-001-002.mat Combinations of 6 naturalistic sounds rep 5 nseq 6 {('amplitude', 'N'): 6, ('frequency', 'N'): 6}
naturalistic 20060904-ha1-001-002.mat Combinations of 4 synthetic sounds rep 4 nseq 8 {('amplitude', 'N'): 2}
naturalistic 20060906-ha1-001-002.mat Combinations of 4 synthetic sounds rep 6 nseq 8 {('amplitude', 'N'): 2}
naturalistic 20060908-ha1-001-002.mat Combinations of 4 synthetic sounds rep 6 nseq 8 
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import pickle, os, numpy as np, asari as A
M=pickle.load(open(os.environ['TMPDIR']+'/synmeta.pkl','rb'))
for name in ['20060929-ha1-001-003','20060930-ha2-003-002','20061022-ha4-001-002']:
    d=[d for d in M if name in d['path']][0]; d['sf']=10000
    print('---',name, d['description']); print('\n'.join(l.strip() for l in d['notes'] if l.strip()))
    for i,s in enumerate(d['stim'],1):
        p={k:(np.round(np.asarray(v,float),3).tolist() if np.asarray(v).dtype.kind in 'fiu' else str(v)[:30]) for k,v in s['param'].items() if k not in ('iniphase','sf','ramp')}
        print(' ',i,s['description'][:40],'|',s['file'][-15:],'|',p)
    print(A.property_classes(d))
    print([(t['prop'],t['probe'],t['cls'],t['natural']) for t in A.synthetic_tests(d)])
EOF
```

```
--- 20060929-ha1-001-003 Combinations of 4 synthetic sounds
Stimulus sequences are given as follows.
Seq.1:  6  1  2  1
Seq.2:  9  1  8  1
Seq.3:  7  1  4  1
Seq.4:  1  13   1  14   1
Seq.5:  11   1  12   1
Seq.6:  16   1   5   1
Seq.7:  10   1   3   1
Seq.8:  15   1  17   1
Effective repeats:  5
See also SoundTrans.m, DMRipple2.m, and MHTones.m.
Forgot to save the state of RANDN function.
  1 neotropical-mammals-1 Track 07 (Greater  | class5/2l.mat | {'duration': 5079.37}
  2 Modulated Harmonic Tone 1 |  | {'m': 7.0, 'f0': 3000.0, 'duration': 5000.0, 'AMrange': [], 'AMmean': 63.0, 'AMstd': 5.0, 'FMrange': [], 'FMstd': 333.333}
  3 Modulated Harmonic Tone 2 |  | {'m': 7.0, 'f0': 3000.0, 'duration': 5000.0, 'AMrange': [0.0, 4.0], 'AMmean': 63.0, 'AMstd': 5.0, 'FMrange': [], 'FMstd': 333.333}
  4 Modulated Harmonic Tone 3 |  | {'m': 7.0, 'f0': 3000.0, 'duration': 5000.0, 'AMrange': [4.0, 12.0], 'AMmean': 63.0, 'AMstd': 5.0, 'FMrange': [], 'FMstd': 333.333}
  5 Modulated Harmonic Tone 4 |  | {'m': 7.0, 'f0': 3000.0, 'duration': 5000.0, 'AMrange': [12.0, 24.0], 'AMmean': 63.0, 'AMstd': 5.0, 'FMrange': [], 'FMstd': 333.333}
  6 Modulated Harmonic Tone 5 |  | {'m': 7.0, 'f0': 3000.0, 'duration': 5000.0, 'AMrange': [], 'AMmean': 63.0, 'AMstd': 5.0, 'FMrange': [0.0, 4.0], 'FMstd': 333.333}
  7 Modulated Harmonic Tone 6 |  | {'m': 7.0, 'f0': 3000.0, 'duration': 5000.0, 'AMrange': [0.0, 4.0], 'AMmean': 63.0, 'AMstd': 5.0, 'FMrange': [0.0, 4.0], 'FMstd': 333.333}
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "table 1" paper/10.1152-jn.00577.2009.txt | head; grep -n "TABLE 1" -A 40 paper/10.1152-jn.00577.2009.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from tab import *
once=collections.defaultdict(set); cells=collections.defaultdict(set); byfile=collections.defaultdict(collections.Counter)
for d in M[:nsyn]:
    if (d['rep'] or 0)<4: continue
    typ=d['triggers'][0]['type'] if d['triggers'] else ''
    for t in A.synthetic_tests(d):
        row='NS' if t['natural'] else typ
        key=(t['prop'],row)
        once[key].add((d['path'],t['probe'])); cells[key].add(d['cell'])
        byfile[key][(typ,d['description'][:25])]+=0
    for t in A.synthetic_tests(d):
        row='NS' if t['natural'] else typ
        byfile[(t['prop'],row)][(typ,d['description'][:25])]+=1
for k in sorted(once): print(k, len(once[k]), len(cells[k]), dict(byfile[k]))
EOF
```

```
('AM', 'NS') 25 24 {('synthetic', 'Natural sound probe follo'): 6, ('synthetic', 'Combinations of 4 synthet'): 76}
('AM', 'synthetic') 14 2 {('synthetic', 'Combinations of 4 synthet'): 14}
('FM', 'NS') 25 24 {('synthetic', 'Natural sound probe follo'): 6, ('synthetic', 'Combinations of 4 synthet'): 76}
('amplitude', 'NS') 45 19 {('synthetic', 'Natural sound probe follo'): 6, ('naturalistic', 'Combinations of 6 natural'): 30, ('naturalistic', 'Combinations of 4 synthet'): 8, ('dmr', 'Combinations of 4 synthet'): 10}
('amplitude', 'dmr') 8 2 {('dmr', 'Combinations of 4 synthet'): 8}
('amplitude', 'torc') 42 9 {('torc', 'Combinations of 6 synthet'): 18, ('torc', 'Combinations of 4 synthet'): 24}
('frequency', 'NS') 46 20 {('synthetic', 'Natural sound probe follo'): 6, ('naturalistic', 'Combinations of 6 natural'): 30, ('naturalistic', 'Combinations of 4 synthet'): 10, ('dmr', 'Combinations of 4 synthet'): 10}
('frequency', 'dmr') 20 5 {('dmr', 'Combinations of 4 synthet'): 20}
('frequency', 'torc') 44 9 {('torc', 'Combinations of 6 synthet'): 24, ('torc', 'Combinations of 4 synthet'): 20}
('higher-order', 'NS') 61 26 {('pinknoise', 'Combinations of 6 sounds '): 122, ('pinknoise', 'Natural sound probe follo'): 18, ('pinknoise', 'Combinations of 4 sounds '): 24}
('higher-order', 'pinknoise') 76 26 {('pinknoise', 'Combinations of 6 sounds '): 154, ('pinknoise', 'Natural sound probe follo'): 12, ('pinknoise', 'Combinations of 4 sounds '): 24}
```

**Agent calls Bash**

```bash
cd  grep -n -i "harmonic\|SoundTrans\|naturalistic\|transform\|frequency-shift\|randomiz" paper/10.1152-jn.00577.2009.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 300,345p paper/10.1152-jn.00577.2009.txt; sed -n 385,420p paper/10.1152-jn.00577.2009.txt; sed -n 1590,1610p paper/10.1152-jn.00577.2009.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd  grep -n -i "Neural encoding models" -A 60 paper/10.1152-jn.00577.2009.txt | sed -n 1,10p; grep -n "wehr\|Wehr" paper/ac-1.data-description.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Neural encoding models\|Model performance\|Machens" paper/10.1152-jn.00577.2009.txt | head -20; ls executed/asari-2009/.venv/bin | grep -i jupyter | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Agent**

````json
{
 "description": "Build STRF claim notebook",
 "subagent_type": "general-purpose",
 "prompt": "You are helping revise a reproduction entry of Asari & Zador (2009, J Neurophysiol 102:2638) on the CRCNS ac-1 data set. Repository root:  Your job is ONE claim, `fig4-strf-performance-low`, built as a separate, self-contained notebook plus helper module in `entries/asari-2009/`. Do not edit any other file (not asari.py, not the main notebook, not attempts/, claims/, questions/).\n\nHARD DEADLINE: you must be finished and have sent your final report by 07:10 UTC (check `date -u` often). If the full analysis cannot be done by then, stop, leave the notebook in a state that runs, and report exactly how far you got. Run every command in the foreground and wait for it.\n\n## The claim (from claims/asari-2009.yaml; you may not change it)\nStatement: Linear STRF models of 20 A1 cells from Machens et al. (2004) predicted less than about 20% of the predictable response power, and extending the window from 180 ms to about 4 s did not improve them significantly, with or without a static nonlinearity; the LN model did only slightly better.\nExpected: STRF model performance at any window length, upper bound, 0.2, tolerance 0.02.\nCriterion: Per the Methods (Neural encoding models; Model performance), the 20 Wehr cells of Machens et al. (2004), spectrogram (Eq. 47) at 3 bins per octave from 0.40 to 22 kHz (17 bins), time bins of 2^k ms for k = 2 to 10 with 45 bins split as the Methods list, giving windows of 180, 324, 548, 884, 1364, 2004, 2772, 3540 and 4052 ms (765 parameters); ridge regression (Eq. 50) with 10-fold cross-validation choosing the ridge parameter on the validation fold; LN by robust lowess (5% span, 5 iterations) on the training set; performance by Eq. 53 on training (upper) and validation (lower) data, averaged over cells. Open, with readings run, the spectrogram window h(t) (readings 10-ms and 20-ms Hann), the response sampling (4-ms bins, the finest time bin, or the 10-kHz trace), the range of ridge values (a log grid wide enough that the best value is interior, a standard choice), and how folds are formed (contiguous blocks, or by stimulus). The paper does not say whether the 20% refers to the validation (lower) or the training (upper) estimate; both are readings. \"Did not improve significantly\" is a claim of absence and the paper names no test; the test fixed here, as an assumption the outcome rests on, is a paired Wilcoxon signed-rank test over the 20 cells of validation performance at 4052 ms against 180 ms, one-sided for an improvement, at 0.05, for STRF and for LN; a Friedman test over the nine windows is shown as a variant and does not decide. Reproduced when, under one reading, the mean performance is at most 0.22 at every window for STRF and LN, and the Wilcoxon test finds no improvement for either; the mean training performance and the LN gain are reported.\n\n## The paper\nFull text: paper/10.1152-jn.00577.2009.txt. Read the Methods \"Neural encoding models\" section (around lines 985-1100: Eqs. 46-53, spectrogram, time bins, ridge regression, static nonlinearity, model performance) and the Results around lines 1420-1450 (Model performance, Figure 4). Every method detail you use must come from the claim's criterion or the paper (cite the passage, e.g. \"Methods, Neural encoding models, Eq. 47\"), or from the authors' code in the data set (the description says the zip ships STRFanalysis.m and ridgesvd1.m with Wehr's data; read them and cite them where they settle a detail), or be stated as an assumption. The predictable response power (Eq. 53 denominator) needs repeated trials of the same stimulus; check how the paper estimates it (Sahani & Linden 2003 style signal power) and follow it.\nData description: paper/ac-1.data-description.txt.\n\n## The data\nCRCNS ac-1 is read in place from the public bucket: https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip (about 1 GB+; Wehr's recordings and stimuli are under `wehr/` inside it: `wehr/Results` with 26 cell folders, plus `wehr/Tools` and `wehr/Stimuli`). Do NOT download files to disk or read local copies: open the zip over HTTP range requests, as the existing helper does:\n```python\nimport fsspec, zipfile\nz = zipfile.ZipFile(fsspec.open(URL, block_size=2**22).open())\n```\nand read members into memory one at a time, reducing each to what is needed. Look at `entries/asari-2009/asari.py` (functions open_zip, load) for how Asari's .mat files are read with scipy.io.loadmat; Wehr's may be similar (Hiroki Asari standardized formats). The 20 cells of Machens et al. (2004): find how to identify them (file notes, a list in the Tools code, the description, which cells have natural-sound responses with repeats). If they cannot be identified exactly, say what you chose and why, and run on the cells that qualify.\n\nPython: use the entry's environment `executed/asari-2009/.venv/bin/python` (numpy, scipy, fsspec, matplotlib, ipykernel, jupyter nbconvert available there). Packages allowed are those in entries/asari-2009/requirements.in; if you truly need another, say so in the report instead of installing it.\n\n## Rules (docs/protocol.md, Author, \"Write the entry\")\n- Compute everything from the data; no embedded numbers taken from the paper except the expected values for comparison.\n- Random seeds: the seed of the claim's generator is `zlib.crc32(b\"asari-2009/fig4-strf-performance-low\")`; a second generator adds 1. If a result depends on random draws (e.g. random fold assignment), also run seeds +1000, +2000, +3000, +4000 and print the range. Never make an unseeded generator.\n- Develop on a subset (one or two cells), time it, measure peak memory (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, KB), and estimate the whole before running it all. The notebook must run in under 20 minutes and under 6 GB of memory (the machine has 4 CPUs and 16 GB shared with other work, and another long job will be running on it at the same time: use at most 2 processes). Limit BLAS threads to 1 or 2 (set OMP_NUM_THREADS / OPENBLAS_NUM_THREADS before importing numpy).\n- Helper module `entries/asari-2009/wehr.py`: loading and reusable measures, with a docstring saying where each parameter comes from (criterion, paper passage, authors' code, assumption, or a standard choice for a detail that cannot change a result).\n- Notebook `entries/asari-2009/strf_wehr.ipynb`, in this order: a header (paper, data set CRCNS ac-1 unversioned, doi 10.6080/K0KW5CXR, what this notebook tests); a data check cell tagged `sanity` (cell metadata tags: [\"sanity\"]) printing what was loaded: cells, stimuli, trials per stimulus, sampling rates, units and ranges; then the claim section: a markdown cell quoting the claim, code cells tagged `claim:fig4-strf-performance-low` that print every number the conclusion rests on (mean validation and training performance per window for STRF and LN under each reading run, per-cell values, ridge values chosen and whether any is at the grid edge, the Wilcoxon results, the Friedman variant, fits that failed or cells dropped), and a markdown cell tagged `conclusion` beginning \"**Result: ...**\" where every sentence is backed by a printed number. Finish with a code cell printing total time and peak memory. Commit the notebook WITHOUT outputs (clear outputs before you finish).\n- Test it by executing it into $TMPDIR, e.g. `cd entries/asari-2009 && executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000`, and read the outputs. Use $TMPDIR for any scratch files; never write elsewhere outside the entry directory.\n- Prose: plain, no em dashes, never the word \"rather\".\n\n## Your final report (your last message, which I will read)\nKeep it factual and short: which cells were used and how they were identified; every method choice with its source (passage or code) or marked as an assumption; the readings run; the key numbers (mean validation and training performance at each window for STRF and LN, Wilcoxon p-values, LN gain), the outcome they give under the criterion (reproduced / partially_reproduced / not_reproduced, or that it could not be finished and how far it got), the notebook's run time and peak memory, and anything about the data set that is wrong or undocumented (for findings)."
}
````

**Subagent prompt**

You are helping revise a reproduction entry of Asari & Zador (2009, J Neurophysiol 102:2638) on the CRCNS ac-1 data set. Repository root:  Your job is ONE claim, `fig4-strf-performance-low`, built as a separate, self-contained notebook plus helper module in `entries/asari-2009/`. Do not edit any other file (not asari.py, not the main notebook, not attempts/, claims/, questions/).

HARD DEADLINE: you must be finished and have sent your final report by 07:10 UTC (check `date -u` often). If the full analysis cannot be done by then, stop, leave the notebook in a state that runs, and report exactly how far you got. Run every command in the foreground and wait for it.

## The claim (from claims/asari-2009.yaml; you may not change it)
Statement: Linear STRF models of 20 A1 cells from Machens et al. (2004) predicted less than about 20% of the predictable response power, and extending the window from 180 ms to about 4 s did not improve them significantly, with or without a static nonlinearity; the LN model did only slightly better.
Expected: STRF model performance at any window length, upper bound, 0.2, tolerance 0.02.
Criterion: Per the Methods (Neural encoding models; Model performance), the 20 Wehr cells of Machens et al. (2004), spectrogram (Eq. 47) at 3 bins per octave from 0.40 to 22 kHz (17 bins), time bins of 2^k ms for k = 2 to 10 with 45 bins split as the Methods list, giving windows of 180, 324, 548, 884, 1364, 2004, 2772, 3540 and 4052 ms (765 parameters); ridge regression (Eq. 50) with 10-fold cross-validation choosing the ridge parameter on the validation fold; LN by robust lowess (5% span, 5 iterations) on the training set; performance by Eq. 53 on training (upper) and validation (lower) data, averaged over cells. Open, with readings run, the spectrogram window h(t) (readings 10-ms and 20-ms Hann), the response sampling (4-ms bins, the finest time bin, or the 10-kHz trace), the range of ridge values (a log grid wide enough that the best value is interior, a standard choice), and how folds are formed (contiguous blocks, or by stimulus). The paper does not say whether the 20% refers to the validation (lower) or the training (upper) estimate; both are readings. "Did not improve significantly" is a claim of absence and the paper names no test; the test fixed here, as an assumption the outcome rests on, is a paired Wilcoxon signed-rank test over the 20 cells of validation performance at 4052 ms against 180 ms, one-sided for an improvement, at 0.05, for STRF and for LN; a Friedman test over the nine windows is shown as a variant and does not decide. Reproduced when, under one reading, the mean performance is at most 0.22 at every window for STRF and LN, and the Wilcoxon test finds no improvement for either; the mean training performance and the LN gain are reported.

## The paper
Full text: paper/10.1152-jn.00577.2009.txt. Read the Methods "Neural encoding models" section (around lines 985-1100: Eqs. 46-53, spectrogram, time bins, ridge regression, static nonlinearity, model performance) and the Results around lines 1420-1450 (Model performance, Figure 4). Every method detail you use must come from the claim's criterion or the paper (cite the passage, e.g. "Methods, Neural encoding models, Eq. 47"), or from the authors' code in the data set (the description says the zip ships STRFanalysis.m and ridgesvd1.m with Wehr's data; read them and cite them where they settle a detail), or be stated as an assumption. The predictable response power (Eq. 53 denominator) needs repeated trials of the same stimulus; check how the paper estimates it (Sahani & Linden 2003 style signal power) and follow it.
Data description: paper/ac-1.data-description.txt.

## The data
CRCNS ac-1 is read in place from the public bucket: https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip (about 1 GB+; Wehr's recordings and stimuli are under `wehr/` inside it: `wehr/Results` with 26 cell folders, plus `wehr/Tools` and `wehr/Stimuli`). Do NOT download files to disk or read local copies: open the zip over HTTP range requests, as the existing helper does:
```python
import fsspec, zipfile
z = zipfile.ZipFile(fsspec.open(URL, block_size=2**22).open())
```
and read members into memory one at a time, reducing each to what is needed. Look at `entries/asari-2009/asari.py` (functions open_zip, load) for how Asari's .mat files are read with scipy.io.loadmat; Wehr's may be similar (Hiroki Asari standardized formats). The 20 cells of Machens et al. (2004): find how to identify them (file notes, a list in the Tools code, the description, which cells have natural-sound responses with repeats). If they cannot be identified exactly, say what you chose and why, and run on the cells that qualify.

Python: use the entry's environment `executed/asari-2009/.venv/bin/python` (numpy, scipy, fsspec, matplotlib, ipykernel, jupyter nbconvert available there). Packages allowed are those in entries/asari-2009/requirements.in; if you truly need another, say so in the report instead of installing it.

## Rules (docs/protocol.md, Author, "Write the entry")
- Compute everything from the data; no embedded numbers taken from the paper except the expected values for comparison.
- Random seeds: the seed of the claim's generator is `zlib.crc32(b"asari-2009/fig4-strf-performance-low")`; a second generator adds 1. If a result depends on random draws (e.g. random fold assignment), also run seeds +1000, +2000, +3000, +4000 and print the range. Never make an unseeded generator.
- Develop on a subset (one or two cells), time it, measure peak memory (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, KB), and estimate the whole before running it all. The notebook must run in under 20 minutes and under 6 GB of memory (the machine has 4 CPUs and 16 GB shared with other work, and another long job will be running on it at the same time: use at most 2 processes). Limit BLAS threads to 1 or 2 (set OMP_NUM_THREADS / OPENBLAS_NUM_THREADS before importing numpy).
- Helper module `entries/asari-2009/wehr.py`: loading and reusable measures, with a docstring saying where each parameter comes from (criterion, paper passage, authors' code, assumption, or a standard choice for a detail that cannot change a result).
- Notebook `entries/asari-2009/strf_wehr.ipynb`, in this order: a header (paper, data set CRCNS ac-1 unversioned, doi 10.6080/K0KW5CXR, what this notebook tests); a data check cell tagged `sanity` (cell metadata tags: ["sanity"]) printing what was loaded: cells, stimuli, trials per stimulus, sampling rates, units and ranges; then the claim section: a markdown cell quoting the claim, code cells tagged `claim:fig4-strf-performance-low` that print every number the conclusion rests on (mean validation and training performance per window for STRF and LN under each reading run, per-cell values, ridge values chosen and whether any is at the grid edge, the Wilcoxon results, the Friedman variant, fits that failed or cells dropped), and a markdown cell tagged `conclusion` beginning "**Result: ...**" where every sentence is backed by a printed number. Finish with a code cell printing total time and peak memory. Commit the notebook WITHOUT outputs (clear outputs before you finish).
- Test it by executing it into $TMPDIR, e.g. `cd entries/asari-2009 && executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000`, and read the outputs. Use $TMPDIR for any scratch files; never write elsewhere outside the entry directory.
- Prose: plain, no em dashes, never the word "rather".

## Your final report (your last message, which I will read)
Keep it factual and short: which cells were used and how they were identified; every method choice with its source (passage or code) or marked as an assumption; the readings run; the key numbers (mean validation and training performance at each window for STRF and LN, Wilcoxon p-values, LN gain), the outcome they give under the criterion (reproduced / partially_reproduced / not_reproduced, or that it could not be finished and how far it got), the notebook's run time and peak memory, and anything about the data set that is wrong or undocumented (for findings).

**Subagent calls Bash**

```bash
date -u; ls entries/asari-2009/; cat entries/asari-2009/requirements.in
```

```
Thu Nov 19 04:23:32 UTC 2026
README.md
__pycache__
asari.py
entry.yaml
reproduce_asari_2009.ipynb
requirements.in
requirements.lock.txt
aiohttp
fsspec
matplotlib
numpy
requests
scipy
```

**Subagent**

About 2h45m. Let me read the paper methods.

**Subagent calls Bash**

```bash
cd  sed -n 960,1110p paper/10.1152-jn.00577.2009.txt
```

Result: not kept, because it reads the paper's text.

**Subagent calls Bash**

```bash
cd  sed -n 1400,1460p paper/10.1152-jn.00577.2009.txt; grep -n -i "wehr\|machens" paper/10.1152-jn.00577.2009.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Subagent calls Bash**

```bash
cd  sed -n 1110,1125p paper/10.1152-jn.00577.2009.txt; echo ----; cat paper/ac-1.data-description.txt | head -200
```

Result: not kept, because it reads the paper's text.

**Subagent calls Bash**

```bash
cd  wc -l paper/ac-1.data-description.txt; grep -n -i "strf\|ridge\|wehr/" paper/ac-1.data-description.txt; sed -n 1,80p entries/asari-2009/asari.py
```

Result: not kept, because it reads the paper's text.

**Subagent calls Bash**

```bash
cd  sed -n 80,160p entries/asari-2009/asari.py; cd $TMPDIR; timeout 300 executed/asari-2009/.venv/bin/python -c "
import fsspec, zipfile
z = zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip', block_size=2**22).open())
for i in z.infolist():
    if i.filename.startswith('wehr') or 'wehr' in i.filename.lower(): print(i.filename, i.file_size)
" > wehr_list.txt; wc -l wehr_list.txt; head -100 wehr_list.txt
```

```
@functools.lru_cache(maxsize=None)
def member_index() -> dict:
    """Map 'Results/<cell>/<file>.mat' to (zip name, member name)."""
    out = {}
    for key in ("r1", "r2"):
        z = open_zip(ZIPS[key])
        for i in z.infolist():
            if i.filename.endswith(".mat"):
                rel = "Results/" + i.filename.split("/", 1)[1]
                out[rel] = (ZIPS[key], i.filename)
    return out


def read_text(member: str) -> str:
    return open_zip(ZIPS["main"]).read(member).decode("latin-1")


def _lst(x):
    return list(np.atleast_1d(x))

[... 163 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; executed/asari-2009/.venv/bin/python -c "
import fsspec, zipfile
z = zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip', block_size=2**22).open())
for n in ['wehr/Contents.m','wehr/Tools/STRFanalysis.m','wehr/Tools/ridgesvd1.m','wehr/Tools/logspectrogram.m','wehr/Tools/GetDataInfo.m','wehr/Tools/GetSpikes.m','wehr/Tools/GetEvoked.m','wehr/Tools/ViewResponse.m']:
    open(n.replace('/','_'),'wb').write(z.read(n))
"; ls; cat wehr_Contents.m wehr_Tools_STRFanalysis.m
```

```
-home-runner-work--temp
-home-runner-work-encore-encore
F.pkl
__pycache__
bash-edit-diff
survey.py
synmeta.pkl
tab.py
tools
wehr_Contents.m
wehr_Tools_GetDataInfo.m
wehr_Tools_GetEvoked.m
wehr_Tools_GetSpikes.m
wehr_Tools_STRFanalysis.m
wehr_Tools_ViewResponse.m
wehr_Tools_logspectrogram.m
wehr_Tools_ridgesvd1.m
wehr_list.txt
%==========================================================================
% DATA
[... 319 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; cat wehr_Tools_ridgesvd1.m wehr_Tools_logspectrogram.m
```

```
function [F,eff] = ridgesvd1(y,X,varargin)

% RIDGESVD1 returns linear filter by SVD-based ridge regression
%
%   [F,eff] = RIDGESVD1(y,X,k,eff);
%   returns the linear transfer function: F = inv(X'*X+k*I)*X'*y
%   for a linear model: y = X*F
%   where X is an n by p matrix, y is the n by 1 vector of observations,
%   and k is a power (ridge) constraint.
%   
%   The computation is based on SVD(X), where effective rank size EFF 
%   specifies the number of basis vectors to be considered.
%
%   If the singular value decomposition of X[n,p] is X = U*S*V',
%   where U and V are [n,p] and [p,p] orthogonal matrices, with the column
%   of U spanning the columns space of X, and the columns of V spanning the
%   row space.  S is a [p,p] diagonal matrix of the singular values 
%   {s1, s2, ..., sp}. 
%   Using the SVD, the pseudoinverse of X is
%       pinv(X) = inv(X'*X)*X' = inv(V*(S^2)*V')*(U*S*V')' = V*inv(S)*U',
[... 197 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; cat wehr_Tools_ViewResponse.m wehr_Tools_GetDataInfo.m; sed -n 1,200p wehr_Tools_GetEvoked.m
```

```
function p = ViewResponse(ID,PARAM)

% displays responses aligned with stimuli
%
% --- Input ---
%   ID - structure containing 
%       .date : experiment date (yyyymmdd)
%       .PenetNo : Penetration Number
%
%   param - structure containing various parameters
%       .smooth : window length of median filter smoothing (default: 10 msec)
%       .fig : vector of stimulus index to be shown
%       .homedir : home directory
%
% --- Output ---
%   p - structure containing 
%       .evoked : cell containing evoked-responses over trials
%       .spont  : cell containing spontaneous activity over trials
%       .stimulus : structure containing corresponding stimuli
%           .description : natural sound description
[... 385 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; grep -c "" wehr_list.txt; grep "Results/" wehr_list.txt | awk -F/ '{print $3}' | sort | uniq -c; executed/asari-2009/.venv/bin/python -c "
import fsspec, zipfile, io, scipy.io as sio, numpy as np
z = zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip', block_size=2**22).open())
m = sio.loadmat(io.BytesIO(z.read('wehr/Summary.mat')), squeeze_me=True, struct_as_record=False)
print(m.keys())
for e in np.atleast_1d(m['experiment']):
    print('EXP', e.description, e._fieldnames)
    for c in np.atleast_1d(e.cell):
        f=list(np.atleast_1d(c.file)); d=list(np.atleast_1d(c.description))
        print('  CELL', c._fieldnames, len(f), f[0])
        from collections import Counter
        print('    ', Counter([s.split(': Trial')[0] for s in d]))
"
```

```
1698
      1  0
    154 20020508-mw-003
    121 20020530-mw-001
     66 20020602-mw-001
    113 20020604-mw-001
     61 20020604-mw-002
    169 20020604-mw-003
     96 20020605-mw-002
     81 20020605-mw-003
     74 20020608-mw-001
    219 20020608-mw-002
     17 20030328-mw-001
     47 20030401-mw-001
     29 20030401-mw-003
     62 20030403-mw-001
     15 20030404-mw-001
     32 20030404-mw-002
     51 20030407-mw-001
     30 20030407-mw-002
[... 60 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; executed/asari-2009/.venv/bin/python -c "
import fsspec, zipfile, io, scipy.io as sio, numpy as np
z = zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip', block_size=2**22).open())
m = sio.loadmat(io.BytesIO(z.read('wehr/Summary.mat')), squeeze_me=True, struct_as_record=False)
for e in np.atleast_1d(m['experiment']):
    print('EXP', repr(e.description)); print('INFO', e.info); print('REF', e.reference)
b=z.read('wehr/Results/20020508-mw-003/20020508-mw-003-020.mat')
mm=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
print(mm.keys())
for k in mm:
  if k.startswith('_'): continue
  v=mm[k]; print(k, type(v), getattr(v,'_fieldnames',None))
p=mm['param']; 
for f in p._fieldnames: print(' param.',f, getattr(p,f) if f!='notes' else '')
print(mm['param'].notes)
t=mm['triggers']; print([ (f,getattr(t,f)) for f in t._fieldnames]); print(t.param._fieldnames, [getattr(t.param,f) for f in t.param._fieldnames])
r=mm['response']; print([(f, getattr(r,f) if f!='trace' else (r.trace.dtype, r.trace.shape)) for f in r._fieldnames])
"
```

```
EXP 'Repeated presentation of a fixed subset of sounds to auditory cortical cell.'
INFO Michael Wehr, Zador Lab, CSHL
REF C. K. Machens, M. S. Wehr, and A. M. Zador (2004) "Linearity of Cortical Receptive Fields Measured with Natural Sounds." J Neurosci, 24(5):1089-1100.
EXP 'Auditory cortical responses to as many natural sounds as possible.'
INFO Michael Wehr, Zador Lab, CSHL
REF C. K. Machens, M. S. Wehr, and A. M. Zador (2004) "Linearity of Cortical Receptive Fields Measured with Natural Sounds." J Neurosci, 24(5):1089-1100.
dict_keys(['__header__', '__version__', '__globals__', 'param', 'response', 'triggers'])
param <class 'scipy.io.matlab._mio5_params.mat_struct'> ['ID', 'animal', 'prep', 'recording', 'photo', 'reference', 'notes']
response <class 'scipy.io.matlab._mio5_params.mat_struct'> ['trace', 'datatype', 'scale', 'unit', 'sf']
triggers <class 'scipy.io.matlab._mio5_params.mat_struct'> ['file', 'type', 'time', 'param']
 param. ID <scipy.io.matlab._mio5_params.mat_struct object at 0x74c2e7034b50>
 param. animal <scipy.io.matlab._mio5_params.mat_struct object at 0x74c2e7034cd0>
 param. prep <scipy.io.matlab._mio5_params.mat_struct object at 0x74c2e7034d50>
 param. recording <scipy.io.matlab._mio5_params.mat_struct object at 0x74c2e7034dd0>
 param. photo <scipy.io.matlab._mio5_params.mat_struct object at 0x74c2e7034ed0>
 param. reference C. K. Machens, M. S. Wehr, and A. M. Zador (2004) "Linearity of Cortical Receptive Fields Measured with Natural Sounds." J Neurosci, 24(5):1089-1100.
 param. notes 
['Trial No.10                                                       '
 '                                                                  '
 'Natural Sound CDs (Cornell Laboratory of Ornithology, Ithaca, NY):'
[... 7 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; date -u; executed/asari-2009/.venv/bin/python -c "
import fsspec, zipfile, io, scipy.io as sio, numpy as np, time
z = zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip', block_size=2**22).open())
open('MakeRamp.m','wb').write(z.read('wehr/Tools/MakeRamp.m'))
for fn in ['wehr/Results/20030410-mw-001/20030410-mw-001-050.mat','wehr/Results/20030401-mw-001/20030401-mw-001-003.mat']:
  mm=sio.loadmat(io.BytesIO(z.read(fn)), squeeze_me=True, struct_as_record=False)
  t=np.atleast_1d(mm['triggers'])
  for tt in t: print(tt.file, tt.type, tt.time, [(f,getattr(tt.param,f)) for f in tt.param._fieldnames])
  r=mm['response']; print(r.sf, r.trace.shape, r.unit, mm['param'].notes)
t0=time.time(); b=z.read('wehr/Stimuli/fragments/3.mat'); print('dl',time.time()-t0, len(b))
s=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False); print(s.keys()); st=s['stimulus']; print(st._fieldnames, st.samples.dtype, st.samples.shape, [(f,getattr(st.param,f)) for f in st.param._fieldnames], np.abs(st.samples).max())
"; cat MakeRamp.m | grep -v "^%" | head -40
```

```
Thu Nov 19 04:25:27 UTC 2026
Traceback (most recent call last):
  File "<string>", line 8, in <module>
    for tt in t: print(tt.file, tt.type, tt.time, [(f,getattr(tt.param,f)) for f in tt.param._fieldnames])
                       ^^^^^^^
AttributeError: 'mat_struct' object has no attribute 'file'
function [X,param] = MakeRamp(X,param)



error(nargchk(1,2,nargin));
if isvector(X), X = X(:);end
if nargin<2, param = struct;end
if isstruct(param),  
    if isfield(param,'ramp') && ~isempty(param.ramp), 
        ramp = param.ramp(1);
    else
        return
    end
    
[... 26 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; grep -v "^%" MakeRamp.m | sed -n 40,60p; executed/asari-2009/.venv/bin/python -c "
import fsspec, zipfile, io, scipy.io as sio, numpy as np, time
z = zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip', block_size=2**22).open())
for fn in ['wehr/Results/20030410-mw-001/20030410-mw-001-050.mat','wehr/Results/20030401-mw-001/20030401-mw-001-003.mat']:
  mm=sio.loadmat(io.BytesIO(z.read(fn)), squeeze_me=True, struct_as_record=False)
  t=np.atleast_1d(mm['triggers'])
  for tt in t: print(tt._fieldnames, [getattr(tt,f) for f in tt._fieldnames if f!='param'], [(f,getattr(tt.param,f)) for f in tt.param._fieldnames])
  r=mm['response']; print(r.sf, r.trace.shape, r.unit, mm['param'].notes)
t0=time.time(); b=z.read('wehr/Stimuli/fragments/3.mat'); print('dl',time.time()-t0, len(b))
s=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False); print(s.keys()); st=s['stimulus']; print(st._fieldnames, st.samples.dtype, st.samples.shape, [(f,getattr(st.param,f)) for f in st.param._fieldnames], np.abs(st.samples).max())
"
```

```
w = window(handle,2*a);
X(1:a,:) = X(1:a,:).*repmat(w(1:a),1,size(X,2));
X(end-a+1:end,:) = X(end-a+1:end,:).*repmat(w(a+1:end),1,size(X,2));


if nargout>1,
    param.ramp = ramp;
    param.sf = sf;
    param.handle = handle;
    param.exp = m;
end
['type', 'time', 'param'] ['whitenoise', 126.49111999999998] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 252.98219999999998] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 379.47332] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 505.96439999999996] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 632.4556] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 758.9468] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 885.4376] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 1011.9287999999999] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
['type', 'time', 'param'] ['whitenoise', 1138.42] [('amplitude', 80), ('duration', 25), ('ramp', 5)]
[... 65 more lines not kept]
```

**Subagent calls Bash**

```bash
cd  sed -n 1,80p docs/protocol.md | head -5; grep -n "sanity\|claim:" entries/asari-2009/reproduce_asari_2009.ipynb | head -5; nproc; free -g; date -u
```

```
# Protocol for an attempt

Version: `pilot-16`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
152:     "sanity"
205:     "sanity"
244:     "claim:methods-recording-counts"
342:     "claim:a1-mgb-firing-rates"
420:     "claim:fig2-example-reliability"
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
Thu Nov 19 04:26:47 UTC 2026
```

**Subagent calls Write**

```json
{
 "file_path": "entries/asari-2009/wehr.py",
 "content": "\"\"\"Wehr's A1 recordings in CRCNS ac-1: loading and the STRF / LN encoding models\nof Asari & Zador (2009), Methods, \"Neural encoding models\" and \"Model\nperformance\" (Eqs. 46 to 53, Fig. 4).\n\nThe data are read in place from the public bucket: ``crcns-ac1.zip`` is opened\nover HTTP range requests (fsspec + zipfile) and each member is read into\nmemory, reduced, and dropped. Nothing is written to disk.\n\nWhere each parameter comes from\n-------------------------------\nPaper (Methods, Neural encoding models; Model performance) and the claim's\ncriterion:\n\n- spectrogram ``S(t, x) = 20 log10 |STFT|`` (Eq. 47); 3 bins per octave from\n  0.40 kHz (17 bins, so 765 = 45 x 17 parameters);\n- time bins of 2^k ms, k = 2..10, 45 bins in total, split as\n  [45,0,...], [9,36,0,...], ..., [9,8,...,1] from near to distant past, giving\n  windows of 180 ... 4052 ms (``BIN_SPLITS``);\n- ridge regression, Eq. 50, via the eigendecomposition of S'S (identical\n  to the SVD form of Eq. 50); 10-fold cross-validation; the ridge value chosen\n  by the best performance on the validation folds;\n- static nonlinearity by robust lowess with 5% span and five iterations, fitted\n  on the training set and applied to the validation set (Eq. 51);\n- performance by Eq. 53 with the predictable power of Eq. 52, on training\n  (upper) and validation (lower) data.\n\nAuthors' code shipped in the zip (``wehr/Tools``; not linked from the paper):\n\n- ``STRFanalysis.m``: per-trial responses are mean-subtracted for each\n  stimulus, the model is fitted to the trial-averaged response, the\n  spectrogram is mean-subtracted per frequency within each stimulus, the\n  stimuli are concatenated and cut into 10 contiguous folds of equal length,\n  one ridge value is chosen for all folds as the one with the best mean\n  validation performance of the linear model, the LN model uses that same\n  filter, and Eq. 53 is computed for each fold as\n  (mean P_total - mean P_error) / mean P_pred over the fold's time bins, with\n  P_pred(t) = (m rbar(t)^2 - P_total(t)) / (m - 1) (``LNperformance``);\n- ``ViewResponse.m`` / ``GetEvoked.m``: the trace is median-filtered with a\n  10-ms window (QX-314 blocks most spikes; the filter removes what is left),\n  the evoked response is the trigger's duration from the trigger time, natural\n  sounds are every stimulus other than \"tuning curve\", \"silence\" and\n  \"white noise\"; the stimulus gets a Hann ramp of ``param.ramp`` ms at both\n  ends (``MakeRamp.m``);\n- ``logspectrogram.m``: frequencies 400 * 2^(k/3) Hz, the DFT evaluated at\n  each centre frequency (no band integration).\n\nAssumptions (each also stated in the notebook):\n\n- cells: the paper's 20 cells cannot be identified from the files; we use every\n  Wehr cell with at least two trials of the same natural sound, since Eq. 52\n  needs m >= 2 (``select_cells``), and only those stimuli;\n- 17 frequencies 400 * 2^(k/3) Hz, k = 0..16 (0.40 to 16.1 kHz): the code's\n  rule with fmax = 22.1 kHz gives 18; the paper says 17 bins;\n- response sampled in 4-ms bins (the finest time bin; mean of 16 samples of the\n  4-kHz trace), the spectrogram computed every 4 ms with the window centred on\n  the bin, the coarser history bins the mean of the 4-ms frames they cover;\n- history before stimulus onset is set to the stimulus mean (zero after\n  centring), so every window is scored on the same time bins;\n- ridge grid: 33 values, lambda = 10^(-6 ... 2) times the mean eigenvalue of\n  the training S'S (a log grid wide enough that the choice is interior; edge\n  hits are printed);\n- lowess: local linear fit with tricube weights, one initial fit then five\n  robustness iterations with bisquare weights (6 x median |residual|), as in\n  Cleveland (1979); the fit is evaluated at 200 quantiles of the training\n  predictions and linearly interpolated (Cleveland's ``delta`` device, a\n  standard choice that cannot change a result), held constant outside the\n  training range;\n- per-cell performance is the mean over the 10 folds; the paper's numbers are\n  means over cells.\n\nNo result depends on random draws (folds are contiguous blocks, or stimuli\nassigned in order), so no generator is used.\n\"\"\"\nfrom __future__ import annotations\n\nimport functools\nimport io\nimport threading\nimport zipfile\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\nfrom scipy.ndimage import median_filter\n\nURL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip\"\nDT = 0.004                      # s, finest time bin (2^2 ms); response bin (assumption)\nFREQS = 400.0 * 2.0 ** (np.arange(17) / 3.0)   # Hz (logspectrogram.m rule, 17 bins)\nBIN_SIZES = 2 ** np.arange(2, 11)              # ms, k = 2..10\nBIN_SPLITS = [[45, 0, 0, 0, 0, 0, 0, 0, 0]] + [\n    list(range(9, 9 - i, -1)) + [45 - sum(range(9, 9 - i, -1))] + [0] * (8 - i)\n    for i in range(1, 9)]\nWINDOWS_MS = [int(np.dot(s, BIN_SIZES)) for s in BIN_SPLITS]\nMEDFILT_MS = 10                 # ViewResponse.m default ``smooth``\nNONNATURAL = (\"tuning curve\", \"silence\", \"white noise\")   # ViewResponse.m\nRIDGE_REL = 10.0 ** np.linspace(-6, 2, 33)\nLOWESS_SPAN, LOWESS_ITER, LOWESS_GRID = 0.05, 5, 200\n\n_local = threading.local()\n\n\ndef zf() -> zipfile.ZipFile:\n    \"\"\"One ZipFile per thread over HTTP range requests.\"\"\"\n    if not hasattr(_local, \"z\"):\n        _local.z = zipfile.ZipFile(fsspec.open(URL, block_size=2**22).open())\n    return _local.z\n\n\ndef _l(x):\n    return list(np.atleast_1d(x))\n\n\n@functools.lru_cache(maxsize=None)\ndef summary() -> list[dict]:\n    \"\"\"wehr/Summary.mat: one row per recording file.\"\"\"\n    m = sio.loadmat(io.BytesIO(zf().read(\"wehr/Summary.mat\")), squeeze_me=True,\n                    struct_as_record=False)\n    rows = []\n    for ei, e in enumerate(_l(m[\"experiment\"])):\n        for c in _l(e.cell):\n            for f, d in zip(_l(c.file), _l(c.description)):\n                f, d = str(f), str(d)\n                rows.append(dict(experiment=ei, exp_description=str(e.description),\n                                 reference=str(e.reference), cell=f.split(\"/\")[1],\n                                 file=f, stim=d.split(\": Trial\")[0].strip()))\n    return rows\n\n\ndef select_cells(min_trials: int = 2) -> dict:\n    \"\"\"Cells with >= ``min_trials`` trials of some natural sound.\n\n    Returns {cell: {stimulus description: [files]}} keeping only natural-sound\n    stimuli with at least ``min_trials`` trials (Eq. 52 needs m >= 2).\n    \"\"\"\n    out = {}\n    for r in summary():\n        if r[\"stim\"].lower() in NONNATURAL:\n            continue\n        out.setdefault(r[\"cell\"], {}).setdefault(r[\"stim\"], []).append(r[\"file\"])\n    sel = {}\n    for c, st in out.items():\n        keep = {s: f for s, f in st.items() if len(f) >= min_trials}\n        if keep:\n            sel[c] = keep\n    return sel\n\n\ndef read_trial(file: str) -> dict:\n    \"\"\"One recording file: the natural-sound trigger and the evoked trace.\n\n    The trace (int16 * scale, mV) is median filtered (10 ms, GetEvoked.m),\n    cut to the trigger's duration and averaged in 4-ms bins.\n    \"\"\"\n    b = zf().read(\"wehr/\" + file)\n    m = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)\n    del b\n    r = m[\"response\"]\n    sf = float(r.sf)\n    tr = [t for t in _l(m[\"triggers\"]) if \"file\" in t._fieldnames]\n    assert len(tr) == 1, file\n    t = tr[0]\n    x = r.trace.astype(np.float64) * float(r.scale)\n    raw_range = (float(x.min()), float(x.max()))\n    w = int(round(MEDFILT_MS / 1000 * sf))\n    x = median_filter(x - x.mean(), size=w, mode=\"constant\") + x.mean()\n    t0 = int(round(float(t.time) - 1))          # GetEvoked.m: samples, 1-based\n    dur = float(t.param.duration) / 1000        # s\n    nb = int(np.floor(dur / DT))\n    spb = int(round(DT * sf))\n    seg = x[t0:t0 + nb * spb]\n    nb = len(seg) // spb\n    resp = seg[:nb * spb].reshape(nb, spb).mean(1)\n    return dict(file=file, stimfile=str(t.file), ramp=float(t.param.ramp),\n                stim_sf=float(t.param.sf), duration=dur, sf=sf, unit=str(r.unit),\n                n_samples=len(r.trace), raw_range=raw_range, resp=resp)\n\n\ndef spectrogram(y: np.ndarray, sf: float, n_bins: int, win_ms: float) -> np.ndarray:\n    \"\"\"Eq. 47 at 17 frequencies (FREQS), one frame per 4-ms bin.\n\n    Hann window of ``win_ms`` (a reading), centred on each bin's centre, DFT\n    evaluated at each centre frequency (logspectrogram.m), 20 log10 |.| in dB,\n    then centred per frequency (STRFanalysis.m). Returns (n_bins, 17).\n    \"\"\"\n    L = int(round(win_ms / 1000 * sf))\n    n = np.arange(L)\n    h = np.hanning(L + 2)[1:-1]\n    ker = h[:, None] * np.exp(-2j * np.pi * FREQS[None, :] * n[:, None] / sf)\n    c = np.round((np.arange(n_bins) + 0.5) * DT * sf).astype(int) - L // 2\n    pad = np.concatenate([np.zeros(L), y, np.zeros(L + int(DT * sf) * 2)])\n    out = np.empty((n_bins, len(FREQS)))\n    for i0 in range(0, n_bins, 500):\n        idx = c[i0:i0 + 500, None] + L + n[None, :]\n        out[i0:i0 + 500] = np.abs(pad[idx] @ ker)\n    S = 20 * np.log10(out + np.finfo(float).eps)\n    return S - S.mean(0)\n\n\ndef read_stimulus(stimfile: str, ramp_ms: float, n_bins: int, wins_ms) -> dict:\n    \"\"\"Stimulus waveform with MakeRamp's Hann ramp; spectrograms for each window.\"\"\"\n    b = zf().read(\"wehr/Stimuli/\" + stimfile)\n    s = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)[\"stimulus\"]\n    del b\n    y = np.asarray(s.samples, dtype=np.float64).ravel()\n    sf = float(s.param.sf)\n    a = int(round(ramp_ms * sf / 1000))\n    if a >= 1:\n        w = np.hanning(2 * a + 2)[1:-1]\n        y[:a] *= w[:a]\n        y[-a:] *= w[a:]\n    out = dict(file=stimfile, sf=sf, n=len(y), dur=len(y) / sf, peak=float(np.abs(y).max()))\n    for wm in wins_ms:\n        out[wm] = spectrogram(y, sf, n_bins, wm)\n    return out\n\n\ndef load_cells(sel: dict, wins_ms=(10, 20), threads: int = 4) -> tuple[dict, dict]:\n    \"\"\"Read every selected trial and stimulus (I/O in threads, one process).\n\n    Returns (cells, stimuli). cells[c] = list of dict(stim, stimfile,\n    R=(m, n_bins) mean-subtracted 4-ms responses); stimuli[file] = spectrograms.\n    \"\"\"\n    files = [f for st in sel.values() for fl in st.values() for f in fl]\n    with ThreadPoolExecutor(threads) as ex:\n        trials = dict(zip(files, ex.map(read_trial, files)))\n    cells, need = {}, {}\n    for c, st in sel.items():\n        cells[c] = []\n        for name, fl in st.items():\n            tr = [trials[f] for f in fl]\n            sfiles = {t[\"stimfile\"] for t in tr}\n            assert len(sfiles) == 1, (c, name, sfiles)\n            nb = min(len(t[\"resp\"]) for t in tr)\n            R = np.array([t[\"resp\"][:nb] for t in tr])\n            R = R - R.mean(1, keepdims=True)          # STRFanalysis.m, per trial\n            sfile = tr[0][\"stimfile\"]\n            need[sfile] = max(need.get(sfile, 0), nb), tr[0][\"ramp\"]\n            cells[c].append(dict(stim=name, stimfile=sfile, R=R, sf=tr[0][\"sf\"],\n                                 unit=tr[0][\"unit\"], duration=tr[0][\"duration\"],\n                                 raw_range=(min(t[\"raw_range\"][0] for t in tr),\n                                            max(t[\"raw_range\"][1] for t in tr)),\n                                 n_samples=[t[\"n_samples\"] for t in tr]))\n    del trials\n\n    def _rs(item):\n        f, (nb, ramp) = item\n        return f, read_stimulus(f, ramp, nb, wins_ms)\n    with ThreadPoolExecutor(min(threads, 2)) as ex:\n        stimuli = dict(ex.map(_rs, need.items()))\n    return cells, stimuli\n\n\n# --------------------------------------------------------------------------\n# design matrix and models\n# --------------------------------------------------------------------------\ndef _edges(split):\n    \"\"\"Lag edges (in 4-ms frames) of the 45 history bins, near to far.\"\"\"\n    e = [0]\n    for k, nk in zip(BIN_SIZES, split):\n        for _ in range(nk):\n            e.append(e[-1] + k // 4)\n    return np.array(e)\n\n\ndef design(Sc: np.ndarray, split, rows: np.ndarray) -> np.ndarray:\n    \"\"\"Rows of the stimulus matrix (Eq. 48) for time bins ``rows``.\n\n    Sc: cumulative sum of the zero-padded spectrogram (pad P frames of zeros\n    before onset). Bin b covers lags [e_b, e_{b+1}) frames before and\n    including the current frame; its value is the mean spectrogram there.\n    \"\"\"\n    e = _edges(split)\n    P = Sc.shape[0] - 1 - 0  # Sc has a leading zero row\n    out = np.empty((len(rows), 45, Sc.shape[1]))\n    for b in range(45):\n        hi = rows + 1 - e[b]          # exclusive end index in padded frames (+1 for cumsum)\n        lo = rows + 1 - e[b + 1]\n        out[:, b] = (Sc[hi] - Sc[lo]) / (e[b + 1] - e[b])\n    return out.reshape(len(rows), -1)\n\n\nPAD = 1013  # frames of 4 ms in the longest window (4052 ms)\n\n\ndef prepare(cell: list, stimuli: dict, win_ms: float):\n    \"\"\"Concatenate a cell's stimuli: cumsum spectrograms, rbar, P_pred, stim id.\"\"\"\n    Scs, rbar, ppred, sid, rows = [], [], [], [], []\n    off = 0\n    for i, s in enumerate(cell):\n        R = s[\"R\"]\n        m, nb = R.shape\n        S = stimuli[s[\"stimfile\"]][win_ms][:nb]\n        Sp = np.vstack([np.zeros((PAD, S.shape[1])), S])\n        Sc = np.vstack([np.zeros((1, S.shape[1])), np.cumsum(Sp, 0)])\n        Scs.append(Sc)\n        rb = R.mean(0)\n        pt = (R ** 2).mean(0)\n        rbar.append(rb)\n        ppred.append((m * rb ** 2 - pt) / (m - 1))   # Eq. 52 / LNperformance\n        sid.append(np.full(nb, i))\n        rows.append(np.arange(nb) + PAD + off)\n        off += Sc.shape[0]\n    Sc = np.vstack(Scs)\n    return Sc, np.concatenate(rbar), np.concatenate(ppred), np.concatenate(sid), np.concatenate(rows)\n\n\ndef folds_contiguous(n: int, k: int = 10) -> np.ndarray:\n    \"\"\"STRFanalysis.m: k blocks of round(n/k) bins, the last takes the rest.\"\"\"\n    f = np.empty(n, int)\n    sz = int(round(n / k))\n    for i in range(k):\n        f[i * sz:(i + 1) * sz if i < k - 1 else n] = i\n    return f\n\n\ndef folds_by_stimulus(sid: np.ndarray, k: int = 10) -> np.ndarray:\n    \"\"\"Stimulus i goes to fold i mod k (fewer folds if fewer stimuli).\"\"\"\n    return sid % min(k, sid.max() + 1)\n\n\ndef perf(rbar, rhat, ppred):\n    \"\"\"Eq. 53 over a set of bins: (P_total - P_error) / P_pred, means over bins.\n\n    P_total - P_error = <2 r_j rhat - rhat^2>_j = 2 rbar rhat - rhat^2.\n    \"\"\"\n    return np.sum(2 * rbar * rhat - rhat ** 2, 0) / np.sum(ppred)\n\n\ndef lowess_fit(x, y, span=LOWESS_SPAN, iters=LOWESS_ITER, ngrid=LOWESS_GRID):\n    \"\"\"Robust lowess (Cleveland 1979) of y on x; returns (grid, fitted values).\"\"\"\n    o = np.argsort(x)\n    xs, ys = x[o], y[o]\n    n = len(xs)\n    k = max(int(np.ceil(span * n)), 3)\n    g = np.unique(np.quantile(xs, np.linspace(0, 1, ngrid)))\n    pos = np.searchsorted(xs, g)\n    # nearest-k window [l, l+k) for each grid point\n    L = np.empty(len(g), int)\n    for i, (gi, p) in enumerate(zip(g, pos)):\n        lo = np.arange(max(0, p - k), min(p, n - k) + 1)\n        cost = np.maximum(gi - xs[lo], xs[lo + k - 1] - gi)\n        L[i] = lo[np.argmin(cost)]\n    idx = L[:, None] + np.arange(k)[None, :]\n    X = xs[idx]\n    Y = ys[idx]\n    d = np.abs(X - g[:, None])\n    dmax = d.max(1, keepdims=True)\n    dmax[dmax == 0] = 1\n    wt = (1 - np.clip(d / dmax, 0, 1) ** 3) ** 3\n    rob = np.ones(n)\n    for it in range(iters + 1):\n        w = wt * rob[idx]\n        sw = w.sum(1)\n        mx = (w * X).sum(1) / sw\n        my = (w * Y).sum(1) / sw\n        vx = (w * (X - mx[:, None]) ** 2).sum(1)\n        cxy = (w * (X - mx[:, None]) * (Y - my[:, None])).sum(1)\n        beta = np.where(vx > 1e-12 * np.maximum(1, mx ** 2), cxy / np.where(vx > 0, vx, 1), 0)\n        fit = my + beta * (g - mx)\n        if it == iters:\n            break\n        res = ys - np.interp(xs, g, fit)\n        s = np.median(np.abs(res))\n        if s == 0:\n            break\n        u = res / (6 * s)\n        rob = np.where(np.abs(u) < 1, (1 - u ** 2) ** 2, 0)\n    return g, fit\n\n\ndef fit_cell(Sc, rbar, ppred, rows, fold, split, ridge_rel=RIDGE_REL, chunk=20000):\n    \"\"\"10-fold ridge STRF (Eq. 50) and LN (Eq. 51) for one window.\n\n    Returns dict with per-fold performance (train, valid) for STRF and LN at\n    the chosen ridge value, the chosen value and its grid index.\n    \"\"\"\n    K = fold.max() + 1\n    p = 45 * Sc.shape[1]\n    G = np.zeros((K, p, p))\n    B = np.zeros((K, p))\n    for f in range(K):\n        ii = np.flatnonzero(fold == f)\n        for c0 in range(0, len(ii), chunk):\n            jj = ii[c0:c0 + chunk]\n            X = design(Sc, split, rows[jj])\n            G[f] += X.T @ X\n            B[f] += X.T @ rbar[jj]\n    Gt, Bt = G.sum(0), B.sum(0)\n    W = np.empty((K, p, len(ridge_rel)))\n    lam = np.empty((K, len(ridge_rel)))\n    for f in range(K):\n        ev, V = np.linalg.eigh(Gt - G[f])\n        ev = np.clip(ev, 0, None)\n        lam[f] = ridge_rel * ev.mean()\n        z = V.T @ (Bt - B[f])\n        W[f] = V @ (z[:, None] / (ev[:, None] + lam[f][None, :]))\n    del G\n    # predictions of every fold's filter on all bins (chunked)\n    n = len(rows)\n    pred = np.empty((K, n, len(ridge_rel)), dtype=np.float32) if n * K * len(ridge_rel) < 3e8 else None\n    vperf = np.empty((K, len(ridge_rel)))\n    if pred is not None:\n        for c0 in range(0, n, chunk):\n            X = design(Sc, split, rows[c0:c0 + chunk])\n            for f in range(K):\n                pred[f, c0:c0 + chunk] = X @ W[f]\n        for f in range(K):\n            v = fold == f\n            vperf[f] = perf(rbar[v, None], pred[f][v].astype(float), ppred[v])\n    best = int(np.argmax(vperf.mean(0)))     # STRFanalysis.m: one value for all folds\n    out = dict(best=best, ridge_rel=float(ridge_rel[best]),\n               lam=lam[:, best], vcurve=vperf.mean(0))\n    lin = np.empty((K, 2))\n    ln = np.empty((K, 2))\n    for f in range(K):\n        rh = pred[f][:, best].astype(float)\n        v = fold == f\n        t = ~v\n        lin[f] = perf(rbar[t], rh[t], ppred[t]), perf(rbar[v], rh[v], ppred[v])\n        g, fit = lowess_fit(rh[t], rbar[t])\n        rs = np.interp(rh, g, fit)\n        ln[f] = perf(rbar[t], rs[t], ppred[t]), perf(rbar[v], rs[v], ppred[v])\n    out[\"strf\"] = lin      # columns: train (upper), valid (lower)\n    out[\"ln\"] = ln\n    return out\n"
}
```

```
File created successfully at: entries/asari-2009/wehr.py (file state is current in your context — no need to Read it back)
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
s=s.replace("""    P = Sc.shape[0] - 1 - 0  # Sc has a leading zero row
""","")
s=s.replace("""    pred = np.empty((K, n, len(ridge_rel)), dtype=np.float32) if n * K * len(ridge_rel) < 3e8 else None
    vperf = np.empty((K, len(ridge_rel)))
    if pred is not None:
        for c0 in range(0, n, chunk):
            X = design(Sc, split, rows[c0:c0 + chunk])
            for f in range(K):
                pred[f, c0:c0 + chunk] = X @ W[f]
        for f in range(K):
            v = fold == f
            vperf[f] = perf(rbar[v, None], pred[f][v].astype(float), ppred[v])
""","""    pred = np.empty((K, n, len(ridge_rel)), dtype=np.float32)
    vperf = np.empty((K, len(ridge_rel)))
    for c0 in range(0, n, chunk):
        X = design(Sc, split, rows[c0:c0 + chunk])
        for f in range(K):
            pred[f, c0:c0 + chunk] = X @ W[f]
    for f in range(K):
        v = fold == f
        vperf[f] = perf(rbar[v, None], pred[f][v].astype(float), ppred[v])
""")
open('wehr.py','w').write(s)
EOF
cat > $TMPDIR/t1.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="2"; os.environ["OPENBLAS_NUM_THREADS"]="2"
import sys, time, resource
sys.path.insert(0, "entries/asari-2009")
import numpy as np, wehr
t0=time.time()
sel=wehr.select_cells()
print(len(sel)); 
for c,st in sel.items(): print(c, len(st), [len(f) for f in st.values()])
print(wehr.WINDOWS_MS, wehr.BIN_SPLITS)
c='20020604-mw-003'
cells, stim = wehr.load_cells({c: sel[c]}, wins_ms=(10,))
print('load', time.time()-t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
for s in cells[c]: print(s['stim'], s['stimfile'], s['R'].shape, s['duration'], s['raw_range'])
Sc, rbar, ppred, sid, rows = wehr.prepare(cells[c], stim, 10)
print(len(rows), ppred.mean(), (rbar**2).mean())
fold=wehr.folds_contiguous(len(rows))
for w in [0,8]:
    t1=time.time()
    o=wehr.fit_cell(Sc, rbar, ppred, rows, fold, wehr.BIN_SPLITS[w])
    print(wehr.WINDOWS_MS[w], 'best', o['best'], 'strf', o['strf'].mean(0), 'ln', o['ln'].mean(0), time.time()-t1)
    print(np.round(o['vcurve'],3))
print('mem', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, 'GB', time.time()-t0)
EOF
date -u; executed/asari-2009/.venv/bin/python $TMPDIR/t1.py
```

```
Thu Nov 19 04:28:10 UTC 2026
16
20020508-mw-003 11 [20, 10, 10, 10, 10, 10, 10, 10, 10, 11, 10]
20020530-mw-001 7 [10, 10, 12, 10, 10, 11, 14]
20020602-mw-001 5 [10, 10, 10, 10, 10]
20020604-mw-001 9 [6, 9, 12, 10, 10, 10, 10, 10, 19]
20020604-mw-002 3 [20, 20, 9]
20020604-mw-003 8 [20, 20, 20, 20, 20, 20, 20, 15]
20020605-mw-002 5 [10, 10, 10, 20, 20]
20020605-mw-003 3 [20, 20, 20]
20020608-mw-001 6 [10, 10, 10, 10, 10, 10]
20020608-mw-002 10 [20, 20, 20, 20, 20, 20, 20, 20, 25, 20]
20030401-mw-001 18 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
20030403-mw-001 18 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
20030404-mw-002 11 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
20030407-mw-001 18 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
20030407-mw-002 7 [2, 2, 2, 2, 2, 2, 2]
20030410-mw-001 30 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
[180, 324, 548, 884, 1364, 2004, 2772, 3540, 4052] [[45, 0, 0, 0, 0, 0, 0, 0, 0], [9, 36, 0, 0, 0, 0, 0, 0, 0], [9, 8, 28, 0, 0, 0, 0, 0, 0], [9, 8, 7, 21, 0, 0, 0, 0, 0], [9, 8, 7, 6, 15, 0, 0, 0, 0], [9, 8, 7, 6, 5, 10, 0, 0, 0], [9, 8, 7, 6, 5, 4, 6, 0, 0], [9, 8, 7, 6, 5, 4, 3, 3, 0], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
load 8.285930395126343 0.27672
[... 19 more lines not kept]
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; grep -n "pred = np.empty" -A 25 wehr.py | head -40
```

```
400:    pred = np.empty((K, n, len(ridge_rel)), dtype=np.float32)
401-    vperf = np.empty((K, len(ridge_rel)))
402-    for c0 in range(0, n, chunk):
403-        X = design(Sc, split, rows[c0:c0 + chunk])
404-        for f in range(K):
405-            pred[f, c0:c0 + chunk] = X @ W[f]
406-    for f in range(K):
407-        v = fold == f
408-        vperf[f] = perf(rbar[v, None], pred[f][v].astype(float), ppred[v])
409-    best = int(np.argmax(vperf.mean(0)))     # STRFanalysis.m: one value for all folds
410-    out = dict(best=best, ridge_rel=float(ridge_rel[best]),
411-               lam=lam[:, best], vcurve=vperf.mean(0))
412-    lin = np.empty((K, 2))
413-    ln = np.empty((K, 2))
414-    for f in range(K):
415-        rh = pred[f][:, best].astype(float)
416-        v = fold == f
417-        t = ~v
418-        lin[f] = perf(rbar[t], rh[t], ppred[t]), perf(rbar[v], rh[v], ppred[v])
419-        g, fit = lowess_fit(rh[t], rbar[t])
[... 5 more lines not kept]
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; wc -l wehr.py; ls -la; grep -n "^def \|^PAD\|^[A-Z_]* = " wehr.py
```

```
424 wehr.py
total 292
drwxr-xr-x   4 runner runner   4096 Nov 19 04:27 .
drwxr-xr-x 326 runner runner  12288 Nov 19 04:11 ..
drwxr-xr-x   3 runner runner   4096 Nov 19 04:18 .claude
-rw-r--r--   1 runner runner   2808 Nov 19 04:11 README.md
drwxr-xr-x   2 runner runner   4096 Nov 19 04:28 __pycache__
-rw-r--r--   1 runner runner  43385 Nov 19 04:11 asari.py
-rw-r--r--   1 runner runner   1035 Nov 19 04:11 entry.yaml
-rw-r--r--   1 runner runner  66648 Nov 19 04:11 reproduce_asari_2009.ipynb
-rw-r--r--   1 runner runner     47 Nov 19 04:11 requirements.in
-rw-r--r--   1 runner runner 124999 Nov 19 04:11 requirements.lock.txt
-rw-r--r--   1 runner runner  17861 Nov 19 04:28 wehr.py
87:URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip"
88:DT = 0.004                      # s, finest time bin (2^2 ms); response bin (assumption)
89:FREQS = 400.0 * 2.0 ** (np.arange(17) / 3.0)   # Hz (logspectrogram.m rule, 17 bins)
90:BIN_SIZES = 2 ** np.arange(2, 11)              # ms, k = 2..10
91:BIN_SPLITS = [[45, 0, 0, 0, 0, 0, 0, 0, 0]] + [
94:WINDOWS_MS = [int(np.dot(s, BIN_SIZES)) for s in BIN_SPLITS]
95:MEDFILT_MS = 10                 # ViewResponse.m default ``smooth``
[... 19 more lines not kept]
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
old=s[s.index("    pred = np.empty((K, n, len(ridge_rel)), dtype=np.float32)"):s.index("    lin = np.empty((K, 2))")]
new='''    # validation predictions for every ridge value, then all bins at the chosen one
    vperf = np.empty((K, len(ridge_rel)))
    for f in range(K):
        v = np.flatnonzero(fold == f)
        X = design(Sc, split, rows[v])
        vperf[f] = perf(rbar[v, None], X @ W[f], ppred[v])
    best = int(np.argmax(vperf.mean(0)))     # STRFanalysis.m: one value for all folds
    out = dict(best=best, ridge_rel=float(ridge_rel[best]),
               lam=lam[:, best], vcurve=vperf.mean(0))
    Wb = W[:, :, best].T                      # (p, K)
    pred = np.empty((K, n))
    for c0 in range(0, n, chunk):
        X = design(Sc, split, rows[c0:c0 + chunk])
        pred[:, c0:c0 + chunk] = (X @ Wb).T
    del X
'''
s=s.replace(old,new).replace("        rh = pred[f][:, best].astype(float)\n","        rh = pred[f]\n")
open('wehr.py','w').write(s)
EOF
sed -i "s/c='20020604-mw-003'/c=sys.argv[1]/; s/for w in \[0,8\]/for w in range(9)/" $TMPDIR/t1.py
date -u; executed/asari-2009/.venv/bin/python $TMPDIR/t1.py 20030410-mw-001 2>&1 | tail -25
```

```
Thu Nov 19 04:28:44 UTC 2026
884 best 24 strf [0.21217816 0.16469113] ln [0.20018237 0.13456317] 5.208621263504028
[0.118 0.118 0.118 0.118 0.118 0.118 0.118 0.118 0.118 0.118 0.118 0.119
 0.119 0.12  0.121 0.123 0.126 0.13  0.135 0.141 0.148 0.154 0.16  0.164
 0.165 0.161 0.154 0.143 0.132 0.12  0.109 0.097 0.083]
1364 best 24 strf [0.21962278 0.17199143] ln [0.20568671 0.14446358] 5.201407432556152
[0.111 0.111 0.111 0.111 0.111 0.111 0.111 0.111 0.111 0.111 0.112 0.112
 0.113 0.115 0.117 0.121 0.125 0.131 0.138 0.145 0.153 0.16  0.166 0.171
 0.172 0.169 0.161 0.15  0.138 0.127 0.115 0.099 0.081]
2004 best 24 strf [0.22748341 0.17982809] ln [0.2110756  0.15309374] 5.1952455043792725
[0.101 0.101 0.101 0.101 0.102 0.102 0.102 0.102 0.102 0.102 0.103 0.104
 0.105 0.108 0.112 0.117 0.123 0.131 0.14  0.149 0.158 0.166 0.173 0.178
 0.18  0.177 0.169 0.157 0.145 0.133 0.12  0.104 0.084]
2772 best 24 strf [0.2286829  0.17806297] ln [0.21226868 0.15257932] 5.223349094390869
[0.093 0.093 0.093 0.093 0.094 0.094 0.094 0.094 0.094 0.095 0.095 0.097
 0.099 0.102 0.106 0.112 0.119 0.128 0.137 0.146 0.155 0.164 0.171 0.176
 0.178 0.175 0.167 0.156 0.143 0.132 0.119 0.103 0.083]
3540 best 24 strf [0.23008783 0.17475518] ln [0.21341401 0.15205954] 5.211991548538208
[0.085 0.085 0.085 0.085 0.085 0.085 0.085 0.085 0.086 0.086 0.087 0.089
 0.091 0.095 0.1   0.106 0.114 0.123 0.132 0.142 0.151 0.16  0.168 0.173
[... 6 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; executed/asari-2009/.venv/bin/python -c "
import sys; sys.path.insert(0,'entries/asari-2009')
import numpy as np, wehr
r=np.random.default_rng(0)
x=r.normal(size=20000); y=np.maximum(x,0)**2+r.normal(size=20000)*0.5
g,f=wehr.lowess_fit(x,y)
print(np.abs(f-np.maximum(g,0)**2)[5:-5].max(), np.abs(f-np.maximum(g,0)**2).max())
"
```

```
0.05318874777948889 1.7498692799728275
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
s=s.replace("""    ln = np.empty((K, 2))
""","""    ln = np.empty((K, 2))
    ln0 = np.empty((K, 2))
""")
s=s.replace("""        ln[f] = perf(rbar[t], rs[t], ppred[t]), perf(rbar[v], rs[v], ppred[v])
""","""        ln[f] = perf(rbar[t], rs[t], ppred[t]), perf(rbar[v], rs[v], ppred[v])
        g, fit = lowess_fit(rh[t], rbar[t], iters=0)   # diagnostic: no robustness steps
        rs = np.interp(rh, g, fit)
        ln0[f] = perf(rbar[t], rs[t], ppred[t]), perf(rbar[v], rs[v], ppred[v])
""")
s=s.replace("""    out["ln"] = ln
""","""    out["ln"] = ln
    out["ln_nonrobust"] = ln0
""")
s=s.replace("""- per-cell performance is the mean over the 10 folds;""","""- a diagnostic only (not a reading): the same lowess without the robustness
  iterations, to show how much the robust weights cost in Eq. 53;
- per-cell performance is the mean over the 10 folds;""")
open('wehr.py','w').write(s)
EOF
grep -n "ln0\|nonrobust" wehr.py
```

```
419:    ln0 = np.empty((K, 2))
430:        ln0[f] = perf(rbar[t], rs[t], ppred[t]), perf(rbar[v], rs[v], ppred[v])
433:    out["ln_nonrobust"] = ln0
```

**Subagent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('entries/asari-2009/reproduce_asari_2009.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:600]); print('=====')
"
```

```
markdown {} # Reproducing Asari & Zador (2009) on CRCNS ac-1

Paper: H. Asari and A. M. Zador (2009), "Long-Lasting Context Dependence Constrains Neural
Encoding Models in Rodent Auditory Cortex", J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.
The claims file (`claims/asari-2009.yaml`) was written from the version of record (a text
extraction of the publisher's PDF); the online supplement was not read.

Dataset: CRCNS ac-1 (doi:10.6080/K0KW5CXR), read in place from the public S3 bucket
`crcnsarchive` (`ac-1/crcns-ac1.zip`, `crcns-ac1-asari-results-1.zip`,
`crcns-ac1-asari-results-2.zip`). CRCNS 
=====
code {} import os, time, zlib, collections, resource
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
import asari as A

[... 42 more lines not kept]
```

**Subagent**

Now write the notebook generator.

**Subagent calls Write**

```json
{
 "file_path": "entries/asari-2009/.claude_tmp_make_nb.py",
 "content": "placeholder\n"
}
```

```
File created successfully at: entries/asari-2009/.claude_tmp_make_nb.py (file state is current in your context — no need to Read it back)
```

**Subagent calls Bash**

```bash
rm entries/asari-2009/.claude_tmp_make_nb.py; echo $TMPDIR
```

```
/tmp/claude-1001
```

**Subagent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\n\nCL = \"claim:fig4-strf-performance-low\"\n\nmd(\"\"\"\n# Asari & Zador (2009), Fig. 4: STRF and LN model performance on Wehr's A1 cells\n\nPaper: H. Asari and A. M. Zador (2009), \"Long-Lasting Context Dependence Constrains Neural\nEncoding Models in Rodent Auditory Cortex\", J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.\n\nData set: CRCNS ac-1 (unversioned; doi:10.6080/K0KW5CXR), Wehr's recordings (`wehr/` in\n`crcns-ac1.zip`), read in place from the public S3 bucket `crcnsarchive` over HTTP range\nrequests; nothing is downloaded to disk.\n\nThis notebook tests one claim, `fig4-strf-performance-low`: linear STRF models (and LN models with\na static nonlinearity) of A1 cells from Machens et al. (2004) predict less than about 20% of the\npredictable response power at every window length from 180 ms to about 4 s, and extending the window\ndoes not improve them significantly. Methods follow the paper (Methods, \"Neural encoding models\",\nEqs. 46 to 51; \"Model performance\", Eqs. 52 and 53), the claim's criterion, and the authors' own code\nshipped in the zip (`wehr/Tools/STRFanalysis.m`, `ridgesvd1.m`, `logspectrogram.m`,\n`ViewResponse.m`, `GetEvoked.m`, `MakeRamp.m`). Where each parameter comes from is listed in the\ndocstring of `wehr.py`; the assumptions are repeated below.\n\"\"\")\n\ncode(\"\"\"\nimport os, time, zlib, resource\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"2\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"2\")\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport wehr as W\n\nT0 = time.time()\nCLAIM = \"asari-2009/fig4-strf-performance-low\"\nSEED = zlib.crc32(CLAIM.encode())   # defined by the protocol; no result here uses random draws\nprint(\"seed\", SEED, \"(unused: folds are contiguous blocks or stimuli in order)\")\nnp.set_printoptions(precision=3, suppress=True, linewidth=140)\n\"\"\")\n\nmd(\"\"\"\n## Data\n\n`wehr/Summary.mat` lists two experiments, both citing Machens et al. (2004): ten cells (2002) with a\nfixed subset of natural sounds repeated 5 to 25 times, and sixteen cells (2003) with many natural\nsound streams presented once or twice. The paper's 20 cells are not marked in the files. Eq. 52\nneeds at least two trials of a stimulus, so we keep every cell with at least two trials of some\nnatural sound, and only those stimuli (an assumption). Each recording file is one trial; the trace\nis median filtered (10 ms, `ViewResponse.m`/`GetEvoked.m`), cut to the stimulus duration, averaged\nin 4-ms bins and mean-subtracted per trial (`STRFanalysis.m`). Spectrograms of every stimulus are\ncomputed with both window readings (10-ms and 20-ms Hann).\n\"\"\")\n\ncode(\"\"\"\nt = time.time()\nrows = W.summary()\nallcells = sorted({r[\"cell\"] for r in rows})\nSEL = W.select_cells(min_trials=2)\nprint(\"Summary.mat: experiments\", sorted({(r[\"experiment\"], r[\"exp_description\"]) for r in rows}))\nprint(\"references:\", sorted({r[\"reference\"] for r in rows}))\nprint(\"cells in Summary.mat:\", len(allcells), \"| cells with >= 2 trials of a natural sound:\", len(SEL))\nprint(\"excluded (every natural sound presented once):\",\n      [c for c in allcells if c not in SEL])\nCELLS, STIM = W.load_cells(SEL, wins_ms=(10, 20), threads=4)\nprint(f\"loaded in {time.time() - t:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nprint()\nprint(f\"{'cell':16s} {'stim':>4s} {'trials per stimulus':40s} {'bins':>7s} {'sf':>6s} unit  raw range (mV)   stim dur (s)\")\nfor c, st in CELLS.items():\n    tr = [s[\"R\"].shape[0] for s in st]\n    nb = sum(s[\"R\"].shape[1] for s in st)\n    lo = min(s[\"raw_range\"][0] for s in st); hi = max(s[\"raw_range\"][1] for s in st)\n    durs = sorted({round(s[\"duration\"], 2) for s in st})\n    print(f\"{c:16s} {len(st):4d} {str(tr):40.40s} {nb:7d} {st[0]['sf']:6.0f} {st[0]['unit']:4s} \"\n          f\"[{lo:6.1f}, {hi:5.1f}]  {durs}\")\nprint()\nprint(\"stimuli:\", len(STIM))\nfor f, s in sorted(STIM.items()):\n    print(f\"  {f:22s} sf {s['sf']:.0f} Hz, {s['dur']:.2f} s, peak |x| {s['peak']:.2f}, \"\n          f\"spectrogram (10 ms) {s[10].shape}, dB range after centring \"\n          f\"[{s[10].min():.0f}, {s[10].max():.0f}]\")\nprint(\"frequencies (Hz):\", np.round(W.FREQS).astype(int))\nprint(\"windows (ms):\", W.WINDOWS_MS)\nprint(\"bin splits:\", W.BIN_SPLITS)\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\n## Claim `fig4-strf-performance-low`\n\n> Linear STRF models of 20 A1 cells from Machens et al. (2004) predicted less than about 20% of the\n> predictable response power, and extending the window from 180 ms to about 4 s did not improve them\n> significantly, with or without a static nonlinearity; the LN model did only slightly better.\n\nExpected: STRF model performance at any window length, upper bound 0.2, tolerance 0.02.\nReproduced when, under one reading, the mean performance is at most 0.22 at every window for STRF and\nLN, and a paired one-sided Wilcoxon signed-rank test (validation performance at 4052 ms against\n180 ms, over cells, at 0.05) finds no improvement for either; a Friedman test over the nine windows\nis a variant that does not decide.\n\nMethod (source in brackets): spectrogram of Eq. 47 at 17 frequencies 400 * 2^(k/3) Hz, k = 0..16\n[paper: 3 bins/octave from 0.40 kHz, 17 bins; `logspectrogram.m` evaluates the DFT at each centre\nfrequency; assumption: its rule would give 18 bins up to 20.3 kHz, we keep 17], centred per frequency\nin each stimulus [`STRFanalysis.m`]; 45 history bins of 2^k ms split as in the Methods [paper];\n4-ms response bins, spectrogram frames every 4 ms with the window centred on the bin, coarse bins the\nmean of the 4-ms frames they cover [assumption]; history before onset set to the stimulus mean\n[assumption; every window is scored on the same bins]; ridge regression (Eq. 50) on the\ntrial-averaged response with 33 ridge values 10^-6 ... 10^2 times the mean eigenvalue of the training\nS'S [assumption: grid]; 10 folds [paper], one ridge value for all folds chosen by the mean validation\nperformance of the linear model, and the LN model uses that filter [`STRFanalysis.m`]; robust lowess\n(5% span, one fit plus five robustness iterations) on the training predictions, applied to the\nvalidation fold [paper; iteration convention an assumption]; Eq. 53 with Eq. 52 per fold as in\n`LNperformance` [code], averaged over folds and then over cells [assumption / paper Fig. 4 legend].\n\nReadings run: spectrogram window 10-ms or 20-ms Hann (criterion); folds as 10 contiguous blocks of\nthe concatenated stimuli (`STRFanalysis.m`) or by stimulus (stimulus i in fold i mod 10, fewer folds\nif a cell has fewer than 10 stimuli); the 20% read as the validation (lower) or training (upper)\nestimate. Response sampling: only 4-ms bins were run (Wehr's traces are sampled at 4 kHz, not 10 kHz).\n\"\"\")\n\ncode(\"\"\"\nREADINGS = [(\"hann10_contig\", 10, \"contig\"), (\"hann20_contig\", 20, \"contig\"),\n            (\"hann10_bystim\", 10, \"stim\"), (\"hann20_bystim\", 20, \"stim\")]\ncellnames = list(CELLS)\nRES = {}\nfor name, wm, fm in READINGS:\n    t = time.time()\n    out = {}\n    for c in cellnames:\n        Sc, rbar, ppred, sid, rws = W.prepare(CELLS[c], STIM, wm)\n        fold = W.folds_contiguous(len(rws)) if fm == \"contig\" else W.folds_by_stimulus(sid)\n        out[c] = [W.fit_cell(Sc, rbar, ppred, rws, fold, sp) for sp in W.BIN_SPLITS]\n        out[c + \"/nfold\"] = int(fold.max() + 1)\n        out[c + \"/snr\"] = float(ppred.sum() / ((rbar ** 2).sum()))\n        del Sc\n    RES[name] = out\n    print(f\"{name}: {time.time() - t:.0f} s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\ndef arr(name, model, col):\n    # (cells, windows): col 0 = training (upper), 1 = validation (lower); mean over folds\n    return np.array([[RES[name][c][w][model][:, col].mean() for w in range(9)] for c in cellnames])\n\"\"\", tags=[CL])\n\ncode(\"\"\"\nprint(\"cells:\", len(cellnames))\nprint(\"folds per cell (by-stimulus reading):\", {c: RES[\"hann10_bystim\"][c + \"/nfold\"] for c in cellnames})\nprint(\"predictable power / power of the trial mean, per cell:\",\n      {c: round(RES[\"hann10_contig\"][c + \"/snr\"], 3) for c in cellnames})\nprint()\nprint(\"Mean over cells of model performance (Eq. 53)\")\nprint(f\"{'window ms':>10s}\", \"\".join(f\"{w:>7d}\" for w in W.WINDOWS_MS), \"   max\")\nfor name, _, _ in READINGS:\n    print(name)\n    for model in (\"strf\", \"ln\", \"ln_nonrobust\"):\n        for col, lab in ((1, \"valid\"), (0, \"train\")):\n            m = arr(name, model, col).mean(0)\n            print(f\"{model + ' ' + lab:>18s}\", \"\".join(f\"{v:7.3f}\" for v in m), f\"  {m.max():.3f}\")\n\"\"\", tags=[CL])\n\ncode(\"\"\"\nprint(\"Per-cell validation (lower) and training (upper) performance, reading hann10_contig\")\nfor model in (\"strf\", \"ln\"):\n    for col, lab in ((1, \"valid\"), (0, \"train\")):\n        a = arr(\"hann10_contig\", model, col)\n        print(f\"{model} {lab}  (rows: cells; columns: windows {W.WINDOWS_MS})\")\n        for c, r in zip(cellnames, a):\n            print(f\"  {c:16s}\", r)\nprint()\nfor name, _, _ in READINGS[1:]:\n    print(f\"Per-cell validation at 180 / 4052 ms, reading {name}\")\n    for model in (\"strf\", \"ln\"):\n        a = arr(name, model, 1)\n        print(\" \", model, [f\"{c[2:8]}-{c[-3:]}: {x:.3f}/{y:.3f}\" for c, x, y in zip(cellnames, a[:, 0], a[:, 8])])\n\"\"\", tags=[CL])\n\ncode(\"\"\"\nprint(\"Ridge value chosen (index into a 33-point grid, 0..32), per cell and window\")\nfor name, _, _ in READINGS:\n    B = np.array([[RES[name][c][w][\"best\"] for w in range(9)] for c in cellnames])\n    edge = int(((B == 0) | (B == len(W.RIDGE_REL) - 1)).sum())\n    print(f\"{name}: grid edge hits {edge} of {B.size}; index range {B.min()}..{B.max()}; \"\n          f\"relative ridge 10^{np.log10(W.RIDGE_REL[B.min()]):.2f} .. 10^{np.log10(W.RIDGE_REL[B.max()]):.2f}\")\n    if name == \"hann10_contig\":\n        for c, b in zip(cellnames, B):\n            print(f\"  {c:16s}\", b)\nbad = [(n, c, w) for n, _, _ in READINGS for c in cellnames for w in range(9)\n       if not np.all(np.isfinite(RES[n][c][w][\"strf\"])) or not np.all(np.isfinite(RES[n][c][w][\"ln\"]))]\nprint(\"fits with non-finite performance:\", bad, \"| cells dropped: none\")\n\"\"\", tags=[CL])\n\ncode(\"\"\"\nprint(\"Paired Wilcoxon signed-rank, validation performance at 4052 ms vs 180 ms, one-sided (improvement)\")\nprint(\"and Friedman test over the nine windows (variant, does not decide)\")\nTESTS = {}\nfor name, _, _ in READINGS:\n    for model in (\"strf\", \"ln\"):\n        a = arr(name, model, 1)\n        w = stats.wilcoxon(a[:, 8], a[:, 0], alternative=\"greater\")\n        w2 = stats.wilcoxon(a[:, 8], a[:, 0])\n        fr = stats.friedmanchisquare(*a.T)\n        TESTS[(name, model)] = w.pvalue\n        print(f\"{name:14s} {model:4s}: median diff {np.median(a[:, 8] - a[:, 0]):+.4f}, \"\n              f\"cells improved {int((a[:, 8] > a[:, 0]).sum())}/{len(a)}, W={w.statistic:.0f}, \"\n              f\"p(one-sided)={w.pvalue:.4f}, p(two-sided)={w2.pvalue:.4f}; \"\n              f\"Friedman chi2={fr.statistic:.1f}, p={fr.pvalue:.4f}\")\nprint()\nprint(\"LN gain (mean LN minus mean STRF), validation and training, per window\")\nfor name, _, _ in READINGS:\n    gv = arr(name, \"ln\", 1).mean(0) - arr(name, \"strf\", 1).mean(0)\n    gt = arr(name, \"ln\", 0).mean(0) - arr(name, \"strf\", 0).mean(0)\n    print(f\"{name:14s} valid\", gv, \" train\", gt)\nprint()\nprint(\"Criterion check per reading: max over windows of mean performance <= 0.22 for STRF and LN, \"\n      \"and no Wilcoxon improvement (p >= 0.05) for either\")\nfor name, _, _ in READINGS:\n    for col, lab in ((1, \"validation\"), (0, \"training\")):\n        mx = max(arr(name, \"strf\", col).mean(0).max(), arr(name, \"ln\", col).mean(0).max())\n        noimp = TESTS[(name, \"strf\")] >= 0.05 and TESTS[(name, \"ln\")] >= 0.05\n        print(f\"  {name:14s} {lab:10s}: max mean {mx:.3f} ({'<=' if mx <= 0.22 else '>'} 0.22); \"\n              f\"no improvement: {noimp} -> {'meets' if (mx <= 0.22 and noimp) else 'fails'}\")\n\"\"\", tags=[CL])\n\ncode(\"\"\"\nsub = [i for i, c in enumerate(cellnames) if c.startswith(\"2002\")]\nprint(\"Variant (does not decide): only the 2002 cells, 5 to 25 trials per stimulus:\", len(sub), \"cells\")\nfor name, _, _ in READINGS:\n    for model in (\"strf\", \"ln\"):\n        v = arr(name, model, 1)[sub]; tr = arr(name, model, 0)[sub]\n        w = stats.wilcoxon(v[:, 8], v[:, 0], alternative=\"greater\")\n        print(f\"  {name:14s} {model:4s} valid {v.mean(0)}  train {tr.mean(0)}  p={w.pvalue:.4f}\")\n\"\"\", tags=[CL])\n\ncode(\"\"\"\nfig, axs = plt.subplots(1, 2, figsize=(10, 3.6), sharey=True)\nx = np.array(W.WINDOWS_MS) / 1000\nfor ax, name in zip(axs, [\"hann10_contig\", \"hann20_contig\"]):\n    for model, col in ((\"strf\", \"0.55\"), (\"ln\", \"k\")):\n        ax.plot(x, arr(name, model, 1).mean(0), \"x-\", color=col, label=f\"{model.upper()} validation\")\n        ax.plot(x, arr(name, model, 0).mean(0), \"o--\", mfc=\"none\", color=col, label=f\"{model.upper()} training\")\n    ax.axhline(0.2, color=\"r\", lw=0.8, ls=\":\")\n    ax.set_title(name); ax.set_xlabel(\"window length (s)\")\naxs[0].set_ylabel(\"model performance (Eq. 53)\"); axs[0].legend(fontsize=8)\nplt.tight_layout(); plt.show()\n\"\"\", tags=[CL])\n\nmd(\"\"\"\n**Result: PLACEHOLDER**\n\"\"\", tags=[\"conclusion\"])\n\ncode(\"\"\"\nprint(f\"total time {time.time() - T0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/asari-2009/strf_wehr.ipynb\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_nb.py (file state is current in your context — no need to Read it back)
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; grep -n "diagnostic only" wehr.py; executed/asari-2009/.venv/bin/python $TMPDIR/make_nb.py && date -u && executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 2>&1 | tail -3; date -u
```

```
68:- a diagnostic only (not a reading): the same lowess without the robustness
Thu Nov 19 04:31:19 UTC 2026

[31mTypeError[39m: '>' not supported between instances of 'int' and 'tuple'

Thu Nov 19 04:31:59 UTC 2026
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
s=s.replace('need[sfile] = max(need.get(sfile, 0), nb), tr[0]["ramp"]','need[sfile] = (max(need.get(sfile, (0, 0))[0], nb), tr[0]["ramp"])')
open('wehr.py','w').write(s)
EOF
date -u && executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 2>&1 | tail -3; date -u
```

```
Thu Nov 19 04:32:04 UTC 2026
[NbConvertApp] Converting notebook strf_wehr.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 127937 bytes to /tmp/claude-1001/strf_wehr.ipynb
Thu Nov 19 04:51:39 UTC 2026
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import json;nb=json.load(open('strf_wehr.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code': continue
  for o in c.get('outputs',[]):
    if 'text' in o: print(f'--- cell {i}'); print(''.join(o['text'])[:9000])
    elif o.get('output_type')=='error': print('ERR', o['ename'], o['evalue'])
"
```

```
--- cell 1
seed 3644763024 (unused: folds are contiguous blocks or stimuli in order)

--- cell 3
Summary.mat: experiments [(0, 'Repeated presentation of a fixed subset of sounds to auditory cortical cell.'), (1, 'Auditory cortical responses to as many natural sounds as possible.')]
references: ['C. K. Machens, M. S. Wehr, and A. M. Zador (2004) "Linearity of Cortical Receptive Fields Measured with Natural Sounds." J Neurosci, 24(5):1089-1100.']
cells in Summary.mat: 25 | cells with >= 2 trials of a natural sound: 16
excluded (every natural sound presented once): ['20030328-mw-001', '20030401-mw-003', '20030404-mw-001', '20030407-mw-003', '20030407-mw-004', '20030407-mw-005', '20030409-mw-001', '20030409-mw-002', '20030410-mw-002']

--- cell 3
loaded in 65 s; peak RSS 0.59 GB

cell             stim trials per stimulus                         bins     sf unit  raw range (mV)   stim dur (s)
20020508-mw-003    11 [20, 10, 10, 10, 10, 10, 10, 10, 10, 11,   45437   4000 mV   [ -50.1,  -3.0]  [15.0, 31.75]
20020530-mw-001     7 [10, 10, 12, 10, 10, 11, 14]               26250   4000 mV   [ -52.0,  31.9]  [15.0]
20020602-mw-001     5 [10, 10, 10, 10, 10]                       18750   4000 mV   [ -66.5, -23.4]  [15.0]
20020604-mw-001     9 [6, 9, 12, 10, 10, 10, 10, 10, 19]         33750   4000 mV   [ -59.7,  21.8]  [15.0]
20020604-mw-002     3 [20, 20, 9]                                11250   4000 mV   [ -65.1, -15.9]  [15.0]
20020604-mw-003     8 [20, 20, 20, 20, 20, 20, 20, 15]           30000   4000 mV   [ -57.3,  18.5]  [15.0]
20020605-mw-002     5 [10, 10, 10, 20, 20]                       18750   4000 mV   [-221.9,  41.7]  [15.0]
[... 258 more lines not kept]
```

**Subagent calls Bash**

```bash
cat > $TMPDIR/prof.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="2"; os.environ["OPENBLAS_NUM_THREADS"]="2"
import sys, time, cProfile, pstats
sys.path.insert(0, "entries/asari-2009")
import numpy as np, wehr
sel=wehr.select_cells(); c='20030407-mw-001'
cells, stim = wehr.load_cells({c: sel[c]}, wins_ms=(10,))
Sc, rbar, ppred, sid, rows = wehr.prepare(cells[c], stim, 10)
fold=wehr.folds_contiguous(len(rows))
cProfile.run("wehr.fit_cell(Sc, rbar, ppred, rows, fold, wehr.BIN_SPLITS[8])", "/tmp/claude-1001/p.out")
pstats.Stats("/tmp/claude-1001/p.out").sort_stats("tottime").print_stats(12)
EOF
executed/asari-2009/.venv/bin/python $TMPDIR/prof.py 2>&1 | tail -25
```

```
Thu Nov 19 04:52:25 2026    /tmp/claude-1001/p.out

         41555 function calls in 3.693 seconds

   Ordered by: internal time
   List reduced from 140 to 12 due to restriction <12>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       27    1.076    0.040    1.079    0.040 entries/asari-2009/wehr.py:268(design)
        1    1.044    1.044    3.690    3.690 entries/asari-2009/wehr.py:373(fit_cell)
       20    0.730    0.036    1.083    0.054 entries/asari-2009/wehr.py:331(lowess_fit)
       10    0.411    0.041    0.411    0.041 executed/asari-2009/.venv/lib/python3.13/site-packages/numpy/linalg/_linalg.py:1513(eigh)
       20    0.119    0.006    0.119    0.006 {method 'argsort' of 'numpy.ndarray' objects}
      745    0.087    0.000    0.087    0.000 {method 'reduce' of 'numpy.ufunc' objects}
       70    0.072    0.001    0.072    0.001 {method 'partition' of 'numpy.ndarray' objects}
       70    0.070    0.001    0.070    0.001 {built-in method numpy._core._multiarray_umath.interp}
       30    0.027    0.001    0.027    0.001 executed/asari-2009/.venv/lib/python3.13/site-packages/numpy/_core/_methods.py:96(_clip)
       70    0.012    0.000    0.017    0.000 entries/asari-2009/wehr.py:323(perf)
     4040    0.010    0.000    0.010    0.000 {built-in method numpy.arange}
     4000    0.005    0.000    0.005    0.000 {method 'argmin' of 'numpy.ndarray' objects}
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; grep -n "def lowess_fit" -A 25 wehr.py | sed -n 1,25p; date -u
```

```
331:def lowess_fit(x, y, span=LOWESS_SPAN, iters=LOWESS_ITER, ngrid=LOWESS_GRID):
332-    """Robust lowess (Cleveland 1979) of y on x; returns (grid, fitted values)."""
333-    o = np.argsort(x)
334-    xs, ys = x[o], y[o]
335-    n = len(xs)
336-    k = max(int(np.ceil(span * n)), 3)
337-    g = np.unique(np.quantile(xs, np.linspace(0, 1, ngrid)))
338-    pos = np.searchsorted(xs, g)
339-    # nearest-k window [l, l+k) for each grid point
340-    L = np.empty(len(g), int)
341-    for i, (gi, p) in enumerate(zip(g, pos)):
342-        lo = np.arange(max(0, p - k), min(p, n - k) + 1)
343-        cost = np.maximum(gi - xs[lo], xs[lo + k - 1] - gi)
344-        L[i] = lo[np.argmin(cost)]
345-    idx = L[:, None] + np.arange(k)[None, :]
346-    X = xs[idx]
347-    Y = ys[idx]
348-    d = np.abs(X - g[:, None])
349-    dmax = d.max(1, keepdims=True)
350-    dmax[dmax == 0] = 1
[... 6 more lines not kept]
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
old=s[s.index("    pos = np.searchsorted(xs, g)\n    # nearest-k"):s.index("    idx = L[:, None] + np.arange(k)[None, :]")]
new='''    # nearest-k window [l, l+k) for each grid point: the smallest l with
    # xs[l] + xs[l+k-1] >= 2 g, or the one before it (vectorized bisection)
    lo = np.zeros(len(g), int)
    hi = np.full(len(g), n - k)
    while np.any(lo < hi):
        mid = (lo + hi) // 2
        right = xs[mid] + xs[mid + k - 1] < 2 * g
        lo = np.where(right & (lo < hi), mid + 1, lo)
        hi = np.where(~right & (lo < hi), mid, hi)
    prev = np.maximum(lo - 1, 0)
    c_lo = np.maximum(g - xs[lo], xs[lo + k - 1] - g)
    c_pr = np.maximum(g - xs[prev], xs[prev + k - 1] - g)
    L = np.where(c_pr < c_lo, prev, lo)
'''
s=s.replace(old,new)
# replace fit_cell
i=s.index("def fit_cell(")
s=s[:i]+'''def fit_window(X, rbar, ppred, schemes, ridge_rel=RIDGE_REL, nonrobust=True):
    """Ridge STRF (Eq. 50) and LN (Eq. 51) for one window under several fold schemes.

    X: (n, 765) stimulus matrix (Eq. 48); schemes: {name: fold id per bin, -1 =
    bin not used}. Grams are computed once per atom (bins sharing all fold ids)
    and summed. For each scheme returns per-fold performance (columns: training
    = upper, validation = lower) of STRF and LN at the one ridge value with the
    best mean validation performance (STRFanalysis.m), and that value.
    """
    names = list(schemes)
    F = np.stack([schemes[k] for k in names], 1)
    atoms, inv = np.unique(F, axis=0, return_inverse=True)
    inv = inv.ravel()
    p = X.shape[1]
    Ga = np.zeros((len(atoms), p, p))
    Ba = np.zeros((len(atoms), p))
    for a in range(len(atoms)):
        ii = np.flatnonzero(inv == a)
        if atoms[a].max() < 0:
            continue
        Xa = X[ii]
        Ga[a] = Xa.T @ Xa
        Ba[a] = Xa.T @ rbar[ii]
    out = {}
    for si, name in enumerate(names):
        fold = schemes[name]
        K = fold.max() + 1
        use = atoms[:, si] >= 0
        Gt, Bt = Ga[use].sum(0), Ba[use].sum(0)
        Wf = np.empty((K, p, len(ridge_rel)))
        lam = np.empty((K, len(ridge_rel)))
        vperf = np.empty((K, len(ridge_rel)))
        for f in range(K):
            m = atoms[:, si] == f
            ev, V = np.linalg.eigh(Gt - Ga[m].sum(0))
            ev = np.clip(ev, 0, None)
            lam[f] = ridge_rel * ev.mean()
            z = V.T @ (Bt - Ba[m].sum(0))
            Wf[f] = V @ (z[:, None] / (ev[:, None] + lam[f][None, :]))
            v = np.flatnonzero(fold == f)
            vperf[f] = perf(rbar[v, None], X[v] @ Wf[f], ppred[v])
        best = int(np.argmax(vperf.mean(0)))     # one value for all folds
        r = dict(best=best, ridge_rel=float(ridge_rel[best]), nfold=int(K))
        lin, ln, ln0 = (np.empty((K, 2)) for _ in range(3))
        for f in range(K):
            t = np.flatnonzero((fold >= 0) & (fold != f))
            v = np.flatnonzero(fold == f)
            pt, pv = X[t] @ Wf[f][:, best], X[v] @ Wf[f][:, best]
            lin[f] = perf(rbar[t], pt, ppred[t]), perf(rbar[v], pv, ppred[v])
            for arr, it in ((ln, LOWESS_ITER), (ln0, 0)):
                if it == 0 and not nonrobust:
                    arr[f] = np.nan
                    continue
                g, fit = lowess_fit(pt, rbar[t], iters=it)
                arr[f] = (perf(rbar[t], np.interp(pt, g, fit), ppred[t]),
                          perf(rbar[v], np.interp(pv, g, fit), ppred[v]))
        r["strf"], r["ln"], r["ln_nonrobust"] = lin, ln, ln0
        out[name] = r
    return out


_DATA = {}


def run_cell(args):
    """All windows and fold schemes for one cell and one spectrogram window.

    Schemes: folds as 10 contiguous blocks or by stimulus, scoring every bin
    from stimulus onset ("all") or only bins at least 4052 ms after onset
    ("late", so no window reaches before onset). Uses ``_DATA`` (set before
    forking) to avoid pickling the data.
    """
    cell, win_ms = args
    Sc, rbar, ppred, sid, rows = prepare(_DATA["cells"][cell], _DATA["stim"], win_ms)
    late = np.concatenate([np.arange(s["R"].shape[1]) >= PAD for s in _DATA["cells"][cell]])
    schemes = {}
    schemes["contig/all"] = folds_contiguous(len(rows))
    schemes["stim/all"] = folds_by_stimulus(sid)
    fl = np.full(len(rows), -1)
    fl[late] = folds_contiguous(int(late.sum()))
    schemes["contig/late"] = fl
    fs = np.full(len(rows), -1)
    fs[late] = folds_by_stimulus(sid)[late]
    schemes["stim/late"] = fs
    res = []
    for sp in BIN_SPLITS:
        X = design(Sc, sp, rows)
        res.append(fit_window(X, rbar, ppred, schemes))
        del X
    snr = float(ppred.sum() / (rbar ** 2).sum())
    return cell, win_ms, res, snr, int(late.sum()), len(rows)
'''
open('wehr.py','w').write(s)
EOF
cat > $TMPDIR/t2.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"
import sys, time, resource
sys.path.insert(0, "entries/asari-2009")
import numpy as np, wehr
r=np.random.default_rng(0)
x=r.normal(size=20000); y=np.maximum(x,0)**2+r.normal(size=20000)*0.5
g,f=wehr.lowess_fit(x,y); print('lowess check', np.abs(f-np.maximum(g,0)**2)[5:-5].max())
sel=wehr.select_cells(); c=sys.argv[1]
cells, stim = wehr.load_cells({c: sel[c]}, wins_ms=(10,))
wehr._DATA.update(cells=cells, stim=stim)
t=time.time(); out=wehr.run_cell((c,10)); print('time', time.time()-t, out[3:], resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
for w in (0,8):
  for k,v in out[2][w].items(): print(w,k,v['best'],v['nfold'],v['strf'].mean(0),v['ln'].mean(0),v['ln_nonrobust'].mean(0))
EOF
executed/asari-2009/.venv/bin/python $TMPDIR/t2.py 20020604-mw-003; date -u
```

```
lowess check 0.05318874777948889
time 42.62610220909119 (0.9392333900370516, 21896, 30000) 0.80946
0 contig/all 26 10 [0.37085842 0.2749009 ] [0.39701424 0.24396972] [0.42114274 0.27240791]
0 stim/all 27 8 [0.35426418 0.22445606] [0.38703458 0.18647929] [0.41273144 0.20280033]
0 contig/late 26 10 [0.41749113 0.30726542] [0.45250333 0.28453858] [0.47516014 0.30446361]
0 stim/late 27 8 [0.39855871 0.23164581] [0.43906055 0.19702748] [0.46326233 0.19384507]
8 contig/all 25 10 [0.4410952  0.30214459] [0.46907961 0.27553234] [0.49091435 0.29595896]
8 stim/all 27 8 [0.38133746 0.22681571] [0.42073898 0.1806244 ] [0.445963  0.1951431]
8 contig/late 26 10 [0.46418502 0.32975347] [0.50583281 0.30621984] [0.52499979 0.32108135]
8 stim/late 27 8 [0.42822028 0.20678402] [0.47436868 0.14480135] [0.49648185 0.14592516]
Thu Nov 19 04:54:00 UTC 2026
```

**Subagent calls Bash**

```bash
cat > $TMPDIR/prof2.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"
import sys, cProfile, pstats
sys.path.insert(0, "entries/asari-2009")
import numpy as np, wehr
sel=wehr.select_cells(); c='20020604-mw-003'
cells, stim = wehr.load_cells({c: sel[c]}, wins_ms=(10,))
wehr._DATA.update(cells=cells, stim=stim)
wehr.BIN_SPLITS = wehr.BIN_SPLITS[:2]
cProfile.run("wehr.run_cell((c,10))", "/tmp/claude-1001/p.out")
pstats.Stats("/tmp/claude-1001/p.out").sort_stats("tottime").print_stats(10)
EOF
executed/asari-2009/.venv/bin/python $TMPDIR/prof2.py 2>&1 | grep -A 16 "ncalls"
```

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       72    4.382    0.061    4.384    0.061 executed/asari-2009/.venv/lib/python3.13/site-packages/numpy/linalg/_linalg.py:1513(eigh)
        2    2.243    1.122    7.051    3.525 entries/asari-2009/wehr.py:379(fit_window)
      144    0.825    0.006    1.298    0.009 entries/asari-2009/wehr.py:331(lowess_fit)
       16    0.740    0.046    7.080    0.442 /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/asyncio/base_events.py:1981(_run_once)
       16    0.354    0.022    1.344    0.084 /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/selectors.py:435(select)
     7898    0.220    0.000    0.220    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        2    0.192    0.096    0.192    0.096 entries/asari-2009/wehr.py:268(design)
      146    0.181    0.001    0.181    0.001 {method 'argsort' of 'numpy.ndarray' objects}
       16    0.147    0.009    0.317    0.020 {method 'poll' of 'select.epoll' objects}
      504    0.111    0.000    0.111    0.000 {method 'partition' of 'numpy.ndarray' objects}
```

**Subagent calls Bash**

```bash
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 executed/asari-2009/.venv/bin/python -c "
import numpy as np, scipy.linalg as sl, time
r=np.random.default_rng(0); A=r.normal(size=(3000,765)); G=A.T@A
for f in [lambda: np.linalg.eigh(G), lambda: sl.eigh(G, driver='evd'), lambda: sl.eigh(G, driver='evr'), lambda: np.linalg.eigh(G.astype(np.float32)), lambda: sl.cho_factor(G)]:
  t=time.time(); [f() for _ in range(5)]; print((time.time()-t)/5)
"
```

```
0.07165374755859374
0.06772704124450683
0.08675575256347656
0.0758544921875
0.005342531204223633
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('make_nb.py').read()
a=s.index('code("""\nREADINGS = [')
b=s.index('code("""\nprint("cells:", len(cellnames))')
s=s[:a]+'''code("""
import multiprocessing as mp
SCHEMES = ["contig/all", "stim/all", "contig/late", "stim/late"]
READINGS = [f"hann{w}/{s}" for w in (10, 20) for s in SCHEMES]
cellnames = list(CELLS)
W._DATA.update(cells=CELLS, stim=STIM)          # inherited by the two forked workers
size = {c: sum(s["R"].shape[1] for s in CELLS[c]) for c in cellnames}
tasks = sorted([(c, w) for c in cellnames for w in (10, 20)], key=lambda t: -size[t[0]])
t = time.time()
RES = {r: {} for r in READINGS}
INFO = {}
with mp.get_context("fork").Pool(2) as pool:
    for c, wm, res, snr, nlate, nall in pool.imap_unordered(W.run_cell, tasks):
        for s in SCHEMES:
            RES[f"hann{wm}/{s}"][c] = [res[w][s] for w in range(9)]
        INFO[c] = dict(snr=snr, late=nlate, all=nall)
print(f"fits: {time.time() - t:.0f} s (2 processes, 1 BLAS thread each)")

def arr(name, model, col):
    # (cells, windows): col 0 = training (upper), 1 = validation (lower); mean over folds
    return np.array([[RES[name][c][w][model][:, col].mean() for w in range(9)] for c in cellnames])
""", tags=[CL])

'''+s[b:]
s=s.replace('''print("folds per cell (by-stimulus reading):", {c: RES["hann10_bystim"][c + "/nfold"] for c in cellnames})
print("predictable power / power of the trial mean, per cell:",
      {c: round(RES["hann10_contig"][c + "/snr"], 3) for c in cellnames})''','''print("folds per cell (by-stimulus readings):", {c: RES["hann10/stim/all"][c][0]["nfold"] for c in cellnames})
print("bins per cell, all / late (>= 4052 ms after onset):", {c: (INFO[c]["all"], INFO[c]["late"]) for c in cellnames})
print("predictable power (Eq. 52) / power of the trial mean, per cell (10-kHz-free check of reliability):",
      {c: round(INFO[c]["snr"], 3) for c in cellnames})''')
s=s.replace("(10-kHz-free check of reliability)","")
s=s.replace('for name, _, _ in READINGS:','for name in READINGS:')
s=s.replace('for name, _, _ in READINGS[1:]:','for name in READINGS[1:]:')
s=s.replace('''for n, _, _ in READINGS''','''for n in READINGS''')
s=s.replace('"hann10_contig"','"hann10/contig/all"').replace('"hann20_contig"','"hann20/contig/all"')
s=s.replace('''print(f"{name:14s} {model:4s}:''','''print(f"{name:18s} {model:4s}:''')
s=s.replace('''print(f"{name:14s} valid"''','''print(f"{name:18s} valid"''')
s=s.replace('''print(f"  {name:14s} {lab:10s}''','''print(f"  {name:18s} {lab:10s}''')
s=s.replace('''print(f"  {name:14s} {model:4s} valid''','''print(f"  {name:18s} {model:4s} valid''')
s=s.replace('''for ax, name in zip(axs, ["hann10/contig/all", "hann20/contig/all"]):''','''for ax, name in zip(axs, ["hann10/contig/all", "hann10/contig/late"]):''')
s=s.replace('''os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")''','''os.environ.setdefault("OMP_NUM_THREADS", "1")       # two worker processes, one BLAS thread each
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")''')
# readings text
s=s.replace('''Readings run: spectrogram window 10-ms or 20-ms Hann (criterion); folds as 10 contiguous blocks of
the concatenated stimuli (`STRFanalysis.m`) or by stimulus (stimulus i in fold i mod 10, fewer folds
if a cell has fewer than 10 stimuli); the 20% read as the validation (lower) or training (upper)
estimate.''','''Readings run (all combinations, 8 in all, each read on validation and on training data):
spectrogram window 10-ms or 20-ms Hann (criterion); folds as 10 contiguous blocks of the
concatenated stimuli (`STRFanalysis.m`) or by stimulus (stimulus i in fold i mod 10, fewer folds if a
cell has fewer than 10 stimuli); bins scored from stimulus onset with the pre-onset history set to the
stimulus mean ("all"), or only bins at least 4052 ms after onset so that no window reaches before
onset ("late"; `STRFanalysis.m` also drops the first window length of each stimulus, there for each
window separately; here the same bins for every window so windows stay comparable). The 20% is read
as the validation (lower) or training (upper) estimate.''')
s=s.replace('''history before onset set to the stimulus mean
[assumption; every window is scored on the same bins]''','''history before onset set to the stimulus mean
in the "all" readings [assumption; every window is scored on the same bins]''')
open('make_nb.py','w').write(s)
EOF
grep -n "hann10_\|_contig\|_bystim\|, _, _" make_nb.py
```

```
174:print("Per-cell validation (lower) and training (upper) performance, reading hann10_contig")
```

**Subagent calls Bash**

```bash
cd $TMPDIR; sed -i 's/performance, reading hann10_contig")/performance, reading hann10\/contig\/all")/' make_nb.py; cd entries/asari-2009; executed/asari-2009/.venv/bin/python $TMPDIR/make_nb.py && date -u && executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARNING | tail -3; date -u
```

```
Thu Nov 19 04:55:06 UTC 2026
[NbConvertApp] Converting notebook strf_wehr.ipynb to notebook
[NbConvertApp] Writing 144805 bytes to /tmp/claude-1001/strf_wehr.ipynb
Thu Nov 19 05:15:31 UTC 2026
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import json;nb=json.load(open('strf_wehr.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code' or i<4: continue
  for o in c.get('outputs',[]):
    if 'text' in o: print(f'--- cell {i}'); print(''.join(o['text'])[:12000])
    elif o.get('output_type')=='error': print('ERR', o['ename'], o['evalue'])
" | grep -v "^  20\|^  strf \[\|^  ln \["
```

```
--- cell 5
fits: 1171 s (2 processes, 1 BLAS thread each)

--- cell 6
cells: 16
folds per cell (by-stimulus readings): {'20020508-mw-003': 10, '20020530-mw-001': 7, '20020602-mw-001': 5, '20020604-mw-001': 9, '20020604-mw-002': 3, '20020604-mw-003': 8, '20020605-mw-002': 5, '20020605-mw-003': 3, '20020608-mw-001': 6, '20020608-mw-002': 10, '20030401-mw-001': 10, '20030403-mw-001': 10, '20030404-mw-002': 10, '20030407-mw-001': 10, '20030407-mw-002': 7, '20030410-mw-001': 10}
bins per cell, all / late (>= 4052 ms after onset): {'20020508-mw-003': (45437, 34294), '20020530-mw-001': (26250, 19159), '20020602-mw-001': (18750, 13685), '20020604-mw-001': (33750, 24633), '20020604-mw-002': (11250, 8211), '20020604-mw-003': (30000, 21896), '20020605-mw-002': (18750, 13685), '20020605-mw-003': (11250, 8211), '20020608-mw-001': (22500, 16422), '20020608-mw-002': (37500, 27370), '20030401-mw-001': (124125, 105891), '20030403-mw-001': (124125, 105891), '20030404-mw-002': (78625, 67482), '20030407-mw-001': (124125, 105891), '20030407-mw-002': (48250, 41159), '20030410-mw-001': (206500, 176110)}
predictable power (Eq. 52) / power of the trial mean, per cell : {'20020508-mw-003': 0.965, '20020530-mw-001': 0.856, '20020602-mw-001': 0.555, '20020604-mw-001': 0.919, '20020604-mw-002': 0.896, '20020604-mw-003': 0.939, '20020605-mw-002': 0.836, '20020605-mw-003': 0.95, '20020608-mw-001': 0.973, '20020608-mw-002': 0.962, '20030401-mw-001': 0.733, '20030403-mw-001': 0.707, '20030404-mw-002': 0.72, '20030407-mw-001': 0.699, '20030407-mw-002': 0.629, '20030410-mw-001': 0.74}

Mean over cells of model performance (Eq. 53)
 window ms     180    324    548    884   1364   2004   2772   3540   4052    max
hann10/contig/all
        strf valid   0.115  0.133  0.143  0.147  0.147  0.148  0.145  0.146  0.147   0.148
        strf train   0.173  0.213  0.240  0.247  0.249  0.254  0.247  0.247  0.249   0.254
          ln valid   0.016 -0.002  0.044  0.054  0.035  0.044  0.044  0.040  0.039   0.054
   
[... 148 more lines not kept]
```

**Subagent calls Bash**

```bash
cat > $TMPDIR/dbg.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="2"; os.environ["OPENBLAS_NUM_THREADS"]="2"
import sys, time
sys.path.insert(0, "entries/asari-2009")
import numpy as np, wehr
sel=wehr.select_cells(); c='20020604-mw-003'
cells, stim = wehr.load_cells({c: sel[c]}, wins_ms=(10,))
wehr._DATA.update(cells=cells, stim=stim)
wehr.BIN_SPLITS=[wehr.BIN_SPLITS[0], wehr.BIN_SPLITS[7]]
t=time.time(); out=wehr.run_cell((c,10)); print(time.time()-t)
for w in range(2):
  r=out[2][w]['contig/late']; print(r['best'], r['strf'])
Sc, rbar, ppred, sid, rows = wehr.prepare(cells[c], stim, 10)
late = np.concatenate([np.arange(s["R"].shape[1]) >= wehr.PAD for s in cells[c]])
fl = np.full(len(rows), -1); fl[late] = wehr.folds_contiguous(int(late.sum()))
for f in range(10):
  v=fl==f; print(f, v.sum(), np.unique(sid[v]), ppred[v].sum(), (rbar[v]**2).sum())
EOF
executed/asari-2009/.venv/bin/python $TMPDIR/dbg.py
```

```
7.180956602096558
26 [[0.43108153 0.15193621]
 [0.41550369 0.33315579]
 [0.40129575 0.41249456]
 [0.39337874 0.46962466]
 [0.41027966 0.40132404]
 [0.44070133 0.09542693]
 [0.43155692 0.03841781]
 [0.43041584 0.2308422 ]
 [0.41191199 0.43786146]
 [0.40878584 0.50157058]]
26 [[0.48034472 0.24304292]
 [0.46545539 0.33042535]
 [0.4493302  0.41750586]
 [0.43561609 0.50171611]
 [0.45629963 0.424924  ]
 [0.48564912 0.09163323]
 [0.47626598 0.04326436]
 [0.4758434  0.25805207]
 [0.46328311 0.35222642]
[... 11 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import json;nb=json.load(open('strf_wehr.ipynb'))
t=''.join(nb['cells'][7]['outputs'][0]['text']); i=t.index('contig/late'); print(t[i:i+1500])
"; executed/asari-2009/.venv/bin/python -c "
import fsspec, zipfile
z = zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/crcns-ac1.zip', block_size=2**22).open())
print(z.read('wehr/Tools/ViewSTRF.m').decode('latin-1'))
" | grep -v "^%" | grep -i -n "perf\|mean"
```

```
contig/late
  strf ['020508-003: 0.194/0.229', '020530-001: 0.081/0.096', '020602-001: 1.201/14.680', '020604-001: -0.134/-0.402', '020604-002: 0.140/0.139', '020604-003: 0.307/0.330', '020605-002: 0.155/0.109', '020605-003: 0.106/0.239', '020608-001: 0.167/0.208', '020608-002: 0.054/0.067', '030401-001: 0.066/0.127', '030403-001: 0.193/0.134', '030404-002: 0.180/0.238', '030407-001: 0.165/0.197', '030407-002: 0.232/0.235', '030410-001: 0.152/0.190']
  ln ['020508-003: 0.144/0.165', '020530-001: 0.081/0.025', '020602-001: 0.448/12.677', '020604-001: -2.924/-2.963', '020604-002: 0.122/0.073', '020604-003: 0.285/0.306', '020605-002: 0.120/0.136', '020605-003: 0.233/0.245', '020608-001: 0.126/0.134', '020608-002: 0.028/0.018', '030401-001: -0.049/0.061', '030403-001: 0.258/0.233', '030404-002: 0.133/0.178', '030407-001: 0.105/0.153', '030407-002: 0.202/0.209', '030410-001: 0.110/0.161']
Per-cell validation at 180 / 4052 ms, reading hann10/stim/late
  strf ['020508-003: 0.198/0.223', '020530-001: 0.048/0.048', '020602-001: -0.032/-0.011', '020604-001: -0.077/-0.405', '020604-002: 0.045/-0.011', '020604-003: 0.232/0.207', '020605-002: 0.154/0.118', '020605-003: 0.144/0.241', '020608-001: 0.083/0.046', '020608-002: 0.054/0.067', '030401-001: 0.053/0.100', '030403-001: 0.129/0.159', '030404-002: 0.163/0.219', '030407-001: 0.143/0.174', '030407-002: 0.210/0.196', '030410-001: 0.147/0.209']
  ln ['020508-003: 0.167/0.173', '020530-001: -0.038/-0.052', '020602-001: -1.124/-0.561', '020
8:        ~isfield(strf,'response') || ~isfield(strf,'performance'),
16:filter = reshape(mean(strf.model.linear,2),[],strf.param.nbin);
59:a = [mean(strf.performance.linear,2),mean(strf.performance.nonlinear,2)]; c = {'r','g'};
69:ylabel('Model performance');
```

**Subagent calls Bash**

```bash
uptime; ps aux --sort=-%cpu | head -8 | cut -c1-150
```

```
05:16:35 up  1:05,  0 users,  load average: 1.14, 1.80, 1.83
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
runner         1 33.3  0.0   3800  1488 ?        Ss   05:16   0:00 bwrap --new-session --die-with-parent --ro-bind / / --ro-bind /home/runner [removed: a home directory path]
runner         2 25.0  0.0  10220  5924 ?        S    05:16   0:00 /bin/bash -c source /home/runner/.claude/shell-snapshots/snapshot-bash-179506186270
runner         5  0.0  0.0   9964  4136 ?        R    05:16   0:00 ps aux --sort=-%cpu
runner         6  0.0  0.0  17596  7712 ?        S    05:16   0:00 head -8
runner         7  0.0  0.0  17536  7300 ?        S    05:16   0:00 cut -c1-150
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
old='''        lin, ln, ln0 = (np.empty((K, 2)) for _ in range(3))
        for f in range(K):
            t = np.flatnonzero((fold >= 0) & (fold != f))
            v = np.flatnonzero(fold == f)
            pt, pv = X[t] @ Wf[f][:, best], X[v] @ Wf[f][:, best]
'''
new='''        lin, ln, ln0 = (np.empty((K, 2)) for _ in range(3))
        P = X @ Wf[:, :, best].T                  # (n, K): every fold's filter on all bins
        for f in range(K):
            t = np.flatnonzero((fold >= 0) & (fold != f))
            v = np.flatnonzero(fold == f)
            pt, pv = P[t, f], P[v, f]
'''
assert old in s
s=s.replace(old,new)
s=s.replace('''                if it == 0 and not nonrobust:''','''                if it == 0 and name not in nonrobust:''')
s=s.replace('''def fit_window(X, rbar, ppred, schemes, ridge_rel=RIDGE_REL, nonrobust=True):''','''def fit_window(X, rbar, ppred, schemes, ridge_rel=RIDGE_REL, nonrobust=("contig/all",)):''')
s=s.replace('''- a diagnostic only (not a reading): the same lowess without the robustness
  iterations, to show how much the robust weights cost in Eq. 53;''','''- a diagnostic only (not a reading): the same lowess without the robustness
  iterations, for the contiguous-fold, all-bins scheme only;
- per-fold performance averaged over folds as ``ViewSTRF.m`` does
  (``mean(strf.performance.linear, 2)``);''')
s=s.replace('''- per-cell performance is the mean over the 10 folds; the paper's numbers are
  means over cells.''','''- the paper's numbers are means over cells.''')
open('wehr.py','w').write(s)
EOF
grep -n "per-cell performance\|ViewSTRF" wehr.py; sed -i "s/c=sys.argv\[1\]/c=sys.argv[1]; os.environ['X']='1'/" $TMPDIR/t2.py; date -u; executed/asari-2009/.venv/bin/python $TMPDIR/t2.py 20030407-mw-001 | grep time; date -u
```

```
70:- per-fold performance averaged over folds as ``ViewSTRF.m`` does
Thu Nov 19 05:16:51 UTC 2026
time 85.87033987045288 (0.6985669171831663, 105891, 124125) 1.691312
Thu Nov 19 05:18:27 UTC 2026
```

**Subagent calls Bash**

```bash
sed -i "s/c='20020604-mw-003'/c='20030407-mw-001'/; s/BIN_SPLITS\[:2\]/BIN_SPLITS[7:8]/" $TMPDIR/prof2.py; executed/asari-2009/.venv/bin/python $TMPDIR/prof2.py 2>&1 | grep -A 14 "ncalls"
```

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       16    4.868    0.304    6.806    0.425 /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/asyncio/base_events.py:1981(_run_once)
       40    2.459    0.061    2.461    0.062 executed/asari-2009/.venv/lib/python3.13/site-packages/numpy/linalg/_linalg.py:1513(eigh)
       50    1.724    0.034    2.662    0.053 entries/asari-2009/wehr.py:332(lowess_fit)
        1    0.675    0.675    2.746    2.746 entries/asari-2009/wehr.py:380(fit_window)
        1    0.453    0.453    0.453    0.453 entries/asari-2009/wehr.py:269(design)
       51    0.384    0.008    0.384    0.008 {method 'argsort' of 'numpy.ndarray' objects}
     3573    0.364    0.000    0.364    0.000 {method 'reduce' of 'numpy.ufunc' objects}
      250    0.247    0.001    0.247    0.001 {method 'partition' of 'numpy.ndarray' objects}
       16    0.214    0.013    0.331    0.021 {method 'poll' of 'select.epoll' objects}
      300    0.193    0.001    0.193    0.001 {built-in method numpy._core._multiarray_umath.interp}
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
old=s[s.index('    fs = np.full(len(rows), -1)\n'):s.index('    res = []\n    for sp in BIN_SPLITS:')]
s=s.replace(old,'')
s=s.replace('''    Schemes: folds as 10 contiguous blocks or by stimulus, scoring every bin
    from stimulus onset ("all") or only bins at least 4052 ms after onset
    ("late", so no window reaches before onset).''','''    Schemes: folds as 10 contiguous blocks or by stimulus, scoring every bin
    from stimulus onset ("all"); and contiguous folds over only the bins at
    least 4052 ms after onset ("late", so no window reaches before onset).''')
s=s.replace("LOWESS_SPAN, LOWESS_ITER, LOWESS_GRID = 0.05, 5, 200","LOWESS_SPAN, LOWESS_ITER, LOWESS_GRID = 0.05, 5, 100")
s=s.replace("evaluated at 200 quantiles","evaluated at 100 quantiles")
open('wehr.py','w').write(s)
EOF
grep -n "stim/late\|200\b" wehr.py; executed/asari-2009/.venv/bin/python $TMPDIR/t2.py 20030407-mw-001 | grep -v "^[08] stim"; date -u
```

```
lowess check 0.04911748486438837
time 61.09872651100159 (0.6985669171831663, 105891, 124125) 1.709024
0 contig/all 22 10 [0.18116738 0.14761713] [0.12482201 0.08791343] [0.26955552 0.22189072]
0 contig/late 22 10 [0.19668434 0.16505014] [0.13191191 0.10408   ] [nan nan]
8 contig/all 22 10 [0.25374047 0.17075163] [0.19450774 0.11412536] [0.32639305 0.21528909]
8 contig/late 22 10 [0.28137795 0.19694178] [0.22913037 0.15283746] [nan nan]
Thu Nov 19 05:20:16 UTC 2026
```

**Subagent calls Bash**

```bash
cat > $TMPDIR/tm.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"
import sys, time
sys.path.insert(0, "entries/asari-2009")
import numpy as np, wehr
sel=wehr.select_cells(); c='20030407-mw-001'
cells, stim = wehr.load_cells({c: sel[c]}, wins_ms=(10,))
Sc, rbar, ppred, sid, rows = wehr.prepare(cells[c], stim, 10)
T=time.perf_counter
t=T(); X=wehr.design(Sc, wehr.BIN_SPLITS[8], rows); print('design', T()-t, X.shape)
t=T(); G=X.T@X; print('gram', T()-t)
fold=wehr.folds_contiguous(len(rows))
t=T(); 
for f in range(10): ii=np.flatnonzero(fold==f); Xa=X[ii]; Ga=Xa.T@Xa
print('atom grams', T()-t)
t=T(); np.linalg.eigh(G); print('eigh', T()-t)
W=np.random.default_rng(0).normal(size=(765,33))
t=T(); 
for f in range(10): v=np.flatnonzero(fold==f); P=X[v]@W
print('valid preds x10', T()-t)
t=T(); P=X@W[:,:10]; print('all preds', T()-t)
t=T(); wehr.lowess_fit(P[:,0], rbar); print('lowess', T()-t)
t=T(); wehr.run_cell.__globals__['_DATA'].update(cells=cells, stim=stim); 
schemes={'a':fold}; wehr.fit_window(X, rbar, ppred, schemes); print('fit_window 1 scheme', T()-t)
EOF
executed/asari-2009/.venv/bin/python $TMPDIR/tm.py
```

```
design 0.4460930539999026 (124125, 765)
gram 1.5189432630004376
atom grams 1.6025964979999117
eigh 0.06397199599996384
valid preds x10 0.2818829560001177
all preds 0.12102417100049934
lowess 0.0491227530001197
fit_window 1 scheme 3.17548437700043
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('make_nb.py').read()
s=s.replace('SCHEMES = ["contig/all", "stim/all", "contig/late", "stim/late"]','SCHEMES = ["contig/all", "stim/all", "contig/late"]')
old='''Readings run (all combinations, 8 in all, each read on validation and on training data):
spectrogram window 10-ms or 20-ms Hann (criterion); folds as 10 contiguous blocks of the
concatenated stimuli (`STRFanalysis.m`) or by stimulus (stimulus i in fold i mod 10, fewer folds if a
cell has fewer than 10 stimuli); bins scored from stimulus onset with the pre-onset history set to the
stimulus mean ("all"), or only bins at least 4052 ms after onset so that no window reaches before
onset ("late"; `STRFanalysis.m` also drops the first window length of each stimulus, there for each
window separately; here the same bins for every window so windows stay comparable).'''
new='''Readings run (6 in all, each read on validation and on training data): spectrogram window 10-ms or
20-ms Hann (criterion), crossed with three fold schemes: 10 contiguous blocks of the concatenated
stimuli (`STRFanalysis.m`) scoring every bin from stimulus onset with the pre-onset history set to the
stimulus mean ("contig/all"); folds by stimulus (stimulus i in fold i mod 10, fewer folds if a cell
has fewer than 10 stimuli), all bins ("stim/all"); and contiguous blocks over only the bins at least
4052 ms after onset, so that no window reaches before onset ("contig/late"; `STRFanalysis.m` also
drops the first window length of each stimulus, there for each window separately; here the same bins
for every window so windows stay comparable).'''
assert old in s
s=s.replace(old,new)
old='''            print(f"{model + ' ' + lab:>18s}", "".join(f"{v:7.3f}" for v in m), f"  {m.max():.3f}")'''
new='''            print(f"{model + ' ' + lab:>18s}", "".join(f"{v:7.3f}" for v in m), f"  {m.max():.3f}")
print()
print("Median over cells (robustness check, does not decide)")
for name in READINGS:
    print(name)
    for model in ("strf", "ln"):
        for col, lab in ((1, "valid"), (0, "train")):
            m = np.median(arr(name, model, col), 0)
            print(f"{model + ' ' + lab:>18s}", "".join(f"{v:7.3f}" for v in m), f"  {m.max():.3f}")'''
s=s.replace(old,new)
s=s.replace('''    for model in ("strf", "ln", "ln_nonrobust"):''','''    for model in (("strf", "ln", "ln_nonrobust") if name.endswith("contig/all") else ("strf", "ln")):''')
open('make_nb.py','w').write(s)
EOF
cd entries/asari-2009; executed/asari-2009/.venv/bin/python $TMPDIR/make_nb.py && date -u && executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARNING | tail -2; date -u
```

```
Thu Nov 19 05:21:01 UTC 2026
[NbConvertApp] Converting notebook strf_wehr.ipynb to notebook
[NbConvertApp] Writing 142845 bytes to /tmp/claude-1001/strf_wehr.ipynb
Thu Nov 19 05:32:18 UTC 2026
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import json;nb=json.load(open('strf_wehr.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code' or i<5: continue
  for o in c.get('outputs',[]):
    if 'text' in o: print(f'--- cell {i}'); print(''.join(o['text'])[:14000])
    elif o.get('output_type')=='error': print('ERR', o['ename'], o['evalue'])
" | grep -v "^  20"
```

```
--- cell 5
fits: 624 s (2 processes, 1 BLAS thread each)

--- cell 6
cells: 16
folds per cell (by-stimulus readings): {'20020508-mw-003': 10, '20020530-mw-001': 7, '20020602-mw-001': 5, '20020604-mw-001': 9, '20020604-mw-002': 3, '20020604-mw-003': 8, '20020605-mw-002': 5, '20020605-mw-003': 3, '20020608-mw-001': 6, '20020608-mw-002': 10, '20030401-mw-001': 10, '20030403-mw-001': 10, '20030404-mw-002': 10, '20030407-mw-001': 10, '20030407-mw-002': 7, '20030410-mw-001': 10}
bins per cell, all / late (>= 4052 ms after onset): {'20020508-mw-003': (45437, 34294), '20020530-mw-001': (26250, 19159), '20020602-mw-001': (18750, 13685), '20020604-mw-001': (33750, 24633), '20020604-mw-002': (11250, 8211), '20020604-mw-003': (30000, 21896), '20020605-mw-002': (18750, 13685), '20020605-mw-003': (11250, 8211), '20020608-mw-001': (22500, 16422), '20020608-mw-002': (37500, 27370), '20030401-mw-001': (124125, 105891), '20030403-mw-001': (124125, 105891), '20030404-mw-002': (78625, 67482), '20030407-mw-001': (124125, 105891), '20030407-mw-002': (48250, 41159), '20030410-mw-001': (206500, 176110)}
predictable power (Eq. 52) / power of the trial mean, per cell : {'20020508-mw-003': 0.965, '20020530-mw-001': 0.856, '20020602-mw-001': 0.555, '20020604-mw-001': 0.919, '20020604-mw-002': 0.896, '20020604-mw-003': 0.939, '20020605-mw-002': 0.836, '20020605-mw-003': 0.95, '20020608-mw-001': 0.973, '20020608-mw-002': 0.962, '20030401-mw-001': 0.733, '20030403-mw-001': 0.707, '20030404-mw-002': 0.72, '20030407-mw-001': 0.699, '20030407-mw-002': 0.629, '20030410-mw-001': 0.74}

Mean over cells of model performance (Eq. 53)
 window ms     180    324    548    884   1364   2004   2772   3540   4052    max
hann10/contig/all
        strf valid   0.115  0.133  0.143  0.147  0.147  0.148  0.145  0.146  0.147   0.148
        strf train   0.173  0.213  0.240  0.247  0.249  0.254  0.247  0.247  0.249   0.254
          ln valid   0.015 -0.019  0.040  0.041  0.022  0.033  0.038  0.033  0.036   0.041
    
[... 150 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('make_nb.py').read()
s=s.replace('''print(f"total time {time.time() - T0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")''','''print(f"total time {time.time() - T0:.0f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB "
      f"(this process), {resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6:.2f} GB (largest worker)")''')
concl = '''**Result: not reproduced under the criterion. The validation (lower) estimate is low at every
window in every reading that scores all bins, but in each of those readings the paired Wilcoxon test
finds that the STRF model improves from 180 ms to 4052 ms.**

Cells: 16 Wehr cells with at least two trials of a natural sound (Eq. 52 needs repeats); the paper's
20 cells are not marked in the files, and the 9 cells whose sounds were all presented once are left
out. Under the four readings that score every bin (10-ms or 20-ms Hann window, contiguous folds or
folds by stimulus), the mean validation performance is at most 0.148 for STRF and at most 0.111 for
LN at every window, both below 0.22. Training (upper) estimates reach 0.245 to 0.268 for STRF and
0.281 to 0.311 for LN, above 0.22, so the 20% bound holds only when read as the validation estimate.

The windows do matter. With 10-ms Hann and contiguous folds the mean STRF validation performance goes
from 0.115 at 180 ms to 0.147 at 4052 ms (0.143 by 548 ms, then flat), and the one-sided Wilcoxon
p-value for STRF is 0.0026; it is 0.0011, 0.037 and 0.029 in the other three such readings. For LN,
p is 0.017 and 0.015 with contiguous folds and 0.11 and 0.25 with folds by stimulus. The Friedman
variant (does not decide) is mixed: STRF p 0.016 to 0.31, LN p 0.0011 to 0.40.

Scoring only bins at least 4052 ms after onset ("contig/late") removes the significant change
(STRF p 0.065 and 0.052, LN p 0.14 and 0.12), but there the mean is not a usable summary: one cell,
20020602-mw-001, reaches 14.7 at 4052 ms because a validation fold has almost no predictable power,
which drives the mean to 1.26 (medians at most 0.195), so that reading fails the 0.22 bound.

The LN model is slightly better than STRF on training data (gain +0.013 to +0.049 across readings
and windows) but worse on validation data (gain -0.025 to -0.34): the robust lowess fitted to
in-sample predictions does not carry over to held-out folds; without the robustness iterations
(diagnostic) the LN validation mean is still at most 0.043 with contiguous folds. The ridge value hit
the grid edge in 9 or 10 of 144 fits in each all-bins reading, all at the strongest ridge (cell
20020608-mw-001 at every window, whose validation performance stays near zero); none of these fits
failed and no cell was dropped.'''
s=s.replace('''md("""
**Result: PLACEHOLDER**
""", tags=["conclusion"])''','md("""\n'+concl+'\n""", tags=["conclusion"])')
open('make_nb.py','w').write(s)
EOF
grep -n "PLACEHOLDER" make_nb.py; cd entries/asari-2009; executed/asari-2009/.venv/bin/python $TMPDIR/make_nb.py && date -u
```

```
Thu Nov 19 05:33:03 UTC 2026
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('make_nb.py').read()
anchor='''code("""
print("Ridge value chosen'''
add='''code("""
c = "20020602-mw-001"
Sc, rbar, ppred, sid, rws = W.prepare(CELLS[c], STIM, 10)
late = np.concatenate([np.arange(s["R"].shape[1]) >= W.PAD for s in CELLS[c]])
fl = np.full(len(rws), -1); fl[late] = W.folds_contiguous(int(late.sum()))
print(f"{c}, reading hann10/contig/late, 4052 ms: per validation fold")
r = RES["hann10/contig/late"][c][8]
for f in range(10):
    v = fl == f
    print(f"  fold {f}: predictable power (sum of Eq. 52 over bins) {ppred[v].sum():9.1f}, "
          f"power of trial mean {np.sum(rbar[v] ** 2):9.1f}, STRF validation {r['strf'][f, 1]:8.3f}")
del Sc
""", tags=[CL])

'''
s=s.replace(anchor, add+anchor)
s=s.replace('''The ridge value hit
the grid edge in 9 or 10 of 144 fits in each all-bins reading, all at the strongest ridge (cell
20020608-mw-001 at every window, whose validation performance stays near zero); none of these fits
failed and no cell was dropped.''','''The ridge value hit
the grid edge in 9 or 10 of 144 fits in each all-bins reading, all at the strongest ridge (with
10-ms Hann and contiguous folds these are cell 20020608-mw-001 at every window, whose validation
performance stays near zero), and in 24 or 25 fits in the "late" readings, at both ends; no fit
gave a non-finite value and no cell was dropped.''')
s=s.replace('''because a validation fold has almost no predictable power,''','''because its folds' predictable power is small and in some folds near zero (printed per fold),''')
open('make_nb.py','w').write(s)
EOF
cd entries/asari-2009; executed/asari-2009/.venv/bin/python $TMPDIR/make_nb.py && date -u && executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARNING | tail -2; date -u
```

```
Thu Nov 19 05:33:19 UTC 2026
[NbConvertApp] Converting notebook strf_wehr.ipynb to notebook
[NbConvertApp] Writing 148376 bytes to /tmp/claude-1001/strf_wehr.ipynb
Thu Nov 19 05:45:02 UTC 2026
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import json;nb=json.load(open('strf_wehr.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code': continue
  for o in c.get('outputs',[]):
    if o.get('output_type')=='error': print('ERR', i, o['ename'], o['evalue'])
print(''.join(nb['cells'][5]['outputs'][0]['text']))
for i in (8,):
  print(''.join(nb['cells'][i]['outputs'][0]['text']))
print(''.join(nb['cells'][-1]['outputs'][0]['text']))
t=''.join(nb['cells'][10]['outputs'][0]['text']); print(t[:1500])
"
```

```
fits: 620 s (2 processes, 1 BLAS thread each)

20020602-mw-001, reading hann10/contig/late, 4052 ms: per validation fold
  fold 0: predictable power (sum of Eq. 52 over bins)     164.4, power of trial mean     216.6, STRF validation  -14.029
  fold 1: predictable power (sum of Eq. 52 over bins)     -17.1, power of trial mean      43.6, STRF validation   80.739
  fold 2: predictable power (sum of Eq. 52 over bins)     -11.1, power of trial mean     104.1, STRF validation   43.747
  fold 3: predictable power (sum of Eq. 52 over bins)     -68.1, power of trial mean     114.3, STRF validation    1.277
  fold 4: predictable power (sum of Eq. 52 over bins)     158.9, power of trial mean     307.0, STRF validation   -3.796
  fold 5: predictable power (sum of Eq. 52 over bins)    -118.1, power of trial mean     207.9, STRF validation    5.574
  fold 6: predictable power (sum of Eq. 52 over bins)     -65.4, power of trial mean     180.9, STRF validation   21.599
  fold 7: predictable power (sum of Eq. 52 over bins)     257.7, power of trial mean     540.7, STRF validation   -1.072
  fold 8: predictable power (sum of Eq. 52 over bins)     -16.8, power of trial mean     209.4, STRF validation   20.260
  fold 9: predictable power (sum of Eq. 52 over bins)      95.5, power of trial mean     427.2, STRF validation   -7.499

total time 701 s; peak RSS 0.70 GB (this process), 2.68 GB (largest worker)

Paired Wilcoxon signed-rank, validation performance at 4052 ms vs 180 ms, one-sided (improvement)
and Friedman test over the nine windows (variant, does not decide)
hann10/contig/all  strf: median diff +0.0234, cells improved 11/16, W=120, p(one-sided)=0.0026, p(two-sided)=0.0052; Friedman chi2=14.2, p=0.0767
hann10/contig/all  ln  : median diff +0.0264, cells improved 11/16, W=109, p(one-sided)=0.0168, p(two-sided)=0.0335; Friedman chi2=20.4, p=0.0088
[... 8 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('make_nb.py').read()
old='tasks = sorted([(c, w) for c in cellnames for w in (10, 20)], key=lambda t: -size[t[0]])'
assert old in s
s=s.replace(old,'''# largest cells first within each spectrogram window, so the two largest fits never run together
tasks = sorted([(c, w) for c in cellnames for w in (10, 20)], key=lambda t: (t[1], -size[t[0]]))''')
old="because its folds' predictable power is small and in some folds near zero (printed per fold),"
assert old in s
s=s.replace(old,"because the predictable power (Eq. 52) summed over a validation fold is negative in 6 of its 10 folds (printed per fold),")
s=s.replace('''print(f"fits: {time.time() - t:.0f} s (2 processes, 1 BLAS thread each)")''','''print(f"fits: {time.time() - t:.0f} s (2 processes, 1 BLAS thread each); "
      f"largest worker peak RSS {resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6:.2f} GB")''')
open('make_nb.py','w').write(s)
EOF
cd entries/asari-2009; executed/asari-2009/.venv/bin/python $TMPDIR/make_nb.py && date -u && /usr/bin/time -v executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute strf_wehr.ipynb --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARNING | grep -i "maximum resident\|elapsed\|Writing"; date -u
```

```
Thu Nov 19 05:45:27 UTC 2026
[NbConvertApp] Writing 148667 bytes to /tmp/claude-1001/strf_wehr.ipynb
	Elapsed (wall clock) time (h:mm:ss or m:ss): 11:16.37
	Maximum resident set size (kbytes): 2545692
Thu Nov 19 05:56:44 UTC 2026
```

**Subagent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import json;nb=json.load(open('strf_wehr.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code': continue
  for o in c.get('outputs',[]):
    if o.get('output_type')=='error': print('ERR', i, o['ename'], o['evalue'])
print(''.join(nb['cells'][5]['outputs'][0]['text']))
print(''.join(nb['cells'][-1]['outputs'][0]['text']))
t=''.join(nb['cells'][6]['outputs'][0]['text']); i=t.index('Mean over'); print(t[i:i+700])
print([c['metadata'].get('tags') for c in nb['cells']])
"; ls entries/asari-2009/; python3 -c "
import json;nb=json.load(open('entries/asari-2009/strf_wehr.ipynb')); print(sum(len(c.get('outputs',[])) for c in nb['cells'] if c['cell_type']=='code'))"
```

```
fits: 622 s (2 processes, 1 BLAS thread each); largest worker peak RSS 2.55 GB

total time 674 s; peak RSS 0.60 GB (this process), 2.55 GB (largest worker)

Mean over cells of model performance (Eq. 53)
 window ms     180    324    548    884   1364   2004   2772   3540   4052    max
hann10/contig/all
        strf valid   0.115  0.133  0.143  0.147  0.147  0.148  0.145  0.146  0.147   0.148
        strf train   0.173  0.213  0.240  0.247  0.249  0.254  0.247  0.247  0.249   0.254
          ln valid   0.015 -0.019  0.040  0.041  0.022  0.033  0.038  0.033  0.036   0.041
          ln train   0.213  0.255  0.275  0.283  0.287  0.294  0.288  0.289  0.290   0.294
ln_nonrobust valid   0.031  0.027  0.039  0.038  0.030  0.037  0.040  0.032  0.030   0.040
ln_nonrobust train   0.304  0.342  0.358  0.364  0.368  0.374  0.370  0.370  0.372   0.374
hann10/s
[None, None, None, ['sanity'], None, ['claim:fig4-strf-performance-low'], ['claim:fig4-strf-performance-low'], ['claim:fig4-strf-performance-low'], ['claim:fig4-strf-performance-low'], ['claim:fig4-strf-performance-low'], ['claim:fig4-strf-performance-low'], ['claim:fig4-strf-performance-low'], ['claim:fig4-strf-performance-low'], ['conclusion'], None]
README.md
__pycache__
asari.py
entry.yaml
reproduce_asari_2009.ipynb
[... 5 more lines not kept]
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; rm -f __pycache__/wehr.*.pyc; ls __pycache__; sed -n 40,85p wehr.py; grep -n "—\|rather" wehr.py $TMPDIR/make_nb.py | head
```

```
asari.cpython-313.pyc
  the evoked response is the trigger's duration from the trigger time, natural
  sounds are every stimulus other than "tuning curve", "silence" and
  "white noise"; the stimulus gets a Hann ramp of ``param.ramp`` ms at both
  ends (``MakeRamp.m``);
- ``logspectrogram.m``: frequencies 400 * 2^(k/3) Hz, the DFT evaluated at
  each centre frequency (no band integration).

Assumptions (each also stated in the notebook):

- cells: the paper's 20 cells cannot be identified from the files; we use every
  Wehr cell with at least two trials of the same natural sound, since Eq. 52
  needs m >= 2 (``select_cells``), and only those stimuli;
- 17 frequencies 400 * 2^(k/3) Hz, k = 0..16 (0.40 to 16.1 kHz): the code's
  rule with fmax = 22.1 kHz gives 18; the paper says 17 bins;
- response sampled in 4-ms bins (the finest time bin; mean of 16 samples of the
  4-kHz trace), the spectrogram computed every 4 ms with the window centred on
  the bin, the coarser history bins the mean of the 4-ms frames they cover;
- history before stimulus onset is set to the stimulus mean (zero after
  centring), so every window is scored on the same time bins;
[... 27 more lines not kept]
```

**Subagent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('wehr.py').read()
s=s.replace('''- history before stimulus onset is set to the stimulus mean (zero after
  centring), so every window is scored on the same time bins;''','''- history before stimulus onset is set to the stimulus mean (zero after
  centring), so every window is scored on the same time bins ("all"); a second
  scoring keeps only bins at least 4052 ms after onset ("late"); folds by
  stimulus are a reading of the criterion;
- spectrogram window: Hann, 10 or 20 ms (the criterion's readings);
  ``logspectrogram.m`` uses a Hamming window of twice the time bin;''')
s=s.replace('''- per-fold performance averaged over folds as ``ViewSTRF.m`` does
  (``mean(strf.performance.linear, 2)``);''','''- (authors' code, not an assumption) per-fold performance averaged over folds
  as ``ViewSTRF.m`` does (``mean(strf.performance.linear, 2)``);''')
open('wehr.py','w').write(s)
EOF
executed/asari-2009/.venv/bin/python -c "import ast;ast.parse(open('entries/asari-2009/wehr.py').read())" && echo ok; date -u
```

```
ok
Thu Nov 19 05:57:05 UTC 2026
```

**Subagent**

By the criterion the claim is **not_reproduced**. Validation performance stays below 0.15 at every window, but the paired Wilcoxon test finds a significant STRF improvement from 180 ms to 4052 ms in every reading where that level bound holds. The notebook ran end to end in 674 s; I finished at 05:57 UTC.

**Files.** `entries/asari-2009/wehr.py` (helper) and `entries/asari-2009/strf_wehr.ipynb`, saved without outputs. No other file was touched. The directory is not a git repository, so nothing was committed.

**Cells (16, not 20).** The paper's 20 cells are not marked anywhere in the files. Both experiments in `wehr/Summary.mat` cite Machens et al. (2004):
- 10 cells from 2002, with 3 to 10 natural sounds repeated 5 to 25 times each.
- 15 cells from 2003, with natural sound streams presented once or twice.

Eq. 52 needs at least two trials, so I kept every cell with two or more trials of some natural sound, and only those stimuli. That gives 16 cells: the 10 from 2002 plus 6 from 2003. The 9 cells whose sounds were all presented once were left out. This choice is an assumption.

**Method choices and sources**
- **From the paper or the criterion:** Eqs. 46 to 53; time bins of 2^k ms split as listed, giving the nine windows and 765 parameters; ridge regression (Eq. 50) with 10-fold cross-validation; robust lowess with 5% span and 5 iterations, fitted on training and applied to validation; performance from Eq. 52/53 on training (upper) and validation (lower) data, averaged over cells.
- **From the authors' code (`wehr/Tools/STRFanalysis.m`):**
  - per-trial mean subtraction, fitting to the trial-averaged response, spectrogram centred per frequency within each stimulus;
  - 10 contiguous equal folds over the concatenated stimuli;
  - one ridge value for all folds, chosen by the best mean linear validation score, with the LN model using that same filter;
  - per-fold Eq. 53 as in its `LNperformance` function.
- **Also from the authors' code:**
  - `ViewSTRF.m`: averaging over folds;
  - `ViewResponse.m` / `GetEvoked.m`: 10-ms median filter, evoked period = trigger duration, which stimuli count as natural sounds;
  - `MakeRamp.m`: Hann ramp on the stimulus;
  - `logspectrogram.m`: DFT evaluated at 400·2^(k/3) Hz.
- **Assumptions:**
  - 17 frequencies, k = 0..16 (0.40 to 16.1 kHz). The code's own rule would give 18 bins up to 20.3 kHz.
  - Response in 4-ms bins, with spectrogram frames every 4 ms.
  - Spectrogram history before stimulus onset set to the stimulus mean.
  - Ridge grid of 33 values from 10^-6 to 10^2 times the mean eigenvalue.
  - Lowess convention: one fit plus five robustness iterations, evaluated on a 100-point grid.
- **Seeds:** no result uses random draws, so no generator is used. The protocol seed is printed.

**Readings run (6, each read on validation and on training data).** Hann window of 10 or 20 ms, crossed with three fold schemes:
- **contig/all:** contiguous folds, every bin scored from stimulus onset.
- **stim/all:** folds by stimulus, every bin scored.
- **contig/late:** contiguous folds, scoring only bins at least 4052 ms after onset (my addition).

Response sampling was 4-ms bins only. Wehr's traces are sampled at 4 kHz, so the "10-kHz trace" reading does not exist.

**Key numbers (10-ms Hann, contig/all)**

| Window (ms) | 180 | 324 | 548 | 884 | 1364 | 2004 | 2772 | 3540 | 4052 |
|---|---|---|---|---|---|---|---|---|---|
| STRF validation | 0.115 | 0.133 | 0.143 | 0.147 | 0.147 | 0.148 | 0.145 | 0.146 | 0.147 |
| STRF training | 0.173 | 0.213 | 0.240 | 0.247 | 0.249 | 0.254 | 0.247 | 0.247 | 0.249 |
| LN validation | 0.015 | -0.019 | 0.040 | 0.041 | 0.022 | 0.033 | 0.038 | 0.033 | 0.036 |
| LN training | 0.213 | 0.255 | 0.275 | 0.283 | 0.287 | 0.294 | 0.288 | 0.289 | 0.290 |

**Level bound across the four "all" readings**
- Mean validation is at most 0.148 for STRF and at most 0.111 for LN at every window, so the 0.22 bound holds.
- Mean training reaches 0.245 to 0.268 for STRF and 0.281 to 0.311 for LN, so the bound fails if the 20% is read as the training estimate.

**Wilcoxon, one-sided, validation at 4052 ms vs 180 ms**

| Reading | STRF p | LN p |
|---|---|---|
| 10-ms contig/all | 0.0026 | 0.017 |
| 10-ms stim/all | 0.037 | 0.11 |
| 20-ms contig/all | 0.0011 | 0.015 |
| 20-ms stim/all | 0.029 | 0.25 |
| 10-ms contig/late | 0.065 | 0.14 |
| 20-ms contig/late | 0.052 | 0.12 |

- Most of the STRF gain comes by 548 ms; performance is flat after that.
- The contig/late readings show no significant improvement, but they fail the level bound: the mean reaches 1.26 and 1.14. That comes from cell 20020602-mw-001, which scores 14.7 because the predictable power summed over a validation fold is negative in 6 of its 10 folds. Medians in those readings are at most 0.195.
- The Friedman variant is mixed: STRF p from 0.016 to 0.31, LN p from 0.0011 to 0.40.

**LN gain.** LN does slightly better than STRF on training data (+0.013 to +0.049) but worse on validation data (-0.025 to -0.34). This contradicts the paper's "slightly better" for held-out data. Without the robustness iterations, LN validation is still at most 0.043 with contiguous folds.

**Ridge choice.** The chosen value hit the grid edge in 9 or 10 of 144 fits per "all" reading, all at the strongest ridge. With 10-ms Hann and contiguous folds these are all cell 20020608-mw-001, at every window, whose validation score is about zero. In the "late" readings, 24 or 25 fits hit an edge, at both ends. No fit failed and no cell was dropped.

**Run cost.** 674 to 701 s per run. Peak memory was 0.6 GB in the main process and 2.55 GB in the largest of the two worker processes, each using one BLAS thread. The largest jobs are ordered so the two biggest never run together, which keeps the combined total at or under about 5 GB (an estimate; I measured each process separately).

**Data set findings (undocumented or wrong)**
- Wehr's traces are sampled at 4 kHz, not 10 kHz, and stimuli at 97,656 Hz.
- `wehr/Results` has 25 cell folders, not 26.
- 9 of the 25 cells have only single-trial natural sounds, which Eq. 52 cannot use.
- Nothing in the files marks which cells make up the paper's 20.
- Cell 20020605-mw-002 contains a trace reaching -221.9 mV, which looks like an artefact.
- `fragments/11.mat` is 31.75 s long; the other fragments are 15 s.
- `logspectrogram.m` with the defaults in `STRFanalysis.m` gives 18 frequency bins, not the paper's 17, and uses a Hamming window of twice the time bin, not Hann.
- The CRCNS description page does not mention the `wehr/Tools` code at all.

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd entries/asari-2009; ls; PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import pickle, os, numpy as np
M=pickle.load(open(os.environ['TMPDIR']+'/synmeta.pkl','rb'))
import collections
c=collections.Counter()
for d in M:
    for l in d['notes']:
        if 'variant' in l.lower() and ':' in l: c[l.strip()]+=1
print(c)
d=[d for d in M if d['triggers'] and d['triggers'][0]['type']=='dmr' and any('frequency' in s['description'] for s in d['stim'])][0]
for i,s in enumerate(d['stim'],1):
    print(i,s['description'][:50],{k:(np.round(np.asarray(v,float),1).tolist() if np.asarray(v).dtype.kind in 'fiu' else '..') for k,v in s['param'].items()})
print(d['seqs'])
EOF
```

```
Thu Nov 19 05:57:48 UTC 2026
README.md
__pycache__
asari.py
entry.yaml
reproduce_asari_2009.ipynb
requirements.in
requirements.lock.txt
strf_wehr.ipynb
wehr.py
Counter({'2-5,8: amplitude variants': 6, '6-10: frequency variants': 6, '8,11-14: amplitude-modulation variants': 6, '8,15-18: frequency-modulation variants': 6})
1 neotropical-mammals-2 Track 06 (Buffy-headed marmo {'ramp': 5.0, 'duration': 5475.0, 'sf': 97656.0}
2 DMR; frequency variants {'ramp': 5.0, 'sf': 97656.0, 'tempmod': [-20.0, 19.8, 8.4, 0.5, -8.7, -19.4, 4.9, -19.0, -15.3, -4.6, 14.3, 8.1, -18.9, 19.3, 0.7, 19.8], 'specmod': [1.4, 1.1, 1.1, 0.2, 1.2, 1.2, 1.5, 1.1, 0.4, 0.3, 0.3, 0.2, 0.3, 0.8, 1.0, 0.8, 0.7, 0.4, 1.2, 0.2, 1.1, 1.2, 0.2, 0.4, 0.1, 0.6, 1.5, 0.2, 1.4, 1.0, 0.6], 'SFtemp': 3.0, 'SFspec': 6.0, 'envphase': 3.4, 'sinphase': [0.4, 5.6, 4.3, 1.7, 5.7, 4.2, 2.5, 1.0, 0.2, 2.8, 4.7, 2.2, 1.6, 0.2, 5.1, 1.8, 6.2, 1.5, 6.2, 0.8, 2.5, 2.9, 4.7, 5.7, 2.3, 6.1, 2.9, 2.4, 6.2, 1.5, 2.6, 4.9, 5.5, 3.3, 3.5, 4.6, 3.7, 4.8, 3.6, 5.0, 3.9, 1.6, 5.6, 0.2, 3.1, 2.2, 2.6, 2.9, 1.9, 0.5, 3.2, 3.3, 5.8, 6.0, 4.4, 2.4, 2.6, 0.7, 5.3, 3.9, 3.5, 1.8, 1.1, 5.6, 3.4, 0.9, 4.5, 5.2, 0.1, 0.5, 5.4, 2.7, 1.5, 5.2, 4.1, 1.8, 5.8, 0.9, 0.8, 5.3, 0.3, 2.2, 5.7, 0.7, 0.4, 0.7, 5.6, 6.1, 2.1, 0.4, 2.9, 5.8, 3.2, 3.9, 5.2, 0.5, 6.1, 1.9, 4.4, 3.6, 2.3, 2.7, 0.8, 6.1, 3.9, 2.8, 1.5, 0.3, 4.7, 4.2, 6.0, 4.4, 2.6, 2.7, 1.8, 4.0, 4.3, 6.2, 2.9, 0.8, 3.4, 3.2, 1.9, 5.0, 0.8, 5.6, 5.1, 0.4, 1.8], 'dx': 0.0, 'ff': [250.0, 1000.0], 'duration': 5000.0}
3 DMR; frequency variants {'ramp': 5.0, 'sf': 97656.0, 'tempmod': [-20.0, 19.8, 8.4, 0.5, -8.7, -19.4, 4.9, -19.0, -15.3, -4.6, 14.3, 8.1, -18.9, 19.3, 0.7, 19.8], 'specmod': [1.4, 1.1, 1.1, 0.2, 1.2, 1.2, 1.5, 1.1, 0.4, 0.3, 0.3, 0.2, 0.3, 0.8, 1.0, 0.8, 0.7, 0.4, 1.2, 0.2, 1.1, 1.2, 0.2, 0.4, 0.1, 0.6, 1.5, 0.2, 1.4, 1.0, 0.6], 'SFtemp': 3.0, 'SFspec': 6.0, 'envphase': 3.4, 'sinphase': [0.4, 5.6, 4.3, 1.7, 5.7, 4.2, 2.5, 1.0, 0.2, 2.8, 4.7, 2.2, 1.6, 0.2, 5.1, 1.8, 6.2, 1.5, 6
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; cp asari.py $TMPDIR/asari_orig.py; python3 - <<'EOF'
p='asari.py'; s=open(p).read()
old='''    st = d["stim"]
    out = {p: [] for p in PROPERTIES}
    typ = d["triggers"][0]["type"] if d["triggers"] else ""'''
new='''    st = d["stim"]
    out = {p: [] for p in PROPERTIES}
    typ = d["triggers"][0]["type"] if d["triggers"] else ""
    # The file's own notes list the variants of each property where they
    # give them ("2-5,8: amplitude variants"); they are used as given.
    named = {"amplitude": "amplitude", "frequency": "frequency",
             "amplitude-modulation": "AM", "frequency-modulation": "FM"}
    for line in d.get("notes", []):
        mm = re.match(r"\\s*([\\d,\\-\\s]+):\\s*([a-z\\-]+) variants", line)
        if mm and mm.group(2) in named:
            idx = set()
            for part in mm.group(1).split(","):
                a, _, b = part.strip().partition("-")
                idx |= set(range(int(a), int(b or a) + 1))
            out[named[mm.group(2)]].append(idx)
    if any(out.values()):
        return out'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
PY=executed/asari-2009/.venv/bin/python; $PY - <<'EOF'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from tab import *
d=[d for d in M if '20061022-ha4-001-002' in d['path']][0]
print(A.property_classes(d))
tabulate()
EOF
```

```
{'amplitude': [{2, 3, 4, 5, 8}], 'frequency': [{6, 7, 8, 9, 10}], 'AM': [{8, 11, 12, 13, 14}], 'FM': [{16, 17, 18, 8, 15}], 'higher-order': []}
('AM', 'NS') 82 24
('AM', 'synthetic') 14 2
('FM', 'NS') 82 24
('amplitude', 'NS') 54 19
('amplitude', 'dmr') 8 2
('amplitude', 'torc') 42 9
('frequency', 'NS') 56 20
('frequency', 'dmr') 20 5
('frequency', 'torc') 44 9
('higher-order', 'NS') 164 26
('higher-order', 'pinknoise') 190 26
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
p='asari.py'; s=open(p).read()
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt, (old, s.count(old)); s=s.replace(old,new)
rep('''        d["unit"] = str(r.unit)
''','''        d["unit"] = str(r.unit)
        d["scale"] = float(r.scale)
''')
# trial bootstrap helper after frac_power
rep('''def bin_mean(y: np.ndarray, k: int = 10) -> np.ndarray:''','''def trial_boot(X: np.ndarray, rngs: list, B: int = 200, tmax: float = 4.0,
               step: int = 10, bin_ms: int = 50):
    """Fig. 8C, the reading where a sample is a trial: ``B`` resamplings of
    the trials of each context with replacement (Methods, Eq. 21 and the
    paragraph after it, "200 resamplings"), each giving the stimulus-related
    and context-independent power of ``frac_power``. Traces are centred over
    the whole probe first (FracPow), then taken every ``step`` samples (1 kHz)
    up to ``tmax`` s and averaged in ``bin_ms`` bins (standard choices for an
    area over 4 s). Returns two arrays (len(rngs), B, bins)."""
    n, m, T = X.shape
    Y = X.astype(np.float64)
    Y = Y - Y.mean(axis=2, keepdims=True)
    Y = Y[:, :, :min(T, int(tmax * SF)):step]
    k = bin_ms * SF // 1000 // step
    nb = Y.shape[2] // k
    P = np.empty((len(rngs), B, nb), np.float32)
    I = np.empty((len(rngs), B, nb), np.float32)
    rows = np.arange(n)[:, None]
    for si, rng in enumerate(rngs):
        idx = rng.integers(0, m, size=(B, n, m))
        for b in range(B):
            Z = Y[rows, idx[b]]
            mu = Z.mean(axis=1)
            pred = ((m * mu ** 2 - (Z ** 2).mean(axis=1)) / (m - 1)).mean(axis=0)
            inv = (n * mu.mean(axis=0) ** 2 - (mu ** 2).mean(axis=0)) / (n - 1)
            P[si, b] = pred[:nb * k].reshape(nb, k).mean(axis=1)
            I[si, b] = inv[:nb * k].reshape(nb, k).mean(axis=1)
    return P, I


def tie_fraction(X: np.ndarray) -> float:
    """Mean over time points of the fraction of the n*m values at that point
    that equal another value (the Kruskal-Wallis ranks break such ties by
    trial order, as CxtDep.m does)."""
    n, m, T = X.shape
    S = np.sort(X.reshape(n * m, T), axis=0)
    eq = S[1:] == S[:-1]
    tied = np.zeros_like(S, dtype=bool)
    tied[1:] |= eq
    tied[:-1] |= eq
    return float(tied.mean())


def bin_mean(y: np.ndarray, k: int = 10) -> np.ndarray:''')
rep('''def reduce_wholecell(path: str, kind: str, seeds: list[int], fidx: int,
                     nshuffle: int = 1000, blank_s: float = 2.5) -> dict:''','''def reduce_wholecell(path: str, kind: str, seeds: list[int], fidx: int,
                     nshuffle: int = 1000, blank_s: float = 2.5,
                     boot_seeds: list[int] | None = None) -> dict:''')
rep('''    of the main reading (the first is also used for the variants)."""''','''    of the main reading (the first is also used for the variants).
    ``boot_seeds``: the seeds of fig8c-relative-effects, for the trial
    resampling of ``trial_boot``."""''')
rep('''               age=d["age"], vrange=(float(np.percentile(x, 1)), float(np.percentile(x, 99))))''','''               age=d["age"], vrange=(float(np.percentile(x, 1)), float(np.percentile(x, 99))),
               scale=d["scale"])''')
rep('''    out["stim"] = [s["description"] for s in d["stim"]]''','''    out["stim"] = [s["description"] for s in d["stim"]]
    out["stim_ff"] = [np.atleast_1d(s["param"]["ff"]).astype(float).tolist()
                      if "ff" in s["param"] else None for s in d["stim"]]
    out["notes"] = d["notes"]
    out["rtype"] = d["rtype"]
    out["ttype"] = d["triggers"][0]["type"] if d["triggers"] else ""
    boot = (lambda X, *keys: trial_boot(X, [_seed(s, fidx, *keys) for s in boot_seeds])) \\
        if boot_seeds else None''')
rep('''            rec["corr_pair_sd"] = float(np.std(pa))''','''            rec["corr_pair_sd"] = float(np.std(pa))
            rec["ties"] = tie_fraction(X)
            if boot:
                rec["boot"] = boot(X, probe, 2)''')
rep('''                rec["ns"] = dict(sig=_intervals(sig), noise=bin_mean(noise).astype(np.float32),
                                 pred=bin_mean(pn), inv=bin_mean(iv), n=len(keep))''','''                rec["ns"] = dict(sig=_intervals(sig), noise=bin_mean(noise).astype(np.float32),
                                 pred=bin_mean(pn), inv=bin_mean(iv), n=len(keep))
                if boot:
                    rec["ns"]["boot"] = boot(Xn, probe, 3)''')
rep('''            rec["pred"], rec["inv"] = bin_mean(pred), bin_mean(inv)
            tests.append(rec)''','''            rec["pred"], rec["inv"] = bin_mean(pred), bin_mean(inv)
            if boot:
                rec["boot"] = boot(X, t["probe"], ti, 2)
            tests.append(rec)''')
# MGB MAD detector
rep('''    thr = 2 / 3 * abs(xf[i])
    del xf
    spk = {"code": extract_spikes(raw),
           "half": extract_spikes(raw, threshold=thr / 2)}
    out["thr_code"] = float(thr)''','''    thr = 2 / 3 * abs(xf[i])
    # noise-based threshold (Quiroga et al. 2004): 4 SD of the noise, the SD
    # estimated as median(|x|) / 0.6745 of the filtered trace
    thr_mad = 4 * float(np.median(np.abs(xf))) / 0.6745
    del xf
    spk = {"code": extract_spikes(raw),
           "half": extract_spikes(raw, threshold=thr / 2),
           "mad": extract_spikes(raw, threshold=thr_mad)}
    out["thr_code"] = float(thr)
    out["thr_mad"] = thr_mad''')
open(p,'w').write(s)
EOF
grep -n "Standard choices\|Assumptions, each" asari.py
```

```
35:- Standard choices that cannot change a result: the median filter's exact
39:- Assumptions, each also stated in the notebook and the record: the A1 spike
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
p='asari.py'; s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old; s=s.replace(old,new)
rep('''- Assumptions, each also stated in the notebook and the record: the A1 spike
  detector (the code extracts whole-cell spikes by hand), see ``a1_spikes``.''','''- Assumptions, each also stated in the notebook and the record: the A1 spike
  detector (the code extracts whole-cell spikes by hand), see ``a1_spikes``;
  the sets of conditioning stimuli of Figure 8 where the file's notes do not
  list them, see ``property_classes``. A variant MGB detector with a
  noise-based threshold (4 SD, the SD from the median absolute value;
  Quiroga et al. 2004, the field's usual choice) is run beside the authors'
  detector, see ``reduce_mgb``.''')
rep('''    value), to show how much the threshold matters."""''','''    value), to show how much the threshold matters, and with a threshold of
    4 noise SDs of the filtered trace (SD = median(|x|) / 0.6745)."""''')
rep('''    only. TORC and DMR ensembles are labelled in their descriptions''','''    only. Where the file's notes list the variants of each property (the six
    files of natural probes after MHT variants), those lists are used. TORC
    and DMR ensembles are labelled in their descriptions''')
open(p,'w').write(s)
EOF
PY=executed/asari-2009/.venv/bin/python; cat > $TMPDIR/t1.py <<'EOF'
import sys, time, resource, pickle, os
sys.path.insert(0, 'entries/asari-2009')
import asari as A
F = pickle.load(open(os.environ['TMPDIR']+'/F.pkl','rb'))
t=time.time(); r=A.reduce_mgb(F['mgb'][0]); print('mgb', time.time()-t, r['thr_code'], r['thr_mad'], r['spk_code'], r['spk_mad'])
t=time.time(); r=A.reduce_wholecell(F['synthetic'][0], 'synthetic', [1,2,3,4,5], 0, boot_seeds=[7,8,9,10,11]); print('syn', time.time()-t, len(r['tests']), r['ttype'], r['tests'][0]['boot'][0].shape if r['tests'] else None)
t=time.time(); r=A.reduce_wholecell(F['natural'][0], 'natural', [1,2,3,4,5], 0, boot_seeds=[7,8,9,10,11]); print('nat', time.time()-t, len(r['tests']), r['scale'], [round(x['ties'],4) for x in r['tests']], r['tests'][0]['boot'][0].shape)
print('maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1024)
EOF
time $PY $TMPDIR/t1.py
```

```
mgb 3.785707950592041 4.905666648479899 0.08777362938958695 {'silence': 0, 'sound': 375, 'silence_late': 0, 'n': 375} {'silence': 59, 'sound': 5131, 'silence_late': 47, 'n': 5190}
syn 14.106106758117676 4 synthetic (5, 200, 80)
nat 14.482715606689453 4 0.006103608758678569 [0.0249, 0.0223, 0.0243, 0.0224] (5, 200, 80)
maxrss MB 1006

real	0m33.273s
user	1m32.745s
sys	0m5.939s
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/cells; cd $TMPDIR/cells; cat > c05.py <<'EOF'
t = time.time()
SEEDS_NAT = five("fig3a-proportion-significant")
SEEDS_SYN = five("fig8a-significance-fits")
BOOT = five("fig8c-relative-effects")  # trial resampling of fig8c-relative-effects
NAT = A.run_many(A.reduce_wholecell, [(p, "natural", SEEDS_NAT, i, 1000, 2.5, BOOT) for i, p in enumerate(F["natural"])])
print("natural files", len(NAT), round(time.time() - t), "s")
t = time.time()
MGB = A.run_many(A.reduce_mgb, [(p,) for p in F["mgb"]])
print("MGB files", len(MGB), round(time.time() - t), "s")
t = time.time()
SYN = A.run_many(A.reduce_wholecell, [(p, "synthetic", SEEDS_SYN, i, 1000, 2.5, BOOT) for i, p in enumerate(F["synthetic"])])
print("synthetic files", len(SYN), round(time.time() - t), "s")
EOF
cat > c06add.py <<'EOF'
print("recording types (current clamp files):", collections.Counter(r["rtype"] for r in NAT + SYN))
print("trace scale (mV per integer step of the stored int16):", sorted({round(r["scale"], 6) for r in NAT + SYN}))
ties = np.array([t["ties"] for r in NAT for t in r["tests"]])
print(f"natural sound probes, fraction of values tied with another at the same time point: median {np.median(ties):.4f}, "
      f"range {ties.min():.4f} to {ties.max():.4f}")
# Files not used: experiment 4 of Summary.mat, and cell folders of the zips that Summary.mat does not list.
for p in F["other"]:
    d = A.load(p, trace=False)
    print("  experiment 4 file:", p.split("/")[-1], "|", d["rtype"], "|", d["description"][:60], "| trigger type",
          d["triggers"][0]["type"] if d["triggers"] else "none")
listed = {r["cell"] for r in sm}
inzip = collections.defaultdict(list)
for k in A.member_index():
    inzip[k.split("/")[1]].append(k)
print("cell folders in the results zips:", len(inzip), "; cells in Summary.mat:", len(listed),
      "; folders not listed:", sorted(set(inzip) - listed))
for c in sorted(set(inzip) - listed):
    for k in sorted(inzip[c]):
        d = A.load(k, trace=False)
        print("   ", k, "|", d["rtype"], "|", d["description"][:60], "| trigger type", d["triggers"][0]["type"] if d["triggers"] else "none")
EOF
cat > c10.py <<'EOF'
def probes(R, minrep, sub=None):
    out = []
    for r in R:
        if (r["rep"] or 0) < minrep:
            continue
        for t in r["tests"]:
            if sub == "ns" and "ns" not in t:
                continue
            out.append((r, t))
    return out
nat = probes(NAT, 4)
nat_ns = probes(NAT, 4, "ns")
print("A1 natural sound probes (silence counted):", len(nat), "in", len({r['cell'] for r, _ in nat}), "cells")
print("A1 natural sound probes (silence not counted):", len(nat_ns), "in", len({r['cell'] for r, _ in nat_ns}), "cells")
print("natural sound files with fewer than 4 effective repeats:", [r['path'] for r in NAT if (r['rep'] or 0) < 4])
mgb_pr = [(r, p) for r in MGB if (r["rep"] or 0) >= 10 for p in r["probes_code"]]
print("MGB probes (>= 10 trials):", len(mgb_pr), "in", len({r['cell'] for r, _ in mgb_pr}), "cells;",
      "MGB cells in the data set:", len(cells_of(MGB)))

# Figure 8 tests. 'class': each probe with each set of conditioning stimuli that differ in one property.
# 'probe': each probe once per property (significant at t when any of its sets is; power averaged over
# its sets; noise floor 1 - prod(1 - floor of each set)). 'table1': 'class' for AM and FM, 'probe' for
# amplitude, frequency and higher-order, the reading whose totals equal every column of Table 1.
syn = probes(SYN, 4)
def merge(group):
    rs, ts = zip(*group)
    if len(ts) == 1:
        return group[0]
    t0 = ts[0]
    return rs[0], dict(prop=t0["prop"], probe=t0["probe"], natural=t0["natural"], T=t0["T"], m=t0["m"],
                       contexts=sorted({c for t in ts for c in t["contexts"]}), n_sets=len(ts),
                       sig=sorted(iv for t in ts for iv in t["sig"]),
                       noise=[1 - np.prod([1 - t["noise"][i] for t in ts], axis=0) for i in range(5)],
                       pred=np.mean([t["pred"] for t in ts], axis=0), inv=np.mean([t["inv"] for t in ts], axis=0),
                       boot=tuple(np.mean([t["boot"][j] for t in ts], axis=0) for j in (0, 1)))
grp = collections.defaultdict(list)
for r, t in syn:
    grp[(r["path"], t["probe"], t["prop"])].append((r, t))
UNITS = {"class": syn, "probe": [merge(g) for g in grp.values()]}
UNITS["table1"] = [x for x in UNITS["class"] if x[1]["prop"] in ("AM", "FM")] + \
                  [x for x in UNITS["probe"] if x[1]["prop"] not in ("AM", "FM")]
def row_of(r, t):
    if t["natural"]:
        return "NS"
    s = r["stim"][t["probe"] - 1]
    return "TORC" if "TORC" in s else "DMR" if "DMR" in s else "MHT" if "Modulated" in s else "MCN" if "pink" in s else "other"
PAPER_T1 = {"NS": (23, 25, 25, 25, 63), "TORC": (39, 40, 0, 0, 0), "DMR": (8, 20, 0, 0, 0), "MHT": (25, 25, 71, 57, 0), "MCN": (0, 0, 0, 0, 74)}
print("\nTable 1 rows (probe type) by property: tests (cells); paper's value after the slash")
for unit in ("table1", "class", "probe"):
    tab = collections.Counter(); tabc = collections.defaultdict(set)
    for r, t in UNITS[unit]:
        tab[(row_of(r, t), t["prop"])] += 1; tabc[(row_of(r, t), t["prop"])].add(r["cell"])
    print(f" reading '{unit}':")
    for row in ("NS", "TORC", "DMR", "MHT", "MCN"):
        print(f"  {row:5s}", "  ".join(f"{p}: {tab[(row, p)]} ({len(tabc[(row, p)])}) / {PAPER_T1[row][i]}"
                                    for i, p in enumerate(A.PROPERTIES) if tab[(row, p)] or PAPER_T1[row][i]))
    tot = collections.Counter(t["prop"] for _, t in UNITS[unit]); totc = collections.defaultdict(set)
    for r, t in UNITS[unit]:
        totc[t["prop"]].add(r["cell"])
    print("   totals:", {p: (tot[p], len(totc[p])) for p in A.PROPERTIES}, " paper: 95 (31), 110 (35), 96 (27), 82 (25), 137 (27)")
# The MHT ensembles with a natural sound: does any MHT fragment have two conditioning stimuli?
mht_nat = [r for r in SYN if r["ttype"] == "synthetic" and any("Modulated" in s for s in r["stim"])
           and any(t["natural"] for t in r["tests"]) and (r["rep"] or 0) >= 4]
nctx = collections.Counter()
for r in mht_nat:
    ctx = collections.defaultdict(set)
    for q in r["seqs"]:
        for a, b in zip(q[:-1], q[1:]):
            ctx[b].add(a)
    for i, s in enumerate(r["stim"], 1):
        if "Modulated" in s:
            nctx[len(ctx[i])] += 1
print(f"\nMHT-ensemble files with a natural sound probe: {len(mht_nat)}; conditioning fragments (silence not counted) "
      f"per MHT fragment: {dict(nctx)}; natural-probe AM tests per set in them: "
      f"{sum(t['prop'] == 'AM' for r in mht_nat for t in r['tests'])}")

ens_name = {"torc": "TORC", "dmr": "DMR", "synthetic": "MHT", "pinknoise": "MCN", "naturalistic": "natural variants"}
syn_cells = {r["cell"] for r, _ in syn}
cc_cells = syn_cells | {r["cell"] for r, _ in nat}
print("\nA1 current-clamp cells with at least one probe meeting the criterion:", len(cc_cells),
      f"(natural {len({r['cell'] for r, _ in nat})}, synthetic {len(syn_cells)}, both {len(syn_cells & {r['cell'] for r, _ in nat})})")
ens = collections.defaultdict(set); ens_files = collections.defaultdict(list)
for r in SYN:
    q = [t for t in r["tests"] if (r["rep"] or 0) >= 4]
    if q:
        e = ens_name.get(r["ttype"], "other")
        ens[e].add(r["cell"])
        ens_files[e].append((r["path"].split("/")[-1], len(q), sum(t["natural"] for t in q)))
print("cells by synthetic ensemble:", {k: len(v) for k, v in ens.items()}, " paper: TORC 14, DMR 6, MHT 39, MCN 27")
print("MHT and natural-variant files together:", len(ens["MHT"] | ens["natural variants"]), "cells")
for e in ("DMR", "natural variants"):
    print(f"files of the {e} ensembles (file, tests, of which natural probes):", ens_files[e])
print("all A1 current-clamp cells in the data set (Summary.mat, natural + synthetic + other):",
      len({r['cell'] for r in sm if r['experiment'] in (0, 2, 3)}))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells; cat > c37.py <<'EOF'
EXP8 = {"amplitude": (77, 95), "frequency": (73, 110), "AM": (62, 96), "FM": (47, 82), "higher-order": (59, 137)}
res8 = {}
for unit in ("table1", "class", "probe"):
    print(f"reading '{unit}':")
    for p in A.PROPERTIES:
        T = [(r, t) for r, t in UNITS[unit] if t["prop"] == p]
        k = sum(len(t["sig"]) > 0 for _, t in T)
        res8[(unit, p)] = (k, len(T), len({r['cell'] for r, _ in T}))
        e = EXP8[p]
        print(f"  {p:12s}: {k} of {len(T)} ({k / len(T):.3f}; {res8[(unit, p)][2]} cells)  paper {e[0]} of {e[1]} ({e[0] / e[1]:.3f}); "
              f"count within tolerance {abs(k - e[0]) <= 0.1 * e[0]}")
    pr = {p: res8[(unit, p)][0] / res8[(unit, p)][1] for p in A.PROPERTIES}
    print(f"  order amplitude > frequency: {pr['amplitude'] > pr['frequency']}; AM > FM > higher-order: {pr['AM'] > pr['FM'] > pr['higher-order']}")
multi = collections.Counter((t["prop"], t.get("n_sets", 1)) for _, t in UNITS["probe"])
print("probes by property and number of sets of conditioning stimuli:", dict(sorted(multi.items())))
EOF
cat > c40.py <<'EOF'
EXP8B = {"amplitude": (0.66, 0.57), "frequency": (0.97, 0.54), "AM": (0.11, 0.86), "FM": (0.15, 0.64), "higher-order": (0.20, 0.52)}
FIT8B = {}
for unit in ("table1", "class", "probe"):
    for p in A.PROPERTIES:
        T = [t for r, t in UNITS[unit] if t["prop"] == p]
        PC = A.power_curves(T)
        short = min(t["T"] for t in T) / 1e4
        for rng in sorted({4.0, round(short, 2)} if unit == "table1" else {4.0}):
            k = int(rng * 1000); tm = np.arange(k) / 1000
            f = A.fit_exp(tm, PC["running"]["Q"][:k], 1, kappa=0.0)
            FIT8B[(unit, p, round(rng, 2))] = f
            print(f"{unit:6s} {p:12s} 0-{rng:.2f} s: alpha {f['alpha'][0]:.3f}, tau {f['tau'][0]:.3f} s (paper {EXP8B[p][1]}, {EXP8B[p][0]} s); "
                  f"tau within tolerance {abs(f['tau'][0] - EXP8B[p][0]) <= 0.1 * EXP8B[p][0]}")
    t4 = {p: FIT8B[(unit, p, 4.0)]["tau"][0] for p in A.PROPERTIES}
    print(f"  {unit}: every tau within tolerance {all(abs(t4[p] - EXP8B[p][0]) <= 0.1 * EXP8B[p][0] for p in A.PROPERTIES)}; "
          "partial pattern (amplitude, frequency > 0.4 s; AM, FM, higher-order < 0.3 s):",
          t4["amplitude"] > .4 and t4["frequency"] > .4 and max(t4["AM"], t4["FM"], t4["higher-order"]) < .3)
EOF
cat > c43.py <<'EOF'
EXP8A = {"amplitude": (0.23, 0.25, 2.8e-3), "frequency": (0.19, 0.27, 2.3e-3), "AM": (0.13, 0.17, 2.3e-3),
         "FM": (0.07, 0.15, 2.1e-3), "higher-order": (0.04, 0.13, 3.6e-3)}
from scipy import optimize
FIT8A = {}
for unit in ("table1", "class", "probe"):
    for si in range(5 if unit == "table1" else 1):
        for p in A.PROPERTIES:
            T = [t for r, t in UNITS[unit] if t["prop"] == p]
            C = A.sig_curve(T, si)
            k = 4000; tm = np.arange(k) / 1000
            kap = float(np.nanmean(C["noise_running"][:k]))
            for bound in ("free", "nonneg"):
                f = A.fit_exp(tm, C["running"][:k], 1, kappa=kap)
                if bound == "nonneg":
                    res = optimize.least_squares(lambda q: A._model(q, tm, 1, kap) - C["running"][:k],
                                                 [max(f["alpha"][0], 1e-3), f["tau"][0]], bounds=([0, 1e-3], [np.inf, 100]))
                    f = dict(alpha=[res.x[0]], tau=[res.x[1]], kappa=kap)
                FIT8A[(unit, si, p, bound)] = f
                if si == 0 or bound == "free":
                    e = EXP8A[p]
                    ok = abs(f["alpha"][0] - e[0]) <= 0.1 * e[0] and abs(f["tau"][0] - e[1]) <= 0.1 * e[1]
                    print(f"{unit:6s} seed {si} {p:12s} {bound:6s}: alpha {f['alpha'][0]:.3f}, tau {f['tau'][0]:.3f} s, noise floor {kap:.5f} "
                          f"(paper {e}); both within tolerance {ok}")
    for bound in ("free", "nonneg"):
        sizes = [FIT8A[(unit, 0, p, bound)]["alpha"][0] for p in A.PROPERTIES]
        print(f"  {unit} {bound}: sizes in the printed order (amplitude > frequency > AM > FM > higher-order): {all(np.diff(sizes) < 0)} {np.round(sizes, 3)}")
EOF
cat > c46.py <<'EOF'
def area(tests, idx=None, sub=None):
    if idx is not None:
        tests = [tests[i] for i in idx]
    PC = A.power_curves(tests, sub)
    return float(np.nansum(PC["running"]["Q"][:4000]) / 1000)
NATDEN = {"silence counted": ([t for _, t in nat], None), "silence not counted": ([t for _, t in nat_ns], "ns")}
for d, (tests, sub) in NATDEN.items():
    print(f"area 0-4 s, natural sounds, {d}: {area(tests, sub=sub):.3f}")
def pattern8c(r):
    hi = all(r[p][2] >= 1 for p in ("amplitude", "frequency"))
    lo_bound = min(r["amplitude"][1], r["frequency"][1])
    low = all(r[p][2] < 1 and r[p][2] < lo_bound for p in ("AM", "FM", "higher-order"))
    pts = min(r["amplitude"][0], r["frequency"][0]) > max(r[p][0] for p in ("AM", "FM", "higher-order"))
    return hi, low, pts
REL = {}
# Reading 1: a sample is a probe (200 resamplings of 1000 probes with replacement).
for unit in ("table1", "class", "probe"):
    for d, (tests, sub) in NATDEN.items():
        for si, s in enumerate(five("fig8c-relative-effects")[: 5 if unit == "table1" else 1]):
            rng = np.random.default_rng(s)
            a_nat = area(tests, sub=sub)
            boot_nat = [area(tests, rng.integers(0, len(tests), 1000), sub) for b in range(200)]
            r = {}
            for p in A.PROPERTIES:
                T = [t for _, t in UNITS[unit] if t["prop"] == p]
                bs = np.array([area(T, rng.integers(0, len(T), 1000)) / boot_nat[b] for b in range(200)])
                r[p] = (area(T) / a_nat, *np.percentile(bs, [2.5, 97.5]))
            REL[("probes", unit, d, si)] = r
            print(f"probes {unit:6s} {d:19s} seed {si}:", {p: tuple(round(float(v), 2) for v in r[p]) for p in A.PROPERTIES},
                  "| amplitude, frequency reach 1; AM, FM, higher-order below 1 and their lower bounds; points in order:", pattern8c(r))
# Reading 2: a sample is a trial (200 resamplings of the trials of every probe and context; 50-ms bins, 1-kHz points).
def boot_area(tests, si, b=None, sub=None):
    get = (lambda t: t[sub]) if sub else (lambda t: t)
    if b is None:  # the point estimate at the same resolution
        P = [A.bin_mean(get(t)["pred"][:4000], 50) for t in tests]; I = [A.bin_mean(get(t)["inv"][:4000], 50) for t in tests]
    else:
        P = [get(t)["boot"][0][si, b] for t in tests]; I = [get(t)["boot"][1][si, b] for t in tests]
    p, _, _ = A.pop_average(P); i, _, _ = A.pop_average(I)
    return float(np.nansum(((p - i) / A.smooth_0_2t(p))[:80]) * 0.05)
for unit in ("table1", "class", "probe"):
    for d, (tests, sub) in NATDEN.items():
        for si in range(5 if unit == "table1" else 1):
            nb = np.array([boot_area(tests, si, b, sub) for b in range(200)])
            a_nat = boot_area(tests, si, None, sub)
            r = {}
            for p in A.PROPERTIES:
                T = [t for _, t in UNITS[unit] if t["prop"] == p]
                bs = np.array([boot_area(T, si, b) for b in range(200)]) / nb
                r[p] = (boot_area(T, si) / a_nat, *np.percentile(bs, [2.5, 97.5]))
            REL[("trials", unit, d, si)] = r
            print(f"trials {unit:6s} {d:19s} seed {si}:", {p: tuple(round(float(v), 2) for v in r[p]) for p in A.PROPERTIES},
                  "| amplitude, frequency reach 1; AM, FM, higher-order below 1 and their lower bounds; points in order:", pattern8c(r))
print("\nreadings meeting the full criterion (claim's seed):", [k for k, r in REL.items() if k[3] == 0 and all(pattern8c(r))])
print("readings meeting it under all five seeds:", sorted({k[:3] for k in REL if k[1] == "table1"
      and all(all(pattern8c(REL[k[:3] + (si,)])) for si in range(5))}))
EOF
cat > c49.py <<'EOF'
for unit in ("table1", "class", "probe"):
    rows = []
    for p in A.PROPERTIES:
        T = [t for r, t in UNITS[unit] if t["prop"] == p]
        a = sum(len(t["sig"]) > 0 for t in T if t["natural"]); n1 = sum(t["natural"] for t in T)
        b = sum(len(t["sig"]) > 0 for t in T if not t["natural"]); n2 = len(T) - n1
        if n1 and n2:
            o, pv = stats.fisher_exact([[a, n1 - a], [b, n2 - b]])
            rows.append((p, a, n1, b, n2, o, pv))
        else:
            print(f"{unit:6s} {p}: only {'natural' if n1 else 'synthetic'} probes ({n1 + n2})")
    m = len(rows)
    for p, a, n1, b, n2, o, pv in rows:
        print(f"{unit:6s} {p:12s}: natural {a}/{n1} ({a / n1:.3f}), synthetic {b}/{n2} ({b / n2:.3f}); odds ratio {o:.2f}, "
              f"p = {pv:.4f}, Bonferroni p = {min(1, pv * m):.4f}")
    print(f"  {unit}: properties with a difference after Bonferroni:", [r[0] for r in rows if r[-1] * m < 0.05])
EOF
cat > c52.py <<'EOF'
FIT9 = {}
for key in ("code", "half", "mad"):
    pr = [(r, p) for r in MGB if (r["rep"] or 0) >= 10 for p in r[f"probes_{key}"]]
    sd, _, n = A.pop_average([p["sd"] for _, p in pr])
    k = min(61, len(sd)); tb = np.arange(k) * 0.1
    plateau = float(np.nanmean(sd[5:k]))
    print(f"detector {key}: {len(pr)} probes; mean SD in the first bins {np.round(sd[:8], 2)}")
    for off in (0.0, 0.05):
        f = A.fit_exp(tb + off, sd[:k], 1)
        FIT9[(key, off)] = (f, plateau)
        print(f"   bin time at {'start ' if off == 0 else 'centre'}: alpha {f['alpha'][0]:.2f} spike/s, tau {f['tau'][0] * 1000:.0f} ms, kappa {f['kappa']:.2f} spike/s; "
              f"tau within 0.08 +/- 0.008 s or below 0.1 s: {f['tau'][0] <= 0.1}")
    print(f"   plateau: mean SD after 0.5 s {plateau:.2f} spike/s against kappa 2.0; within 25% (1.5 to 2.5): {abs(plateau - 2.0) <= 0.5}")
    bycell = collections.defaultdict(list)
    for r, p in pr:
        bycell[r["cell"]].append(p["sd"][0] / max(np.mean(p["sd"][1:]), 1e-9))
    print("   per cell, median ratio of the first bin's SD to later bins':", {c: round(float(np.median(v)), 1) for c, v in bycell.items()})
print("MGB thresholds per file, the authors' detector against 4 noise SDs:",
      [(r["path"].split("/")[-1], round(r["thr_code"], 2), round(r["thr_mad"], 3)) for r in MGB][:21])
EOF
cat > c55.py <<'EOF'
for key in ("code", "half", "mad"):
    pr = [(r, p) for r in MGB if (r["rep"] or 0) >= 10 for p in r[f"probes_{key}"]]
    good = [(r, p) for r, p in pr if len(p["sd"]) > 1 and p["sd"][0] >= 2 * np.max(p["sd"][1:]) and p["sd"][0] > 0]
    des = [(r, p) for r, p in pr if len(r["seqs"]) == 7 and len(p["contexts"]) == 3]
    gd = [(r, p) for r, p in des if any(p is q for _, q in good)]
    print(f"detector {key}: probes with first bin >= 2x every later bin: {len(good)} of {len(pr)} ({len(good) / len(pr):.3f}); "
          f"of the Figure 9A design (7 fragments, 3 contexts): {len(gd)} of {len(des)}")
    for r, p in gd[:5]:
        print("    ", r["path"].split("/")[-1], "probe", p["probe"], "contexts", p["contexts"], "SD:", np.round(p["sd"][:6], 1))
EOF
cat > c7.py <<'EOF'
# Every DMR frequency-variant file: the frequency band of each fragment, and for each frequency test
# the bands of its conditioning stimuli and the end of its last significant period.
target = {(625.0, 2500.0), (2500.0, 10000.0), (10000.0, 40000.0)}
found7 = []
for r in SYN:
    if r["ttype"] != "dmr" or not any("frequency" in s for s in r["stim"]):
        continue
    bands = sorted({tuple(f) for f in r["stim_ff"] if f})
    natp = [i + 1 for i, s in enumerate(r["stim"]) if "DMR" not in s and s not in ("", "[]")]
    print(r["path"].split("/")[-1], "| repeats", r["rep"], "| natural fragments", natp, "| bands (Hz):", bands)
    for t in r["tests"]:
        if t["prop"] != "frequency":
            continue
        cb = sorted({tuple(r["stim_ff"][c - 1]) for c in t["contexts"]})
        sig = [(a / 1e4, b / 1e4) for a, b in t["sig"]]
        last = max(b for a, b in sig) if sig else None
        print(f"   probe {t['probe']} ({'natural' if t['natural'] else 'DMR'}), contexts {t['contexts']}, bands {cb}, "
              f"last significant period ends at {last} s")
        if t["natural"] and set(cb) == target:
            found7.append((r["path"], t["probe"], last))
print("\nnatural sound probes after DMR contexts in 0.625-2.5, 2.5-10 and 10-40 kHz:", found7)
print("bands of DMR fragments over all DMR files:", sorted({tuple(f) for r in SYN if r["ttype"] == "dmr" for f in r["stim_ff"] if f}))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/asari-2009; cp reproduce_asari_2009.ipynb $TMPDIR/nb_orig.ipynb; python3 - <<'EOF'
import json, os
T=os.environ['TMPDIR']+'/cells/'
nb=json.load(open('reproduce_asari_2009.ipynb'))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.splitlines(True)
rd=lambda f: open(T+f).read().rstrip('\n')
setsrc(5, rd('c05.py'))
s6=src(6); marker='print("peak memory so far (MB):"'
assert marker in s6
setsrc(6, s6.replace(marker, rd('c06add.py')+'\n'+marker))
setsrc(10, rd('c10.py'))
s13=src(13)
s13=s13.replace('for key in ("code", "half"):\n    for late','for key in ("code", "half", "mad"):\n    for late')
s13=s13.replace('    for key in ("code", "half"):\n        for late','    for key in ("code", "half", "mad"):\n        for late')
assert s13.count('"mad"')==2
setsrc(13, s13)
setsrc(37, rd('c37.py')); setsrc(40, rd('c40.py')); setsrc(43, rd('c43.py')); setsrc(46, rd('c46.py')); setsrc(49, rd('c49.py'))
setsrc(52, rd('c52.py')); setsrc(55, rd('c55.py'))
# fig7 section inserted before figs1 (cell 57)
md={'cell_type':'markdown','metadata':{},'source':[]}
def mk(kind, s, tags=None):
    c={'cell_type':kind,'metadata':({'tags':tags} if tags else {}),'source':s.splitlines(True)}
    if kind=='code': c.update(execution_count=None, outputs=[])
    return c
new=[mk('markdown','''## fig7-example-frequency-context

> In an example A1 neuron, a natural sound probe preceded by three DMR contexts that differed only in frequency
> band gave significant context dependence for about 4 s.

The criterion asks for a DMR frequency-variant cell with contexts in 0.625-2.5, 2.5-10 and 10-40 kHz and a
natural sound probe. Every DMR frequency-variant file is listed with the band (`ff`) of each fragment and, for
each frequency test, the bands of its conditioning stimuli and its significant periods.'''),
 mk('code', rd('c7.py'), ['claim:fig7-example-frequency-context']),
 mk('markdown','**Result: TBD**', ['conclusion'])]
C[57:57]=new
nb['cells']=C
json.dump(nb, open('reproduce_asari_2009.ipynb','w'), indent=1)
print(len(C))
EOF
```

```
65
```

**Agent calls Bash**

```bash
cd entries/asari-2009; date -u; python3 - <<'EOF'
import json, os
T=os.environ['TMPDIR']
nb=json.load(open('reproduce_asari_2009.ipynb'))
mk=lambda s: {'cell_type':'code','metadata':{},'source':s,'execution_count':None,'outputs':[]}
nb['cells'].insert(1, mk("import sys; sys.path.insert(0, 'entries/asari-2009')"))
nb['cells'].insert(7, mk(f"import pickle; pickle.dump((F, NAT, MGB, SYN), open('{T}/data.pkl', 'wb'))"))
json.dump(nb, open(T+'/dev.ipynb','w'))
EOF
cd $TMPDIR && time timeout 3600 executed/asari-2009/.venv/bin/jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --allow-errors --ExecutePreprocessor.timeout=3500 2>&1 | tail -3; date -u
```

```
Thu Nov 19 06:02:05 UTC 2026
  _validate(nbdict, ref, version, version_minor, relax_add_props)
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 234740 bytes to dev_out.ipynb

real	29m42.339s
user	91m4.789s
sys	11m16.226s
Thu Nov 19 06:31:48 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json
nb=json.load(open('dev_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    if i in (8,9,11,12,15,17): pass
    out=''
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': out+='ERROR '+o['ename']+': '+o['evalue']+'\n'
        t=o.get('text',''); out+= t if isinstance(t,str) else ''.join(t)
    tags=c['metadata'].get('tags')
    if tags and any(x in str(tags) for x in ('methods-recording','a1-mgb','fig8','fig9','fig7','sanity')):
        print('=== cell',i,tags); print(out[:6000])
    elif 'ERROR' in out: print('=== cell',i, out[:2000])
EOF
```

```
<persisted-output>
Output too large (38KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/b4x5a6nlx.txt

Preview (first 2KB):
=== cell 8 ['sanity']
A1 natural: 46 files, 39 cells, 34 animal-days; effective repeats [(4, 16), (5, 7), (6, 8), (7, 10), (8, 2), (9, 1), (10, 1), (12, 1)]
A1 synthetic: 105 files, 96 cells, 70 animal-days; effective repeats [(4, 37), (5, 19), (6, 40), (7, 7), (8, 1), (9, 1)]
MGB: 21 files, 14 cells, 4 animal-days; effective repeats [(10, 2), (13, 1), (15, 1), (17, 1), (19, 2), (20, 4), (21, 4), (22, 1), (23, 2), (24, 2), (25, 1)]
units (current clamp): Counter({'mV': 151})  sampling rates: Counter({10000: 151})
median-filtered membrane potential, 1st and 99th percentiles over files: -87.0 to -2.7 mV (median of file medians of the 1st pct -68.6)
ages (days): [('', 1), ('20', 5), ('21', 28), ('22', 22), ('23', 21), ('24', 35), ('25', 21), ('26', 15), ('27', 3)]
fragment lengths (s), natural: 1.98 to 6.06
recording time per natural file: silence 236 s, sound 985 s (medians)
experiments in Summary.mat: [(0, 'Auditory cortical cell responses to natural sound combinations.'), (1, 'Thalamic cell responses to natural sound combinations.'), (2, 'Auditory cortical cell responses to synthetic sound combinations.'), (3, 'Auditory cortical cell responses to various acoustic stimuli.')]
files sharing their first probe's power trace (duplicates): 0
recording types (current clamp files): Counter({'Whole-cell': 151})
trace scale (mV per integer step of the stored int16): [0.006104, 0.015259]
natural sound probes, fraction of values tied with another at the same time point: median 0.0251, range 0.0068 to 0.1336
  experiment 4 file: 20060709-ha1-001-002.mat | Whole-cell | Variety of stimuli: white noise, natural sounds, and random  | trigger type randomchords
  experiment 4 file: 20060709-ha1-002-002.mat | Whole-cell | Variety of stimuli: white noise, natural sounds, and r
[... 4 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fd571f3d-07ce-4c05-a127-a099f494fcc6/tool-results/b4x5a6nlx.txt"
}
```

```
1	=== cell 8 ['sanity']
2	A1 natural: 46 files, 39 cells, 34 animal-days; effective repeats [(4, 16), (5, 7), (6, 8), (7, 10), (8, 2), (9, 1), (10, 1), (12, 1)]
3	A1 synthetic: 105 files, 96 cells, 70 animal-days; effective repeats [(4, 37), (5, 19), (6, 40), (7, 7), (8, 1), (9, 1)]
4	MGB: 21 files, 14 cells, 4 animal-days; effective repeats [(10, 2), (13, 1), (15, 1), (17, 1), (19, 2), (20, 4), (21, 4), (22, 1), (23, 2), (24, 2), (25, 1)]
5	units (current clamp): Counter({'mV': 151})  sampling rates: Counter({10000: 151})
6	median-filtered membrane potential, 1st and 99th percentiles over files: -87.0 to -2.7 mV (median of file medians of the 1st pct -68.6)
7	ages (days): [('', 1), ('20', 5), ('21', 28), ('22', 22), ('23', 21), ('24', 35), ('25', 21), ('26', 15), ('27', 3)]
8	fragment lengths (s), natural: 1.98 to 6.06
9	recording time per natural file: silence 236 s, sound 985 s (medians)
10	experiments in Summary.mat: [(0, 'Auditory cortical cell responses to natural sound combinations.'), (1, 'Thalamic cell responses to natural sound combinations.'), (2, 'Auditory cortical cell responses to synthetic sound combinations.'), (3, 'Auditory cortical cell responses to various acoustic stimuli.')]
11	files sharing their first probe's power trace (duplicates): 0
12	recording types (current clamp files): Counter({'Whole-cell': 151})
13	trace scale (mV per integer step of the stored int16): [0.006104, 0.015259]
14	natural sound probes, fraction of values tied with another at the same time point: median 0.0251, range 0.0068 to 0.1336
15	  experiment 4 file: 20060709-ha1-001-002.mat | Whole-cell | Variety of stimuli: white noise, natural sounds, and random  | trigger type randomchords
16	  experiment 4 file: 20060709-ha1-002-002.mat | Whole-cell | Variety of stimuli: white noise, natural sounds, and random  | trigger type randomchords
17	  experiment 4 file: 20060714-ha1-002-002.mat | Whole-cell | Variety of stimuli: white noise, natural sounds, and random  | trigger type 
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json
nb=json.load(open('dev_out.ipynb'))
for i in (45,48):
    c=nb['cells'][i]
    out=''.join(''.join(o.get('text','')) for o in c['outputs'])
    lines=out.splitlines()
    if i==45: print('\n'.join(lines[-8:]))
    else: print('\n'.join(l for l in lines if l.startswith('trials') or l.startswith('readings')))
c=nb['cells'][-1]; print(''.join(''.join(o.get('text','')) for o in c['outputs']))
EOF
```

```
probe  seed 0 AM           free  : alpha 0.149, tau 0.175 s, noise floor 0.00509 (paper (0.13, 0.17, 0.0023)); both within tolerance False
probe  seed 0 AM           nonneg: alpha 0.149, tau 0.175 s, noise floor 0.00509 (paper (0.13, 0.17, 0.0023)); both within tolerance False
probe  seed 0 FM           free  : alpha 0.043, tau 0.138 s, noise floor 0.00674 (paper (0.07, 0.15, 0.0021)); both within tolerance False
probe  seed 0 FM           nonneg: alpha 0.043, tau 0.138 s, noise floor 0.00674 (paper (0.07, 0.15, 0.0021)); both within tolerance False
probe  seed 0 higher-order free  : alpha 0.078, tau 0.118 s, noise floor 0.00602 (paper (0.04, 0.13, 0.0036)); both within tolerance False
probe  seed 0 higher-order nonneg: alpha 0.078, tau 0.118 s, noise floor 0.00602 (paper (0.04, 0.13, 0.0036)); both within tolerance False
  probe free: sizes in the printed order (amplitude > frequency > AM > FM > higher-order): False [0.13  0.155 0.149 0.043 0.078]
  probe nonneg: sizes in the printed order (amplitude > frequency > AM > FM > higher-order): False [0.13  0.155 0.149 0.043 0.078]
trials table1 silence counted     seed 0: {'amplitude': (0.73, 1.11, 1.27), 'frequency': (0.64, 1.05, 1.16), 'AM': (0.15, 0.81, 0.93), 'FM': (0.13, 0.76, 0.89), 'higher-order': (0.37, 0.89, 1.0)} | amplitude, frequency reach 1; AM, FM, higher-order below 1 and their lower bounds; points in order: (True, False, True)
trials table1 silence counted     seed 1: {'amplitude': (0.73, 1.12, 1.27), 'frequency': (0.64, 1.04, 1.16), 'AM': (0.15, 0.81, 0.92), 'FM': (0.13, 0.77, 0.9), 'higher-order': (0.37, 0.9, 0.99)} | amplitude, frequency reach 1; AM, FM, higher-order below 1 and their lower bounds; points in order: (True, True, True)
trials table1 silence counted     seed 2: {'amplitude': (0.73, 1.12, 1.26), 'frequency': (0.64, 1.04, 1.15), 'AM': (0.15, 0.81, 0.92), 'FM': (0.13, 0.77, 0.88), 'higher-order': (0.37, 0.9, 1.0)} | amplitude, frequency reach 1; AM, FM, higher-order below 1 and their lower 
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/asari-2009.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig3b-fractional-power-decay','fig4-predictability-upper-bound','a1-mgb-firing-rates'):
        print(cl['id'], '::', cl['criterion'], '\n')
EOF
date -u
```

```
a1-mgb-firing-rates :: Tolerances are 10% of each mean; the printed SDs (0.61, 0.77, 1.25, 16.9 Hz) are the spread over cells, not an uncertainty of the mean, and are reported for comparison (within 10% of each). Spikes in MGB are extracted by a high-pass filter and a threshold with spike times at the peaks (Methods, Analysis, paragraph 3). The paper fixes neither the filter cutoff, the threshold, nor how A1 spikes were detected, nor the windows for "spontaneous" (readings are the intersequence silence, about 6 s, or a pre-stimulus baseline) and "evoked" (readings are all sound periods, or the probe periods analysed). The author runs a standard detector on each reading of the windows; reproduced when the four means are within tolerance under one reading, partially reproduced when the A1 means are below 1 Hz and the MGB evoked mean above 5 Hz but some means fall outside tolerance. 

fig3b-fractional-power-decay :: Q(t) of Eq. 20 from the 305 natural sound probes, numerator Eq. 19 and denominator Eq. 17 averaged over probes at each time point, the denominator smoothed by a running mean over [0, 2t] before the division; one exponential with constant 0 fitted (Figure 3B legend). The same open details as fig3a-proportion-significant (silence as a context; which probes enter the average at time t) and the fit range (0 to 4 s, 0 to 6 s) are run as readings. The printed values in the legend are garbled in the text extraction and read as alpha1 = 0.49, tau1 = 1.04 s with kappa = 0, which the Results (1.04 s) and Figure 4 legend confirm. Reproduced when both are within tolerance under one reading. 

fig4-predictability-upper-bound :: Eq. 43 at each time after probe onset, context-independent power (Eq. 18) over stimulus-related power (Eq. 17), both averaged over the 305 natural sound probes in 39 cells; the Methods (Eq. 20) say the denominator is smoothed over [0, 2t] before Eq. 43 too, which is the main reading, with the unsmoothed ratio as a variant. One exponential with co
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
import json
nb=json.load(open('strf_wehr.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(f"=== {i} {c['cell_type']} {c['metadata'].get('tags')} outputs={len(c.get('outputs',[]))}")
    if c['cell_type']=='markdown': print(s[:3000])
    else: print(s[:400])
EOF
wc -l wehr.py; head -60 wehr.py
```

```
=== 0 markdown None outputs=0
# Asari & Zador (2009), Fig. 4: STRF and LN model performance on Wehr's A1 cells

Paper: H. Asari and A. M. Zador (2009), "Long-Lasting Context Dependence Constrains Neural
Encoding Models in Rodent Auditory Cortex", J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.

Data set: CRCNS ac-1 (unversioned; doi:10.6080/K0KW5CXR), Wehr's recordings (`wehr/` in
`crcns-ac1.zip`), read in place from the public S3 bucket `crcnsarchive` over HTTP range
requests; nothing is downloaded to disk.

This notebook tests one claim, `fig4-strf-performance-low`: linear STRF models (and LN models with
a static nonlinearity) of A1 cells from Machens et al. (2004) predict less than about 20% of the
predictable response power at every window length from 180 ms to about 4 s, and extending the window
does not improve them significantly. Methods follow the paper (Methods, "Neural encoding models",
Eqs. 46 to 51; "Model performance", Eqs. 52 and 53), the claim's criterion, and the authors' own code
shipped in the zip (`wehr/Tools/STRFanalysis.m`, `ridgesvd1.m`, `logspectrogram.m`,
`ViewResponse.m`, `GetEvoked.m`, `MakeRamp.m`). Where each parameter comes from is listed in the
docstring of `wehr.py`; the assumptions are repeated below.
=== 1 code None outputs=0
import os, time, zlib, resource
[... 228 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 -c "
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='markdown': print(i, c['metadata'].get('tags'), ''.join(c['source'])[:70].replace('\n',' '))
"
```

```
0 None # Reproducing Asari & Zador (2009) on CRCNS ac-1  Paper: H. Asari and 
2 None ## Data  The data set's checksums and its own documentation are read f
4 None Each file is read once, in four processes, and reduced to what the cla
7 None Clock check. The trial tables give the onset of each sequence in sampl
9 None ## methods-recording-counts  > Of 194 A1 cells recorded in current cla
11 ['conclusion'] **Result: partially reproduced.** Whether silence counts or not, 305 n
12 None ## a1-mgb-firing-rates  > Firing rates were low in A1 (spontaneous 0.4
14 ['conclusion'] **Result: partially reproduced.** With the 15-mV detector the A1 means
15 None ## fig2-example-reliability  > The example A1 neuron of Figure 2 had h
17 ['conclusion'] **Result: reproduced.** The mean pairwise correlation is 0.310 +/- 0.0
18 None ## fig2-example-long-context  > In an example A1 neuron, changing the 
20 ['conclusion'] **Result: reproduced.** For the matched probe (20051222-ha1-001, probe
21 None ## fig3a-proportion-significant  > Of 305 natural sound probes tested 
23 ['conclusion'] **Result: reproduced.** With silence as a context, 186 of 305 probes a
24 None ## fig3a-significance-decay  > The proportion of probes with significa
26 ['conclusion'] **Result: partially reproduced.** No reading puts every value within t
27 None ## fig3b-fractional-power-decay  > The context-dependent fraction of t
29 ['conclusion'] **Result: partially reproduced.** The size is within tolerance under e
30 None ## timescale-longer-than-membrane  > The trial-to-trial noise autocorr
32 ['conclusion'] **Result: reproduced.** The mean noise autocorrelation falls below 1/e
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; cat > $TMPDIR/md.py <<'PYEOF'
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
C=nb['cells']
def setmd(i, s, must=None):
    if must: assert ''.join(C[i]['source']).startswith(must), (i, ''.join(C[i]['source'])[:60])
    C[i]['source']=s.strip('\n').splitlines(True)
h=''.join(C[0]['source'])
h=h.replace('''zips). Michael Wehr's recordings (`wehr/`), which the paper reanalyses for its STRF models
(Figure 4), are not used: that claim was not run in the time of this attempt.''','''zips). Michael Wehr's recordings (`wehr/`), which the paper reanalyses for its STRF models
(Figure 4), are used by the second notebook, `strf_wehr.ipynb`, which tests
fig4-strf-performance-low.''')
h=h.replace('| fig4-strf-performance-low | blocked: not run within the time of this attempt |','| fig4-strf-performance-low | tested in `strf_wehr.ipynb` |')
h=h.replace('| fig8c-relative-effects | tested (probe resampling only) |','| fig8c-relative-effects | tested |')
h=h.replace('| fig7-example-frequency-context | blocked: no recording matches the example |','| fig7-example-frequency-context | searched; blocked, no recording matches the example |')
assert 'strf_wehr' in h and 'searched; blocked' in h
C[0]['source']=h.splitlines(True)
setmd(4,'''Each file is read once, in four processes, and reduced to what the claims need
(`A.reduce_wholecell`, `A.reduce_mgb`): for every probe its significant periods, the shuffle noise
floor (1000 shuffles under each of five seeds), the power estimates, trial correlations and
autocorrelations, at 1-ms resolution; 200 resamplings of the trials of every probe and context under
the five seeds of fig8c-relative-effects (`A.trial_boot`); spike counts for the rates.''','Each file')
setmd(9,'''## methods-recording-counts

> Of 194 A1 cells recorded in current clamp, 123 met the analysis criterion (39 tested with natural
> sounds, 14 with TORCs, 6 with DMRs, 39 with modulated harmonic tones, 27 with modulated colored
> noise); 14 of 42 voltage-clamped cells and 14 of 16 MGB cells were analysed.

A probe counts when it has at least two conditioning stimuli with at least 4 trials each (current
clamp; the file's "Effective repeats", CxtDep.m) or at least 10 (MGB, Methods, Context dependence
at suprathreshold level). Both readings of silence (counted as a conditioning stimulus or not) are
shown. For the synthetic ensembles, the sets of conditioning stimuli that differ in one property
are formed by `A.property_classes` (from the file's notes where they list the variants, otherwise
from the stimulus descriptions and parameters), and Table 1 is shown under three readings of what
is counted: each probe with each such set ('class'), each probe once per property ('probe'), and
'class' for AM and FM with 'probe' for the other three ('table1', the only reading whose totals equal
every column of Table 1). The rows are the probe type, as in Table 1.''','## methods')
setmd(11,'''**Result: partially reproduced.** Whether silence counts or not, 305 natural sound probes in 39
cells meet the criterion, and 93 MGB probes in 14 cells (every MGB cell of the data set), as in
Table 1. Summary.mat lists four experiments and none is in voltage clamp, so the 14 cells and 29
probes of the voltage-clamp claims cannot be counted. 133 current-clamp cells have at least one
probe meeting the criterion, not 123 (natural 39, synthetic 96, 2 in both). By ensemble, TORC (14)
and MCN (27) match; MHT and natural-variant files together give 40 cells against the paper's 39
MHT cells; DMR files give 15 cells against 6. Of the 17 DMR files, the 7 with DMR probes come from 6
cells, as in the paper; the other 10 files (20060915 to 20060917) test only a natural sound probe after
DMR variants, in 9 cells, and are the probes that make most of the difference (133 less 9 is 124). Under
the 'table1' reading the property totals are 95, 110, 96, 82 and 137, equal to the paper's; under
'class' they are 95 is 104, 120, 96, 82 and 354, and under 'probe' 95, 110, 39, 25 and 137. The rows do
not match Table 1 under any reading: the MHT row has 14 AM tests and no amplitude, frequency or FM
test, where the paper has 25, 25, 71 and 57, because in the 25 MHT-ensemble files with a natural sound
every MHT fragment follows at most one other fragment (235 none, 171 one), so only the natural sound
is a probe there.''','**Result')
s=''.join(C[11]['source']).replace("under\n'class' they are 95 is 104","under\n'class' they are 104")
C[11]['source']=s.splitlines(True)
s=''.join(C[12]['source'])
s=s.replace("MGB spikes: the authors' automatic detector (GetSpikes.m) and\nthe same with half its threshold.","MGB spikes: the authors' automatic detector (GetSpikes.m), the\nsame with half its threshold, and a noise-based threshold of 4 SD (the SD from the median absolute\nvalue of the filtered trace, the field's usual choice, Quiroga et al. 2004).")
assert 'Quiroga' in s; C[12]['source']=s.splitlines(True)
setmd(14,'''**Result: partially reproduced.** With the 15-mV detector the A1 means are 0.481 Hz spontaneous and
0.547 Hz evoked over 133 cells (SD 0.597 and 0.677), within 10% of 0.47 and 0.57, and the A1 means
are below 1 Hz under every reading. The MGB evoked mean is 4.99 Hz with the authors' detector, 7.07
Hz with half its threshold and 18.02 Hz with the 4-SD noise threshold, outside 11.4 +/- 1.14 under
all three; it is above 5 Hz with the two lower thresholds. The MGB spontaneous mean is within
tolerance only with half the authors' threshold (0.768 Hz); with the 4-SD threshold it is 2.84 Hz.
Under the authors' detector one MGB cell fires at 43 Hz during sounds and nine below 1.5 Hz. The data
set holds 14 MGB cells; the paper's rates are over 16.''','**Result')
setmd(29,'''**Result: not reproduced.** The size is within tolerance under every reading (0.445 to 0.468
against 0.49 +/- 0.049), but the decay constant is outside 1.04 +/- 0.104 s under every reading (1.29
to 1.78 s), and the criterion has no partial rule. Q(t) is 0.626 at 0.1 s and 0.191 at 1 s, the value
of the paper's curve there (0.49 exp(-1/1.04) = 0.188), and 0.049 at 2 s; it rises to 0.13 at 4 s,
which lengthens the fitted constant.''','**Result')
setmd(35,'''**Result: not reproduced.** No reading puts both values within tolerance, and the criterion has no
partial rule. With the denominator smoothed as the Methods say, 1 + alpha is 0.43 to 0.49 over the
running probes (0.51 +/- 0.051) and tau 1.86 to 2.81 s; over all probes fitted to 6 s the fit runs to
the bound of 100 s. Unsmoothed, 1 + alpha is 0.50 to 0.54, within tolerance, and tau 1.46 to 1.92 s,
outside 1.04 +/- 0.104 s. The bound is below 1 near the onset (0.54 to 0.83 at 0.1 s) under every
reading.''','**Result')
setmd(36,'''## fig8a-proportion-by-property

> When only one property of synthetic conditioning stimuli varied, context dependence was found in
> 77 of 95 probes (81.1%, 31 cells) for amplitude, 73 of 110 (35 cells) for frequency, 62 of 96
> (64.6%, 27 cells) for AM, 47 of 82 (57.3%, 25 cells) for FM and 59 of 137 (43.1%, 27 cells) for
> higher-order properties.

The criterion says the probes of each property follow the columns of Table 1. Main reading
'table1': each probe with each set of conditioning stimuli that differ in AM or in FM is a test, and
each probe is counted once for amplitude, frequency and higher-order properties (significant when
any of its sets is); its totals equal all five of Table 1 (see methods-recording-counts). Variants:
'class' (every probe with every set) and 'probe' (every probe once per property).''','## fig8a')
setmd(38,'''**Result: not reproduced (resting on the assumed reading of Table 1).** Under the 'table1'
reading, whose denominators equal the paper's (95, 110, 96, 82, 137), the significant tests are
amplitude 58, frequency 62, AM 41, FM 29 and higher-order 64; only higher-order is within tolerance
(59 +/- 5.9). Amplitude (0.611) is above frequency (0.564), but AM (0.427) is above FM (0.354) and
below higher-order (0.467), so the paper's order fails and the partial rule does not hold. The two
variants keep the order and would be partial: 'class' gives 61 of 104, 70 of 120, 41 of 96, 29 of 82 and
109 of 354 (frequency within tolerance; 0.587 > 0.583, 0.427 > 0.354 > 0.308), 'probe' gives 58 of 95,
62 of 110, 25 of 39, 16 of 25 and 64 of 137 (higher-order within tolerance; 0.611 > 0.564, 0.641 >
0.640 > 0.467).''','**Result')
setmd(39,'''## fig8b-decay-by-property

> The normalized context-dependent power decays slowly for amplitude and frequency changes (time
> constants 0.66 and 0.97 s) and fast for AM, FM and higher-order changes (0.11, 0.15 and 0.20 s).

Q(t) per property over the tests of fig8a-proportion-by-property (probes running), one
exponential with constant 0, fitted from 0 to 4 s, under the three readings of the tests; for the
main reading also from 0 to the shortest probe length. A probe counted once has the mean of its
sets' power curves.''','## fig8b')
setmd(41,'''**Result: partially reproduced.** Under the 'table1' reading, fitted from 0 to 4 s, the decay
constants are 1.39 s (amplitude), 0.80 s (frequency), 0.109 s (AM), 0.28 s (FM) and 0.25 s
(higher-order); only AM is within tolerance. The pattern of the partial rule holds: amplitude and
frequency above 0.4 s, the other three below 0.3 s; it holds under the 'class' and 'probe' readings
too. The sizes are 0.40, 0.50, 0.87, 0.21 and 0.76 against 0.57, 0.54, 0.86, 0.64 and 0.52.''','**Result')
setmd(42,'''## fig8a-significance-fits

> The proportion of probes with significant context dependence decays fastest and is smallest for
> higher-order changes, with fitted (size, time constant) of (0.23, 0.25 s) for amplitude, (0.19,
> 0.27 s) for frequency, (0.13, 0.17 s) for AM, (0.07, 0.15 s) for FM and (0.04, 0.13 s) for
> higher-order properties.

One exponential with the constant at the mean noise floor of each property (probes running),
fitted from 0 to 4 s; the main reading under the claim's seed and four more, the variants under the
claim's seed; sizes free in sign or non-negative. For a probe counted once, the noise floor is
1 - prod(1 - floor of each set), as if its sets' shuffles were independent.''','## fig8a-sig')
setmd(44,'''**Result: not reproduced.** No property has both values within tolerance under any reading or
seed. Under 'table1' the sizes are 0.130, 0.155, 0.067, 0.013 and 0.078 against 0.23, 0.19, 0.13, 0.07
and 0.04, with constants 0.275, 0.295, 0.198, 0.137 and 0.118 s, and the sizes are not in the printed
order. Under 'class' and 'probe' the sizes are not in the printed order either (0.121, 0.150, 0.067,
0.013, 0.035 and 0.130, 0.155, 0.149, 0.043, 0.078). Bounding the sizes at 0 changes nothing.''','**Result')
setmd(45,'''## fig8c-relative-effects

> Changes in amplitude and frequency of the conditioning stimuli produced context effects as large
> and long-lasting as natural sound contexts, while AM, FM and higher-order changes produced
> substantially smaller and shorter effects.

Area under Q(t) from 0 to 4 s for each property over the area for natural sounds (probes running),
with 95% intervals from 200 resamplings (Methods, Eq. 21 and the paragraph after it). Readings: the
natural sound denominator with silence counted as a context or not; a sample is a probe (1000
probes drawn with replacement within each property and within the natural sounds) or a trial
(the trials of every probe and context drawn with replacement, `A.trial_boot`, 50-ms bins); the
three readings of the tests. The main reading of the tests runs under five seeds.''','## fig8c')
setmd(47,'''**Result: partially reproduced.** Under the claim's seed no reading meets the full criterion,
and under every reading the point estimates fall in the claimed pattern. Resampling probes, with the
'table1' tests and silence counted, the ratios are 0.73 (0.62 to 0.84) for amplitude, 0.63 (0.55 to
0.72) for frequency, 0.15 (0.11 to 0.19) for AM, 0.13 (0.10 to 0.17) for FM and 0.36 (0.31 to 0.42) for
higher-order; with silence not counted in the natural denominator (area 0.621 against 0.762), they
are 0.89 (0.76 to 1.04), 0.77 (0.67 to 0.90), 0.18, 0.16 and 0.45, so the amplitude interval reaches 1
and the frequency interval does not. Resampling trials, the amplitude and frequency intervals lie
above 1 (1.11 to 1.27 and 1.05 to 1.16 with silence counted) while the AM and FM intervals lie below
1; the higher-order upper bound is 1.00 under the claim's seed and 0.99 to 1.00 under the other four,
which meet the full criterion, so the outcome is seed sensitive. These trial intervals do not contain
their own point estimates (amplitude 0.73 against 1.11 to 1.27): drawing trials with replacement
duplicates trials and biases the power estimates, so this reading is not a sound interval.''','**Result')
setmd(48,'''## fig8-natural-synthetic-probes-alike

> Natural and synthetic probes gave no difference in the context effects of the synthetic
> conditioning stimuli, so they were combined.

Fisher's exact test per property of the proportion of significant tests, natural against
synthetic probes, at 0.05 with Bonferroni over the properties tested with both, under the three
readings of the tests. A probe is natural when its fragment is a natural sound or a transform of
one, from the file's stimulus descriptions; the MHT-ensemble files with a natural sound have only the
natural sound as a probe (methods-recording-counts).''','## fig8-nat')
setmd(50,'''**Result: reproduced, resting on the test fixed by the claims file.** No property differs between
natural and synthetic probes under any reading. Under 'table1': amplitude 0.600 against 0.620 (odds
ratio 0.92, p = 1.0), frequency 0.500 against 0.609 (0.64, p = 0.33), AM 0.402 against 0.571 (0.51,
p = 0.26), higher-order 0.475 against 0.461 (1.06, p = 0.87), Bonferroni over four. FM was tested with
natural probes only, and AM has 14 synthetic probe tests in 2 cells, so the comparison has little
power for AM and none for FM.''','**Result')
s=''.join(C[51]['source']).replace("spikes by the authors' detector and with half its threshold.","spikes by the authors' detector, with half its threshold, and with the\n4-SD noise threshold of a1-mgb-firing-rates. The plateau is the mean SD after 0.5 s, against the\npaper's kappa of 2.0.")
assert '4-SD' in s; C[51]['source']=s.splitlines(True)
setmd(53,'''**Result: partially reproduced.** Under every detector a single exponential gives tau below 0.1 s
(55 ms with the authors' detector, 61 ms with half its threshold, 54 ms with the 4-SD threshold), but
the plateau after 0.5 s is 1.27, 1.38 and 3.24 spike/s, outside 2.0 +/- 25% under all three, so the
second condition fails. The mean SD of PSTHs is 6.45 spike/s in the first bin and 2.04 in the second
with the authors' detector. The sizes are 5.2 or 12.9 spike/s (bin start or centre) with the authors'
detector and 10.0 or 25.4 with the 4-SD threshold, against 15.0. tau is far below 0.3 s, so the claim
is not not reproduced by the criterion.''','**Result')
s=''.join(C[54]['source']).replace("fraction over all 93 probes too.","fraction over all 93 probes too; under the three detectors of fig9-mgb-fast-decay.")
C[54]['source']=s.splitlines(True)
setmd(56,'''**Result: reproduced.** Of the 12 probes with the Figure 9A design (all in 20071010-ha2-003), 4
have a first-bin SD at least twice every later bin's (for example 31.4 spike/s against at most 7.2),
under all three detectors; over all 93 probes, 35 (authors' detector), 45 (half threshold) or 40 (4-SD
threshold) do.''','**Result')
setmd(59,'''**Result: blocked, no recording matches.** No natural sound probe follows DMR contexts in 0.625-2.5,
2.5-10 and 10-40 kHz. The five DMR frequency-variant files with a natural sound probe use six 2-octave
bands from 250-1000 to 8000-32000 Hz, each band once with and once without randomized syllables; in
two of their ten frequency tests the last significant period ends after 3.6 s (4.58 s in
20060916-ha4-001-002 and 4.83 s in 20060916-ha5-002-002), but neither has the example's bands. The
bands 625-2500, 2500-10000 and 10000-40000 Hz occur in the data set only as parts of other DMR
fragments (625-2500 with 10000-40000, 2500-10000 alone, 2500-40000), none of them with a natural
sound probe.''','**Result')
json.dump(nb, open('reproduce_asari_2009.ipynb','w'), indent=1)
PYEOF
python3 $TMPDIR/md.py && echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
c=nb['cells'][59]; s=''.join(c['source'])
s=s.replace("bands from 250-1000 to 8000-32000 Hz, each band once with and once without randomized syllables; in","bands from 250-1000 to 8000-32000 Hz, in two sets of six fragments with the same bands; in")
s=s.replace('''bands 625-2500, 2500-10000 and 10000-40000 Hz occur in the data set only as parts of other DMR
fragments (625-2500 with 10000-40000, 2500-10000 alone, 2500-40000), none of them with a natural
sound probe.''','''bands 625-2500, 2500-10000 and 10000-40000 Hz occur in the data set only in other DMR files, as one
band (2500-10000) or within others (625-2500 with 10000-40000, 2500-40000), never as the three
conditioning stimuli of one probe.''')
c['source']=s.splitlines(True)
json.dump(nb, open('reproduce_asari_2009.ipynb','w'), indent=1)
EOF
date -u
```

```
Thu Nov 19 06:34:10 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
c=nb['cells'][59]; s=''.join(c['source']).replace("never as the three\nconditioning stimuli of one probe.","never as the three\nconditioning stimuli of a natural sound probe."); c['source']=s.splitlines(True)
assert 'natural sound probe.' in s
summ='''## Summary

| Claim | Outcome |
|---|---|
| methods-recording-counts | partially reproduced |
| a1-mgb-firing-rates | partially reproduced (assumed detectors) |
| fig2-example-reliability | reproduced |
| fig2-example-long-context | reproduced |
| fig3a-proportion-significant | reproduced |
| fig3a-significance-decay | partially reproduced |
| fig3b-fractional-power-decay | not reproduced |
| timescale-longer-than-membrane | reproduced |
| fig4-predictability-upper-bound | not reproduced |
| fig4-strf-performance-low | not reproduced (`strf_wehr.ipynb`; assumed cells and test) |
| fig5-example-conductances | blocked (data missing: no voltage clamp) |
| fig6-conductance-decay | blocked (data missing: no voltage clamp) |
| fig8a-proportion-by-property | not reproduced (assumed reading of Table 1) |
| fig8b-decay-by-property | partially reproduced (assumed reading of Table 1) |
| fig8a-significance-fits | not reproduced |
| fig8c-relative-effects | partially reproduced (seed sensitive) |
| fig8-natural-synthetic-probes-alike | reproduced (assumed test) |
| fig9-mgb-fast-decay | partially reproduced |
| fig9-example-first-bin | reproduced |
| fig7-example-frequency-context | blocked (no recording matches) |
| figs1-silence-probe | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's. Details the Methods leave open are taken from the
authors' code in the data set (CxtDep.m): silence as a context, trials per context, the
significance run rule, the centring of traces for the power measure, the MGB spike detector. The
A1 spike detector is assumed (the authors extracted whole-cell spikes by hand), and a noise-based MGB
detector is shown beside the authors'. The sets of conditioning stimuli of Figure 8 come from the
files' notes where they list them and are otherwise formed from the stimulus parameters; what is
counted as a test is assumed ('table1': each set for AM and FM, each probe once for the other
properties, the reading whose totals equal Table 1), and two other readings are shown. Curves are
fitted at 1-ms resolution. The Figure 8C intervals resample probes or trials. The STRF claim uses 16
of Wehr's cells, as the paper's 20 are not marked in the files.

What was found about the data set. Asari's natural sound and thalamic recordings match the paper's
counts exactly (305 probes in 39 cells; 93 probes in 14 cells). The data set holds no
voltage-clamp recordings, though the paper analyses 14 voltage-clamped cells. It holds 145
current-clamp A1 cells where the paper recorded 194, and 14 MGB cells where it recorded 16; every
cell folder of the zips is listed in Summary.mat. The 15 files of Summary.mat's fourth experiment
(white noise, natural sounds, random chords and TORCs) are outside the context design and are not
used. The MHT row of Table 1 (71 AM and 57 FM probes) cannot be formed from the files: in the MHT
ensembles only the natural sound is preceded by more than one fragment. In two files
(20051107-ha1-001-003 and -004) the trigger descriptions number the sequences 2, 4, 6, 8 while the
notes number them 1 to 4; the sequences are matched by content. The analysis code in `asari/Tools`
documents details the paper leaves open. The trial tables share the traces' clock.'''
nb['cells'][63]['source']=summ.splitlines(True)
json.dump(nb, open('reproduce_asari_2009.ipynb','w'), indent=1)
EOF
grep -n "—\|rather" reproduce_asari_2009.ipynb strf_wehr.ipynb wehr.py asari.py | head; cat entry.yaml | sed -n 12,18p; cat README.md
```

```
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_asari_2009.ipynb
  title: Reproducing Asari & Zador (2009) from CRCNS ac-1
  runtime_minutes: 35
helpers:
# Asari & Zador (2009) from CRCNS ac-1

Tests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) that can be
tested on [CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR): Hiroki Asari's whole-cell recordings
from rat primary auditory cortex with natural and synthetic sound ensembles, and his cell-attached
recordings from the auditory thalamus. The data set holds no voltage-clamp recordings (Figures 5
and 6). The STRF models on Michael Wehr's recordings (Figure 4) were not run in this attempt.

| Claim | Outcome |
|---|---|
| Counts of cells and probes (Table 1) | Partially reproduced |
| Low firing rates in A1, high in MGB | Partially reproduced |
| Trial-to-trial reliability, example and population | Reproduced |
[... 31 more lines not kept]
```

**Agent**

Now entry.yaml and README, then the final run.

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('entry.yaml').read()
s=s.replace('''  runtime_minutes: 35
helpers:
- asari.py''','''  runtime_minutes: 35
- path: strf_wehr.ipynb
  title: STRF and LN model performance on Wehr's A1 cells (Figure 4)
  runtime_minutes: 12
helpers:
- asari.py
- wehr.py''')
s=s.replace('''conditioning sounds, and how short it is in the thalamus. The voltage-clamp''','''conditioning sounds, how short it is in the thalamus, and how well STRF models of Michael
  Wehr's recordings predict responses. The voltage-clamp''')
open('entry.yaml','w').write(s)
r=open('README.md').read()
rep=[("The STRF models on Michael Wehr's recordings (Figure 4) were not run in this attempt.","The STRF models on Michael Wehr's recordings (Figure 4) are tested in a second notebook."),
("| Normalized context-dependent power decays with tau about 1 s | Partially reproduced |","| Normalized context-dependent power decays with tau about 1 s | Not reproduced |"),
("| Upper bound on prediction without context (0.51, tau 1.04 s) | Partially reproduced |","| Upper bound on prediction without context (0.51, tau 1.04 s) | Not reproduced |"),
("| STRF models predict under 20% at any window | Blocked: not run in the time of this attempt |","| STRF models predict under 20% at any window | Not reproduced |"),
("| Proportion significant by sound property | Partially reproduced |","| Proportion significant by sound property | Not reproduced |"),
("""  data set can import it.""","""  data set can import it.
- `strf_wehr.ipynb` and `wehr.py`: the STRF and LN encoding models of Figure 4 on Wehr's
  recordings (spectrograms, ridge regression over nine window lengths with 10-fold
  cross-validation, robust lowess nonlinearity); about 12 minutes.""")]
for a,b in rep:
    assert a in r, a; r=r.replace(a,b)
open('README.md','w').write(r)
EOF
grep -n "description" entry.yaml; rm -rf __pycache__; ls
```

```
5:description: Tests the findings of Asari and Zador (2009) on CRCNS ac-1, which holds Hiroki
README.md
asari.py
entry.yaml
reproduce_asari_2009.ipynb
requirements.in
requirements.lock.txt
strf_wehr.ipynb
wehr.py
```

**Agent calls Bash**

```bash
cd  timeout 600 python tools/entry.py check entries/asari-2009 2>&1 | tail -20
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/asari-2009; executed/asari-2009/.venv/bin/python - <<'EOF'
import nbformat, json
for f in ('reproduce_asari_2009.ipynb','strf_wehr.ipynb'):
    nb=nbformat.read(f, as_version=4)
    ch, nb2 = nbformat.validator.normalize(nb)
    nb2=nbformat.from_dict(nb2)
    for c in nb2.cells:
        if c.cell_type=='code': c.outputs=[]; c.execution_count=None
    nbformat.write(nb2, f)
    print(f, ch)
EOF
cd  date -u; time timeout 7000 python tools/entry.py all entries/asari-2009 2>&1 | tail -15; date -u
```

```
executed/asari-2009/.venv/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
reproduce_asari_2009.ipynb 0
strf_wehr.ipynb 0
Thu Nov 19 06:34:48 UTC 2026
Installed kernelspec registry-asari-2009 in executed/asari-2009/.venv/share/jupyter/kernels/registry-asari-2009
0 error(s)
pass  reproduce_asari_2009.ipynb  (1801 s)
pass  strf_wehr.ipynb  (687 s)

real	41m38.688s
user	111m58.307s
sys	12m17.417s
Thu Nov 19 07:16:27 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json, os
a=json.load(open(os.environ['TMPDIR']+'/dev_out.ipynb'))
b=json.load(open('executed/asari-2009/reproduce_asari_2009.ipynb'))
def outs(nb):
    d={}
    for c in nb['cells']:
        t=c['metadata'].get('tags') or []
        for x in t:
            if x.startswith('claim:'):
                d.setdefault(x,'')
                d[x]+=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    return d
A,B=outs(a),outs(b)
for k in B: print(k, A.get(k)==B[k])
for c in b['cells'][-1:]: print(''.join(''.join(o.get('text','')) for o in c['outputs']))
s=json.load(open('executed/asari-2009/strf_wehr.ipynb'))
for c in s['cells']:
    if c['cell_type']=='code' and 'claim' in str(c['metadata'].get('tags')):
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        print(t[:2500]); print('----')
EOF
```

```
claim:methods-recording-counts True
claim:a1-mgb-firing-rates True
claim:fig2-example-reliability True
claim:fig2-example-long-context True
claim:fig3a-proportion-significant True
claim:fig3a-significance-decay True
claim:fig3b-fractional-power-decay True
claim:timescale-longer-than-membrane True
claim:fig4-predictability-upper-bound True
claim:fig8a-proportion-by-property True
claim:fig8b-decay-by-property True
claim:fig8a-significance-fits True
claim:fig8c-relative-effects True
claim:fig8-natural-synthetic-probes-alike True
claim:fig9-mgb-fast-decay True
claim:fig9-example-first-bin True
claim:fig7-example-frequency-context True
claim:figs1-silence-probe True
total time (min): 29.9
peak memory (MB): 2003
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/asari-2009.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig8a-significance-fits','fig3b-fractional-power-decay','fig4-predictability-upper-bound'):
        print(cl['id'], [(e['quantity'], e['value']) for e in cl.get('expected',[])])
EOF
ls questions | grep -i asari; date -u
```

```
fig3b-fractional-power-decay [('decay size alpha1 of the normalized context-dependent power', 0.49), ('decay constant tau1', 1.04)]
fig4-predictability-upper-bound [('upper bound on model performance near probe onset (1 + alpha1, with alpha1 = -0.49)', 0.51), ('time constant of the approach to one', 1.04)]
fig8a-significance-fits [('amplitude tau1', 0.25), ('frequency tau1', 0.27), ('AM tau1', 0.17), ('FM tau1', 0.15), ('higher-order tau1', 0.13), ('amplitude alpha1', 0.23), ('frequency alpha1', 0.19), ('AM alpha1', 0.13), ('FM alpha1', 0.07), ('higher-order alpha1', 0.04)]
Thu Nov 19 07:16:59 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
P='attempts/asari-2009-03.yaml'
R=yaml.safe_load(open(P))
O={o['claim']:o for o in R['outcomes']}
def upd(cid, **kw):
    o=O[cid]
    for k,v in kw.items():
        if v is None: o.pop(k,None)
        else: o[k]=v
upd('methods-recording-counts', notes=(
 "Whether silence counts as a conditioning stimulus or not, 305 natural sound probes in 39 cells meet the "
 "criterion (at least two contexts, at least 4 effective repeats), and 93 MGB probes in 14 cells (at least 10 "
 "repeats), as in Table 1; these four counts match exactly. The data set holds no voltage-clamp recordings "
 "(Summary.mat lists four experiments, all current clamp or cell-attached), so the 29 voltage-clamp probes in 14 "
 "cells cannot be counted. 133 current-clamp cells have at least one probe meeting the criterion (39 natural, 96 "
 "synthetic, 2 in both), not 123. By ensemble, TORC 14 and MCN 27 cells match the paper; MHT and natural-variant "
 "files together give 40 cells against the paper's 39 MHT cells; DMR files give 15 cells against 6. Of the 17 DMR "
 "files, the 7 with DMR probes come from 6 cells, as in the paper; the other 10 (20060915-ha1-001-002, "
 "20060916-ha1-001-002, -ha2-001-002, -ha3-001-002, -ha3-002-002, -ha3-003-002, -ha4-001-002, -ha5-002-002, "
 "-ha5-002-003 and 20060917-ha1-002-002) test only a natural sound probe after DMR variants, in 9 cells, and are "
 "the probes that make most of the difference (133 less 9 is 124). Under the 'table1' reading (each set of "
 "conditioning stimuli for AM and FM, each probe once for amplitude, frequency and higher-order) the property "
 "totals are 95, 110, 96, 82 and 137, equal to the paper's; under 'class' they are 104, 120, 96, 82 and 354 and "
 "under 'probe' 95, 110, 39, 25 and 137. The Table 1 rows do not match under any reading: the MHT row has 14 AM "
 "tests and no amplitude, frequency or FM test (paper 25, 25, 71, 57), because in the 25 MHT-ensemble files with "
 "a natural sound every MHT fragment follows at most one other fragment (235 none, 171 one), so only the natural "
 "sound is a probe there."),
 deviations=[
  "The voltage-clamp counts are not tested; the data set holds no voltage-clamp recordings.",
  "The inclusion rule follows the authors' CxtDep.m, in the data set, for what the Methods leave open (the first "
  "\"Effective repeats\" presentations of each sequence, each context truncated to the smallest trial count over "
  "contexts, a probe kept with at least two distinct contexts).",
  "The sets of conditioning stimuli for the property columns are taken from the file's notes where they list the "
  "variants of each property (the six files of a natural probe after MHT variants) and are otherwise formed from the "
  "stimulus parameters and descriptions (asari.py, property_classes), as no passage of the paper lists them. Three "
  "readings of what is counted are shown."])
o=O['a1-mgb-firing-rates']
o['notes']=(o['notes'].replace("Hz. The MGB evoked mean is outside 11.4 +/- 1.14 under every reading, and above 5 Hz only with\n    the lower threshold.","")
 )
o['notes']=("Measured values are for the reading on which the outcome rests (A1 detector at 15 mV, MGB detector at half the "
 "authors' threshold, whole intersequence silences). A1 over 133 cells, spontaneous 0.481 +/- 0.597 Hz and evoked "
 "0.547 +/- 0.677 Hz with the 15-mV detector (both means within 10%); 0.533 and 0.608 at 10 mV, 0.406 and 0.457 at "
 "20 mV; below 1 Hz under every reading. MGB over 14 cells, the authors' detector gives spontaneous 0.551 +/- 1.236 "
 "and evoked 4.99 +/- 11.45 Hz; half its threshold gives 0.768 +/- 1.309 (within tolerance of 0.78) and 7.07 +/- "
 "12.25 Hz; a noise-based threshold of 4 SD gives 2.84 +/- 6.36 and 18.02 +/- 14.86 Hz. The MGB evoked mean is "
 "outside 11.4 +/- 1.14 under every detector, and above 5 Hz with the two lower thresholds. Leaving out the first "
 "second of each silence changes the spontaneous means by at most 0.04 Hz. Under the authors' detector one MGB cell "
 "fires at 43 Hz during sounds and nine below 1.5 Hz. The partial rule (A1 below 1 Hz, MGB evoked above 5 Hz) holds "
 "under the two lower MGB thresholds and not under the authors' own detector (4.99 Hz).")
o['deviations'][1]=("MGB spikes by the authors' automatic detector in the data set (GetSpikes.m, ExtractSpikes, a high-pass FIR "
 "filter and a threshold at two thirds of the largest filtered value) and, as variants, half that threshold and a "
 "threshold of 4 noise SDs (SD = median absolute value / 0.6745 of the filtered trace, Quiroga et al. 2004). The "
 "Methods say only \"a high-pass filter and thresholding\".")
upd('fig3b-fractional-power-decay', outcome='not_reproduced', notes=(
 "Measured values are for silence counted, running probes, 0 to 4 s. The size is within tolerance under every "
 "reading (0.445 to 0.468 against 0.49 +/- 0.049) and the constant is outside 1.04 +/- 0.104 s under every reading "
 "(1.29 to 1.78 s; 1.29 to 1.33 s without silence as a context). The criterion has no partial rule, so the outcome "
 "is not reproduced. Q(t) is 0.626 at 0.1 s and 0.191 at 1 s, the value of the paper's curve at 1 s (0.188), 0.049 "
 "at 2 s, and rises to 0.13 at 4 s, which lengthens the fitted constant."))
upd('fig4-predictability-upper-bound', outcome='not_reproduced', notes=(
 "Measured values are for the main reading (denominator smoothed over [0, 2t], silence counted, running probes, 0 to "
 "4 s). No reading puts both values within tolerance, and the criterion has no partial rule. Smoothed, 1 + alpha is "
 "0.428 to 0.490 and tau 1.66 to 2.81 s over the readings that converge (the two all-probes readings fitted to 6 s "
 "stop at the bound of 100 s); unsmoothed, 1 + alpha is 0.499 to 0.536, within 0.51 +/- 0.051, and tau 1.46 to 1.92 "
 "s. The ratio at 0.1 s is 0.742 smoothed and 0.542 unsmoothed (0.831 and 0.589 without silence). The bound is below "
 "1 near the onset and approaches it over seconds under every reading, with a constant longer than 1.04 s."))
o=O['fig4-strf-performance-low']
for k in ('blocked_by',): o.pop(k,None)
o.update(outcome='not_reproduced', notebook='strf_wehr.ipynb', output='claim:fig4-strf-performance-low', measured=0.148,
 notes=("Measured value is the largest mean validation performance of the STRF model over the nine windows (10-ms Hann "
 "window, contiguous folds). 16 of Wehr's cells are used (the 10 of 2002 and 6 of 2003 with at least two trials of a "
 "natural sound); the paper's 20 are not marked in the files. Under the four readings that score every bin, the mean "
 "validation performance is at most 0.148 for STRF and 0.111 for LN at every window, below 0.22, while the training "
 "estimates reach 0.245 to 0.268 (STRF) and 0.281 to 0.311 (LN). In each of those four readings the one-sided "
 "Wilcoxon test finds that STRF improves from 180 to 4052 ms (p = 0.0026, 0.037, 0.0011, 0.029; mean 0.115 at 180 "
 "ms to 0.147 at 4052 ms with 10-ms Hann and contiguous folds, most of it by 548 ms); for LN p is 0.017 and 0.015 "
 "with contiguous folds and 0.11 and 0.25 with folds by stimulus. Scoring only bins at least 4052 ms after onset "
 "removes the significant change (STRF p 0.065 and 0.052) but the mean then exceeds 0.22 (1.26 and 1.14), as one "
 "cell has negative predictable power in 6 of 10 folds. So no reading meets both conditions. The LN model is "
 "better than STRF on training data (+0.013 to +0.049) and worse on validation data (-0.025 to -0.34). The Friedman "
 "variant gives STRF p 0.016 to 0.31. No result uses random draws."),
 assumed=True,
 deviations=[
  "Cells: every Wehr cell with at least two trials of a natural sound (16), as Eq. 52 needs repeats; the paper's 20 "
  "cells of Machens et al. (2004) cannot be identified from the files.",
  "From the authors' STRFanalysis.m in the data set: per-trial mean subtraction, fitting to the trial-averaged "
  "response, the spectrogram centred per frequency, 10 contiguous folds, one ridge value for all folds chosen by the "
  "mean linear validation score, the LN model on that filter, Eq. 53 per fold (LNperformance).",
  "Assumed: 17 frequencies 400 * 2^(k/3) Hz for k = 0 to 16 (logspectrogram.m's rule would give 18); 4-ms response "
  "bins (Wehr's traces are at 4 kHz, so the 10-kHz reading does not exist); spectrogram history before onset set to "
  "the stimulus mean; a ridge grid of 33 values from 1e-6 to 1e2 times the mean eigenvalue; one lowess fit plus five "
  "robustness iterations.",
  "The Wilcoxon test is the one the claims file fixes; the outcome rests on it."])
upd('fig8a-proportion-by-property', outcome='not_reproduced', measured=[58,62,41,29,64], notes=(
 "Under the 'table1' reading, whose denominators equal the paper's (95, 110, 96, 82, 137), significant tests are "
 "amplitude 58 of 95 (0.611, 30 cells), frequency 62 of 110 (0.564, 34 cells), AM 41 of 96 (0.427, 26 cells), FM 29 "
 "of 82 (0.354, 24 cells) and higher-order 64 of 137 (0.467, 27 cells). Only higher-order is within tolerance. "
 "Amplitude is above frequency, but AM is above FM and below higher-order, so the paper's order fails and the partial "
 "rule does not hold. The variants keep the order and would be partial: 'class' gives 61 of 104, 70 of 120, 41 of "
 "96, 29 of 82 and 109 of 354 (frequency within tolerance), 'probe' 58 of 95, 62 of 110, 25 of 39, 16 of 25 and 64 "
 "of 137 (higher-order within tolerance). The outcome rests on the reading of Table 1."),
 deviations=[
  "Assumed what is counted. 'table1': each probe with each set of conditioning stimuli that differ in AM or in FM is "
  "a test, and each probe is counted once for amplitude, frequency and higher-order properties (significant when any "
  "of its sets is). The criterion says the probes of each property follow the columns of Table 1, and this is the "
  "only reading run whose totals equal all five columns; 'class' (every set) and 'probe' (every probe once) are shown "
  "and give partially reproduced.",
  "The sets of conditioning stimuli come from the file's notes where they list the variants and are otherwise formed "
  "from the stimulus descriptions (TORC and DMR \"amplitude\", \"bandwidth\" or \"frequency\" variants) and parameters "
  "(attenuation; f0, df, ff; AMrange or AMmean with AMstd; FMrange, FMstd; a natural sound with the modulated coloured "
  "noise made from it), as the paper gives no list.",
  "Silence and unrelated fragments are left out of the contexts (Methods, Stimulus design, paragraph 2)."])
upd('fig8b-decay-by-property', measured=[1.387,0.799,0.109,0.278,0.254,0.395,0.501,0.866,0.214,0.758], notes=(
 "Under the 'table1' reading, fitted from 0 to 4 s over running probes, tau is 1.39 s (amplitude), 0.80 s "
 "(frequency), 0.109 s (AM, within tolerance), 0.28 s (FM) and 0.25 s (higher-order); only AM is within tolerance. "
 "The partial pattern holds (amplitude and frequency above 0.4 s, AM, FM and higher-order below 0.3 s), under the "
 "'class' (1.35, 0.84, 0.109, 0.28, 0.23 s) and 'probe' (1.39, 0.80, 0.108, 0.114, 0.25 s) readings too. Sizes 0.40, "
 "0.50, 0.87, 0.21 and 0.76 against 0.57, 0.54, 0.86, 0.64 and 0.52. Fitting to the shortest probe length gives the "
 "same values."),
 deviations=["Rests on the reading of the tests assumed in fig8a-proportion-by-property; a probe counted once has the "
  "mean of its sets' power curves."])
upd('fig8a-significance-fits', measured=[0.275,0.295,0.198,0.137,0.118,0.130,0.155,0.067,0.013,0.078], notes=(
 "One exponential with the constant at each property's mean noise floor, 0 to 4 s, running probes, 'table1' reading. "
 "Sizes 0.130, 0.155, 0.067, 0.013 and 0.078 (paper 0.23, 0.19, 0.13, 0.07, 0.04) and constants 0.275, 0.295, 0.198, "
 "0.137 and 0.118 s (paper 0.25, 0.27, 0.17, 0.15, 0.13). No property has both values within tolerance under any "
 "reading or seed, and the sizes are not in the printed order under any reading ('class' 0.121, 0.150, 0.067, 0.013, "
 "0.035; 'probe' 0.130, 0.155, 0.149, 0.043, 0.078), so the partial rule fails too. The noise floors are 0.0036, "
 "0.0025, 0.0021, 0.0021 and 0.0060 ('table1'; for a probe counted once 1 - prod(1 - floor of each set)) against "
 "0.0028, 0.0023, 0.0023, 0.0021 and 0.0036. The five seeds give the same values to the third decimal, and holding "
 "the sizes non-negative changes nothing."))
upd('fig8c-relative-effects', seed_sensitive=True, notes=(
 "Area under Q(t) from 0 to 4 s relative to natural sounds. Under the claim's seed no reading meets the full "
 "criterion, and under every reading the point estimates fall in the claimed pattern. Resampling probes ('table1' "
 "tests, silence counted, natural area 0.762): amplitude 0.73 (0.62 to 0.84), frequency 0.63 (0.55 to 0.72), AM 0.15 "
 "(0.11 to 0.19), FM 0.13 (0.10 to 0.17), higher-order 0.36 (0.31 to 0.42); with silence not counted in the natural "
 "denominator (area 0.621), amplitude 0.89 (0.76 to 1.04) reaches 1 and frequency 0.77 (0.67 to 0.90) does not. "
 "Resampling trials within each probe and context, the amplitude and frequency intervals lie above 1 (1.11 to 1.27, "
 "1.05 to 1.16) and AM and FM below 1; the higher-order upper bound is 1.00 under the claim's seed, so it fails, and "
 "0.99 to 1.00 under the other four seeds, which meet the full criterion: the outcome is seed sensitive. These trial "
 "intervals do not contain their own point estimates (amplitude 0.73 against 1.11 to 1.27), as drawing trials with "
 "replacement duplicates trials and biases the power estimates; the 'class' and 'probe' readings give the same "
 "pattern."),
 deviations=[
  "Both readings of a sample are run: probes (1000 drawn with replacement, 200 times) and trials (the trials of every "
  "probe and context drawn with replacement, 200 times, power at 1-kHz points in 50-ms bins), with the natural sound "
  "denominator with and without silence as a context.",
  "Rests on the reading of the tests assumed in fig8a-proportion-by-property."])
upd('fig8-natural-synthetic-probes-alike', notes=(
 "Fisher's exact test per property, Bonferroni over the four properties tested with both probe types, 'table1' "
 "reading: amplitude natural 27 of 45 against synthetic 31 of 50 (odds ratio 0.92, p = 1.0), frequency 23 of 46 "
 "against 39 of 64 (0.64, p = 0.33), AM 33 of 82 against 8 of 14 (0.51, p = 0.26), higher-order 29 of 61 against 35 "
 "of 76 (1.06, p = 0.87); no difference, and none under the 'class' or 'probe' readings. FM was tested with natural "
 "probes only, and AM has 14 synthetic-probe tests in 2 cells, so the test has little power for AM and none for FM. "
 "The labels follow the files: in the 25 MHT-ensemble files with a natural sound, every MHT fragment follows at most "
 "one other fragment, so only the natural sound is a probe there; the paper's 71 MHT AM and 57 MHT FM probes cannot "
 "be formed from the data set."))
upd('fig9-mgb-fast-decay', notes=(
 "Measured values are for the authors' detector with the bin's time at its start. Over 93 probes in 14 cells the "
 "mean SD of PSTHs is 6.45 spike/s in the first 100-ms bin and 2.04 in the second. The fit gives tau 55 ms (61 ms "
 "with half the threshold, 54 ms with the 4-SD noise threshold), below 0.1 s, with size 5.18 (bin start) or 12.87 "
 "spike/s (bin centre) and constant 1.27 spike/s. The mean SD after 0.5 s is 1.27, 1.38 and 3.24 spike/s under the "
 "three detectors, outside 2.0 +/- 25% under each, so the plateau condition fails; tau is far below 0.3 s, so the "
 "claim is not not_reproduced by the criterion. No partial rule is given; it is partial because the fast decay holds "
 "and the plateau does not match."),
 deviations=["MGB spikes by the authors' detector in the data set (GetSpikes.m), half its threshold, and a threshold "
  "of 4 noise SDs.",
  "PSTH bins start at the probe onset and only whole bins inside a probe are kept, as in CxtDep.m (psth); the "
  "population average at each bin is over the probes that have it."])
upd('fig9-example-first-bin', notes=(
 "The Figure 9A design (the seven-fragment sequence, three contexts) is in one MGB file, 20071010-ha2-003-003, with "
 "12 such probes. Four have a first-bin SD at least twice every later bin's (for example probe 4, 31.4 spike/s "
 "against at most 7.2 in bins 2 to 6), under all three detectors. Over all 93 probes, 35 (authors' detector), 45 "
 "(half threshold) or 40 (4-SD threshold) do."))
upd('fig7-example-frequency-context', notebook='reproduce_asari_2009.ipynb', output='claim:fig7-example-frequency-context', notes=(
 "No recording matches the criterion's description (a DMR frequency-variant cell with contexts in 0.625-2.5, 2.5-10 "
 "and 10-40 kHz and a natural sound probe); the notebook lists every DMR frequency-variant file. The five with a "
 "natural sound probe use six 2-octave bands from 250-1000 to 8000-32000 Hz, in two sets of six fragments; in two of "
 "their ten frequency tests the last significant period ends after 3.6 s (4.58 s in 20060916-ha4-001-002, 4.83 s in "
 "20060916-ha5-002-002), with those bands. The example's bands occur only in other DMR files, as one band "
 "(2500-10000 Hz) or within others (625-2500 with 10000-40000, 2500-40000), never as the three conditioning stimuli "
 "of a natural sound probe. The criterion says the claim is not testable when no cell matches. The kHz values may be "
 "axis ticks of Figure 7A, not bands."))
# findings
F=R['findings']
for f in F:
    if f['statement'].startswith('Question for the authors. Which sets of conditioning stimuli'):
        f['statement']=("Question for the authors. What is counted in each column of Table 1 and Figure 8? With the "
         "sets of conditioning stimuli formed here, counting each probe with each set reproduces the AM (96) and FM "
         "(82) totals, and counting each probe once reproduces the amplitude (95), frequency (110) and higher-order "
         "(137) totals; neither reproduces all five, and the proportions keep the paper's order under each but not "
         "under the mix. Was each probe of the natural-and-noise ensembles counted once, or once per natural-noise pair?")
F.insert(2, dict(kind='other', about='data', statement=(
 "The MHT row of Table 1 (25 amplitude, 25 frequency, 71 AM and 57 FM probes) cannot be formed from the data set. In "
 "the 25 MHT-ensemble files with a natural sound, every MHT fragment follows at most one other fragment, so only the "
 "natural sound has two conditioning stimuli; the data set gives 14 AM tests on MHT probes (2 cells) and none for "
 "the other properties. The paper's 71 and 57 equal the per-set natural-probe tests of the 19 sixteen-MHT files "
 "less one per file (76 - 19 = 57), plus the 14 for AM, which suggests the row split counts tests differently.")))
F.append(dict(kind='selection_undocumented', about='data', statement=(
 "Nothing in Wehr's recordings marks the 20 cells of Machens et al. (2004) used for Figure 4. wehr/Summary.mat lists "
 "two experiments citing that paper; 9 of their cells have only single presentations of each natural sound, which "
 "the predictable power of Eq. 52 cannot use, leaving 16.")))
F.append(dict(kind='code_mismatch', about='paper', statement=(
 "wehr/Tools/logspectrogram.m with the defaults of STRFanalysis.m gives 18 frequency bins up to 20.3 kHz and a "
 "Hamming window of twice the time bin, where the Methods give 17 bins from 0.40 to 22 kHz and the claims file "
 "a Hann window.")))
R['verifications']=[dict(date='2026-11-19', kind='agent',
 by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
 reviewed=("Round 1: the first executed notebook with the conclusion cells and the summary removed, the helper module "
  "asari.py and the claims file, with the paper's full text. The verifier read the archive's zips and the "
  "authors' CxtDep.m and tested kw_significance, frac_power, smooth_0_2t, fit_select and psth_sd on synthetic "
  "inputs. It had no attempt record."),
 results=[])]
V=R['verifications'][0]['results']
def v(c, agrees, outcome, reason, response): V.append(dict(claim=c, agrees=agrees, outcome=outcome, reason=reason, response=response))
v('methods-recording-counts', True, 'partially_reproduced',
 "Cell 10 matches 305 natural probes in 39 cells and 93 MGB probes in 14 cells, under both silence readings. It finds "
 "133 A1 cells meeting the criterion, not 123, and the synthetic counts don't match (MHT 26 cells vs 39, DMR 15 vs 6; "
 "Table 1 rows differ). The voltage-clamp counts can't be tested. The criterion asks for the probes that make the "
 "difference to be listed; they aren't (B7). The natural-sound rows are AM 82 and FM 82 where the paper has 25 each, "
 "and the MHT rows AM 14 and FM 0 where it has 71 and 57; most likely the MHT stimuli are labelled natural (B1).",
 "The cell now lists the files of the DMR and natural-variant ensembles: the 10 DMR files of 20060915 to 20060917, in "
 "9 cells, test only a natural probe and are the probes that make most of the 133 against 123; the 7 DMR files with "
 "DMR probes are 6 cells, as in the paper. MHT and natural-variant files together are 40 cells (paper 39 MHT). On "
 "B1, the labels follow the files: in the 25 MHT-ensemble files with a natural sound no MHT fragment has two "
 "conditioning stimuli (printed), so those tests are natural-probe tests; counted once per probe the natural row has "
 "AM 25 and FM 25 as in the paper. The MHT row cannot be formed from the data set; this is now a finding. Table 1 is "
 "shown under three readings, and the 'table1' reading gives all five column totals. The sets of the six files whose "
 "notes list the variants now follow the notes (the AM set had included the amplitude variants). Outcome unchanged.")
v('a1-mgb-firing-rates', True, 'partially_reproduced',
 "No reading puts all four means within tolerance, because MGB evoked is at most 7.07 Hz against 11.4 +/- 1.14. The "
 "A1 15-mV reading (0.481 / 0.547 Hz) and the half-threshold MGB reading (spontaneous 0.768, evoked 7.07 > 5 Hz) "
 "meet the partial rule. MGB spikes look under-detected (threshold at two thirds of the largest filtered value), "
 "which lowers the rates (B6). Of the three A1 thresholds tried, only 15 mV fits (B12).",
 "Added a noise-based MGB detector (4 SD, the SD from the median absolute value, Quiroga et al. 2004): evoked 18.02 "
 "Hz and spontaneous 2.84 Hz, both outside tolerance, so no detector puts the MGB means within tolerance. Outcome "
 "unchanged.")
v('fig2-example-reliability', True, 'reproduced',
 "Mean over pairs of trials, averaged over cells, is 0.310 +/- 0.092 (paper 0.31 +/- 0.09). The matched cell gives "
 "0.611 and its probe 0.737. The example cell is chosen by the very correlation values being tested, so those values "
 "match by construction; the population value decides the claim (B11).", "No change.")
v('fig2-example-long-context', True, 'reproduced',
 "Matched probe (20051222-ha1-001-002, probe 4, contexts [0,2,3], 6 repeats): significant periods up to 1.60 s, none "
 "in 2.2-3.6 s, then periods from 3.97 s.", "No change.")
v('fig3a-proportion-significant', True, 'reproduced',
 "Silence counted, all-probes reading: 186 of 305 (within 204 +/- 20.4), 0.610, late fraction 0.255 (within 0.237 "
 "+/- 0.024). Noise floor 0.00281 matches the paper's chance level. This holds narrowly; the probes-running reading "
 "gives 0.270, which is out. Ties are broken by trial order with no tie correction, as in the authors' KWtest (B9); "
 "runs of 51 or more points match CxtDep.m (B10).",
 "Added the trace scale (0.0061 and 0.0153 mV per step) and the fraction of tied values per time point over the "
 "natural probes (median 0.025, range 0.007 to 0.134) to the data check. Outcome unchanged.")
v('fig3a-significance-decay', True, 'partially_reproduced',
 "No reading has all four values within tolerance. Two exponentials with the slow constant between 0.5 and 2 s are "
 "selected in many readings (e.g. 0.159/0.26 s and 0.072/1.05 s).", "No change.")
v('fig3b-fractional-power-decay', False, 'not_reproduced',
 "alpha is 0.45-0.47 but tau is 1.29-1.78 s in every reading (tolerance 1.04 +/- 0.10). The criterion has no partial "
 "clause.",
 "Changed to not_reproduced: the criterion gives only a reproduced rule, and the constant, half of what it tests, is "
 "outside tolerance under every reading.")
v('timescale-longer-than-membrane', True, 'reproduced',
 "Lag below 1/e is 71 ms for noise and 77/75 ms for spontaneous activity; lag below 0.1 is 115-121 ms. All are under "
 "150 ms and under 347 ms.", "No change.")
v('fig4-predictability-upper-bound', False, 'not_reproduced',
 "1+alpha is within tolerance in some readings (0.50, 0.53), but tau is never within 1.04 +/- 0.10 (1.46-2.8 s; two "
 "fits stop at the 100-s bound).",
 "Changed to not_reproduced, as the criterion has no partial rule and tau is outside tolerance under every reading. "
 "The notes say that the two all-probes fits to 6 s stop at the 100-s bound (B8).")
v('fig4-strf-performance-low', True, 'blocked',
 "Blocked only \"for time\", which is not a blocking reason. The archive has Wehr's data: wehr/Results holds the cell "
 "folders, plus Tools and Stimuli. The claim is testable.",
 "Tested in a new notebook, strf_wehr.ipynb, with the helper wehr.py, on the 16 Wehr cells with repeated natural "
 "sounds: not_reproduced. Validation performance is at most 0.148 at every window, but the one-sided Wilcoxon test "
 "finds that STRF improves from 180 to 4052 ms in every reading that meets the level bound.")
v('fig5-example-conductances', True, 'blocked',
 "Confirmed in the archive: the data set's Methods.txt describes current clamp only, with a K-gluconate internal "
 "solution. No Summary.mat experiment is voltage clamp, and all 151 files read are in mV.", "No change.")
v('fig6-conductance-decay', True, 'blocked', "Same evidence as fig5.", "No change.")
v('fig8a-proportion-by-property', True, 'partially_reproduced',
 "Only frequency (70/120) is within tolerance, and its denominator is wrong. The proportion order holds under both "
 "readings. The main reading counts each (probe, class) pair as a test: higher-order 354 (paper 137), amplitude 104 "
 "(95), frequency 120 (110). Counting each probe once gives exactly 95, 110 and 137, so that is the reading the "
 "criterion's \"columns of Table 1\" points to (B2).",
 "Changed to not_reproduced. The main reading is now 'table1': each set for AM and FM (96 and 82, as in Table 1) and "
 "each probe once for amplitude, frequency and higher-order (95, 110, 137), the only reading whose totals equal all "
 "five columns. Under it only higher-order (64 of 137) is within tolerance and AM (0.427) is below higher-order "
 "(0.467), so the order fails. The 'class' and 'probe' variants keep the order and would be partial; the outcome is "
 "marked as resting on the assumption.")
v('fig8b-decay-by-property', True, 'partially_reproduced',
 "Only AM's tau (0.112 s) is within tolerance. The partial pattern holds: amplitude 1.35 s and frequency 0.84 s are "
 "above 0.4 s; AM 0.11, FM 0.28 and higher-order 0.23 s are below 0.3 s. Run only on the per-class tests (B2).",
 "Re-run under the three readings; under 'table1' tau is 1.39, 0.80, 0.109, 0.28 and 0.25 s, and the partial pattern "
 "holds under all three. Outcome unchanged.")
v('fig8a-significance-fits', True, 'not_reproduced',
 "No property has both values within tolerance. The sizes aren't in the paper's order (amplitude 0.121 < frequency "
 "0.150; FM 0.013 < higher-order 0.035), so the partial rule fails too. Run only on the per-class tests (B2).",
 "Re-run under the three readings; no property has both values within tolerance and the sizes are out of order under "
 "each. Outcome unchanged.")
v('fig8c-relative-effects', True, 'partially_reproduced',
 "The point estimates follow the pattern, but the amplitude (0.58-0.78) and frequency (0.55-0.73) intervals don't "
 "reach 1. The natural-sound denominator uses only the silence-counted reading while the synthetic tests leave silence "
 "out; the silence-not-counted reading would scale the ratios by about 1.37 and could move the claim to reproduced. "
 "The trial-resampling reading the criterion names was also not run (B3).",
 "Added the silence-not-counted denominator (area 0.621; amplitude 0.89, 0.76 to 1.04, reaches 1, frequency 0.77, "
 "0.67 to 0.90, does not) and the trial-resampling reading, under the three readings of the tests. No reading meets "
 "the full criterion under the claim's seed; the trial reading meets it under the other four seeds, so the outcome "
 "stays partially_reproduced with seed_sensitive set. The trial intervals exclude their own point estimates, which "
 "the notes report.")
v('fig8-natural-synthetic-probes-alike', False, 'blocked',
 "Cell 36 finds no difference, but its natural/synthetic split contradicts Table 1. FM is \"only natural (82)\" where "
 "the paper has 57 MHT probes, and AM has 14 synthetic where the paper has 71. Mixing the labels pushes the test "
 "toward finding no difference. Testable once the labels are fixed.",
 "Kept reproduced and the disagreement recorded. The labels follow the files: in the 25 MHT-ensemble files with a "
 "natural sound, no MHT fragment follows more than one other fragment (printed: 235 none, 171 one), so the only "
 "probe tested with MHT conditioning stimuli there is the natural sound, and the data set holds 14 MHT-probe AM tests "
 "and no MHT-probe FM test. The paper's MHT row cannot be formed from the files (a finding). Under every reading no "
 "property differs; the notes say the test has little power for AM and none for FM.")
v('fig9-mgb-fast-decay', True, 'partially_reproduced',
 "tau is 55-61 ms, below 0.1 s, so the tau condition passes. The level after 0.5 s is 1.27-1.38 spike/s, more than "
 "25% below the paper's kappa of 2.0, so the plateau condition fails. The plateau test isn't printed; MGB spikes look "
 "under-detected, which lowers kappa and alpha (B6).",
 "The plateau test is now printed for each detector, with a noise-based 4-SD detector added: plateau 1.27, 1.38 and "
 "3.24 spike/s, outside 1.5 to 2.5 under all three, tau 54 to 61 ms. Outcome unchanged.")
v('fig9-example-first-bin', True, 'reproduced',
 "4 of the 12 probes with the Figure 9A design have a first-bin SD at least twice every later bin's (e.g. 31.4 against "
 "at most 7.2). Over all 93 probes the fraction is 35/93.", "Shown under the added detector too (4 of 12). No change.")
v('fig7-example-frequency-context', True, 'blocked',
 "The notebook contains no search for the example cell. The data set has DMR frequency/bandwidth-variant files, so a "
 "match may exist.",
 "Added a section that lists every DMR frequency-variant file, the band of each fragment and, for each frequency test, "
 "the bands of its conditioning stimuli and its significant periods. No natural probe follows the example's bands; "
 "outcome stays blocked, now with the search shown.")
v('figs1-silence-probe', True, 'reproduced',
 "24 silence probes in 21 cells have a significant period starting within 0.5 s. Stimulus-related power first falls "
 "below 10% of its onset value at 0.72 s. The 10% threshold is crossed on a noisy curve, and the mean over 1.1-2.5 s "
 "is 13% of the onset value; the criterion is met literally (B13).", "No change.")
yaml.safe_dump(R, open(P,'w'), sort_keys=False, width=100, allow_unicode=True)
PYEOF
python3 $TMPDIR/rec.py && grep -c "" attempts/asari-2009-03.yaml; date -u
```

```
674
Thu Nov 19 07:18:51 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
P='attempts/asari-2009-03.yaml'; R=yaml.safe_load(open(P))
O={o['claim']:o for o in R['outcomes']}
O['a1-mgb-firing-rates']['notes']=O['a1-mgb-firing-rates']['notes'].replace('by at most 0.04 Hz','by at most 0.05 Hz')
for v in R['verifications'][0]['results']:
    if v['claim']=='methods-recording-counts':
        v['response']+=(" The data check now lists the 15 files of Summary.mat's fourth experiment (white noise, natural "
          "sounds, random chords and TORCs, outside the context design) and shows that every cell folder of the zips "
          "that holds a recording file is listed in Summary.mat (159 and 159) (B15). The dead code in the cell is "
          "removed (B14).")
yaml.safe_dump(R, open(P,'w'), sort_keys=False, width=100, allow_unicode=True)
EOF
timeout 900 python tools/entry.py check entries/asari-2009 2>&1 | grep -v Warning | tail -15; grep -n ": .*—\|rather" attempts/asari-2009-03.yaml | head
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  ls tools | head -40; grep -ln "attempt.schema" tools/*.py | head
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
datasets.py
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def main\|argparse\|add_argument\|check" tools/build_site.py | head -20; python3 - <<'EOF'
import json, yaml, jsonschema
s=json.load(open('schemas/attempt.schema.json'))
r=yaml.safe_load(open('attempts/asari-2009-03.yaml'))
r=json.loads(json.dumps(r, default=str))
errs=list(jsonschema.Draft202012Validator(s).iter_errors(r))
for e in errs[:10]: print(e.path, e.message[:200])
print(len(errs))
EOF
```

```
36:import argparse
244:        last = (body.get("checks") or [None])[-1]
247:            "check": None if last is None else {"ready": bool(last.get("ready")), "date": str(last.get("date"))},
260:        last = (data.get("checks") or [None])[-1]
264:            "check": None if last is None else {"ready": bool(last.get("ready")), "date": str(last.get("date"))},
462:    (papers/manifest.yaml), each claims file's last check, and each attempt's open questions."""
465:    checks, questions, items, paper_checks, paper_questions = {}, {}, {}, {}, {}
469:        last = ((load_yaml(path) or {}).get("checks") or [None])[-1]
473:            checks[key] = found
475:        had = paper_checks.get(paper_key(path))
476:        paper_checks[paper_key(path)] = found if had is None else {
487:    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions,
488:            "question_items": items, "paper_checks": paper_checks, "paper_questions": paper_questions}
569:    (docs/protocol.md, "Repeat attempts"), and list the earlier findings it found fixed or could not check."""
586:                     for f in rec["findings"] if f["status"] in ("fixed", "not_checked")],
608:    ("elsewhere"), and the registry's checks that the dataset is the paper's data ("link"), which are
628:    The registry's own checks that a dataset is the data behind its paper (claims of kind `link`) are not here:
629:    they are a step of the work, not a result of the paper. Each is still in the list of claims, marked as a check
660:# The overview's most reproduced attempts: verified ones only, so that an unchecked attempt cannot top the list, and
670:PIPELINE_STEPS = [("paper", "Paper"), ("claims", "Claims"), ("check", "Claims check"),
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  timeout 600 python tools/entry.py handover entries/asari-2009 2>&1 | tail -3; ls executed/asari-2009/ executed/asari-2009/handover 2>/dev/null; date -u
```

```
wrote executed/asari-2009/handover
executed/asari-2009/:
handover
reproduce_asari_2009.ipynb
result.json
strf_wehr.ipynb

executed/asari-2009/handover:
asari-2009.yaml
asari.py
reproduce_asari_2009.ipynb
strf_wehr.ipynb
wehr.py
Thu Nov 19 07:19:31 UTC 2026
```

**Agent**

I've revised the attempt for every point in the round-1 report. `tools/entry.py all` passed: the main notebook ran in 30 min and the new STRF notebook in 11 min. `check` reports 0 errors, the record validates against the schema, and the handover is rebuilt. Round 1 is recorded under `verifications`, with the verifier's reasons in its own words and a `response` for each claim.

**Outcome changes**
- **fig3b-fractional-power-decay** and **fig4-predictability-upper-bound**: partially reproduced → **not reproduced**. I followed the verifier: neither criterion has a partial rule, and τ is out of tolerance under every reading.
- **fig4-strf-performance-low**: blocked → **not reproduced**, in a new notebook (`strf_wehr.ipynb`, helper `wehr.py`). Validation performance stays at or below 0.148 at every window, but the Wilcoxon test finds a significant STRF improvement from 180 ms to 4052 ms in every reading that meets the level bound. This rests on assumptions: 16 cells are used, because the paper's 20 are not marked in the files. A subagent built this notebook; I checked its outputs against the criterion but did not read its code line by line.
- **fig8a-proportion-by-property**: partially reproduced → **not reproduced**, marked as assumed. Following the verifier's point B2, the main reading now counts each set of conditioning stimuli for AM and FM and each probe once for the other three properties. It is the only reading whose totals equal all five Table 1 columns (95, 110, 96, 82, 137). Under it, AM (0.427) falls below higher-order (0.467), so the paper's order fails. The other two readings keep the order and are shown as variants.
- **fig8c-relative-effects** stays partially reproduced but is now `seed_sensitive`. I added the silence-not-counted denominator and the trial-resampling reading. No reading meets the full criterion under the claim's seed; the trial reading does under the other four seeds. The trial intervals do not contain their own point estimates, because resampling trials with replacement biases the power estimates; the notes say so.

**Corrections and added outputs**
- **Labelling (B1):** I kept the labels and recorded the disagreement. In the 25 MHT-ensemble files with a natural sound, no MHT fragment ever follows more than one other fragment, so the natural sound is the only probe there. The paper's MHT row of Table 1 cannot be formed from the files, and that is now a finding. fig8-natural-synthetic-probes-alike stays reproduced, against the verifier's "blocked", and its notes say the test has little power for AM and none for FM.
- **Property sets:** where a file's notes list the variants, those lists are now used. This fixes an AM set that wrongly included the amplitude variants.
- **MGB detector (B6):** I added a noise-based 4-SD detector. MGB evoked is then 18.0 Hz, still outside tolerance. The fig9 plateau test is printed for all three detectors and fails under each.
- **Recording counts (B7):** the 10 DMR files from 2006-09-15 to 17 (9 cells) test only natural probes and account for most of the 133 against 123 cells.
- **Data check:** it now shows the trace scale, the fraction of tied values, the 15 files of Summary.mat's fourth experiment, and that every cell folder of the zips holding a recording file is listed in Summary.mat.
- **fig7:** a search section now lists every DMR frequency-variant file. No natural probe follows the example's bands, so the claim stays blocked.
- **Other:** dead code removed; the fig4 fits stopping at the 100-s bound are noted; README, entry.yaml, summary and findings updated, including two new findings on Wehr's data and one updated question for the authors.

**Not done**
- No question was added to `questions/asari-2009.yaml`, because the verifier reported no place where the claims file misreads the paper.

## End of run

63 turns, 182 minutes, $14.59 at API prices, result: success.
