# brudner-2026 · author-revise-3 · run 43190261081

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/brudner-2026/verifier-3-report.md; ls entries/brudner-2026; grep -n "step 6\|^## \|^### " docs/protocol.md | head -60
```

```
Thu Nov 12 09:23:51 UTC 2026
# Round 3 verifier report: brudner-2026-01

The attempt record lists 22 claims under `outcomes`. Only one has a `proposed` block: figs5c-turn-angles, at `brudner-2026-01.yaml:339`. I reviewed only that claim.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| figs5c-turn-angles | not_reproduced | Yes | — | Cell 24 measures the claims file's two displacements over the dataset's turn events: the heading change from start to stop, and the integral of dtheta over the event. Under both turn sets the claims file names (all turns pooled, or the kept turns), and with every complex file set, the medians are −19.6 to −21.4 and +20.7 to +22.0 degrees. The tolerances are −34.2 ± 3.42 and +33.8 ± 3.38, so every one is outside. The criterion says "Reproduced when both medians are within tolerance under one reading", and no named reading passes. The only bounds that pass are the 20% crossings on both edges of the peak. That reading is not in the claims file, the SI states the 20% rule only for the rising edge (turn onset), and the record says it was adopted after the event bounds failed. So it cannot decide the outcome and is rightly kept as a variant. |

## How I checked it

- **The numbers come from the data.** In `plumes.py:349-357`, `theta_start`/`theta_stop` and `int_dtheta` are read from each file's own heading and dtheta between the event's start and stop indices. Turns are split by the sign of dtheta at the peak, as the S5C legend says. The pooled sets have 80,445, 86,450 and 103,095 turns, and the kept sets have 3,141 and 3,531.
- **The heading change and the integral agree with each other.** The two event measures differ by no more than about 1 degree.
- **The extra readings also fail or are unstated.** Integrating over the run at or above half the peak (Fig. S5A measures peak width at half height) gives −25.0 to −26.6 and +26.8 to +27.7, outside tolerance under every set. Only the 20% bounds g
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 433,535p docs/protocol.md; sed -n 639,700p docs/protocol.md; ls attempts 2>/dev/null | head; find . -name "brudner-2026-01*" -not -path "./.git/*"
```

```
### 5. Record the attempt

Write `attempts/<paper>-<nn>.yaml`, numbered after the paper's earlier attempts.

- **`datasets`**: every dataset the attempt used, each with `archive`, `id`,
  the pinned `version`, its `doi` where the archive gives one, and
  `relation` as `papers/datasets/<paper>.yaml` gives it (`primary` or
  `reuses`). Use as many of the paper's datasets as can be loaded.
- **`missing_datasets`**: each dataset the paper's claims rest on that this
  attempt could not use, with `archive` and `id` where it has them, and
  `why` (not in any open archive, not yet converted, unreadable). A missing
  dataset does not stop the attempt: test what the others allow, and block
  each claim that needs a missing one with `dataset_missing`. The site flags
  the attempt, so that a later one can add the dataset.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
  - `reproduced`: the result matches the claim.
  - `partially_reproduced`: the effect is present but weaker, or holds only in
    part.
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 320,380p attempts/brudner-2026-01.yaml; grep -n "^verifications\|^  - round\|round:" attempts/brudner-2026-01.yaml
```

```
and +35.8; kept turns -32.7 and +36.2), all within tolerance of -34.2 +/- 3.42 and +33.8 +/- 3.38.
    Over the files' events (start to stop), the claims file's two displacements, the medians are -19.6
    to -21.4 and +20.7 to +22.0 under every turn set, outside tolerance. Over the run at or above half
    the peak (Fig. S5A measures peak width at half height) they are -25.0 to -26.6 and +26.8 to +27.7,
    outside tolerance. The events lie inside the half-height run (start a median of 1 frame after its
    rising crossing, stop 1 frame before its falling one; median length 7 frames against 10 for the half-height
    run and 16 for the 20% run), and 99.9% stop before the 20% crossing on the falling edge. By group,
    over the SI-bounded turn, smooth -34.1 and +35.2, smoke-1a -35.1 and +35.1, smoke-2a -37.6 and +37.7.
    The first version's run of |dtheta| gives the same medians. Whether the dataset's events are the paper's
    turn bounds is asked of a reader.
  deviations:
  - Assumed the turn runs from the SI's onset (20% of the peak on the rising edge; SI, Behavioral Analysis)
    to the 20% crossing on the falling edge of the rotation in the turn's direction, the end the paper
    does not state; this bound was adopted after the event bounds failed. The claims file's readings integrate
    over the event; the files' events start after the paper's onset (a median of 4 frames), so the paper's
    turn is taken as the event, bounded as the SI defines its onset. Over the files' events neither displacement
    is within tolerance, nor over the half-height run.
  - The complex files are smoke-1a, as assumed for fig5e-cue-betas; smoke-2a and both sets are shown and
    give the same outcome.
  proposed:
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 300,320p attempts/brudner-2026-01.yaml; sed -n 418,2000p attempts/brudner-2026-01.yaml | grep -n "round\|^  [a-z]\|^- " | head -40
```

```
notes: The files code turn direction as +1 or -1, the sign of the rotational velocity at the event's
    peak (all 15841 turns checked), and describe it only as 'Turn direction label'. The heading is atan2(-vy,
    vx) (92.5% of moving frames within 30 degrees), so +1 turns are counterclockwise in the (x, -y) frame,
    but whether that is left or right depends on how the camera viewed the arena, which the files do not
    state; nor do they say where the projector mount is. The intensity coefficient of the full model (heading
    160 to 200) favours the -1 direction in the smooth plume (-0.0497, p below 0.0001, SI onset; -0.0506
    with the turn start; also per trajectory) and is not significant in the complex plume (smoke-1a +0.0058,
    p 0.27; smoke-2a -0.0001, p 0.95; every onset and z-scoring p above 0.26). So the criterion holds
    under every reading if -1 is a right turn and fails under every reading if +1 is a right turn.
- claim: figs5c-turn-angles
  outcome: reproduced
  assumed: true
  notebook: reproduce_brudner_2026.ipynb
  output: claim:figs5c-turn-angles
  measured:
  - -34.3
  - 35.2
  notes: All detected turns of both plumes pooled (smooth and smoke-1a, 80445 turns), the integral of
    rotational velocity over the turn bounded by the 20% crossings of its peak in the turn's direction,
    gives medians of -34.3 and +35.2 degrees (with smoke-2a -35.0 and +35.9; with both complex sets -35.0
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 418,440p attempts/brudner-2026-01.yaml; sed -n 622,700p attempts/brudner-2026-01.yaml; grep -n -A25 "figs5c-turn-angles" papers/claims/brudner-2026.yaml 2>/dev/null || grep -rln "figs5c-turn-angles" --include=*.yaml . | head
```

```
verifications:
- date: '2026-11-12'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The handover of the author run, the executed notebook with the conclusions and summary
    removed, except one Result cell (then cell 26) that the handover left in, the helper module and the
    claims file; the verifier also read the paper under paper/ and the archive's file list and dandiset
    description.
  results:
  - claim: fig5e-cue-betas
    agrees: false
    outcome: not_reproduced
    reason: 'The criterion counts a claim as reproduced only if every reading gives that result; here
      the result depends on the reading. With the SI onset and smoke-2a, both plumes pass with stored
      or pooled z-scored signals; per-trajectory z-scoring fails both plumes. Under the code''s readings
      the complex coefficients have the wrong sign and are out of tolerance. The choice of complex file
      set is doubtful: the archive''s dandiset description says smoke_1a_orig was analyzed throughout
      the paper, and smoke-1a with the event start and heading 160 to 200 reproduces the published Fig.
      5E coefficients almost exactly. The onset rule ignores the sign of the rotation and can run into
      an adjacent opposite-direction turn.'
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A25 "id: figs5c-turn-angles" claims/brudner-2026.yaml; awk 'NR>=622' attempts/brudner-2026-01.yaml | grep -n -B2 -A12 "figs5c-turn"; tail -5 attempts/brudner-2026-01.yaml
```

```
618:- id: figs5c-turn-angles
619-  statement: The detected saccade-like turns reorient flies by about 30 degrees, with median angular
620-    displacements of -34.2 and +33.8 degrees for the two turn directions.
621-  source: SI Figure S5C, legend; Results, Different Directional Odor Cues Predict Fly Crosswind
622-    Turning in Different Plume Types, paragraph 2
623-  quote: Median values (dashed lines; -34.2°, +33.8°) are similar to turn displacements reported in
624-    flies navigating plumes of smoke
625-  expected:
626-  - quantity: median angular displacement, negative-velocity turns
627-    value: -34.2
628-    tolerance: 3.42
629-    unit: degrees
630-  - quantity: median angular displacement, positive-velocity turns
631-    value: 33.8
632-    tolerance: 3.38
633-    unit: degrees
634-  criterion: Turns are the dataset's detected turn events, split by the sign of the rotational
635-    velocity at the peak (Fig. S5C legend). Open, with readings named. Which turns, (a) all detected
636-    turns of both plumes pooled, (b) only the turns kept in fig5e-cue-betas. The displacement,
637-    (a) the heading change from the event's start to its end, (b) the integral of rotational
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/brudner-2026; grep -n -i "s5c\|turn-angle\|turn angle\|34\.\|reproduced" README.md entry.yaml | head -40; cd ../..; grep -n -i "s5c\|turn-angles\|^notes\|^summary" attempts/brudner-2026-01.yaml | head
```

```
README.md:11:| Fig. 5E, gradient predicts turns in the smooth plume, motion in the complex plume | Not reproduced |
README.md:12:| Fig. 5F, cue dominance positive (smooth) and negative (complex) | Partially reproduced, resting on assumptions (file set and turn onset) |
README.md:13:| Fig. S5C, turns of about -34 and +34 degrees | Reproduced, resting on an assumption; a change to not reproduced is proposed |
README.md:14:| Fig. 2C, motion predicts the centerline side better than the gradient (complex plume) | Partially reproduced, resting on an assumption |
README.md:15:| Fig. 2E, motion weighted above the gradient (complex plume) | Partially reproduced |
README.md:16:| Fig. S1F-G, cue maps robust to sensor spacing and delay | Not reproduced |
README.md:27:motion cue becomes significant (p 0.0079). Fig. 5F would be reproduced with the files' own turn start
README.md:30:files' own turn start, and closely by the smoke-1a files with the SI's onset. Fig. S5C is reproduced
README.md:33:not reproduced is proposed for the next verification round.
entry.yaml:8:  cue dominance of Fig. 5, the turn angles of Fig. S5C, the centerline logistic models of Fig. 2 in the
309:- claim: figs5c-turn-angles
313:  output: claim:figs5c-turn-angles
347:      and the bounds are asked of a reader (questions/brudner-2026.yaml). Notebook, figs5c-turn-angles.
414:    for the displacement of Fig. S5C? (5) How is the motion cue of Fig. S1G defined for a sensor spacing
459:  - claim: figs5c-turn-angles
773:  - claim: figs5c-turn-angles
```

**Agent calls Bash**

```bash
cd entries/brudner-2026; sed -n 1,60p README.md; cd ../..; sed -n 1,30p attempts/brudner-2026-01.yaml; sed -n 400,417p attempts/brudner-2026-01.yaml
```

```
# Brudner, Zhou et al. (2026) from dandiset 001871

Tests the findings of [Brudner, Zhou et al. (2026)](https://doi.org/10.1073/pnas.2608896123) that can
be tested on [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657). It holds the
walking trajectories and turn events of flies navigating a projected smooth plume (83 trials) and a
complex smoke plume (48 trials, in two sets named smoke-1a and smoke-2a), a 1500-frame window of the
complex plume movie, and three freestream plume windows. The smooth plume movie is not in it.

| Claim | Outcome |
|---|---|
| Fig. 5E, gradient predicts turns in the smooth plume, motion in the complex plume | Not reproduced |
| Fig. 5F, cue dominance positive (smooth) and negative (complex) | Partially reproduced, resting on assumptions (file set and turn onset) |
| Fig. S5C, turns of about -34 and +34 degrees | Reproduced, resting on an assumption; a change to not reproduced is proposed |
| Fig. 2C, motion predicts the centerline side better than the gradient (complex plume) | Partially reproduced, resting on an assumption |
| Fig. 2E, motion weighted above the gradient (complex plume) | Partially reproduced |
| Fig. S1F-G, cue maps robust to sensor spacing and delay | Not reproduced |
| Rightward turning bias with light intensity | Blocked: metadata insufficient |
| 15 claims on the smooth plume, the trained networks and the agents | Blocked: the smooth plume (Dryad) could not be read |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
[... 71 more lines not kept]
```

**Agent**

Now the notebook's conclusion and summary cells.

**Agent calls Bash**

```bash
cd entries/brudner-2026; python - <<'EOF'
import json
nb=json.load(open('reproduce_brudner_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and ('S5C' in s or 's5c' in s or 'Summary' in s[:200] or 'proposed' in s):
        print('=== cell',i, c.get('metadata',{}).get('tags')); print(s[:4000])
EOF
```

```
=== cell 0 None
# Reproducing Brudner, Zhou et al. (2026) from dandiset 001871

**Paper.** Brudner S, Zhou B, Jayaram V, Madeira Santana G, Crimaldi J, Clark DA, Emonet T (2026).
Fly navigational responses exploit plume-specific odor motion and gradient cues. *PNAS* 123(29)
e2608896123. [doi:10.1073/pnas.2608896123](https://doi.org/10.1073/pnas.2608896123). The claims file
(`claims/brudner-2026.yaml`) was written from the version of record and its SI Appendix; this attempt
read the same text, under `paper/`.

**Dandiset.** [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657), version
0.260630.1657. The paper cites no version. This is the only published version and the one the paper's
code (github.com/emonetlab/GradientMotionMultiplePlumes, commit effc7b0, `metadata/published_panel_params.json`)
names as the source of its Fig. 5 tables. The draft has the same 136 assets and total size.

**What the dandiset holds.** 131 behavior NWB files, one per trial of a fly cohort (83 smooth-plume
files, "nagel-smoke"; 24 "smoke-1a" and 24 "smoke-2a" complex-plume files), with per-trajectory
position, heading, velocities and the odor intensity, gradient and motion signals at the antennae,
and a table of turn events; the complex plume movie window (frames 300 to 1799 of smoke_1a_orig);
three freestream plume windows; and a compact asset of Fig. S1 panel inputs. The smooth plume movie
is not in it: it is on Dryad (doi:10.5061/dryad.g27mq71), which answers 401 to downloads without an
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/brudner-2026; python - <<'EOF'
import json
nb=json.load(open('reproduce_brudner_2026.ipynb'))
c=nb['cells'][24]
print(''.join(c['source'])[-2500:])
for o in c['outputs']:
    print(''.join(o.get('text','')) if 'text' in o else o.get('data',{}).get('text/plain'))
EOF
ls ../../executed/brudner-2026/ 2>/dev/null
```

```
]),
    "all turns, smooth + complex smoke-2a": pd.concat([TT[("smooth", "start")], TT[("complex_2a", "start")]]),
    "all turns, smooth + both complex": pd.concat([TT[("smooth", "start")], TT[("complex_both", "start")]]),
    "kept turns (SI onset, 160-200, no margin), smooth + smoke-1a": pd.concat([plumes.keep(TT[("smooth", "rule20")], main_s), plumes.keep(TT[("complex_1a", "rule20")], main_s)]),
    "kept turns (SI onset, 160-200, no margin), smooth + smoke-2a": pd.concat([plumes.keep(TT[("smooth", "rule20")], main_s), plumes.keep(TT[("complex_2a", "rule20")], main_s)]),
}
rows = []
for name, tt in sets.items():
    for meas, (neg, pos) in medians(tt).items():
        rows.append({"turns": name, "n": len(tt), "measure": meas, "median, negative": neg, "median, positive": pos,
                     "within tolerance": abs(neg + 34.2) <= 3.42 and abs(pos - 33.8) <= 3.38})
print(pd.DataFrame(rows).to_string(index=False))
for g in ["smooth", "complex_1a", "complex_2a"]:
    print(g, "by group, all turns:", medians(TT[(g, "start")]))
allt = pd.concat([TT[("smooth", "start")], TT[("complex_both", "start")]])
d = (allt.theta_stop - allt.theta_start + 180) % 360 - 180
print("Range of the heading change over all turns:", round(d.min(), 1), "to", round(d.max(), 1), "deg; 5th and 95th percentiles of |change|:",
      np.percentile(np.abs(d), [5, 95]).round(1))
print("Range of the SI-bounded integral:", round(allt.int_dtheta_20.min(), 1), "to", round(allt.int_dtheta_20.max(), 1), "deg")
allg = pd.concat([TT[(g, "start")] for g in ("smooth", "complex_1a", "complex_2a")])
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/brudner-2026/reproduce_brudner_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='code' and 'within tolerance' in s and 'medians(tt)' in s:
        print(i)
        for o in c['outputs']:
            print(''.join(o.get('text','')) if 'text' in o else o.get('data',{}).get('text/plain'))
EOF
```

```
24
                                                       turns      n                                  measure  median, negative  median, positive  within tolerance
                        all turns, smooth + complex smoke-1a  80445                           heading change             -20.8              21.3             False
                        all turns, smooth + complex smoke-1a  80445                       integral of dtheta             -20.3              20.9             False
                        all turns, smooth + complex smoke-1a  80445        integral over the SI-bounded turn             -34.3              35.2              True
                        all turns, smooth + complex smoke-1a  80445        integral over the half-height run             -26.0              26.8             False
                        all turns, smooth + complex smoke-1a  80445 SI-bounded, first version's |dtheta| run             -34.3              35.2              True
                        all turns, smooth + complex smoke-2a  86450                           heading change             -21.2              21.8             False
                        all turns, smooth + complex smoke-2a  86450                       integral of dtheta             -20.8              21.3             False
                        all turns, smooth + complex smoke-2a  86450        integral over the SI-bounded turn             -35.0              35.9              True
                        all turns, smooth + complex smoke-2a  86450        integral over the half-height run             -26.5              27.2             False
                        all turns, smooth + complex smoke-2a  86450 SI-bounded, first version's |dtheta| run             -35.0              35.9              True
                            all turns, smooth + both complex 103095                           heading change             -21.4              22.0             False
                            all turns, sm
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "measured\|proposed" tools/entry.py | head -40; grep -n "figs5c" -A3 executed/brudner-2026/result.json | head -20; python - <<'EOF'
import json
nb=json.load(open('entries/brudner-2026/reproduce_brudner_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'claim:figs5c' in s or ('figs5c-turn-angles' in s and c['cell_type']=='code'):
        print(i); print(s[:1500])
EOF
```

```
367:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
```

**Agent calls Bash**

```bash
cd  sed -n 330,380p tools/entry.py; grep -rn "claim:" tools/entry.py | head; cat executed/brudner-2026/result.json | head -30; python - <<'EOF'
import json
nb=json.load(open('entries/brudner-2026/reproduce_brudner_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    print(i, c['cell_type'], c.get('metadata',{}), ''.join(c['source'])[:60].replace('\n',' '))
EOF
```

```
for d in attempt.get("datasets") or ([attempt["dataset"]] if attempt.get("dataset") else [])]
        for n, f in enumerate(attempt.get("findings") or [], 1):
            if f.get("kind") in ("other", "selection_undocumented") and not f.get("about"):
                report.error(where, f"finding {n} ({f.get('kind')}): say what it is about, `about: data` or `about: paper`")
            about = f.get("about") or ("paper" if f.get("kind") in ("methods_unavailable", "code_mismatch",
                                                                   "paper_inconsistency") else "data")
            if about == "data" and len(used) > 1 and not f.get("datasets"):
                report.error(where, f"finding {n}: the attempt used {len(used)} datasets; name the ones it is about "
                                    f"(`datasets:`, from {', '.join(used)})")
            for d in f.get("datasets") or []:
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
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/brudner-2026-01.yaml'
s=open(p).read()
start=s.index('- claim: figs5c-turn-angles\n  outcome: reproduced')
end=s.index('- claim: figs5fh-smoothing-agent')
new='''- claim: figs5c-turn-angles
  outcome: not_reproduced
  notebook: reproduce_brudner_2026.ipynb
  output: claim:figs5c-turn-angles
  measured:
  - -20.8
  - 21.3
  notes: All detected turns of both plumes pooled (smooth and smoke-1a, 80445 turns), the heading change
    from the event's start to its stop gives medians of -20.8 and +21.3 degrees, and the integral of rotational
    velocity over the event -20.3 and +20.9. Under every turn set the claims file names (all turns or the
    kept turns) and every complex file set, the two displacements give medians of -19.6 to -21.4 and +20.7
    to +22.0 degrees, outside tolerance of -34.2 +/- 3.42 and +33.8 +/- 3.38. Over the run at or above half
    the peak (Fig. S5A measures peak width at half height) they are -25.0 to -26.6 and +26.8 to +27.7,
    also outside tolerance. Only the integral over the turn bounded by the 20% crossings of its peak on
    both edges, a variant the claims file does not name, gives medians within tolerance (all turns -34.3
    and +35.2; with smoke-2a -35.0 and +35.9; with both complex sets -35.0 and +35.8; kept turns -32.7
    and +36.2). The events lie inside the half-height run (start a median of 1 frame after its rising crossing,
    stop 1 frame before its falling one; median length 7 frames against 10 for the half-height run and 16
    for the 20% run), start a median of 4 frames after the SI's onset, and 99.9% stop before the 20% crossing
    on the falling edge. By group, over the 20%-bounded turn, smooth -34.1 and +35.2, smoke-1a -35.1 and
    +35.1, smoke-2a -37.6 and +37.7. The first version's run of |dtheta| gives the same medians. Whether
    the dataset's events are the paper's turn bounds is asked of a reader.
  deviations:
  - 'Variant, not deciding the outcome: the turn bounded from the SI''s onset (20% of the peak on the rising
    edge; SI, Behavioral Analysis) to the 20% crossing on the falling edge of the rotation in the turn''s
    direction, the end the paper does not state. This bound was adopted after the event bounds failed.'
  - The complex files are smoke-1a, as assumed for fig5e-cue-betas; smoke-2a and both sets are shown and
    give the same outcome.
'''
s=s[:start]+new+s[end:]
open(p,'w').write(s)
EOF
grep -n "Variant, not" attempts/brudner-2026-01.yaml
```

```
332:  - 'Variant, not deciding the outcome: the turn bounded from the SI''s onset (20% of the peak on the rising
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/brudner-2026-01.yaml'
s=open(p).read()
old=s[s.index("  - 'Variant, not deciding"):s.index("  - The complex files are smoke-1a, as assumed for fig5e-cue-betas; smoke-2a and both sets are shown and\n    give the same outcome.\n- claim: figs5fh")]
new='''  - A variant, which does not decide the outcome, bounds the turn from the SI's onset (20% of the peak
    on the rising edge; SI, Behavioral Analysis) to the 20% crossing on the falling edge of the rotation
    in the turn's direction, the end the paper does not state. This bound was adopted after the event bounds
    failed.
'''
s=s.replace(old,new); open(p,'w').write(s)
EOF
sed -n 309,345p attempts/brudner-2026-01.yaml
```

```
- claim: figs5c-turn-angles
  outcome: not_reproduced
  notebook: reproduce_brudner_2026.ipynb
  output: claim:figs5c-turn-angles
  measured:
  - -20.8
  - 21.3
  notes: All detected turns of both plumes pooled (smooth and smoke-1a, 80445 turns), the heading change
    from the event's start to its stop gives medians of -20.8 and +21.3 degrees, and the integral of rotational
    velocity over the event -20.3 and +20.9. Under every turn set the claims file names (all turns or the
    kept turns) and every complex file set, the two displacements give medians of -19.6 to -21.4 and +20.7
    to +22.0 degrees, outside tolerance of -34.2 +/- 3.42 and +33.8 +/- 3.38. Over the run at or above half
    the peak (Fig. S5A measures peak width at half height) they are -25.0 to -26.6 and +26.8 to +27.7,
    also outside tolerance. Only the integral over the turn bounded by the 20% crossings of its peak on
    both edges, a variant the claims file does not name, gives medians within tolerance (all turns -34.3
    and +35.2; with smoke-2a -35.0 and +35.9; with both complex sets -35.0 and +35.8; kept turns -32.7
    and +36.2). The events lie inside the half-height run (start a median of 1 frame after its rising crossing,
    stop 1 frame before its falling one; median length 7 frames against 10 for the half-height run and 16
    for the 20% run), start a median of 4 frames after the SI's onset, and 99.9% stop before the 20% crossing
    on the falling edge. By group, over the 20%-bounded turn, smooth -34.1 and +35.2, smoke-1a -35.1 and
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 618,632p attempts/brudner-2026-01.yaml; grep -rn "Round 3" attempts/*.yaml | head -3
```

```
results:
  - claim: fig1eh-snapshot-organization
    agrees: true
    outcome: blocked
    reason: Agreed, listed among the other 13 blocked claims, with no reason given.
    response: No change.
  - claim: fig1il-zscore-reliability
    agrees: true
    outcome: blocked
    reason: Agreed, listed among the other 13 blocked claims, with no reason given.
    response: No change of outcome. The report notes, unchanged from round 1, that 'Dryad answers 401'
      was not backed by any output; the notebook's data check now requests the file without a token and
      prints the 401.
  - claim: figs1-antisymmetry-index
    agrees: true
attempts/bech-2026-01.yaml:1242:  reviewed: Round 3. Only the four changes of outcome proposed after round 2 (fig3h-rsc-first-context-discrimination and
attempts/bennett-2024-01.yaml:1262:  reviewed: Round 3. The two changes of outcome proposed after round 2 (fig7cd-mop-coupling and fig8d-response-latencies)
attempts/bruno-2017-01.yaml:965:  reviewed: Round 3. The proposed change of outcome of fig6d-decode-p10, the only one in the record, with
```

**Agent calls Bash**

```bash
cd  tail -c 1 attempts/brudner-2026-01.yaml | xxd | head -1; cat >> attempts/brudner-2026-01.yaml <<'EOF'
- date: '2026-11-12'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 3. The proposed change of outcome of figs5c-turn-angles, the only one in the record, with
    the analysis behind it in the notebook (cell 24), the helper module, the claims file and the attempt
    record; the verifier also read the paper under paper/.
  results:
  - claim: figs5c-turn-angles
    agrees: true
    outcome: not_reproduced
    reason: Cell 24 measures the claims file's two displacements over the dataset's turn events, the heading
      change from start to stop and the integral of dtheta over the event. Under both turn sets the claims
      file names (all turns pooled, or the kept turns), and with every complex file set, the medians are
      -19.6 to -21.4 and +20.7 to +22.0 degrees. The tolerances are -34.2 +/- 3.42 and +33.8 +/- 3.38,
      so every one is outside. No named reading passes. The only bounds that pass are the 20% crossings
      on both edges of the peak. That reading is not in the claims file, the SI states the 20% rule only
      for the rising edge (turn onset), and the record says it was adopted after the event bounds failed.
      So it cannot decide the outcome and is rightly kept as a variant. The report adds that the event
      positions now printed in cell 24 support the record's description, which it had said in round 2
      was not shown by any output, and that the claims file may misread the paper in taking the deposited
      event bounds as the turn's bounds, which the attempt has put to a reader.
    response: Changed to not_reproduced and removed `proposed`. The measured values are now the first reading
      the criterion lists (all turns pooled, heading change), -20.8 and +21.3, and the outcome no longer
      rests on an assumption, since it holds under every turn set and complex file set; the 20% bounds
      are recorded as a variant. The notebook's result and summary, the README and the notes now say so.
EOF
python -c "import yaml;yaml.safe_load(open('attempts/brudner-2026-01.yaml'))" && echo ok
```

Result: not kept, because it reads the paper's text.

**Agent**

Record updated. Now the notebook's result and summary cells and the README.

**Agent calls Bash**

```bash
cd entries/brudner-2026; python - <<'EOF'
import json
p='reproduce_brudner_2026.ipynb'
raw=open(p).read()
nb=json.loads(raw)
def setsrc(i, text):
    lines=text.split('\n')
    nb['cells'][i]['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
c25='''**Result: not reproduced.** Over the files' events, the two displacements the claims file names, the
medians are -20.8 and +21.3 degrees (heading change) and -20.3 and +20.9 (integral of dtheta) for all
turns of the smooth and smoke-1a files, and -19.6 to -21.4 and +20.7 to +22.0 for every turn set and
complex file set, outside -34.2 +/- 3.42 and +33.8 +/- 3.38. Integrated over the run at or above half
the peak (Fig. S5A) they are -25.0 to -26.6 and +26.8 to +27.7, also outside. Only the turn bounded by
the 20% crossings on both edges gives medians within tolerance: -34.3 and +35.2 degrees for all turns
of the smooth and smoke-1a files (-35.0 and +35.9 with smoke-2a, -35.0 and +35.8 with both), and -32.7
and +36.2 for the kept turns (-33.1 and +36.7 with smoke-2a). The medians are the same with the first
version's run of |dtheta|. The 20% end is not stated in the paper and was adopted after the event
bounds failed, so it is kept as a variant and does not decide the outcome. The files' events lie inside
the half-height run: they start a median of 1 frame after its rising crossing and stop 1 frame before
its falling one (median length 7 frames, against 10 for the half-height run and 16 for the 20% run),
and 99.9% stop before the 20% crossing on the falling edge (a median of 4 frames before). Whether the
dataset's events are the paper's turn bounds is asked of a reader.'''
setsrc(25,c25)
s46=''.join(nb['cells'][46]['source'])
old="| figs5c-turn-angles | reproduced, assumed (turn bounded by the 20% crossings); about -21 and +21 degrees over the files' events and about -26 and +27 over the half-height run, so a change to not reproduced is proposed |"
new="| figs5c-turn-angles | not reproduced: about -21 and +21 degrees over the files' events under every reading, and about -26 and +27 over the half-height run; within tolerance only over the turn bounded by the 20% crossings, a variant the paper does not state |"
assert old in s46
setsrc(46,s46.replace(old,new))
assert '—' not in json.dumps(nb,ensure_ascii=False)
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False)+'\n')
EOF
git diff --stat reproduce_brudner_2026.ipynb
```

```
entries/brudner-2026/reproduce_brudner_2026.ipynb | 30 +++++++++++------------
 1 file changed, 15 insertions(+), 15 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/brudner-2026; python - <<'EOF'
p='README.md'; s=open(p).read()
a="| Fig. S5C, turns of about -34 and +34 degrees | Reproduced, resting on an assumption; a change to not reproduced is proposed |"
b="| Fig. S5C, turns of about -34 and +34 degrees | Not reproduced |"
assert a in s; s=s.replace(a,b)
a2="""Fig. S5C is reproduced
only when the turn is bounded by the 20% crossings of its peak, a bound the paper does not state; over
the files' turn events, as the claims file reads it, the medians are about 21 degrees, so a change to
not reproduced is proposed for the next verification round."""
b2="""Fig. S5C is not
reproduced: over the files' turn events, as the claims file reads it, the medians are about 21 degrees.
They match the paper only when the turn is bounded by the 20% crossings of its peak, a bound the paper
does not state, and whether the files' events are the paper's turn bounds has been asked of a reader."""
assert a2 in s; s=s.replace(a2,b2); open(p,'w').write(s)
EOF
grep -rn "proposed" README.md entry.yaml; cd ../..; grep -n "proposed" attempts/brudner-2026-01.yaml | head
```

```
778:      falling 20% crossing, a median of 4 frames before. Kept the verified outcome and proposed not_reproduced,
789:  reviewed: Round 3. The proposed change of outcome of figs5c-turn-angles, the only one in the record, with
807:    response: Changed to not_reproduced and removed `proposed`. The measured values are now the first reading
```

**Agent**

Now the check, then the full run (about 18 minutes last time).

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py check entries/brudner-2026 2>&1 | tail -15
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/brudner-2026 > $TMPDIR/all.log 2>&1; echo exit $?; tail -25 $TMPDIR/all.log; date -u
```

```
Thu Nov 12 09:25:14 UTC 2026
0 error(s)
```

```
exit 0
Installed kernelspec registry-brudner-2026 in executed/brudner-2026/.venv/share/jupyter/kernels/registry-brudner-2026
0 error(s)
pass  reproduce_brudner_2026.ipynb  (929 s)
Thu Nov 12 09:40:57 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/brudner-2026/reproduce_brudner_2026.ipynb'))
t=''.join(''.join(o.get('text','')) for o in nb['cells'][24]['outputs'])
print([l for l in t.splitlines() if 'smoke-1a  80445' in l])
EOF
git status --short | grep -v tools/
```

```
['                        all turns, smooth + complex smoke-1a  80445                           heading change             -20.8              21.3             False', '                        all turns, smooth + complex smoke-1a  80445                       integral of dtheta             -20.3              20.9             False', '                        all turns, smooth + complex smoke-1a  80445        integral over the SI-bounded turn             -34.3              35.2              True', '                        all turns, smooth + complex smoke-1a  80445        integral over the half-height run             -26.0              26.8             False', "                        all turns, smooth + complex smoke-1a  80445 SI-bounded, first version's |dtheta| run             -34.3              35.2              True"]
 M attempts/brudner-2026-01.yaml
 M entries/brudner-2026/README.md
 M entries/brudner-2026/reproduce_brudner_2026.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? scripts
```

**Agent**

Round 3 reviewed only one claim, figs5c-turn-angles. The verifier agreed with the change I proposed, so I applied it.

**Outcome that changed**
- **figs5c-turn-angles** went from reproduced (resting on an assumption) to **not_reproduced**, and `proposed` is removed. The claims file names two ways to measure a turn over the dataset's turn events. Under both, the medians are about -21 and +21 degrees for every turn set and every complex file set, and the paper's values are -34.2 ± 3.42 and +33.8 ± 3.38, so none is within tolerance. Only bounding each turn at 20% of its peak on both edges matches the paper. The paper never states that end bound, and I adopted it after the other bounds had failed, so it is now recorded as a variant that does not decide the outcome.
- To match, I changed three other fields on this claim:
  - `measured` is now the first reading the criterion lists (all turns pooled, heading change): -20.8 and +21.3.
  - I dropped `assumed: true`, because the result holds under every turn set and complex file set.
  - The deviation now describes the 20% bound as a variant.
- No other outcome changed.

**Proposals that stand:** none. This was the record's only proposal.

**Other updates**
- **Notebook:** the result cell (25) and the summary row for this claim now say not reproduced.
- **README:** the table row and the paragraph say not reproduced, and mention that a reader has been asked whether the dataset's turn events are the paper's turn bounds.
- **Attempt record:** round 3 is under `verifications`, with the verifier's reason in its own words and my response.

`python tools/entry.py all entries/brudner-2026` ran with 0 errors and the notebook passed (929 s); cell 24 gives the same numbers as before. Nothing is committed.

## End of run

23 turns, 17 minutes, $0.65 at API prices, result: success.
