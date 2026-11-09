# 001193 · recorder · run 41366527878

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/001193/ claims/001193/; cat attempts/001193-zhu-2022-01.yaml; python tools/readme_row.py 001193; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001193' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (57.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b7e74b43-5c4e-4b9f-8626-0a83d1c8a07b/tool-results/bfqmw3y5t.txt

Preview (first 2KB):
docs/pilot-notes/001277-silkuniene-2025-01.md
docs/pilot-notes/001074-kalugin-2026-01.md
docs/pilot-notes/001065-dembrow-2024-01.md
docs/pilot-notes/001273-semenov-2025-01.md
docs/pilot-notes/001272-semenov-2025-01.md
claims/001193/:
10.1038-s41562-022-01334-6.yaml

transcripts/001193/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001193-zhu-2022-01.yaml | sed -n 20,400p; python tools/readme_row.py 001193; grep -n '"001193"' -A25 targets/dandisets.json | head -40
```

```
platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41284865063
outcomes:
- claim: participants
  outcome: partially_reproduced
  notebook: reproduce_zhu_2022.ipynb
  output: claim:participants
  notes: The dataset holds 10 distinct subjects (TC5, TC6, TC7, TC9, TC12, TC16 to TC20), each
    with 256 electrodes in two groups of 128, so the counts of participants (10) and electrodes per
    participant (256) match. The sex field is U (unknown) in every file, so the numbers of male and
    female participants (4 and 6 expected) are not determinable from the subjects; 4 and 6 appear
    only in the free-text subject description "chinese, 4 males and 6 females", copied into every
    file, which cannot be checked per subject. Ages are given only as the group range P19Y/P50Y,
    which matches the paper's 19 to 50 years but not the per-participant ages of Supplementary
    Table 1. No file says which task a participant did, so the 5 COM and 5 NL participants cannot
    be counted; the two recording periods (TC5 to TC12 in 2019-03 to 2019-05, TC16 to TC20 in
    2019-11) split the subjects 5 and 5, but nothing ties them to the task groups, and they are not
    used as such. No `measured` is given, as four of the six expected values cannot be measured.
    The criterion's partial outcome is "a subset of the participants with matching metadata"; here
    all participants are present but most of their metadata is missing, which the criterion does not
[... 388 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^| Dandiset\|^| Dataset\|^|---" README.md | head -3; grep -n "^- date\|^  kind\|^  reviewed\|agrees: false\|Round" attempts/001193-zhu-2022-01.yaml; for f in 001277-silkuniene-2025-01 001074-kalugin-2026-01 001065-dembrow-2024-01 001273-semenov-2025-01 001272-semenov-2025-01 001754-knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done
```

```
<persisted-output>
Output too large (42.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b7e74b43-5c4e-4b9f-8626-0a83d1c8a07b/tool-results/b3kgnqfxi.txt

Preview (first 2KB):
12:  kind: agent
266:- date: '2026-11-01'
267:  kind: agent
269:  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
569:    agrees: false
587:- date: '2026-11-02'
588:  kind: agent
590:  reviewed: Round 2. The full executed notebook of the first revision, the helper modules ifg_hga.py and keyword_frequency.py,
=== 001277-silkuniene-2025-01
# 001277, Silkuniene et al. 2025

One claim reproduced on the dataset (on an assumption), none partially, one not
reproduced and 15 blocked, 10 for missing data, three as
`methods_underspecified` and two for insufficient metadata. The first
verification round agreed with 14 of the 17 outcomes as they stood and the
second with all 17, and nothing was proposed after the second, so there was no
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in 001074-kalugin-2026-01 001273-semenov-2025-01 001754-knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; sed -n 560,700p attempts/001193-zhu-2022-01.yaml
```

```
<persisted-output>
Output too large (29.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b7e74b43-5c4e-4b9f-8626-0a83d1c8a07b/tool-results/bdqez16rd.txt

Preview (first 2KB):
=== 001074-kalugin-2026-01
# 001074, Kalugin et al. 2026

Three claims reproduced on the dataset (all three on an assumption), one
partially (on an assumption), seven not reproduced (all on an assumption) and
35 blocked, 13 for missing data and 22 for insufficient metadata; the nine
claims on labelled cells rest on the well order of the paper's code, and the
link claim `link-revision-well-order`, which the author added, reproduced. The
first verification round agreed with 44 of the 47 outcomes as they stood and
the second with all 47, and nothing was proposed after the second, so there was
no third round. It pins version 0.260928.0807, the most recent; the paper cites
none, and all three published versions hold the same 713 assets with the same
blobs. The paper, Kalugin, Soden et al., "Simultaneous, real-time tracking of
many neuromodulatory signals with multiplexed optical recording of sensors on a
micro-endoscope" in Neuron, describes MORSE probes, HEK-293T cells each
expressing one GRAB sensor in a hydrogel on a GRIN lens, calibrated by dipping
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b7e74b43-5c4e-4b9f-8626-0a83d1c8a07b/tool-results/bdqez16rd.txt"
}
```

```
1	=== 001074-kalugin-2026-01
2	# 001074, Kalugin et al. 2026
3	
4	Three claims reproduced on the dataset (all three on an assumption), one
5	partially (on an assumption), seven not reproduced (all on an assumption) and
6	35 blocked, 13 for missing data and 22 for insufficient metadata; the nine
7	claims on labelled cells rest on the well order of the paper's code, and the
8	link claim `link-revision-well-order`, which the author added, reproduced. The
9	first verification round agreed with 44 of the 47 outcomes as they stood and
10	the second with all 47, and nothing was proposed after the second, so there was
11	no third round. It pins version 0.260928.0807, the most recent; the paper cites
12	none, and all three published versions hold the same 713 assets with the same
13	blobs. The paper, Kalugin, Soden et al., "Simultaneous, real-time tracking of
14	many neuromodulatory signals with multiplexed optical recording of sensors on a
15	micro-endoscope" in Neuron, describes MORSE probes, HEK-293T cells each
16	expressing one GRAB sensor in a hydrogel on a GRIN lens, calibrated by dipping
17	into wells of ligands and then used in acute slices and in the CSF of awake
18	mice, and the dataset holds only the CaImAn traces and 3D masks of the probe
19	recordings. The claims were written from the author manuscript (PMC13568791)
20	with its supplement and the paper's code (pkalugin/kalugin-et-al-morse at
[... 392 more lines not kept]
```

**Agent**

Round 1 disagreed only on the stimuli claim; round 2 agreed with all 25. Now the README column meaning and the reports.

**Agent calls Bash**

```bash
cd  grep -n "(+" README.md | head -5; grep -n "^| Dataset\|^| Dandiset\|Reproduced" README.md | head -5; wc -c transcripts/001193/*-report.md; cat transcripts/001193/author-report.md
```

```
650 transcripts/001193/answer-report.md
 1547 transcripts/001193/author-answers-report.md
 4829 transcripts/001193/author-report.md
 4160 transcripts/001193/author-revise-1-report.md
 2760 transcripts/001193/author-revise-2-report.md
 3734 transcripts/001193/claims-check-report.md
 4245 transcripts/001193/claims-report.md
 6894 transcripts/001193/verifier-1-report.md
 5520 transcripts/001193/verifier-2-report.md
34339 total
I've finished steps 1 to 6 of the Author section for DANDI:001193 / doi:10.1038/s41562-022-01334-6. The entry passes its checks and runs from a clean environment in 52 s, and the handover package is built. Almost nothing could be tested: the dataset holds only one z-scored high-gamma matrix per block, and every analysis in the paper needs things it doesn't have. Nothing is committed.

The pinned version is 0.240921.1006. The paper cites no version, and this is the only published one. The draft has the same 40 files with the same checksums and differs only in version-naming fields, as the notebook shows.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| participants | partially_reproduced |
| task-structure, behaviour-response-time, fig1b-high-gamma-best-band, fig1c-responsive-in-ifg, fig1d-only-after-keyword, fig2b-violation-electrodes, fig2b-single-type, suppfig6a-half-split, suppfig6b-duration-metric, fig2c-euclidean-similarity, suppfig7a-com-overlap, suppfig7b-not-nonlinguistic, fig2de-no-spatial-separation, suppfig8b-individual-no-separation, fig2f-circuit-diameter, suppfig9-predict-from-corr, fig3-latency-values, fig3d-latency-differences, fig3-sync-latency-variability, fig3e-latency-not-location, suppfig10a-separable-400-700, suppfig10b-duration-differs, nl-low-frequency (23 claims) | blocked, data_missing |
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in claims claims-check answer author-answers verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat transcripts/001193/$f-report.md; done; sed -n 1,80p tools/readme_row.py | grep -n "+\|col\|header" | head -20
```

```
=== claims
I wrote `claims/001193/10.1038-s41562-022-01334-6.yaml`. The quote checker passes with 0 problems (24 claims, 24 quotes, 9 statistical values). Nothing is committed.

**Text read.** The version of record (Nature Human Behaviour 6, 1104–1111): main text, figure legends, Methods, reporting summary, and the Supplementary Information PDF (Table 1, Figs. 1–10, the stimulus sentence lists). The paper links no code; it is "available from the authors upon reasonable request", so no repository was read. The PDF could not be rendered here because poppler is not installed. So numbers printed only inside figure panels, such as the region counts of the Fig. 2b Venn diagram, are not used.

**Claims.** There are 24, all with quotes and all with a criterion. The task-structure count of 32 sentences per condition comes from the supplement's lists; no sentence of the text gives it, and the criterion says so.
- **Statistics:** 9 entries on 4 claims: the six pairwise latency p-values of Fig. 3d, the t-test against 25% chance in Suppl. Fig. 9, the ANOVA in Suppl. Fig. 10b, and the word-frequency t-test.
- **Coverage:** participants and task structure, behaviour, frequency band, IFG localisation, effects only after the keyword, the 58 violation electrodes, 49 single-type and 9 co-activated electrodes, the half-split and duration robustness checks, Euclidean similarity, the COM overlap, the non-linguistic control, absence of spatial separation (pooled and per participant), the 3.25 mm circuit diameter, prediction from correct sentences, latency values and their tests, latency not depending on location, the 400–700 ms classification peak, the duration differences, the low-frequency effect in the non-linguistic task, and keyword frequency matching.
- **Data:** one claim (word frequency) is `with_inputs`, using the corpus the paper names. The rest are `dataset`. The dandiset's description says it holds high-gamma activity only, so the band-comparison and low-frequency claims (Fig.
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 30,62p tools/readme_row.py; grep -n "version\|published" attempts/001193-zhu-2022-01.yaml | head; grep -n "title\|journal" claims/001193/*.yaml | head -5
```

```
key = datasets.key_of_folder(folder)
    shown = folder if datasets.split_key(key)[0] == "dandi" else datasets.label(key)
    return f"| [{shown}]({datasets.url(key)})"


def claim_kinds(dandiset: str, paper: str) -> dict[str, str]:
    for path in sorted((ROOT / "claims" / dandiset).glob("*.yaml")):
        data = yaml.load(path.read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
        if data.get("paper") == paper:
            return {c["id"]: "link" if c.get("kind") == "link" else c.get("data", "dataset")
                    for c in data["claims"]}
    raise SystemExit(f"error: no claims file for {dandiset} and {paper}")


def row(dandiset: str) -> str:
    found = attempt_of(dandiset)
    if found is None:
        raise SystemExit(f"error: no attempt on {datasets.label(datasets.key_of_folder(dandiset))}")
    record, entry_dir = found
    if record.get("deprecated"):
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p claims/001193/*.yaml; grep -n "questions\|001193.yaml" attempts/001193-zhu-2022-01.yaml | head
```

```
# Claims for Zhu, Xu, Lu, Hu et al. (2022), Nature Human Behaviour 6, 1104-1111, on dandiset 001193.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md, version pilot-10.
#
# Text read: the version of record (paper/10.1038-s41562-022-01334-6.txt, from the publisher PDF
# supplied by hand), with main text, figure legends, Methods and reporting summary, and the
# Supplementary Information PDF (Supplementary Table 1, Supplementary Figures 1 to 10 and the list of
# stimulus sentences). The Supplementary Excel file and the Source Data named in the paper were not
# supplied; nothing below needs them except where said. Figure panels were not viewed (the PDF could
# not be rendered here), so numbers printed only inside panels (the region counts of the Fig. 2b Venn
# diagram) are not used.
#
# Code. The paper links no code: "The completely developed code that operates on the full data set
# will be made available from the authors upon reasonable request" (Code availability). No repository
# was read. Every method detail below is from the Methods, the figure legends or the supplement.
#
# Which dataset. The dandiset's title and description say it holds high-gamma (70-150 Hz) ECoG activity
# from the paper's syntactic and semantic tasks in the inferior frontal gyrus, in NWB. Claims that need
# other frequency bands (Fig. 1b, Supplementary Figs. 3, 4 and 7c) cannot be tested on high-gamma alone.
#
[... 22 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001193-zhu-2022-01.md",
 "content": "# 001193, Zhu et al. 2022\n\nNo claim reproduced on the dataset, one partially and 23 blocked, all 23 for\nmissing data; the one claim on outside inputs, `stimuli-word-frequency`,\nreproduced on an assumption. The first verification round agreed with 24 of\nthe 25 outcomes as they stood and the second with all 25, and nothing was\nproposed after the second, so there was no third round. It pins version\n0.240921.1006, the only published one; the paper cites none, and the draft has\nthe same 40 files with the same checksums. The paper, Zhu, Xu, Lu, Hu et al.,\n\"Distinct spatiotemporal patterns of syntactic and semantic processing in human\ninferior frontal gyrus\" in Nature Human Behaviour, records high-density ECoG\nfrom ten native Mandarin speakers in awake brain tumour surgery, two\n128-channel grids each, while they read Chinese sentences that were correct or\nheld a syntactic or semantic violation at a keyword, and the dataset holds only\nthe z-scored high-gamma activity, one matrix per block. The claims were written\nfrom the version of record with its supplement; the paper links no code.\n`participants` is partial: the 10 subjects and the 256 electrodes each (two\ngroups of 128) match, but sex is U in every file, age is only the group range\nP19Y/P50Y and nothing says who did COM or NL, so four of the six expected\nvalues cannot be measured. `stimuli-word-frequency` uses no data of the\ndataset; the keywords of the supplement's lists were looked up in the bigram\ncounts of Jun Da's site, which the Methods name, and with the news and fiction\nsub-corpora pooled, per million bigrams, the CORR and SYN-C keywords have means\nof 31.568 and 29.955 per million and t(62) = 0.113, p = 0.910 (paper t(62) =\n0.11, P = 0.91), the one reading of six within the tolerances. The other 23\nclaims, from the task structure and behaviour to every electrode selection,\nlatency, spatial and band analysis, are blocked as `data_missing`. The author's\nfirst run blocked `stimuli-word-frequency` as other, for needing an unpinned\nweb corpus; round 1 disagreed, since its inputs are public, and it was tested\nin the revision, which also listed every object in all 40 files and tabulated\ntheir sizes. Round 2 asked that the assumption rest on the t statistic and the\ncommon ratio, which was done, and found sentences the outputs did not support\n(a standard deviation within 3e-5, a list of 16 of the 17 files with a start\ntransient, a run time of about a minute), all corrected. The author asked a\nreader nothing, so the answer and author-answers runs changed nothing; a reader\nquestion on the claim's \"Modern Chinese word frequency list\", which the site\ndoes not have, was added in the round-2 revision, after those runs. The\nauthor's run took about 15 minutes (07:28 to 07:43 UTC), its first duplicate\ncheck falsely matching many files on their shared start transient until it was\nfixed; the notebook ran in 52 s at first, 90 s after the author-answers run,\n67 s after round 1 and 84 s at the end. `tools/build_site.py` and\n`tools/site_assets/progress.js` were found modified and left untouched.\n\nNo file holds trial, word or keyword event times, condition labels (CORR,\nSYN-P, SYN-C, SEM, COM, NL-CORR, NL-VIO), button responses or the photodiode\nsignal; the stimulus, analysis and processing groups are empty and there is no\ntrials table or intervals, so no analysis of the paper can be repeated, though\nthe description says the dataset supports the paper's findings. Every file\nholds exactly 242,424 bytes beyond its uncompressed float32 ECoG data. The\nelectrode table has no coordinates and no anatomical labels, every location\nbeing \"unknown\", and the two electrode groups (Grid_1 and Grid_2) do not say\nwhich covers the IFG. Only the high-gamma activity is deposited, not the\nbroadband signal or any other band that Figure 1b and Supplementary Figures 3,\n4 and 7c use. Every subject has sex U and age P19Y/P50Y, with \"chinese, 4 males\nand 6 females\" as the subject description in every file, and nothing maps the\nsubject ids TC5 to TC20 to participants 1 to 10 of Supplementary Table 1 or\nsays which did the COM task and which the NL task. The ECoG series is stated in\nvolts, but every channel of every file has mean 0 (within 3e-6) and standard\ndeviation 1 (within 1e-4), z scores per channel and per block as the Methods\ndescribe. The stated rate of 400 Hz makes every block last 70 to 95 s, too\nshort for its trials, where at the Methods' 100 Hz for the high-gamma activity\nblocks last 282 to 381 s, and a weak spectral check at the 2 Hz word rate leans\nthe same way (34 of 40 files against 19 of 40). All 256 channels are present in\nevery file and nothing marks the bad channels or intervals the Methods exclude.\nIn the paper, the Methods say the SYN-P and SEM keywords are those of CORR, but\nsentences 3 and 11 differ (孩子 and 衣服 for 小孩 and 上衣), and with them the\nCORR mean would be 47.35 per million. A question is put to the paper's authors:\nwhich sub-corpus and which total the keyword frequencies divide by, the Methods\ngiving only the site's address.\n\nThe author's points on the protocol: outside data must be pinned, but the\nprotocol covers only inputs that are not public and not a public site that\ncannot be pinned, nor a claim that uses no data of the dataset; it has no\nguidance for a criterion where some expected values cannot be measured, while\n`measured` needs one number per expected value; it is unclear whether missing\nevent times or labels are `data_missing` or `metadata_insufficient`, and\n`data_missing` was used; and the clock check assumes trial tables exist.\n"
}
```

```
File created successfully at: docs/pilot-notes/001193-zhu-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -c "—\|rather" docs/pilot-notes/001193-zhu-2022-01.md
```

```
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
?? docs/pilot-notes/001193-zhu-2022-01.md
?? scripts
0
```

**Agent**

I wrote `docs/pilot-notes/001193-zhu-2022-01.md` and changed no other file. Nothing is committed. The untracked dotfiles and folders at the repository root were already there before this run, and I left them alone.

# 001193, Zhu et al. 2022

No claim reproduced on the dataset, one partially and 23 blocked, all 23 for
missing data; the one claim on outside inputs, `stimuli-word-frequency`,
reproduced on an assumption. The first verification round agreed with 24 of
the 25 outcomes as they stood and the second with all 25, and nothing was
proposed after the second, so there was no third round. It pins version
0.240921.1006, the only published one; the paper cites none, and the draft has
the same 40 files with the same checksums. The paper, Zhu, Xu, Lu, Hu et al.,
"Distinct spatiotemporal patterns of syntactic and semantic processing in human
inferior frontal gyrus" in Nature Human Behaviour, records high-density ECoG
from ten native Mandarin speakers in awake brain tumour surgery, two
128-channel grids each, while they read Chinese sentences that were correct or
held a syntactic or semantic violation at a keyword, and the dataset holds only
the z-scored high-gamma activity, one matrix per block. The claims were written
from the version of record with its supplement; the paper links no code.
`participants` is partial: the 10 subjects and the 256 electrodes each (two
groups of 128) match, but sex is U in every file, age is only the group range
P19Y/P50Y and nothing says who did COM or NL, so four of the six expected
values cannot be measured. `stimuli-word-frequency` uses no data of the
dataset; the keywords of the supplement's lists were looked up in the bigram
counts of Jun Da's site, which the Methods name, and with the news and fiction
sub-corpora pooled, per million bigrams, the CORR and SYN-C keywords have means
of 31.568 and 29.955 per million and t(62) = 0.113, p = 0.910 (paper t(62) =
0.11, P = 0.91), the one reading of six within the tolerances. The other 23
claims, from the task structure and behaviour to every electrode selection,
latency, spatial and band analysis, are blocked as `data_missing`. The author's
first run blocked `stimuli-word-frequency` as other, for needing an unpinned
web corpus; round 1 disagreed, since its inputs are public, and it was tested
in the revision, which also listed every object in all 40 files and tabulated
their sizes. Round 2 asked that the assumption rest on the t statistic and the
common ratio, which was done, and found sentences the outputs did not support
(a standard deviation within 3e-5, a list of 16 of the 17 files with a start
transient, a run time of about a minute), all corrected. The author asked a
reader nothing, so the answer and author-answers runs changed nothing; a reader
question on the claim's "Modern Chinese word frequency list", which the site
does not have, was added in the round-2 revision, after those runs. The
author's run took about 15 minutes (07:28 to 07:43 UTC), its first duplicate
check falsely matching many files on their shared start transient until it was
fixed; the notebook ran in 52 s at first, 90 s after the author-answers run,
67 s after round 1 and 84 s at the end. `tools/build_site.py` and
`tools/site_assets/progress.js` were found modified and left untouched.

No file holds trial, word or keyword event times, condition labels (CORR,
SYN-P, SYN-C, SEM, COM, NL-CORR, NL-VIO), button responses or the photodiode
signal; the stimulus, analysis and processing groups are empty and there is no
trials table or intervals, so no analysis of the paper can be repeated, though
the description says the dataset supports the paper's findings. Every file
holds exactly 242,424 bytes beyond its uncompressed float32 ECoG data. The
electrode table has no coordinates and no anatomical labels, every location
being "unknown", and the two electrode groups (Grid_1 and Grid_2) do not say
which covers the IFG. Only the high-gamma activity is deposited, not the
broadband signal or any other band that Figure 1b and Supplementary Figures 3,
4 and 7c use. Every subject has sex U and age P19Y/P50Y, with "chinese, 4 males
and 6 females" as the subject description in every file, and nothing maps the
subject ids TC5 to TC20 to participants 1 to 10 of Supplementary Table 1 or
says which did the COM task and which the NL task. The ECoG series is stated in
volts, but every channel of every file has mean 0 (within 3e-6) and standard
deviation 1 (within 1e-4), z scores per channel and per block as the Methods
describe. The stated rate of 400 Hz makes every block last 70 to 95 s, too
short for its trials, where at the Methods' 100 Hz for the high-gamma activity
blocks last 282 to 381 s, and a weak spectral check at the 2 Hz word rate leans
the same way (34 of 40 files against 19 of 40). All 256 channels are present in
every file and nothing marks the bad channels or intervals the Methods exclude.
In the paper, the Methods say the SYN-P and SEM keywords are those of CORR, but
sentences 3 and 11 differ (孩子 and 衣服 for 小孩 and 上衣), and with them the
CORR mean would be 47.35 per million. A question is put to the paper's authors:
which sub-corpus and which total the keyword frequencies divide by, the Methods
giving only the site's address.

The author's points on the protocol: outside data must be pinned, but the
protocol covers only inputs that are not public and not a public site that
cannot be pinned, nor a claim that uses no data of the dataset; it has no
guidance for a criterion where some expected values cannot be measured, while
`measured` needs one number per expected value; it is unclear whether missing
event times or labels are `data_missing` or `metadata_insufficient`, and
`data_missing` was used; and the clock check assumes trial tables exist.

## End of run

12 turns, 1 minutes, result: success.
