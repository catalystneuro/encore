I've done steps 1 to 5 of the Author section and built the handover. 42 claims were tested and 3 are blocked. Most of the STRF claims did not reproduce, and most outcomes rest on assumptions about methods the paper leaves open. The final run passed `entry.py all` in 947 s with 0 errors, and its outputs were identical to the two earlier full runs.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cc-cohort-counts, vc-cohort-counts | reproduced (mouse counts cannot be checked) |
| fig1-psp-amplitude-kinetics, fig1d-ndr-distribution, fig1e-ndr-vs-rest-weak | reproduced, assumed |
| fig1c-resting-potential-range | reproduced |
| fig1fgh-trf-bandwidth-narrowing | partially reproduced |
| fig2-psp-histogram-modality | not reproduced, assumed |
| fig2-strf-significance-groups, fig2-psp-amplitude-ranges | not reproduced |
| supfig2 (both claims), supfig3 | blocked, data_missing |
| fig3d, fig3e | not reproduced, assumed |
| fig3f | reproduced, assumed |
| fig4c-btmf | reproduced, assumed (only under D11 reading (b)) |
| fig4d, fig4b | not reproduced |
| tab1-modulation-large-psp-like-spikes, fig5b, tab1-total-bandwidth, tab1-event-rate, fig5df, fig5e | reproduced, assumed |
| fig5a, fig5c, tab1-single-band, tab1-latency-duration, tab1-fsi, fig6b, fig6c, fig6bc, fig6d, fig6efg | not reproduced, assumed |
| fig7-unimodal, fig7c, fig7e, tab2-event-rate | partially reproduced, assumed |
| fig7d, fig7f, tab2-btmf, tab2-nonlinearity, tab2-fsi, tab2-latency-duration | not reproduced, assumed |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- All 66 tone, 40 DMR and 39 voltage-clamp recordings are present and paired as the paper says.
- The Supplementary folders hold one neuron each, so Supp. Figs. 2 and 3 cannot be tested.
- Two Supplementary recordings are byte-identical copies of main recordings (17726007, 17921007).
- There are no animal identifiers, so the 41 and 24 mouse counts can't be checked. The recordings fall on 39 and 22 dates.
- The data description says processed = raw minus smooth(raw, 1e5). This holds for only 16 of 84 DMR recordings; 67 differ over most samples and one at 39 samples. I detected events on the processed traces, since the description calls them the data used for the figures.
- Five excitatory recordings were held at -70 mV, not the "~-80 mV" the description gives.

**The paper's code:** the dataset ships the paper's Matlab code. It settles the event detector, the STRF estimator, the nonlinearity fit and the FSI. It uses analytic significance thresholds (p = 0.005, 0.01 and 0.001 in different scripts) where the Methods describe circular shuffles; I followed the Methods and showed the code's threshold as a variant. This is recorded as a code_mismatch finding.

**Main assumptions:**
- Very small events are those below 4 × the noise s.d. of event-free 50-ms segments during the DMR. Using the pre-stimulus s.d. instead removes nearly every PSP.
- Bimodality is judged from a smoothed amplitude histogram (two maxima with a trough).
- An STRF subfield counts as significant only if it passes a cluster test on the paper's shuffle null. This is my own addition: without it, chance pixels make nearly every STRF double-peaked.
- As a result, 15 neurons have STRFs for all three event types (the paper has 30). The Table 1 claims use those 15, with the 37 from the any-pixel reading shown as a variant. Several outcomes flip between the two groups (FSI, the nonlinearity correlations, two of the no-difference tests).
- Voltage-clamp events use the inverted current for excitation, at 20 pA selectivity (40 pA shown as a variant).
- The tone baseline s.d. is pooled over all pre-tone segments.

**Questions for the paper's authors** are recorded as a methods_unavailable finding. They ask about: the baseline segments behind the 4×/3× s.d. cuts, the bimodality test, how significant subfields and second peaks were told from chance pixels, how STRF bandwidth was measured, and the voltage-clamp event sign and selectivity.

**Questions to a reader:** none.

## 3. Protocol points

1. archives.md describes opening a CRCNS zip in place, but ac-5 is two `.tar.gz` files (6.3 GB and 1.5 GB) that can't be range-read. I streamed `data.tar.gz` once per run and reduced each file as it loaded; that pass takes 5 to 10 minutes.
2. The protocol doesn't say whether analysis code shipped inside the dataset counts as "code the paper links". The reader skipped it; I treated it as the paper's code, ranked after the Methods.
3. "Develop on a subset" and "do not download" don't say whether a development-only cache is allowed. I cached decoded arrays in `$TMPDIR` during development; the notebook streams everything.
4. The protocol doesn't say which selection dependent claims use when the selection claim itself fails. I used the main reading and showed the other group as a variant.
5. Some criteria have no partial clause, or one that doesn't fit the result (fig7e, tab2-event-rate). Where the effect holds but values miss, I graded partial using the protocol's general definition.
6. An expected value can be untestable (the mouse counts), and `measured` can't hold null. I left `measured` out of those two outcomes and explained in the notes.
7. A harness scratch folder, `entries/kim-2020/.claude/`, is inside the entry. My attempt to delete it was denied (no approval possible in this session), so it is still there and the workflow may need to drop it before committing.

## 4. Runtime and failures

- The notebook takes about 16 minutes (947 s).
- Including the session, the work took about 2 h 10 min, from 18:49 to 20:57 UTC.
- Nothing failed in the final runs. During development, one voltage-clamp amplitude sign bug was found and fixed.
- The record is `attempts/kim-2020-01.yaml` and the handover is in `executed/kim-2020/handover/`. Nothing is committed.
