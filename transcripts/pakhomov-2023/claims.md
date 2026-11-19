# pakhomov-2023 · claims · run 42829173527

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ | grep -i pakhomov; ls claims/pakhomov-2023/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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

**Agent calls Bash**

```bash
ls paper/ | grep -i -E "pakhomov|108437"; cat claims/fouke-2025.yaml | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/10.1016-j.bioelechem.2023.108437.txt; cat paper/10.1016-j.bioelechem.2023.108437.txt; ls paper/; cat papers/datasets/pakhomov-2023.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/9cc7d88a-3403-424a-8ece-441957abf591/tool-results/bhhjpeqqh.txt"
}
```

```
1	86 paper/10.1016-j.bioelechem.2023.108437.txt
2	DOI: 10.1016/j.bioelechem.2023.108437
3	Version: as served by ncbi_pmc
4	Source: ncbi_pmc+crossref (paper-text-fetcher)
5	Stored: 2026-10-20
6	Extracted: as fetched
7	------------------------------------------------------------------------
8	pmc Bioelectrochemistry Bioelectrochemistry 319 nihpa 100953583 Bioelectrochemistry (Amsterdam, Netherlands) 1567-5394 1878-562X pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC10247516 PMC10247516.319 10247516 10247516 NIHMS1891360 37030093 10.1016/j.bioelechem.2023.108437 NIHMS1891360 NIHPA1891360 319 Article Next generation CANCAN focusing for remote stimulation by nanosecond electric pulses Pakhomov Andrei G. a * Gudvangen Emily a Mangalanathan Uma a Kondratiev Oleg b Redondo Luis c Semenov Iurii a a Frank Reidy Research Center for Bioelectrics, Old Dominion University, Norfolk, VA 23508, USA b Energy Pulse Systems, Lisbon, Portugal c Pulsed Power Advanced Applications Group, Lisbon Engineering Superior Institute, GIAAPP/ISEL, Lisbon, Portugal Author contributions A.G.P. conceived the study; I.S. and U.M. performed experiments; O.K. and L.R. built the nsEP generator; E.G. performed electric field simulations; I.S., U.M., and A.G.P. analyzed and interpreted the data; A.G.P. wrote the manuscript, with contributions and editing by all authors. * Corresponding author: Andrei G. Pakhomov, Frank Reidy Research Center for Bioelectrics Old Dominion University, 4211 Monarch Way., Suite 300, Norfolk, VA 23508, +1(210)2049012, +1(757)6838003, Fax: +1(757)4511010, [removed: an e-mail address] ; [removed: an e-mail address] 8 2023 05 4 2023 152 437681 108437 108437 13 04 2023 01 08 2024 01 08 2024 09 06 2023 01 08 2024 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Focusing electric pulse effects away from electrodes is a challenge because the electric field weakens with distance. Previously we intr
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/pakhomov-2023; for f in *.yaml; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (114KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9cc7d88a-3403-424a-8ece-441957abf591/tool-results/b029cpiid.txt

Preview (first 2KB):
=== 000686.yaml
# Claims for Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023),
# "Next generation CANCAN focusing for remote stimulation by nanosecond electric pulses",
# Bioelectrochemistry 152, 108437, on dandiset 000686.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (PMC10247516, NIHMS1891360), as
# served by ncbi_pmc, full text with Methods (sections 2.1 to 2.4), Results, Discussion and
# figure legends. The version of record was not read. PMC lists no supplement and the text cites
# none. The paper links no code, so no repository was read. Every method detail below comes from
# the Methods or the figure legends.
#
# Data the paper used (as the paper reports it). All experiments are in CHO-K1 cells (Chinese
# hamster ovary). The archive's metadata names the species as Bos taurus, which does not match
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/9cc7d88a-3403-424a-8ece-441957abf591/tool-results/b029cpiid.txt"
}
```

```
1	=== 000686.yaml
2	# Claims for Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023),
3	# "Next generation CANCAN focusing for remote stimulation by nanosecond electric pulses",
4	# Bioelectrochemistry 152, 108437, on dandiset 000686.
5	#
6	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
7	# protocol pilot-10 as stated in docs/protocol.md.
8	#
9	# Text read: the accepted author manuscript in PubMed Central (PMC10247516, NIHMS1891360), as
10	# served by ncbi_pmc, full text with Methods (sections 2.1 to 2.4), Results, Discussion and
11	# figure legends. The version of record was not read. PMC lists no supplement and the text cites
12	# none. The paper links no code, so no repository was read. Every method detail below comes from
13	# the Methods or the figure legends.
14	#
15	# Data the paper used (as the paper reports it). All experiments are in CHO-K1 cells (Chinese
16	# hamster ovary). The archive's metadata names the species as Bos taurus, which does not match
17	# the paper. Electroporation is measured by YO-PRO-1 (YP) dye uptake.
18	# - Individual cells (Fig. 4, Sections 2.2 and 3.1). Cells on glass coverslips, YP 1 uM, confocal
19	#   images (40x) every 10 s for 600 s, pulses at 57 s. Two tungsten electrodes (140 um gap, 50 um
20	#   above the coverslip) driven from two EPULSUS-FPM4-7 channels. Five groups, 21 to 30 cells
[... 787 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/pakhomov-2023; for f in *.yaml; do echo "=== $f"; grep -E "^- id:|^#.*[Dd]andiset|title" $f; done; sed -n '/^# Dandiset\|dandiset 0010/,+6p' 001025.yaml 001027.yaml | head -40
```

```
=== 000686.yaml
# Bioelectrochemistry 152, 108437, on dandiset 000686.
# The dandiset's title matches the legend of Fig. 5 ("Focusing electroporation to the center of a
- id: fig3-field-simulation
- id: fig4-sham-no-uptake
- id: fig4-unipolar-uptake
- id: fig4-bipolar-weaker
- id: fig4-8phase-cancellation
- id: fig5a-trains-stronger
- id: fig5a-packet-center-enhanced
- id: fig5b-rotation-center-peak
- id: fig5c-normalized-contrast
- id: fig6a-more-packets-more-uptake
- id: fig6b-center-to-periphery
- id: fig6-void-between
- id: fig6-peak-narrower
- id: fig7a-amplitude-scales-uniformly
- id: fig7-amplitude-no-effect-on-distribution
- id: fig8-center-equal-packets
- id: fig8a-periphery-packets-1-3-higher
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git show --stat HEAD | head -20; grep -rl "001028" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | head; grep -rh "001028" -A3 papers/ 2>/dev/null | head -30; grep -h "title" claims/pakhomov-2023/001025.yaml claims/pakhomov-2023/001027.yaml -A2 | head
```

```
commit 68022d17b2e4f32e89a4a36b9c5ccd45e19fa8d9
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Tue Nov 10 08:56:24 2026 -0500

    Paper match for DANDI:001028: matched
    
    From attempt/001028 (docs/pipeline.md, step 1).

 papers/datasets/pakhomov-2023.yaml             |  3 +
 papers/match/001028.yaml                       | 24 +++++++
 transcripts/match/001028/paper-match-report.md |  9 +++
 transcripts/match/001028/paper-match.md        | 95 ++++++++++++++++++++++++++
 4 files changed, 131 insertions(+)
./transcripts/semenov-2025/001048/verifier-1.md
./transcripts/pakhomov-2023/001025/answer.md
./transcripts/pakhomov-2023/001025/author-revise-1.md
./transcripts/pakhomov-2023/001025/author-answers.md
./transcripts/pakhomov-2023/001025/author-answers-report.md
./transcripts/pakhomov-2023/001025/author.md
./transcripts/pakhomov-2023/001025/author-report.md
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/match/001028.yaml; cat transcripts/match/001028/paper-match-report.md; grep -i -E "title|description|3D|gap|distance" transcripts/match/001028/paper-match.md | head -20
```

```
# Whether each paper DANDI:001028 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: 001028
date: '2026-11-10'
papers:
- doi: 10.1016/j.bioelechem.2023.108437
  relation: IsPublishedIn
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: partial
  by: agent
  reason: The dataset holds the 3D focusing experiment of Fig. 9 (array placed 0 to 3 mm above CHO monolayers, Packet 2, YO-PRO-1 imaging), whose name and description copy that figure's legend. The paper's other experiments (bipolar cancellation in Fig. 4, focusing and parameter studies in Figs. 5 to 8) are not in it, and the paper names no repository for them.
  evidence:
  - source: archive metadata
    quote: CANCAN focusing of electroporation in 3D
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "^  datasets:" claims/*.yaml | head; grep -n -B2 -A6 "datasets:\|not_available\|not available" docs/paper-first.md | head -60; ls tools/
```

```
claims/kim-2022.yaml
30-- A paper's claims are extracted once, for the paper. Most papers rely on one dataset, and then
31-  claims name none: they rest on it. Only when the paper lists more than one does each claim
32:  carry `datasets:`, naming the ones it rests on. An attempt tests the paper against as many of those datasets as can be found and
33-  loaded: Semenov 2026's next attempt loads all 7 dandisets.
34-- The paper's datasets are listed in `papers/datasets/<paper key>.yaml`: each with archive, id,
35-  relation (primary or reuses) and how it was found (archive metadata, the paper's data
36-  availability statement, find_reuse). A dataset the paper relies on that is in no open archive,
37-  or cannot be loaded, is listed with `available: false` and why.
38-- **Missing datasets do not stop an attempt.** It runs on what is there; its record lists the
--
58-id: tingley-2021-01
59-paper: doi:10.1038/s41586-021-03811-w
60:datasets:
61-- archive: dandi
62-  id: "000233"
63-  version: 0.250624.0414
64-  relation: primary        # the paper the data were published with; or: reuses
65:missing_datasets: []       # datasets the paper relies on that this attempt could not use, each with why
66-entry: tingley-2021
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
head -40 claims/kim-2022.yaml; grep -n "datasets:\|data: elsewhere\|data_missing" -A3 claims/kim-2022.yaml | head -60; grep -n "datasets\|dataset" tools/claims_check.py | head -30
```

```
# Claims for Kim, Semenov, Kiester, Keppler, Ibey, Bixler & Pakhomov (2022), tested on dandisets
# 000489 and 000448.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol pilot-14 as stated in docs/protocol.md. It replaces the file written 2026-10-23 under
# pilot-10 for dandiset 000489 alone; ids are kept where the finding is the same.
#
# Text read. The accepted author manuscript in PubMed Central (PMC9729435, NIHMS1849847), as
# served by ncbi_pmc, in paper/10.1016-j.bioelechem.2022.108319.txt. It holds the main text, the
# Methods (sections 2.1 to 2.6), the Results (3.1 to 3.5), the Discussion and the legends of Figs.
# 1 to 7. It is not the version of record. The paper has no supplement (PMC marks
# "has-supplement no", and the text cites none). No PDF was supplied, so figures were not read and
# values shown only in a figure are not used. The paper links no code and no data deposit, so no
# repository was read.
#
# The datasets, from their titles on DANDI.
# - 000489, "The impact of the second phase amplitude (% to the first phase) on the electroporation
#   efficiency (measured as YP emission)", bovine cells. This is the title of Fig. 2A, so it is
#   meant to hold the experiment of Fig. 2 (Results 3.1). The claims on Fig. 2 rest on it.
# - 000448, "Time kinetics of the membrane potential at the cathode- and anode-facing poles of a
#   cell induced by a train of 5 pulses at 833 kHz", Chinese hamster. This is the title of Fig. 7,
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p tools/claims_check.py | grep -n -i "dataset\|elsewhere\|required\|data_missing\|def " | head -60
```

```
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
105:def main() -> int:
```

**Agent calls Bash**

```bash
grep -l "^  datasets:" claims/*.yaml claims/*/*.yaml 2>/dev/null; grep -rn "datasets: \[\]" claims/ | head
```

```
claims/kim-2022.yaml
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/9cc7d88a-3403-424a-8ece-441957abf591/tool-results/b029cpiid.txt",
 "offset": 807,
 "limit": 420
}
```

```
807	    YP emission in the center from 183% for Packet 2 to 83% and 74% for Packets 3 and 1,
808	    respectively
809	  expected:
810	  - quantity: normalized center, Packet 2
811	    value: 183
812	    tolerance: 18.3
813	    unit: percent of most peripheral ROI
814	  - quantity: normalized center, Packet 3
815	    value: 83
816	    tolerance: 8.3
817	    unit: percent of most peripheral ROI
818	  - quantity: normalized center, Packet 1
819	    value: 74
820	    tolerance: 7.4
821	    unit: percent of most peripheral ROI
822	  criterion: Profile method of the header, normalized as in Fig. 8B. Reproduced when all three are
823	    within tolerance under one combination of readings; partially reproduced when Packet 2 is
824	    highest and above 100% but some values fall outside tolerance.
825	- id: fig8-cancellation-predicts-targeting
826	  statement: The bipolar signal with the strongest cancellation between two electrodes (8-phase,
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
ls questions/ | grep -i pakhomov; cat questions/pakhomov-2023*.yaml 2>/dev/null | head -150; sed -n '/^checks:/,$p' claims/pakhomov-2023/001025.yaml claims/pakhomov-2023/001027.yaml
```

```
<persisted-output>
Output too large (29.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9cc7d88a-3403-424a-8ece-441957abf591/tool-results/b8x0mp1jv.txt

Preview (first 2KB):
pakhomov-2023
checks:
- date: 2026-10-22
  kind: agent
  model: "claude-opus-5-5"
  ready: true
  changes:
  - fig4-bipolar-cancellation, criterion. Dropped Welch's t-test as a reading; the only test the paper names is Student's t-test (Section 2.4). Welch is kept as a variant.
  - fig5bc-rotation-focuses-center, statistics removed. The paper reports no test result for Fig. 5; the entry was the Methods' significance threshold, which is not a result.
  - fig5bc-rotation-focuses-center, criterion. The void test (center below the trough-to-periphery mean) was not from the paper; replaced by two named readings of "void", (a) normalized center below 100%, (b) center as the profile minimum.
  - fig6b-normalized-center-by-packets, criterion. Removed the remark that 180% to 200% is the plain reading of "almost", which contradicted the stated tolerance; the claim holds from 180% to 220%.
  - fig8a-packets-differ-near-electrodes, expected. The range 215 to 235 widened by 10% of each bound is 193.5 to 258.5, so the value is 226 (was 225).
  - fig8a-packets-differ-near-electrodes, expected. The range 250 to 350 widened by 10% of each bound is 225 to 385, so value 305 and tolerance 80 (was 300 and 85, which allowed 215).
  - Open. fig5a-center-enhanced-without-rotation reads "enhanced electroporation in the center" as center above the trough between center and e1, and fig7b and fig7cd test amplitude independence at the center and half-way ROIs only. The paper gives no measure for either; these are the writer's readings, stated in the criteria, and the all-ROI test is shown as a variant for Fig. 7.
  - Open. fig4-unipolar-strongest judges "no gain" for sham with a one-sample t-test of F minus F0 against zero; the paper names no test for this, and the criterion says so
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
ls questions/pakhomov-2023/; grep -h -E "claim:|question:|answer:" -A4 questions/pakhomov-2023/*.yaml | cut -c1-400 | head -120
```

```
000686.yaml
001025.yaml
- claim: fig6a-more-packets-more-uptake
  asked: 2026-10-31
  question: The monolayer data of Figs. 6 to 9 are not in dandiset 000686, which holds only the 18
    images of Fig. 5. Four other published dandisets of the same lab name this paper as the one they
    are published in (relatedResource IsPublishedIn 10.1016/j.bioelechem.2023.108437) and their
    titles and descriptions match the figures, DANDI:000875 (0.240515.1925, packet number, Fig. 6),
    DANDI:001025 (0.240605.1826, voltage and array size, Fig. 7), DANDI:001027 (0.240605.1859, the
--
- claim: fig5b-rotation-center-peak
  asked: 2026-10-31
  question: The criterion requires both comparisons "under all readings of O1, O2 and O4" and says
    "Each comparison uses a two-sided t-test at p < 0.05 (Methods 2.4, O6)". O6 runs both the paired
    and the unpaired test for comparisons inside the same dishes. Must both tests hold for the claim
    to be reproduced, as the fig5a-packet-center-enhanced criterion says outright ("paired and
    unpaired, O6"), or does one of them suffice, and if so which?
--
- claim: fig5c-normalized-contrast
  asked: 2026-10-31
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cat questions/pakhomov-2023/*.yaml | cut -c1-600
```

```
dandiset: "000686"
paper: doi:10.1016/j.bioelechem.2023.108437
questions:
- claim: fig6a-more-packets-more-uptake
  asked: 2026-10-31
  question: The monolayer data of Figs. 6 to 9 are not in dandiset 000686, which holds only the 18
    images of Fig. 5. Four other published dandisets of the same lab name this paper as the one they
    are published in (relatedResource IsPublishedIn 10.1016/j.bioelechem.2023.108437) and their
    titles and descriptions match the figures, DANDI:000875 (0.240515.1925, packet number, Fig. 6),
    DANDI:001025 (0.240605.1826, voltage and array size, Fig. 7), DANDI:001027 (0.240605.1859, the
    three packets at 4 kV, Fig. 8) and DANDI:001028 (0.240605.1954, electrodes 0 to 3 mm above the
    monolayer, Fig. 9). Should the claims on Figs. 6 to 9 (fig6a-more-packets-more-uptake,
    fig6b-center-to-periphery, fig6-void-between, fig6-peak-narrower,
    fig7a-amplitude-scales-uniformly, fig7-amplitude-no-effect-on-distribution,
    fig8-center-equal-packets, fig8a-periphery-packets-1-3-higher, fig8b-normalized-center,
    fig9a-gap-reduces-periphery-more, fig9b-gap-boosts-targeting) say `data` set to `elsewhere` with these
    dandisets under `where`, so that an attempt may test them there?
  passage: Each dish was used in one experiment (Methods 2.1). Fluorescence data are presented as a
    mean +/- s.e. for 3-5 independent experiments (Methods 2.4). The claims file's header says "Which
    of the other experiments it holds is for the author to find", and every claim has the default
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^# Details\|^# Open\|^# Method/,/^schema/p' claims/pakhomov-2023/001027.yaml | head -60; sed -n '/id: fig8a-equal/,/id: fig9-gap/p' claims/pakhomov-2023/001027.yaml
```

```
# Details the paper leaves open, named in the criteria with the readings it allows: which array
# was used in Figs. 6 and 8 (small or large); whether a profile is taken along one diagonal or
# averaged over both (stated only for Fig. 5); which ROI is "the center" and which is "most
# peripheral" when a diagonal has two ends; the ROI size; whether monolayer intensities are
# background-subtracted; whether the t-test is applied in Fig. 4 (the Methods name it only in
# Section 2.4); and how peak width is measured (Fig. 6).
schema_version: 2
- id: fig8a-equal-center-uptake
  statement: Packets 1, 2 and 3 (4 kV, 1Px4) produce the same YP uptake in the center of the array,
    215 to 235 a.u.
  source: Results, 3.4, paragraph 2; Figure 8A
  quote: All packets produced the same YP uptake in the center (215–235 a.u.)
  expected:
  - quantity: center YP uptake, lower bound of the range over packets
    value: 215
    tolerance: 21.5
    unit: a.u.
  - quantity: center YP uptake, upper bound of the range over packets
    value: 235
    tolerance: 23.5
[... 68 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/pakhomov-2023.yaml",
 "content": "# Claims for Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023), \"Next\n# generation CANCAN focusing for remote stimulation by nanosecond electric pulses\",\n# Bioelectrochemistry 152, 108437, tested on dandisets 000686, 000875, 001025, 001027 and 001028.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md. It replaces the four files written 2026-10-22\n# and 2026-10-23 under pilot-10, one per dataset (claims/pakhomov-2023/); ids are kept where the\n# finding is the same, taken from the file of the dataset that holds the figure.\n#\n# Text read. The accepted author manuscript in PubMed Central (PMC10247516, NIHMS1891360), as\n# served by ncbi_pmc, in paper/10.1016-j.bioelechem.2023.108437.txt: Introduction, Materials and\n# methods (2.1 to 2.4), Results (3.1 to 3.5), Discussion and the legends of Figs. 1 to 9. It is\n# not the version of record. The paper has no supplement (PMC marks \"has-supplement no\", and the\n# text cites none). No PDF was supplied, so no figure was read, and values printed only in a\n# figure (the voltages of Fig. 7 other than 2.4 and 5.6 kV, every axis value) are not used. The\n# paper links no code and no data deposit (images were measured in MetaMorph 7.8.13 and Fiji,\n# graphs drawn in Grapher 16), so no repository was read. Every method below is from the Methods\n# or the figure legends.\n#\n# The datasets, from their titles on DANDI.\n# - 000686, \"Focusing electroporation to the center of a quadrupole electrode array by\n#   interference of unipolar pulses\", the title of Fig. 5. Claims on Fig. 5 rest on it.\n# - 000875, \"Influence of unipolar pulse packet quantity on centering the electroporation effect\n#   within a quadrupole electrode array\", the experiment of Fig. 6.\n# - 001025, \"The impact of voltage on CANCAN focusing of electroporation using four-electrode\n#   arrays of varying sizes\", the experiment of Fig. 7.\n# - 001027, \"CANCAN focusing of electroporation in a quadrupole array by different pulsing\n#   protocols\", the experiment of Fig. 8 (three packets, 1Px4, 4 kV).\n# - 001028, \"CANCAN focusing of electroporation in 3D\", the title of Fig. 9.\n# - No title names the single-cell experiment of Fig. 4 or the field simulations of Fig. 3, and\n#   the paper gives no other data location. Those claims list all five datasets: the author checks\n#   each, and blocks the claim as data_missing when none holds the data. They are kept because\n#   Fig. 4 is the basis of the paper's design and of its last finding.\n#\n# Data the paper used, as it reports them. All experiments are in CHO-K1 cells. Electroporation is\n# measured as uptake of YO-PRO-1 dye (YP), as fluorescence intensity.\n# - Individual cells (Fig. 4; Methods 2.2, Results 3.1). Cells on 10-mm glass coverslips, 1 uM YP,\n#   confocal images (40x, 0.95 NA) every 10 s for 600 s, pulses at 57 s. Two tungsten electrodes\n#   (100 um diameter, 140 um gap, 50 um above the coverslip) driven from two EPULSUS-FPM4-7\n#   channels. Five groups, 21 to 30 cells each (25 for the unipolar pulse): sham; one 600-ns\n#   unipolar pulse at 15 kV/cm; and three bipolar signals that start with the same pulse and lose\n#   1/8 of the first amplitude per phase (4 phases; 8 phases; 8 phases with 5-us delays). Per\n#   cell, a manual ROI; F is its mean intensity, F0 the mean of the six images before the pulses,\n#   and F-F0 is the measure. Groups were run in random order.\n# - Cell monolayers (Figs. 5 to 9; Methods 2.3 and 2.4). 35-mm glass-bottom dishes, one dish per\n#   experiment (Methods 2.1). A quadrupole array of four 1.5-mm needles (e1 to e4), small or large\n#   (about 2-fold apart; the large has an 8.4-mm diagonal), touching the glass or, in Fig. 9, 1 to\n#   3 mm above it. Packets 1, 2 and 3 of 600-ns unipolar pulses (Fig. 2B to D), delivered at 1 Hz.\n#   \"nPx4\" is n packets from each electrode in turn; \"1Px40\" is one packet rotated 40 times; the\n#   control \"trains\" energize one electrode with the same pulses. YP 1 uM for 10 min, rinsed, then\n#   stitched 10x images. Intensity in 92 or 224 ROIs along one or both diagonals, over +/- 1.65 mm\n#   (small array) or +/- 3.65 mm (large array) from the geometric center, leaving out areas next to\n#   the electrodes (<5% of the diagonal length). Values in a.u. or in % of the most peripheral ROI\n#   (closest to the electrode). Mean +/- s.e. over 3 to 5 independent experiments, LOESS fits.\n#   Per figure: Fig. 5, Packet 2 at 6.4 kV, 40 packets against 40 trains, from e1 only (A, e1 to e3\n#   diagonal) or rotated (B, C, both diagonals averaged), large array (Results 3.2 refers to Fig.\n#   3C), n = 4 to 5. Fig. 6, Packet 2, 1Px4, 5Px4 and 10Px4, n = 3 to 4. Fig. 7, Packet 2 at\n#   several first-pulse voltages, 1Px4 in the small array (A, B; 2.4 to 5.6 kV) and 10Px4 in the\n#   large array (C, D), n = 3. Fig. 8, Packets 1, 2 and 3, 4 kV, 1Px4, n = 3 to 4. Fig. 9, large\n#   array, Packet 2, 10Px4, 6.4 kV, 0, 1, 2 or 3 mm above the monolayer, n = 3 to 4.\n# - Electric field simulations (Fig. 3; Methods 2.3) in Sim4Life, as in the paper's reference 15\n#   (doi:10.1016/j.bioelechem.2021.107876). Model outputs, not recordings.\n#\n# Statistics (Methods 2.4). \"Two-sided Student's t-test\", p < 0.05, the only test the paper\n# names; Student's names the equal-variance form, and Welch's form is a variant only. Between\n# treatments the groups are different dishes, so the test is unpaired. In the figures,\n# significance is read from the gap between error bars (a gap longer than the bars means\n# p < 0.05); this rule is shown as a variant where a claim rests on a figure. Methods 2.2 names no\n# test for the single cells; the Methods 2.4 test is used for them, and this is a reading.\n#\n# Details the paper leaves open, with the readings it allows. A criterion that uses one says so.\n# For an expected value, the claim holds when it matches under any combination of readings. For a\n# test, the outcome is the one all readings give; when they differ, the author adopts the reading\n# the paper best supports, as an assumption, or blocks the claim as methods_underspecified, with\n# every result shown.\n# (O1) ROI layout. 92 (small) or 224 (large) ROIs \"along one or both diagonals\" over the stated\n#      range. Readings (a) the count is for one diagonal, spacing about 36 um (small) or 33 um\n#      (large); (b) the count is split over two diagonals, about 72 um or 65 um. The count and\n#      range fix the ROI length along the diagonal under each reading; the extent across the\n#      diagonal is not given. Readings (w1) square ROIs, side equal to the spacing (a standard\n#      choice); (w2) three spacings wide, as a check on sensitivity. Neither comes from the paper.\n# (O2) Diagonals. Fig. 5A uses the e1 to e3 diagonal and Fig. 5B averages both (legends). For\n#      Figs. 6 to 9 the paper does not say. Readings (a) both diagonals averaged by distance;\n#      (b) one diagonal.\n# (O3) Center. Readings (a) the ROI nearest the geometric center; (b) the mean of the two ROIs on\n#      either side of it when none is centered.\n# (O4) Most peripheral ROI. Each measured diagonal has two ends. Readings (a) the mean of the end\n#      ROIs; (b) each half-diagonal taken to its own end ROI, then averaged. For Fig. 5A the e1\n#      end is named by the text.\n# (O5) Normalization order. Readings (a) each dish normalized to its own most peripheral ROI,\n#      then averaged; (b) the mean profile divided by its own most peripheral value. Tests on\n#      normalized values use (a), which gives per-dish values.\n# (O6) Background. Methods 2.4 says nothing about background for the monolayer images\n#      (Methods 2.2 subtracts F0 for single cells). Readings (a) raw ROI intensity; (b) intensity\n#      minus a background the images allow (a cell-free or dark area, or the needle footprints).\n# (O7) Raw values or LOESS. Values in the text may have been read from ROI means or from the LOESS\n#      fits, whose span is not given. Readings (a) dish means of ROI values; (b) the LOESS fit of\n#      the mean profile, spans 0.25 and 0.75 as standard choices.\n# (O8) Paired or unpaired. For comparisons inside the same dishes (center against trough, center\n#      against periphery) the paper does not say. Readings (a) paired; (b) unpaired.\n# (O9) Trough. \"The least affected area ... between the center and the electrodes\" (Results\n#      3.3). The ROI with the lowest mean between the center and the most peripheral ROI.\n#      Readings (a) the mean of the two sides; (b) each side.\n# (O10) \"End of recording\" (Fig. 4). Readings (a) the last image (600 s); (b) the mean of the last\n#      six images, matching the six-image baseline.\n# (O11) Arrays and voltages. The paper does not state the array of Figs. 6 and 8, nor the\n#      first-pulse voltage of Fig. 6, nor the voltages of Fig. 7C, D. The author takes them from\n#      the dataset and reports them; they do not change a criterion.\nschema_version: 2\npaper: doi:10.1016/j.bioelechem.2023.108437\nclaims:\n- id: fig3-field-simulation\n  statement: In the simulations, 1 kV applied to one electrode gives about 1.8 kV/cm in the center\n    of the small array and 0.8 kV/cm in the center of the large array, and about 4-fold more near\n    the energized electrode (7 and 3.5 kV/cm per kV). Energizing one diagonal gives no field in the\n    center.\n  source: Methods 2.3, paragraph 4; Figure 3\n  quote: For example, applying 1 kV to one electrode produced the electric field of approximately\n    1.8 kV/cm and 0.8 kV/cm in center of the small and large arrays ... The electric field strength\n    was about 4-fold higher near the energized electrode (7 kV/cm and 3.5 kV/cm per 1 kV applied, for\n    the small and large arrays, respectively) Note that energizing either electrode diagonal produced\n    no electric field in the center of the array\n  datasets:\n  - \"000686\"\n  - \"000875\"\n  - \"001025\"\n  - \"001027\"\n  - \"001028\"\n  expected:\n  - quantity: center field, small array, per kV on one electrode\n    value: 1.8\n    tolerance: 0.18\n    unit: kV/cm\n  - quantity: center field, large array, per kV on one electrode\n    value: 0.8\n    tolerance: 0.08\n    unit: kV/cm\n  - quantity: field near the energized electrode, small array, per kV\n    value: 7\n    tolerance: 0.7\n    unit: kV/cm\n  - quantity: field near the energized electrode, large array, per kV\n    value: 3.5\n    tolerance: 0.35\n    unit: kV/cm\n  criterion: The values are outputs of the paper's Sim4Life model (Methods 2.3, built as in its\n    reference 15), which the paper does not deposit. The claim is tested only if a dataset holds\n    the simulated field maps; a field model built by the author is not the paper's and is not a\n    test. With the maps, reproduced when the four values are within tolerance and the center field\n    with a diagonal energized is below 1% of the single-electrode center field. How far from the\n    electrode \"near\" is measured is not given; the highest value outside the needle is used. Without\n    the maps, blocked as data_missing.\n- id: fig4-sham-no-uptake\n  statement: Sham-exposed cells gain no YP fluorescence over the 10 min of imaging, while cells\n    given pulses show a gradual rise in YP signal from the first image after exposure.\n  source: Results 3.1, paragraph 2; Figure 4\n  quote: Sham-exposed cells showed no gain in YP fluorescence during the 10 min of observation. In\n    contrast, cells treated by electric pulses displayed gradual increase in YP signal, starting from\n    the image frame taken immediately after nsEP exposure.\n  datasets:\n  - \"000686\"\n  - \"000875\"\n  - \"001025\"\n  - \"001027\"\n  - \"001028\"\n  criterion: Per cell F-F0 (Methods 2.2). A claim of absence for sham, for which the paper reports\n    no test; it is judged with the test Methods 2.4 names, a two-sided Student's t-test at p < 0.05,\n    here one-sample against zero at the end of recording (O10, both readings). Reproduced when sham\n    F-F0 does not differ from zero, and, for every pulsed group, the mean at the first image after\n    57 s exceeds zero by the same test and the end value exceeds the first post-pulse value. Not\n    reproduced when sham differs from zero. The sham effect size is given either way.\n- id: fig4-unipolar-strongest\n  statement: A single 600-ns pulse at 15 kV/cm causes by far the strongest YP uptake, 126 +/- 14\n    a.u. (n = 25 cells) by the end of recording.\n  source: Results 3.1, paragraph 2; Figure 4\n  quote: A single 600-ns pulse at 15 kV/cm caused by far the strongest YP uptake, reaching 126±14\n    a.u. (n=25) by the end of recording.\n  datasets:\n  - \"000686\"\n  - \"000875\"\n  - \"001025\"\n  - \"001027\"\n  - \"001028\"\n  expected:\n  - quantity: unipolar pulse, F-F0 at end of recording, mean over cells\n    value: 126\n    tolerance: 14\n    unit: a.u.\n  criterion: Tolerance is the paper's s.e. Per cell F-F0 (Methods 2.2), mean over cells, at the end\n    of recording (O10). Reproduced when, under one reading, the mean is within tolerance and exceeds\n    every other group's mean. The group size is reported against n = 25.\n- id: fig4-bipolar-weaker\n  statement: Bipolar signals that start with the same pulse cause significantly weaker uptake\n    (p < 0.001). By the end of recording the 4-phasic signal reaches 20.8 +/- 2.0 a.u., the 8-phasic\n    6.9 +/- 1.6 a.u., and the 8-phasic with 5-us delays 25.4 +/- 2.8 a.u.\n  source: Results 3.1, paragraph 2; Figure 4\n  quote: Bipolar signals started with exactly the same pulse (600 ns, 15 kV/cm) but caused\n    significantly weaker effects (p<0.001). By the end of recording, YP signal reached only 20.8±2.0\n    a.u. for the 4-phasic signal; 6.9±1.6 a.u. for the 8-phasic signal; and 25.4±2.8 a.u. for the\n    8-phasic signal with 5-μs delays between phases.\n  datasets:\n  - \"000686\"\n  - \"000875\"\n  - \"001025\"\n  - \"001027\"\n  - \"001028\"\n  statistics:\n  - about: each bipolar signal against the single unipolar pulse, end of recording\n    test: not named for single cells (Methods 2.2 names none; Methods 2.4 names a two-sided\n      Student's t-test)\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 to 30 cells per group\n  expected:\n  - quantity: 4-phasic, F-F0 at end of recording\n    value: 20.8\n    tolerance: 2.0\n    unit: a.u.\n  - quantity: 8-phasic, F-F0 at end of recording\n    value: 6.9\n    tolerance: 1.6\n    unit: a.u.\n  - quantity: 8-phasic with 5-us delays, F-F0 at end of recording\n    value: 25.4\n    tolerance: 2.8\n    unit: a.u.\n  criterion: Tolerances are the paper's s.e. Per cell F-F0 at the end of recording (O10). Each\n    bipolar group is compared with the unipolar group by an unpaired two-sided Student's t-test\n    (Methods 2.4, applied to single cells as a reading; Welch's form is a variant). Reproduced when,\n    under one reading of O10, all three means are within tolerance and all three tests give\n    p < 0.001. Partially reproduced when the tests hold but a mean is outside tolerance.\n- id: fig4-twenty-fold-cancellation\n  statement: The 8-phasic signal with no delays causes about 20-fold weaker electroporation than a\n    single unipolar pulse and is the most efficient at cancellation; the 4-phasic signal and the\n    delayed 8-phasic signal cancel 4 to 5-fold.\n  source: Figure 4 legend; Results 3.1, paragraph 2; Results 3.4, paragraph 1\n  quote: Note that applying the 8-phasic bipolar signal with no inter-phase delays caused about\n    20-fold weaker electroporation than a single unipolar pulse\n  datasets:\n  - \"000686\"\n  - \"000875\"\n  - \"001025\"\n  - \"001027\"\n  - \"001028\"\n  depends_on:\n  - fig4-unipolar-strongest\n  - fig4-bipolar-weaker\n  expected:\n  - quantity: unipolar over 8-phasic, F-F0 at end of recording\n    value: 20\n    tolerance: 2\n  - quantity: unipolar over 4-phasic, and over delayed 8-phasic (range 4 to 5, widened by 10% of\n      each bound)\n    value: 4.55\n    tolerance: 0.95\n  criterion: Ratios of group means at the end of recording (O10). Results 3.4 gives the other two\n    signals as \"4-5-fold, Fig. 4\"; the paper's own means give 18.3 for the 8-phasic signal, 6.1 for\n    the 4-phasic and 5.0 for the delayed 8-phasic, so its 4-phasic value is outside its own range.\n    Reproduced when, under one reading, the 8-phasic ratio is within 18 to 22, is the largest of the\n    three, and the other two ratios are within 3.6 to 5.5. Partially reproduced when the 8-phasic\n    ratio is within tolerance and the largest but another ratio is outside 3.6 to 5.5; the paper's\n    6.1 is reported beside the result.\n- id: fig5a-trains-stronger\n  statement: Without rotation, 40 unipolar trains from e1 cause much stronger electroporation\n    throughout the array than 40 Packet 2 packets started from e1, and the uptake after trains\n    follows the field strength distribution.\n  source: Results 3.2, paragraph 1; Figure 5A\n  quote: The lack of cancellation caused a much stronger electroporation throughout the array, and\n    the distribution of YP uptake expectedly followed the electric field strength distribution in\n    Fig. 3C .\n  datasets:\n  - \"000686\"\n  criterion: Along the e1 to e3 diagonal (Fig. 5A legend), Packet 2 at 6.4 kV, n = 4 to 5 dishes,\n    under O1, O3, O6 and O7. \"Throughout\" is read at the e1 end, the center and the e3 end. Reproduced\n    when the train mean exceeds the packet mean at all three places by unpaired two-sided Student's\n    t-tests at p < 0.05 (Methods 2.4), and the train profile falls from the e1 end to the center, as\n    the field of Fig. 3C does with distance from the energized electrode, by the same test (O8). The\n    paper gives no test of the profile's shape; the full train profile is shown.\n- id: fig5a-packet-center-enhanced\n  statement: Without rotation, Packet 2 enhances electroporation in the center of the array despite\n    the weakening of the field with distance from e1, but uptake near e1 stays stronger than in the\n    center.\n  source: Results 3.2, paragraph 1; Figure 5A\n  quote: In contrast, Packet 2 enhanced electroporation in the center of the array, despite gradual\n    weakening of the electric field with distance from e1. However, the bipolar cancellation only\n    partially offset the electric field weakening, and electroporation near e1 remained stronger than\n    in the center.\n  datasets:\n  - \"000686\"\n  depends_on:\n  - fig5a-trains-stronger\n  criterion: The 40-packet profile along the e1 to e3 diagonal (Fig. 5A), under O1, O3, O6, O7 and O8.\n    \"Enhanced in the center\" has two readings the sentence allows, (a) a central peak, the center\n    above the trough between the center and the e1 end (O9) by a two-sided Student's t-test at\n    p < 0.05; (b) relative to the trains, the center over e1-end ratio higher for packets than for\n    trains by an unpaired t-test on per-dish ratios at p < 0.05. Reproduced when (a) or (b) holds,\n    under the rule for readings of the opening comment, and the e1-end value exceeds the center\n    value of the packet profile by the same test. Partially reproduced when only one of the two\n    parts holds.\n- id: fig5b-rotation-center-peak\n  statement: With rotation (1P x 40), Packet 2 smears the effect at the perimeter and brings out a\n    remote effect in the center, while the same rotation of unipolar trains (1T x 40) leaves a void\n    of electroporation in the center.\n  source: Results 3.2, paragraph 2; Figure 5B\n  quote: Rotation with Packet 2 “smeared” the electroporation effect at the perimeter and emphasized\n    the remote effect in the center. This remote effect contrasted with a void of electroporation in\n    the center when the pulse train was applied in the same manner instead of the packet.\n  datasets:\n  - \"000686\"\n  criterion: Profiles averaged across both diagonals (Fig. 5B legend), n = 4 to 5, under O1, O3, O4,\n    O6, O7 and O8. Reproduced when the 1P x 40 center exceeds its trough (O9) by a two-sided\n    Student's t-test at p < 0.05, and the 1T x 40 profile shows a void in the center. The paper does\n    not define a void; readings (a) the 1T x 40 center below its most peripheral value by the same\n    test; (b) the center ROI is the lowest point of the 1T x 40 mean profile.\n- id: fig5c-normalized-contrast\n  statement: Normalized to the most peripheral ROI (100%), rotated Packet 2 and rotated trains show\n    sharply different spatial distributions, the packet's center being relatively high and the\n    trains' relatively low.\n  source: Results 3.2, paragraph 2; Figure 5C\n  quote: The striking difference in the spatial distribution of electroporation between the CANCAN\n    and control treatments is appreciated best by comparing the normalized fluorescence data, when\n    the emission intensity in the most peripheral (closest to the electrode) ROI is taken as 100% (\n    Fig. 5C ).\n  datasets:\n  - \"000686\"\n  depends_on:\n  - fig5b-rotation-center-peak\n  criterion: The paper prints no number for Fig. 5C. Same data as Fig. 5B in % of the most\n    peripheral ROI (O4, O5), under O1, O3, O6 and O7. Reproduced when the normalized center of\n    1P x 40 exceeds that of 1T x 40 by an unpaired two-sided Student's t-test at p < 0.05 on per-dish\n    values. Both normalized centers are reported, and whether the 1P x 40 value is above 100%.\n- id: fig6a-more-packets-more-uptake\n  statement: Raising the total number of rotated Packet 2 packets from 4 (1Px4) to 20 (5Px4) and\n    40 (10Px4) strongly raises YP uptake throughout the array, and a central peak is discernible\n    for every treatment.\n  source: Results 3.3, paragraph 1; Figure 6A\n  quote: Increasing the total number of applied packets from 4 to 20 and 40 profoundly enhanced the\n    electroporative YP dye uptake throughout the electrode array ( Fig. 6A ). The peak of\n    electroporation in the center was clearly discernable for all tested treatments.\n  datasets:\n  - \"000875\"\n  criterion: In a.u., n = 3 to 4 dishes (Fig. 6 legend), under O1 to O4, O6 to O9 and O11.\n    \"Throughout\" is read at the most peripheral ROI, the trough and the center. Reproduced when at\n    all three places the means rise from 4 to 20 to 40 packets and 40 exceeds 4 by an unpaired\n    two-sided Student's t-test at p < 0.05, and for each treatment the center exceeds the trough by\n    the same test. Partially reproduced when the rise holds at one or two of the places.\n- id: fig6b-peak-relative-to-periphery\n  statement: The central peak is almost twofold brighter than the periphery for 1Px4, and about the\n    same as the periphery for 5Px4 and 10Px4.\n  source: Results 3.3, paragraph 1; Figure 6B\n  quote: Its brightness was almost twofold higher than at the periphery for a single packet was\n    applied 4 times from different directions, or about the same as at the periphery for the rotation\n    of 5 and 10 packets ( Fig. 6B ).\n  datasets:\n  - \"000875\"\n  expected:\n  - quantity: normalized center, 1Px4\n    value: 200\n    tolerance: 20\n    unit: \"%\"\n  - quantity: normalized center, 5Px4\n    value: 100\n    tolerance: 10\n    unit: \"%\"\n  - quantity: normalized center, 10Px4\n    value: 100\n    tolerance: 10\n    unit: \"%\"\n  criterion: Center in % of the most peripheral ROI, under O1 to O7. \"Almost twofold\" is taken as\n    200% with the default 10% tolerance. Reproduced when, under one combination of readings, all\n    three values are within tolerance. Partially reproduced when the 1Px4 value is within tolerance\n    and above both others.\n- id: fig6-trough-half-of-center\n  statement: For all three packet numbers, the least affected area between the center and the\n    electrodes shows about 2-fold lower fluorescence than the center.\n  source: Results 3.3, paragraph 1; Figure 6\n  quote: Interestingly, the least affected area of the cell monolayer (between the center and the\n    electrodes) showed about 2-fold lower fluorescence intensity than in the center for all the\n    treatments.\n  datasets:\n  - \"000875\"\n  expected:\n    quantity: center over trough, each of 1Px4, 5Px4 and 10Px4\n    value: 2\n    tolerance: 0.2\n  criterion: Trough as O9, center as O3, under O1, O2, O6 and O7. Reproduced when, under one\n    combination of readings, the ratio is within 1.8 to 2.2 for all three treatments. Partially\n    reproduced when it is within tolerance for one or two and above 1 for all.\n- id: fig6-peak-narrower\n  statement: The central peak becomes narrower with more packets.\n  source: Results 3.3, paragraph 1; Figure 6\n  quote: Also, the central peak appeared narrower (sharper) with increasing the number of packets.\n  datasets:\n  - \"000875\"\n  criterion: The paper defines no width (the Discussion names the width or sharpness of the remote\n    peak as a parameter, without a definition). Readings (a) full width of the central peak at half\n    its height above the trough (O9), on the mean normalized profile; (b) the distance between the\n    two troughs on either side of the center; each also on the LOESS fit (O7). Reproduced when the\n    width falls from 1Px4 to 5Px4 to 10Px4; partially reproduced when 10Px4 is narrower than 1Px4\n    but 5Px4 is out of order. The rule for readings of the opening comment applies.\n- id: fig7a-amplitude-scales-uptake\n  statement: With 1Px4 in the small array, raising the first-pulse amplitude from 2.4 to 5.6 kV\n    raises YP fluorescence 15.5 times at the most peripheral point, 16.2 times half-way to the\n    center and 16.8 times in the center.\n  source: Results 3.3, paragraph 2; Figure 7A\n  quote: For example, when the first pulse amplitude was increased from 2.4 to 5.6 kV ... YP\n    fluorescence increased 15.5 times at the most peripheral point; 16.2 times half-way to the\n    center; and 16.8 times in the center ( Fig. 7A ).\n  datasets:\n  - \"001025\"\n  expected:\n  - quantity: 5.6 kV over 2.4 kV, most peripheral ROI\n    value: 15.5\n    tolerance: 1.55\n  - quantity: 5.6 kV over 2.4 kV, half-way to the center\n    value: 16.2\n    tolerance: 1.62\n  - quantity: 5.6 kV over 2.4 kV, center\n    value: 16.8\n    tolerance: 1.68\n  criterion: Ratios of the mean intensities over dishes (n = 3; dishes are not paired across\n    voltages, Methods 2.1) at the most peripheral ROI (O4), the ROI nearest half the distance from\n    the center to it, and the center (O3), under O1, O2, O6 and O7. Background (O6) changes ratios\n    this large, so both readings are run. Reproduced when, under one combination of readings, all\n    three ratios are within tolerance. Partially reproduced when one or two are.\n- id: fig7b-targeting-independent-of-amplitude\n  statement: Normalized to the most peripheral ROI, the profiles for different amplitudes fully\n    overlap; amplitude changes the degree of electroporation but not its spatial distribution.\n  source: Results 3.3, paragraph 2; Figure 7B\n  quote: In contrast, changing nsEP amplitude affected the degree of electroporation but not its\n    spatial distribution ( Fig. 7 ). ... When the YP emission was normalized to the most peripheral\n    ROI, the data for different nsEP amplitudes fully overlapped ( Fig. 7B ).\n  datasets:\n  - \"001025\"\n  criterion: A claim of absence, for which the paper reports no test; it is judged on the test\n    Methods 2.4 names, an unpaired two-sided Student's t-test at p < 0.05, with no correction, as\n    the paper applies none. Small array, 1Px4, every voltage of Fig. 7A and B (n = 3 each; the\n    voltages between 2.4 and 5.6 kV are printed only in the figure and are taken from the dataset).\n    Per-dish normalized values (O5 a) at the center and at the half-way ROI of\n    fig7a-amplitude-scales-uptake are compared between every pair of voltages, under O1 to O4, O6\n    and O7. Reproduced when no pair differs; not reproduced when any does. The differences in\n    percentage points and their p-values are given either way; a test over all ROIs and the\n    error-bar rule of Methods 2.4 are shown as variants.\n- id: fig7cd-holds-for-large-array\n  statement: The independence of the normalized distribution from amplitude also holds when\n    rotating multiple packets (10Px4) in the larger array.\n  source: Results 3.3, paragraph 2; Figures 7C and 7D\n  quote: The findings held true for rotating multiple packets and when using the larger array ( Fig.\n    7C and D ). Overall, our results show that NG-CANCAN targeting of electroporation does not\n    depend on nsEP amplitude, at least within the studied amplitude range.\n  datasets:\n  - \"001025\"\n  criterion: As fig7b-targeting-independent-of-amplitude, on the large array with 10Px4 (Fig. 7C\n    and D, n = 3), with the same test, places and rule. The voltages are not given in the text and\n    are taken from the dataset (O11). The rise of a.u. values with voltage at the three places is\n    reported as well.\n- id: discussion-independent-of-array-size\n  statement: Remote targeting, within the studied limits, depends neither on pulse amplitude nor on\n    array size, so findings from small arrays can be extrapolated to larger inter-electrode\n    distances.\n  source: Discussion, paragraph 5; Figure 7\n  quote: the remote targeting, at least within studied limits, did not depend on either the electric\n    pulse amplitude or array size ( Fig. 7 ). We infer that findings from small electrode arrays\n    can be extrapolated to larger inter-electrode distances.\n  datasets:\n  - \"001025\"\n  depends_on:\n  - fig7b-targeting-independent-of-amplitude\n  - fig7cd-holds-for-large-array\n  criterion: The paper's evidence is Fig. 7, where the small array received 1Px4 and the large\n    array 10Px4, and Fig. 6B reports that packet number alone changes the normalized center; no\n    comparison in the paper isolates array size, and it names no test for it. The claim is judged\n    as the Discussion rests it, on amplitude independence in both arrays. Reproduced when\n    fig7b-targeting-independent-of-amplitude and fig7cd-holds-for-large-array are both\n    reproduced. The normalized profiles of the two arrays, on distance as a fraction of the\n    measured half-diagonal, are shown side by side, with the packet confound stated.\n- id: fig8a-equal-center-uptake\n  statement: Packets 1, 2 and 3 at 4 kV, rotated one cycle (1Px4), give the same YP uptake in the\n    center of the array, 215 to 235 a.u.\n  source: Results 3.4, paragraph 2; Figure 8A\n  quote: All packets produced the same YP uptake in the center (215–235 a.u.)\n  datasets:\n  - \"001027\"\n  expected:\n    quantity: center YP intensity, each of Packets 1, 2 and 3 (range 215 to 235, widened by 10% of\n      each bound)\n    value: 226\n    tolerance: 32.5\n    unit: a.u.\n  criterion: Center (O3) in a.u., n = 3 to 4, under O1, O2, O6, O7 and O11. The equality is a claim\n    of absence, judged on the test Methods 2.4 names, an unpaired two-sided Student's t-test at\n    p < 0.05 between each pair of packets. Reproduced when, under one reading, the three means are\n    inside 193.5 to 258.5 a.u. and no pair differs. Not reproduced when a pair differs; partially\n    reproduced when no pair differs but a mean is outside the range. Effect sizes are given either\n    way.\n- id: fig8a-more-uptake-near-electrodes\n  statement: Packets 1 and 3 cause much more YP uptake near the electrodes (250 to 350 a.u.) than\n    Packet 2 (about 120 a.u.), p < 0.01.\n  source: Results 3.4, paragraph 2; Figure 8A\n  quote: but Packets 1 and 3 caused drastically more YP uptake near the electrodes (250–350 a.u. vs\n    ~120 a.u. for packet 1, p<0.01, Fig. 8A )\n  datasets:\n  - \"001027\"\n  statistics:\n  - about: Packets 1 and 3 against Packet 2, near the electrodes\n    test: two-sided Student's t-test (Methods 2.4)\n    p: 0.01\n    p_relation: \"<\"\n    n: 3 to 4 experiments per packet\n  expected:\n  - quantity: most peripheral ROI, Packets 1 and 3 (range 250 to 350, widened by 10% of each bound)\n    value: 305\n    tolerance: 80\n    unit: a.u.\n  - quantity: most peripheral ROI, Packet 2\n    value: 120\n    tolerance: 12\n    unit: a.u.\n  criterion: The text prints \"~120 a.u. for packet 1\", which its own clause contradicts (Packets 1\n    and 3 are the 250 to 350 group); it is read as Packet 2, which also fits Fig. 8B (about 226\n    over 120 is near 183%). \"Near the electrodes\" is the most peripheral ROI (O4), under O1, O2, O6\n    and O7. Reproduced when, under one reading, Packets 1 and 3 are inside 225 to 385 a.u., Packet 2\n    within tolerance, and each of Packets 1 and 3 exceeds Packet 2 by an unpaired two-sided\n    Student's t-test at p < 0.01. Partially reproduced when the tests hold but values are outside.\n- id: fig8b-packet2-best-targeting\n  statement: Normalized to the most peripheral ROI, YP emission in the center is 183% for Packet 2\n    and drops to 83% for Packet 3 and 74% for Packet 1.\n  source: Results 3.4, paragraph 2; Figure 8B\n  quote: The superiority of Packet 2 for CANCAN targeting is highlighted by the drop of normalized\n    YP emission in the center from 183% for Packet 2 to 83% and 74% for Packets 3 and 1, respectively\n    ( Fig. 8B ).\n  datasets:\n  - \"001027\"\n  expected:\n  - quantity: normalized center, Packet 2\n    value: 183\n    tolerance: 18.3\n    unit: \"%\"\n  - quantity: normalized center, Packet 3\n    value: 83\n    tolerance: 8.3\n    unit: \"%\"\n  - quantity: normalized center, Packet 1\n    value: 74\n    tolerance: 7.4\n    unit: \"%\"\n  criterion: Center (O3) in % of the most peripheral ROI (O4, O5), under O1, O2, O6 and O7. Reproduced\n    when, under one combination of readings, all three values are within tolerance. Partially\n    reproduced when Packet 2 is above 100% and Packets 1 and 3 below it but a value is outside\n    tolerance.\n- id: fig8-cancellation-predicts-targeting\n  statement: The bipolar signal with the strongest cancellation between two electrodes (8-phasic,\n    Fig. 4) gives the most efficient remote targeting in the quadrupole (Packet 2, Fig. 8).\n  source: Discussion, paragraph 3; Results 3.4, paragraphs 1 and 2; Figures 4 and 8\n  quote: Three packets for CANCAN targeting were designed to produce three types of bipolar signals\n    near electrodes and we showed that, indeed, the strongest bipolar cancellation has led to the\n    most efficient remote targeting ( Figs. 4 and 8 ).\n  datasets:\n  - \"001027\"\n  depends_on:\n  - fig4-twenty-fold-cancellation\n  - fig8b-packet2-best-targeting\n  criterion: Results 3.4 matches the signals to the packets (4-phasic to Packet 1, 8-phasic to\n    Packet 2, delayed 8-phasic to Packet 3). Reproduced when the signal with the largest\n    unipolar-over-bipolar ratio in Fig. 4 corresponds to the packet with the highest normalized\n    center in Fig. 8. The paper claims only the top match; the order of the other two is reported\n    (the paper's own numbers give Packet 1 more cancellation, 6.1 against 5.0, but less targeting,\n    74% against 83%). Blocked as data_missing when the Fig. 4 data are in no dataset.\n- id: fig9a-gap-reduces-periphery-more\n  statement: With the large array lifted 1, 2 and 3 mm above the monolayer, YP emission near the\n    electrodes falls 2.4, 6.4 and 9 times against electrodes touching the cells, while in the center\n    it falls only 1.02, 1.4 and 3.8 times.\n  source: Results 3.5, paragraph 1; Figure 9A\n  quote: Specifically, YP emission near the electrodes decreased 2.4, 6.4, and 9 times with 1-, 2-\n    and 3-mm gaps (as compared to electrodes being in the same plane with cells); in the center, it\n    decreased just 1.02, 1.4, and 3.8 times, respectively.\n  datasets:\n  - \"001028\"\n  expected:\n  - quantity: 0 mm over 1 mm, near electrodes\n    value: 2.4\n    tolerance: 0.24\n  - quantity: 0 mm over 2 mm, near electrodes\n    value: 6.4\n    tolerance: 0.64\n  - quantity: 0 mm over 3 mm, near electrodes\n    value: 9\n    tolerance: 0.9\n  - quantity: 0 mm over 1 mm, center\n    value: 1.02\n    tolerance: 0.102\n  - quantity: 0 mm over 2 mm, center\n    value: 1.4\n    tolerance: 0.14\n  - quantity: 0 mm over 3 mm, center\n    value: 3.8\n    tolerance: 0.38\n  criterion: Ratios of the mean intensities over dishes (n = 3 to 4), 0 mm over each gap. \"Near the\n    electrodes\" is the most peripheral ROI (Fig. 9B legend, \"measurements most distant from the\n    center\"; O4); center as O3; under O1, O2, O6 and O7. Reproduced when, under one combination of\n    readings, all six ratios are within tolerance. Partially reproduced when at every gap the\n    near-electrode ratio exceeds the center ratio but some values are outside tolerance.\n- id: fig9b-gap-boosts-targeting\n  statement: The faster fading near the electrodes raises targeting efficiency (center over\n    periphery) to as much as 600% with a 2-mm gap.\n  source: Results 3.5, paragraph 1; Figure 9B\n  quote: Such disproportionally faster fading of the effect near electrodes boosted the CANCAN\n    targeting efficiency (measured as a ratio of the effect in the center and at the periphery) to as\n    much as 600% for the 2-mm gap ( Fig. 9B ).\n  datasets:\n  - \"001028\"\n  depends_on:\n  - fig9a-gap-reduces-periphery-more\n  expected:\n    quantity: normalized center, 2-mm gap\n    value: 600\n    tolerance: 60\n    unit: \"%\"\n  criterion: Center (O3) in % of the most peripheral ROI (O4, O5), under O1, O2, O6 and O7.\n    Reproduced when, under one combination of readings, the 2-mm value is within 540 to 660% and\n    is the largest of the four distances (\"as much as\"). Partially reproduced when it is within\n    tolerance but another distance is higher. The 0, 1 and 3 mm values are reported.\n- id: fig9c-restricted-to-center\n  statement: With the electrodes placed above the monolayer, electroporation is restricted almost\n    exclusively to the center of the array.\n  source: Results 3.5, paragraph 1; Figure 9C\n  quote: Consistent with these measurements, YP fluorescence images in Fig. 9C show that\n    electroporation is restricted almost exclusively to the remote target (center) when electrodes\n    are placed above the cell monolayer.\n  datasets:\n  - \"001028\"\n  criterion: The paper shows sample images and gives no measure. Read on the profiles, under O1 to\n    O9. Reproduced when, at each of 1, 2 and 3 mm, the center exceeds the most peripheral ROI by a\n    two-sided Student's t-test at p < 0.05 (O8), and the center is the highest point of the mean\n    profile. The normalized profiles are shown.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/pakhomov-2023.yaml paper/10.1016-j.bioelechem.2023.108437.txt; python -c "import yaml;d=yaml.safe_load(open('claims/pakhomov-2023.yaml'));c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; grep -n "—\|rather" claims/pakhomov-2023.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/pakhomov-2023.yaml`. The quote checker passes: 24 claims, 24 quotes, 0 problems. Nothing is committed.

**Text read:** the accepted author manuscript in PubMed Central (PMC10247516), not the version of record. It has the full Methods (2.1 to 2.4), Results, Discussion and the legends of Figs. 1 to 9. The paper has no supplement and links no code or data deposit, so no repository was read. No PDF was supplied, so no figure was read.

**Claims:**
- 24 claims, all with quotes and all with criteria; 12 have expected values.
- 2 have statistics: the bipolar signals against the single unipolar pulse in Fig. 4 (p < 0.001), and Packets 1 and 3 against Packet 2 near the electrodes in Fig. 8 (p < 0.01).
- Where a finding was the same, I reused the id from the old file for the dataset that holds that figure.

**Which claims rest on which dataset** (from the dataset titles):
- 000686: Fig. 5
- 000875: Fig. 6
- 001025: Fig. 7, plus the Discussion's claim that targeting does not depend on array size
- 001027: Fig. 8, plus the claim that cancellation predicts targeting
- 001028: Fig. 9

No title names the single-cell experiment of Fig. 4 or the field simulations of Fig. 3. Those 5 claims list all five datasets; the author checks each and blocks them as `data_missing` if none holds the data.

**Details the paper leaves open, with the readings named:**
- **O1, ROI layout:** the 92 or 224 ROIs cover (a) one diagonal or (b) both. The ROI width across the diagonal is not given; I named a square ROI (side equal to the spacing) and a band three spacings wide. Neither comes from the paper.
- **O2, diagonals:** for Figs. 6 to 9, (a) both diagonals averaged or (b) one diagonal.
- **O3, center:** (a) the ROI nearest the center, or (b) the mean of the two ROIs on either side of it.
- **O4, most peripheral ROI:** (a) the mean of the end ROIs, or (b) each half-diagonal taken to its own end ROI.
- **O5, normalization order:** (a) each dish normalized, then averaged, or (b) the mean profile normalized.
- **O6, background:** for monolayer images, (a) raw intensity, or (b) a background subtracted.
- **O7, raw or fitted:** (a) ROI means, or (b) the LOESS fit; spans 0.25 and 0.75 are standard choices, not the paper's.
- **O8, within-dish comparisons:** (a) paired or (b) unpaired t-test.
- **O9, trough between center and periphery:** (a) the mean of the two sides, or (b) each side.
- **O10, "end of recording" in Fig. 4:** (a) the last image, or (b) the mean of the last six images.
- **Undefined terms:**
  - "Enhanced in the center" in Fig. 5A: (a) a central peak, or (b) a higher center-to-e1 ratio than the trains.
  - The "void" in Fig. 5B: (a) the center below the periphery, or (b) the center as the profile minimum.
  - Peak width in Fig. 6: (a) full width at half height, or (b) the distance between the troughs.
- **Not stated at all:** the array used in Figs. 6 and 8, the voltage of Fig. 6, and the voltages of Fig. 7C and D. The author takes these from the data.
- **Test for the single cells:** Methods 2.2 names none. I used the two-sided Student's t-test that Methods 2.4 names, as a reading, with Welch's test as a variant.

**What the paper is missing or gets wrong:**
- **Fig. 4 and Fig. 3 data:** no dataset title names either. The simulation model is not deposited.
- **Fig. 7 voltages:** the voltages between 2.4 and 5.6 kV appear only in the figure.
- **"~120 a.u. for packet 1":** this contradicts its own sentence, which puts Packets 1 and 3 at 250 to 350 a.u. I read it as Packet 2, which also fits the 183% of Fig. 8B.
- **Fig. 4 fold values:** the paper's own means give 6.1-fold for the 4-phasic signal, outside its stated "4–5-fold". The claim keeps the stated range and reports 6.1 beside the result.
- **Array size:** Fig. 7 gave the small and large arrays different packet numbers (1Px4 against 10Px4), so no comparison in the paper isolates array size. The criterion states this confound.

## End of run

22 turns, 4 minutes, $1.85 at API prices, result: success.
