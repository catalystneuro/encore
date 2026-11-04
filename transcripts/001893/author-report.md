I've done steps 1 to 6 for DANDI:001893 (version 0.260817.1647). The entry runs from a clean environment in about 6 minutes, `entry.py check` reports 0 errors, and the handover is built. Nothing is committed and nothing was verified by me.

## 1. Outcomes

| Claim | Outcome | Basis |
|---|---|---|
| patchseq-sample | reproduced | 96 cells and 28 mice; 27/8, 15/7 and 54/13 by group, all exact |
| patchseq-transcriptome-link (link I added) | reproduced | 64/64 libraries resolve at NeMO, MD5 sums match |
| patchseq-ne-identity | partially reproduced | Dbh found in 60 of 64 cells, all four markers in 58 of 64; 32 cells have no transcriptome |
| tau-table-link (link I added) | reproduced | 94% of cells within 10% of the paper's frozen table, r = 0.992 |
| AP waveform, spinal cord vs cortex | reproduced | p = 0.0002 (code variant 0.0097) |
| AP waveform, spinal cord vs cerebellum | reproduced | p = 0.041 (code variant 0.031) |
| tau, cortex vs spinal cord | partially reproduced | p = 0.0071 against the claimed p < 0.001 (frozen table 4e-5) |
| tau, cortex vs cerebellum | partially reproduced | p = 0.0025 (frozen table 3e-4) |
| 19 anatomy and in vivo claims | blocked, `data_missing` | data not in the dandiset |
| 4 snRNA-seq, retro-seq and MERFISH claims | blocked, `not_runnable` | see point 4 in section 3 |

## 2. Dataset findings
- **Wild-type cells:** 8 spinal-cord cells from 2 donors are wild type (genotype `wt/wt`, C57BL6J sample names). The Methods say Dbh-Cre;Ai65 mice. The waveform result depends on them: without them the code's p for spinal cord vs cortex goes from 0.0097 to 0.14, and spinal cord vs cerebellum is no longer significant (p = 0.19).
- **Sweep rule not applied by the paper:** the Methods' rule (bias current within ±100 pA) leaves 19 cells with no usable sweep. The paper's code applies no rule, and its frozen tau table has values for 17 of those 19 cells. This rule is what weakens the tau results.
- **Missing values:** 32 of 96 cells have no transcriptome. The frozen tau table lacks 14 cells without saying why.
- **Wrong NeMO pointer:** the collection the paper names (col-p9d5w39) holds no files. The FASTQ files are in col-s96tk9a.
- **Metadata errors:** the filter field reads "PLACEHOLDER" in all 96 files. One subject has no sex or age in participants.tsv. datasets.tsv gives dandiset 001858 the URL of 001748.

**Assumptions:** none recorded. The details the paper leaves open were each run under every reading and gave the same outcome: which sweeps give the input resistance for the bridge rule, which stimulus sets count as long squares, and where the noise windows sit. These are listed as deviations.

**Questions:** none for the paper's authors as `methods_unavailable`; the points above are recorded as findings. No reader was asked.

## 3. Protocol gaps
1. **Main reading versus variant.** When a criterion names a main reading (the Methods) and a code variant, the protocol does not say whether "reproduced under any reading" applies. I judged by the main reading, following reader step 2; that is why both tau claims are partial.
2. **Adding a link to an existing claim.** It is unclear whether adding a link claim to an existing claim's `depends_on` counts as changing that claim. I added `patchseq-transcriptome-link` to the identity claim's `depends_on`.
3. **`elsewhere` data found somewhere else.** The 4 sequencing claims name an empty collection, but processed counts exist elsewhere at NeMO. `data_missing` is not allowed for them, and no block reason fits "not attempted for lack of time before the deadline". I used `not_runnable` and said why.
4. **Unpinnable public data.** Code Ocean data assets have no DOI or fixed version. I treated them as unpinnable, so those claims are `data_missing`; I did not check whether they are readable without an account.
5. **Pinning outside files.** The FASTQ files are checked against MD5 sums fetched from NeMO at run time, not against a stored list.
6. **Clock check.** The protocol's suggested check (decoding around trial starts) doesn't fit patch-clamp data. I used stimulus amplitude against the voltage change, with a window shifted earlier as the control.
7. **Identity counting.** No aligner was set up, so marker reads were counted by exact 31-mer matching instead of the paper's STAR alignment. This is recorded as a deviation.

## 4. Runtime and failures
About 1 h 25 min (06:29 to 07:52 UTC); notebook 6.1 min. Nothing failed. One Ensembl REST request timed out, so gene sequences come from the UCSC API instead.

Files are in `entries/001893-su-2026/`:
- reproduce_su_2026.ipynb
- lcne.py
- rna.py

The record is `attempts/001893-su-2026-01.yaml`.
