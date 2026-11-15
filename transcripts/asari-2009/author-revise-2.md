# asari-2009 · author-revise-2 · run 43737263281

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls entries/asari-2009 transcripts/asari-2009 questions 2>/dev/null | head -50; cat transcripts/asari-2009/verifier-2-report.md
```

```
Sun Nov 15 16:48:50 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
executed
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## 6\|step 6\|Hand over/,+60p' docs/protocol.md | head -150; wc -l docs/protocol.md
```

```
### 6. Answer questions

A reader is asked only when the author or a verifier believes the claims file
misreads the paper: a wrong expected value, the wrong panel, a claim that does
not say what the paper says (author, step 1.6, and "Hand over for
verification"). A method detail the claims file lacks is not asked: the author
takes it from the paper. The reader, who has not seen the data, checks each
question against the paper and decides whether the claims file is to change.
Where it is, the reader amends the claim, and the question's `answer` says
what changed and why, citing the passage; where it is not, the answer says why
the claim stands. The reader marks each question answered in
`questions/<paper>.yaml`.

## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Hand over for verification" docs/protocol.md; awk '/^### .*Hand over for verification/,/^### [0-9]+\. [^H]/' docs/protocol.md
```

```
493:  verification round, with its `reason` (see "Hand over for verification").
524:### 6. Hand over for verification
### 6. Hand over for verification

Do not verify your own attempt. Give the verifier:

- the executed notebook with the conclusion cells and the summary removed;
- the helper module;
- the claims file.

`python tools/entry.py handover entries/<name>` builds these in
`executed/<name>/handover/` from the executed copy. The verifier also gets the
paper, under `paper/`, but checks the analysis against the claims file, and a
method detail the author took from the paper against the passage the author
cites. A place where the claims file misreads the paper is reported; the
revision adds it to `questions/<paper>.yaml` as a question for a reader, as in
step 1.6, and does not change the claim. A reader answers it after the
attempt, in an `answer` run started by hand; the claim's outcome stays as
tested on the claims file, and a later attempt takes up any change.

[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep asari; ls attempts/asari* 2>/dev/null; cat entries/asari-2009/entry.yaml entries/asari-2009/README.md; cat questions/asari-2009.yaml
```

```
asari-2009-02.yaml
attempts/asari-2009-02.yaml
schema_version: 1
name: asari-2009
type: reproduction
title: Long-lasting context dependence in rat auditory cortex (Asari and Zador 2009)
description: Tests the findings of Asari and Zador (2009) on CRCNS ac-1, which holds the whole-cell
  current-clamp recordings of A1 neurons to sequences of natural and synthetic sounds, the
  cell-attached recordings of MGB units, and the earlier recordings of Wehr. It covers the cell and
  probe counts, firing rates, trial reliability, the significance and fractional power measures of
  context dependence and their time constants (Fig. 2 to 4), the timescale of membrane noise, the
  silence probes, the effects of single stimulus properties (Fig. 8), the fast decay in the
  thalamus (Fig. 9), and the STRF and LN model performance on the Wehr cells (Fig. 4).
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_asari_2009.ipynb
  title: Reproducing Asari and Zador (2009) from CRCNS ac-1
  runtime_minutes: 5
- path: strf_asari_2009.ipynb
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims | grep asari; wc -l attempts/asari-2009-02.yaml; cat attempts/asari-2009-02.yaml
```

```
<persisted-output>
Output too large (50.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9c6102a6-3ef7-4b92-8daa-411bad2a237d/tool-results/bcp5m1lj2.txt

Preview (first 2KB):
asari-2009.yaml
797 attempts/asari-2009-02.yaml
schema_version: 3
id: asari-2009-02
datasets:
- archive: crcns
  id: ac-1
  version: unversioned
  doi: 10.6080/K0KW5CXR
  relation: primary
paper: doi:10.1152/jn.00577.2009
date: 2026-11-15
entry: asari-2009
provenance:
  kind: agent
  accountable:
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/asari-2009-02.yaml"
}
```

```
1	schema_version: 3
2	id: asari-2009-02
3	datasets:
4	- archive: crcns
5	  id: ac-1
6	  version: unversioned
7	  doi: 10.6080/K0KW5CXR
8	  relation: primary
9	paper: doi:10.1152/jn.00577.2009
10	date: 2026-11-15
11	entry: asari-2009
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 778 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims; python -c "
import yaml;d=yaml.safe_load(open('asari-2009.yaml'))
print(d.keys())
for c in d['claims']:
  if c['id'] in ('fig7-example-frequency-context','fig9-mgb-fast-decay','fig2-example-reliability'): print(yaml.safe_dump(c,width=120))
"; ls ../paper
```

```
dict_keys(['schema_version', 'paper', 'claims', 'checks'])
criterion: Tolerances are the stated SDs, as the paper gives them as the spread of the values (protocol, expected). The correlation
  is between response traces (median-filtered, zero-mean membrane potential) of trials within one context, over a probe. The
  paper does not say whether the coefficient is the mean over all pairs of trials or the correlation of each trial with the
  mean of the others, nor what the population mean is taken over (cells, or probes); each reading is run. The example cell
  is not identified; the author looks for a current-clamp cell tested with seven natural sound fragments over six repeats,
  and the example values are not tested when no cell can be matched. The population value decides the claim.
expected:
- quantity: population mean trial-to-trial correlation coefficient
  tolerance: 0.09
  value: 0.31
- quantity: example cell, correlation over its seven natural sound fragments
  tolerance: 0.07
  value: 0.61
- quantity: example cell, correlation for the shown probe
  tolerance: 0.08
  value: 0.74
id: fig2-example-reliability
quote: the correlation coefficient of the response traces across trials in a given context was 0.61 ... 0.07 (mean ... SD)
  for the seven natural sound fragments tested in this cell. The reliability varied within a given neuron as a function of
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../paper; grep -n -i "dmr\|ripple\|0\.625\|40 kHz\|kHz" 10.1152-jn.00577.2009.txt | head -60; grep -n -i "dmr\|ff\b\|ripple" ac-1.data-description.txt | head -30
```

```
137:potential at 10 kHz using an amplifier Axopatch 200B (Molecular
158:cells with ensembles of temporally orthogonal ripple combinations, 6
159:cells with ensembles of dynamic moving ripples, 39 cells with ensembles of modulated harmonic tones, and 27 cells with ensembles of
197:DMR
215:synthetic sounds (TORC, DMR, MHT, and MCN) were used to examine the effects caused by the changes in each of the following sound properties among
218:modulated colored noise. VC, voltage-clamp; CC, current-clamp; TORC, temporally orthogonal ripple combination; DMR, dynamic moving ripple; MHT,
259:All stimuli were delivered at 97.656 or 200 kHz using a TDT
265:kHz to within SD of 3.7 dB. Sound levels were measured with a type
272:sound fragments were taken from commercially available audio compact discs, originally sampled at 44.1 kHz and resampled at 97.656 or
273:200 kHz for stimulus presentation: The Diversity of Animal Sounds
306:almost all frequencies from 0 to 22 kHz and ranged from narrow- to
318:properties (Figs. 7 and 8): intensity (amplitude), frequency, amplitude-modulation (AM), frequency-modulation (FM), and higherorder spectrotemporal acoustic features. We used temporally orthogonal ripple combinations (TORCs; for details, see, e.g., Klein et al.
319:2000) and dynamic moving ripples (DMRs; for details, see, e.g.,
329:sampled at 97.656 or 200 kHz and lasted for 4.0–5.5 s (Fig. 1B and
339:Temporally orthogonal ripple combinations (TORCs). The following equation was used to generate ripples and their combinations
354:and spectral ripple modulations, respectively, xi �log2 [ fi/f0] in
358:TORCs were first generated, each consisting of six ripples with
367:frequencies over a bandwidth of 5 octaves (0.88–28.16 kHz in
373:octaves (0.625–40 kHz in steps of 1/128 octaves, random phase at
375:bandwidth (e.g., 0.625–10 kHz, 2.5–40 kHz, and so on). We then
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../paper; sed -n 360,395p 10.1152-jn.00577.2009.txt; sed -n 1570,1600p 10.1152-jn.00577.2009.txt; sed -n 1770,1800p 10.1152-jn.00577.2009.txt
```

```
a fixed (k �1) spectral modulation: ���1.5, �0.9, �0.3, 0, 0.6,
1.2, and 1.8 cycles/octave, respectively. All TORCs had rise and fall
times of 5 ms, modulation depth of �30 dB (with ajk �30/6), and
lasted for 250 ms. Such short TORC envelopes were then randomly
adjoined to generate a “default envelope” that lasted for 4–5.5 s.
To examine the effects of the changes in sound intensities in
conditioning stimuli, we applied the default envelope to the carrier
frequencies over a bandwidth of 5 octaves (0.88–28.16 kHz in
steps of 1/128 octaves), scaled the peak amplitude to the speaker
driver range, and then varied the amplitudes over the maximum
range of 40-dB attenuation. To examine the effects of frequency
changes, we generated a default envelope over the bandwidth of 2
or 4 octaves and chose carrier sinusoidals within the range of 6
octaves (0.625–40 kHz in steps of 1/128 octaves, random phase at
time 0) so that the signals had the same envelope with shifted
bandwidth (e.g., 0.625–10 kHz, 2.5–40 kHz, and so on). We then
normalized the peak amplitude of sound fragments with respect to
their total signal powers (��y(t) �2dt) and uniformly scaled to fit
them all within the speaker driver range.
Dynamic moving ripples (DMRs). To generate the DMR envelopes
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; python - <<'E'
import json
nb=json.load(open('entries/asari-2009/reproduce_asari_2009.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(f"--- {i} {c['cell_type']} {c.get('id','')} :: {s[:150]!r}")
E
python tools/entry.py --help 2>&1 | head -30
```

```
--- 0 markdown 2b5a2aa8 :: '# Reproducing Asari and Zador (2009) on CRCNS ac-1\n\nPaper: H. Asari and A. M. Zador (2009), "Long-Lasting Context Dependence Constrains Neural Encodin'
--- 1 code 447bfafc :: 'import os, time, zlib, resource, collections\nos.environ.setdefault("OMP_NUM_THREADS", "1")\nos.environ.setdefault("OPENBLAS_NUM_THREADS", "1")\nfrom con'
--- 2 markdown 1f528c86 :: '## Data: listing, checksums, and one pass over the recordings'
--- 3 code 66c4c595 :: 'listing = cd.bucket_listing()\nmd5 = cd.checksums()\nprint("bucket listing of ac-1/:")\nfor k, s in listing:\n    print(f"  {k:45s} {int(s):>12d} bytes")\n'
--- 4 code 60d4b671 :: 'NAT, MGB, SYN, MISC = S[0], S[1], S[2], S[3]\nassert "natural sound" in NAT["description"] and "Thalamic" in MGB["description"]\nassert "synthetic" in S'
--- 5 markdown 78d6d5ab :: '## Data check'
--- 6 code b5a0085f :: 'F = pd.DataFrame([{k: v for k, v in o.items() if k in ("group", "cell", "path", "desc", "type", "sf", "unit", "dur", "rep",\n                          '
--- 7 markdown 5fa70d68 :: 'Clock check. The trigger times must share the clock of the traces. For each sequence, the\nacross-trial predictable power (Eq. 52) of the membrane pote'
--- 8 code b4c90831 :: 'ck = pd.DataFrame([dict(group=o["group"], path=o["path"], post=o["clock"]["post"], pre=o["clock"]["pre"])\n                   for o in A1 + MG if "cloc'
--- 9 markdown d815ff4b :: "Duplicates. Recordings deposited twice would have identical traces. Each file's trace extremes and\nmedian, and its length, are compared across distinc"
--- 10 code c5281a83 :: 'multi = F.groupby("path").group.agg(list)\nmulti = multi[multi.apply(len) > 1]\nprint("files listed in more than one experiment group of Summary.mat:")\n'
--- 11 markdown afede4cf :: 'Time resolution. The analysis runs at 1 kHz (helper docstring). On the probes of one recording the\nKruskal-Wallis significance is recomputed at the pa'
--- 12 code 51e92c7b :: 'def kw_fullres(trace10, starts, length, rep
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/asari-2009; python - <<'E'
import json
nb=json.load(open('executed/asari-2009/reproduce_asari_2009.ipynb'))
for i in (47,48,53,54,55):
    c=nb['cells'][i]
    print(f"=== {i}\n"+''.join(c['source']))
    for o in c.get('outputs',[]):
        print('>>>', ''.join(o.get('text','')) if 'text' in o else list(o.get('data',{}).keys()))
E
```

```
reproduce_asari_2009.ipynb
result.json
strf_asari_2009.ipynb
=== 47
MP = {inc: [p for o in MG for p in o.get("probes", []) if p["silence"] == inc and p["rep"] >= 10] for inc in (True, False)}
for inc in (True, False):
    print(f"silence counted={inc}: {len(MP[inc])} probes in {len({p['cell'] for p in MP[inc]})} cells")
rows = []
SDC = {}
for det, key in (("GetSpikes auto", "sd"), ("half threshold", "sd5")):
    for inc in (True, False):
        Sd = cd.stack_curves([p[key] for p in MP[inc]], 61)
        for denom in ("running", "all"):
            y = np.nanmean(Sd, 0) if denom == "running" else np.nan_to_num(Sd).sum(0) / len(MP[inc])
            SDC[(det, inc, denom)] = y
            for pos in ("start", "centre"):
                tb = np.arange(61) * 0.1 + (0.05 if pos == "centre" else 0.0)
                f = cd.fit_exp(tb, y, 1, kappa=None)
                late = float(np.nanmean(y[tb > 0.5]))
                rows.append(dict(detector=det, silence=inc, denom=denom, bin_time=pos, alpha1=f["alpha"][0], tau1=f["tau"][0], kappa=f["kappa"],
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; wc -l ctxdep.py strf.py; grep -n "ff\b\|\"ff\"\|'ff'\|def \|waveform\|Stimuli\|stim_file\|\.sf" ctxdep.py | head -120
```

```
743 ctxdep.py
  222 strf.py
  965 total
73:def open_zip(name: str) -> zipfile.ZipFile:
77:def checksums() -> dict:
82:def bucket_listing() -> list:
89:def member_index() -> dict:
99:def loadmat_member(zn: str, member: str) -> dict:
103:def _txt(x) -> str:
109:def summary(who: str = "asari") -> list:
143:def _medfilt_decimated(x: np.ndarray) -> np.ndarray:
154:def load_recording(path: str, keep_raw: bool = False, filtered: bool = True) -> Recording:
162:        trig.append((str(t.type), int(t.time), int(round(float(dur) / 1000 * r.sf)) if np.size(dur) == 1 else 0,
170:    durs = np.array([int(round(float(s.param.duration) / 1000 * r.sf)) for s in stim]) if stim else np.array([], int)
172:                    sf=int(r.sf), unit=str(r.unit), n_samples=len(x), triggers=trig, notes=notes, stimuli=stim,
184:def sequence_segments(rec: Recording):
187:    Returns a list of presentations in time order: dict(seq=tuple of fragments, on, off,
196:        off = min(on + dur, rec.n_samples)
200:        out.append(dict(type=typ, desc=desc, seq=seq, on=on, off=off, pre=(prev_end, on), post=(off, nxt)))
201:        prev_end = off
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,72p ctxdep.py; sed -n 425,555p ctxdep.py
```

```
"""Loading and context-dependence measures for CRCNS ac-1 (Asari and Zador 2009).

The data set is read from the public S3 bucket of CRCNS by range requests into
its zip files (docs/archives.md, "CRCNS"); nothing is written to disk.

Where each parameter comes from:

- Probe and context construction, the "silence" context (last 4 s of the
  intersequence interval) and the "silence probe" (first 2.5 s after a
  sequence), the rule that a probe needs at least two distinct contexts, the
  truncation of every context to the smallest number of trials, the
  Kruskal-Wallis significance with P < 0.01 for at least 5 ms, the noise
  floor from 1000 trial shuffles, the fractional power estimates (Eqs. 17 to
  19, each trial centred over the probe period) and the PSTH of the MGB units
  (100-ms bins from probe onset, SD over contexts with n - 1) are ported from
  the authors' analysis code deposited in the data set
  (asari/Tools/CxtDep.m, GetEvoked.m, ViewResp.m in crcns-ac1.zip), and agree
  with the paper's Methods (Analysis; Eqs. 10, 17 to 19, 42).
- The 10-ms median filter that clips spikes: Methods, Analysis, paragraph 2,
  and CxtDep.m (param.smooth = 10).
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; date -u; timeout 600 python - <<'E'
import ctxdep as cd, numpy as np
idx=cd.member_index()
paths=[k for k in idx if '20060916-ha3-002-002' in k]
print(paths)
rec=cd.load_recording(paths[0])
print(rec.notes)
for i,s in enumerate(rec.stimuli,1):
    p=s.param
    print(i, s.name, '|', cd._txt(s.description), '|', {f:(getattr(p,f) if np.size(getattr(p,f))<8 else ('arr',np.shape(getattr(p,f)))) for f in p._fieldnames})
print([f for f in rec.stimuli[0]._fieldnames])
E
```

```
Exit code 1
/bin/bash: line 1: cd: entries/asari-2009: No such file or directory
Sun Nov 15 16:49:32 UTC 2026
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "entries/asari-2009/ctxdep.py", line 47, in <module>
    import fsspec
ModuleNotFoundError: No module named 'fsspec'
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|uv " tools/entry.py | head -20; ls -a ~/.cache 2>/dev/null | head; ls -d .venv* /tmp/*venv* $TMPDIR/* 2>/dev/null | head
```

```
519:        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
555:    venv = (output_dir / ".venv").resolve()
556:    python = venv / "bin" / "python"
560:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
563:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
577:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
/tmp/claude-1001/-home-runner-work--temp
/tmp/claude-1001/-home-runner-work-encore-encore
/tmp/claude-1001/bash-edit-diff
```

**Agent calls Bash**

```bash
cd  ls -a executed/asari-2009/; sed -n 545,575p tools/entry.py
```

```
.
..
.clean-run.json
.venv
reproduce_asari_2009.ipynb
result.json
strf_asari_2009.ipynb
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; timeout 900 $PY - <<'E'
import ctxdep as cd, numpy as np
idx=cd.member_index()
paths=[k for k in idx if '20060916-ha3-002-002' in k]
print(paths)
rec=cd.load_recording(paths[0])
print(rec.notes)
for i,s in enumerate(rec.stimuli,1):
    p=s.param
    print(i, s.name, '|', cd._txt(s.description), '|', {f:(getattr(p,f) if np.size(getattr(p,f))<8 else ('arr',np.shape(getattr(p,f)))) for f in p._fieldnames})
print([f for f in rec.stimuli[0]._fieldnames])
E
```

```
['Results/20060916-ha3-002/20060916-ha3-002-002.mat']
['Stimulus sequences are given as follows.', 'Seq.1:  6  1  8  1', 'Seq.2:  10   1   7   1', 'Seq.3:  5   1  12   1', 'Seq.4:  13   1   9   1', 'Seq.5:  11   1   3   1', 'Seq.6:  1  4  1  2  1', '', 'Effective repeats:  4', '', 'See also SoundTrans.m, DMRipple2.m, and MHTones.m.', '', 'Forgot to save the state of RANDN function.']
1 natural sound (probe) | neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec | {'ramp': 5, 'duration': 5475.0143360367, 'sf': 97656}
2 naturalistic sound (forward) | DMR; frequency variants | {'ramp': 5, 'sf': 97656, 'tempmod': ('arr', (16,)), 'specmod': ('arr', (31,)), 'SFtemp': 3, 'SFspec': 6, 'envphase': 3.4483112998305607, 'sinphase': ('arr', (129,)), 'dx': 0.015625, 'ff': array([ 250, 1000], dtype=uint16), 'duration': 5000}
3 naturalistic sound (forward) | DMR; frequency variants | {'ramp': 5, 'sf': 97656, 'tempmod': ('arr', (16,)), 'specmod': ('arr', (31,)), 'SFtemp': 3, 'SFspec': 6, 'envphase': 3.4483112998305607, 'sinphase': ('arr', (129,)), 'dx': 0.015625, 'ff': array([ 500, 2000], dtype=uint16), 'duration': 5000}
4 naturalistic sound (forward) | DMR; frequency variants | {'ramp': 5, 'sf': 97656, 'tempmod': ('arr', (16,)), 'specmod': ('arr', (31,)), 'SFtemp': 3, 'SFspec': 6, 'envphase': 3.4483112998305607, 'sinphase': ('arr', (129,)), 'dx': 0.015625, 'ff': array([1000, 4000], dtype=uint16), 'duration': 5000}
5 naturalistic sound (forward) | DMR; frequency variants | {'ramp': 5, 'sf': 97656, 'tempmod': ('arr', (16,)), 'specmod': ('arr', (31,)), 'SFtemp': 3, 'SFspec': 6, 'envphase': 3.4483112998305607, 'sinphase': ('arr', (129,)), 'dx': 0.015625, 'ff': array([2000, 8000], dtype=uint16), 'duration': 5000}
6 naturalistic sound (forward) | DMR; frequency variants | {'ramp': 5, 'sf': 97656, 'tempmod': ('arr', (16,)), 'specmod': ('arr', (31,)), 'SFtemp': 3, 'SFspec': 6, 'envphase': 3.4483112998305607, 'sinphase': ('arr', (129,)), 'dx': 0.015625, 'ff': arra
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; timeout 900 $PY - <<'E'
import ctxdep as cd, numpy as np, collections
idx=cd.member_index()
rec=cd.load_recording('Results/20060916-ha3-002/20060916-ha3-002-002.mat')
for s in rec.stimuli[:3]: print(repr(s.file))
ks=list(idx)
print(len(ks)); print(collections.Counter(k.split('/')[0] for k in ks))
print([k for k in ks if 'DMR' in k or 'ipple' in k or k.lower().endswith(('.wav','.f32'))][:30])
print([k for k in ks if not k.startswith('Results/')][:80])
E
```

```
'class6/6l.mat'
array([], dtype=float64)
array([], dtype=float64)
346
Counter({'Results': 346})
[]
[]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; sed -n 73,102p ctxdep.py; PY=executed/asari-2009/.venv/bin/python; timeout 900 $PY - <<'E'
import ctxdep as cd
for z in cd.ZIPS:
    n=cd.open_zip(z).namelist()
    print(z,len(n))
    print([x for x in n if 'DMR' in x or 'ipple' in x or 'Stim' in x or x.endswith('.m')][:80])
E
```

```
def open_zip(name: str) -> zipfile.ZipFile:
    return zipfile.ZipFile(fsspec.open(BASE + name, block_size=2**22).open())


def checksums() -> dict:
    with fsspec.open(BASE + "checksums.md5", "rt") as f:
        return {ln.split()[1]: ln.split()[0] for ln in f if ln.strip()}


def bucket_listing() -> list:
    import urllib.request
    xml = urllib.request.urlopen(BASE.replace("ac-1/", "") + "?list-type=2&prefix=ac-1/").read().decode()
    return re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", xml)


@functools.lru_cache(maxsize=None)
def member_index() -> dict:
    """Map 'Results/<cell>/<file>.mat' (as Summary.mat names files) to (zip, member)."""
    idx = {}
    for zn in ZIPS[1:]:
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; timeout 900 $PY - <<'E'
import ctxdep as cd
z=cd.open_zip('crcns-ac1.zip')
n=z.namelist()
ms=[x for x in n if x.endswith('.m')]
print(ms)
for x in ms:
    if 'ipple' in x or 'DMR' in x or 'TORC' in x or 'Trans' in x:
        print('=====',x); print(z.read(x).decode('latin1')[:6000])
E
```

```
['asari/Contents.m', 'asari/Tools/ViewResp.m', 'asari/Tools/ViewCxtDep.m', 'asari/Tools/SoundTrans.m', 'asari/Tools/TuningCurve.m', 'asari/Tools/PinkNoise.m', 'asari/Tools/MovingRipple4.m', 'asari/Tools/MHTones.m', 'asari/Tools/MakeWhiteNoise.m', 'asari/Tools/MakeTone.m', 'asari/Tools/MakeRandomChords.m', 'asari/Tools/MakeRamp.m', 'asari/Tools/logspectrogram.m', 'asari/Tools/GetSpikes.m', 'asari/Tools/GetEvoked.m', 'asari/Tools/GetData.m', 'asari/Tools/DMRipple2.m', 'asari/Tools/CxtDep.m', 'wehr/Contents.m', 'wehr/Tools/ViewSTRF.m', 'wehr/Tools/ViewResponse.m', 'wehr/Tools/STRFanalysis.m', 'wehr/Tools/ridgesvd1.m', 'wehr/Tools/MakeWhiteNoise.m', 'wehr/Tools/MakeTuningCurve.m', 'wehr/Tools/MakeTone.m', 'wehr/Tools/MakeRamp.m', 'wehr/Tools/logspectrogram.m', 'wehr/Tools/GetSpikes.m', 'wehr/Tools/GetEvoked.m', 'wehr/Tools/GetDataInfo.m']
===== asari/Tools/SoundTrans.m
function X = SoundTrans(y,param)

%SOUNDTRANS trnasforms sound signals according to give parameters
%
%   X=SoundTrans(Y,PARAM);
%     transforms signal Y in PARAM.SF Hz based on the parameters PARAM:
%       1. shifts spectrum of Y by PARAM.DF Hz.
%       2. apply PARAM.RAMP-msec-ramp at the beggining and the end of Y.
%       3. scale Y by PARAM.ATTENUATION
%       4. scramble sequences of syllables as specified by PARAM.SYLLABLES.
%
%
%   ----- INPUT -----
%     Y       : original signal (column vector)
%     PARAM   : structure to specify parameters
%       .sf         : sampling frequency (default: 8000 Hz)
%       .df         : frequency shift size in Hz (default: 0 Hz)
%       .ff         : a vector whose 1st and 2nd elements specify the
[... 529 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; sed -n 205,335p ctxdep.py; python3 - <<'E'
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
for i in (1,3):
    print(f"=== {i}\n"+''.join(nb['cells'][i]['source']))
E
```

```
@dataclass
class Probe:
    cell: str
    path: str
    probe: int            # fragment index (1-based), or 0 for the silence probe
    contexts: list        # context fragment per group (0 = silence)
    traces: list          # per context: (n_trials, T) arrays at 1 kHz (median filtered)
    n_trials: list        # trials available per context before truncation
    duration: float       # s
    spikes: list | None = None   # per context: list of spike-time arrays (s, from probe onset)
    kind: str = ""

    @property
    def rep(self) -> int:
        return min(self.n_trials)


def build_probes(rec: Recording, include_silence_context: bool = True, include_silence_probe: bool = False,
                 spikes: np.ndarray | None = None) -> list:
    """Port of CxtDep.m: all probes with at least two distinct contexts.
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'E'
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
print(''.join(nb['cells'][4]['source']))
E
```

```
NAT, MGB, SYN, MISC = S[0], S[1], S[2], S[3]
assert "natural sound" in NAT["description"] and "Thalamic" in MGB["description"]
assert "synthetic" in SYN["description"]


def fig8_tests(rec):
    """Significance (contexts of one property set only) and fractional power of every probe
    with at least two contexts of a set, each with at least 4 trials (Fig. 8)."""
    kinds = [cd.stim_kind(s) for s in rec.stimuli]
    sets = cd.property_sets(rec)
    tests = []
    for p in (cd.build_probes(rec, include_silence_context=False) if sets else []):
        for k, S in enumerate(sets):
            ctx = [c for c, X in zip(p.contexts, p.traces) if c in S["members"] and X.shape[0] >= 4]
            if len(ctx) < 2:
                continue
            r = cd.kw_significance(p, contexts_subset=ctx, rng=seed(rec.path, p.probe, "fig8", k))
            fp = cd.frac_power(p, contexts_subset=ctx)
            tests.append(dict(cell=p.cell, path=rec.path, probe=p.probe, kind=kinds[p.probe - 1], prop=S["prop"], label=S["label"],
                              members=tuple(S["members"]), main=S["main"], own=p.probe in S["members"], ctx=tuple(ctx), rep=r["rep"],
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; PY=executed/asari-2009/.venv/bin/python; time timeout 900 $PY - <<'E'
import ctxdep as cd, numpy as np, zlib, re
def seed(*parts): return np.random.default_rng([zlib.crc32("/".join(map(str, parts)).encode())])
src = cd.open_zip("crcns-ac1.zip").read("asari/Tools/DMRipple2.m").decode("latin1")
print([l.strip() for l in src.splitlines() if re.search(r"\.ff |f = ff\(1\)|ysin = ", l)])
paths = ["20060916-ha3-002","20060916-ha3-003","20060916-ha4-001","20060916-ha5-002","20060917-ha1-002"]
sub = [(250.,1000.),(1000.,4000.),(4000.,16000.)]
for c in paths:
    path=f"Results/{c}/{c}-002.mat"
    rec=cd.load_recording(path)
    st=rec.stimuli
    for p in cd.build_probes(rec, include_silence_context=False):
        if cd.stim_kind(st[p.probe-1])!="natural": continue
        for d in ("forward","backward"):
            ctx=[c_ for c_,X in zip(p.contexts,p.traces) if c_>0 and "DMR; frequency" in cd._txt(st[c_-1].description) and f"({d})" in str(st[c_-1].name) and cd._par(st[c_-1],"ff") in sub and X.shape[0]>=4]
            bands=[cd._par(st[c_-1],"ff") for c_ in ctx]
            if len(ctx)<2: print(c,p.probe,d,"contexts",ctx); continue
            r=cd.kw_significance(p,contexts_subset=ctx,rng=seed(path,p.probe,"fig7",d))
            s=r["sig"]
            print(c,p.probe,d,ctx,bands,r["rep"],round(p.duration,2), s.any(), (np.where(s)[0].max()/cd.FS if s.any() else None))
E
```

```
['%           .ff      : frequency range in Hz', 'f = ff(1)*2.^x;', 'ysin = sin(2*pi*f*t+repmat(sinphase,1,length(t))); % original sinusoidals', 'param.ff = ff;']
20060916-ha3-002 1 forward [2, 4, 6] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 4 5.48 True 0.05
20060916-ha3-002 1 backward [8, 10, 12] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 4 5.48 False None
20060916-ha3-003 1 forward [2, 4, 6] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 4 5.7 False None
20060916-ha3-003 1 backward [8, 10, 12] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 4 5.7 False None
20060916-ha4-001 1 forward [2, 4, 6] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 6 5.08 True 4.532
20060916-ha4-001 1 backward [8, 10, 12] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 6 5.08 True 0.18
20060916-ha5-002 1 forward [2, 4, 6] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 6 5.8 True 5.354
20060916-ha5-002 1 backward [8, 10, 12] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 6 5.8 True 2.777
20060917-ha1-002 1 forward [2, 4, 6] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 6 5.08 True 1.253
20060917-ha1-002 1 backward [8, 10, 12] [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)] 6 5.08 True 0.109

real	0m9.947s
user	0m10.166s
sys	0m0.585s
```

**Agent calls Bash**

```bash
cd  ls transcripts/asari-2009/; grep -n -i "fig7\|B12\|B11\|tuning files" transcripts/asari-2009/verifier-1-report.md | head -30
```

```
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
recorder-report.md
recorder.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; python3 - <<'E'
import json,glob
for f in glob.glob('schemas/*attempt*'):
    s=json.load(open(f)) if f.endswith('json') else None
    print(f)
E
grep -n -A40 '"verifications"' schemas/attempt*.json | grep -n -i "outcome\|required\|agrees\|proposed\|response\|reason" | head -40
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/attempt.schema.json
6:391-        "required": [
32:417-              "required": [
34:419-                "agrees"
40:425-                "agrees": {
```

**Agent calls Bash**

```bash
cd  sed -n 380,470p schemas/attempt.schema.json; grep -n -B2 -A30 '"proposed"' schemas/attempt.schema.json | head -60
```

```
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
        ],
        "properties": {
          "date": {
            "type": "string",
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import json
nb=json.load(open('executed/asari-2009/reproduce_asari_2009.ipynb'))
for i in (17,19,24,28,39):
    c=nb['cells'][i]
    print(f"=== {i}\n"+''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('>>>', ''.join(o['text'])[:5000])
E
```

```
=== 17
def cell_rates(objs, key=None, files="all"):
    rows = []
    for o in objs:
        if files == "seq" and o["desc"] == "tuning curve":
            continue
        if files == "tuning" and o["desc"] != "tuning curve":
            continue
        r = o["rates"][key] if key is not None else o["rates"]
        rows.append(dict(cell=o["cell"], **r))
    d = pd.DataFrame(rows).groupby("cell").sum()
    return pd.DataFrame(dict(spont=d.n_sp / d.t_sp, pre=d.n_pre / d.t_pre, evoked=d.n_ev / d.t_ev))


out = []
for h in (10, 15, 20):
    for files in ("all", "seq"):
        r = cell_rates(A1, h, files)
        out.append(dict(region="A1", detector=f"{h} mV", files=files, cells=len(r), spont_mean=r.spont.mean(), spont_sd=r.spont.std(),
                        pre_mean=r.pre.mean(), pre_sd=r.pre.std(), evoked_mean=r.evoked.mean(), evoked_sd=r.evoked.std()))
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/asari-2009.yaml'))
for c in d['claims']:
  if c['id'] in ('a1-mgb-firing-rates','fig8c-relative-effects','fig3b-fractional-power-decay'): print(c['id'],'::',c['criterion'],'\n')
"
```

```
a1-mgb-firing-rates :: Tolerances are 10% of each mean; the printed SDs (0.61, 0.77, 1.25, 16.9 Hz) are the spread over cells, not an uncertainty of the mean, and are reported for comparison (within 10% of each). Spikes in MGB are extracted by a high-pass filter and a threshold with spike times at the peaks (Methods, Analysis, paragraph 3). The paper fixes neither the filter cutoff, the threshold, nor how A1 spikes were detected, nor the windows for "spontaneous" (readings are the intersequence silence, about 6 s, or a pre-stimulus baseline) and "evoked" (readings are all sound periods, or the probe periods analysed). The author runs a standard detector on each reading of the windows; reproduced when the four means are within tolerance under one reading, partially reproduced when the A1 means are below 1 Hz and the MGB evoked mean above 5 Hz but some means fall outside tolerance. 

fig3b-fractional-power-decay :: Q(t) of Eq. 20 from the 305 natural sound probes, numerator Eq. 19 and denominator Eq. 17 averaged over probes at each time point, the denominator smoothed by a running mean over [0, 2t] before the division; one exponential with constant 0 fitted (Figure 3B legend). The same open details as fig3a-proportion-significant (silence as a context; which probes enter the average at time t) and the fit range (0 to 4 s, 0 to 6 s) are run as readings. The printed values in the legend are garbled in the text extraction and read as alpha1 = 0.49, tau1 = 1.04 s with kappa = 0, which the Results (1.04 s) and Figure 4 legend confirm. Reproduced when both are within tolerance under one reading. 

fig8c-relative-effects :: Per the Methods (Eq. 21 and the paragraph after it), the area under Q(t) from 0 to 4 s for each property, divided by the area for natural sounds (Figure 3B), with 95% confidence intervals from 200 resamplings of 1000 samples. The paper does not say what a sample is; readings are probes drawn with replacement, and trials drawn with replacement within each 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import json
nb=json.load(open('executed/asari-2009/reproduce_asari_2009.ipynb'))
for i in (42,60,63,66,68,69,72,76,77):
    c=nb['cells'][i]
    print(f"=== {i}\n"+(''.join(c['source']) if c['cell_type']=='markdown' else ''))
    for o in c.get('outputs',[]):
        if 'text' in o: print('>>>', ''.join(o['text'])[:6000])
E
```

```
=== 42
**Result: not reproduced.** The bound near probe onset is within tolerance in several readings
(1 + alpha1 from 0.459 to 0.534, for example 0.498 with the unsmoothed denominator and silence
counted), and the mean of Eq. 43 over the first 100 ms is 0.492 (smoothed, silence counted). The time
constant is 1.45 to 2.81 s in every fit to 4 or 6 s that converged, none within 0.936 to 1.144 s;
the two fits over all probes to 6 s with the smoothed denominator stop at the 100-s bound. The main
reading (smoothed, silence counted, running probes, 0 to 4 s) gives 0.430 and 2.32 s. No reading
puts both values within tolerance, and the criterion has no rule for partial. The closest constant,
0.928 s, comes from a fit to 1.98 s, a range the claims file does not list, where the bound is
0.439. 1 - Q(t) gives 0.53 to 0.55 at onset and 1.27 to 1.76 s.
=== 60
**Result: partially reproduced, resting on an assumption (the property sets).** Main reading:
amplitude 43 of 70 tests significant (0.614, 30 cells), frequency 52 of 85 (0.612, 34), AM 19 of 39
(0.487, 26), FM 12 of 25 (0.480, 24) and higher-order 41 of 131 (0.313, 26). Every count is outside
its tolerance, as the data set holds fewer tests: the MHT probes of Table 1 (25 amplitude, 25
frequency, 71 AM and 57 FM) are represented by 14 AM tests in 2 cells. The proportions keep the
order amplitude > frequency and AM > FM > higher-order, by 0.002 and 0.007 for the first two
comparisons. With every set as a test the order fails (frequency 0.632 above amplitude 0.608); with
the naturalistic probes added it holds (0.600 > 0.582; 0.487 > 0.480 > 0.313). Where the data hold
the cells, the main reading gives the rows of Table 1 closely: natural AM and FM 25 tests in 24
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'E'
import json
nb=json.load(open('reproduce_asari_2009.ipynb'))
for i in (14,26,59):
    print(f"=== {i}\n"+''.join(nb['cells'][i]['source'])[:3000])
print(nb['cells'][54].keys(), nb['cells'][54]['metadata'])
E
```

```
=== 14
rows = []
for o in A1 + MG:
    if "counts" in o:
        for inc, lst in o["counts"].items():
            for pr, ctx, ntr, dur in lst:
                rows.append(dict(group=o["group"], cell=o["cell"], path=o["path"], desc=o["desc"], silence=inc, probe=pr,
                                 nctx=len(ctx), rep=min(ntr), dur=dur))
C = pd.DataFrame(rows)


def ens_kind(o):
    if o["group"] == "natural":
        return "natural"
    d = " ".join(st[1] for st in o.get("stim", []))
    for key, name in (("TORC", "TORC"), ("DMR", "DMR"), ("Modulated Harmonic Tone", "MHT"), ("pink noise", "MCN")):
        if key in d:
            return name
    return "naturalistic" if "naturalistic" in o["desc"] else "natural sound variants"

[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "claim:" tools/entry.py | head -20; grep -n "proposed" tools/entry.py | head
```

```
463:            if tag.startswith("claim:"):
372:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
```

**Agent calls Bash**

```bash
cd  sed -n 345,385p tools/entry.py; sed -n 450,480p tools/entry.py
```

```
if str(d) not in used:
                    report.error(where, f"finding {n}: {d} is not a dataset of this attempt ({', '.join(used)})")
        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
        # does not bind: the revision after it may change outcomes, and round 2 reviews them.
        agreed = {}
        for rnd in (attempt.get("verifications") or [])[1:]:
            for r in rnd["results"]:
                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
        kinds = lookup(kinds_by_target, attempt) or {}
        for outcome in attempt.get("outcomes", []):
            # A claim on data in another archive names where they are, so it is never blocked for missing data,
            # and when it is tested the archive is an input. Only the latest attempt is held to this: the
            # claims file is shared, and an earlier attempt may predate the claim's `elsewhere`.
            if kinds.get(outcome.get("claim")) == "elsewhere" and path == mine[-1]:
                if outcome.get("blocked_by") == "data_missing":
                    report.error(where, f"claim {outcome.get('claim')!r} has its data in another archive "
                                        "(`elsewhere`); test it there, or block it for the reason it cannot be "
                                        "tested, not `data_missing`")
                if outcome.get("outcome") != "blocked" and not attempt.get("inputs"):
                    report.error(where, f"claim {outcome.get('claim')!r} was tested on data in another archive; "
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'E'
import json
f='reproduce_asari_2009.ipynb'
nb=json.load(open(f))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(keepends=True)

# B12: count a file listed in two groups once; tuning-only is outside the claims file's readings
s=src(17)
old='''    rows = []
    for o in objs:
        if files == "seq" and o["desc"] == "tuning curve":'''
new='''    rows, seen = [], set()
    for o in objs:
        if (o["cell"], o["path"]) in seen:   # a file listed in two groups of Summary.mat counts once
            continue
        seen.add((o["cell"], o["path"]))
        if files == "seq" and o["desc"] == "tuning curve":'''
assert old in s; s=s.replace(old,new)
old='''print("tolerances: A1 0.423-0.517 and 0.513-0.627; MGB 0.702-0.858 and 10.26-12.54 Hz")'''
new=old+'''\nprint("files='tuning' (tuning-curve recordings only) is not a reading of the claims file and is shown for comparison only")'''
assert old in s; s=s.replace(old,new); put(17,s)

# fig7: the three bands that are the Figure 7 bands divided by 2.5, and what the stimulus code says ff is
s=src(54)
s=s.rstrip('\n')+'''

# The bands 0.25-1, 1-4 and 4-16 kHz of these recordings are the Figure 7 bands divided by 2.5. The generator named in
# their notes (DMRipple2.m, in the data set) states the unit of ff:
code = cd.open_zip("crcns-ac1.zip").read("asari/Tools/DMRipple2.m").decode("latin1").splitlines()
print("\\nDMRipple2.m:")
for ln in code:
    if ".ff " in ln or ln.strip().startswith(("f = ff(1)*2", "ysin = sin")):
        print("   ", ln.strip())
sub = [(250.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0)]
rows = []
for o in A1:
    if o["group"] != "synthetic" or not any("DMR; frequency" in st[1] for st in o.get("stim", [])):
        continue
    rec = cd.load_recording(o["path"])
    st = rec.stimuli
    sfs = sorted({int(s_.param.sf) for s_ in st})
    for p in cd.build_probes(rec, include_silence_context=False):
        if cd.stim_kind(st[p.probe - 1]) != "natural":
            continue
        for d in ("forward", "backward"):
            ctx = [c for c, X in zip(p.contexts, p.traces) if c > 0 and "DMR; frequency" in cd._txt(st[c - 1].description)
                   and f"({d})" in str(st[c - 1].name) and cd._par(st[c - 1], "ff") in sub and X.shape[0] >= 4]
            r = cd.kw_significance(p, contexts_subset=ctx, rng=seed(o["path"], p.probe, "fig7", d))
            s_ = r["sig"]
            rows.append(dict(path=o["path"].split("/")[-1], variants=d, contexts=len(ctx),
                             bands=", ".join("-".join(f"{v / 1000:g}" for v in cd._par(st[c - 1], "ff")) for c in ctx),
                             trials=r["rep"], length_s=round(p.duration, 2), stimulus_sf_hz=sfs, significant=bool(s_.any()),
                             last_significant_s=(np.where(s_)[0].max() / cd.FS if s_.any() else np.nan)))
F7 = pd.DataFrame(rows)
print("\\nnatural probes with only the three DMR contexts 0.25-1, 1-4 and 4-16 kHz (Figure 7 bands / 2.5):")
print(F7.round(3).to_string())
print("probes (forward variants) significant up to 3.6 s or later:", int((F7[F7.variants == "forward"].last_significant_s >= 3.6).sum()), "of",
      int((F7.variants == "forward").sum()), "| backward:", int((F7[F7.variants == "backward"].last_significant_s >= 3.6).sum()), "of",
      int((F7.variants == "backward").sum()))
print("the band 8-32 kHz times 2.5 would be 20-80 kHz, above half the stimulus sampling rate (48.8 kHz)")
'''
put(54,s)
json.dump(nb,open(f,'w'),indent=1,ensure_ascii=False); open(f,'a').write('\n')
E
head -c 300 reproduce_asari_2009.ipynb; tail -c 100 reproduce_asari_2009.ipynb | od -c | tail -3
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2b5a2aa8",
   "metadata": {},
   "source": [
    "# Reproducing Asari and Zador (2009) on CRCNS ac-1\n",
    "\n",
    "Paper: H. Asari and A. M. Zador (2009), \"Long-Lasting Context Dependence Constrains Neural Encoding\n",
    "Models in Rode0000120   b   f   o   r   m   a   t   _   m   i   n   o   r   "   :    
0000140   5  \n   }  \n
0000144
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'E'
import json
f='reproduce_asari_2009.ipynb'
nb=json.load(open(f))
c=nb['cells'][54]; s=''.join(c['source'])
old='''            r = cd.kw_significance(p, contexts_subset=ctx, rng=seed(o["path"], p.probe, "fig7", d))'''
new='''            if len(ctx) < 2:
                continue
'''+old
assert old in s; s=s.replace(old,new); c['source']=s.splitlines(keepends=True)
json.dump(nb,open(f,'w'),indent=1,ensure_ascii=False); open(f,'a').write('\n')
E
date -u
```

```
Sun Nov 15 16:52:19 UTC 2026
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/asari-2009 2>&1 | tail -40
```

```
Installed kernelspec registry-asari-2009 in executed/asari-2009/.venv/share/jupyter/kernels/registry-asari-2009
0 error(s)
pass  reproduce_asari_2009.ipynb  (288 s)
pass  strf_asari_2009.ipynb  (1418 s)

real	28m32.313s
user	74m2.317s
sys	1m44.904s
```

**Agent calls Bash**

```bash
cd  date -u; python3 - <<'E'
import json
nb=json.load(open('executed/asari-2009/reproduce_asari_2009.ipynb'))
for i in (14,17,47,54,78):
    c=nb['cells'][i]
    for o in c.get('outputs',[]):
        if 'text' in o: print(f'>>> {i}\n', ''.join(o['text'])[-4500:])
nb=json.load(open('executed/asari-2009/strf_asari_2009.ipynb'))
c=nb['cells'][-1]
print(''.join(c['source']), [''.join(o.get('text','')) for o in c.get('outputs',[])])
E
```

```
Sun Nov 15 17:21:01 UTC 2026
>>> 14
                    probes  cells
group     silence               
natural   False       305     39
          True        305     39
synthetic False       333     95
          True        333     95
silence counted=True: A1 cells meeting the criterion (natural and synthetic ensembles) 132 of 145 whole-cell cells in the data set
silence counted=False: A1 cells meeting the criterion (natural and synthetic ensembles) 132 of 145 whole-cell cells in the data set
probes in the data set failing the rule: 12
A1 cells in the data set: {'natural': 39, 'synthetic': 96, 'various': 12} | MGB cells: 14
voltage-clamp recordings in the data set: 0 (see the data check)

A1 cells meeting the rule by ensemble (stimulus descriptions):
                        probes  cells  paper_cells
kind                                              
DMR                         38     15          6.0
MCN                        131     26         27.0
MHT                         39     26         39.0
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'E'
import json
f='reproduce_asari_2009.ipynb'
nb=json.load(open(f))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,old,new):
    s=src(i); assert old in s,(i,old); put(i,s.replace(old,new))

rep(19,"alone give 11.66 Hz evoked.","alone, a comparison outside the claims file's readings, give 11.66 Hz evoked.")
rep(19,"0.822 Hz spontaneous and 7.15 Hz evoked over all recordings, and 1.03 and 13.37 Hz on the\ntuning-curve recordings,","0.822 Hz spontaneous and 7.15 Hz evoked over all recordings (1.03 and 13.37 Hz on the\ntuning-curve recordings),")
rep(19,"the automatic detector and 7.07 Hz at half its threshold.","the automatic detector and 7.07 Hz at half its threshold. A file listed in two groups of Summary.mat\n(the tuning-curve file of two A1 cells) is counted once.")

put(24,"""**Result: reproduced, resting on an assumption (reliability as the mean correlation over pairs of
trials).** The mean pairwise trial correlation is 0.310 +/- 0.098 over 39 cells (0.319 +/- 0.129 over
305 probes), against 0.31 +/- 0.09. The leave-one-out reading gives 0.436, outside the tolerance, so
the outcome holds under the pairwise reading only; it is adopted as in fig2-example-long-context. One
recording with seven fragments and six trials (20051222-ha1-001) has a cell mean of 0.603 and 15
probe-context values between 0.66 and 0.82, consistent with the example cell (0.61 and 0.74).
""")

rep(39,"No reading puts both values within tolerance, and the criterion has\nno rule for partial.","The decay constant, the quantity the claim is about, is outside its\ntolerance in every listed reading, so the claim is not reproduced.")
rep(42,"No reading\nputs both values within tolerance, and the criterion has no rule for partial.","The time\nconstant, the quantity the claim is about, is outside its tolerance in every listed reading, so the\nclaim is not reproduced.")

put(48,"""**Result: reproduced, resting on an assumption (the plateau is judged against the fitted kappa).**
The mean SD of the PSTHs over 93 probes in 14 cells falls from 6.45 spikes/s in the first bin to 2.04
in the second. With silence counted and the running probes, tau1 is 0.058 s and the mean after 0.5 s
is 0.99 times the fitted constant; over all probes with bin starts tau1 is 0.080 s. At half the
detection threshold, with silence counted, tau1 is 0.064 and 0.081 s. With silence counted the sizes
are smaller than the paper's: alpha1 5.2 to 12.4 spikes/s against 15.0 (7.0 to 15.4 at half the
threshold), and kappa 0.81 to 1.21 against 2.0. Without silence the first bin is 2.50 spikes/s
(3.45 at half the threshold), alpha1 is 1.56 to 3.04 over the running probes (2.34 to 4.26 at half
the threshold) and tau1 0.075 s (0.083 s); the fits over all probes do not converge to a decay, tau1
at its bound of 100 s with the automatic detector and 31.3 s at half the threshold. Apart from those
two fits, tau1 is at most 0.083 s. The criterion asks that the mean after 0.5 s be within 25% of
kappa. Read as the fitted kappa, which the fit draws towards the late mean, this holds in every
converged fit (0.97 to 1.00), and the claim is reproduced. Read as the paper's kappa of 2.0, the
mean after 0.5 s is 0.39 to 0.66 of it, the rule for reproduced fails, and with tau1 below 0.3 s
neither rule applies. The fitted kappa is adopted: the criterion calls this test a plateau, a
flattening of the curve, and reports the sizes against their values without testing them.
""")

put(55,"""**Result: not testable (blocked, data missing).** Of the 105 synthetic recordings, 35 hold DMR or TORC
stimuli and the other 70 hold none (MHT, pink noise, natural and naturalistic sounds). None has
DMR contexts in the three Figure 7 bands. The stimuli with edges 0.625, 2.5, 10 and 40 kHz are
single two-band DMRs and TORCs (0.625-2.5 with 10-40 kHz) in designs without a natural probe, and
one recording has a natural probe after DMR amplitude variants in 2.5-10 kHz only. The five
recordings of a natural probe after DMR frequency variants use two-octave bands from 0.25-1 to 8-32
kHz. In these five, with the forward variants as contexts, the probe is significant in 4, last at
1.25 to 3.67 s.

Three of their bands (0.25-1, 1-4 and 4-16 kHz) are the Figure 7 bands divided by 2.5, and 0.25 kHz
is below the 0.625 to 40 kHz carrier range of the Methods, so these recordings could hold the
Figure 7 design with band edges stored in other units. With only those three contexts, the forward
variants are significant up to 3.6 s or later in 2 of the 5 probes (last at 4.53 and 5.35 s) and the
backward variants in none. The generator named in these recordings' notes, DMRipple2.m, gives ff as
the "frequency range in Hz" and builds the carriers as ff(1) times powers of 2, and every stimulus
was played at 97656 Hz, where 8-32 kHz can be played and 20-80 kHz (the top band times 2.5) cannot.
The stored edges are therefore in Hz, no recording has the bands of the legend, and the claim stays
not testable. The bands of these recordings differ from the carrier range of the Methods.
""")

rep(76,"- fig7-example-frequency-context: no recording has the design (see its section).","- fig7-example-frequency-context: no recording has the bands of the design (see its section).")

s=src(77)
for old,new in [
 ("| fig2-example-reliability | reproduced |","| fig2-example-reliability | reproduced (assumption: pairwise reliability); leave-one-out gives 0.436, outside |"),
 ("| fig4-strf-performance-low | partially reproduced (`strf_asari_2009.ipynb`) |","| fig4-strf-performance-low | partially reproduced (assumption: the claims file's test; 16 of the paper's 20 cells; `strf_asari_2009.ipynb`) |"),
 ("| fig8a-proportion-by-property | partially reproduced (assumption: property sets): order of the proportions holds, counts lower |","| fig8a-proportion-by-property | partially reproduced (assumption: property sets): order of the proportions holds, counts lower; amplitude above frequency by 0.002, and the order fails with every set as a test |"),
 ("| fig8b-decay-by-property | not reproduced (assumption: property sets): amplitude constant 0.35 s |","| fig8b-decay-by-property | not reproduced (assumption: property sets): amplitude constant 0.35 s; partial with the naturalistic probes added |"),
 ("| fig8c-relative-effects | not reproduced (assumption: property sets): amplitude and frequency effects smaller than natural |","| fig8c-relative-effects | not reproduced (assumption: property sets): amplitude interval below 1 in every main-reading variant, higher-order estimate above amplitude; partial with every set or the naturalistic probes |"),
 ("| fig9-mgb-fast-decay | reproduced |","| fig9-mgb-fast-decay | reproduced (assumption: plateau against the fitted kappa); sizes smaller than the paper's |"),
 ("| fig7-example-frequency-context | blocked: no recording with the example's design (all 105 synthetic recordings searched) |","| fig7-example-frequency-context | blocked: no recording with the example's bands (all 105 synthetic recordings searched; stored edges are in Hz) |"),
]:
    assert old in s,old; s=s.replace(old,new)
put(77,s)
json.dump(nb,open(f,'w'),indent=1,ensure_ascii=False); open(f,'a').write('\n')
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'E'
import json
f='reproduce_asari_2009.ipynb'
nb=json.load(open(f))
c=nb['cells'][48]; s=''.join(c['source'])
old="Read as the paper's kappa of 2.0, the\nmean after 0.5 s is 0.39 to 0.66 of it,"
new="Read as the paper's kappa of 2.0, the\nmean after 0.5 s is 0.39 to 0.60 of it with silence counted (0.45 to 0.66 at half the threshold),"
assert old in s; c['source']=s.replace(old,new).splitlines(keepends=True)
json.dump(nb,open(f,'w'),indent=1,ensure_ascii=False); open(f,'a').write('\n')
nb=json.load(open('strf_asari_2009.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='markdown': print(i, ''.join(c['source'])[:1500]); print()
E
```

```
0 # Asari and Zador (2009): STRF and LN model performance on Wehr's recordings (CRCNS ac-1)

Paper: doi:10.1152/jn.00577.2009, Figure 4 and Methods, "Neural encoding models" and "Model
performance". Dataset: CRCNS ac-1, `unversioned` (MD5 sums printed below), the folder `wehr/` of
`crcns-ac1.zip`, which holds the recordings of Machens et al. (2004) that the paper reanalysed.

This notebook tests one claim, fig4-strf-performance-low; the other claims are in
`reproduce_asari_2009.ipynb`. Every method detail and its source is in the docstring of
`strf.py`.

| Claim | Tested here |
|---|---|
| fig4-strf-performance-low | tested |

2 ## Data check

5 Clock check: the trial-averaged response must follow the stimulus. A model with the 180-ms window
fitted on the true alignment is compared with one fitted after shifting the response by half the
stimulus length (circularly), on the first cell.

[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import json
nb=json.load(open('executed/asari-2009/strf_asari_2009.ipynb'))
t=''.join(''.join(o.get('text','')) for c in nb['cells'] for o in c.get('outputs',[]))
for k in ['0.0031','0.025','0.0083','0.0081','0.153','0.131','0.078','0.112','1 of 208','0.037','0.033','0.017','-0.047','0.029','97656','0.178','12 of 16','13 of 16','0.016','0.023']:
    print(k, k in t)
E
grep -n "0\.309" attempts/asari-2009-02.yaml entries/asari-2009/README.md 2>/dev/null | head
```

```
0.0031 True
0.025 True
0.0083 True
0.0081 True
0.153 True
0.131 True
0.078 True
0.112 True
1 of 208 True
0.037 True
0.033 True
0.017 True
-0.047 True
0.029 True
97656 True
0.178 True
12 of 16 True
13 of 16 True
0.016 True
0.023 True
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'E'
f='README.md'; s=open(f).read()
for old,new in [
("| Low firing rates in A1, high evoked rates in MGB | Partially reproduced |","| Low firing rates in A1, high evoked rates in MGB | Partially reproduced, resting on an assumption (A1 spike detector) |"),
("| Trial-to-trial reliability, 0.31 over the population | Reproduced |","| Trial-to-trial reliability, 0.31 over the population | Reproduced, resting on an assumption (pairwise reliability) |"),
("| Example neuron with context effects for about 4 s, absent from 2 to 4 s | Reproduced, resting on an assumption (pairwise reliability) |","| Example neuron with context effects before 2 s, none from 2 to 3.6 s, and again after 3.6 s | Reproduced, resting on an assumption (pairwise reliability) |"),
("| STRF and LN models stay below about 20% and do not improve with longer windows | Partially reproduced |","| STRF and LN models stay below about 20% and do not improve with longer windows | Partially reproduced, resting on an assumption (the claims file's test, 16 of 20 cells) |"),
("| Proportions of significant probes by stimulus property (Figure 8A) | Partially reproduced, resting on an assumption (property sets) |","| Proportions of significant probes by stimulus property (Figure 8A) | Partially reproduced, resting on an assumption (property sets); the order holds by 0.002 and fails with every set as a test |"),
("| Decay of the normalized power by property (Figure 8B) | Not reproduced, resting on an assumption (property sets) |","| Decay of the normalized power by property (Figure 8B) | Not reproduced, resting on an assumption (property sets); partial with the naturalistic probes added |"),
("| Effects of each property relative to natural sounds (Figure 8C) | Not reproduced, resting on an assumption (property sets) |","| Effects of each property relative to natural sounds (Figure 8C) | Not reproduced, resting on an assumption (property sets); partial with every set or the naturalistic probes |"),
("| Fast decay of context dependence in MGB (about 80 ms) | Reproduced |","| Fast decay of context dependence in MGB (about 80 ms) | Reproduced, resting on an assumption (plateau against the fitted constant) |"),
("It takes about 24 minutes.","It took 24 minutes in the latest run and 31 in the one before."),
]:
    assert old in s,old; s=s.replace(old,new)
open(f,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
f='attempts/asari-2009-02.yaml'; s=open(f).read()
R=[
# a1-mgb
("""recordings, 0.817 Hz in the second before each stimulus, and 5.07 Hz evoked (SD 11.46); the tuning-curve
    recordings alone give 0.868 and 11.66 Hz, and the sequence recordings alone 0.551 and 4.99 Hz.""",
"""recordings, 0.817 Hz in the second before each stimulus, and 5.07 Hz evoked (SD 11.46); the sequence
    recordings alone give 0.551 and 4.99 Hz, and the tuning-curve recordings alone, a comparison outside
    the claims file's readings, 0.868 and 11.66 Hz. A file listed in two groups of Summary.mat (the
    tuning-curve file of two A1 cells) is counted once since verification round 2; this moved one value
    in the third decimal (20-mV detector, all recordings, spontaneous 0.310 Hz)."""),
# fig2 reliability
("""- claim: fig2-example-reliability
  outcome: reproduced
  notebook""","""- claim: fig2-example-reliability
  outcome: reproduced
  assumed: true
  notebook"""),
("""    fragments); this claim's criterion and outcome are unchanged.
""","""    fragments); this claim's criterion and outcome are unchanged. The outcome holds under the pairwise
    reading only, as leave-one-out (0.436) is outside the tolerance; marked as resting on that
    assumption after verification round 2.
  deviations:
  - Assumed that reliability is the mean correlation over pairs of trials of one context, as for
    fig2-example-long-context. The claims file leaves pairs and leave-one-out open, and the two give
    different outcomes (0.310, within 0.22 to 0.40, and 0.436, outside). The pairwise reading is
    adopted as the paper speaks of the "correlation coefficient of the response traces across trials"
    (Results, Context dependence, paragraph 2); the question for the paper's authors is under findings.
"""),
# fig3b
("""  notes: Changed from partially_reproduced after verification round 1, as the criterion has no rule
    for partial and the decay constant is outside tolerance in every listed reading. Q(t) falls""",
"""  notes: Changed from partially_reproduced after verification round 1, as the decay constant, the
    quantity the claim is about, is outside tolerance in every listed reading. Q(t) falls"""),
# fig4
("""  notes: Changed from partially_reproduced after verification round 1, as the criterion has no rule
    for partial and the time constant is outside tolerance in every listed reading. Measured""",
"""  notes: Changed from partially_reproduced after verification round 1, as the time constant, the
    quantity the claim is about, is outside tolerance in every listed reading. Measured"""),
# fig9
("""- claim: fig9-mgb-fast-decay
  outcome: reproduced
  notebook""","""- claim: fig9-mgb-fast-decay
  outcome: reproduced
  assumed: true
  notebook"""),
("""    their start or centre, and the mean after 0.5 s is 0.99 times the fitted constant; over all
    probes with bins at their start, tau1 is 0.080 s. The sizes are smaller than the paper's,
    alpha1 5.2 to 12.4 spikes/s against 15.0 and kappa 0.81 to 1.21 against 2.0. Without silence
    the first bin is 2.50 spikes/s, tau1 is 0.075 s over the running probes, and the fit over all
    probes does not converge to a decay (tau1 at its 100 s bound); apart from that fit, tau1 is at
    most 0.080 s. With spikes at half the detection threshold, tau1 is 0.064 s (running probes) and
    0.081 s (all), alpha1 7.0 to 15.4 spikes/s with silence counted. The plateau test compares the
    late mean with the fitted kappa, which the fit draws towards it; against the paper's kappa of
    2.0 the mean after 0.5 s is 0.39 to 0.60 of it.""",
"""    their start or centre, and the mean after 0.5 s is 0.99 times the fitted constant; over all
    probes with bins at their start, tau1 is 0.080 s. With silence counted the sizes are smaller
    than the paper's, alpha1 5.2 to 12.4 spikes/s against 15.0 and kappa 0.81 to 1.21 against 2.0.
    Without silence the first bin is 2.50 spikes/s, alpha1 is 1.56 to 3.04 and tau1 0.075 s over the
    running probes, and the fit over all probes does not converge to a decay (tau1 at its 100 s
    bound). With spikes at half the detection threshold, tau1 is 0.064 s (running probes) and 0.081
    s (all) with silence counted, alpha1 7.0 to 15.4 spikes/s; without silence tau1 is 0.083 s over
    the running probes (alpha1 2.34 to 4.26) and the fit over all probes does not converge either
    (tau1 31.3 s). Apart from those two fits, tau1 is at most 0.083 s. The plateau test compares the
    late mean with the fitted kappa, which the fit draws towards it, and holds in every converged fit
    (0.97 to 1.00). Against the paper's kappa of 2.0 the mean after 0.5 s is 0.39 to 0.60 of it with
    silence counted (0.45 to 0.66 at half the threshold), the rule for reproduced fails, and as tau1
    is below 0.3 s neither rule applies. The outcome rests on reading kappa as the fitted constant,
    marked as an assumption after verification round 2."""),
("""  - Spikes from the automatic detector of GetSpikes.m, as for a1-mgb-firing-rates; spikes at half
    its threshold are a second reading.
""","""  - Spikes from the automatic detector of GetSpikes.m, as for a1-mgb-firing-rates; spikes at half
    its threshold are a second reading.
  - Assumed that the plateau test of the criterion (the mean SD after 0.5 s within 25% of kappa)
    uses the fitted kappa. The criterion calls the test a plateau, a flattening of the curve at its
    own constant, and says the sizes, kappa among them, are reported against their values, not
    tested. Read with the paper's kappa of 2.0 the claim matches neither rule.
"""),
# fig7
("""    is significant in 4, last at 1.25 to 3.67 s; this nearest design does not decide the claim. The
    recording of Figure 7 is not in the data set, or not with the bands the legend gives.""",
"""    is significant in 4, last at 1.25 to 3.67 s. After verification round 2, which noted that three
    of these bands (0.25-1, 1-4 and 4-16 kHz) are the Figure 7 bands divided by 2.5 and that 0.25 kHz
    is below the Methods' carrier range of 0.625 to 40 kHz, the significance measure was run with
    only those three contexts. The forward variants are significant up to 3.6 s or later in 2 of the
    5 probes (last at 4.53 and 5.35 s; the others 0.05 s, 1.25 s and none) and the backward variants
    in none. The stored edges are read in Hz, as the generator named in these recordings' notes
    (DMRipple2.m, in the data set) documents ff as the "frequency range in Hz" and builds the
    carriers as ff(1) times powers of 2, and every stimulus was played at 97656 Hz, at which the
    stored top band of 8-32 kHz can be played and the same band times 2.5 (20-80 kHz) cannot. So no
    recording has the bands of the legend; the recording of Figure 7 is not in the data set, or not
    with those bands. The verifier's disagreement is recorded under verifications."""),
# finding
("""  statement: No recording has the design of Figure 7 (a natural sound probe after DMR contexts in
    0.625-2.5, 2.5-10 and 10-40 kHz). The DMR frequency variants in the data set use the bands 0.25-1
    to 8-32 kHz.""",
"""  statement: No recording has the design of Figure 7 (a natural sound probe after DMR contexts in
    0.625-2.5, 2.5-10 and 10-40 kHz). The DMR frequency variants in the data set use the bands 0.25-1
    to 8-32 kHz, in Hz by the stimulus code (DMRipple2.m), which extend below the carrier range of
    0.625 to 40 kHz that the paper's Methods give. Three of them (0.25-1, 1-4 and 4-16 kHz) are the
    Figure 7 bands divided by 2.5."""),
# round-1 a1-mgb reason
("""    reason: A1 at the 15 mV threshold on sequence files is within tolerance (spont 0.488, evoked
      0.541). No MGB reading has both means in tolerance, which meets the partial rule. Separately,""",
"""    reason: A1 at the 15 mV threshold on sequence files is within tolerance (spont 0.488, evoked
      0.541). No MGB reading has both means in tolerance; sequence files give spont 0.551 and evoked
      4.99, tuning files give 0.868 and 11.66. This meets the partial rule (A1 below 1 Hz, MGB evoked
      above 5 Hz in the "all" and "tuning" readings). Separately,"""),
("""      count checks are printed.
    response: ViewResp.m""","""      count checks are printed. Separately (point B12), the "tuning files only" MGB reading is not
      among the claims file's readings, and two files listed in both groups are counted twice in the
      per-cell sums.
    response: ViewResp.m"""),
("""      threshold is run as a reading for the rates and for fig9; it gives 7.15 Hz evoked, still
      outside tolerance. Outcome unchanged.""","""      threshold is run as a reading for the rates and for fig9; it gives 7.15 Hz evoked, still
      outside tolerance. Outcome unchanged. Point B12 was not answered in this revision; it is
      answered in the round-2 revision."""),
]
for old,new in R:
    assert s.count(old)==1,old[:80]; s=s.replace(old,new)
open(f,'w').write(s)
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 119, in <module>
AssertionError: recordings, 0.817 Hz in the second before each stimulus, and 5.07 Hz evoked (SD
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import re
src=open('/dev/stdin').read() if False else None
E
python3 - <<'E'
f='attempts/asari-2009-02.yaml'; s=open(f).read()
old="""    0.817 Hz in the second before each stimulus, and 5.07 Hz evoked (SD 11.46); the tuning-curve
    recordings alone give 0.868 and 11.66 Hz, and the sequence recordings alone 0.551 and 4.99 Hz."""
new="""    0.817 Hz in the second before each stimulus, and 5.07 Hz evoked (SD 11.46); the sequence
    recordings alone give 0.551 and 4.99 Hz, and the tuning-curve recordings alone, a comparison
    outside the claims file's readings, 0.868 and 11.66 Hz. Since verification round 2 a file listed
    in two groups of Summary.mat (the tuning-curve file of two A1 cells) is counted once; this moved
    one value in the third decimal (20-mV detector, all recordings, spontaneous 0.310 Hz)."""
assert s.count(old)==1; s=s.replace(old,new); open(f,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent**

Now the remaining replacements (same list, minus the first).

**Agent calls Bash**

```bash
cd  python3 - <<'E'
f='attempts/asari-2009-02.yaml'; s=open(f).read()
R=[
("""- claim: fig2-example-reliability
  outcome: reproduced
  notebook""","""- claim: fig2-example-reliability
  outcome: reproduced
  assumed: true
  notebook"""),
("""    fragments); this claim's criterion and outcome are unchanged.
""","""    fragments); this claim's criterion and outcome are unchanged. The outcome holds under the pairwise
    reading only, as leave-one-out (0.436) is outside the tolerance; marked as resting on that
    assumption after verification round 2.
  deviations:
  - Assumed that reliability is the mean correlation over pairs of trials of one context, as for
    fig2-example-long-context. The claims file leaves pairs and leave-one-out open, and the two give
    different outcomes (0.310, within 0.22 to 0.40, and 0.436, outside). The pairwise reading is
    adopted as the paper speaks of the "correlation coefficient of the response traces across trials"
    (Results, Context dependence, paragraph 2); the question for the paper's authors is under findings.
"""),
("""  notes: Changed from partially_reproduced after verification round 1, as the criterion has no rule
    for partial and the decay constant is outside tolerance in every listed reading. Q(t) falls""",
"""  notes: Changed from partially_reproduced after verification round 1, as the decay constant, the
    quantity the claim is about, is outside tolerance in every listed reading. Q(t) falls"""),
("""  notes: Changed from partially_reproduced after verification round 1, as the criterion has no rule
    for partial and the time constant is outside tolerance in every listed reading. Measured""",
"""  notes: Changed from partially_reproduced after verification round 1, as the time constant, the
    quantity the claim is about, is outside tolerance in every listed reading. Measured"""),
("""- claim: fig9-mgb-fast-decay
  outcome: reproduced
  notebook""","""- claim: fig9-mgb-fast-decay
  outcome: reproduced
  assumed: true
  notebook"""),
("""    their start or centre, and the mean after 0.5 s is 0.99 times the fitted constant; over all
    probes with bins at their start, tau1 is 0.080 s. The sizes are smaller than the paper's,
    alpha1 5.2 to 12.4 spikes/s against 15.0 and kappa 0.81 to 1.21 against 2.0. Without silence
    the first bin is 2.50 spikes/s, tau1 is 0.075 s over the running probes, and the fit over all
    probes does not converge to a decay (tau1 at its 100 s bound); apart from that fit, tau1 is at
    most 0.080 s. With spikes at half the detection threshold, tau1 is 0.064 s (running probes) and
    0.081 s (all), alpha1 7.0 to 15.4 spikes/s with silence counted. The plateau test compares the
    late mean with the fitted kappa, which the fit draws towards it; against the paper's kappa of
    2.0 the mean after 0.5 s is 0.39 to 0.60 of it.""",
"""    their start or centre, and the mean after 0.5 s is 0.99 times the fitted constant; over all
    probes with bins at their start, tau1 is 0.080 s. With silence counted the sizes are smaller
    than the paper's, alpha1 5.2 to 12.4 spikes/s against 15.0 and kappa 0.81 to 1.21 against 2.0.
    Without silence the first bin is 2.50 spikes/s, alpha1 is 1.56 to 3.04 and tau1 0.075 s over the
    running probes, and the fit over all probes does not converge to a decay (tau1 at its 100 s
    bound). With spikes at half the detection threshold, tau1 is 0.064 s (running probes) and 0.081
    s (all) with silence counted, alpha1 7.0 to 15.4 spikes/s; without silence tau1 is 0.083 s over
    the running probes (alpha1 2.34 to 4.26) and the fit over all probes does not converge either
    (tau1 31.3 s). Apart from those two fits, tau1 is at most 0.083 s. The plateau test compares the
    late mean with the fitted kappa, which the fit draws towards it, and holds in every converged fit
    (0.97 to 1.00). Against the paper's kappa of 2.0 the mean after 0.5 s is 0.39 to 0.60 of it with
    silence counted (0.45 to 0.66 at half the threshold), the rule for reproduced fails, and as tau1
    is below 0.3 s neither rule applies. The outcome rests on reading kappa as the fitted constant,
    marked as an assumption after verification round 2."""),
("""  - Spikes from the automatic detector of GetSpikes.m, as for a1-mgb-firing-rates; spikes at half
    its threshold are a second reading.
""","""  - Spikes from the automatic detector of GetSpikes.m, as for a1-mgb-firing-rates; spikes at half
    its threshold are a second reading.
  - Assumed that the plateau test of the criterion (the mean SD after 0.5 s within 25% of kappa)
    uses the fitted kappa. The criterion calls the test a plateau, a flattening of the curve at its
    own constant, and says the sizes, kappa among them, are reported against their values, not
    tested. Read with the paper's kappa of 2.0 the claim matches neither rule.
"""),
("""    is significant in 4, last at 1.25 to 3.67 s; this nearest design does not decide the claim. The
    recording of Figure 7 is not in the data set, or not with the bands the legend gives.""",
"""    is significant in 4, last at 1.25 to 3.67 s. After verification round 2, which noted that three
    of these bands (0.25-1, 1-4 and 4-16 kHz) are the Figure 7 bands divided by 2.5 and that 0.25 kHz
    is below the Methods' carrier range of 0.625 to 40 kHz, the significance measure was run with
    only those three contexts. The forward variants are significant up to 3.6 s or later in 2 of the
    5 probes (last at 4.53 and 5.35 s; the others 0.05 s, 1.25 s and none) and the backward variants
    in none. The stored edges are read in Hz, as the generator named in these recordings' notes
    (DMRipple2.m, in the data set) documents ff as the "frequency range in Hz" and builds the
    carriers as ff(1) times powers of 2, and every stimulus was played at 97656 Hz, at which the
    stored top band of 8-32 kHz can be played and the same band times 2.5 (20-80 kHz) cannot. So no
    recording has the bands of the legend; the recording of Figure 7 is not in the data set, or not
    with those bands. The verifier's disagreement is recorded under verifications."""),
("""  statement: No recording has the design of Figure 7 (a natural sound probe after DMR contexts in
    0.625-2.5, 2.5-10 and 10-40 kHz). The DMR frequency variants in the data set use the bands 0.25-1
    to 8-32 kHz.""",
"""  statement: No recording has the design of Figure 7 (a natural sound probe after DMR contexts in
    0.625-2.5, 2.5-10 and 10-40 kHz). The DMR frequency variants in the data set use the bands 0.25-1
    to 8-32 kHz, in Hz by the stimulus code (DMRipple2.m), which extend below the carrier range of
    0.625 to 40 kHz that the paper's Methods give. Three of them (0.25-1, 1-4 and 4-16 kHz) are the
    Figure 7 bands divided by 2.5."""),
("""    reason: A1 at the 15 mV threshold on sequence files is within tolerance (spont 0.488, evoked
      0.541). No MGB reading has both means in tolerance, which meets the partial rule. Separately,""",
"""    reason: A1 at the 15 mV threshold on sequence files is within tolerance (spont 0.488, evoked
      0.541). No MGB reading has both means in tolerance; sequence files give spont 0.551 and evoked
      4.99, tuning files give 0.868 and 11.66. This meets the partial rule (A1 below 1 Hz, MGB evoked
      above 5 Hz in the "all" and "tuning" readings). Separately,"""),
("""      count checks are printed.
    response: ViewResp.m""","""      count checks are printed. Separately (point B12), the "tuning files only" MGB reading is not
      among the claims file's readings, and two files listed in both groups are counted twice in the
      per-cell sums.
    response: ViewResp.m"""),
("""      threshold is run as a reading for the rates and for fig9; it gives 7.15 Hz evoked, still
      outside tolerance. Outcome unchanged.""","""      threshold is run as a reading for the rates and for fig9; it gives 7.15 Hz evoked, still
      outside tolerance. Outcome unchanged. Point B12 was not answered in this revision; it is
      answered in the round-2 revision."""),
]
for old,new in R:
    assert s.count(old)==1,old[:80]; s=s.replace(old,new)
open(f,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/asari-2009-02.yaml <<'E'
- date: '2026-11-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)
  reviewed: Round 2. The full executed notebooks reproduce_asari_2009.ipynb and strf_asari_2009.ipynb
    with the conclusions and the summary, the helper modules, the README, the attempt record and the
    claims file, with the paper's full text. Its report is transcripts/asari-2009/verifier-2-report.md.
  results:
  - claim: methods-recording-counts
    agrees: true
    outcome: partially_reproduced
    reason: 305/39 and 93/14 are exact under both silence readings (cell 14). A1 has 132 cells, or 118
      in the five named ensembles, against 123.
    response: No change.
  - claim: a1-mgb-firing-rates
    agrees: true
    outcome: partially_reproduced
    reason: The A1 detector assumption is stated and reasonable. The partial rule holds with both MGB
      detectors (5.07 and 7.15 Hz, cell 17). Separately, cell 18 shows many large deflections between
      half the threshold and the threshold (file 34 has 1220 spikes, against 23781 at half the
      threshold); the rates outcome and the fig9 tau hold under both detectors, but the MGB evoked
      rate and the fig9 magnitudes stay uncertain. The README row leaves out "resting on an
      assumption". Point B12 (the tuning-files-only reading is not in the claims file, and the
      duplicated tuning file is counted twice for two A1 cells) is not recorded anywhere, and the
      restated round-1 reason is garbled.
    response: A file listed in two groups of Summary.mat is now counted once in the per-cell rates;
      one value moved in the third decimal (20 mV, all recordings, spontaneous 0.309 to 0.310 Hz) and
      the measured values are unchanged. The tuning-only rows are now labelled in the notebook, the
      conclusion and the notes as a comparison outside the claims file's readings. B12 is added to the
      round-1 entry, and the round-1 reason now quotes the round-1 report. The README row says the
      outcome rests on an assumption. The uncertainty of the MGB detector is left as stated in the
      notes; no further detector was run. Outcome unchanged.
  - claim: fig2-example-reliability
    agrees: true
    outcome: reproduced
    reason: The outcome depends on the pairwise reading (0.310). Leave-one-out gives 0.436, outside
      tolerance. fig2-example-long-context marks this same choice assumed; this claim should too, or
      say it holds under one reading.
    response: Marked assumed, with a deviation that states the choice and the two results; the
      conclusion, the summary and the README say it rests on the pairwise reading. Outcome unchanged.
  - claim: fig2-example-long-context
    agrees: true
    outcome: reproduced
    reason: The pairwise assumption is stated and reasonable, since it alone gives the population
      0.31. The gap of 1.60 to 3.97 s is confirmed at 0.1 ms (cell 27). The README row "absent from 2
      to 4 s" conflicts with the output, as the matched probe is significant again from 3.971 s and
      fails the 2 to 4 s reading (strict_2_4 False).
    response: The README row now states the amended criterion (before 2 s, none from 2 to 3.6 s,
      again after 3.6 s). Outcome unchanged.
  - claim: fig3a-proportion-significant
    agrees: true
    outcome: reproduced
    reason: Silence counted, all probes, 187, 0.613 and 0.251 (cell 30).
    response: No change.
  - claim: fig3a-significance-decay
    agrees: true
    outcome: partially_reproduced
    reason: Cell 34.
    response: No change.
  - claim: fig3b-fractional-power-decay
    agrees: true
    outcome: not_reproduced
    reason: tau1 is 1.27 to 1.78 s in all 8 listed readings (cell 37). The stated reason, "criterion
      has no rule for partial", also fits methods-recording-counts, which is graded partial. The real
      reason is that tau, the quantity the claim is about, fails.
    response: The notes and the conclusion now give that reason; the same wording is used for
      fig4-predictability-upper-bound. Outcome unchanged.
  - claim: timescale-longer-than-membrane
    agrees: true
    outcome: reproduced
    reason: Cell 44.
    response: No change.
  - claim: fig4-predictability-upper-bound
    agrees: true
    outcome: not_reproduced
    reason: tau1 is within tolerance in 0 of 24 fits (cell 41).
    response: No change to the outcome; the reason in the notes and conclusion is reworded as for
      fig3b-fractional-power-decay.
  - claim: fig4-strf-performance-low
    agrees: true
    outcome: partially_reproduced
    reason: The claims file's test is stated and reasonable; the outcome also rests on using 16 of
      the paper's 20 cells. Wilcoxon p = 0.0031 and 0.025 (strf cell 10). The README row leaves out
      "resting on an assumption", and the README gives about 24 minutes for the STRF notebook where it
      printed 31.2 min. Point B11, the 10-kHz response-sampling reading, was not run.
    response: The README and summary rows say the outcome rests on the claims file's test and 16 of 20
      cells. In this run the STRF notebook printed 23.6 min; the README gives both runs. The 10-kHz
      reading was again not run, as the verifier lists it among the points that do not affect a
      conclusion. Outcome unchanged.
  - claim: fig5-example-conductances
    agrees: true
    outcome: blocked
    reason: No voltage-clamp files in the data set.
    response: No change.
  - claim: fig6-conductance-decay
    agrees: true
    outcome: blocked
    reason: No voltage-clamp files in the data set.
    response: No change.
  - claim: fig8a-proportion-by-property
    agrees: true
    outcome: partially_reproduced
    reason: Yes, but fragile. The order amplitude > frequency holds by 0.0025 (43/70 against 52/85),
      so one test flips it. It fails with every set as a test (cell 59). This dependence should stay
      explicit wherever the outcome is reported.
    response: The README and summary rows now give the margin and the failure with every set as a
      test. Outcome unchanged.
  - claim: fig8a-significance-fits
    agrees: true
    outcome: not_reproduced
    reason: The sizes are out of order in every reading (cell 62).
    response: No change.
  - claim: fig8b-decay-by-property
    agrees: true
    outcome: not_reproduced
    reason: This holds only in the main reading. Adding the naturalistic probes gives partial (cell
      65). The property-set assumption is stated and checked against Table 1 rows. The main reading
      is said to be fixed before results; nothing in the materials can verify that.
    response: The README and summary rows now say the outcome is partial with the naturalistic probes
      added. Nothing in the record can show when the main reading was fixed, and the statement is
      left as the author's. Outcome unchanged.
  - claim: fig8c-relative-effects
    agrees: true
    outcome: not_reproduced
    reason: Same dependence on the reading as fig8b (cell 68). The Summary row "amplitude and
      frequency effects smaller than natural" is too strong for frequency; in the main reading
      without silence, with as many probes as the set holds, the frequency interval is 0.552 to 1.066
      and includes 1 (cell 68, row 7).
    response: The summary row now gives the reason the rules fail (the amplitude interval below 1 in
      every main-reading variant, the higher-order estimate above the amplitude one) and the
      dependence on the reading; the README row gives the dependence. Outcome unchanged.
  - claim: fig8-natural-synthetic-probes-alike
    agrees: true
    outcome: reproduced
    reason: Low power. There are no synthetic FM probes, and the synthetic AM probes come from 2 cells.
    response: No change; the notes already say so.
  - claim: fig9-mgb-fast-decay
    agrees: true
    outcome: reproduced
    reason: Yes, but undeclared assumption. Reproduced only if the plateau's kappa means the fitted
      kappa, which is close to circular. Against the paper's kappa = 2.0 the late mean is 0.39 to 0.60
      of it (cell 47). Then the criterion's reproduced rule fails and no rule applies. This should be
      assumed. Cell 48's alpha1 and kappa ranges cover only the silence-counted readings (without
      silence alpha1 is 1.56 to 3.04); the half-threshold fit without silence over all probes does
      not converge either (tau1 = 31.3 s); and "apart from that fit, tau1 is at most 0.080 s" is true
      only for the automatic detector, as the half-threshold fit without silence gives 0.083 s.
    response: Marked assumed, with a deviation giving the reason for reading kappa as the fitted
      constant and the result under the paper's kappa. The conclusion and notes now give the ranges
      by silence reading, the second fit that does not converge, and tau1 at most 0.083 s. Outcome
      unchanged.
  - claim: fig9-example-first-bin
    agrees: true
    outcome: reproduced
    reason: Cell 50.
    response: No change.
  - claim: fig7-example-frequency-context
    agrees: false
    reason: Not established. The search now covers all 105 recordings, but the block still reads ff
      as Hz at face value. The five "DMR; frequency variants" recordings with a natural probe include
      bands at 0.25 to 1, 1 to 4 and 4 to 16 kHz, exactly the Figure 7 bands divided by 2.5, and 0.25
      kHz is below the 0.625 to 40 kHz carrier range given in the Methods. These recordings may hold
      the Figure 7 design with differently stored band edges. The forward set already reaches 3.673 s
      in 20060916-ha3-002 (cell 54). Running the significance measure on the three-context subset
      would settle it; until then, "blocked (data_missing)" and the matching finding are not
      supported. The round-1 entry has no outcome field.
    response: The significance measure is now run on the three-context subset of each of the five
      recordings (cell 54). The forward variants reach 3.6 s or later in 2 of 5 probes (4.53 and 5.35
      s) and the backward variants in none. The notebook also prints the lines of DMRipple2.m, the
      generator named in the recordings' notes, which give ff as the frequency range in Hz and build
      the carriers from it, and the stimulus rate of 97656 Hz, at which the stored 8-32 kHz band can
      be played and the same band times 2.5 cannot. The edges are therefore kept in Hz, and the claim
      is kept blocked (data_missing) with the disagreement recorded here; the finding now says the
      deposited bands extend below the Methods' carrier range and that three of them are the Figure 7
      bands divided by 2.5. The round-1 verifier gave no outcome for this claim, so none is recorded.
  - claim: figs1-silence-probe
    agrees: true
    outcome: reproduced
    reason: Cell 74.
    response: No change.
E
python tools/entry.py check entries/asari-2009 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import re,yaml
lines=open('attempts/asari-2009-02.yaml').read().splitlines()
for n,l in enumerate(lines,1):
    body=re.sub(r'^\s*(- )?[A-Za-z_]+: ','',l) if re.match(r'^\s*(- )?[A-Za-z_]+:( |$)',l) else l
    if ': ' in body or body.rstrip().endswith(':') and not re.match(r'^\s*(- )?[A-Za-z_]+:$',l): print(n,l)
yaml.safe_load(open('attempts/asari-2009-02.yaml'))
E
grep -n "—\|rather" attempts/asari-2009-02.yaml entries/asari-2009/README.md entries/asari-2009/reproduce_asari_2009.ipynb | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/asari-2009 2>&1 | tail -5; date -u
```

```
Sun Nov 15 17:23:41 UTC 2026
Installed kernelspec registry-asari-2009 in executed/asari-2009/.venv/share/jupyter/kernels/registry-asari-2009
0 error(s)
pass  reproduce_asari_2009.ipynb  (293 s)
pass  strf_asari_2009.ipynb  (1414 s)
Sun Nov 15 17:52:13 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import json
nb=json.load(open('executed/asari-2009/reproduce_asari_2009.ipynb'))
for i in (17,47,54,78):
    for o in nb['cells'][i].get('outputs',[]):
        if 'text' in o and ('20 mV' in o['text'] if isinstance(o['text'],str) else True): pass
t=lambda i:''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
print(t(54)[-1200:]); print(t(78))
print([l for l in t(17).splitlines() if '20 mV' in l])
nb2=json.load(open('executed/asari-2009/strf_asari_2009.ipynb')); print(''.join(''.join(o.get('text','')) for o in nb2['cells'][-1].get('outputs',[])))
E
```

```
0.25-1, 1-4, 4-16       4      5.70        [97656]        False                 NaN
3  20060916-ha3-003-002.mat  backward         3  0.25-1, 1-4, 4-16       4      5.70        [97656]        False                 NaN
4  20060916-ha4-001-002.mat   forward         3  0.25-1, 1-4, 4-16       6      5.08        [97656]         True               4.532
5  20060916-ha4-001-002.mat  backward         3  0.25-1, 1-4, 4-16       6      5.08        [97656]         True               0.180
6  20060916-ha5-002-002.mat   forward         3  0.25-1, 1-4, 4-16       6      5.80        [97656]         True               5.354
7  20060916-ha5-002-002.mat  backward         3  0.25-1, 1-4, 4-16       6      5.80        [97656]         True               2.777
8  20060917-ha1-002-002.mat   forward         3  0.25-1, 1-4, 4-16       6      5.08        [97656]         True               1.253
9  20060917-ha1-002-002.mat  backward         3  0.25-1, 1-4, 4-16       6      5.08        [97656]         True               0.109
probes (forward variants) significant up to 3.6 s or later: 2 of 5 | backward: 0 of 5
the band 8-32 kHz times 2.5 would be 20-80 kHz, above half the stimulus sampling rate (48.8 kHz)

notebook runtime 4.8 min; peak memory 6.69 GB

['4      A1           20 mV     all    145       0.310     0.367     0.214   0.295        0.447      0.530', '5      A1           20 mV     seq    145       0.409     0.505     0.423   0.583        0.453      0.542']
runtime 23.5 min; peak memory 3.87 GB
```

**Agent**

No outcome changed and nothing is proposed for a third round. I re-ran the entry with `python tools/entry.py all entries/asari-2009`: 0 check errors, both notebooks pass, and the conclusions match the new numbers. I recorded round 2 under `verifications`, with the verifier's reasons in its words and my reply under `response`.

**Disagreement kept: fig7 stays blocked (`data_missing`)**
- I ran the test the verifier asked for: the five recordings, using only the three bands that equal the Figure 7 bands divided by 2.5 (0.25–1, 1–4 and 4–16 kHz).
- With the forward stimulus variants as contexts, 2 of 5 probes stay significant to 3.6 s or later (4.53 and 5.35 s). With the backward variants, none do.
- I still read the stored band edges as Hz, for two reasons:
  - The authors' generator code in the data set (`DMRipple2.m`) defines the band parameter as "frequency range in Hz" and builds the tones directly from it.
  - The sounds were played at 97656 Hz. The top stored band, 8–32 kHz, can be played at that rate; the same band times 2.5 (20–80 kHz) cannot.
- The record keeps the verifier's disagreement. The data finding now says the deposited bands extend below the 0.625–40 kHz range given in the paper's Methods, and that three of them are the Figure 7 bands divided by 2.5.

**Marked as resting on an assumption (outcome unchanged)**
- **fig2-example-reliability:** reproduced only with reliability taken over pairs of trials (0.310). Correlating each trial with the mean of the others gives 0.436, outside tolerance. I added a deviation saying so.
- **fig9-mgb-fast-decay:** reproduced only if the plateau test compares against the fitted constant. Against the paper's 2.0, neither rule of the criterion applies. The deviation gives my reason for the first reading and the result under the second.

**Corrected or added**
- **fig9 text:** the size ranges are now split by whether silence counts as a context. I added the second fit that does not converge (31.3 s), and the bound is now "tau1 at most 0.083 s".
- **fig3b and fig4:** the stated reason is now that the time constant, the quantity each claim is about, fails in every reading.
- **Summary, fig8c row:** no longer says the frequency effect is smaller than for natural sounds.
- **fig8a, 8b and 8c rows** (Summary and README): now say how the outcome depends on which stimulus sets are counted.
- **README:**
  - The fig2 row now states the amended criterion.
  - Four more rows say their outcome rests on an assumption.
  - The STRF runtime now gives both runs, 24 and 31 minutes.
- **Point B12:**
  - A recording file listed under two groups is now counted once in the firing rates. One value moved in the third decimal (0.309 to 0.310 Hz); the measured values are unchanged.
  - The MGB rows using tuning-curve recordings only are labelled as outside the claims file's readings.
  - B12 is now recorded in round 1.
- **Round 1 record:** the garbled firing-rates reason now quotes the round-1 report.

**Not done**
- I did not run the 10-kHz response-sampling version of the STRF models (B11), because the verifier lists it as not affecting a conclusion.
- I ran no further MGB spike detector. The uncertainty in the MGB evoked rate and the fig9 magnitudes stays as stated in the notes.
- I did not add a question for the paper's authors on the fig9 plateau assumption, because it is about the claims file's wording, not a method in the paper.
- The verifier reported no place where the claims file misreads the paper, so `questions/asari-2009.yaml` is unchanged.
- The round-1 fig7 result still has no `outcome`, because that verifier gave none.
- Nothing can show when the fig8 main reading was fixed, so that statement stays as my own.

## End of run

48 turns, 64 minutes, $2.95 at API prices, result: success.
