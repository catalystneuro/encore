I've done steps 1 to 6 for dandiset 001075 (Randi et al. 2023): the entry ran clean, `check` reports 0 errors, and the handover package is built in `executed/001075-randi-2023/handover/`. Nothing is committed. I used the paper's full text, which is open access (PMC10632145, CC BY), together with its Source Data files; all of it is saved under `paper/`. I pinned version 0.240930.1859. It is the most recent, and it is the only one with `target_pumpprobe_id`, the column that says which neuron was stimulated in a manually targeted stimulation. The notebook header shows how the two versions differ.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| recordings-protocol (113 animals, up to 40 min, stimulus every 30 s) | dandiset | partially reproduced: traces exist for only 110 of 113 animals |
| pairs-measured (23,433 pairs / 186 neurons / at most 59 observations) | dandiset | partially reproduced: 20,587 / 184 / 50 |
| fig1e AVJR→AVDR | dandiset | reproduced |
| fig1f AVER→AVAR | dandiset | reproduced, but only 7 trials |
| fig1g SAADL→OLLR | dandiset | reproduced, but only 5 trials, and the sign flips under the paper code's correction |
| edfig2ij neighbours mostly don't respond | dandiset | reproduced: 74.1% below 0.1, against 75% |
| sourcedata-link (per-pair counts and means vs the paper's Source Data) | with inputs | partially reproduced: 81.7% of pairs found, ρ = 0.77, r = 0.55 |
| fig2d 11% inhibitory | with inputs | not reproduced: 15.1% here; the paper's own per-pair means give 11.5% |
| osf-link (recordings and stimulated neurons vs the paper's OSF export) | with labels | reproduced: same stimulated neuron in 87.4% of stimulations |
| fig2c-1310, fig2c-bilateral, fig2efg path length, fig3 model, edfig7b, fig5 screen | dandiset | blocked: data missing |
| edfig6 kernels | dandiset | blocked: not runnable |
| fig4-rid-wt | dandiset | blocked: metadata insufficient |
| fig4-rid-unc31 | elsewhere | blocked: metadata insufficient |
| fig6 spontaneous activity | elsewhere | blocked: not runnable |

## 2. What I found about the dandiset

- **Missing subjects:** 3 of the 113 subjects (20, 23, 33) have only the raw imaging file, with no traces or stimulation table.
- **Missing recordings:** the unc-31 recordings, the Fig. 6 spontaneous recordings and the unstimulated control recordings are not in the dandiset. Every q value needs the controls, and they are not public anywhere: the paper's code reads them from private lab paths, and they are not on OSF.
- **Stimulated neuron not identified:** for about half the stimulations the files give only a target position, not the stimulated neuron. Picking the nearest neuron to the target matches the paper's choice in 66% of these. The paper also excluded 950 stimulations, and the dandiset does not mark which ones.
- **Wrong labels:** in subjects 64, 76, 77, 86 and 91, every neuron's label reached through the files' NeuroPAL link names a different neuron than the paper's exported labels. In subject 11 the neuron count differs from the export.
- **Metadata errors:**
  - `depth_in_um` holds values from −0.875 to 0.875, which cannot be micrometres.
  - Stimulus duration and power are constants copied from the paper.
  - The red channel's indicator is listed as GCaMP6s.
  - Two subjects have strain "none", and every animal's age is P1D.
  - `neuropal_ids` contains text such as "merge", and some neurons are labelled "target".
  - One label confidence is 11.
  - Nine recordings contain intensities down to −196,646.
  - The traces have unit "n.a." and their processing is not described.

## 3. Where the protocol was unclear, wrong or missing something

1. It does not say how to treat the paper's own published results, such as per-pair q values and means in its Source Data. I used them as `with_inputs`: reference values for a link claim, and the q < 0.05 selection for fig2d, with the response signs computed from the dandiset.
2. Some claims need data that is on OSF (elsewhere) and also data that is public nowhere. The rule "elsewhere is never data_missing" doesn't fit them. I classified each claim by the missing piece: the unc-31 q-value claims stay `data: dandiset` and are blocked as data missing; fig6 is `elsewhere` and blocked as not runnable.
3. There is no guidance for an identifier that is absent but can be inferred from the dandiset itself (the stimulated neuron, from the target position). I inferred it from the dandiset alone and tested the inference in its own claim (osf-link) against the paper's export.
4. The list of 188 head neurons from the paper's code is a definition, not labels or measurements. I kept those claims as `data: dandiset` and listed the code under `inputs`.
5. The Extended Data Fig. 2j "75%" does not say which neighbours it refers to, and the number is only resolvable from the Source Data. I listed three readings, and the pooled one matches.
6. The default 10% tolerance is meaningless for a count of 113 animals. I set the tolerance to 0 and wrote an explicit rule for partial.
7. Two block reasons rest on checks I ran outside the notebook: listing the OSF comment files, and trying to install the paper's code. I stated what I looked at without giving any numbers from those checks.
8. The two published versions list the same 223 files, but every file was re-uploaded. I showed the difference as a list of changed fields in one file.
9. For the clock check I used how often the stimulated neuron responds at the true stimulation times against times shifted by 15 s (55% against 10%). The protocol suggests decoding instead.
10. The protocol says nothing about outside services that rate-limit. OSF returned HTTP 429 when I fetched its files one at a time, so I stream a single tarball and check its md5. The OSF project is not versioned as a whole, so I pinned the file's version and md5.

## 4. Runtime and failures

- **Runtime:** the notebook takes 404 s in the clean environment; the whole `entry.py all` step took 6 min 54 s. It processes 110 recordings in 4 worker processes and streams a 523 MB file from OSF.
- **Paper's code would not install:** pumpprobe fails at build time (its build does not find the numpy headers, and its dependency mistofrutta needs gitpython to build). This is why the kernel and Fig. 6 claims are blocked as not runnable.
- **OSF rate limit:** fetching OSF files one by one failed with HTTP 429 even with backoff. Switching to the single tarball fixed it.
- **Errors fixed while developing:** some `neuropal_ids` are not numbers, and the photobleaching fit failed on traces with too few points. With fits that converge slowly, the first full run took about 14 minutes; I added an analytic Jacobian and a cap on evaluations, and the full run now takes 404 s. All of these are fixed, and the final executed outputs match the conclusions.
