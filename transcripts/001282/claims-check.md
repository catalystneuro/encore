# 001282 · claims-check · run 39708673673

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001282/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims | head; ls claims | grep -i 1282; git show --stat HEAD | head -30; sed -n 96,200p docs/protocol.md
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
commit 8915b891d6d0b5806187df2eb735585bcbb30a85
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Thu Oct 22 01:56:43 2026 +0000

    Agent run on 001282: claims (success)
    
    Run: https://github.com/catalystneuro/reproduction-registry/actions/runs/39708165927
    
    Account: unverified

[... 109 more lines not kept]
```

**Agent**

The claims folder doesn't exist. Let me read the claims run's report.

**Agent calls Bash**

```bash
cat transcripts/001282/claims-report.md; tail -60 transcripts/001282/claims.md; git log --all --oneline -- claims/001282 | head
```

```
I stopped without writing any claims. The text I was given lacks the supplement that the NHP insertion results rest on, and the protocol says to stop in that case.

**What is under `paper/`**
- `10.1038-s41592-025-02614-5.txt`, the version of record. This is only the paywalled Nature page: the abstract, the figure titles, the Data and Code availability sections and the references. It has no Results, no Methods and no figure legends. There is no PDF.
- `10.1101-2023.10.24.563768.txt`, the bioRxiv preprint posted October 29, 2023. It has the main text, the figure legends and the Methods, but not the supplement. The page shows only a "Supplementary Material" link, and none of the Supplementary Figure legends appear in the text.

**Why the supplement is needed for this dataset**
The Data availability section says dandiset 001282 holds the NP1-NHP insertion datasets. In the preprint those results are in Fig. 4 and in Supp. Figs. 11 to 13 (Results, "Tracking long-range drift during probe insertion in non-human primates"):
- Supp. Fig. 11 shows the second of the two insertion datasets ("N = 2, Fig. 4 and Supp. Fig. 11") and its spike raster.
- Supp. Fig. 12 shows the finding that Kilosort's template-based drift tracking failed on these recordings.
- Supp. Fig. 13 shows the anatomical trajectory used to align the feature map with brain regions.

Without these, the second recording and the Kilosort comparison have neither a source nor a method, and the anatomical alignment is only partly specified.

**What would let this run go ahead**
Either of these would do:
- The accepted author manuscript in PubMed Central (PMC13055889, NIHMS2068114) with its supplement file (NIHMS2068114-supplement-supplementary.pdf). The claims file for the same paper, `claims/001290/`, was written from exactly these.
- The bioRxiv supplementary PDF for 10.1101/2023.10.24.563768, together with the main text.

Since no claims were written, there are none to count, and no open details or readings to rep
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i -E '^(Methods|Results|Supplementary)' *.txt | head; grep -c -i 'Supplementary Fig' *.txt
```

```
318 10.1038-s41592-025-02614-5.txt
   695 10.1101-2023.10.24.563768.txt
  1013 total
10.1101-2023.10.24.563768.txt:450:Supplementary Material
10.1038-s41592-025-02614-5.txt:1
10.1101-2023.10.24.563768.txt:0
```

**Agent**

I couldn't do the check: there is no claims file for DANDI:001282. The folder `claims/001282/` doesn't exist, and nothing in the git history ever touched it.

**Checker result:** not run, because there was no file to give it.

**Why there is no file.** The earlier claims run (commit 8915b891, report in `transcripts/001282/claims-report.md`) stopped on purpose without writing claims, as protocol step 1 requires when the supplement is missing. I confirmed what it found:
- `paper/10.1038-s41592-025-02614-5.txt`, the version of record, is only the paywalled page: abstract, figure titles, data and code availability, and references. It has no Results or Methods, and there is no PDF.
- `paper/10.1101-2023.10.24.563768.txt`, the bioRxiv preprint, has the main text, legends and Methods. It has no supplement, only a "Supplementary Material" link at line 450.
- The NHP insertion results that this dataset holds depend on Supp. Figs. 11 to 13. Those cover the second insertion recording, the Kilosort drift-tracking failure and the anatomical trajectory. None of them are in either text.

**Changes:** none. I added no `checks` entry, because there is no file to add it to, and writing claims is the claims role's job.

**Open:** a claims run needs the full text with its supplement first. The earlier run suggests either of these:
- the PMC author manuscript PMC13055889 (NIHMS2068114) with its supplementary PDF; `claims/001290/` was written from these
- the bioRxiv supplementary PDF together with the preprint

**Ready:** no. Nothing exists yet that an attempt could use.

## End of run

5 turns, 0 minutes, result: success.
