# nishimoto-2011-reconstructing · recorder · run 43664553492

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/nishimoto-2011-reconstructing/; python tools/readme_row.py nishimoto-2011-reconstructing; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 ashworth-2025-01 knierim-2000-02; do echo "=== $f"; cat $f.md; done; cd ../../summaries; for f in amjad-2025-01 andrews-2024-01 asari-2009-01; do echo "=== $f"; cat $f.md; done; cat README.md
```

```
<persisted-output>
Output too large (42.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4d782b73-206e-4891-924c-4bb59eb846a3/tool-results/bkq8jqkqr.txt

Preview (first 2KB):
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4d782b73-206e-4891-924c-4bb59eb846a3/tool-results/bkq8jqkqr.txt"
}
```

```
1	=== amjad-2025-01
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 561 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/nishimoto-2011-reconstructing-01.yaml; echo ======; cat claims/nishimoto-2011-reconstructing.yaml; echo =====; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for e in (items if isinstance(items,list) else items.values()):
  if 'vim-2' in json.dumps(e) or 'nishimoto' in json.dumps(e).lower(): print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (63.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4d782b73-206e-4891-924c-4bb59eb846a3/tool-results/bacz1sqdl.txt

Preview (first 2KB):
schema_version: 3
id: nishimoto-2011-reconstructing-01
datasets:
- archive: crcns
  id: vim-2
  version: unversioned
  doi: 10.6080/K00Z715X
  relation: primary
paper: doi:10.1016/j.cub.2011.08.031
date: 2026-11-14
entry: nishimoto-2011-reconstructing
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4d782b73-206e-4891-924c-4bb59eb846a3/tool-results/bacz1sqdl.txt"
}
```

```
1	schema_version: 3
2	id: nishimoto-2011-reconstructing-01
3	datasets:
4	- archive: crcns
5	  id: vim-2
6	  version: unversioned
7	  doi: 10.6080/K00Z715X
8	  relation: primary
9	paper: doi:10.1016/j.cub.2011.08.031
10	date: 2026-11-14
11	entry: nishimoto-2011-reconstructing
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 866 more lines not kept]
```

**Agent**

I've read the recent notes, the attempt record and the claims file. Next: the dataset entry, the counting script and the reports.

**Agent calls Bash**

```bash
cd  grep -n -B3 -A15 'vim-2' targets/dandisets.json | head -60; sed -n 1,200p tools/readme_row.py | grep -n -i -A3 'with_inputs\|(+' | head -40
```

```
6:elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
7-findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
8-left out, as the README says. A deprecated attempt's row has no counts.
9-"""
--
62:            m = sum(1 for o in mine if kinds.get(o["claim"]) == "with_inputs")
63:            cells.append(f"{n} (+{m})" if m else str(n))
64-    paper = record["id"].rsplit("-", 1)[0]
65-    surname, year = re.match(r"^(.+?)-(\d{4})(?:-|$)", paper).groups()
66-    surname = " ".join(w.capitalize() for w in surname.split("-"))
```

**Agent calls Bash**

```bash
cd  grep -n -i 'vim\|nishimoto\|crcns' targets/dandisets.json | head; ls targets
```

```
contributors.yaml
crcns.json
dandisets.json
description_papers.yaml
dryad.json
ebrains.json
figshare.json
openneuro.json
pilot.yaml
reuse.yaml
reuse_datasets.json
sparc.json
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/crcns.json'))
s=json.dumps(d)
items=d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list))
for e in items:
  if 'vim-2' in json.dumps(e): print(json.dumps(e,indent=1))
"; grep -n -i 'catalystneuro' targets/crcns.json | head -3
```

```
{
 "id": "vim-2",
 "name": "Gallant Lab Natural Movie 4T fMRI Data",
 "url": "http://crcns.org/data-sets/vc/vim-2",
 "doi": "10.6080/K00Z715X",
 "published_version": null,
 "asset_count": 17,
 "size_gb": 21.88,
 "data_standards": [
  "compressed archives"
 ],
 "species": [
  "Human"
 ],
 "approaches": [
  "functional magnetic resonance imaging"
 ],
 "papers": [
  {
   "doi": "10.1016/j.cub.2011.08.031",
[... 11 more lines not kept]
```

**Agent**

The dataset is not in `targets/dandisets.json`. It is in `targets/crcns.json`, where `catalystneuro` is empty, so the CatalystNeuro sentence does not apply. Now the reports.

**Agent calls Bash**

```bash
cd transcripts/nishimoto-2011-reconstructing; ls -la; for f in author-report.md author-answers-report.md answer-report.md; do echo "=== $f"; cat $f; done
```

```
total 676
drwxr-xr-x   2 runner runner   4096 Nov 15 01:45 .
drwxr-xr-x 286 runner runner  12288 Nov 15 01:45 ..
-rw-r--r--   1 runner runner    895 Nov 15 01:45 answer-report.md
-rw-r--r--   1 runner runner   5348 Nov 15 01:45 answer.md
-rw-r--r--   1 runner runner   1851 Nov 15 01:45 author-answers-report.md
-rw-r--r--   1 runner runner  15174 Nov 15 01:45 author-answers.md
-rw-r--r--   1 runner runner   5144 Nov 15 01:45 author-report.md
-rw-r--r--   1 runner runner   3961 Nov 15 01:45 author-revise-1-report.md
-rw-r--r--   1 runner runner 179684 Nov 15 01:45 author-revise-1.md
-rw-r--r--   1 runner runner   3209 Nov 15 01:45 author-revise-2-report.md
-rw-r--r--   1 runner runner 127821 Nov 15 01:45 author-revise-2.md
-rw-r--r--   1 runner runner   1635 Nov 15 01:45 author-revise-3-report.md
-rw-r--r--   1 runner runner  35255 Nov 15 01:45 author-revise-3.md
-rw-r--r--   1 runner runner 107146 Nov 15 01:45 author.md
-rw-r--r--   1 runner runner   3203 Nov 15 01:45 claims-check-report.md
-rw-r--r--   1 runner runner  16723 Nov 15 01:45 claims-check.md
-rw-r--r--   1 runner runner   3690 Nov 15 01:45 claims-report.md
-rw-r--r--   1 runner runner  36168 Nov 15 01:45 claims.md
-rw-r--r--   1 runner runner   7788 Nov 15 01:45 verifier-1-report.md
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/nishimoto-2011-reconstructing; for f in verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; done
```

```
=== verifier-1-report.md
**Verifier report, round 1: Nishimoto et al. 2011 on CRCNS vim-2**

The claims file has 10 claims. The notebook tests 4 and treats 6 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig2de-prediction-accuracy | reproduced | Cell 10, reading (a)(i) and (a)(ii): static 0.217, nondirectional 0.375, directional 0.379. All three are within tolerance, in the right order, and both Wilcoxon tests give p ≈ 0 (underflow). The margin is tiny: static 0.217 sits just above the 0.216 lower bound, and the fit is ridge, not the L1 regression the criterion names (problem 1). Reading (b) gives means of 0.12 to 0.21, all outside tolerance. |
| fig2e-directional-gain-small | reproduced | Cell 12: directional minus nondirectional is 0.0042, against a motion gain of 0.158. The ratio of 0.027 is below the claims file's bound of 0.1, and p ≈ 0. This holds under all four readings. |
| figs1a-motion-better-every-area | reproduced | Cell 14: both motion models beat the static model in 15 of 15 cells. V1 has the highest mean in every subject and every model. With V1 against the other four areas pooled (reading b), p ≤ 1e-11 in 3 of 3 subjects for every model. Against each area in turn (reading a), only the static model passes in all 3; the directional model passes in 1 of 3 (S3 V1 vs V3A, p = 0.03). |
| fig2fgh-retinotopic-receptive-fields | blocked (other: not run, though testable) | Cell 17 says "too_large (time)", but the whole run took 30.9 min and 11.7 GB (cell 18), and the probes are cheap. The archive holds everything the claims file's proxy test needs (problem 2). |
| fig2j-speed-eccentricity | blocked (other: not run, though testable) | Same as above. The grating probes need only the fitted weights and the filter bank. |
| fig3ab-identification-s1 | reproduced | Cell 16, model (a) with the repeat-averaged signal (i): 424 of 486 at the Tikhonov penalty 3.0, chosen on the held-out training data. That clears the threshold of 418. Chan
[... 206 more lines not kept]
```

**Agent**

I have everything I need. Writing the notes now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/nishimoto-2011-reconstructing-01.md",
 "content": "# nishimoto-2011-reconstructing, Nishimoto et al. 2011\n\nSix claims reproduced on the data set and none partially, not reproduced or\nblocked, plus four claims that also use outside data, of which\n`fig2fgh-retinotopic-receptive-fields` reproduced and three were blocked for\nmissing data. Eight of the reproduced outcomes rest on an assumption. The first\nverification round agreed with 7 of the 10 outcomes as they stood and the second\nwith all 10. The author then proposed `fig3ab-identification-s1` as reproduced,\nso a third round reviewed that one claim and agreed. CRCNS data sets carry no\nversion, so the record gives `unversioned` (doi 10.6080/K00Z715X), and the\nnotebook prints the MD5 sums of the files it reads. The paper, Nishimoto, Vu,\nNaselaris, Benjamini, Yu and Gallant in Current Biology (21, 1641-1646), records\nBOLD responses in early visual cortex of three subjects watching natural movies.\nIt fits voxel-wise motion-energy encoding models (static, nondirectional and\ndirectional), identifies which test second evoked a response and reconstructs\nthe movies from a sampled prior of about 18,000,000 s of YouTube clips. The\nclaims were written from the version of record and its supplement, without\nrendered figures, so every number comes from the text; the paper links no code.\nThe motion-energy bank is pymoten 0.1.3, recorded as an input, whose defaults\ngive the paper's 6,555 filters. Reproduced are the prediction accuracies of the\nthree models (0.233, 0.384 and 0.386 against 0.24, 0.39 and 0.40), the small\ndirectional gain (ratios of 0.012 to 0.022), the motion models' advantage in\nevery area with V1 best, the receptive fields (on the claims file's proxy test,\nwith no multifocal maps), the speed against eccentricity correlation in all nine\narea and subject cells, S1 identification (426 of 486 against 464, chance 2.96)\nand the absence of a gain from color (0.0095 below luminance). Blocked are the\n1,000,000-clip identification and both reconstruction claims. Every model is fit\nby ridge regression in place of the paper's L1, and fig2de and fig3ab pass only\nwith penalties chosen by five-fold cross-validation (reading b): with a single\nheld-out 10% the static mean is 0.211, 0.005 below its bound, and the count 408.\nThe author's first run gave 4 reproduced and 6 blocked, with fig2fgh, fig2j and\nthe color claim blocked as too large for the time. Round 1 found all three\ntestable from the data set, the fits ridge with the cross-validated reading not\nrun, and a bug in the nondirectional model, which summed zero-spatial-frequency\nfilters by position. In reply the three claims were run (the color claim in a\nsecond notebook, `color_no_gain.ipynb`), the bug was fixed (4,275 features),\nreading (b) was added and the S1 count fell to 409, partially reproduced. Round 2\nasked for an L1 comparison, identification under reading (b) and a color fit\nwith a separate weight per channel, and found sentences the outputs did not\nsupport (the figs1a exceptions, 750 held-out samples, the 424 to 409 change put\ndown to the split, about 46 minutes). In reply an approximate L1 fit on 120\nvoxels predicted better than ridge by 0.005 to 0.025, the banded color model was\nstill 0.0066 below luminance, and identification under reading (b) gave 426. The\nauthor asked a reader nothing, so the answer and author-answers runs changed\nnothing. In the author's run two commands hung and cost about 85 min (a\nrapidgzip test that ran into its 1 h timeout and a wait loop whose `pgrep -f`\nmatched its own shell), and a third run was cut off at 40 min by a slow\nthree-operand `einsum`; the final run took 1,547 s with peak memory 11.7 GB. The\nnotebooks ran in 43 and 46 min after round 1 (peak memory 6.9 GB), 37 and 42 min\nafter round 2 and 40 and 43 min at the end.\n\nThe sampled natural movie prior (about 18,000,000 s of YouTube clips), the\n1,000,000-clip identification set and the multifocal retinotopic mapping data\nare not in the data set and not public, so the reconstruction findings of\nFigure 4 and the large-set identification of Figure 3C cannot be tested, and the\nreceptive-field maps can be judged only on a proxy. The paper fits each voxel by\nL1-regularized least squares by coordinate descent but does not say how the\npenalty or the stopping point was chosen, and publishes no code; nor does it say\nwhether prediction and identification use the mean of the ten test repeats or\nsingle repeats, or how the Tikhonov penalty of the noise covariance was chosen.\nSingle repeats give static means of 0.118 to 0.128 and directional means of 0.207\nto 0.212. The data descriptor does not say that the responses include the first\n6 s of each 600 s training run and each 60 s test block, which the paper\ndiscards; the mean training response over those seconds is 0.42, 0.41 and 0.28\nin the three subjects, against 0.01 over the other samples. It does not give the\nunits of the test responses: rt is z-scored per run (s.d. 0.99), while rv and\nrva have s.d. 0.10 to 0.11 and 0.20 to 0.23. It does not say that 179, 46 and 29\nof the V1 to V3B voxels of S1, S2 and S3 have missing training or test values.\nIts phrase that peak BOLD responses were estimated could be read as responses\nalready aligned to the stimulus, but the hemodynamic delay is still in the data:\na single-delay directional model gives 0.06 to 0.09 at 0 s, 0.30 to 0.33 at 4 s\nand 0.13 to 0.15 at 8 s. The files hold 30, 30 and 44 ROI masks by hemisphere,\ndifferent between subjects (PPA empty on both sides in S1), which the descriptor\nnames only by example and does not say how they were defined, and one subject 3\nvoxel lies in two of the V1 to V3B masks. V1 to V3B hold 4,183, 4,668 and 4,410\nvoxels, against the paper's about 4,500. The files are tar.gz archives around\nHDF5 files that cannot be read at random, and each member was streamed once into\nmemory. Two questions are put to the paper's authors: how the L1 penalty was\nchosen and on which split, and whether identification used the repeat mean,\nwith which Tikhonov and encoding penalties.\n\nThe author's points on the protocol: `docs/archives.md` says CRCNS files are zips\nto open in place, while vim-2's are tar.gz around HDF5 files, which were streamed\nmember by member; it has no rule for a computation-heavy method replaced for time\n(L1 by ridge), which was recorded as a deviation, not a block; it does not say how\nto record a reading not run for time, which went in the deviations; and\n`entry.py check` requires the version string \"unversioned\" to appear in the\ncode, which is not documented for CRCNS, so a constant was added to the helper.\n"
}
```

```
File created successfully at: docs/pilot-notes/nishimoto-2011-reconstructing-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p='docs/pilot-notes/nishimoto-2011-reconstructing-01.md'
s=open(p).read()
a="missing data. Eight of the reproduced outcomes rest on an assumption. The first"
b="missing data. All seven reproduced outcomes rest on an assumption. The first"
assert a in s; s=s.replace(a,b)
a="""chosen and on which split, and whether identification used the repeat mean,
with which Tikhonov and encoding penalties."""
b="""chosen and on which split, and whether prediction and identification used the
repeat mean, with the Tikhonov penalty and the encoding penalties for
identification chosen as here."""
assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -c -e '—' -e 'rather' docs/pilot-notes/nishimoto-2011-reconstructing-01.md
```

```
0
```

**Agent calls Bash**

```bash
cd  && cat > summaries/nishimoto-2011-reconstructing-01.md <<'EOF'
The paper's encoding findings held up in this data, while its movie reconstructions could not be tested. Motion-energy models predicted visual cortex responses better than a static model, with a small gain from direction, V1 best predicted, retinotopic receptive fields and faster preferred speeds in the periphery. The model identified the test second behind 88% of one subject's responses, against the paper's 95%. Both results rest on ridge regression in place of the paper's L1 fit, whose penalty choice the paper does not give, and hold only with penalties chosen by cross-validation. Reconstruction and identification among a million clips need a library of internet movies that is not public.
EOF
wc -w summaries/nishimoto-2011-reconstructing-01.md; git status --short
```

```
109 summaries/nishimoto-2011-reconstructing-01.md
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
?? docs/pilot-notes/nishimoto-2011-reconstructing-01.md
?? scripts
?? summaries/nishimoto-2011-reconstructing-01.md
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/nishimoto-2011-reconstructing-01.md"
}
```

```
1	# nishimoto-2011-reconstructing, Nishimoto et al. 2011
2	
3	Six claims reproduced on the data set and none partially, not reproduced or
4	blocked, plus four claims that also use outside data, of which
5	`fig2fgh-retinotopic-receptive-fields` reproduced and three were blocked for
6	missing data. All seven reproduced outcomes rest on an assumption. The first
7	verification round agreed with 7 of the 10 outcomes as they stood and the second
8	with all 10. The author then proposed `fig3ab-identification-s1` as reproduced,
9	so a third round reviewed that one claim and agreed. CRCNS data sets carry no
10	version, so the record gives `unversioned` (doi 10.6080/K00Z715X), and the
11	notebook prints the MD5 sums of the files it reads. The paper, Nishimoto, Vu,
12	Naselaris, Benjamini, Yu and Gallant in Current Biology (21, 1641-1646), records
13	BOLD responses in early visual cortex of three subjects watching natural movies.
14	It fits voxel-wise motion-energy encoding models (static, nondirectional and
15	directional), identifies which test second evoked a response and reconstructs
16	the movies from a sampled prior of about 18,000,000 s of YouTube clips. The
17	claims were written from the version of record and its supplement, without
18	rendered figures, so every number comes from the text; the paper links no code.
19	The motion-energy bank is pymoten 0.1.3, recorded as an input, whose defaults
20	give the paper's 6,555 filters. Reproduced are the prediction accuracies of the
[... 70 more lines not kept]
```

**Agent**

I wrote both files and committed nothing. The dataset has no entry in `targets/dandisets.json`. I found it in `targets/crcns.json`, where its `catalystneuro` field is empty, so the notes leave out the CatalystNeuro sentence. Besides my two new files, `git status` shows untracked files in the repository root that I did not create (`.bashrc`, `.idea`, `scripts` and others); I left them alone.

`docs/pilot-notes/nishimoto-2011-reconstructing-01.md`:

# nishimoto-2011-reconstructing, Nishimoto et al. 2011

Six claims reproduced on the data set and none partially, not reproduced or blocked, plus four claims that also use outside data, of which `fig2fgh-retinotopic-receptive-fields` reproduced and three were blocked for missing data. All seven reproduced outcomes rest on an assumption. The first verification round agreed with 7 of the 10 outcomes as they stood and the second with all 10. The author then proposed `fig3ab-identification-s1` as reproduced, so a third round reviewed that one claim and agreed. CRCNS data sets carry no version, so the record gives `unversioned` (doi 10.6080/K00Z715X), and the notebook prints the MD5 sums of the files it reads. The paper, Nishimoto, Vu, Naselaris, Benjamini, Yu and Gallant in Current Biology (21, 1641-1646), records BOLD responses in early visual cortex of three subjects watching natural movies. It fits voxel-wise motion-energy encoding models (static, nondirectional and directional), identifies which test second evoked a response and reconstructs the movies from a sampled prior of about 18,000,000 s of YouTube clips. The claims were written from the version of record and its supplement, without rendered figures, so every number comes from the text; the paper links no code. The motion-energy bank is pymoten 0.1.3, recorded as an input, whose defaults give the paper's 6,555 filters. Reproduced are the prediction accuracies of the three models (0.233, 0.384 and 0.386 against 0.24, 0.39 and 0.40), the small directional gain (ratios of 0.012 to 0.022), the motion models' advantage in every area with V1 best, the receptive fields (on the claims file's proxy test, with no multifocal maps), the speed against eccentricity correlation in all nine area and subject cells, S1 identification (426 of 486 against 464, chance 2.96) and the absence of a gain from color (0.0095 below luminance). Blocked are the 1,000,000-clip identification and both reconstruction claims. Every model is fit by ridge regression in place of the paper's L1, and fig2de and fig3ab pass only with penalties chosen by five-fold cross-validation (reading b): with a single held-out 10% the static mean is 0.211, 0.005 below its bound, and the count 408. The author's first run gave 4 reproduced and 6 blocked, with fig2fgh, fig2j and the color claim blocked as too large for the time. Round 1 found all three testable from the data set, the fits ridge with the cross-validated reading not run, and a bug in the nondirectional model, which summed zero-spatial-frequency filters by position. In reply the three claims were run (the color claim in a second notebook, `color_no_gain.ipynb`), the bug was fixed (4,275 features), reading (b) was added and the S1 count fell to 409, partially reproduced. Round 2 asked for an L1 comparison, identification under reading (b) and a color fit with a separate weight per channel, and found sentences the outputs did not support (the figs1a exceptions, 750 held-out samples, the 424 to 409 change put down to the split, about 46 minutes). In reply an approximate L1 fit on 120 voxels predicted better than ridge by 0.005 to 0.025, the banded color model was still 0.0066 below luminance, and identification under reading (b) gave 426. The author asked a reader nothing, so the answer and author-answers runs changed nothing. In the author's run two commands hung and cost about 85 min (a rapidgzip test that ran into its 1 h timeout and a wait loop whose `pgrep -f` matched its own shell), and a third run was cut off at 40 min by a slow three-operand `einsum`; the final run took 1,547 s with peak memory 11.7 GB. The notebooks ran in 43 and 46 min after round 1 (peak memory 6.9 GB), 37 and 42 min after round 2 and 40 and 43 min at the end.

The sampled natural movie prior (about 18,000,000 s of YouTube clips), the 1,000,000-clip identification set and the multifocal retinotopic mapping data are not in the data set and not public, so the reconstruction findings of Figure 4 and the large-set identification of Figure 3C cannot be tested, and the receptive-field maps can be judged only on a proxy. The paper fits each voxel by L1-regularized least squares by coordinate descent but does not say how the penalty or the stopping point was chosen, and publishes no code; nor does it say whether prediction and identification use the mean of the ten test repeats or single repeats, or how the Tikhonov penalty of the noise covariance was chosen. Single repeats give static means of 0.118 to 0.128 and directional means of 0.207 to 0.212. The data descriptor does not say that the responses include the first 6 s of each 600 s training run and each 60 s test block, which the paper discards; the mean training response over those seconds is 0.42, 0.41 and 0.28 in the three subjects, against 0.01 over the other samples. It does not give the units of the test responses: rt is z-scored per run (s.d. 0.99), while rv and rva have s.d. 0.10 to 0.11 and 0.20 to 0.23. It does not say that 179, 46 and 29 of the V1 to V3B voxels of S1, S2 and S3 have missing training or test values. Its phrase that peak BOLD responses were estimated could be read as responses already aligned to the stimulus, but the hemodynamic delay is still in the data: a single-delay directional model gives 0.06 to 0.09 at 0 s, 0.30 to 0.33 at 4 s and 0.13 to 0.15 at 8 s. The files hold 30, 30 and 44 ROI masks by hemisphere, different between subjects (PPA empty on both sides in S1), which the descriptor names only by example and does not say how they were defined, and one subject 3 voxel lies in two of the V1 to V3B masks. V1 to V3B hold 4,183, 4,668 and 4,410 voxels, against the paper's about 4,500. The files are tar.gz archives around HDF5 files that cannot be read at random, and each member was streamed once into memory. Two questions are put to the paper's authors: how the L1 penalty was chosen and on which split, and whether prediction and identification used the repeat mean, with the Tikhonov penalty and the encoding penalties for identification chosen as here.

The author's points on the protocol: `docs/archives.md` says CRCNS files are zips to open in place, while vim-2's are tar.gz around HDF5 files, which were streamed member by member; it has no rule for a computation-heavy method replaced for time (L1 by ridge), which was recorded as a deviation, not a block; it does not say how to record a reading not run for time, which went in the deviations; and `entry.py check` requires the version string "unversioned" to appear in the code, which is not documented for CRCNS, so a constant was added to the helper.

`summaries/nishimoto-2011-reconstructing-01.md` (109 words):

The paper's encoding findings held up in this data, while its movie reconstructions could not be tested. Motion-energy models predicted visual cortex responses better than a static model, with a small gain from direction, V1 best predicted, retinotopic receptive fields and faster preferred speeds in the periphery. The model identified the test second behind 88% of one subject's responses, against the paper's 95%. Both results rest on ridge regression in place of the paper's L1 fit, whose penalty choice the paper does not give, and hold only with penalties chosen by cross-validation. Reconstruction and identification among a million clips need a library of internet movies that is not public.

## End of run

15 turns, 2 minutes, $1.00 at API prices, result: success.
