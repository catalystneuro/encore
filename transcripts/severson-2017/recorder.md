# 000226 · recorder · run 39015964980

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000226 --write; git diff; ls claims/000226 transcripts/000226; cat attempts/000226-severson-2017-01.yaml
```

```
<persisted-output>
Output too large (45KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e6326e76-e495-4e0a-b4fb-ab9156bc1fe9/tool-results/bdovbi1wg.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 6f8b3ab..2b30051 100644
--- a/README.md
+++ b/README.md
@@ -77,6 +77,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000114](https://dandiarchive.org/dandiset/000114) | [Carcea et al. 2021](https://doi.org/10.1038/s41586-021-03814-7) | 1 | 3 | 3 | 12 | [`000114-carcea-2021`](entries/000114-carcea-2021) |
 | [000213](https://dandiarchive.org/dandiset/000213) | [Tingley et al. 2018](https://doi.org/10.1016/j.neuron.2018.04.028) | 3 | 8 | 9 | 5 | [`000213-tingley-2018`](entries/000213-tingley-2018) |
 | [000218](https://dandiarchive.org/dandiset/000218) | [Tingley et al. 2019](https://doi.org/10.1016/j.neuron.2019.10.012) | 4 | 7 | 10 | 10 | [`000218-tingley-2019`](entries/000218-tingley-2019) |
+| [000226](https://dandiarchive.org/dandiset/000226) | [Severson et al. 2017](https://doi.org/10.1016/j.neuron.2017.03.045) | 12 (+2) | 2 (+1) | 0 | 11 | [`000226-severson-2017`](entries/000226-severson-2017) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000226:
10.1016-j.neuron.2017.03.045.yaml

transcripts/000226:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
git diff --stat; cat attempts/000226-severson-2017-01.yaml; head -60 README.md | tail -30; grep -n "^### " docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (46.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e6326e76-e495-4e0a-b4fb-ab9156bc1fe9/tool-results/bskxyruj1.txt

Preview (first 2KB):
 README.md | 1 +
 1 file changed, 1 insertion(+)
schema_version: 1
id: 000226-severson-2017-01
dandiset: "000226"
dandiset_version: 0.230607.1747
paper: doi:10.1016/j.neuron.2017.03.045
date: 2026-10-17
entry: 000226-severson-2017
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^### " docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md attempts/000226-severson-2017-01.yaml transcripts/000226/*report.md; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if str(x.get('dandiset',x.get('id','')))=='000226'];print(e)"
```

```
Exit code 1
1594:### 000067, Fujisawa et al. 2008
1670:### 000070, Churchland et al. 2012
1743:### 000121, Even-Chen et al. 2019
1817:### 000114, Carcea et al. 2021
1890:### 000213, Tingley et al. 2018
1975:### 000218, Tingley et al. 2019
  2057 docs/pilot-notes.md
   788 attempts/000226-severson-2017-01.yaml
    57 transcripts/000226/author-report.md
    21 transcripts/000226/author-revise-1-report.md
    24 transcripts/000226/author-revise-2-report.md
    59 transcripts/000226/verifier-1-report.md
    41 transcripts/000226/verifier-2-report.md
  3047 total
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if str(x.get('dandiset',x.get('id','')))=='000226'];print(e)
                                                                                                                                              ^^^^^
AttributeError: 'int' object has no attribute 'get'
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 1670
}
```

**Agent calls Grep**

```json
{
 "pattern": "\"000226\"",
 "path": "targets/dandisets.json",
 "output_mode": "content",
 "-A": 15
}
```

```
1559:   "dandiset": "000226",
1560-   "name": "Active Touch and Self-Motion Encoding by Merkel Cell-Associated Afferents",
1561-   "published_version": "0.230607.1747",
1562-   "asset_count": 60,
1563-   "size_gb": 13.75,
1564-   "data_standards": [
1565-    "Neurodata Without Borders (NWB)"
1566-   ],
1567-   "species": [
1568-    "Mus musculus - House mouse"
1569-   ],
1570-   "approaches": [
1571-    "electrophysiological approach",
1572-    "behavioral approach"
1573-   ],
1574-   "papers": [
```

```
1670	### 000070, Churchland et al. 2012
1671	
1672	Five claims reproduced, seven partially, four not reproduced and six blocked,
1673	all on the dandiset. Round 1 gave its own outcome for each claim without
1674	seeing the record and agreed with all 22; round 2 agreed again and nothing was
1675	proposed, so there was no third round. The paper reports that the population
1676	activity of premotor (PMd) and motor (M1) cortex in monkeys making reaches in
1677	a maze task rotates in the plane found by jPCA, and that a rotational dynamics
1678	matrix (M_skew) fits it nearly as well as an unconstrained one, while
1679	simulated kinematic populations and muscle activity show no consistent
1680	rotations. The direction of rotation across conditions and reach curvature,
1681	the prediction of the phase from the preparatory state, the variance captured
1682	by the jPCA planes and by PC2 and PC3, the angle between the state and its
1683	derivative, the fit of M_skew, the rotation frequency, the shuffle controls,
1684	the two arrays analysed separately and the two kinematic models were tested on
1685	the J-array and N-array datasets, with the 192 per-electrode units each file
1686	holds in place of the paper's sorted isolations. The six claims on the leech
1687	and walking-monkey data, the single-electrode datasets, the EMG, the generator
1688	model and the speed task are blocked as `data_missing`. Some outcomes rest on
1689	weak ground: in `fig3ef-same-direction` jPCA orients the plane so that the net
[... 369 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "targets/dandisets.json",
 "offset": 1574,
 "limit": 25
}
```

```
1574	   "papers": [
1575	    {
1576	     "doi": "10.1016/j.neuron.2017.03.045",
1577	     "title": "Active Touch and Self-Motion Encoding by Merkel Cell-Associated Afferents",
1578	     "relation": "IsDescribedBy",
1579	     "resource_type": null,
1580	     "preprint": false
1581	    }
1582	   ],
1583	   "catalystneuro": [
1584	    "contributor Dichter, Benjamin of CatalystNeuro",
1585	    "contributor Tauffer, Luiz of CatalystNeuro"
1586	   ]
1587	  },
1588	  {
1589	   "dandiset": "000230",
1590	   "name": "Jacobsen 2022",
1591	   "published_version": "0.220506.1516",
1592	   "asset_count": 9,
1593	   "size_gb": 0.24,
[... 5 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/000226/author-report.md"
}
```

```
1	I've finished protocol steps 1 to 6 for dandiset 000226, using the full text. The entry passed `check` and ran from a clean environment in 12.7 minutes, and the verifier's handover package is built in `executed/000226-severson-2017/handover/`. Nothing is committed.
2	
3	**Paper and version.** The version of record is not open access. I used the accepted author manuscript from PubMed Central (PMC5528144) and the publisher's supplement `mmc1.pdf`, which holds Table S1. The supplement could only be fetched from the Elsevier CDN; PMC and Europe PMC returned a challenge page. I pinned 0.230607.1747: the paper cites no version, this is the only published one, and the draft has the same 60 assets and size.
4	
5	### 1. Outcome per claim
6	| Claim | Data | Outcome |
7	|---|---|---|
8	| table-s1-link | with_labels | reproduced (60 of 60 files match and agree) |
9	| video-frames | with_labels | reproduced (54,660,000 and 65,710,000 frames) |
10	| merkel-minutes | with_inputs | reproduced (823.8, 998.2 and 846.4 min) |
11	| fig2c-baseline-rate | with_labels | reproduced (0.03 Hz) |
12	| fig2c-touch-rate | with_labels | reproduced (47.9 Hz, all 33 touch-sensitive) |
13	| fig2c-wt-star | with_labels | reproduced under reading (b) (13 afferents, 19.0 Hz) |
14	| fig3a-direction-selective | with_inputs | partially reproduced (17 of 26 selective, criterion 80%) |
15	| fig3d-gam-full | with_labels | reproduced (r = 0.708) |
16	| fig3d-gam-single | with_labels | reproduced (0.441 and 0.415) |
17	| fig3d-gam-best-pair | with_labels | partially reproduced (0.622, ranked 2nd of 45 pairs) |
18	| fig4c-viscoelastic | with_inputs | reproduced (0.657 against 0.686) |
19	| fig5-phase-modulation | with_labels | reproduced (2.43 and 51.1 Hz) |
20	| fig5e-phase-span | with_labels | partially reproduced (all four quarter cycles, but Rayleigh p = 0.047) |
[... 38 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/000226/verifier-1-report.md"
}
```

```
1	**A. Outcomes (28 claims in the claims file: 14 reproduced, 3 partially reproduced, 11 blocked)**
2	
3	| Claim | Outcome | Reason |
4	|---|---|---|
5	| table-s1-link | reproduced | Cell 18: all 60 files match a distinct Table S1 recording (2 matched by number and mouse), and 60 of 60 agree on mouse, sex, line and date. |
6	| video-frames | reproduced | Cell 21: 54,660,000 frames against 54,647,500. Reading (a) gives 65,710,000 against 65,257,500 (ratio 1.007). |
7	| merkel-minutes | reproduced | Cell 23: 823.8, 998.2 and 846.4 min (reading a), against 823, 999 and 846. |
8	| fig2c-baseline-rate | reproduced | Cell 25: median 0.03 Hz with IQR 0.20, against 0.0 ± 0.2. |
9	| fig2c-touch-rate | reproduced | Cell 25: median 47.9 Hz with IQR 94.8, against 48.0. All 33 afferents are touch-sensitive with bootstrap CIs, and also with Poisson CIs. |
10	| fig2c-wt-star | reproduced | Cell 26, reading (b): 13 WT*, median 19.0 Hz (IQR 57.4), classes agree with Table S1 for 31 of 33, and the WT* set is the same as Table S1's. Reading (a) gives 15 WT*, which fails the count tolerance. |
11	| fig3a-direction-selective | partially_reproduced | Cell 28: 17 of 26 Merkel/SA afferents (65%) have an index of 0.5 or more. That is at least half but below the 80% needed for reproduced. |
12	| fig3d-gam-full | reproduced | Cell 30: mean r 0.708 (SD 0.141), against 0.71 ± 0.16. |
13	| fig3d-gam-single | reproduced | Cell 31: M0 0.441 and M0' 0.415, against 0.45 and 0.42. |
14	| fig3d-gam-best-pair | partially_reproduced | Cell 31: M0+M0' has r 0.622 and ranks 2nd of 45 behind M0+omega (0.633). Both values are within tolerance and it is above M0,Fax,Flat (0.475). |
15	| fig4c-viscoelastic | reproduced | Cell 34: mean r 0.657 for the viscoelastic model against 0.686 for the M0,M0' model over 25 afferents, a difference of -0.029. The threshold is -0.1. |
16	| fig5-phase-modulation | reproduced | Cell 36: medians 2.43 and 51.1 Hz, within the claim's tolerances of 3.4 and 105.7. All 15 afferents
[... 44 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/000226/author-revise-1-report.md"
}
```

```
1	Round 1 is handled. The verifier agreed with all 28 outcomes and none changed: 14 reproduced, 3 partially reproduced, 11 blocked. I re-ran `python tools/entry.py all entries/000226-severson-2017` after the last analysis change and it passed in 21 minutes. I then checked every conclusion and the summary against the new numbers. `entry.py check` also passes after the attempt-record and header edits.
2	
3	**What I added or corrected, by verifier point:**
4	- **B1 (tolerance check):** the fig5 cell, and the fig2c rate cell, now check against the claim's tolerance (the paper's IQR), and both checks pass. The 10% check is still printed but labelled "not the criterion".
5	- **B2 (fig5e, Rayleigh p = 0.047):** I added other ways of estimating each afferent's preferred phase. Using the circular mean of the tuning curve gives p = 0.062, which would be "reproduced". Taking the highest of 20 bins gives p = 0.023, and of 60 bins p = 0.046. The criterion fixes the highest of 30 bins, so the outcome stays partially reproduced. The notes say it sits on the threshold and depends on the estimator.
6	- **B3 (fig3d best pair):** I fitted all 45 pairs again with lambda 100, and again on held-out frames (fit on one half, scored on the other). M0 and M0' still rank second behind M0 and velocity in both: 0.589 against 0.600, and 0.620 against 0.630. The outcome stays partially reproduced.
7	- **B4 (phase convention):** position by phase is no longer all NaN, and it peaks next to phase 0 in all 60 files. I added a cosine correlation (median 0.9999, against sine -0.9999), which shows the stored phase is the negative of the Hilbert phase, not shifted by pi. I reworded the finding.
8	- **B5 (viscoelastic bounds):** `fit_visco` now reports which parameters end at a bound, on the scale it fits. 7 of 25 fits do (eps_lim in 6, E in 1, eta in 2). The text now says the parameter values are not interpreted.
9	- **B8 (cut-whisker files):** 199B and 209A hold distance-to-pole series and some contact 
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/000226/verifier-2-report.md"
}
```

```
1	**1. Outcomes**
2	
3	The claims file has 28 claims. The attempt record gives 28 outcomes: 14 reproduced, 3 partially reproduced and 11 blocked. I agree with all 28.
4	
5	- **fig7d-cut-emg:** In round 1 I gave the block as metadata_insufficient. The record keeps data_missing and gives the missing cut condition in its notes. Both blockers apply, so I accept this.
6	- **fig5e-phase-span:** I agree with partially reproduced. The criterion fixes the estimator (highest of 30 bins), which gives p = 0.047 (cell 50). The record discloses that the circular-mean variant gives p = 0.062.
7	- **fig3d-gam-best-pair:** I agree with partially reproduced. M0+M0' ranks 2nd in all three variants (cell 40).
8	
9	**2. Sentence check against printed outputs**
10	
11	Every "**Result:" cell (19, 23, 26, 29, 30, 32, 35, 41–43, 46, 49, 51, 53, 56, 59, 62, 65, 68, 71) matches the printed numbers. So do the README and nearly all the record notes and findings. The exceptions:
12	
13	- **Record, verifications, fig3d-gam-full response:** "The held-out variant … gives pair values within 0.003 of the in-sample ones." Cell 40 prints only the top five pairs for each variant. The statement is supported for those five (differences 0.002–0.003) and not shown for the other 40 pairs. The held-out r of the full model was not computed.
14	- **Record, fig5e-phase-span notes:** "At the preferred phase the whisker is retracting for 11 of 15, which fits the paper's remark of a slight abundance in retraction." Cell 50 gives 11 of 15 (73%), which is not "slight". The record's own finding says the stored phase is negated. If the paper's Figure 7G used the stored phase under the usual convention, these 11 would be labelled protraction. "Fits" is not established. This does not affect an outcome.
15	- **Record, fig5e notes:** "with the highest of 20 or 60 bins p = 0.023 and 0.046". In cell 50 these two variants also use a different frame set (the outlier-free frames kept for figs6). The note does not say so.
16	- *
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/000226/author-revise-2-report.md"
}
```

```
1	No outcome changed: all 28 stay as verified (14 reproduced, 3 partially reproduced, 11 blocked), and nothing is proposed. The entry ran three times with `tools/entry.py all`. All passed, and the last two runs gave identical numbers.
2	
3	**Added to the notebook:**
4	- **Table S1 check (the open point).** A new cell downloads the supplement from the publisher, parses Table S1 and compares it with the transcription in `merkel.py`. All 60 rows parse and agree on every column, including the experiment group. A test copy with two values changed is caught. `pypdf` is now in the requirements and the lock file is updated. The record's `inputs` now says where the check is shown.
5	- **Mi and dMi in the EMG files.** A new cell compares their curves across the whisk cycle with positive and negative velocity. In 7A, 8A and 9A, the correlation with positive velocity is −0.026 to 0.002 for Mi and −0.570 to −0.534 for dMi. That is close to the medians in every group of afferent files, so neither series is the intrinsic protractor EMG. The units are N·m and N·m/s.
6	- **Viscoelastic fit stability.** This run gave slightly different fig4c numbers from round 2, with the same code, data and locked packages:
7	  - mean r 0.656 against 0.657;
8	  - difference −0.030 against −0.029;
9	  - confidence interval −0.061 to −0.006;
10	  - 10 of 25 higher against 9;
11	  - 6 fits at a bound against 7.
12	
13	  I did not find the cause. A new cell refits with three other sets of random starts. The mean difference is −0.037, −0.040 and −0.017, all inside the criterion's 0.1, but single recordings can change by up to 0.555 in r. The notes and conclusion now give the new numbers and say this.
14	
15	**Corrected text:**
16	- **fig5e-phase-span notes.** Removed the claim that 11 of 15 "fits" the paper's slight excess of retraction. They now say that agreement with Figure 7G is not established, and that the 20- and 60-bin variants use the outlier-free frames.
17	- **EMG files.** "Whisker video serie
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^Counts are of claims/,/^$/p' README.md; grep -n "more that also\|also use\|outside data\|with_inputs" docs/pilot-notes.md | head -20
```

```
Counts are of claims that rest on the dandiset, including those that take
names for its own codes from elsewhere. Claims that also use data from
outside the dandiset are counted apart, in brackets. Claims on data the
paper deposited in other archives are not in this table; the dashboard
shows them on each dandiset's page.

581:dandiset with outside data cannot say which of them failed. So:
584:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
587:- When outside data must be matched to the dandiset's cells, sessions or
596:RDMs that are not public, are now marked `with_inputs`, and its attempt
602:nine blocked. With outside data, counted apart: two reproduced, one
640:3. Whether a link claim is needed when outside data is matched by label,
658:outside data, counted apart: five reproduced, one partially and two not
668:### Stimulus names as outside data
674:tested claims are `with_inputs`, and the dandiset is judged on two. A link
701:1. A table of stimulus names is a label; counting it as outside data leaves
940:on the dandiset, plus one claim using outside data, not reproduced; both
983:dandiset's claims and from `with_inputs` claims. It is never blocked with
```

**Agent calls Bash**

```bash
sed -n 598,606p docs/pilot-notes.md; sed -n 655,662p docs/pilot-notes.md; sed -n 936,944p docs/pilot-notes.md
```

```
## 000035, Scala et al. 2021 (2026-10-14): first attempt under pilot-5

Outcome, on the dandiset alone: three claims reproduced, one partially and
nine blocked. With outside data, counted apart: two reproduced, one
partially and one blocked. No outcome changed through either round. See
[`attempts/000035-scala-2021-01.yaml`](../attempts/000035-scala-2021-01.yaml)
and [`transcripts/000035/`](../transcripts/000035).

## 001453, Fouke et al. 2025 (2026-10-14): the last pilot target

Outcome, on the dandiset alone: two claims reproduced and ten blocked. With
outside data, counted apart: five reproduced, one partially and two not
reproduced. No outcome changed through either round. See
[`attempts/001453-fouke-2025-01.yaml`](../attempts/001453-fouke-2025-01.yaml)
and [`transcripts/001453/`](../transcripts/001453).


### 001933, Chen et al. 2026

Six claims reproduced, two partially, one not reproduced and eight blocked
[... 5 more lines not kept]
```

**Agent**

Now the findings section of the attempt record.

**Agent calls Bash**

```bash
grep -n "^[a-z_]*:" attempts/000226-severson-2017-01.yaml; grep -n "^- kind\|^  kind\|severity" attempts/000226-severson-2017-01.yaml | head -40
```

```
1:schema_version: 1
2:id: 000226-severson-2017-01
3:dandiset: "000226"
4:dandiset_version: 0.230607.1747
5:paper: doi:10.1016/j.neuron.2017.03.045
6:date: 2026-10-17
7:entry: 000226-severson-2017
8:provenance:
16:inputs:
27:outcomes:
324:findings:
382:verifications:
9:  kind: agent
325:- kind: metadata_insufficient
330:- kind: selection_undocumented
333:- kind: metadata_error
339:- kind: data_missing
344:- kind: metadata_error
348:- kind: metadata_insufficient
354:- kind: metadata_insufficient
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000226-severson-2017-01.yaml",
 "offset": 27,
 "limit": 400
}
```

```
27	outcomes:
28	- claim: table-s1-link
29	  outcome: reproduced
30	  notebook: reproduce_severson_2017.ipynb
31	  output: claim:table-s1-link
32	  notes: All 60 files match a distinct Table S1 recording, 58 by recording id (the NWB identifier
33	    without "KS" and leading zeros) and 2 (KS0125_ and KS0128_, matched to 125B and 128D) by
34	    number and mouse. All 60 agree on mouse, sex, mouse line and date. Groups - 33 touch, 13
35	    progressive cutting, 5 cut-whisker, 4 EMG, 3 excluded touch, 2 whisking-only. No Table S1
36	    recording lacks a file. The transcription of Table S1 agrees with the table parsed from the
37	    supplement on all 60 rows and every column used.
38	  deviations:
39	  - The criterion's rule of removing "KS0" was applied as removing "KS" and leading zeros, so that
40	    the EMG files KS0007A to KS0011A match 7A to 11A.
41	- claim: video-frames
42	  outcome: reproduced
43	  notebook: reproduce_severson_2017.ipynb
44	  output: claim:video-frames
45	  measured:
46	  - 54660000
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^- id:\|^  statement:\|^paper\|^title\|summary" claims/000226/*.yaml | head -80
```

```
50:paper: doi:10.1016/j.neuron.2017.03.045
52:- id: table-s1-link
53:  statement: The dandiset's recordings can be matched one to one to the recordings of Table S1,
63:- id: video-frames
64:  statement: The initial dataset of 33 touch afferents comprises 54,647,500 video frames with
83:- id: merkel-minutes
84:  statement: Identified Merkel afferents account for 823 minutes of the initial dataset and 846
105:- id: fig2c-baseline-rate
106:  statement: During non-whisking periods most afferents spiked at low rates (0.0 plus or minus
117:- id: fig2c-touch-rate
118:  statement: All afferents responded with increased spike rates during whisker-pole contact
133:- id: fig2c-wt-star
134:  statement: A subset of 13 of the 33 touch afferents (WT*) spiked especially strongly during
156:- id: fig3a-direction-selective
157:  statement: Merkel and SA afferents responded to contact in a dramatically direction-selective
171:- id: fig3d-gam-full
172:  statement: A full statistical model of ten mechanical and kinematic variables strongly
183:- id: fig3d-gam-single
184:  statement: Models fitted to moment or its rate of change alone explained spiking relatively
197:- id: fig3d-gam-best-pair
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 596,606p attempts/000226-severson-2017-01.yaml; sed -n 1,49p claims/000226/*.yaml | head -50
```

```
response: The archive check cell shows no series or path for manual labels. Outcome kept.
- date: '2026-10-17'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full executed notebook after the round-1 revision, the helper module, the claims
    file and the attempt record, with the paper (PMC5528144). The verifier checked every conclusion cell,
    the README and the record against the printed outputs and reviewed the round-1 responses. It agreed
    with all 28 outcomes, found seven statements not fully supported by the outputs, and said the Table S1
    transcription had still not been checked by a verifier. The cell numbers in its reasons refer to the
    round-2 notebook; this revision adds code cells
    at positions 19, 47 and 64, so later cells move.
# Claims for Severson, Xu, Van de Loo, Bai, Ginty and O'Connor (2017) on dandiset 000226.
# Source: the accepted author manuscript in PubMed Central (PMC5528144), full text, read from
# its Results, STAR Methods, Glossary and figure legends, and the publisher's Supplemental
# Information (mmc1.pdf), whose Table S1 lists every recording with its type and analyses.
# The version of record is not open access. The paper's analysis code is not public (the
# Methods say it is available on request); no repository for this paper was found.
#
# When these criteria were written, the author had seen the data check only: the file list,
# the metadata and trial tables of every file, the units and ranges of every series, the
[... 40 more lines not kept]
```

**Agent**

I have everything I need. Writing the subsection now.

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 000226, Severson et al. 2017

Twelve claims reproduced, two partially and eleven blocked on the dandiset.
With outside data, counted apart: two reproduced and one partially. Round 1
gave its own outcome for each claim from the notebook with its conclusions
removed and agreed with all 28; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports how
Merkel cell-associated afferents and other slowly (SA) and rapidly (RA)
adapting afferents of the mouse whisker follicle respond to active touch and
to whisking: touch responses explained by the bending moment (M0) and its
rate of change in statistical and viscoelastic models, direction selectivity,
a subset (WT*) tuned to whisk phase with preferred phases spanning the cycle,
responses that remain or vanish after progressive whisker cutting, and
comparisons with whisking EMG. The link to Table S1, frame counts, Merkel
minutes, baseline, touch and WT* rates, direction selectivity, the spline
models in place of the paper's GAMs, the viscoelastic fit, phase modulation
and its span and invariance, the kinematic models, nasolabialis motor units
and curvature noise were tested, with experiment groups taken from Table S1
as labels and afferent type and Merkel identity from it as outside data. The
claims on the progressive cutting experiment are blocked as
`metadata_insufficient`, and those needing the intrinsic protractor EMG, the
remaining whisker length, the optogenetic tagging, the histology and the
manually curated contact frames as `data_missing`. Some outcomes rest on weak
ground: `fig5e-phase-span` turns on a Rayleigh p of 0.047, which is 0.062
with the circular mean of the tuning curve; in `fig3d-gam-best-pair` M0 and
M0' ranks second of 45 pairs, at 0.622 against 0.633 for M0 and velocity,
also with lambda 100 and on held-out frames; `figs6-kinematic-gam` uses 15 of
the paper's 28 afferents; `fig5-phase-modulation` and `sigma-kappa` pass on
the paper's spreads while the non-preferred rate is 16% and curvature noise
28% above the paper's values; and `fig3a-direction-selective` reaches 65%
against the criterion's 80%. The author used the accepted manuscript in
PubMed Central (PMC5528144) and took the supplement holding Table S1 from the
publisher's file server, as PubMed Central and Europe PMC returned a
challenge page.

The dandiset was converted by CatalystNeuro (Benjamin Dichter and Luiz
Tauffer of CatalystNeuro are contributors). Its 60 files match Table S1 one
to one, but they do not say which experiment each recording belongs to, the
afferent type, which afferents were identified as Merkel afferents or the
whisking and touch class, and the three recordings the paper excludes (227C,
214A, 271A) are held without saying so. In the 13 progressive cutting
recordings every trial has cuttingGroup "intact" and MOI has one value per
file, although the whisking-in-air rate falls over most sessions (last fifth
below half the first in 10 of 13), so the cut conditions appear to be in the
files under the wrong label and Figure 6 and parts of Figure 7 are blocked.
The EMG files 7A, 8A and 9A hold tracked whisker series but no EMG signal,
11A holds nasolabialis spike times but not the EMG, and the optogenetic
tagging data, the histology, the whisker geometry and the curated contact
frames are not deposited. Velocity, acceleration, jerk, dM0, dFaxial and
dFlateral are stated per second but are per millisecond (median ratios 0.467
to 0.502), and the stored whisk phase is the negative of the Hilbert phase,
so phases from -pi to 0 are retraction, which neither the files nor the
paper describe. Other findings: every series has the description "no
description", distanceToPoleCenter has unit "unknown" and fits the Methods'
distance from whisker to pole in mm, and Mi, dMi and other series are not
explained; trial stop_time is 6.998 s after start_time while each trial holds
5 s of frames; the spike times of KS0277A are not sorted; KS0125_ and KS0128_
lack the unit letter of 125B and 128D, and all session start times are
12:00; some series hold extreme values, such as whisker position from -985 to
596 degrees, that are not flagged; the cut-whisker recordings 199B and 209A
hold distance-to-pole series and contact frames (5,014 and 32) that the files
do not explain; and the paper's analysis code is available only on request.
No recording is deposited twice.

Streaming the files by range requests took 22 minutes for the metadata
alone, so the notebook reads each file whole into memory. The first two runs
gave wrong model results from a diverging spline fitter and a badly
conditioned viscoelastic fit, both fixed without changing a criterion, and
in the last revision the viscoelastic results moved slightly from round 2
(difference -0.030 against -0.029) with the same code, data and locked
packages, for a cause not found; refits from three other sets of random
starts keep the outcome. The round 1 verifier could not download the
supplement and round 2 found the Table S1 check unshown, so the notebook now
fetches and parses Table S1 on every run, which needs access to the
publisher's file server. The author's points on the protocol: no case for a
table from the paper itself as input; the paper's stated spread as tolerance,
which makes median and IQR claims nearly untestable; streaming that is slow
for files of many small datasets; a step that assumes public code exists; no
rule for fixing bugs in the attempt's own code after seeing outputs; whether
to block or test a subset when a model can be fitted on 15 of 28 afferents;
and small ambiguities in the link rule for the EMG ids and in a blocked claim
with two reasons.
EOF
git diff --stat
```

```
README.md           |  1 +
 docs/pilot-notes.md | 83 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 84 insertions(+)
```

**Agent**

I ran `python tools/readme_row.py 000226 --write`, which added this row to README.md: 12 (+2) reproduced, 2 (+1) partially reproduced, 0 not reproduced, 11 blocked. I then added the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed, and the attempt, its claims and its entry are unchanged.

### 000226, Severson et al. 2017

Twelve claims reproduced, two partially and eleven blocked on the dandiset.
With outside data, counted apart: two reproduced and one partially. Round 1
gave its own outcome for each claim from the notebook with its conclusions
removed and agreed with all 28; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports how
Merkel cell-associated afferents and other slowly (SA) and rapidly (RA)
adapting afferents of the mouse whisker follicle respond to active touch and
to whisking: touch responses explained by the bending moment (M0) and its
rate of change in statistical and viscoelastic models, direction selectivity,
a subset (WT*) tuned to whisk phase with preferred phases spanning the cycle,
responses that remain or vanish after progressive whisker cutting, and
comparisons with whisking EMG. The link to Table S1, frame counts, Merkel
minutes, baseline, touch and WT* rates, direction selectivity, the spline
models in place of the paper's GAMs, the viscoelastic fit, phase modulation
and its span and invariance, the kinematic models, nasolabialis motor units
and curvature noise were tested, with experiment groups taken from Table S1
as labels and afferent type and Merkel identity from it as outside data. The
claims on the progressive cutting experiment are blocked as
`metadata_insufficient`, and those needing the intrinsic protractor EMG, the
remaining whisker length, the optogenetic tagging, the histology and the
manually curated contact frames as `data_missing`. Some outcomes rest on weak
ground: `fig5e-phase-span` turns on a Rayleigh p of 0.047, which is 0.062
with the circular mean of the tuning curve; in `fig3d-gam-best-pair` M0 and
M0' ranks second of 45 pairs, at 0.622 against 0.633 for M0 and velocity,
also with lambda 100 and on held-out frames; `figs6-kinematic-gam` uses 15 of
the paper's 28 afferents; `fig5-phase-modulation` and `sigma-kappa` pass on
the paper's spreads while the non-preferred rate is 16% and curvature noise
28% above the paper's values; and `fig3a-direction-selective` reaches 65%
against the criterion's 80%. The author used the accepted manuscript in
PubMed Central (PMC5528144) and took the supplement holding Table S1 from the
publisher's file server, as PubMed Central and Europe PMC returned a
challenge page.

The dandiset was converted by CatalystNeuro (Benjamin Dichter and Luiz
Tauffer of CatalystNeuro are contributors). Its 60 files match Table S1 one
to one, but they do not say which experiment each recording belongs to, the
afferent type, which afferents were identified as Merkel afferents or the
whisking and touch class, and the three recordings the paper excludes (227C,
214A, 271A) are held without saying so. In the 13 progressive cutting
recordings every trial has cuttingGroup "intact" and MOI has one value per
file, although the whisking-in-air rate falls over most sessions (last fifth
below half the first in 10 of 13), so the cut conditions appear to be in the
files under the wrong label and Figure 6 and parts of Figure 7 are blocked.
The EMG files 7A, 8A and 9A hold tracked whisker series but no EMG signal,
11A holds nasolabialis spike times but not the EMG, and the optogenetic
tagging data, the histology, the whisker geometry and the curated contact
frames are not deposited. Velocity, acceleration, jerk, dM0, dFaxial and
dFlateral are stated per second but are per millisecond (median ratios 0.467
to 0.502), and the stored whisk phase is the negative of the Hilbert phase,
so phases from -pi to 0 are retraction, which neither the files nor the
paper describe. Other findings: every series has the description "no
description", distanceToPoleCenter has unit "unknown" and fits the Methods'
distance from whisker to pole in mm, and Mi, dMi and other series are not
explained; trial stop_time is 6.998 s after start_time while each trial holds
5 s of frames; the spike times of KS0277A are not sorted; KS0125_ and KS0128_
lack the unit letter of 125B and 128D, and all session start times are
12:00; some series hold extreme values, such as whisker position from -985 to
596 degrees, that are not flagged; the cut-whisker recordings 199B and 209A
hold distance-to-pole series and contact frames (5,014 and 32) that the files
do not explain; and the paper's analysis code is available only on request.
No recording is deposited twice.

Streaming the files by range requests took 22 minutes for the metadata
alone, so the notebook reads each file whole into memory. The first two runs
gave wrong model results from a diverging spline fitter and a badly
conditioned viscoelastic fit, both fixed without changing a criterion, and
in the last revision the viscoelastic results moved slightly from round 2
(difference -0.030 against -0.029) with the same code, data and locked
packages, for a cause not found; refits from three other sets of random
starts keep the outcome. The round 1 verifier could not download the
supplement and round 2 found the Table S1 check unshown, so the notebook now
fetches and parses Table S1 on every run, which needs access to the
publisher's file server. The author's points on the protocol: no case for a
table from the paper itself as input; the paper's stated spread as tolerance,
which makes median and IQR claims nearly untestable; streaming that is slow
for files of many small datasets; a step that assumes public code exists; no
rule for fixing bugs in the attempt's own code after seeing outputs; whether
to block or test a subset when a model can be fitted on 15 of 28 afferents;
and small ambiguities in the link rule for the EMG ids and in a blocked claim
with two reasons.

## End of run

19 turns, 1 minutes, result: success.
