# wright-2019 · claims · run 42927202259

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper; grep -n "Reader" docs/protocol.md | head
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/protocol.md; cat claims/fouke-2025.yaml; cat paper/pag-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc paper/10.7554-elife.45013.txt; cat paper/10.7554-elife.45013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8676d42d-90c8-40af-a13c-ecc00a523947/tool-results/bw5f520wz.txt"
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
[... 990 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.45013.txt",
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.45013.txt",
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Reading the paper text now; its lines are long, so I'm wrapping it into a temp copy to read in chunks.

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.7554-elife.45013.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 450
}
```

```
File content (25470 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 400
}
```

```
1	DOI: 10.7554/elife.45013
2	Version: version of record, PMC6435320 (open access)
3	Source: europepmc fullTextXML
4	Stored: 2026-11-06
5	Extracted: JATS XML flattened
6	------------------------------------------------------------------------
7	Ventrolateral periaqueductal gray neurons prioritize threat probability over fear output
8	
9	Faced with potential harm, individuals must estimate the probability of threat and initiate an appropriate fear response. In the prevailing view, threat probability estimates are relayed to the 
10	ventrolateral periaqueductal gray (vlPAG) to organize fear output. A straightforward prediction is that vlPAG single-unit activity reflects fear output, invariant of threat probability. We recorded 
11	vlPAG single-unit activity in male, Long Evans rats undergoing fear discrimination. Three 10 s auditory cues predicted unique foot shock probabilities: danger (p=1.00), uncertainty (p=0.375) and 
12	safety (p=0.00). Fear output was measured by suppression of reward seeking over the entire cue and in one-second cue intervals. Cued fear non-linearly scaled to threat probability and cue-responsive 
13	vlPAG single-units scaled their firing on one of two timescales: at onset or ramping toward shock delivery. VlPAG onset activity reflected threat probability, invariant of fear output, while ramping 
14	activity reflected both signals with threat probability prioritized.
15	
16	## Introduction
17	
18	When confronted with potential harm, an estimate of threat probability must be made and followed by an appropriate fear response. The ventrolateral periaqueductal gray (vlPAG) has long been 
19	implicated in this fear response ( Fanselow, 1993 ; Kim et al., 1993 ; Liebman et al., 1970 ; Carrive et al., 1997 ; Bandler et al., 1985 ; Vianna et al., 2001 ; Arico et al., 2017 ; Assareh et al., 
20	2017 ). In the canonical fear circuit, threat probability estimates (the stored associative strength of cue and foot shock, for example a danger cue in Pavlovian
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 400,
 "limit": 330
}
```

```
400	was not significant ( Figure 4B ). Underscoring their specificity to cue onset, single-units were biased towards greater firing to danger in the first 1 s cue interval compared to the last interval, 
401	and there was no correlation between firing in the two epochs ( Figure 4C ). Examining relative cue firing for each Onset neuron in the first 1 s interval revealed the most common pattern to be: 
402	danger > uncertainty > safety (n = 14). This was the only pattern to contain more units than would be expected than chance ( Figure 4D ).
403	
404	Single-unit biases in Onset and Ramping populations. ( A ) Normalized firing to uncertainty (purple) vs. danger (red) during the first, 1 s cue interval is plotted for all Onset neurons (n = 29). 
405	Trendline, the square of the Pearson correlation coefficient (R 2 ) with associated p value (p), and sign test p value p(s) are shown for each plot. ( B ) Normalized firing to safety (blue) vs. 
406	uncertainty (purple) during the first, 1 s cue interval is plotted for Onset neurons (n = 29). ( C ) Normalized firing to danger in the first, 1 s cue interval vs. the last, 1 s cue interval is 
407	plotted for Onset neurons (n = 29). ( D ) Number of observed neurons (closed circle) vs shuffled distribution (median, 25 th percentile, 75 th percentile, lowest/highest non-outliers) shown for four 
408	most common firing patterns: danger > uncertainty > safety, danger > safety > uncertainty, safety > uncertainty > danger, and uncertainty > danger > safety. ( E ) Normalized firing to uncertainty 
409	(purple) vs. danger (red) during the last, 1 s cue interval is plotted for Ramping neurons (n = 14). ( F ) Normalized firing to safety (blue) vs. uncertainty (purple) during the last, 1 s cue 
410	interval is plotted for Ramping neurons (n = 14). ( G ) Normalized firing to danger in the first, 1 s cue interval vs. the last, 1 s cue interval is plotted for Ramping neurons (n = 14). ( H ) Number 
411	of observed neurons vs shuffled distrib
[... 318 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 730,
 "limit": 330
}
```

```
730	
731	Cat # PK-6106
732	
733	[1:200] in 0.05M PBS
734	
735	Chemical compound, drug
736	
737	Normal Rabbit Serum
738	
739	Vector Labs
740	
741	Cat # PK-6106
742	
743	1% in 0.05M PBS
744	
745	Chemical compound, drug
746	
747	Avidin
748	
749	Vector Labs
[... 310 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 1059,
 "limit": 160
}
```

```
1059	to observe possible neural activity during the delay period not driven by an explicit cue. A single session consisted of six danger trials, ten uncertainty no-shock trials, six uncertainty shock 
1060	trials, and ten safety trials. The order of trial type presentation was randomly determined by the behavioral program, and differed for each rat, each session. After the eighth session, rats were 
1061	removed from discrimination, given full food and received stereotaxic surgery. Following recovery, discrimination (identical to that described above) resumed with single-unit recording. Animals 
1062	received discrimination every other day with recording. After each discrimination session with recording, electrodes were advanced either 0.042 mm or 0.084 mm to record from new units during the 
1063	following session.
1064	
1065	## Histology
1066	
1067	Rats were deeply anesthetized using isoflurane and final electrode coordinates were marked by passing current from a 6 V battery through 4 of the 16 nichrome electrode wires. Rats were perfused with 
1068	0.9% biological saline and 4% paraformaldehyde in a 0.2 M Potassium Phosphate Buffered Solution. Brains were extracted and post-fixed in a 10% neutral-buffered formalin solution for 24 hr, stored in 
1069	10% sucrose/formalin and sectioned via microtome. All brains processed for light microscopy using anti-tryptophan hydroxylase immunohistochemistry (T8575, Sigma-Aldrich, St. Louis, MO) and a NovaRed 
1070	chromagen reaction (SK-4800, Vector Laboratories, Burlingame, CA) Sections were mounted, imaged using a light microscope and electrode placement was confirmed ( Paxinos and Watson, 2007 ).
1071	
1072	## Single-unit data acquisition
1073	
1074	Sixteen individual recording wires were bundled and soldered to individual channels of an Omnetics connector. The bundle was integrated into a microdrive permitting advancement in ~0.042 mm 
1075	increments. The microdrive was cemented on top of the skull and the Omnetics connec
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk 'NR>1218' $TMPDIR/p.txt | grep -v '^$' | awk 'length>25' | head -80; grep -n -i "github\|code availab\|source code\|data availab\|crcns\|Dryad\|supplementary file\|Transparent" $TMPDIR/p.txt | head
```

```
The regression output of greatest interest was the beta coefficient for each regressor (interval fear, total fear and probability), quantifying the strength (greater distance from zero = stronger) 
and direction (>0 = positive) of the predictive relationship between each regressor and single-unit firing. ANOVA, two-tailed dependent samples t-test, sign test and The Pearson correlation 
coefficient was used to analyze beta coefficients, exactly as described for normalized firing. An identical approach was used for the pairs analysis ( Figure 3 ) only now firing of the Ramping neuron 
was used as a regressor to predict firing of the paired Onset neuron. Beta coefficient (β) and significance of the predictive relationship ( p ) are reported.
## Threat probability tuning curve
Single-unit, linear regression was performed using the interval fear, total fear and probability regressor as above. Only now, nine separate regression analyses were performed in which the 
uncertainty component of the probability regressor was systematically varied from 0 to 1 in 0.125 increments (0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875 and 1.000). The result of primary 
interest was the mean beta coefficient for the probability regressor from each variant of regression, as plotted in Figure 5E/J .
A correlation matrix was created for the post-cue period for the Onset population (n = 29) as well as the Ramping population (n = 14). The periods of interest were the four, 500 ms intervals prior to 
shock presentation and the five, 500 ms intervals following shock. Starting with interval 1, The Pearson correlation coefficient (R 2 ) and associated p value was calculated by comparing the 
probability beta coefficient for each neuron to those for intervals 2–4 and 6–10. Most critical were the comparison with intervals 6–10, that permitted comparison of beta coefficients between 
pre-shock and post-shock periods. The same relationships were determined for each of the remaining intervals (
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL -m 30 http://mcdannaldlab.org/resources | sed 's/<[^>]*>/ /g' | tr -s ' \n' | head -c 3000; echo; curl -sL -m 30 -o /dev/null -w "%{http_code}\n" http://mcdannaldlab.org/resources
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for u in http://mcdannaldlab.org https://www.mcdannaldlab.org/resources https://www.mcdannaldlab.org "http://web.archive.org/web/2019/http://mcdannaldlab.org/resources"; do echo "== $u"; curl -sL -m 30 "$u" | sed 's/<[^>]*>/ /g' | grep -io "[^ ]*\(matlab\|\.m\b\|resource\|github\|download\)[^ ]*" | sort -u | head -20; done
```

```
<persisted-output>
Output too large (105.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8676d42d-90c8-40af-a13c-ecc00a523947/tool-results/brdpio9uk.txt

Preview (first 2KB):
== http://mcdannaldlab.org
Restricted\",\"hideTitle\":true,\"icon\":\"\",\"descriptionSEO\":\"\",\"metaKeywordsSEO\":\"\",\"pageTitleSEO\":\"\",\"underConstruction\":false,\"pageBackgrounds\":{\"desktop\":{\"custom\":true,\"ref\":{\"type\":\"BackgroundMedia\",\"metaData\":{\"schemaVersion\":\"2.0\",\"isPreset\":true,\"isHidden\":false,\"pageId\":\"imglb\",\"sig\":\"1hv-1839\"},\"color\":\"{color_16}\",\"alignType\":\"top\",\"fittingType\":\"fill\",\"scrollType\":\"fixed\",\"id\":\"dataItem-mqh0n0de\"},\"isPreset\":true},\"mobile\":{\"custom\":true,\"ref\":{\"type\":\"BackgroundMedia\",\"metaData\":{\"schemaVersion\":\"2.0\",\"isPreset\":true,\"isHidden\":false,\"pageId\":\"imglb\",\"sig\":\"1hv-1840\"},\"color\":\"{color_16}\",\"alignType\":\"top\",\"fittingType\":\"fill\",\"scrollType\":\"fixed\",\"colorOverlay\":\"\",\"colorOverlayOpacity\":0,\"id\":\"dataItem-mqh0n0de1\"},\"isPreset\":true,\"mediaSizing\":\"viewport\"}},\"translationData\":{\"uriSEOTranslated\":false},\"pageSecurity\":{\"requireLogin\":false,\"passwordDigest\":\"\",\"dialogLanguage\":\"\"},\"isLandingPage\":false,\"isMobileLandingPage\":false,\"isPopup\":false}]}","group":"","pages":{"expired-token":"wn685","reset-password":"r148l","access-restricted":"imglb"},"roleVariations":{}}},"urlMappings":null},"mpaNavigation":{"forceMpaNavigation":false,"isRunningInDifferentSiteContext":false},"ooiTpaSharedConfig":{"imageSpriteUrl":"https:\/\/static.parastorage.com\/services\/santa-resources\/resources\/viewer\/editorUI\/fonts.v19.png","wixStaticFontsLinks":["https:\/\/static.parastorage.com\/services\/fonts-data\/dist\/fonts.hz267ac7fkkfb3a18o8z.css","https:\/\/static.parastorage.com\/services\/fonts-data\/dist\/wixMadefor.j95mkaziqjnrn77aekr8.css","https:\/\/static.parastorage.com\/services
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL -m 30 "http://archive.org/wayback/available?url=mcdannaldlab.org/resources&timestamp=20190401"; echo; curl -sL -m 30 "http://web.archive.org/cdx/search/cdx?url=mcdannaldlab.org*&output=txt&limit=50&filter=statuscode:200" | awk '{print $2, $3}' | sort -u -k2 | head -50
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -m 60 "http://web.archive.org/web/20201025131136/http://mcdannaldlab.org/resources/" | sed 's/<[^>]*>/\n/g' | grep -v '^\s*$' | grep -iv "script\|function\|var \|{" | head -80; curl -sL -m 60 "http://web.archive.org/web/20201025131136/http://mcdannaldlab.org/resources/" | grep -o 'href="[^"]*"' | grep -iv "archive.org/static\|\.css\|\.js" | head -40
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8676d42d-90c8-40af-a13c-ecc00a523947/tool-results/bw5f520wz.txt",
 "offset": 1010,
 "limit": 210
}
```

```
1010	review and the complete methods will be available with that publication, which is: 
1011	Wright KM and McDannald MA. (2019); Ventrolateral periaqueductal gray 
1012	neurons prioritize threat probability over fear output.  eLife. 
1013	 
1014	Conditions for using the data 
1015	Publications created through usage of the data should cite the paper in which they are 
1016	first reported (Wright and McDannald, 2019; reference above) and also cite the dataset 
1017	using: 
1018	 
1019	Wright KM and McDannald MA. (2019); Ventrolateral periaqueductal gray singlesingle unit activity during multi-cue fear discrimination in rats. CRCNS.org. 
1020	http://dx.doi.org/10.6080/K0R49P0V 
1021	 
1022	 
1023	
1024	Page 2 of 6 
1025	Methods 
1026	Experimental Subjects 
1027	Ten adult male Long Evans rats (RRID:RGD_2308852) weighing 241-268g arrived from 
1028	Charles River Laboratories, Raleigh, NC on postnatal day 55. All rats were implanted 
1029	with drivable microelectrode bundles. Data are reported from 6 rats; 3 rats did not yield 
[... 187 more lines not kept]
```

**Agent**

Now I'll check the claims schema and the quote checker before writing.

**Agent calls Bash**

```bash
cd  ls schemas; sed -n 1,80p tools/claims_check.py; ls claims | head -50
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; ls papers/datasets | grep -i wright; cat papers/datasets/wright-2019.yaml 2>/dev/null; ls claims | grep -i crcns | head; grep -l "archive: crcns" claims/*.yaml | head -3
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; head -40 claims/deweese-2004.yaml
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^dataset:" claims/simmons-2026.yaml claims/bruno-2017.yaml; grep -n "^[a-z_]*:" claims/simmons-2026.yaml | head; grep -n "open\|readings" claims/simmons-2026.yaml | head -5
```

```
claims/simmons-2026.yaml:0
claims/bruno-2017.yaml:1
80:schema_version: 2
81:paper: doi:10.1126/sciadv.adq8840
82:claims:
770:checks:
8:# were opened to read Fig. 2B (the train runs from 2 to 4 s of a 6-s sweep), Fig. 3B (about 45
62:#    cell's percent change. Where the paper writes "mean", readings (a) and (b) only.
133:    the pre-pulse baseline or from the decaying first IPSC is open. Readings (a) second peak from
152:    sweep gives the basal rate; readings (a) 0 to 2 s, before the train; (b) 0 to 2 s and 4 to
390:    not said; readings (a) the control cells recorded alongside the shRNA experiments, as the
```

**Agent**

I have the findings mapped out. Before writing, I'm checking whether the paper fixes the nose-poke baseline window anywhere, since it decides the suppression ratio.

**Agent calls Bash**

```bash
cd  grep -o -i "[^.]*baseline[^.]*poke[^.]*\.\|[^.]*poke[^.]*baseline[^.]*\." paper/10.7554-elife.45013.txt | sort -u
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper never says which window the nose-poke baseline uses, so that stays open. I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/wright-2019.yaml",
 "content": "# Claims for Wright & McDannald (2019), eLife 8:e45013, \"Ventrolateral periaqueductal gray neurons\n# prioritize threat probability over fear output\", on CRCNS data set pag-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (Reader, version pilot-14).\n#\n# Text read: the version of record, PMC6435320 (open access), from the Europe PMC full-text JATS\n# XML as supplied under paper/ (10.7554-elife.45013.txt): main text, Materials and methods, the\n# legends of Figures 1 to 6 and of all figure supplements (Figure 1, supplements 1 to 6; Figure 2,\n# supplements 1 and 2; Figure 5, supplements 1 and 2), and the example regression input table of\n# the Methods. The paper has no other supplement. No PDF was supplied, so the values printed only\n# inside figures (the R2 and sign-test p-values of Figure 4, the F values of Figure 5, supplement\n# 1, the tuning curves of Figure 5E and 5J) could not be read; the claims on them are judged on\n# the tests the legends name.\n#\n# Code. The paper links one source of code, the lab website (\"Med Associates programs used for\n# behavior and MATLAB programs used for behavioral analyses are made freely available at our lab\n# website, http://mcdannaldlab.org/resources\"). On 2026-11-10 that address returned 404, and the\n# only Internet Archive capture (2020-10-25) of the page holds no files or links. No code was\n# read. The data set's description says it includes sample MATLAB scripts (a cube-building script,\n# population plots and a sample regression); these are files of the data set and were not read\n# here. Every method below comes from the paper's text.\n#\n# Data the paper used. Six adult male Long Evans rats (of ten implanted; three yielded no units\n# and one had a misplaced electrode), each with a drivable 16-wire bundle aimed at caudal vlPAG\n# (bregma -7.62 to -7.98). 88 recording sessions of fear discrimination, each of 32 trials with a\n# mean ITI of 3.5 min, in randomized order: six danger trials (shock p = 1.00), six uncertainty\n# shock and ten uncertainty omission trials (p = 0.375), ten safety trials (p = 0.00). Cues are\n# 10 s auditory motifs (click, phaser, trumpet, counterbalanced across rats); the foot shock (0.5\n# mA, 0.5 s) starts 2 s after cue offset on danger and uncertainty shock trials. Rats nose poke for\n# food on a VI-60 schedule throughout. 245 single units (Plexon, sorted offline), with spike times,\n# mean waveforms, and the timestamps of cues, shocks and nose pokes. The measured variables are\n# spike times, waveform half duration and amplitude ratio, baseline firing rate, and nose poke\n# rates, from which suppression ratios are computed. The data set, by its description, holds the\n# 245 units of the 88 sessions from these six rats, with per-unit firing, nose poke rates and\n# suppression ratios for the 32 trials, so it is meant to hold every experiment of the paper.\n#\n# Method details fixed by the paper (Materials and methods unless stated).\n# - Suppression ratio = (baseline poke rate - cue poke rate) / (baseline poke rate + cue poke\n#   rate), for the whole 10 s cue (total fear) or one 1 s interval (interval fear), per trial (the\n#   Methods regression table gives one total and one interval ratio per trial).\n# - Uncertainty shock and omission trials are collapsed for all cue-period analyses and split for\n#   the post-cue period (\"Population and single-unit firing analyses\").\n# - Cue-responsive screen: paired two-tailed t-test across a cue's trials of raw firing rate\n#   (spikes/s) in the 2 s before cue onset against the first 1 s cue interval, for each of the\n#   three cues, p < 0.017; an increase makes an Onset neuron. The remaining neurons are screened\n#   the same way with the last 1 s interval; those in the LFR cluster are the Ramping neurons.\n# - 100 ms firing for population ANOVAs: per neuron and trial type, mean rate in 100 ms bins from\n#   10 s before cue onset to 12 s after cue offset (320 bins), minus the trial type's mean 2 s\n#   pre-cue rate, then Z-scored across all trial types and bins of the neuron.\n# - Interval firing for t-tests, single-unit biases, pairs and regressions: per neuron, the\n#   differential firing in the interval of interest on each of the 32 trials, Z-scored across the\n#   32 trials, separately for each interval (1 s in the cue, 500 ms after it).\n# - Population ANOVAs are repeated measures over neurons (or sessions); the reported degrees of\n#   freedom fix the design, for example F(218, 6104) for cue (3) x bin (110 bins of 100 ms, 1 s\n#   before onset to the end of the 10 s cue) over 29 neurons, and F(132, 1716) for trial type (4)\n#   x bin (45 bins, the 5 s after cue offset without the five 100 ms bins of the shock) over 14.\n#   No sphericity correction is named; the uncorrected tests are the reading the integer degrees\n#   of freedom imply.\n# - Single-unit regression: per neuron and interval, ordinary least squares (MATLAB regress, with\n#   a constant) of interval Z firing over the 32 trials on interval fear, total fear and\n#   probability (1.00, 0.375, 0.00); after the cue, 500 ms intervals and no total fear regressor.\n#   Betas are compared across neurons by ANOVA (regressor x interval), paired two-tailed t-tests,\n#   single-sample t-tests against zero at p < 0.005 (Bonferroni for 10 tests, Figure 5D legend),\n#   sign tests and Pearson correlations.\n#\n# Details the paper leaves open, with the readings each criterion names.\n# 1. The nose poke baseline window of the suppression ratio is not stated. Readings (a) the 2 s\n#    before cue onset, the baseline the paper uses for firing; (b) the 10 s before cue onset, the\n#    length of the cue.\n# 2. A ratio with no pokes in baseline or cue (0/0). Readings (a) set to 0, as the 0.00 entries\n#    of the Methods regression table allow; (b) left out of means.\n# 3. A session's suppression ratio for a cue (Figure 1C, 1D, n = 88). Readings (a) the mean of the\n#    per-trial ratios; (b) the ratio of the session's mean baseline and cue rates.\n# 4. The baseline of the per-trial interval differential firing. Readings (a) the trial's own 2 s\n#    before cue onset; (b) the trial type's mean 2 s baseline, as for the 100 ms bins.\n# 5. The k-means features. The baseline firing rate is not defined (readings (a) the mean rate in\n#    the 2 s pre-cue baselines of all 32 trials; (b) the mean rate over the session); nor is\n#    feature scaling (readings (a) raw values; (b) each feature Z-scored). Initialization is a\n#    standard choice (MATLAB kmeans defaults, several replicates, fixed seed).\n# 6. Sign tests are two-sided unless the reading says otherwise; the paper does not say.\n# 7. Others are named in the claims they bear on (shuffles, sliding windows, nose poke cessation).\n#\n# Inconsistencies within the paper, noted for the author. The danger vs uncertainty first-interval\n# test of the Onset population is p = 9.70x10-5 in the Results and 9.70x10-4 in the Figure 2B\n# legend (t(28) = 4.54 gives about 1e-4). The Ramping first-interval uncertainty vs safety test is\n# p = 0.81 in the Results and 0.82 in the legend. The mean danger suppression ratio is 0.80 in the\n# Results and 0.83 in the Figure 2, supplement 2 legend.\n#\n# All claims use the data set's own recordings (data: dataset, the default).\nschema_version: 2\npaper: doi:10.7554/elife.45013\nclaims:\n- id: fig1c-total-suppression\n  statement: Over the 88 recording sessions, suppression ratio over the whole 10 s cue differs by\n    cue, high to danger (0.80), intermediate to uncertainty (0.53) and low to safety (0.03), and\n    each cue pair differs.\n  source: Results, first section, paragraph 2 (after Figure 1 supplements); Figure 1C\n  quote: Across all 88 recording sessions, these six rats showed excellent discriminative fear ...\n    high to danger, intermediate to uncertainty, and low to safety\n  statistics:\n  - about: cue effect, one-way ANOVA over danger, uncertainty and safety\n    test: ANOVA\n    statistic: F(2,174) = 592.00\n    p: 2.32e-78\n  - about: danger against uncertainty\n    test: paired t-test\n    statistic: t(87) = 12.36\n    p: 7.44e-21\n  - about: uncertainty against safety\n    test: paired t-test\n    statistic: t(87) = 20.85\n    p: 3.50e-35\n  expected:\n  - quantity: mean suppression ratio to danger, total cue\n    value: 0.80\n    tolerance: 0.08\n  - quantity: mean suppression ratio to uncertainty, total cue\n    value: 0.53\n    tolerance: 0.053\n  - quantity: mean suppression ratio to safety, total cue\n    value: 0.03\n    tolerance: 0.05\n  criterion: Per session (88, each counted once however many units it holds) and cue, the total\n    cue suppression ratio (Methods, Calculating suppression ratios), uncertainty trials collapsed.\n    Reproduced when, under one reading of details 1 to 3 of the opening comment, all three means\n    are within tolerance, the repeated-measures ANOVA of cue has p < 0.05 and both paired t-tests\n    have p < 0.05 in the reported direction; partially reproduced when the tests hold and a mean\n    is outside tolerance. The safety tolerance is 0.05, not 10%, because 10% of 0.03 is below the\n    printed precision; 0.05 is the tolerance of the uncertainty value. The 0.83 for danger in the\n    Figure 2, supplement 2 legend is reported against the same values.\n- id: fig1c-nonlinear-scaling\n  statement: Suppression scales non-linearly with shock probability. Uncertainty's shock\n    probability is closer to safety, but its mean suppression ratio is closer to danger.\n  source: Results, first section, paragraph 2\n  quote: While the foot shock probability associated with uncertainty was closer to safety ... the\n    mean suppression ratio to uncertainty was closer to danger\n  depends_on:\n  - fig1c-total-suppression\n  criterion: From the session means of fig1c-total-suppression. Reproduced when the mean ratio to\n    uncertainty exceeds the midpoint of the danger and safety means, under the reading that\n    claim matched on (under every reading if it matched none).\n- id: fig1d-interval-suppression\n  statement: Suppression ratios in each 1 s cue interval discriminate every cue pair in every\n    interval, with a cue effect and a cue x interval interaction.\n  source: Results, first section, paragraph 3; Figure 1D\n  quote: When the total cue period was divided into 10, 1 s intervals, discrimination was observed\n    in each interval and its pattern showed subtle change over cue presentation\n  statistics:\n  - about: cue effect, cue x interval ANOVA\n    test: ANOVA\n    statistic: F(2,174) = 489.40\n    p: 3.59e-72\n  - about: cue x interval interaction\n    test: ANOVA\n    statistic: F(18,1566) = 6.21\n    p: 5.90e-15\n  - about: danger against uncertainty, each interval\n    test: paired t-test\n    statistic: all t(87) > 3.00\n    p: 0.005\n    p_relation: \"<\"\n    corrected: Bonferroni for 10 tests\n  - about: uncertainty against safety, each interval\n    test: paired t-test\n    statistic: all t(87) > 7.00\n    p: 0.005\n    p_relation: \"<\"\n    corrected: Bonferroni for 10 tests\n  criterion: Per session and cue, the suppression ratio of each of the ten 1 s cue intervals\n    (readings of details 1 to 3). Reproduced when the two-way repeated-measures ANOVA has a cue\n    effect and a cue x interval interaction at p < 0.05 and, in all ten intervals, danger exceeds\n    uncertainty and uncertainty exceeds safety by paired t-tests at p < 0.005; partially\n    reproduced when the ANOVA holds and the pairs differ at p < 0.005 in at least eight intervals\n    each.\n- id: fig1s1a-nose-poke-rates\n  statement: Baseline nose poke rates do not differ between trial types, and poking falls from\n    baseline to cue for danger and uncertainty but not for safety.\n  source: Figure 1, figure supplement 1A\n  quote: Baseline nose poke rates did not differ between trial types and rats showed significant\n    reductions in poking to danger and uncertainty, but not safety\n  statistics:\n  - about: baseline against cue, per trial type\n    test: paired samples t-test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Per session (88) and trial type (danger, uncertainty shock, uncertainty omission,\n    safety), the mean baseline and cue poke rates (baseline readings of detail 1). Baseline against\n    cue is the paired t-test the legend names, at p < 0.05; reproduced for that part when danger\n    and both uncertainty types fall significantly and safety does not. The paper names no test for\n    baseline across trial types; the reading is a one-way repeated-measures ANOVA over the four\n    types at p < 0.05, with paired t-tests of each pair as a variant. The claim is reproduced when\n    both parts hold.\n- id: fig1s1b-sr-poke-correlation\n  statement: Suppression ratio and cue nose poke rate are significantly correlated across\n    sessions, particularly for danger and uncertainty.\n  source: Figure 1, figure supplement 1B\n  quote: The two measures were significantly correlated, particularly for danger and uncertainty\n  criterion: For each cue, the Pearson correlation over the 88 sessions of the total cue\n    suppression ratio and the cue poke rate (readings of details 1 to 3). Reproduced when the\n    correlation is negative with p < 0.05 for danger and for uncertainty; safety is reported.\n- id: fig1e-two-clusters\n  statement: K-means clustering (k = 2) of all 245 neurons on baseline firing rate, waveform half\n    duration and amplitude ratio splits them on baseline firing rate alone into a low firing rate\n    cluster of 199 and a high firing rate cluster of 46.\n  source: Results, vlPAG neurons are responsive at cue onset or ramp over cue presentation,\n    paragraph 1; Methods, K-means clustering; Figure 1E\n  quote: All neurons separated into one of two clusters purely on the basis of baseline firing rate\n    ... with majority of neurons falling into the low firing rate (LFR) cluster (n = 199) and the\n    remaining in the high firing rate (HFR) cluster (n = 46)\n  statistics:\n  - about: baseline firing rate by cluster\n    test: ANOVA\n    statistic: F(1,243) = 829\n    p: 0.001\n    p_relation: \"<\"\n  - about: amplitude ratio and duration by cluster\n    test: ANOVA\n    statistic: Fs < 0.2\n    p: 0.6\n    p_relation: \">\"\n  expected:\n  - quantity: neurons recorded\n    value: 245\n    tolerance: 24.5\n  - quantity: LFR cluster size\n    value: 199\n    tolerance: 19.9\n  - quantity: HFR cluster size\n    value: 46\n    tolerance: 4.6\n  criterion: Features as the Methods define them (half the time from peak depolarization to the\n    after-hyperpolarization trough of the mean waveform; amplitude ratio (n - p) / (n + p));\n    baseline rate and scaling under the readings of detail 5. Reproduced when, under one reading,\n    both cluster sizes are within tolerance, the one-way ANOVA of baseline rate by cluster has p <\n    0.001 and those of amplitude ratio and duration have p > 0.05; the cluster with the lower\n    centroid rate is the LFR cluster.\n- id: onset-population\n  statement: 29 neurons (from 5 of 6 rats, about 12% of all) increase firing in the first 1 s of\n    danger, uncertainty or safety over the 2 s pre-cue baseline, and all of them are in the LFR\n    cluster. These are the Onset population.\n  source: Results, vlPAG neurons are responsive at cue onset or ramp over cue presentation,\n    paragraph 2; Methods, Identifying cue-responsive vlPAG neurons\n  quote: We identified 29 neurons (obtained from 5/6 rats, ~12% of all neurons recorded) with\n    phasic increases in firing to danger, uncertainty, or safety ... All 29 neurons belonged to the\n    LFR cluster\n  expected:\n  - quantity: Onset neurons\n    value: 29\n    tolerance: 2.9\n  - quantity: rats contributing Onset neurons\n    value: 5\n    tolerance: 0\n  depends_on:\n  - fig1e-two-clusters\n  criterion: The screen of the Methods (paired two-tailed t-test over a cue's trials, raw rate in\n    the 2 s before onset against the first 1 s, each cue, p < 0.017, cue rate higher), uncertainty\n    trials collapsed. Reproduced when the count is within tolerance, the neurons come from five\n    rats, and every one is in the LFR cluster of fig1e-two-clusters (under the reading that claim\n    matched on); partially reproduced when the count holds and one or two fall outside the LFR\n    cluster or the rat count differs.\n- id: ramping-population\n  statement: Of the remaining neurons, 17 increase firing over baseline in the last 1 s of at\n    least one cue; three are in the HFR cluster, and the other 14 (from 4 of 6 rats, about 6%)\n    are the Ramping population.\n  source: Results, vlPAG neurons are responsive at cue onset or ramp over cue presentation,\n    paragraph 2\n  quote: 17 neurons increased firing to at least one cue during the last 1 s cue interval (interval\n    > baseline, p<0.017). Three neurons belonged to the high firing cluster ... The remaining 14\n    neurons (obtained from 4/6 rats, ~6% of all neurons recorded) belonged to the LFR cluster\n  expected:\n  - quantity: late-responsive neurons\n    value: 17\n    tolerance: 1.7\n  - quantity: late-responsive neurons in the HFR cluster\n    value: 3\n    tolerance: 0.3\n  - quantity: Ramping neurons (LFR)\n    value: 14\n    tolerance: 1.4\n  - quantity: rats contributing Ramping neurons\n    value: 4\n    tolerance: 0\n  depends_on:\n  - fig1e-two-clusters\n  - onset-population\n  criterion: The same t-test with the last 1 s cue interval, on the neurons that are not Onset\n    neurons. Reproduced when the three counts are within tolerance and the Ramping neurons come\n    from four rats; partially reproduced when the late-responsive count holds and the split by\n    cluster or rats differs.\n- id: fig2a-onset-anova\n  statement: Onset population firing (100 ms bins, 1 s before to the end of the cue) shows main\n    effects of cue and bin and a cue x bin interaction.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 1;\n    Figure 2A\n  quote: revealed main effects of cue and bin (Fs > 9, ps<0.01, η p 2 > 0.20, op > 0.95) but most\n    critically, a cue x bin interaction (F 218,6104 = 1.94, p<0.01\n  statistics:\n  - about: main effects of cue and bin\n    test: ANOVA\n    statistic: Fs > 9\n    p: 0.01\n    p_relation: \"<\"\n  - about: cue x bin interaction\n    test: ANOVA\n    statistic: F(218,6104) = 1.94\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - onset-population\n  criterion: Z-scored 100 ms firing as in the Methods, 110 bins from 1 s before onset to cue\n    offset, three cues, repeated-measures ANOVA over the 29 Onset neurons. Reproduced when both\n    main effects and the interaction have p < 0.01.\n- id: fig2b-onset-first-interval\n  statement: In the first 1 s cue interval Onset neurons fire more to danger than to uncertainty;\n    firing to uncertainty is numerically but not significantly above safety, while an ANOVA over\n    the first 5 s of uncertainty and safety shows a cue x bin interaction.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 1;\n    Figure 2B, left\n  quote: Onset neurons showed significantly greater firing to danger compared to uncertainty in the\n    first 1 s cue interval (t 28 = 4.54, p=9.70×10 −5 ). While numerically greater firing to\n    uncertainty over safety failed to reach significance in the first 1 s interval (t 28 = 1.37,\n    p=0.18), ANOVA restricted to uncertainty and safety\n  statistics:\n  - about: danger against uncertainty, first interval\n    test: paired t-test, two-tailed\n    statistic: t(28) = 4.54\n    p: 9.70e-5\n  - about: uncertainty against safety, first interval\n    test: paired t-test, two-tailed\n    statistic: t(28) = 1.37\n    p: 0.18\n  - about: uncertainty and safety, cue x bin, 1 s before onset to 5 s into the cue\n    test: ANOVA\n    statistic: F(59,1652) = 1.50\n    p: 0.01\n  depends_on:\n  - onset-population\n  criterion: Per neuron, mean interval Z firing (Methods, Z-score normalization, second paragraph;\n    readings of detail 4) over each cue's trials in the first 1 s. Reproduced when danger exceeds\n    uncertainty by a paired two-tailed t-test at p < 0.05, uncertainty is above safety in mean\n    with p >= 0.05 (the paper's test, as written), and the repeated-measures ANOVA of the 100 ms\n    data for uncertainty and safety, 60 bins, has a cue x bin interaction at p < 0.05.\n- id: fig2b-onset-last-interval\n  statement: Differential firing of Onset neurons is absent in the last 1 s cue interval, for\n    danger against uncertainty and uncertainty against safety.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 1;\n    Figure 2B, right\n  quote: Differential firing was not observed to danger vs. uncertainty (t 28 = 1.69, p=0.10) or to\n    uncertainty vs. safety (t 28 = 0.60, p=0.55) in the last 1 s cue interval\n  statistics:\n  - about: danger against uncertainty, last interval\n    test: paired t-test, two-tailed\n    statistic: t(28) = 1.69\n    p: 0.10\n  - about: uncertainty against safety, last interval\n    test: paired t-test, two-tailed\n    statistic: t(28) = 0.60\n    p: 0.55\n  depends_on:\n  - onset-population\n  criterion: A claim of absence, judged on the paper's paired two-tailed t-tests at p < 0.05 on the\n    last 1 s interval Z firing. Reproduced when neither pair differs; the effect sizes are given\n    either way.\n- id: fig2c-ramping-anova\n  statement: Ramping population firing (100 ms bins over the cue) shows main effects of cue and\n    bin and a cue x bin interaction, with ramping greatest to danger, intermediate to uncertainty\n    and absent to safety.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 2;\n    Figure 2C\n  quote: Ramping activity was most apparent to danger, intermediate to uncertainty, and absent to\n    safety\n  statistics:\n  - about: main effects of cue and bin\n    test: ANOVA\n    statistic: Fs > 60\n    p: 0.01\n    p_relation: \"<\"\n  - about: cue x bin interaction\n    test: ANOVA\n    statistic: F(218,2834) = 4.33\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - ramping-population\n  criterion: As fig2a-onset-anova, over the 14 Ramping neurons. Reproduced when both main effects\n    and the interaction have p < 0.01 and the mean Z firing of the last 1 s of the cue orders\n    danger > uncertainty > safety.\n- id: fig2d-ramping-first-interval\n  statement: Ramping neurons show no differential firing in the first 1 s cue interval.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 2;\n    Figure 2D, left\n  quote: Ramping neurons showed no significant differences in firing to danger vs. uncertainty (t\n    13 = 0.62, p=0.55) or uncertainty vs. safety (t 13 = 0.24, p=0.81) in the first 1 s cue\n    interval\n  statistics:\n  - about: danger against uncertainty, first interval\n    test: paired t-test, two-tailed\n    statistic: t(13) = 0.62\n    p: 0.55\n  - about: uncertainty against safety, first interval\n    test: paired t-test, two-tailed\n    statistic: t(13) = 0.24\n    p: 0.81\n  depends_on:\n  - ramping-population\n  criterion: A claim of absence, judged on the paper's paired two-tailed t-tests at p < 0.05 on\n    first 1 s interval Z firing. Reproduced when neither pair differs. The legend prints 0.82 for\n    the second test.\n- id: fig2d-ramping-last-interval\n  statement: In the last 1 s cue interval Ramping neurons fire more to danger than to uncertainty\n    and more to uncertainty than to safety.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 2;\n    Figure 2D, right\n  quote: However, differential firing to danger vs. uncertainty (t 13 = 3.17, p=7.41×10 −3 ), and\n    uncertainty vs. safety (t 13 = 8.26, p=2.00×10 −6 ), was observed in the last 1 s cue interval\n  statistics:\n  - about: danger against uncertainty, last interval\n    test: paired t-test, two-tailed\n    statistic: t(13) = 3.17\n    p: 7.41e-3\n  - about: uncertainty against safety, last interval\n    test: paired t-test, two-tailed\n    statistic: t(13) = 8.26\n    p: 2.00e-6\n  depends_on:\n  - ramping-population\n  criterion: Reproduced when both differences are significant by paired two-tailed t-tests at p <\n    0.05 in the stated direction (readings of detail 4).\n- id: fig2e-departure-times\n  statement: Ramping population firing departs from safety earlier for danger (2.8 s after cue\n    onset at p < 0.05, 5.8 s with Bonferroni correction) than for uncertainty (5.7 s, 6.5 s).\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 3;\n    Methods, Population and single-unit firing analyses, paragraph 2; Figure 2E\n  quote: Ramping activity to danger emerged earlier ( Figure 2E ; 2.8 s following cue onset for\n    p<0.05; 5.8 s for full Bonferroni correction, p<0.00025 [0.05/200]) than ramping activity to\n    uncertainty (5.7 s following cue onset; 6.5 s for full Bonferroni correction)\n  expected:\n  - quantity: danger departure, p < 0.05\n    value: 2.8\n    tolerance: 0.28\n    unit: s\n  - quantity: danger departure, p < 0.00025\n    value: 5.8\n    tolerance: 0.58\n    unit: s\n  - quantity: uncertainty departure, p < 0.05\n    value: 5.7\n    tolerance: 0.57\n    unit: s\n  - quantity: uncertainty departure, p < 0.00025\n    value: 6.5\n    tolerance: 0.65\n    unit: s\n  depends_on:\n  - ramping-population\n  criterion: A 1 s window starting at cue onset and advanced in 100 ms steps across the cue;\n    in each, a paired two-tailed t-test over the 14 Ramping neurons of danger (or uncertainty)\n    against safety firing; departure is the first window with p < 0.05 (or p < 0.00025). Open\n    are the firing measure (readings (a) the mean of the 100 ms Z-scored bins of Figure 2C within\n    the window; (b) the per-trial interval Z transformation of the Methods applied to each\n    window) and the time reported (readings (a) the window's start; (b) its end). Reproduced\n    when, under one reading, all four times are within tolerance; partially reproduced when\n    danger departs before uncertainty at both thresholds and a time is outside tolerance.\n- id: fig2e-rate-no-difference\n  statement: The rate of firing increase from the departure window to the last 1 s window does\n    not differ between danger and uncertainty, so the earlier departure, not a faster rise,\n    separates them.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 3;\n    Figure 2E inset\n  quote: Change in firing rate did not differ between danger and uncertainty ( Figure 2E , Inset)\n  depends_on:\n  - fig2e-departure-times\n  criterion: A claim of absence. Per Ramping neuron and cue, (firing in the last 1 s window minus\n    firing in the cue's departure window at p < 0.05) divided by the time between the two windows\n    (Methods); the paper's test is the paired t-test of the inset legend, at p < 0.05. Reproduced\n    when danger and uncertainty do not differ, under the reading fig2e-departure-times matched on\n    (under every reading if none).\n- id: fig2s1-single-trial\n  statement: The population patterns hold trial by trial. Onset population firing in the first 1\n    s exceeds baseline on every individual trial of every cue, and Ramping population firing in\n    the last 1 s exceeds baseline on danger and uncertainty trials but not safety trials.\n  source: Figure 2, figure supplement 1\n  quote: Note that increased cue firing over baseline tended to be highest on trial 1, but was\n    observed for every individual trial for all cues ... Increased cue firing over baseline was\n    consistently observed on danger and uncertainty trials, but not safety trials\n  depends_on:\n  - onset-population\n  - ramping-population\n  criterion: Per trial position within each trial type (danger 1 to 6, uncertainty shock 1 to 6,\n    uncertainty omission 1 to 10, safety 1 to 10), the population mean raw firing rate (Hz) of the\n    interval against the population mean rate of the 2 s before onset. Reproduced when Onset\n    first-interval firing exceeds baseline at all 32 positions, and Ramping last-interval firing\n    exceeds baseline at all 22 danger and uncertainty positions and at no more than half of the\n    10 safety positions; the paper gives no rule for \"not safety trials\", and this is the reading\n    named here.\n- id: fig2s2-nose-poke-cessation\n  statement: Onset and Ramping firing is not driven by nose poke cessation. Across neurons,\n    firing to danger (Onset first interval, Ramping last interval) is uncorrelated with firing to\n    the first second of an ITI poke cessation and is consistently greater.\n  source: Figure 2, figure supplement 2; Results, Population biases are evident in vlPAG\n    single-units, paragraph 3\n  quote: Comparison of single-unit firing to danger (Onset, first interval; Ramping, last interval)\n    and nose poke suppression (first interval) revealed no correlation and an overwhelming bias\n    towards greater firing to danger\n  statistics:\n  - about: Onset neurons, correlation\n    test: Pearson correlation\n    statistic: R2 = 0.01\n    p: 0.32\n  - about: Onset neurons, bias to danger\n    test: sign test\n    p: 1.62e-6\n  - about: Ramping neurons, correlation\n    test: Pearson correlation\n    statistic: R2 = 0.08\n    p: 0.10\n  - about: Ramping neurons, bias to danger\n    test: sign test\n    p: 1.22e-4\n  depends_on:\n  - onset-population\n  - ramping-population\n  criterion: Cessation events are ITI periods (no cue) in which a nose poke is followed by at\n    least 2 s without a poke; the interval of the poke is -1 and the first no-poke second +1\n    (legend). Open are the ITI limits (readings (a) any time outside cue, delay and shock\n    periods; (b) excluding also 10 s after each cue offset) and the firing measure (readings (a)\n    raw rate in Hz for danger and for the +1 interval; (b) each as differential firing, danger\n    against its 2 s pre-cue baseline and cessation against the -1 interval). Reproduced when,\n    under one reading, the Pearson correlation across neurons is not significant (p >= 0.05) and a\n    two-sided sign test finds danger greater at p < 0.05, for both populations; partially\n    reproduced when this holds for one.\n- id: fig3-onset-ramping-independent\n  statement: In the four sessions with an Onset and a Ramping neuron recorded together, trial by\n    trial firing of the two is not negatively related; a significant negative beta appears for one\n    interval of one pair only.\n  source: Results, vlPAG neurons show differential firing that is maximal to danger, paragraph 4;\n    Figure 3\n  quote: A significant (p<0.05), negative β was only found for one interval, for one neuron pair\n    (pair 1, interval indicated by +)\n  expected:\n  - quantity: Onset-Ramping pairs recorded in the same session\n    value: 4\n    tolerance: 0\n  depends_on:\n  - onset-population\n  - ramping-population\n  criterion: For each pair and each 1 s cue interval, a regression (with constant) over the 32\n    trials of the Onset neuron's interval Z firing on the Ramping neuron's (Methods, Single-unit,\n    linear regression, last sentences). Reproduced when four pairs are found and at most two of\n    the 40 interval regressions give a negative beta with p < 0.05 (one reported; at a 0.05 level\n    about one is expected by chance); not reproduced when three or more do.\n- id: fig4abc-onset-single-unit-biases\n  statement: In the first 1 s interval, Onset single units' danger and uncertainty firing are\n    correlated and biased to danger; uncertainty and safety firing are correlated but the bias\n    to uncertainty is not significant; danger firing is biased to the first over the last\n    interval, with no correlation between them.\n  source: Results, Population biases are evident in vlPAG single-units, paragraph 1; Figure 4A to\n    4C; Methods, Population and single-unit firing analyses, paragraph 3\n  quote: Danger and uncertainty firing were correlated, and single-units were biased towards greater\n    firing to danger ( Figure 4A ). Uncertainty and safety firing were also correlated; however, the\n    single-unit bias towards greater firing to uncertainty was not significant\n  depends_on:\n  - onset-population\n  criterion: Per Onset neuron, mean interval Z firing per cue (readings of detail 4). Pearson\n    correlation (p < 0.05) and sign test (p < 0.05, two-sided per detail 6) for each panel.\n    Reproduced when A has a positive correlation and a danger bias, B a positive correlation and a\n    sign test with p >= 0.05, and C a first-interval bias and a correlation with p >= 0.05;\n    partially reproduced when two of the three panels hold. The R2 and p values printed in the\n    panels could not be read from the text.\n- id: fig4d-onset-patterns\n  statement: The most common pattern of Onset neurons in the first 1 s interval is danger >\n    uncertainty > safety (14 neurons), the only pattern with more neurons than expected by\n    chance.\n  source: Results, Population biases are evident in vlPAG single-units, paragraph 1; Figure 4D;\n    Methods, Determining observed and expected cue firing patterns\n  quote: Examining relative cue firing for each Onset neuron in the first 1 s interval revealed the\n    most common pattern to be ... danger > uncertainty > safety (n = 14). This was the only pattern\n    to contain more units than would be expected than chance\n  expected:\n  - quantity: Onset neurons with danger > uncertainty > safety\n    value: 14\n    tolerance: 1.4\n  depends_on:\n  - onset-population\n  criterion: Each neuron is placed by the order of its mean interval Z firing to the three cues;\n    the chance distribution comes from 1000 shuffles. Open are the shuffle (readings (a) the\n    three cue values permuted within each neuron; (b) each cue's values permuted across neurons)\n    and \"more than expected by chance\" (readings (a) above the 95th percentile of the shuffled\n    counts; (b) above the most extreme non-outlier of the box plot, 1.5 interquartile ranges above\n    the 75th percentile). Reproduced when, under one reading, the count is within tolerance, is\n    the largest, and is the only one of the six orders above chance.\n- id: fig4efg-ramping-single-unit-biases\n  statement: In the last 1 s interval, Ramping single units' danger and uncertainty firing are\n    correlated and biased to danger; uncertainty and safety firing are not correlated but are\n    biased to uncertainty; danger firing is biased to the last over the first interval, with no\n    correlation between them.\n  source: Results, Population biases are evident in vlPAG single-units, paragraph 2; Figure 4E to\n    4G\n  quote: A significant correlation between firing to danger and uncertainty was observed, along with\n    a single-unit bias towards greater firing to danger ( Figure 4E ). Only now, there was no\n    correlation between uncertainty and safety firing, but a consistent bias towards greater\n    uncertainty firing\n  depends_on:\n  - ramping-population\n  criterion: As fig4abc-onset-single-unit-biases, on the 14 Ramping neurons and the last 1 s\n    interval. Reproduced when E has a positive correlation and a danger bias, F a correlation with\n    p >= 0.05 and an uncertainty bias, and G a last-interval bias and a correlation with p >=\n    0.05; partially reproduced when two of the three hold.\n- id: fig4h-ramping-patterns\n  statement: The most common pattern of Ramping neurons in the last 1 s interval is danger >\n    uncertainty > safety (11 neurons), the only pattern above chance.\n  source: Results, Population biases are evident in vlPAG single-units, paragraph 2; Figure 4H\n  quote: The most common firing pattern in the last 1 s interval was ... danger > uncertainty >\n    safety (n = 11). This was the only pattern to contain more units than expected by chance\n  expected:\n  - quantity: Ramping neurons with danger > uncertainty > safety\n    value: 11\n    tolerance: 1.1\n  depends_on:\n  - ramping-population\n  criterion: As fig4d-onset-patterns, on the 14 Ramping neurons and the last 1 s interval, with the\n    same readings.\n- id: fig5a-onset-probability-first-interval\n  statement: In the first 1 s cue interval the Onset population's probability beta is positive\n    and significant and exceeds both fear betas, neither of which differs from zero.\n  source: Results, Onset neurons signal threat probability, paragraph 2; Figure 5A\n  quote: The beta coefficient for the probability regressor was positive and significant, exceeding\n    the beta coefficient for either measure of fear output – neither of which differed from zero\n  statistics:\n  - about: probability against total fear\n    test: paired samples t-test\n    statistic: t(28) = 3.75\n    p: 8.01e-4\n  - about: probability against interval fear\n    test: paired samples t-test\n    statistic: t(28) = 4.57\n    p: 8.90e-5\n  depends_on:\n  - onset-population\n  criterion: Single-unit regressions of the Methods on first-interval Z firing (readings of details\n    1, 2 and 4). Reproduced when the probability beta exceeds each fear beta by paired two-tailed\n    t-tests at p < 0.05, the probability beta is above zero by a single-sample t-test at p <\n    0.005, and neither fear beta differs from zero at p < 0.005 (the threshold of the Figure 5D\n    legend, the paper's test for comparisons to zero); the result at 0.05 is shown as a variant.\n- id: fig5bc-onset-beta-bias\n  statement: Onset single-unit betas are positively biased for threat probability but not for\n    total or interval fear.\n  source: Results, Onset neurons signal threat probability, paragraph 2; Figure 5B and 5C\n  quote: Single-unit beta coefficients were positively biased for threat probability, but not for\n    either measure of fear output\n  depends_on:\n  - fig5a-onset-probability-first-interval\n  criterion: First-interval betas of the 29 Onset neurons; the legend's sign test of each\n    regressor against zero, two-sided, p < 0.05. Reproduced when probability is biased positive\n    and neither fear regressor is (p >= 0.05, the paper's test, as written).\n- id: fig5d-onset-all-intervals\n  statement: Over the ten 1 s cue intervals, Onset threat probability signaling is highest in the\n    first interval, persists several seconds and diminishes, while total and interval fear account\n    for firing in no interval; an ANOVA shows a main effect of regressor and a regressor x interval\n    interaction.\n  source: Results, Onset neurons signal threat probability, paragraph 3; Figure 5D\n  quote: Examining the entirety of cue presentation, threat probability signaling was highest in the\n    first interval, persisted several more seconds and diminished ( Figure 5D ). Total fear or\n    interval fear did not account for variance in single-unit firing at any interval\n  statistics:\n  - about: main effect of regressor\n    test: ANOVA\n    statistic: F(2,56) = 7.16\n    p: 0.01\n    p_relation: \"<\"\n  - about: regressor x interval interaction\n    test: ANOVA\n    statistic: F(18,504) = 2.38\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig5a-onset-probability-first-interval\n  criterion: Betas of the 29 Onset neurons for the three regressors in each of the ten intervals;\n    repeated-measures ANOVA (regressor x interval). Reproduced when both effects have p < 0.01,\n    the mean probability beta is largest in the first interval and above zero (single-sample\n    t-test, p < 0.005) in it and in at least one later interval, and no fear beta differs from\n    zero at p < 0.005 in any interval.\n- id: fig5s1-regressor-combinations\n  statement: Onset neurons prioritize probability whatever the combination of regressors; a fear\n    beta reaches significance only when total fear is the sole regressor, and even then its\n    relation is weaker than that of probability.\n  source: Results, Onset neurons signal threat probability, paragraph 3; Figure 5, figure\n    supplement 1A to 1E\n  quote: In fact, significance for fear output could only be found if total fear was the only\n    regressor used in the analysis ... Even then, the predictive relationship was weaker than that\n    of probability\n  depends_on:\n  - fig5a-onset-probability-first-interval\n  criterion: Regressions as in fig5d-onset-all-intervals with the regressors (A) probability and\n    total fear, (B) probability and interval fear, (C) interval fear, (D) total fear, (E)\n    probability. Reproduced when, in A, B and C, no fear beta differs from zero (single-sample\n    t-test, p < 0.005) in any interval, in D at least one interval does, and the D beta is below\n    the E beta. \"Weaker\" is open; readings (a) the mean betas of the first interval; (b) the\n    largest mean beta over intervals.\n- id: fig5e-onset-tuning-curve\n  statement: Varying the probability assigned to uncertainty from 0 to 1 in 0.125 steps, the\n    Onset population's mean probability beta in the first interval peaks at the actual 0.375,\n    with the flanking values next highest and betas falling off toward the extremes.\n  source: Results, Onset neurons signal threat probability, paragraph 4; Methods, Threat\n    probability tuning curve; Figure 5E\n  quote: The beta coefficient resulting from regression using the actual shock probability\n    (uncertainty = 0.375), was the 'peak' of the tuning curve. The probabilities with the next\n    highest beta coefficients were those flanking 0.375\n  expected:\n  - quantity: uncertainty assignment at the peak of the Onset tuning curve\n    value: 0.375\n    tolerance: 0\n  depends_on:\n  - fig5a-onset-probability-first-interval\n  criterion: Nine regressions per neuron with all three regressors, danger 1.00 and safety 0.00,\n    uncertainty 0 to 1 in steps of 0.125; mean probability beta over the 29 neurons per\n    assignment. Reproduced when the largest mean is at 0.375 and the next two are at 0.25 and\n    0.5; partially reproduced when the peak is at 0.375 and the order of the next two differs.\n    The tolerance is 0 because the assignments are a grid of 0.125.\n- id: fig5s2-binary-regressor\n  statement: Onset firing is better captured by the actual shock probability (uncertainty 0.375)\n    than by a binary regressor equating uncertainty with safety, in the first interval and\n    across the cue.\n  source: Figure 5, figure supplement 2; Results, Onset neurons signal threat probability,\n    paragraph 5\n  quote: The activity of vlPAG single-units was better captured by the regressor that reflected the\n    actual foot shock probability (uncertainty = 0.375) over a regressor that equated uncertainty\n    to safety (uncertainty = 0.000)\n  statistics:\n  - about: analysis x regressor x interval, all ten intervals\n    test: ANOVA\n    statistic: F(18,504) = 2.51\n    p: 5.89e-4\n  - about: analysis x regressor, first interval\n    test: ANOVA\n    statistic: F(2,56) = 7.80\n    p: 1.03e-3\n  depends_on:\n  - fig5d-onset-all-intervals\n  criterion: A second set of regressions with the binary regressor (danger 1, uncertainty and\n    safety 0) in place of probability, run separately. Repeated-measures ANOVA on betas with\n    analysis (probability or binary), regressor and interval. Reproduced when both interactions\n    have p < 0.05 and the first-interval mean beta is larger for probability than for binary.\n- id: fig5f-ramping-last-interval\n  statement: In the last 1 s cue interval, Ramping probability and total fear betas both exceed\n    the interval fear beta and do not differ from each other.\n  source: Results, Ramping neurons prioritize threat probability over fear output, paragraph 1;\n    Figure 5F\n  quote: Beta coefficients for probability and total fear were significantly greater than interval\n    fear (probability vs. interval fear, t 13 = 3.61, p=3.20×10 −3 ; total fear vs. interval fear, t\n    13 = 4.68, p=4.34×10 −4 ), but did not differ from one another (t 13 = 1.11, p=0.29)\n  statistics:\n  - about: probability against interval fear\n    test: paired samples t-test\n    statistic: t(13) = 3.61\n    p: 3.20e-3\n  - about: total fear against interval fear\n    test: paired samples t-test\n    statistic: t(13) = 4.68\n    p: 4.34e-4\n  - about: probability against total fear\n    test: paired samples t-test\n    statistic: t(13) = 1.11\n    p: 0.29\n  depends_on:\n  - ramping-population\n  criterion: Last-interval betas of the 14 Ramping neurons. Reproduced when both comparisons with\n    interval fear are significant at p < 0.05 in the stated direction and probability against\n    total fear has p >= 0.05 (the paper's test, as written).\n- id: fig5gh-ramping-beta-bias\n  statement: Ramping single-unit betas in the last interval are biased positive for probability\n    and total fear, which are uncorrelated; they are not biased for interval fear, and the\n    probability and interval fear betas are negatively correlated.\n  source: Results, Ramping neurons prioritize threat probability over fear output, paragraph 1;\n    Figure 5G and 5H\n  quote: Ramping single-units were biased towards positive beta coefficients for probability and\n    total fear ( Figure 5G ), but there was no correlation between these regressors. Ramping\n    single-units were not biased towards positive beta coefficients for interval fear ( Figure 5H\n    ), but signaling of probability and interval fear were negatively correlated\n  depends_on:\n  - fig5f-ramping-last-interval\n  criterion: Sign tests against zero (two-sided, p < 0.05) and Pearson correlations (p < 0.05)\n    across the 14 neurons. Reproduced when probability and total fear are biased positive, their\n    correlation has p >= 0.05, interval fear is not biased (p >= 0.05), and probability and\n    interval fear correlate negatively at p < 0.05; partially reproduced when three of the four\n    hold.\n- id: fig5i-ramping-all-intervals\n  statement: Over all ten cue intervals Ramping neurons prioritize probability (mean beta 0.58,\n    against 0.12 for total fear and -0.03 for interval fear); only the probability beta differs\n    from zero and it exceeds both fear betas, with a main effect of regressor and a regressor x\n    interval interaction.\n  source: Results, Ramping neurons prioritize threat probability over fear output, paragraph 1;\n    Figure 5I\n  quote: Linear regression for all ten intervals revealed that threat probability signaling was\n    prioritized over total fear and interval fear ... Only the beta coefficient for probability\n    differed significantly from zero\n  statistics:\n  - about: main effect of regressor\n    test: ANOVA\n    statistic: F(2,26) = 8.96\n    p: 0.01\n    p_relation: \"<\"\n  - about: regressor x interval interaction\n    test: ANOVA\n    statistic: F(18,234) = 2.16\n    p: 0.01\n    p_relation: \"<\"\n  - about: probability beta against zero\n    test: single-sample t-test\n    statistic: t(13) = 4.21\n    p: 1.02e-3\n  - about: probability against total fear\n    test: paired t-test\n    statistic: t(13) = 2.32\n    p: 0.04\n  - about: probability against interval fear\n    test: paired t-test\n    statistic: t(13) = 4.32\n    p: 8.28e-4\n  expected:\n  - quantity: mean probability beta over the ten intervals\n    value: 0.58\n    tolerance: 0.14\n  - quantity: mean total fear beta over the ten intervals\n    value: 0.12\n    tolerance: 0.10\n  - quantity: mean interval fear beta over the ten intervals\n    value: -0.03\n    tolerance: 0.05\n  depends_on:\n  - ramping-population\n  criterion: Per Ramping neuron, the mean of its betas over the ten intervals; tolerances are the\n    reported SEMs. Reproduced when the three means are within tolerance under one reading of\n    details 1, 2 and 4, the ANOVA effects have p < 0.01, the probability mean differs from zero\n    and exceeds both fear means at p < 0.05, and the fear means do not differ from zero at p <\n    0.05; partially reproduced when the tests hold and a mean is outside tolerance.\n- id: fig5j-ramping-tuning-curve\n  statement: The Ramping population's tuning curve for the last interval is shifted right of the\n    actual probability, peaking at 0.625, consistent with mixed signaling of probability and fear.\n  source: Results, Ramping neurons prioritize threat probability over fear output, paragraph 2;\n    Figure 5J\n  quote: Tuning was shifted right of the actual probability, with a 'peak' at 0.625\n  expected:\n  - quantity: uncertainty assignment at the peak of the Ramping tuning curve\n    value: 0.625\n    tolerance: 0\n  depends_on:\n  - fig5f-ramping-last-interval\n  criterion: As fig5e-onset-tuning-curve, on the 14 Ramping neurons and the last 1 s interval.\n    Reproduced when the largest mean probability beta is at 0.625; partially reproduced when it\n    is at 0.5 or 0.75 (right of 0.375 but not at 0.625).\n- id: fig6ab-post-cue-firing\n  statement: In the 5 s after cue offset (delay, shock, post-shock; the shock itself excluded)\n    Onset neurons show no effects of trial type or bin, while Ramping neurons keep firing to\n    danger and uncertainty through the delay, with a trial x bin interaction, and the two\n    populations differ.\n  source: Results, Ramping neurons signal threat probability through delay until shock receipt,\n    paragraph 1; Figure 6A and 6B\n  quote: ANOVA for normalized firing rate ... revealed no main effects or interactions for Onset\n    neurons (F s <2.3, ps >0.09). By contrast, identical ANOVA revealed main effects of trial and\n    bin (Fs >3, ps <0.01), as well as a trial x bin interaction for Ramping neurons (F 132,1716 =\n    3.14, p<0.01\n  statistics:\n  - about: Onset neurons, all effects\n    test: ANOVA\n    statistic: Fs < 2.3\n    p: 0.09\n    p_relation: \">\"\n  - about: Ramping neurons, main effects of trial type and bin\n    test: ANOVA\n    statistic: Fs > 3\n    p: 0.01\n    p_relation: \"<\"\n  - about: Ramping neurons, trial type x bin\n    test: ANOVA\n    statistic: F(132,1716) = 3.14\n    p: 0.01\n    p_relation: \"<\"\n  - about: neuron type interactions (trial type, bin, trial type x bin)\n    test: ANOVA\n    statistic: Fs > 2.50\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - onset-population\n  - ramping-population\n  criterion: Z-scored 100 ms firing (Methods) for the four trial types, 45 bins from cue offset to\n    5 s after it without the 0.5 s shock (2.0 to 2.5 s after offset). Reproduced when, for Onset\n    neurons, no effect has p < 0.05 (the paper's test, as written); for Ramping neurons, both main\n    effects and the interaction have p < 0.01; and in the mixed ANOVA with neuron type the three\n    neuron type interactions have p < 0.01. Partially reproduced when two of these three parts\n    hold.\n- id: fig6c-onset-post-cue-regression\n  statement: After cue offset Onset neurons signal neither interval fear nor probability; no\n    effect of regressor or regressor x interval interaction, and no beta differs from zero.\n  source: Results, Ramping neurons signal threat probability through delay until shock receipt,\n    paragraph 2; Figure 6C\n  quote: Onset neurons did not signal interval fear or probability at any time following cue offset\n    ( Figure 6C ). ANOVA revealed no main effect of regressor (F 1,28 = 1.02, p=0.32\n  statistics:\n  - about: main effect of regressor\n    test: ANOVA\n    statistic: F(1,28) = 1.02\n    p: 0.32\n  - about: regressor x interval interaction\n    test: ANOVA\n    statistic: F(8,224) = 0.53\n    p: 0.83\n  depends_on:\n  - onset-population\n  criterion: A claim of absence. Regressions per neuron in the nine 500 ms post-cue intervals (four\n    of the delay, five after the shock) on interval fear (the suppression ratio of that 500 ms\n    interval, readings of details 1 and 2) and probability; repeated-measures ANOVA at p < 0.05\n    and single-sample t-tests against zero at p < 0.005 (the Figure 6D legend). Reproduced when\n    neither ANOVA effect is significant and no beta differs from zero.\n- id: fig6d-ramping-post-cue-regression\n  statement: Ramping neurons signal probability throughout the delay (the first four 500 ms\n    intervals after cue offset), and this signal diminishes after shock delivery, with a\n    regressor x interval interaction.\n  source: Results, Ramping neurons signal threat probability through delay until shock receipt,\n    paragraph 2; Figure 6D\n  quote: By contrast, Ramping neurons signaled probability throughout the delay period ( Figure 6D ,\n    first four intervals), which diminished following shock delivery\n  statistics:\n  - about: regressor x interval interaction\n    test: ANOVA\n    statistic: F(8,104) = 5.20\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - ramping-population\n  criterion: As fig6c-onset-post-cue-regression, on the 14 Ramping neurons. Reproduced when the\n    interaction has p < 0.01, the mean probability beta is above zero at p < 0.005 (single-sample\n    t-test, the legend's threshold) in all four delay intervals, and the mean over the five\n    post-shock intervals is below the mean over the delay; partially reproduced when the\n    interaction holds and the probability beta is significant in one to three delay intervals.\n- id: fig6ef-beta-correlations\n  statement: Probability betas of the delay intervals correlate with those of the post-shock\n    intervals in 13 of 20 comparisons for Onset neurons but 4 of 20 for Ramping neurons, a\n    significant difference (6 and 1 of 20 after Bonferroni correction, also different).\n  source: Results, Ramping neurons signal threat probability through delay until shock receipt,\n    paragraph 3; Figure 6E and 6F\n  quote: Significant between-interval correlations for the probability beta coefficient were\n    observed for 13/20 comparisons in Onset neurons ... significant correlations were found for\n    only 4/20 comparisons in Ramping neurons\n  statistics:\n  - about: proportions at p < 0.05, Onset against Ramping\n    test: chi-square test\n    statistic: χ2 = 8.08\n    p: 4.5e-3\n  - about: proportions at p < 0.01 (Bonferroni, five tests per interval)\n    test: chi-square test\n    statistic: χ2 = 4.22\n    p: 0.039\n  expected:\n  - quantity: significant delay against post-shock correlations, Onset, p < 0.05\n    value: 13\n    tolerance: 1.3\n  - quantity: significant delay against post-shock correlations, Ramping, p < 0.05\n    value: 4\n    tolerance: 0.4\n  - quantity: significant correlations, Onset, p < 0.01\n    value: 6\n    tolerance: 0.6\n  - quantity: significant correlations, Ramping, p < 0.01\n    value: 1\n    tolerance: 0.1\n  depends_on:\n  - fig6c-onset-post-cue-regression\n  - fig6d-ramping-post-cue-regression\n  criterion: For each population, the Pearson correlation across neurons of the probability beta\n    of each of the four delay intervals with each of the five post-shock intervals (20 pairs),\n    significant at p < 0.05 and at p < 0.01. The chi-square test on the 2 x 2 counts is open;\n    readings (a) Pearson chi-square times (N - 1) / N, which gives the reported 8.08 and 4.22 from\n    the reported counts (8.29 x 39/40 and 4.33 x 39/40, worked here); (b) Pearson chi-square\n    without correction; (c) with Yates' correction. Reproduced when, under one reading, the\n    chi-square test has p < 0.05 at both thresholds and the four counts are within tolerance;\n    partially reproduced when Onset has more significant comparisons than Ramping at both\n    thresholds but a count or a test differs.\n- id: fig1s5-hfr-units\n  statement: The three late-responsive neurons of the HFR cluster each fire most to danger in the\n    last 1 s cue interval.\n  source: Figure 1, figure supplement 5\n  quote: Each neuron showed maximal firing to danger in the last 1 s cue interval\n  expected:\n  - quantity: HFR late-responsive neurons\n    value: 3\n    tolerance: 0\n  depends_on:\n  - ramping-population\n  criterion: For each of the three, the mean last-interval firing (raw rate over trials of each\n    cue, and mean interval Z firing as a second reading) is higher for danger than for uncertainty\n    and safety. Reproduced when this holds for all three under one reading.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Draft written with 39 claims. Running the quote checker.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/wright-2019.yaml paper/10.7554-elife.45013.txt; echo EXIT $?; grep -n "—\|rather" claims/wright-2019.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "[^ ]: " claims/wright-2019.yaml | grep -v "^[0-9]*:#" | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wright-2019.yaml",
 "old_string": "    printed precision; 0.05 is the tolerance of the uncertainty value.",
 "new_string": "    printed precision; 0.05 is about the tolerance of the uncertainty value (0.053)."
}
```

```
The file claims/wright-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/wright-2019.yaml paper/10.7554-elife.45013.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/wright-2019.yaml` and did not commit it. It holds 38 claims, every one with a quote. The quote checker passes every quote and the schema. It flags 3 of the 50 p-values as "not found". The paper prints those three with trailing zeros: p = 9.70×10⁻⁵ and 8.90×10⁻⁵ for the Onset tests (fig2b, fig5a) and p = 3.20×10⁻³ for the Ramping test (fig5f). I read all three in the text and they are correct; the checker just doesn't recognise that printed form, so it still exits non-zero.

**Text read.** The version of record (PMC6435320, Europe PMC full text): main text, Methods, all figure legends and all figure-supplement legends, plus the Methods' example regression table. The paper has no other supplement. No PDF was supplied, so numbers printed only inside figures could not be read: the R² and sign-test p-values of Fig 4, the F values of Fig 5–supplement 1, and the values of the tuning curves. Those claims are judged on the tests the legends name.

**Code.** The paper's only code link is the lab website (http://mcdannaldlab.org/resources). It returns 404, and the one archived copy, from 2020, has no files. So no code was read, and every method in the file comes from the paper's text. The data set's description mentions sample MATLAB scripts, but those are data-set files, so I did not open them.

**Contents.**
- **Statistics:** 50 values are recorded, mostly p-values with their F, t and χ² statistics.
- **Expected values:** 19 claims have them. They are suppression ratios, neuron and cluster counts, departure times, tuning-curve peaks, mean Ramping betas and correlation counts. Tolerances are the reported SEM for the betas and 10% elsewhere. The exceptions, each with its reason in the file, are 0.05 for the safety ratio and 0 for the tuning peaks and exact counts.
- **Criteria:** all 38 claims have one. Five are claims of absence, judged on the paper's own test.

**Details the paper leaves open, and the readings named:**
1. **Nose-poke baseline window for the suppression ratio:** the 2 s before cue onset (the firing baseline), or the 10 s before onset (the cue's length).
2. **A ratio with no pokes at all (0/0):** set to 0, or left out.
3. **A session's ratio:** the mean of per-trial ratios, or the ratio of the session's mean rates.
4. **Baseline for per-trial interval firing:** the trial's own 2 s baseline, or the trial type's mean baseline.
5. **K-means:** baseline rate taken from the pre-cue windows or from the whole session, and features raw or Z-scored. Initialisation is a standard choice.
6. **Sign tests:** two-sided, since the paper doesn't say.
7. **Fig 4 shuffle:** cue values permuted within each neuron, or across neurons. "Above chance" means above the 95th percentile, or above the box plot's upper whisker.
8. **Fig 2E sliding window:** firing taken as the mean of the 100 ms Z-scored bins, or re-Z-scored per window. The reported time is the window's start or its end.
9. **Fig 2–supplement 2 (nose-poke cessation):** where the ITI starts and ends, and whether firing is raw or minus a baseline.
10. **Fig 6E/F χ² test:** Pearson χ² × (N−1)/N, plain Pearson, or Yates-corrected. The first reproduces the reported 8.08 and 4.22 from the reported counts.
11. **Smaller ones:** what counts as "weaker" in Fig 5–supplement 1, the rule for "not safety trials" in Fig 2–supplement 1, and that the ANOVAs are uncorrected repeated-measures designs, as the reported degrees of freedom imply.

**Inconsistencies within the paper, noted in the file:**
- The Onset danger vs uncertainty test is p = 9.70×10⁻⁵ in the Results but 9.70×10⁻⁴ in the Fig 2B legend; t(28) = 4.54 fits the Results.
- A Ramping first-interval test is p = 0.81 in the Results and 0.82 in the legend.
- The mean danger suppression ratio is 0.80 in the Results and 0.83 in the Fig 2–supplement 2 legend.

**Missing.** No claim was blocked for missing text. Only the linked code and the in-figure numbers were unavailable.

## End of run

29 turns, 7 minutes, $2.53 at API prices, result: success.
