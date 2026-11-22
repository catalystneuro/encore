# seneque-2026 · claims · run 45036371782

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; ls claims | head; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls -la paper/; ls claims | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
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
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.48550-arxiv.2606.12923.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.48550-arxiv.2606.12923.txt",
 "offset": 1293,
 "limit": 1100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/seneque-2026.yaml; grep -n -A3 "seneque" papers/keys.yaml; ls papers/datasets | head -3
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.48550/arxiv.2606.12923
title: 'Order Is Not Control: Driven-Dissipative Response Laws Across Artificial and Biological Systems'
datasets:
- archive: dandi
  id: '001075'
  relation: reuses
313:  10.48550/arxiv.2606.12923: seneque-2026
314-  10.48550/arxiv.2610.00990: salahshour-2026
315-  10.52202/085713-4642: temmar-2025
316-  10.64898/2025.12.12.694045: daste-2025
alasfour-2024.yaml
amjad-2025.yaml
andrews-2024.yaml
```

**Agent**

Read through Appendix B.3 so far. The dataset (Randi et al. C. elegans signal propagation atlas) backs only the paper's worm panel; reading the rest for its methods and any code link.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "worm|elegans|neuropal|github|zenodo|code avail|repository|315|0\.596825|randi|001075" 10.48550-arxiv.2606.12923.txt | sed -n '1,200p'
```

```
grep: 10.48550-arxiv.2606.12923.txt: binary file matches
```

**Agent calls Grep**

```json
{
 "pattern": "(?i)worm|elegans|neuropal|github|zenodo|code avail|repositor|\\b315\\b|0\\.596825|randi|001075|event-receiver|propagation",
 "path": "paper/10.48550-arxiv.2606.12923.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.48550-arxiv.2606.12923.txt",
 "offset": 2392,
 "limit": 990
}
```

Result: not kept, because it reads the paper's text.

**Agent calls ToolSearch**

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```

Result: no output.

**Agent calls WebFetch**

```json
{
 "url": "https://arxiv.org/abs/2606.12923",
 "prompt": "List: versions available, any ancillary files, any linked code repository or supplementary material, and the comments field."
}
```

Result: the fetched text is not kept.

**Agent**

I wrote no claims file. The only claim DANDI:001075 could test rests on methods that are in neither the paper nor any code, so under the protocol's Reader step 1 I stopped. `claims/seneque-2026.yaml` does not exist and nothing in the working tree changed.

**Text read:** I read the whole of `paper/10.48550-arxiv.2606.12923.txt`: arXiv preprint v2 (12 June 2026), the main text plus Appendices A to D. There is no PDF in `paper/`. The arXiv page shows v1 and v2, no ancillary files and no code repository, and the paper links no code.

**What the dataset can test:** DANDI:001075 is the Randi et al. C. elegans signal propagation atlas (reference [64]). The paper reuses it for one result, the worm "neural perturbation-propagation" operator:
- 315 event-receiver rows and 67 NeuroPAL labels.
- Held-out weighted sign accuracy of 0.596825 over 68 receiver/operator groups.
- Wilson 95% CI 0.541803 to 0.649515, and p = 6.988 x 10^-4 against a 50% sign null (Appendix B.1, Table 1).

The body text (Section 3) conflicts with this. It calls the result "68 held-out receiver/operator rows", where Appendix B.1 has 315 eval rows in 68 groups.

**What is missing for that claim:** Nothing in the paper defines the method. Appendix A.6 only lists generic denominator parts (perturbation family, receiver variables, event window, held-out split, validation test). It does not say:
- what an "event-receiver row" is (which stimulation events, which receiving neurons, which response window);
- what sign is predicted, and from what predictor or model;
- how the 68 held-out groups are formed;
- how the accuracy is weighted.

Appendix D.1 says the implementation details, analysis labels and figure source data "remain in supplementary materials". Those are not under `paper/` and not on arXiv. The predecessor ATLAS paper (arXiv 2604.17663, ref [3]), which supplies the "intervention and geometry pipeline", may describe the method, but it is a different paper and I did not use it.

If I wrote a criterion now, I would be making up every part of the method, which the protocol forbids. Since the method is missing entirely, not left partly open, I have no "open details with named readings" to report.

**Rest of the paper:** The other findings (mouse ALM, zebrafish, and all the LLM and adapter panels) use data outside this dataset. They report tables of numbers with no recoverable methods, and their source artifacts are internal (T-numbered rows) and unpublished.

**Needed before claims can be written:** the authors' supplementary materials or analysis code for the C. elegans panel (the T2541 to T2600 biological rows), or the methods document for it.

## End of run

13 turns, 1 minutes, $0.91 at API prices, result: success.
