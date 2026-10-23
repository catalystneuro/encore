# 000034 · claims · run 39700724695

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/ | head -50; ls claims/000034 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 30,200p claims/001453/*.yaml
```

```
paper: doi:10.1016/j.cub.2025.04.027
claims:
- id: stimulus-code-link
  kind: link
  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
    the paper's analysis code and the protocol file of its stimulus software, and the values
    computed through that link agree with those the paper's code printed.
  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
  data: with_labels
  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
    the counts per species are compared instead. The sign of the zebrafish turning response
    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
    is lateral right.
- id: fig1d-dc-faster-all-codes
  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/10.7554-elife.61834.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.61834.txt",
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' 10.7554-elife.61834.txt | sort -t: -k2 -n -r | head;
```

```
32: 62110
7: 35990
28: 14424
23: 7655
11: 4378
17: 2635
21: 2148
26: 2060
14: 1671
19: 1149
```

**Agent calls Bash**

```bash
cd  sed -n 7p paper/10.7554-elife.61834.txt | fold -w 4000 -s
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -w 200 -s paper/10.7554-elife.61834.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 330
}
```

```
1	DOI: 10.7554/elife.61834
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC7704107), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	1894 elife eLife eLife eLife Sciences Publications, Ltd PMC7704107 7704107 7704107 33170122 10.7554/eLife.61834 SpikeInterface, a unified framework for spike sorting Buccino Alessio P 1 2 † ✉ Hurwitz 
8	Cole L 3 † Garcia Samuel 4 Magland Jeremy 5 Siegle Joshua H 6 Hurwitz Roger 7 Hennig Matthias H 3 Colgin Laura L Reviewing Editor 8 Colgin Laura L Senior Editor 9 1 Department of Biosystems Science 
9	and Engineering, ETH Zurich, Zürich, Switzerland 2 Centre for Integrative Neuroplasticity (CINPLA), University of Oslo, Oslo, Norway 3 School of Informatics, University of Edinburgh, Edinburgh, 
10	United Kingdom 4 Centre de Recherche en Neuroscience de Lyon, CNRS, Lyon, France 5 Flatiron Institute, New York, United States 6 Allen Institute for Brain Science, Seattle, United States 7 
11	Independent Researcher, Portland, United States 8 University of Texas at Austin, United States 9 University of Texas at Austin, United States † These authors contributed equally to this work. ✉ 
12	Corresponding author. 10 11 2020 9 e61834 e61834 2 12 2020 © 2020, Buccino et al This article is distributed under the terms of the Creative Commons Attribution License , which permits unrestricted 
13	use and redistribution provided that the original author and source are credited. Abstract Much development has been directed toward improving the performance and automation of spike sorting. This 
14	continuous development, while essential, has contributed to an over-saturation of new, incompatible tools that hinders rigorous benchmarking and complicates reproducible analysis. To address these 
15	limitations, we 
[... 315 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 330,
 "limit": 120
}
```

```
330	https://github.com/SpikeInterface/spikely ; Hurwitz et al., 2020 ), a PyQt-based GUI that allows for simple construction of complex spike sorting pipelines. With spikely , users can build workflows 
331	that include: (i) loading a recording and a probe file; (ii) performing pre-processing on the underlying recording with multiple processing steps; (iii) running any spike sorter supported by 
332	SpikeInterface on the processed recording; (iv) automatically curating the sorter’s output; and (v) exporting the final result to a variety of file formats, including Phy. At its core, spikely 
333	utilizes SpikeInterface’s Python API to run any constructed spike sorting workflow. This ensures that the functionality of spikely grows organically with that of SpikeInterface. Figure 6C shows a 
334	screenshot from spikely where the pipeline in Figure 6A is constructed. Each stage of the pipeline is added using drop-down lists, and all the parameters (which were not left at their default values) 
335	are set in the right-hand panel. Once a pipeline is constructed in spikely , the user can save it using the built-in save functionality and then load it back into spikely at a later date. Since 
336	spikely is cross-platform and user-friendly, we believe it can be utilized to increase the accessibility and reproducibility of spike sorting. Discussion In this paper, we introduced SpikeInterface, 
337	a Python framework designed to enhance the accessibility, reliability, efficiency, and reproducibility of spike sorting. To illustrate the use-cases and advantages of SpikeInterface, we performed a 
338	detailed meta-analysis that included: quantifying the agreement among six modern sorters on a real dataset, benchmarking each sorter on a simulated ground-truth recording, and investigating the 
339	performance of a consensus-based spike sorting and how it compares with manually curated results. To highlight the modular design of SpikeInterface, we then provided descriptions and code 
[... 110 more lines not kept]
```

**Agent**

The paper's full text is present: main text, Methods, and a supplement file. Now checking what follows the references.

**Agent calls Bash**

```bash
cd /tmp/claude-1001; grep -n -i -E "supplement|decision letter|author response|transparent|^=|-----" p.txt | sed -n 1,60p | cut -c1-200; sed -n 9,40p paper/10.7554-elife.61834.txt | cut -c1-300
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 497,
 "limit": 215
}
```

```
497	processing and analysis. BioMedical Engineering OnLine. 2017;16:129.  doi: 10.1186/s12938-017-0419-7. eLife eLife 10.7554/eLife.61834.sa1 Decision letter Colgin Laura L Reviewing Editor 1 Grün Sonja 
498	Reviewer 2 Kloosterman Fabian Reviewer 3 1 University of Texas at Austin, United States 2 Jülich Research Centre, Germany 3 KU Leuven, Belgium In the interests of transparency, eLife publishes the 
499	most substantive revision requests and the accompanying author responses. Acceptance summary: SpikeInterface is an integrated set of tools that makes it straightforward for researchers to set up a 
500	complete spike sorting workflow. SpikeInterface supports many common data formats and modern spike sorters and provides post-processing tools for characterization of the spike sorting results. This 
501	allows for validation and comparison of multiple spike sorting results. Results suggest that combining the results of multiple spike sorters could help to reduce the number of false positive units, 
502	which is an interesting future direction that will likely inspire further investigation. This tool is expected to be useful for researchers in many different areas who are studying neuronal 
503	responses. Decision letter after peer review: [Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first 
504	round of review.] Thank you for submitting your work entitled "SpikeInterface, a unified framework for spike sorting" for consideration by eLife . Your article has been reviewed by a Senior Editor, a 
505	Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Fabian Kloosterman (Reviewer #2). Our decision has been 
506	reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered furt
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; sed -n 712,730p p.txt | cut -c1-150; sed -n 1210,1336p p.txt | cut -c1-200
```

```
[HYPERLINKS]
http://creativecommons.org/licenses/by/4.0/
https://pypi.org/project/spikeinterface/
https://spikeinterface.github.io/
https://gui.dandiarchive.org/#/dandiset/000034/draft
https://spikeinterface.github.io/blog/ensemble-sorting-of-a-neuropixels-recording
https://gui.dandiarchive.org/#/dandiset/000034/draft
https://spikeinterface.github.io/blog/ensemble-sorting-of-a-neuropixels-recording-2/
https://gui.dandiarchive.org/#/dandiset/000034/draft
https://spikeinterface.github.io/blog/ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina/
https://spikeinterface.github.io/blog/ensemble-sorting-of-a-neuropixels-recording-2/
https://spikeinterface.github.io/blog/ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina/
https://spikeinterface.github.io/blog/ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording/
https://spikeforest.flatironinstitute.org/
https://github.com/SpikeInterface/spikeextractors
https://github.com/SpikeInterface/spiketoolkit
https://github.com/AllenInstitute/ecephys_spike_sorting
https://github.com/SpikeInterface/spikesorters
##### Supplement: elife-61834-transrepform.pdf

[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/SpikeInterface/spikeinterface.github.io.git si_blog 2>&1 | tail -3; cd si_blog && git log -1 --format='%H %cd' && ls; ls blog 2>/dev/null | head -50
```

```
657c6d83c282fd787a4cad5bbc92c80403f093b4 Wed Feb 22 09:35:26 2023 +0100
LICENSE
README.md
conf.py
images
pages
posts
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/si_blog && ls posts pages; git log --format='%h %cd %s' | tail -40
```

```
pages:
index.rst

posts:
check-if-duration-affects-spike-sorting.ipynb
collision-paper-generate-recordings.ipynb
collision-paper-simulated-recordings.ipynb
collision-paper-spike-sorting-performance.ipynb
compare-old-vs-new-spikeinterface-api.ipynb
draft_parameters_grid.py
ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina.ipynb
ensemble-sorting-of-a-neuropixels-recording-2.ipynb
ensemble-sorting-of-a-neuropixels-recording.ipynb
example-of-ground-truth-comparison-study.ipynb
example-of-parameters-optimization.ipynb
ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording.ipynb
marques-smith-neuropixel-384ch-paired-recording.ipynb
probeinterface-paper-figures.ipynb
quick-benchmarck-with-new-api-and-new-sorters-april-2021.ipynb
sortingcomponentsoverview.ipynb
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/si_blog && for f in ensemble-sorting-of-a-neuropixels-recording ensemble-sorting-of-a-neuropixels-recording-2 ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording; do echo "== $f"; git log --format='%h %cd' -- posts/$f.ipynb | head -5; done
```

```
== ensemble-sorting-of-a-neuropixels-recording
ee08fb6 Tue Sep 29 17:43:37 2020 +0200
acc5de6 Tue Sep 1 22:19:29 2020 +0100
b260501 Mon Aug 24 22:15:04 2020 +0100
90cb653 Sun Aug 23 16:36:46 2020 +0100
04f51c6 Sun Aug 23 16:34:39 2020 +0100
== ensemble-sorting-of-a-neuropixels-recording-2
ee08fb6 Tue Sep 29 17:43:37 2020 +0200
4beb4b8 Wed Aug 26 09:45:44 2020 +0200
c6c9e9a Tue Aug 25 10:53:24 2020 +0100
== ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina
ee08fb6 Tue Sep 29 17:43:37 2020 +0200
0054bce Wed Sep 2 11:11:12 2020 +0100
c6c9e9a Tue Aug 25 10:53:24 2020 +0100
== ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording
ee08fb6 Tue Sep 29 17:43:37 2020 +0200
4beb4b8 Wed Aug 26 09:45:44 2020 +0200
90cb653 Sun Aug 23 16:36:46 2020 +0100
04f51c6 Sun Aug 23 16:34:39 2020 +0100
Shell cwd was reset to
```

**Agent**

The analysis notebooks were last changed at commit ee08fb6 (29 Sep 2020), before publication. Dumping their code and printed outputs.

**Agent calls Bash**

```bash
cd $TMPDIR/si_blog/posts && cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
    src=''.join(c['source'])
    print('#### ['+c['cell_type']+']'); print(src)
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain')
        if t: print('>>> '+''.join(t)[:1500])
EOF
python $TMPDIR/dump.py ensemble-sorting-of-a-neuropixels-recording.ipynb
```

```
#### [markdown]
# Ensemble sorting of a Neuropixels recording

This notebook reproduces figures 1 and 4 from the paper [**SpikeInterface, a unified framework for spike sorting**](https://www.biorxiv.org/content/10.1101/796599v2).

The data set for this notebook is available on the Dandi Archive: [https://gui.dandiarchive.org/#/dandiset/000034](https://gui.dandiarchive.org/#/dandiset/000034)

The entire data archive can be downloaded with the command `dandi download https://gui.dandiarchive.org/#/dandiset/000034/draft` (about 75GB).

Files required to run the code are:
- the raw data: [sub-mouse412804_ecephys.nwb](https://girder.dandiarchive.org/api/v1/item/5f2b250fee8baa608594a166/download)
- two manually curated sortings: 
    - [sub-mouse412804_ses-20200824T155542.nwb](https://girder.dandiarchive.org/api/v1/item/5f43c74cbf3ae27e069e0aee/download)
    - [sub-mouse412804_ses-20200824T155543.nwb](https://girder.dandiarchive.org/api/v1/item/5f43c74bbf3ae27e069e0aed/download)

These files should be in the same directory where the notebook is located (otherwise adjust paths below).

Author: [Matthias Hennig](http://homepages.inf.ed.ac.uk/mhennig/), University of Edinburgh, 24 Aug 2020
#### [markdown]
### Requirements
[... 467 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/si_blog/posts && python $TMPDIR/dump.py ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording.ipynb
```

```
#### [markdown]
# Ground-truth comparison and ensemble sorting of a synthetic Neuropixels recording

This notebook reproduces figures 2 and 3 from the paper [**SpikeInterface, a unified framework for spike sorting**](https://www.biorxiv.org/content/10.1101/796599v2).

The data set for this notebook is available on the Dandi Archive: [https://gui.dandiarchive.org/#/dandiset/000034](https://gui.dandiarchive.org/#/dandiset/000034).

The entire data archive can be downloaded with the command `dandi download https://gui.dandiarchive.org/#/dandiset/000034/draft` (about 75GB).

The data file required to run the code is:
- the raw data: [sub-MEAREC-250neuron-Neuropixels_ecephys.nwb](https://girder.dandiarchive.org/api/v1/item/5f2c0e33ee8baa608594a16b/download)

This file should be in the same directory where the notebook is located (otherwise adjust paths below).

Author: [Matthias Hennig](http://homepages.inf.ed.ac.uk/mhennig/), University of Edinburgh, 22 Aug 2020
#### [markdown]
### Requirements

For this need you will need the following Python packages:

[... 444 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/si_blog/posts && for f in ensemble-sorting-of-a-neuropixels-recording-2 ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina; do echo "=========== $f"; python $TMPDIR/dump.py $f.ipynb | grep -v -E "^>>> <(Figure|matplotlib)"; done
```

```
=========== ensemble-sorting-of-a-neuropixels-recording-2
#### [markdown]
# Ensemble sorting of a Neuropixel recording (2)

This notebook reproduces supplemental figure S2 from the paper [**SpikeInterface, a unified framework for spike sorting**](https://www.biorxiv.org/content/10.1101/796599v2).

The recording was made by [André Marques-Smith](https://andremarques-smith.com/) in the lab of [Adam Kampff](https://kampff-lab.github.io/sc.io/Paired%20Recordings/). Reference:

Marques-Smith, A., Neto, J.P., Lopes, G., Nogueira, J., Calcaterra, L., Frazão, J., Kim, D., Phillips, M., Dimitriadis, G., Kampff, A.R. (2018). Recording from the same neuron with high-density CMOS probes and patch-clamp: a ground-truth dataset and an experiment in collaboration. bioRxiv 370080; doi: https://doi.org/10.1101/370080

The data set for this notebook is available on the Dandi Archive: [https://gui.dandiarchive.org/#/dandiset/000034](https://gui.dandiarchive.org/#/dandiset/000034)

The entire data archive can be downloaded with the command `dandi download https://gui.dandiarchive.org/#/dandiset/000034/draft` (about 75GB).

File required to run the code:
- the raw data: [sub-c1_ecephys.nwb](https://girder.dandiarchive.org/api/v1/item/5f2e9568ee8baa608594bcaa/download)

This file should be in the same directory where the notebook is located (otherwise adjust paths below).

Author: [Matthias Hennig](http://homepages.inf.ed.ac.uk/mhennig/), University of Edinburgh, 25 Aug 2020
[... 403 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/si_blog && grep -l -E "itertools|combinations|keep_good_only" posts/*.ipynb; git show ee08fb6 --stat | head; ls paper/; ls tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/SpikeInterface/spikecomparison.git sc 2>&1|tail -2; cd sc && git tag | tail -15; git checkout -q 0.2.6 2>&1 || git log --oneline | head -3; git rev-parse HEAD; ls spikecomparison
```

```
0.1.0
0.1.1
0.1.2
0.2.0
0.2.1
0.2.2
0.2.3
0.2.4
0.2.5
0.2.6
0.3.0
0.3.1
0.3.2
0.3.3
6ad882af3c0c5206e4aaabfb074bb2f0b75d2f9b
__init__.py
basecomparison.py
comparisontools.py
groundtruthcomparison.py
groundtruthstudy.py
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sc/spikecomparison && grep -n -E "def (compare|__init__|run_comparisons|get_well|get_false|get_redundant|get_overmerged|count_|_do_|get_agreement_sorting|compute_subgraphs)|_score=|delta_time=|chance_score|exhaustive|match_mode" *.py | cut -c1-220
```

```
basecomparison.py:19:    def __init__(self, sorting_list, name_list=None, delta_time=0.4, sampling_frequency=None,
basecomparison.py:20:                 match_score=0.5, chance_score=0.1, n_jobs=-1, verbose=False):
basecomparison.py:50:        self.chance_score = chance_score
basecomparison.py:60:    def __init__(self, sorting1, sorting2, sorting1_name=None, sorting2_name=None,
basecomparison.py:61:                 delta_time=0.4, sampling_frequency=None, match_score=0.5,
basecomparison.py:62:                 chance_score=0.1, n_jobs=1, verbose=False):
basecomparison.py:71:        BaseComparison.__init__(self, sorting_list, name_list=name_list, delta_time=delta_time,
basecomparison.py:72:                                sampling_frequency=sampling_frequency, match_score=match_score,
basecomparison.py:73:                                chance_score=chance_score, verbose=verbose, n_jobs=n_jobs)
basecomparison.py:97:    def _do_agreement(self):
basecomparison.py:114:    def _do_matching(self):
comparisontools.py:11:def count_matching_events(times1, times2, delta=10):
comparisontools.py:85:def count_match_spikes(times1, all_times2, delta_frames):  # , event_counts1, event_counts2  unit2_ids,
comparisontools.py:458:def compare_spike_trains(spiketrain1, spiketrain2, delta_frames=10):
groundtruthcomparison.py:28:    def __init__(self, gt_sorting, tested_sorting, gt_name=None, tested_name=None,
groundtruthcomparison.py:29:                 delta_time=0.4, sampling_frequency=None, match_score=0.5, well_detected_score=0.8,
groundtruthcomparison.py:30:                 redundant_score=0.2, overmerged_score=0.2, chance_score=0.1, exhaustive_gt=False, n_jobs=-1,
groundtruthcomparison.py:31:                 match_mode='hungarian', compute_labels=False, compute_misclassifications=False, verbose=False):
groundtruthcomparison.py:38:                                         sorting2_name=tested_name, delta_time=delta_time,
groundtruthcomparison.py:39:                                     
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sc/spikecomparison && sed -n 136,212p multisortingcomparison.py; sed -n 226,300p groundtruthcomparison.py; sed -n 338,365p groundtruthcomparison.py
```

```
def _do_graph(self):
        if self._verbose:
            print('Multicomaprison step 2: make graph')

        self.graph = nx.Graph()
        # nodes
        for i, sorting in enumerate(self.sorting_list):
            sorter_name = self.name_list[i]
            for unit in sorting.get_unit_ids():
                node_name = str(sorter_name) + '_' + str(unit)
                self.graph.add_node(node_name)
        # edges
        for comp in self.comparisons:
            for u1 in comp.sorting1.get_unit_ids():
                u2 = comp.hungarian_match_12[u1]
                if u2 != -1:
                    node1_name = str(comp.sorting1_name) + '_' + str(u1)
                    node2_name = str(comp.sorting2_name) + '_' + str(u2)
                    score = comp.agreement_scores.loc[u1, u2]
                    self.graph.add_edge(node1_name, node2_name, weight=score)
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sc/spikecomparison && sed -n 29,135p multisortingcomparison.py; grep -n "def _clean_graph\|def clean" -A40 multisortingcomparison.py | sed -n 1,45p
```

```
def get_agreement_sorting(self, minimum_agreement_count=1, minimum_agreement_count_only=False):
        '''
        Returns AgreementSortingExtractor with units with a 'minimum_matching' agreement.

        Parameters
        ----------
        minimum_agreement_count: int
            Minimum number of matches among sorters to include a unit.
        minimum_agreement_count_only: bool
            If True, only units with agreement == 'minimum_matching' are included.
            If False, units with an agreement >= 'minimum_matching' are included

        Returns
        -------
        agreement_sorting: AgreementSortingExtractor
            The output AgreementSortingExtractor
        '''
        assert minimum_agreement_count > 0, "'minimum_agreement_count' should be greater than 0"
        sorting = AgreementSortingExtractor(self, min_agreement_count=minimum_agreement_count,
                                            min_agreement_count_only=minimum_agreement_count_only)
[... 87 more lines not kept]
```

**Agent**

Code read. Now the dandiset's title and description (metadata only, no data files).

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000034/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d[k] for k in ('identifier','most_recent_published_version','draft_version') if k in d},indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/000034/versions/draft/ | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent**

Now the schema: the rest of the example file and the checker.

**Agent calls Bash**

```bash
sed -n 200,330p claims/001453/*.yaml; grep -n -E "inferred|kind|data|elsewhere|with_labels|allowed|KEYS|required|range" tools/claims_check.py | head -60
```

```
relatively constant velocity.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1C and
    Figure S1D
  quote: These visually evoked bouts in ZF consist of sharp velocity increases ... followed by
    interbout glides, resulting in characteristic periodic patterns. While DC also match the optic
    flow direction, they swim continuously, maintaining a relatively constant velocity
  criterion: The paper shows this with representative traces and a bout analysis whose bout
    files are not in the dandiset, so a measure is fixed here. Per trial, positions resampled
    to 30 Hz between 3 and 35 s, instantaneous speed, and the ratio of its median to its mean
    (near 1 for steady swimming, low for bursts); per fish, the median over all trials of all
    stimulus codes. Reproduced when the ZF fish have lower ratios than the DC fish by a
    two-sided Mann-Whitney test at p < 0.05.
- id: fig1cef-representative-values
  statement: In representative trials ZF bouts reach a peak velocity of 44.7 mm/s with a median
    of 1.8 mm/s, DC swim at a median of 13.7 mm/s to forward motion; to oblique motion ZF show
    a median angular velocity of 12.0 degrees/s and median peak angular acceleration of 174
    degrees/s2, and DC an average peak of 103 degrees/s2 to rightward motion.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1, and Results, Optic
    flow induces angular matching and turns in DC, paragraph 1; Figure 1C, 1E and 1F
  quote: sharp velocity increases (peak velocity = 44.7 mm/s, median velocity = 1.8 mm/s) ...
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -A3 "data: elsewhere\|inferred:" claims/ | head -30; grep -rn -B2 -A6 "^outside_data\|^  outside\|external:" claims/ | head -30; tail -40 claims/001453/*.yaml
```

```
claims/001752/10.1038-s41556-026-02009-4.yaml:182:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-183-  where: GEO GSE319557 (10x scRNA-seq, FASTQ, per the Data availability statement); processed
claims/001752/10.1038-s41556-026-02009-4.yaml-184-    data in Zenodo doi:10.5281/zenodo.18814764
claims/001752/10.1038-s41556-026-02009-4.yaml-185-  expected:
--
claims/001752/10.1038-s41556-026-02009-4.yaml:210:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-211-  where: GEO GSE319557
claims/001752/10.1038-s41556-026-02009-4.yaml-212-  criterion: Judged on the paper's cluster labels if the deposit carries them (counts of types per
claims/001752/10.1038-s41556-026-02009-4.yaml-213-    class equal to those stated); a re-clustering with the Methods' pipeline (SCANPY, Harmony,
--
claims/001752/10.1038-s41556-026-02009-4.yaml:219:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-220-  where: GEO GSE319557
claims/001752/10.1038-s41556-026-02009-4.yaml-221-  criterion: A claim of absence. The test is shown in Supplementary Fig. 3, which was not in the
claims/001752/10.1038-s41556-026-02009-4.yaml-222-    text read, so the paper's test and threshold are not known here; blocked as
--
claims/001752/10.1038-s41556-026-02009-4.yaml:231:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-232-  where: GEO GSE319369 (Patch-seq); mapping results in github.com/RFLiu2021/AIC_proj at commit
claims/001752/10.1038-s41556-026-02009-4.yaml-233-    44cd8a6, patchSeqMappingTo10X/data/mappingRes/
claims/001752/10.1038-s41556-026-02009-4.yaml-234-  expected:
--
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rhoE "^    [a-z_]+:" claims/*/*.yaml | sort | uniq -c | sort -rn | head -30; grep -rhoE "^  [a-z_]+:" claims/*/*.yaml | sort | uniq -c | sort -rn | head -30; grep -rh -A2 "relation:" claims/*/*.yaml | grep -v p_relation | head -10; sed -n 1,40p tools/claims_check.py
```

```
4045     value:
   4043     tolerance:
   3104     p:
   2295     test:
   1670     unit:
   1491     n:
   1369     statistic:
    873     p_relation:
    439     corrected:
    282     quantity:
     76     ci:
     16     doi:
      2     https:
      1     transparent:
      1     temperature:
      1     set:
      1     sessions:
      1     rpe:
      1     peak:
      1     paragraph:
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:3500])"
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

Key facts gathered. Checking two sorter defaults in spikesorters 0.3.3 (HerdingSpikes `filter`, Kilosort2 `keep_good_only`), as the notebooks set these.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/SpikeInterface/spikesorters.git ss 2>&1|tail -1; cd ss && git checkout -q 0.3.3 && git rev-parse HEAD && grep -n "'filter'\|keep_good_only\|minFR\|'adjacency_radius'" spikesorters/herdingspikes/*.py spikesorters/kilosort2/*.py spikesorters/spyking_circus/*.py | head; grep -n "sorter_params\[" -B3 -A3 spikesorters/sorterlist.py spikesorters/launcher.py 2>/dev/null | head -30
```

```
cfdc9737d61c8fdbe5ad333eec0b13c9d668bdbd
spikesorters/herdingspikes/herdingspikes.py:47:        if p['filter'] and p['freq_min'] is not None and p['freq_max'] is not None:
spikesorters/herdingspikes/herdingspikes.py:69:        if recording.is_filtered and p['filter']:
spikesorters/herdingspikes/herdingspikes.py:71:                  "filters by setting 'filter' parameter to False")
spikesorters/herdingspikes/herdingspikes.py:157:    'filter': True,
spikesorters/kilosort2/kilosort2.py:44:        'minFR': 0.1,
spikesorters/kilosort2/kilosort2.py:52:        'keep_good_only': False
spikesorters/kilosort2/kilosort2.py:139:            minFR=p['minFR'],
spikesorters/kilosort2/kilosort2.py:193:        sorting = se.KiloSortSortingExtractor(folder_path=output_folder, keep_good_only=sorter_params['keep_good_only'])
spikesorters/spyking_circus/spyking_circus.py:28:        'adjacency_radius': 100,  # Channel neighborhood adjacency radius corresponding to geom file
spikesorters/spyking_circus/spyking_circus.py:31:        'filter': True,
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ss && grep -rn "sorter_params" spikesorters/launcher.py | head -20; grep -n "sorter_name = \|spykingcircus" spikesorters/spyking_circus/spyking_circus.py spikesorters/sorterlist.py | head
```

```
33:def run_sorters(sorter_list, recording_dict_or_list, working_folder, sorter_params={}, grouping_property=None,
68:    sorter_params: dict of dict with sorter_name as key
149:            params = sorter_params.get(sorter_name, {})
spikesorters/spyking_circus/spyking_circus.py:22:    sorter_name = 'spykingcircus'
spikesorters/spyking_circus/spyking_circus.py:93:        # set up spykingcircus config file
spikesorters/spyking_circus/spyking_circus.py:131:            raise Exception('spykingcircus returned a non-zero exit code')
spikesorters/sorterlist.py:365:def run_spykingcircus(*args, **kwargs):
spikesorters/sorterlist.py:367:    Runs spykingcircus sorter
spikesorters/sorterlist.py:388:        Spike sorter specific arguments (they can be retrieved with 'get_default_params('spykingcircus')
spikesorters/sorterlist.py:395:    return run_sorter('spykingcircus', *args, **kwargs)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p claims/000034 && cat > $TMPDIR/build.py <<'PYEOF'
import yaml

HEADER = """\
# Claims for Buccino, Hurwitz, Garcia, Magland, Siegle, Hurwitz & Hennig (2020), eLife 9:e61834,
# on dandiset 000034.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, full text from Europe PMC (PMC7704107): main text, figure and
# figure-supplement legends, Materials and methods, the decision letter and author response. The
# one supplementary file is eLife's transparent reporting form, which says "The manuscript does
# not contain any statistical analysis"; so no claim has `statistics`. No PDF of the main text was
# supplied: numbers drawn only in figures (Figure 1, figure supplements 3 and 4; the dots of
# Figure 3, figure supplement 1) could not be read and are not used.
#
# Code read: the notebooks the paper links, in github.com/SpikeInterface/spikeinterface.github.io
# (clone at 657c6d8; the four notebooks were last changed at ee08fb6, 2020-09-29, before
# publication): posts/ensemble-sorting-of-a-neuropixels-recording.ipynb (Figures 1 and 4),
# ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording.ipynb
# (Figures 2 and 3), ensemble-sorting-of-a-neuropixels-recording-2.ipynb (Figure 1, figure
# supplement 3) and ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina.ipynb (Figure 1,
# figure supplement 4). They hold the sorter runs, the comparisons, the plots and printed counts.
# No code was found for Figure 3, figure supplements 1 and 2. The library code read is
# spikecomparison 0.2.6 (tag, 6ad882a) and spikesorters 0.3.3 (tag, cfdc973), the versions the
# notebooks printed.
#
# Data the paper used (all four recordings are said to be in dandiset 000034, in NWB):
# 1. Real Neuropixels: a head-fixed mouse from the Allen Brain Observatory (Siegle et al. 2019;
#    session 766640955, probe 77359232; mouse 412804 in the notebook), V1, CA1, dentate gyrus and
#    LP, visual stimuli while running on a disk; trimmed to 15 min, 30 kHz, 246 active channels
#    (the notebook's file printed 248 channels and 27,000,000 frames). Notebook file
#    sub-mouse412804_ecephys.nwb. Two manual curations of its Kilosort2 output in Phy by experts C1
#    and C2: sub-mouse412804_ses-20200824T155542.nwb (read as curated 1) and
#    sub-mouse412804_ses-20200824T155543.nwb (curated 2).
# 2. Simulated Neuropixels (MEArec): 10 min, 250 neurons (200 excitatory, 50 inhibitory, from the
#    Neocortical Micro Circuit Portal), independent Poisson firing, additive Gaussian noise of 10 uV
#    SD; ground-truth spike trains in the same file, sub-MEAREC-250neuron-Neuropixels_ecephys.nwb.
# 3. Rat cortex Neuropixels (Marques-Smith et al. 2018, dataset spe-c1), spontaneous activity in
#    motor and somatosensory cortex; sub-c1_ecephys.nwb (notebook printed 384 channels, 30 kHz,
#    270.0 s).
# 4. Mouse retina on a 3Brain Biocam (Hilgen et al. 2017), 1024 channels, 23199 Hz;
#    sub-P29-16-05-14-retina02-left_ecephys.nwb (notebook printed 135.7 s).
# The measured variables are the spike trains the sorters output, the ground-truth spike trains of
# recording 2 and the two curated sortings of recording 1. The sorters' own outputs are not said to
# be deposited, so the attempt runs the sorters.
#
# Method fixed here for every claim, from the paper and, where it is silent, the code:
# - Sorters (Results, Spike sorters show low agreement, paragraph 2): HerdingSpikes2 0.3.7,
#   Kilosort2 at commit 48bf2b81d8ad, IronClust 5.9.8, Tridesclous 1.6.0, SpyKING Circus 0.9.7,
#   HDSort 1.0.1, all with default parameters, the same on the simulated recording. The notebooks
#   printed HDSort 1.0.2 (a variant). They pass SpyKING Circus adjacency_radius 50 under the key
#   'spyking_circus', which run_sorters in spikesorters 0.3.3 does not match to the sorter name
#   'spykingcircus', so it ran on its default (100); HerdingSpikes filter=True is its default. So
#   code and Methods agree on defaults. For the Biocam recording the code applies
#   spiketoolkit.preprocessing.blank_saturation before sorting (the paper is silent; the code is
#   followed). The paper names spikeinterface 0.10.0; the notebooks ran spikeinterface 0.9.9
#   (spikeextractors 0.8.4, spiketoolkit 0.6.3, spikesorters 0.3.3, spikecomparison 0.2.6). The
#   code's versions are used; 0.10.0 is a variant.
# - Agreement among sorters (Methods, SpikeComparison; compare_multiple_sorters in spikecomparison
#   0.2.6): agreement score = matches / (n1 + n2 - matches); spikes match within 0.4 ms; each pair
#   of sorters is matched by the Hungarian method with a minimum score of 0.5; the units of all
#   sorters form a graph with the matched pairs as edges; where a connected component holds two
#   units of one sorter the code removes the weaker edge; each remaining connected component is one
#   agreement unit, and k is the number of sorters in it.
# - Ground-truth comparison (Methods, SpikeComparison; notebook cell run_comparisons): Hungarian
#   matching, 0.4 ms, exhaustive_gt=True, match_score=0.1, chance_score 0.1; accuracy, precision
#   and recall per ground-truth unit as the Methods define them; units well detected above 0.8,
#   false positive when unmatched or best score below 0.2, redundant and overmerged at 0.2 (the
#   Methods' thresholds, which equal the code's defaults).
# - True and false positive agreement units on the simulation (Figure 3C; notebook cell after the
#   multicomparison, the paper is silent): an agreement unit is a true positive when every member
#   unit is the best match (best_match_12, chance score 0.1) of some ground-truth unit in its
#   sorter's ground-truth comparison, and otherwise a false positive; each member unit is counted
#   for its sorter at that k.
# - Ground-truth SNR (notebook): spiketoolkit.validation.compute_snrs(gt sorting, recording,
#   apply_filter=False, memmap=True, max_spikes_per_unit_for_snr=500), other arguments default.
# - Comparisons with the curated sortings (Figure 4; notebook): compare_two_sorters(sorter units,
#   curated sorting) with its defaults (0.4 ms, minimum score 0.5); a sorter's percentage is the
#   number of its units with a match over its number of units. Consensus units of a sorter are its
#   units in agreement units with k >= 2; non-consensus units those with k = 1.
# - Spike sorters do not give the same output twice (the author response shows this for
#   Kilosort2), so counts are held to the 10% tolerance and never to exact values, and the
#   curators worked on the paper's own Kilosort2 run, which a new run will not repeat exactly.
# The Methods' descriptions of the software (file formats, sorters supported, widgets, the GUI)
# are descriptions, not findings, and have no claims.
"""

COMMON = "Sorters, agreement graph and k as in the opening comment."

claims = []
def C(**kw):
    claims.append(kw)

C(id="recordings-as-described", kind="link",
  statement="The dandiset holds the recordings the paper analyses and the files its notebooks name, "
            "with the properties the paper and the notebooks give.",
  source="Results, opening paragraph; Data availability; the four notebooks at ee08fb6",
  quote="The datasets are publicly available in NWB format on the DANDI archive",
  criterion="Each of the six files named in the opening comment is present. The real Neuropixels "
            "recording has a sampling rate of 30 kHz and lasts 15 min (27,000,000 frames), with 246 "
            "channels (the paper) or 248 (the notebook); the simulated recording lasts 10 min and its "
            "ground truth has 250 units; the rat recording has 384 channels at 30 kHz; the Biocam "
            "recording has 1024 channels at about 23199 Hz. Reproduced when all hold under one of the "
            "two channel counts; partially reproduced when a file is missing or a property differs, "
            "naming which.")

C(id="fig1b-unit-counts",
  statement="On the real Neuropixels recording the six sorters return very different numbers of units: "
            "Tridesclous the fewest (187) and SpyKING Circus the most (628); HerdingSpikes2 210, Kilosort2 "
            "446, IronClust 233 and HDSort 317.",
  source="Results, Spike sorters show low agreement for the same high-density dataset, paragraph 3; "
         "Figure 1B",
  quote="with Tridesclous (TDC) finding the least units (187) and SpyKING Circus (SC) finding the most "
        "units (628). HerdingSpikes2 finds 210 units; Kilosort2 finds 446 units; IronClust finds 233 "
        "units; and HDSort finds 317 units",
  expected=[
    dict(quantity="Tridesclous units", value=187, tolerance=18.7, unit="units"),
    dict(quantity="SpyKING Circus units", value=628, tolerance=62.8, unit="units"),
    dict(quantity="HerdingSpikes2 units", value=210, tolerance=21.0, unit="units"),
    dict(quantity="Kilosort2 units", value=446, tolerance=44.6, unit="units"),
    dict(quantity="IronClust units", value=233, tolerance=23.3, unit="units"),
    dict(quantity="HDSort units", value=317, tolerance=31.7, unit="units")],
  criterion="Sorters, versions and parameters as in the opening comment, on the real Neuropixels "
            "recording. Reproduced when all six counts are within tolerance; partially reproduced when "
            "Tridesclous has the fewest units and SpyKING Circus the most but some count is outside "
            "tolerance. The notebook printed 448 for Kilosort2 and 234 for IronClust.")

C(id="fig1c-low-agreement",
  statement="Of the 2031 units detected on the real recording, all six sorters agree on only 33, and two "
            "or more sorters agree on only 263.",
  source="Results, Spike sorters show low agreement for the same high-density dataset, paragraph 4; "
         "Figure 1C",
  quote="Of the 2031 total detected units, all six sorters agree on just 33 of the units ... We also "
        "find that two or more sorters agree on just 263 of the total units",
  expected=[
    dict(quantity="total detected units", value=2031, tolerance=203.1, unit="units"),
    dict(quantity="agreement units with k = 6", value=33, tolerance=3.3, unit="units"),
    dict(quantity="agreement units with k >= 2", value=263, tolerance=26.3, unit="units")],
  depends_on=["fig1b-unit-counts"],
  criterion=COMMON + " The counts of agreement units with k = 6 and with k >= 2 are compared with 33 "
            "and 263. The paper's 2031 is not the sum of the counts it gives in Figure 1B (2021), so "
            "the total is read as (a) the sum of the six sorters' unit counts, or (b) that sum as the "
            "notebook's sorters gave it; the number of agreement units (components) is reported as well. "
            "Reproduced when the k = 6 and k >= 2 counts are within tolerance and the total is within "
            "tolerance under one reading.")

C(id="fig1d-most-units-unmatched",
  statement="For most sorters more than half of their units match no other sorter; IronClust and "
            "Tridesclous are the exceptions.",
  source="Results, Spike sorters show low agreement for the same high-density dataset, paragraph 4; "
         "Figure 1D",
  quote="For most sorters, over 50% of the units that they find do not match with any other sorter "
        "(with the exceptions of Ironclust and Tridesclous)",
  depends_on=["fig1b-unit-counts"],
  criterion=COMMON + " Per sorter, the fraction of the agreement units holding one of its units that "
            "have k = 1, as the notebook's per-sorter table computes it. Reproduced when the fraction "
            "exceeds 0.5 for HerdingSpikes2, Kilosort2, SpyKING Circus and HDSort and is below 0.5 for "
            "IronClust and Tridesclous; partially reproduced when it exceeds 0.5 for at least four "
            "sorters but the exceptions are other sorters. The notebook printed 50.7% for Kilosort2, "
            "close to the boundary.")

C(id="fig1s2-agreement-scores-high",
  statement="Matched units mostly agree closely: around 80% of the agreement scores of agreed-upon units "
            "are 0.8 or higher.",
  source="Results, Spike sorters show low agreement for the same high-density dataset, paragraph 4; "
         "Figure 1, figure supplement 2",
  quote="For agreed-upon units, around 80% of the agreement scores are 0.8 or higher, indicating that "
        "matched units typically have high spike train agreement",
  expected=dict(quantity="fraction of agreement scores of 0.8 or higher", value=80, tolerance=8,
                unit="percent"),
  criterion=COMMON + " Two details are open. The recording: the Results cite the supplement in the "
            "paragraph on the real recording, while its legend and the author response say it shows "
            "the simulated ground-truth recording; both are read. The scores: (a) the agreement scores "
            "of all matched pairs (the graph's edges, all at least 0.5), or (b) the average agreement "
            "of each agreement unit with k >= 2 (the code's avg_agreement). The legend says \"over "
            "80%\" and \"greater than 0.8\"; the Results \"around 80%\" and \"0.8 or higher\"; the "
            "tolerance covers both. Reproduced when the fraction is within tolerance under one reading.")

C(id="fig1s3-s4-other-recordings-disagree",
  statement="On a rat cortex Neuropixels recording (six sorters) and a mouse retina Biocam recording "
            "(the four sorters able to process it, HerdingSpikes2, Kilosort2, IronClust and HDSort) "
            "the sorters disagree as much as on the first recording.",
  source="Results, Spike sorters show low agreement for the same high-density dataset, paragraph 5; "
         "Figure 1, figure supplements 3 and 4",
  quote="In both cases, we find similar disagreement among the sorters",
  criterion=COMMON + " The Biocam recording is first passed through blank_saturation, as in its "
            "notebook. The paper does not say how similarity was judged and its figures could not be "
            "read here, so the readings are the two measures it uses for the first recording: (a) "
            "Figure 1D, more than half of the sorters have over 50% of their units at k = 1 (the "
            "legends of both supplements say most sorters find many units that other sorters do not); "
            "(b) Figure 1C, agreement units found by all sorters are at most 8% of all detected units "
            "(the 7.24% of the simulated recording, which the paper calls a large disagreement, widened "
            "by 10%). Reproduced when, for both recordings, one reading holds; partially reproduced "
            "when it holds for one recording only.")

C(id="fig2c-sim-unit-counts",
  statement="On the simulated recording with 250 ground-truth units the sorters again return very "
            "different numbers of units: Tridesclous 189, HDSort 458, HerdingSpikes2 233, Kilosort2 415, "
            "IronClust 283 and SpyKING Circus 343.",
  source="Results, Evaluating spike sorters on a simulated dataset, paragraph 2; Figure 2C",
  quote="The number of detected units range from the 189 units found by Tridesclous to the 458 units "
        "found by HDSort. HerdingSpikes2 finds 233 units; Kilosort2 finds 415 units; IronClust finds "
        "283 units; and SpyKING Circus finds 343 units",
  expected=[
    dict(quantity="Tridesclous units", value=189, tolerance=18.9, unit="units"),
    dict(quantity="HDSort units", value=458, tolerance=45.8, unit="units"),
    dict(quantity="HerdingSpikes2 units", value=233, tolerance=23.3, unit="units"),
    dict(quantity="Kilosort2 units", value=415, tolerance=41.5, unit="units"),
    dict(quantity="IronClust units", value=283, tolerance=28.3, unit="units"),
    dict(quantity="SpyKING Circus units", value=343, tolerance=34.3, unit="units")],
  criterion="Sorters as in the opening comment, with the same parameters as on the real recording, on "
            "the simulated recording. Reproduced when all six counts are within tolerance; partially "
            "reproduced when Tridesclous has the fewest and HDSort the most but some count is outside "
            "tolerance.")

C(id="fig2s1a-precision-recall-bias",
  statement="Sorters trade precision against recall differently: HerdingSpikes2, SpyKING Circus and "
            "HDSort favour precision, IronClust recall, Kilosort2 scores well on both, and Tridesclous "
            "shows no bias.",
  source="Figure 2, figure supplement 1A legend; Results, Evaluating spike sorters on a simulated "
         "dataset, paragraph 2",
  quote="Some sorters seem to favor precision (HerdingSpikes, SpyKING Circus, HDSort), others instead "
        "have higher recall (Ironclust) or score well on both measures (Kilosort2). Tridesclous does not "
        "show a bias towards precision or recall",
  depends_on=["fig2c-sim-unit-counts"],
  criterion="Precision and recall per ground-truth unit from the ground-truth comparison of the opening "
            "comment (the notebook's perf_by_units). The paper shows scatter plots and does not say how "
            "a bias is summarized, so the readings are the per-sorter median precision and median recall "
            "over (a) all 250 ground-truth units or (b) the ground-truth units with a Hungarian match. "
            "Under a reading, the claim holds when median precision exceeds median recall for "
            "HerdingSpikes2, SpyKING Circus and HDSort; median recall exceeds median precision for "
            "IronClust; both Kilosort2 medians are at least 0.8 (the Methods' well-detected score); "
            "and Tridesclous has a smaller absolute difference between the two than each of those four. "
            "Reproduced when all hold under one reading; partially reproduced when the directions for "
            "HerdingSpikes2, SpyKING Circus, HDSort and IronClust hold.")

C(id="fig2s1b-accuracy-snr",
  statement="Accuracy depends on the SNR of the ground-truth units for every sorter except Kilosort2, "
            "which reaches almost perfect accuracy on low-SNR units.",
  source="Results, Evaluating spike sorters on a simulated dataset, paragraph 2; Figure 2, figure "
         "supplement 1B",
  quote="Moreover, the accuracy is modulated by the SNR of the ground-truth units for all spike sorters "
        "except Kilosort2 which achieves an almost perfect performance on the low-SNR units",
  depends_on=["fig2c-sim-unit-counts"],
  criterion="Accuracy per ground-truth unit as in fig2s1a-precision-recall-bias; ground-truth SNR as in "
            "the opening comment. The paper reports no test (its reporting form says it has none), so "
            "dependence is read as a Spearman correlation of accuracy with SNR over the 250 ground-truth "
            "units, positive with p < 0.05. Low-SNR units are open, read as (a) those below the median "
            "ground-truth SNR or (b) those below the mode of the ground-truth SNR histogram (bins of 1, "
            "a standard choice), the reference Figure 3, figure supplement 2 uses. Reproduced when, under "
            "one reading, the correlation is positive with p < 0.05 for HerdingSpikes2, IronClust, "
            "Tridesclous, SpyKING Circus and HDSort, Kilosort2 has the weakest correlation of the six, "
            "and Kilosort2's median accuracy on low-SNR units is at least 0.8 and above every other "
            "sorter's; partially reproduced when the Kilosort2 parts hold but the correlation fails for "
            "one other sorter.")

C(id="fig2d-ks2-highest-scores",
  statement="Kilosort2 scores higher than the other sorters for most ground-truth units.",
  source="Results, Evaluating spike sorters on a simulated dataset, paragraph 2; Figure 2D",
  quote="Kilosort2 attains significantly higher scores than the rest of the spike sorters for most "
        "ground-truth units",
  depends_on=["fig2c-sim-unit-counts"],
  criterion="Scores per ground-truth unit as in fig2s1a-precision-recall-bias. The paper reports no test "
            "behind \"significantly\", so the claim is judged by its words \"for most ground-truth "
            "units\": for each of the five other sorters, Kilosort2's score exceeds that sorter's for "
            "more than half of the 250 ground-truth units. \"Scores\" is read as (a) accuracy or (b) each "
            "of accuracy, precision and recall, the three metrics of Figure 2D. Reproduced when this "
            "holds for all five sorters under one reading; partially reproduced when it holds for three "
            "or four. A paired Wilcoxon signed-rank test per pair is shown, not used.")

C(id="fig2e-ks2-unit-types",
  statement="Kilosort2 has the most well-detected units (245) but also many false positive (147) and "
            "redundant (21) units, and two overmerged units.",
  source="Results, Evaluating spike sorters on a simulated dataset, paragraph 3; Figure 2E",
  quote="While Kilosort2 has the most well-detected units (245), this comes at the cost of a high "
        "percentage of false positive (147) and redundant (21) units ... In both cases two overmerged "
        "units are found",
  expected=[
    dict(quantity="Kilosort2 well-detected units", value=245, tolerance=24.5, unit="units"),
    dict(quantity="Kilosort2 false positive units", value=147, tolerance=14.7, unit="units"),
    dict(quantity="Kilosort2 redundant units", value=21, tolerance=2.1, unit="units"),
    dict(quantity="Kilosort2 overmerged units", value=2, tolerance=1, unit="units")],
  depends_on=["fig2c-sim-unit-counts"],
  criterion="Unit classes from the ground-truth comparison of the opening comment. The tolerance for the "
            "overmerged count is one unit, since 10% of 2 is below the smallest difference a count can "
            "show. Reproduced when the four counts are within tolerance and Kilosort2 has more "
            "well-detected units than each other sorter; partially reproduced when it has the most "
            "well-detected units but a count is outside tolerance.")

C(id="fig2e-ks2-curated-unit-types",
  statement="With Kilosort2's own curation, which removes units with an estimated contamination above "
            "20%, false positive and redundant units are fewer but persist: 241 well detected, 93 false "
            "positive, 18 redundant and 2 overmerged.",
  source="Results, Evaluating spike sorters on a simulated dataset, paragraph 3 (parenthesis)",
  quote="In that case the number of well-detected units is 241, false positives are 93, and redundant "
        "units are 18. In both cases two overmerged units are found",
  expected=[
    dict(quantity="well-detected units", value=241, tolerance=24.1, unit="units"),
    dict(quantity="false positive units", value=93, tolerance=9.3, unit="units"),
    dict(quantity="redundant units", value=18, tolerance=1.8, unit="units"),
    dict(quantity="overmerged units", value=2, tolerance=1, unit="units")],
  depends_on=["fig2e-ks2-unit-types"],
  criterion="Kilosort2's automated curation is the sorter wrapper's keep_good_only=True (spikesorters "
            "0.3.3, the line commented out in the notebooks), which keeps the units Kilosort2 labels "
            "good. Applied to (a) the same Kilosort2 run as fig2e-ks2-unit-types, or (b) a run with "
            "keep_good_only=True; the paper does not say which. Classes as in fig2e-ks2-unit-types, "
            "overmerged tolerance one unit for the reason given there. Reproduced when the four counts "
            "are within tolerance under one reading; partially reproduced when false positive and "
            "redundant counts fall below those of fig2e-ks2-unit-types but stay above zero.")

C(id="fig2e-tdc-few-fp-hds-many-fp",
  statement="Tridesclous detects very few false positive or redundant units while finding many "
            "well-detected units, and HDSort finds many more false positive units than any other sorter.",
  source="Results, Evaluating spike sorters on a simulated dataset, paragraph 3; Figure 2E",
  quote="Notably, Tridesclous detects very few false positive/redundant units while still finding many "
        "well-detected units. HDSort, on the flip side, finds many more false positive units than any "
        "other spike sorter",
  depends_on=["fig2c-sim-unit-counts"],
  criterion="Unit classes as in fig2e-ks2-unit-types. Reproduced when HDSort's false positive count is "
            "the highest of the six sorters, Tridesclous has the lowest fraction of its units that are "
            "false positive or redundant, and at least half of Tridesclous's units are well detected "
            "(\"many\"); partially reproduced when the HDSort part or the Tridesclous part holds alone.")

C(id="fig3a-sim-low-agreement",
  statement="On the simulated recording only 139 of the 1921 detected units (7.24%) are agreed upon by "
            "all six sorters.",
  source="Results, Low-agreement units are mainly false positives, paragraph 1; Figure 3A",
  quote="Again, we observe a large disagreement among the spike sorting outputs with only 139 units of "
        "the 1921 total units (7.24%) being in agreement among all sorters",
  expected=[
    dict(quantity="agreement units with k = 6", value=139, tolerance=13.9, unit="units"),
    dict(quantity="total detected units", value=1921, tolerance=192.1, unit="units"),
    dict(quantity="k = 6 units over total detected units", value=7.24, tolerance=0.72,
         unit="percent")],
  depends_on=["fig2c-sim-unit-counts"],
  criterion=COMMON + " The 7.24% is 139 over 1921, the sum of the six sorters' unit counts, not over the "
            "number of agreement units; it is computed that way. Reproduced when the three values are "
            "within tolerance.")

C(id="fig3b-sorters-prone-to-low-agreement",
  statement="HDSort, SpyKING Circus and Kilosort2 are more prone to finding low-agreement units than "
            "HerdingSpikes2, IronClust and Tridesclous.",
  source="Results, Low-agreement units are mainly false positives, paragraph 1; Figure 3B",
  quote="highlighting that some sorters are more prone to finding low agreement units (HDSort, SpyKING "
        "Circus, Kilosort2) than other sorters (HerdingSpikes2, Ironclust, Tridesclous)",
  depends_on=["fig3a-sim-low-agreement"],
  criterion=COMMON + " Per sorter, the fraction of its agreement units with k = 1, as in "
            "fig1d-most-units-unmatched. Reproduced when each of HDSort, SpyKING Circus and Kilosort2 "
            "has a higher fraction than each of HerdingSpikes2, IronClust and Tridesclous; partially "
            "reproduced when two of the three named sorters are among the three highest.")

C(id="fig3c-fp-found-by-one-sorter",
  statement="Almost all false positive units are found by a single sorter, while most real units are "
            "matched by more than one sorter; false positives found by two or more sorters number 4 for "
            "HerdingSpikes2, Kilosort2 and IronClust, 2 for SpyKING Circus and HDSort and 1 for "
            "Tridesclous.",
  source="Results, Low-agreement units are mainly false positives, paragraph 2; Figure 3C legend",
  quote="The plots show that (almost) all false positive units are ones that are found by only a single "
        "sorter (not matched with any other sorters), while most real units are matched by more than one "
        "sorter",
  expected=[
    dict(quantity="HerdingSpikes2 false positive units with k >= 2", value=4, tolerance=1, unit="units"),
    dict(quantity="Kilosort2 false positive units with k >= 2", value=4, tolerance=1, unit="units"),
    dict(quantity="IronClust false positive units with k >= 2", value=4, tolerance=1, unit="units"),
    dict(quantity="SpyKING Circus false positive units with k >= 2", value=2, tolerance=1, unit="units"),
    dict(quantity="Tridesclous false positive units with k >= 2", value=1, tolerance=1, unit="units"),
    dict(quantity="HDSort false positive units with k >= 2", value=2, tolerance=1, unit="units")],
  depends_on=["fig3a-sim-low-agreement"],
  criterion=COMMON + " True and false positive agreement units as in the opening comment (the "
            "notebook's rule; the Methods do not define them for this figure). The counts are from the "
            "legend; their tolerance is one unit, since 10% of a count below 5 is less than one unit. "
            "Reproduced when, for every sorter, the false positive units with k >= 2 are within "
            "tolerance and at most 10% of its false positive units, and its true positive units with "
            "k >= 2 outnumber those with k = 1; partially reproduced when this holds for four or five "
            "sorters.")

C(id="fig3s1-ks2-ic-best-pair",
  statement="With two sorters, combining Kilosort2 and IronClust identified true positives most reliably, "
            "with false positive and true positive detection rates of 96% and 95%.",
  source="Results, Low-agreement units are mainly false positives, paragraph 2; Figure 3, figure "
         "supplement 1 legend",
  quote="For two sorters, the most reliable identification of true positives for this dataset was "
        "achieved by combining Kilosort2 and Ironclust (96% and 95% false positive and true positive "
        "detection rate, respectively)",
  expected=[
    dict(quantity="false positive detection rate, Kilosort2 and IronClust", value=96, tolerance=9.6,
         unit="percent"),
    dict(quantity="true positive detection rate, Kilosort2 and IronClust", value=95, tolerance=9.5,
         unit="percent")],
  depends_on=["fig3c-fp-found-by-one-sorter"],
  criterion="No code for this figure was found; the legend gives the method: for each subset of sorters, "
            "the units of the other sorters are removed from the full comparison of fig3a, the units of "
            "the subset found by one sorter (k = 1) are predicted false positive and the others true "
            "positive, against the truth of fig3c-fp-found-by-one-sorter. The false positive detection "
            "rate is the fraction of false positive units predicted so, the true positive rate likewise. "
            "Open, with readings: removal (a) drops the nodes and recomputes connected components, or (b) "
            "keeps the full comparison's components and counts the subset's sorters in each; the rate is "
            "(i) pooled over the units of the subset's sorters or (ii) the mean of the per-sorter rates. "
            "The legend says the best pairs combine two of Kilosort2, IronClust and HDSort; the Results "
            "name Kilosort2 and IronClust. Reproduced when, under one reading, both rates are within "
            "tolerance and Kilosort2 with IronClust has the highest true positive rate of the 15 pairs; "
            "partially reproduced when the rates are within tolerance and the best pair is another pair "
            "of Kilosort2, IronClust and HDSort.")

C(id="fig3s1-pairs-remove-fp-four-keep-tp",
  statement="A pair of sorters suffices to isolate almost all false positive units, but with fewer than "
            "four sorters a significant fraction of true positive units, found by only one sorter, are "
            "wrongly classed as false positives; four or more sorters reliably identify most true "
            "positives.",
  source="Results, Low-agreement units are mainly false positives, paragraph 2; Figure 3, figure "
         "supplement 1 legend",
  quote="This analysis showed that using a pair of sorters is sufficient to isolate almost all false "
        "positive units in each sorter, yet when fewer than four sorter outputs are compared, a "
        "significant fraction of true positive units found by only one sorter can be wrongly classified "
        "as false positives with this approach",
  depends_on=["fig3s1-ks2-ic-best-pair"],
  criterion="Subsets of two to five sorters and the rates as in fig3s1-ks2-ic-best-pair, under the same "
            "readings. \"Almost all\" is read against the paper's own example of a pair, 96%, widened by "
            "10%: the median false positive detection rate over the 15 pairs is at least 86.4%. \"Most\" "
            "true positives is more than half: every subset of four or five sorters has a true positive "
            "rate above 0.5. The loss with fewer sorters: the lowest true positive rate over pairs and "
            "over triples is below the lowest over subsets of four. Reproduced when all three hold under "
            "one reading; partially reproduced when the false positive part holds and one true positive "
            "part fails.")

C(id="fig3d-snr-rises-with-agreement",
  statement="Ground-truth units with higher SNR are found by more sorters.",
  source="Results, Low-agreement units are mainly false positives, paragraph 3; Figure 3D",
  quote="This shows, as expected, that higher SNR units have higher agreement among sorters",
  depends_on=["fig3c-fp-found-by-one-sorter"],
  criterion=COMMON + " For each sorter, its true positive units (as in fig3c-fp-found-by-one-sorter) with "
            "the SNR of the ground-truth unit each matches (ground-truth SNR as in the opening comment), "
            "as the notebook's Figure 3D cell pairs them. The paper reports no test; the claim is read as "
            "a positive Spearman correlation between k and SNR. Reproduced when the correlation is "
            "positive for all six sorters; partially reproduced when positive for four or five.")

C(id="fig3s2-snr-does-not-separate-ks2-fp",
  statement="For Kilosort2, SNR is not a good predictor of false positives: many of its false positive "
            "units have an SNR above the mode of the ground-truth SNR.",
  source="Results, Low-agreement units are mainly false positives, paragraph 3; Figure 3, figure "
         "supplement 2 legend",
  quote="Many detected false positive units have an SNR above the mode of the ground-truth SNR, "
        "indicating that SNR is not a good measure to separate false and true positives in this case",
  depends_on=["fig2e-ks2-unit-types"],
  criterion="No code for this figure was found. The SNR of each Kilosort2 unit is computed with the same "
            "function and arguments as the ground-truth SNR (opening comment); the mode of the "
            "ground-truth SNR is the peak of its histogram in bins of 1 (a standard choice). Units "
            "\"without matches\" are read as (a) the Methods' false positive class (fig2e-ks2-unit-types) "
            "or (b) units that are the best match of no ground-truth unit (the rule of "
            "fig3c-fp-found-by-one-sorter). \"Many\" is open, read as more than half or as at least a "
            "quarter of those units above the mode. Reproduced when every reading holds; not reproduced "
            "when none does; blocked as methods_underspecified when they differ.")

C(id="fig4a-curators-agree",
  statement="The two experts' manual curations of the Kilosort2 output agree on most curated units (226 "
            "of 351, 64.2%), and 174 Kilosort2 units are discarded by both.",
  source="Results, Consensus units highly overlap with manually curated ones, paragraph 1; Figure 4A",
  quote="most of the curated units (226 out of 351–64.2%) are agreed upon by both experts. Notably, 174 "
        "units found by Kilosort2 are discarded by both experts",
  expected=[
    dict(quantity="curated units agreed by both curators", value=226, tolerance=22.6, unit="units"),
    dict(quantity="curated units in all", value=351, tolerance=35.1, unit="units"),
    dict(quantity="agreed curated units over all curated units", value=64.2, tolerance=6.42,
         unit="percent"),
    dict(quantity="Kilosort2 units discarded by both curators", value=174, tolerance=17.4,
         unit="units")],
  depends_on=["fig1b-unit-counts"],
  criterion="As the notebook's Venn diagram: compare_multiple_sorters on curated 1, curated 2 and the "
            "Kilosort2 run (defaults), and the counts of agreement units by which of the three they hold. "
            "Read as 226 = units holding both curators, 351 = units holding either curator, 174 = units "
            "holding Kilosort2 alone. For 226 and 351 a second reading is the pairwise "
            "compare_two_sorters(curated 1, curated 2): matched pairs, and the two counts summed less the "
            "matched pairs. Curated counts do not depend on a sorter run; 174 does, as the curators worked "
            "on the paper's run. Reproduced when the values are within tolerance under one reading; "
            "partially reproduced when 226, 351 and 64.2% are and 174 is not.")

C(id="fig4b-single-sorter-match-curated",
  statement="Only a small percentage of each sorter's units match the curated units; IronClust matches "
            "best (59.83% and 61.1%), above Kilosort2 (50.67% and 56.25%), from whose output the "
            "curations were made.",
  source="Results, Consensus units highly overlap with manually curated ones, paragraph 2; Figure 4B",
  quote="The highest percentage match is actually IronClust which is surprising given that the initial "
        "sorting output was curated from Kilosort2’s output (IC ∩ C1 = 59.83%, IC ∩ C2 = 61.1%, KS ∩ C1 "
        "= 50.67%, KS ∩ C2 = 56.25%)",
  expected=[
    dict(quantity="IronClust units matched to C1", value=59.83, tolerance=5.98, unit="percent"),
    dict(quantity="IronClust units matched to C2", value=61.1, tolerance=6.11, unit="percent"),
    dict(quantity="Kilosort2 units matched to C1", value=50.67, tolerance=5.07, unit="percent"),
    dict(quantity="Kilosort2 units matched to C2", value=56.25, tolerance=5.63, unit="percent")],
  depends_on=["fig1b-unit-counts"],
  criterion="Percentages as in the opening comment (comparisons with the curated sortings), for all of "
            "each sorter's units. Reproduced when the four values are within tolerance and IronClust has "
            "the highest percentage of the six sorters for both curators; partially reproduced when "
            "IronClust is highest but a value is outside tolerance.")

C(id="fig4c-consensus-match-curated",
  statement="Consensus units (found by at least two sorters) match the curated units at above 70% for "
            "every sorter; Kilosort2 is highest (84.55% and 89.55%), slightly above IronClust (82.63% and "
            "83.83%).",
  source="Results, Consensus units highly overlap with manually curated ones, paragraph 2; Figure 4C",
  quote="The average match percentage is above 70% for all sorters showing that there is a large "
        "agreement between the manually curated outputs and the consensus-based output. Kilosort2 has "
        "the highest match (KS c ∩ C1 = 84.55%, KS c ∩ C2 = 89.55%), slightly higher than Ironclust (IC "
        "c ∩ C1 = 82.63%, IC c ∩ C2 = 83.83%)",
  expected=[
    dict(quantity="Kilosort2 consensus units matched to C1", value=84.55, tolerance=8.46,
         unit="percent"),
    dict(quantity="Kilosort2 consensus units matched to C2", value=89.55, tolerance=8.96,
         unit="percent"),
    dict(quantity="IronClust consensus units matched to C1", value=82.63, tolerance=8.26,
         unit="percent"),
    dict(quantity="IronClust consensus units matched to C2", value=83.83, tolerance=8.38,
         unit="percent")],
  depends_on=["fig1c-low-agreement"],
  criterion="Consensus units and percentages as in the opening comment. \"The average match percentage "
            "is above 70%\" is read as (a) the mean of the two curators' percentages for each sorter, or "
            "(b) each curator's percentage (the legend says the percent is above 70% for all sorters). "
            "Reproduced when, under one reading, every sorter is above 70%, the four values are within "
            "tolerance and Kilosort2 is highest for both curators; partially reproduced when every sorter "
            "is above 70% but the Kilosort2 parts fail.")

C(id="fig4d-nonconsensus-rarely-curated",
  statement="Units found by only one sorter rarely match the curated units; the only notable overlap is "
            "Kilosort2's (18.58% with C1 and 24.34% with C2).",
  source="Results, Consensus units highly overlap with manually curated ones, paragraph 2; Figure 4D "
         "legend",
  quote="The only significant overlap is between Curator one and Kilosort2, with a percent around 18% "
        "(KS nc ∩ C1 = 18.58%, KS nc ∩ C2 = 24.34%)",
  expected=[
    dict(quantity="Kilosort2 non-consensus units matched to C1", value=18.58, tolerance=1.86,
         unit="percent"),
    dict(quantity="Kilosort2 non-consensus units matched to C2", value=24.34, tolerance=2.43,
         unit="percent")],
  depends_on=["fig4c-consensus-match-curated"],
  criterion="Non-consensus units and percentages as in the opening comment. Reproduced when the two "
            "Kilosort2 values are within tolerance, every other sorter's percentage is below Kilosort2's "
            "for the same curator, and every sorter's non-consensus percentage is below its consensus "
            "percentage (fig4c), the contrast the Results draw; partially reproduced when the last two "
            "hold but a Kilosort2 value is outside tolerance.")

doc = {"schema_version": 2, "dataset": {"archive": "dandi", "id": "000034"},
       "paper": "doi:10.7554/elife.61834", "claims": claims}
out = yaml.safe_dump(doc, sort_keys=False, width=100, allow_unicode=True)
open("claims/000034/10.7554-elife.61834.yaml", "w").write(HEADER + out)
PYEOF
python $TMPDIR/build.py && python tools/claims_check.py claims/000034/10.7554-elife.61834.yaml paper/10.7554-elife.61834.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/build.py'
s=open(p).read()
old='''The paper's 2031 is not the sum of the counts it gives in Figure 1B (2021), so "
            "the total is read as (a) the sum of the six sorters' unit counts, or (b) that sum as the "
            "notebook's sorters gave it; the number of agreement units (components) is reported as well. "
            "Reproduced when the k = 6 and k >= 2 counts are within tolerance and the total is within "
            "tolerance under one reading.")'''
new='''The total is the sum of the six sorters' unit counts, the only reading the text "
            "allows (\\"total detected units\\"); the counts the paper gives in Figure 1B sum to 2021, not "
            "2031, which is within tolerance. The number of agreement units (components) is reported as "
            "well. Reproduced when the three values are within tolerance.")'''
assert old in s
open(p,'w').write(s.replace(old,new))
EOF
python $TMPDIR/build.py && python tools/claims_check.py claims/000034/10.7554-elife.61834.yaml paper/10.7554-elife.61834.txt; grep -n -c "—" claims/000034/*.yaml; grep -n -i "rather" claims/000034/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/000034/10.7554-elife.61834.yaml'));print(len(d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))"; grep -n -E "^\s+[a-z_]+: [^\"'].*: " claims/000034/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 95,140p claims/000034/10.7554-elife.61834.yaml; git status --short
```

```
criterion: Each of the six files named in the opening comment is present. The real Neuropixels recording
    has a sampling rate of 30 kHz and lasts 15 min (27,000,000 frames), with 246 channels (the paper)
    or 248 (the notebook); the simulated recording lasts 10 min and its ground truth has 250 units; the
    rat recording has 384 channels at 30 kHz; the Biocam recording has 1024 channels at about 23199 Hz.
    Reproduced when all hold under one of the two channel counts; partially reproduced when a file is
    missing or a property differs, naming which.
- id: fig1b-unit-counts
  statement: 'On the real Neuropixels recording the six sorters return very different numbers of units:
    Tridesclous the fewest (187) and SpyKING Circus the most (628); HerdingSpikes2 210, Kilosort2 446,
    IronClust 233 and HDSort 317.'
  source: Results, Spike sorters show low agreement for the same high-density dataset, paragraph 3; Figure
    1B
  quote: with Tridesclous (TDC) finding the least units (187) and SpyKING Circus (SC) finding the most
    units (628). HerdingSpikes2 finds 210 units; Kilosort2 finds 446 units; IronClust finds 233 units;
    and HDSort finds 317 units
  expected:
  - quantity: Tridesclous units
    value: 187
    tolerance: 18.7
    unit: units
[... 38 more lines not kept]
```

**Agent**

I wrote `claims/000034/10.7554-elife.61834.yaml`. The quote checker reports 24 claims, 24 quotes, 0 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (eLife 2020;9:e61834), full text from Europe PMC (PMC7704107): main text, figure and figure-supplement legends, Methods, decision letter and author response. The only supplement is the transparent reporting form, which says "The manuscript does not contain any statistical analysis".

**Code read.** The paper's notebooks in `SpikeInterface/spikeinterface.github.io`. The repository's latest commit is 657c6d8; the four notebooks last changed at ee08fb6 (2020-09-29), before publication. They cover Figures 1–4 and Figure 1 supplements 3 and 4. I also read the library defaults in spikecomparison 0.2.6 and spikesorters 0.3.3, the versions the notebooks ran. Two things the code settles:
- **Sorter parameters:** the notebooks pass a SpyKING Circus setting under the key `spyking_circus`, which never matches the sorter name `spykingcircus`. So every sorter ran on its defaults, as the Methods say.
- **True and false positives in Figure 3C:** the Methods do not define them for that figure; the notebook's rule is used.

**Claims.**
- 24 claims: 23 findings and one link claim (the dandiset holds the six files with the properties the paper and notebooks give).
- 24 quotes, no `inferred` notes.
- 0 statistics: the paper reports no tests.
- 24 criteria; 13 claims have expected values, each at 10% tolerance. The exception is counts under 5 (false positives found by two or more sorters, overmerged units), which get ±1 unit, with the reason given.

**Details left open, and the readings named:**
- **Total detected units (Fig 1C):** the paper says 2031, but its own per-sorter counts sum to 2021. Read as that sum, which is within tolerance.
- **Agreement-score histogram (Fig 1 supp 2):**
  - Which recording: the real one (where the Results cite it) or the simulated one (its legend and the author response).
  - Which scores: all matched-pair scores, or each agreement unit's average score.
- **"Similar disagreement" on the rat and retina recordings:** the Figure 1D measure (over 50% of units found by one sorter), or the Figure 1C measure (units found by all sorters at most 8% of detected units).
- **Precision/recall bias:** medians over all 250 ground-truth units, or over matched units only.
- **Accuracy versus SNR:** "low-SNR" read as below the median SNR, or below the mode. "Modulated" read as a Spearman correlation, since the paper reports no test.
- **"Higher scores" for Kilosort2:** accuracy alone, or each of accuracy, precision and recall. Judged on "most units"; "significantly" has no test behind it.
- **Kilosort2's own curation:** applied to the same run, or to a fresh run with `keep_good_only`.
- **Sorter subsets (Fig 3 supp 1):** removed units' nodes dropped and components recomputed, or the full components kept. Rates pooled over the sorters, or averaged per sorter.
- **Kilosort2 false-positive SNR (Fig 3 supp 2):**
  - Unmatched units: the Methods' false-positive class, or the Figure 3C rule.
  - "Many": more than half, or at least a quarter.
- **Curator agreement (Fig 4A):** the notebook's three-way Venn, or a pairwise comparison of the two curators.
- **"Average above 70%" (Fig 4C):** the mean of the two curators, or each curator separately.
- **Version variants:** spikeinterface 0.10.0 (paper) against 0.9.9 (notebooks); HDSort 1.0.1 against 1.0.2; 246 channels against the notebook file's 248.

**What claims needed but the paper lacks:**
- There is no PDF of the main text, so numbers drawn only in figures (Fig 1 supplements 3 and 4, Fig 3 supplement 1) could not be read.
- No code exists for Figure 3 supplements 1 and 2; those methods come from the legends.
- The sorter outputs are not said to be deposited, so the author must re-run all six sorters. That needs MATLAB and a GPU for Kilosort2. Sorters don't give the same output twice, and the curators worked on the paper's own Kilosort2 run, so a re-run won't match it exactly.

## End of run

37 turns, 8 minutes, result: success.
