# 000467 · claims · run 39955723970

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000467/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '30,400p'; ls claims/001453/ claims/000467/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc paper/*.txt; head -50 paper/*.txt; grep -n -i "STAR\|method\|supplement\|Figure S" paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -c 15000 claims/001453/*.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 236 more lines not kept]
```

**Agent calls Bash**

```bash
wc paper/*.txt; head -30 paper/*.txt; grep -n -i "^STAR\|^method\|supplement\|Figure S[0-9]\|github\|zenodo\|dandi" paper/*.txt | head -80; ls -la paper
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper text and supplement are in `paper/`. Reading the full text now.

**Agent calls Bash**

```bash
fold -s -w 200 paper/10.1016-j.cell.2023.05.025.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; grep -n -i "STAR Methods\|github\|zenodo\|dandi\|Supplement\|Quantification and statistical\|KEY RESOURCES" $TMPDIR/p.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 28,
 "limit": 200
}
```

```
28	pmc-prop-has-supplement yes pmc-prop-pdf-only no pmc-prop-suppress-copyright no pmc-prop-is-real-version no pmc-prop-is-scanned-article no pmc-prop-preprint no pmc-prop-in-epmc yes Introduction 
29	Eusocial insects, like ants and honeybees, use vast arrays of pheromones to communicate information with conspecifics and to regulate colony life. These adaptations correspond to elaborations of the 
30	chemosensory system, which are particularly striking in ants. Insect olfactory systems have a conserved organization, with olfactory sensory neurons (OSNs) in peripheral sensory organs innervating 
31	glomeruli in the antennal lobes (ALs) in the brain. 1 – 3 Much of the detailed knowledge of insect olfactory system development, anatomy, and neural function comes from studies of the vinegar fly 
32	Drosophila melanogaster . However, ants express an order of magnitude more odorant receptor genes (ORs) in their antennae, and possess an order of magnitude more AL glomeruli, than Drosophila . 4 – 
33	14 In Drosophila , the ~50 AL glomeruli each receive input from a functional class of OSNs and have stereotyped positions across individuals, which allowed the creation of atlases mapping odor-evoked 
34	response functions for each glomerulus. 2 , 15 – 18 By contrast, little is known about the wiring of OSN subpopulations, OR expression patterns at the level of individual OSNs, or how odors are 
35	represented in the more complex olfactory system of ants, which contains up to ~500 AL glomeruli. Here we focus on the neural representation of alarm pheromones, “danger” signals that are chemically 
36	well characterized across several ant species. Ant alarm pheromones are typically produced in the mandibular-, poison-, or Dufour’s gland, and stored in a glandular reservoir. The pheromone is then 
37	released into the surrounding air in response to danger. 19 Stimulating individuals with volatile alarm pheromones is experimentally simple and quickly elicits behavioral responses, whic
[... 190 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 227,
 "limit": 450
}
```

```
File content (38597 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 227,
 "limit": 180
}
```

```
227	(indicative of intercastes) 114 – 115 were excluded from our imaging study. METHOD DETAILS Behavior Alarm pheromones. We purchased 96% 4-methyl-3-heptanone from Pfaltz and Bauer (Item #: M19160 ), 
228	and ≥99% 4-methyl-3-heptanol and 99% 6-methyl-5-hepten-2-one from SigmaAldrich (Item numbers M48309 and M48805–100ML, respectively). 95% 4-methyl-3-hexanol was purchased from Enamine (CAS# 615–29-2), 
229	and paraffin oil from Hampton Research (cat. #HR3–421). We also initially tested the compound undecane, which functions as an alarm pheromone in several other ant species and is found in clonal 
230	raider ant extracts. 22 , 116 – 119 However, undecane has a lower volatility / vapor pressure than the other alarm pheromones ( Table S3 ), and only elicited non-specific walking behavior and no 
231	robust calcium responses in our experimental paradigms. We therefore did not investigate undecane further. General odorants. 98% 3-hexanone was purchased from Aldrich Chemistry (Item number 
232	103020–10G). 98% ethylpyrazine and 99% propionic acid were purchased from Sigma-Aldrich (Item numbers 250384–5G and W292419-SAMPLE-K, respectively). 100% ethanol was purchased from Decon Laboratories 
233	(Item #: 2716), and ≥99.5% isopropanol from Fisher Chemical (Item #: A416SK-4). We initially also tested six additional general odorants with lower volatility / vapor pressure ( Table S3 ). However, 
234	these odorants did not elicit robust calcium responses in our experimental paradigm and were therefore not studied further. Colony alarm bioassay. Alarm behavior assays were performed as described 
235	previously. 22 For experiments with 4-methyl-3-hexanol and 6-methyl-5-hepten-2-one, 30 mixed-age ants from clonal line B were introduced without brood into each arena. Trials were also performed with 
236	undecane, which only induced non-specific walking behavior. For behavioral experiments with GCaMP6s ants, due to limited numbers, 15–20 ants were introduced into each arena. Prior
[... 170 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 406,
 "limit": 240
}
```

```
406	phalloidin, but not GCaMP6s and Orco. The AL in (B) comes from a different ant than that in (A) and is shown in mirror image to align more closely with the image in (A). (C-F) Colony alarm bioassay, 
407	showing mean±SEM. (C-D) GCaMP6s ants and wild type ants leave the nest in response to 4-methyl-3-heptanone, 4-methyl-3-heptanol, and a 9:1 blend of the two compounds. (E-F) GCaMP6s ants and wild type 
408	ants leave the nest chamber in response to 4-methyl-3-heptanone and the blend; wild type ants also leave the nest chamber in response to 4-methyl-3-heptanol, while this response was not statistically 
409	significant in the GCaMP6s ants. Analyses for wild type ants (D, F) are based on previously published data ( Fig. 3 , 2600μg and vehicle control treatments in Lopes et al. 22 ). For the experiment in 
410	GCaMP6s ants (C, E), all pheromone treatments were compared to the same set of vehicle control trials. For the experiments in wild type ants (D, F), each pheromone treatment was conducted alongside 
411	its own set of vehicle control trials. Treatments and controls from the same experiment were statistically compared to each other and are plotted using identical symbol shapes. *: p<0.05; **: p<0.01; 
412	***: p<0.001; ****: p<0.0001. L: lateral; A: anterior. 6 Figure S3. Genomic analyses of the transgenic line used for imaging, related to Fig. 2 . (A) Normalized read depth for reads aligning to a 
413	panel of heterozygous SNPs, the ObirOrco promoter, and the non-ObirOrco portion of the transgene. Normalized read depth for ObirOrco is ~1.5, corresponding to a single additional copy of ObirOrco 
414	inserted into the genome (added to the two endogenous copies). Normalized read depth of ~0.5 at the rest of the insert is also consistent with a single copy (haploid) insertion. (B) The transgene 
415	insert was localized to a site on the 2 nd chromosomal scaffold. Black bars indicate breaks between contigs. (C) Close-up of the transgene insertion locus within an i
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '646,700p' $TMPDIR/p.txt | cut -c1-200; echo ----; sed -n '940,1180p' $TMPDIR/p.txt
```

```
phalloidin Invitrogen Cat#A34055 DAPI Invitrogen Cat#D1306 Paraffin oil Hampton Research Cat#HR3-421 100% pentane Sigma Aldrich Cat#236705 96% 4-methyl-3-heptanone Pfaltz and Bauer Cat# M19160 ≥99% 
4-methyl-3-heptanol Sigma-Aldrich Cat#M48309 99% 6-methyl-5-hepten-2-one Sigma-Aldrich Cat#M48805-100ML 95% 4-methyl-3-hexanol Enamine Cat# 615-29-2 98% 3-hexanone Aldrich Chemistry Cat#103020-10G 
98% ethylpyrazine Sigma-Aldrich Cat#250384-5G 99% propionic acid Sigma-Aldrich Cat#W292419-SAMPLE-K 100% ethanol Decon Laboratories Cat#2716 ≥99.5% isopropanol Fisher Chemical Cat#A416SK-4 RNAClean 
SPRI XPBeads Beckman Coulter Cat#A63987 Critical commercial assays Endotoxin-free midiprep kit Machery-Nagel Cat#740420.10 HiScribe T7 Arca mRNA kit (with tailing) New England Biolabs Cat#E2060S 
Experimental models: Organisms/strains O. biroi clonal line A wild type Kronauer Lab N/A O. biroi clonal line B wild type Kronauer Lab N/A O. biroi clonal line B 
[ie1-DsRed-ObirOrco-QF2-15xQUAS-GCaMP6s]; “GCaMP6s ant” This paper N/A Deposited data O. biroi reference genome v5.4 McKenzie and Kronauer 10 GCA: 003672135.1 Whole-genome sequence of GCaMP6s ant 
This paper BioProject ID: PRJNA947257 Confocal microscopy data This paper Brain Image Library IDs: 7b20a5b168a92088; 626fd578e97289bc; c2031d8218de058b Calcium imaging data This paper DANDI Archive 
ID: 000467 Oligonucleotides Primers for plasmid construction; see Table S4 This paper N/A Recombinant DNA plasmid pGL3-IE1 Gift from Zach Adelman; Anderson et al. 62 Addgene, ID 52894 plasmid 
pBAC-ECFP-15xQUAS_TATA-SV40 Gift from Christopher Potter; Riabinina et al. 122 Addgene, ID 104875 plasmid pBac-DsRed-ORCO_9kbProm-QF2 Gift from Christopher Potter; Riabinina et al. 122 Addgene, ID 
104877 plasmid pGP-CMV-GCaMP6s Gift from Douglas Kim & GENIE Project; Chen et al. 60 Addgene 40753 plasmid hyPB apis Gift from Martin Beye; Otte et al. 65 N/A plasmid 
pBAC-ie1-DsRed-ObirOrco-QF2-15xQUAS-GCaMP6s This paper Addgene, ID 200400 Software and alg
[... 286 more lines not kept]
```

**Agent**

I have the full text: the PMC author manuscript, its STAR Methods, figure legends including S1 to S7, and the supplemental tables PDF. Next I'll read the paper's GitHub code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/Social-Evolution-and-Behavior/HartKronauer2023 && cd HartKronauer2023 && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100
```

```
Exit code 128
fatal: could not read Username for 'https://github.com': No such device or address
```

**Agent calls Bash**

```bash
gh api repos/Social-Evolution-and-Behavior/HartKronauer2023 2>&1 | head -20; gh search repos HartKronauer2023 2>&1 | head; gh api orgs/Social-Evolution-and-Behavior/repos --paginate -q '.[].name' 2>&1 | head -50
```

```
gh: To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN environment variable. Example:
  env:
    GH_TOKEN: ${{ github.token }}
gh: To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN environment variable. Example:
  env:
    GH_TOKEN: ${{ github.token }}
gh: To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN environment variable. Example:
  env:
    GH_TOKEN: ${{ github.token }}
```

**Agent calls Bash**

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://api.github.com/repos/Social-Evolution-and-Behavior/HartKronauer2023; curl -s https://api.github.com/orgs/Social-Evolution-and-Behavior/repos?per_page=100 | grep -o '"full_name": "[^"]*"' | head -40
```

Result: the fetched text is not kept.

**Agent**

The linked URL (HartKronauer2023) returns 404; the lab has a repository named `Hart_Kronauer2023`, likely the same one. Cloning it.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/Social-Evolution-and-Behavior/Hart_Kronauer2023 && cd Hart_Kronauer2023 && git log --format='%H %ad %s' | head && find . -type f -not -path './.git/*' | head -100; cat README* 2>/dev/null | head -50
```

```
72d041a85dcec7c1429351a00a210d2353d0c6db Tue May 9 17:03:05 2023 -0400 Update macro_calcium_imaging.txt
566da93098e2cf0c652f40957832e9723138344b Tue May 9 17:02:30 2023 -0400 Update macro_calcium_imaging.txt
f735e2a7f6e6cf817f7cadaaa9d6d00b11572553 Tue May 9 17:02:07 2023 -0400 Update generate_tif_files.py
d477f8ac7562d9da2d8ad42365ee7f806d5ce5fe Mon May 8 15:02:27 2023 -0400 Delete macro_dffv4_batch_peak_img_3dtif.txt
950f3c9a31a5bfbe35aab9c7e7854a2a92621bc8 Mon May 8 15:01:31 2023 -0400 Add files via upload
aaea232900d47b378cb6ce69dbc88f97ed22f171 Mon May 8 14:59:41 2023 -0400 Update README.md
5e2b325eaaf8d4c48db641ed7f106237bd39b65b Mon May 8 14:47:32 2023 -0400 Add files via upload
63b7b688e716fa7dd1c12f3656ed4c67b246759c Thu May 4 14:46:39 2023 -0400 Update README.md
8f3443897ad03ef791323b901975e345609dbe15 Thu May 4 14:41:41 2023 -0400 Initial commit
./macro_calcium_imaging.txt
./generate_tif_files.py
./README.md
# Hart_Kronauer2023
Processing code for calcium imaging data from "Sparse and stereotyped encoding implicates a core glomerulus for ant alarm behavior".

Raw data with .nwb files can be found at https://dandiarchive.org/dandiset/000467

To re-analyze data, first download the archived data at the above link. Next, run the python script "generate_tif_files.py" on the downloaded archive to convert .nwb files to .tif files. Finally, install and run the ImageJ macro script "macro_calcium_imaging.txt". In each case you will need to enter the directory containing the source data into the scripts before running..
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/Hart_Kronauer2023 && cat generate_tif_files.py && echo ===== && cat macro_calcium_imaging.txt
```

```
import tifffile as tiff
import os
from pynwb import NWBHDF5IO


# this script reads .nwb files and writes corresponding new .tif files, for analysis in ImageJ. 
# source data: https://dandiarchive.org/dandiset/000467
# written by Taylor Hart
# specify the input and output directories below:


indir_path = "/Volumes/My Passport/test_download/000467/"
outdir_path = "/Volumes/My Passport/test_convert/"

if not os.path.exists(outdir_path):
	os.mkdir(outdir_path)

for antnum in os.listdir(indir_path):


[... 285 more lines not kept]
```

**Agent**

The code is two scripts at commit 72d041a: an NWB-to-TIFF converter and the ImageJ macro for stabilization, ΔF/F0 and max projection. Now the dandiset's title and description (metadata only).

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000467/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d[k] for k in ('identifier','most_recent_published_version','draft_version') if k in d},indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/000467/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'));print(d.get('assetsSummary',{}).get('approach'), d.get('assetsSummary',{}).get('numberOfSubjects'))"
```

Result: the fetched text is not kept.

**Agent**

The dandiset holds the calcium imaging only: 6 general-odorant ants, 3 bilateral ants, 13 alarm-pheromone ants. Checking the claims schema before writing.

**Agent calls Bash**

```bash
grep -oE '^ *-? ?[a-z_]+:' claims/001453/*.yaml | sort | uniq -c | sort -rn; ls docs tools; grep -n "data:\|elsewhere\|with_labels\|with_inputs" docs/*.md | head -30
```

```
20 - id:
     20   statement:
     20   source:
     19   quote:
     14     p:
     13   statistics:
     12   - test:
     12     p_relation:
      9   criterion:
      9     n:
      8   data:
      7   depends_on:
      4   - quantity:
      4     value:
      4     unit:
      4     tolerance:
      2   expected:
      2   - about:
      2     test:
      1 schema_version:
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,262p docs/protocol.md; sed -n 155,175p docs/pilot-notes.md; head -60 tools/claims_check.py; grep -n "kind\|deviation\|open" tools/entry.py | head -30
```

```
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -250
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
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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
[... 82 more lines not kept]
```

**Agent**

I have what I need: the full text, figure legends S1 to S7, the supplemental tables, the code at commit 72d041a, and the dandiset description. Writing the claims file now.

**Agent calls Bash**

```bash
cd paper; for s in "Both compounds caused ants to leave the initial nest pile" "in at least 80% of trials" "lacks panic alarm activity" "GCaMP6s labels the great majority" "greatly reduced across the entire AL" "only significantly different from control" "contains a 	single" "median of at most 6" "Sparse, unique subsets" "PG a was always located anterior" "with a single glomerulus activated by all three" "Both glomeruli were identified" "did not respond to 6-methyl" "return to baseline" "Fluorescence increases were frequently large"; do grep -o ".\{0,10\}$s.\{0,250\}" *.txt | head -2; echo; done
```

```
en-2-one. Both compounds caused ants to leave the initial nest pile (consisting of at least 2 adult workers and at least 1 egg) and the initial nest chamber ( Fig. 1C – D ). However, the behavioral responses were qualitatively distinct from one another, prompting additional analyses. Blinded categorization of the ma

 exposure in at least 80% of trials. We call this response “immediate panic alarm”. The most common response to 6-methyl-5-hepten-2-one was for the majority of ants to slowly walk away from the nest, while the nest pile persisted for more than one minute. We call this response “ants l

her hand, lacks panic alarm activity and does not normally cause nest evacuation. The occasional alarm responses to 6-methyl-5-hepten-2-one could represent secondary responses, in which an ant emits actual alarm pheromone in response to the stimulus compound. Creation of transgenic ant

ound that GCaMP6s labels the great majority of Orco-positive cells ( Fig. 2C ). In the ALs, high levels of GCaMP6s co-localized with Orco, which labels OSN afferents ( Fig. 2D ). 11 GCaMP6s is also expressed in parts of the sub-esophageal zone and central complex ( Fig. S1C – D ). These fluor

nals were greatly reduced across the entire AL connected to the ablated antenna, and no clear glomerular labeling remained ( Fig. 2F ). This indicates that GCaMP6s signal in the AL derives from the antennae and is likely to be exclusive to sensory neuron axons. Expression of genetically encoded 

amber was only significantly different from control for 4-methyl-3-heptanone and the blend ( Fig. S2E – F ). Crucially, GCaMP6s ants perceive both alarm pheromones, and their behavioral response is qualitatively similar to wild types. Finally, non-targeted transgene insertions can disrupt endogenous 


tivated a median of at most 6 glomeruli ( Fig. S5A ). Despite the small number of responding glomeruli, we observed consistent partial overlap in the response patterns activated by the three compounds elicitin
[... 14 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000467/10.1016-j.cell.2023.05.025.yaml",
 "content": "# Claims for Hart, Frank, Lopes et al. (2023), Cell, on dandiset 000467.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# under protocol pilot-10 (docs/protocol.md, Reader).\n#\n# Text read. The accepted author manuscript in PubMed Central (PMC10334690, NIHMS1904919), not\n# the version of record: the Results, Discussion, STAR Methods, Key Resources Table and the\n# legends of Figures 1 to 6, Table 1 and Figures S1 to S7, as served by PMC. The supplement read\n# is NIHMS1904919-supplement-1.pdf (Tables S1 to S4 and the supplemental references). The two\n# supplemental videos were not read. No PDF of the main text was supplied, so values shown only\n# in figures (the medians written on Figure 6, the boxes of Figure S5, the vectors of Figure 5D)\n# could not be read; every claim below rests on numbers printed in the text.\n#\n# Code read. The Key Resources Table links https://github.com/Social-Evolution-and-Behavior/\n# HartKronauer2023, which returns 404. The same lab's repository Hart_Kronauer2023 (README\n# \"Processing code for calcium imaging data from\" this paper, pointing to dandiset 000467) was\n# read at commit 72d041a85dcec7c1429351a00a210d2353d0c6db (2023-05-09). It holds two files.\n# generate_tif_files.py reads each NWB file (one z-plane of one trial, acquisition\n# \"TwoPhotonSeries1\") and writes a TIFF; it keeps only trials t288, t293, t284 and t290, a\n# hard-coded filter that no Methods text explains and that an attempt should not copy.\n# macro_calcium_imaging.txt is the ImageJ macro for the whole-AL peak maps (below). The ROI\n# drawing, the single-glomerulus traces, the R models (glm, lme) and the GraphPad analyses are\n# not in the repository.\n#\n# Data the paper used. Subjects are adult female transgenic O. biroi workers (clonal line B,\n# \"GCaMP6s ants\", GCaMP6s in olfactory sensory neurons under ObirOrco-QF2/15xQUAS), aged 55 to\n# 60 days (general odorants) and 90 to 104 days (alarm pheromones) after eclosion. Two-photon\n# volumes of the right antennal lobe (AL), 512 x 512 pixels x 33 planes at 5 um steps, 148 um\n# square at 2X zoom (0.289 um per pixel), 27.5 frames/s, one volume every 1.2 s (0.83\n# volumes/s); each trial is 48 s with a 3 s lead and a 5 s odor pulse. Three experiments.\n# (1) General odorants, n=6 ants, 7 to 9 odorants at 48% in random order, three repeats; five\n# odorants (3-hexanone, ethylpyrazine, ethanol, isopropanol, propionic acid) gave robust\n# responses and are analysed, each tested in 2 to 6 ants. (2) Bilateral imaging, n=3 ants, 1X\n# zoom (296 um square), paraffin oil and 4-methyl-3-hexanol at 48%. (3) Alarm pheromones, n=13\n# ants, paraffin oil vehicle then isopropanol positive control, then 4-methyl-3-heptanone,\n# 4-methyl-3-heptanol, 4-methyl-3-hexanol and 6-methyl-5-hepten-2-one (abbreviated 6MHO here)\n# in random order, three trials at the lower then three at the higher of two concentrations (24\n# presentations); 3 ants at 0.75% and 12%, 2 at 3% and 12%, 3 at 12% and 48%, 5 at 3% and 48%\n# (so n=8 at 48%). Undecane trials were also run and not analysed. Separately, 144 s recordings\n# of 6MHO at 48% in five ants (Figure S7A). The dandiset's description lists the same 6, 3 and\n# 13 subjects. Behaviour videos (Figures 1, S2C-F), confocal stacks (Brain Image Library) and\n# the genome sequence (NCBI BioProject) are not in the dandiset.\n#\n# Shared methods, from the STAR Methods (Image processing and analysis) and the macro.\n# (M1) Whole-AL peak map. Per plane, Image Stabilizer (translation, pyramid level 1, template\n# update 0.90, 200 iterations, tolerance 1e-7, from the macro); F0 the mean of frames 1 to 5\n# (frames are volumes, counted from 1 as ImageJ does); dF/F0; peak fold change the mean of\n# dF/F0 over frames 9 to 14; a 2-pixel Minimum filter; the maximum over the 33 planes; values\n# clipped to [-1, 4]. The Methods put the Minimum filter before the clipping; the macro clips\n# each plane, then filters, then clips the projection. The Methods order is the main reading,\n# the macro's a variant. The 1-sigma Gaussian blur the Methods name is for the first\n# per-plane look only, and the macro has none.\n# (M2) ROIs and responding glomeruli. The paper drew ROIs by eye on the M2 maps at each ant's\n# higher concentration around \"every glomerular region that responded to any odor in at least\n# two trials\", and called an ROI responding when its peak fold change, quantified \"across all\n# trials for a particular odor and concentration\", was at least 0.2. Open details, with the\n# readings the paper allows. Drawing ROIs: (a) connected regions of at least 0.2 in a trial's\n# map, kept when they recur in at least two trials of one odor; (b) as (a), keeping only\n# regions of glomerulus size (10 to 20 um diameter, Results) and splitting wider ones at local\n# maxima. The ROI value: (i) the mean over its pixels (ImageJ's default measure) or (ii) its\n# maximum. Counting: (x) an ROI responds when its value averaged over the trials of an\n# odor/concentration is at least 0.2 (Methods); (y) count per trial and average the counts\n# over trials (Figure S5 legend, \"the mean number of responding glomeruli for a given ant\n# across all trials\"). Overlapping ROIs of two odors at different depths count as different\n# glomeruli (Methods). Every claim built on M2 is judged under each reading.\n# (M3) Single glomeruli. For each trial, the plane holding the glomerulus centre, the maximum\n# over that plane and its two neighbours, then dF/F0 with F0 frames 1 to 5 and peak fold change\n# the mean over frames 9 to 14. The centre plane was chosen by eye, and the ROI within the plane\n# is not described. Readings: centre plane (a) where the glomerulus's area of at least 0.2 is\n# largest, (b) where its peak fold change is highest; ROI a disc of 15 um diameter (the typical\n# glomerulus of Figure 5D) on the centre, or the region of at least 0.2 there. Stabilization as\n# in M1 is assumed, as the Methods apply it to every plane.\n# (M4) Identifying PGb, PGa and 6G, from their definitions in the Results. PGb is the ROI that\n# responds (M2) to 4-methyl-3-heptanone, 4-methyl-3-heptanol and 4-methyl-3-hexanol; 6G the\n# adjacent ROI, lateral to PGb, that responds to 6MHO; PGa the adjacent ROI, anterior to PGb,\n# that responds to 4-methyl-3-heptanol and 4-methyl-3-hexanol and not to 4-methyl-3-heptanone.\n# All three lie in one optical plane, in the anterior ventral hemi-lobe next to a gap without\n# glomeruli. Image axes are taken as the anatomical axes, as the figures' L and A labels imply;\n# if the files give an orientation, it is used.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000467\"\npaper: doi:10.1016/j.cell.2023.05.025\nclaims:\n- id: fig1cd-new-pheromones-leave-nest\n  statement: Both 4-methyl-3-hexanol and 6MHO cause wild-type ants to leave the initial nest pile\n    and the initial nest chamber, compared with the vehicle control.\n  source: Results, Alarm pheromones elicit a range of behavioral responses, paragraph 1; Figure 1C-D\n  quote: Both compounds caused ants to leave the initial nest pile (consisting of at least 2 adult\n    workers and at least 1 egg) and the initial nest chamber\n  statistics:\n  - test: two-way repeated measures ANOVA, Dunnett's multiple comparisons test against vehicle\n      control at each timepoint\n    p: 0.05\n    p_relation: \"<\"\n  data: dataset\n  criterion: The paper's test (Methods, Colony alarm bioassay) on hand-scored counts of ants\n    outside the nest pile and outside the nest chamber, from 1 minute before to 2 minutes after\n    the stimulus, two-way repeated measures ANOVA and Dunnett's test against vehicle at each\n    timepoint. Reproduced when, for each compound and each of the two measures, at least one\n    post-stimulus timepoint differs from vehicle at p < 0.05. The behaviour videos are not\n    named among the paper's deposits.\n- id: fig1e-categorical-response\n  statement: In blinded categorization, 4-methyl-3-heptanone, 4-methyl-3-heptanol, their blend\n    and 4-methyl-3-hexanol caused immediate panic alarm (nest pile disassembled within one\n    minute) in at least 80% of trials, while the most common response to 6MHO was \"ants leave\n    nest\", the nest pile persisting for more than one minute.\n  source: Results, Alarm pheromones elicit a range of behavioral responses, paragraph 1; Figure 1E\n  quote: all caused the ants to rapidly leave and disassemble the nest pile ... within one minute\n    after exposure in at least 80% of trials. We call this response \"immediate panic alarm\". The\n    most common response to 6-methyl-5-hepten-2-one was for the majority of ants to slowly walk\n    away from the nest, while the nest pile persisted for more than one minute\n  data: dataset\n  expected:\n  - quantity: lowest fraction of trials with immediate panic alarm among the four panic compounds\n    value: 0.8\n    tolerance: 0.08\n  criterion: Each video classified as in the Methods (immediate panic alarm, ants leave nest, no\n    immediate response). Reproduced when each of the four compounds gives immediate panic in at\n    least 72% of trials (80% less 10%) and \"ants leave nest\" is the most frequent class for 6MHO.\n    Trials per compound, from Table S2, are 17, 11, 9, 10 and 10 (heptanone, heptanol, blend,\n    hexanol, 6MHO).\n- id: fig1f-hexanol-like-native\n  statement: 4-methyl-3-hexanol disassembles the nest pile as fast as the native O. biroi alarm\n    pheromones; the time the initial pile persists does not differ from 4-methyl-3-heptanone,\n    4-methyl-3-heptanol or the blend.\n  source: Results, Alarm pheromones elicit a range of behavioral responses, paragraph 1; Figure 1F;\n    Table S2\n  quote: treatment with 4-methyl-3-hexanol led to similarly rapid disassembly of the nest as\n    4-methyl-3-heptanone, 4-methyl-3-heptanol, and the blend\n  statistics:\n  - about: 4-methyl-3-hexanol against 4-methyl-3-heptanone, mean difference -2.049\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.99\n    p_relation: \">\"\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: -22.87\n      high: 18.78\n    n: 10 and 17 trials\n  - about: 4-methyl-3-hexanol against 4-methyl-3-heptanol, mean difference 7.805\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.97\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: -15.03\n      high: 30.64\n    n: 10 and 11 trials\n  - about: 4-methyl-3-hexanol against the blend, mean difference 8.724\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.96\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: -15.29\n      high: 32.73\n    n: 10 and 9 trials\n  data: dataset\n  criterion: A claim of absence, judged on the paper's test. The percentage of the first two\n    minutes after the stimulus during which the initial pile (at least one egg and two adults in\n    the same area) persists, per trial; one-way ANOVA over the six treatments and Sidak's test of\n    each new compound against each native one. Reproduced when none of the three hexanol\n    comparisons has adjusted p < 0.05; the mean differences are reported either way.\n- id: fig1f-mho-differs\n  statement: With 6MHO the initial nest pile persists significantly longer than with each native\n    alarm pheromone, and its outcomes vary widely.\n  source: Results, Alarm pheromones elicit a range of behavioral responses, paragraph 1; Figure 1F;\n    Table S2\n  quote: treatment with 6-methyl-5-hepten-2-one produced a wide range of outcomes, and the average\n    response was significantly different from responses to clonal raider ant alarm pheromones\n  statistics:\n  - about: 6MHO against 4-methyl-3-heptanone, mean difference 20.92\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.048\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: 0.096\n      high: 41.75\n    n: 10 and 17 trials\n  - about: 6MHO against 4-methyl-3-heptanol, mean difference 30.77\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.0025\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: 7.94\n      high: 53.61\n    n: 10 and 11 trials\n  - about: 6MHO against the blend, mean difference 31.69\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.0032\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: 7.69\n      high: 55.70\n    n: 10 and 9 trials\n  data: dataset\n  criterion: As for fig1f-hexanol-like-native. Reproduced when all three 6MHO comparisons have\n    adjusted p < 0.05 with 6MHO persisting longer; partially reproduced for one or two.\n- id: fig1f-vehicle-differs\n  statement: After the vehicle control the initial nest pile persists far longer than after any\n    native alarm pheromone.\n  source: Figure 1F; Table S2\n  quote: non- O. biroi alarm pheromones and the vehicle control were compared to known O. biroi\n    alarm pheromones for (F)\n  statistics:\n  - about: vehicle against 4-methyl-3-heptanone, mean difference 78.87\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: 56.47\n      high: 101.3\n    n: 8 and 17 trials\n  - about: vehicle against 4-methyl-3-heptanol, mean difference 88.72\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: 64.44\n      high: 113.0\n    n: 8 and 11 trials\n  - about: vehicle against the blend, mean difference 89.4\n    test: one-way ANOVA, Sidak's multiple comparisons test\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Sidak\n    ci:\n      level: 0.95\n      low: 64.25\n      high: 115.0\n    n: 8 and 9 trials\n  data: dataset\n  criterion: As for fig1f-hexanol-like-native. Reproduced when all three comparisons have\n    adjusted p < 0.05 with the vehicle persisting longer.\n- id: table1-transgenesis\n  statement: piggyBac injection of eggs yielded one stable transgenic line from the four pooled\n    treatments (overall efficiency 0.00021, transformation efficiency 0.026) and one from the\n    last treatment (0.0028 and 0.059); higher rates of fluorescent G0s came from eggs under 3\n    hours old, and mixes above 110 ng/uL mRNA gave low hatch rates and no fluorescent G0s.\n  source: Results, Creation of transgenic ants; Methods, Egg collection, microinjection, and larval\n    rearing; Table 1\n  quote: Higher rates of fluorescent G0s were obtained when eggs were <3 hours old ... than <5 hours\n    old at the time of injection. Mixes with >110ng/μL mRNA concentrations produced low hatch rates\n    and no fluorescent G0s\n  data: dataset\n  expected:\n  - quantity: overall efficiency, first four treatments pooled\n    value: 0.00021\n    tolerance: 0.000021\n  - quantity: transformation efficiency, first four treatments pooled\n    value: 0.026\n    tolerance: 0.0026\n  - quantity: overall efficiency, last treatment\n    value: 0.0028\n    tolerance: 0.00028\n  - quantity: transformation efficiency, last treatment\n    value: 0.059\n    tolerance: 0.0059\n  criterion: Efficiencies as Table 1 defines them (lines over eggs injected; lines over G0 adults\n    eclosed). Injection records are not named among the paper's deposits.\n- id: fig2b-s1a-transgene-fluorescence\n  statement: Transgenic pupae show GCaMP6s fluorescence in the antennae and broadly visible DsRed\n    under epifluorescence, unlike wild type.\n  source: Results, Characterization of transgenic ants, paragraph 1; Figure 2B; Figure S1A\n  quote: Transgenic pupae had detectable GCaMP6s fluorescence in the antennae, consistent with\n    expression in OSNs, and DsRed was broadly visible under epifluorescence\n  data: dataset\n  criterion: A qualitative comparison of transgenic and wild-type pupae images; the epifluorescence\n    images are not named among the paper's deposits.\n- id: fig2cd-gcamp-in-osns\n  statement: GCaMP6s labels the great majority of Orco-positive cells in the antennal club, and\n    in the ALs GCaMP6s co-localizes with Orco in OSN afferents.\n  source: Results, Characterization of transgenic ants, paragraph 1; Figure 2C-D\n  quote: GCaMP6s labels the great majority of Orco-positive cells ( Fig. 2C ). In the ALs, high\n    levels of GCaMP6s co-localized with Orco, which labels OSN afferents\n  data: elsewhere\n  where: Brain Image Library IDs 7b20a5b168a92088, 626fd578e97289bc and c2031d8218de058b (the paper\n    does not say which figure each holds)\n  criterion: The paper gives no count. Anti-GFP and anti-Orco confocal stacks of the antennal club;\n    reproduced when more than half of Orco-positive cells are GFP-positive and AL GFP and Orco\n    signals overlap. Which deposited stacks are these is not stated.\n- id: figs1-expression-outside-al\n  statement: DsRed is expressed at a low level in the ALs, and GCaMP6s is also expressed in parts\n    of the subesophageal zone and central complex; these patterns are consistent across\n    individuals.\n  source: Results, Characterization of transgenic ants, paragraph 1; Figure S1B-D\n  quote: DsRed is expressed at a low level in the ALs, possibly due to leaky expression from\n    ObirOrco ... GCaMP6s is also expressed in parts of the sub-esophageal zone and central complex\n  data: elsewhere\n  where: Brain Image Library IDs 7b20a5b168a92088, 626fd578e97289bc and c2031d8218de058b (the paper\n    does not say which figure each holds)\n  criterion: Qualitative, from the confocal stacks; reproduced when anti-DsRed signal is present in\n    the ALs and GCaMP6s fluorescence in the subesophageal zone and central complex.\n- id: figs2ab-glomerulus-counts\n  statement: Reconstructions of two GCaMP6s ALs found 505 (anti-SYNORF1) and 508 (phalloidin)\n    glomeruli, within the wild-type range; in the second, 502 glomeruli were Orco-positive and all\n    of them GCaMP6s-positive, the 6 Orco-negative ones were the T7 cluster, and 4 of these had\n    weak GCaMP6s.\n  source: Results, Characterization of transgenic ants, paragraph 2; Figure S2A-B\n  quote: From the first AL, we reconstructed 505 glomeruli using anti-SYNORF1 signal ... we\n    reconstructed 508 glomeruli ... we counted 502 Orco-positive glomeruli, all of which were also\n    GCaMP6s-positive ... The 6 glomeruli of the T7 cluster were the only Orco-negative glomeruli\n  data: elsewhere\n  where: Brain Image Library IDs 7b20a5b168a92088, 626fd578e97289bc and c2031d8218de058b (the paper\n    does not say which figure each holds)\n  expected:\n  - quantity: glomeruli in the anti-SYNORF1 reconstruction\n    value: 505\n    tolerance: 50.5\n  - quantity: glomeruli in the phalloidin reconstruction\n    value: 508\n    tolerance: 50.8\n  - quantity: Orco-positive glomeruli, all GCaMP6s-positive\n    value: 502\n    tolerance: 50.2\n  - quantity: T7 glomeruli with weak GCaMP6s, of 6\n    value: 4\n    tolerance: 0.4\n  criterion: Manual segmentation (LABKIT, 1 um z resolution) of the right AL (anti-SYNORF1) and the\n    left AL (anti-Orco and phalloidin), as in the Methods. The segmentations themselves are not\n    named among the deposits, so the stacks would have to be segmented again.\n- id: fig2e-t7-ammc\n  statement: GCaMP6s robustly labels glomeruli of clusters T1 to T6, while T7 signal is weaker and\n    often undetectable and the antennal mechanosensory and motor center is unlabeled, so the line\n    can report from about 99% of glomeruli.\n  source: Results, Characterization of transgenic ants, paragraph 2; Figure 2E\n  quote: While glomeruli in T1-T6 were always robustly labeled by anti-GFP, signal in the T7\n    glomeruli was consistently weaker than in other glomeruli and was often undetectable\n  data: elsewhere\n  where: Brain Image Library IDs 7b20a5b168a92088, 626fd578e97289bc and c2031d8218de058b (the paper\n    does not say which figure each holds)\n  criterion: Qualitative, from anti-GFP and anti-SYNORF1 confocal stacks; reproduced when T7\n    anti-GFP intensity is below that of the other glomeruli and the AMMC shows no anti-GFP signal.\n- id: fig2f-ablation\n  statement: After unilateral antennal ablation, GCaMP6s and anti-Orco signals are greatly reduced\n    across the AL on the ablated side, with no glomerular labeling left, while GCaMP6s in the\n    subesophageal zone and central complex is unaffected; AL GCaMP6s thus comes from the antennae.\n  source: Results, Characterization of transgenic ants, paragraph 2; Figure 2F; Figure S1E\n  quote: While GCaMP6s signal in the sub-esophageal zone and central complex was unaffected ( Fig.\n    S1E ), GCaMP6s and anti-Orco signals were greatly reduced across the entire AL connected to\n    the ablated antenna, and no clear glomerular labeling remained\n  data: elsewhere\n  where: Brain Image Library IDs 7b20a5b168a92088, 626fd578e97289bc and c2031d8218de058b (the paper\n    does not say which figure each holds)\n  criterion: Qualitative; reproduced when AL GCaMP6s and anti-Orco intensity on the ablated side\n    is below that on the intact side and the SEZ and CC signals are bilaterally present.\n- id: ablation-al-volume-trend\n  statement: One month after unilateral antennal ablation, the AL on the ablated side tends to be\n    smaller (mean 165,360 against 209,412 um3), not significantly (n=3).\n  source: Methods, Immunohistochemistry, last paragraph\n  quote: we reconstructed AL volumes from several brains (n=3) and found a non-significant trend\n    toward smaller volumes on the ablated side (means of 165,360μm 3 and 209,412μm 3 for ablated\n    vs. non-ablated ALs, respectively; p=0.073, paired values T-test)\n  statistics:\n  - test: paired t-test\n    p: 0.073\n    n: 3 brains\n  data: elsewhere\n  where: Brain Image Library IDs 7b20a5b168a92088, 626fd578e97289bc and c2031d8218de058b (the paper\n    does not say which figure each holds)\n  expected:\n  - quantity: mean ablated-side AL volume\n    value: 165360\n    tolerance: 16536\n    unit: um3\n  - quantity: mean intact-side AL volume\n    value: 209412\n    tolerance: 20941\n    unit: um3\n  criterion: AL volumes reconstructed from confocal stacks of three ablated brains; a two-sided\n    paired t-test. Reproduced when both means are within tolerance and p is between 0.05 and 0.1\n    (a trend, not significant).\n- id: figs2cf-gcamp-ants-behavior\n  statement: GCaMP6s ants, like wild type, leave the nest pile in response to 4-methyl-3-heptanone,\n    4-methyl-3-heptanol and the 9:1 blend; leaving the nest chamber differs significantly from\n    control only for 4-methyl-3-heptanone and the blend.\n  source: Results, Characterization of transgenic ants, paragraph 3; Figure S2C-F\n  quote: The ants left the nest cluster in response to 4-methyl-3-heptanone, 4-methyl-3-heptanol\n    and the blend, similar to wild types ( Fig. S2C – D ). The effect on leaving the nest chamber\n    was only significantly different from control for 4-methyl-3-heptanone and the blend\n  statistics:\n  - test: two-way repeated measures ANOVA, Dunnett's multiple comparisons test against vehicle\n    p: 0.05\n    p_relation: \"<\"\n  data: dataset\n  criterion: As in fig1cd-new-pheromones-leave-nest, with all GCaMP6s treatments compared with one\n    shared set of vehicle trials (Figure S2 legend), 15 to 20 ants per arena. Reproduced when all\n    three compounds differ from vehicle at some post-stimulus timepoint for ants outside the nest\n    pile, and for ants outside the chamber heptanone and the blend do while heptanol does not.\n- id: figs3-single-insertion\n  statement: The GCaMP6s line carries a single haploid transgene insertion on chromosomal scaffold\n    2, at Chr2 3,870,844 to 3,870,847, within an intron of trace amine-associated receptor 9;\n    normalized read depth is about 1.5 at ObirOrco and about 0.5 over the rest of the insert.\n  source: Results, Characterization of transgenic ants, paragraph 3; Figure S3; Methods, Genome\n    sequencing and genomic analyses\n  quote: The line contains a single, haploid transgene insertion on the 2 nd chromosomal scaffold\n    ( Fig. S3A – B ). The insertion occurred at location Chr2:3,870,844–3,870,847, within an intron\n    of the gene trace amine-associated receptor 9\n  data: elsewhere\n  where: NCBI BioProject PRJNA947257\n  expected:\n  - quantity: normalized read depth at ObirOrco\n    value: 1.5\n    tolerance: 0.15\n  - quantity: normalized read depth over the rest of the insert\n    value: 0.5\n    tolerance: 0.05\n  criterion: The Methods pipeline (Trimmomatic 0.36, bwa mem to Obir_v5.4 GCA_003672135.1 and the\n    linearized plasmid, Picard deduplication, samtools depth -aa, normalization to heterozygous\n    SNPs below twice the genome-wide median depth, junction reads). Reproduced when the depths are\n    within tolerance and the junction reads place the insert at the stated position.\n- id: fig3f-general-odorants-unique\n  statement: Each general odorant activates a unique combination of glomeruli, and the same\n    odorant activates similar AL regions in different individuals.\n  source: Results, Recording calcium responses to general odorants, paragraph 2; Figure 3F\n  quote: each odorant activated a unique combination of glomeruli, and responses to the same\n    odorant occurred in similar regions of the AL in different individuals\n  data: dataset\n  criterion: The paper judged this by eye from M1 maps (n=6 ants, 48%). Fixed here. Within each\n    ant, the M2 sets of responding ROIs differ between every pair of the five odorants. Across\n    ants, the centroid of each odorant's responding pixels (at least 0.2, trial-averaged map), in\n    coordinates scaled to the AL's bounding box in raw fluorescence, lies closer to the same\n    odorant's centroids in the other ants than to other odorants' centroids, in more than half of\n    the ant and odorant cases. Reproduced when both hold under every M2 reading.\n- id: fig3fg-hexanone-broad\n  statement: The breadth of responses varies across general odorants; most activate a few\n    glomeruli, while 3-hexanone activates large regions of the ventral and medial AL.\n  source: Results, Recording calcium responses to general odorants, paragraph 2; Figure 3F-G\n  quote: the breadth of glomerular responses varied dramatically across odorants, with most\n    odorants activating a few glomeruli, while 3-hexanone activated large regions of the\n    ventral/medial AL\n  data: dataset\n  criterion: The paper gives no measure; one is fixed here. Breadth is the area of pixels of at\n    least 0.2 (the Methods threshold) in each ant's trial-averaged M1 map. Reproduced when\n    3-hexanone has the largest area of the five odorants in every ant where it was tested, and\n    its median area across ants is at least twice that of each other odorant.\n- id: figs4a-bilateral-symmetry\n  statement: Responses to 4-methyl-3-hexanol are bilaterally symmetrical in the two ALs imaged\n    together, so later experiments imaged only the right AL.\n  source: Results, Pheromone representation is sparse, paragraph 1; Figure S4A\n  quote: we first imaged responses to 4-methyl-3-hexanol in both ALs simultaneously (n=3 ants) and\n    found that response patterns were bilaterally symmetrical\n  data: dataset\n  criterion: The paper gives no measure; one is fixed here. In each of the three bilateral ants\n    (1X zoom, 4-methyl-3-hexanol 48%), M1 maps split at the midline between the ALs, the left\n    mirrored. Reproduced when in every ant both ALs have responding ROIs (M2) and their counts\n    differ by at most one, and the mirrored-left and right maps of responding pixels correlate\n    better than the right map does with itself shifted by half its width.\n- id: fig4b-vehicle-no-response\n  statement: Sparse, unique subsets of glomeruli respond to each alarm pheromone, while the\n    paraffin oil vehicle generates no responses.\n  source: Results, Pheromone representation is sparse, paragraph 1; Figure 4B-C\n  quote: Sparse, unique subsets of AL glomeruli responded to all pheromones, while the paraffin oil\n    vehicle did not generate responses\n  data: dataset\n  criterion: A claim of absence for the vehicle, on the paper's rule (M2, peak fold change at least\n    0.2). Reproduced when no ROI responds in any ant's vehicle trials, and each pheromone has at\n    least one responding ROI in most ants at their higher concentration, under every M2 reading;\n    the largest vehicle ROI value is reported.\n- id: fig4-no-decreases\n  statement: Odors cause no fluorescence decreases; only small non-specific decreases from shifts\n    in AL position and photobleaching occur.\n  source: Results, Pheromone representation is sparse, paragraph 1\n  quote: We did not observe any fluorescence decreases in response to odor, although we did detect\n    small, non-specific decreases in fluorescence due to minor shifts in AL position and\n    photobleaching\n  data: dataset\n  criterion: A claim of absence. The paper's only threshold is 0.2; it is applied with the sign\n    reversed. M1 with the minimum over planes in place of the maximum (the maximum hides\n    decreases). Reproduced when no glomerulus-sized region (10 to 20 um) reaches -0.2 or below in\n    at least two trials of the same odor and concentration without doing so in that ant's vehicle\n    trials; the most negative such region is reported.\n- id: fig4-large-lasting-responses\n  statement: Fluorescence increases to alarm pheromones are often large (1 to 2-fold change) and\n    outlast the 5 s odor pulse.\n  source: Results, Pheromone representation is sparse, paragraph 1\n  quote: Fluorescence increases were frequently large (1–2-fold change) and lasted longer than the\n    5s odor presentation\n  data: dataset\n  expected:\n    quantity: peak fold change of responding glomeruli (range)\n    value: 1.5\n  criterion: Over responding ROI-trials (M2) at each ant's higher concentration, the ROI peak fold\n    change. \"Frequently large\" is read as the median lying in 1 to 2 widened by 10% of each bound\n    (0.9 to 2.2), under ROI value reading (i) or (ii). \"Lasted longer\" is read with the paper's\n    onset rule (Methods, temporal dynamics); reproduced when, in more than half of those\n    ROI-trials, dF/F0 at the first volume after the pulse ends (8 s) is still above the baseline\n    mean plus 3 SD.\n- id: figs5a-sparse-median-6\n  statement: Each alarm pheromone activates few of the roughly 500 glomeruli; even at the highest\n    concentration the median number of responding glomeruli is at most 6.\n  source: Results, Pheromone representation is sparse, paragraph 2; Figure S5A; Figure 6 legend\n  quote: Even at the highest concentration tested, the four pheromones activated a median of at most\n    6 glomeruli\n  data: dataset\n  expected:\n    quantity: largest median number of responding glomeruli over the four pheromones at 48%\n    value: 6\n    tolerance: 0.6\n  criterion: Counts per ant from M2 (each reading). \"The highest concentration tested\" is read as\n    (a) 48%, the 8 ants of Figure 6, or (b) each ant's higher concentration (13 ants).\n    Reproduced when, under a reading, the median over ants is at most 6.6 for every pheromone.\n- id: figs5a-concentration-more-glomeruli\n  statement: Higher concentrations give more robust responses and a few more glomeruli passing the\n    threshold, while the overall spatial pattern stays similar across concentrations.\n  source: Results, Pheromone representation is sparse, paragraph 2; Figure S5A; Figure S6\n  quote: Higher concentrations produced more robust responses, with a few more glomeruli passing the\n    threshold, but overall spatial response patterns were similar across concentrations\n  data: dataset\n  criterion: The paper shows box plots and no test; a rule is fixed here. Within each ant and\n    pheromone, M2 counts at the higher minus the lower concentration. Reproduced when, pooled over\n    pheromones, positive differences outnumber negative ones by a two-sided sign test at p < 0.05,\n    and in more than half of ant and pheromone pairs every ROI that responds at the lower\n    concentration also responds at the higher one. Shown under every M2 reading.\n- id: figs5b-shared-glomerulus\n  statement: The three compounds that elicit panic alarm (4-methyl-3-heptanone, 4-methyl-3-heptanol,\n    4-methyl-3-hexanol) activate partly overlapping sets of glomeruli, with a single glomerulus,\n    PGb, activated by all three.\n  source: Results, Pheromone representation is sparse, paragraph 2; Figure S5B\n  quote: we observed consistent partial overlap in the response patterns activated by the three\n    compounds eliciting panic alarm responses ... with a single glomerulus activated by all three\n  data: dataset\n  criterion: Per ant at its higher concentration, the number of M2 ROIs responding to all three.\n    Reproduced when, under each M2 reading, the median over ants is 1 and more than half of the\n    ants have exactly one such ROI.\n- id: figs5c-mho-rarely-overlaps\n  statement: 6MHO only rarely and inconsistently activates glomeruli shared with 4-methyl-3-heptanone\n    or 4-methyl-3-hexanol.\n  source: Results, Pheromone representation is sparse, paragraph 2; Figure S5C\n  quote: while we sometimes observed responses to 6-methyl-5-hepten-2-one and either\n    4-methyl-3-heptanone or 4-methyl-3-hexanol in an overlapping region, those occurrences were\n    rare and inconsistent\n  data: dataset\n  criterion: Per ant at its higher concentration, the number of M2 ROIs responding to 6MHO and to\n    any other pheromone (overlaps at different depths excluded, as in the Methods). Reproduced\n    when, under each M2 reading, the median over ants is 0 and the count is non-zero in fewer than\n    half of the ants.\n- id: fig5ab-focal-glomeruli\n  statement: PGb lies in the anterior ventral hemi-lobe next to a gap without glomeruli, about\n    halfway between the dorsal and ventral AL surfaces, with two neighbouring alarm-responsive\n    glomeruli in the same plane; PGb and 6G were found in 13 of 13 ants and PGa in 11 of 13.\n  source: Results, Alarm pheromone-responsive glomeruli are spatially stereotyped, paragraph 1;\n    Figure 5A-B\n  quote: PG b is located approximately halfway between the dorsal and ventral AL surfaces, and is\n    neighbored by two additional glomeruli that respond to alarm pheromones, with all three visible\n    in the same optical plane ... Both glomeruli were identified in 13/13 individuals. In 11/13\n    individuals, we identified a third neighboring glomerulus\n  data: dataset\n  expected:\n  - quantity: ants with PGb identified, of 13\n    value: 13\n    tolerance: 1.3\n  - quantity: ants with 6G identified, of 13\n    value: 13\n    tolerance: 1.3\n  - quantity: ants with PGa identified, of 13\n    value: 11\n    tolerance: 1.1\n  criterion: Identification by M4 on each ant's higher-concentration ROIs (M2, each reading).\n    Reproduced when the counts are within tolerance (12 or 13, 12 or 13, 10 to 12) and, in most\n    ants with PGb, its centre plane lies in the middle third of the AL depth (from the top plane,\n    the dorsal surface, to the deepest plane with AL fluorescence, Methods).\n- id: fig5c-s6-tuning\n  statement: PGb, PGa and 6G each respond to a unique combination of pheromones, with several\n    pheromone and glomerulus pairs giving no response; PGb responds to 4-methyl-3-heptanone,\n    4-methyl-3-heptanol and 4-methyl-3-hexanol and not to 6MHO, PGa to 4-methyl-3-heptanol and\n    4-methyl-3-hexanol, and 6G to 6MHO.\n  source: Results, Alarm pheromone-responsive glomeruli are spatially stereotyped, paragraph 2;\n    Figure 5C; Figure S6\n  quote: while PG b , PG a , and 6G are spatially adjacent, they each reliably respond to unique\n    combinations of odorants, with several pheromone/glomerulus combinations producing no\n    detectable responses ... PG b did not respond to 6-methyl-5-hepten-2-one\n  data: dataset\n  depends_on:\n  - fig5ab-focal-glomeruli\n  criterion: Peak fold change per trial from M3 (each reading), all concentrations, 13 ants (11\n    for PGa). The Methods model, peak response on concentration with a random effect for\n    individual, fitted with \"the glm function\", which has no random effects; readings (a) a\n    linear model with individual as a fixed factor, (b) a linear mixed model with a random\n    intercept per ant. Concentration log-transformed (Figure S6 legend; the base is a standard\n    choice that cannot change the outcome). A combination responds when the model's prediction at\n    48% is at least 0.2 (the Methods threshold) with its 95% CI above 0, and gives no response\n    when the 95% CI at 48% includes 0. Reproduced when the seven named combinations respond, PGb\n    to 6MHO does not, and the three glomeruli's sets of responding pheromones all differ.\n- id: fig5c-6g-slow\n  statement: Responses in PGb and PGa peak and then decline close to baseline by the end of the\n    48 s recording, while 6G responses to 6MHO are very slow, with a plateau of tens of seconds.\n  source: Results, Alarm pheromone-responsive glomeruli are spatially stereotyped, paragraph 2;\n    Figure 5C\n  quote: while responses in PG b and PG a peaked and then declined close to baseline by the end of\n    the recording, responses in 6G were extremely slow, with a fluorescence plateau of tens of\n    seconds\n  data: dataset\n  depends_on:\n  - fig5ab-focal-glomeruli\n  criterion: Mean M3 traces for the robust combinations of the Methods (heptanone in PGb; heptanol\n    and hexanol in PGb and PGa; 6MHO in 6G). The concentration of Figure 5C is not stated;\n    readings (a) 48% (8 ants, as Figure S7C), (b) all concentrations pooled. Thresholds are\n    fixed here. Reproduced when the PGb and PGa mean traces over the last five volumes are below\n    0.2 (the Methods threshold) and below a quarter of their peak, while the 6G trace stays at or\n    above half its peak for at least 20 s.\n- id: figs7a-6g-extended\n  statement: In 144 s recordings, 6G responses to 6MHO plateau for about 30 s and return to\n    baseline about 80 s after odor presentation, sometimes taking more than 100 s.\n  source: Results, Alarm pheromone-responsive glomeruli are spatially stereotyped, paragraph 2;\n    Figure S7A\n  quote: Fluorescence plateaued for ~30s before declining and returning to baseline ~80s after odor\n    presentation\n  data: dataset\n  depends_on:\n  - fig5ab-focal-glomeruli\n  expected:\n  - quantity: plateau duration of the mean 6G trace\n    value: 30\n    tolerance: 3\n    unit: s\n  - quantity: time from odor presentation to return to baseline, mean trace\n    value: 80\n    tolerance: 8\n    unit: s\n  criterion: Single 144 s trials from five ants at 48%, M3 traces of 6G, and their mean. Plateau\n    and return are not defined in the paper. Readings, return to baseline as the first volume\n    after the peak where the mean trace falls (a) below baseline mean plus 3 SD (the Methods onset\n    rule) or (b) below 0.2; plateau as the time the mean trace stays at or above (c) 90% or (d)\n    80% of its peak. Odor presentation read as odor onset at 3 s. Reproduced when, under one\n    reading, both values are within tolerance and at least one trial takes more than 100 s.\n- id: figs7c-temporal-lme\n  statement: Onset and peak times differ by pheromone and glomerulus; for PGb and PGa responses to\n    4-methyl-3-heptanol and 4-methyl-3-hexanol, onset time depends on pheromone, glomerulus and\n    their interaction, and time to maximum on pheromone and glomerulus but not their interaction.\n  source: Results, Alarm pheromone-responsive glomeruli are spatially stereotyped, paragraph 2;\n    Figure S7C legend\n  quote: 'Time to response onset: significant effects of pheromone (p=0.0034), glomerulus (p<0.0001),\n    and the interaction (p=0.0030). Time to response maximum: significant effects of pheromone\n    (p<0.0001) and glomerulus (p=0.047), but not the interaction (p=0.88)'\n  statistics:\n  - about: onset, pheromone\n    test: linear mixed effects model (lme)\n    p: 0.0034\n    n: 8 ants, three trials per condition per ant, 48%\n  - about: onset, glomerulus\n    test: linear mixed effects model (lme)\n    p: 0.0001\n    p_relation: \"<\"\n    n: 8 ants, three trials per condition per ant, 48%\n  - about: onset, pheromone by glomerulus interaction\n    test: linear mixed effects model (lme)\n    p: 0.0030\n    n: 8 ants, three trials per condition per ant, 48%\n  - about: time to maximum, pheromone\n    test: linear mixed effects model (lme)\n    p: 0.0001\n    p_relation: \"<\"\n    n: 8 ants, three trials per condition per ant, 48%\n  - about: time to maximum, glomerulus\n    test: linear mixed effects model (lme)\n    p: 0.047\n    n: 8 ants, three trials per condition per ant, 48%\n  - about: time to maximum, interaction\n    test: linear mixed effects model (lme)\n    p: 0.88\n    n: 8 ants, three trials per condition per ant, 48%\n  data: dataset\n  depends_on:\n  - fig5ab-focal-glomeruli\n  criterion: M3 traces at 48%; baseline the first five frames; onset the latency from stimulus\n    start (3 s) to the first volume where dF/F0 exceeds baseline mean plus 3 SD; time to maximum\n    the latency to the largest dF/F0; traces that never exceed the bound excluded (Methods).\n    Volume times taken as (index - 1) x 1.2 s, a standard choice that shifts all latencies alike.\n    Model per parameter, pheromone, glomerulus and their interaction, random effect for trial\n    nested in ant (lme). How the p-values were taken is not stated; readings (a) anova of the lme\n    fit, sequential F-tests in the order the Methods list, (b) marginal F-tests, (c) the t-tests\n    of the coefficients in its summary. Reproduced when, under every reading, the five effects\n    have p < 0.05 and the time-to-maximum interaction has p of 0.05 or more (a claim of absence on\n    the paper's test); partially reproduced when three or four of the five hold.\n- id: fig5d-stereotyped-positions\n  statement: PGa is always anterior (12.9 +/- 1.9 SD um) and slightly lateral (5.1 +/- 2.9 um) to\n    PGb, and 6G always lateral to PGb (13.1 +/- 2.6 um) at a similar anterior-posterior position\n    (0.6 +/- 2.2 um); the SDs are much smaller than a glomerulus diameter, so the three occupy\n    stereotyped positions.\n  source: Results, Alarm pheromone-responsive glomeruli are spatially stereotyped, paragraph 3;\n    Figure 5D\n  quote: 'PG a was always located anterior (mean distance between centers: 12.9±1.9SD μm), and\n    slightly lateral (mean distance: 5.1±2.9SD μm) to PG b ( Fig. 5D ). In comparison, 6G was always\n    lateral to PG b (mean distance: 13.1±2.6SD μm), and in a similar position along the\n    anterior-posterior axis (mean distance: 0.6±2.2SD μm)'\n  data: dataset\n  depends_on:\n  - fig5ab-focal-glomeruli\n  expected:\n  - quantity: PGa anterior offset from PGb\n    value: 12.9\n    tolerance: 1.9\n    unit: um\n  - quantity: PGa lateral offset from PGb\n    value: 5.1\n    tolerance: 2.9\n    unit: um\n  - quantity: 6G lateral offset from PGb\n    value: 13.1\n    tolerance: 2.6\n    unit: um\n  - quantity: 6G anterior offset from PGb\n    value: 0.6\n    tolerance: 2.2\n    unit: um\n  criterion: Tolerances are the paper's SDs. One plane per ant where all three are visible\n    (n=11 for PGa, 13 for 6G), PGb at (0,0), 0.289 um per pixel. The centres were placed by hand;\n    readings (a) the centroid of each glomerulus's responding pixels (at least 0.2) to its defining\n    odor (M4) in that plane, (b) its peak pixel; and the plane from (c) one higher-concentration\n    trial or (d) the mean over that ant's higher-concentration trials. Reproduced when, under one\n    reading, the four means are within tolerance, PGa is anterior in every ant and 6G lateral in\n    every ant, and each SD is below 10 um. If the files give no orientation, only distances are\n    tested and the claim is at most partially reproduced.\n- id: fig6-shared-panic-pathway\n  statement: The three pheromones with overlapping AL responses all elicit panic alarm, while 6MHO\n    does not elicit panic and gives a non-overlapping response, pointing to a shared pathway for\n    panic alarm centred on PGb.\n  source: Results, Alarm pheromone-responsive glomeruli are spatially stereotyped, paragraph 4;\n    Figure 6\n  quote: The three pheromones with overlapping calcium response patterns all robustly elicited panic\n    alarm behavior, while 6-methyl-5-hepten-2-one did not elicit panic alarm behavior and generated\n    a non-overlapping response\n  data: dataset\n  depends_on:\n  - figs5b-shared-glomerulus\n  - figs5c-mho-rarely-overlaps\n  - fig1e-categorical-response\n  criterion: The synthesis of the claims it depends on. The imaging half is tested here; the\n    behaviour half rests on fig1e-categorical-response, whose data are not in the dataset.\n    Reproduced in its imaging half when figs5b-shared-glomerulus and figs5c-mho-rarely-overlaps\n    are reproduced; the claim is reported as partially tested.\n"
}
```

```
File created successfully at: claims/000467/10.1016-j.cell.2023.05.025.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/000467/10.1016-j.cell.2023.05.025.yaml paper/10.1016-j.cell.2023.05.025.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && grep -o "found a non-significant.\{0,200\}" paper/*.txt | od -c | sed -n 1,30p | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import sys,yaml;sys.path.insert(0,'tools');import claims_check as c
d=yaml.safe_load(open('claims/000467/10.1016-j.cell.2023.05.025.yaml'))
q=[x for x in d['claims'] if x['id']=='ablation-al-volume-trend'][0]['quote']
t=c.norm(open('paper/10.1016-j.cell.2023.05.025.txt').read())
qq=c.norm(q)
for i in range(10,len(qq),10):
  if qq[:i] not in t: print(repr(qq[:i]));break
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000467/10.1016-j.cell.2023.05.025.yaml",
 "old_string": "  quote: we reconstructed AL volumes",
 "new_string": "  quote: We therefore reconstructed AL volumes"
}
```

```
The file claims/000467/10.1016-j.cell.2023.05.025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000467/10.1016-j.cell.2023.05.025.yaml paper/10.1016-j.cell.2023.05.025.txt; grep -n -i "rather\|—" claims/000467/*.yaml; grep -nE "^\s+[a-z_]+: [^'\"].*: " claims/000467/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes. One last scan for ": " inside plain scalars on continuation lines.

**Agent calls Bash**

```bash
grep -nE ": " claims/000467/*.yaml | grep -vE "^[0-9]+:#" | grep -vE "^[0-9]+:\s*-?\s*[a-z_]+: " | head; grep -nE "^[0-9]*.*[a-z_]+: [^'\"\n].*: " claims/000467/*.yaml | grep -v ":#" | head
```

```
643:    and the interaction (p=0.0030). Time to response maximum: significant effects of pheromone
693:    slightly lateral (mean distance: 5.1±2.9SD μm) to PG b ( Fig. 5D ). In comparison, 6G was always
694:    lateral to PG b (mean distance: 13.1±2.6SD μm), and in a similar position along the
695:    anterior-posterior axis (mean distance: 0.6±2.2SD μm)'
```

**Agent**

I've written the claims file at `claims/000467/10.1016-j.cell.2023.05.025.yaml`. `tools/claims_check.py` passes it with 32 claims, 32 quotes, 36 statistical values and 0 problems. Nothing is committed.

**Text read.** The PubMed Central author manuscript (PMC10334690, NIHMS1904919), not the version of record. That covers the Results, STAR Methods, Key Resources Table, the legends of Figures 1 to 6, Table 1 and Figures S1 to S7, and the supplement PDF (Tables S1 to S4). I did not read the supplemental videos. There is no PDF of the main text, so I could not read values shown only in figures (the medians on Fig. 6, the boxes of Fig. S5, the vectors of Fig. 5D). Every claim rests on numbers printed in the text.

**Code.** The repository linked in the paper (`HartKronauer2023`) returns 404. I read the lab's `Hart_Kronauer2023` instead, at commit 72d041a; its README names this paper and dandiset 000467. It holds:
- an NWB-to-TIFF converter, which keeps only trials t288, t293, t284 and t290 through a hard-coded filter the Methods never mention (I flagged it so the author doesn't copy it);
- the ImageJ macro for the peak maps. It fixes the stabilizer settings and that frames are counted from 1. It also clips values before the minimum filter, where the Methods filter first; I kept the Methods order as the main reading and the macro's as a variant.

The ROI drawing, the single-glomerulus traces and the R and GraphPad analyses are not in the repository.

**Claims.** 32 in all, every one with a quote. Seven carry statistics: the Fig. 1F / Table S2 Šidák tests with their confidence intervals, the behaviour Dunnett tests, the ablation paired t-test (p = 0.073), and the six Fig. S7C mixed-model p-values. Eleven have expected values and 30 have criteria. By data:
- **In the dataset (calcium imaging), 17 claims.** Several criteria had to be fixed by me because the paper judged them by eye: general odorants, 3-hexanone breadth, bilateral symmetry, absence of decreases, concentration effect and the Fig. 5C dynamics. Each criterion says so.
- **Data the paper never deposited, 7 claims:** the behaviour videos (Fig. 1C to F, S2C to F), Table 1 and the pupa images. These are recorded as `data: dataset` and will be blocked as `data_missing`.
- **Deposited elsewhere, 8 claims:** confocal stacks in the Brain Image Library (the paper doesn't say which of its three IDs holds which figure) and the genome in NCBI BioProject PRJNA947257.

**Details the paper leaves open, with the readings named:**
- **How ROIs are drawn:** connected regions at or above 0.2 that recur in two trials, or the same restricted to glomerulus-sized regions (10 to 20 µm).
- **ROI value:** mean or maximum over its pixels.
- **Counting responding glomeruli:** trial-averaged value at or above 0.2 (Methods), or counts per trial averaged over trials (Fig. S5 legend).
- **Which "highest concentration":** 48% in 8 ants, or each ant's higher concentration in 13 ants.
- **Single glomeruli:** the centre plane is the one where the glomerulus is largest or where its response peaks; the ROI is a 15 µm disc or the region at or above 0.2.
- **Fig. S6 model:** the Methods say "glm with a random effect"; read as individual as a fixed factor, or as a random intercept.
- **Fig. S7C p-values:** sequential F-tests, marginal F-tests, or coefficient t-tests.
- **Concentration in Fig. 5C:** 48%, or all concentrations pooled.
- **Plateau and return to baseline in Fig. S7A:** 90% or 80% of peak; baseline plus 3 SD, or 0.2.
- **Fig. 5D centres:** response centroid or peak pixel, from one trial or the mean over trials.
- **Image orientation:** taken as the figures' L/A axes. If the files give none, Fig. 5D's direction claims are at most partially reproduced.

**Missing from the paper:** the behaviour, transgenesis and pupa-imaging data are not deposited anywhere the paper names. The mapping of the Brain Image Library IDs to figures is not given. The analysis steps above, apart from the peak-map macro, have no code.

## End of run

30 turns, 7 minutes, result: success.
